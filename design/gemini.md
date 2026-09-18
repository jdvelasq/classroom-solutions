# Propuesta de Arquitectura Curricular en Analítica (Analytics)
**Diseñador Curricular:** Gemini  
**Fecha de Regeneración:** 17 de Septiembre de 2026  
**Base Documental Exclusiva:** Corpus documental en `./curriculum/` (31 documentos PDF verificados)

---

# 1. Lectura global del corpus

### 1.1. La concepción de Analítica que emerge del corpus
El análisis exhaustivo del corpus documental revela que la **Analítica (Analytics)** no es una rama subordinada de las ciencias de la computación, ni un sinónimo cosmético de *Machine Learning*, ni una extensión avanzada del *Business Intelligence* tradicional, ni la aplicación aislada de la Investigación Operativa clásica. La Analítica se constituye como una **disciplina integradora y orientada a la toma de decisiones**, cuyo propósito fundamental es cerrar la brecha entre los datos disponibles y la generación sostenible de valor en las organizaciones.

A partir de los marcos académicos y profesionales analizados (en particular **INFORMS Analytics Framework 2024**, **INFORMS CAP Blueprints**, **ACM Computing Competencies 2021**, **National Academies 2018**, **UC Berkeley DATA C101/C102**, **MIT IDSS** y la serie metodológica **DataOps**), la Analítica se define como un ciclo de vida continuo y sistemático estructurado en torno a una cadena de valor ininterrumpida:

$$\text{Problema de Negocio} \longrightarrow \text{Encuadre Analítico} \longrightarrow \text{Ingeniería de Datos} \longrightarrow \text{Evidencia Descriptiva} \longrightarrow \text{Inferencia y Predicción} \longrightarrow \text{Prescripción y Decisión} \longrightarrow \text{Producto de Datos} \longrightarrow \text{Operacionalización (DataOps)} \longrightarrow \text{Valor Organizacional}$$

Esta cadena exige que el profesional en Analítica posea una triple identidad:
1. **Traductor y estratega de negocio**, capaz de formular preguntas estructuradas a partir de la ambigüedad estratégica y de evaluar el impacto económico y ético de las intervenciones.
2. **Científico e inferenciador riguroso**, capaz de razonar bajo incertidumbre, distinguir entre patrones correlacionales y mecanismos causales, y formular modelos matemáticos, predictivos y prescriptivos válidos.
3. **Ingeniero de sistemas analíticos**, capaz de construir soluciones robustas, automatizadas, reproducibles y monitoreables que se integren de manera orgánica en los flujos operativos y de decisión de la organización.

### 1.2. El impacto material de los documentos de DataOps
La incorporación de los diez documentos de la serie DataOps (`dataops-01-the-problem.pdf` a `dataops-10-organization.pdf`) **altera de forma profunda y sustancial la concepción de Analítica** que se derivaría de una lectura aislada del resto del corpus:

* **Superación del "Mito del Modelo Omnisciente" y la "Falacia del Cuaderno"**: Los documentos `dataops-01-the-problem.pdf` y `dataops-03-methodologies.pdf` demuestran que el fracaso endémico de las iniciativas de ciencia de datos no proviene de una falta de sofisticación matemática o algorítmica, sino de la desconexión operativa entre el modelo y el sistema productivo. La práctica convencional de desarrollar prototipos en cuadernos interactivos (*notebooks*) aislados, siguiendo modelos en cascada o variantes ingenuas de CRISP-DM, genera deuda técnica masiva, trabajo mundano repetitivo y dependencia del "heroísmo" individual (horas extras, fines de semana).
* **Dualidad de Tuberías (Value Pipeline vs. Innovation Pipeline)**: A partir de la adaptación de *Lean Thinking* (`dataops-04-lean-thinking.pdf`), el corpus establece que un sistema analítico moderno opera simultáneamente bajo dos lógicas complementarias:
  1. La **Tubería de Valor** (*Value Pipeline*): análoga a una planta de manufactura esbelta, donde los datos fluyen continuamente desde las fuentes hacia los consumidores finales, requiriendo calidad impecable, monitoreo en tiempo real y cero defectos.
  2. La **Tubería de Innovación** (*Innovation Pipeline*): análoga al desarrollo ágil de productos, donde los científicos e ingenieros experimentan con nuevas hipótesis, variables y algoritmos para introducir cambios en la tubería de valor sin comprometer su estabilidad.
* **"Analytics is Code" y Calidad de Datos Continua**: `dataops-09-data-quality.pdf` y `dataops-06-definition.pdf` introducen el principio no negociable de que toda solución analítica es código y, por ende, debe regirse por el rigor de la ingeniería de software moderna (control de versiones, ramificación, pruebas automatizadas, parametrización y ambientes aislados). Sin embargo, el corpus aclara la diferencia irreductible entre DevOps y DataOps: mientras en DevOps el código es variable pero el entorno de ejecución y los datos de prueba son controlables y fijos, en DataOps tanto el código como los datos son variables y cambiantes. Esto exige una disciplina de pruebas dual: pruebas sobre la lógica del código (unitarias, integración, regresión) y pruebas continuas sobre los datos (pruebas de balance, integridad referencial, frescura y deriva).
* **Reconceptualización de la Ingeniería de Datos y de los Productos de Datos**: La Ingeniería de Datos ya no puede ser concebida como mera administración de bases de datos o soporte pasivo de infraestructura; es la disciplina encargada de diseñar la cadena de suministro de datos (*data supply chain*) y la arquitectura canónica (`dataops-08-data-scientids.pdf`). Asimismo, los Productos de Datos dejan de ser vistos como tableros estáticos (*dashboards*) para entenderse como aplicaciones complejas que combinan tuberías de datos, modelos, lógica de negocio e interfaces de decisión (`dataops-06-definition.pdf`, `mit-designing-and-building-ai-products-and-services.pdf`).
* **Coordinación Relacional y Topología Organizacional**: Los documentos `dataops-07-cdo.pdf` y `dataops-10-organization.pdf` evidencian que los silos entre TI, ingeniería de datos, ciencia de datos y las áreas de negocio son la principal causa de desconfianza y retrasos. La solución exige coordinación relacional, tableros de control operativos de DataOps y estructuras organizacionales fluidas (equipos orientados a producto/dominio complementados por capítulos funcionales).

En conclusión, la evidencia de DataOps transforma la Analítica de ser un ejercicio puramente matemático-exploratorio a ser una **disciplina de ingeniería de sistemas de decisión y productos de datos de misión crítica**.

---

# 2. Competencias que debe desarrollar la cadena completa

Un egresado de un programa de Analítica integral debe poseer nueve grandes familias de competencias que abarcan la totalidad del ciclo de vida analítico:

### Familia 1: Encuadre Estratégico y Traducción de Problemas de Decisión
* Capacidad para identificar, desglosar y reformular problemas de negocio o institucionales ambiguos en preguntas analíticas estructuradas, precisas y tratables (INFORMS Dominios I y II).
* Formulación de casos de valor (*value cases*) sustentados, definiendo la línea base de desempeño (*baseline*), los indicadores clave de éxito (KPIs) y los criterios de aceptación técnica y económica (`dataops-02-data-strategy.pdf`).
* Alineación de las iniciativas de datos con la estrategia organizacional, evaluando la viabilidad analítica, los riesgos y las restricciones organizacionales (`dataops-02-data-strategy.pdf`, `cambridge-business-analytics.pdf`).

### Familia 2: Ingeniería de Datos, Modelamiento y Tuberías a Escala
* Diseño de modelos de datos conceptuales, lógicos y físicos adaptados a requerimientos analíticos (modelos relacionales, dimensionales, semiestructurados y columnares) (ACM DG, Berkeley DATA C101, MIT Data Engineering).
* Construcción y orquestación de tuberías de datos reproducibles y escalables (ETL/ELT) para la ingestión, limpieza, transformación y enriquecimiento de datos masivos y heterogéneos.
* Tratamiento de la preparación y limpieza de datos como un proceso de ingeniería determinista y automatizado, erradicando los scripts ad-hoc manuales (`dataops-08-data-scientids.pdf`).
* Implementación de arquitecturas de datos canónicas y modernas (Data Lake, Data Warehouse, Lakehouse) que sustenten la cadena de suministro de datos de la organización (`dataops-06-definition.pdf`, `dataops-08-data-scientids.pdf`).

### Familia 3: Exploración, Síntesis Descriptiva y Comunicación de Evidencia
* Ejecución de análisis exploratorio de datos (EDA) para identificar patrones, distribuciones, anomalías y relaciones multivariadas sin incurrir en conclusiones espurias (USC, Warwick, National Academies).
* Diseño de visualizaciones y síntesis analíticas efectivas fundamentadas en principios de percepción visual, ergonomía cognitiva y diseño de información (PwC, Cambridge).
* Comunicación persuasiva, rigurosa y adaptada a audiencias directivas y operativas, traduciendo evidencia estadística en narrativas accionables (*data storytelling*) que faciliten la toma de decisiones.

### Familia 4: Inferencia Estadística, Causalidad y Razonamiento bajo Incertidumbre
* Dominio de los fundamentos probabilísticos de la inferencia, contrastando y aplicando marcos frecuentistas y bayesianos para la estimación de parámetros y cuantificación de la incertidumbre (Berkeley DATA C102, National Academies).
* Formulación y evaluación de pruebas de hipótesis rigurosas, con control estricto de tasas de error múltiple y tasa de descubrimientos falsos (FDR) (Berkeley DATA C102).
* Distinción conceptual y matemática formal entre asociación estadística ($P(Y|X)$) e intervención causal ($P(Y|\text{do}(X))$), aplicando diagramas causales (DAGs), diseño experimental riguroso (A/B testing) y métodos cuasi-experimentales (variables instrumentales, regresión discontinua, diferencias en diferencias, emparejamiento) para evaluar el impacto real de políticas y decisiones.

### Familia 5: Modelamiento Predictivo y Aprendizaje Estadístico
* Selección, entrenamiento, calibración y evaluación crítica de algoritmos de aprendizaje supervisado (regresión lineal/logística regularizada, árboles de decisión, ensambles, redes neuronales) y no supervisado (agrupamiento, reducción de dimensionalidad) (MIT DSML, ACM ML).
* Comprensión profunda del compromiso sesgo-varianza (*bias-variance tradeoff*), generalización fuera de muestra, validación cruzada y métricas de desempeño alineadas con los costos asimétricos de error en el negocio (INFORMS Dominio V).
* Diagnóstico de modos de fallo de los modelos, análisis de sensibilidad, detección de sesgos algorítmicos e interpretabilidad de modelos complejos.

### Familia 6: Analítica Prescriptiva y Optimización de Decisiones
* Formulación y resolución de modelos matemáticos de optimización (programación lineal, entera, mixta y no lineal) para asignar recursos escasos y maximizar o minimizar funciones objetivo bajo restricciones del mundo real (INFORMS Dominio IV/V, MIT Quantitative Methods).
* Modelamiento de sistemas complejos mediante simulación estocástica (Monte Carlo, eventos discretos y modelos basados en agentes) para evaluar el comportamiento dinámico y evaluar riesgos bajo incertidumbre profunda (`mit-machine-learning-modeling-and-simulation-principles.pdf`).
* Aplicación de la teoría de decisiones, árboles de decisión, análisis de compensación (*tradeoff analysis*, matrices Pugh) y algoritmos de decisión secuencial bajo incertidumbre (bandidos multilineales, aprendizaje por refuerzo básico) (Berkeley DATA C102, MIT Quantitative Methods).

### Familia 7: Diseño y Desarrollo de Productos de Datos
* Adopción de una mentalidad de producto (*product thinking*), formulando declaraciones de hipótesis de épicas (*Epic Hypothesis Statements*) y definiendo el Producto Mínimo Viable (MVP) para verificar hipótesis analíticas con usuarios reales (`dataops-05-agile.pdf`, `dataops-06-definition.pdf`, `mit-rapid-prototyping-methodologies.pdf`).
* Diseño de interfaces de usuario interactivas, tableros de comando analíticos y mecanismos de interacción humano-máquina (*human-in-the-loop*) orientados a la adopción y usabilidad (`mit-designing-and-building-ai-products-and-services.pdf`).
* Empaquetamiento de modelos y lógicas prescriptivas en servicios de software modulares y reutilizables mediante APIs (REST/gRPC) y microservicios analíticos.

### Familia 8: Operacionalización, DataOps y Calidad Continua
* Implementación de los principios de DataOps para el ciclo de vida analítico: integración continua y entrega continua (CI/CD) de tuberías y modelos (`dataops-06-definition.pdf`).
* Construcción de sistemas de pruebas automatizadas en múltiples niveles: pruebas de código (unitarias, integración, regresión) y pruebas continuas de datos (pruebas de balance, integridad, límites y frescura) (`dataops-09-data-quality.pdf`).
* Monitoreo continuo y observabilidad en producción, detectando deriva de datos (*data drift*), degradación conceptual (*concept drift*) y anomalías en los flujos de la Tubería de Valor (`dataops-03-methodologies.pdf`, `dataops-07-cdo.pdf`).
* Gestión de la deuda técnica en analítica y aprendizaje automático, garantizando la reproducibilidad total mediante contenerización, parametrización y versionado unificado de código, datos y modelos (`dataops-06-definition.pdf`, `dataops-08-data-scientids.pdf`).

### Familia 9: Gobernanza, Ética, Seguridad y Dinámica Organizacional
* Aplicación de principios de gobernanza de datos, seguridad, privacidad desde el diseño (e.g., privacidad diferencial, anonimización) y cumplimiento normativo (ACM DP/PR, National Academies).
* Evaluación ética de los sistemas analíticos, previniendo la discriminación algorítmica y garantizando la equidad, transparencia y auditabilidad del uso de datos (`dataops-02-data-strategy.pdf`, `dataops-03-methodologies.pdf`).
* Comprensión de las estructuras y topologías de equipos de datos (equipos centralizados vs. federados por dominio, células ágiles, capítulos y comunidades de práctica) y desarrollo de coordinación relacional para erradicar silos organizacionales (`dataops-07-cdo.pdf`, `dataops-10-organization.pdf`).

---

# 3. Tensiones y decisiones curriculares fundamentales

El diseño del currículo exige tomar postura frente a tensiones estructurales que atraviesan los documentos del corpus:

### 3.1. Estadística vs. Aprendizaje Automático (Machine Learning)
* **Tensión**: La estadística clásica prioriza la inferencia paramétrica, la interpretabilidad de coeficientes, la caracterización matemática asintótica y el contraste formal de hipótesis. El *Machine Learning* moderno prioriza la capacidad predictiva sobre datos no vistos, la minimización del riesgo empírico y la flexibilidad no paramétrica en estructuras de datos de alta dimensionalidad.
* **Decisión Curricular**: No subordinar una a la otra ni presentarlas en cursos separados y desconectados. El currículo debe articularlas a través del concepto de **Aprendizaje Estadístico**: la estadística provee el marco de evaluación rigurosa del error y la cuantificación de incertidumbre, mientras que el *Machine Learning* provee los algoritmos y la disciplina computacional de generalización.

### 3.2. Predicción vs. Inferencia Estadística vs. Inferencia Causal
* **Tensión**: Como subraya explícitamente el curso **Berkeley DATA C102** y ratifica `dataops-03-methodologies.pdf`, un modelo puede exhibir una correlación predictiva casi perfecta y, sin embargo, ser un pésimo instrumento para tomar decisiones si se fundamenta en variables de confusión o correlaciones espurias que colapsan ante una intervención del negocio. Predecir quién abandonará un servicio ($P(Y|X)$) no explica si una llamada de retención modificará su conducta ($P(Y|\text{do}(X))$).
* **Decisión Curricular**: La inferencia causal y el diseño experimental deben formar parte intrínseca de la formación en modelamiento, y no dejarse como un tema optativo menor. Los estudiantes deben aprender a distinguir rigurosamente entre modelar una respuesta observacional y predecir el efecto de una decisión.

### 3.3. Predicción vs. Prescripción (Optimización y Decisión)
* **Tensión**: La tendencia común en la industria es asumir que una buena predicción equivale a una solución analítica ("tenemos un modelo con 92% de precisión, el problema está resuelto"). Sin embargo, como señalan **INFORMS** y `dataops-03-methodologies.pdf`, un pronóstico es solo una entrada. La verdadera intervención requiere decidir qué hacer bajo restricciones operativas, presupuestarias y de capacidad.
* **Decisión Curricular**: Mantener un espacio curricular explícito y robusto para la **Analítica Prescriptiva**. El estudiante debe aprender a conectar salidas predictivas con funciones de utilidad, modelos de optimización matemática y simulaciones estocásticas que orienten de manera vinculante la acción operativa.

### 3.4. Optimización Matemática vs. Analítica de Decisiones Amplia
* **Tensión**: Existe el riesgo de reducir la prescripción a un curso abstracto de Investigación Operativa centrado en demostraciones formales de algoritmos de optimización (método Simplex, ramificación y acotamiento) que desconozca la incertidumbre del mundo real y los juicios cualitativos.
* **Decisión Curricular**: Adoptar una visión moderna de la Analítica de Decisiones (en la línea de **MIT Quantitative Methods**, **MIT Modeling & Simulation** e **INFORMS**). La optimización matemática se complementa necesariamente con simulación estocástica (Monte Carlo, eventos discretos), análisis de riesgo, árboles de decisión y métodos multicriterio de compensación (*tradeoffs*).

### 3.5. Ciencia de Datos vs. Ingeniería de Datos
* **Tensión**: Muchos programas académicos tratan la Ingeniería de Datos como un prerrequisito utilitario y pasivo (apenas unas clases de SQL o administración de servidores) o la ignoran, asumiendo que los datos ya están limpios en un archivo CSV. **Berkeley DATA C101**, el certificado de **MIT** y `dataops-08-data-scientids.pdf` demuestran que el 80% del esfuerzo analítico real reside en la gestión, arquitectura y aseguramiento de datos a escala.
* **Decisión Curricular**: La Ingeniería de Datos debe situarse como un pilar fundacional y formativo de primer nivel. Debe enfocarse no en la administración rutinaria de sistemas operativos, sino en el modelamiento de datos, el diseño de arquitecturas modernas (Data Lakes, Warehouses), la construcción de tuberías programáticas y la automatización de la calidad del dato.

### 3.6. Cuadernos Exploratorios vs. Sistemas Analíticos en Producción
* **Tensión**: El análisis exploratorio y la experimentación inicial florecen en cuadernos interactivos (*Jupyter Notebooks*), pero trasladar esos cuadernos directamente a producción es la causa directa del fracaso de la mayoría de proyectos analíticos (`dataops-01`, `dataops-08`, `dataops-09`).
* **Decisión Curricular**: Enseñar explícitamente la transición entre el código de exploración científica y el código de sistemas de producción. La reproducibilidad, modularidad, tipado, parametrización y empaquetamiento en módulos de software son exigencias transversales que culminan en un curso especializado de operacionalización.

### 3.7. Tubería de Innovación (Desarrollo Ágil) vs. Tubería de Valor (Operaciones Robustas)
* **Tensión**: Los científicos de datos demandan libertad y flexibilidad para probar nuevas librerías y algoritmos rápidamente, mientras que las operaciones de TI demandan estabilidad, rigidez y cero interrupciones en los sistemas productivos (`dataops-06-definition.pdf`, `dataops-07-cdo.pdf`).
* **Decisión Curricular**: Integrar el marco conceptual de DataOps para armonizar ambas necesidades. El currículo enseña a construir entornos aislados y parametrizados (ambientes de desarrollo, pruebas y producción) donde la innovación ágil pueda ocurrir a través de bifurcaciones (*branching*) sin poner en riesgo la tubería de valor.

### 3.8. Análisis Técnico vs. Decisión y Adopción Organizacional
* **Tensión**: Un modelo analítico perfecto que nadie utiliza no genera valor alguno (`dataops-02-data-strategy.pdf`, `cambridge-business-analytics.pdf`, `pwc-data-and-analytics-academy.pdf`). La excelencia técnica es inútil si la organización carece de capacidades para adoptar la solución o si las partes interesadas desconfían de los resultados.
* **Decisión Curricular**: El encuadre estratégico, el diseño centrado en el usuario, la comunicación visual convincente y la comprensión de la dinámica organizacional y el rol del CDO deben enmarcar el inicio y el cierre del currículo.

---

# 4. Arquitectura curricular propuesta

Se propone una arquitectura macro-curricular compuesta por **seis (6) cursos nucleares estructurados de manera secuencial y progresiva**. Esta estructura respeta el ciclo de vida natural de la analítica, garantiza los prerrequisitos cognitivos y técnicos, y evita tanto el aislamiento de temas como la sobrecarga superficial.

```
                    ┌────────────────────────────────────────────────────────┐
                    │  Curso 1: Encuadre Estratégico y Analítica Descriptiva │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                                ▼
                    ┌────────────────────────────────────────────────────────┐
                    │  Curso 2: Ingeniería de Datos y Tuberías Analíticas    │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                                ▼
                    ┌────────────────────────────────────────────────────────┐
                    │ Curso 3: Inferencia Estadística, Causalidad y Modelos  │
                    │                       Predictivos                      │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                                ▼
                    ┌────────────────────────────────────────────────────────┐
                    │  Curso 4: Analítica Prescriptiva y Modelamiento de     │
                    │                       Decisiones                       │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                                ▼
                    ┌────────────────────────────────────────────────────────┐
                    │  Curso 5: Diseño y Desarrollo de Productos de Datos    │
                    └───────────────────────────┬────────────────────────────┘
                                                │
                                                ▼
                    ┌────────────────────────────────────────────────────────┐
                    │ Curso 6: Operacionalización Analítica, DataOps y Ciclo │
                    │                       de Vida                          │
                    └────────────────────────────────────────────────────────┘
```

---

### Detalle de los Cursos Propuestos

#### Curso 1: Encuadre Estratégico y Analítica Descriptiva
* **Posición en la secuencia**: Primer semestre / Bloque inicial (Curso 1).
* **Propósito central**: Capacitar al estudiante para transformar problemas de negocio ambiguos en problemas analíticos estructurados, evaluar la disponibilidad y calidad de las fuentes de datos, explorar rigurosamente la evidencia empírica mediante estadística descriptiva y visualización avanzada, y comunicar hallazgos de forma convincente a tomadores de decisión en el marco de una estrategia de datos organizacional.
* **Competencias principales**:
  * Encuadre de problemas de negocio y traducción a problemas analíticos (INFORMS Dominios I y II).
  * Formulación de casos de valor, métricas de éxito y alineación estratégica (`dataops-02-data-strategy.pdf`).
  * Análisis exploratorio de datos (EDA) univariado y multivariado, identificación de anomalías y patrones (USC, Warwick, National Academies).
  * Principios de diseño visual, percepción gráfica, ergonomía informativa y *data storytelling* (PwC, Cambridge).
  * Identificación temprana de consideraciones éticas, gobernanza y uso responsable de datos (`dataops-02`, `dataops-03`).
* **Prerrequisitos**: Admisión al programa (alfabetización cuantitativa básica y familiaridad elemental con programación).
* **Qué recibe de cursos previos**: Es el punto de partida; recibe el contexto organizacional del estudiante y su intuición de negocio.
* **Para qué prepara al estudiante hacia adelante**: Proporciona el rigor para no saltar prematuramente al código o a los algoritmos sin entender el problema; prepara directamente para el diseño de requerimientos de datos en el Curso 2 y para el análisis probabilístico formal en el Curso 3.

---

#### Curso 2: Ingeniería de Datos y Tuberías Analíticas
* **Posición en la secuencia**: Segundo curso (Curso 2; articulado consecutivamente con el Curso 1).
* **Propósito central**: Desarrollar la capacidad de diseñar, construir y mantener arquitecturas de almacenamiento y tuberías de datos escalables, deterministas y reproducibles (ETL/ELT), aplicando principios de ingeniería de software, pruebas automatizadas de datos y aseguramiento de la cadena de suministro de datos para analítica.
* **Competencias principales**:
  * Modelamiento de datos relacional, multidimensional (estrella/copo de nieve) y no relacional (documental, columnar) (Berkeley DATA C101, MIT Data Engineering).
  * Construcción de tuberías programáticas de extracción, limpieza y transformación masiva de datos estructurados y no estructurados.
  * Implementación de la arquitectura de datos canónica: separación entre *Raw Lake*, datos enriquecidos y capas de consumo (`dataops-06-definition.pdf`, `dataops-08-data-scientids.pdf`).
  * Tratamiento de la limpieza de datos como código estructurado, parametrizado y auditable, superando los scripts manuales (`dataops-04-lean-thinking.pdf`, `dataops-08-data-scientids.pdf`).
  * Pruebas automatizadas de datos en la ingestión: pruebas de esquema, balance, integridad y validación de rangos (`dataops-09-data-quality.pdf`).
  * Control de versiones de código y linaje de datos con Git (ACM SDM, `dataops-06-definition.pdf`).
* **Prerrequisitos**: Curso 1 (Encuadre Estratégico y Analítica Descriptiva).
* **Qué recibe de cursos anteriores**: Especificación formal de requerimientos de datos, comprensión de la calidad inicial de las fuentes y el marco del problema analítico.
* **Para qué prepara al estudiante hacia adelante**: Alimenta con datos confiables, estructurados y versionados al modelamiento estadístico y predictivo del Curso 3, y establece la infraestructura base que sustentará los productos y operaciones en los Cursos 5 y 6.

---

#### Curso 3: Inferencia Estadística, Causalidad y Modelos Predictivos
* **Posición en la secuencia**: Tercer curso (Curso 3; requiere Cursos 1 y 2).
* **Propósito central**: Dominar el razonamiento probabilístico formal, la inferencia estadística (frecuentista y bayesiana), la identificación causal y el modelamiento predictivo mediante *Machine Learning*, asegurando que el estudiante distinga nítidamente entre predecir un resultado bajo condiciones observacionales y evaluar el efecto de intervenir una variable del sistema.
* **Competencias principales**:
  * Fundamentos probabilísticos de la inferencia, estimación puntual, intervalos de confianza y cuantificación rigurosa de incertidumbre (Berkeley DATA C102, National Academies).
  * Pruebas de hipótesis múltiples y control formal de la tasa de descubrimientos falsos (FDR) (Berkeley DATA C102).
  * Inferencia causal: diagramas causales (DAGs), variables confusoras, diseño de experimentos controlados aleatorizados (A/B testing) y métodos cuasi-experimentales en datos observacionales (Cambridge, Berkeley DATA C102).
  * Algoritmos de aprendizaje estadístico supervisado: regresión lineal y logística regularizada (Ridge, Lasso, ElasticNet), árboles de decisión, ensambles (Random Forest, Gradient Boosting) y conceptos nucleares de redes neuronales (MIT DSML, ACM ML).
  * Validación rigurosa de modelos: partición cruzada, prevención del sobreajuste (*leakage*), funciones de pérdida asimétricas y evaluación de costos de error en negocio (INFORMS Dominio V).
  * Diagnóstico de sesgo, equidad (*fairness*) e interpretabilidad en modelos predictivos (`dataops-03-methodologies.pdf`).
* **Prerrequisitos**: Curso 1 (Encuadre y Analítica Descriptiva) y Curso 2 (Ingeniería de Datos).
* **Qué recibe de cursos anteriores**: Datos limpios, estructurados y curados desde la tubería de ingeniería (Curso 2) y un encuadre riguroso de las hipótesis del negocio (Curso 1).
* **Para qué prepara al estudiante hacia adelante**: Entrega pronósticos calibrados y probabilidades de respuesta para el motor de optimización prescriptiva del Curso 4, así como artefactos de modelos para su integración en productos de datos en el Curso 5.

---

#### Curso 4: Analítica Prescriptiva y Modelamiento de Decisiones
* **Posición en la secuencia**: Cuarto curso (Curso 4; requiere Cursos 1 y 3).
* **Propósito central**: Capacitar al estudiante para conectar predicciones y escenarios de incertidumbre con la acción óptima del negocio, formulando y resolviendo modelos de optimización matemática, simulación estocástica y marcos formales de análisis de decisiones bajo restricciones de recursos del mundo real.
* **Competencias principales**:
  * Formulación y resolución de modelos de programación matemática: optimización lineal (LP), entera/mixta (MIP) y no lineal (NLP) orientada a la toma de decisiones empresariales (INFORMS Dominio IV/V).
  * Simulación estocástica y de sistemas: simulación Monte Carlo para cuantificación del riesgo, y modelos de simulación de eventos discretos o basados en agentes (`mit-machine-learning-modeling-and-simulation-principles.pdf`).
  * Teoría de decisión y análisis de compensaciones: árboles de decisión, valor de la información perfecta e imperfecta, y matrices de evaluación multicriterio (Pugh matrices, trade studies) (MIT Quantitative Methods).
  * Optimización robusta y análisis de sensibilidad de decisiones frente a perturbaciones de parámetros.
  * Introducción a la toma de decisiones secuenciales bajo incertidumbre: algoritmos de bandidos multilínea (*multi-armed bandits*) y nociones de procesos de decisión de Markov (Berkeley DATA C102).
* **Prerrequisitos**: Curso 1 (Encuadre) y Curso 3 (Inferencia y Predicción); recomendado Curso 2.
* **Qué recibe de cursos anteriores**: Distribuciones de probabilidad, estimaciones de impacto causal y modelos predictivos provenientes del Curso 3, además de las restricciones del problema de negocio definidas en el Curso 1.
* **Para qué prepara al estudiante hacia adelante**: Provee los motores de decisión y optimización que constituyen el núcleo de inteligencia activa en los productos de datos desarrollados en el Curso 5.

---

#### Curso 5: Diseño y Desarrollo de Productos de Datos
* **Posición en la secuencia**: Quinto curso (Curso 5; requiere Cursos 2, 3 y 4).
* **Propósito central**: Aprender a concebir, diseñar, prototipar y construir **Productos de Datos** funcionales y modulares, integrando tuberías de datos, modelos predictivos y lógicas prescriptivas en sistemas orientados al usuario final, con interfaces de decisión efectivas y arquitecturas basadas en servicios.
* **Competencias principales**:
  * Concepción de soluciones analíticas con mentalidad de producto: declaración de hipótesis de épicas (*Epic Hypothesis Statements*), definición del MVP y gestión ágil del ciclo de innovación analítica (`dataops-05-agile.pdf`, `dataops-06-definition.pdf`, `mit-rapid-prototyping-methodologies.pdf`).
  * Diseño centrado en el usuario para analítica: arquitectura de información, interacción humano-algoritmo (*human-in-the-loop*), heurísticas de usabilidad para tableros de control y herramientas de soporte a decisiones (`mit-designing-and-building-ai-products-and-services.pdf`).
  * Empaquetamiento de capacidades analíticas: diseño e implementación de APIs (RESTful/gRPC) para exponer modelos y motores prescriptivos.
  * Modularización de software analítico: separación estricta entre capas de datos, lógica de inferencia/optimización y capa de presentación.
  * Prototipado rápido y validación temprana con usuarios y partes interesadas antes de la escala industrial (`mit-rapid-prototyping-methodologies.pdf`, `dataops-05-agile.pdf`).
* **Prerrequisitos**: Curso 2 (Ingeniería de Datos), Curso 3 (Inferencia y Predicción) y Curso 4 (Analítica Prescriptiva).
* **Qué recibe de cursos anteriores**: Tuberías de datos reproducibles (Curso 2), modelos predictivos calibrados (Curso 3) y algoritmos de optimización prescriptiva (Curso 4).
* **Para qué prepara al estudiante hacia adelante**: Entrega prototipos funcionales y empaquetados como software analítico, listos para ser sometidos a la automatización industrial, pruebas continuas y gobernanza del ciclo de vida en el Curso 6.

---

#### Curso 6: Operacionalización Analítica, DataOps y Ciclo de Vida
* **Posición en la secuencia**: Sexto curso / Curso culminante e integrador (Curso 6; requiere Cursos 2, 3, 4 y 5).
* **Propósito central**: Operacionalizar, automatizar, monitorear y gobernar sistemas analíticos a escala corporativa aplicando los principios y prácticas de DataOps y MLOps, asegurando la sincronización de la Tubería de Valor y la Tubería de Innovación, la calidad continua de código y datos, y la coordinación efectiva en equipos multidisciplinarios.
* **Competencias principales**:
  * Arquitectura e implementación de DataOps y MLOps: integración y entrega continuas (CI/CD) para flujos de datos y modelos (`dataops-06-definition.pdf`, `mit-cloud-and-devops.pdf`).
  * Implementación de los 7 pasos prácticos de DataOps: pruebas automatizadas de datos y lógica, control de versiones unificado, ramificación/fusión (*branch/merge*), gestión de múltiples ambientes (desarrollo, pruebas, producción), reutilización/contenerización (Docker), parametrización integral y erradicación del heroísmo (`dataops-06-definition.pdf`).
  * Pirámide de pruebas continuas para analítica: pruebas unitarias, de integración, funcionales, de regresión, de desempeño, pruebas de humo y pruebas de balance de datos (`dataops-09-data-quality.pdf`).
  * Monitoreo en producción y observabilidad: tableros de control de DataOps, detección de deriva de datos (*data drift*), degradación conceptual (*concept drift*), alertas tempranas y protocolos de reentrenamiento/recalibración (`dataops-03-methodologies.pdf`, `dataops-07-cdo.pdf`, INFORMS Dominio VII).
  * Gestión de la deuda técnica en analítica y mitigación del acoplamiento entre código y datos (`dataops-08-data-scientids.pdf`).
  * Dinámica organizacional y liderazgo del CDO: coordinación relacional entre TI, ingeniería, ciencia de datos y negocio; topologías de equipos de datos (dominio vs. centrales, capítulos y comunidades); gobernanza del ciclo de vida y auditoría ética continua (`dataops-07-cdo.pdf`, `dataops-10-organization.pdf`, `mit-data-leadership.pdf`).
* **Prerrequisitos**: Cursos 2, 3, 4 y 5.
* **Qué recibe de cursos anteriores**: El producto de datos completo (código, datos, modelos, optimizador e interfaces) generado en los Cursos 2 a 5.
* **Para qué prepara al estudiante hacia adelante**: Prepara para el ejercicio profesional de alto nivel, la dirección técnica de iniciativas analíticas corporativas y el despliegue de soluciones que perduren en el tiempo sin degradarse ni colapsar operativamente.

---

# 5. Fronteras entre cursos

Para garantizar la coherencia del programa y evitar solapamientos destructivos o vacíos de contenido, se establecen las siguientes delimitaciones explícitas:

### 5.1. Curso 1 (Encuadre y Analítica Descriptiva) vs. Curso 2 (Ingeniería de Datos)
* **Dónde termina el Curso 1**: Termina en el análisis exploratorio de datos (EDA), la interpretación de distribuciones univariadas y bivariadas, la agregación descriptiva para responder preguntas de negocio, el diseño de visualizaciones para comunicar hallazgos y la identificación de requerimientos de datos. Utiliza datos en formatos planos o extractos preparados para explorar la viabilidad analítica.
* **Dónde comienza el Curso 2**: Comienza en el momento en que los datos deben ser tratados como un **sistema de producción a escala**: diseño de esquemas de bases de datos relacionales y dimensionales, modelamiento conceptual/lógico, pipelines automatizados de extracción/ingestión masiva, orquestación de flujos de transformación (ETL/ELT), versionado de datos y pruebas automatizadas de integridad de datos en la carga.
* **Zona de debate resuelta**: La "limpieza de datos". En el Curso 1, la limpieza se aborda conceptualmente para entender la semántica del dato y las anomalías en un análisis exploratorio. En el Curso 2, la limpieza se sistematiza como **código de ingeniería determinista, modular y testeable** que opera automáticamente sobre flujos continuos de datos.

### 5.2. Curso 1 (Encuadre y Analítica Descriptiva) vs. Curso 3 (Inferencia y Predicción)
* **Dónde termina el Curso 1**: Termina en la descripción rigurosa de la muestra observada (lo que los datos muestran que ocurrió en el pasado histórico) mediante frecuencias, medidas de tendencia central, dispersión, correlaciones lineales y visualizaciones.
* **Dónde comienza el Curso 3**: Comienza cuando se pasa de la muestra observada al **universo no observado** y a la toma de decisiones probabilística: distribuciones de probabilidad, intervalos de confianza, pruebas de hipótesis formales, control de falsos descubrimientos, generalización matemática a datos futuros y estimación causal de intervenciones.

### 5.3. Curso 2 (Ingeniería de Datos) vs. Curso 3 (Inferencia y Predicción)
* **Dónde termina el Curso 2**: Termina en la entrega de la **capa de datos refinados** (*refined data layer*) y tablas de características (*feature tables*) validadas sintácticamente, versionadas y expuestas a través de consultas optimizadas o servicios de acceso a datos.
* **Dónde comienza el Curso 3**: Comienza con la formulación matemática de la función de pérdida, la optimización algorítmica de los parámetros del modelo predictivo, la validación cruzada y el análisis de significancia estadística o causal de las variables.
* **Zona de debate resuelta**: El *Feature Engineering* (ingeniería de características). La concepción, selección de variables y diseño matemático de transformaciones informativas pertenece al Curso 3; la ejecución automatizada, eficiente y escalable de esas transformaciones dentro de la tubería de datos pertenece al Curso 2.

### 5.4. Curso 3 (Inferencia y Predicción) vs. Curso 4 (Analítica Prescriptiva)
* **Dónde termina el Curso 3**: Termina en la estimación rigurosa de lo que ocurrirá o de cuál es la probabilidad de que ocurra un evento (e.g., "el cliente $i$ tiene un 78% de probabilidad de abandono", "la demanda estimada para el periodo $t$ sigue una distribución Normal con media $\mu$ y varianza $\sigma^2$") y la cuantificación del efecto causal de intervenciones potenciales.
* **Dónde comienza el Curso 4**: Comienza en la pregunta: **"Dado este pronóstico y dada esta incertidumbre, ¿qué decisión debemos tomar?"**. El Curso 4 introduce formalmente las restricciones operativas (capacidad de inventario, presupuesto de mercadeo, rutas de transporte), las funciones objetivo de negocio y la teoría de decisiones para optimizar la asignación de recursos o simular el comportamiento de políticas alternativas.
* **Zona de debate resuelta**: Un modelo predictivo nunca debe ser confundido con una política de decisión. El Curso 3 enseña a predecir; el Curso 4 enseña a decidir óptimamente bajo restricciones.

### 5.5. Curso 4 (Analítica Prescriptiva) vs. Curso 5 (Diseño de Productos de Datos)
* **Dónde termina el Curso 4**: Termina en la formulación, codificación matemática y resolución algorítmica del modelo de optimización o simulación (e.g., un script que formula un programa lineal entero en un solver y arroja el vector óptimo de decisión $X^*$, o una simulación Monte Carlo que calcula la probabilidad de pérdida financiera).
* **Dónde comienza el Curso 5**: Comienza en la **transformación de ese modelo algorítmico en una solución utilizable por humanos o sistemas**: diseño de la experiencia de usuario (UX), desarrollo de la interfaz de decisión (pantallas interactivas, sliders de parámetros, alertas), diseño de contratos de API para conectar el motor prescriptivo con aplicaciones del negocio y verificación rápida de hipótesis de adopción mediante prototipos mínimos viables (MVP).

### 5.6. Curso 5 (Diseño de Productos de Datos) vs. Curso 6 (Operacionalización y DataOps)
* **Dónde termina el Curso 5**: Termina en el prototipo funcional verificado del producto analítico (el código del frontend, la lógica del backend analítico en APIs, la orquestación local y las métricas de valor validadas con el usuario en la Tubería de Innovación).
* **Dónde comienza el Curso 6**: Comienza cuando ese producto debe ser **industrializado para operar de forma continua, ininterrumpida y a escala corporativa en la Tubería de Valor**: pipelines de CI/CD automatizados, pruebas unitarias y de integración del código, pruebas continuas de balance e integridad de datos en producción, contenerización con Docker en entornos múltiples (Dev/Staging/Prod), monitoreo activo de deriva (*drift*), protocolos de degradación y alineación organizacional de los equipos según los principios de DataOps.

---

# 6. Competencias transversales

Existen competencias fundamentales que no pueden confinarse a una única asignatura sin correr el riesgo de convertirlas en asignaciones teóricas desconectadas. Estas competencias deben trabajarse de forma explícita y acumulativa a lo largo de toda la malla curricular:

1. **Formulación y Encuadre de Problemas (Problem Framing)**:
   * Se introduce formalmente en el Curso 1 (traducción de preguntas de negocio a analíticas).
   * Se ejercita en el Curso 2 (traducción de requerimientos analíticos a esquemas y contratos de datos).
   * Se profundiza en los Cursos 3 y 4 (traducción a hipótesis estadísticas, objetivos predictivos y modelos de optimización).
   * Se consolida en los Cursos 5 y 6 (traducción a declaraciones de hipótesis de épicas y casos de valor corporativos).

2. **Reproducibilidad Científica e Ingeniería de Software para Analítica**:
   * Introducida desde el Curso 1 (cuadernos reproducibles y estructuración de proyectos).
   * Desarrollada rigurosamente en el Curso 2 (control de versiones con Git, entornos virtuales aislados, código modular).
   * Mantenida en los Cursos 3 y 4 (semillas pseudoaleatorias, reproducibilidad de particiones y corridas de optimización).
   * Dominada en los Cursos 5 y 6 (contenerización con Docker, pipelines deterministas, parametrización total y empaquetamiento de productos).

3. **Pruebas Automatizadas y Calidad Continua (Mentalidad DataOps)**:
   * En el Curso 2 se introducen las pruebas de datos (validación de esquemas, pruebas de integridad y balance).
   * En el Curso 3 se introducen las pruebas de validación estadística y no regresión de modelos.
   * En el Curso 4 se introducen las pruebas de admisibilidad y sensibilidad de soluciones prescriptivas.
   * En el Curso 5 se prueban las interfaces y contratos de APIs.
   * En el Curso 6 se integra la **pirámide completa de pruebas de DataOps** (unitarias, integración, regresión, humo y balance de datos) en pipelines automatizados de CI/CD (`dataops-09-data-quality.pdf`).

4. **Razonamiento Probabilístico y Cuantificación de la Incertidumbre**:
   * Introducido en el Curso 1 (variabilidad en datos empíricos).
   * Formalizado matemáticamente en el Curso 3 (inferencia estadística, distribuciones muestrales, intervalos de predicción y confianza).
   * Aplicado a la toma de decisiones en el Curso 4 (optimización estocástica, simulación Monte Carlo, árboles de decisión).
   * Monitoreado operativamente en el Curso 6 (degradación de la calibración probabilística en producción).

5. **Comunicación, Visualización y Storytelling con Datos**:
   * Introducido y desarrollado en el Curso 1 (gramática de los gráficos, percepción visual, presentaciones ejecutivas).
   * Aplicado en el Curso 3 (comunicación de resultados predictivos y métricas de error).
   * Aplicado en el Curso 4 (visualización de fronteras de compromiso y análisis de escenarios).
   * Dominado en el Curso 5 (diseño ergonómico de interfaces de usuario y tableros interactivos).

6. **Ética, Privacidad, Seguridad y Gobernanza Responsable**:
   * Introducido en el Curso 1 (regulaciones, consentimiento informado y uso ético de datos).
   * Desarrollado en el Curso 2 (seguridad en bases de datos, anonimización, control de acceso basado en roles).
   * Profundizado en el Curso 3 (detección y mitigación de sesgos algorítmicos, justicia y equidad en modelos).
   * Integrado en los Cursos 5 y 6 (auditoría ética de productos de datos, gobernanza del ciclo de vida, privacidad por diseño y liderazgo ético del CDO).

---

# 7. Mapa de contenidos

La siguiente matriz presenta la progresión curricular detallada de las competencias y temas clave a través de los seis cursos propuestos, utilizando la escala estándar:
* **I** = *Introduced* (Introducido)
* **D** = *Developed* (Desarrollado)
* **M** = *Mastered / Integrated* (Dominado e Integrado)
* **—** = No es foco del curso

| Dominio / Competencia / Tema Clave | Curso 1: Encuadre & Descriptiva | Curso 2: Ingeniería de Datos | Curso 3: Inferencia & Predicción | Curso 4: Prescriptiva & Decisión | Curso 5: Productos de Datos | Curso 6: Operaciones & DataOps |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Encuadre y Estrategia de Negocio** | | | | | | |
| Encuadre de problemas de negocio a analítica (INFORMS I-II) | **M** | D | D | D | D | M |
| Formulación de casos de valor y KPIs (`dataops-02`) | **M** | I | — | D | D | M |
| Estrategia de datos corporativa y rol del CDO (`dataops-02`, `dataops-07`) | **I** | — | — | — | I | **M** |
| **Ingeniería y Gestión de Datos** | | | | | | |
| Modelamiento de datos (relacional, dimensional, NoSQL) | I | **M** | — | — | D | D |
| Tuberías programáticas de datos (ETL/ELT escalables) | — | **M** | I | — | D | M |
| Arquitectura de datos canónica (Lakes/Warehouses/Lakehouse) | I | **M** | — | — | D | M |
| Preparación y limpieza de datos como código determinista | D | **M** | D | — | — | M |
| **Analítica Descriptiva y Comunicación** | | | | | | |
| Análisis exploratorio de datos (EDA) multivariado | **M** | D | D | — | — | — |
| Visualización de datos, percepción y ergonomía gráfica | **M** | — | D | D | M | — |
| *Data Storytelling* y comunicación a partes interesadas | **M** | — | D | D | M | D |
| **Inferencia Estadística y Causalidad** | | | | | | |
| Inferencia probabilística frecuentista y bayesiana | I | — | **M** | D | — | — |
| Pruebas de hipótesis y control de descubrimientos falsos (FDR) | I | — | **M** | — | — | D |
| Inferencia causal, DAGs y métodos cuasi-experimentales | — | — | **M** | D | — | — |
| Diseño y análisis de experimentos aleatorizados (A/B testing) | I | — | **M** | D | D | D |
| **Modelamiento Predictivo y Machine Learning** | | | | | | |
| Aprendizaje supervisado (regresión, árboles, ensambles) | — | — | **M** | D | D | — |
| Compromiso sesgo-varianza, regularización y validación cruzada | — | — | **M** | — | — | D |
| Diagnóstico de errores, costos asimétricos y equidad (*fairness*) | I | — | **M** | D | D | D |
| **Analítica Prescriptiva y Optimización** | | | | | | |
| Programación matemática (LP, MIP, NLP) bajo restricciones | — | — | — | **M** | D | — |
| Simulación estocástica (Monte Carlo, eventos discretos) | I | — | D | **M** | D | — |
| Teoría de decisiones y análisis de compensaciones (*tradeoffs*) | I | — | D | **M** | D | — |
| Decisiones secuenciales bajo incertidumbre (Bandidos / MDPs) | — | — | I | **M** | — | — |
| **Diseño y Desarrollo de Productos de Datos** | | | | | | |
| Declaración de hipótesis de épicas y MVPs analíticos (`dataops-05`) | I | — | — | — | **M** | D |
| Diseño de interfaces de decisión y soporte al usuario (*human-in-the-loop*) | I | — | — | — | **M** | D |
| Empaquetamiento de modelos y lógica en APIs y microservicios | — | I | — | — | **M** | D |
| Arquitectura de software modular para productos analíticos | — | D | — | — | **M** | D |
| **Operacionalización, DataOps y Calidad Continua** | | | | | | |
| Dualidad Tubería de Valor vs. Tubería de Innovación (`dataops-04`, `06`) | I | D | — | — | D | **M** |
| Pruebas automatizadas de datos (balance, límites, esquema) (`dataops-09`) | — | **D** | — | — | D | **M** |
| Pruebas automatizadas de código (unitarias, integración, regresión) | — | D | I | — | D | **M** |
| CI/CD, ramificación y ambientes múltiples (Dev/Test/Prod) (`dataops-06`) | — | I | — | — | D | **M** |
| Contenerización (Docker) y parametrización total (`dataops-06`) | — | I | — | — | D | **M** |
| Monitoreo de deriva (*drift*), degradación y alertas (`dataops-03`, `07`) | — | — | I | — | D | **M** |
| Gestión de deuda técnica en analítica y ML (`dataops-08`) | — | D | D | — | D | **M** |
| Coordinación relacional y topología de equipos de datos (`dataops-10`) | I | — | — | — | D | **M** |
| **Gobernanza, Ética y Seguridad** | | | | | | |
| Privacidad, anonimización y seguridad de datos (ACM DP) | I | **D** | — | — | D | **M** |
| Ética algorítmica, transparencia y uso responsable | **D** | D | D | D | D | **M** |
| Gobernanza del ciclo de vida analítico (INFORMS VII, `dataops-03`) | I | — | — | — | D | **M** |

---

# 8. Qué queda deliberadamente fuera

Un currículo riguroso se define tanto por lo que incluye como por lo que excluye conscientemente. Los siguientes temas se dejan deliberadamente fuera del núcleo obligatorio de este programa de Analítica:

1. **Administración Profunda de Infraestructura en la Nube y Operaciones de Servidores (SysAdmin / Bare-Metal DevOps)**:
   * *Exclusión*: Configuración de redes de bajo nivel, aprovisionamiento de clústeres de Kubernetes desde cero, configuración de firewalls, ensamblaje de hardware para servidores y administración profunda de sistemas operativos Linux.
   * *Justificación*: El rol del profesional en Analítica (incluso bajo el paradigma de DataOps) es el de un consumidor inteligente de plataformas que interactúa con la infraestructura a través de abstracciones declarativas (contenedores Docker, archivos de configuración CI/CD, infraestructura como código orientada a servicios). La administración física o profunda de la infraestructura corresponde a ingenieros de DevOps/SRE e infraestructura de TI, con quienes los analistas colaboran a través de la coordinación relacional (`dataops-07-cdo.pdf`, `dataops-10-organization.pdf`).

2. **Investigación de Operaciones Teórica Pura y Demostración Formal de Algoritmos**:
   * *Exclusión*: Demostraciones formales de teoremas de dualidad, lemas de Farkas, desarrollo manual del método Simplex paso a paso o teoría de grafos abstracta.
   * *Justificación*: El objetivo de la Analítica Prescriptiva no es formar matemáticos teóricos de optimización, sino modeladores capaces de traducir restricciones y objetivos de negocio complejos en modelos matemáticos formulables y computacionalmente resolubles utilizando solvers modernos y simuladores estocásticos (INFORMS, MIT Quantitative Methods).

3. **Inteligencia Artificial Generativa y Deep Learning Extremo no Vinculado a Decisiones**:
   * *Exclusión*: Preentrenamiento de modelos masivos de lenguaje (LLMs) desde cero, diseño de arquitecturas de modelos de difusión para generación de imágenes o procesamiento fonético de audio en tiempo real.
   * *Justificación*: El núcleo de la Analítica son los sistemas de apoyo a decisiones organizacionales basados en datos empíricos. Aunque las herramientas generativas pueden usarse como interfaces o asistentes, dedicar un curso troncal a la física matemática de los modelos generativos alejaría al programa de su mandato decisional, inferencial y prescriptivo.

4. **Especializaciones Temáticas de Dominio Vertical (FinTech, Bioinformática, Smart Cities)**:
   * *Exclusión*: Cursos obligatorios enfocados exclusivamente en un único sector económico (e.g., analítica de riesgo crediticio específico, genómica computacional, analítica deportiva).
   * *Justificación*: El currículo nuclear debe proporcionar los fundamentos metodológicos, inferenciales, algorítmicos e ingenieriles universales. Los dominios específicos deben ofrecerse como asignaturas optativas, electivas o casos de aplicación en proyectos finales.

5. **Entrenamiento en Herramientas de Software Propietarias y Pasajeras**:
   * *Exclusión*: Cursos estructurados alrededor de la certificación o el uso de interfaces de software comercial privativo específico (e.g., herramientas propietarias de arrastrar y soltar que ocultan el código).
   * *Justificación*: Como dictamina `dataops-06-definition.pdf` y la recomendación de la **ACM (2021)**, la analítica es una disciplina fundamentada en conceptos duraderos y código abierto auditable. Atar el currículo a un proveedor o herramienta propietaria genera obsolescencia rápida y debilita las competencias de ingeniería y reproducibilidad del estudiante.

---

# 9. Evidencia documental

A continuación se detalla la correspondencia entre los cursos propuestos y los documentos de `./curriculum/` que ejercieron la influencia más directa sobre su diseño:

### Curso 1: Encuadre Estratégico y Analítica Descriptiva
* **`informs-analytics-framework-2024.pdf` & `informs-cap-essentials-blueprint.pdf` / `informs-cap-pro-blueprint.pdf`**:
  * *Contribución*: Proveen la base para los Dominios I (Business Problem Framing) y II (Analytics Problem Framing), estructurando el proceso formal de desglosar preguntas de negocio en variables, hipótesis y métricas de éxito.
* **`dataops-01-the-problem.pdf`**:
  * *Contribución*: Justifica la necesidad del encuadre riguroso al revelar los mitos y problemas reales de la analítica (silos, metas cambiantes, desconexión entre analistas y directivos).
* **`dataops-02-data-strategy.pdf`**:
  * *Contribución*: Aporta el marco metodológico para conectar objetivos organizacionales, capacidades analíticas e iniciativas priorizadas mediante casos de valor sustentados.
* **`cambridge-business-analytics.pdf`**:
  * *Contribución*: Enfatiza el encuadre de la toma de decisiones basada en datos en entornos empresariales cambiantes y la necesidad de una mentalidad de experimentación continua.
* **`pwc-data-and-analytics-academy.pdf`**:
  * *Contribución*: Modela la enseñanza de visualización de datos, *data storytelling* y comunicación ejecutiva estructurada.
* **`usc-introduction-to-data-analytics.pdf` & `warwick-foundations-of-data-analytics.pdf`**:
  * *Contribución*: Fundamentan el núcleo riguroso de estadística descriptiva y análisis exploratorio de datos (EDA).

### Curso 2: Ingeniería de Datos y Tuberías Analíticas
* **`berkeley-data-c101-data-engineering.pdf`**:
  * *Contribución*: Define el alcance moderno de la ingeniería de datos: gestión de datos a escala para analítica y ML, cubriendo el ciclo completo desde ingestión hasta exploración y operaciones escalables y confiables.
* **`mit-professional-certificate-data-engineering.pdf`**:
  * *Contribución*: Estructura el contenido de modelamiento de datos relacional y dimensional, consultas avanzadas (SQL), almacenes de datos y diseño de flujos ETL/ELT.
* **`acm-computing-competencies-undergraduate-data-science-2021.pdf` (Áreas DG y SDM)**:
  * *Contribución*: Aporta las competencias de gobierno, adquisición, almacenamiento y principios de desarrollo y mantenimiento de software.
* **`dataops-04-lean-thinking.pdf`**:
  * *Contribución*: Introduce el mapeo del flujo de valor (*value stream mapping*) aplicado a los datos para erradicar desperdicios, tiempos de espera y cuellos de botella en la preparación de datos.
* **`dataops-08-data-scientids.pdf`**:
  * *Contribución*: Provee los principios de la arquitectura de datos canónica (*Raw Lake* $\rightarrow$ *Refined Data*) y el tratamiento sistemático de esquemas y tipos de datos.
* **`dataops-09-data-quality.pdf`**:
  * *Contribución*: Establece que la limpieza de datos debe complementarse con pruebas de datos automatizadas (pruebas de balance, integridad y límites).

### Curso 3: Inferencia Estadística, Causalidad y Modelos Predictivos
* **`berkeley-data-c102-data-inference-and-decisions.pdf`**:
  * *Contribución*: Es la influencia primordial para integrar la inferencia frecuentista y bayesiana, el control de descubrimientos falsos (FDR), los modelos gráficos probabilísticos y, fundamentalmente, la inferencia causal para la toma de decisiones.
* **`national-academies-data-science-for-undergraduates-2018.pdf`**:
  * *Contribución*: Fundamenta las áreas de competencia estadística y matemática del *Data Acumen*, insistiendo en la cuantificación de incertidumbre y la reproducibilidad del análisis.
* **`mit-data-science-and-machine-learning.pdf`**:
  * *Contribución*: Estructura el espectro de algoritmos de aprendizaje supervisado (regresión regularizada, árboles, ensambles, redes neuronales) y su calibración práctica.
* **`acm-computing-competencies-undergraduate-data-science-2021.pdf` (Área ML)**:
  * *Contribución*: Define las competencias computacionales en aprendizaje automático, compromiso sesgo-varianza y evaluación rigurosa fuera de muestra.
* **`dataops-03-methodologies.pdf`**:
  * *Contribución*: Advierte que "un buen modelo no garantiza un buen proyecto de analítica" y fundamenta la necesidad de evaluar el desempeño considerando el contexto de uso y los costos asimétricos de error.

### Curso 4: Analítica Prescriptiva y Modelamiento de Decisiones
* **`informs-analytics-framework-2024.pdf` (Dominios IV y V - Analítica Prescriptiva)**:
  * *Contribución*: Establece formalmente la metodología prescriptiva (optimización matemática, simulación estocástica y árboles de decisión) como el pináculo de la cadena analítica.
* **`mit-quantitative-methods-in-systems-engineering.pdf`**:
  * *Contribución*: Aporta métodos cuantitativos de análisis de compensaciones (*tradeoffs*), matrices Pugh, toma de decisiones multicriterio y evaluación de alternativas bajo restricciones.
* **`mit-machine-learning-modeling-and-simulation-principles.pdf`**:
  * *Contribución*: Aporta los principios de modelamiento de sistemas dinámicos y simulación estocástica, vinculando simulación física y probabilística con modelos basados en datos.
* **`berkeley-data-c102-data-inference-and-decisions.pdf`**:
  * *Contribución*: Aporta las bases de decisión bajo incertidumbre y algoritmos secuenciales (bandidos multilínea y formulaciones de teoría de decisión).

### Curso 5: Diseño y Desarrollo de Productos de Datos
* **`mit-designing-and-building-ai-products-and-services.pdf`**:
  * *Contribución*: Define el ciclo de vida del producto analítico/IA, los modelos de interacción humano-algoritmo (*human-in-the-loop*), la usabilidad y la integración de modelos en servicios funcionales.
* **`mit-rapid-prototyping-methodologies.pdf`**:
  * *Contribución*: Provee metodologías de prototipado rápido, validación temprana de conceptos y reducción de la tasa de fallo de productos analíticos comerciales.
* **`dataops-05-agile.pdf`**:
  * *Contribución*: Establece las prácticas de colaboración ágil adaptadas a analítica: ideación, concepción, desarrollo de MVPs para validar hipótesis y marcos ágiles escalados.
* **`dataops-06-definition.pdf`**:
  * *Contribución*: Define qué es un producto de datos ("resuelve un problema, combina datos con algoritmos, es rápido, escalable, repetible, reproducible, de uso continuo y monitoreo constante").

### Curso 6: Operacionalización Analítica, DataOps y Ciclo de Vida
* **`dataops-06-definition.pdf`**:
  * *Contribución*: Documento eje que define los 7 pasos para implementar DataOps (pruebas de lógica y datos, control de versiones, bifurcación/fusión, ambientes múltiples, contenerización, parametrización y erradicación del heroísmo) y la diferenciación formal entre DevOps y DataOps.
* **`dataops-04-lean-thinking.pdf`**:
  * *Contribución*: Aporta los fundamentos de manufactura esbelta aplicados a la Tubería de Valor y Tubería de Innovación, eliminación de desperdicios y análisis de causa raíz.
* **`dataops-09-data-quality.pdf`**:
  * *Contribución*: Fundamenta la pirámide de pruebas continuas automatizadas (pruebas unitarias, de integración, regresión, pruebas de humo y pruebas de balance de datos).
* **`dataops-07-cdo.pdf` & `dataops-10-organization.pdf`**:
  * *Contribución*: Estructuran el rol del CDO, los tableros de control de DataOps, la erradicación de silos mediante coordinación relacional y las topologías de equipos de datos por dominio.
* **`dataops-08-data-scientids.pdf`**:
  * *Contribución*: Aborda la reducción de deuda técnica en machine learning, la desconexión entre desarrollo y despliegue, y el reuso de código en la cadena analítica.
* **`informs-analytics-framework-2024.pdf` (Dominios VI - Deployment y VII - Lifecycle Management)**:
  * *Contribución*: Valida formalmente los requerimientos de despliegue, verificación en producción, recalibración de modelos, mantenimiento y monitoreo a largo plazo.
* **`mit-cloud-and-devops.pdf` & `mit-data-leadership.pdf`**:
  * *Contribución*: Respaldan la integración de infraestructura en la nube, pipelines de CI/CD automatizados y el liderazgo corporativo de iniciativas de datos.

---

# 10. Riesgos y decisiones discutibles

Un diseño curricular maduro debe reconocer explícitamente sus puntos de tensión interna y evaluar las alternativas viables:

### 10.1. ¿Separar Productos de Datos (Curso 5) y Operacionalización/DataOps (Curso 6) o fusionarlos en una malla de 5 cursos?
* **Decisión adoptada**: Separarlos en dos cursos distintos (Curso 5 centrado en la Tubería de Innovación y diseño de producto; Curso 6 centrado en la Tubería de Valor e industrialización operativa).
* **Riesgo percibido**: Puede argumentarse que seis cursos alargan la secuencia y que un producto de datos no debería concebirse sin pensar simultáneamente en su despliegue operativo.
* **La alternativa más fuerte**: Unificar ambos en un curso único denominado *"Productos de Datos y Operaciones Analíticas"* dentro de un esquema de 5 cursos.
* **Por qué se mantuvo la separación**: La evidencia de `dataops-04-lean-thinking.pdf` y `dataops-06-definition.pdf` demuestra que la **Tubería de Innovación** (ideación, UX, interacción humano-máquina, valor de negocio, APIs y MVPs) responde a una lógica de exploración y diseño de producto que resulta asfixiada si se sobrecarga al mismo tiempo con la ingeniería dura de la **Tubería de Valor** (Docker, CI/CD, pirámide completa de pruebas automatizadas, pruebas de balance, monitoreo de deriva en producción, gobierno de datos a nivel CDO y topología organizacional). Fusionar ambos temas en un solo curso genera inevitablemente una de dos fallas pedagógicas: o se reduce el producto a un simple dashboard exploratorio en Streamlit sin rigor operativo, o se reduce DataOps a scripts técnicos de despliegue ignorando la usabilidad y la adopción por parte del usuario.

### 10.2. La distribución de competencias DataOps: ¿Curso independiente, distribuidas o transversales?
* **Decisión adoptada**: Un **modelo híbrido escalonado**:
  1. *Prácticas transversales tempranas*: Control de versiones (Git), código modular, reproducibilidad y pruebas básicas de datos se introducen desde el Curso 2 (Ingeniería de Datos).
  2. *Consolidación en curso culminante*: La arquitectura formal de DataOps, la dualidad de tuberías, el CI/CD industrial, las pruebas de balance automatizadas, la observabilidad en producción y la coordinación relacional se sintetizan en el Curso 6.
* **Riesgo percibido**: Que los estudiantes pospongan la disciplina operativa hasta el último curso, o por el contrario, que el curso final sienta que repite temas de ingeniería de datos.
* **La alternativa más fuerte**: Distribuir DataOps exclusivamente a lo largo de los cursos sin crear una asignatura dedicada a la operacionalización.
* **Por qué se mantuvo el curso culminante**: Los documentos `dataops-06-definition.pdf`, `dataops-07-cdo.pdf` y `dataops-10-organization.pdf` demuestran que DataOps requiere una síntesis de alto nivel que involucra la relación entre infraestructura, modelos entrenados, flujos prescriptivos y estrategia corporativa. Un estudiante que aún no sabe construir un modelo predictivo (Curso 3) ni un motor prescriptivo (Curso 4) no puede aprender a monitorear la deriva de conceptos (*concept drift*), ni a implementar pipelines de despliegue de modelos (*MLOps*), ni a liderar la coordinación relacional entre científicos de datos e ingenieros.

### 10.3. Ubicación de la Inferencia Causal: ¿Curso Predictivo (Curso 3) o Prescriptivo (Curso 4)?
* **Decisión adoptada**: Ubicar la inferencia causal en el Curso 3, junto con la inferencia estadística y el aprendizaje automático predictivo.
* **Riesgo percibido**: Sobrecargar el Curso 3 con conceptos epistemológicos complejos mientras los estudiantes aprenden algoritmos de machine learning.
* **La alternativa más fuerte**: Mover la inferencia causal al Curso 4, conectándola directamente con la toma de decisiones y las intervenciones prescriptivas.
* **Por qué se ubicó en el Curso 3**: La evidencia de **Berkeley DATA C102** es contundente: el mayor peligro formativo es enseñar machine learning como un proceso aislado de minimización empírica del riesgo, permitiendo que los estudiantes confundan predicción correlacional con causalidad. La inferencia causal debe ser el contrapeso pedagógico inmediato al aprendizaje predictivo, enseñando desde el primer momento que $P(Y|X) \neq P(Y|\text{do}(X))$.

### 10.4. La Estrategia de Datos y el Rol del CDO: ¿Al inicio (Curso 1) o al cierre (Curso 6)?
* **Decisión adoptada**: Introducir la estrategia de datos y los casos de valor en el Curso 1 (para orientar el encuadre analítico) y consolidar el rol del CDO, la coordinación relacional y las topologías de equipos en el Curso 6.
* **Riesgo percibido**: Fragmentar el tema de gobernanza y estrategia en dos extremos del currículo.
* **Por qué se adoptó**: En el Curso 1, la estrategia de datos se requiere para saber qué problemas priorizar y cómo formular un caso de valor (`dataops-02-data-strategy.pdf`). En el Curso 6, la perspectiva del CDO se requiere para liderar la transformación organizacional, eliminar silos y gestionar la operación continua de los sistemas analíticos (`dataops-07-cdo.pdf`, `dataops-10-organization.pdf`).

---

# 11. Arquitectura final resumida

A continuación se presenta la síntesis estructural compacta del currículo propuesto, sus prerrequisitos y su flujo formativo:

### Estructura de Cursos y Prerrequisitos

```
[ Curso 1: Encuadre Estratégico y Analítica Descriptiva ]
       │
       ▼
[ Curso 2: Ingeniería de Datos y Tuberías Analíticas ]
       │
       ▼
[ Curso 3: Inferencia Estadística, Causalidad y Modelos Predictivos ]
       │
       ▼
[ Curso 4: Analítica Prescriptiva y Modelamiento de Decisiones ]
       │
       ▼
[ Curso 5: Diseño y Desarrollo de Productos de Datos ]
       │
       ▼
[ Curso 6: Operacionalización Analítica, DataOps y Ciclo de Vida ]
```

### Grafo de Dependencias y Flujo de Artefactos

* **Curso 1 $\longrightarrow$ Curso 2**: Entrega el encuadre formal del problema, la formulación del caso de valor y la auditoría inicial de las fuentes de datos.
* **Curso 2 $\longrightarrow$ Curso 3**: Entrega tuberías de datos automatizadas y reproducibles, esquemas modelados y capas de datos refinados con pruebas de calidad.
* **Curso 3 $\longrightarrow$ Curso 4**: Entrega modelos predictivos calibrados, cuantificación formal de incertidumbre y estimaciones de impacto causal.
* **Curso 4 $\longrightarrow$ Curso 5**: Entrega motores de optimización matemática, modelos de simulación estocástica y políticas de decisión óptimas.
* **Curso 5 $\longrightarrow$ Curso 6**: Entrega productos de datos modulares con interfaces de usuario y contratos de API (prototipos de la Tubería de Innovación).
* **Curso 6 (Cierre y Síntesis)**: Industrializa el producto en la Tubería de Valor corporativa mediante CI/CD, pirámide completa de pruebas automatizadas de lógica y datos, monitoreo de deriva en producción, gobernanza del ciclo de vida y alineación de equipos bajo los principios de DataOps.

Esta arquitectura asegura una formación integral, robusta y contemporánea, capaz de responder tanto a los más altos estándares académicos globales como a las exigencias operativas reales del entorno productivo moderno.
