import csv
import json
import sqlite3
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")

def test_catalog_has_variable_document_shapes():
    products = json.loads((ROOT / "data/products.json").read_text())
    assert {p["category"] for p in products} == {"Laptop", "Shoe", "Book"}
    assert {tuple(sorted(p["attributes"])) for p in products} == {("processor", "ram_gb", "storage_gb"), ("color", "material", "size"), ("author", "isbn", "pages")}


def test_comparison_covers_required_decisions():
    with (ROOT / "submission/model_comparison.csv").open(newline="", encoding="utf-8") as file: rows = list(csv.DictReader(file))
    assert [r["criterion"] for r in rows] == ["fixed_schema", "nested_data", "variable_attributes", "relationships", "duplication", "updates", "analytical_integration"]
