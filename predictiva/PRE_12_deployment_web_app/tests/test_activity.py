"""Autograding script"""

import os

def test_01():

    assert os.path.exists("src/train_model.py")
    assert os.path.exists("src/web_app.py")
    assert os.path.exists("src/descriptivo.ipynb")
    assert os.path.exists("submission/house_predictor.pkl")
