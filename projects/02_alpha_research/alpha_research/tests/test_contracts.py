def test_imports():
    import alpha_research
    from alpha_research.core.dates import parse_date_any
    assert str(parse_date_any("2026-03-09")) == "2026-03-09"
