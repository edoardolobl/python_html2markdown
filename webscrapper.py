import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import os
import time
import logging

# Setup logging to track which conversion algorithm is used and general events.
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (e.g., INFO, DEBUG, WARNING)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Define message format
)

# Attempt to import tiktoken for accurate token counting.
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
    # Attempt to get the encoding to ensure it's valid and catch errors early if needed
    tiktoken.get_encoding("o200k_base") 
    logging.info("`tiktoken` library found and 'o200k_base' encoding is available. Using for token estimation.")
except ImportError:
    TIKTOKEN_AVAILABLE = False
    logging.warning("`tiktoken` library not found. Falling back to word count for token estimation.")
except Exception as e: # Catch other potential errors from tiktoken like invalid encoding
    TIKTOKEN_AVAILABLE = False
    logging.warning(f"Failed to initialize `tiktoken` with 'o200k_base' encoding: {e}. Falling back to word count.")

# Attempt to import Docling for advanced HTML to Markdown conversion.
try:
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import InputFormat  # Required by DocumentConverter
    DOCLING_AVAILABLE = True
    logging.info("Docling library found. Advanced conversion is available.")
except ImportError:
    DOCLING_AVAILABLE = False
    logging.warning(
        "Docling library not found. Will use standard Markdown conversion. "
        "For advanced conversion, please install 'docling'."
    )

# Attempt to import Markdownify for an alternative HTML to Markdown conversion.
try:
    from markdownify import markdownify as md, MarkdownConverter as MarkdownifyConverterClass
    MARKDOWNIFY_AVAILABLE = True
    logging.info("Markdownify library found. Markdownify conversion is available.")
except ImportError:
    MARKDOWNIFY_AVAILABLE = False
    logging.warning(
        "Markdownify library not found. Markdownify conversion will be skipped. "
        "Consider installing 'markdownify' for this option."
    )

# Import html_to_markdown for fallback conversion (html2text equivalent).
# This is the primary fallback if other methods are unavailable or fail.
try:
    from html_to_markdown import convert_to_markdown
    HTML_TO_MARKDOWN_AVAILABLE = True
    logging.info("html_to_markdown library found. Standard fallback conversion is available.")
except ImportError:
    HTML_TO_MARKDOWN_AVAILABLE = False
    logging.error(
        "html_to_markdown library not found. This is a critical fallback. "
        "Plain text extraction will be the only option if other converters fail."
        "Please install 'html_to_markdown'."
    )


def estimate_tokens(text: str) -> tuple[int, str]:
    """
    Estimates the number of tokens in a given text.

    It attempts to use the `tiktoken` library with the "o200k_base"
    encoding for an accurate count. If `tiktoken` is unavailable or fails,
    it falls back to a simple word count (splitting by whitespace).

    Args:
        text: The input string for which to estimate tokens.

    Returns:
        A tuple containing:
            - token_count (int): The estimated number of tokens.
            - method_used (str): A string indicating the method used for
                                 estimation ("tiktoken (o200k_base)" or "word count").
    """
    if not text:
        return 0, "word count" # Or "N/A" if text is empty

    global TIKTOKEN_AVAILABLE # Ensure we are using the global flag defined at the top
    
    if TIKTOKEN_AVAILABLE:
        try:
            # The 'o200k_base' encoding is suitable for models like gpt-4o, gpt-4-turbo
            encoding = tiktoken.get_encoding("o200k_base")
            num_tokens = len(encoding.encode(text))
            method = "tiktoken (o200k_base)"
            logging.info("Token estimation using tiktoken (o200k_base).")
            return num_tokens, method
        except Exception as e:
            logging.warning(f"Error using tiktoken: {e}. Falling back to word count.")
            # Fall through to word count method by setting TIKTOKEN_AVAILABLE to False for this call
            # This is not ideal as it modifies a global for a local issue.
            # Better: just proceed to the fallback block directly.
            # TIKTOKEN_AVAILABLE = False # Avoid this side-effect
    
    # Fallback to word count
    num_tokens = len(text.split())
    method = "word count"
    # No need to log here again if tiktoken failed, as the warning above is sufficient.
    # Only log if tiktoken was not available from the start.
    if not TIKTOKEN_AVAILABLE: # This condition is a bit tricky now due to the above.
                               # Let's assume initial TIKTOKEN_AVAILABLE was False.
        logging.info("Token estimation using word count (tiktoken was not available or failed).")
    elif TIKTOKEN_AVAILABLE and not method == "tiktoken (o200k_base)": 
        # This means TIKTOKEN_AVAILABLE was true, but it failed, and now we are in fallback.
        # The warning "Error using tiktoken..." already covered this.
        pass

    return num_tokens, method


def get_code_language_from_class(el: BeautifulSoup) -> str | None:
    """
    Extracts the programming language from an HTML element's class attribute.

    This function is typically used as a callback for the Markdownify library
    to correctly format code blocks by identifying their language. It checks
    for class names starting with 'language-' or 'lang-'.

    Args:
        el: A BeautifulSoup element (e.g., a <pre> or <code> tag).

    Returns:
        The detected language string (e.g., 'python', 'javascript')
        in lowercase, or None if no language class is found.
    """
    if not el:
        return None
    classes = el.get('class', [])
    for cls in classes:
        if cls.startswith('language-'):
            return cls.split('language-', 1)[1].lower()
        if cls.startswith('lang-'):
            return cls.split('lang-', 1)[1].lower()
        # Consider adding more common direct language classes if observed, e.g.:
        # if cls in ['python', 'javascript', 'java', 'csharp']:
        #     return cls.lower()
    return None


class DocumentationConverter:
    """
    A class to scrape and convert documentation websites into Markdown.

    This class handles the process of fetching web pages starting from a
    base URL, discovering relevant documentation links within the same domain,
    converting the HTML content of these pages to Markdown using various
    conversion strategies, and finally compiling all converted content into
    a single Markdown file.

    It prioritizes conversion methods in the following order:
    1. Docling (if available and enabled)
    2. Markdownify (if available)
    3. html_to_markdown (html2text equivalent)
    4. Plain text extraction from HTML (ultimate fallback)

    Attributes:
        base_url (str): The starting URL for scraping documentation.
        visited_urls (set): A set to keep track of URLs already processed.
        use_docling (bool): User's preference to use Docling (if available).
        docling_available (bool): Flag indicating if Docling library is installed.
        markdownify_available (bool): Flag indicating if Markdownify library is installed.
        html_to_markdown_available (bool): Flag indicating if html_to_markdown library is installed.
        preferred_converter (str): The user's preferred primary conversion method.
        converter (DocumentConverter, optional): An instance of Docling's DocumentConverter.
    """

    def __init__(self, base_url: str, use_docling: bool = True, preferred_converter: str = "docling"):
        """
        Initializes the DocumentationConverter.

        Args:
            base_url: The base URL of the documentation site to scrape.
                      Must be a valid HTTP/HTTPS URL.
            use_docling: Whether to attempt using Docling if it's available.
                         Defaults to True. This acts as an explicit override.
            preferred_converter: The user's preferred primary HTML-to-Markdown
                                 converter. Accepts 'docling', 'markdownify',
                                 or 'html2text'. Defaults to 'docling'.
        """
        if not base_url.startswith(("http://", "https://")):
            raise ValueError("Base URL must be a valid HTTP/HTTPS URL.")
        self.base_url: str = base_url
        self.visited_urls: set[str] = set()

        # Initialize flags for library availability from global scope
        self.docling_available: bool = DOCLING_AVAILABLE
        self.markdownify_available: bool = MARKDOWNIFY_AVAILABLE
        self.html_to_markdown_available: bool = HTML_TO_MARKDOWN_AVAILABLE

        # User's preference for using Docling (can be True even if Docling is not available)
        self.use_docling_preference: bool = use_docling
        # Effective use_docling flag: True only if user wants AND it's available
        self.use_docling: bool = use_docling and self.docling_available

        # Store preferred converter
        if preferred_converter not in ["docling", "markdownify", "html2text"]:
            logging.warning(
                f"Invalid preferred_converter '{preferred_converter}'. "
                "Defaulting to 'docling'. Valid options are 'docling', 'markdownify', 'html2text'."
            )
            self.preferred_converter: str = "docling"
        else:
            self.preferred_converter: str = preferred_converter
        logging.info(f"User preferred converter set to: {self.preferred_converter}")


        self.converter: DocumentConverter | None = None  # For Docling
        # Initialize Docling converter only if it's going to be effectively used
        if self.use_docling: # This implies self.docling_available is True
            try:
                self.converter = DocumentConverter()
                logging.info("Docling converter initialized successfully.")
            except Exception as e:
                logging.warning(
                    f"Docling initialization failed: {e}. Docling will be disabled."
                )
                self.use_docling = False  # Disable if initialization fails

    def get_all_documentation_links(
            self, url: str, max_depth: int = 3, current_depth: int = 0
        ) -> list[str]:
        """
        Recursively finds all unique documentation links from a given URL.

        This method crawls web pages starting from the provided URL up to
        `max_depth`, collecting links that belong to the same domain as the
        `base_url`. It avoids visiting the same URL multiple times and
        ignores fragment links (#) and mailto links.

        Args:
            url: The current URL to scrape for links.
            max_depth: The maximum depth of recursion for link discovery.
                       Prevents excessively deep crawling.
            current_depth: The current depth in the recursion, used to track
                           against `max_depth`.

        Returns:
            A list of unique URLs found within the specified domain and depth.
            Returns an empty list if the depth limit is reached, the URL has
            been visited, or an error occurs during processing.
        """
        if current_depth >= max_depth or url in self.visited_urls:
            # Stop recursion if max depth is reached or URL is already visited
            return []
        self.visited_urls.add(url)
        links: list[str] = []

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            soup = BeautifulSoup(response.content, 'html.parser')

            for link in soup.find_all('a', href=True):
                href: str = link['href']
                full_url: str = urljoin(url, href)  # Resolve relative URLs

                # Check if the link is within the same domain, not visited,
                # and not an anchor or mailto link.
                if (urlparse(full_url).netloc == urlparse(self.base_url).netloc and
                        full_url not in self.visited_urls and
                        not href.startswith('#') and
                        not href.startswith('mailto:')):
                    links.append(full_url)
                    # Recursively get links from the newly found page
                    links.extend(
                        self.get_all_documentation_links(
                            full_url, max_depth, current_depth + 1
                        )
                    )
            # Brief pause to be polite to the server
            time.sleep(0.5)
        except requests.exceptions.RequestException as e:
            # Handle network errors, timeouts, etc.
            logging.error(f"Request error while processing {url}: {e}")
        except Exception as e:
            # Handle other potential errors (e.g., parsing errors)
            logging.error(f"Unexpected error processing {url} for links: {e}")
        # Return unique links
        return list(set(links))

    def convert_html_to_markdown_docling(self, html_content: str) -> str | None:
        """
        Converts HTML content to Markdown using the Docling library.

        This method requires Docling to be installed and initialized.
        It writes the HTML content to a temporary file, as Docling currently
        operates on file paths.

        Args:
            html_content: A string containing the HTML to be converted.

        Returns:
            The converted Markdown string if successful, or None if Docling
            is not available/fails or if any error occurs during conversion.
        """
        if not self.use_docling or not self.converter:
            logging.warning(
                "Docling is not available or not initialized. Skipping Docling conversion."
            )
            return None

        logging.info("Attempting HTML to Markdown conversion using Docling.")
        temp_html_path = "temp_doc.html"  # Temporary file for Docling processing
        try:
            with open(temp_html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            # Assuming self.converter is an initialized DocumentConverter instance
            result = self.converter.convert(temp_html_path)
            markdown = result.document.export_to_markdown()
            logging.info("Docling conversion succeeded.")
            return markdown
        except Exception as e:
            logging.warning(f"Docling conversion failed: {e}")
            return None  # Return None to allow fallback to other converters
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_html_path):
                os.remove(temp_html_path)

    def convert_html_to_markdown_markdownify(self, html_content: str) -> str | None:
        """
        Converts HTML content to Markdown using the Markdownify library.

        This method utilizes the `markdownify` function with specific options
        for heading style, bullet points, and a callback for code language
        detection.

        Args:
            html_content: A string containing the HTML to be converted.

        Returns:
            The converted Markdown string if successful, or None if Markdownify
            is not available or if any error occurs during conversion.
        """
        if not self.markdownify_available:
            logging.warning(
                "Markdownify is not available. Skipping Markdownify conversion."
            )
            return None

        logging.info("Attempting HTML to Markdown conversion using Markdownify.")
        try:
            # Use Markdownify with ATX style headings, common bullet characters,
            # and a code language callback for better code block formatting.
            markdown = md(
                html_content,
                heading_style='atx',
                bullets='*+-',
                code_language_callback=get_code_language_from_class
            )
            logging.info("Markdownify conversion succeeded.")
            return markdown
        except Exception as e:
            logging.warning(f"Markdownify conversion failed: {e}")
            return None  # Return None to allow fallback

    def convert_html_to_markdown_html2text(self, html_content: str) -> str | None:
        """
        Converts HTML to Markdown using the `html_to_markdown` library.

        This method serves as a fallback if more advanced converters like
        Docling or Markdownify are unavailable or fail. If `html_to_markdown`
        also fails, it attempts to extract plain text from the HTML using
        BeautifulSoup as a final measure.

        Args:
            html_content: A string containing the HTML to be converted.

        Returns:
            The converted Markdown string if successful. If `html_to_markdown`
            fails, returns plain text extracted from HTML. Returns None if
            the library is not available.
        """
        if not self.html_to_markdown_available:
            logging.error(
                "html_to_markdown library is not available. Cannot perform this conversion."
            )
            return None # Critical fallback missing

        logging.info(
            "Attempting HTML to Markdown conversion using html_to_markdown (html2text equivalent)."
        )
        try:
            # This function is imported as 'convert_to_markdown'
            markdown = convert_to_markdown(html_content)
            logging.info("html_to_markdown (html2text) conversion succeeded.")
            return markdown
        except Exception as e:
            logging.warning(
                f"html_to_markdown (html2text) conversion failed: {e}. "
                "Falling back to plain text extraction."
            )
            # Ultimate fallback: extract all text content from HTML
            try:
                soup = BeautifulSoup(html_content, 'html.parser')
                return soup.get_text()
            except Exception as soup_err:
                logging.error(f"Plain text extraction with BeautifulSoup also failed: {soup_err}")
                return "" # Return empty string if even text extraction fails.

    def process_single_page(self, url: str) -> dict[str, str] | None:
        """
        Fetches, converts, and processes a single documentation page.

        This method retrieves HTML content from the given URL, attempts to
        extract the main content area, and then converts this HTML to Markdown
        using a prioritized list of converters (Docling, Markdownify,
        html_to_markdown, then plain text).

        Args:
            url: The URL of the documentation page to process.

        Returns:
            A dictionary containing the 'url', 'title', and 'content' (Markdown)
            of the page if successful. Returns None if the page cannot be
            fetched or if all conversion methods ultimately fail to produce content.
        """
        try:
            logging.info(f"Processing page: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Ensure we process only successful requests
            soup = BeautifulSoup(response.content, 'html.parser')

            # Attempt to find the main content area of the page.
            # Common tags/classes for main content are 'main', 'article',
            # 'content', 'documentation', 'docs'. Falls back to 'body'.
            main_content_tags = (
                soup.find('main') or
                soup.find('article') or
                soup.find('div', class_=['content', 'documentation', 'docs']) or
                soup.find('body')  # Fallback to the entire body if specific tags aren't found
            )
            html_content = str(main_content_tags) if main_content_tags else response.text
            page_title = soup.title.string if soup.title else urlparse(url).path.split('/')[-1] or url

            markdown_content: str | None = None
            tried_preferred = False # To track if the preferred converter was attempted

            # --- Attempt 1: User's preferred method ---
            logging.info(f"User's preferred converter: {self.preferred_converter}")

            if self.preferred_converter == "docling":
                if self.use_docling: # self.use_docling implies self.docling_available is True
                    logging.info(f"Attempting user-preferred conversion: Docling for {url}")
                    markdown_content = self.convert_html_to_markdown_docling(html_content)
                    tried_preferred = True
                else:
                    logging.warning(
                        f"Preferred converter Docling is not available or not enabled for {url}. "
                        "Proceeding to fallbacks."
                    )
                    # Set tried_preferred to True because the category 'docling' was selected,
                    # even if it couldn't run. This prevents it from being tried again as a fallback.
                    tried_preferred = True # Or False if we want to allow it as a fallback if not initially available
                                          # Based on logic, if preferred is X, don't try X again in fallback.
            elif self.preferred_converter == "markdownify":
                if self.markdownify_available:
                    logging.info(f"Attempting user-preferred conversion: Markdownify for {url}")
                    markdown_content = self.convert_html_to_markdown_markdownify(html_content)
                    tried_preferred = True
                else:
                    logging.warning(
                        f"Preferred converter Markdownify is not available for {url}. "
                        "Proceeding to fallbacks."
                    )
                    tried_preferred = True # Mark as 'tried' to prevent re-attempt
            elif self.preferred_converter == "html2text":
                if self.html_to_markdown_available:
                    logging.info(f"Attempting user-preferred conversion: html2text for {url}")
                    markdown_content = self.convert_html_to_markdown_html2text(html_content)
                    tried_preferred = True
                else: # This case should be rare if html_to_markdown is a critical dependency
                    logging.warning(
                        f"Preferred converter html2text (html_to_markdown) is somehow not available for {url}. "
                        "Proceeding to fallbacks."
                    )
                    tried_preferred = True # Mark as 'tried'

            # --- Fallback logic ---
            # Try Docling if it wasn't the preferred (and failed) or if it wasn't preferred at all
            if markdown_content is None:
                if not (tried_preferred and self.preferred_converter == "docling") and self.use_docling:
                    logging.info(f"Falling back to Docling conversion for {url}")
                    markdown_content = self.convert_html_to_markdown_docling(html_content)
            
            # Try Markdownify if it wasn't the preferred (and failed) or if it wasn't preferred at all
            if markdown_content is None:
                if not (tried_preferred and self.preferred_converter == "markdownify") and self.markdownify_available:
                    logging.info(f"Falling back to Markdownify conversion for {url}")
                    markdown_content = self.convert_html_to_markdown_markdownify(html_content)

            # Try html2text if it wasn't the preferred (and failed) or if it wasn't preferred at all
            if markdown_content is None:
                if not (tried_preferred and self.preferred_converter == "html2text") and self.html_to_markdown_available:
                    logging.info(f"Falling back to html2text conversion for {url}")
                    markdown_content = self.convert_html_to_markdown_html2text(html_content)
                elif not self.html_to_markdown_available: # If html2text wasn't available for fallback either
                     logging.error("html_to_markdown library is not available, cannot use as fallback.")


            # Ultimate fallback to plain text extraction if all else fails.
            # This should ideally be caught by convert_html_to_markdown_html2text's internal get_text(),
            # but as a safety net here if html2text itself returned None or was unavailable.
            if markdown_content is None:
                logging.error(
                    f"All conversion methods (preferred: {self.preferred_converter}, and fallbacks) "
                    f"failed for {url}. Extracting plain text as a last resort."
                )
                # Re-parse html_content to a new soup object if necessary, or use existing 'soup' if html_content was main_content_tags
                # If html_content is a string, it needs to be parsed.
                # The original 'soup' is for the whole page, 'html_content' is for the main part.
                temp_soup_for_get_text = BeautifulSoup(html_content, 'html.parser')
                markdown_content = temp_soup_for_get_text.get_text(separator='\n', strip=True)
                if not markdown_content: # If even get_text yields nothing
                    logging.warning(f"Plain text extraction yielded no content for {url}.")
                    markdown_content = "" # Ensure it's an empty string not None

            return {
                'url': url,
                'title': page_title.strip(), # page_title defined earlier
                'content': markdown_content.strip() if markdown_content else ""
            }
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch page {url}: {e}")
            return None
        except Exception as e:
            # Catch-all for other unexpected errors during page processing
            logging.error(f"An unexpected error occurred while processing page {url}: {e}")
            return None

    def convert_documentation_site(
            self,
            output_file: str = "comprehensive_documentation.md",
            max_pages: int = 50,
            max_depth: int = 3
        ) -> str:
        """
        Converts an entire documentation site to a single Markdown file.

        It starts by discovering all relevant links from the base URL up to
        `max_depth`, then processes each page up to `max_pages`, and finally
        compiles the results into the specified `output_file`.

        Args:
            output_file: The name of the Markdown file to generate.
                         Defaults to "comprehensive_documentation.md".
            max_pages: The maximum number of pages to convert.
                       Defaults to 50.
            max_depth: The maximum crawl depth for discovering links.
                       Defaults to 3.

        Returns:
            The path to the generated output file.
        """
        print(f"Starting conversion of documentation site: {self.base_url}")
        print(
            f"Discovery parameters - Max Depth: {max_depth}, Max Pages to Convert: {max_pages}"
        )

        # Discover all documentation links starting from the base URL
        # The base URL itself is added to ensure it's processed if it's a content page.
        all_links = [self.base_url] + self.get_all_documentation_links(
            self.base_url, max_depth=max_depth
        )
        # Remove duplicates and limit the number of pages to process
        unique_links = list(set(all_links))
        links_to_process = unique_links[:max_pages]

        print(
            f"Found {len(unique_links)} unique pages. Processing up to {len(links_to_process)} pages."
        )

        all_converted_content: list[dict[str,str]] = []
        for i, url in enumerate(links_to_process, 1):
            print(f"Processing page {i}/{len(links_to_process)}: {url}")
            page_data = self.process_single_page(url)
            if page_data and page_data.get('content'): # Ensure content is not empty
                all_converted_content.append(page_data)
            else:
                logging.warning(f"Skipping page {url} due to processing error or empty content.")
            # Polite delay between requests
            time.sleep(0.5) # Consider making this configurable

        print(f"\nGenerating comprehensive documentation file: {output_file}")

        # Prepare the final Markdown string
        title_section = f"# Comprehensive Documentation for {self.base_url}\n\n"
        generation_time_section = f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        metadata_section = (
            f"Source URL: {self.base_url}\n"
            f"Max Crawl Depth: {max_depth}\n"
            f"Max Pages Processed: {len(links_to_process)} (out of {len(unique_links)} found)\n\n"
        )
        separator = "---\n\n"

        final_markdown_list = [title_section, generation_time_section, metadata_section, separator]

        if not all_converted_content:
            final_markdown_list.append("No content was successfully converted.\n")
        else:
            for page in all_converted_content:
                final_markdown_list.append(f"## {page['title']}\n\n")
                final_markdown_list.append(f"**Source URL:** <{page['url']}>\n\n")
                final_markdown_list.append(page['content'] + "\n\n")
                final_markdown_list.append(separator)
        
        final_markdown_string = "".join(final_markdown_list)

        # Estimate tokens
        token_estimate, estimation_method = estimate_tokens(final_markdown_string)

        # Write the final string to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_markdown_string)

        print(
            f"Conversion complete! Generated {output_file} with content from "
            f"{len(all_converted_content)} pages."
        )
        print(
            f"Estimated token count for the generated document: ~{token_estimate} tokens (using {estimation_method})."
        )
        return output_file


if __name__ == "__main__":
    # Main execution block for running the script from the command line.

    # --- User Input for Script Parameters ---

    # Prompt for the base URL
    while True:
        base_url_input = input(
            "Enter the base URL for the documentation (e.g., https://docs.example.com): "
        ).strip()
        if not base_url_input:
            print("Base URL cannot be empty.")
        elif base_url_input.startswith("http://") or base_url_input.startswith("https://"):
            break
        else:
            print("Invalid URL. Please ensure it starts with 'http://' or 'https://'.")

    # Prompt for maximum crawl depth
    while True:
        try:
            max_depth_str = input(
                "Enter the maximum crawl depth for links (integer, default: 3): "
            ).strip()
            if not max_depth_str:
                max_depth_input = 3  # Default value
                break
            max_depth_input = int(max_depth_str)
            if max_depth_input < 0:
                print("Max depth cannot be negative. Please enter 0 or a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for max depth.")

    # Prompt for maximum number of pages to convert
    while True:
        try:
            max_pages_str = input(
                "Enter the maximum number of pages to convert (integer, default: 50): "
            ).strip()
            if not max_pages_str:
                max_pages_input = 50  # Default value
                break
            max_pages_input = int(max_pages_str)
            if max_pages_input <= 0:
                print("Max pages must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for max pages.")

    # Prompt for the output filename
    output_filename_input = input(
        "Enter the desired output filename (default: comprehensive_documentation.md): "
    ).strip()
    if not output_filename_input:
        output_filename_input = "comprehensive_documentation.md"  # Default value
    # Ensure the filename ends with .md
    if not output_filename_input.endswith(".md"):
        output_filename_input += ".md"

    # Prompt for preferred converter
    while True:
        preferred_converter_input = input(
            "Choose your preferred HTML-to-Markdown converter ('docling', 'markdownify', 'html2text') (default: 'docling'): "
        ).strip().lower()
        if not preferred_converter_input:
            preferred_converter_input = "docling"  # Default value
            break
        if preferred_converter_input in ["docling", "markdownify", "html2text"]:
            break
        else:
            print(
                "Invalid choice. Please enter 'docling', 'markdownify', or 'html2text'."
            )

    # --- Display Parameters and Start Conversion ---
    print(f"\nStarting documentation conversion with the following parameters:")
    print(f"  Base URL: {base_url_input}")
    print(f"  Max Crawl Depth: {max_depth_input}")
    print(f"  Max Pages to Convert: {max_pages_input}")
    print(f"  Output File: {output_filename_input}")
    print(f"  Preferred Converter: {preferred_converter_input}\n")

    try:
        # Initialize the converter with the user's preferred method
        converter_instance = DocumentationConverter(
            base_url_input,
            preferred_converter=preferred_converter_input
            # Assuming use_docling preference is still implicitly True by default in __init__
            # or could be another input if we want explicit control over enabling Docling at all
        )

        # Run the documentation conversion process
        final_output_file = converter_instance.convert_documentation_site(
            output_file=output_filename_input,
            max_pages=max_pages_input,
            max_depth=max_depth_input
        )
        print(f"Documentation successfully saved to: {final_output_file}")
    except ValueError as ve: # Catch specific error from __init__
        print(f"Error initializing converter: {ve}")
    except Exception as e:
        # Catch any other unexpected errors during the main execution
        print(f"An unexpected error occurred during the script execution: {e}")
        logging.error(f"Unhandled exception in __main__: {e}", exc_info=True)
