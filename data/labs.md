# LAB — Data para Analytics

Los LAB son evaluaciones independientes. No justifican cobertura curricular, no reemplazan PRE y no constituyen un proyecto integrador. Cada uno plantea una necesidad analítica concreta y evalúa un activo de datos verificable.

## LAB_01_integracion_y_grano_analitico

**Caso.** El equipo comercial necesita ventas mensuales por cliente, pero recibe órdenes con varias líneas, clientes duplicados y una tabla de segmentación.

**Competencia evaluada.** Definir el grano de la salida, integrar las fuentes sin duplicar ventas y reconciliar el resultado con el total transaccional.

**Datos de entrada.** `orders.csv`, `order_lines.csv`, `customers.csv` y `segments.csv`.

**Entrega.** `submission/customer_month_sales.csv` y `submission/reconciliation.json`.

**Criterios verificables.** Una fila por cliente-mes; claves y tipos válidos; ninguna línea duplicada; suma de ventas reconciliada con el origen; segmento vigente incorporado sin cambiar el grano.

**Frontera.** No evalúa normalización formal ni administración de una base de datos.

## LAB_02_calidad_y_contrato_de_datos

**Caso.** Un modelo de propensión consume diariamente un archivo de clientes. La nueva entrega cambia un tipo, omite valores obligatorios y contiene categorías no permitidas.

**Competencia evaluada.** Expresar un contrato de datos, diagnosticar calidad y separar registros aceptados de registros en cuarentena sin alterar la fuente.

**Datos de entrada.** `customer_feed.csv` y `customer_contract.json`.

**Entrega.** `submission/quality_report.json`, `submission/accepted_customers.csv` y `submission/quarantined_customers.csv`.

**Criterios verificables.** Esquema, obligatoriedad, unicidad y dominios evaluados; causas de cuarentena trazables por registro; conteos reconciliados; falla explícita ante un cambio incompatible del contrato.

**Frontera.** No evalúa una herramienta de DataOps ni un servicio de calidad en producción.

## LAB_03_pipeline_incremental_idempotente

**Caso.** Un analista de operaciones recibe lotes diarios de transacciones, con correcciones y reenvíos. Necesita una tabla curada que pueda recalcularse sin duplicar resultados.

**Competencia evaluada.** Diseñar una actualización incremental con llave de negocio, checkpoint y comportamiento idempotente.

**Datos de entrada.** `baseline_transactions.csv`, `daily_batch.csv` y `checkpoint.json`.

**Entrega.** `submission/transactions_current.csv`, `submission/pipeline_run.json` y `submission/reconciliation.json`.

**Criterios verificables.** Cada transacción aparece una sola vez en el estado vigente; las correcciones reemplazan el registro anterior; una segunda ejecución produce el mismo resultado; checkpoint y métricas de inserción/actualización son consistentes.

**Frontera.** No exige orquestador, colas, nube ni CDC productivo.

## LAB_04_eventos_tardios_y_metricas

**Caso.** Un centro de distribución monitorea despachos por hora. Los eventos llegan fuera de orden; la gerencia necesita métricas por hora de evento y evidencia de los registros tardíos.

**Competencia evaluada.** Distinguir tiempo de evento de tiempo de llegada, construir ventanas y aplicar una política explícita para eventos tardíos.

**Datos de entrada.** `delivery_events.csv` y `late_event_policy.json`.

**Entrega.** `submission/hourly_delivery_metrics.csv`, `submission/late_events.csv` y `submission/window_report.json`.

**Criterios verificables.** Las ventanas se construyen por tiempo de evento; los registros tardíos se identifican según la política; totales y conteos se reconcilian; la salida permite explicar qué métrica puede revisarse posteriormente.

**Frontera.** No evalúa Kafka, Spark Streaming ni operación de un broker.

## LAB_05_serving_linaje_y_consumidor_analitico

**Caso.** Un equipo de Analítica Descriptiva requiere una vista diaria de desempeño comercial. Existen fuentes, una tabla curada, transformaciones y distintos consumidores con necesidades incompatibles.

**Competencia evaluada.** Preparar un activo de datos para un consumidor definido y documentar su contrato, grano, procedencia, propiedad y limitaciones.

**Datos de entrada.** `sales_curated.csv`, `data_assets.csv`, `transformations.csv` y `consumer_request.json`.

**Entrega.** `submission/sales_serving_view.csv`, `submission/serving_manifest.json` y `submission/lineage.csv`.

**Criterios verificables.** El grano responde a la solicitud del consumidor; esquema y definiciones son explícitos; el linaje conecta fuente, transformación y salida; propiedad y restricciones de uso están documentadas; se distingue el activo de datos de un producto de datos.

**Frontera.** No evalúa desarrollo de APIs, tableros ni un producto de datos en operación.

## Cobertura evaluativa

| LAB | Evidencia principal |
|---|---|
| 01 | significado, integración y grano |
| 02 | confianza, calidad y contrato |
| 03 | continuidad, incrementalidad e idempotencia |
| 04 | escala temporal, ventanas y llegada tardía |
| 05 | serving, metadatos, linaje y consumidor |

Antes de implementar un LAB se crea su estructura estándar `LAB_XX_nombre/{data,notebooks,src,submission,temp,tests}`. El LAB recibe datos, enunciado y pruebas de evaluación; no contiene la solución docente desarrollada en los PRE.
