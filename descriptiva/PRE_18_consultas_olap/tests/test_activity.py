"""Verificaciones del taller de consultas OLAP."""

import sqlite3

import nbformat
import pandas as pd
import pytest


def test_olap_rollup_reconciles_with_the_mart_total():
    monthly_region = pd.read_csv("submission/monthly_region_sales.csv")
    with sqlite3.connect("data/sales_mart.db") as connection:
        total = connection.execute("SELECT SUM(net_sales) FROM fact_sales").fetchone()[0]

    assert monthly_region["net_sales"].sum() == pytest.approx(total)
    assert not monthly_region[["year", "month", "region"]].duplicated().any()


def test_notebook_contains_rollup_slice_and_drilldown():
    notebook = nbformat.read("notebooks/notebook.ipynb", as_version=4)
    source = "\n".join(cell.source for cell in notebook.cells)

    for concept in ["monthly_region", "north_category", "product_drilldown"]:
        assert concept in source
