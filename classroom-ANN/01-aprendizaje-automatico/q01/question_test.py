from question import Regressor
import numpy as np


def test_predict():
    reg = Regressor()
    reg.coef_ = np.array([1, 2, 3])
    reg.intercept_ = 2
    x = [[1, 2, 3]]
    assert reg.predict(x) == [16]
