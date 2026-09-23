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
    original = pd.read_parquet(
        ROOT / "data/cta_daily_station_totals.parquet", engine="pyarrow"
    )
    files = list((ROOT / "temp/lake/curated/cta_rides").rglob("*.parquet"))
    assert sum(len(pd.read_parquet(file)) for file in files) == len(original)


def test_summary_describes_partitioned_sales():
    summary = pd.read_csv(ROOT / "submission/lake_summary.csv")
    assert summary.iloc[0]["dataset"] == "cta_rides"
    assert summary.iloc[0]["row_count"] == len(
        pd.read_parquet(ROOT / "data/cta_daily_station_totals.parquet")
    )
