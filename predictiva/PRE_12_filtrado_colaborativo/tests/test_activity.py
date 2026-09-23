"""Verifica la evidencia producida durante el taller de FilmTrust."""

from pathlib import Path


def test_collaborative_filtering_workshop_artifacts_exist():
    expected_files = [
        "coverage_summary.csv",
        "nearest_neighbors.csv",
        "recommendations.csv",
    ]
    for filename in expected_files:
        assert Path("submission", filename).exists()
