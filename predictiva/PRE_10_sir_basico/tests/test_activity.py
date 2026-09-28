from pathlib import Path


def test_01():
    assert Path("submission/expected_evolution.png").is_file()
    assert Path("submission/fit_comparison.csv").is_file()
    assert Path("submission/forecasts.csv").is_file()
    assert Path("submission/model_assumptions.json").is_file()
    assert Path("submission/scenario_peaks.csv").is_file()
