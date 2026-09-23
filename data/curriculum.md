# Currículo macro — Data para Analytics

## Identidad y lugar curricular

Curso optativo de pregrado que desarrolla la capacidad de convertir fuentes heterogéneas en activos confiables, reproducibles, documentados y adecuados para un consumidor analítico. Acompaña a **Fundamentos de Analítica**: este formula y responde preguntas con datos; Data para Analytics hace posible que esos datos sean utilizables con confianza.

No es un curso de Bases de Datos ni una introducción abreviada a Ingeniería de Datos. El curso usa representación relacional y SQL como alfabetización para integrar, transformar y verificar datos; no cubre diseño formal de bases de datos, administración, optimización o infraestructura. De igual manera, introduce escala, eventos y streaming para razonar sobre requisitos y *trade-offs*, sin formar en la implementación u operación de plataformas.

La relación con Fundamentos de Analítica es de **correquisito flexible**:

```text
Fundamentos de Analítica: problema → análisis → hallazgo → decisión
                                      ↕
Data para Analytics: fuente → preparación → confianza → consumo
```

Fundamentos explica qué aprender o decidir con datos. Este curso explica qué debe ocurrir para que esos datos merezcan confianza y puedan consumirse de forma repetible.

La secuencia siguiente es conceptual, no un calendario ni una asignación de duración. En la programación detallada, una sesión puede incluir varios `PRE_*` autocontenidos cuando su complejidad y progresión pedagógica lo permitan.

Los `PRE_*` son evidencia y vehículo de la práctica presencial; el marco conceptual y el vocabulario necesario se preparan antes y se aplican durante los minicasos. Esta modalidad permite atender una cohorte masiva y disciplinariamente diversa sin transformar la clase en una capacitación de plataforma.

## Resultado de aprendizaje integrador

Al terminar, el estudiante podrá partir de una necesidad analítica y diseñar, construir y justificar un flujo de datos acotado que integre fuentes, aplique transformaciones explícitas, controle calidad y cambios, documente procedencia y entregue una representación estable para un consumidor analítico.

El estudiante no será evaluado por administrar servidores, desplegar servicios, optimizar motores, ni operar herramientas cloud o de orquestación.

## Resultados de aprendizaje

1. Formular una necesidad de datos a partir de una pregunta analítica y explicitar grano, fuentes, transformaciones y consumidor.
2. Integrar y transformar datos relacionales, tabulares y semiestructurados sin alterar su significado analítico.
3. Construir un flujo reproducible con capas explícitas, validaciones y comportamiento seguro ante reejecución y cambio.
4. Evaluar la aptitud de un activo de datos mediante calidad, contrato, metadatos, linaje, privacidad y responsabilidad.
5. Diseñar una representación de datos estable y justificar decisiones de arquitectura según necesidades analíticas, no según tecnologías de moda.

## Límites explícitos

| Pertenece al curso | No pertenece al curso |
|---|---|
| Grano analítico, integración, transformación y validación | Normalización formal, dependencias funcionales, índices, tuning y administración de bases de datos |
| Archivos, tablas, APIs y datos semiestructurados | Diseño y operación de APIs, backends, autenticación implementada y servidores |
| Capas de datos, pipeline reproducible, incrementalidad y fallas controladas | Airflow, dbt, Kafka, Spark, Docker, CI/CD, Kubernetes, Terraform o infraestructura cloud implementados |
| Calidad, contratos, metadatos, linaje, privacidad y serving | Observabilidad, SRE y acuerdos de nivel de servicio de plataforma |
| Batch, eventos y streaming como decisiones y *trade-offs* | Certificación o especialización en ingeniería de datos de producción |

## Unidades

Los veintiséis `PRE` son unidades desarrollables y evaluables; no son, por sí mismos, veintiséis clases de tres horas.

### 1. Fundamentos de procesamiento por clave--valor

Después de la inducción, pares clave--valor, consultas MapReduce, paralelismo local, particiones, claves calientes y preagregación hacen visibles los fundamentos de Big Data Analytics. Incluye `PRE_02` a `PRE_06`; no requiere Spark, Hadoop ni un clúster.

### 2. Representación e integración para Analytics

Entidades, claves, relaciones, integridad y SQL se usan para preservar el significado y el grano de un resultado analítico al separar, combinar y reconciliar datos. Incluye `PRE_07` a `PRE_09`; no es diseño formal ni administración de bases de datos.

### 3. Transformación y organización analítica

Tipado, faltantes, deduplicación, estandarización, grano analítico y un mart simple convierten registros operacionales en una representación apta para preguntas recurrentes. Incluye `PRE_09` y `PRE_10`.

### 4. Formatos, estructuras y almacenamiento para consumo

Formatos físicos, particiones y datos semiestructurados se comparan según la estructura, el acceso y el consumidor analítico. Incluye `PRE_11` a `PRE_13`; no forma en plataformas lakehouse.

### 5. Adquisición y trazabilidad de fuentes

Archivos, bases y APIs se adquieren con control de completitud, errores y evidencia de origen, preservando una capa raw distinguible del dato preparado. Incluye `PRE_14` y `PRE_15`.

### 6. Flujos reproducibles de preparación

Fuentes, capas raw, staging y curated, validaciones, configuración y ejecución desde estado limpio transforman una secuencia manual en un pipeline reproducible. Corresponde a `PRE_16`.

### 7. Confianza: calidad y contratos

Completitud, validez, unicidad, consistencia y frescura determinan si un dato puede avanzar. Los contratos hacen explícita la interfaz, detectan cambios incompatibles y permiten fallar o poner en cuarentena de manera controlada. Incluye `PRE_17` y `PRE_18`.

### 8. Continuidad y operación acotada

Incrementalidad, checkpoints, idempotencia, dependencias, reintentos y fallas deterministas permiten actualizar datos sin corromper resultados ni confundir un problema de datos con un problema transitorio. Incluye `PRE_19` y `PRE_20`.

### 9. Escala, eventos y tiempo

Particiones, evaluación diferida, eventos, estado, ventanas y llegada tardía se estudian como condiciones que cambian una decisión de arquitectura y la interpretación de un resultado. Incluye `PRE_21` a `PRE_23`; no es entrenamiento de Spark, Kafka ni streaming productivo.

### 10. Serving, metadatos y linaje

Un activo curado debe exponerse con grano, esquema y mecanismo apropiados para cada consumidor, además de contar con propiedad, catálogo, procedencia y evaluación de impacto. Incluye `PRE_24` y `PRE_25`.

### 11. Arquitectura de datos orientada a Analytics

Fuentes, necesidades de consumidores, procesamiento, controles y decisiones se conectan en una arquitectura justificable por requisitos y riesgos. `PRE_26` integra capacidades ya conocidas; no introduce una tecnología nueva.

## Auditoría conceptual de los PRE existentes

Los nombres y la secuencia sí son compatibles con la identidad del curso. Su formulación en verbo y problema —por ejemplo, “Integrar datos con SQL”, “Detectar datos que no deberían pasar” y “Preparar datos para quien los va a consumir”— comunica una acción al servicio de Analytics, no una tecnología.

Se hacen estas precisiones de diseño:

| Grupo | Decisión macro |
|---|---|
| PRE 01–06 | Inducción y fundamentos de escala: clave--valor, paralelismo, particiones y sesgo. No se convierten en capacitación de plataforma. |
| PRE 07–10 | Nivelación relacional, SQL, transformación y mart analítico; evitan derivar hacia diseño formal de bases de datos. |
| PRE 11–16 | Representación, adquisición y reproducibilidad; privilegian significado, integridad y reejecución sobre automatización de producción. |
| PRE 17–20 | Confianza y continuidad: calidad, contratos, incrementalidad y operación acotada. |
| PRE 21–26 | Eventos, streaming, serving, metadatos, linaje y arquitectura; no se convierten en BI, APIs ni productos de datos. |

## Minicasos y didáctica

Los `PRE` son minicasos independientes, focalizados en una capacidad particular. No requieren un dataset ni una historia común: cambiar de dominio ayuda a que el estudiante distinga el principio transferible de los detalles de un contexto específico.

La coherencia del curso proviene de una progresión de capacidades —representar, integrar, transformar, adquirir, asegurar, actualizar, servir y justificar— y de preguntas recurrentes de Analytics: ¿qué representa cada registro?, ¿puedo confiar en este resultado?, ¿qué cambió?, ¿de dónde vino este dato? y ¿quién lo necesita?

Cada minicaso comienza por una pregunta analítica que no puede responderse con confianza y termina con un activo de datos o decisión que hace posible responderla. Los ejercicios deben ser deterministas, ejecutables localmente y manejables por una cohorte masiva. La dificultad reside en decisiones de datos observables, no en instalación, credenciales o configuración de infraestructura.

## Estándar de diseño 10/10 para cada PRE

Un PRE se considera listo para desarrollo solo si cumple todos los criterios siguientes:

1. Declara una pregunta analítica, un consumidor y el grano del resultado esperado.
2. Tiene un único aprendizaje central, en lenguaje simple y verificable.
3. Parte de una falla, ambigüedad o restricción de datos observable; no de una definición tecnológica aislada.
4. Produce un activo concreto —dataset, vista, mart, contrato, manifiesto o decisión arquitectónica— que demuestre de manera verificable el aprendizaje del minicaso.
5. Incluye validaciones visibles de significado analítico: grano, completitud, reconciliación, idempotencia, contrato o trazabilidad, según corresponda.
6. Contiene pruebas automáticas deterministas, criterios de aceptación y una solución docente completa, ejecutable e independiente. La solución se ubica exclusivamente en `notebooks/notebook.ipynb` cuando es un desarrollo didáctico interactivo o exclusivamente en `src/main.py` cuando corresponde a un programa Python; nunca en ambos ni en la raíz del PRE.
7. Delimita explícitamente lo que no se enseña, para evitar deriva hacia Bases de Datos, Ingeniería de Datos de producción, BI o Productos de Datos.
8. Puede realizarse con herramientas locales y sin cuentas, nube, instalación pesada ni dependencias frágiles.
9. Es apropiado para estudiantes de pregrado de diversas carreras: explica el vocabulario indispensable y evalúa criterio, no experiencia previa de plataforma.
10. Conecta de forma explícita con Fundamentos de Analítica y con el PRE anterior o siguiente.

## Forma didáctica de la solución

La solución docente se ubica donde mejor hace visible el aprendizaje central; la elección no depende de que el repositorio sea docente o estudiante.

| Forma | Usar cuando el aprendizaje requiere | Ejemplos en Data para Analytics |
|---|---|---|
| `notebooks/notebook.ipynb` | Alternar datos visibles, código corto, resultado y discusión; revelar progresivamente una transformación, un grano, una validación o un *trade-off*. | representación relacional, SQL, transformación, formatos, calidad, contratos, incrementalidad, eventos, ventanas y arquitectura. |
| `src/main.py` | Ejecutar un proceso completo y reproducible cuya lógica ya se entiende; separar etapas, materializar artefactos o demostrar una interfaz o comportamiento operacional. | ingestión batch, simulador de API, pipeline por capas, operación de pipeline y serving programático. |

Un notebook puede llamar funciones pequeñas de `src/` solo cuando estas no oculten el razonamiento que se quiere enseñar. Un programa Python debe imprimir o persistir evidencia suficiente para que el docente pueda discutir su resultado; no se acepta una ejecución opaca. Los `PRE` no incluyen `README.md`: el docente conduce el problema, el razonamiento y la solución paso a paso durante la clase.

## Secuencia de desarrollo

1. Validar este diseño macro y la selección de minicasos independientes.
2. Revisar y normalizar las especificaciones de los veintiséis PRE contra el estándar 10/10.
3. Implementar los PRE por bloques de sesión, empezando por 01–04 y sus artefactos compartidos.
4. Para cada PRE: construir datos de entrada, notebook, validaciones, pruebas, solución de referencia y guía docente; ejecutar todo desde un estado limpio.
5. Ejecutar una prueba de extremo a extremo de las diez sesiones y una revisión específica de carga operativa para una cohorte de aproximadamente 130 estudiantes.
