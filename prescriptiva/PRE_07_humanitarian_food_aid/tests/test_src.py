import os

FOLDER = "PRE_07_humanitarian_food_aid"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/shipment_plan.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/supplier_utilization.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/plan_comparison.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/humanitarian_supply_planner.png")
