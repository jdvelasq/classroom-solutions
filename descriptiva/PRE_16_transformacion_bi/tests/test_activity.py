"""Verificaciones del taller de transformación para BI."""

import nbformat
import pandas as pd
import pytest


def test_publishes_one_analytical_row_per_order_line():
    source = pd.read_csv("data/order_lines.csv")
    sales = pd.read_csv("submission/sales_analytics.csv")

    assert len(sales) == len(source)
    assert not sales[["order_id", "line_id"]].duplicated().any()
    assert sales["net_sales"].sum() == pytest.approx(
        (sales["gross_sales"] - sales["discount_amount"]).sum()
    )


def test_notebook_keeps_the_grain_and_reconciliation_visible():
    notebook = nbformat.read("notebooks/notebook.ipynb", as_version=4)
    source = "\n".join(cell.source for cell in notebook.cells)

    assert all(cell.cell_type == "code" for cell in notebook.cells)
    assert "validate=\"many_to_one\"" in source
    assert "sales_analytics.csv" in source
