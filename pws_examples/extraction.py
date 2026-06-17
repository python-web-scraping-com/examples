"""Text extraction with regular expressions.

Companion code for:
- https://python-web-scraping.com/the-complete-guide-to-python-web-scraping/extracting-data-with-regular-expressions/
"""

from __future__ import annotations

import re

EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_RE = re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")


def extract_contacts(text: str) -> dict[str, list[str]]:
    """Return de-duplicated, sorted emails and phone numbers found in free text."""
    emails = sorted(set(EMAIL_RE.findall(text)))
    phones = sorted(set(PHONE_RE.findall(text)))
    return {"emails": emails, "phones": phones}


if __name__ == "__main__":
    print(extract_contacts("Reach us at info@python-web-scraping.com or +1 (555) 123-4567."))
