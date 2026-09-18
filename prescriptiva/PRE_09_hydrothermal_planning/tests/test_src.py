import os

FOLDER = "PRE_09_hydrothermal_planning"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/generation_schedule.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/reservoir_schedule.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/plan_comparison.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/hydrothermal_planning_dashboard.png")
