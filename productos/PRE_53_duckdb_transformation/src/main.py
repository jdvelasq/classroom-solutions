"""Construye una tabla analítica reproducible mediante una consulta DuckDB."""

from pathlib import Path

import duckdb


ROOT_DIR = Path(__file__).resolve().parents[1]


def build_factory_totals():
    """La transformación declarada en SQL puede revisarse y repetirse sin pasos manuales."""

    query = """
        SELECT factory_id, SUM(daily_units_produced) AS total_units_produced
        FROM read_csv_auto(?)
        GROUP BY factory_id
        ORDER BY factory_id
    """
    return duckdb.execute(query, [str(ROOT_DIR / "data" / "daily_operations.csv")]).fetchall()
