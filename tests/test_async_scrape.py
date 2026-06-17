import asyncio

import httpx

from pws_examples.async_scrape import scrape


def test_scrape_fetches_all_urls_with_mock_transport():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, text=f"<html>{request.url.path}</html>")

    transport = httpx.MockTransport(handler)
    urls = ["https://x.test/a", "https://x.test/b", "https://x.test/c"]
    results = asyncio.run(scrape(urls, transport=transport))
    assert len(results) == 3
    assert all(body and "html" in body for body in results)


def test_scrape_returns_none_for_failed_requests():
    transport = httpx.MockTransport(lambda request: httpx.Response(500))
    results = asyncio.run(scrape(["https://x.test/fail"], transport=transport))
    assert results == [None]
