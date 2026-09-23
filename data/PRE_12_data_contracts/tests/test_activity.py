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

def test_contract_distinguishes_breaking_and_compatible_changes():
    r=pd.read_csv(ROOT/"submission/contract_report.csv").set_index("batch_name")
    assert r.loc["missing_segment"].tolist()==["FAIL","BREAKING","REJECT"]
    assert r.loc["optional_column"].tolist()==["PASS","COMPATIBLE","ACCEPT"]
