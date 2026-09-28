from pathlib import Path


def test_01():
    assert Path("submission/estimator.pkl").is_file()
    assert Path("submission/metrics.json").is_file()
