import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_course_table_has_one_row_per_course_and_valid_aggregates():
    output = pd.read_csv(ROOT / "submission/course_ratings.csv")
    assert len(output) == 100
    assert output.course_id.is_unique
    assert output.average_rating.between(0, 5).all()


def test_transformation_reconciles_all_source_ratings():
    output = pd.read_csv(ROOT / "submission/course_ratings.csv")
    assert output.rating_count.sum() == 59172
    assert set(output.columns) == {"course_id", "title", "programming_language", "rating_count", "average_rating"}
