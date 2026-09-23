from pathlib import Path
def test_priority_workshop_artifacts_exist():
    for name in ['calibration_summary.csv', 'threshold_tradeoff.csv', 'group_review.csv']:
        assert Path('submission', name).exists()
