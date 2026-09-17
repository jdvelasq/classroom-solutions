# Arquitectura Curricular en Analítica: Una Propuesta desde Primeros Principios

---

# 1. Lectura global del corpus

El análisis integral de los veintiún documentos que conforman el corpus documental revela que la **Analítica** (*Analytics*) no es una mera extensión utilitaria de la informática, ni un apéndice aplicado de la estadística clásica, ni un sinónimo contemporáneo del aprendizaje automático (*Machine Learning*). Por el contrario, la Analítica emerge como una **disciplina integradora y una práctica profesional autónoma** cuyo núcleo intelectual es la transformación sistemática, cuantitativa y reproducible de datos complejos en **decisiones operativas y estratégicas rigurosas bajo condiciones de incertidumbre**.

Al sintetizar el corpus en su conjunto, emergen tres grandes tradiciones o perspectivas complementarias que deben converger en un currículo coherente:

1. **La perspectiva de los estándares profesionales y el marco decisional (INFORMS CAP Essentials/Pro, INFORMS Analytics Framework):**
   Esta vertiente sitúa el punto de partida de la Analítica en el mundo de los problemas reales. La práctica analítica no se origina en un conjunto de datos disponible (*dataset*), sino en la necesidad de resolver una disyuntiva organizacional o social. El marco de INFORMS descompone este viaje en siete dominios interdependientes: el enmarcamiento del problema de negocio (*Business Problem Framing*), la traducción a un problema analítico (*Analytics Problem Framing*), la gestión del dato (*Data*), la selección metodológica (*Methodology Selection*), el desarrollo del modelo (*Analytics/Model Development*), el despliegue operativo (*Deployment*) y la gestión del ciclo de vida de la solución (*Analytics Solution Lifecycle Management*). Desde esta óptica, la Analítica es inherentemente orientada a la acción; un modelo estadístico o computacional carece de valor si no está anclado a un proceso decisorio y si no se operacionaliza dentro de un contexto institucional.

2. **La perspectiva académica y epistemológica (National Academies 2018, ACM 2021, UC Berkeley Data C101 y C102, University of Warwick, USC):**
   Esta corriente proporciona la solidez conceptual y el rigor metodológico. El informe de las *National Academies of Sciences, Engineering, and Medicine (2018)* introduce el concepto articulador de **Perspicacia con los Datos** (*Data Acumen*): la capacidad de razonar de manera crítica a través de todo el ciclo de vida de los datos, reconociendo las limitaciones de las herramientas, la procedencia del dato, las fuentes de sesgo, la reproducibilidad y las implicaciones éticas. Por su parte, la *ACM (2021)* formaliza el cuerpo de conocimiento a través de áreas de competencia que exigen balancear la infraestructura computacional (*Big Data Systems*, *Cloud Computing*, *Data Management*) con el análisis algorítmico (*Machine Learning*, *Data Mining*, *Interface Design*). Asimismo, la aproximación curricular de UC Berkeley (DATA C101 y C102) articula dos pilares fundamentales: por un lado, la ingeniería de datos a escala para habilitar la analítica confiable; por el otro, la teoría de la inferencia, la causalidad y las decisiones (*Data, Inference, and Decisions*), que rescata la inferencia probabilística, el diseño experimental y el control de tasas de error falsas como contrapeso al empirismo ciego del aprendizaje automático superficial.

3. **La perspectiva de sistemas, ingeniería, plataformas y liderazgo (MIT, PwC, Cambridge Judge Business School):**
   El conjunto de programas del MIT (*Data Engineering*, *Data Science and Analytics*, *Quantitative Methods in Systems Engineering*, *Machine Learning, Modeling and Simulation Principles*, *Cloud and DevOps*, *Designing AI Products*, *Digital Platforms*, *Data Leadership*) y las escuelas profesionales de negocios (Cambridge, PwC) evidencian que la analítica moderna no opera en el vacío artesanal de los cuadernos de programación (*notebooks*). La analítica madura exige:
   - **Ingeniería de datos de producción:** canalizaciones de datos (*data pipelines*), captura de datos de cambio (*Change Data Capture - CDC*), procesamiento en tiempo real (*streaming*), contenerización y orquestación.
   - **Analítica prescriptiva y teoría de decisiones complejas:** métodos cuantitativos de compensación (*trade studies*), teoría de utilidad multiatributo (*Multi-Attribute Utility Theory - MAUT*), exploración de espacios de diseño de Pareto, y modelado y simulación estocástica de eventos raros.
   - **Productos analíticos y plataformas:** el tránsito de modelos analíticos aislados a productos de software interactivos centrados en el usuario, interfaces humano-IA, plataformas digitales de dos lados y APIs.
   - **Liderazgo y transformación organizacional:** juicio directivo, adopción por parte de los usuarios, gobernanza corporativa, gestión del cambio y realización de valor.

La síntesis de estas tres corrientes demuestra que un currículo en Analítica no puede concebirse como una secuencia lineal de herramientas de software (Python, SQL, Spark, Tableau), ni como un compendio de algoritmos de caja negra. La Analítica es la disciplina del **ciclo completo de la decisión guiada por datos**: desde la clarificación del dilema y la construcción de la infraestructura que sostiene la evidencia, pasando por el modelado inferencial, predictivo y prescriptivo, hasta la arquitectura del producto analítico, su despliegue y su supervisión continua en la sociedad.

---

# 2. Competencias que debe desarrollar la cadena completa

Un graduado de un programa de Analítica concebido desde este corpus debe poseer un repertorio holístico de competencias articuladas en torno a diez grandes familias formativas. Estas familias no describen un curso en particular, sino la capacidad integral acumulada al finalizar la totalidad del plan de estudios:

### Familia 1: Enmarcamiento, Formulación y Abstracción del Problema Decisional
- Capacidad para interactuar con partes interesadas (*stakeholders*) para desentrañar el problema de decisión latente tras síntomas operativos o demandas superficiales.
- Reformulación rigurosa del problema organizacional en una o más preguntas analíticas formidables, identificando objetivos cuantitativos, restricciones operativas, supuestos de negocio y métricas de éxito.
- Evaluación temprana de viabilidad técnica, disponibilidad de datos, horizonte temporal, costos de desarrollo y valor esperado de la solución analítica (*business case*).

### Familia 2: Ingesta, Curaduría, Calidad y Arquitectura de Datos a Escala
- Capacidad para adquirir, ingerir y conectar datos heterogéneos (estructurados, semiestructurados y no estructurados) provenientes de bases transaccionales, APIs, sistemas de eventos y repositorios masivos.
- Evaluación crítica de la procedencia, integridad, linaje y calidad de los datos, aplicando técnicas formales de limpieza, deduplicación, reconciliación y perfilado.
- Modelado de datos relacional y dimensional, así como esquemas para tecnologías NoSQL y almacenes analíticos distribuidos (*data warehouses*, *data lakes*, *lakehouses*).
- Diseño e implementación de canalizaciones reproducibles de procesamiento por lotes (*batch*) y por secuencias en tiempo real (*streaming*), utilizando principios de contenerización y orquestación.

### Familia 3: Exploración Analítica, Modelado Descriptivo y Comunicación de Evidencia
- Ejecución de análisis exploratorio de datos (*Exploratory Data Analysis - EDA*) para descubrir estructuras, anomalías, correlaciones espurias y distribuciones subyacentes.
- Síntesis descriptiva mediante estadística resumen robusta y agregaciones multidimensionales.
- Diseño de representaciones visuales de datos basadas en principios perceptuales, cognitivos y de diseño centrado en el usuario, evitando distorsiones visuales y artefactos engañosos.
- Comunicación efectiva de hallazgos mediante narrativas con datos (*storytelling*) adaptadas a audiencias técnicas, directivas y operativas, traduciendo evidencia estadística en implicaciones de negocio.

### Familia 4: Razonamiento Probabilístico, Inferencia Estadística y Gestión de la Incertidumbre
- Pensamiento estocástico y modelado formal de la variabilidad y la incertidumbre en procesos de generación de datos.
- Aplicación rigurosa de marcos inferenciales clásicos (frecuentistas) y bayesianos para estimación paramétrica, pruebas de hipótesis y cuantificación de errores.
- Control de tasas de descubrimientos falsos (*False Discovery Rate - FDR*) y corrección por multiplicidad de pruebas en contextos de alta dimensionalidad.
- Diseño y análisis de experimentos controlados aleatorizados (pruebas A/B multivariadas), pruebas de permutación y métodos de remuestreo (*bootstrap*).

### Familia 5: Modelado Predictivo y Aprendizaje Automático Generalizable
- Formulación y ajuste de algoritmos de aprendizaje supervisado (clasificación y regresión) y no supervisado (agrupamiento, reducción de dimensionalidad, filtrado colaborativo).
- Dominio del compromiso sesgo-varianza, principios de regularización matemática ($L_1, L_2$) y protocolos estrictos de validación cruzada y evaluación fuera de muestra (*out-of-sample*).
- Selección fundamentada de arquitecturas algorítmicas, abarcando modelos lineales generalizados, métodos de árboles y ensambles (*Random Forests*, *Gradient Boosting*), y redes neuronales profundas.
- Evaluación de modelos mediante matrices de costos asimétricos y curvas de rendimiento (ROC, PR, curvas de calibración probabilística), subordinando la precisión abstracta al valor de la decisión.
- Diagnóstico de explicabilidad, interpretabilidad algorítmica (SHAP, LIME) y auditoría de equidad e impacto dispar en predicciones.

### Familia 6: Inferencia Causal y Análisis Contrafactual
- Distinción formal, matemática y operativa entre asociación estadística, capacidad predictiva e impacto causal.
- Representación de supuestos causales mediante grafos acíclicos dirigidos (*Directed Acyclic Graphs - DAGs*) y modelos causales estructurales.
- Aplicación de métodos cuasiexperimentales sobre datos observacionales: variables instrumentales, emparejamiento por puntaje de propensión (*propensity score matching*), regresión discontinua y diferencias en diferencias.
- Estimación del efecto de intervenciones y políticas contrafactuales para responder a la pregunta directiva: *"¿Qué ocurriría si cambiamos la regla de decisión?"*

### Familia 7: Analítica Prescriptiva, Optimización y Simulación de Decisiones
- Modelado matemático de problemas prescriptivos mediante programación matemática (lineal, entera mixta, no lineal y estocástica).
- Modelado de valor y preferencias complejas mediante la Teoría de Utilidad Multiatributo (MAUT) y estructuración de estudios de compensación (*trade studies*).
- Generación y exploración de espacios de diseño, análisis de fronteras de Pareto y evaluación de compromisos (*trade-offs*) entre objetivos en conflicto.
- Simulación estocástica (Monte Carlo, eventos discretos) para evaluar la robustez de decisiones ante eventos extremos y dinámicas no lineales.
- Toma de decisiones secuenciales bajo incertidumbre, incluyendo bandidos multibrazo (*multi-armed bandits*) y aprendizaje por refuerzo básico.

### Familia 8: Operacionalización, Sistemas en Producción y MLOps
- Empaquetamiento, contenedorización e integración de modelos y tuberías analíticas en arquitecturas de software modernas mediante microservicios y APIs (REST/gRPC).
- Implementación de flujos de Integración y Despliegue Continuos (CI/CD) adaptados al ciclo de vida de datos y modelos (CT - *Continuous Training*).
- Registro, versionado y trazabilidad integral de código, datos, hiperparámetros y artefactos (*Model and Data Registries*).
- Monitoreo continuo de soluciones en producción: observabilidad técnica, latencia, detección de deriva de datos (*data drift*) y deriva de concepto (*concept drift*).
- Protocolos de degradación elegante, pruebas de contingencia, reentrenamiento automatizado y retiro de modelos obsoletos.

### Familia 9: Diseño de Productos Analíticos e Interacción Humano-Sistema
- Concepción de soluciones analíticas como productos digitales centrados en usuarios reales, aplicando metodologías de prototipado rápido y ciclos de retroalimentación iterativos.
- Diseño de interfaces analíticas e interacciones humano-computadora (HCI para analítica e IA interactiva), habilitando la colaboración entre inteligencia humana y sistemas autónomos (*superminds*).
- Comprensión de las dinámicas de plataformas digitales, economías de dos lados, efectos de red en datos y diseño de APIs de datos como canales de valor.

### Familia 10: Gobernanza, Ética, Privacidad y Responsabilidad Social
- Identificación proactiva de dilemas éticos a lo largo de la cadena analítica: sesgo en el muestreo, discriminación algorítmica, opacidad y riesgos sistémicos.
- Implementación de técnicas para la protección de la privacidad y seguridad de los datos (anonimización, privacidad diferencial, cifrado y control de accesos basado en roles).
- Alineación con marcos de gobernanza de datos y regulación de IA responsable, garantizando auditoría, responsabilidad (*accountability*), transparencia y cumplimiento normativo.

---

# 3. Tensiones y decisiones curriculares fundamentales

El diseño de un currículo coherente exige abordar explícitamente las tensiones epistémicas, conceptuales y prácticas que el corpus pone al descubierto. Estas disyuntivas no deben ocultarse, sino resolverse de forma deliberada en la arquitectura formativa:

### 3.1. Estadística vs. Machine Learning
- **La tensión:** La tradición estadística clásica prioriza la inferencia sobre el proceso generador de datos, la parsimonia, las propiedades asintóticas de los estimadores y la interpretabilidad estructural. El aprendizaje automático moderno prioriza el poder predictivo empírico, la capacidad de generalización sobre datos no observados, la optimización numérica no convexa y la capacidad de absorber alta dimensionalidad y no linealidades complejas, a menudo a expensas de la transparencia analítica.
- **Decisión curricular:** No se debe reemplazar la estadística por el machine learning ni viceversa. El currículo debe enseñar primero los fundamentos probabilísticos de la estimación, la variabilidad muestral y el modelado probabilístico, para luego construir sobre ellos los conceptos de aprendizaje supervisado, regularización y optimización de funciones de pérdida. El estudiante debe entender que el machine learning es una extensión computacional y optimizadora de la inferencia empírica, pero que sin rigor probabilístico conduce inevitablemente a sobreajuste, ilusiones de correlación y fallos de validación.

### 3.2. Predicción vs. Inferencia Estadística
- **La tensión:** La inferencia estadística busca responder *"¿cuál es la relación verosímil entre la variable $X$ y el fenómeno $Y$, y cuál es el nivel de incertidumbre de esa estimación en la población?"*. La predicción busca responder *"dado un vector de características $X$, ¿cuál es el valor más probable de $Y$ en una instancia no observada?"*. Un modelo con excelente capacidad predictiva puede tener estimadores inestables o coeficientes estadísticamente ambiguos si existe multicolinealidad severa.
- **Decisión curricular:** Debe separarse pedagógicamente la enseñanza del razonamiento inferencial (estimación de parámetros, intervalos de confianza, contrastes de hipótesis y control de descubrimientos falsos) de la construcción de modelos predictivos orientados a la minimización del riesgo empírico. El currículo debe enfatizar que predecir con precisión no equivale a comprender la estructura del fenómeno.

### 3.3. Predicción vs. Inferencia Causal
- **La tensión:** La predicción opera bajo la distribución observacional pasiva $P(Y|X)$. La inferencia causal opera bajo la distribución de intervención activa $P(Y|\text{do}(X))$. Confundir predicción con causalidad es uno de los errores más costosos en la práctica analítica: una variable altamente predictiva (como el uso de un fármaco o la visita a una página de soporte) puede ser un síntoma y no la causa de un desenlace, por lo que intervenir sobre ella basándose en un modelo predictivo puede tener consecuencias desastrosas.
- **Decisión curricular:** La inferencia causal y el diseño experimental deben tener un estatus formativo explícito y riguroso. No pueden reducirse a una mención lateral en un curso de regresión. Los estudiantes deben dominar el uso de grafos causales (DAGs), el diseño de experimentos A/B, el marco de resultados potenciales (*potential outcomes*) y los métodos cuasiexperimentales para evaluar políticas de intervención.

### 3.4. Predicción vs. Prescripción
- **La tensión:** La analítica predictiva anticipa lo que sucederá en el futuro dado el estado actual; la analítica prescriptiva determina **qué se debe hacer** para optimizar un resultado bajo restricciones operacionales, escasez de recursos y compensaciones de valor. Conocer una predicción (e.g., demanda futura estimada) no indica automáticamente la decisión óptima (e.g., plan de producción e inventario que minimiza costos de ruptura y almacenamiento bajo restricciones de capacidad).
- **Decisión curricular:** El currículo debe reservar un espacio nuclear para la analítica prescriptiva que conecte de forma natural con los modelos predictivos. Los modelos predictivos no son el fin de la analítica; son las funciones de entrada y los parámetros estocásticos que alimentan los motores de optimización y decisión prescriptiva.

### 3.5. Optimización Matemática vs. Analítica Decisional Amplia
- **La tensión:** La Investigación de Operaciones académica tradicional suele concentrarse en la programación matemática formal (algoritmos símplex, ramificación y acotamiento, dualidad, teoría de politopos). Sin embargo, en el ejercicio profesional de la Analítica (como destacan MIT Systems Engineering e INFORMS), los problemas reales involucran múltiples objetivos en conflicto, preferencias subjetivas no lineales de las partes interesadas, incertidumbre no estructurada y necesidad de análisis de compensaciones (*trade-offs*).
- **Decisión curricular:** No equiparar la analítica prescriptiva con la teoría algorítmica de la Investigación de Operaciones abstracta. Se debe enseñar programación matemática (lineal, entera, no lineal), pero integrada con la Teoría de Utilidad Multiatributo (MAUT), los estudios de compensación (*trade studies*), la exploración de fronteras de Pareto, la simulación estocástica y la toma de decisiones robustas bajo riesgo.

### 3.6. Ciencia de Datos vs. Ingeniería de Datos
- **La tensión:** En muchos programas académicos, la ingeniería de datos se relega a la administración de infraestructura de sistemas (TI) o se ignora, asumiendo que los datos ya residen en archivos CSV limpios. En la realidad industrial (como demuestran UC Berkeley Data C101 y MIT Data Engineering), más del 70% del esfuerzo analítico se invierte en la ingesta, integración, limpieza, estructuración y escalabilidad de datos complejos.
- **Decisión curricular:** La Ingeniería de Datos no es soporte periférico; es un componente central de la Analítica. Sin embargo, no debe reducirse a la administración de servidores ni a devops de bajo nivel, sino enfocarse en el ciclo de vida del dato a escala: modelado relacional y NoSQL, canalizaciones ETL/ELT, captura de cambios en bases de datos (CDC), procesamiento distribuido, streaming y gobernanza de la calidad.

### 3.7. Análisis en Cuadernos (*Notebooks*) vs. Sistemas de Producción Operacionales
- **La tensión:** La formación universitaria típica entrena a los estudiantes para explorar datos en cuadernos interactivos lineales (*Jupyter Notebooks*) que nunca salen del entorno local. En la práctica profesional (INFORMS Dominios VI y VII, MIT Cloud and DevOps), los modelos deben ejecutarse de manera confiable, automatizada, con baja latencia y alta concurrencia dentro del ecosistema de software corporativo.
- **Decisión curricular:** El currículo debe forzar la transición desde el análisis interactivo exploratorio hacia las buenas prácticas de desarrollo de software: modularización en paquetes, control de versiones formal (Git), pruebas unitarias e integración continua, contenedorización (Docker), empaquetamiento de modelos en APIs y despliegue automatizado.

### 3.8. Modelado Aislado vs. Gestión del Ciclo de Vida y MLOps
- **La tensión:** Los cursos estándar evalúan a los estudiantes sobre un conjunto estático de datos de prueba (*test set*) y dan por terminada la tarea cuando se alcanza un valor determinado de métrica ($R^2$ o AUC). En el mundo real, los modelos comienzan a degradarse en el instante en que se despliegan debido a cambios en el comportamiento de los clientes, fluctuaciones macroeconómicas o cambios en los sistemas de captura (*data drift* y *concept drift*).
- **Decisión curricular:** Debe incorporarse formalmente la disciplina de MLOps y el ciclo de vida de la solución (Dominio VII de INFORMS): registro de modelos, observabilidad, monitorización de deriva estadística, reentrenamiento periódico programado y gobernanza de retiro.

### 3.9. Análisis Técnico vs. Toma de Decisiones Organizacionales
- **La tensión:** Es común formar profesionales técnicamente competentes que son incapaces de entender el contexto estratégico de la organización, que no saben cómo formular un caso de negocio, que no pueden explicar las suposiciones de un modelo a un directivo no técnico y que ignoran los factores humanos de la adopción tecnológica.
- **Decisión curricular:** El currículo debe iniciar y culminar con el impacto decisional y humano. Desde el enmarcamiento inicial del problema y la alineación con los tomadores de decisiones (INFORMS I-II), hasta el diseño de productos analíticos interactivos, interfaces humano-sistema, plataformas y gestión del cambio cultural (MIT Designing AI Products, MIT Data Leadership, Cambridge, PwC).

---

# 4. Arquitectura curricular propuesta

A partir de las competencias exigidas y la resolución de las tensiones fundamentales, se propone una **cadena formativa de siete cursos macro**. Esta arquitectura articula una progresión lógica y epistemológica rigurosa: desde la formulación del problema y la preparación del dato, pasando por la escala computacional, el rigor inferencial/causal, la capacidad predictiva y la optimización prescriptiva, hasta la ingeniería de producción y la creación de productos analíticos de alto impacto.

```
[Curso 1: Formulación de Problemas, Exploración de Datos y Comunicación de Evidencia]
                                      │
                                      ▼
             [Curso 2: Ingeniería de Datos y Sistemas Escalables]
                                      │
                                      ▼
             [Curso 3: Inferencia Estadística, Incertidumbre y Causalidad]
                                      │
                                      ▼
             [Curso 4: Modelado Predictivo y Aprendizaje Automático]
                                      │
                                      ▼
             [Curso 5: Analítica Prescriptiva, Optimización y Decisiones]
                                      │
                                      ▼
             [Curso 6: Operacionalización, MLOps y Ciclo de Vida]
                                      │
                                      ▼
             [Curso 7: Productos de Datos, Interacción Humano-IA y Estrategia]
```

---

### Curso 1: Formulación de Problemas, Exploración de Datos y Comunicación de Evidencia
- **Posición en la secuencia:** Curso 1 (Punto de entrada a la cadena).
- **Propósito central:** Desarrollar la capacidad de traducir problemas organizacionales y decisionales mal definidos en preguntas analíticas resolubles; forjar la *perspicacia con los datos* (*data acumen*) mediante la ingesta, limpieza, perfilado y análisis exploratorio riguroso; y dominar la comunicación persuasiva de evidencia cuantitativa mediante diseño visual y narrativa analítica.
- **Principales competencias:**
  - Enmarcamiento y clarificación de problemas de negocio y decisión (INFORMS Dominios I y II).
  - Adquisición de datos estructurados y semiestructurados desde archivos planos, bases de datos y APIs web básicas.
  - Limpieza, manipulación, transformación y perfilado de datos mediante programación analítica (Python/Pandas).
  - Análisis exploratorio de datos (EDA) multivariado para detección de anomalías, valores atípicos y patrones distributivos.
  - Diseño de visualizaciones efectivas fundamentadas en percepción gráfica humana y gramática de gráficos (ACM AP).
  - Comunicación estructurada de evidencia mediante narrativas cuantitativas (*storytelling*) e informes reproducibles.
  - Razonamiento inicial sobre procedencia del dato, reproducibilidad del flujo de trabajo y ética analítica.
- **Prerrequisitos:** Conocimientos introductorios de álgebra elemental y fundamentos básicos de programación funcional/estructurada.
- **Qué recibe:** Estudiantes con motivación para resolver problemas reales pero con tendencia a pensar en soluciones técnicas desarticuladas o a confiar ciegamente en datos sin depurar.
- **Qué prepara para hacer después:** Entrega la disciplina de enmarcar problemas rigurosamente y comprender la naturaleza sucia y heterogénea de los datos reales, preparando al estudiante para aprender a gestionar datos masivos de forma robusta y automatizada (Curso 2) y para formular modelos formales de incertidumbre e hipótesis (Curso 3).

---

### Curso 2: Ingeniería de Datos y Sistemas Escalables
- **Posición en la secuencia:** Curso 2 (Pilar de infraestructura y computación).
- **Propósito central:** Capacitar al estudiante para diseñar, construir y operar la infraestructura técnica y las canalizaciones de datos que permiten almacenar, transformar y entregar datos de manera confiable, escalable y gobernada para su consumo en modelos analíticos avanzados.
- **Principales competencias:**
  - Modelado conceptual, lógico y físico de bases de datos relacionales (PostgreSQL) y formulación avanzada de consultas SQL analíticas.
  - Modelos de datos no relacionales y distribuidos (documentales, clave-valor, columnas anchas).
  - Arquitectura de almacenes analíticos modernos: *Data Warehouses*, *Data Lakes* y *Lakehouses* (formatos columnares como Parquet).
  - Diseño e implementación de canalizaciones reproducibles ETL/ELT por lotes (*batch*) y por secuencias (*streaming* con Kafka).
  - Captura de datos de cambio (*Change Data Capture - CDC*) mediante herramientas como Debezium para sincronización de bases operacionales y analíticas.
  - Orquestación de flujos de trabajo basados en grafos acíclicos dirigidos (DAGs con Apache Airflow).
  - Procesamiento analítico distribuido para grandes volúmenes de datos (PySpark / Dask).
  - Contenerización de entornos y servicios analíticos mediante Docker.
  - Prácticas de gobernanza técnica, calidad de datos, pruebas de integridad y catalogación de metadatos.
- **Prerrequisitos:** Curso 1 (Formulación de Problemas, Exploración de Datos y Comunicación de Evidencia).
- **Qué recibe del curso previo:** Comprensión de las anomalías de datos, tipos de variables y los requerimientos de preparación que exige el análisis de datos en pequeña y mediana escala.
- **Qué prepara para hacer después:** Garantiza que el estudiante pueda alimentar con datos limpios, reproducibles y a escala los modelos inferenciales (Curso 3), predictivos (Curso 4) y prescriptivos (Curso 5), y establece la base de contenedores y pipelines necesaria para la operacionalización (Curso 6).

---

### Curso 3: Inferencia Estadística, Incertidumbre y Causalidad
- **Posición en la secuencia:** Curso 3 (Pilar de rigor matemático, inferencial y epistemológico).
- **Propósito central:** Desarrollar el razonamiento estocástico riguroso para cuantificar la incertidumbre en procesos empíricos; dominar los paradigmas inferenciales frecuentista y bayesiano; y diferenciar de manera categórica la asociación estadística de la inferencia causal, dotando al estudiante de herramientas para evaluar el impacto de intervenciones y experimentos.
- **Principales competencias:**
  - Modelado probabilístico formal, funciones de distribución, variables aleatorias y teoría asintótica.
  - Estimación puntual y por intervalos; métodos de remuestreo empírico (*bootstrap*, pruebas de permutación).
  - Pruebas de hipótesis clásicas y control de multiplicidad de pruebas (control de errores tipo I/II y *False Discovery Rate - FDR*).
  - Inferencia Bayesiana: distribuciones a priori y a posteriori, muestreo MCMC e inferencia en modelos jerárquicos básicos.
  - Fundamentos de privacidad estadística y Privacidad Diferencial (*Differential Privacy*).
  - Diseño y análisis formal de experimentos controlados aleatorizados (pruebas A/B multivariadas, asignación y potencia estadística).
  - Inferencia causal estructural: grafos causales (DAGs), criterio de puerta trasera (*backdoor criterion*) y el operador $\text{do}(\cdot)$.
  - Métodos cuasiexperimentales sobre datos observacionales: emparejamiento (*matching*), variables instrumentales, regresión discontinua y diferencias en diferencias.
- **Prerrequisitos:** Curso 1 (Fundamentos y Exploración de Datos) y cálculo diferencial/álgebra lineal básica.
- **Qué recibe del curso previo:** Dominio en la manipulación y exploración de datos, y capacidad para plantear hipótesis de análisis claras.
- **Qué prepara para hacer después:** Otorga el rigor epistemológico indispensable para validar apropiadamente modelos de Machine Learning (Curso 4), suministrar distribuciones de probabilidad a la analítica prescriptiva (Curso 5) y evitar confusiones letales entre correlación y causa en la toma de decisiones.

---

### Curso 4: Modelado Predictivo y Aprendizaje Automático
- **Posición en la secuencia:** Curso 4 (Pilar predictivo y algorítmico).
- **Propósito central:** Desarrollar la capacidad de formular, entrenar, optimizar y evaluar modelos de aprendizaje automático capaces de predecir desenlaces futuros o clasificar entidades con alta capacidad de generalización fuera de muestra, vinculando el rendimiento técnico con las consecuencias económicas y operativas del error.
- **Principales competencias:**
  - Paradigmas de aprendizaje supervisado y no supervisado; formulación matemática de funciones de pérdida y riesgo empírico.
  - Compromiso sesgo-varianza, sobreajuste (*overfitting*) y regularización rigurosa ($L_1$ Lasso, $L_2$ Ridge, ElasticNet).
  - Modelos lineales generalizados (GLM): regresión logística, multinomial y Poisson.
  - Métodos no lineales basados en árboles: árboles de decisión (CART), ensambles paralelos (*Random Forests*) y ensambles secuenciales (*Gradient Boosted Trees*: XGBoost, LightGBM).
  - Fundamentos de redes neuronales profundas (*Deep Learning*): perceptrón multicapa, propagación hacia atrás (*backpropagation*), funciones de activación y optimizadores estocásticos (SGD, Adam).
  - Métodos de agrupamiento (*clustering*: k-means, DBSCAN, jerárquico) y reducción de dimensionalidad (PCA, t-SNE) para aprendizaje no supervisado.
  - Protocolos de validación rigurosos: validación cruzada estratificada y temporal, curvas ROC/PR, calibración de probabilidades y evaluación basada en matrices de costo de decisión.
  - Interpretabilidad algorítmica y explicabilidad (valores SHAP, LIME, importancia de características).
  - Auditoría de equidad, sesgo algorítmico y disparidad de impacto en predicciones automatizadas.
- **Prerrequisitos:** Curso 2 (Canalizaciones de datos a escala) y Curso 3 (Probabilidad, inferencia y diseño experimental).
- **Qué recibe de cursos previos:** Canalizaciones reproducibles y datos escalables (Curso 2); protocolos de diseño experimental, control de error y comprensión de distribuciones (Curso 3).
- **Qué prepara para hacer después:** Proporciona los modelos predictivos que generan estimaciones y pronósticos para los sistemas prescriptivos (Curso 5) y genera los artefactos algorítmicos que deben empaquetarse y monitorearse en producción (Curso 6).

---

### Curso 5: Analítica Prescriptiva, Optimización y Simulación de Decisiones
- **Posición en la secuencia:** Curso 5 (Pilar de acción, optimización y decisión).
- **Propósito central:** Capacitar al estudiante para dar el salto desde la predicción hacia la prescripción óptima; formular y resolver problemas de decisión complejos bajo restricciones operativas, escasez de recursos y múltiples objetivos en conflicto; y modelar sistemas estocásticos dinámicos mediante simulación.
- **Principales competencias:**
  - Estructuración formal de problemas de optimización matemática: variables de decisión, funciones objetivo y restricciones.
  - Programación lineal (LP), programación entera mixta (MIP) y programación no lineal (NLP) aplicada a asignación de recursos, logística, precios y planificación.
  - Optimización estocástica y optimización robusta: toma de decisiones con parámetros predictivos inciertos generados por modelos del Curso 4.
  - Teoría de Utilidad Multiatributo (MAUT), funciones de valor y estructuración de estudios de compensación (*trade studies*) para evaluar alternativas complejas (según metodología de ingeniería de sistemas del MIT).
  - Exploración de espacios de diseño, análisis de fronteras de Pareto y cuantificación de compromisos (*trade-offs*) multidimensionales.
  - Modelado y simulación estocástica: simulación Monte Carlo, simulación de eventos discretos, análisis de sensibilidad global y modelado de eventos raros.
  - Toma de decisiones secuenciales bajo incertidumbre: árboles de decisión, bandidos multibrazo (*multi-armed bandits*) y fundamentos de control y aprendizaje por refuerzo (*Q-learning*).
- **Prerrequisitos:** Curso 3 (Razonamiento probabilístico y causalidad) y Curso 4 (Modelado predictivo como insumo de parámetros).
- **Qué recibe de cursos previos:** Comprensión de incertidumbre y efectos causales (Curso 3); pronósticos probabilísticos de demanda, riesgo o fallas (Curso 4).
- **Qué prepara para hacer después:** Genera las políticas de decisión y algoritmos de asignación óptima que deben ser operacionalizados e integrados en sistemas de producción (Curso 6) y embebidos en productos analíticos interactivos (Curso 7).

---

### Curso 6: Operacionalización, MLOps y Ciclo de Vida de Soluciones Analíticas
- **Posición en la secuencia:** Curso 6 (Pilar de ingeniería de software para analítica e implementación continua).
- **Propósito central:** Desarrollar las competencias de ingeniería para llevar modelos predictivos y políticas prescriptivas desde entornos locales de experimentación hacia sistemas de producción confiables, escalables y gobernados; implementar canalizaciones de MLOps; y gestionar el ciclo de vida continuo de las soluciones analíticas.
- **Principales competencias:**
  - Principios de ingeniería de software para analítica: modularización, tipado, pruebas unitarias y de integración, control de versiones avanzado con Git.
  - Empaquetamiento de modelos analíticos y creación de servicios web de inferencia mediante APIs (FastAPI / gRPC) y microservicios en contenedores (Docker).
  - Paradigmas de inferencia: predicción por lotes (*batch scoring*), inferencia en tiempo real de baja latencia y procesamiento en secuencias (*streaming inference*).
  - Integración Continua, Entrega Continua y Entrenamiento Continuo (CI/CD/CT) adaptado a analítica (GitHub Actions, orquestación de tuberías MLOps).
  - Registro, gobernanza y versionado de modelos, hiperparámetros y conjuntos de datos (*Model Registries* como MLflow).
  - Observabilidad analítica y monitoreo en tiempo real: seguimiento de métricas de servicio (latencia, throughput, memoria) y métricas de desempeño analítico.
  - Detección sistemática de degradación: deriva de datos (*data drift*), deriva de concepto (*concept drift*) y valores fuera de distribución (*out-of-distribution*).
  - Estrategias de despliegue controlado (*shadow deployments*, despliegues *canary*, pruebas A/B en producción) y mecanismos de reversión (*rollback*).
  - Resiliencia operativa, seguridad en APIs de modelos y gestión del retiro formal (*retirement*) de soluciones analíticas obsoletas (INFORMS Dominio VII).
- **Prerrequisitos:** Curso 2 (Ingeniería de datos y contenedores) y Cursos 4 y 5 (Modelos predictivos y prescriptivos a desplegar).
- **Qué recibe de cursos previos:** Bases de infraestructura de datos y Docker (Curso 2); artefactos matemáticos, predictivos y prescriptivos validados (Cursos 4 y 5).
- **Qué prepara para hacer después:** Garantiza que los modelos operen de manera robusta como servicios desatendidos, listos para ser consumidos por productos de datos orientados a usuarios finales y plataformas empresariales (Curso 7).

---

### Curso 7: Productos de Datos, Interacción Humano-IA y Transformación Organizacional
- **Posición en la secuencia:** Curso 7 (Curso integrador, estratégico y capstone de la cadena).
- **Propósito central:** Articular la convergencia de la analítica avanzada con el diseño de productos digitales, la interacción humano-sistema y la estrategia corporativa; habilitar al estudiante para concebir, diseñar y liderar la implementación de productos de datos interactivos que generen valor medible, fomenten la adopción organizacional y cumplan con rigurosos estándares éticos y de gobernanza.
- **Principales competencias:**
  - Metodología de diseño de productos analíticos y de IA: identificación de casos de uso de alto impacto, mapeo de necesidades de usuarios y formulación de la propuesta de valor del producto.
  - Metodologías de prototipado rápido (*rapid prototyping*): desarrollo ágil de productos mínimos viables (MVP) analíticos y bucles de retroalimentación temprana.
  - Diseño de interacción humano-computadora para analítica (HCI para IA): interfaces de toma de decisiones aumentadas, presentación de recomendaciones algorítmicas, explicabilidad interactiva y diseño para la colaboración humano-máquina (*superminds*).
  - Plataformas digitales y economías de datos: arquitecturas de dos lados, APIs de datos como productos, efectos de red en datos y modelos de monetización.
  - Liderazgo analítico y gestión del cambio organizacional: superación de barreras culturales a la adopción de datos, rediseño de procesos, alineación de incentivos y medición del retorno sobre la inversión analítica (ROI).
  - Gobernanza corporativa de la analítica y marcos de IA Responsable: auditorías de cumplimiento, rendición de cuentas, políticas de transparencia y gestión de riesgos sistémicos.
  - Ejecución de un proyecto integrador (*capstone*) que atraviese todos los dominios de INFORMS: desde el problema de negocio original hasta el producto de datos funcional y su plan de adopción.
- **Prerrequisitos:** Cursos 1 a 6 (Haber completado o estar cursando en paralelo la totalidad de la cadena técnica).
- **Qué recibe de cursos previos:** La totalidad de las capacidades analíticas: enmarcamiento y datos (C1), arquitectura escalable (C2), rigor inferencial (C3), modelos predictivos (C4), prescripción óptima (C5) e infraestructura operativa en producción (C6).
- **Qué prepara para hacer después:** Prepara al egresado para desempeñarse como líder analítico, científico de datos principal (*lead data scientist*), ingeniero de analítica (*analytics engineer*) o gerente de producto analítico (*analytics product manager*), capaz de transformar organizaciones mediante soluciones analíticas completas, sostenibles y éticas.

---

# 5. Fronteras entre cursos

Para garantizar la coherencia interna de la arquitectura y evitar tanto vacíos formativos como duplicaciones redundantes, se definen explícitamente las fronteras epistemológicas y metodológicas entre cada par de cursos adyacentes:

### 5.1. Frontera entre Curso 1 (Formulación y Exploración) y Curso 2 (Ingeniería de Datos)
- **Dónde termina el Curso 1:** El Curso 1 concluye con la exploración interactiva, la limpieza manual o semi-automatizada en memoria local (usando scripts y DataFrames de Pandas) de conjuntos de datos estáticos previamente extraídos, y la comunicación visual de hallazgos para responder preguntas descriptivas puntuales.
- **Dónde comienza el Curso 2:** El Curso 2 comienza cuando los datos no caben en memoria, no provienen de un archivo estático aislado, cambian en tiempo real o requieren una infraestructura persistente, transaccional o distribuida. Aborda el diseño de esquemas de bases de datos relacionales y no relacionales, canalizaciones automatizadas y orquestadas (ETL/ELT), captura de cambios (CDC) y procesamiento paralelo.
- **Tema en disputa:** *Limpieza y transformación de datos (Data Wrangling).*
  - *Justificación de la frontera:* En el Curso 1, el *wrangling* se enseña desde la perspectiva semántica del analista: entender el significado de las variables, imputar valores atípicos evidentes, codificar categorías y explorar distribuciones para responder una pregunta inmediata. En el Curso 2, la transformación de datos se aborda desde la perspectiva sistémica de la ingeniería: diseñar tuberías repetibles, idempotentes, validadas mediante esquemas de calidad automatizados, desacopladas mediante mensajería y optimizadas para su ingestión en almacenes analíticos masivos.

### 5.2. Frontera entre Curso 2 (Ingeniería de Datos) y Curso 3 (Inferencia y Causalidad)
- **Dónde termina el Curso 2:** El Curso 2 termina cuando los datos han sido capturados, limpiados, transformados, almacenados de forma distribuida y puestos a disposición a través de consultas analíticas o tablas analíticas optimizadas (*gold tables* o *data marts*).
- **Dónde comienza el Curso 3:** El Curso 3 comienza en el momento en que se cuestiona el proceso generador de esos datos: ¿provienen de una muestra representativa?, ¿cuál es la variabilidad estocástica inherente?, ¿qué hipótesis podemos contrastar con validez estadística?, ¿reflejan correlación o una relación causal genuina?
- **Tema en disputa:** *Diseño de experimentos y muestreo (A/B testing).*
  - *Justificación de la frontera:* El Curso 2 proporciona los mecanismos de ingeniería para registrar eventos, telemetría y particionar tráfico de usuarios en bases de datos. Sin embargo, el Curso 3 es el dueño absoluto de la lógica de asignación aleatoria, cálculo del tamaño muestral, potencia estadística, control de tasa de descubrimientos falsos y formalización de contrafactuales. La ingeniería ejecuta el flujo; la inferencia garantiza la validez de la conclusión.

### 5.3. Frontera entre Curso 3 (Inferencia y Causalidad) y Curso 4 (Modelado Predictivo)
- **Dónde termina el Curso 3:** El Curso 3 concluye con la comprensión de los mecanismos causales y la estimación rigurosa de parámetros poblacionales con sus intervalos de confianza, asegurando que el analista sepa si una relación observada es atribuible al azar, a un sesgo de selección, o a una intervención causal identificable.
- **Dónde comienza el Curso 4:** El Curso 4 comienza cuando el objetivo prioritario deja de ser la estimación no sesgada de un parámetro o la prueba de una hipótesis, y pasa a ser la optimización del rendimiento predictivo empírico sobre instancias futuras o no observadas, explotando patrones complejos, alta dimensionalidad y no linealidades.
- **Tema en disputa:** *Regresión lineal y modelos lineales generalizados (GLM).*
  - *Justificación de la frontera:* En el Curso 3, la regresión se estudia como una herramienta inferencial: supuestos de Gauss-Markov, significancia estadística de coeficientes ($p$-valores), intervalos de confianza e identificación de efectos causales con control de variables confusoras. En el Curso 4, la regresión se reformula como un problema de optimización de una función de pérdida bajo regularización ($L_1, L_2$), evaluada mediante particiones de validación cruzada y métricas de error de predicción (RMSE, MAE), sin requerir que los coeficientes individuales tengan interpretación estructural.

### 5.4. Frontera entre Curso 4 (Modelado Predictivo) y Curso 5 (Analítica Prescriptiva)
- **Dónde termina el Curso 4:** El Curso 4 culmina cuando se ha obtenido y evaluado un modelo capaz de generar estimaciones probabilísticas o puntuales sobre variables de interés futuras (e.g., probabilidad de deserción de un cliente, volumen esperado de demanda de un producto, riesgo de falla de un componente).
- **Dónde comienza el Curso 5:** El Curso 5 comienza en el instante en que se debe decidir qué acción emprender ante esas predicciones. Saber que un cliente tiene un 78% de probabilidad de abandonar el servicio no define qué oferta comercial maximiza el valor esperado de la compañía considerando un presupuesto limitado de retención y diferentes sensibilidades al precio.
- **Tema en disputa:** *Árboles de decisión vs. Programación matemática.*
  - *Justificación de la frontera:* Los árboles de decisión y bosques aleatorios del Curso 4 son algoritmos de particionamiento predictivo supervisado (clasificación y regresión basadas en datos). Los árboles de decisión y métodos prescriptivos del Curso 5 son representaciones de alternativas de decisión secuencial bajo riesgo, donde las ramas representan elecciones humanas y eventos de la naturaleza con matrices de pago (*payoff matrices*) y funciones de utilidad. El Curso 4 predice desenlaces; el Curso 5 prescribe políticas óptimas.

### 5.5. Frontera entre Curso 5 (Analítica Prescriptiva) y Curso 6 (Operacionalización y MLOps)
- **Dónde termina el Curso 5:** El Curso 5 termina con la especificación matemática y algorítmica de la política de decisión, el modelo de optimización o la simulación resuelta mediante solvers y scripts de experimentación analítica.
- **Dónde comienza el Curso 6:** El Curso 6 comienza cuando esa política, algoritmo u optimizador debe empaquetarse en un contenedor de software, exponerse mediante un endpoint de API con tiempos de respuesta garantizados, integrarse a una tubería de integración continua y monitorearse contra la degradación de sus entradas.
- **Tema en disputa:** *Tiempos de ejecución y restricciones computacionales.*
  - *Justificación de la frontera:* El Curso 5 aborda la formulación matemática para garantizar la factibilidad y optimalidad de la solución. El Curso 6 aborda la ingeniería del servicio: cómo desacoplar la ejecución pesada de un modelo mediante colas asíncronas, cómo balancear carga, cómo gestionar la memoria de los modelos en producción y cómo asegurar que las predicciones y prescripciones lleguen a los sistemas transaccionales con la latencia requerida por el negocio.

### 5.6. Frontera entre Curso 6 (Operacionalización y MLOps) y Curso 7 (Productos de Datos y Estrategia)
- **Dónde termina el Curso 6:** El Curso 6 concluye con una solución técnica en producción: un microservicio con monitoreo activo de *drift*, despliegue automatizado y canalizaciones resilientes.
- **Dónde comienza el Curso 7:** El Curso 7 comienza cuando esa capacidad operativa de producción se traduce en una experiencia tangible para un usuario humano (interfaz interactiva, explicabilidad cognitiva, soporte a la decisión) y en una iniciativa de valor estratégico dentro del modelo de negocio de la organización.
- **Tema en disputa:** *Métricas de éxito (Técnicas vs. Valor del Producto).*
  - *Justificación de la frontera:* El Curso 6 evalúa el éxito mediante métricas de sistema y estabilidad analítica: latencia, tasa de errores HTTP, PSI (*Population Stability Index*), deriva de Wasserstein y disponibilidad del servicio. El Curso 7 evalúa el éxito mediante métricas de producto, humanas y de negocio: tasa de adopción por parte del usuario, efectividad de la colaboración humano-máquina, retorno de inversión (ROI), impacto ético en la sociedad y transformación de la cultura organizacional.

---

# 6. Competencias transversales

Existen competencias fundamentales que, por su naturaleza sistémica y duradera, no pueden quedar encapsuladas en un curso aislado sin riesgo de desconexión práctica. El currículo establece **diez hilos conductores transversales** que deben ejercitarse y evaluarse progresivamente a lo largo de los siete cursos:

1. **Enmarcamiento y traducción de problemas (Problem Framing):**
   - Desde la formulación inicial en el Curso 1, pasando por la delimitación de restricciones en ingeniería de datos (Curso 2), el diseño de hipótesis causales (Curso 3), la elección de funciones de costo (Curso 4), la definición de objetivos en optimización (Curso 5), hasta los requerimientos de servicio (Curso 6) y el diseño de la propuesta de valor del producto (Curso 7).

2. **Reproducibilidad y gestión rigurosa de artefactos:**
   - La reproducibilidad no es un tema de una semana; es una ética de trabajo. Comienza en el Curso 1 con entornos virtuales y control de versiones elemental, avanza en el Curso 2 con canalizaciones de datos deterministas, en el Curso 3 con semillas aleatorias y registros de experimentación, en el Curso 4 con particiones reproducibles y registro de hiperparámetros, en el Curso 5 con trazabilidad de instancias de optimización, y madura en los Cursos 6 y 7 con herramientas formales de MLOps (DVC, MLflow) y repositorios de código profesionales (Git/CI).

3. **Razonamiento y cuantificación explícita de la incertidumbre:**
   - La analítica se distingue del determinismo informático por su convivencia constante con lo estocástico. La incertidumbre se introduce en el Curso 1 mediante variabilidad empírica, se formaliza en el Curso 3 con probabilidad e inferencia, se gestiona en el Curso 4 mediante probabilidades calibradas de predicción, se optimiza en el Curso 5 mediante programación estocástica y simulación Monte Carlo, y se monitorea en los Cursos 6 y 7 ante la incertidumbre del cambio ambiental (*concept drift*).

4. **Experimentación metódica y validación empírica:**
   - Todo avance analítico debe someterse a prueba. Se cultiva desde la validación de hipótesis descriptivas (Curso 1), pruebas de carga de datos (Curso 2), pruebas A/B y contrastes causales (Curso 3), validación cruzada fuera de muestra (Curso 4), simulación de escenarios extremos (Curso 5), pruebas canarias y despliegues en sombra (Curso 6), hasta pruebas de usabilidad y pilotos de campo con usuarios reales (Curso 7).

5. **Comunicación y narrativa con datos (*Data Storytelling*):**
   - La evidencia analítica debe ser comprendida para tener impacto. Se desarrolla desde los gráficos descriptivos iniciales (Curso 1), documentación de arquitecturas de datos (Curso 2), comunicación de márgenes de error e intervalos de confianza a no expertos (Curso 3), explicación de factores de influencia en modelos complejos (Curso 4), visualización de fronteras de compromiso de Pareto (Curso 5), informes de monitoreo operativo (Curso 6), hasta la defensa ejecutiva de casos de negocio y diseño de interfaces interactivas (Curso 7).

6. **Ética, equidad y mitigación de sesgos algorítmicos (*Responsible AI*):**
   - La ética no puede ser un apéndice teórico final. Se evalúa en la recolección y sesgo de representación de los datos (Curso 1), en el acceso y custodia de la información (Curso 2), en la asignación justa de tratamientos experimentales (Curso 3), en la auditoría matemática de impacto dispar y paridad predictiva (Curso 4), en la equidad distributiva de recursos en modelos de optimización (Curso 5), en la equidad en producción (Curso 6) y en la gobernanza y rendición de cuentas institucional del producto (Curso 7).

7. **Privacidad y seguridad de los datos:**
   - La protección del dato sensible permea la cadena: anonimización básica y manejo ético (Curso 1), control de accesos basado en roles, cifrado en reposo y en tránsito (Curso 2), privacidad diferencial en consultas agregadas (Curso 3), técnicas de aprendizaje federado o privacidad en representaciones latentes (Curso 4), seguridad en APIs y prevención de ataques de inversión de modelos (Curso 6), y gobernanza corporativa de privacidad (Curso 7).

8. **Gobernanza, procedencia y linaje de datos:**
   - Saber de dónde proviene cada dato, cómo fue transformado y qué modelo lo utilizó. Se rastrea desde la documentación del origen del dato (Curso 1), catálogos de metadatos y trazabilidad de transformaciones ETL (Curso 2), supuestos de validez ecológica (Curso 3), registros de datos de entrenamiento vs. inferencia (Curso 4 y 6), hasta la auditoría regulatoria integral del producto analítico (Curso 7).

9. **Buenas prácticas de ingeniería de software:**
   - Escribir código legible, modular, eficiente y testeable. Evoluciona desde scripts limpios en Python (Curso 1), desarrollo de paquetes y código SQL optimizado (Curso 2), funciones inferenciales vectorizadas (Curso 3), tuberías de modelado modular (*pipelines* de Scikit-Learn) (Curso 4), integración con solvers comerciales y abiertos (Curso 5), hasta desarrollo profesional guiado por pruebas, integración continua y contenedores (Curso 6 y 7).

10. **Juicio directivo y enfoque centrado en la decisión humana:**
    - Recordar permanentemente que la analítica es un medio para mejorar las decisiones humanas y organizacionales, no un fin en sí misma. Esta actitud crítica se cultiva a lo largo de toda la cadena formativa para inmunizar al estudiante contra la fascinación tecnológica desmedida.

---

# 7. Mapa de contenidos

La siguiente matriz curricular define la distribución y profundidad de cada competencia/tema a lo largo de los siete cursos propuestos. 
Convención utilizada:
- **I** = *Introducido* (Se presentan los conceptos teóricos fundamentales y aplicaciones guiadas).
- **D** = *Desarrollado* (Se profundiza en el dominio formal, matemático, técnico y metodológico autónomo).
- **M** = *Dominado / Integrado* (Se aplica a nivel profesional en problemas complejos, integrándose con el resto del ecosistema).
- **—** = *No es un foco del curso*.

| Competencia / Tema Curricular | Curso 1: Formulación, Exploración y Evidencia | Curso 2: Ingeniería de Datos Escalable | Curso 3: Inferencia, Incertidumbre y Causalidad | Curso 4: Modelado Predictivo y Machine Learning | Curso 5: Analítica Prescriptiva y Decisiones | Curso 6: Operacionalización y MLOps | Curso 7: Productos de Datos y Estrategia |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Enmarcamiento de problemas de decisión (INFORMS I-II)** | **D** | — | I | I | D | I | **M** |
| **Construcción de casos de negocio y cálculo de ROI** | I | — | — | — | I | I | **M** |
| **Data Acumen (Procedencia, sesgo, sentido crítico)** | **D** | D | D | D | D | D | **M** |
| **Bases de datos relacionales y consultas SQL avanzadas** | I | **M** | I | — | — | D | — |
| **Bases de datos NoSQL y almacenes columnares (Parquet)** | — | **M** | — | I | — | D | — |
| **Canalizaciones ETL/ELT y orquestación (DAGs/Airflow)** | I | **M** | — | — | — | D | — |
| **Captura de cambios (CDC) y Streaming (Kafka)** | — | **M** | — | — | — | D | — |
| **Procesamiento distribuido masivo (Spark/Dask)** | — | **M** | — | D | — | D | — |
| **Análisis exploratorio de datos (EDA) y calidad** | **M** | D | D | D | — | — | — |
| **Percepción gráfica, visualización y storytelling** | **M** | — | I | D | D | I | **M** |
| **Teoría de probabilidad y modelado de incertidumbre** | I | — | **M** | D | D | — | — |
| **Pruebas de hipótesis, remuestreo y control FDR** | I | — | **M** | D | — | — | — |
| **Inferencia Bayesiana y modelos jerárquicos** | — | — | **D** | I | I | — | — |
| **Diseño experimental y pruebas A/B** | I | — | **M** | D | I | D | D |
| **Inferencia causal y modelos estructurales (DAGs)** | — | — | **M** | I | D | — | D |
| **Métodos cuasiexperimentales (IV, Matching, DiD)** | — | — | **M** | — | I | — | D |
| **Modelos lineales generalizados (GLM)** | I | — | D | **M** | — | — | — |
| **Regularización ($L_1, L_2$) y compromiso sesgo-varianza**| — | — | I | **M** | — | — | — |
| **Árboles y ensambles (Random Forest, Gradient Boosting)**| — | — | — | **M** | — | D | — |
| **Redes neuronales profundas (Deep Learning básico)** | — | — | — | **D** | — | D | — |
| **Evaluación basada en costos y curvas ROC/PR** | I | — | D | **M** | I | D | — |
| **Explicabilidad algorítmica (SHAP, LIME)** | — | — | — | **M** | — | D | D |
| **Programación matemática (Lineal, Entera, No Lineal)**| — | — | — | — | **M** | I | — |
| **Teoría de utilidad multiatributo (MAUT) y Trade Studies**| — | — | — | — | **M** | — | D |
| **Exploración de espacios de diseño y frentes de Pareto**| — | — | — | — | **M** | — | D |
| **Simulación estocástica y métodos Monte Carlo** | — | — | D | I | **M** | — | — |
| **Decisiones secuenciales (Bandidos y Reinforcement L.)**| — | — | I | — | **D** | — | — |
| **Ingeniería de software, testing y modularización** | I | D | I | D | D | **M** | D |
| **Contenedores (Docker) y microservicios** | — | D | — | — | — | **M** | D |
| **APIs para analítica (FastAPI, gRPC, batch/stream)** | — | I | — | — | — | **M** | D |
| **CI/CD/CT y registros de modelos (MLOps)** | — | I | — | — | — | **M** | D |
| **Monitoreo de deriva (Data Drift & Concept Drift)** | — | — | I | I | — | **M** | D |
| **Diseño de productos analíticos y prototipado rápido**| I | — | — | — | — | I | **M** |
| **HCI para analítica y colaboración humano-IA** | I | — | — | — | — | — | **M** |
| **Plataformas digitales y efectos de red en datos** | — | — | — | — | — | — | **M** |
| **Gobernanza corporativa, auditoría y adopción cultural**| I | I | — | — | I | I | **M** |
| **Ética, equidad algorítmica y privacidad diferencial** | I | D | D | D | D | D | **M** |

---

# 8. Qué queda deliberadamente fuera

Un currículo riguroso se define tanto por lo que incluye como por lo que excluye con deliberación. Para preservar la profundidad conceptual y la identidad disciplinar de la Analítica, se han dejado fuera del núcleo formativo obligatorio las siguientes áreas:

1. **Administración profunda de infraestructura de TI y redes de bajo nivel (*Sysadmin & Networking*):**
   - *Razón de exclusión:* La configuración de hardware de servidores, conmutadores de red, topologías de cables de fibra o administración de sistemas operativos a nivel de kernel pertenece a la ingeniería de sistemas tradicional y a la administración de tecnologías de la información. El analista e ingeniero de datos opera en la capa de software, abstracción en la nube y contenedores; incluir administración de redes desviaría horas formativas vitales.

2. **Desarrollo algorítmico de bajo nivel de librerías de Machine Learning desde cero (*Kernel Programming* en C++/CUDA):**
   - *Razón de exclusión:* Escribir kernels optimizados para GPUs o implementar librerías matriciales desde cero en C/C++ corresponde a la ingeniería de compiladores y al cómputo de alto rendimiento (*HPC*). La Analítica se enfoca en comprender matemáticamente los algoritmos, sus supuestos, sus limitaciones y su aplicación óptima a decisiones, no en escribir motores numéricos de bajo nivel.

3. **Modelado continuo de física matemática compleja y ecuaciones diferenciales para sistemas continuos físicos (CFD, dinámica de estructuras):**
   - *Razón de exclusión:* Aunque el documento *mit-machine-learning-modeling-and-simulation-principles.pdf* cubre ecuaciones diferenciales ordinarias y parciales (ODEs/PDEs) para modelado en ingeniería mecánica y química, estas aplicaciones pertenecen al dominio de las ciencias físicas y la ingeniería computacional especializada. En la Analítica general, se retienen de esa fuente los métodos estocásticos, la simulación Monte Carlo, el análisis de sensibilidad y la transición de optimización numérica a machine learning, excluyendo las PDEs de dinámica de fluidos continuos.

4. **Investigación de Operaciones puramente teórica y demostrativa (Teoría profunda de politopos y algoritmos de corte abstractos):**
   - *Razón de exclusión:* La teoría abstracta de optimización matemática avanzada (demostraciones matemáticas formales de convergencia de métodos de puntos interiores, lemas de dualidad pura) se excluye en favor de la formulación aplicada, la modelación de restricciones de negocio, los estudios de compensación multiatributo (MAUT) y la resolución computacional con solvers modernos.

5. **Desarrollo web frontend general de propósito múltiple (*Full-Stack Web Development* en React/Angular):**
   - *Razón de exclusión:* Construir sitios web comerciales completos o aplicaciones móviles generales es competencia del desarrollo de software web. En el currículo se incluye exclusivamente el diseño de interfaces centradas en la analítica, tableros analíticos interactivos, visualización de datos y consumo de APIs de modelos, sin abarcar ingeniería frontend general.

6. **Gestión empresarial y gobierno corporativo general sin base analítica:**
   - *Razón de exclusión:* La administración general de empresas, contabilidad financiera tradicional o derecho mercantil se excluyen. Solo se retienen aquellos aspectos de gestión que inciden directamente en el éxito de la analítica: enmarcamiento de problemas de decisión, formulación del caso de negocio analítico, diseño de productos de datos, gestión del cambio orientada a datos y gobernanza ética de IA.

---

# 9. Evidencia documental

A continuación se detalla la evidencia documental directa tomada exclusivamente de los veintiún archivos del corpus `./curriculum/` que sustentó el diseño de cada uno de los cursos propuestos:

### Curso 1: Formulación de Problemas, Exploración de Datos y Comunicación de Evidencia
- **`informs-analytics-framework-2024.pdf`:** Fundamenta de forma directa los Dominios I (*Business Problem Framing*) y II (*Analytics Problem Framing*), estableciendo que la práctica analítica comienza con la clarificación del problema de decisión y la alineación con las partes interesadas antes de tocar cualquier algoritmo.
- **`informs-cap-essentials-blueprint.pdf` y `informs-cap-pro-blueprint.pdf`:** Aportan el desglose de tareas profesionales para la reformulación de preguntas de negocio en preguntas analíticas (Tareas 1.1 a 1.6 y 2.1 a 2.5), así como las tareas de exploración inicial de datos (Dominio III).
- **`national-academies-data-science-for-undergraduates-2018.pdf`:** Proporciona el concepto rector de **Perspicacia con los Datos** (*Data Acumen*), enfatizando la necesidad de que los estudiantes experimenten el ciclo de vida completo de los datos desde el inicio, entendiendo la procedencia de los datos, la limpieza profunda y la exploración crítica.
- **`acm-computing-competencies-undergraduate-data-science-2021.pdf`:** Fundamenta el área de *Analysis and Presentation (AP)*: consideraciones fundacionales, visualización, diseño centrado en el usuario y comunicación efectiva de la evidencia.
- **`warwick-foundations-of-data-analytics.pdf`:** Aporta la estructura pedagógica de ir *"from raw data to deeper understanding"*, cubriendo tipos de datos, limpieza, resúmenes estadísticos e interpretación.
- **`usc-introduction-to-data-analytics.pdf`:** Evidencia la efectividad de integrar desde el primer curso la preparación de datos con Python/Pandas, consultas básicas en bases de datos y la visualización orientada a la toma de decisiones.
- **`cambridge-business-analytics.pdf`:** Aporta el marco de pensamiento analítico para ejecutivos y la traducción de problemas organizacionales en análisis descriptivos y visualización con impacto.

### Curso 2: Ingeniería de Datos y Sistemas Escalables
- **`berkeley-data-c101-data-engineering.txt`:** Constituye el referente académico central para concebir la ingeniería de datos como la disciplina de gestionar datos a escala a lo largo de todo el ciclo de vida de la ciencia de datos (preparación, almacenamiento, orquestación y operacionalización confiable).
- **`mit-professional-certificate-data-engineering.pdf`:** Aporta la columna vertebral técnica del curso: modelado de bases de datos relacionales y no relacionales, contenerización con Docker, captura de cambios en bases de datos (*Change Data Capture - CDC*) con Debezium, streaming con Kafka, orquestación con Airflow y procesamiento distribuido con Spark/Dask.
- **`acm-computing-competencies-undergraduate-data-science-2021.pdf`:** Fundamenta las áreas de competencia *Data Acquisition, Management, and Governance (DG)* y *Big Data Systems (BDS)* (arquitecturas de big data, almacenamiento distribuido, computación en la nube y complejidad computacional).
- **`pwc-data-and-analytics-academy.pdf`:** Influye en la inclusión de la manipulación de bases de datos relacionales y NoSQL estructuradas en función de las necesidades de modelado posterior (*Data Wrangling* corporativo).

### Curso 3: Inferencia Estadística, Incertidumbre y Causalidad
- **`berkeley-data-c102-data-inference-and-decisions.txt`:** Es el principal soporte documental para este curso. Proporciona la estructura conceptual que integra fundamentos probabilísticos, toma de decisiones frecuentista y bayesiana, pruebas de permutación, control de tasas de descubrimientos falsos (FDR), diseño experimental formal, inferencia causal y privacidad diferencial.
- **`national-academies-data-science-for-undergraduates-2018.pdf`:** Justifica la inclusión obligatoria de fundamentos matemáticos y estadísticos sólidos, el razonamiento bajo incertidumbre y la distinción entre inferencia y modelado empírico.
- **`mit-professional-certificate-data-science-and-analytics.pdf`:** Respalda el módulo específico de *"Thinking About Risk and Uncertainty Through Probability and Distributions"*, así como los módulos dedicados a *"Interpretability and Causality in Models"*.
- **`pwc-data-and-analytics-academy.pdf`:** Aporta los modelos lineales generalizados (GLM) y la matemática para modeladores como puente entre la inferencia y la predicción.

### Curso 4: Modelado Predictivo y Aprendizaje Automático
- **`mit-data-science-and-machine-learning.pdf`:** Proporciona la estructura temática de progresión en machine learning: desde regresión regularizada y clasificación hasta métodos no lineales de árboles, ensambles (*Random Forests*, *Boosting*), clustering, sistemas de recomendación y redes neuronales profundas.
- **`acm-computing-competencies-undergraduate-data-science-2021.pdf`:** Define las áreas de conocimiento *Machine Learning (ML)* y *Data Mining (DM)*: aprendizaje supervisado, no supervisado, métodos mixtos, aprendizaje profundo y evaluación rigurosa.
- **`mit-professional-certificate-data-science-and-analytics.pdf`:** Aporta la visión de evaluar los modelos predictivos considerando matrices de costos de decisión, así como el módulo explícito sobre equidad y sesgo en predicciones automatizadas (*Fairness and Bias Issues in Data-Driven Predictions*).
- **`warwick-foundations-of-data-analytics.pdf`:** Contribuye con el enfoque de aprendizaje a partir de patrones de datos para realizar predicciones confiables y evaluar el sobreajuste.

### Curso 5: Analítica Prescriptiva, Optimización y Simulación de Decisiones
- **`mit-quantitative-methods-in-systems-engineering.pdf`:** Es el documento clave que expande la prescripción más allá de la optimización matemática clásica hacia la ingeniería de decisiones: estructuración de estudios de compensación (*trade studies*), Teoría de Utilidad Multiatributo (MAUT), modelado de valor (*Value-Focused Thinking*), evaluación de espacios de diseño y exploración de fronteras de Pareto.
- **`mit-machine-learning-modeling-and-simulation-principles.pdf`:** Fundamenta la integración de la optimización numérica (gradiente descendente, Newton, mínimos cuadrados no lineales) con la simulación probabilística (métodos Monte Carlo, pronóstico probabilístico, simulación de eventos raros y análisis de sensibilidad).
- **`informs-analytics-framework-2024.pdf`:** Aporta la definición formal de los métodos prescriptivos dentro de los Dominios IV (*Methodology Selection*) y V (*Analytics/Model Development*), integrando optimización matemática y modelos de simulación de decisiones operacionales.
- **`cambridge-business-analytics.pdf`:** Respalda el enfoque de analítica prescriptiva orientada a la toma de decisiones empresariales estratégicas bajo restricciones operativas.
- **`berkeley-data-c102-data-inference-and-decisions.txt`:** Conecta la prescripción con decisiones secuenciales bajo incertidumbre, bandidos multibrazo (*Thompson sampling*), control óptimo y fundamentos de aprendizaje por refuerzo (*Q-learning*).

### Curso 6: Operacionalización, MLOps y Ciclo de Vida de Soluciones Analíticas
- **`informs-analytics-framework-2024.pdf`:** Define con precisión los Dominios VI (*Deployment*) y VII (*Analytics Solution Lifecycle Management*), estableciendo que la entrega de una solución analítica requiere validación de negocio, integración en sistemas existentes, monitoreo de desempeño, reentrenamiento ante degradación y protocolos de retiro.
- **`informs-cap-pro-blueprint.pdf`:** Detalla las tareas profesionales críticas de validación en producción (Tareas 6.1 a 6.4) y seguimiento continuo del ciclo de vida, rastreo de variables predictoras y re-calibración de modelos (Tareas 7.1 a 7.5).
- **`mit-cloud-and-devops.pdf`:** Proporciona los patrones arquitectónicos de computación en la nube, microservicios, integración continua y despliegue continuo (CI/CD), contenerización, observabilidad y resiliencia en entornos de producción.
- **`berkeley-data-c101-data-engineering.txt`:** Respalda el mandato formativo de asegurar la *"reliable, scalable operationalization"* de canalizaciones y modelos de machine learning.
- **`acm-computing-competencies-undergraduate-data-science-2021.pdf`:** Fundamenta las áreas de *Software Development and Maintenance (SDM)* y *Data Privacy, Security, Integrity, and Analysis for Security (DPSIA)* aplicadas a la operación de sistemas analíticos.

### Curso 7: Productos de Datos, Interacción Humano-IA y Transformación Organizacional
- **`mit-designing-and-building-ai-products-and-services.pdf`:** Es el pilar documental para la concepción de la analítica como producto: proceso de diseño de IA, diseño de máquinas inteligentes para resolver problemas de usuarios, Interacción Humano-Computadora (HCI para IA), diseño organizacional integrador (*superminds*) y fronteras de mercado de productos inteligentes.
- **`mit-digital-platforms.pdf`:** Aporta los conceptos de arquitectura de plataformas digitales, mercados de dos lados, APIs como productos, gobernanza de ecosistemas y hojas de ruta de funcionalidades (*feature roadmaps*).
- **`mit-data-leadership.pdf`:** Fundamenta las competencias de liderazgo de datos: transformación de operaciones corporativas, mentalidad para apalancar datos/IA, estrategia organizacional, cultura analítica y gestión del cambio.
- **`mit-rapid-prototyping-methodologies.pdf`:** Aporta las metodologías de diseño iterativo, prototipado rápido digital, pruebas con usuarios y desarrollo de productos mínimos viables (MVP) para validar soluciones antes de su escalamiento masivo.
- **`pwc-data-and-analytics-academy.pdf`:** Refuerza la perspectiva de que la analítica requiere juicio directivo, incentivos organizacionales y alineación con los procesos de negocio.
- **`national-academies-data-science-for-undergraduates-2018.pdf`:** Sustenta el código ético integrador, la responsabilidad social del científico de datos y el juramento profesional (*Data Science Oath*).

---

# 10. Riesgos y decisiones discutibles

Un diseño curricular transparente debe explicitar sus propias áreas de debate interno y reconocer las alternativas viables que otros diseñadores podrían defender:

### Disputa 1: ¿Separar Inferencia Causal y Estadística del Modelado Predictivo, o fusionarlos en una sola materia extensa de "Modelado"?
- **La decisión tomada:** Se separaron formalmente en dos cursos consecutivos: *Curso 3: Inferencia Estadística, Incertidumbre y Causalidad* y *Curso 4: Modelado Predictivo y Aprendizaje Automático*.
- **Riesgo identificado:** Posible fragmentación metodológica. Los estudiantes podrían percibir inicialmente que la regresión del Curso 3 es redundante con la regresión del Curso 4 si no se enfatiza con claridad el contraste entre estimación de parámetros causales/estructurales y minimización del riesgo empírico predictivo.
- **La alternativa más fuerte:** Unificar ambos cursos en una secuencia de dos partes de "Ciencia de Datos y Modelado", donde cada familia de algoritmos se estudie simultáneamente desde su perspectiva inferencial y predictiva.
- **Por qué se prefirió la decisión actual:** El corpus (particularmente Berkeley DATA C102 y MIT DSA) demuestra que cuando la predicción y la inferencia se mezclan en una sola asignatura, la inferencia estadística, el control de errores falsos y la causalidad suelen ser avasallados por la emoción superficial de entrenar modelos de machine learning con alto $R^2$, perpetuando el grave defecto profesional de confundir correlación con causa. Separarlos salvaguarda la madurez epistemológica del estudiante.

### Disputa 2: ¿Ubicar la Ingeniería de Datos al principio de la cadena formativa o colocarla más adelante como una especialización técnica de producción?
- **La decisión tomada:** Se ubicó el *Curso 2: Ingeniería de Datos y Sistemas Escalables* en una posición temprana (segundo curso), inmediatamente después de los fundamentos exploratorios.
- **Riesgo identificado:** Curva de aprendizaje técnica empinada. Los estudiantes deben dominar SQL avanzado, Docker, Airflow y conceptos de streaming antes de haber entrenado modelos complejos de machine learning o algoritmos prescriptivos.
- **La alternativa más fuerte:** Colocar la Ingeniería de Datos después del Machine Learning y la Prescripción, como un curso avanzado de "Sistemas de Big Data y Datos Masivos".
- **Por qué se prefirió la decisión actual:** El informe de las *National Academies (2018)* y *Berkeley DATA C101* enfatizan que construir modelos predictivos sobre datos de juguete en memoria desacostumbra al estudiante a la realidad de los datos a escala. Colocar la ingeniería de datos temprano garantiza que cuando los estudiantes aborden inferencia, machine learning y optimización en los cursos 3, 4 y 5, lo hagan sobre canalizaciones robustas y comprendiendo la estructura de almacenamiento y escala de los datos que alimentan sus modelos.

### Disputa 3: ¿Dedicar un curso completo autónomo a la Analítica Prescriptiva y Optimización, o integrarla como módulos finales de cursos predictivos?
- **La decisión tomada:** Se estableció un curso independiente y de peso completo (*Curso 5: Analítica Prescriptiva, Optimización y Simulación de Decisiones*).
- **Riesgo identificado:** Exigencia de un perfil docente altamente multidisciplinario, capaz de enseñar programación matemática, teoría de utilidad multiatributo de ingeniería de sistemas y simulación estocástica en un mismo semestre.
- **La alternativa más fuerte:** Incluir optimización básica al final del curso de machine learning (aprovechando el uso de gradiente descendente) y dejar la prescripción avanzada como materia electiva.
- **Por qué se prefirió la decisión actual:** El mandato explícito del marco de INFORMS y del MIT evidencia que la Analítica no termina en la predicción. Diluir la prescripción dentro del machine learning reduce la analítica a la pasividad predictiva y priva al estudiante de las herramientas que realmente cierran el ciclo de decisión: programación lineal/entera, análisis de compensaciones de Pareto y simulación estocástica.

### Disputa 4: ¿Un curso final centrado en Productos de Datos, Plataformas y Liderazgo, o un Capstone de desarrollo técnico tradicional?
- **La decisión tomada:** El *Curso 7* no es un simple taller de programación de proyecto final desasistido; es un curso estructurado en diseño de productos de IA, interfaces humano-computadora (HCI), plataformas de datos y liderazgo organizacional, articulado alrededor de un proyecto integrador.
- **Riesgo identificado:** Que perfiles con vocación puramente algorítmica consideren los temas de adopción organizacional, plataformas de dos lados y diseño de producto como "blandos" o secundarios frente a la optimización matemática.
- **La alternativa más fuerte:** Sustituir el Curso 7 por un curso puramente técnico de "Aprendizaje Profundo Avanzado e IA Generativa" o un Capstone puramente técnico de software.
- **Por qué se prefirió la decisión actual:** Los documentos del MIT (*Designing and Building AI Products*, *Digital Platforms*, *Data Leadership*) y Cambridge demuestran de forma incontestable que la mayor causa de fracaso de proyectos analíticos en la sociedad no es la falta de precisión algorítmica, sino la incapacidad de empaquetar la analítica en un producto utilizable, la falta de alineación con el modelo de negocio y el rechazo cultural de los usuarios. Omitir estas competencias mutilaría la formación del profesional de analítica.

---

# 11. Arquitectura final resumida

La arquitectura curricular propuesta se resume en una estructura secuencial con ramificaciones de interdependencia lógica y metodológica clara:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CURSO 1: Formulación de Problemas, Exploración de Datos y Comunicación     │
│          de Evidencia                                                       │
│ (Enmarcamiento INFORMS I-II, Data Acumen, EDA, Visualización, Ética)       │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
┌──────────────────────────────────────┐┌─────────────────────────────────────┐
│ CURSO 2: Ingeniería de Datos         ││ CURSO 3: Inferencia Estadística,     │
│          y Sistemas Escalables       ││          Incertidumbre y Causalidad │
│ (SQL/NoSQL, ETL/ELT, Streaming,      ││ (Probabilidad, A/B Testing, FDR,    │
│  Orquestación, Docker, Spark/Dask)   ││  Inferencia Causal, DAGs, Bayes)    │
└──────────────────┬───────────────────┘└──────────────────┬──────────────────┘
                   │                                       │
                   └───────────────────┬───────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ CURSO 4: Modelado Predictivo y Aprendizaje Automático                        │
│ (GLM, Regularización, Ensamble Trees, Deep Learning, Curvas de Costo, SHAP) │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
┌──────────────────────────────────────┐┌─────────────────────────────────────┐
│ CURSO 5: Analítica Prescriptiva,     ││ CURSO 6: Operacionalización,        │
│          Optimización y Decisiones   ││          MLOps y Ciclo de Vida      │
│ (LP/MIP/NLP, MAUT, Trade Studies,    ││ (APIs, Microservicios, CI/CD/CT,    │
│  Frentes de Pareto, Monte Carlo)     ││  Model Registry, Drift Monitoring)  │
└──────────────────┬───────────────────┘└──────────────────┬──────────────────┘
                   │                                       │
                   └───────────────────┬───────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ CURSO 7: Productos de Datos, Interacción Humano-IA y Estrategia              │
│ (Diseño de Productos IA, HCI, Plataformas Digitales, Adopción, Capstone)    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Relaciones de Precedencia y Dependencia de la Cadena:

1. **Curso 1 $\rightarrow$ Curso 2 y Curso 3:**
   - El Curso 1 es el punto de entrada obligatorio. Entrega la comprensión del problema y los datos limpios necesarios para aprender a construirlos a gran escala (Curso 2) y para someterlos a pruebas inferenciales rigurosas (Curso 3).
2. **Curso 2 y Curso 3 $\rightarrow$ Curso 4:**
   - El modelado predictivo de machine learning requiere la confluencia indispensable de dos corrientes: canalizaciones de datos escalables y reproducibles (Curso 2) y protocolos de validación experimental, tratamiento de la incertidumbre y distinción causal (Curso 3).
3. **Curso 4 $\rightarrow$ Curso 5 y Curso 6:**
   - Los modelos predictivos proporcionan los parámetros probabilísticos futuros que alimentan la optimización y simulación prescriptiva (Curso 5). Al mismo tiempo, constituyen los artefactos algorítmicos que deben empaquetarse, desplegarse y monitorearse en producción mediante MLOps (Curso 6).
4. **Curso 3 $\rightarrow$ Curso 5:**
   - La teoría de utilidad multiatributo, la toma de decisiones secuenciales bajo riesgo y el modelado estocástico del Curso 5 se fundamentan en las distribuciones de probabilidad y los supuestos causales del Curso 3.
5. **Curso 2 $\rightarrow$ Curso 6:**
   - La infraestructura de contenedores (Docker) y pipelines de datos del Curso 2 sirve de base técnica para las canalizaciones avanzadas de integración, despliegue y entrenamiento continuo de MLOps del Curso 6.
6. **Curso 5 y Curso 6 $\rightarrow$ Curso 7:**
   - El curso integrador culminante toma las políticas prescriptivas óptimas (Curso 5) operando en sistemas en producción robustos (Curso 6) para transformarlas en productos analíticos interactivos, plataformas de valor y procesos de transformación organizacional sostenible y ética.

Esta arquitectura representa de manera íntegra, no redundante y rigurosa la Analítica como una disciplina académica sólida y una práctica profesional de alto impacto en el mundo contemporáneo.
