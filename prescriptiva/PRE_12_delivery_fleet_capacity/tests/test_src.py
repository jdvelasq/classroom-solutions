import os

FOLDER = "PRE_12_delivery_fleet_capacity"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/fleet_evaluation.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/reference_policies.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/outsourcing_cost_sensitivity.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/delivery_fleet_capacity_planner.png")
