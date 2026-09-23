# LAB — Data para Analytics

Los LAB son evaluaciones independientes. No justifican cobertura curricular, no reemplazan PRE y no constituyen un proyecto integrador. Cada uno plantea una necesidad analítica concreta y evalúa un activo de datos verificable.

## LAB_01_integracion_y_grano_analitico

**Caso.** El equipo de operaciones de una fábrica necesita producción diaria por planta. Recibe producción por máquina, disponibilidad de máquinas y condiciones ambientales en extractos separados.

**Competencia evaluada.** Definir el grano de la salida, integrar las fuentes sin duplicar unidades producidas y reconciliar el resultado con el total operacional.

**Datos de entrada.** `machine_throughput_export.csv`, `machine_uptime_export.csv` y `factory_ambient_export.csv`.

**Entrega.** `submission/factory_daily_operations.csv` y `submission/reconciliation.json`.

**Criterios verificables.** Una fila por fábrica-día; claves y tipos válidos; ninguna máquina-día duplicada; unidades producidas reconciliadas con el origen; disponibilidad y ambiente incorporados sin cambiar el grano.

**Frontera.** No evalúa normalización formal ni administración de una base de datos.

## LAB_02_calidad_y_contrato_de_datos

**Caso.** Analítica recibe un extracto tributario real de Vermont por código postal y tramo de ingreso. La entrega contiene registros que deben aceptarse o ponerse en cuarentena de acuerdo con reglas explícitas.

**Competencia evaluada.** Expresar un contrato de datos, diagnosticar calidad y separar registros aceptados de registros en cuarentena sin alterar la fuente.

**Datos de entrada.** `vemont.csv`, con defectos controlados introducidos durante la ejecución para evaluar las reglas.

**Entrega.** `submission/quality_report.json`, `submission/accepted_tax_records.csv` y `submission/quarantined_tax_records.csv`.

**Criterios verificables.** Estado, dominio de tramo de ingreso, unicidad de la llave código postal--tramo y no negatividad evaluados; causas de cuarentena trazables por registro; conteos reconciliados.

**Frontera.** No evalúa una herramienta de DataOps ni un servicio de calidad en producción.

## LAB_03_pipeline_incremental_idempotente

**Caso.** Un analista de operaciones recibe lotes diarios de producción máquina--día, con una corrección, un reenvío y una operación nueva. Necesita un estado vigente que pueda recalcularse sin duplicar resultados.

**Competencia evaluada.** Diseñar una actualización incremental con llave de negocio, checkpoint y comportamiento idempotente.

**Datos de entrada.** `machine_throughput_export.csv`; el programa construye de manera determinista el estado base y el lote incremental.

**Entrega.** `submission/operations_current.csv`, `submission/pipeline_run.json` y `submission/reconciliation.json`.

**Criterios verificables.** Cada operación máquina--día aparece una sola vez en el estado vigente; la corrección reemplaza el registro anterior; una segunda ejecución produce el mismo resultado; checkpoint y métricas de inserción, actualización y reenvío son consistentes.

**Frontera.** No exige orquestador, colas, nube ni CDC productivo.

## LAB_04_eventos_tardios_y_metricas

**Caso.** Un centro de distribución monitorea telemetría de camiones. Los eventos llegan fuera de orden; la gerencia necesita métricas por hora de evento y evidencia de los registros tardíos.

**Competencia evaluada.** Distinguir tiempo de evento de tiempo de llegada, construir ventanas y aplicar una política explícita para eventos tardíos.

**Datos de entrada.** `truck_events.csv.gz`, una muestra local de telemetría, y `late_event_policy.json`.

**Entrega.** `submission/hourly_delivery_metrics.csv`, `submission/late_events.csv` y `submission/window_report.json`.

**Criterios verificables.** Las ventanas se construyen por tiempo de evento; los registros tardíos se identifican según la política; totales y conteos se reconcilian; la salida permite explicar qué métrica puede revisarse posteriormente.

**Frontera.** No evalúa Kafka, Spark Streaming ni operación de un broker.

## LAB_05_serving_linaje_y_consumidor_analitico

**Caso.** Un equipo de operaciones requiere una vista diaria de producción por fábrica. La fuente está a nivel de máquina--día y la salida debe responder al consumidor sin perder su procedencia.

**Competencia evaluada.** Preparar un activo de datos para un consumidor definido y documentar su contrato, grano, procedencia, propiedad y limitaciones.

**Datos de entrada.** `machine_throughput_export.csv`.

**Entrega.** `submission/factory_daily_serving_view.csv`, `submission/serving_manifest.json` y `submission/lineage.csv`.

**Criterios verificables.** El grano fábrica--día responde a la solicitud del consumidor; esquema y definiciones son explícitos; el linaje conecta fuente, agregación y salida; propiedad y restricciones de uso están documentadas; se distingue el activo de datos de un producto de datos.

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
