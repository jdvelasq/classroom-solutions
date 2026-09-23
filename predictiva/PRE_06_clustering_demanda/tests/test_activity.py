from pathlib import Path

import pandas as pd


def test_saved_daily_patterns_are_complete_and_interpretable():
    figures = [
        Path("submission/demanda-comercial-patrones-ejemplo.png"),
        Path("submission/demanda-comercial-perfiles.png"),
        Path("submission/demanda-comercial.png"),
    ]

    for figure in figures:
        assert figure.exists()
        assert figure.stat().st_size > 0

    daily_patterns = pd.read_csv("submission/demanda-comercial-clusters.csv")
    weekday_summary = pd.read_csv("submission/demanda-comercial-dias.csv")

    assert list(daily_patterns.columns) == ["Fecha", "cluster", "day_of_week"]
    assert len(daily_patterns) == 2069
    assert daily_patterns["Fecha"].is_unique
    assert set(daily_patterns["cluster"]) == {0, 1}
    day_names = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    assert set(daily_patterns["day_of_week"]) == set(day_names)

    assert list(weekday_summary.columns) == [
        "day_of_week",
        "cluster_0_days",
        "cluster_1_days",
    ]
    assert weekday_summary["day_of_week"].tolist() == day_names
    assert weekday_summary[["cluster_0_days", "cluster_1_days"]].to_numpy().sum() == len(
        daily_patterns
    )
