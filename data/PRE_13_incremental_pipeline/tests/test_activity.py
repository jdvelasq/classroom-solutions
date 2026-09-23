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

def test_current_state_is_unique_and_contains_change_results():
    x=pd.read_parquet(ROOT/"submission/customers_current.parquet");assert x.customer_id.is_unique and x.customer_id.tolist()==["C1","C2","C3","C4"] and x.loc[x.customer_id=="C2","segment"].iloc[0]=="Corporate"
def test_checkpoint_and_change_report_are_deterministic():
    assert json.loads((ROOT/"temp/checkpoint.json").read_text())["high_water_mark"]=="2026-09-16T10:30:00"
    assert pd.read_csv(ROOT/"submission/incremental_report.csv").record_count.tolist()==[1,1,1]
