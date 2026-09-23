# Inventario de PRE — Data para Analytics

Cada fila representa un `PRE_*`; las unidades de `curriculum.md` se comprueban agregando la cobertura de varios PRE, no se convierten en sesiones. Los tiempos incluyen exposición docente del problema, razonamiento y solución.

| Orden | Actividad | Foco | Tiempo estimado |
|---:|---|---|---:|
| 1 | `PRE_01_hola_mundo` | ambiente, estructura y pruebas | 20 min |
| 2 | `PRE_02_mapreduce` | `map`, pares clave--valor, ordenamiento y `reduce` | 50 min |
| 3 | `PRE_03_consultas_basicas_en_mapreduce` | filtros, cálculo y agregación sobre `tips.csv` | 55 min |
| 4 | `PRE_04_consultas_avanzadas_en_mapreduce` | agregación, segunda pasada, unión y top 10 por clave | 65 min |
| 5 | `PRE_05_programacion_en_python_multiprocessing` | procesamiento local por particiones y aceleración verificable | 60 min |
| 6 | `PRE_06_particionamiento_y_sesgo_de_claves` | particiones, claves calientes y preagregación local | 55 min |
| 7 | `PRE_07_relational_data` | tablas, claves, relaciones e integridad | 75 min |
| 8 | `PRE_08_sql_integration` | consultas, joins, agregación e integración SQL | 60 min |
| 9 | `PRE_09_sql_transformation` | transformación y vista curada | 60 min |
| 10 | `PRE_10_analytical_warehouse` | hechos, dimensiones y data mart | 70 min |
| 11 | `PRE_11_data_formats` | CSV, JSON, Parquet y criterios de uso | 55 min |
| 12 | `PRE_12_data_lakehouse` | particiones, almacenamiento y recuperación | 60 min |
| 13 | `PRE_13_nosql_data` | datos semiestructurados y criterio SQL/NoSQL | 55 min |
| 14 | `PRE_14_batch_ingestion` | extracción por lote y persistencia | 60 min |
| 15 | `PRE_15_api_ingestion` | APIs, paginación y reintentos | 60 min |
| 16 | `PRE_16_data_pipeline` | pipeline ETL/ELT reproducible | 65 min |
| 17 | `PRE_17_data_quality` | completitud, validez, unicidad y consistencia | 60 min |
| 18 | `PRE_18_data_contracts` | esquemas, evolución y fallos controlados | 60 min |
| 19 | `PRE_19_incremental_pipeline` | incrementalidad e idempotencia | 65 min |
| 20 | `PRE_20_pipeline_operations` | dependencias y observabilidad básica | 55 min |
| 21 | `PRE_21_distributed_processing` | particiones y procesamiento a escala | 60 min |
| 22 | `PRE_22_event_streams` | eventos y tiempo de evento | 55 min |
| 23 | `PRE_23_streaming_pipeline` | estado, ventanas y entrega continua | 60 min |
| 24 | `PRE_24_data_serving` | vistas y datos curados para consumo | 55 min |
| 25 | `PRE_25_metadata_lineage` | catálogo, linaje y propiedad | 50 min |
| 26 | `PRE_26_end_to_end_architecture` | arquitectura integral y trade-offs | 70 min |

Los PRE 01--06 forman el bloque de fundamento de Big Data Analytics: hacen visible cómo una clave organiza una agregación, una unión y el intercambio de datos entre particiones. No requieren instalar Spark ni operar un clúster.

Los cinco `LAB_*` de evaluación están diseñados en [`labs.md`](labs.md). No forman parte de esta secuencia ni de su carga horaria.
