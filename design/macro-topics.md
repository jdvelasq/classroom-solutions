# Diseño macro de temas — iteración 2

## Propósito y alcance

Este documento traduce el benchmark internacional consolidado en `design/synthesis.md` al conjunto de seis cursos reales bajo alcance. Define **temas macro**, no todavía el calendario de sesiones, lecturas, talleres ni evaluaciones. El contenido actual de las carpetas de curso no se usa como insumo ni como restricción para este diseño.

El diseño debe cubrir de forma complementaria el ciclo completo:

```text
problema y valor → datos confiables → evidencia descriptiva → modelo y efecto
→ decisión → producto → operación responsable
```

Las definiciones de producto de datos y las fronteras no negociables entre los cursos se desarrollan en [conceptual-boundaries.md](conceptual-boundaries.md). Son parte de esta especificación y prevalecen sobre interpretaciones basadas en herramientas.

El contraste específico de este diseño con los programas de educación continua del corpus está documentado en [benchmark-real-courses.md](benchmark-real-courses.md).

El curso de posgrado *Big Data Analytics* está excluido: no cubre vacíos, no provee prerrequisitos y no se usa para justificar omisiones.

## Rúbrica de contraste con el benchmark

Cada diseño se califica sobre 10 a partir de cinco criterios de dos puntos:

1. **Cobertura esencial:** trata los temas que el benchmark identifica como irrenunciables para la pregunta propia del curso.
2. **Identidad y profundidad:** la pregunta rectora, el entregable y las exclusiones hacen que el curso desarrolle una competencia propia, no una lista de herramientas o una versión reducida de otra disciplina.
3. **Fronteras:** no duplica el dominio de otro curso ni deja una transición sin responsable.
4. **Ciclo profesional:** conecta el contenido con una entrega, decisión o producto verificable.
5. **Responsabilidad transversal:** incorpora reproducibilidad, comunicación, calidad, ética, privacidad y seguridad en la profundidad pertinente.

Una calificación de 10 significa que el **diseño macro** satisface esta rúbrica; no certifica aún la calidad de la implementación, que se validará en la programación detallada.

## Contrato de identidad del programa

| Curso | Pregunta rectora | Entregable propio | Exclusión que protege su identidad |
|---|---|---|---|
| Fundamentos de Analítica | ¿Cuál es la pregunta correcta y qué tipo de analítica puede crear valor responsablemente? | Encargo analítico bien formulado, con criterios de valor, riesgo y éxito; nivel mínimo común para el ingreso práctico a posgrado. | No domina las técnicas de Descriptiva, Predictiva o Prescriptiva: sus `PRE_*` nivelan y sitúan esas técnicas antes de que el posgrado las desarrolle. |
| Fundamentos de Datos para Analítica | ¿Cómo se hacen confiables y disponibles los datos para un consumidor analítico? | Datos curados, documentados y verificables, con su arquitectura y contrato de calidad. | No entrega un producto analítico a usuario final ni asume su operación completa. |
| Analítica Descriptiva y Visualización | ¿Qué ocurre en los datos y qué evidencia lo sustenta? | Evidencia explorada, contextualizada y comunicada con límites claros. | No es Estadística básica, ni predice, ni recomienda acciones. |
| Analítica Predictiva | ¿Qué puede anticiparse y con qué desempeño, incertidumbre y condiciones? | Predicción validada y documentada, o evidencia de que no es posible predecir útilmente. | No es una colección de algoritmos de ML ni convierte predicciones en decisiones. |
| Analítica Prescriptiva | ¿Qué se debería hacer dadas metas, restricciones, incertidumbre y efectos? | Política, plan o recomendación defendible con escenarios y sensibilidad. | No es una formación exhaustiva en Investigación de Operaciones ni una interfaz de producto. |
| Productos de Datos | ¿Cómo se empaqueta, entrega, gobierna y evoluciona una capacidad de datos o analítica para un consumidor? | Producto de datos o producto analítico con consumidor, contrato, propiedad y operación verificable. | No es Ingeniería de Software general ni certificación de una herramienta MLOps/DataOps. |

Todo tema propuesto debe superar esta prueba: debe aportar directamente a la pregunta rectora y al entregable del curso, y no debe pertenecer con mayor propiedad a la exclusión indicada.

## Diseño tentativo de temas macro

### 1. Fundamentos de Analítica

**Pregunta rectora:** ¿cómo convertir una situación organizacional ambigua en una pregunta analítica responsable, útil y evaluable?

1. Analítica como ciclo de creación de valor: problema, datos, evidencia, modelo, decisión, producto y operación.
2. Formulación y reformulación de problemas: actores, decisión, objetivo, restricciones, métricas de éxito y riesgos de una mala formulación.
3. Tipos de pregunta y de evidencia: descripción, diagnóstico, predicción, causalidad y prescripción; sesgos de decisión y el papel de la experimentación; qué puede y qué no puede concluirse de cada una.
4. Alfabetización de datos para analítica: fuentes, calidad, sesgo, privacidad, trazabilidad y límites de datos observacionales.
5. Panorama práctico de evidencia descriptiva: resumen, exploración y visualización como apoyo a una pregunta, sin convertir el curso en Descriptiva.
6. Panorama práctico de modelado: regresión, clasificación, agrupamiento y pronóstico como familias de problemas, sin desarrollar sus algoritmos.
7. Panorama práctico de decisión: optimización, simulación y análisis de escenarios como formas de actuar con evidencia, sin desarrollar teoría de investigación de operaciones.
8. Valor, estrategia y gobierno de datos: caso de valor, priorización de iniciativas, derechos de decisión, capacidades organizacionales y adopción.
9. Responsabilidad profesional: sesgo, privacidad, propiedad intelectual, seguridad y supervisión humana desde el encuadre inicial.
10. Reproducibilidad, comunicación y colaboración: evidencia auditable, interpretación para públicos distintos y uso crítico de IA generativa.

**Frontera:** introduce el mapa y el criterio de elección; no domina programación, EDA, estadística, ingeniería de datos, ML, optimización ni despliegue.

**Función de articulación:** los `PRE_*` de este curso se diseñan como sesiones iniciales y nivelatorias para los cursos de posgrado. Cada uno establece una competencia mínima, lenguaje común y caso de referencia, que el curso de posgrado correspondiente retoma con profundidad propia; no se interpreta como una versión comprimida del curso de posgrado.

### 2. Fundamentos de Datos para Analítica

**Pregunta rectora:** ¿cómo transformar fuentes heterogéneas en datos confiables, reproducibles y utilizables por consumidores analíticos?

1. Papel de la ingeniería de datos en el ciclo analítico: fuentes, consumidores, arquitectura, confiabilidad, escala y costo.
2. Representación y modelado mínimo para analítica: tablas, claves, relaciones, integridad y SQL de nivelación.
3. Integración y transformación reproducible: joins, agregaciones, ventanas, deduplicación, tipado, manejo de faltantes y capas raw/staging/curated.
4. Almacenamiento analítico y formatos: OLTP/OLAP, hechos y dimensiones, warehouse, lake y lakehouse; CSV/JSON/Parquet, partición y selección de estructura por necesidad.
5. Ingestión por lote y API: extracción, paginación, parámetros, manejo de errores, persistencia e idempotencia.
6. Pipelines: ETL/ELT, configuración, dependencias, incrementales, backfills y trazabilidad de la transformación.
7. Calidad de datos y contratos: reglas de completitud, validez, unicidad, consistencia y frescura; esquemas, evolución, cuarentena y fallo controlado.
8. Escala y eventos: procesamiento distribuido, eventos, tiempo de evento, ventanas y streaming, enseñados como decisiones arquitectónicas y no como certificación de herramientas.
9. Serving, metadatos y gobierno técnico: datasets curados, catálogos, linaje, propiedad, acceso y privacidad.
10. Arquitectura integral: diagnóstico de una arquitectura, trade-offs y propuesta de mejora que entregue datos aptos para Descriptiva, Predictiva y Productos.

**Frontera:** diseña y produce datos confiables; no diseña interfaces de producto ni industrializa el ciclo completo de un producto en producción.

### 3. Analítica Descriptiva y Visualización de Datos

**Pregunta rectora:** ¿qué está ocurriendo en los datos, cuán confiable es esa lectura y cómo comunicarla sin inducir conclusiones indebidas?

1. Pregunta descriptiva, unidad de análisis, población, granularidad, contexto de decisión y criterios de una exploración útil.
2. Preparación analítica de datos: estructura tabular, tipos, faltantes, duplicados, valores atípicos y bitácora reproducible de limpieza; la ingeniería de origen pertenece a Datos.
3. EDA univariado y multivariado: distribuciones, asociaciones, segmentación, cohortes, comparaciones y detección de patrones/anomalías; diagnóstico guiado por hipótesis, sin atribuir causalidad.
4. Resumen cuantitativo y variabilidad: estadísticos descriptivos, tasas, proporciones, escalas y límites de agregación; la inferencia formal pertenece a Predictiva en este conjunto real.
5. Gramática de gráficos y percepción: codificación visual, escala, color, orden, anotación, accesibilidad y selección de gráfico según pregunta.
6. Visualización de relaciones, espacio y tiempo: series y cambios, mapas cuando el espacio importa, redes y datos textuales solo cuando son evidencia pertinente.
7. Tableros e informes: jerarquía de información, interacción, filtros, definición de métricas y prevención de tableros que ocultan incertidumbre o decisiones.
8. Narrativa y comunicación de evidencia: argumento, audiencia, recomendación proporcionada a la evidencia y comunicación de limitaciones.
9. Privacidad, sesgo y ética de representación: anonimización, riesgo de reidentificación, grupos invisibilizados y visualizaciones engañosas.
10. Caso autocontenido de evidencia descriptiva: informe o tablero reproducible que responda una pregunta real y entregue un hallazgo trazable a Predictiva, Prescriptiva o Productos.

**Frontera:** describe y comunica patrones; no usa ajuste predictivo para prometer resultados futuros ni interpreta asociación como efecto causal.

### 4. Analítica Predictiva

**Pregunta rectora:** ¿qué puede anticiparse con datos y bajo qué condiciones una predicción deja —o no— justificar una intervención?

1. Encuadre predictivo: unidad de predicción, horizonte, variable objetivo, costo de error, línea base y protocolo de evaluación.
2. Base estadística aplicada: muestreo, variabilidad, partición temporal o aleatoria, incertidumbre de métricas y prevención de fugas de información.
3. Preparación y representación para modelos: codificación, transformaciones, imputación, ingeniería y selección de variables, con trazabilidad.
4. Regresión y pronóstico básico: ajuste, supuestos operativos, error, regularización y evaluación según el contexto.
5. Clasificación y priorización: probabilidades, umbrales, matrices de confusión, precisión/recall, ROC/PR, calibración y costo de falsos positivos/negativos.
6. Validación y generalización: validación cruzada, selección/ajuste de hiperparámetros, sobreajuste, comparación justa y monitoreo de desempeño fuera de muestra.
7. Aprendizaje no supervisado: clustering y reducción de dimensionalidad como exploración estructurada, con validación sustantiva y sin tratarlos como verdades descubiertas. Aprendizaje profundo, recomendadores, grafos y series de tiempo avanzadas quedan como extensiones electivas, no como núcleo.
8. Pivote predicción → causalidad: correlación, confusión, sesgo de selección, aleatorización, A/B testing y estudios observacionales; distinguir "predecir" de "cambiar".
9. Equidad, interpretabilidad y documentación: análisis de subgrupos, explicaciones adecuadas al uso, privacidad y límites de automatización.
10. Caso autocontenido reproducible: modelo validado, ficha de modelo, evidencia de desempeño y condiciones de traspaso a Prescriptiva o Productos; operación continua pertenece a Productos.

**Frontera:** entrega estimaciones y, cuando procede, evidencia causal; Prescriptiva define la función de valor y escoge acciones.

### 5. Analítica Prescriptiva

**Pregunta rectora:** ¿qué acción conviene tomar, dadas restricciones, incertidumbre, valor y consecuencias para las partes afectadas?

1. De la predicción a la decisión: decisión, alternativas, restricciones, objetivos, función de valor y responsables de la elección.
2. Formulación de modelos de optimización: variables de decisión, parámetros, restricciones, objetivos y verificación de unidades/supuestos.
3. Optimización determinista para asignación, mezcla, cobertura, capacidad, redes y programación; interpretación de factibilidad y solución, no demostración formal de algoritmos de IO.
4. Decisión bajo incertidumbre: escenarios, distribuciones, riesgo, robustez y valor de información.
5. Simulación Monte Carlo y de eventos cuando la dinámica del sistema o la incertidumbre hacen insuficiente una solución cerrada.
6. Análisis de sensibilidad y *tradespace*: qué cambia la recomendación, cuáles son los inductores de valor y cuándo la decisión deja de ser robusta.
7. Optimización basada en datos: cómo usar pronósticos, probabilidades o efectos causales sin confundir su incertidumbre con certeza de la recomendación.
8. Factores humanos, equidad y explicabilidad de la decisión: automatización apropiada, revisión humana y consecuencias distributivas.
9. Comunicación ejecutiva de decisiones: política recomendada, alternativas descartadas, supuestos, riesgos, plan de contingencia y métricas de seguimiento.
10. Caso autocontenido: una política o plan reproducible, con sus supuestos, escenarios y recomendaciones para un decisor.

**Frontera:** determina una política o recomendación defendible; no resuelve el diseño de interfaz, MVP, adopción ni operación del producto.

### 6. Productos de Datos

**Pregunta rectora:** ¿cómo entregar, operar y evolucionar de forma confiable una capacidad analítica que aporte valor a un usuario?

1. Las dos acepciones de producto de datos: activo de datos curado para un consumidor y capacidad analítica que habilita observar, predecir, decidir o actuar; consumidor, propiedad, contrato y propuesta de valor.
2. Descubrimiento y diseño de producto: necesidad, decisión o tarea, actores, hipótesis de valor, requisito funcional/no funcional, medida de adopción, interacción humano–IA, supervisión humana y límite de uso responsable.
3. Ciclo de vida MLOps/DataOps: del experimento al servicio y de allí al monitoreo, mejora o retiro; relación entre Tubería de Innovación y Tubería de Valor.
4. Reproducibilidad y trazabilidad: versionado de código, datos, modelos, configuraciones y prompts; registro de experimentos, artefactos y linaje. MLflow es un ejemplo histórico posible, no el objeto del curso.
5. Empaquetamiento y entrega: servicios, APIs, contratos de entrada/salida, ambientes, contenerización y despliegue reproducible como medios para entregar una capacidad analítica.
6. Calidad y pruebas: validación de datos, lógica y modelos; pruebas unitarias, de integración, regresión, desempeño y humo; automatización de controles de calidad.
7. Operación y observabilidad: métricas de servicio y de valor, monitoreo de datos/modelos, deriva, alertas, incidentes, recalibración y retiro seguro.
8. Gobierno y seguridad operacional: acceso, privacidad, secretos, auditoría, aprobación humana, documentación y trazabilidad de decisiones.
9. Lean, Agile y DataOps: flujo de valor, priorización, trabajo en equipos multidisciplinarios, entrega continua y eliminación de heroísmo; tendencias como evaluación y operación responsable de LLM/RAG/agentes cuando el caso lo requiera.
10. Casos pequeños autocontenidos: cada `PRE_*` simplifica una situación real para el aula y recorre una porción completa y verificable del ciclo (por ejemplo, consumidor→contrato→entrega; experimento→registro→empaquetamiento; servicio→monitoreo→respuesta a deriva), sin proyecto integrador acumulativo.

**Frontera:** este es el curso que domina el producto, su entrega y su operación; recibe una capacidad analítica ya definida y no vuelve a enseñar EDA, modelado u optimización. No es ingeniería de software: las prácticas de construcción se tratan solo cuando hacen posible un contrato de datos, una experiencia de consumo, calidad, seguridad, observabilidad o evolución de la capacidad analítica.

## Reevaluación de la iteración 2

| Curso | Cobertura | Foco | Fronteras | Ciclo profesional | Responsabilidad | Calificación | Estado |
|---|---:|---:|---:|---:|---:|---:|---|
| Fundamentos de Analítica | 2 | 2 | 2 | 2 | 2 | **10** | Enmarca, prioriza y diferencia; los panoramas técnicos se limitan al criterio de elección, no a la enseñanza de métodos. |
| Fundamentos de Datos para Analítica | 2 | 2 | 2 | 2 | 2 | **10** | Responde por disponibilidad, confiabilidad, contrato y gobierno técnico de los datos; no por la experiencia final de producto. |
| Analítica Descriptiva y Visualización de Datos | 2 | 2 | 2 | 2 | 2 | **10** | La estadística descriptiva es lenguaje de evidencia, no el objeto del curso; el dominio es exploración, representación y comunicación. |
| Analítica Predictiva | 2 | 2 | 2 | 2 | 2 | **10** | El modelado se subordina a encuadre, validación, incertidumbre, costo de error y límite causal. |
| Analítica Prescriptiva | 2 | 2 | 2 | 2 | 2 | **10** | Optimización y simulación se usan para construir decisiones con datos, restricciones y consecuencias; no como estudio exhaustivo de IO. |
| Productos de Datos | 2 | 2 | 2 | 2 | 2 | **10** | Distingue activo de datos y producto analítico; MLOps/DataOps habilitan valor, contrato y operación, sin convertirlo en Ingeniería de Software. |

## Cierre de esta iteración

El conjunto alcanza 10 en el nivel macro porque cada competencia esencial tiene un curso responsable y las exclusiones evitan que las técnicas borren su identidad disciplinar. La integración se obtiene mediante fronteras, vocabulario y prácticas reproducibles compartidas; no depende de un proyecto integrador. La siguiente fase convertirá estos bloques en fundamentos y talleres `PRE_*` de situaciones reales simplificadas, autocontenidos y de duración variable.
