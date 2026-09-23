"""Misma agregación de vuelos: secuencial frente a procesos locales."""

import csv
import os
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from time import perf_counter

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def count_partition(task):
    """Procesa una partición independiente y devuelve vuelos por origen."""
    rows, repetitions = task
    counts = Counter()
    for _ in range(repetitions):
        counts.update(row["Origin"] for row in rows if row["Cancelled"] == "0")
    return counts


def combine(partials):
    """Reduce los resultados parciales por palabra, como en MapReduce."""
    result = Counter()
    for partial in partials:
        result.update(partial)
    return result


def run(repetitions=50, workers=None):
    """Compara ejecución secuencial y paralela del mismo trabajo por particiones."""
    with __import__("gzip").open(
        DATA_DIR / "flights.csv.gz", "rt", encoding="utf-8", newline=""
    ) as file:
        rows = list(csv.DictReader(file))
    partition_size = (len(rows) + 3) // 4
    tasks = [
        (rows[index : index + partition_size], repetitions)
        for index in range(0, len(rows), partition_size)
    ]
    workers = workers or min(4, os.cpu_count() or 1, len(tasks))

    started = perf_counter()
    sequential = combine(count_partition(task) for task in tasks)
    sequential_seconds = perf_counter() - started

    started = perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        parallel = combine(executor.map(count_partition, tasks))
    parallel_seconds = perf_counter() - started
    assert sequential == parallel

    SUBMISSION_DIR.mkdir(exist_ok=True)
    with (SUBMISSION_DIR / "origin_flights.csv").open(
        "w", encoding="utf-8", newline=""
    ) as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["origin", "flight_count"])
        writer.writerows(sorted(sequential.items()))
    speedup = (
        sequential_seconds / parallel_seconds if parallel_seconds else float("inf")
    )
    with (SUBMISSION_DIR / "benchmark.csv").open(
        "w", encoding="utf-8", newline=""
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "repetitions",
                "workers",
                "sequential_seconds",
                "parallel_seconds",
                "speedup",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow(
            {
                "repetitions": repetitions,
                "workers": workers,
                "sequential_seconds": round(sequential_seconds, 6),
                "parallel_seconds": round(parallel_seconds, 6),
                "speedup": round(speedup, 3),
            }
        )
    return sequential, {
        "workers": workers,
        "sequential_seconds": sequential_seconds,
        "parallel_seconds": parallel_seconds,
        "speedup": speedup,
    }


if __name__ == "__main__":
    _, benchmark = run()
    print(
        f"Aceleración: {benchmark['speedup']:.2f}x con {benchmark['workers']} procesos"
    )
