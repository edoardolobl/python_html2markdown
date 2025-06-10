"""
This script scrapes documentation from a given base URL, converts the HTML content to Markdown, and saves it to local files.
It supports various HTML to Markdown conversion methods and allows for filtering URLs based on include/exclude patterns.
"""

import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import os
import time
import logging
import argparse
from collections import deque
import re

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global flags for library availability (will be updated based on imports)
TIKTOKEN_AVAILABLE = False
DOCLING_AVAILABLE = False
MARKDOWNIFY_AVAILABLE = False
HTML_TO_MARKDOWN_AVAILABLE = False
PYHTML2MD_AVAILABLE = False

# Attempt to import tiktoken for token estimation
try:
    import tiktoken

    TIKTOKEN_AVAILABLE = True
    tiktoken.get_encoding("o200k_base")
    logging.info("`tiktoken` library found and 'o200k_base' encoding is available. Using for token estimation.")
except ImportError:
    logging.warning("`tiktoken` library not found. Falling back to word count for token estimation.")
except Exception as e:
    logging.warning(f"Failed to initialize `tiktoken` with 'o200k_base' encoding: {e}. Falling back to word count.")

# Attempt to import Docling for advanced conversion
try:
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import InputFormat  # noqa: F401

    DOCLING_AVAILABLE = True
    logging.info("Docling library found. Advanced conversion is available.")
except ImportError:
    logging.warning("Docling library not found. Will use standard Markdown conversion.")

# Attempt to import Markdownify
try:
    from markdownify import markdownify as md, MarkdownConverter as MarkdownifyConverterClass  # noqa: F401

    MARKDOWNIFY_AVAILABLE = True
    logging.info("Markdownify library found. Markdownify conversion is available.")
except ImportError:
    logging.warning("Markdownify library not found. Markdownify conversion will be skipped.")

# Attempt to import html_to_markdown
try:
    from html_to_markdown import convert_to_markdown

    HTML_TO_MARKDOWN_AVAILABLE = True
    logging.info("html_to_markdown library found. Standard fallback conversion is available.")
except ImportError:
    logging.error(
        "html_to_markdown library not found. This is a critical fallback. Plain text extraction will be the only option if other converters fail.")

# Attempt to import pyhtml2md
try:
    import pyhtml2md

    PYHTML2MD_AVAILABLE = True
    logging.info("pyhtml2md library found. pyhtml2md conversion is available.")
except ImportError:
    logging.warning("pyhtml2md library not found. pyhtml2md conversion will be skipped.")


def estimate_tokens(text: str) -> tuple[int, str]:
    """
    Estimates the number of tokens in a given text string.
    Prioritizes `tiktoken` if available, otherwise falls back to word count.

    Args:
        text (str): The input text string.

    Returns:
        tuple[int, str]: A tuple containing the estimated token count and the method used.
    """
    if not text:
        return 0, "word count"

    if TIKTOKEN_AVAILABLE:
        try:
            encoding = tiktoken.get_encoding("o200k_base")
            num_tokens = len(encoding.encode(text))
            method = "tiktoken (o200k_base)"
            logging.debug("Token estimation using tiktoken (o200k_base).")
            return num_tokens, method
        except Exception as e:
            logging.warning(f"Error using tiktoken: {e}. Falling back to word count.")

    num_tokens = len(text.split())
    method = "word count"
    logging.debug("Token estimation using word count.")
    return num_tokens, method


def get_code_language_from_class(el: BeautifulSoup) -> str | None:
    """
    Extracts the code language from a BeautifulSoup element's class attribute.
    Looks for classes starting with 'language-' or 'lang-'.

    Args:
        el (BeautifulSoup): The BeautifulSoup element to inspect.

    Returns:
        str | None: The extracted language string in lowercase, or None if not found.
    """
    if not el:
        return None
    classes = el.get("class", [])
    for cls in classes:
        if cls.startswith("language-"):
            return cls.split("language-", 1)[1].lower()
        if cls.startswith("lang-"):
            return cls.split("lang-", 1)[1].lower()
    return None


class DocumentationConverter:
    """
    A class to scrape web documentation, preprocess HTML, convert it to Markdown,
    and save the results.
    """

    def __init__(self, config: argparse.Namespace):
        """
        Initializes the DocumentationConverter with the given configuration.

        Args:
            config (argparse.Namespace): An object containing configuration parameters
                                         from command-line arguments.
        Raises:
            ValueError: If the base URL is not a valid HTTP/HTTPS URL.
        """
        if not config.base_url.startswith(("http://", "https://")):
            raise ValueError("Base URL must be a valid HTTP/HTTPS URL.")
        self.base_url: str = config.base_url
        self.output_dir: str = config.output_dir
        self.max_depth: int = config.max_depth
        self.max_pages: int = config.max_pages
        self.conversion_method: str = config.conversion_method
        self.concatenate_output: bool = config.concatenate_output
        self.log_level = config.log_level
        self.main_content_selector = config.main_content_selector
        self.include_patterns = [re.compile(p) for p in config.include_patterns] \
            if config.include_patterns else []
        self.exclude_patterns = [re.compile(p) for p in config.exclude_patterns] \
            if config.exclude_patterns else []

        logging.getLogger().setLevel(self.log_level)

        self.visited_urls: set[str] = set()
        self.docling_converter: DocumentConverter | None = None

        if self.conversion_method == "docling" and DOCLING_AVAILABLE:
            try:
                self.docling_converter = DocumentConverter()
                logging.info("Docling converter initialized successfully.")
            except Exception as e:
                logging.warning(f"Docling initialization failed: {e}. Docling will be disabled.")
                self.conversion_method = "auto"  # Fallback
        elif self.conversion_method == "docling" and not DOCLING_AVAILABLE:
            logging.warning("Docling was selected but is not available. Falling back to auto-selection.")
            self.conversion_method = "auto"

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logging.info(f"Created output directory: {self.output_dir}")

    def _should_scrape(self, url: str) -> bool:
        """
        Determines if a given URL should be scraped based on include/exclude patterns.

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if the URL should be scraped, False otherwise.
        """
        if self.include_patterns:
            if not any(pattern.search(url) for pattern in self.include_patterns):
                logging.debug(f"Skipping {url}: Does not match any include patterns.")
                return False
        if self.exclude_patterns:
            if any(pattern.search(url) for pattern in self.exclude_patterns):
                logging.debug(f"Skipping {url}: Matches an exclude pattern.")
                return False
        return True

    def discover_links_bfs(self) -> list[str]:
        """
        Discovers links within the base URL using a Breadth-First Search (BFS) algorithm.
        Respects max_depth, max_pages, and include/exclude URL patterns.

        Returns:
            list[str]: A list of unique URLs to be scraped.
        """
        queue = deque([(self.base_url, 0)])  # (url, depth)
        all_links = []
        pages_processed = 0

        while queue and pages_processed < self.max_pages:
            current_url, current_depth = queue.popleft()

            if current_url in self.visited_urls or current_depth >= self.max_depth:
                continue

            if not self._should_scrape(current_url):
                continue

            self.visited_urls.add(current_url)
            all_links.append(current_url)
            pages_processed += 1
            logging.info(
                f"Processing URL (Depth: {current_depth}, Pages: {pages_processed}/{self.max_pages}): {current_url}")

            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
                response = requests.get(current_url, timeout=10, headers=headers)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")

                for link in soup.find_all("a", href=True):
                    href = link["href"]
                    full_url = urljoin(current_url, href)

                    parsed_full_url = urlparse(full_url)
                    parsed_base_url = urlparse(self.base_url)

                    # Ensure the link is within the same domain and not already visited
                    # Also skip anchor links and mailto links
                    if (parsed_full_url.netloc == parsed_base_url.netloc and
                            full_url not in self.visited_urls and
                            not href.startswith("#") and
                            not href.startswith("mailto:")):
                        queue.append((full_url, current_depth + 1))
                time.sleep(0.5)  # Be polite to the server

            except requests.exceptions.RequestException as e:
                logging.error(f"Request error while discovering links from {current_url}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error discovering links from {current_url}: {e}")
        return all_links

    def preprocess_html(self, html_content: str) -> BeautifulSoup:
        """
        Preprocesses the raw HTML content by removing unwanted tags and attributes,
        and optionally extracting the main content area.

        Args:
            html_content (str): The raw HTML content as a string.

        Returns:
            BeautifulSoup: A BeautifulSoup object containing the preprocessed HTML.
        """
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove unwanted tags that typically don't contribute to main content
        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form", "iframe"]):
            tag.decompose()

        # Extract main content if a CSS selector is provided
        if self.main_content_selector:
            main_content = soup.select_one(self.main_content_selector)
            if main_content:
                # Create a new soup with only the main content to isolate it
                new_soup = BeautifulSoup("", "html.parser")
                new_soup.append(main_content)
                soup = new_soup
            else:
                logging.warning(
                    f"Main content selector '{self.main_content_selector}' not found. Processing entire page.")

        # Strip unnecessary attributes to clean up HTML before conversion
        for tag in soup.find_all(True):
            if "class" in tag.attrs: del tag.attrs["class"]
            if "id" in tag.attrs: del tag.attrs["id"]
            if "style" in tag.attrs: del tag.attrs["style"]
            # Add more attributes to remove as needed, e.g., 'data-*'

        # Normalize relative URLs to absolute URLs for consistency
        for attr in ["href", "src"]:
            for tag in soup.find_all(attrs={attr: True}):
                if not urlparse(tag[attr]).netloc:  # Check if it's a relative URL
                    tag[attr] = urljoin(self.base_url, tag[attr])

        return soup

    def convert_html_to_markdown(self, html_content: str, url: str) -> str | None:
        """
        Converts HTML content to Markdown using the specified or auto-selected method.

        Args:
            html_content (str): The HTML content to convert.
            url (str): The URL of the page being converted (for logging purposes).

        Returns:
            str | None: The Markdown content, or None if all conversions fail.
        """
        markdown_content = None
        conversion_attempted = []

        # Prioritize user's preferred method
        if self.conversion_method == "docling" and DOCLING_AVAILABLE:
            conversion_attempted.append("Docling")
            logging.info(f"Attempting Docling conversion for {url}")
            markdown_content = self._convert_with_docling(html_content)
            if markdown_content: return markdown_content

        if self.conversion_method == "markdownify" and MARKDOWNIFY_AVAILABLE:
            conversion_attempted.append("Markdownify")
            logging.info(f"Attempting Markdownify conversion for {url}")
            markdown_content = self._convert_with_markdownify(html_content)
            if markdown_content: return markdown_content

        if self.conversion_method == "pyhtml2md" and PYHTML2MD_AVAILABLE:
            conversion_attempted.append("pyhtml2md")
            logging.info(f"Attempting pyhtml2md conversion for {url}")
            markdown_content = self._convert_with_pyhtml2md(html_content)
            if markdown_content: return markdown_content

        if self.conversion_method == "html2text" and HTML_TO_MARKDOWN_AVAILABLE:
            conversion_attempted.append("html_to_markdown")
            logging.info(f"Attempting html_to_markdown conversion for {url}")
            markdown_content = self._convert_with_html_to_markdown(html_content)
            if markdown_content: return markdown_content

        # Auto-selection fallback if preferred method failed or was 'auto'
        if self.conversion_method == "auto" or not conversion_attempted:
            if DOCLING_AVAILABLE and "Docling" not in conversion_attempted:
                conversion_attempted.append("Docling (auto)")
                logging.info(f"Attempting Docling conversion (auto) for {url}")
                markdown_content = self._convert_with_docling(html_content)
                if markdown_content: return markdown_content

            if MARKDOWNIFY_AVAILABLE and "Markdownify" not in conversion_attempted:
                conversion_attempted.append("Markdownify (auto)")
                logging.info(f"Attempting Markdownify conversion (auto) for {url}")
                markdown_content = self._convert_with_markdownify(html_content)
                if markdown_content: return markdown_content

            if PYHTML2MD_AVAILABLE and "pyhtml2md" not in conversion_attempted:
                conversion_attempted.append("pyhtml2md (auto)")
                logging.info(f"Attempting pyhtml2md conversion (auto) for {url}")
                markdown_content = self._convert_with_pyhtml2md(html_content)
                if markdown_content: return markdown_content

            if HTML_TO_MARKDOWN_AVAILABLE and "html_to_markdown" not in conversion_attempted:
                conversion_attempted.append("html_to_markdown (auto)")
                logging.info(f"Attempting html_to_markdown conversion (auto) for {url}")
                markdown_content = self._convert_with_html_to_markdown(html_content)
                if markdown_content: return markdown_content

        # Ultimate fallback: plain text extraction if all converters fail
        conversion_attempted.append("Plain Text Extraction")
        logging.warning(f"All HTML to Markdown converters failed for {url}. Falling back to plain text extraction.")
        markdown_content = self._extract_plain_text_from_html(html_content)

        if not markdown_content:
            logging.error(f"Failed to extract any content from {url} after all attempts.")

        return markdown_content

    def _convert_with_docling(self, html_content: str) -> str | None:
        """
        Converts HTML content to Markdown using the Docling library.
        Note: Docling currently requires a temporary file for conversion.

        Args:
            html_content (str): The HTML content to convert.

        Returns:
            str | None: The Markdown content, or None if conversion fails.
        """
        if not self.docling_converter:
            return None
        temp_html_path = os.path.join(self.output_dir, "temp_doc.html")
        try:
            with open(temp_html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            result = self.docling_converter.convert(temp_html_path)
            markdown = result.document.export_to_markdown()
            logging.info("Docling conversion succeeded.")
            return markdown
        except Exception as e:
            logging.warning(f"Docling conversion failed: {e}")
            return None
        finally:
            if os.path.exists(temp_html_path):
                os.remove(temp_html_path)

    def _convert_with_markdownify(self, html_content: str) -> str | None:
        """
        Converts HTML content to Markdown using the Markdownify library.

        Args:
            html_content (str): The HTML content to convert.

        Returns:
            str | None: The Markdown content, or None if conversion fails.
        """
        if not MARKDOWNIFY_AVAILABLE:
            return None
        try:
            markdown = md(
                html_content,
                heading_style="ATX",
                bullets="*",
                code_language=get_code_language_from_class,
                # strip=["a"], # Example: strip links, adjust as needed
                # add more options as needed
            )
            logging.info("Markdownify conversion succeeded.")
            return markdown
        except Exception as e:
            logging.warning(f"Markdownify conversion failed: {e}")
            return None

    def _convert_with_html_to_markdown(self, html_content: str) -> str | None:
        """
        Converts HTML content to Markdown using the html-to-markdown library.

        Args:
            html_content (str): The HTML content to convert.

        Returns:
            str | None: The Markdown content, or None if conversion fails.
        """
        if not HTML_TO_MARKDOWN_AVAILABLE:
            return None
        try:
            markdown = convert_to_markdown(html_content)
            logging.info("html_to_markdown conversion succeeded.")
            return markdown
        except Exception as e:
            logging.warning(f"html_to_markdown conversion failed: {e}")
            return None

    def _convert_with_pyhtml2md(self, html_content: str) -> str | None:
        """
        Converts HTML content to Markdown using the pyhtml2md library.

        Args:
            html_content (str): The HTML content to convert.

        Returns:
            str | None: The Markdown content, or None if conversion fails.
        """
        if not PYHTML2MD_AVAILABLE:
            return None
        try:
            markdown = pyhtml2md.convert(html_content)
            logging.info("pyhtml2md conversion succeeded.")
            return markdown
        except Exception as e:
            logging.warning(f"pyhtml2md conversion failed: {e}")
            return None

    def _extract_plain_text_from_html(self, html_content: str) -> str:
        """
        Extracts plain text from HTML content as a fallback when other converters fail.

        Args:
            html_content (str): The HTML content to extract text from.

        Returns:
            str: The extracted plain text.
        """
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text(separator="\n")

    def scrape_and_save(self):
        """
        Orchestrates the scraping, conversion, and saving process.
        Discovers links, fetches HTML, preprocesses, converts, and saves Markdown files.
        """
        all_urls = self.discover_links_bfs()
        output_files = []
        failed_urls = []

        for i, url in enumerate(all_urls):
            logging.info(f"Scraping and converting page {i + 1}/{len(all_urls)}: {url}")
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
                response = requests.get(url, timeout=10, headers=headers)
                response.raise_for_status()
                html_content = response.text

                # Preprocess HTML content
                preprocessed_soup = self.preprocess_html(html_content)
                cleaned_html_content = str(preprocessed_soup)

                markdown_content = self.convert_html_to_markdown(cleaned_html_content, url)

                if markdown_content:
                    # Sanitize URL to create a valid filename
                    parsed_url = urlparse(url)
                    path = parsed_url.path.strip("/")
                    if path:
                        # Replace non-alphanumeric characters with underscores
                        filename_base = re.sub(r"[^a-zA-Z0-9_.-]", "_", path)
                    else:
                        # Use netloc if path is empty (e.g., for base URL)
                        filename_base = re.sub(r"[^a-zA-Z0-9_.-]", "_", parsed_url.netloc)

                    # Ensure filename is not empty after sanitization
                    if not filename_base: filename_base = "index"

                    output_filename = os.path.join(self.output_dir, f"{filename_base}.md")

                    # Ensure unique filename if it already exists (e.g., for different query params
                    # that result in the same sanitized base name)
                    counter = 1
                    while os.path.exists(output_filename):
                        output_filename = os.path.join(self.output_dir, f"{filename_base}_{counter}.md")
                        counter += 1

                    with open(output_filename, 'w', encoding='utf-8') as f:
                        f.write(f"# {url}\n\n")  # Add URL as a heading for context
                        f.write(markdown_content)
                    output_files.append(output_filename)
                    logging.info(f"Successfully converted and saved: {output_filename}")
                else:
                    logging.warning(f"No markdown content generated for {url}")
                    failed_urls.append((url, "No markdown content"))

            except requests.exceptions.RequestException as e:
                logging.error(f"Failed to fetch {url}: {e}")
                failed_urls.append((url, f"Fetch error: {e}"))
            except Exception as e:
                logging.error(f"Error processing {url}: {e}")
                failed_urls.append((url, f"Processing error: {e}"))

        if self.concatenate_output and output_files:
            concatenated_filepath = os.path.join(self.output_dir, "all_documentation.md")
            with open(concatenated_filepath, 'w', encoding='utf-8') as outfile:
                for fname in output_files:
                    with open(fname, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write("\n\n---\n\n")  # Separator between documents
            logging.info(f"All individual markdown files concatenated into: {concatenated_filepath}")

        if failed_urls:
            logging.warning("--- Failed URLs ---")
            for url, reason in failed_urls:
                logging.warning(f"URL: {url}, Reason: {reason}")


def main():
    """
    Main function to parse command-line arguments and initiate the scraping process.
    """
    parser = argparse.ArgumentParser(description="Scrape documentation from a website and convert to Markdown.")
    parser.add_argument("base_url", type=str, help="The base URL of the documentation site to scrape.")
    parser.add_argument("--output_dir", type=str, default="./output",
                        help="Directory to save the Markdown files. Defaults to ./output.")
    parser.add_argument("--max_depth", type=int, default=3,
                        help="Maximum depth for link discovery. Defaults to 3.")
    parser.add_argument("--max_pages", type=int, default=50,
                        help="Maximum number of unique pages to scrape. Defaults to 50.")
    parser.add_argument("--conversion_method", type=str, default="auto",
                        choices=["auto", "docling", "markdownify", "html2text", "pyhtml2md"],
                        help="Preferred HTML to Markdown conversion method. Defaults to 'auto'.")
    parser.add_argument("--concatenate_output", action="store_true",
                        help="Concatenate all individual Markdown files into a single file.")
    parser.add_argument("--log_level", type=str, default="INFO",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Set the logging level. Defaults to INFO.")
    parser.add_argument("--main_content_selector", type=str, default=None,
                        help="CSS selector to identify the main content area of a page.")
    parser.add_argument("--include_patterns", nargs='*',
                        help="List of regex patterns for URLs to include. If provided, only URLs matching any of these patterns will be scraped.")
    parser.add_argument("--exclude_patterns", nargs='*',
                        help="List of regex patterns for URLs to exclude. URLs matching any of these patterns will be skipped.")

    args = parser.parse_args()

    converter = DocumentationConverter(args)
    converter.scrape_and_save()


if __name__ == "__main__":
    main()


