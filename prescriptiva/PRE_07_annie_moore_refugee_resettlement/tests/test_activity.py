import os

FOLDER = "PRE_07_annie_moore_refugee_resettlement"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/placement_decisions.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/location_utilization.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/assignment_comparison.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/refugee_placement_console.png")
