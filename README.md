# Scrapping

## Project Overview
This repository contains a collection of Python scripts demonstrating foundational web scraping techniques. It shows how to retrieve HTML contents from websites, parse the markup to extract specific elements, and handle potential network or HTTP errors during extraction.

## Tech Stack
- **Python**: Core programming language.
- **BeautifulSoup4**: HTML parsing library for extracting data from markup.
- **urllib**: Standard library for making HTTP requests and handling errors.
- **lxml**: Fast XML/HTML parser back-end for BeautifulSoup.

## Key Implementation Details
- **Markup Extraction (`demo.py`)**: Uses `urllib.request.urlopen` to retrieve webpage content and parses it with `BeautifulSoup` to find specific HTML tags.
- **Robust Exception Handling (`ErrorHandingForScrapping.py`)**: Uses Python try-except blocks to catch HTTP errors (like 404/500 status codes) and URL errors (like domain resolution failures), ensuring graceful failures when scraping.
