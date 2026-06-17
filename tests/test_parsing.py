from pws_examples.parsing import extract_table, parse_products

PRODUCTS_HTML = """
<article class="product_pod"><h3><a title="Clean Code">Clean Code</a></h3>
<p class="price_color">£42.00</p></article>
<article class="product_pod"><h3><a title="The Pragmatic Programmer">PP</a></h3>
<p class="price_color">£35.50</p></article>
"""

TABLE_HTML = """
<table>
  <thead><tr><th>Name</th><th>Role</th></tr></thead>
  <tbody>
    <tr><td>Ada</td><td>Engineer</td></tr>
    <tr><td>Linus</td><td>Maintainer</td></tr>
  </tbody>
</table>
"""


def test_parse_products_extracts_all_cards():
    products = parse_products(PRODUCTS_HTML)
    assert len(products) == 2
    assert products[0] == {"title": "Clean Code", "price": "£42.00"}


def test_parse_products_handles_empty_html():
    assert parse_products("<div>nothing here</div>") == []


def test_extract_table_maps_headers_to_cells():
    rows = extract_table(TABLE_HTML)
    assert rows == [
        {"Name": "Ada", "Role": "Engineer"},
        {"Name": "Linus", "Role": "Maintainer"},
    ]


def test_extract_table_returns_empty_when_no_table():
    assert extract_table("<p>no table</p>") == []
