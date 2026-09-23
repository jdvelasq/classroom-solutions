# PRE_06 — Particionamiento y sesgo de claves

## Problema

Las 24 transacciones del caso pueden repartirse por `event_id` o por `account_id`. Una cuenta `HOT` concentra 16 transacciones: la misma cantidad de datos deja de representar la misma carga de trabajo cuando la clave cambia.

## Idea central

Particionar por clave permite reunir registros relacionados, pero una clave frecuente produce desbalance. Un combiner suma localmente importes de la misma cuenta y reduce los pares que viajan al shuffle; no elimina por sí solo el trabajo concentrado de la clave caliente.

## Entregables

`partition_loads.csv` muestra ambos repartos y `shuffle_comparison.csv` compara pares originales contra pares tras la preagregación local. El notebook contiene únicamente celdas de código y comienza con `# Problema:`.
