# Web Documentation Scraper to Markdown

## Description

This Python script scrapes documentation websites and converts their HTML content into a single Markdown file. The output is optimized for easy ingestion by AI agents and Large Language Models (LLMs), facilitating the process of gathering and preprocessing online documentation.

## Features

*   **Recursive Link Scraping:** Efficiently crawls and discovers documentation links within a specified domain.
*   **Configurable Crawling:** Allows users to set the maximum crawl depth and the total number of pages to convert.
*   **Multiple Conversion Methods:** Offers a choice of HTML-to-Markdown conversion engines:
    *   **Docling:** Advanced conversion (if available and installed separately).
    *   **Markdownify:** Robust conversion, particularly good for handling code blocks.
    *   **html2text:** A basic fallback converter.
*   **Preferred Converter Selection:** Users can select their primary preferred conversion method.
*   **Graceful Fallback:** If the preferred converter fails or is unavailable, the script automatically falls back through other methods (Docling -> Markdownify -> html2text -> Plain Text Extraction).
*   **Main Content Extraction:** Intelligently attempts to extract only the main content from web pages, reducing noise and irrelevant elements like sidebars or footers.
*   **Consolidated Output:** Generates a single, well-structured Markdown file containing all scraped and converted documentation.
*   **Token Estimation:** Provides an estimated token count for the output document using `tiktoken` with the `o200k_base` encoding for accuracy (falls back to word count if `tiktoken` is unavailable).
*   **User-Friendly CLI:** Interactive command-line interface for easy input of scraping parameters.
*   **Well-Commented Code:** The script is thoroughly commented, with logging for better understanding and debugging.

## Prerequisites

*   Python 3.7+ (or a similar recent version)
*   `pip` (Python package installer)

## Installation

1.  Ensure Python and pip are installed on your system.
2.  Clone or download the `webscrapper.py` script.
3.  Install the necessary Python libraries by running the following command in your terminal:
    ```bash
    pip install requests beautifulsoup4 html-to-markdown markdownify tiktoken
    ```
4.  **Optional Dependency (Docling):**
    If you have access to Docling and wish to use it as a conversion method, ensure it is installed in your Python environment. Docling is not included in the standard installation command above.

## Usage

1.  Navigate to the directory where you saved `webscrapper.py`.
2.  Run the script from your terminal:
    ```bash
    python webscrapper.py
    ```
3.  The script will then prompt you for the following information:
    *   **Base URL:** The starting URL for the documentation you want to scrape (e.g., `https://docs.example.com`). This URL must include the scheme (`http://` or `https://`).
    *   **Maximum Crawl Depth:** An integer specifying how many links deep the scraper should follow from the base URL (e.g., `3`). Press Enter for the default value (3).
    *   **Maximum Number of Pages:** An integer limiting the total number of pages to convert (e.g., `50`). Press Enter for the default value (50).
    *   **Preferred Converter:** Your choice of primary HTML-to-Markdown conversion engine. Options are `'docling'`, `'markdownify'`, or `'html2text'`. Press Enter for the default ('docling').
    *   **Output Filename:** The desired name for the generated Markdown file (e.g., `my_docs.md`). Press Enter for the default (`comprehensive_documentation.md`). If you don't add `.md`, it will be appended.

The script will then proceed to scrape and convert the documentation. The final Markdown file will be saved in the same directory where the script was executed.

## Conversion Methods

The script employs several HTML-to-Markdown conversion methods to provide flexibility and robustness:

1.  **Docling:** (If available and selected/enabled) Offers advanced document structure analysis and conversion.
2.  **Markdownify:** A powerful library that is generally good at preserving code block formatting and overall structure.
3.  **html2text:** A more basic converter that serves as a reliable fallback.
4.  **Plain Text Extraction:** If all Markdown conversion methods fail for a page, the script will extract the raw text content from the HTML.

The script will first attempt to use the user's **preferred converter**. If the preferred method fails or is unavailable, it will cycle through the other methods in the order: Docling -> Markdownify -> html2text, skipping any method that was already tried as preferred.

## Output

*   A single Markdown file (e.g., `comprehensive_documentation.md`) containing the scraped content from all processed pages.
*   A message printed to the console after completion, indicating the path to the output file and an estimated token count for the document.

### Token Estimation Details
The script provides an estimated token count for the generated Markdown file. By default, it uses the `tiktoken` library with the `o200k_base` encoding, which aligns with tokenization methods used by advanced OpenAI models (like GPT-4o and GPT-4 Turbo). This provides a more accurate estimate of how many tokens the document will consume in an LLM context.

If `tiktoken` is not installed or fails to initialize (e.g., if the specific encoding is not available), the script will fall back to a simpler word-based count (`len(text.split())`). The method used for estimation (`tiktoken (o200k_base)` or `word count`) will be indicated in the console output.

## Example

```bash
python webscrapper.py
Enter the base URL for the documentation (e.g., https://docs.example.com): https://requests.readthedocs.io/en/latest/
Enter the maximum crawl depth for links (integer, default: 3): 
Enter the maximum number of pages to convert (integer, default: 50): 20
Choose your preferred HTML-to-Markdown converter ('docling', 'markdownify', 'html2text') (default: 'docling'): markdownify
Enter the desired output filename (default: comprehensive_documentation.md): requests_docs.md

Starting documentation conversion with the following parameters:
  Base URL: https://requests.readthedocs.io/en/latest/
  Max Crawl Depth: 3
  Max Pages to Convert: 20
  Output File: requests_docs.md
  Preferred Converter: markdownify

Starting conversion of documentation site: https://requests.readthedocs.io/en/latest/
Discovery parameters - Max Depth: 3, Max Pages to Convert: 20
Found 50 unique pages. Processing up to 20 pages.
Processing page 1/20: https://requests.readthedocs.io/en/latest/
... (script output continues) ...
Conversion complete! Generated requests_docs.md with content from 20 pages.
Estimated token count for the generated document: ~14500 tokens (using tiktoken (o200k_base)). 
```
*(Note: The exact token count in the example output may vary based on library versions and content.)*

## Troubleshooting

*   **Poor Conversion Quality:** If a website doesn't convert well, try selecting a different preferred conversion method when prompted. Some websites with heavy client-side JavaScript rendering might pose challenges for this scraper.
*   **Dependency Issues:** Ensure all required libraries (requests, beautifulsoup4, html-to-markdown, markdownify, tiktoken) are correctly installed in your Python environment. Use `pip list` to check installed packages.
*   **Docling Not Found:** If you intend to use Docling, verify it's installed. It's an optional dependency not included in the standard `pip install` command.
*   **Network Errors:** Ensure you have a stable internet connection. The script includes basic error handling for request issues, but persistent network problems will hinder scraping.

## License

This project is open-source. You are free to use, modify, and distribute it as you see fit.
(Consider adding a specific license like MIT if you wish formalize terms).
