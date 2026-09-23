import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_course_documents_embed_the_analytics_read_model():
    documents = json.loads((ROOT / "submission/course_documents.json").read_text())
    assert len(documents) == 100
    assert {"course_id", "title", "programming_language", "analytics_summary"} <= set(
        documents[0]
    )
    assert sum(x["analytics_summary"]["rating_count"] for x in documents) == 59172
