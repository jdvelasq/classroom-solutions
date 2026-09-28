from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01():
    assert (ACTIVITY_DIR / "submission" / "production/model.pkl").is_file()
    assert (ACTIVITY_DIR / "submission" / "production/rollback_record.json").is_file()
