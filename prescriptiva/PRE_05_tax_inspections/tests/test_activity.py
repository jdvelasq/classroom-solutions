import os

FOLDER = "PRE_05_tax_inspections"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/inspection_decisions.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/portfolio_comparison.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/capacity_sensitivity.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/tax_inspection_planner.png")
