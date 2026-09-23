# Pronóstico de demanda eléctrica

## Propósito

Pronosticar el pico diario de demanda eléctrica para apoyar la planificación operativa.

## Competencia

Respeta el orden temporal al separar entrenamiento y prueba, compara pronósticos base con un patrón semanal y evalúa el error fuera de muestra.

## Datos

`data/demanda_comercial.csv.gz` contiene demanda comercial observada por hora y día.

## Entregables

Genere `forecast.csv` y `metrics.json` en `submission/`. El pronóstico debe conservar fecha, pico observado, pronóstico base y pronóstico por día de la semana para el período de prueba.
