from pathlib import Path


def test_01():
    assert Path("submission/stocks.png").is_file()
