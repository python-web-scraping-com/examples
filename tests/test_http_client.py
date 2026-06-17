from pws_examples.http_client import build_session


def test_build_session_configures_retries():
    session = build_session(retries=5)
    adapter = session.get_adapter("https://example.com")
    assert adapter.max_retries.total == 5
    assert 429 in adapter.max_retries.status_forcelist


def test_build_session_sets_identifying_user_agent():
    session = build_session()
    assert "pws-examples" in session.headers["User-Agent"]
