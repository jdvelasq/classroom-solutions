"""Pruebas del laboratorio de análisis de vuelos."""

from pathlib import Path

import pandas as pd
import pytest

from ..src.pregunta_01 import analyze_flights


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_generates_the_four_required_deliverables():
    """Genera todos los resultados persistentes del diagnóstico."""
    analyze_flights()

    for filename in [
        "overall_kpis.csv",
        "monthly_national_kpis.csv",
        "carrier_summary.csv",
        "priority_segments.csv",
    ]:
        assert (SUBMISSION_DIR / filename).exists()


def test_overall_kpis_use_the_correct_denominators():
    """Distingue vuelos programados de vuelos operados al calcular tasas."""
    overall = pd.read_csv(SUBMISSION_DIR / "overall_kpis.csv")

    assert overall.shape == (1, 8)
    assert overall.columns.tolist() == [
        "scheduled_flights",
        "cancelled_flights",
        "operated_flights",
        "delayed_departure_15_flights",
        "positive_departure_delay_minutes",
        "cancellation_rate",
        "delay_rate",
        "mean_positive_delay_minutes",
    ]
    assert overall.loc[0, "scheduled_flights"] == 21607106
    assert overall.loc[0, "cancelled_flights"] == 420175
    assert overall.loc[0, "operated_flights"] == 21186931
    assert overall.loc[0, "delay_rate"] == pytest.approx(0.2041330573)
    assert overall.loc[0, "cancellation_rate"] == pytest.approx(0.0194461489)
    assert overall.loc[0, "mean_positive_delay_minutes"] == pytest.approx(12.7886029364)


def test_monthly_kpis_preserve_the_time_series_grain():
    """Resume los 36 meses observados y conserva su orden cronológico."""
    monthly = pd.read_csv(SUBMISSION_DIR / "monthly_national_kpis.csv")

    assert monthly.shape == (36, 10)
    assert monthly[["year", "month"]].iloc[0].tolist() == [2006, 1]
    assert monthly[["year", "month"]].iloc[-1].tolist() == [2008, 12]
    peak = monthly.loc[monthly["delay_rate"].idxmax()]
    assert [peak["year"], peak["month"]] == [2007, 12]
    assert peak["delay_rate"] == pytest.approx(0.2849697728)


def test_carrier_summary_retains_volume_and_rates():
    """Permite comparar aerolíneas sin ocultar el volumen operativo."""
    carriers = pd.read_csv(SUBMISSION_DIR / "carrier_summary.csv")

    assert carriers.shape == (21, 9)
    assert carriers["delay_rate"].is_monotonic_decreasing
    assert carriers.iloc[0]["reporting_airline"] == "EV"
    assert carriers.iloc[0]["operated_flights"] == 819223
    assert carriers.iloc[0]["delay_rate"] == pytest.approx(0.2815950459)
    assert carriers["operated_flights"].sum() == 21186931


def test_priority_segments_combine_rate_with_minimum_volume():
    """Identifica diez segmentos de alto retraso con base operacional suficiente."""
    priorities = pd.read_csv(SUBMISSION_DIR / "priority_segments.csv")

    assert priorities.shape == (10, 11)
    assert priorities["operated_flights"].ge(25_000).all()
    assert priorities["delay_rate"].is_monotonic_decreasing
    assert list(
        zip(
            priorities["reporting_airline"],
            priorities["day_of_week"],
            priorities["scheduled_departure_hour"],
        )
    ) == [
        ("WN", 5, 20),
        ("WN", 5, 19),
        ("WN", 4, 20),
        ("WN", 4, 19),
        ("WN", 5, 18),
        ("WN", 5, 17),
        ("WN", 4, 18),
        ("WN", 7, 20),
        ("WN", 5, 16),
        ("WN", 7, 19),
    ]
    assert priorities.iloc[0]["delay_rate"] == pytest.approx(0.4505962814)
