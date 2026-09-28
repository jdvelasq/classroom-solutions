from pathlib import Path


def test_01():
    assert Path("submission/base_estimator.pkl").is_file()
    assert Path("submission/flexible_estimator.pkl").is_file()
    assert Path("submission/metrics.json").is_file()
    assert Path("submission/model_comparison.csv").is_file()
