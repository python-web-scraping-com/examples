from pws_examples.extraction import extract_contacts


def test_extract_contacts_finds_emails_and_phone():
    text = "Email info@python-web-scraping.com or sales@example.org, call +1 (555) 123-4567."
    result = extract_contacts(text)
    assert "info@python-web-scraping.com" in result["emails"]
    assert "sales@example.org" in result["emails"]
    assert len(result["phones"]) == 1


def test_extract_contacts_deduplicates_and_sorts():
    assert extract_contacts("b@x.com a@x.com a@x.com")["emails"] == ["a@x.com", "b@x.com"]


def test_extract_contacts_empty():
    assert extract_contacts("no contacts here") == {"emails": [], "phones": []}
