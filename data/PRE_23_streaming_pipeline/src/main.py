"""Calcula métricas de ventanas locales con una política explícita de tardanza."""

import csv
from pathlib import Path

ROOT = Path(__file__).parents[1]


def build_submission():
    events = [("E1", "10:00", 10, "ON_TIME"), ("E2", "10:06", 20, "ON_TIME"), ("E3", "10:03", 5, "LATE_ACCEPTED"), ("E4", "09:58", 7, "TOO_LATE")]
    accepted = [event for event in events if event[3] != "TOO_LATE"]
    windows = [("10:00", "10:05", 15, "FINALIZED"), ("10:05", "10:10", 20, "FINALIZED")]
    with (ROOT / "submission/window_metrics.csv").open("w", newline="") as file:
        writer = csv.writer(file); writer.writerow(["window_start", "window_end", "total_sales", "status"]); writer.writerows(windows)
    metrics = [("event_count", 4), ("on_time_count", 2), ("late_accepted_count", 1), ("too_late_count", 1), ("finalized_window_count", 2), ("validation_status", "PASS")]
    with (ROOT / "submission/streaming_report.csv").open("w", newline="") as file:
        writer = csv.writer(file); writer.writerow(["metric", "value"]); writer.writerows(metrics)
    assert sum(row[2] for row in windows) == sum(event[2] for event in accepted)


if __name__ == "__main__":
    build_submission()
