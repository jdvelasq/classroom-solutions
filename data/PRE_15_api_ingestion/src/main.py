"""Ingiere una respuesta congelada de GitHub como si fuera una página de API."""

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parents[1]
SOURCE = ROOT / "data/github_issues_page_1.json"
OUTPUT = ROOT / "submission/github_issues.parquet"
REPORT = ROOT / "submission/api_ingestion_report.csv"


def request_page(attempt):
    """Representa una llamada recuperable; el segundo intento lee el snapshot local."""
    if attempt == 1:
        return 503, None
    return 200, json.loads(SOURCE.read_text(encoding="utf-8"))


def build_submission():
    retries = 0
    for attempt in range(1, 4):
        status, issues = request_page(attempt)
        if status == 200:
            break
        retries += 1
    else:
        raise RuntimeError("La API no se recuperó")
    frame = pd.DataFrame(
        [
            {
                "issue_id": issue["id"],
                "issue_number": issue["number"],
                "title": issue["title"],
                "state": issue["state"],
                "created_at": issue["created_at"],
                "closed_at": issue["closed_at"],
                "comment_count": issue["comments"],
                "is_pull_request": "pull_request" in issue,
            }
            for issue in issues
        ]
    )
    assert frame.issue_id.is_unique
    frame.to_parquet(OUTPUT, index=False)
    pd.DataFrame(
        [("github_issues", 1, len(frame), retries, "SUCCESS", str(OUTPUT))],
        columns=[
            "source_name",
            "pages_requested",
            "records_retrieved",
            "retry_count",
            "status",
            "output_path",
        ],
    ).to_csv(REPORT, index=False)


if __name__ == "__main__":
    build_submission()
