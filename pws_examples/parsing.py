"""HTML parsing with BeautifulSoup.

Companion code for:
- https://python-web-scraping.com/the-complete-guide-to-python-web-scraping/parsing-html-with-beautifulsoup/
- https://python-web-scraping.com/the-complete-guide-to-python-web-scraping/understanding-http-requests-and-responses/step-by-step-guide-to-extracting-tables-from-html/
"""

from __future__ import annotations

from bs4 import BeautifulSoup


def parse_products(html: str) -> list[dict]:
    """Extract product cards (title + price) from a listing page's HTML."""
    soup = BeautifulSoup(html, "lxml")
    products: list[dict] = []
    for card in soup.select("article.product_pod"):
        title = card.select_one("h3 a")
        price = card.select_one("p.price_color")
        if title and price:
            products.append(
                {
                    "title": title.get("title") or title.get_text(strip=True),
                    "price": price.get_text(strip=True),
                }
            )
    return products


def extract_table(html: str) -> list[dict]:
    """Convert the first ``<table>`` into a list of row dicts keyed by header."""
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table")
    if table is None:
        return []
    headers = [th.get_text(strip=True) for th in table.select("thead th")]
    rows: list[dict] = []
    for tr in table.select("tbody tr"):
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if cells:
            rows.append(dict(zip(headers, cells, strict=False)))
    return rows


if __name__ == "__main__":
    demo = (
        '<article class="product_pod"><h3><a title="Clean Code">Clean Code</a></h3>'
        '<p class="price_color">£42.00</p></article>'
    )
    print(parse_products(demo))
