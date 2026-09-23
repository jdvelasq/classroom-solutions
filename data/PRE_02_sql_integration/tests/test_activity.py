import csv
import json
import sqlite3
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))
from notebook_runner import execute_notebook
DATABASE, OUTPUT = ROOT / "data/sales.db", ROOT / "submission/customer_sales.csv"

def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")

def test_customer_sales_has_the_required_grain_and_columns():
    with OUTPUT.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    assert list(rows[0]) == ["customer_id", "customer_name", "customer_city", "number_of_orders", "total_units", "total_sales"]
    assert [row["customer_id"] for row in rows] == ["C001", "C002", "C003", "C004"]
    assert len({row["customer_id"] for row in rows}) == len(rows)


def test_sales_and_distinct_orders_reconcile_with_source_lines():
    with sqlite3.connect(DATABASE) as db, OUTPUT.open(newline="", encoding="utf-8") as file:
        output = list(csv.DictReader(file))
        total = db.execute("SELECT SUM(i.quantity * p.unit_price) FROM order_items i JOIN products p USING(product_id)").fetchone()[0]
        assert sum(float(row["total_sales"]) for row in output) == total
        assert next(row for row in output if row["customer_id"] == "C001")["number_of_orders"] == "2"
