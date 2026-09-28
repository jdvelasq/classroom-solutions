from pathlib import Path


def test_01():
    assert Path("submission/coverage_summary.csv").is_file()
    assert Path("submission/nearest_neighbors.csv").is_file()
    assert Path("submission/recommendations.csv").is_file()
