import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook

def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")

def test_quality_report_distinguishes_valid_data_from_scope_risk():
    report = pd.read_csv(ROOT / "submission/quality_report.csv").set_index("rule_name")
    assert report.loc["income_group_domain", "status"] == "PASS"
    assert report.loc["postal_income_key_unique", "violations"] == 0
    assert report.loc["statewide_total_separated"].tolist() == ["scope", 6, "FAIL"]
