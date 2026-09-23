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

def test_formats_preserve_the_same_logical_rows():
    csv = pd.read_csv(ROOT / "data/sales.csv"); parquet = pd.read_parquet(ROOT / "data/sales.parquet", engine="pyarrow")
    assert len(csv) == len(parquet) == 2000
    assert list(csv.columns) == list(parquet.columns)


def test_comparison_declares_three_formats():
    result = pd.read_csv(ROOT / "submission/format_comparison.csv")
    assert list(result["format"]) == ["CSV", "JSON", "Parquet"]
