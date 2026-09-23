import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_contract_distinguishes_breaking_and_compatible_changes():
    report = pd.read_csv(ROOT / "submission/contract_report.csv").set_index(
        "batch_name"
    )
    assert report.loc["missing_income_group"].tolist() == ["FAIL", "BREAKING", "REJECT"]
    assert report.loc["wrong_state"].tolist() == ["FAIL", "BREAKING", "REJECT"]
    assert report.loc["optional_column"].tolist() == ["PASS", "COMPATIBLE", "ACCEPT"]
