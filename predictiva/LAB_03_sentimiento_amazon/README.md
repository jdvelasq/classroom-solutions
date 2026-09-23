# Sentimiento de reseñas de Amazon

## Propósito

Anticipar si una reseña textual de Amazon expresa una opinión positiva o negativa.

## Competencia

Convierte texto en variables numéricas, construye un clasificador reproducible y evalúa la calidad de las predicciones de sentimiento sobre reseñas reservadas.

## Datos

`data/amazon_cells_labelled.tsv` contiene reseñas reales etiquetadas de Amazon. Las filas sin etiqueta no hacen parte de la evaluación supervisada.

## Entregables

Genere `model.pkl`, `test_predictions.csv` y `metrics.json` en `submission/`. El archivo de predicciones debe conservar la reseña, la etiqueta observada y el sentimiento predicho.
