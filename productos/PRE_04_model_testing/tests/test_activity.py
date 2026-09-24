from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = ACTIVITY_DIR / "submission" / "model_test_report.json"


def test_model_test_report_exists():
    assert REPORT_PATH.is_file()
    assert REPORT_PATH.stat().st_size > 0
