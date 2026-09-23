import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_lateness_policy_and_window_totals_are_visible():
    with (ROOT / "submission/streaming_report.csv").open() as file:
        report = dict(csv.reader(file))
    assert report["late_accepted_count"] == "1"
    assert report["too_late_count"] == "1"
    assert report["validation_status"] == "PASS"
