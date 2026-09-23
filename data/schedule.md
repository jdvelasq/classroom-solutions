# Inventario heredado — Fundamentos de Datos para Analítica

## Propósito y lectura

Este archivo inventaría material heredado de `PRE_*`; no propone una programación nueva ni modifica actividades. El orden es numérico. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. El estado **Esqueleto** se basa en la presencia de estructura, `__init__.py` y pruebas, sin datos, notebooks, implementación o entregables no vacíos observables.

Los talleres de Datos producen insumos confiables para consumo analítico —datasets curados, contratos, vistas, flujos o servicios de datos—, no el producto analítico final. Un activo de datos adquiere condición de producto cuando tiene consumidor, semántica, contrato, propiedad y compromiso de servicio; empaquetar la capacidad analítica para ese consumidor corresponde a Productos de Datos.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

El tiempo estimado incluye presentar datos, problema, razonamiento y solución; se registra solo para material desarrollado y se redondea a múltiplos de 5 minutos.

| Orden | Actividad | Ideas o conceptos inferidos | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---|---:|
| 1 | `PRE_01_relational_data` | tablas, claves, relaciones e integridad | Esqueleto con pruebas | BASE | — |
| 2 | `PRE_02_sql_integration` | consultas, joins, agregación e integración SQL | Esqueleto con pruebas | BASE | — |
| 3 | `PRE_03_sql_transformation` | transformación, tipado, faltantes, ventanas y deduplicación | Esqueleto con pruebas | BASE | — |
| 4 | `PRE_04_analytical_warehouse` | hechos, dimensiones, esquema estrella y data marts | Esqueleto con pruebas | BASE | — |
| 5 | `PRE_05_data_formats` | CSV, JSON, Parquet, tipos y compresión | Esqueleto con pruebas | BASE | — |
| 6 | `PRE_06_data_lakehouse` | almacenamiento de objetos, particiones, lago y lakehouse | Esqueleto con pruebas | BASE | — |
| 7 | `PRE_07_nosql_data` | datos semiestructurados y criterios SQL/NoSQL | Esqueleto con pruebas | OPT | — |
| 8 | `PRE_08_batch_ingestion` | extracción por lote, persistencia y manejo de errores | Esqueleto con pruebas | BASE | — |
| 9 | `PRE_09_api_ingestion` | APIs, paginación, parámetros, reintentos y persistencia | Esqueleto con pruebas | BASE | — |
| 10 | `PRE_10_data_pipeline` | ETL/ELT, capas y pipeline reproducible | Esqueleto con pruebas | BASE | — |
| 11 | `PRE_11_data_quality` | completitud, validez, unicidad, consistencia y frescura | Esqueleto con pruebas | BASE | — |
| 12 | `PRE_12_data_contracts` | esquemas, evolución, contrato, cuarentena y fallo controlado | Esqueleto con pruebas | BASE | — |
| 13 | `PRE_13_incremental_pipeline` | incrementales, append/upsert, idempotencia y CDC | Esqueleto con pruebas | BASE | — |
| 14 | `PRE_14_pipeline_operations` | dependencias, DAG, programación, reintentos y observabilidad básica | Esqueleto con pruebas | BASE | — |
| 15 | `PRE_15_distributed_processing` | particiones y procesamiento distribuido | Esqueleto con pruebas | OPT | — |
| 16 | `PRE_16_event_streams` | productores, consumidores, brokers y tiempo de evento | Esqueleto con pruebas | OPT | — |
| 17 | `PRE_17_streaming_pipeline` | ingestión continua, ventanas, estado y entrega | Esqueleto con pruebas | OPT | — |
| 18 | `PRE_18_data_serving` | datasets curados, vistas y consumidores analíticos | Esqueleto con pruebas | BASE | — |
| 19 | `PRE_19_metadata_lineage` | catálogo, linaje, propiedad, acceso y privacidad | Esqueleto con pruebas | BASE | — |
| 20 | `PRE_20_end_to_end_architecture` | arquitectura extremo a extremo y trade-offs | Esqueleto con pruebas | BASE | — |

La clasificación curricular `BASE`/`OPT` es independiente del hecho de que todos estos PRE sean actualmente esqueletos. Los `BASE` son trabajo de desarrollo requerido antes de la oferta.

## Cobertura frente a `curriculum.md`

| Unidad curricular | Actividades heredadas | Estado de cobertura |
|---|---|---|
| Datos en el ciclo analítico | Ninguna actividad inequívoca; corresponde a fundamentación. | Pendiente de contraste teórico. |
| Representación relacional y SQL | PRE 01–03 | Inventariada. |
| Integración y transformación | PRE 02–03 | Inventariada. |
| Modelado y almacenamiento analítico | PRE 04, 06–07 | Inventariada. |
| Formatos y datos semiestructurados | PRE 05, 07 | Inventariada. |
| Ingestión | PRE 08–09 | Inventariada. |
| Pipelines e incrementalidad | PRE 10, 13–14 | Inventariada. |
| Calidad y contratos | PRE 11–12 | Inventariada. |
| Escala, eventos y streaming | PRE 15–17 | Inventariada. |
| Serving, metadatos y gobierno técnico | PRE 18–19 | Inventariada. |
| Arquitectura integral | PRE 20 | Inventariada. |

## Observación de inventario

La secuencia heredada cubre nominalmente todas las unidades prácticas del currículo macro, pero su profundidad de implementación no puede acreditarse aún: las actividades observables son principalmente esqueletos con pruebas.
