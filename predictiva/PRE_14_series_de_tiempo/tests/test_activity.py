from pathlib import Path


def test_01():
    assert Path("submission/forecasts.csv").is_file()
    assert Path("submission/metrics.csv").is_file()
