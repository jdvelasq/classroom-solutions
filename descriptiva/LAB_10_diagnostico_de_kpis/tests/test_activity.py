"""Pruebas de la actividad de diagnóstico de KPIs."""

from pathlib import Path

import pandas as pd
import pytest

from ..src.pregunta_01 import diagnose_kpis


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_generates_all_required_deliverables():
    """Genera los tres archivos de diagnóstico solicitados."""
    diagnose_kpis()

    for filename in [
        "kpi_summary.csv",
        "category_summary.csv",
        "priority_segments.csv",
    ]:
        assert (SUBMISSION_DIR / filename).exists()


def test_global_kpis_measure_gross_returns_and_net_sales():
    """Calcula los KPIs globales con denominadores explícitos."""
    kpis = pd.read_csv(SUBMISSION_DIR / "kpi_summary.csv")

    assert kpis.columns.tolist() == [
        "orders",
        "customers",
        "gross_sales",
        "returned_amount",
        "net_sales",
        "return_rate_by_orders",
        "return_rate_by_value",
        "net_sales_per_order",
    ]
    assert kpis.shape == (1, 8)
    assert kpis.loc[0, "orders"] == 1000
    assert kpis.loc[0, "customers"] == 428
    assert kpis.loc[0, ["gross_sales", "returned_amount", "net_sales"]].tolist() == pytest.approx(
        [1280745.55, 643703.02, 637042.53]
    )
    assert kpis.loc[0, "gross_sales"] - kpis.loc[0, "returned_amount"] == pytest.approx(
        kpis.loc[0, "net_sales"]
    )
    assert kpis.loc[0, "return_rate_by_orders"] == pytest.approx(0.516)
    assert kpis.loc[0, "return_rate_by_value"] == pytest.approx(0.5026002394)


def test_category_summary_explains_the_global_kpis():
    """Desagrega los KPIs por categoría sin perder el total."""
    categories = pd.read_csv(SUBMISSION_DIR / "category_summary.csv")

    assert categories.columns.tolist() == [
        "Category",
        "orders",
        "gross_sales",
        "returned_amount",
        "net_sales",
        "return_rate",
    ]
    assert categories["Category"].tolist() == ["Fashion", "Electronics", "Home & Garden"]
    assert categories["net_sales"].tolist() == pytest.approx(
        [225430.13, 214153.75, 197458.65]
    )
    assert categories["orders"].sum() == 1000
    assert categories["returned_amount"].sum() == pytest.approx(643703.02)


def test_priority_segments_focus_on_value_and_have_sufficient_volume():
    """Prioriza segmentos comparables por impacto monetario y volumen."""
    priorities = pd.read_csv(SUBMISSION_DIR / "priority_segments.csv")

    assert priorities.columns.tolist() == [
        "Category",
        "SalesChannel",
        "orders",
        "gross_sales",
        "returned_amount",
        "return_rate",
    ]
    assert priorities.shape == (5, 6)
    assert priorities["orders"].ge(50).all()
    assert priorities["returned_amount"].is_monotonic_decreasing
    assert list(zip(priorities["Category"], priorities["SalesChannel"])) == [
        ("Fashion", "Mobile App"),
        ("Fashion", "Website"),
        ("Electronics", "Mobile App"),
        ("Electronics", "In-Store"),
        ("Home & Garden", "Mobile App"),
    ]
    assert priorities["returned_amount"].tolist() == pytest.approx(
        [87672.87, 83604.72, 78806.27, 74284.36, 73969.23]
    )
