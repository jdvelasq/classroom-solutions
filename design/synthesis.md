# 1. Comparación global de las tres propuestas

Las tres propuestas —ChatGPT (9 cursos), Claude (14 cursos) y Gemini (6 cursos)— convergen en una misma concepción profunda de Analítica: **una disciplina de ciclo completo para la decisión basada en evidencia, que no equivale a Machine Learning, que exige ingeniería de datos propia, que distingue predicción/inferencia/causalidad/decisión, y que ahora —por la incorporación de los diez documentos DataOps— exige una disciplina explícita de entrega ágil, lean y organizacional para no fracasar en producción**. Ninguna de las tres reduce la Analítica a algoritmos, a infraestructura o a tableros. Esta es una convergencia genuina, no terminológica: las tres derivan la misma arquitectura conceptual profunda (problema → datos → evidencia → modelo → decisión → producto → operación → valor) a partir de lecturas independientes del mismo corpus.

Donde las tres propuestas divergen radicalmente es en la **granularidad de la traducción de esa concepción común en cursos**. ChatGPT y Gemini comparten una filosofía de consolidación explícita: ambas argumentan textualmente contra la fragmentación excesiva (ChatGPT: "la amplitud del corpus obliga a priorizar dominio sobre cobertura superficial"; Gemini: "evita tanto el aislamiento de temas como la sobrecarga superficial"), y ambas producen arquitecturas compactas (9 y 6 cursos respectivamente) donde varias competencias que Claude trata como cursos independientes —estrategia de datos, analítica descriptiva, gobernanza/ética— se funden dentro de cursos más amplios. Claude, en cambio, prioriza la separación explícita de cada competencia bien evidenciada en un curso propio, resultando en 14 cursos.

Esta diferencia de granularidad no es meramente estilística: tiene consecuencias conceptuales reales. Por ejemplo, Gemini funde **inferencia estadística, causalidad y aprendizaje predictivo en un solo curso** (su Curso 3), argumentando explícitamente que separarlas en cursos desconectados fragmentaría un razonamiento que debe aprenderse como un continuo. ChatGPT y Claude, en cambio, separan causalidad de predicción en cursos distintos. Aquí la similitud superficial ("los tres distinguen predicción de causalidad") oculta una divergencia real sobre **dónde debe vivir esa distinción**: como frontera entre dos cursos, o como un pivote pedagógico dentro de un mismo curso. De manera simétrica, dos proposiciones que usan nombres de curso casi idénticos —"Analítica Prescriptiva" en las tres— sí representan la misma frontera curricular en los tres casos (optimización + simulación + decisión, sin equipararlo a Investigación de Operaciones completa): aquí la convergencia de nombre sí refleja convergencia conceptual real.

# 2. Convergencias sólidas

**(a) La Analítica Prescriptiva es un curso único que integra optimización, simulación y teoría de decisión, sin equipararse a Investigación de Operaciones completa.** Las tres propuestas coinciden exactamente en esta frontera y en esta exclusión. Está respaldada por `mit-quantitative-methods-in-systems-engineering.pdf` (tradespace, pensamiento de valor, sensibilidad), `mit-machine-learning-modeling-and-simulation-principles.pdf` (simulación estocástica) y la taxonomía descriptivo/predictivo/prescriptivo de `informs-analytics-framework-2024.pdf`, ninguno de los cuales exige profundidad matemática de teoría de colas o dualidad para ejercer esta competencia.

**(b) La Ingeniería de Datos merece un curso propio y temprano, distinto de la analítica descriptiva y del despliegue.** Las tres construyen un curso dedicado (ChatGPT C3, Claude C6, Gemini C2) apoyado en `berkeley-data-c101-data-engineering.pdf` ("operacionalización confiable y escalable"), `mit-professional-certificate-data-engineering.pdf` y, de forma nueva, `dataops-08-data-scientids.pdf` (arquitectura canónica vs. arquitectura DataOps, diseño de lagos/bodegas/mercados de datos). El corpus no deja espacio para tratar esto como una sección menor de otro curso.

**(c) DataOps constituye una competencia de curso completo, no una sección del curso de despliegue clásico.** Las tres reservan un curso final o cuasi-final íntegramente dedicado a Lean/Agile/DevOps aplicados a analítica, apoyado en `dataops-04-lean-thinking.pdf`, `dataops-05-agile.pdf`, `dataops-06-definition.pdf` y `dataops-09-data-quality.pdf`. Este es el cambio estructural más importante que la incorporación del corpus DataOps produjo en las tres propuestas simultáneamente, y es la convergencia más fuerte de todo el ejercicio: ningún diseñador consideró que el contenido de despliegue previo (solo Dominios VI-VII de INFORMS + un curso de MIT sobre nube) bastaba para representar lo que el corpus nuevo evidencia.

**(d) Un "producto analítico" no es un tablero.** Las tres exigen tratamiento explícito de diseño de producto (interacción humano-máquina, hipótesis de épica, MVP, empaquetamiento en servicios/APIs), apoyadas en `mit-designing-and-building-ai-products-and-services.pdf` y en la definición de producto de datos de `dataops-06-definition.pdf` ("combina datos con algoritmos... es rápido, escalable, repetible, reproducible, de uso continuo y monitoreo constante").

**(e) La distinción predicción/inferencia causal/decisión debe enseñarse explícitamente, no darse por sentada.** Las tres, sin excepción, identifican esta distinción como un riesgo pedagógico central (el "modelo con 92% de precisión no es la solución"), apoyadas en `berkeley-data-c102-data-inference-and-decisions.pdf` y `mit-data-science-and-machine-learning.pdf`. Divergen en dónde vive esa distinción (ver Sección 3), pero no en que deba enseñarse con rigor propio.

**(f) La ética, la privacidad y el sesgo algorítmico no pueden confinarse a una sola clase aislada.** Las tres, incluyendo la que sí crea un curso dedicado (Claude), insisten en que la responsabilidad debe ser transversal desde el primer curso. Esto está anclado en la recomendación explícita de `national-academies-data-science-for-undergraduates-2018.pdf` ("ética tejida desde el principio y a lo largo del currículo") y en el tratamiento de "Gobernanza y Ética" como dimensión transversal (no como fase aislada) en `dataops-03-methodologies.pdf`.

**(g) Ningún dominio de aplicación vertical, ninguna certificación de herramienta propietaria y ninguna profundidad matemática completa de Investigación de Operaciones pertenecen al núcleo.** Las tres coinciden en dejar esto como electivo, apoyadas en la recomendación explícita de National Academies sobre anclaje de dominio vía electivas y en la naturaleza vendor-neutral de los marcos INFORMS y ACM.

# 3. Divergencias curriculares principales

**Divergencia 1 — Número total de cursos.**
- ChatGPT: 9 cursos.
- Claude: 14 cursos.
- Gemini: 6 cursos.
- **Pregunta curricular subyacente:** ¿cuál es el nivel de granularidad que maximiza coherencia sin fragmentar artificialmente competencias que pueden convivir en un mismo curso, ni comprimir competencias que requieren tratamiento propio?

**Divergencia 2 — Ubicación de la Estrategia de Datos (`dataops-02`).**
- ChatGPT: no crea un curso ni un módulo explícito de estrategia; usa `dataops-02` como evidencia de su curso de "Ingeniería y gobierno de datos analíticos" (C3).
- Claude: crea un curso propio y temprano, "Estrategia de Datos y Analítica" (curso 2).
- Gemini: funde la estrategia dentro de su curso 1 ("Encuadre Estratégico y Analítica Descriptiva"), junto con EDA y comunicación.
- **Pregunta subyacente:** ¿la estrategia organizacional de datos es una competencia de ingeniería, una competencia de encuadre inicial, o una competencia de nivel de curso propio?

**Divergencia 3 — Ubicación de la Analítica Descriptiva.**
- ChatGPT: fusionada en el curso de entrada (C1), junto con formulación de problemas.
- Claude: curso propio (curso 5), después de programación y en paralelo con estadística — es decir, más tarde en la secuencia.
- Gemini: fusionada en el curso de entrada (C1), junto con encuadre y estrategia.
- **Pregunta subyacente:** ¿el análisis exploratorio de datos es una competencia conceptual de entrada (se puede enseñar antes de programar) o una competencia técnica que requiere código y por tanto debe ubicarse después de la programación?

**Divergencia 4 — Predicción, inferencia estadística y causalidad: ¿cursos separados o un solo curso integrado?**
- ChatGPT: tres cursos distintos y secuenciales (C4 Inferencia, C5 Predictivo, C6 Causal).
- Claude: estadística separada (curso 4), luego predictivo (curso 7), luego causal (curso 8) intercalado antes de un segundo curso predictivo (curso 9).
- Gemini: un único curso (C3) que integra estadística, causalidad y aprendizaje predictivo (supervisado y no supervisado).
- **Pregunta subyacente:** ¿la distinción predicción/causalidad se enseña mejor como frontera administrativa entre cursos, o como un pivote pedagógico dentro de un mismo curso construido sobre el mismo vehículo técnico (regresión)?

**Divergencia 5 — Aprendizaje profundo, series de tiempo, sistemas de recomendación y redes: ¿núcleo obligatorio o electivo?**
- ChatGPT: explícitamente electivo ("no son obligatorios para toda la cadena: aprendizaje profundo y generativo, ... recomendadores, grafos, series de tiempo avanzadas... investigación de operaciones especializada").
- Claude: curso obligatorio propio (curso 9, "Analítica Predictiva II").
- Gemini: no le dedica un curso propio; los menciona brevemente y de forma no central dentro de su curso 3.
- **Pregunta subyacente:** ¿estos métodos avanzados son parte del núcleo irreducible de un profesional de Analítica, o son una especialización que debería dejarse fuera del tronco común?

**Divergencia 6 — Orden entre Productos de Datos y DataOps/Despliegue.**
- ChatGPT: Productos (C8) antes de Operación (C9).
- Claude: DataOps (curso 11) antes de Productos (curso 12) — orden invertido respecto a las otras dos.
- Gemini: Productos (C5, "Tubería de Innovación") antes de Operacionalización (C6, "Tubería de Valor").
- **Pregunta subyacente:** ¿se diseña primero el producto (hipótesis de valor, MVP, interfaz) y luego se industrializa, o se industrializa primero la entrega confiable y luego se empaqueta como producto?

**Divergencia 7 — Gobernanza/Ética: ¿curso dedicado o exclusivamente transversal?**
- ChatGPT: exclusivamente transversal, sin curso dedicado.
- Claude: curso dedicado (curso 13), además de tratamiento transversal.
- Gemini: exclusivamente transversal, con consolidación de "M" (dominio) concentrada en el curso final (C6).
- **Pregunta subyacente:** ¿la responsabilidad profesional requiere un espacio curricular propio para integrarse como sistema, o el riesgo de aislarla en un curso separado supera el beneficio de esa integración explícita?

**Divergencia 8 — Programación como curso propio vs. integrada en Ingeniería de Datos.**
- ChatGPT: curso propio y paralelo de entrada ("Computación reproducible para Analytics", C2).
- Claude: curso propio ("Programación y Manejo de Datos", curso 3).
- Gemini: no tiene curso propio; la programación se asume como prerrequisito de admisión y se practica dentro del curso de Ingeniería de Datos (C2).
- **Pregunta subyacente:** ¿la fluidez computacional general es una competencia de entrada que merece un curso propio, o basta con exigirla como prerrequisito y desarrollarla dentro del curso de datos?

**Divergencia 9 — ¿Existe un curso de Capstone separado del último curso técnico?**
- ChatGPT: no; su C9 (Operación y evolución) es el curso terminal e integrador, sin un curso adicional de capstone.
- Claude: sí, un curso 14 explícito de Capstone, posterior a Gobernanza.
- Gemini: no; su C6 (Operacionalización) es explícitamente el "curso culminante e integrador".
- **Pregunta subyacente:** ¿el proyecto integrador final merece un espacio curricular administrativamente separado, o basta con que el último curso técnico se diseñe como una práctica integradora con patrocinador?

# 4. Resolución de las divergencias mediante la evidencia

**Resolución 1 — Número de cursos.**
Evidencia relevante: ninguno de los documentos del corpus prescribe un número de cursos; sin embargo, la densidad y autocontención de cada bloque temático es observable directamente. `dataops-02-data-strategy.pdf` tiene la coherencia interna de un curso completo (marco propio de 12 pasos), pero también es cierto que ni ACM ni National Academies ni Berkeley proponen un curso dedicado solo a estrategia organizacional —lo tratan como parte del encuadre de negocio (Dominio I de INFORMS). Por otro lado, `berkeley-data-c102-data-inference-and-decisions.pdf` demuestra en su propia descripción oficial que inferencia, causalidad, decisión y una porción de aprendizaje automático (árboles, redes neuronales, ensambles) pueden convivir en **un solo curso universitario real**, lo que es evidencia directa contra la fragmentación de Claude en ese punto específico. **Decisión canónica:** un total de **9 cursos**, coincidiendo numéricamente con ChatGPT pero no en su composición interna (ver más abajo). Esta cifra emerge de aplicar consistentemente el principio "un curso por pregunta de naturaleza distinta, no por tema evidenciado", que documentado en el corpus solo sostiene 9 preguntas de naturaleza verdaderamente distinta (ver Sección 7).

**Resolución 2 — Estrategia de Datos.**
Evidencia: `dataops-02-data-strategy.pdf` es un documento sobre planeación organizacional (objetivos, brechas de capacidad, iniciativas, gobierno de decisión, caso de valor, portafolio, hoja de ruta) — no contiene una sola línea sobre modelado de datos, SQL, arquitectura o calidad técnica. Colocarlo como evidencia de un curso de "ingeniería y gobierno de datos" (como hace ChatGPT) confunde dos sentidos de "gobierno": el gobierno de **derechos de decisión organizacional** (quién decide qué) que trata `dataops-02`, y el gobierno **operativo de calidad de datos** (linaje, validación) que tratan Berkeley C101 y el certificado de ingeniería de datos de MIT. Esta es una imprecisión real en la propuesta de ChatGPT. Al mismo tiempo, `informs-cap-essentials-blueprint.pdf` sitúa el encuadre de negocio (Dominio I) como la fase que antecede a los datos, no como una fase de ingeniería — lo cual respalda situar la estrategia junto al encuadre de problemas, no junto a la ingeniería de datos. **Decisión canónica:** la estrategia de datos se integra como un módulo sustantivo (no una mención de una diapositiva) dentro del curso de apertura, junto con la formulación de problemas — siguiendo la lógica estructural de Gemini, pero dándole el peso que su propia riqueza documental exige, en lugar de comprimirla como Gemini hace.

**Resolución 3 — Analítica Descriptiva.**
Evidencia: el propio `usc-introduction-to-data-analytics.pdf` ubica la visualización y los tableros en las **últimas semanas** de su semestre, después de bases de datos, SQL y NoSQL — es decir, después de que el estudiante ya programa y consulta datos. El patrón "Data 8" citado extensamente por `national-academies-data-science-for-undergraduates-2018.pdf` sí enseña visualización desde el principio, pero como parte de un curso introductorio que **ya incluye programación básica** desde su primera semana, no antes de ella. Ningún documento del corpus enseña EDA/visualización rigurosa sin que el estudiante haya escrito código previamente. **Decisión canónica:** la Analítica Descriptiva es un curso propio, posicionado **después** del curso de programación (no fusionado con el curso de encuadre conceptual de entrada), corrigiendo tanto a ChatGPT como a Gemini en este punto específico, y confirmando la intuición estructural (aunque no la ubicación exacta) de Claude.

**Resolución 4 — Predicción, inferencia y causalidad.**
Evidencia: `berkeley-data-c102-data-inference-and-decisions.pdf` bunde en un solo curso universitario real "frequentist and Bayesian decision-making... causal inference... decision trees, neural networks, ensemble methods", y `mit-data-science-and-machine-learning.pdf` ubica su módulo de "regresión causal, RCT y estudios observacionales" en la semana inmediatamente posterior a su módulo de regresión predictiva, dentro del mismo programa continuo de 12 semanas — no en un curso separado varios meses después. Esta es la evidencia documental más directa y específica de todo el corpus sobre este punto, y respalda la posición de Gemini frente a la de ChatGPT y Claude. Sin embargo, Berkeley exige como prerrequisito un curso de probabilidad ya completado (Math 54/56/110 o un curso de probabilidad formal) **antes** de tomar ese curso integrado — lo que significa que el corpus no respalda fusionar la estadística *introductoria* con la causalidad y el aprendizaje automático, solo fusionar causalidad+aprendizaje automático **después** de una base estadística ya consolidada. **Decisión canónica:** se mantiene una Estadística e Inferencia introductoria como curso propio (evitando el error de Gemini de comprimir probabilidad básica junto con ML avanzado), pero se **fusiona** la inferencia causal con el modelado predictivo en un único curso posterior (corrigiendo a ChatGPT y Claude), con una frontera pedagógica interna explícita entre ambos módulos (ver Sección 9).

**Resolución 5 — Aprendizaje profundo, series de tiempo, recomendadores, redes.**
Evidencia: el propio marco de competencias de `acm-computing-competencies-undergraduate-data-science-2021.pdf` clasifica el aprendizaje profundo dentro de la Knowledge Area de Machine Learning con tramos que corresponden a Tier 2 (mayoría, no todos) o Electivo, no a Tier 1 (núcleo obligatorio para todos). Sí es cierto que `mit-data-science-and-machine-learning.pdf` dedica semanas completas a aprendizaje profundo, sistemas de recomendación y redes — pero ese es un certificado profesional compacto de 12 semanas diseñado para practicantes que ya tienen experiencia cuantitativa previa, no evidencia de que esto deba ser núcleo obligatorio de un programa académico completo dirigido a una población más amplia. **Decisión canónica:** se confirma la posición de ChatGPT (implícitamente compartida por la no-inclusión de Gemini): estos métodos son una **extensión electiva** construida sobre el curso de modelado predictivo/causal, no un curso obligatorio del núcleo. Esto corrige la decisión de Claude de dedicarles un curso completo obligatorio.

**Resolución 6 — Orden Productos vs. DataOps.**
Evidencia directa y decisiva: el propio ciclo de vida analítico que `dataops-05-agile.pdf` y `dataops-06-definition.pdf` documentan explícitamente —Ideación → Incepción → Investigación y Desarrollo → **Transición/Producción** → Retiro— sitúa la definición del producto (hipótesis de épica, MVP, alcance) en las fases **tempranas** (Ideación/Incepción), y sitúa la industrialización DataOps completa (pruebas automatizadas de producción, CI/CD, ambientes múltiples) en la fase **posterior** (Transición/Producción). Este es el propio marco temporal que el corpus DataOps define para sí mismo, y coloca al diseño de producto **antes** de la industrialización operativa completa. **Decisión canónica:** Productos antes de DataOps, coincidiendo con ChatGPT y Gemini y corrigiendo el orden inverso de Claude.

**Resolución 7 — Gobernanza/Ética como curso dedicado.**
Evidencia: ningún documento primario del corpus propone un curso autónomo de ética/gobernanza. `national-academies-data-science-for-undergraduates-2018.pdf` recomienda explícitamente que la ética esté "tejida desde el principio y a lo largo de todo el currículo" (Finding/Recomendación 2.4), lo cual es una recomendación **contra** el aislamiento en un curso separado, no a favor. `dataops-03-methodologies.pdf` diagrama "Gobernanza y Ética" como una dimensión **transversal** que atraviesa las seis etapas de un proyecto analítico, no como una séptima etapa independiente. `acm-computing-competencies-undergraduate-data-science-2021.pdf` la incorpora dentro de la Knowledge Area de "Profesionalismo", integrada con otras competencias, no aislada. Esta es una convergencia de evidencia (dos de los documentos más autorizados del corpus en este tema específico) contra la práctica de aislar la ética, y coincide con la decisión independiente de dos de los tres diseñadores (ChatGPT y Gemini). **Decisión canónica:** no se crea un curso dedicado de gobernanza/ética; se mantiene exclusivamente transversal, con un punto de consolidación explícito (no un curso nuevo) en el curso final de DataOps, corrigiendo la decisión de Claude.

**Resolución 8 — Programación como curso propio.**
Evidencia: `acm-computing-competencies-undergraduate-data-science-2021.pdf` mantiene "Programming, Data Structures, and Algorithms" como una Knowledge Area explícitamente distinta de "Data Acquisition, Management, and Governance" — es decir, el propio marco más autorizado del corpus en currículo de pregrado las trata como competencias separables. El certificado de ingeniería de datos de MIT también secuencia explícitamente "Python fundamentals + NumPy/Pandas/Matplotlib" como sus primeros tres módulos, **antes** de entrar a bases de datos relacionales. **Decisión canónica:** se mantiene un curso propio de programación y fundamentos computacionales, corrigiendo la fusión de Gemini y confirmando a ChatGPT/Claude.

**Resolución 9 — Capstone separado.**
Evidencia: ninguno de los documentos de marco profesional (INFORMS, ACM) exige un curso administrativamente distinto para la integración final; el propio marco INFORMS presenta sus siete dominios como un **ciclo recurrente**, no como una secuencia que culmina en un curso extra. Dos de los tres diseñadores llegaron independientemente a la misma conclusión de que el último curso técnico (DataOps/Operacionalización) puede y debe funcionar como el espacio de integración final. **Decisión canónica:** no se crea un curso 10 de "Capstone"; el curso final de DataOps se diseña explícitamente como práctica integradora con patrocinador real (heredando el espíritu del Capstone de Claude, pero sin agregar un curso adicional), corrigiendo la fragmentación de Claude en este punto.

# 5. Aportes únicos valiosos de cada propuesta

**De ChatGPT:** la exclusión explícita y razonada de aprendizaje profundo/series de tiempo/recomendadores/redes/RL/optimización a gran escala como electivos ("no son obligatorios para toda la cadena") es la formulación más clara y defendible de los tres documentos sobre este punto, y se adopta directamente en la Resolución 5. También es valioso su principio articulador de que "cada curso debe demostrar un objeto distinto" (una formulación, un proceso reproducible, un flujo de datos apto, una conclusión bajo incertidumbre, una generalización predictiva, una atribución causal, una recomendación, una solución usable, una operación sostenible) — un criterio de diseño más explícito y verificable que el de las otras dos propuestas, que se adopta como principio rector en la Sección 7.

**De Claude:** el reconocimiento explícito de que "gobernanza" significa **tres cosas distintas según el nivel** —institucional/de decisión, operativo/de calidad, y ético/de responsabilidad— es un hallazgo analítico genuino que ni ChatGPT ni Gemini articulan con esa precisión, y se conserva en la síntesis como estructura conceptual (Sección 10), aunque no como tres cursos separados. También es valiosa la evidencia recopilada sobre `dataops-08-data-scientids.pdf` como "documento bisagra" entre ingeniería de datos y DataOps (mitad arquitectura, mitad deuda técnica/Design Thinking) — una observación fina sobre la estructura del propio corpus que ninguna otra propuesta hace explícita, y que se preserva en la Sección 9.

**De Gemini:** la articulación de la dualidad **Tubería de Valor vs. Tubería de Innovación** como el eje organizador de la frontera entre "hacer analítica" y "operar analítica" es la lectura más precisa y mejor anclada documentalmente (`dataops-04`, `dataops-06`) de las tres sobre esta distinción, y se adopta explícitamente como marco conceptual en la Sección 9. También es valiosa la insistencia explícita en no fragmentar predicción/causalidad en cursos separados, que —aunque matizada en la Resolución 4— resultó ser la posición mejor respaldada por evidencia directa de todo el ejercicio de comparación.

# 6. Problemas detectados en las tres propuestas

- **ChatGPT** ubica `dataops-02-data-strategy.pdf` como evidencia de un curso de ingeniería/gobierno de datos con el que no comparte contenido técnico (ver Resolución 2) — una imprecisión de mapeo evidencia→curso. Además, al no tener módulo de estrategia explícito en ningún curso, el "caso de valor" y el "portafolio de iniciativas" —competencias reales y bien evidenciadas— quedan sin hogar curricular claro en su arquitectura.
- **Claude** fragmenta en exceso: separa en cursos distintos Estrategia/Fundamentos, Predictivo I/Causal/Predictivo II, y Productos/DataOps/Gobernanza, cuando el corpus (Resoluciones 1, 4, 6, 7) sostiene fusiones más económicas sin pérdida de rigor. También invierte el orden Productos↔DataOps respecto de la lógica de ciclo de vida que el propio corpus DataOps define, y da a los métodos avanzados (aprendizaje profundo, series de tiempo, redes) un peso de curso obligatorio que ni ACM ni la comparación entre programas profesionales y académicos sostienen para un núcleo universal.
- **Gemini** comprime en exceso en el sentido opuesto: al fusionar estadística introductoria con causalidad y aprendizaje automático en un solo curso (C3) sin un curso previo de probabilidad/estadística autónomo, no respeta el propio prerrequisito que Berkeley exige antes de un curso equivalente (C102 requiere probabilidad ya aprobada). También fusiona la analítica descriptiva con el encuadre estratégico de apertura (C1) antes de que el estudiante haya programado, lo cual ningún documento del corpus respalda directamente (Resolución 3). Su curso 1 termina siendo el más sobrecargado de temas de naturaleza heterogénea (encuadre, estrategia, EDA, visualización, ética inicial) de las tres propuestas.
- **Las tres** comparten una limitación: ninguna resuelve explícitamente si la "arquitectura, calidad y gobernanza operativa de datos" del curso de Ingeniería de Datos y las "pruebas automatizadas de calidad de datos" del curso de DataOps son la misma competencia enseñada dos veces o dos competencias distintas (diseño de reglas de calidad vs. automatización continua de esas reglas en producción). Esta frontera, aunque mencionada, no se traza con precisión suficiente en ninguna de las tres (se resuelve en la Sección 9 de esta síntesis).
- **Las tres** subtratan la posibilidad de que la Estrategia de Datos (`dataops-02`) sea insuficientemente aprovechada si se comprime demasiado (Gemini) o se aísla demasiado de la ejecución técnica (Claude); ninguna ofrece una integración intermedia explícita hasta esta síntesis.

# 7. Principios de la arquitectura canónica

1. **Un curso se justifica por una pregunta de naturaleza irreductible, no por la existencia de un documento que la evidencie.** `dataops-02` es rico, pero "estrategia organizacional" y "formulación de problemas" responden a la misma pregunta de altitud ("¿qué debemos analizar y por qué?"), así que comparten curso.
2. **Una distinción conceptual importante puede vivir como pivote pedagógico dentro de un curso, sin requerir un curso propio.** Predicción vs. causalidad se enseña como el giro central de un mismo curso construido sobre el mismo vehículo técnico (regresión), siguiendo el precedente directo de Berkeley C102 y MIT IDSS.
3. **La secuencia de cursos debe reflejar el ciclo de vida documentado por el propio corpus, no una preferencia de diseño.** El orden Producto→Operación replica exactamente el ciclo Ideación→...→Transición/Producción que `dataops-05` y `dataops-06` definen.
4. **Las competencias con evidencia amplia pero dispersa (ética, gobernanza, comunicación, reproducibilidad) son transversales por diseño, no por defecto.** Se planifican explícitamente en cada curso, con puntos de consolidación nombrados, en lugar de asumir que "aparecerán".
5. **Lo que un marco de competencias autorizado (ACM) clasifica como Tier 2/Electivo no se promueve a núcleo obligatorio solo porque un programa profesional compacto lo cubra en extenso.** La densidad de un certificado de 12 semanas no es evidencia de necesidad curricular universal.
6. **Cada curso debe producir un objeto de aprendizaje verificable y distinto de los demás** (principio explícito de ChatGPT, adoptado aquí): una formulación, un dato gobernado, una síntesis descriptiva, una conclusión bajo incertidumbre, una generalización predictiva/causal validada, una recomendación de decisión, un producto usable, una operación sostenible.
7. **La arquitectura debe ser auditable por prerrequisitos, no solo por narrativa.** Cada curso declara explícitamente qué recibe y qué entrega, de modo que la cadena de dependencias sea verificable curso a curso.

# 8. Arquitectura curricular canónica

Nueve cursos. Los cursos 3 y 4 pueden cursarse en paralelo (ambos dependen únicamente del curso 2).

### Curso 1 — Fundamentos de Analítica: Encuadre de Problemas y Estrategia de Datos
- **Posición:** primer curso, sin prerrequisitos de analítica.
- **Propósito central:** traducir una situación de decisión ambigua en una pregunta analítica bien formulada; instalar el mapa mental de ciclo de vida completo (encuadre de negocio → encuadre analítico → datos → método → modelo → decisión → producto → operación), incluyendo la evolución histórica de las metodologías (KDD → CRISP-DM → marcos ágiles → DataOps) y su convergencia con los siete dominios de INFORMS; diagnosticar por qué fracasan las iniciativas de analítica (mitos de adopción, brechas de conocimiento); y desarrollar la capacidad de diagnosticar capacidades organizacionales de datos, formular objetivos estratégicos, construir un caso de valor y priorizar un portafolio de iniciativas.
- **Competencias principales:** formulación de problemas; taxonomía descriptivo/predictivo/prescriptivo; estrategia y portafolio de datos; evaluación de oportunidades de IA y creación de valor; gobierno de decisión institucional (centralizado/federado/descentralizado); introducción a la responsabilidad ética.
- **Prerrequisitos:** ninguno (razonamiento cuantitativo básico de admisión).
- **Qué recibe:** nada; es la puerta de entrada.
- **Qué prepara:** el vocabulario, la historia, el marco de ciclo de vida y el criterio de valor organizacional que da sentido a todos los cursos siguientes.

### Curso 2 — Programación y Fundamentos Computacionales para Analítica
- **Posición:** segundo curso, en paralelo o inmediatamente después del curso 1.
- **Propósito central:** desarrollar fluidez computacional — programación, estructuras de datos, manipulación de datos tabulares y semiestructurados, fundamentos de control de versiones y de SQL — como condición habilitante de todo el resto de la cadena.
- **Competencias principales:** programación; estructuras de datos; control de versiones básico; consultas SQL introductorias.
- **Prerrequisitos:** curso 1 (recomendado, no estricto).
- **Qué recibe:** el marco conceptual del curso 1.
- **Qué prepara:** la base computacional de los cursos 3, 4 y 5.

### Curso 3 — Analítica Descriptiva, Exploración y Comunicación de Evidencia
- **Posición:** tercer curso, en paralelo con el curso 4.
- **Propósito central:** análisis exploratorio de datos (EDA), principios de visualización y percepción, construcción de tableros/informes, narrativa de evidencia para audiencias técnicas y no técnicas.
- **Competencias principales:** EDA multivariada; visualización; comunicación/storytelling.
- **Prerrequisitos:** curso 2.
- **Qué recibe:** capacidad de programar y manejar datos.
- **Qué prepara:** el hábito de examinar datos con rigor antes de modelarlos o gobernarlos, insumo informal de los cursos 5 y 6.

### Curso 4 — Estadística e Inferencia para la Analítica
- **Posición:** cuarto curso, en paralelo con el curso 3.
- **Propósito central:** probabilidad aplicada, estimación, pruebas de hipótesis, intervalos de confianza, razonamiento frecuentista y bayesiano, diseño experimental básico.
- **Competencias principales:** razonamiento estadístico; cuantificación de la incertidumbre; diseño de estudios.
- **Prerrequisitos:** curso 2.
- **Qué recibe:** capacidad de programar y manejar datos.
- **Qué prepara:** el lenguaje formal de incertidumbre que sostiene los cursos 5, 6 y 7, y el prerrequisito exacto que Berkeley exige antes de un curso integrado de inferencia/causalidad/ML.

### Curso 5 — Ingeniería y Arquitectura de Datos para la Analítica
- **Posición:** quinto curso.
- **Propósito central:** modelado de datos relacional y no relacional; diseño de arquitecturas (lagos, bodegas, mercados de datos) con reglas explícitas de gobernanza (qué se ingiere, qué se transforma, cómo se alinea con el resto de la arquitectura); contraste entre arquitectura canónica (optimizada para estabilidad) y arquitectura orientada a DataOps (optimizada para cambio frecuente); calidad y linaje de datos como principio de gobernanza operativa (definición de reglas, no su automatización continua, que pertenece al curso 9).
- **Competencias principales:** arquitectura de datos; modelado de datos; gobernanza operativa y calidad de datos.
- **Prerrequisitos:** cursos 2 y 3.
- **Qué recibe:** de 3, el criterio de qué hace útil un dato para el análisis; de 2, la base de programación.
- **Qué prepara:** datos gobernados y arquitecturas conocidas para los cursos 6 y 7, y el sustrato técnico sobre el cual el curso 9 (DataOps) aplicará sus prácticas de entrega.

### Curso 6 — Modelado Predictivo, Aprendizaje Automático e Inferencia Causal
- **Posición:** sexto curso.
- **Propósito central:** construir, evaluar, regularizar y validar modelos supervisados (regresión, clasificación, árboles, ensambles) y no supervisados (clustering, reducción de dimensionalidad); a partir del mismo vehículo técnico de regresión, dar el giro pedagógico hacia la inferencia causal — diseño y análisis de experimentos controlados y estudios observacionales con variables de confusión— para que el estudiante distinga con rigor cuándo un modelo que predice bien no autoriza una afirmación causal ni una intervención.
- **Competencias principales:** aprendizaje supervisado y no supervisado; validación y regularización; inferencia causal y diseño experimental.
- **Prerrequisitos:** cursos 4 y 5.
- **Qué recibe:** el aparato de incertidumbre (curso 4) y datos gobernados (curso 5).
- **Qué prepara:** estimaciones predictivas y causales validadas, insumo directo del curso 7.

### Curso 7 — Analítica Prescriptiva: Optimización, Simulación y Decisión bajo Incertidumbre
- **Posición:** séptimo curso.
- **Propósito central:** modelado de decisiones mediante optimización matemática, simulación (Monte Carlo, análisis de sensibilidad) y análisis de valor/tradespace, incorporando restricciones, riesgo y sesgos de comportamiento relevantes a la decisión — sin equipararse a un curso completo de Investigación de Operaciones.
- **Competencias principales:** optimización; simulación; decisión bajo incertidumbre; sesgos de comportamiento.
- **Prerrequisitos:** cursos 4 y 6.
- **Qué recibe:** estimaciones predictivas y causales del curso 6 como insumos/restricciones del problema de decisión.
- **Qué prepara:** una recomendación de decisión, insumo directo del curso 8.

### Curso 8 — Diseño de Productos y Sistemas Analíticos
- **Posición:** octavo curso.
- **Propósito central:** convertir una recomendación de decisión en un producto analítico: mentalidad de producto (hipótesis de épica, MVP), diseño de la interacción humano-máquina, empaquetamiento en servicios/APIs, prototipado rápido y validación temprana con usuarios reales, antes de cualquier industrialización a escala. Cuando el caso lo requiera, esto incluye prototipar flujos basados en LLM, recuperación aumentada (RAG) y agentes con herramientas, sin convertir el curso en una especialización autónoma de IA agéntica.
- **Competencias principales:** diseño de producto; HCI; prototipado; empaquetamiento en servicios; diseño responsable de flujos LLM/RAG/agénticos.
- **Prerrequisitos:** curso 7.
- **Qué recibe:** una recomendación de decisión y los modelos que la sustentan.
- **Qué prepara:** un prototipo funcional y validado, listo para ser industrializado en el curso 9.

### Curso 9 — DataOps: Operacionalización, Gobernanza y Ciclo de Vida Analítico (curso integrador/práctica final)
- **Posición:** noveno y último curso.
- **Propósito central:** aplicar Lean Thinking (eliminación de desperdicio, mapeo de flujo de valor, teoría de restricciones) y metodologías ágiles (Scrum, Kanban, el Manifiesto DataOps) para industrializar el producto del curso 8: pruebas automatizadas de datos/lógica/modelos, control de versiones, ambientes múltiples, contenerización, parametrización, eliminación de heroísmo; monitoreo y MLOps (deriva, recalibración); y, cuando el producto incluya componentes LLM/RAG/agénticos, evaluación de precisión, latencia, robustez, fundamentación y trazabilidad, con controles de seguridad, privacidad y supervisión humana; organización del equipo de entrega (arquetipos, roles, trampas del líder de datos, madurez organizacional); y consolidación explícita de los tres niveles de gobierno evidenciados por el corpus —institucional (retomando el curso 1), operativo/de calidad (retomando el curso 5) y ético/de responsabilidad— aplicados de forma integrada a la solución completa. Este curso se diseña explícitamente como práctica integradora con patrocinador real, cumpliendo la función de capstone sin requerir un curso administrativo adicional.
- **Competencias principales:** Lean/Agile/DataOps; pruebas automatizadas; MLOps y evaluación operacional de sistemas agénticos; organización de equipos; gobernanza y ética integradas.
- **Prerrequisitos:** cursos 5 y 8.
- **Qué recibe:** una arquitectura de datos conocida (curso 5) y un producto validado (curso 8) que debe entregarse, mantenerse y gobernarse de forma confiable.
- **Qué prepara:** práctica profesional o estudios de posgrado.

# 9. Fronteras canónicas entre cursos

**1 → 2.** El curso 1 formula y estrategiza sin código; el curso 2 produce evidencia reproducible en código. Frontera: "hablar sobre datos" vs. "manipular datos".

**2 → 3 / 2 → 4 (paralelos).** El curso 2 entrega la capacidad de programar; el curso 3 la usa para explorar y comunicar patrones sin exigir su justificación probabilística; el curso 4 exige esa justificación (intervalos, pruebas de hipótesis) para cualquier afirmación de incertidumbre. Un histograma puede mostrarse en el curso 3 sin justificar su base distribucional; esa justificación pertenece exclusivamente al curso 4.

**3/4 → 5.** Los cursos 3 y 4 trabajan con datos pequeños y limpios con fines de exploración e inferencia; el curso 5 comienza donde los datos son grandes, múltiples o de mala calidad y requieren una arquitectura para producirse de forma confiable y repetible. **Frontera Ingeniería de Datos ↔ cursos analíticos:** el curso 5 responde "¿puedo confiar en este dato y en la arquitectura que lo produjo?"; los cursos 3/4/6/7 asumen esa confianza como insumo y preguntan qué se puede describir, inferir, predecir o decidir con él.

**5 → 6.** El curso 5 entrega datos gobernados y arquitecturas conocidas (lagos/bodegas/mercados de datos); el curso 6 no repite ese diseño, lo asume como insumo. **Frontera Descriptiva ↔ Predictiva:** ya resuelta en 3→5; aquí la frontera relevante es que el diseño de esquemas y la decisión lago/bodega/mercado de datos pertenecen enteramente al curso 5, mientras que la ingeniería de características con fundamento estadístico (qué transformar y por qué) pertenece al curso 6.

**Dentro del curso 6 — frontera interna Predictiva ↔ Causal (no una frontera entre cursos, sino un pivote pedagógico deliberado):** la primera mitad del curso pregunta "¿qué tan bien predice este modelo?" (regularización, validación cruzada, métricas); la segunda mitad, sobre el mismo modelo de regresión, pregunta "¿puedo afirmar causalidad, y bajo qué condiciones (aleatorización, ausencia de confusión)?". Esta frontera interna reemplaza la frontera entre cursos que ChatGPT y Claude proponían, sin eliminar la distinción conceptual.

**6 → 7 (frontera Predictiva/Causal ↔ Prescriptiva).** El curso 6 entrega estimaciones y efectos causales; el curso 7 los toma como insumos/restricciones de un problema de decisión con una función de valor explícita, que no forma parte del criterio estadístico del curso 6. Un tema ambiguo —elegir entre modelos según su "valor de negocio" esperado— pertenece al curso 7, porque introduce una función de decisión ausente en el curso 6.

**7 → 8 (frontera Prescriptiva ↔ Productos).** El curso 7 entrega una recomendación de decisión (política, asignación óptima); el curso 8 pregunta si esa recomendación puede convertirse en algo que un humano use y adopte. Un modelo de optimización nunca debe confundirse con un producto: el curso 7 enseña a decidir; el curso 8 enseña a empaquetar esa decisión en una interfaz, un servicio o una API que alguien pueda usar.

**8 → 9 (frontera Productos ↔ DataOps — la más importante de la arquitectura).** El curso 8 entrega un prototipo validado con usuarios en la lógica de la **Tubería de Innovación** (ideación, UX, MVP); el curso 9 pregunta si ese prototipo puede sostenerse en la **Tubería de Valor** (pruebas automatizadas, CI/CD, ambientes múltiples, monitoreo continuo, gobierno del ciclo de vida). Esta es exactamente la dualidad que `dataops-04-lean-thinking.pdf` y `dataops-06-definition.pdf` documentan como el eje organizador de todo sistema analítico maduro. Un tema ambiguo —la plantilla de "Hipótesis de Épica"— se usa en el curso 8 para especificar el valor y el diseño de un producto para el usuario final, y se retoma en el curso 9 únicamente para organizar el flujo de trabajo del equipo de entrega en un tablero Kanban, con un propósito distinto.

Cuando el producto incorpora RAG o agentes, esta frontera se mantiene: el curso 8 diseña la interacción, el caso de uso y el prototipo con sus herramientas; el curso 9 verifica y opera el sistema completo mediante evaluación, pruebas, observabilidad, trazabilidad, controles de seguridad y supervisión humana. Herramientas, memoria, MCP, planificación y colaboración multiagente son capacidades de diseño que requieren una decisión de ubicación más precisa antes de asignarse como dominio obligatorio de un curso (ver Sección 16).

**Frontera Ingeniería de Datos (5) ↔ DataOps (9), no adyacente pero crítica:** el curso 5 diseña reglas de calidad y arquitectura (qué debe ser cierto de los datos); el curso 9 automatiza la verificación continua de esas mismas reglas en producción (pruebas de balance, integridad, frescura, control estadístico de proceso). Esta frontera —insuficientemente trazada en las tres propuestas originales (Sección 6)— se resuelve así: **diseñar una regla de calidad es competencia del curso 5; automatizar su verificación continua en producción es competencia del curso 9**; ambas son necesarias y no son la misma competencia repetida.

# 10. Competencias transversales

- **Formulación y reformulación de problemas.** Introducida en el curso 1; retomada al definir la función de valor en el curso 7; integrada en el curso 9 al validar el caso de negocio con el patrocinador.
- **Comunicación y narrativa de evidencia.** Introducida en el curso 1, desarrollada en el curso 3, exigida en la entrega de cada curso posterior, integrada en el curso 9 frente a un patrocinador real.
- **Reproducibilidad y control de versiones.** Introducida en el curso 2, desarrollada en los cursos 3 a 7 (cada entrega debe ser reproducible), dominada en el curso 9 (control de versiones unificado de código, datos y modelos, ambientes múltiples, contenerización).
- **Calidad de software y pruebas.** Introducida como prueba básica en el curso 2, desarrollada como validación de datos en el curso 5, integrada como pirámide completa de pruebas automatizadas (unitarias, integración, funcionales, regresión, desempeño, humo, balance de datos) en el curso 9.
- **Automatización.** Ausente como tema explícito antes del curso 5 (automatización de limpieza/transformación), desarrollada en el curso 8 (automatización de la lógica de decisión en un servicio), dominada en el curso 9 (CI/CD, orquestación).
- **Cuantificación de la incertidumbre y experimentación.** Introducida en el curso 4, desarrollada en el curso 6 (validación, diseño experimental, causalidad) y el curso 7 (simulación, sensibilidad), monitoreada operativamente en el curso 9 (deriva de datos y de modelos).
- **Gobierno de datos en tres niveles simultáneos (hallazgo preservado de la propuesta de Claude, ver Sección 5).** Nivel institucional/de decisión: introducido en el curso 1. Nivel operativo/de calidad: introducido en el curso 5. Nivel ético/de responsabilidad: consolidado en el curso 9. Se mantiene como estructura conceptual transversal, no como tres cursos separados.
- **Ética, privacidad, seguridad y responsabilidad en IA.** Introducida en el curso 1 (siguiendo la recomendación explícita de National Academies de tejerla desde el principio), instanciada técnicamente en el curso 5 (gobernanza operativa) y el curso 6 (sesgo algorítmico en modelos), integrada en el curso 8 (diseño responsable de producto) y consolidada como dimensión transversal explícita del ciclo de vida completo en el curso 9.
- **Organización y liderazgo de equipos de datos.** Introducida conceptualmente en el curso 1 (mención de mitos organizacionales), concentrada y desarrollada en profundidad en el curso 9 (arquetipos de equipo, roles, madurez, trampas del líder de datos).
- **Monitoreo y observabilidad.** No es tema antes del curso 5 (calidad estática); se convierte en tema dinámico en el curso 9 (deriva, control estadístico de proceso, alertas).

# 11. Mapa curricular integrado

I = Introducido, D = Desarrollado, M = Dominado/Integrado, — = No es foco.

| Competencia / Tema | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
|---|---|---|---|---|---|---|---|---|---|
| Formulación de problemas de decisión | I | — | — | — | — | D | D | D | M |
| Historia y marcos metodológicos (KDD/CRISP-DM/INFORMS/DataOps) | M | — | — | — | — | — | — | — | D |
| Estrategia de datos: objetivos, portafolio, caso de valor | M | — | — | — | — | — | D | D | D |
| Gobierno de datos: derechos de decisión institucional | M | — | — | — | I | — | — | — | D |
| Programación y estructuras de datos | I | M | D | D | D | D | D | D | D |
| Bases de datos y modelado de datos (SQL/NoSQL) | — | I | D | — | M | D | — | — | D |
| Arquitectura de datos y gobernanza operativa/calidad | — | — | — | — | M | D | — | — | D |
| Análisis exploratorio y visualización | — | I | M | D | D | D | D | D | D |
| Comunicación de evidencia / storytelling | I | — | M | D | D | D | D | D | M |
| Probabilidad e inferencia estadística | — | — | D | M | D | D | D | — | D |
| Diseño experimental (A/B, RCT) | — | — | — | D | — | M | — | — | D |
| Aprendizaje supervisado (regresión/clasificación/ensambles) | — | — | — | — | D | M | D | D | D |
| Aprendizaje no supervisado (clustering/reducción dimensional) | — | — | — | — | — | M | — | D | D |
| Inferencia causal y variables de confusión | — | — | — | I | — | M | D | — | D |
| Optimización matemática | — | — | — | I | — | I | M | D | — |
| Simulación y análisis de sensibilidad | — | — | — | I | — | — | M | D | — |
| Decisión bajo incertidumbre y sesgos de comportamiento | I | — | — | I | — | — | M | D | D |
| Diseño de producto / HCI / MVP-hipótesis de épica | I | — | — | — | — | — | I | M | D |
| Lean thinking y eliminación de desperdicio en analítica | I | — | — | — | I | — | — | — | M |
| Metodologías ágiles y manifiesto DataOps | I | — | — | — | — | — | — | I | M |
| Pruebas automatizadas (datos, lógica, modelos) | — | I | — | — | D | — | — | D | M |
| Prácticas de entrega continua (versionado, ambientes, contenedores) | — | I | — | — | D | — | — | D | M |
| MLOps: monitoreo, deriva, recalibración | — | — | — | — | I | — | — | I | M |
| Sistemas LLM/RAG/agénticos: diseño, evaluación y operación | — | — | — | — | — | — | — | I | M |
| Organización y liderazgo de equipos de datos | I | — | — | — | — | — | — | — | M |
| Ética, sesgo algorítmico, privacidad, responsabilidad en IA | I | — | — | — | D | D | — | D | M |
| Reproducibilidad y control de versiones (transversal) | — | I | D | D | D | D | D | D | M |

La matriz hace visibles tres decisiones de la síntesis: (a) ninguna fila de contenido técnico tiene más de una "M", preservando que cada competencia se domina en un único curso; (b) las tres filas de gobierno de datos (institucional, operativo, ético) muestran trayectorias de maduración independientes que convergen todas en el curso 9, sin fusionarse en una sola fila ambigua; (c) "aprendizaje supervisado" y "causal" comparten el mismo curso (6) con una "M" cada una, visibilizando el pivote interno descrito en la Sección 9 en lugar de una frontera entre cursos.

# 12. Temas que quedan fuera del núcleo

- **Aprendizaje profundo, series de tiempo avanzadas, sistemas de recomendación, redes/grafos y aprendizaje por refuerzo.** Extensiones electivas construidas sobre el curso 6 (Resolución 5), consistente con la clasificación Tier 2/Electivo de ACM y la exclusión explícita razonada por ChatGPT.
- **Teoría matemática completa de Investigación de Operaciones** (dualidad, teoría de colas, procesos estocásticos avanzados, método Simplex demostrado paso a paso). Electivo, consistente con la instrucción de no equiparar prescriptivo con IO completa.
- **Administración de infraestructura en la nube a nivel de proveedor específico y certificación de herramientas DataOps/CI-CD nombradas** (Puppet, Chef, Jenkins, Kubeflow, etc.). Se enseñan como categorías ilustrativas dentro del curso 9, no como currículo de certificación.
- **Marcos comerciales de escalamiento ágil a nivel de certificación** (SAFe). Se estudia conceptualmente como parte de la evolución histórica de la colaboración ágil dentro del curso 1 y 9, no a profundidad de certificación.
- **Teorías completas de comportamiento organizacional o de innovación de producto** (Coordinación Relacional como cuerpo teórico completo, algoritmos de innovación dirigida por resultados). Se introducen como constructos aplicados dentro del módulo organizacional del curso 9; su desarrollo teórico completo es electivo.
- **Prototipado físico y metodologías de manufactura** (evidenciado en MIT Rapid Prototyping). Fuera del núcleo — pertenece al diseño de producto físico, no a productos de datos.
- **Un curso ejecutivo de "Liderazgo de Datos" para audiencias no técnicas** (MIT Data Leadership, Cambridge, PwC Master Class). El contenido de liderazgo propio de un currículo de Analítica ya se incorpora en el curso 9 con la profundidad apropiada para un practicante; un programa ejecutivo para consumidores no técnicos seguiría siendo un producto distinto.
- **Especialización vertical por dominio de aplicación** (finanzas, salud, mercadeo, manufactura). Electivas o contexto del proyecto integrador del curso 9, siguiendo la recomendación explícita de National Academies.
- **Un curso dedicado exclusivamente a Estrategia de Datos como programa gerencial completo.** Se integra como módulo sustantivo del curso 1 (Resolución 2); una expansión a curso propio es una especialización legítima para programas de orientación más gerencial, no para el núcleo de un programa de Analítica que forma practicantes técnicos.

# 13. Trazabilidad de las decisiones

| Tema de diseño | ChatGPT | Claude | Gemini | Decisión canónica | Evidencia documental principal |
|---|---|---|---|---|---|
| Número de cursos | 9 | 14 | 6 | 9 | Ninguna fuente prescribe un número; se deriva de aplicar el principio "una pregunta irreductible por curso" a los 8 bloques identificados en la Sección 7 |
| Estrategia de datos | Evidencia dispersa en curso de ingeniería | Curso propio (curso 2) | Fusionada en curso 1 | Módulo sustantivo dentro del curso 1 | `dataops-02-data-strategy.pdf`; `informs-cap-essentials-blueprint.pdf` (Dominio I) |
| Analítica descriptiva | Fusionada en curso 1 | Curso propio, tras programación (curso 5) | Fusionada en curso 1 | Curso propio, tras programación (curso 3) | `usc-introduction-to-data-analytics.pdf` (visualización al final del semestre, tras SQL); `national-academies-data-science-for-undergraduates-2018.pdf` (Data 8 incluye programación desde el inicio) |
| Predicción vs. causalidad | Cursos separados (C5, C6) | Cursos separados con orden intercalado | Curso único integrado (C3) | Un curso (curso 6) con pivote pedagógico interno, tras estadística separada | `berkeley-data-c102-data-inference-and-decisions.pdf`; `mit-data-science-and-machine-learning.pdf` (semanas consecutivas) |
| Aprendizaje profundo/series de tiempo/redes | Electivo explícito | Curso obligatorio propio (curso 9) | No tratado como núcleo | Electivo | `acm-computing-competencies-undergraduate-data-science-2021.pdf` (clasificación Tier 2/Electivo) |
| Orden Productos ↔ DataOps | Productos antes de Operación | DataOps antes de Productos | Productos antes de Operación | Productos (curso 8) antes de DataOps (curso 9) | `dataops-05-agile.pdf` y `dataops-06-definition.pdf` (ciclo Ideación→...→Transición/Producción) |
| Gobernanza/ética como curso dedicado | No (transversal) | Sí (curso 13) | No (transversal, M en curso final) | No; transversal con consolidación en el curso final | `national-academies-data-science-for-undergraduates-2018.pdf` (ética "tejida desde el principio"); `dataops-03-methodologies.pdf` (gobernanza como dimensión transversal) |
| Programación como curso propio | Sí (C2) | Sí (curso 3) | No (fusionada en Ingeniería de Datos) | Sí (curso 2) | `acm-computing-competencies-undergraduate-data-science-2021.pdf` (KA de Programación distinta de KA de Datos) |
| Capstone como curso separado | No | Sí (curso 14) | No | No; el curso final de DataOps cumple esa función | `informs-analytics-framework-2024.pdf` (ciclo recurrente de siete dominios, no una fase final separada) |

# 14. Arquitectura final resumida

```
[1] Fundamentos de Analítica: Encuadre de Problemas y Estrategia de Datos
        │
        ▼
[2] Programación y Fundamentos Computacionales para Analítica
        │
        ├──────────────────────┐
        ▼                      ▼
[3] Analítica Descriptiva,   [4] Estadística e Inferencia
    Exploración y Comunicación    para la Analítica
    de Evidencia                    │
        │                           │
        └───────────┬───────────────┘
                     ▼
        [5] Ingeniería y Arquitectura de Datos
            para la Analítica
                     │
                     ▼
        [6] Modelado Predictivo, Aprendizaje
            Automático e Inferencia Causal
            (pivote interno: predicción → causalidad)
                     │
                     ▼
        [7] Analítica Prescriptiva: Optimización,
            Simulación y Decisión bajo Incertidumbre
                     │
                     ▼
        [8] Diseño de Productos y Sistemas Analíticos
            (Tubería de Innovación)
                     │
                     ▼
        [9] DataOps: Operacionalización, Gobernanza
            y Ciclo de Vida Analítico
            (Tubería de Valor — curso integrador/capstone,
             retoma gobierno institucional de [1] y
             gobierno operativo de [5])
```

**Hilo transversal:** `Formulación de problemas · Comunicación · Reproducibilidad y control de versiones · Calidad de software y pruebas · Incertidumbre y experimentación · Gobierno de datos (3 niveles) · Ética, privacidad y responsabilidad en IA · Organización y liderazgo de equipos · Monitoreo y observabilidad`

# 15. Incertidumbres pendientes

- **Carga del curso 6.** Fusionar aprendizaje supervisado, no supervisado e inferencia causal en un solo curso está respaldado por evidencia directa (Berkeley C102, MIT IDSS), pero ningún documento del corpus permite determinar a nivel macro si esa carga cabe razonablemente en un semestre estándar o si en la práctica requerirá dos períodos académicos conectados (una decisión de nivel meso, no macro, que corresponde a una fase posterior de diseño).
- **Peso relativo de la Estrategia de Datos dentro del curso 1.** El corpus evidencia que `dataops-02` tiene la riqueza de un curso completo, pero no hay evidencia documental que determine si, en la práctica, un único curso de apertura puede tratar con suficiente profundidad tanto el encuadre de problemas como la estrategia organizacional sin que una de las dos partes quede subdesarrollada; esto depende de decisiones de carga horaria que exceden el nivel macro.
- **Punto exacto de introducción de la programación previa al curso 1.** El corpus no permite determinar de forma concluyente si la programación (curso 2) debe ser estrictamente posterior al curso 1 o si ambos deberían ser plenamente paralelos desde el primer día; los documentos consultados no distinguen ese matiz de secuenciación temprana.
- **Umbral exacto entre "core" y "electivo" para aprendizaje profundo.** La Resolución 5 se apoya en la clasificación Tier 2/Electivo de ACM (2021) y en la naturaleza compacta del certificado profesional de MIT IDSS, pero el corpus no contiene evidencia suficiente para determinar si, a medida que el aprendizaje profundo se vuelve más ubicuo en la práctica profesional, este umbral debería desplazarse hacia el núcleo — es una pregunta que depende de la evolución del campo, no resoluble solo con el corpus actual.
- **Si el curso 9 requiere dividirse administrativamente en dos (DataOps técnico y Capstone/práctica) por razones de acreditación o de carga de proyecto**, aun cuando conceptualmente no se requiera contenido nuevo. Esta es una decisión institucional/administrativa, no una decisión que el corpus documental pueda resolver.

# 16. Nueva evidencia curricular: IA estratégica y sistemas agénticos

Los documentos incorporados en `curriculum/` se tratan como evidencia nueva, no como una instrucción para rediseñar la arquitectura canónica.

- **`berkeley-ai-business-strategy-applications.pdf`** refuerza decisiones ya tomadas: la IA debe abordarse como una fuente de valor y ventaja competitiva, con estrategia, equipos, transformación organizacional, tolerancia al riesgo, supervisión y gobernanza. También refuerza el carácter transversal de sesgo, privacidad, propiedad intelectual y responsabilidad. Por ello amplía explícitamente la competencia de evaluación de oportunidades de IA del curso 1 y confirma la integración de diseño responsable en los cursos 8 y 9; no justifica una nueva frontera ni un nuevo curso.
- **`ut-austin-agentic-ai-business-applications.pdf`** amplía competencias de productos y operación: IA generativa, RAG, agentes, integración de herramientas, memoria, MCP, planificación, razonamiento, sistemas multiagente, evaluación y pruebas, seguridad, privacidad y trazabilidad. La síntesis incorpora ahora el diseño de prototipos LLM/RAG/agénticos en el curso 8 y su evaluación y operación responsable en el curso 9. Esto reconoce la evidencia sin presentar esos temas como un bloque curricular ya resuelto.

**Pregunta abierta de diseño — ubicación curricular de IA agéntica.** La evidencia de UT Austin describe una progresión coherente —LLM → RAG → agentes → herramientas y memoria → MCP → planificación/razonamiento → multiagente → evaluación, seguridad y trazabilidad— cuya amplitud excede una mención puntual. Aún no se crea un curso de IA agéntica ni se modifica la arquitectura de nueve cursos. En la próxima revisión de nivel meso se deberá decidir, con evidencia adicional de carga, prerrequisitos y resultados de aprendizaje, si esa progresión debe: (a) permanecer como módulos articulados entre Productos de Datos y DataOps; (b) constituir un módulo transversal con prerrequisitos explícitos; o (c) justificar un curso o línea electiva propia. Hasta entonces, la decisión canónica es conservarla como pregunta abierta y no desplazar contenidos existentes.
