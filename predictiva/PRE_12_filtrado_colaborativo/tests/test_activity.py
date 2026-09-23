"""Verifica las recomendaciones colaborativas."""

import numpy as np
import pandas as pd


def test_recommendations_exclude_owned_products_and_rank_vida_first():
    recommendations = pd.read_csv("submission/recommendations.csv")
    assert not recommendations.empty
    assert not recommendations["already_owned"].any()
    assert recommendations["predicted_preference"].between(0, 1).all()
    assert recommendations.iloc[0]["product"] == "vida"


def test_similarity_matrix_is_complete_and_has_unit_diagonal():
    matrix = pd.read_csv("submission/customer_similarity.csv", index_col=0)
    assert matrix.shape == (10, 10)
    assert (matrix.index == matrix.columns).all()
    assert np.allclose(matrix.values.diagonal(), 1)
