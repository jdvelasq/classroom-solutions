from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def test_01():
    assert (ACTIVITY_DIR / "submission" / "model_registry/production/model.pkl").is_file()
    assert (ACTIVITY_DIR / "submission" / "model_registry/production/registry.json").is_file()
