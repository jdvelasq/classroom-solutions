import os

FOLDER = "PRE_08_flood_protection_investment"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/protection_curve.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/investment_comparison.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/risk_sensitivity.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/flood_protection_investment_planner.png")
