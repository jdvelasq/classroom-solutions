# PRE Specification

## Identification

**Activity:** `PRE_15_distributed_processing`

**Status:** `READY`

## Activity title

**Entender cómo se organiza un procesamiento**

## Central insight

Una agregación conserva su resultado lógico aunque el trabajo se divida físicamente. Las particiones producen resultados parciales que deben consolidarse cuando una categoría aparece en más de una parte.

La actividad responde: ¿qué cambia y qué no cambia cuando el mismo cálculo se ejecuta sobre partes de un dataset?

## Course capability

Introduce partición, resultados parciales, consolidación, resultado lógico frente a organización física y orden determinista. No es un curso de Spark ni de procesamiento distribuido productivo.

## Engineering problem

Un analista necesita ventas por categoría. El cálculo se ejecuta sobre dos particiones locales y se compara con la agregación de referencia sobre el dataset completo. El dataset tiene cuatro líneas y dos categorías; una categoría aparece en ambas particiones.

## Solution form

La solución docente vive en `notebooks/notebook.ipynb`. Hace visibles el dataset, las particiones, las agregaciones parciales, la consolidación y la comparación final.

## Expected artifacts

`submission/category_sales.parquet` contiene una fila por categoría con `product_category` y `sales_amount`.

`submission/execution_summary.csv` contiene `input_rows`, `teaching_input_partitions`, `output_categories` y `validation_status`.

## Visible validation

1. El resultado de las particiones consolidadas es igual a la referencia no particionada.
2. Cada categoría aparece una vez después de ordenar explícitamente la salida.

## Required tests

Las pruebas verifican artefactos, grano por categoría y equivalencia con la referencia lógica.

## Boundaries

No introducir PySpark, Spark SQL, clusters, *shuffle*, planes físicos, benchmarking, streaming ni infraestructura cloud. La lección es el criterio sobre particiones, no una plataforma.

## Acceptance criteria

1. El notebook ejecuta de arriba abajo con el stack declarado.
2. Toda la lógica de partición y consolidación es visible.
3. El resultado final reconcilia con la referencia.
4. El PRE no requiere una dependencia de procesamiento distribuido.
