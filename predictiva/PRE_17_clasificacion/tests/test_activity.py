import os

FOLDER = "PRE_17_clasificacion"


def test_01():

    assert os.path.exists(f"{FOLDER}/notebooks/notebook-1.ipynb")
    assert os.path.exists(f"{FOLDER}/notebooks/notebook-2.ipynb")
