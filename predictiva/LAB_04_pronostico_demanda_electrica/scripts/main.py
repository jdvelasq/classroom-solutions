"""Pronostica la demanda máxima diaria de electricidad."""

import json
from pathlib import Path

import pandas as pd
from sklearn.metrics import mean_absolute_error

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ACTIVITY_DIR / "data" / "demanda_comercial.csv.gz"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def main():
    """
    El operador del sistema eléctrico necesita anticipar el pico diario de
    demanda para programar la generación. El archivo
    `data/demanda_comercial.csv.gz` tiene una fila por día, desde el
    2017-01-01 hasta el 2022-08-31, con la fecha (`Fecha`) y la demanda
    comercial de cada una de las 24 horas del día (`H01`, `H02`, ...,
    `H24`).

    Use estas definiciones:

    - Pico diario (`actual_peak`): la mayor demanda horaria del día.
    - Conjunto de entrenamiento: el primer 80 % de los días, en orden
      cronológico (redondee la cantidad de días hacia abajo). Conjunto de
      prueba: los días restantes.
    - Pronóstico base (`baseline_forecast`): el pico diario promedio del
      conjunto de entrenamiento, igual para todos los días de prueba.
    - Pronóstico por día de la semana (`weekday_forecast`): el pico diario
      promedio de los días del conjunto de entrenamiento que caen en el
      mismo día de la semana que el día pronosticado.

    Genere dos archivos en `submission/`:

    1. `forecast.csv`, sin el índice de Pandas, con una fila por día del
       conjunto de prueba, en orden cronológico, y las columnas `Fecha` (en
       formato `AAAA-MM-DD`), `actual_peak`, `baseline_forecast` y
       `weekday_forecast`.

    2. `metrics.json`, con dos llaves: `baseline_mae` y `weekday_mae`, el
       error absoluto medio de cada pronóstico sobre el conjunto de prueba.

    Escriba su solución en la función `main()`, que debe generar los dos
    archivos al ejecutarse.

    Ejemplo del formato de `forecast.csv`:

        Fecha,actual_peak,baseline_forecast,weekday_forecast
        2021-07-14,10185785.87,9361644.7507,9636851.2230
        2021-07-15,10199084.8,9361644.7507,9639853.9742
        ...

    Ejemplo del formato de `metrics.json`:

        {
          "baseline_mae": 746571.3821,
          "weekday_mae": 682405.6048
        }
    """
    demand = pd.read_csv(DATA_PATH, parse_dates=["Fecha"])
    demand["daily_peak"] = demand.filter(regex="^H").max(axis=1)
    demand["day_of_week"] = demand["Fecha"].dt.dayofweek
    split = int(len(demand) * 0.8)
    train, test = demand.iloc[:split].copy(), demand.iloc[split:].copy()
    weekday_profile = train.groupby("day_of_week")["daily_peak"].mean()
    test["baseline_forecast"] = train["daily_peak"].mean()
    test["weekday_forecast"] = test["day_of_week"].map(weekday_profile)
    forecast = test[
        ["Fecha", "daily_peak", "baseline_forecast", "weekday_forecast"]
    ].rename(columns={"daily_peak": "actual_peak"})
    metrics = {
        "baseline_mae": mean_absolute_error(
            forecast["actual_peak"], forecast["baseline_forecast"]
        ),
        "weekday_mae": mean_absolute_error(
            forecast["actual_peak"], forecast["weekday_forecast"]
        ),
    }
    SUBMISSION_DIR.mkdir(exist_ok=True)
    forecast.to_csv(SUBMISSION_DIR / "forecast.csv", index=False)
    (SUBMISSION_DIR / "metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
