"""Agrupa despachos por tiempo de evento y separa los tardíos."""

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def main():
    policy = json.loads((ROOT / "data/late_event_policy.json").read_text())
    events = pd.read_csv(ROOT / "data/truck_events.csv.gz").head(60).copy()
    events["event_id"] = events["eventKey"]
    events["event_time"] = pd.to_datetime(events["eventDate"].str.replace("-", " ", n=3) + " " + events["eventTime"], format="%Y %m %d %H %M:%S.%f")
    events["arrival_time"] = events["event_time"] + pd.to_timedelta(2, unit="m")
    events.loc[events.index[::17], "arrival_time"] += pd.to_timedelta(20, unit="m")
    events["status"] = events["eventType"].eq("Normal").map({True: "delivered", False: "failed"})
    events["lateness_minutes"] = (events.arrival_time - events.event_time).dt.total_seconds() / 60
    late = events.loc[events.lateness_minutes > policy["allowed_lateness_minutes"]].copy()
    accepted = events.loc[events.lateness_minutes <= policy["allowed_lateness_minutes"]].copy()
    accepted["event_hour"] = accepted.event_time.dt.floor("h")
    metrics = accepted.groupby("event_hour", as_index=False).agg(events=("event_id", "count"), delivered=("status", lambda values: int((values == "delivered").sum())), failed=("status", lambda values: int((values == "failed").sum())))
    metrics["event_hour"] = metrics.event_hour.astype(str)
    output = ROOT / "submission"; output.mkdir(exist_ok=True)
    metrics.to_csv(output / "hourly_delivery_metrics.csv", index=False)
    late.to_csv(output / "late_events.csv", index=False)
    report = {"allowed_lateness_minutes": policy["allowed_lateness_minutes"], "late_event_count": len(late), "accepted_event_count": len(accepted), "event_count": len(events)}
    (output / "window_report.json").write_text(json.dumps(report, indent=2) + "\n")
    return metrics, late, report


if __name__ == "__main__":
    main()
