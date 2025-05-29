import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import os
import time
import logging

# Setup logging to track which conversion algorithm is used
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import InputFormat
    DOCLING_AVAILABLE = True
except ImportError:
    DOCLING_AVAILABLE = False
    from html_to_markdown import convert_to_markdown

class DocumentationConverter:
    def __init__(self, base_url, use_docling=True):
        self.base_url = base_url
        self.visited_urls = set()
        # Only enable Docling if installed and requested
        self.use_docling = use_docling and DOCLING_AVAILABLE
        if use_docling and DOCLING_AVAILABLE:
            try:
                self.converter = DocumentConverter()
            except Exception as e:
                logging.warning(f"Docling init failed: {e}. Falling back to html-to-markdown.")
                self.use_docling = False

    def get_all_documentation_links(self, url, max_depth=3, current_depth=0):
        """Recursively find all documentation links from the base URL"""
        if current_depth >= max_depth or url in self.visited_urls:
            return []
        self.visited_urls.add(url)
        links = []
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(url, href)
                if (urlparse(full_url).netloc == urlparse(self.base_url).netloc and
                    full_url not in self.visited_urls and
                    not href.startswith('#') and
                    not href.startswith('mailto:')):
                    links.append(full_url)
                    links.extend(
                        self.get_all_documentation_links(
                            full_url, max_depth, current_depth + 1
                        )
                    )
            time.sleep(0.5)
        except Exception as e:
            logging.error(f"Error processing {url}: {e}")
        return list(set(links))

    def convert_html_to_markdown_docling(self, html_content):
        """Convert HTML to Markdown using Docling"""
        logging.info("Using Docling conversion")
        temp_html_path = "temp_doc.html"
        try:
            with open(temp_html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            result = self.converter.convert(temp_html_path)
            markdown = result.document.export_to_markdown()
            logging.info("Docling conversion succeeded")
            return markdown
        except Exception as e:
            logging.warning(f"Docling conversion failed: {e}")
            return self.convert_html_to_markdown_fallback(html_content)
        finally:
            if os.path.exists(temp_html_path):
                os.remove(temp_html_path)

    def convert_html_to_markdown_fallback(self, html_content):
        """Fallback HTML to Markdown conversion using html-to-markdown library"""
        logging.info("Using html-to-markdown conversion")
        try:
            markdown = convert_to_markdown(html_content)
            logging.info("html-to-markdown conversion succeeded")
            return markdown
        except Exception as e:
            logging.warning(f"html-to-markdown conversion failed: {e}")
            logging.info("Using plain text conversion")
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup.get_text()

    def process_single_page(self, url):
        """Convert a single documentation page to Markdown"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            main_content = (
                soup.find('main') or
                soup.find('article') or
                soup.find('div', class_=['content', 'documentation', 'docs']) or
                soup.find('body')
            )
            html_content = str(main_content) if main_content else response.text
            if self.use_docling:
                markdown_content = self.convert_html_to_markdown_docling(html_content)
            else:
                markdown_content = self.convert_html_to_markdown_fallback(html_content)
            return {
                'url': url,
                'title': soup.title.string if soup.title else url,
                'content': markdown_content
            }
        except Exception as e:
            logging.error(f"Error processing {url}: {e}")
            return None

    def convert_documentation_site(self, output_file="comprehensive_documentation.md", max_pages=50):
        """Convert entire documentation site to a single Markdown file"""
        print(f"Starting conversion of {self.base_url}")
        print("Discovering documentation pages...")
        all_links = [self.base_url] + self.get_all_documentation_links(self.base_url)
        all_links = list(set(all_links))[:max_pages]
        print(f"Found {len(all_links)} pages to convert")
        all_content = []
        for i, url in enumerate(all_links, 1):
            print(f"Processing page {i}/{len(all_links)}: {url}")
            page_data = self.process_single_page(url)
            if page_data:
                all_content.append(page_data)
            time.sleep(0.5)
        print(f"Generating comprehensive documentation file: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Comprehensive Documentation for {self.base_url}\n\n")
            f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n")
            for page in all_content:
                f.write(f"## {page['title']}\n\n")
                f.write(f"**Source URL:** {page['url']}\n\n")
                f.write(page['content'] + "\n\n---\n\n")
        print(f"Conversion complete! Generated {output_file} with {len(all_content)} pages")
        return output_file

if __name__ == "__main__":
    converter = DocumentationConverter("https://nextjs.org/docs/")
    output_file = converter.convert_documentation_site(
        output_file="google_ai_api_documentation.md",
        max_pages=500
    )
    print(f"Documentation saved to: {output_file}")
