"""Encuentra asociaciones y recomendaciones en canastas de supermercado."""

from collections import Counter
from itertools import combinations
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "groceries.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"
MIN_SUPPORT = 0.006
MIN_CONFIDENCE = 0.25
MIN_LIFT = 1.10
SELECTED_ITEMS = frozenset({"tropical fruit", "yogurt"})


def load_transactions():
    """Lee las filas de longitud variable y las convierte en canastas."""
    transactions = []
    with DATA_PATH.open(encoding="utf-8") as file:
        for line in file:
            basket = frozenset(item.strip() for item in line.split(",") if item.strip())
            if basket:
                transactions.append(basket)
    return transactions


def frequent_itemsets(transactions):
    """Aplica Apriori hasta pares y ternas con soporte suficiente."""
    total = len(transactions)
    item_counts = Counter(item for basket in transactions for item in basket)
    supports = {frozenset([item]): count / total for item, count in item_counts.items()}
    previous = {itemset for itemset, support in supports.items() if support >= MIN_SUPPORT}
    all_itemsets = dict(supports)

    for size in (2, 3):
        candidates = {
            left | right
            for left, right in combinations(previous, 2)
            if len(left | right) == size
        }
        counts = Counter()
        for basket in transactions:
            for candidate in candidates:
                if candidate.issubset(basket):
                    counts[candidate] += 1
        previous = {
            itemset for itemset, count in counts.items() if count / total >= MIN_SUPPORT
        }
        all_itemsets.update({itemset: count / total for itemset, count in counts.items()})

    return {
        itemset: support
        for itemset, support in all_itemsets.items()
        if support >= MIN_SUPPORT
    }


def association_rules(itemsets, total_transactions):
    """Calcula soporte, confianza y lift para reglas de dos o más productos."""
    rules = []
    for itemset, support in itemsets.items():
        if len(itemset) < 2:
            continue
        for antecedent_size in range(1, len(itemset)):
            for antecedent_items in combinations(itemset, antecedent_size):
                antecedent = frozenset(antecedent_items)
                consequent = itemset - antecedent
                confidence = support / itemsets[antecedent]
                lift = confidence / itemsets[consequent]
                if confidence >= MIN_CONFIDENCE and lift >= MIN_LIFT:
                    rules.append(
                        {
                            "antecedent": " | ".join(sorted(antecedent)),
                            "consequent": " | ".join(sorted(consequent)),
                            "basket_count": round(support * total_transactions),
                            "support": support,
                            "confidence": confidence,
                            "lift": lift,
                        }
                    )
    return pd.DataFrame(rules).sort_values(
        ["lift", "confidence", "support"], ascending=False
    )


def main():
    transactions = load_transactions()
    total = len(transactions)
    item_counts = Counter(item for basket in transactions for item in basket)
    top_items = pd.DataFrame(
        [{"product": item, "basket_count": count, "support": count / total} for item, count in item_counts.items()]
    ).sort_values("basket_count", ascending=False)
    basket_sizes = pd.Series([len(basket) for basket in transactions], name="items_in_basket")
    basket_summary = basket_sizes.value_counts().sort_index().rename_axis("items_in_basket").reset_index(name="transaction_count")
    itemsets = frequent_itemsets(transactions)
    itemsets_frame = pd.DataFrame(
        [{"items": " | ".join(sorted(items)), "size": len(items), "basket_count": round(support * total), "support": support} for items, support in itemsets.items()]
    ).sort_values(["size", "support"], ascending=[True, False])
    rules = association_rules(itemsets, total)
    recommendations = rules.loc[
        rules["antecedent"].map(lambda value: frozenset(value.split(" | ")).issubset(SELECTED_ITEMS))
    ].copy()
    SUBMISSION_DIR.mkdir(exist_ok=True)
    top_items.to_csv(SUBMISSION_DIR / "top_items.csv", index=False)
    basket_summary.to_csv(SUBMISSION_DIR / "basket_size_distribution.csv", index=False)
    itemsets_frame.to_csv(SUBMISSION_DIR / "frequent_itemsets.csv", index=False)
    rules.to_csv(SUBMISSION_DIR / "association_rules.csv", index=False)
    recommendations.to_csv(SUBMISSION_DIR / "recommendations.csv", index=False)


if __name__ == "__main__":
    main()
