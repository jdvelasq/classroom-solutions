"""Verifica las reglas de asociación del taller."""

import numpy as np
import pandas as pd


def test_rules_have_correct_metrics_and_volume_thresholds():
    rules = pd.read_csv("submission/cross_sell_rules.csv")
    assert not rules.empty
    assert {"antecedent", "consequent", "support", "confidence", "lift", "basket_count"} == set(rules.columns)
    assert (rules["support"] >= 0.15).all()
    assert (rules["confidence"] >= 0.50).all()
    assert (rules["lift"] >= 1.10).all()
    auto_home = rules.loc[(rules["antecedent"] == "auto") & (rules["consequent"] == "hogar")].iloc[0]
    assert auto_home["basket_count"] == 13
    assert np.isclose(auto_home["confidence"], 13 / 14)


def test_frequent_itemsets_preserve_support_definition():
    itemsets = pd.read_csv("submission/frequent_itemsets.csv")
    auto_home = itemsets.loc[itemsets["items"] == "auto | hogar"].iloc[0]
    assert auto_home["basket_count"] == 13
    assert auto_home["support"] == 0.65
