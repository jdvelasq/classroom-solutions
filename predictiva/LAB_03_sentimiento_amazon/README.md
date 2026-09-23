# Completar sentimiento de reseñas de Amazon

## Propósito

Completar la etiqueta de sentimiento faltante en reseñas textuales de Amazon.

## Competencia

Convierte texto en variables numéricas, entrena un clasificador con las reseñas etiquetadas y completa responsablemente una variable de salida faltante.

## Datos

`data/amazon_cells_labelled.tsv` contiene 1.000 reseñas etiquetadas y reseñas adicionales cuya columna de sentimiento está vacía. Las etiquetas disponibles son el conjunto de entrenamiento; las filas restantes son el objetivo de la predicción.

## Entregables

Genere `model.pkl` y `completed_reviews.csv` en `submission/`. El archivo final debe conservar todas las reseñas, mantener intactas las etiquetas observadas y completar cada valor de sentimiento originalmente faltante.
