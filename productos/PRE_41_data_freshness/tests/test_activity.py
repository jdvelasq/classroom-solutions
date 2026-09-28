from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01():
    assert (ACTIVITY_DIR / "submission" / "freshness_report.json").is_file()
