"""Verificaciones del taller de mart analítico."""

import sqlite3

import nbformat
import pandas as pd


def test_mart_preserves_the_fact_grain_and_dimensions():
    source = pd.read_csv("data/order_lines.csv")
    with sqlite3.connect("submission/sales_mart.db") as connection:
        fact = pd.read_sql_query("SELECT * FROM fact_sales", connection)
        tables = pd.read_sql_query(
            "SELECT name FROM sqlite_master WHERE type='table'", connection
        )["name"].tolist()

    assert len(fact) == len(source)
    assert not fact[["order_id", "line_id"]].duplicated().any()
    assert {"fact_sales", "dim_date", "dim_customer", "dim_product"}.issubset(tables)


def test_notebook_makes_fact_and_dimension_design_explicit():
    notebook = nbformat.read("notebooks/notebook.ipynb", as_version=4)
    source = "\n".join(cell.source for cell in notebook.cells)

    assert all(cell.cell_type == "code" for cell in notebook.cells)
    assert "fact_sales" in source
    assert "dim_date" in source
