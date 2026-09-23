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

def test_arrival_order_and_delayed_event_are_preserved():
    with (ROOT/"submission/consumed_events.csv").open() as f:r=list(csv.DictReader(f))
    assert [x["event_id"] for x in r]==["E1","E2","E3","E4"] and r[2]["is_delayed"]=="True"
