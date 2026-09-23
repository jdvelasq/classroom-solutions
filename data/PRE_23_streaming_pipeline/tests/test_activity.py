import csv
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pre23", ROOT / "src/main.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def setup_module():
    MODULE.build_submission()


def test_lateness_policy_and_window_totals_are_visible():
    with (ROOT / "submission/streaming_report.csv").open() as file:
        report = dict(csv.reader(file))
    assert report["late_accepted_count"] == "1"
    assert report["too_late_count"] == "1"
    assert report["validation_status"] == "PASS"
