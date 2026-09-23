"""Consultas elementales sobre ``tips.csv`` mediante pares clave--valor."""

import csv
from collections import defaultdict
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tips.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def read_tips():
    """Lee el archivo local del caso, sin requerir una descarga al ejecutar."""
    with DATA_FILE.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def reduce_counts(pairs):
    """Combina valores por clave, la operación equivalente a ``COUNT(*)``."""
    counts = defaultdict(int)
    for key, value in pairs:
        counts[key] += value
    return dict(sorted(counts.items()))


def run():
    """Materializa cinco consultas simples y sus resultados reproducibles."""
    rows = read_tips()
    SUBMISSION_DIR.mkdir(exist_ok=True)

    rates = [
        {**row, "tip_rate": round(float(row["tip"]) / float(row["total_bill"]), 6)}
        for row in rows
    ]
    dinner = [row for row in rows if row["time"] == "Dinner"]
    dinner_large_tip = [row for row in dinner if float(row["tip"]) > 5.0]
    large_party = [
        row for row in rows if int(row["size"]) >= 5 or float(row["total_bill"]) > 45.0
    ]
    counts_by_sex = reduce_counts((row["sex"], 1) for row in rows)

    outputs = {
        "query_1_tip_rates.csv": (rates, list(rates[0])),
        "query_2_dinner.csv": (dinner, list(rows[0])),
        "query_3_dinner_large_tip.csv": (dinner_large_tip, list(rows[0])),
        "query_4_large_party.csv": (large_party, list(rows[0])),
        "query_5_count_by_sex.csv": (
            [{"sex": key, "count": value} for key, value in counts_by_sex.items()],
            ["sex", "count"],
        ),
    }
    for name, (result, fieldnames) in outputs.items():
        with (SUBMISSION_DIR / name).open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(result)
    return outputs


if __name__ == "__main__":
    run()
