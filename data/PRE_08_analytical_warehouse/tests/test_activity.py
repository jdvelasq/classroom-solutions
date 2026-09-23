import csv
import json
import sqlite3
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook
MART, SOURCE = ROOT / "submission/sales_mart.db", ROOT / "data/sales_operational.db"

def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")

def test_fact_grain_and_sales_reconcile_with_operational_source():
    with sqlite3.connect(SOURCE) as source, sqlite3.connect(MART) as mart:
        source_rows = source.execute("SELECT COUNT(*) FROM order_items").fetchone()[0]
        source_sales = source.execute("SELECT SUM(i.quantity*p.unit_price) FROM order_items i JOIN products p USING(product_id)").fetchone()[0]
        assert mart.execute("SELECT COUNT(*) FROM fact_sales").fetchone()[0] == source_rows
        assert mart.execute("SELECT SUM(sales_amount) FROM fact_sales").fetchone()[0] == source_sales


def test_star_schema_has_valid_dimension_references():
    with sqlite3.connect(MART) as mart:
        tables = {r[0] for r in mart.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        assert tables == {"dim_customer", "dim_product", "dim_date", "fact_sales"}
        invalid = mart.execute("SELECT COUNT(*) FROM fact_sales f LEFT JOIN dim_customer c USING(customer_key) LEFT JOIN dim_product p USING(product_key) LEFT JOIN dim_date d USING(date_key) WHERE c.customer_key IS NULL OR p.product_key IS NULL OR d.date_key IS NULL").fetchone()[0]
        assert invalid == 0
