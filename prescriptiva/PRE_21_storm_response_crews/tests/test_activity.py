import os

FOLDER = "PRE_21_storm_response_crews"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/reserve_evaluation.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/scenario_actions.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/extreme_probability_sensitivity.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/storm_response_capacity_planner.png")
