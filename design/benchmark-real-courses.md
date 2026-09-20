# Contraste con programas de educación continua del corpus

## Alcance y método

Esta revisión contrasta los seis cursos reales contra los programas de educación continua y cursos profesionales incluidos en `curriculum/`. No compara el diseño con los archivos o talleres existentes en los directorios de curso. Su objetivo es verificar que los temas macro y las fronteras de [macro-topics.md](macro-topics.md) representen una traducción rigurosa de la evidencia, adecuada a la arquitectura real: dos cursos de pregrado de 13 semanas y cuatro cursos de posgrado de ocho sesiones, con talleres `PRE_*` pequeños, autocontenidos y basados en situaciones realistas simplificadas.

La escala de 0 a 10 evalúa el diseño **macro**, no duración de cada tema, calidad futura de los talleres ni resultados de estudiantes. Un 10 significa: cobertura esencial, identidad propia, frontera clara, ciclo profesional y responsabilidad transversal.

## Hallazgo global

Los programas de educación continua confirman la arquitectura de ciclo completo, pero suelen mezclar varias competencias porque son certificados largos, orientados a roles o a una pila tecnológica. El programa CLASSROOM no debe imitarlos módulo por módulo. Debe extraer sus competencias esenciales y asignarlas una sola vez a la pregunta curricular que les corresponde.

| Patrón del benchmark | Decisión para CLASSROOM |
|---|---|
| Los certificados de MIT combinan datos, ML, optimización, despliegue y, a veces, interfaces en programas de varios meses. | Desagregar por pregunta profesional en los seis cursos; no convertir un curso corto en una copia abreviada de un certificado. |
| Berkeley separa Ingeniería de Datos de Data, Inference, and Decisions, con prerrequisitos fuertes. | Fundamentos de Datos es un curso propio; Predictiva desarrolla inferencia aplicada, validación y el pivote causal sobre una base nivelada. |
| Cambridge enseña descriptiva, predictiva y prescriptiva como metodologías para decidir, junto con sesgos y experimentación. | Fundamentos introduce el mapa, los sesgos y los límites; cada curso posterior desarrolla solo su metodología. |
| Los materiales DataOps distinguen innovación de producto y operación sostenida. | Productos de Datos enseña producto de datos/producto analítico y usa MLOps/DataOps como disciplinas de entrega y ciclo de vida, no como curso de Ingeniería de Software. |

## Resultado por curso

| Curso real | Evidencia comparada | Ajuste derivado del benchmark | Calificación macro |
|---|---|---|---:|
| **Fundamentos de Analítica** | Cambridge Business Analytics; MIT Professional Certificate in Data Science and Analytics; INFORMS. | Mantiene encuadre, tipos de analítica, valor, sesgos, experimentación y gobierno. Sus `PRE_*` nivelan para posgrado; no desarrollan algoritmos de los cursos posteriores. | **10** |
| **Fundamentos de Datos para Analítica** | Berkeley Data C101; MIT Professional Certificate in Data Engineering; USC. | Mantiene arquitectura, integración, transformación, calidad, contratos, linaje y serving. Excluye teoría completa de bases de datos, certificaciones de herramientas y el producto final. | **10** |
| **Analítica Descriptiva y Visualización de Datos** | USC Introduction to Data Analytics; Cambridge; Warwick. | Añade diagnóstico guiado por hipótesis y sostiene EDA, percepción, narrativa y límites de interpretación. Los resúmenes estadísticos son lenguaje de evidencia, no el objeto del curso. | **10** |
| **Analítica Predictiva** | Berkeley Data C102; MIT Data Science and Machine Learning; PwC Advanced and Predictive Analytics. | Centra encuadre, evaluación, calibración, incertidumbre, costo de error y pivote predictivo–causal. Deep learning, recomendadores, grafos y series de tiempo avanzadas quedan electivos. | **10** |
| **Analítica Prescriptiva** | MIT Machine Learning, Modeling, and Simulation Principles; MIT Quantitative Methods in Systems Engineering; MIT Professional Certificate in Data Science and Analytics; INFORMS. | Mantiene optimización, simulación, incertidumbre, sensibilidad, valor y comunicación de políticas. Excluye demostraciones exhaustivas de métodos de IO y administración de solvers. | **10** |
| **Productos de Datos** | MIT Designing and Building AI Products and Services; MIT Cloud & DevOps; DataOps 04–06, 09–10. | Incorpora explícitamente descubrimiento de producto, interacción humano–IA y adopción; MLOps/DataOps, pruebas, observabilidad y gobierno operan la capacidad analítica, sin desplazar su identidad de producto. | **10** |

## Lectura detallada de la evidencia

### Fundamentos de Analítica

Cambridge organiza un programa ejecutivo de 11 semanas alrededor de sesgos, experimentación y análisis descriptivo, predictivo y prescriptivo para la toma de decisiones. El certificado de MIT combina incertidumbre, correlación, clustering, regresión, optimización, equidad, causalidad y transformación digital. Ambos confirman que el vocabulario de decisiones, riesgos, experimentación y tipos de evidencia debe aparecer temprano.

La conclusión no es trasladar su temario técnico a Fundamentos. El curso tiene una función distinta: permitir que el estudiante identifique la pregunta, el tipo de evidencia pertinente y el riesgo de pedir a una técnica una conclusión que no puede justificar. Sus `PRE_*` sirven como nivelación práctica inicial para el posgrado.

### Fundamentos de Datos para Analítica

Berkeley C101 define Ingeniería de Datos como gestión de datos a escala para análisis y ML, con atención a operacionalización confiable y escalable. El certificado de MIT cubre arquitectura, warehouse, modelo de datos, pipelines, automatización y big data; USC evidencia una ruta práctica donde SQL, integración y almacenamiento analítico preceden visualización.

La evidencia respalda un curso independiente de datos, pero también advierte contra copiar su amplitud de herramientas: el certificado de MIT incluye tecnologías y hasta ML avanzado por razones de empleabilidad. En CLASSROOM, la identidad se conserva al preguntar cómo se hacen los datos disponibles y confiables para otros consumidores, no cómo se certifica una plataforma.

### Analítica Descriptiva y Visualización de Datos

USC sitúa el trabajo con bases de datos, SQL y estructuras analíticas antes de visualización y tableros. Cambridge trata el análisis descriptivo como una metodología para interpretar resultados de negocio, mientras Warwick mezcla bases de datos, limpieza, SQL y minería en un módulo de fundamentos. En conjunto, la evidencia respalda que Descriptiva requiera datos manipulables y que su producto sea evidencia inteligible, no una tabla de estadísticos.

Por ello se incorporó diagnóstico guiado por hipótesis, sin confundirlo con inferencia causal. El curso usa distribuciones, tasas y variabilidad para leer los datos; no se convierte en Estadística básica porque la competencia dominante es explorar, representar y comunicar evidencia para una audiencia y una decisión.

### Analítica Predictiva

Berkeley C102 integra fundamentos probabilísticos, diseño experimental, causalidad, clustering, recomendación y herramientas de ML, pero lo hace como un curso avanzado con prerrequisitos formales. El programa de MIT organiza regresión, clasificación, hipótesis, deep learning, recomendadores y grafos a lo largo de 12 semanas. PwC incorpora preparación, desarrollo, validación y despliegue de modelos en una ruta más amplia de analítica avanzada.

La traducción correcta no es “otro curso de ML”. El núcleo debe empezar por la unidad de predicción, horizonte, costo de error y protocolo de evaluación; continuar con modelos y validación; y terminar con el límite entre predicción y causalidad. Los métodos de alta especialización siguen siendo electivos, pues el benchmark los presenta como ampliaciones en programas más largos, no como condición mínima de toda formación analítica.

### Analítica Prescriptiva

Los programas de MIT unen modelado, optimización, simulación Monte Carlo, pronóstico probabilístico, sensibilidad, trade-offs y casos. La evidencia de INFORMS sitúa la prescripción donde se intersectan el paradigma centrado en datos y el centrado en problemas: una recomendación requiere objetivo, restricciones, variables de decisión y consecuencias, no solo una técnica matemática.

La frontera queda clara: el curso usa optimización, simulación, reglas y análisis de decisión para formular una política defendible bajo incertidumbre. No pretende reemplazar un programa de Investigación de Operaciones con teoría completa de colas, dualidad, demostraciones de algoritmos o administración avanzada de solvers.

### Productos de Datos

MIT Designing and Building AI Products and Services dedica sus ocho semanas a proceso de diseño, tecnologías de IA, resolución de problemas, interacción humano–computador, organizaciones y fronteras de mercado. MIT Cloud & DevOps cubre nube, contenedores, DevOps, seguridad, casos, agilidad y operación. Los documentos DataOps separan explícitamente ideación/incepción/investigación y desarrollo de transición, producción, monitoreo y retiro.

La comparación corrige una reducción posible: Productos no es simplemente MLOps/DataOps. Su objeto es una capacidad con consumidor, valor, contrato, propiedad y evolución. MLOps/DataOps proporciona las prácticas para que esa capacidad sea trazable, comprobable, desplegable, observable y gobernada. La interacción humano–IA y la adopción entran porque el producto debe ser utilizable; la Ingeniería de Software general queda fuera porque no resuelve por sí misma una pregunta de valor analítico.

## Implicaciones para la fase de programación

1. Cada tema macro debe convertirse en uno o varios `PRE_*` solo si puede expresarse como una situación profesional realista simplificada, con entrada, tensión, decisión o consumidor y resultado verificable.
2. La procedencia del caso puede ser Kaggle, una organización, un libro o un ejemplo adaptado de herramienta; la prueba es conservar la pregunta profesional, no la marca tecnológica.
3. Los programas continuos sirven para verificar cobertura y fronteras, no para imponer capstones, duración, herramientas propietarias ni el orden exacto de sus módulos.
4. La programación detallada debe empezar por Fundamentos de Analítica, porque sus `PRE_*` establecen la nivelación compartida que los cuatro cursos de posgrado retomarán.

## Fuentes del corpus revisadas

- Datos y descriptiva: [Berkeley Data C101](../curriculum/berkeley-data-c101-data-engineering.pdf), [MIT Professional Certificate in Data Engineering](../curriculum/mit-professional-certificate-data-engineering.pdf), [USC Introduction to Data Analytics](../curriculum/usc-introduction-to-data-analytics.pdf), [Warwick Foundations of Data Analytics](../curriculum/warwick-foundations-of-data-analytics.pdf).
- Predicción y decisión: [Berkeley Data C102](../curriculum/berkeley-data-c102-data-inference-and-decisions.pdf), [MIT Data Science and Machine Learning](../curriculum/mit-data-science-and-machine-learning.pdf), [MIT Professional Certificate in Data Science and Analytics](../curriculum/mit-professional-certificate-data-science-and-analytics.pdf), [MIT Machine Learning, Modeling, and Simulation Principles](../curriculum/mit-machine-learning-modeling-and-simulation-principles.pdf), [MIT Quantitative Methods in Systems Engineering](../curriculum/mit-quantitative-methods-in-systems-engineering.pdf).
- Encuadre, producto y operación: [Cambridge Business Analytics](../curriculum/cambridge-business-analytics.pdf), [MIT Designing and Building AI Products and Services](../curriculum/mit-designing-and-building-ai-products-and-services.pdf), [MIT Cloud & DevOps](../curriculum/mit-cloud-and-devops.pdf), [PwC Data & Analytics Academy](../curriculum/pwc-data-and-analytics-academy.pdf), [DataOps 04](../curriculum/dataops-04-lean-thinking.pdf), [DataOps 05](../curriculum/dataops-05-agile.pdf), [DataOps 06](../curriculum/dataops-06-definition.pdf), [DataOps 09](../curriculum/dataops-09-data-quality.pdf) y [DataOps 10](../curriculum/dataops-10-organization.pdf).
