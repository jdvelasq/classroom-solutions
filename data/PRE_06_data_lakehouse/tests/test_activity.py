import csv
import json
import sqlite3
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")

def test_partitioned_rows_match_history_and_selected_partition_is_correct():
    original = pd.read_parquet(ROOT / "data/sales_history.parquet", engine="pyarrow")
    january = pd.read_parquet(ROOT / "temp/lake/curated/sales/year=2026/month=01/sales.parquet", engine="pyarrow")
    assert len(original) == 40
    assert january.transaction_date.str.startswith("2026-01").all()


def test_summary_describes_partitioned_sales():
    summary = pd.read_csv(ROOT / "submission/lake_summary.csv")
    assert summary.iloc[0].to_dict() == {"dataset":"sales", "partition_columns":"year,month", "partition_count":4, "file_count":4, "row_count":40}
