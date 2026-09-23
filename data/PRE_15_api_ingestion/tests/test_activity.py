import importlib.util
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("pre15", ROOT / "src/main.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

def setup_module(): MODULE.build_submission()

def test_snapshot_is_complete_and_has_unique_github_issues():
    issues = pd.read_parquet(ROOT / "submission/github_issues.parquet")
    assert len(issues) == 20 and issues.issue_id.is_unique
    assert {"issue_id", "issue_number", "title", "state", "comment_count"} <= set(issues.columns)

def test_transient_failure_is_reported_as_one_retry():
    report = pd.read_csv(ROOT / "submission/api_ingestion_report.csv")
    assert report.loc[0, "retry_count"] == 1
    assert report.loc[0, "status"] == "SUCCESS"
