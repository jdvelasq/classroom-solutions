"""Construye una tabla analítica reproducible mediante una consulta DuckDB."""

import json
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


def main():
    """La tabla calculada queda disponible para revisar la transformación."""

    output_path = ROOT_DIR / "submission" / "factory_totals.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps({"factory_totals": [list(row) for row in build_factory_totals()]}, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
