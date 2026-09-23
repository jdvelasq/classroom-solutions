"""Verificaciones de los indicadores y segmentos del caso de ventas minoristas."""

import json

import pandas as pd
import pytest


DATA_FILE = "data/sales.csv"
NOTEBOOK_FILE = "notebooks/notebook.ipynb"


def prepare_sales():
    """Reconstruye las métricas que el taller desarrolla paso a paso."""
    sales = pd.read_csv(DATA_FILE)
    sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])
    sales["ReturnedAmount"] = sales["TotalAmount"].where(sales["IsReturned"].eq(1), 0)
    sales["NetAmount"] = sales["TotalAmount"] - sales["ReturnedAmount"]
    return sales


def test_01_global_kpis_reconcile_sales_returns_and_net_sales():
    """Las ventas netas no pueden omitir el valor de las devoluciones."""
    sales = prepare_sales()

    assert sales["OrderID"].nunique() == 1000
    assert sales["CustomerID"].nunique() == 428
    assert sales["TotalAmount"].sum() == pytest.approx(1_280_745.55)
    assert sales["ReturnedAmount"].sum() == pytest.approx(643_703.02)
    assert sales["NetAmount"].sum() == pytest.approx(637_042.53)
    assert sales["NetAmount"].sum() == pytest.approx(
        sales["TotalAmount"].sum() - sales["ReturnedAmount"].sum()
    )


def test_02_priority_segments_have_volume_and_return_risk():
    """La priorización combina tasa de devolución con un mínimo de 50 órdenes."""
    sales = prepare_sales()
    risk = (
        sales.groupby(["Category", "SalesChannel"])
        .agg(orders=("OrderID", "size"), return_rate=("IsReturned", "mean"))
        .reset_index()
        .query("orders >= 50")
    )

    assert risk.shape[0] == 9
    assert risk["orders"].ge(50).all()
    highest_risk = risk.loc[risk["return_rate"].idxmax()]
    assert highest_risk["Category"] == "Home & Garden"
    assert highest_risk["SalesChannel"] == "Mobile App"


def test_03_notebook_covers_kpis_trend_and_diagnostic_segments():
    """El guion guiado incluye los tres niveles analíticos del caso."""
    notebook = json.loads(open(NOTEBOOK_FILE, encoding="utf-8").read())
    source = "\n".join(
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    )

    for concept in [
        "return_rate_by_value",
        "monthly_sales",
        "category_summary",
        "return_risk",
        "minimum_orders = 50",
    ]:
        assert concept in source
