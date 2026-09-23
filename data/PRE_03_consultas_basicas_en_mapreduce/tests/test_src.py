"""Pruebas de las consultas básicas por clave--valor."""

import csv

from ..src.main import SUBMISSION_DIR, run


def test_materializes_the_five_queries():
    run()
    assert {path.name for path in SUBMISSION_DIR.glob("query_*.csv")} == {
        "query_1_tip_rates.csv",
        "query_2_dinner.csv",
        "query_3_dinner_large_tip.csv",
        "query_4_large_party.csv",
        "query_5_count_by_sex.csv",
    }


def test_group_by_sex_uses_key_value_aggregation():
    run()
    with (SUBMISSION_DIR / "query_5_count_by_sex.csv").open(encoding="utf-8") as file:
        counts = {row["sex"]: int(row["count"]) for row in csv.DictReader(file)}
    assert counts == {"Female": 87, "Male": 157}
