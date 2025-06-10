# Web Documentation Scraper

This script is a versatile tool for scraping online documentation from websites and converting the HTML content into Markdown format. It is designed to handle various documentation structures and provides options for controlling the scraping depth, filtering URLs, and selecting different conversion methods.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Command-Line Arguments](#command-line-arguments)
- [Conversion Methods](#conversion-methods)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

*   **Consistent Scraping**: Uses Breadth-First Search (BFS) to traverse links predictably.
*   **Multiple Conversion Methods**: Supports `markdownify`, `html-to-markdown`, `pyhtml2md`, and `docling-core`.
*   **Configurable Scraping**: Control depth, number of pages, and target specific content areas using CSS selectors.
*   **URL Filtering**: Include or exclude URLs based on regex patterns.
*   **Flexible Output**: Save individual Markdown files or concatenate them into a single document.
*   **Detailed Logging**: Monitor the scraping and conversion process.




## Installation

To use this script, you need Python 3.8 or higher. You can install the required dependencies using pip:

```bash
pip install requests beautifulsoup4 markdownify html-to-markdown pyhtml2md docling-core tiktoken
```

*   `requests`: For making HTTP requests to fetch web pages.
*   `beautifulsoup4`: For parsing HTML and extracting content.
*   `markdownify`: A powerful HTML to Markdown converter.
*   `html-to-markdown`: Another robust HTML to Markdown converter.
*   `pyhtml2md`: A simple HTML to Markdown converter.
*   `docling-core`: A core component of the Docling library for advanced document processing and conversion. (Note: The full `docling` package has extensive dependencies, `docling-core` is a lighter alternative for HTML to Markdown conversion).
*   `tiktoken`: (Optional) Used for more accurate token estimation, especially useful for AI agent applications. If not installed, the script will fall back to word count.




## Usage

To run the script, execute it from your terminal with the base URL of the documentation site you want to scrape, along with any desired arguments.

```bash
python improved_webscrapper.py <base_url> [options]
```

Replace `<base_url>` with the actual URL of the documentation site. For example:

```bash
python improved_webscrapper.py https://docs.python.org/3/ --output_dir python_docs --max_depth 2 --max_pages 100 --conversion_method markdownify
```




## Command-Line Arguments

| Argument                  | Description                                                                                                                              | Default Value      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `base_url`                | **(Required)** The base URL of the documentation site to scrape.                                                                         | N/A                |
| `--output_dir`            | Directory to save the Markdown files.                                                                                                    | `./output`         |
| `--max_depth`             | Maximum depth for link discovery.                                                                                                        | `3`                |
| `--max_pages`             | Maximum number of unique pages to scrape.                                                                                                | `50`               |
| `--conversion_method`     | Preferred HTML to Markdown conversion method. See [Conversion Methods](#conversion-methods) for options.                                   | `auto`             |
| `--concatenate_output`    | Concatenate all individual Markdown files into a single file named `all_documentation.md`.                                               | `False` (flag)     |
| `--log_level`             | Set the logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).                                                                 | `INFO`             |
| `--main_content_selector` | CSS selector to identify the main content area of a page. This is highly recommended for cleaner output.                                 | `None`             |
| `--include_patterns`      | List of regex patterns for URLs to include. If provided, only URLs matching any of these patterns will be scraped.                       | `None`             |
| `--exclude_patterns`      | List of regex patterns for URLs to exclude. URLs matching any of these patterns will be skipped.                                         | `None`             |




## Conversion Methods

The script supports several HTML to Markdown conversion libraries. You can specify your preferred method using the `--conversion_method` argument. If set to `auto` (default), the script will attempt to use available converters in a predefined order.

*   **`auto` (Default)**: The script will try `docling`, then `markdownify`, then `pyhtml2md`, and finally `html-to-markdown`. If all fail, it falls back to plain text extraction.
*   **`docling`**: Utilizes the `docling-core` library. This method might offer more advanced document structure preservation but currently requires writing to a temporary file.
*   **`markdownify`**: A popular and generally robust converter. It provides good control over output formatting.
*   **`pyhtml2md`**: A straightforward converter that often produces clean Markdown.
*   **`html2text`**: Uses the `html-to-markdown` library (note the argument name `html2text` for historical reasons, it maps to `html-to-markdown` library). A reliable fallback for many HTML structures.

It is recommended to experiment with different conversion methods for your target documentation site to find the one that yields the best-formatted Markdown.




## Examples

Here are a few examples demonstrating how to use the `improved_webscrapper.py` script:

**1. Basic Usage (Scrape with default settings):**

```bash
python improved_webscrapper.py https://docs.python.org/3/
```

This will scrape the Python 3 documentation starting from the base URL, go up to a depth of 3, scrape a maximum of 50 pages, use the `auto` conversion method, and save individual Markdown files in an `./output` directory.

**2. Specify Output Directory and Max Pages:**

```bash
python improved_webscrapper.py https://nextjs.org/docs --output_dir ./nextjs_docs --max_pages 100
```

This command scrapes the Next.js documentation, saves the output to `./nextjs_docs`, and limits the scraping to the first 100 unique pages found.

**3. Use a Specific Conversion Method and Concatenate Output:**

```bash
python improved_webscrapper.py https://developers.google.com/gemini/docs --conversion_method markdownify --concatenate_output
```

This example scrapes the Google Gemini API documentation, forces the use of the `markdownify` converter, and combines all the resulting Markdown into a single file (`all_documentation.md`) in the default `./output` directory.

**4. Scrape with Limited Depth and Specific Content Selector:**

```bash
python improved_webscrapper.py https://react.dev/reference/react --max_depth 2 --main_content_selector "article.markdown"
```

This scrapes the React documentation reference section up to depth 2, focusing only on content within `<article class="markdown">` tags.

**5. Include and Exclude Specific URL Patterns:**

```bash
python improved_webscrapper.py https://docs.djangoproject.com/en/5.0/ --include_patterns ".*/topics/.*" ".*/ref/.*" --exclude_patterns ".*/migrations/.*"
```

This command scrapes the Django documentation, but only includes URLs containing `/topics/` or `/ref/` in their path, while explicitly excluding any URLs containing `/migrations/`.

**6. Set Logging Level to Debug:**

```bash
python improved_webscrapper.py https://docs.docker.com/get-started/ --log_level DEBUG
```

This runs the scraper on the Docker documentation with detailed debug logging enabled, which can be helpful for troubleshooting.

Feel free to combine these options to tailor the scraping process to your specific needs.




## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.



