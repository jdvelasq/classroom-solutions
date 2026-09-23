# PRE_04 — Consultas avanzadas en MapReduce

## Problema

Resolver las mismas preguntas y usar los mismos archivos `drivers.csv` y `timesheet.csv` de `descriptiva/PRE_07_drivers_pandas`, pero mediante operaciones clave--valor.

## Idea central

`driverId` es la clave que permite combinar sumas, conteos, mínimos y máximos. El promedio requiere una primera agregación; comparar cada semana con ese promedio necesita una segunda pasada. Incorporar el nombre del conductor es una unión por clave.

## Entregables

`summary.csv`, `below_average_hours.csv` y `top10_drivers.csv` en `submission/`, más un notebook de celdas exclusivamente de código.
