# CLASSROOM — Contexto operativo común

## Cursos de pregrado ya definidos

Este marco aplica por ahora a los cursos reales **Fundamentos de Analítica** (`fundamentos/`) y **Fundamentos de Datos para Analítica** (`data/`); no se debe asumir para otros cursos de pregrado sin confirmación explícita.

- **Población:** estudiantes principalmente de Ingeniería de Sistemas y Computación, Ingeniería Industrial, Ingeniería Administrativa, Estadística y otros programas.
- **Duración y ritmo:** 13 semanas, con una sesión semanal de 3 horas.
- **Estructura:** las semanas 1 a 3 se destinan a fundamentación teórica; las semanas 4 a 13 a 10 talleres dirigidos, con varios talleres por sesión cuando corresponda.
- **Modelo pedagógico:** aula invertida para las sesiones prácticas.

## Cursos de posgrado

 - **Población:** reciben graduados con el mismo perfil disciplinar de los cursos de pregrado. Una proporción importante de estudiantes de pregrado los toma al final de su carrera mediante acceso anticipado; el resto incluye estudiantes de la Maestría en Analítica y graduados de otras universidades.
 - **Duración y ritmo:** 8 sesiones presenciales de 5 a 5,5 horas cada una.
 - **Estructura:** las sesiones 1 y 2 se destinan siempre a fundamentación teórica; las sesiones 3 a 8 a talleres presenciales, con varios talleres por sesión cuando corresponda.
 - **Modelo pedagógico:** aula invertida para las sesiones prácticas.

Este marco es común a todos los cursos de posgrado. Las decisiones de contenido, prerrequisitos y evaluación se documentan en el directorio de cada curso.

## Alcance y autoridad curricular

- El curso de posgrado **Big Data Analytics** existe, pero queda fuera de este análisis: no se considerarán su programa, sus contenidos ni sus posibles efectos sobre los demás cursos.
- El profesor titular tiene control curricular completo sobre los demás cursos que irá presentando; las propuestas podrán, por tanto, modificar de forma integral sus contenidos, secuencia y diseño pedagógico dentro de las restricciones operativas documentadas.

## Cursos de posgrado incluidos

- **Analítica Descriptiva y Visualización de Datos** — `descriptiva/`
- **Analítica Predictiva** — `predictiva/`
- **Productos de Datos** — `productos/`
- **Analítica Prescriptiva** — `prescriptiva/`

## Fase actual: diseño macro de temas

La primera fase define qué debe enseñarse en cada curso incluido, a nivel macro y con suficiente detalle para una programación posterior de sesiones, lecturas y talleres.

Para cada curso se seguirá un ciclo iterativo:

1. Proponer un diseño tentativo de temas.
2. Calificarlo frente a los referentes internacionales ya analizados, en una escala de 0 a 10.
3. Identificar brechas, redundancias y fronteras con los demás cursos.
4. Modificar el diseño y repetir la evaluación hasta alcanzar una calificación de 10.

El criterio de éxito de esta fase es que el conjunto de cursos forme un programa de excelencia en formación analítica, con coberturas complementarias y sin depender de contenidos del curso excluido Big Data Analytics.

## Regla común para talleres presenciales

- Cada taller presencial (`PRE_*`) presenta un caso pequeño, autocontenido y completo: simplifica deliberadamente una situación real para que pueda resolverse en aula, pero conserva la decisión, los datos, restricciones y tensiones que hacen auténtico el problema. Desarrolla la solución mínima necesaria y produce un resultado verificable dentro del mismo caso.
- Un `PRE_*` puede adaptar casos de Kaggle, libros, organizaciones reales o ejemplos de herramientas (por ejemplo, TensorFlow o Apache Pig). La procedencia no define su valor pedagógico: la adaptación debe plantear una pregunta profesional concreta, conservar su contexto y evitar convertirse en una demostración de comandos.
- Los `PRE_*` son miniproyectos de duración variable; algunos pueden ser muy cortos cuando una pregunta acotada —por ejemplo, convertir de forma confiable archivos CSV a JSON— permite practicar una capacidad completa dentro de una sesión.
- Los `PRE_*` de **Fundamentos de Analítica** cumplen además una función de articulación: son las sesiones iniciales y nivelatorias de los cursos de posgrado. Establecen un mínimo común práctico y de vocabulario antes de que cada curso de posgrado desarrolle su competencia propia; no sustituyen ese desarrollo posterior.
- Los talleres siguen el estilo de los ejemplos prácticos breves de proveedores y repositorios de referencia; no son componentes secuenciales de un proyecto mayor.
- Por esta razón, ningún curso requiere un proyecto integrador o *capstone*. La integración curricular se logra mediante fronteras y vocabulario compartidos, no mediante una única entrega acumulativa.
- El curso **Productos de Datos** se centra en MLOps, DataOps y tendencias afines. MLflow es una referencia histórica válida para introducir trazabilidad de experimentos y ciclo de vida de modelos, sin convertir el curso en una certificación de una herramienta.

### Referencias de estilo para `PRE_*`

- [cloudera-tutorial-assets](https://github.com/jdvelasq/cloudera-tutorial-assets)
- [hortonworks-hdp](https://github.com/jdvelasq/hortonworks-hdp)

Estos repositorios se usan como referentes de forma y nivel de concreción: ejemplos ejecutables, situaciones profesionales acotadas y resultados observables. No se copian ni fijan los contenidos del currículo.
