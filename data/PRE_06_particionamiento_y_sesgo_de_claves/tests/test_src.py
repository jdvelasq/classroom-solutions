"""El sesgo debe ser observable y el combiner debe reducir pares."""

from ..src.main import SUBMISSION_DIR, run


def test_makes_skew_and_preaggregation_visible():
    result = run()
    assert max(result["skewed"]) > max(result["balanced"])
    assert result["combined_pairs"] < sum(result["skewed"])
    assert (SUBMISSION_DIR / "partition_loads.csv").exists()
    assert (SUBMISSION_DIR / "shuffle_comparison.csv").exists()
