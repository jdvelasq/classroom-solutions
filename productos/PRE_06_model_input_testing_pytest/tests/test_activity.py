from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = ACTIVITY_DIR / "submission" / "input_distribution_report.json"


def test_input_distribution_report_exists():
    assert REPORT_PATH.is_file()
    assert REPORT_PATH.stat().st_size > 0
