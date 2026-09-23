"""Pruebas: ambos modos deben producir exactamente el mismo resultado."""

from ..src.main import SUBMISSION_DIR, run


def test_parallel_and_sequential_results_match():
    counts, benchmark = run(repetitions=2, workers=2)
    assert counts["IAD"] > 0
    assert benchmark["workers"] == 2
    assert (SUBMISSION_DIR / "origin_flights.csv").exists()
    assert (SUBMISSION_DIR / "benchmark.csv").exists()
