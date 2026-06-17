import sqlite3

from pws_examples.storage import Product, store_sqlite, validate


def test_validate_coerces_price_and_skips_invalid():
    rows = [{"title": "Clean Code", "price": "£42.00"}, {"title": "missing price"}]
    products = validate(rows)
    assert len(products) == 1
    assert products[0].price == 42.0


def test_store_sqlite_deduplicates_by_title():
    conn = sqlite3.connect(":memory:")
    products = [Product(title="A", price=1.0), Product(title="A", price=1.0)]
    inserted = store_sqlite(products, conn)
    assert inserted == 1
    count = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    assert count == 1
