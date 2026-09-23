"""Pruebas: ambos modos deben producir exactamente el mismo resultado."""

from ..src.main import SUBMISSION_DIR, run


def test_parallel_and_sequential_results_match():
    counts, benchmark = run(repetitions=100, workers=2)
    assert counts["analytics"] > 0
    assert benchmark["workers"] == 2
    assert (SUBMISSION_DIR / "word_counts.csv").exists()
    assert (SUBMISSION_DIR / "benchmark.csv").exists()
