from pathlib import Path


def test_01():
    assert Path("submission/calibration_summary.csv").is_file()
    assert Path("submission/group_review.csv").is_file()
    assert Path("submission/threshold_tradeoff.csv").is_file()
