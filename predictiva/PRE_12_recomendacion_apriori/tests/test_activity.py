from pathlib import Path


def test_01():
    assert Path("submission/association_rules.csv").is_file()
    assert Path("submission/recommendations.csv").is_file()
    assert Path("submission/top_items.csv").is_file()
