"""Pruebas del laboratorio de diagnóstico de entregas."""

from pathlib import Path

import pandas as pd
import pytest

from ..src.pregunta_01 import diagnose_deliveries


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_generates_the_required_delivery_diagnostics():
    """Genera los tres entregables persistentes solicitados."""
    diagnose_deliveries()

    for filename in [
        "overall_delivery_kpis.csv",
        "shipment_mode_summary.csv",
        "priority_segments.csv",
    ]:
        assert (SUBMISSION_DIR / filename).exists()


def test_overall_kpis_measure_compliance_and_exposure():
    """Calcula el cumplimiento y el valor expuesto a demora."""
    overall = pd.read_csv(SUBMISSION_DIR / "overall_delivery_kpis.csv")

    assert overall.columns.tolist() == [
        "shipments",
        "line_item_value_usd",
        "on_time_rate",
        "median_days_vs_schedule",
        "late_value_usd",
    ]
    assert overall.shape == (1, 5)
    assert overall.loc[0, "shipments"] == 10324
    assert overall.loc[0, "line_item_value_usd"] == pytest.approx(1627584457.29)
    assert overall.loc[0, "on_time_rate"] == pytest.approx(0.8851220457)
    assert overall.loc[0, "median_days_vs_schedule"] == 0
    assert overall.loc[0, "late_value_usd"] == pytest.approx(259034270.94)


def test_mode_summary_keeps_volume_time_and_value_together():
    """Compara modos de envío sin perder volumen, demora ni exposición."""
    modes = pd.read_csv(SUBMISSION_DIR / "shipment_mode_summary.csv")

    assert modes.columns.tolist() == [
        "Shipment Mode",
        "shipments",
        "on_time_rate",
        "avg_days_vs_schedule",
        "line_item_value_usd",
        "late_value_usd",
    ]
    assert modes["Shipment Mode"].iloc[:4].tolist() == [
        "Ocean",
        "Truck",
        "Air Charter",
        "Air",
    ]
    assert pd.isna(modes["Shipment Mode"].iloc[4])
    assert modes["on_time_rate"].is_monotonic_increasing
    assert modes["shipments"].sum() == 10324
    assert modes.loc[modes["Shipment Mode"].eq("Truck"), "late_value_usd"].iloc[0] == pytest.approx(
        142838225.95
    )


def test_priority_segments_apply_a_volume_threshold_and_rank_exposure():
    """Prioriza países y modos con suficiente volumen por valor tardío."""
    priorities = pd.read_csv(SUBMISSION_DIR / "priority_segments.csv")

    assert priorities.columns.tolist() == [
        "Country",
        "Shipment Mode",
        "shipments",
        "on_time_rate",
        "late_value_usd",
    ]
    assert priorities.shape == (10, 5)
    assert priorities["shipments"].ge(30).all()
    assert priorities["late_value_usd"].is_monotonic_decreasing
    assert list(zip(priorities["Country"], priorities["Shipment Mode"])) == [
        ("Mozambique", "Truck"),
        ("Zambia", "Truck"),
        ("Nigeria", "Air Charter"),
        ("Nigeria", "Air"),
        ("South Africa", "Ocean"),
        ("Tanzania", "Truck"),
        ("Zimbabwe", "Truck"),
        ("Côte d'Ivoire", "Truck"),
        ("Uganda", "Truck"),
        ("South Africa", "Air"),
    ]
    assert priorities.iloc[0]["late_value_usd"] == pytest.approx(51421328.26)
