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

def test_each_controlled_quality_defect_is_reported():
    report=pd.read_csv(ROOT/"submission/quality_report.csv"); assert report.dimension.tolist()==["completeness","validity","uniqueness","consistency","freshness"] and report.violations.tolist()==[1,1,1,1,1]
