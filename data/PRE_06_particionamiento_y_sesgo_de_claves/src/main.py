"""Particiones, claves sesgadas y preagregación local."""

import csv
import hashlib
from collections import defaultdict
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "events.csv"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def partition_for(key, partitions=4):
    """Ubica determinísticamente una clave en una partición."""
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % partitions


def read_events():
    with DATA_FILE.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def loads(rows, key_column, partitions=4):
    result = [0] * partitions
    for row in rows:
        result[partition_for(row[key_column], partitions)] += 1
    return result


def local_combiner(rows, partitions=4):
    """Suma importes por cuenta dentro de cada partición antes del shuffle."""
    partials = [defaultdict(float) for _ in range(partitions)]
    for row in rows:
        partials[partition_for(row["account_id"], partitions)][row["account_id"]] += float(row["amount"])
    return partials


def run():
    """Compara reparto por evento, reparto por cuenta y efecto del combiner."""
    rows = read_events()
    balanced = loads(rows, "event_id")
    skewed = loads(rows, "account_id")
    partials = local_combiner(rows)
    combined_pairs = sum(len(partition) for partition in partials)
    SUBMISSION_DIR.mkdir(exist_ok=True)
    with (SUBMISSION_DIR / "partition_loads.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["partition", "event_key_load", "account_key_load"])
        writer.writeheader()
        writer.writerows({"partition": index, "event_key_load": balanced[index], "account_key_load": skewed[index]} for index in range(4))
    with (SUBMISSION_DIR / "shuffle_comparison.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["raw_pairs", "pairs_after_local_combiner", "hot_key_load"])
        writer.writeheader()
        writer.writerow({"raw_pairs": len(rows), "pairs_after_local_combiner": combined_pairs, "hot_key_load": max(skewed)})
    return {"balanced": balanced, "skewed": skewed, "combined_pairs": combined_pairs}


if __name__ == "__main__":
    print(run())
