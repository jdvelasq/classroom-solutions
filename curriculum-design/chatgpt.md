# Lectura global del corpus

Los 31 PDF presentan Analytics como una cadena de valor basada en evidencia: formular una decisión, obtener y gobernar datos, analizar con métodos apropiados, comunicar incertidumbre e integrar, operar y revisar una solución. No equivale a visualización, programación, modelos ni infraestructura por separado. La propuesta se deriva de esa relación entre problema, datos, supuestos, resultado, decisión y personas afectadas; no replica la arquitectura de ninguna institución.

El corpus converge en una formación que une pensamiento estadístico, computación, matemáticas, datos, comunicación, contexto y responsabilidad. Los marcos profesionales añaden que una predicción correcta no garantiza valor. DataOps incorpora el ciclo de vida del producto analítico: desarrollo reproducible, control de versiones, pruebas de datos, lógica y modelos, automatización de flujos y entrega, coordinación entre desarrollo y operación, monitoreo, soporte y evolución. Los programas especializados amplían el mapa, pero también identifican contenidos que deben ser electivos y no requisitos universales.

# Competencias que debe desarrollar la cadena completa

Al finalizar, la persona egresada podrá formular problemas e indicadores; distinguir descripción, predicción, causalidad y prescripción; construir análisis reproducibles y versionados; diseñar datos con calidad, procedencia, acceso y propósito; razonar con incertidumbre; validar modelos; evaluar intervenciones; comparar alternativas bajo restricciones; diseñar soluciones usables y operables; y mantener productos analíticos mediante pruebas automatizables, orquestación, entrega controlada, observabilidad, monitoreo, retroalimentación y revisión de valor.

# Tensiones y decisiones curriculares fundamentales

La amplitud del corpus obliga a priorizar dominio sobre cobertura superficial. Predicción, causalidad y decisión se separan porque responden preguntas distintas: anticipar, atribuir y elegir. Datos, inferencia, modelos y operación se diferencian para hacer visibles sus supuestos, y convergen después para evitar formación fragmentada.

Las herramientas son medios intercambiables; las prácticas duraderas son reproducibilidad, procedencia, control de cambios, pruebas sobre datos, lógica y modelos, automatización, validación, monitoreo, observabilidad y revisión de valor. Desarrollo y operación se distinguen para aprender a construir y probar cambios antes de liberarlos, pero se coordinan como responsabilidades continuas de un mismo producto analítico. La ética no se limita a una clase: se aplica al propósito, acceso, calidad, sesgo, automatización, explicación, uso y retiro.

# Arquitectura curricular propuesta

La propuesta contiene nueve cursos. C1 y C2 inician en paralelo; C3 y C4 construyen bases paralelas; C5, C6 y C7 son rutas analíticas distintas; C8 integra; C9 sostiene la evolución. Álgebra, funciones, probabilidad y razonamiento cuantitativo deben estar disponibles desde la entrada y demostrarse antes de C5 y C7.

| Curso | Posición y propósito | Competencias | Prerrequisitos | Recibe | Prepara |
|---|---|---|---|---|---|
| C1. Formulación, exploración y comunicación de problemas con datos | Entrada. Convertir situaciones de decisión en preguntas y argumentos de evidencia. | Contexto, interesados, indicadores, exploración, visualización, comunicación y límites. | Razonamiento cuantitativo básico. | — | C3, C4 y el encuadre de C5–C9. |
| C2. Computación reproducible para Analytics | Entrada, paralela. Construir análisis programables y revisables. | Programación, estructuras de datos, transformación, documentación, control de versiones y pruebas básicas como preparación para automatizarlas. | Razonamiento lógico básico. | — | C3, C4, C5 y C8. |
| C3. Ingeniería y gobierno de datos analíticos | Base. Hacer los datos aptos y responsables para análisis y productos. | Modelado, consulta, integración, procedencia, calidad, validación de datos, acceso, privacidad y gobierno. | C1 y C2. | Problema y cómputo reproducible. | C5, C6, C7, C8 y C9. |
| C4. Inferencia estadística y diseño de estudios | Base. Cuantificar incertidumbre y diseñar evidencia. | Variabilidad, muestreo, estimación, pruebas, intervalos, diagnóstico y diseños. | C1, C2 y probabilidad elemental. | Preguntas y cómputo. | C5, C6, C7 y C8. |
| C5. Representación, aprendizaje y validación de modelos | Núcleo predictivo. Generalizar a casos futuros con rigor. | Líneas base, validación, regresión, clasificación, agrupamiento, regularización, métricas e interpretación. | C3, C4 y álgebra lineal elemental. | Datos gobernados e incertidumbre. | C8 y C9. |
| C6. Causalidad y evaluación de intervenciones | Núcleo explicativo. Defender qué puede atribuirse a una acción. | Contrafactuales, confusión, aleatorización, cuasiexperimentos, validez y heterogeneidad. | C3 y C4. | Datos y diseño de estudio. | C8 y C9. |
| C7. Decisiones, simulación y optimización bajo incertidumbre | Núcleo prescriptivo. Elegir entre alternativas y restricciones. | Valor, simulación, sensibilidad, escenarios, optimización, robustez y trade-offs. | C3, C4 y matemáticas requeridas. | Datos, incertidumbre y alternativas. | C8 y C9. |
| C8. Diseño e integración de productos y soluciones analíticas | Convergencia. Convertir evidencia en una solución usable, adoptable y preparada para operar. | Requisitos, interfaz de decisión, prototipado, integración, validación de uso, requisitos operativos, cambio y documentación. | C5, C6 y C7. | Rutas predictiva, causal y prescriptiva. | C9. |
| C9. Operación y evolución de soluciones analíticas | Cierre. Mantener calidad, confiabilidad y valor tras la integración. | DataOps, ambientes de desarrollo/prueba/producción, pruebas automatizadas, orquestación, entrega controlada, observabilidad, monitoreo, deriva, incidentes, retroalimentación, valor, efectos y retiro. | C8. | Solución integrada y requisitos operativos. | Práctica profesional y retornos a C1–C8. |

C8 no requiere que una solución use modelos, causalidad y optimización a la vez. Requiere que se justifique cuáles de esas formas de evidencia son pertinentes.

# Fronteras entre cursos

| Transición | Frontera curricular |
|---|---|
| C1 → C2 | Formular y comunicar una pregunta no equivale a producir evidencia reproducible; C2 introduce código, transformaciones, registro y verificación. |
| C2 → C3 | Programar y versionar un análisis no equivale a diseñar datos reutilizables; C3 concentra esquemas, integración, procedencia, validación de datos, acceso y calidad. |
| C3 → C4 | Tener datos no convierte una comparación en evidencia; C4 aporta muestreo, incertidumbre y diseño. |
| C4 → C5 | Inferir sobre una población no es generalizar predicciones futuras; C5 usa líneas base, validación fuera de muestra y regularización. |
| C5 → C6 | Asociación predictiva no identifica el efecto de actuar; C6 trata contrafactuales, asignación y confusión. |
| C6 → C7 | Conocer un efecto no selecciona una acción; C7 incorpora objetivos, restricciones, utilidad, sensibilidad y robustez. |
| C7 → C8 | Una recomendación no es una solución utilizable y operable; C8 trabaja requisitos, interacción, integración, adopción, responsabilidades y condiciones de operación. |
| C8 → C9 | Integrar una solución no prueba que siga válida, confiable o valiosa; C9 convierte requisitos operativos en ambientes, pruebas automatizadas, orquestación, entrega, observabilidad, monitoreo, soporte y retiro. |

La visualización exploratoria inicia en C1; la inspección de modelos se desarrolla en C5; la interfaz para actuar corresponde a C8. Calidad y gobierno tienen su núcleo en C3; C2 enseña la base de pruebas y versiones; C9 automatiza y observa controles de datos, lógica y modelos durante la operación.

# Competencias transversales

| Competencia | Anclaje | Progresión |
|---|---|---|
| Formulación y valor | C1 | De definir decisión a revisar uso, valor y efectos en C9. |
| Comunicación y visualización | C1 | De explorar a diseñar interfaces y reportes operativos. |
| Reproducibilidad | C2 | De análisis documentado a cambios controlados en C9. |
| Ingeniería de ciclo de vida | C2 y C9 | De versiones y pruebas básicas a automatización, orquestación, entrega controlada, observabilidad y soporte. |
| Responsabilidad de datos | C3 | De propósito y acceso a impactos y retiro. |
| Incertidumbre y validación | C4 y C5 | De variación estadística a datos, modelos, uso y valor. |
| Colaboración interdisciplinaria | C1 y C8 | De interesados a coordinación entre dominio, producto y plataforma. |
| Ética, privacidad, equidad y seguridad | C1, C3 y C8 | De anticipar daño a justificar y vigilar automatización. |

Cada curso debe demostrar un objeto distinto: C1 una formulación; C2 un proceso reproducible; C3 un flujo de datos apto; C4 una conclusión bajo incertidumbre; C5 una generalización predictiva; C6 una atribución causal; C7 una recomendación; C8 una solución usable; C9 una operación sostenible.

# Mapa de contenidos

I = introducción; D = desarrollo; M = dominio esperado; — = fuera del alcance principal.

| Contenido | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Problemas, interesados, indicadores y valor | M | — | D | D | D | D | D | M | M |
| Preguntas descriptivas, predictivas, causales y prescriptivas | M | I | D | D | M | M | M | D | D |
| Exploración, visualización y narrativa | M | D | D | D | D | D | D | M | D |
| Programación y transformación | I | M | D | D | D | D | D | D | D |
| Reproducibilidad, documentación y versiones | I | M | D | D | D | D | D | M | M |
| Consulta, modelado e integración de datos | I | D | M | D | D | D | D | D | M |
| Procedencia, acceso, privacidad y gobierno | I | I | M | D | D | D | D | M | M |
| Calidad, limpieza y validación de datos | I | D | M | D | D | D | D | D | M |
| Probabilidad, muestreo y variabilidad | I | I | D | M | D | M | M | D | D |
| Estimación, pruebas, intervalos y diseño | I | D | D | M | D | M | D | D | D |
| Predicción, representación y validación | I | D | D | D | M | D | D | D | M |
| Interpretabilidad, sesgo y costos de error | I | I | D | D | M | M | M | M | M |
| Contrafactuales, confusión y efectos | I | — | D | D | D | M | D | D | D |
| Simulación, sensibilidad y optimización | I | D | D | D | D | D | M | D | D |
| Requisitos, prototipado, integración y adopción | D | I | D | I | D | D | D | M | D |
| Pruebas de lógica, datos y modelos | — | M | D | D | D | D | D | D | M |
| Automatización, orquestación y entrega controlada | — | I | D | — | D | — | — | D | M |
| Observabilidad, monitoreo, soporte, deriva y retiro | — | I | D | I | D | D | D | D | M |
| Colaboración y comunicación profesional | M | D | D | D | D | D | D | M | M |

# Qué queda deliberadamente fuera

No son obligatorios para toda la cadena: aprendizaje profundo y generativo, visión, lenguaje natural, recomendadores, grafos, series de tiempo avanzadas, inferencia bayesiana avanzada, aprendizaje por refuerzo, optimización a gran escala e investigación operativa especializada. Son electivos construidos sobre C3–C7.

También quedan fuera del tronco la simulación física con ecuaciones diferenciales, administración exhaustiva de redes y nube, desarrollo integral de plataformas, estrategia de plataformas de dos lados, liderazgo ejecutivo general y prototipado físico. Sus ideas transferibles —restricciones, iteración, recuperación y prueba de hipótesis— sí se incorporan. No toda solución debe culminar en aprendizaje automático, tablero o automatización, ni C9 pretende certificar administración de infraestructura.

# Evidencia documental

| Curso | PDF más determinantes |
|---|---|
| C1 | national-academies-data-science-for-undergraduates-2018.pdf; informs-analytics-framework-2024.pdf; usc-introduction-to-data-analytics.pdf |
| C2 | acm-computing-competencies-undergraduate-data-science-2021.pdf; national-academies-data-science-for-undergraduates-2018.pdf; dataops-06-definition.pdf |
| C3 | berkeley-data-c101-data-engineering.pdf; mit-professional-certificate-data-engineering.pdf; dataops-02-data-strategy.pdf; dataops-09-data-quality.pdf |
| C4 | national-academies-data-science-for-undergraduates-2018.pdf; berkeley-data-c102-data-inference-and-decisions.pdf; warwick-foundations-of-data-analytics.pdf |
| C5 | mit-data-science-and-machine-learning.pdf; acm-computing-competencies-undergraduate-data-science-2021.pdf; dataops-03-methodologies.pdf |
| C6 | national-academies-data-science-for-undergraduates-2018.pdf; berkeley-data-c102-data-inference-and-decisions.pdf; mit-data-science-and-machine-learning.pdf |
| C7 | mit-quantitative-methods-in-systems-engineering.pdf; mit-machine-learning-modeling-and-simulation-principles.pdf; informs-cap-pro-blueprint.pdf |
| C8 | mit-designing-and-building-ai-products-and-services.pdf; mit-rapid-prototyping-methodologies.pdf; dataops-04-lean-thinking.pdf; dataops-10-organization.pdf |
| C9 | dataops-01-the-problem.pdf; dataops-05-agile.pdf; dataops-06-definition.pdf; dataops-07-cdo.pdf; dataops-08-data-scientids.pdf; dataops-09-data-quality.pdf |

El resto del corpus actúa como contraste de alcance: informs-cap-essentials-blueprint.pdf e informs-cap-pro-blueprint.pdf aportan el ciclo profesional sin imponer ponderaciones de certificación; cambridge-business-analytics.pdf, pwc-data-and-analytics-academy.pdf y mit-data-leadership.pdf sostienen la orientación a decisión y adopción; mit-cloud-and-devops.pdf, mit-digital-platforms.pdf y mit-professional-certificate-data-science-and-analytics.pdf justifican capacidades de operación y electivos sin copiar programas profesionales.

# Riesgos y decisiones discutibles

Nueve cursos pueden parecer excesivos. Fusionar C5, C6 y C7 reduciría carga administrativa, pero borraría la distinción entre anticipar, atribuir y elegir. Si fuera imprescindible compactar, C6 y C7 pueden compartir un marco de métodos de decisión, con evidencias separadas.

C9 puede confundirse con infraestructura. Se mantiene porque DataOps atribuye a Analytics calidad, pruebas, automatización, observabilidad, seguimiento y valor aun cuando especialistas administren plataformas. El riesgo inverso es convertirlo en una certificación de herramientas: el currículo exige comprender y especificar controles operativos, colaborar en su implementación y juzgar sus resultados, no administrar toda la infraestructura. C8 tampoco acredita un producto comercial terminado: demuestra coherencia entre necesidad, datos, método, interacción, requisitos operativos, responsabilidades y seguimiento.

La matemática puede excluir si se oculta o se impone sin apoyo. La decisión es nivelar y demostrar competencia antes de cursos que la usan, no reducir inferencia, causalidad u optimización a recetas. Por último, una unidad ética aislada puede complementar, pero no sustituye decisiones situadas sobre datos, modelos, uso y retiro.

# Arquitectura final resumida

    C1 Formulación y comunicación ─┐
                                  ├─> C3 Ingeniería y gobierno de datos ─┐
    C2 Computación reproducible ──┘                                      ├─> C5 Aprendizaje y validación ─┐
    C1 + C2 + probabilidad ─────────> C4 Inferencia y diseño ────────────├─> C6 Causalidad e intervención ─┼─> C8 Diseño e integración ─> C9 Operación y evolución
    C3 + C4 + matemáticas ────────────────────────────────────────────────└─> C7 Decisiones, simulación y optimización ─┘

Las flechas son dependencias de aprendizaje, no un proceso profesional rígido. La operación puede devolver hallazgos a problema, datos, modelos o decisión; la condición es mantener trazabilidad hacia el problema y las personas afectadas.
