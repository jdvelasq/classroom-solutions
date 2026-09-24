"""Verifica que el proyecto declare una semilla, modelo y pruebas dbt."""

from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]


def test_dbt_project_declares_reproducible_model_and_tests():
    """La transformación debe tener fuente, modelo y condiciones de calidad explícitas."""

    model = (PRE_DIR / "models" / "factory_totals.sql").read_text()
    schema = (PRE_DIR / "models" / "schema.yml").read_text()

    assert "ref('daily_operations')" in model
    assert "not_null" in schema
    assert "unique" in schema
