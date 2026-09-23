import csv
import json
import sqlite3
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook
OUTPUT = ROOT / "submission/customers_curated.csv"

def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")

def test_curated_customers_have_one_latest_version_each():
    with OUTPUT.open(newline="", encoding="utf-8") as file: rows = list(csv.DictReader(file))
    assert len(rows) == len({r["customer_id"] for r in rows}) == 8
    assert next(r for r in rows if r["customer_id"] == "C003") == {"customer_id":"C003","customer_name":"Mariana Torres","city":"Cali","segment":"Corporate","age":"41","updated_at":"2026-02-10"}


def test_semantic_cleaning_is_visible_in_output():
    with OUTPUT.open(newline="", encoding="utf-8") as file: rows = list(csv.DictReader(file))
    assert {r["segment"] for r in rows} <= {"Premium", "Corporate", "Unknown"}
    assert next(r for r in rows if r["customer_id"] == "C004")["segment"] == "Unknown"
    assert next(r for r in rows if r["customer_id"] == "C004")["age"] == "29"
