# Python Web Scraping — Examples

[![CI](https://github.com/python-web-scraping-com/examples/actions/workflows/ci.yml/badge.svg)](https://github.com/python-web-scraping-com/examples/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Runnable, **tested** Python web scraping examples — the companion code for
[python-web-scraping.com](https://python-web-scraping.com).

Every example is a small, self-contained function with a test. Each module maps
to a guide on the site, so you can read the explanation there and run the code here.

## Quick start

```bash
git clone https://github.com/python-web-scraping-com/examples.git
cd examples
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Run any example directly:

```bash
python -m pws_examples.parsing
python -m pws_examples.storage
python -m pws_examples.async_scrape   # this one makes real HTTP requests
```

Run the tests and linter:

```bash
pytest
ruff check .
```

## What's inside

| Module | What it shows | Guide |
| --- | --- | --- |
| `pws_examples/parsing.py` | Parse product cards and HTML tables with BeautifulSoup | [Parsing HTML with BeautifulSoup](https://python-web-scraping.com/the-complete-guide-to-python-web-scraping/parsing-html-with-beautifulsoup/) |
| `pws_examples/extraction.py` | Extract emails and phone numbers with regex | [Extracting Data with Regular Expressions](https://python-web-scraping.com/the-complete-guide-to-python-web-scraping/extracting-data-with-regular-expressions/) |
| `pws_examples/http_client.py` | A `requests` session with retries and backoff | [Understanding HTTP Requests and Responses](https://python-web-scraping.com/the-complete-guide-to-python-web-scraping/understanding-http-requests-and-responses/) |
| `pws_examples/storage.py` | Validate with Pydantic, store in SQLite, de-duplicate | [Storing and Exporting Scraped Data](https://python-web-scraping.com/scaling-python-web-scrapers/storing-and-exporting-scraped-data/) |
| `pws_examples/async_scrape.py` | Concurrent fetching with asyncio + HTTPX and a semaphore | [Asynchronous Scraping with asyncio and HTTPX](https://python-web-scraping.com/scaling-python-web-scrapers/asynchronous-scraping-with-asyncio-and-httpx/) |

The tests use local HTML fixtures and `httpx.MockTransport`, so the suite is
deterministic and runs offline — no live websites are hit in CI.

## Scrape responsibly

These examples are for learning. When scraping real sites, respect `robots.txt`,
rate-limit your requests, identify your client honestly, and follow each site's
terms of service.

## Contributing

Contributions are welcome. Please keep each example small and focused, add a test
for it, and make sure `pytest` and `ruff check .` pass before opening a PR.

## License

[MIT](LICENSE) © Python Web Scraping
