# Inventario heredado — Analítica Predictiva

## Propósito y lectura

Este archivo inventaría material heredado de `PRE_*`; no propone una programación nueva ni modifica actividades. El orden sigue su numeración; `PRE_covid19` y `PRE_sura` se registran como colecciones heredadas sin numeración estándar. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. La columna **Actividad** identifica cada taller y describe analíticamente la tarea que el estudiante realiza; esta descripción es la base para comparar el curso con otros programas y para evaluar su cobertura. **Desarrollado** se basa en artefactos visibles; **Parcial** en notebooks, datos o pruebas sin un entregable verificable completo.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

El tiempo estimado incluye presentar datos, problema, razonamiento y solución; se registra solo para material desarrollado y se redondea a múltiplos de 5 minutos.

## Programación propuesta

| Orden | Taller | Tiempo | Acumulado |
|---:|---|---:|---:|
| 1 | `PRE_01_hola_mundo` — repositorio, entorno y pruebas automatizadas | 60 min | 60 min |
| 2 | `PRE_02_regresion_basica` — preparación de datos, regresión lineal, red neuronal y error de predicción | 150 min | 210 min |
| 3 | `PRE_03_clasificacion_basica_imagenes` — clasificación multiclase, probabilidades y matriz de confusión | 90 min | 300 min |
| 4 | `PRE_04_clasificacion_basica_texto` — bolsa de palabras y clasificación de sentimiento | 90 min | 390 min |
| 5 | `PRE_05_clustering_demanda` — perfiles temporales de demanda, K-means y silueta | 120 min | 510 min |
| 6 | `PRE_06_clustering_mercadeo` — segmentación con intereses, TF-IDF y caracterización de grupos | 120 min | 630 min |
| 7 | `PRE_07_deployment` — serialización de modelos, interfaz web y API de predicción | 120 min | 750 min |
| 8 | `PRE_08_series_de_tiempo` — rezagos, tendencia, estacionalidad, modelos y evaluación de pronósticos | 240 min | 990 min |
| 9 | `PRE_09_hiperparametros` — búsqueda y selección de hiperparámetros con validación | 100 min | 1.090 min |
| 10 | `PRE_10_pipelines` — preprocesamiento y clasificación encapsulados en pipelines | 120 min | 1.210 min |
| 11 | `PRE_11_selection_inputs_regresion` — selección de variables para regresión | 90 min | 1.300 min |
| 12 | `PRE_12_selection_inputs_clasificacion` — selección de variables para clasificación | 90 min | 1.390 min |
| 13 | `PRE_13_lasso` — regularización, trayectoria de coeficientes y validación cruzada | 90 min | 1.480 min |
| 14 | `PRE_14_reduccion_dimensionalidad` — PCA, t-SNE y UMAP para explorar estructura de clases | 90 min | 1.570 min |
| 15 | `PRE_15_estructura_mercado` — relaciones entre acciones, clustering y red de mercado | 120 min | 1.690 min |
| 16 | `PRE_16_tokenizacion` — limpieza, tokenización y filtrado de documentos | 90 min | 1.780 min |
| 17 | `PRE_17_clasificacion` — preparación de solicitudes de crédito y clasificación con bosque aleatorio | 180 min | 1.960 min |

## Talleres `PRE_*`

| Orden | Actividad | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---:|
| 1 | `PRE_01_hola_mundo`: configurar y verificar el entorno de trabajo mediante la implementación y prueba de dos funciones Python que retornan cadenas de texto. | Desarrollado | BASE | 50 min |
| 2 | `PRE_02_regresion_basica`: preparar el conjunto Auto MPG, separar entrenamiento y prueba, estandarizar entradas, comparar regresión lineal y una red neuronal para predecir consumo, y evaluar el error cuadrático medio. | Desarrollado | BASE | 60 min |
| 3 | `PRE_03_clasificacion_basica_imagenes`: transformar imágenes de dígitos en vectores, entrenar una regresión logística multiclase, evaluar exactitud y matriz de confusión, e inspeccionar predicciones y sus probabilidades. | Desarrollado | OPT | 60 min |
| 4 | `PRE_04_clasificacion_basica_texto`: vectorizar frases financieras con bolsa de palabras, entrenar un clasificador de sentimiento positivo, negativo o neutral, evaluar su exactitud y guardar el vectorizador y el modelo. | Desarrollado | OPT | 60 min |
| 5 | `PRE_05_clustering_demanda`: depurar y normalizar perfiles horarios diarios de demanda, seleccionar el número de grupos con silueta, agruparlos con K-means y describir los patrones y días asociados a cada grupo. | Desarrollado | BASE | 50 min |
| 6 | `PRE_06_clustering_mercadeo`: depurar e imputar perfiles de estudiantes, ponderar intereses con TF-IDF, segmentarlos con K-means y caracterizar cada segmento por intereses, edad, amistades, género y año de graduación. | Desarrollado | OPT | 60 min |
| 7 | `PRE_07_deployment`: entrenar y serializar un predictor lineal de precios de vivienda, y exponerlo mediante una interfaz web y una API con cliente de ejemplo. | Desarrollado | OPT | 65 min |
| 8 | `PRE_08_series_de_tiempo`: construir variables rezagadas sobre una serie mensual, ajustar y comparar modelos lineales y de red neuronal con transformaciones temporales, y exportar pronósticos y métricas. | Desarrollado | BASE | 90 min |
| 9 | `PRE_09_hiperparametros`: evaluar configuraciones de un modelo de predicción sobre calidad de vino, seleccionar hiperparámetros y guardar el estimador resultante. | Desarrollado | BASE | 60 min |
| 10 | `PRE_10_pipelines`: encapsular preprocesamiento de texto y clasificación en pipelines reproducibles, comparar sus configuraciones y guardar el estimador final. | Desarrollado | BASE | 70 min |
| 11 | `PRE_11_selection_inputs_regresion`: comparar subconjuntos de variables y seleccionar entradas para un modelo de regresión de consumo de combustible. | Desarrollado | BASE | 60 min |
| 12 | `PRE_12_selection_inputs_clasificacion`: preparar datos de enfermedad cardíaca, seleccionar variables de entrada para clasificación y guardar el estimador resultante. | Desarrollado | BASE | 60 min |
| 13 | `PRE_13_lasso`: ajustar regresión lineal y LASSO sobre datos de automóviles, analizar la trayectoria de coeficientes, seleccionar la penalización con validación cruzada y evaluar el error fuera de muestra. | Desarrollado | BASE | 60 min |
| 14 | `PRE_14_reduccion_dimensionalidad`: proyectar imágenes de dígitos en dos dimensiones mediante PCA, t-SNE y UMAP, y comparar visualmente la separación de sus clases. | Desarrollado | BASE | 60 min |
| 15 | `PRE_15_estructura_mercado`: integrar cotizaciones de acciones, estimar una red de dependencias con Graphical Lasso, agrupar empresas por afinidad y visualizar la estructura del mercado. | Desarrollado | OPT | 70 min |
| 16 | `PRE_16_tokenizacion`: cargar documentos de texto, normalizar y tokenizar su contenido, filtrar puntuación y palabras vacías, y guardar las versiones procesadas. | Desarrollado | OPT | 60 min |
| 17 | `PRE_17_clasificacion`: explorar y depurar solicitudes de tarjeta de crédito, codificar variables, entrenar un bosque aleatorio y evaluar sus predicciones con exactitud y matrices de confusión. | Parcial (notebooks/datos/pruebas, sin entrega visible) | BASE | — |
| — | `PRE_covid19`: colección de notebooks que construyen y aplican modelos SIR y Bass a datos epidemiológicos; no tiene la estructura ni entregables de un `PRE_*` estándar. | Colección legado no normalizada | OPT | — |
| — | `PRE_sura`: colección de notebooks heterogéneos sobre reglas de asociación, Bayes, clustering, k-NN, regresión, árboles y ensambles; no tiene la estructura ni entregables de un `PRE_*` estándar. | Colección legado no normalizada | OPT | — |

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
