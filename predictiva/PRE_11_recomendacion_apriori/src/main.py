"""Deriva reglas de asociación para recomendaciones de cross-sell."""

from itertools import combinations
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "policy_baskets.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
MIN_SUPPORT = 0.15
MIN_CONFIDENCE = 0.50
MIN_LIFT = 1.10


def main():
    purchases = pd.read_csv(DATA_PATH)
    baskets = purchases.groupby("customer_id")["product"].agg(set)
    products = sorted(purchases["product"].unique())
    total_baskets = len(baskets)
    supports = {}
    frequent_itemsets = []
    for size in (1, 2, 3):
        for itemset in combinations(products, size):
            itemset = frozenset(itemset)
            count = sum(itemset.issubset(basket) for basket in baskets)
            support = count / total_baskets
            supports[itemset] = support
            if support >= MIN_SUPPORT:
                frequent_itemsets.append({"items": " | ".join(sorted(itemset)), "size": size, "basket_count": count, "support": support})
    rules = []
    for itemset, support in supports.items():
        if len(itemset) < 2 or support < MIN_SUPPORT:
            continue
        for antecedent_size in range(1, len(itemset)):
            for antecedent_items in combinations(itemset, antecedent_size):
                antecedent = frozenset(antecedent_items)
                consequent = itemset - antecedent
                confidence = support / supports[antecedent]
                lift = confidence / supports[consequent]
                if confidence >= MIN_CONFIDENCE and lift >= MIN_LIFT:
                    rules.append({"antecedent": " | ".join(sorted(antecedent)), "consequent": " | ".join(sorted(consequent)), "support": support, "confidence": confidence, "lift": lift, "basket_count": int(support * total_baskets)})
    SUBMISSION_DIR.mkdir(exist_ok=True)
    pd.DataFrame(frequent_itemsets).sort_values(["size", "support"], ascending=[True, False]).to_csv(SUBMISSION_DIR / "frequent_itemsets.csv", index=False)
    pd.DataFrame(rules).sort_values(["lift", "confidence", "support"], ascending=False).to_csv(SUBMISSION_DIR / "cross_sell_rules.csv", index=False)


if __name__ == "__main__":
    main()
