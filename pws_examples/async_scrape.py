"""Asynchronous scraping with asyncio + HTTPX, bounded by a semaphore.

Companion code for:
- https://python-web-scraping.com/scaling-python-web-scrapers/asynchronous-scraping-with-asyncio-and-httpx/
"""

from __future__ import annotations

import asyncio

import httpx


async def _fetch(client: httpx.AsyncClient, url: str, semaphore: asyncio.Semaphore) -> str | None:
    async with semaphore:
        try:
            response = await client.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except httpx.HTTPError:
            return None


async def scrape(
    urls: list[str],
    concurrency: int = 5,
    transport: httpx.AsyncBaseTransport | None = None,
) -> list[str | None]:
    """Fetch many URLs concurrently, capping in-flight requests with a semaphore.

    Failed requests come back as ``None`` rather than cancelling the batch. The
    ``transport`` parameter lets tests inject ``httpx.MockTransport`` for
    deterministic, offline runs.
    """
    semaphore = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient(transport=transport) as client:
        tasks = [_fetch(client, url, semaphore) for url in urls]
        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    targets = [f"https://books.toscrape.com/catalogue/page-{i}.html" for i in range(1, 4)]
    pages = asyncio.run(scrape(targets))
    print("fetched:", sum(page is not None for page in pages))
