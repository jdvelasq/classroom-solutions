from pathlib import Path


def test_01():
    assert Path("submission/clf.pkl").is_file()
    assert Path("submission/metrics.json").is_file()
    assert Path("submission/vectorizer.pkl").is_file()
