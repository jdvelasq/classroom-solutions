from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01():
    assert (ACTIVITY_DIR / "submission" / "record_v2.json").is_file()
