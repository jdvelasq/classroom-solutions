# Inventario heredado — Analítica Predictiva

## Propósito y lectura

Este archivo inventaría material heredado de `PRE_*`; no propone una programación nueva ni modifica actividades. El orden sigue su numeración; `PRE_covid19` y `PRE_sura` se registran como colecciones heredadas sin numeración estándar. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. El nivel se determina por artefactos visibles, no por auditoría semántica.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

El tiempo estimado incluye presentar datos, problema, razonamiento y solución; se registra solo para material desarrollado y se redondea a múltiplos de 5 minutos.

## Talleres `PRE_*`

| Orden | Actividad | Ideas o conceptos inferidos | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---|---:|
| 1 | `PRE_01_hola_mundo` | inducción: GitHub, resolución, pytest en VS Code, GitHub Desktop y Actions | Desarrollado | BASE | 50 min |
| 2 | `PRE_02_regresion_basica` | regresión y predicción | Desarrollado | BASE | 60 min |
| 3 | `PRE_03_clasificacion_basica_imagenes` | clasificación de imágenes | Desarrollado | OPT | 60 min |
| 4 | `PRE_04_clasificacion_basica_texto` | clasificación de texto | Desarrollado | OPT | 60 min |
| 5 | `PRE_05_clustering_demanda` | clustering de demanda | Desarrollado; referencia reportada de 50 min pendiente de confirmar numeración | BASE | 50 min* |
| 6 | `PRE_06_clustering_mercadeo` | clustering y segmentación | Desarrollado | OPT | 60 min |
| 7 | `PRE_07_deployment` | empaquetamiento/despliegue de predictor | Desarrollado | OPT | 65 min |
| 8 | `PRE_08_series_de_tiempo` | pronóstico y métricas temporales | Desarrollado | BASE | 90 min |
| 9 | `PRE_09_hiperparametros` | ajuste y selección de hiperparámetros | Desarrollado | BASE | 60 min |
| 10 | `PRE_10_pipelines` | pipeline de modelado | Desarrollado | BASE | 70 min |
| 11 | `PRE_11_selection_inputs_regresion` | selección de variables para regresión | Desarrollado | BASE | 60 min |
| 12 | `PRE_12_selection_inputs_clasificacion` | selección de variables para clasificación | Desarrollado | BASE | 60 min |
| 13 | `PRE_13_lasso` | regularización LASSO | Desarrollado | BASE | 60 min |
| 14 | `PRE_14_reduccion_dimensionalidad` | reducción de dimensionalidad | Desarrollado | BASE | 60 min |
| 15 | `PRE_15_estructura_mercado` | estructura de mercado; objetivo exacto pendiente | Desarrollado | OPT | 70 min |
| 16 | `PRE_16_tokenizacion` | tokenización y preparación de texto | Desarrollado | OPT | 60 min |
| 17 | `PRE_17_clasificacion` | clasificación; alcance exacto pendiente | Parcial (notebooks/datos/pruebas, sin entrega visible) | BASE | — |
| — | `PRE_covid19` | modelos epidemiológicos/SIR, según nombres de notebooks | Colección legado no normalizada | OPT | — |
| — | `PRE_sura` | notebooks heterogéneos de estadística, modelos y segmentación | Colección legado no normalizada | OPT | — |

\* Corresponde a la observación reportada para clustering de demanda; el repositorio usa el identificador `PRE_05` y la referencia recibida indicó `PRE_08`.

`PRE_17_clasificacion` es `BASE` aunque está parcial, porque se requiere una actividad de clasificación para la oferta. La oferta requiere además nuevos PRE `BASE` para encuadre predictivo, línea base, incertidumbre y costo de error; los `OPT` no sustituyen esas brechas.

## Cobertura frente a `curriculum.md`

| Unidad curricular | Evidencia heredada | Estado de cobertura |
|---|---|---|
| Flujo reproducible de modelado | PRE 01, 07, 10 | Parcial. |
| Encuadre predictivo y línea base | No hay actividad inequívoca. | Pendiente. |
| Incertidumbre y diseño de evaluación | Hiperparámetros y laboratorios de comparación lo sugieren. | Parcial, inferida. |
| Preparación y representación | Selección de variables, tokenización y pipelines. | Inventariada. |
| Regresión y pronóstico básico | PRE 02, 08, 11, 13. | Inventariada. |
| Clasificación y priorización | PRE 03, 04, 12, 17. | Inventariada. |
| Validación, selección y generalización | PRE 09–13. | Parcial; métricas/calibración no verificables. |
| Aprendizaje no supervisado | PRE 05, 06, 14. | Inventariada. |
| Pivote predictivo–causal | No hay actividad inequívoca. | Pendiente. |
| Uso responsable y documentación | No hay actividad inequívoca. | Pendiente. |
| Extensiones electivas | Imágenes, texto, series, SIR y colecciones Sura. | Inventariada como legado; requiere clasificación posterior. |
