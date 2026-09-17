# 1. Lectura global del corpus

El corpus reunido —21 documentos que van desde marcos curriculares de sociedades profesionales (ACM, INFORMS) y un informe de política académica (National Academies), pasando por registros de catálogo de dos cursos de pregrado (Berkeley C101/C102) y un módulo de posgrado (Warwick), hasta programas profesionales de educación ejecutiva y certificados (MIT xPRO, MIT IDSS, MIT Professional Education, Cambridge Judge, PwC) y un curso universitario introductorio (USC)— no describe una disciplina única y homogénea. Describe una **tensión productiva entre tres conceptualizaciones distintas de "Analítica"** que coexisten en la práctica real:

1. **Analítica como ingeniería de sistemas de datos** (Berkeley C101, ACM-BDS/CCF/SDM, MIT Data Engineering, MIT Cloud & DevOps): el énfasis está en la escala, la arquitectura, la confiabilidad y la "operacionalización" —construir la infraestructura que hace posible el análisis, no el análisis mismo.

2. **Analítica como razonamiento estadístico y de aprendizaje bajo incertidumbre** (Berkeley C102, Warwick, MIT IDSS Data Science and ML, National Academies): el énfasis está en la inferencia, la causalidad, la cuantificación de la incertidumbre y el modelado predictivo como actividades intelectuales con fundamentos matemáticos propios, distintas de la ingeniería de datos y de la administración de sistemas.

3. **Analítica como disciplina de decisión organizacional** (INFORMS Analytics Framework y sus dos blueprints CAP, Cambridge Business Analytics, PwC Academy, MIT Data Leadership): el énfasis está en el ciclo completo que va desde el encuadre de un problema de negocio hasta el despliegue, la validación del caso de negocio y el acompañamiento del patrocinador ("sponsor agreement") en cada etapa. Aquí el dato y el modelo son instrumentales; lo que se evalúa es la calidad de la decisión resultante.

Ninguna de las tres conceptualizaciones es suficiente por sí sola para explicar el corpus completo, y de hecho el propio corpus contiene advertencias explícitas contra la reducción de la disciplina a solo una de ellas: la ACM insiste en que su documento es apenas "un paso productivo en una conversación" y no reclama la propiedad completa de la Ciencia de Datos; el reporte de National Academies afirma textualmente que la disciplina "no es estadística... no es ciencia de la computación con foco en aprendizaje de máquina... no es matemática aplicada"; y el marco INFORMS presenta explícitamente los siete dominios como un ciclo cerrado y recurrente, no como una tubería lineal que termina en el modelo.

De la lectura conjunta emerge una cuarta capa, menos visible pero estructuralmente necesaria, que atraviesa las tres anteriores: una **capa de responsabilidad** (ética, gobernanza, privacidad, sesgo algorítmico, impacto social) que aparece en casi todos los documentos —aunque con grados de centralidad muy distintos—, desde el "Juramento de Ciencia de Datos" propuesto por National Academies (inspirado en el juramento hipocrático) hasta la fusión explícita de privacidad diferencial dentro del propio curso de inferencia de Berkeley (C102), pasando por los dos módulos dedicados a sesgo y gobernanza de MIT Data Leadership y el énfasis en "impacto en la sociedad" que CAP-Pro añade sobre CAP-Essentials.

En consecuencia, la concepción de Analítica que se adopta en este diseño es la de **una disciplina de ciclo completo para la toma de decisiones basada en evidencia**, que integra sistemáticamente cuatro capacidades irreducibles entre sí —construir/gestionar datos, describir/inferir/predecir con rigor estadístico, prescribir/decidir bajo incertidumbre, y operar/productizar la solución de forma responsable— y que trata el encuadre del problema y la responsabilidad ética como puntos de entrada y de control transversales, no como pasos opcionales al principio o al final.

# 2. Competencias que debe desarrollar la cadena completa

Estas familias de competencias son independientes de la arquitectura de cursos que se propone más adelante; representan lo que un egresado de la cadena completa debe poder hacer, sin importar en qué curso específico lo haya aprendido.

**A. Formulación y encuadre de problemas analíticos.** Traducir una pregunta de negocio, de política pública o de investigación en una pregunta analítica bien definida; identificar actores interesados y sus perspectivas divergentes; distinguir cuándo un problema es "amenable" al análisis de datos y cuándo no; construir y validar un caso de negocio inicial; obtener y mantener el acuerdo del patrocinador a lo largo del ciclo (INFORMS Dominios I–II).

**B. Adquisición, gestión, gobernanza y calidad de datos.** Identificar y priorizar necesidades de datos; evaluar fuentes y estructuras (relacionales, no relacionales, streaming); construir planes de gestión de datos; limpiar, armonizar, transformar y validar; documentar linaje y decisiones de calidad; aplicar principios de gobernanza (propiedad, custodia, políticas de retención) sin reducir esto a administración de infraestructura.

**C. Análisis descriptivo y comunicación de evidencia.** Explorar datos de forma rigurosa (EDA), elegir representaciones visuales apropiadas al tipo de variable y a la audiencia, construir tableros e informes que soporten decisiones, y —de forma más amplia— narrar evidencia de manera comprensible para audiencias técnicas y no técnicas.

**D. Razonamiento estadístico y cuantificación de la incertidumbre.** Probabilidad, estimación, pruebas de hipótesis, intervalos de confianza, razonamiento frecuentista y bayesiano, diseño experimental, y evaluación crítica de la evidencia estadística (incluyendo el reconocimiento de la tasa de descubrimientos falsos y los límites de la significancia).

**E. Modelado predictivo y aprendizaje automático.** Construcción, evaluación, calibración, regularización y validación de modelos supervisados y no supervisados —desde regresión y árboles hasta aprendizaje profundo—, con criterios explícitos de desempeño, generalización e interpretabilidad.

**F. Distinción entre predicción, inferencia estadística, causalidad y decisión.** Reconocer cuándo un modelo predictivo no permite una afirmación causal; diseñar o evaluar experimentos controlados y estudios observacionales con variables de confusión; distinguir el objetivo de "predecir bien" del objetivo de "actuar correctamente" ante una decisión.

**G. Analítica prescriptiva: optimización, simulación y decisión bajo incertidumbre.** Modelado de decisiones mediante optimización, simulación y análisis de "tradespace"/valor; incorporación explícita de restricciones, riesgo y sesgos de comportamiento en la recomendación de una acción, sin equiparar esto a un curso completo de investigación de operaciones.

**H. Ingeniería y arquitectura de soluciones analíticas.** Diseño de arquitecturas de datos escalables, confiables y mantenibles; comprensión de las opciones tecnológicas (arquitecturas distribuidas, almacenamiento, cómputo en la nube) al nivel de sus propiedades y compromisos, no de certificación en una herramienta específica.

**I. Despliegue, operacionalización y gestión del ciclo de vida.** Validar una solución con el negocio antes de desplegarla, definir requerimientos de producción, dar soporte a la implementación, monitorear el desempeño en producción, recalibrar modelos, y mantener la trazabilidad del caso de negocio en el tiempo (INFORMS Dominios VI–VII).

**J. Diseño de productos y sistemas analíticos.** Diseñar la interacción humano-máquina de una solución analítica, decidir el nivel apropiado de involucramiento humano frente al automatizado, considerar la integración organizacional y —cuando aplique— la lógica de plataforma/ecosistema de la solución; esto excede ampliamente la construcción de un tablero.

**K. Prácticas de trabajo reproducible y colaborativo.** Control de versiones, documentación de supuestos y decisiones, estructuración de proyectos analíticos como software mantenible, trabajo en equipo con roles complementarios (ingeniería, modelado, negocio).

**L. Gobernanza, ética, privacidad, seguridad y responsabilidad en IA.** Reconocer y mitigar sesgo algorítmico, aplicar principios de privacidad (incluida la privacidad diferencial), entender el marco regulatorio general que rodea el uso de datos personales, y asumir una postura profesional ante el impacto social de una solución analítica.

**M. Comunicación, framing organizacional y gestión del cambio basado en datos.** Comunicar resultados técnicos a audiencias ejecutivas, negociar el alcance y las expectativas con patrocinadores, y acompañar la adopción organizacional de una solución analítica.

# 3. Tensiones y decisiones curriculares fundamentales

**Estadística vs. aprendizaje automático.** El corpus no trata estas dos tradiciones como sinónimos ni como una jerarquía donde una reemplaza a la otra. Berkeley las separa institucionalmente en dos cursos (C101 ingeniería vs. C102 inferencia/decisiones), y la propia ACM decide *no* reclamar el terreno de la estadística ("dejamos math/stats a las sociedades hermanas"), mientras que el aprendizaje automático sí forma parte de su núcleo computacional. Decisión adoptada: la estadística inferencial se enseña como fundamento previo y autónomo (no como introducción al aprendizaje automático), y el aprendizaje automático se construye explícitamente sobre ella, pero se le reconoce una identidad propia (optimización, representación, generalización) que no se agota en la inferencia clásica.

**Predicción vs. inferencia estadística.** Un modelo puede predecir bien sin que sus coeficientes tengan interpretación inferencial válida (y viceversa). Berkeley C102 y el módulo de "modern regression" de MIT IDSS tratan esto como un punto de inflexión pedagógico explícito. Decisión: este contraste se enseña como contenido central, no como nota al pie, en el curso de Inferencia Causal.

**Predicción vs. inferencia causal.** El corpus ofrece evidencia inusualmente fuerte y consistente de que esta distinción merece tratamiento dedicado: Berkeley C102 la nombra en su descripción oficial, MIT IDSS le dedica semanas consecutivas (regresión para predicción → RCT y estudios observacionales con variables de confusión), y el certificado de MIT en Ciencia de Datos y Analítica incluye un módulo explícito de "Interpretabilidad y Causalidad". Decisión: se crea un curso propio (no un módulo dentro de otro curso) para esta competencia.

**Predicción vs. prescripción.** El marco INFORMS distingue explícitamente el encuadre "descriptivo/predictivo/prescriptivo" como parte de la Fase II (Analytics Problem Framing), y Cambridge Business Analytics dedica módulos separados a cada uno. Decisión: la analítica prescriptiva se trata como una competencia con lógica propia (optimización, simulación, decisión bajo incertidumbre) que *consume* las salidas de los modelos predictivos y causales, no como una extensión de estos.

**Optimización vs. analítica de decisión más amplia.** El corpus muestra dos maneras distintas de tratar "lo prescriptivo": como optimización matemática clásica (MIT Data Science and Analytics: programación lineal, filtrado colaborativo) y como exploración de espacio de diseño/valor bajo incertidumbre y sesgos de comportamiento (MIT Quantitative Methods: tradespace, Pareto, sensibilidad; Cambridge: sesgos de decisión, aversión al riesgo). Decisión explícita del enunciado del ejercicio (no equiparar prescriptivo con toda la Investigación de Operaciones): el curso de Analítica Prescriptiva integra ambas miradas a nivel de modelado de decisiones, dejando la profundidad matemática completa de IO (dualidad, teoría de colas, procesos estocásticos) como especialización electiva.

**Ciencia de datos vs. ingeniería de datos.** Esta es quizás la bifurcación mejor documentada del corpus: Berkeley separa institucionalmente C101 (ingeniería, "operacionalización confiable y escalable") de C102 (inferencia y decisiones), y MIT ofrece dos certificados profesionales completos y distintos —uno con un stack tecnológico de más de 40 herramientas nombradas (Data Engineering) y otro centrado en estadística, optimización y comunicación ejecutiva (Data Science and Analytics)— compartiendo el mismo formato comercial pero con contenidos casi disjuntos. Decisión: se mantienen como competencias distintas con cursos propios, unidas por un curso de fundamentos común.

**Análisis vs. sistemas de producción.** INFORMS separa el Dominio V (Desarrollo de Modelos) del Dominio VI (Despliegue) y VII (Gestión del Ciclo de Vida) como fases con entregables, actores y validaciones distintas; MIT Cloud & DevOps es enteramente un curso de operación de sistemas en producción. Decisión: el despliegue y el mantenimiento en producción constituyen un curso propio, no una sección final de "extras" en el curso de modelado.

**Modelado vs. despliegue.** Relacionado con lo anterior pero distinto: un modelo puede ser estadísticamente correcto y no ser desplegable (por requisitos de negocio, de sistema o de usabilidad no satisfechos). El propio marco INFORMS exige una "validación de negocio" y un "reporte de validación" *antes* de construir requisitos de producción. Decisión: el curso de Despliegue explicita esta frontera como su punto de entrada.

**Análisis técnico vs. toma de decisiones organizacional.** MIT Data Leadership, Cambridge y PwC Academy (con su "Master Class" para líderes no técnicos) muestran que existe una audiencia y un tipo de contenido dedicado a la traducción organizacional del análisis, separado del contenido técnico. Sin embargo, estos documentos están dirigidos a *consumidores* de analítica (gerentes, ejecutivos), no a quienes la producen. Dado que este diseño forma profesionales que **producen** soluciones analíticas, se decide no crear un curso de "liderazgo" dedicado, sino tratar la comunicación ejecutiva y el encuadre organizacional como competencia transversal, concentrada especialmente en el curso de Fundamentos y en el Capstone (ver Sección 10 para la discusión de esta decisión como punto discutible).

**Profundidad técnica vs. amplitud de herramientas.** El contraste entre MIT Machine Learning, Modeling and Simulation Principles (cero herramientas nombradas, contenido puramente conceptual/numérico) y el certificado de Ingeniería de Datos de MIT (más de 40 herramientas nombradas) ilustra una tensión entre durabilidad conceptual y relevancia inmediata de mercado laboral. Decisión: el diseño prioriza principios durables como columna vertebral de cada curso, y trata las herramientas específicas como el "laboratorio" instanciado de esos principios en un momento dado, sustituible sin rediseñar el curso.

**Ética como módulo separado vs. ética fusionada en cada competencia técnica.** National Academies exige explícitamente que la ética esté "tejida a través de todo el currículo desde el principio", mientras que Berkeley C102 la funde directamente dentro del curso técnico de inferencia (privacidad diferencial como parte de un curso de estadística, no de un curso de ética aparte). ACM, en cambio, la agrupa bajo "Profesionalismo" como área de conocimiento distinguible. Decisión: se adoptan ambas estrategias simultáneamente y de forma deliberada (ver Sección 6 y Sección 10).

# 4. Arquitectura curricular propuesta

La arquitectura consta de 13 cursos organizados en cuatro niveles progresivos. Los cursos 3 y 4 pueden cursarse en paralelo (ambos dependen solo del curso 2); el resto sigue una cadena de prerrequisitos estricta.

---

**Nivel I — Fundamentos**

### 1. Fundamentos de Analítica y Formulación de Problemas de Decisión
- **Posición:** primer curso de la cadena, sin prerrequisitos de analítica.
- **Propósito central:** instalar el mapa mental de ciclo completo (encuadre de negocio → encuadre analítico → datos → método → modelo → despliegue → ciclo de vida) como marco que organizará todos los cursos siguientes; introducir la taxonomía descriptivo/predictivo/prescriptivo; exponer los sesgos cognitivos más comunes en la toma de decisiones antes de introducir cualquier herramienta técnica.
- **Competencias principales:** A (formulación de problemas), M (comunicación/framing), introducción a L (ética) y a la idea de "acumen de datos".
- **Prerrequisitos:** ninguno (solo prerrequisitos institucionales externos: razonamiento cuantitativo básico).
- **Qué recibe de cursos previos:** nada; es la puerta de entrada.
- **Qué prepara para lo siguiente:** el vocabulario y el marco de referencia (los "siete dominios") que los cursos 2 a 13 llenarán de contenido técnico.

### 2. Programación y Manejo de Datos
- **Posición:** segundo curso; puede iniciarse junto con el curso 1.
- **Propósito central:** desarrollar fluidez computacional (programación, estructuras de datos, manipulación de datos tabulares y semiestructurados, fundamentos de SQL) como condición habilitante de todo lo posterior.
- **Competencias principales:** B (parcial: manejo básico de datos), K (parcial: buenas prácticas de código).
- **Prerrequisitos:** curso 1 (recomendado, no estricto).
- **Qué recibe:** el marco conceptual del curso 1 para dar sentido a por qué se manipulan datos de cierta manera.
- **Qué prepara:** la base computacional para los cursos 3, 4 y 5.

---

**Nivel II — Núcleo técnico**

### 3. Estadística e Inferencia para la Analítica
- **Posición:** tercer curso, en paralelo con el curso 4.
- **Propósito central:** probabilidad aplicada, estimación, pruebas de hipótesis, intervalos de confianza, razonamiento frecuentista y bayesiano, diseño experimental básico.
- **Competencias principales:** D (razonamiento estadístico).
- **Prerrequisitos:** curso 2 (más prerrequisito externo de cálculo/álgebra lineal básica).
- **Qué recibe:** capacidad de programar y manejar datos del curso 2.
- **Qué prepara:** el lenguaje formal de incertidumbre que sostiene los cursos 6, 7, 8 y 9.

### 4. Analítica Descriptiva y Comunicación de Evidencia
- **Posición:** cuarto curso, en paralelo con el curso 3.
- **Propósito central:** análisis exploratorio de datos, principios de visualización según tipo de variable y audiencia, construcción de tableros/informes, narrativa de datos.
- **Competencias principales:** C (descripción y comunicación).
- **Prerrequisitos:** curso 2.
- **Qué recibe:** datos ya manejables gracias al curso 2; se apoya en nociones básicas de variabilidad que el curso 3 profundizará en paralelo.
- **Qué prepara:** el hábito de "mirar los datos antes de modelarlos", que se vuelve prerrequisito informal de los cursos 5 y 6.

### 5. Ingeniería de Datos para la Analítica
- **Posición:** quinto curso.
- **Propósito central:** arquitecturas de datos (relacional y no relacional), pipelines de adquisición/transformación, calidad y gobernanza de datos, principios de escalabilidad y confiabilidad —explícitamente **no** reducido a administración de infraestructura: incluye documentación de linaje, gestión de calidad y decisiones de gobernanza como entregables intelectuales.
- **Competencias principales:** B (completa), H (parcial).
- **Prerrequisitos:** cursos 2 y 4.
- **Qué recibe:** del curso 4, el criterio sobre qué hace que un conjunto de datos sea útil para el análisis; del curso 2, la base de programación.
- **Qué prepara:** datos confiables y bien gobernados como insumo de los cursos 6 a 9; principios de arquitectura que se retoman en el curso 10.

### 6. Analítica Predictiva I: Aprendizaje Supervisado
- **Posición:** sexto curso.
- **Propósito central:** regresión, clasificación, árboles, ensambles; evaluación, regularización y validación de modelos; criterios de desempeño y generalización.
- **Competencias principales:** E (modelado predictivo, primera mitad).
- **Prerrequisitos:** cursos 3 y 5 (y beneficio del curso 4).
- **Qué recibe:** el aparato formal de incertidumbre (curso 3) y datos gobernados (curso 5).
- **Qué prepara:** el vehículo técnico (regresión/clasificación) que el curso 7 usará para introducir la distinción causal.

---

**Nivel III — Razonamiento avanzado**

### 7. Inferencia Causal y Diseño de Experimentos
- **Posición:** séptimo curso.
- **Propósito central:** distinguir explícitamente predicción de causalidad; diseño y análisis de experimentos controlados (incluyendo pruebas A/B); estudios observacionales con variables de confusión; los límites de la inferencia causal a partir de modelos predictivos.
- **Competencias principales:** F (distinción predicción/inferencia/causalidad/decisión).
- **Prerrequisitos:** curso 6 (usa la regresión como vehículo técnico compartido) y curso 3.
- **Qué recibe:** el modelo de regresión ya dominado técnicamente en el curso 6, reinterpretado bajo una pregunta distinta.
- **Qué prepara:** el criterio para no confundir "el modelo predice bien" con "la intervención recomendada funcionará", que sostiene los cursos 8 y 9.

### 8. Analítica Predictiva II: No Supervisado, Series de Tiempo y Aprendizaje Profundo
- **Posición:** octavo curso.
- **Propósito central:** clustering, reducción de dimensionalidad, sistemas de recomendación, redes y modelos gráficos, series de tiempo, fundamentos de aprendizaje profundo —tratado como extensión del aparato de optimización visto en el curso 6, no como disciplina separada.
- **Competencias principales:** E (modelado predictivo, segunda mitad, con foco no supervisado y de representación).
- **Prerrequisitos:** cursos 6 y 7.
- **Qué recibe:** la base de aprendizaje supervisado (curso 6) y la disciplina de no confundir correlación con causalidad (curso 7), relevante para interpretar clusters y representaciones aprendidas.
- **Qué prepara:** modelos avanzados que alimentarán las decisiones prescriptivas del curso 9 y los productos analíticos del curso 11.

### 9. Analítica Prescriptiva: Optimización, Simulación y Decisión bajo Incertidumbre
- **Posición:** noveno curso.
- **Propósito central:** modelado de decisiones mediante optimización (formulación, no teoría matemática profunda), simulación (Monte Carlo, análisis de sensibilidad), y análisis de valor/tradespace bajo múltiples criterios y restricciones; incorporación de sesgos de comportamiento relevantes a la decisión.
- **Competencias principales:** G (analítica prescriptiva).
- **Prerrequisitos:** cursos 6, 7 y 8 (usa salidas predictivas y causales como insumos de la decisión) y curso 3.
- **Qué recibe:** estimaciones predictivas y causales de los cursos anteriores como parámetros/restricciones del problema de decisión.
- **Qué prepara:** una "solución candidata" (no solo un modelo) lista para ser evaluada de cara al despliegue.

---

**Nivel IV — Operacionalización y producto**

### 10. Despliegue y Ciclo de Vida de Soluciones Analíticas
- **Posición:** décimo curso.
- **Propósito central:** validación de negocio previa al despliegue, definición de requisitos de producción (modelo, usabilidad, sistema, negocio), principios de arquitectura en la nube, contenerización, prácticas DevOps/MLOps, monitoreo y recalibración de modelos en producción, mantenimiento del caso de negocio en el tiempo.
- **Competencias principales:** I (despliegue y ciclo de vida), H (parcial, arquitectura de producción).
- **Prerrequisitos:** cursos 5 y 9.
- **Qué recibe:** principios de arquitectura del curso 5 y una solución candidata del curso 9.
- **Qué prepara:** una solución en producción, monitoreada y mantenible, que el curso 11 convertirá en producto.

### 11. Productos y Sistemas Analíticos
- **Posición:** undécimo curso.
- **Propósito central:** diseño de la interacción humano-máquina de una solución analítica; decisión del nivel apropiado de automatización frente a intervención humana; integración organizacional de la solución; nociones de plataforma/ecosistema cuando la solución conecta a múltiples partes interesadas —explícitamente más allá de construir un tablero.
- **Competencias principales:** J (diseño de productos analíticos).
- **Prerrequisitos:** curso 10.
- **Qué recibe:** una solución ya desplegada y monitoreada.
- **Qué prepara:** una solución adoptable organizacionalmente, lista para ser evaluada bajo un lente de gobernanza y responsabilidad.

### 12. Gobernanza, Ética y Responsabilidad en Analítica e IA
- **Posición:** duodécimo curso (integrador, no introductorio: ver Sección 6 sobre por qué la ética también es transversal desde el curso 1).
- **Propósito central:** consolidar, a nivel de sistema completo, los principios de gobernanza de datos, privacidad (incluida la privacidad diferencial), sesgo algorítmico, impacto social y responsabilidad profesional, aplicándolos retrospectivamente a las soluciones construidas en los cursos 5 a 11.
- **Competencias principales:** L (gobernanza, ética, privacidad, seguridad, IA responsable).
- **Prerrequisitos:** cursos 10 y 11 (para tener un objeto concreto —una solución desplegada y productizada— sobre el cual razonar la responsabilidad).
- **Qué recibe:** una solución completa de principio a fin sobre la cual auditar implicaciones éticas y de gobernanza.
- **Qué prepara:** el criterio de responsabilidad profesional que se exige explícitamente en el Capstone.

### 13. Capstone: Proyecto Integrador de Analítica
- **Posición:** curso final.
- **Propósito central:** ejecutar el ciclo completo de los siete dominios (encuadre de negocio → encuadre analítico → datos → método → modelo → despliegue → ciclo de vida) sobre un problema real, con patrocinador, incluyendo la gestión explícita del acuerdo con el patrocinador en cada etapa.
- **Competencias principales:** integración de A a M.
- **Prerrequisitos:** todos los cursos anteriores.
- **Qué recibe:** todas las competencias previas.
- **Qué prepara:** al egresado para la práctica profesional o estudios de posgrado.

# 5. Fronteras entre cursos

**1 → 2.** El curso 1 puede mencionar Python/SQL como ejemplos al hablar de "qué hace un analista", pero no enseña sintaxis ni sintaxis de consultas; el curso 2 no discute taxonomías de decisión ni sesgos cognitivos. La frontera es: "hablar sobre" vs. "hacer".

**2 → 3 / 2 → 4.** La limpieza y transformación de datos vive en el curso 2; la pregunta de "¿son estos datos suficientes para generalizar una conclusión?" vive en el curso 3; la pregunta de "¿cómo represento estos datos para que alguien entienda un patrón?" vive en el curso 4. Un tema ambiguo —detección de valores atípicos— se resuelve así: la detección mecánica (reglas, percentiles) es del curso 2; la justificación estadística de por qué un valor es atípico (bajo qué distribución, con qué probabilidad) es del curso 3; su visualización para una audiencia es del curso 4.

**3 ↔ 4 (paralelos).** Ambos usan el mismo tipo de datasets pequeños/limpios. La frontera: el curso 4 puede mostrar un histograma o un boxplot como herramienta descriptiva sin justificar su base probabilística; el curso 3 exige justificar el supuesto distribucional detrás de cualquier afirmación de incertidumbre (p. ej., un intervalo de confianza). Los intervalos de confianza y las pruebas de hipótesis pertenecen exclusivamente al curso 3, aun si se visualizan gráficamente.

**4 → 5.** La visualización y el storytelling con datos ya limpios y pequeños terminan en el curso 4; el curso 5 empieza donde los datos son grandes, múltiples, desincronizados o de mala calidad y se requiere una arquitectura (no solo un script) para producirlos de forma confiable y repetible. Un tema ambiguo —el diseño de un tablero de monitoreo de calidad de datos— se resuelve a favor del curso 5, porque su propósito es operacional (gobernanza), no comunicativo hacia un tomador de decisiones de negocio.

**5 → 6.** La ingeniería de datos entrega conjuntos de datos gobernados, documentados y con calidad conocida; el curso 6 no vuelve a enseñar limpieza de datos salvo como repaso rápido — asume el insumo del curso 5. La frontera es explícita: el curso 5 responde "¿puedo confiar en este dato?"; el curso 6 responde "¿qué puedo predecir con este dato?".

**6 → 7.** Ambos cursos pueden usar el mismo modelo de regresión sobre el mismo conjunto de datos. La frontera no es el método sino la pregunta: el curso 6 pregunta "¿qué tan bien predice este modelo un valor futuro?"; el curso 7 pregunta "¿puedo afirmar que X causa Y a partir de este modelo, y bajo qué condiciones (aleatorización, ausencia de confusión) sería válido hacerlo?". Un tema ambiguo —regularización (Lasso/Ridge)— pertenece al curso 6 (mejora predictiva), mientras que el ajuste por variables de confusión en un estudio observacional pertenece al curso 7, aun cuando ambos usen manipulaciones algebraicas similares sobre la matriz de diseño.

**7 → 8.** La inferencia causal cierra con un criterio: "no todo patrón hallado en los datos, ni todo modelo bien ajustado, respalda una intervención". El curso 8 retoma el modelado predictivo (ahora no supervisado y profundo) sin reabrir la pregunta causal, aunque advierte —como recordatorio, no como contenido nuevo— que los clusters o las representaciones aprendidas no deben interpretarse causalmente sin el aparato del curso 7.

**8 → 9.** El curso 8 entrega estimaciones, agrupamientos, representaciones y pronósticos; el curso 9 los toma como *insumos* de un problema de decisión (parámetros, restricciones, escenarios), pero no vuelve a estimarlos. Un tema ambiguo —la elección entre varios modelos predictivos según su "valor de negocio" esperado— pertenece al curso 9, porque introduce una función de valor/decisión que no forma parte del criterio puramente estadístico del curso 8.

**9 → 10.** El curso 9 entrega una recomendación de decisión (una política, una asignación, un diseño óptimo bajo los supuestos modelados); el curso 10 pregunta si esa recomendación puede convertirse en un sistema que opera de forma confiable en producción. La frontera: el curso 9 no discute contenerización, monitoreo ni arquitectura de despliegue; el curso 10 no vuelve a discutir la formulación matemática de la decisión, solo la consume como una caja que debe operar de forma robusta y observable.

**10 → 11.** El curso 10 entrega un sistema desplegado, monitoreado y mantenible desde una perspectiva técnica; el curso 11 pregunta si ese sistema es usable, adoptado y bien integrado organizacionalmente. Un tema ambiguo —el diseño de la interfaz de un dashboard operacional de monitoreo de modelos— se resuelve a favor del curso 10 si su propósito es técnico (alertas de deriva del modelo), y a favor del curso 11 si su propósito es la interacción humano-máquina con el usuario final de la decisión.

**11 → 12.** El curso 11 diseña la solución completa (técnica + producto); el curso 12 la audita bajo un lente de responsabilidad. La frontera: cuestiones de sesgo algorítmico y privacidad que surgen naturalmente durante el diseño (curso 11) se señalan pero no se resuelven allí en profundidad; se convierten en objeto de análisis sistemático en el curso 12. Esta es la frontera más deliberadamente porosa del diseño (ver Sección 6): se espera que ambos cursos toquen estos temas, con distinto nivel de profundidad.

**12 → 13.** El curso 12 entrega un criterio de responsabilidad profesional aplicable a cualquier solución; el Capstone lo aplica en tiempo real a un proyecto con patrocinador real, junto con todas las demás competencias. No hay contenido nuevo en la frontera; el Capstone es integración, no adición.

# 6. Competencias transversales

Las siguientes competencias no pertenecen a un curso único; se refuerzan de manera creciente a lo largo de la cadena, con puntos de mayor intensidad señalados entre paréntesis.

- **Comunicación y narrativa de evidencia.** Presente desde el curso 1 (framing) y el curso 4 (visualización), pero exigida en cada curso posterior como parte de la entrega de cualquier proyecto (intensidad máxima: cursos 4 y 13).
- **Formulación y reformulación de problemas.** No se agota en el curso 1; cada curso técnico (6 a 11) exige retomar la pregunta original y verificar que el método elegido siga siendo pertinente (intensidad máxima: cursos 1 y 13).
- **Reproducibilidad y prácticas de ingeniería de software.** Control de versiones, documentación de supuestos, estructuración de código como proyecto mantenible; se introduce en el curso 2 y se exige como estándar de entrega en todos los cursos con componente de proyecto (intensidad máxima: cursos 5, 10 y 13).
- **Cuantificación y comunicación de la incertidumbre.** No es exclusiva del curso 3; se exige al reportar cualquier modelo predictivo, causal o prescriptivo (intensidad máxima: cursos 3, 7 y 9).
- **Ética, privacidad, seguridad y responsabilidad en IA.** Esta es la competencia transversal más deliberadamente duplicada del diseño, siguiendo la recomendación explícita de National Academies de que la ética esté "tejida desde el principio" y la evidencia de Berkeley C102 de que la privacidad puede fusionarse directamente en un curso técnico de inferencia. Se introduce como sensibilización en el curso 1, se instancia técnicamente dentro de los cursos 5 (gobernanza de datos), 6/8 (sesgo algorítmico en modelos), 7 (uso ético de inferencias causales) y 11 (diseño responsable de la interacción), y se consolida de forma sistemática e integradora en el curso 12. No se considera un defecto de diseño que el tema aparezca varias veces: se considera una condición de eficacia (ver Sección 10).
- **Gobernanza de datos.** Introducida en el curso 5 pero retomada como objeto de auditoría en el curso 12.
- **Experimentación y pensamiento causal.** Concentrada en el curso 7, pero su disciplina ("¿esto es correlación o causalidad?") debe aplicarse como hábito crítico en los cursos 8, 9 y 13.
- **Comunicación ejecutiva y gestión de patrocinadores.** Introducida conceptualmente en el curso 1 (el "acuerdo del patrocinador" de INFORMS), practicada de forma aplicada en el curso 9 (justificar una recomendación de decisión) y en el curso 11 (justificar una decisión de diseño de producto), y ejercida en su forma completa en el Capstone.
- **Trabajo en equipos multidisciplinarios.** Implícita en todos los proyectos grupales, explícita en el Capstone, donde se espera que los roles de ingeniería de datos, modelado y comunicación con el patrocinador se distribuyan y coordinen.

# 7. Mapa de contenidos

I = Introducido, D = Desarrollado, M = Dominado/Integrado, — = No es foco.

| Competencia / Tema | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Formulación de problemas de decisión | I | — | — | — | — | D | — | D | D | — | — | — | M |
| Programación y estructuras de datos | I | M | D | D | D | D | D | D | D | D | — | — | D |
| Bases de datos (SQL/NoSQL) | — | I | — | D | M | — | — | — | — | D | — | — | D |
| Ingeniería de datos, calidad y gobernanza | — | I | — | — | M | D | — | — | — | D | — | D | D |
| Arquitectura y escalabilidad | — | — | — | — | D | — | — | — | — | M | I | — | D |
| Probabilidad e inferencia estadística | — | — | M | I | D | D | D | D | D | — | — | — | D |
| Diseño experimental (A/B, RCT) | I | — | D | — | — | — | M | — | — | — | — | — | D |
| Análisis exploratorio y visualización | — | I | D | M | D | D | — | D | D | D | D | — | D |
| Comunicación de evidencia / storytelling | I | — | D | M | D | D | D | D | D | D | D | D | M |
| Aprendizaje supervisado (regresión/clasificación) | — | I | D | — | — | M | D | D | D | D | — | — | D |
| Aprendizaje no supervisado / representación | — | — | — | — | — | I | — | M | D | — | D | — | D |
| Series de tiempo | — | — | — | — | — | I | — | M | D | — | — | — | D |
| Aprendizaje profundo | — | — | — | — | — | — | — | M | I | D | I | — | D |
| Inferencia causal y variables de confusión | — | — | I | — | — | I | M | D | D | — | — | D | D |
| Optimización | — | — | — | — | — | I | — | I | M | — | — | — | D |
| Simulación y análisis de sensibilidad | — | — | I | — | — | — | — | I | M | — | — | — | D |
| Decisión bajo incertidumbre / sesgos de decisión | I | — | I | — | — | — | — | — | M | — | D | — | D |
| Despliegue y MLOps | — | — | — | — | I | — | — | — | I | M | D | — | D |
| Monitoreo y ciclo de vida en producción | — | — | — | — | I | — | — | — | — | M | D | D | D |
| Diseño de producto / HCI / automatización | I | — | — | — | — | — | — | — | — | I | M | D | D |
| Ética, sesgo algorítmico, responsabilidad en IA | I | — | — | — | I | I | D | I | — | — | D | M | D |
| Privacidad, seguridad y gobernanza | I | — | — | — | D | — | I | — | — | I | — | M | D |
| Trabajo reproducible y prácticas de software | — | I | D | D | D | D | D | D | D | D | D | — | M |
| Comunicación ejecutiva y gestión de patrocinador | I | — | — | — | — | — | — | — | D | — | D | — | M |

La progresión visible en el mapa confirma dos decisiones de diseño: (a) la ética/gobernanza aparece de forma distribuida (I repetido en varios cursos) antes de consolidarse (M) en el curso 12, en lugar de aparecer una sola vez; (b) casi ninguna fila tiene más de una "M", lo que indica que se evitó la duplicación de dominio pleno entre cursos —cada competencia se domina en un único lugar de la cadena, aunque se practique en varios.

# 8. Qué queda deliberadamente fuera

- **Teoría matemática completa de Investigación de Operaciones** (dualidad, teoría de colas, procesos estocásticos avanzados, programación entera a profundidad). El corpus deja claro que existe una versión "ligera" de optimización orientada a la decisión (MIT Quantitative Methods, módulo de optimización del certificado MIT Data Science and Analytics) que es suficiente para un profesional de analítica; la profundidad matemática completa se deja como especialización electiva, siguiendo la instrucción explícita de no equiparar lo prescriptivo con toda la IO.
- **Administración y certificación de infraestructura en la nube a nivel de proveedor específico** (Kubernetes en profundidad operativa, certificaciones AWS/Azure/GCP). El curso 10 enseña los principios (contenerización, arquitectura nativa de la nube, métricas DevOps) evidenciados en MIT Cloud & DevOps, pero la profundidad de administración de un proveedor específico se dirige a un elective/certificación complementaria, no al núcleo, porque es conocimiento que caduca rápido y no es transferible entre proveedores.
- **Prototipado físico y metodologías de manufactura** (evidenciado en MIT Rapid Prototyping Methodologies). Este contenido pertenece al diseño de producto físico/manufactura, no a productos de datos; se excluye del núcleo por completo. Se reconoce como un dominio de aplicación válido (analítica aplicada a manufactura) pero no como parte de la columna vertebral.
- **Estrategia de plataformas digitales y economía de mercados de dos lados como curso de negocio completo** (evidenciado en MIT Digital Platforms). Los conceptos de efectos de red y diseño de API se incorporan de forma acotada dentro del curso 11 (Productos y Sistemas Analíticos) cuando la solución tiene lógica de ecosistema, pero el aparato completo de estrategia de plataformas (regulación antimonopolio, "cuestiones de los cinco preguntas") es más propio de una escuela de negocios que de un currículo de Analítica.
- **Un curso dedicado de "Liderazgo de Datos" para audiencias ejecutivas no técnicas** (evidenciado en MIT Data Leadership, Cambridge Business Analytics y el "Master Class" de PwC). Estos documentos están diseñados para consumidores de analítica, no para quienes la producen; su contenido (sin código, orientado a decisión ejecutiva) se considera un programa distinto (posiblemente un certificado ejecutivo complementario), no parte del núcleo de formación de un analista/científico de datos.
- **Fundamentos matemáticos completos como cursos de este currículo** (cálculo, álgebra lineal formal, teoría de la medida, estructuras discretas). Siguiendo la misma decisión que toma la ACM (dejar estos temas a los departamentos de matemáticas), se tratan como prerrequisitos institucionales externos, no como cursos de la cadena de Analítica.
- **Ciencias de la computación teórica profunda** (arquitectura de computadores, sistemas operativos, teoría de compiladores — evidenciado en la KA "Computing and Computer Fundamentals" de ACM). Solo se retienen los elementos estrictamente necesarios para la ingeniería de datos (curso 5); una formación completa en estas áreas corresponde a un programa de Ciencias de la Computación, no de Analítica.
- **Especialización vertical por dominio de aplicación** (finanzas, salud, mercadeo, manufactura, sector público). Siguiendo la recomendación explícita de National Academies de anclar la analítica a un dominio mediante cursos "conectores", electivas o un menor/co-major, estas especializaciones se dejan fuera del núcleo y se ofrecen como electivas o como el contexto del proyecto del Capstone.
- **Investigación de frontera en arquitecturas de aprendizaje profundo** (diseño de arquitecturas transformer, GANs a nivel de investigación). El curso 8 cubre el uso aplicado de aprendizaje profundo; la investigación de arquitecturas de vanguardia se considera contenido de posgrado/electivo avanzado.
- **Adopción de un stack tecnológico específico como columna vertebral curricular** (el extenso listado de herramientas del certificado de Ingeniería de Datos de MIT: Kafka, Airflow, Debezium, ThingsBoard, etc.). Se reconoce su valor de empleabilidad inmediata, pero se decide explícitamente no organizar el currículo alrededor de herramientas nombradas —estas se instancian como laboratorios dentro de los cursos 5 y 10, sustituibles sin rediseñar el curso.

# 9. Evidencia documental

**Curso 1 — Fundamentos de Analítica y Formulación de Problemas de Decisión.**
- `informs-analytics-framework-2024.pdf`: aporta el marco de los siete dominios usado como mapa mental organizador de todo el currículo.
- `cambridge-business-analytics.pdf`: aporta el módulo inicial de sesgos de decisión y la taxonomía descriptivo/predictivo/prescriptivo como punto de entrada antes de cualquier contenido técnico.
- `national-academies-data-science-for-undergraduates-2018.pdf`: aporta el concepto de "acumen de datos" y la exigencia de introducir la ética desde el primer curso.
- `acm-computing-competencies-undergraduate-data-science-2021.pdf`: aporta el concepto de "disposiciones profesionales" no técnicas como parte de la identidad del analista.

**Curso 2 — Programación y Manejo de Datos.**
- `acm-computing-competencies-undergraduate-data-science-2021.pdf`: aporta las áreas de conocimiento de programación, estructuras de datos y fundamentos de cómputo.
- `usc-introduction-to-data-analytics.pdf`: aporta el tratamiento de modelado de datos y SQL como punto de entrada técnico.
- `mit-professional-certificate-data-engineering.pdf`: aporta los módulos introductorios de Python/NumPy/Pandas como referencia de habilidades computacionales de entrada.

**Curso 3 — Estadística e Inferencia para la Analítica.**
- `berkeley-data-c102-data-inference-and-decisions.pdf`: aporta la estructura frecuentista/bayesiana, pruebas de hipótesis y estimación como núcleo del curso.
- `warwick-foundations-of-data-analytics.pdf`: aporta el bloque de probabilidad y estadística de un módulo de posgrado denso, usado como referencia de profundidad.
- `mit-data-science-and-machine-learning.pdf`: aporta el módulo "Statistics for Data Science" y el tratamiento de pruebas de hipótesis (caso Challenger).
- `national-academies-data-science-for-undergraduates-2018.pdf`: aporta la definición del área de "fundamentos estadísticos" como concepto nuclear de acumen de datos.

**Curso 4 — Analítica Descriptiva y Comunicación de Evidencia.**
- `usc-introduction-to-data-analytics.pdf`: aporta el bloque de visualización y tableros interactivos.
- `national-academies-data-science-for-undergraduates-2018.pdf`: aporta el área de "descripción y visualización de datos" como concepto nuclear.
- `cambridge-business-analytics.pdf`: aporta el módulo de análisis descriptivo con foco en minería de datos y estadística descriptiva para audiencias de negocio.
- `acm-computing-competencies-undergraduate-data-science-2021.pdf`: aporta la KA de "Análisis y Presentación" (visualización, HCI, diseño centrado en el usuario).

**Curso 5 — Ingeniería de Datos para la Analítica.**
- `berkeley-data-c101-data-engineering.pdf`: evidencia central; aporta la definición de "operacionalización confiable y escalable" como identidad propia de la ingeniería de datos, distinta del análisis.
- `mit-professional-certificate-data-engineering.pdf`: aporta el contenido de arquitecturas de bases de datos, ETL/CDC y plataformas de datos a gran escala.
- `acm-computing-competencies-undergraduate-data-science-2021.pdf`: aporta las KAs de "Sistemas de Big Data" y "Gobernanza, Adquisición y Gestión de Datos".
- `informs-analytics-framework-2024.pdf` e `informs-cap-essentials-blueprint.pdf`: aportan el Dominio III (Datos) y su definición de calidad, linaje y gobernanza como competencias evaluables.

**Curso 6 — Analítica Predictiva I: Aprendizaje Supervisado.**
- `mit-data-science-and-machine-learning.pdf`: evidencia más rica; aporta la secuencia de regresión lineal/logística, árboles, boosting y evaluación de modelos.
- `mit-professional-certificate-data-science-and-analytics.pdf`: aporta los módulos de regresión lineal/logística, CART y ensamblado.
- `warwick-foundations-of-data-analytics.pdf`: aporta el bloque de regresión y clasificación de un currículo de posgrado compacto.
- `pwc-data-and-analytics-academy.pdf`: aporta evidencia de la secuencia comercial típica (regresión → modelos lineales generalizados → aprendizaje automático) usada en formación profesional.

**Curso 7 — Inferencia Causal y Diseño de Experimentos.**
- `berkeley-data-c102-data-inference-and-decisions.pdf`: aporta la inclusión explícita de inferencia causal en la descripción oficial del curso.
- `mit-data-science-and-machine-learning.pdf`: aporta el módulo dedicado a regresión causal, ensayos aleatorizados controlados y estudios observacionales con variables de confusión.
- `mit-professional-certificate-data-science-and-analytics.pdf`: aporta el módulo de "Interpretabilidad y Causalidad en Modelos".
- `cambridge-business-analytics.pdf`: aporta el módulo de experimentación como "estándar de oro" de la evidencia causal en contextos de negocio.

**Curso 8 — Analítica Predictiva II: No Supervisado, Series de Tiempo y Aprendizaje Profundo.**
- `mit-data-science-and-machine-learning.pdf`: aporta los módulos de clustering, PCA/reducción de dimensionalidad, sistemas de recomendación, redes y modelos gráficos.
- `mit-professional-certificate-data-science-and-analytics.pdf`: aporta los módulos de redes neuronales, transferencia de aprendizaje y procesamiento de lenguaje natural.
- `warwick-foundations-of-data-analytics.pdf`: aporta el bloque de clustering, clasificación y análisis matricial (SVD/PCA).
- `mit-machine-learning-modeling-and-simulation-principles.pdf`: aporta el tratamiento del aprendizaje automático como extensión de métodos numéricos y de optimización clásicos.

**Curso 9 — Analítica Prescriptiva: Optimización, Simulación y Decisión bajo Incertidumbre.**
- `mit-quantitative-methods-in-systems-engineering.pdf`: evidencia central; aporta el modelo de exploración de tradespace, pensamiento orientado a valor y análisis de sensibilidad/robustez.
- `cambridge-business-analytics.pdf`: aporta los módulos de analítica prescriptiva y los sesgos de comportamiento relevantes para la decisión (aversión al riesgo, costos hundidos).
- `mit-professional-certificate-data-science-and-analytics.pdf`: aporta el bloque de "Fundamentos de Optimización" (modelos de optimización lineal, filtrado colaborativo).
- `informs-analytics-framework-2024.pdf`: aporta la taxonomía formal descriptivo/predictivo/prescriptivo del Dominio II que ancla conceptualmente el curso.

**Curso 10 — Despliegue y Ciclo de Vida de Soluciones Analíticas.**
- `informs-analytics-framework-2024.pdf`, `informs-cap-essentials-blueprint.pdf` e `informs-cap-pro-blueprint.pdf`: evidencia central; aportan los Dominios VI (Despliegue) y VII (Gestión del Ciclo de Vida) con sus tareas específicas y ponderaciones de examen.
- `mit-cloud-and-devops.pdf`: aporta el contenido técnico de contenerización, métricas DevOps, arquitecturas *serverless* y *cloud native*.
- `berkeley-data-c101-data-engineering.pdf`: aporta la idea de "operacionalización confiable y escalable" como puente entre ingeniería de datos y despliegue.

**Curso 11 — Productos y Sistemas Analíticos.**
- `mit-designing-and-building-ai-products-and-services.pdf`: evidencia central; aporta el proceso de diseño de producto de IA, el diseño de interacción humano-máquina y el concepto de "supermentes" (colaboración humano-IA).
- `mit-digital-platforms.pdf`: aporta la lógica de plataforma/ecosistema y efectos de red para soluciones que conectan múltiples partes interesadas.
- `mit-data-leadership.pdf`: aporta el concepto de plataformas de datos y "fábricas de IA" como infraestructura organizacional del producto analítico.

**Curso 12 — Gobernanza, Ética y Responsabilidad en Analítica e IA.**
- `national-academies-data-science-for-undergraduates-2018.pdf`: evidencia central; aporta el tratamiento de la ética como competencia de primer orden, el "Juramento de Ciencia de Datos" y el uso de casos de fracaso (Google Flu Trends, vigilancia predictiva sesgada) como material pedagógico.
- `acm-computing-competencies-undergraduate-data-science-2021.pdf`: aporta las KAs de Profesionalismo y de Privacidad/Seguridad, junto con el capítulo de accesibilidad y ampliación de la participación.
- `informs-cap-pro-blueprint.pdf`: aporta el énfasis explícito en "impacto en la sociedad" y ética en el reporte de resultados, ausente en el nivel de entrada (CAP-Essentials).
- `berkeley-data-c102-data-inference-and-decisions.pdf`: aporta la evidencia de que la privacidad diferencial puede tratarse como contenido técnico de un curso de inferencia.
- `warwick-foundations-of-data-analytics.pdf`: aporta el bloque dedicado de anonimización, k-anonimato y privacidad diferencial.
- `mit-data-leadership.pdf`: aporta las sesiones dedicadas a sesgo y equidad en IA y gobernanza de datos.

**Curso 13 — Capstone: Proyecto Integrador de Analítica.**
- `informs-analytics-framework-2024.pdf`: aporta el modelo cíclico de siete dominios como estructura organizadora del proyecto integrador.
- `national-academies-data-science-for-undergraduates-2018.pdf`: aporta la recomendación de anclar el proyecto final a un dominio de aplicación real.
- `mit-designing-and-building-ai-products-and-services.pdf`: aporta el modelo de propuesta de diseño como formato de entrega final.
- `mit-professional-certificate-data-science-and-analytics.pdf` y `mit-professional-certificate-data-engineering.pdf`: aportan el formato de proyecto de portafolio acumulativo como referencia de evaluación final.

*Nota:* `mit-rapid-prototyping-methodologies.pdf` no se usó como evidencia de diseño de ningún curso del núcleo; su contenido (prototipado físico/manufactura) se consideró explícitamente en la Sección 8 como fuera del alcance de un currículo de Analítica.

# 10. Riesgos y decisiones discutibles

**1. Ausencia de un curso dedicado de "Liderazgo y Comunicación Organizacional de Datos".** Tres fuentes completas del corpus (MIT Data Leadership, Cambridge Business Analytics, PwC Academy con su Master Class) dedican programas enteros a esta competencia para audiencias no técnicas. La alternativa más fuerte: crear un curso propio, posiblemente en el Nivel IV, que profundice en gestión del cambio organizacional, negociación con patrocinadores y comunicación ejecutiva más allá de lo que un tratamiento transversal puede lograr. Se descartó porque el público objetivo de este currículo son productores, no consumidores, de analítica, pero un diseñador que priorice la empleabilidad en roles híbridos analista-gerente podría preferir un curso dedicado.

**2. Dos cursos de Analítica Predictiva con Inferencia Causal intercalada entre ambos, en lugar de un único curso de "Modelado Predictivo" con un módulo de causalidad.** La decisión actual multiplica la superficie curricular (tres cursos en vez de uno o dos) para una distinción que en varias fuentes (PwC, Cambridge) se trata como un módulo, no como un curso. La alternativa más fuerte: comprimir en dos cursos (Predictivo unificado + Causal como módulo dentro de él), liberando un espacio de crédito para, por ejemplo, el curso de liderazgo mencionado arriba. Se prefirió la separación porque la evidencia de mayor rigor (Berkeley C102 como curso institucional propio, MIT IDSS con semanas consecutivas dedicadas) sugiere que comprimir esta distinción arriesga precisamente el error que más se busca evitar: que los estudiantes traten un modelo predictivo bien ajustado como si autorizara una afirmación causal.

**3. Posición de la Ingeniería de Datos (curso 5) después de la Analítica Descriptiva (curso 4) y no inmediatamente después de Programación (curso 2).** La alternativa más fuerte: mover la ingeniería de datos justo después del curso 2, tratándola como la base de infraestructura que debería preceder a cualquier análisis, tal como lo sugiere la lógica de "primero la tubería, después el análisis" de varias fuentes profesionales (PwC, MIT Data Engineering). Se prefirió el orden actual porque permite que los estudiantes primero desarrollen intuición analítica sobre datos pequeños y limpios (siguiendo el patrón pedagógico de introducción de Berkeley/Data 8) antes de enfrentar la complejidad de datos grandes y sucios en escala.

**4. Tratar la Analítica Prescriptiva como un único curso que combina optimización, simulación y análisis de decisión, en lugar de separarlos.** La alternativa más fuerte, defendida por quienes ven la Investigación de Operaciones como una disciplina propia con suficiente profundidad matemática para justificar dos o tres cursos (optimización determinística, simulación estocástica, análisis de decisión bajo incertidumbre por separado). Se prefirió la compresión siguiendo la instrucción explícita de no equiparar lo prescriptivo con toda la IO, dejando la profundidad matemática completa como especialización electiva.

**5. Separar Despliegue (curso 10) de Productos y Sistemas Analíticos (curso 11) en dos cursos distintos.** La alternativa más fuerte: fusionarlos en un único curso de "Productización", ya que en la práctica profesional ambas actividades suelen ejecutarse por el mismo equipo y de forma entrelazada. Se prefirió la separación porque la evidencia (INFORMS Dominio VI centrado en validación técnica/de negocio vs. MIT AI Products centrado en diseño de interacción humano-máquina y colaboración humano-IA) muestra que son preguntas de naturaleza distinta ("¿funciona de forma confiable?" vs. "¿es adoptado y usable?"), y fusionarlas arriesga que la segunda pregunta quede subordinada a la primera, como ocurre quie en varios programas de ingeniería que tratan el producto como un detalle posterior al despliegue técnico.

**6. Un curso dedicado de Gobernanza/Ética (curso 12) además del tratamiento transversal, en lugar de solo tratamiento transversal.** La alternativa más fuerte, defendida por quienes siguen al pie de la letra la recomendación de National Academies de que la ética esté "tejida a través de todo el currículo" (lo cual podría leerse como una advertencia contra crear un curso separado, por el riesgo de que los demás cursos entonces "deleguen" la responsabilidad ética a ese curso y dejen de tratarla). Se prefirió incluir ambos porque la evidencia muestra que un tratamiento puramente distribuido, sin un punto de consolidación, corre el riesgo inverso: que ningún curso individual tenga el tiempo o el mandato de tratar con la profundidad necesaria temas como la privacidad diferencial formal o el diseño de un marco de gobernanza organizacional completo.

**7. Diseño de un Capstone único al final en lugar de proyectos integradores distribuidos en varios puntos de la cadena.** La alternativa más fuerte, sugerida indirectamente por el carácter cíclico (no lineal) del propio marco INFORMS: si el ciclo completo de siete dominios se practica solo una vez, al final, se pierde la oportunidad de que los estudiantes experimenten la naturaleza iterativa y recurrente del proceso real. Un diseño alternativo defendible incluiría "miniciclos" integradores después de los niveles II y III, no solo al final. Se prefirió el Capstone único por simplicidad de secuenciación, pero se reconoce que esto privilegia la integración final sobre la práctica iterativa temprana.

**8. Excluir del núcleo la profundidad matemática de sistemas a gran escala** (estructuras de datos para streams, *sketches*, filtros de Bloom, evidenciados en Warwick) **y confinarla a un módulo dentro del curso 5.** La alternativa más fuerte: crear un curso propio de "Sistemas de Datos a Gran Escala" para programas con mayor orientación a ciencias de la computación. Se prefirió la compresión porque el resto del corpus (fuera de Warwick) no sostiene esta profundidad como núcleo de un currículo de Analítica —parece más propia de un currículo de Ciencias de la Computación con especialización en sistemas de datos.

# 11. Arquitectura final resumida

```
NIVEL I — Fundamentos
  [1] Fundamentos de Analítica y Formulación de Problemas de Decisión
        │
        ▼
  [2] Programación y Manejo de Datos
        │
        ├──────────────┐
        ▼              ▼
NIVEL II — Núcleo técnico
  [3] Estadística      [4] Analítica Descriptiva
      e Inferencia          y Comunicación de Evidencia
        │              │
        └──────┬───────┘
               ▼
        [5] Ingeniería de Datos para la Analítica
               │
               ▼
        [6] Analítica Predictiva I
            (Aprendizaje Supervisado)
               │
               ▼
NIVEL III — Razonamiento avanzado
        [7] Inferencia Causal y Diseño de Experimentos
               │
               ▼
        [8] Analítica Predictiva II
            (No Supervisado, Series de Tiempo, Aprendizaje Profundo)
               │
               ▼
        [9] Analítica Prescriptiva
            (Optimización, Simulación, Decisión bajo Incertidumbre)
               │
               ▼
NIVEL IV — Operacionalización y producto
        [10] Despliegue y Ciclo de Vida de Soluciones Analíticas
               │
               ▼
        [11] Productos y Sistemas Analíticos
               │
               ▼
        [12] Gobernanza, Ética y Responsabilidad en Analítica e IA
               │
               ▼
        [13] CAPSTONE: Proyecto Integrador de Analítica
             (ciclo completo de los 7 dominios, con patrocinador real)
```

**Hilo transversal** (presente en todos los niveles, no confinado a un curso):
`Ética · Privacidad · Gobernanza · Comunicación · Reproducibilidad · Formulación de problemas`

**Lectura del diagrama:** la cadena es predominantemente lineal a partir del curso 5, con una única bifurcación/reconvergencia temprana (cursos 3–4) que refleja la única relación verdaderamente paralela (no secuencial) del diseño. La ausencia de bifurcaciones posteriores es deliberada: refleja la decisión de tratar cada competencia de la Sección 2 como parte de una única columna vertebral compartida por todo estudiante del programa, dejando la especialización (dominio de aplicación, profundidad en optimización, profundidad en sistemas a escala) para el espacio electivo que queda fuera de esta arquitectura de núcleo.
