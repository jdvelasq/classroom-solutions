# Inventario heredado — Analítica Descriptiva y Visualización de Datos

## Propósito y lectura

Este archivo inventaría material heredado de `PRE_*`; no propone una programación nueva ni modifica actividades. El orden sigue su numeración. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. **Desarrollado** se basa en artefactos visibles; **Enunciado/esqueleto** en pruebas o estructura sin solución/datos/entregables observables.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

El tiempo estimado incluye presentar datos, problema, razonamiento y solución; se registra solo para material desarrollado y se redondea a múltiplos de 5 minutos.

## Talleres `PRE_*`

| Orden | Actividad | Ideas o conceptos inferidos | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---|---:|
| 1 | `PRE_01_hola_mundo` | inducción: GitHub, resolución, pytest en VS Code, GitHub Desktop y Actions | Desarrollado | BASE | 50 min |
| 2 | `PRE_02_word_count_mapreduce` | conteo, partición y MapReduce | Desarrollado | OPT | 45 min |
| 3 | `PRE_03_word_count_pandas` | conteo y transformación tabular con pandas | Parcial (código/datos/pruebas; sin notebook o entrega visible) | OPT | — |
| 4 | `PRE_04_limpieza` | limpieza y calidad de datos | Desarrollado | BASE | 50 min |
| 7 | `PRE_07_anonimizacion` | anonimización y privacidad | Desarrollado | BASE | 50 min |
| 8 | `PRE_08_vuelos` | análisis de vuelos; concepto exacto pendiente de lectura | Parcial (notebook y pruebas, sin datos/entrega visibles) | BASE | — |
| 12 | `PRE_12_visualiazacion_scopus` | visualización de producción científica/redes | Desarrollado | BASE | 60 min |
| 15 | `PRE_15_csv2json` | formatos y conversión CSV→JSON | Desarrollado | OPT | 45 min |
| 27 | `PRE_27_pandas_drivers` | análisis tabular, resúmenes y visualización | Desarrollado | BASE | 50 min |
| 28 | `PRE_28_analisis_sqlite` | consultas y análisis con SQLite | Desarrollado | BASE | 50 min |
| 30 | `PRE_30_enigma` | caso por determinar a partir de su enunciado | Enunciado/esqueleto | OPT | — |
| 32 | `PRE_32_analisis_chatgpt` | análisis asistido por IA generativa y validación crítica | Desarrollado | BASE | 45 min |
| 33 | `PRE_33_consultas_sql_en_mapreduce` | integración de SQL y MapReduce | Enunciado/esqueleto | OPT | — |
| 34 | `PRE_34_programacion_en_python_multiprocessing` | paralelismo y procesamiento local | Enunciado/esqueleto | OPT | — |

`PRE_08_vuelos` es `BASE` porque aporta una capacidad curricular requerida, aunque está por completar y revisar. Se crearán otros PRE `BASE` para tableros, narrativa de evidencia y las demás brechas indicadas en la matriz.

## Cobertura frente a `curriculum.md`

| Unidad curricular | Evidencia heredada | Estado de cobertura |
|---|---|---|
| Python para Analytics | PRE 01, 03 y 27 | Inventariada. |
| Pregunta descriptiva y contexto | Casos de vuelos, drivers y Scopus lo sugieren. | Parcial, inferida. |
| Preparación analítica | PRE 04 | Inventariada. |
| Exploración univariada | Pandas/drivers y SQLite lo sugieren. | Parcial, inferida. |
| Exploración multivariada y diagnóstico | Pandas/drivers y vuelos podrían cubrirla. | Pendiente de lectura de notebooks. |
| Gramática visual y percepción | PRE 12 | Parcial; percepción no verificable. |
| Relaciones, espacio y tiempo | Scopus/redes y vuelos. | Parcial. |
| Tableros e informes | No hay `PRE_*` inequívoco. | Pendiente. |
| Narrativa de evidencia | No hay actividad inequívoca. | Pendiente. |
| Representación responsable | PRE 07; IA generativa en PRE 32. | Parcial. |
