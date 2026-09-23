"""Consume un log de eventos y marca los que llegan tarde."""

import csv
from pathlib import Path

ROOT = Path(__file__).parents[1]
EVENTS = ROOT / "data/events.csv"
CONSUMED = ROOT / "submission/consumed_events.csv"
SUMMARY = ROOT / "submission/stream_summary.csv"


def build_submission():
    rows = [("E1", "2026-01-01T10:00:00", "P1", 1, 10), ("E2", "2026-01-01T10:10:00", "P2", 2, 20), ("E3", "2026-01-01T10:05:00", "P1", 1, 10), ("E4", "2026-01-01T10:15:00", "P3", 3, 30)]
    with EVENTS.open("w", newline="") as file:
        writer = csv.writer(file); writer.writerow(["event_id", "event_time", "product_id", "quantity", "sales_amount"]); writer.writerows(rows)
    maximum, consumed = "", []
    for position, row in enumerate(rows, 1):
        delayed = row[1] < maximum; maximum = max(maximum, row[1]); consumed.append((position, *row, delayed))
    with CONSUMED.open("w", newline="") as file:
        writer = csv.writer(file); writer.writerow(["arrival_position", "event_id", "event_time", "product_id", "quantity", "sales_amount", "is_delayed"]); writer.writerows(consumed)
    metrics = [("event_count", len(rows)), ("unique_products", len({row[2] for row in rows})), ("total_sales", sum(row[4] for row in rows)), ("delayed_event_count", sum(row[-1] for row in consumed))]
    with SUMMARY.open("w", newline="") as file:
        writer = csv.writer(file); writer.writerow(["metric", "value"]); writer.writerows(metrics)


if __name__ == "__main__":
    build_submission()
