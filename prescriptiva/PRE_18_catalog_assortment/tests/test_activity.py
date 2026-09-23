import os

FOLDER = "PRE_18_catalog_assortment"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/assortment_results.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/product_decisions.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/capacity_sensitivity.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/catalog_portfolio_planner.png")
