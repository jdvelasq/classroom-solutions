from pathlib import Path


def test_01():
    assert Path("submission/adaptive_evolution.png").is_file()
    assert Path("submission/forecasts.csv").is_file()
    assert Path("submission/infection_rate_forecast.csv").is_file()
