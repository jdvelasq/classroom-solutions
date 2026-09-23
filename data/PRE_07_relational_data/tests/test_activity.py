import sqlite3
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / "tests"))
from notebook_runner import execute_notebook

OUTPUT = ROOT / "submission/museum_collection.db"
SOURCE = ROOT / "data/museum_collection.csv"


def setup_module():
    execute_notebook(ROOT / "notebooks/notebook.ipynb")


def test_database_preserves_the_grain_of_the_source_extract():
    raw = pd.read_csv(SOURCE)
    with sqlite3.connect(OUTPUT) as connection:
        tables = {
            row[0]
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
        }
        assert tables == {
            "categories",
            "artworks",
            "creators",
            "artwork_creators",
            "citations",
        }
        assert (
            connection.execute("SELECT COUNT(*) FROM artworks").fetchone()[0]
            == raw.itemid.nunique()
        )
        expected_citations = (
            raw.dropna(subset=["citation"])[["itemid", "citation"]]
            .drop_duplicates()
            .shape[0]
        )
        assert (
            connection.execute("SELECT COUNT(*) FROM citations").fetchone()[0]
            == expected_citations
        )


def test_many_to_many_creator_relationship_has_valid_references():
    with sqlite3.connect(OUTPUT) as connection:
        invalid = connection.execute(
            """
            SELECT COUNT(*) FROM artwork_creators ac
            LEFT JOIN artworks a USING(artwork_id)
            LEFT JOIN creators c USING(creator_id)
            WHERE a.artwork_id IS NULL OR c.creator_id IS NULL
        """
        ).fetchone()[0]
        assert invalid == 0
        assert (
            connection.execute("SELECT COUNT(*) FROM artwork_creators").fetchone()[0]
            > 0
        )
