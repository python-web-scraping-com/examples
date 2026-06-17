"""Validate scraped records and store them, de-duplicated, in SQLite.

Companion code for:
- https://python-web-scraping.com/scaling-python-web-scrapers/storing-and-exporting-scraped-data/
"""

from __future__ import annotations

import sqlite3

from pydantic import BaseModel, ValidationError, field_validator


class Product(BaseModel):
    """A validated product record. ``price`` is coerced from strings like '£42.00'."""

    title: str
    price: float
    in_stock: bool = True

    @field_validator("price", mode="before")
    @classmethod
    def _clean_price(cls, value: object) -> float:
        return float(str(value).replace("£", "").replace("$", "").strip())


def validate(rows: list[dict]) -> list[Product]:
    """Validate raw dict rows into ``Product`` models, skipping malformed ones."""
    products: list[Product] = []
    for row in rows:
        try:
            products.append(Product(**row))
        except ValidationError:
            continue
    return products


def store_sqlite(products: list[Product], conn: sqlite3.Connection) -> int:
    """Create the table if needed and insert, de-duplicating by title.

    Returns the number of rows actually inserted.
    """
    conn.execute(
        "CREATE TABLE IF NOT EXISTS products ("
        "title TEXT UNIQUE, price REAL, in_stock INTEGER)"
    )
    before = conn.total_changes
    conn.executemany(
        "INSERT OR IGNORE INTO products (title, price, in_stock) VALUES (?, ?, ?)",
        [(p.title, p.price, int(p.in_stock)) for p in products],
    )
    conn.commit()
    return conn.total_changes - before


if __name__ == "__main__":
    connection = sqlite3.connect(":memory:")
    records = validate([{"title": "Clean Code", "price": "£42.00"}, {"title": "no price"}])
    print("stored:", store_sqlite(records, connection))
