import os

def test_01():

    assert os.path.exists("notebooks/notebook-1.ipynb")
    assert os.path.exists("notebooks/notebook-2.ipynb")
