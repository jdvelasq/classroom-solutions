# Inventario heredado — Analítica Predictiva

## Propósito y lectura

Este archivo inventaría material heredado de `PRE_*` y registra su programación. `PRE_08_covid` proviene de una colección heredada y queda incorporado en la secuencia por su aporte a la discusión de modelos mecanísticos; todavía requiere normalización para alcanzar el estándar de un PRE aprobado. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. La columna **Actividad** identifica cada taller y describe analíticamente la tarea que el estudiante realiza; esta descripción es la base para comparar el curso con otros programas y para evaluar su cobertura. **Desarrollado** se basa en artefactos visibles; **Parcial** en notebooks, datos o pruebas sin un entregable verificable completo.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

La secuencia establece prerrequisitos y relevancia curricular; no es una promesa de completar todos los PRE en cada cohorte. El docente avanza según la evidencia de comprensión y ejecución del grupo. Cada PRE completado debe producir un incremento de aprendizaje reconocible por sí mismo, y los PRE posteriores amplían ese incremento sin invalidarlo.

El tiempo estimado incluye presentar datos, problema, razonamiento y solución; es una referencia de planeación, no una cuota de cobertura por cohorte.

## Programación propuesta

| Orden | Taller | Tiempo | Acumulado |
|---:|---|---:|---:|
| 1 | `PRE_01_hola_mundo` — repositorio, entorno y pruebas automatizadas | 60 min | 60 min |
| 2 | `PRE_02_regresion_basica` — regresión lineal, red neuronal y error de predicción | 90 min | 150 min |
| 3 | `PRE_03_clasificacion_basica_imagenes` — clasificación multiclase y probabilidades | 75 min | 225 min |
| 4 | `PRE_04_clasificacion_basica_texto` — bolsa de palabras, sentimiento y desbalance | 90 min | 315 min |
| 5 | `PRE_05_clasificacion_basica_numerica` — logística, transformaciones e interacciones | 105 min | 420 min |
| 6 | `PRE_06_clustering_demanda` — perfiles temporales, normalización y K-means | 100 min | 520 min |
| 7 | `PRE_07_clustering_mercadeo` — segmentación y caracterización de grupos | 100 min | 620 min |
| 8 | `PRE_08_covid` — modelos SIR, supuestos y escenarios | 120 min | 740 min |
| 9 | `PRE_09_recomendacion_apriori` — reglas de asociación y cross-sell | 90 min | 830 min |
| 10 | `PRE_10_filtrado_colaborativo` — interacción cliente–ítem y recomendaciones top-*k* | 105 min | 935 min |
| 11 | `PRE_11_series_de_tiempo` — tendencia, estacionalidad y combinación de pronósticos | 180 min | 1.115 min |
| 12 | `PRE_12_deployment_web_app` — interfaz web para una predicción | 75 min | 1.190 min |
| 13 | `PRE_13_deployment_api` — API de predicción para otro sistema | 75 min | 1.265 min |
| 14 | `PRE_14_hiperparametros` — búsqueda y selección con validación | 75 min | 1.340 min |
| 15 | `PRE_15_pipelines` — preprocesamiento y clasificación encapsulados | 90 min | 1.430 min |
| 16 | `PRE_16_selection_inputs_regresion` — selección de variables para regresión | 75 min | 1.505 min |
| 17 | `PRE_17_selection_inputs_clasificacion` — selección de variables para clasificación | 75 min | 1.580 min |
| 18 | `PRE_18_lasso` — regularización y trayectoria de coeficientes | 75 min | 1.655 min |
| 19 | `PRE_19_reduccion_dimensionalidad` — PCA, t-SNE y UMAP | 75 min | 1.730 min |
| 20 | `PRE_20_estructura_mercado` — red de dependencias y estructura de mercado | 105 min | 1.835 min |
| 21 | `PRE_21_tokenizacion` — preparación de texto para modelado | 75 min | 1.910 min |
| 22 | `PRE_22_clasificacion` — riesgo de crédito y clasificación responsable | 120 min | 2.030 min |

## Talleres `PRE_*`

| Orden | Actividad | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---:|
| 1 | `PRE_01_hola_mundo`: configurar y verificar el entorno de trabajo mediante la implementación y prueba de dos funciones Python que retornan cadenas de texto. | Desarrollado | BASE | 50 min |
| 2 | `PRE_02_regresion_basica`: preparar el conjunto Auto MPG, separar entrenamiento y prueba, estandarizar entradas, comparar regresión lineal y una red neuronal para predecir consumo, y evaluar el error cuadrático medio. | Desarrollado | BASE | 60 min |
| 3 | `PRE_03_clasificacion_basica_imagenes`: transformar imágenes de dígitos en vectores, entrenar una regresión logística multiclase, evaluar exactitud y matriz de confusión, e inspeccionar predicciones y sus probabilidades. | Desarrollado | OPT | 60 min |
| 4 | `PRE_04_clasificacion_basica_texto`: vectorizar frases financieras con bolsa de palabras, entrenar un clasificador de sentimiento positivo, negativo o neutral, evaluar su exactitud y guardar el vectorizador y el modelo. | Desarrollado | OPT | 60 min |
| 5 | `PRE_05_clasificacion_basica_numerica`: usar dos mediciones numéricas disponibles antes de una evaluación adicional, comparar una logística base con una transformación de predictor y una interacción, y expresar la priorización como probabilidades sobre datos reservados. | Verificable | BASE | 105 min |
| 6 | `PRE_06_clustering_demanda`: depurar y normalizar perfiles horarios diarios de demanda, seleccionar el número de grupos con silueta, agruparlos con K-means y describir los patrones y días asociados a cada grupo. | Desarrollado | BASE | 50 min |
| 7 | `PRE_07_clustering_mercadeo`: depurar e imputar perfiles de estudiantes, ponderar intereses con TF-IDF, segmentarlos con K-means y caracterizar cada segmento por intereses, edad, amistades, género y año de graduación. | Desarrollado | OPT | 60 min |
| 8 | `PRE_08_covid`: colección de notebooks sobre modelos SIR y Bass para discutir modelos mecanísticos, supuestos epidemiológicos y escenarios; todavía no tiene la estructura ni entregables de un PRE estándar. | Parcial | BASE | — |
| 9 | `PRE_09_recomendacion_apriori`: reconstruir canastas de pólizas, derivar reglas de asociación y generar recomendaciones de cross-sell con soporte, confianza y lift. | Planificado | BASE | 90 min |
| 10 | `PRE_10_filtrado_colaborativo`: representar interacciones cliente–ítem, reservar interacciones, producir recomendaciones personalizadas y evaluar listas top-*k*. | Planificado | BASE | 105 min |
| 11 | `PRE_11_series_de_tiempo`: construir variables rezagadas sobre una serie mensual, ajustar y comparar modelos lineales y de red neuronal con transformaciones temporales, y exportar pronósticos y métricas. | Desarrollado | BASE | 90 min |
| 12 | `PRE_12_deployment_web_app`: entrenar y serializar un predictor lineal de precios de vivienda, y usarlo desde una interfaz web. | Desarrollado | OPT | 65 min |
| 13 | `PRE_13_deployment_api`: exponer un predictor mediante una API, enviar una solicitud desde un cliente y validar la respuesta. | Parcial | BASE | 75 min |
| 14 | `PRE_14_hiperparametros`: evaluar configuraciones de un modelo de predicción sobre calidad de vino, seleccionar hiperparámetros y guardar el estimador resultante. | Desarrollado | BASE | 60 min |
| 15 | `PRE_15_pipelines`: encapsular preprocesamiento de texto y clasificación en pipelines reproducibles, comparar sus configuraciones y guardar el estimador final. | Desarrollado | BASE | 70 min |
| 16 | `PRE_16_selection_inputs_regresion`: comparar subconjuntos de variables y seleccionar entradas para un modelo de regresión de consumo de combustible. | Desarrollado | BASE | 60 min |
| 17 | `PRE_17_selection_inputs_clasificacion`: preparar datos de enfermedad cardíaca, seleccionar variables de entrada para clasificación y guardar el estimador resultante. | Desarrollado | BASE | 60 min |
| 18 | `PRE_18_lasso`: ajustar regresión lineal y LASSO sobre datos de automóviles, analizar la trayectoria de coeficientes, seleccionar la penalización con validación cruzada y evaluar el error fuera de muestra. | Desarrollado | BASE | 60 min |
| 19 | `PRE_19_reduccion_dimensionalidad`: proyectar imágenes de dígitos en dos dimensiones mediante PCA, t-SNE y UMAP, y comparar visualmente la separación de sus clases. | Desarrollado | BASE | 60 min |
| 20 | `PRE_20_estructura_mercado`: integrar cotizaciones de acciones, estimar una red de dependencias con Graphical Lasso, agrupar empresas por afinidad y visualizar la estructura del mercado. | Desarrollado | OPT | 70 min |
| 21 | `PRE_21_tokenizacion`: cargar documentos de texto, normalizar y tokenizar su contenido, filtrar puntuación y palabras vacías, y guardar las versiones procesadas. | Desarrollado | OPT | 60 min |
| 22 | `PRE_22_clasificacion`: explorar y depurar solicitudes de tarjeta de crédito, codificar variables, entrenar un bosque aleatorio y evaluar sus predicciones con exactitud y matrices de confusión. | Parcial (notebooks/datos/pruebas, sin entrega visible) | BASE | — |
| — | `PRE_sura`: colección de notebooks heterogéneos sobre reglas de asociación, Bayes, clustering, k-NN, regresión, árboles y ensambles; no tiene la estructura ni entregables de un `PRE_*` estándar. | Colección legado no normalizada | OPT | — |

`PRE_22_clasificacion` es `BASE` aunque está parcial, porque se requiere una actividad de clasificación para la oferta. La oferta requiere además nuevos PRE `BASE` para encuadre predictivo, línea base, incertidumbre y costo de error; los `OPT` no sustituyen esas brechas.

## Cobertura frente a `curriculum.md`

| Unidad curricular | Evidencia heredada | Estado de cobertura |
|---|---|---|
| Flujo reproducible de modelado | PRE 01, 12, 15 | Parcial. |
| Encuadre predictivo y línea base | No hay actividad inequívoca. | Pendiente. |
| Incertidumbre y diseño de evaluación | Hiperparámetros y laboratorios de comparación lo sugieren. | Parcial, inferida. |
| Preparación y representación | Selección de variables, tokenización y pipelines. | Inventariada. |
| Regresión y pronóstico básico | PRE 02, 11, 16, 18. | Inventariada. |
| Clasificación y priorización | PRE 03–05, 17, 22. | Inventariada. |
| Validación, selección y generalización | PRE 14–18. | Parcial; métricas/calibración no verificables. |
| Recomendación y ranking | PRE 09–10. | Planificada; pendiente de implementación. |
| Aprendizaje no supervisado | PRE 06, 07, 19. | Inventariada. |
| Pivote predictivo–causal | No hay actividad inequívoca. | Pendiente. |
| Uso responsable y documentación | No hay actividad inequívoca. | Pendiente. |
| Extensiones electivas | Imágenes, texto, series, SIR y estructura de mercado. | Inventariada; SIR aún requiere normalización. |
