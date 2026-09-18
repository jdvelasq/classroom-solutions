# 1. Lectura global del corpus

El corpus actualmente disponible en `./curriculum/` contiene 31 documentos. Veintiuno de ellos ya habían sido objeto de un análisis previo (marcos de sociedades profesionales —ACM, INFORMS—, un informe de política académica —National Academies—, registros de catálogo de Berkeley, un módulo de posgrado de Warwick, y una familia de programas profesionales de MIT, Cambridge Judge, PwC y USC). Los diez restantes son una serie coherente de diapositivas en español, numeradas `dataops-01` a `dataops-10`, que documentan de manera sistemática **una disciplina que los 21 documentos anteriores apenas mencionaban de forma tangencial: DataOps**, entendida como la aplicación de Lean Thinking, Agile y DevOps al ciclo de vida completo de las soluciones analíticas.

La incorporación de estos diez documentos no es un simple añadido temático: cambia el centro de gravedad del corpus. Antes, la "operacionalización" de una solución analítica estaba evidenciada casi únicamente por los Dominios VI-VII del marco INFORMS y por un curso de MIT sobre nube y DevOps orientado a la infraestructura. Ahora, casi un tercio del corpus completo (10 de 31 documentos) está dedicado, con notable rigor histórico y conceptual, a explicar *por qué* los proyectos de analítica fallan en la práctica organizacional (desperdicio de trabajo, falta de pruebas automatizadas, silos funcionales, heroísmo y miedo operacional, metodologías rígidas tipo ycascada) y *cómo* una disciplina de ingeniería y gestión —no solo un conjunto de algoritmos— resuelve ese problema.

De la lectura conjunta de los 31 documentos emerge una concepción de Analítica organizada en **cuatro capas irreducibles entre sí, más una capa transversal de responsabilidad**:

1. **Analítica como razonamiento estadístico y de aprendizaje bajo incertidumbre** (Berkeley C102, Warwick, MIT IDSS, National Academies): la actividad intelectual de inferir, predecir y distinguir causalidad de correlación.
2. **Analítica como ingeniería de sistemas de datos** (Berkeley C101, ACM-BDS/CCF/SDM, MIT Data Engineering, y ahora también `dataops-08`): la construcción de arquitecturas de datos confiables y escalables.
3. **Analítica como disciplina de decisión y estrategia organizacional** (INFORMS Analytics Framework y sus dos blueprints CAP, Cambridge, PwC, y ahora de forma mucho más desarrollada `dataops-02`): el encuadre de problemas de negocio, la construcción de un caso de valor, y la gestión de un portafolio de iniciativas.
4. **Analítica como disciplina de entrega e ingeniería organizacional ágil (DataOps)** (evidenciada casi en su totalidad por `dataops-01, 03, 04, 05, 06, 07, 09, 10`, con apoyo técnico de MIT Cloud & DevOps): la aplicación sistemática de Lean, Agile y DevOps para que la analítica se produzca, se pruebe, se despliegue y se mantenga de forma rápida, confiable y sin heroísmo, junto con el diseño organizacional de los equipos que la producen.

La capa transversal de responsabilidad (ética, privacidad, gobernanza, sesgo algorítmico) atraviesa las cuatro anteriores y ahora tiene un anclaje adicional muy concreto: `dataops-02` incluye un modelo explícito de gobierno de datos (derechos de decisión centralizados/federados/descentralizados) y una sección de "uso responsable de los datos" (privacidad, seguridad, equidad, transparencia, rendición de cuentas, cumplimiento) que complementa —sin duplicar— el tratamiento ya evidenciado por National Academies, ACM y Berkeley C102.

El hallazgo más importante para el diseño curricular es que el propio corpus de DataOps narra su origen histórico: el problema (adopción fallida de analítica, `dataops-01`) se resuelve mediante una **evolución documentada de metodologías** —KDD (1989) → CRISP-DM (1996) → SEMMA → marco de procesos de INFORMS (2014) → ASUM-DM → TDSP → CRISP-ML(Q) → híbridos ágiles de CRISP-DM → DataOps (`dataops-03`)— que converge, de forma casi exacta, con los siete dominios del propio marco INFORMS ya presente en el corpus original. Esta convergencia entre dos linajes documentales independientes (el linaje académico/profesional de INFORMS y el linaje de ingeniería de datos de DataOps) es la evidencia más fuerte de todo el corpus para sostener que **el ciclo completo de vida analítico —encuadre, datos, método, modelo, entrega, mantenimiento, gobernanza— es la estructura organizadora natural de todo el currículo**, y no una fase aislada al final.

En consecuencia, este diseño trata la concepción de Analítica como **una disciplina de ciclo completo para la toma de decisiones basada en evidencia, que se produce y se entrega mediante prácticas de ingeniería ágil y organizacional deliberadas**, no simplemente como una secuencia de técnicas estadísticas seguida de un despliegue técnico incidental.

# 2. Competencias que debe desarrollar la cadena completa

**A. Formulación y encuadre de problemas analíticos.** Traducir una pregunta de negocio en una pregunta analítica bien definida; distinguir cuándo un problema es "amenable" al análisis de datos; reconocer los mitos y fallas típicas de adopción de la analítica (`dataops-01`) antes de comenzar cualquier proyecto.

**B. Estrategia y gestión de portafolio de datos.** Diagnosticar capacidades de datos existentes, identificar mecanismos de creación de valor (mejorar procesos, enriquecer productos, ofrecer información), formular objetivos estratégicos de datos, diseñar iniciativas, construir y evaluar un caso de valor, priorizar un portafolio, y trazar una hoja de ruta por horizontes —una competencia de nivel organizacional, no de proyecto individual (`dataops-02`).

**C. Adquisición, gestión, gobernanza y calidad de datos.** Identificar y priorizar necesidades de datos; diseñar arquitecturas (lagos, bodegas, mercados de datos); limpiar, transformar y validar; documentar linaje; aplicar principios de gobernanza operativa (propiedad, custodia, calidad).

**D. Análisis descriptivo y comunicación de evidencia.** Exploración rigurosa de datos (EDA), visualización apropiada, construcción de tableros e informes, narrativa de evidencia para audiencias técnicas y no técnicas.

**E. Razonamiento estadístico y cuantificación de la incertidumbre.** Probabilidad, estimación, pruebas de hipótesis, diseño experimental, razonamiento frecuentista y bayesiano.

**F. Modelado predictivo y aprendizaje automático.** Construcción, evaluación, calibración y validación de modelos supervisados y no supervisados, desde regresión hasta aprendizaje profundo.

**G. Distinción entre predicción, inferencia estadística, causalidad y decisión.** Reconocer los límites de un modelo predictivo para sostener una afirmación causal; diseñar y evaluar experimentos y estudios observacionales con variables de confusión.

**H. Analítica prescriptiva: optimización, simulación y decisión bajo incertidumbre.** Modelado de decisiones mediante optimización, simulación y análisis de valor/tradespace, incorporando restricciones, riesgo y sesgos de comportamiento.

**I. Ingeniería ágil y lean de la entrega analítica (DataOps).** Aplicar principios Lean (eliminación de desperdicio, mapeo de flujo de valor, teoría de restricciones, análisis de causa raíz) y Agile (Scrum, Kanban, el Manifiesto DataOps) al ciclo de vida de un producto analítico; diseñar pruebas automatizadas de datos, lógica y modelos; usar control de versiones, ambientes múltiples, contenerización y parametrización; operar bajo un modelo de MLOps sin heroísmo ni miedo operacional.

**J. Diseño y organización de equipos y liderazgo de datos.** Elegir arquetipos de equipo (funcional vs. orientado a dominio), definir roles y habilidades (ingeniero de datos, científico de datos, ingeniero DataOps), reconocer las trampas típicas de un líder de datos (defensa de datos, valor diferido, valoración de datos) y los niveles de madurez organizacional de la analítica.

**K. Despliegue, operacionalización y gestión del ciclo de vida.** Validar una solución con el negocio antes de desplegarla, definir requisitos de producción, monitorear el desempeño, recalibrar modelos, mantener la trazabilidad del caso de negocio en el tiempo.

**L. Diseño de productos y sistemas analíticos.** Diseñar la interacción humano-máquina de una solución, decidir el nivel apropiado de automatización, considerar la integración organizacional y la lógica de plataforma cuando aplique.

**M. Prácticas de trabajo reproducible.** Control de versiones, documentación de supuestos, estructuración de proyectos analíticos como software mantenible.

**N. Gobernanza, ética, privacidad, seguridad y responsabilidad en IA.** Sesgo algorítmico, privacidad (incluida la privacidad diferencial), impacto social, y los distintos niveles de gobierno de datos (institucional/de decisión, operativo/de calidad, y ético/de responsabilidad).

**O. Comunicación y gestión de patrocinadores/stakeholders.** Comunicar resultados técnicos a audiencias ejecutivas, negociar alcance y expectativas, construir confianza organizacional mediante entrega continua de valor.

# 3. Tensiones y decisiones curriculares fundamentales

**Estadística vs. aprendizaje automático.** Berkeley separa institucionalmente estas tradiciones (C101 ingeniería vs. C102 inferencia); ACM cede explícitamente el terreno estadístico a otras sociedades. Decisión: la estadística se enseña como fundamento autónomo, no como introducción al aprendizaje automático.

**Predicción vs. inferencia estadística**, **predicción vs. inferencia causal**, y **predicción vs. prescripción.** Evidenciadas de forma consistente por Berkeley C102, MIT IDSS y el certificado MIT de Ciencia de Datos y Analítica (módulo dedicado de causalidad), y por INFORMS/Cambridge en la distinción descriptivo/predictivo/prescriptivo. Cada una recibe tratamiento dedicado y no se comprime en un único curso de "modelado".

**Optimización vs. analítica de decisión más amplia.** El corpus ofrece dos miradas de lo prescriptivo (optimización matemática clásica vs. exploración de valor/tradespace bajo sesgos de comportamiento). Se integran en un único curso, dejando la profundidad matemática completa de Investigación de Operaciones como especialización electiva.

**Ciencia/ingeniería de datos vs. DataOps — la tensión más importante que añade el corpus nuevo.** Antes de incorporar los documentos DataOps, "ingeniería de datos" y "despliegue" parecían dos caras de una misma fase técnica. La lectura de `dataops-08` frente a `dataops-01,03,04,05,06,07,09,10` revela que son en realidad **dos disciplinas distintas que comparten objeto pero no método**: la ingeniería de datos responde "¿cómo construyo una arquitectura de datos correcta, escalable y gobernable?" (una pregunta de diseño técnico), mientras que DataOps responde "¿cómo organizo el trabajo, las pruebas, los ambientes y el equipo para que esa arquitectura —y los modelos que la usan— se entreguen y mantengan de forma rápida, confiable y sin heroísmo?" (una pregunta de proceso, ingeniería de software y diseño organizacional). `dataops-08` es el documento bisagra: la mitad de su contenido (arquitectura canónica vs. arquitectura DataOps, diseño de lagos/bodegas/mercados de datos, diseño de esquemas) pertenece a la primera pregunta, y la otra mitad (Design Thinking, deuda técnica de ML, plataforma DataOps) pertenece a la segunda. Decisión: se mantienen como dos cursos distintos, con esta frontera explícita (ver Sección 5).

**Metodología estructurada (cascada/CRISP-DM clásico) vs. metodología adaptativa (Ágil/DataOps).** `dataops-01` y `dataops-05` documentan explícitamente el fracaso del modelo en cascada (Royce 1970, Boehm 1980, Sommerville 1985) para proyectos analíticos —el "Big-Bang Deliverable", el valor diferido al final del proyecto, la imposibilidad de responder al cambio— y `dataops-03` narra 36 años de evolución metodológica (KDD→CRISP-DM→...→DataOps) como una respuesta progresiva a esa falla. Esta es una tensión genuinamente histórica, no solo técnica: el corpus muestra que la propia definición de "buena metodología analítica" ha cambiado con el tiempo. Decisión: el curso de Fundamentos enseña esta evolución explícitamente como contenido (no como anécdota), y el curso de DataOps enseña la resolución práctica (Agile/Lean/DevOps aplicados).

**Estrategia organizacional de datos vs. ejecución técnica de un proyecto analítico.** `dataops-02` opera en una altitud distinta (objetivos, iniciativas, portafolio, gobierno de decisión, caso de valor) que el resto del currículo técnico. Es una competencia real y bien evidenciada, pero no debe confundirse con la ejecución de un proyecto individual (que es lo que cubre el curso de Fundamentos/Metodologías y, más adelante, el Capstone). Decisión: curso propio, temprano en la secuencia.

**Valor defensivo vs. valor ofensivo de los datos.** `dataops-07` documenta explícitamente la "trampa de la defensa de los datos": las actividades de gobierno, calidad, seguridad y cumplimiento son necesarias pero producen valor solo indirecto, mientras que la innovación analítica produce valor directo — y una organización que solo hace lo primero nunca demuestra el retorno de su inversión en datos. Esta tensión, no presente en el corpus original, se enseña explícitamente en el curso de DataOps como una trampa a evitar, y se conecta con el módulo de gobernanza (Sección 6).

**Equipos funcionales centralizados vs. equipos orientados a dominio.** `dataops-10` desarrolla en detalle las ventajas y desventajas de ambos modelos de organización de equipos de datos (aprovechamiento de talento escaso vs. apropiación/velocidad/conocimiento profundo del problema). Es una decisión de diseño organizacional real que un profesional de analítica debe poder argumentar, no una verdad única.

**Análisis vs. sistemas de producción**, y **modelado vs. despliegue.** INFORMS separa el Dominio V (modelado) de los Dominios VI-VII (despliegue, ciclo de vida); ahora `dataops-06` aporta el contenido técnico concreto (pruebas, control de versiones, ambientes, contenerización, parametrización) que antes solo estaba sugerido por MIT Cloud & DevOps. Se mantiene como frontera de curso explícita.

**Análisis técnico vs. toma de decisiones organizacional.** MIT Data Leadership, Cambridge y PwC muestran una audiencia ejecutiva/consumidora de analítica separada de quien la produce. La incorporación de `dataops-07` (dirigido explícitamente al Chief Data/Analytics/Information Officer) refuerza que existe contenido de liderazgo genuino en el corpus, pero ahora anclado en la organización específica de equipos de datos (no en gestión ejecutiva genérica). Decisión: este contenido se incorpora dentro del curso de DataOps (módulo organizacional) y del curso de Estrategia, no como un curso ejecutivo aparte (ver Sección 10 para la discusión).

# 4. Arquitectura curricular propuesta

Catorce cursos en cuatro niveles. Los cursos 2 y 3 pueden cursarse en paralelo (ambos dependen solo del curso 1).

---

**Nivel I — Fundamentos y marco de referencia**

### 1. Fundamentos de Analítica: Problemas, Decisiones y Evolución de las Metodologías
- **Posición:** primer curso, sin prerrequisitos de analítica.
- **Propósito central:** instalar el mapa mental de ciclo completo de un proyecto analítico; enseñar explícitamente por qué fallan las iniciativas de analítica (mitos de adopción, brechas de conocimiento, cultura organizacional) y cómo ha evolucionado la respuesta metodológica de la disciplina, desde KDD y CRISP-DM hasta los marcos ágiles y DataOps, comparando esta evolución con el marco de los siete dominios de INFORMS; introducir la taxonología descriptivo/predictivo/prescriptivo y los sesgos de decisión.
- **Competencias principales:** A, introducción a I y a N.
- **Prerrequisitos:** ninguno.
- **Qué recibe:** nada; es la puerta de entrada.
- **Qué prepara:** el vocabulario, la historia y el marco de referencia que da sentido a todos los cursos siguientes, en particular a los cursos 2 y 11.

### 2. Estrategia de Datos y Analítica
- **Posición:** segundo curso, en paralelo con el curso 3.
- **Propósito central:** diagnosticar capacidades organizacionales de datos, identificar mecanismos de creación de valor (mejorar/enriquecer/ofrecer), formular objetivos estratégicos, diseñar iniciativas, definir un modelo de gobierno de decisión de datos (centralizado/federado/descentralizado), construir un caso de valor con manejo explícito de incertidumbre, priorizar un portafolio y trazar una hoja de ruta por horizontes.
- **Competencias principales:** B, introducción al gobierno institucional de N, O.
- **Prerrequisitos:** curso 1.
- **Qué recibe:** el vocabulario de ciclo de vida y la taxonomía descriptivo/predictivo/prescriptivo del curso 1.
- **Qué prepara:** el criterio para priorizar y justificar organizacionalmente cualquier proyecto que se construya en los cursos técnicos siguientes, y el modelo de gobierno de decisión que se retomará en el curso 13.

### 3. Programación y Manejo de Datos
- **Posición:** tercer curso, en paralelo con el curso 2.
- **Propósito central:** fluidez computacional — programación, estructuras de datos, manipulación de datos tabulares y semiestructurados, fundamentos de SQL.
- **Competencias principales:** C (parcial), M (parcial).
- **Prerrequisitos:** curso 1 (recomendado).
- **Qué recibe:** el marco conceptual del curso 1.
- **Qué prepara:** la base computacional de los cursos 4, 5 y 6.

---

**Nivel II — Núcleo técnico**

### 4. Estadística e Inferencia para la Analítica
- **Posición:** cuarto curso, en paralelo con el curso 5.
- **Propósito central:** probabilidad, estimación, pruebas de hipótesis, intervalos de confianza, razonamiento frecuentista y bayesiano, diseño experimental básico.
- **Competencias principales:** E.
- **Prerrequisitos:** curso 3.
- **Qué recibe:** capacidad de programar y manejar datos.
- **Qué prepara:** el lenguaje formal de incertidumbre para los cursos 7, 8, 9 y 10.

### 5. Analítica Descriptiva y Comunicación de Evidencia
- **Posición:** quinto curso, en paralelo con el curso 4.
- **Propósito central:** EDA, principios de visualización, tableros/informes, narrativa de datos.
- **Competencias principales:** D.
- **Prerrequisitos:** curso 3.
- **Qué recibe:** datos manejables del curso 3.
- **Qué prepara:** el hábito de examinar datos antes de modelarlos, insumo informal de los cursos 6 y 7.

### 6. Ingeniería y Arquitectura de Datos para la Analítica
- **Posición:** sexto curso.
- **Propósito central:** arquitecturas de datos relacionales y no relacionales; diseño de lagos, bodegas y mercados de datos con reglas explícitas de gobernanza (qué se ingiere, qué se transforma, cómo se alinea con el resto de la arquitectura); diseño de esquemas para consumo analítico frente a consumo transaccional; contraste entre una arquitectura canónica (optimizada para estabilidad) y una arquitectura orientada a DataOps (optimizada para cambio frecuente); calidad y linaje de datos como principio de gobernanza operativa.
- **Competencias principales:** C (completa).
- **Prerrequisitos:** cursos 3 y 5.
- **Qué recibe:** de 5, el criterio sobre qué hace útil un dato para el análisis; de 3, la base de programación.
- **Qué prepara:** datos gobernados y arquitecturas conocidas para los cursos 7 a 10, y el sustrato técnico sobre el cual el curso 11 (DataOps) aplicará sus prácticas de entrega.

### 7. Analítica Predictiva I: Aprendizaje Supervisado
- **Posición:** séptimo curso.
- **Propósito central:** regresión, clasificación, árboles, ensambles; evaluación, regularización y validación de modelos.
- **Competencias principales:** F (primera mitad).
- **Prerrequisitos:** cursos 4 y 6 (y 5).
- **Qué recibe:** el aparato de incertidumbre (curso 4) y datos gobernados (curso 6).
- **Qué prepara:** el vehículo técnico que el curso 8 usará para introducir la distinción causal.

---

**Nivel III — Razonamiento avanzado**

### 8. Inferencia Causal y Diseño de Experimentos
- **Posición:** octavo curso.
- **Propósito central:** distinguir predicción de causalidad; diseño y análisis de experimentos controlados y estudios observacionales con variables de confusión.
- **Competencias principales:** G.
- **Prerrequisitos:** curso 7.
- **Qué recibe:** el modelo de regresión del curso 7, reinterpretado bajo una pregunta distinta.
- **Qué prepara:** el criterio para no confundir ajuste predictivo con validez de una intervención, que sostiene los cursos 9 y 10.

### 9. Analítica Predictiva II: No Supervisado, Series de Tiempo y Aprendizaje Profundo
- **Posición:** noveno curso.
- **Propósito central:** clustering, reducción de dimensionalidad, sistemas de recomendación, redes y modelos gráficos, series de tiempo, fundamentos de aprendizaje profundo.
- **Competencias principales:** F (segunda mitad).
- **Prerrequisitos:** cursos 7 y 8.
- **Qué recibe:** la base supervisada y la disciplina causal.
- **Qué prepara:** modelos avanzados que alimentan las decisiones del curso 10 y los productos del curso 12.

### 10. Analítica Prescriptiva: Optimización, Simulación y Decisión bajo Incertidumbre
- **Posición:** décimo curso.
- **Propósito central:** modelado de decisiones mediante optimización, simulación (Monte Carlo, sensibilidad), análisis de valor/tradespace, sesgos de comportamiento relevantes a la decisión.
- **Competencias principales:** H.
- **Prerrequisitos:** cursos 7, 8 y 9 (y 4).
- **Qué recibe:** estimaciones predictivas y causales como insumos/restricciones del problema de decisión.
- **Qué prepara:** una solución candidata lista para ser entregada de forma confiable, insumo directo del curso 11.

---

**Nivel IV — Entrega, producto y responsabilidad**

### 11. DataOps: Ingeniería Ágil y Lean del Ciclo de Vida Analítico
- **Posición:** undécimo curso.
- **Propósito central:** aplicar Lean Thinking (eliminación de desperdicio, mapeo de flujo de valor, teoría de restricciones, análisis de causa raíz) y metodologías ágiles (Scrum, Kanban, el Manifiesto DataOps, el ciclo de vida Ideación→Incepción→I+D→Transición/Producción→Retiro) al desarrollo y operación de soluciones analíticas; implementar la hoja de ruta técnica de DataOps (pruebas de datos/lógica/modelos, control de versiones, bifurcación y fusión, ambientes múltiples, contenerización, parametrización, eliminación de heroísmo); diseñar pruebas automatizadas de calidad de datos (unitarias, de integración, funcionales, de regresión, de desempeño, de humo) y monitoreo estadístico de procesos; operar bajo un modelo de MLOps de tres fases (configuración de infraestructura, desarrollo de modelos, transición a operaciones); diseñar la organización del equipo de entrega (arquetipos de equipo, roles y habilidades, estructuras funcionales vs. de dominio) y reconocer las trampas de liderazgo de datos (defensa de datos, valor diferido, valoración de datos) y los niveles de madurez organizacional.
- **Competencias principales:** I, J, K (parcial).
- **Prerrequisitos:** cursos 6 y 10.
- **Qué recibe:** una arquitectura de datos conocida (curso 6) y una solución candidata completa —predictiva, causal y prescriptiva— (curso 10) que debe entregarse y mantenerse de forma confiable.
- **Qué prepara:** una solución en producción, monitoreada, mantenible y producida por un equipo bien organizado, que el curso 12 convertirá en producto y el curso 13 auditará bajo un lente de responsabilidad.

### 12. Productos y Sistemas Analíticos
- **Posición:** duodécimo curso.
- **Propósito central:** diseño de la interacción humano-máquina de una solución analítica; decisión del nivel apropiado de automatización frente a intervención humana; integración organizacional; nociones de plataforma/ecosistema cuando la solución conecta múltiples partes interesadas.
- **Competencias principales:** L.
- **Prerrequisitos:** curso 11.
- **Qué recibe:** una solución ya entregada, probada y monitoreada.
- **Qué prepara:** una solución adoptable, lista para ser auditada bajo gobernanza.

### 13. Gobernanza, Ética y Responsabilidad en Analítica e IA
- **Posición:** decimotercer curso.
- **Propósito central:** consolidar, a nivel de sistema completo, los tres niveles de gobierno evidenciados por el corpus —gobierno institucional/de decisión (retomando el curso 2), gobierno operativo/de calidad (retomando el curso 6), y responsabilidad ética/de privacidad/de sesgo algorítmico (evidencia central de National Academies, ACM, Berkeley C102 y Warwick)— aplicándolos a la solución completa construida en los cursos 6 a 12.
- **Competencias principales:** N.
- **Prerrequisitos:** cursos 2, 11 y 12.
- **Qué recibe:** una solución completa de principio a fin y los tres modelos de gobierno ya introducidos por separado en cursos anteriores.
- **Qué prepara:** el criterio de responsabilidad profesional exigido en el Capstone.

### 14. Capstone: Proyecto Integrador de Analítica
- **Posición:** curso final.
- **Propósito central:** ejecutar el ciclo completo (encuadre → estrategia → datos → método → modelo → entrega DataOps → producto → gobernanza) sobre un problema real, con patrocinador.
- **Competencias principales:** integración de A a O.
- **Prerrequisitos:** todos los anteriores.
- **Qué recibe:** todas las competencias previas.
- **Qué prepara:** práctica profesional o estudios de posgrado.

# 5. Fronteras entre cursos

**1 → 2.** El curso 1 diagnostica *por qué fallan* los proyectos de analítica y narra la evolución metodológica general; el curso 2 construye, a partir de ese diagnóstico, una estrategia *para una organización específica* (objetivos, iniciativas, portafolio). Un tema ambiguo —la taxonomía descriptivo/predictivo/prescriptivo— se introduce en el curso 1 como marco conceptual, y se retoma en el curso 2 únicamente como insumo para clasificar iniciativas dentro de un portafolio, no para enseñarla de nuevo.

**2 ↔ 3 (paralelos).** No comparten contenido: el curso 2 es conceptual/estratégico y no requiere programación; el curso 3 es técnico/computacional y no discute estrategia organizacional. La única superposición posible —"gobierno de datos"— se resuelve a favor del curso 2 en su dimensión de derechos de decisión institucional, dejando cualquier aspecto técnico de control de acceso o permisos de bases de datos para el curso 6.

**3 → 4 / 3 → 5.** Igual que en el diseño técnico general: limpieza/transformación mecánica de datos pertenece al curso 3; la justificación probabilística de una afirmación de incertidumbre pertenece al curso 4; la representación visual de un patrón pertenece al curso 5.

**4 ↔ 5 (paralelos).** El curso 5 puede mostrar un histograma sin justificar su base distribucional; el curso 4 exige esa justificación para cualquier afirmación de incertidumbre (intervalos, pruebas de hipótesis), que permanece exclusivamente en el curso 4 aunque se visualice en el curso 5.

**5 → 6.** El curso 5 trabaja con datos pequeños y limpios con fines de comunicación; el curso 6 comienza donde los datos son grandes, múltiples o de mala calidad y requieren una arquitectura para producirse de forma confiable y repetible. La pregunta que separa ambos cursos: el curso 5 responde "¿cómo comunico este patrón?"; el curso 6 responde "¿puedo confiar en este dato y en la arquitectura que lo produjo?".

**6 → 7.** El curso 6 entrega datos gobernados, documentados y arquitecturas conocidas (lagos/bodegas/mercados de datos); el curso 7 no repite el diseño de esa arquitectura, la asume como insumo y pregunta "¿qué puedo predecir con este dato?". Un tema explícitamente ambiguo por evidencia directa del corpus (`dataops-08` cubre tanto arquitectura como deuda técnica de modelos de ML): el diseño de esquemas y la decisión lago/bodega/mercado de datos pertenecen enteramente al curso 6; el concepto de "deuda técnica oculta en sistemas de ML" (la porción del código de modelo frente a la infraestructura circundante) se **menciona** en el curso 7 como advertencia, pero se **desarrolla** en el curso 11, porque es fundamentalmente un problema de proceso de entrega, no de arquitectura de datos.

**7 → 8.** Ambos cursos pueden usar el mismo modelo de regresión. La frontera es la pregunta, no el método: el curso 7 pregunta "¿qué tan bien predice?"; el curso 8 pregunta "¿puedo afirmar causalidad, y bajo qué condiciones?". La regularización pertenece al curso 7; el ajuste por variables de confusión pertenece al curso 8.

**8 → 9.** El curso 8 cierra con el criterio de que un patrón hallado no autoriza automáticamente una intervención; el curso 9 retoma el modelado (ahora no supervisado y profundo) sin reabrir esa pregunta, aunque la recuerda al interpretar representaciones aprendidas.

**9 → 10.** El curso 9 entrega estimaciones y representaciones; el curso 10 las toma como insumos de un problema de decisión con una función de valor explícita, que no forma parte del criterio puramente estadístico del curso 9.

**10 → 11.** Esta es la frontera más importante del rediseño. El curso 10 entrega una **recomendación de decisión** (una política, una asignación óptima); el curso 11 pregunta si esa recomendación —junto con los modelos y datos que la sustentan— puede **entregarse de forma repetible, probada y sin heroísmo, por un equipo bien organizado**. Un tema ambiguo por evidencia directa (`dataops-03` incluye tanto el diseño del proyecto como su evaluación y operación): la formulación matemática de la decisión y su evaluación de desempeño estadístico permanecen en el curso 10; la prueba automatizada de esa misma decisión en producción (pruebas de entrada, de lógica de negocio, de salida; control estadístico de proceso) pertenece enteramente al curso 11.

**11 → 12.** El curso 11 entrega un sistema desplegado, probado, monitoreado y producido por un equipo organizado; el curso 12 pregunta si ese sistema es usable, adoptado e integrado organizacionalmente. Un tema ambiguo —la plantilla de "Hipótesis de Épica" (Epic Hypothesis Statement) usada para priorizar trabajo en un tablero Kanban de DataOps— se resuelve a favor del curso 11, porque su función allí es gestionar el flujo de trabajo del equipo de entrega; el curso 12 puede retomar la misma plantilla, pero con el propósito distinto de especificar el valor y el diseño de un producto para el usuario final, no de organizar el trabajo del equipo.

**12 → 13.** El curso 12 diseña la solución completa (técnica + producto); el curso 13 la audita bajo los tres niveles de gobierno (institucional, operativo, ético). Frontera deliberadamente porosa: cuestiones de sesgo o privacidad que surgen durante el diseño de producto se señalan pero no se resuelven en profundidad hasta el curso 13.

**13 → 14.** El curso 13 entrega un criterio de responsabilidad aplicable a cualquier solución; el Capstone lo aplica en tiempo real junto con todas las demás competencias, sin contenido nuevo.

# 6. Competencias transversales

- **Comunicación y narrativa de evidencia.** Introducida en los cursos 1 y 5, exigida en cada entrega posterior (máxima intensidad: 5, 14).
- **Formulación y reformulación de problemas.** No se agota en el curso 1; se retoma explícitamente en 2 (a nivel organizacional), 10 (al definir la función de valor de una decisión) y 14.
- **Reproducibilidad y prácticas de ingeniería de software.** Introducida en el curso 3, reforzada de manera muy concreta en el curso 11 (control de versiones, ambientes, contenerización, parametrización) — a diferencia del diseño previo, ahora existe evidencia documental extensa y específica para esta práctica, no solo un principio general.
- **Cuantificación de la incertidumbre.** Exigida en los cursos 4, 8, 10 y en el reporte de cualquier modelo.
- **Experimentación y pensamiento causal.** Concentrada en el curso 8, exigida como hábito crítico en 9, 10 y 14.
- **Ética, privacidad, seguridad y responsabilidad en IA.** Introducida en el curso 1, instanciada técnicamente en 6 (gobernanza operativa), 7/9 (sesgo algorítmico en modelos), 11 (calidad y confiabilidad como responsabilidad de entrega), 12 (diseño responsable), y consolidada en el curso 13.
- **Gobierno de datos (tres niveles simultáneos, no un único concepto).** Nivel institucional/de decisión: introducido en el curso 2, retomado en el 13. Nivel operativo/de calidad: introducido en el curso 6, retomado técnicamente en el 11 (pruebas automatizadas de calidad) y consolidado en el 13. Nivel ético/de responsabilidad: consolidado en el 13. Se enfatiza como transversal precisamente porque el corpus muestra que "gobernanza" significa cosas distintas según el nivel, y un profesional debe reconocer las tres.
- **Estrategia y valor organizacional.** Introducida en el curso 2, retomada explícitamente en el curso 11 al discutir la trampa de la "defensa de datos" (valor indirecto) frente al valor directo de la innovación analítica, y en el Capstone al construir un caso de valor real ante un patrocinador.
- **Organización y liderazgo de equipos de datos.** Concentrada en el curso 11 (arquetipos de equipo, roles, habilidades, madurez organizacional), pero su lógica de "confianza mediante entrega continua de valor" se practica de forma aplicada en el Capstone.
- **Trabajo en equipos multidisciplinarios.** Implícita en todos los proyectos grupales, explícita en el curso 11 (organización de equipos) y en el Capstone (donde los roles de estrategia, ingeniería de datos, modelado, entrega DataOps y comunicación con el patrocinador deben distribuirse y coordinarse).

# 7. Mapa de contenidos

I = Introducido, D = Desarrollado, M = Dominado/Integrado, — = No es foco.

| Competencia / Tema | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Formulación de problemas de decisión | I | D | — | — | — | — | D | — | — | D | — | — | — | M |
| Historia y marcos de metodología analítica | M | D | — | — | — | — | — | — | — | — | D | — | — | D |
| Estrategia de datos: objetivos, iniciativas, portafolio, hoja de ruta | I | M | — | — | — | — | — | — | — | — | D | — | D | D |
| Gobierno de datos: modelo de decisión institucional | — | M | — | — | — | I | — | — | — | — | — | — | D | D |
| Programación y estructuras de datos | I | — | M | D | D | D | D | D | D | D | D | — | — | D |
| Bases de datos (SQL/NoSQL) | — | — | I | — | D | M | — | — | — | — | D | — | — | D |
| Arquitectura, calidad y gobernanza operativa de datos | — | — | — | — | — | M | — | — | — | — | D | — | D | D |
| Probabilidad e inferencia estadística | — | — | — | M | D | D | D | D | D | D | — | — | — | D |
| Diseño experimental (A/B, RCT) | — | — | — | D | — | — | — | M | — | — | — | — | — | D |
| Análisis exploratorio y visualización | — | — | I | D | M | D | D | — | D | D | D | D | — | D |
| Comunicación de evidencia / storytelling | I | D | — | D | M | D | D | D | D | D | D | D | D | M |
| Aprendizaje supervisado (regresión/clasificación) | — | — | I | D | — | — | M | D | D | D | — | — | — | D |
| Aprendizaje no supervisado / representación | — | — | — | — | — | — | I | — | M | D | — | D | — | D |
| Series de tiempo y aprendizaje profundo | — | — | — | — | — | — | I | — | M | D | I | I | — | D |
| Inferencia causal y variables de confusión | — | — | — | I | — | — | I | M | D | D | — | — | D | D |
| Optimización y simulación | — | — | — | I | — | — | I | — | I | M | — | — | — | D |
| Decisión bajo incertidumbre y sesgos de decisión | I | — | — | I | — | — | — | — | — | M | D | D | — | D |
| Lean thinking aplicado a analítica (desperdicio, VSM, teoría de restricciones) | I | — | — | — | — | — | — | — | — | — | M | — | — | D |
| Metodologías ágiles y manifiesto DataOps | I | — | — | — | — | — | — | — | — | — | M | D | — | D |
| Pruebas automatizadas de datos, lógica y modelos | — | — | I | — | — | I | — | — | — | — | M | — | D | D |
| Prácticas de entrega continua (versionado, ambientes, contenedores) | — | — | I | — | — | I | — | — | — | — | M | — | — | D |
| MLOps: despliegue, monitoreo y recalibración | — | — | — | — | — | I | — | — | — | I | M | D | D | D |
| Organización y liderazgo de equipos de datos | I | D | — | — | — | — | — | — | — | — | M | D | — | D |
| Diseño de producto / HCI / automatización | I | — | — | — | — | — | — | — | — | I | I | M | D | D |
| Ética, sesgo algorítmico, privacidad y responsabilidad en IA | I | I | — | — | — | I | I | D | — | — | D | D | M | D |
| Trabajo reproducible y comunicación ejecutiva (transversal) | I | D | I | D | D | D | D | D | D | D | D | D | D | M |

La progresión visible confirma tres decisiones de diseño: (a) el gobierno de datos aparece en tres filas distintas con trayectorias de maduración independientes (institucional en C2/C13, operativo en C6/C11/C13, ético en C13), evitando tratarlo como un concepto único; (b) "historia y marcos de metodología" alcanza dominio ya en el curso 1 pero se retoma deliberadamente en el 11, porque el dominio conceptual (saber que existen metodologías y por qué evolucionaron) es distinto del dominio práctico (aplicarlas); (c) casi ninguna fila tiene más de una "M", preservando la regla de que cada competencia se domina en un único lugar de la cadena, aunque se practique en varios.

# 8. Qué queda deliberadamente fuera

- **Certificación o profundidad de administración en un stack específico de herramientas DataOps/CI-CD** (Puppet, Chef, Ansible, Jenkins, Travis CI, Vault, Okta, Auth0, Airflow, Kubeflow, Grafana, evidenciados en `dataops-08`). Se enseñan como ejemplos ilustrativos de categorías (orquestación, gestión de configuración, secretos) dentro del curso 11, no como currículo de certificación en un producto.
- **Marcos comerciales de escalamiento ágil a nivel de certificación** (SAFe, evidenciado en `dataops-05`). Se estudia conceptualmente como parte de la evolución histórica de la colaboración ágil, no se enseña a profundidad de certificación.
- **Teorías completas de comportamiento organizacional o de innovación de producto** (Coordinación Relacional como cuerpo teórico completo, el algoritmo de "oportunidad" de innovación dirigida por resultados, evidenciados en `dataops-07`). Se introducen como constructos nombrados y aplicados dentro del módulo organizacional del curso 11, pero su desarrollo teórico completo pertenece a una especialización electiva en comportamiento organizacional o gestión de producto.
- **Teoría matemática completa de Investigación de Operaciones** (dualidad, teoría de colas, procesos estocásticos avanzados). Se mantiene como especialización electiva, consistente con la instrucción de no equiparar lo prescriptivo con toda la IO.
- **Administración de infraestructura en la nube a nivel de proveedor específico.** Los principios (contenerización, ambientes, orquestación) se enseñan en el curso 11; la certificación en un proveedor específico se deja como elective complementario.
- **Prototipado físico y metodologías de manufactura** (evidenciado en MIT Rapid Prototyping). Fuera del núcleo por completo — pertenece al diseño de producto físico, no a productos de datos.
- **Un curso ejecutivo de "Liderazgo de Datos" para audiencias no técnicas** (MIT Data Leadership, Cambridge, PwC Master Class). El contenido de liderazgo que sí es propio de un currículo de Analítica —organización de equipos de datos, trampas del líder de datos, madurez organizacional— ya se incorpora dentro del curso 11 con la profundidad que amerita para un practicante; un programa ejecutivo para consumidores no técnicos de analítica seguiría siendo un producto distinto.
- **Especialización vertical por dominio de aplicación** (finanzas, salud, mercadeo, manufactura). Se deja como electivas o como contexto del Capstone, siguiendo la recomendación explícita de National Academies.
- **Investigación de frontera en arquitecturas de aprendizaje profundo.** El curso 9 cubre el uso aplicado; la investigación de vanguardia es contenido de posgrado/electivo avanzado.
- **Profundidad completa en ingeniería de software de pruebas** (frameworks de automatización de pruebas, ingeniería de pipelines CI/CD a nivel de SRE). El curso 11 enseña la taxonomía y el razonamiento de pruebas de datos/modelos; la implementación de frameworks de prueba a profundidad de ingeniería de software es una especialización electiva.

# 9. Evidencia documental

**Curso 1 — Fundamentos de Analítica: Problemas, Decisiones y Evolución de las Metodologías.**
- `dataops-01-the-problem.pdf`: evidencia central; aporta el catálogo de mitos, problemas y brechas de conocimiento que motivan por qué se necesita una disciplina completa de analítica, no solo algoritmos.
- `dataops-03-methodologies.pdf`: aporta la línea histórica de 36 años de metodologías (KDD→CRISP-DM→...→DataOps) y el marco sintetizado de 8 dimensiones de un proyecto analítico.
- `informs-analytics-framework-2024.pdf`: aporta el marco de los siete dominios, usado en comparación directa con el marco de `dataops-03`.
- `cambridge-business-analytics.pdf`: aporta el módulo inicial de sesgos de decisión y la taxonomía descriptivo/predictivo/prescriptivo.
- `national-academies-data-science-for-undergraduates-2018.pdf`: aporta el concepto de "acumen de datos" como punto de entrada conceptual.

**Curso 2 — Estrategia de Datos y Analítica.**
- `dataops-02-data-strategy.pdf`: evidencia central y prácticamente exclusiva; aporta la totalidad del marco (diagnóstico, mecanismos de valor, brechas de capacidad, objetivos, iniciativas, gobierno de decisión, caso de valor, priorización, hoja de ruta, ejecución, evaluación).
- `informs-cap-essentials-blueprint.pdf` / `informs-cap-pro-blueprint.pdf`: aportan el Dominio I (encuadre del problema de negocio) como referencia profesional complementaria del "acuerdo del patrocinador".

**Curso 3 — Programación y Manejo de Datos.**
- `acm-computing-competencies-undergraduate-data-science-2021.pdf`: aporta las áreas de conocimiento de programación y fundamentos de cómputo.
- `usc-introduction-to-data-analytics.pdf`: aporta el tratamiento de modelado de datos y SQL introductorio.
- `mit-professional-certificate-data-engineering.pdf`: aporta los módulos introductorios de Python/NumPy/Pandas.

**Curso 4 — Estadística e Inferencia para la Analítica.**
- `berkeley-data-c102-data-inference-and-decisions.pdf`: aporta la estructura frecuentista/bayesiana y de pruebas de hipótesis.
- `warwick-foundations-of-data-analytics.pdf`: aporta el bloque de probabilidad y estadística de un módulo de posgrado denso.
- `mit-data-science-and-machine-learning.pdf`: aporta el módulo "Statistics for Data Science".

**Curso 5 — Analítica Descriptiva y Comunicación de Evidencia.**
- `usc-introduction-to-data-analytics.pdf`: aporta el bloque de visualización y tableros.
- `national-academies-data-science-for-undergraduates-2018.pdf`: aporta el área de "descripción y visualización de datos".
- `cambridge-business-analytics.pdf`: aporta el módulo de análisis descriptivo.

**Curso 6 — Ingeniería y Arquitectura de Datos para la Analítica.**
- `berkeley-data-c101-data-engineering.pdf`: evidencia central; aporta la definición de "operacionalización confiable y escalable".
- `dataops-08-data-scientids.pdf`: evidencia central nueva; aporta el contraste entre arquitectura canónica y arquitectura DataOps, las reglas de diseño de lagos/bodegas/mercados de datos, y el diseño de esquemas para consumo analítico.
- `mit-professional-certificate-data-engineering.pdf`: aporta arquitecturas de bases de datos y ETL.
- `acm-computing-competencies-undergraduate-data-science-2021.pdf`: aporta las KAs de "Sistemas de Big Data" y "Gobernanza, Adquisición y Gestión de Datos".

**Curso 7 — Analítica Predictiva I: Aprendizaje Supervisado.**
- `mit-data-science-and-machine-learning.pdf`: evidencia más rica; regresión, árboles, boosting, evaluación de modelos.
- `mit-professional-certificate-data-science-and-analytics.pdf`: regresión lineal/logística, CART, ensamblado.
- `warwick-foundations-of-data-analytics.pdf`: bloque de regresión y clasificación.
- `dataops-08-data-scientids.pdf`: aporta el diagrama de "deuda técnica oculta en sistemas de ML" (Sculley et al.), introducido aquí como advertencia conceptual y desarrollado en el curso 11.

**Curso 8 — Inferencia Causal y Diseño de Experimentos.**
- `berkeley-data-c102-data-inference-and-decisions.pdf`: inferencia causal explícita en su descripción oficial.
- `mit-data-science-and-machine-learning.pdf`: módulo de regresión causal, RCT y estudios observacionales.
- `mit-professional-certificate-data-science-and-analytics.pdf`: módulo de interpretabilidad y causalidad.
- `cambridge-business-analytics.pdf`: módulo de experimentación como "estándar de oro".

**Curso 9 — Analítica Predictiva II: No Supervisado, Series de Tiempo y Aprendizaje Profundo.**
- `mit-data-science-and-machine-learning.pdf`: clustering, PCA, recomendación, redes y modelos gráficos.
- `mit-professional-certificate-data-science-and-analytics.pdf`: redes neuronales, transferencia de aprendizaje, NLP.
- `warwick-foundations-of-data-analytics.pdf`: clustering, clasificación, SVD/PCA.

**Curso 10 — Analítica Prescriptiva: Optimización, Simulación y Decisión bajo Incertidumbre.**
- `mit-quantitative-methods-in-systems-engineering.pdf`: evidencia central; tradespace, pensamiento orientado a valor, sensibilidad/robustez.
- `cambridge-business-analytics.pdf`: módulos de analítica prescriptiva y sesgos de comportamiento.
- `mit-professional-certificate-data-science-and-analytics.pdf`: bloque de optimización lineal y filtrado colaborativo.
- `informs-analytics-framework-2024.pdf`: taxonomía descriptivo/predictivo/prescriptivo del Dominio II.

**Curso 11 — DataOps: Ingeniería Ágil y Lean del Ciclo de Vida Analítico.**
- `dataops-04-lean-thinking.pdf`: evidencia central; Lean/TPS, desperdicios en analítica, mapeo de flujo de valor, teoría de restricciones, análisis de causa raíz.
- `dataops-05-agile.pdf`: evidencia central; evolución de Waterfall a Scrum/XP/Kanban/SAFe, el Manifiesto DataOps, el ciclo de vida analítico (Ideación→Incepción→I+D→Transición/Producción→Retiro), el tablero Kanban ágil de DataOps y la plantilla de Hipótesis de Épica.
- `dataops-06-definition.pdf`: evidencia central; define DataOps como fusión de Agile/Lean/DevOps, aporta la hoja de ruta de 7 pasos de implementación y el modelo de MLOps de 3 fases.
- `dataops-09-data-quality.pdf`: evidencia central; taxonomía de pruebas automatizadas (unitarias, integración, funcionales, regresión, desempeño, humo) y control estadístico de proceso.
- `dataops-07-cdo.pdf`: aporta el módulo organizacional/de liderazgo — silos, Coordinación Relacional, trampas del líder de datos, niveles de madurez.
- `dataops-10-organization.pdf`: aporta los arquetipos de equipo, la matriz de roles/habilidades y el marco de "formas de habilidad" (T/Pi/M-shaped).
- `dataops-08-data-scientids.pdf`: aporta la porción de Design Thinking, deuda técnica de ML y plataforma DataOps (complementaria a su aporte al curso 6).
- `mit-cloud-and-devops.pdf`: aporta contenido técnico de contenerización, métricas DevOps, arquitecturas serverless y cloud-native.
- `informs-analytics-framework-2024.pdf` / `informs-cap-essentials-blueprint.pdf` / `informs-cap-pro-blueprint.pdf`: aportan los Dominios VI-VII (Despliegue, Gestión del Ciclo de Vida).

**Curso 12 — Productos y Sistemas Analíticos.**
- `mit-designing-and-building-ai-products-and-services.pdf`: evidencia central; proceso de diseño de producto de IA, HCI, "supermentes".
- `mit-digital-platforms.pdf`: lógica de plataforma/ecosistema y efectos de red.
- `mit-data-leadership.pdf`: concepto de plataformas de datos y "fábricas de IA".

**Curso 13 — Gobernanza, Ética y Responsabilidad en Analítica e IA.**
- `national-academies-data-science-for-undergraduates-2018.pdf`: evidencia central; ética de primer orden, Juramento de Ciencia de Datos, casos de fracaso.
- `acm-computing-competencies-undergraduate-data-science-2021.pdf`: KAs de Profesionalismo y Privacidad/Seguridad.
- `informs-cap-pro-blueprint.pdf`: énfasis en "impacto en la sociedad".
- `berkeley-data-c102-data-inference-and-decisions.pdf`: privacidad diferencial fusionada en un curso técnico.
- `warwick-foundations-of-data-analytics.pdf`: bloque dedicado de anonimización y privacidad diferencial.
- `dataops-02-data-strategy.pdf`: aporta el modelo de gobierno de decisión institucional (centralizado/federado/descentralizado) que aquí se retoma y conecta con la responsabilidad ética.
- `mit-data-leadership.pdf`: sesiones dedicadas a sesgo y equidad en IA.

**Curso 14 — Capstone: Proyecto Integrador de Analítica.**
- `informs-analytics-framework-2024.pdf`: modelo cíclico de siete dominios como estructura organizadora del proyecto.
- `dataops-03-methodologies.pdf`: el marco de 8 dimensiones como plantilla alternativa/complementaria de ejecución del proyecto integrador.
- `national-academies-data-science-for-undergraduates-2018.pdf`: recomendación de anclar el proyecto final a un dominio de aplicación real.
- `mit-designing-and-building-ai-products-and-services.pdf`: modelo de propuesta de diseño como formato de entrega final.

*Nota:* `mit-rapid-prototyping-methodologies.pdf` no se usó como evidencia de diseño de ningún curso del núcleo; su contenido (prototipado físico/manufactura) se consideró en la Sección 8 como fuera del alcance de un currículo de Analítica.

# 10. Riesgos y decisiones discutibles

**1. DataOps como un único curso (11) en lugar de dividirlo en dos o tres.** Siete de los diez documentos nuevos del corpus (`01,03,04,05,06,07,09,10`, parcialmente también `08`) alimentan un solo curso. La alternativa más fuerte: dividir en "Lean y Ágil para Analítica" (04, 05) y "Ingeniería de Entrega y Calidad de Datos" (06, 08, 09) y "Organización y Liderazgo de Equipos de Datos" (07, 10) como tres cursos separados, dado el volumen y la heterogeneidad de audiencias que el propio corpus distingue (el CDO en `07` no es el mismo lector que el ingeniero de datos en `08`). Se prefirió un curso único porque las tres audiencias comparten un mismo objeto (la entrega confiable de soluciones analíticas) y fragmentarlas arriesga perder la narrativa unificadora que el propio Manifiesto DataOps ofrece; pero un diseñador que priorice profundidad sobre integración podría preferir la división.

**2. Estrategia de Datos y Analítica (curso 2) como curso obligatorio temprano, en lugar de un módulo dentro de Fundamentos o un curso electivo tardío.** La alternativa más fuerte: fusionar con el curso 1 (ya que ambos son conceptuales y no requieren programación) o moverlo al final, junto a Gobernanza, argumentando que un estudiante sin experiencia técnica no puede diagnosticar capacidades de datos de forma realista. Se prefirió un curso propio y temprano porque `dataops-02` tiene la profundidad y coherencia interna de un curso completo (25 diapositivas con marco propio de 12 pasos), y porque conceptualmente ancla la justificación organizacional de todo lo que sigue; pero se reconoce que un estudiante de primer año puede carecer del contexto empresarial para aprovecharlo plenamente, lo que podría argumentar a favor de recolocarlo más adelante (p. ej., en paralelo con el curso 10).

**3. Separar Ingeniería de Datos (curso 6) de DataOps (curso 11) pese a que `dataops-08` evidencia un solapamiento real entre ambos.** La alternativa más fuerte: fusionarlos en un único curso de "Ingeniería y Operación de Datos", ya que en la práctica un mismo equipo suele ejecutar ambas funciones y `dataops-08` mismo no las separa limpiamente. Se prefirió mantenerlos separados porque representan preguntas de naturaleza distinta —diseño de arquitectura frente a proceso de entrega y organización— y porque la separación permite que el curso 11 reciba, como insumo ya resuelto, una arquitectura de datos estable sobre la cual practicar Lean/Agile/DataOps; fusionarlos arriesga que la profundidad de cualquiera de las dos preguntas se diluya.

**4. Incluir contenido de liderazgo y organización de equipos (`dataops-07`, `dataops-10`) dentro del curso técnico de DataOps, en lugar de crear un curso de liderazgo separado.** La alternativa más fuerte, ahora reforzada por la evidencia nueva: un curso dedicado de "Liderazgo y Organización de Datos" que desarrolle a profundidad la Coordinación Relacional, los arquetipos de equipo y las trampas del CDO, posiblemente compartido con estudiantes de programas de gestión. Se prefirió integrarlo en el curso 11 porque su audiencia natural (ingenieros/científicos de datos que eventualmente lideran equipos) coincide con la audiencia del resto del curso, y porque fragmentar el contenido organizacional del contenido técnico de entrega reproduciría exactamente el problema de silos que `dataops-07` diagnostica como causa raíz de fallas organizacionales.

**5. Colocar "Historia y marcos de metodología analítica" (contenido de `dataops-03`) dentro de Fundamentos (curso 1) en lugar de crear un curso propio.** La alternativa más fuerte: dado que `dataops-03` es el documento más denso en citas históricas de todo el corpus de 31 documentos (36 años de metodologías con autores y fechas), podría justificar un curso breve propio de "Metodología de Proyectos Analíticos". Se prefirió integrarlo en Fundamentos porque su función pedagógica —dar un mapa mental antes de cualquier contenido técnico— es exactamente la función que ya cumple el curso 1, y crear un curso adicional fragmentaría innecesariamente algo que se entiende mejor como una sola narrativa continua (el problema → su evolución histórica → el marco vigente).

**6. Un curso dedicado de Gobernanza/Ética (curso 13) que consolida tres niveles de gobierno distintos, en lugar de mantenerlos completamente separados o completamente transversales.** La evidencia nueva (`dataops-02`) añade un tercer nivel de gobierno (institucional/de decisión) al que ya existía (operativo/ético), lo que multiplica el riesgo de que "gobernanza" se vuelva un término ambiguo que los estudiantes no logren distinguir. La alternativa más fuerte: dedicar un curso a cada nivel, o renombrar el curso 13 para que el título mismo distinga los tres niveles. Se prefirió un curso único e integrador porque el propósito de este curso es precisamente que el estudiante aprenda a distinguir los tres niveles al aplicarlos simultáneamente a una misma solución, no a estudiarlos en aislamiento.

**7. Mantener dos cursos de Analítica Predictiva con Inferencia Causal intercalada.** (Decisión heredada del análisis del corpus original, no alterada por la evidencia DataOps). La alternativa más fuerte sigue siendo comprimir en un curso de "Modelado Predictivo" con un módulo de causalidad. Se mantiene la separación por las mismas razones documentadas en el corpus original (Berkeley C102 como curso institucional propio, MIT IDSS con semanas consecutivas dedicadas).

**8. Tratar la Analítica Prescriptiva como un único curso.** (Decisión heredada, no alterada). Se mantiene por la instrucción explícita de no equiparar prescriptivo con toda la Investigación de Operaciones.

# 11. Arquitectura final resumida

```
NIVEL I — Fundamentos y marco de referencia
  [1] Fundamentos de Analítica: Problemas, Decisiones
      y Evolución de las Metodologías
        │
        ├──────────────┐
        ▼              ▼
  [2] Estrategia de   [3] Programación y
      Datos y            Manejo de Datos
      Analítica           │
        │                 │
        │        ┌────────┴────────┐
        │        ▼                 ▼
NIVEL II │  [4] Estadística    [5] Analítica Descriptiva
—Núcleo  │      e Inferencia       y Comunicación de Evidencia
técnico  │        │                 │
        │        └────────┬────────┘
        │                 ▼
        │        [6] Ingeniería y Arquitectura
        │            de Datos para la Analítica
        │                 │
        │                 ▼
        │        [7] Analítica Predictiva I
        │            (Aprendizaje Supervisado)
        │                 │
NIVEL III│                ▼
—Razona- │       [8] Inferencia Causal y Diseño
miento   │           de Experimentos
avanzado │                │
        │                 ▼
        │       [9] Analítica Predictiva II
        │           (No Supervisado, Series de Tiempo,
        │            Aprendizaje Profundo)
        │                 │
        │                 ▼
        │       [10] Analítica Prescriptiva
        │            (Optimización, Simulación, Decisión)
        │                 │
        └─────────────────┤
                           ▼
NIVEL IV — Entrega,  [11] DataOps: Ingeniería Ágil y Lean
producto y                del Ciclo de Vida Analítico
responsabilidad            │
                           ▼
                    [12] Productos y Sistemas Analíticos
                           │
                           ▼
                    [13] Gobernanza, Ética y Responsabilidad
                         en Analítica e IA
                    (retoma el gobierno institucional de [2]
                     y el gobierno operativo de [6])
                           │
                           ▼
                    [14] CAPSTONE: Proyecto Integrador
                         de Analítica
                    (ciclo completo: encuadre → estrategia →
                     datos → método → modelo → entrega DataOps
                     → producto → gobernanza, con patrocinador real)
```

**Hilo transversal** (presente en todos los niveles):
`Ética · Privacidad · Gobierno de datos (3 niveles) · Comunicación · Reproducibilidad · Formulación de problemas · Organización de equipos`

**Lectura del diagrama:** la única bifurcación temprana (cursos 2–3, y su reconvergencia interna 4–5) refleja las dos únicas relaciones verdaderamente paralelas del diseño: estrategia organizacional frente a formación técnica, y estadística frente a comunicación descriptiva. A partir del curso 6 la cadena es estrictamente lineal, reflejando la decisión de tratar cada competencia como parte de una columna vertebral única y compartida, mientras que la profundización en herramientas específicas de DataOps, la teoría completa de Investigación de Operaciones, la especialización organizacional/de liderazgo y los dominios de aplicación quedan reservados al espacio electivo fuera de esta arquitectura de núcleo.
