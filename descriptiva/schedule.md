# Inventario heredado — Analítica Descriptiva y Visualización de Datos

## Propósito y lectura

Este archivo inventaría material heredado de `PRE_*`; no propone una programación nueva ni modifica actividades. El orden sigue su numeración. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. La columna **Actividad** identifica cada taller y describe analíticamente la tarea que el estudiante realiza; esta descripción es la base para comparar el curso con otros programas y para evaluar su cobertura. **Desarrollado** se basa en artefactos visibles; **Enunciado/esqueleto** en pruebas o estructura sin solución/datos/entregables observables.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

El tiempo estimado incluye presentar datos, problema, razonamiento y solución; se registra solo para material desarrollado y se redondea a múltiplos de 5 minutos.

## Talleres `PRE_*`

| Orden | Actividad | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---:|
| 1 | `PRE_01_hola_mundo`: configurar y verificar el entorno de trabajo mediante la implementación y prueba de dos funciones Python que retornan cadenas de texto. | Desarrollado | BASE | 50 min |
| 2 | `PRE_02_word_count_mapreduce`: replicar archivos de texto, normalizar y tokenizar sus líneas, emitir pares palabra–conteo, ordenarlos, agregarlos y escribir el resultado con la estructura de salida de MapReduce. | Desarrollado | OPT | 45 min |
| 3 | `PRE_03_manejo_editor`: tomar el programa procedimental de `PRE_02_word_count_mapreduce`, usar las herramientas de VS Code para refactorizarlo en funciones y ejecutar sus pruebas para comprobar que conserva el resultado correcto. | Desarrollado | BASE | 50 min |
| 4 | `PRE_04_limpieza`: estandarizar una tabla de ventas mediante normalización de nombres de columnas, proveedores, países y ciudades; y conversión de fechas, montos, descuentos, pesos y precios unitarios. | Desarrollado | BASE | 50 min |
| 5 | `PRE_05_anonimizacion`: evaluar el riesgo de reidentificación al cruzar cuasiidentificadores con datos auxiliares y aplicar supresión, enmascaramiento, seudonimización y generalización de edad y ubicación. | Desarrollado | BASE | 50 min |
| 6 | `PRE_06_drivers_pandas`: integrar tablas de conductores y sus registros semanales, calcular promedios, totales y comparaciones con la media por conductor; generar una tabla resumen y un gráfico de los diez mayores kilometrajes. | Desarrollado | BASE | 50 min |
| 7 | `PRE_07_drivers_sqlite`: cargar las tablas de conductores y registros semanales en SQLite, crear vistas, consultar agregados y funciones de ventana, y generar una tabla resumen y un gráfico de los diez mayores kilometrajes. | Desarrollado | BASE | 50 min |
| 8 | `PRE_08_drivers_chatgpt`: analizar datos con apoyo de IA generativa y validar críticamente los resultados producidos. | Desarrollado | BASE | 45 min |
| 9 | `PRE_09_retail_sales`: cargar y validar órdenes de venta; calcular ventas brutas, devoluciones y ventas netas; diagnosticar meses, tipo de día, clientes, productos, categorías, canales y medios de pago; y priorizar segmentos para reducir devoluciones. | Desarrollado | BASE | 230 min |
| 10 | `PRE_10_vuelos`: cargar y explorar agregados reales de vuelos; validar su consistencia; calcular indicadores de demora, cancelación y minutos positivos; diagnosticar aerolíneas, día–hora y segmentos prioritarios; y analizar evolución mensual y estacionalidad. | Desarrollado | BASE | 320 min |
| 11 | `PRE_11_supply_chain`: cargar y validar entregas; convertir fechas y limpiar fletes sin interpretar textos operativos como cero; calcular cumplimiento, demora y valor expuesto; diagnosticar modos, países y segmentos país–modo; y evaluar la cobertura disponible para comparar costos logísticos. | Desarrollado | BASE | 320 min |
| 12 | `PRE_12_scopus`: analizar producción científica por año, fuentes, autores, palabras clave y países mediante frecuencias, mapas, matrices de coocurrencia, comunidades y redes. | Desarrollado | BASE | 245 min |
| 16 | `PRE_16_csv2json`: leer un archivo CSV con encabezados, convertir sus registros a una colección JSON y guardar el resultado mediante una interfaz de conversión. | Desarrollado | OPT | 45 min |
| 31 | `PRE_31_enigma`: taller disponible como enunciado/esqueleto; no hay artefactos suficientes para establecer la tarea analítica exacta. | Enunciado/esqueleto | OPT | — |
| 34 | `PRE_34_consultas_sql_en_mapreduce`: taller disponible como enunciado/esqueleto sobre consultas SQL en un flujo MapReduce. | Enunciado/esqueleto | OPT | — |
| 35 | `PRE_35_programacion_en_python_multiprocessing`: taller disponible como enunciado/esqueleto sobre paralelismo y procesamiento local en Python. | Enunciado/esqueleto | OPT | — |
| 99 | `PRE_99_word_count_pandas`: cargar líneas de múltiples archivos de texto en un DataFrame, limpiar el texto, separar las palabras, calcular sus frecuencias por agrupación y guardar el resultado tabulado. | Parcial (código/datos/pruebas; sin notebook o entrega visible) | OPT | — |

`PRE_10_vuelos` es `BASE` porque aporta una capacidad curricular requerida: diagnóstico descriptivo con indicadores, segmentación y análisis temporal. `PRE_09_retail_sales` y `PRE_11_supply_chain` complementan esa capacidad con diagnósticos comercial y operativo. Los tres tienen notebooks ejecutables y se usan como mini casos de principio a fin.

## Cobertura frente a `curriculum.md`

| Unidad curricular | Evidencia heredada | Estado de cobertura |
|---|---|---|
| Python para Analytics | PRE 01, 03 y 06: funciones Python, transformación tabular y análisis con Pandas. | Inventariada. |
| Pregunta descriptiva y contexto | PRE 10 formula indicadores de demora y los compara por aerolínea, día y hora; PRE 06/07 resumen horas y kilometraje por conductor. | Parcial. |
| Preparación analítica | PRE 04 normaliza valores y tipos de una tabla de ventas. | Inventariada. |
| Exploración univariada | PRE 10 calcula tasas de demora y cancelación; PRE 06/07 calculan promedios, mínimos, máximos y totales por conductor. | Parcial. |
| Exploración multivariada y diagnóstico | PRE 10 segmenta demoras por aerolínea, día y hora; PRE 06/07 comparan registros semanales con el promedio de cada conductor. | Parcial. |
| Gramática visual y percepción | PRE 10, PRE 12 y PRE 06/07 generan gráficos de barras, matriz, mapa y red; no se documentan criterios explícitos de percepción o accesibilidad. | Parcial. |
| Relaciones, espacio y tiempo | PRE 10 compara demoras por día, hora y mes; PRE 12 representa países y coocurrencias de afiliaciones. | Parcial. |
| Tableros e informes | No hay `PRE_*` inequívoco. | Pendiente. |
| Narrativa de evidencia | No hay actividad inequívoca. | Pendiente. |
| Representación responsable | PRE 05; IA generativa en PRE 08. | Parcial. |
