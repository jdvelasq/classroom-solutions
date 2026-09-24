# Currículo macro — Productos de Datos

## Rol en el programa

Curso que diseña, entrega, gobierna y evoluciona capacidades de datos y analítica para consumidores definidos. Integra producto de datos, producto analítico, MLOps y DataOps sin reducirse a Ingeniería de Software, UX aislado o certificación de herramientas.

Es el único curso que convierte deliberadamente un activo de datos o un artefacto analítico en una oferta para un consumidor: usuario, necesidad, valor, modo de consumo, contrato, propiedad, responsabilidad y evolución. Un modelo, tablero o recomendación aislados no satisfacen por sí mismos esa definición.

No tiene prerrequisitos formales ni implícitos: cualquier estudiante de posgrado puede cursarlo sin haber visto analítica, ciencia de datos o machine learning. En consecuencia, el curso debe proporcionar el contexto mínimo necesario para entender y operar una capacidad analítica; no puede pedir que el estudiante llegue con un modelo ya construido ni con experiencia previa en notebooks, bibliotecas de ML o proyectos de datos.

La secuencia siguiente es conceptual, no un calendario ni una asignación de duración.

En la programación detallada, una sesión puede incluir varios `PRE_*` autocontenidos cuando su complejidad y progresión pedagógica lo permitan.

## Estructura de la oferta

La oferta se organiza en ocho sesiones. Esta secuencia concreta prevalece para Productos de Datos sobre la distribución general de sesiones de posgrado:

| Sesión | Modalidad | Contenido confirmado |
|---:|---|---|
| 1 | Fundamentación | Estrategia de datos: cómo una organización identifica, prioriza y sostiene iniciativas analíticas y de ML. Usa `curriculum/dataops-02-data-strategy.pdf`. |
| 2 | Fundamentación | Metodologías para llevar a la práctica una iniciativa analítica definida: encuadre, datos, desarrollo, validación, despliegue y evolución. Usa `curriculum/dataops-03-methodologies.pdf`. |
| 3 | Fundamentación | Fundamentos teóricos de DataOps y MLOps: flujos de innovación y valor, calidad, automatización, colaboración y operación. La presentación de esta sesión está pendiente de diseñar a partir del material DataKitchen disponible en `curriculum/`. |
| 4–8 | Taller presencial | Cinco sesiones prácticas de 5 a 5,5 horas. Cada sesión articula una secuencia de `PRE_*` autocontenidos, de distintas duraciones, para explicar y llevar DataOps/MLOps a la práctica. |

## Condición de entrada y nivelación

DataOps y MLOps no comienzan con una herramienta ni con un conjunto de reglas organizacionales: hacen operables prácticas de construcción de software aplicadas a datos y modelos. El material de DataKitchen que respalda este curso presupone control de versiones, pruebas automáticas de código y datos, ramas e integración, ambientes, parametrización, reutilización, contenerización y despliegue automatizado.

Por tanto, el curso **no presupone un título de ingeniería de sistemas ni conocimientos previos de analítica/ML**, pero debe construir una competencia de programación profesional básica antes de introducir DataOps/MLOps. La mayoría de estudiantes requerirá nivelación; no basta con haber usado notebooks, scripts lineales o bibliotecas de ML.

La nivelación debe permitir que cada estudiante pueda:

- convertir un script analítico en un paquete pequeño, legible y modular;
- usar Git para crear cambios pequeños, interpretar un historial, resolver un conflicto sencillo y colaborar mediante una rama y una revisión;
- gestionar dependencias, configuración y secretos sin fijarlos en el código;
- escribir y ejecutar pruebas unitarias y de integración básicas, interpretar sus fallos y corregirlos;
- usar la terminal, entornos aislados y estructuras de proyecto reproducibles;
- documentar cómo ejecutar, verificar y entregar una capacidad analítica.

Esta condición se verifica mediante un diagnóstico práctico y una actividad de nivelación con recuperación. Quien no la alcance completa apoyos y práctica adicional antes de los componentes de DataOps y MLOps; no se debe introducir su marco de prácticas como si compensara carencias de programación. El diagnóstico sirve para personalizar la ruta, no para excluir a quien no trae formación técnica.

El umbral se considera alcanzado cuando el estudiante entrega un repositorio pequeño que otra persona puede clonar, instalar, ejecutar y verificar; la revisión evalúa estructura, configuración, pruebas, historial de cambios y documentación, no solo que el resultado numérico sea correcto.

## Unidades

### 0. Fundamentos y nivelación: capacidades analíticas operables

Contexto mínimo y práctica aplicada sobre qué son datos, transformaciones, reglas analíticas, modelos y métricas; no busca enseñar EDA, estadística o modelado en profundidad. Incluye diagnóstico y nivelación de organización de un proyecto Python, modularidad, interfaces, manejo de errores, dependencias, configuración, Git, pruebas y ejecución reproducible. Se trabaja con una transformación y un modelo pequeño, entregados o construidos de forma guiada: el objetivo no es enseñar analítica ni diseño de software avanzado, sino llegar a un estándar mínimo de código mantenible y verificable que permita aprender DataOps/MLOps con sentido.

### 1. Productos de datos y productos analíticos

Dos acepciones relacionadas: activo de datos curado, descubrible y confiable para un consumidor; y capacidad analítica que permite observar, predecir, decidir o actuar. Consumidor, propiedad, contexto, contrato y propuesta de valor.

### 2. Descubrimiento y encuadre de producto

Necesidad, tarea o decisión del usuario, actores, hipótesis de valor, requisitos funcionales y no funcionales, riesgos, métrica de adopción y límites de uso.

### 3. Interacción humano–IA y adopción

Flujos de uso, explicaciones, supervisión humana, consentimiento, accesibilidad, confianza apropiada y validación de utilidad antes de escalar.

### 4. Ciclo de vida de una capacidad analítica

De experimento a servicio, y de servicio a monitoreo, mejora o retiro. Tubería de Innovación y Tubería de Valor; roles y responsabilidades en el ciclo.

### 5. Reproducibilidad y trazabilidad

Versionado de código, datos, modelos, configuraciones y prompts; registro de experimentos, artefactos, linaje y documentación. La práctica se organiza alrededor de las siete reglas de implementación de DataKitchen —pruebas de datos y lógica; control de versiones; ramas y fusión; ambientes múltiples; reutilización y contenedores; parametrización; trabajo sin miedo ni heroísmo—. MLflow puede ser un ejemplo, no el objeto del curso.

### 6. Empaquetamiento y entrega

Servicios, APIs, contratos de entrada/salida, ambientes, contenerización y despliegue reproducible como medios para entregar una capacidad analítica a un consumidor.

### 7. Calidad y pruebas de productos analíticos

Pruebas de datos, lógica y modelos; pruebas unitarias, integración, regresión, desempeño y humo; automatización de controles de calidad.

### 8. Operación, observabilidad y evolución

Métricas de servicio y valor, monitoreo de datos y modelos, deriva, alertas, incidentes, recalibración, mejora y retiro seguro.

### 9. Gobierno y seguridad operacional

Acceso, privacidad, secretos, auditoría, documentación, aprobación humana, trazabilidad de decisiones y cumplimiento de condiciones de uso.

### 10. Lean, Agile y DataOps

Flujo de valor, priorización, entrega continua, colaboración entre negocio/datos/tecnología, organización de equipos y eliminación de heroísmo.

### 11. Tendencias de productos analíticos

Diseño, evaluación y operación responsable de soluciones LLM, RAG y agénticas cuando el caso lo requiera: fundamentación, latencia, robustez, permisos, memoria y límites de autonomía.

### 12. Microproyectos de producto y operación

Casos `PRE_*` autocontenidos que recorren una unidad completa de valor: consumidor → contrato → entrega; experimento → registro → empaquetamiento; o servicio → monitoreo → respuesta a deriva. No requieren capstone.

## Bases de diseño curricular

Las presentaciones y referencias en `curriculum/` se usan como fuentes de diseño, con el siguiente papel: DataKitchen para el flujo DataOps y sus prácticas operativas; INFORMS para el encuadre del problema, despliegue y gestión del ciclo de vida; ACM y Berkeley para delimitar las competencias de programación, desarrollo, pruebas, gobierno y decisión responsable; y los materiales de MIT para producto de IA, interacción humano–IA, DevOps, métricas de operación y APIs. La matriz de aplicación concreta se conserva en `referencias-curriculares.md`.

## Frontera curricular

Productos hace visible y entrega una capacidad analítica como una oferta utilizable, confiable y sostenible. Los ejemplos de analítica o machine learning son deliberadamente simples: aportan solo el mínimo de datos, transformación, modelo y métrica necesario para comprender el caso. El trabajo se concentra en la práctica específica de programación, DataOps o MLOps que se desea exponer —por ejemplo, una prueba, un contrato, el versionado, el registro, el despliegue o el monitoreo—, no en enseñar EDA, estadística, modelado u optimización en profundidad.
