# Inventario heredado — Fundamentos de Analítica

## Propósito y lectura

Este archivo inventaría material heredado de `PRE_*`; no propone una programación nueva ni modifica actividades. El orden es numérico. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. **Desarrollado** indica presencia observable de datos/código o notebook/pruebas y entregables; no certifica revisión semántica. Los conceptos se infieren del nombre y artefactos visibles.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

El tiempo se registra solo para material desarrollado y se redondea a múltiplos de 5 minutos. La duración observada en aula tiene precedencia; si no existe, se consigna una estimación según el perfil didáctico definido en `PROJECT.md` (microcaso técnico, caso analítico acotado o sustantivo, o inducción operativa).

| Orden | Actividad | Ideas o conceptos inferidos | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---|---:|
| 1 | `PRE_01_hola_mundo` | inducción: GitHub, resolución, pytest en VS Code, GitHub Desktop y Actions | Desarrollado (código y pruebas) | BASE | 50 min |
| 2 | `PRE_02_mapreduce` | procesamiento distribuido, conteo de palabras, particionamiento | Desarrollado | BASE | 45 min |
| 3 | `PRE_03_csv2json` | formatos, transformación CSV→JSON, datos semiestructurados | Desarrollado | BASE | 30 min (observado) |
| 4 | `PRE_04_limpieza` | calidad, limpieza y diagnóstico de datos | Desarrollado | BASE | 50 min |
| 5 | `PRE_05_anonimizacion` | privacidad, anonimización y riesgo de reidentificación | Desarrollado | BASE | 50 min |
| 6 | `PRE_06_analisis_pandas` | tablas, exploración y resúmenes con pandas | Desarrollado | BASE | 50 min |
| 7 | `PRE_07_analisis_sqlite` | consulta analítica y SQLite | Desarrollado | BASE | 50 min |
| 8 | `PRE_08_analisis_chatgpt` | análisis asistido por IA generativa y verificación crítica | Desarrollado | BASE | 45 min |
| 9 | `PRE_09_visualiazacion` | visualización de datos, redes y mapas | Desarrollado | BASE | 60 min |
| 10 | `PRE_10_regresion_basica` | regresión y predicción básica | Desarrollado | BASE | 60 min |
| 11 | `PRE_11_clasificacion_basica_imagenes` | clasificación de imágenes | Desarrollado | OPT | 60 min |
| 12 | `PRE_12_clasificacion_basica_texto` | clasificación de texto | Desarrollado | OPT | 60 min |
| 13 | `PRE_13_clustering_demanda` | segmentación y clustering de demanda | Desarrollado | BASE | 60 min |
| 14 | `PRE_14_clustering_mercadeo` | segmentación de mercados | Desarrollado | OPT | 60 min |
| 15 | `PRE_15_deployment` | empaquetamiento y despliegue de un predictor | Desarrollado | OPT | 65 min |
| 16 | `PRE_16_series_de_tiempo` | pronóstico y evaluación de series temporales | Desarrollado | OPT | 90 min |
| 17 | `PRE_17_air_france_447` | planeación de búsqueda y decisión bajo incertidumbre | Desarrollado | BASE | 75 min |
| 18 | `PRE_18_airline_revenue_management` | asignación de capacidad e ingresos | Desarrollado | OPT | 75 min |
| 19 | `PRE_19_covid_hospital_capacity` | planeación de capacidad hospitalaria y escenarios | Desarrollado | OPT | 75 min |

Los PRE `BASE` heredados suman aproximadamente **11 h 15 min**. La capacidad práctica de 30 horas no implica llenar el resto con `OPT`: se destina a los nuevos PRE `BASE` necesarios para las unidades aún pendientes de `curriculum.md` y a la programación detallada.

## Cobertura frente a `curriculum.md`

| Unidad curricular | Evidencia heredada | Estado de cobertura |
|---|---|---|
| Analytics como creación de valor | No hay `PRE_*` inequívoco; corresponde principalmente a fundamentación teórica. | Pendiente de contraste teórico. |
| Encuadre de problemas | Casos de búsqueda, ingresos y capacidad lo sugieren. | Parcial, inferida. |
| Tipos de pregunta y límites de evidencia | Descripción, predicción y prescripción aparecen en actividades distintas. | Parcial; la distinción explícita no es verificable por nombres. |
| Datos como evidencia | Limpieza, anonimización, CSV/JSON, pandas y SQLite. | Cubierta en práctica. |
| Panorama descriptivo | Pandas, SQLite y visualización. | Cubierta en práctica. |
| Panorama predictivo | Regresión, clasificación, clustering y series. | Cubierta, con profundidad mayor que un panorama. |
| Panorama prescriptivo | Air France, revenue management y capacidad hospitalaria. | Cubierta, con profundidad mayor que un panorama. |
| Estrategia, gobierno y valor | No hay actividad inequívoca. | Pendiente. |
| Responsabilidad y colaboración | Anonimización y análisis con ChatGPT. | Parcial. |
| Nivelación para posgrado | Varias actividades aportan capacidades técnicas. | Cubierta, pero requiere posterior selección/ordenamiento. |

## Observación de inventario

El material heredado abarca ampliamente temas que el currículo macro reserva para cursos posteriores. Esta observación no ordena retirar ni mover actividades; señala una decisión que el trabajo individual deberá resolver al programar la función nivelatoria del curso.
