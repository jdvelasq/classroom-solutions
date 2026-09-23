"""Las preguntas de Drivers resueltas mediante agregaciones por clave."""

import csv
from collections import defaultdict
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def read_csv(name):
    with (DATA_DIR / name).open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def aggregate_timesheet(rows):
    """Map: ``driverId -> medidas parciales``; reduce: combina por conductor."""
    partials = defaultdict(lambda: [0.0, 0.0, 0, float("inf"), float("-inf")])
    for row in rows:
        hours = float(row["hours-logged"])
        miles = float(row["miles-logged"])
        value = partials[row["driverId"]]
        value[0] += hours
        value[1] += miles
        value[2] += 1
        value[3] = min(value[3], hours)
        value[4] = max(value[4], hours)
    return {
        driver_id: {
            "hours-logged": round(value[0], 2),
            "miles-logged": round(value[1], 2),
            "mean_hours-logged": round(value[0] / value[2], 2),
            "min_hours-logged": round(value[3], 2),
            "max_hours-logged": round(value[4], 2),
        }
        for driver_id, value in partials.items()
    }


def run():
    """Responde las mismas preguntas del PRE de pandas con pares clave--valor."""
    timesheet = read_csv("timesheet.csv")
    drivers = read_csv("drivers.csv")
    aggregates = aggregate_timesheet(timesheet)
    names = {row["driverId"]: row["name"] for row in drivers}

    summary = [
        {"driverId": driver_id, "name": names[driver_id], **metrics}
        for driver_id, metrics in aggregates.items()
    ]
    summary.sort(key=lambda row: int(row["driverId"]))
    below_average = [
        {
            **row,
            "mean_hours-logged": aggregates[row["driverId"]]["mean_hours-logged"],
        }
        for row in timesheet
        if float(row["hours-logged"])
        < aggregates[row["driverId"]]["mean_hours-logged"]
    ]
    top10 = sorted(summary, key=lambda row: row["miles-logged"], reverse=True)[:10]

    SUBMISSION_DIR.mkdir(exist_ok=True)
    outputs = {
        "summary.csv": (summary, list(summary[0])),
        "below_average_hours.csv": (below_average, list(below_average[0])),
        "top10_drivers.csv": (top10, list(top10[0])),
    }
    for name, (result, fieldnames) in outputs.items():
        with (SUBMISSION_DIR / name).open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(result)
    return outputs


if __name__ == "__main__":
    run()
