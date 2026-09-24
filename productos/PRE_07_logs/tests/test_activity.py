from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
LOG_PATH = ACTIVITY_DIR / "submission" / "pipeline.log"


def test_pipeline_log_exists():
    assert LOG_PATH.is_file()
    assert LOG_PATH.stat().st_size > 0
