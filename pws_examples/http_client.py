"""A resilient HTTP session with retries and exponential backoff.

Companion code for:
- https://python-web-scraping.com/the-complete-guide-to-python-web-scraping/understanding-http-requests-and-responses/
"""

from __future__ import annotations

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (compatible; pws-examples/1.0; +https://python-web-scraping.com)"
)


def build_session(retries: int = 3, backoff_factor: float = 1.0) -> requests.Session:
    """Create a ``requests.Session`` that retries transient failures politely.

    Retries ``429`` and ``5xx`` responses on idempotent methods with exponential
    backoff, and sets a transparent, identifying User-Agent.
    """
    session = requests.Session()
    retry = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({"User-Agent": DEFAULT_USER_AGENT})
    return session


if __name__ == "__main__":
    session = build_session()
    adapter = session.get_adapter("https://example.com")
    print("Session ready, total retries:", adapter.max_retries.total)
