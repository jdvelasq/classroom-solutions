"""Pronostica la demanda máxima diaria de electricidad."""

from pathlib import Path
import json

import pandas as pd
from sklearn.metrics import mean_absolute_error

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "demanda_comercial.csv.zip"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def main():
    demand = pd.read_csv(DATA_PATH, parse_dates=["Fecha"])
    demand["daily_peak"] = demand.filter(regex="^H").max(axis=1)
    demand["day_of_week"] = demand["Fecha"].dt.dayofweek
    split = int(len(demand) * 0.8)
    train, test = demand.iloc[:split].copy(), demand.iloc[split:].copy()
    weekday_profile = train.groupby("day_of_week")["daily_peak"].mean()
    test["baseline_forecast"] = train["daily_peak"].mean()
    test["weekday_forecast"] = test["day_of_week"].map(weekday_profile)
    forecast = test[["Fecha", "daily_peak", "baseline_forecast", "weekday_forecast"]].rename(columns={"daily_peak": "actual_peak"})
    metrics = {"baseline_mae": mean_absolute_error(forecast["actual_peak"], forecast["baseline_forecast"]), "weekday_mae": mean_absolute_error(forecast["actual_peak"], forecast["weekday_forecast"])}
    SUBMISSION_DIR.mkdir(exist_ok=True)
    forecast.to_csv(SUBMISSION_DIR / "forecast.csv", index=False)
    (SUBMISSION_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
