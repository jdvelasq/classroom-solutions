"""Verifica que el estudiante produjo la evidencia del taller Apriori."""

from pathlib import Path


def test_apriori_workshop_artifacts_exist():
    expected_files = [
        "top_items.csv",
        "association_rules.csv",
        "recommendations.csv",
    ]
    for filename in expected_files:
        assert Path("submission", filename).exists()
