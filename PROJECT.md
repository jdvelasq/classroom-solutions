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

### Estructura obligatoria de talleres y laboratorios

Todo taller `PRE_XX_activity_name/` y laboratorio `LAB_XX_activity_name/` conserva la misma estructura:

```text
PRE_XX_activity_name/
├── data/
├── notebooks/
├── src/
├── submission/
├── temp/
├── tests/
│   ├── __init__.py
│   └── test_src.py
└── __init__.py
```

`data/` contiene los insumos; `notebooks/` y `src/` el desarrollo; `submission/` los artefactos finales generados; `temp/` los intermedios descartables; y `tests/` las pruebas de validación. La estructura no se reorganiza, renombra ni simplifica durante el diseño o implementación de actividades.

Los directorios vacíos se preservan con `.gitkeep`.

- `data/`: datos de entrada requeridos por la actividad.
- `notebooks/`: notebooks con la solución completa del taller, cuando corresponda.
- `src/`: código Python de la solución completa cuando se requieran scripts, funciones reutilizables, simulaciones, lógica de optimización o interfaces.
- `submission/`: artefactos finales generados al ejecutar la solución; no se colocan manualmente solo para satisfacer pruebas.
- `temp/`: archivos temporales o intermedios.
- `tests/`: pruebas `pytest` usadas para validar y calificar la actividad.

### Principio de diseño de actividades

Cada actividad representa un caso práctico completo y su solución debe permitir desarrollo incremental durante una clase presencial. El problema real y la decisión que habilita organizan la actividad; un algoritmo, paquete o biblioteca se introduce solamente cuando ayuda a resolver ese problema.

La progresión de referencia es:

```text
problema
↓
datos
↓
enfoque analítico inicial
↓
limitación o problema de decisión
↓
razonamiento analítico mejorado
↓
lógica prescriptiva, cuando el caso requiera una decisión
↓
decisión recomendada
↓
salida generada
```

En cursos cuya pregunta no es prescriptiva, el flujo se detiene en la evidencia, predicción, producto o dato confiable que corresponde a su frontera curricular. Ninguna actividad se organiza principalmente como demostración de un algoritmo, paquete o biblioteca.

### Notebooks

Se usan notebooks cuando el razonamiento analítico se beneficia del desarrollo incremental, experimentación, visualización o interpretación. Su código debe ser conciso, legible, secuencial, con celdas razonablemente cortas y resultados intermedios cuando ayuden a explicar el razonamiento. Debe ser apto para *live coding*.

Los notebooks evitan Markdown excesivo, explicaciones extensas de estilo tutorial, abstracciones innecesarias y comentarios que narren sintaxis obvia de Python. Los comentarios aclaran el razonamiento analítico o computacional cuando sea útil. Una actividad puede contener uno o varios notebooks si ello mejora la progresión analítica.

Cuando una actividad incluya un modelo matemático explícito de decisión, su formulación algebraica pedagógica se muestra en comentarios Python concisos inmediatamente antes del código que lo implementa o resuelve. Se usa notación legible similar a AMPL —con conjuntos/índices, parámetros, cantidades derivadas, variables de decisión, objetivo y restricciones cuando correspondan— y no se oculta la formulación dentro de cálculos Python ni se fuerza en casos que no requieran optimización real.

### Código fuente

`src/` se usa para programas ejecutables, funciones reutilizables, simulaciones, lógica de optimización, modelos, interfaces u otros componentes que se expresen mejor como módulos o scripts Python. El código debe ser directo, legible, determinista, fácil de explicar y mínimamente abstraído.

No se introducen clases, frameworks, capas arquitectónicas, fábricas, sistemas de configuración o módulos auxiliares sin una necesidad pedagógica explícita. Se prefiere la implementación más simple que exponga claramente el razonamiento analítico.

### Datos, temporales y entregables

`data/` contiene solo los datos de entrada requeridos. Cuando un caso real sea demasiado grande o complejo, se reduce pedagógicamente preservando su estructura esencial de análisis o decisión y suficiente realismo para que la conclusión sea significativa.

`temp/` contiene artefactos intermedios o descartables, nunca resultados finales. `submission/` contiene exclusivamente los artefactos finales generados por ejecutar la solución completa; no se crean manualmente para satisfacer una prueba. Según el caso, pueden ser CSV, JSON, modelos entrenados, figuras, mapas, HTML, asignaciones, horarios, rankings, políticas, planes u otras salidas de decisión. En Prescriptiva, cuando aplique, representan la recomendación, decisión, asignación, política o plan resultante.

### Pruebas, reproducibilidad y dependencias

`tests/test_src.py` contiene pruebas de calificación con `pytest`. Las pruebas verifican resultados observables que importan: estructura, artefactos, columnas, tipos, valores con tolerancia, factibilidad, restricciones de capacidad/recursos, no negatividad, balance/conservación u otras propiedades esenciales de la solución. Deben ser simples, robustas y centradas en resultados, no en detalles irrelevantes de implementación.

Las soluciones deben ser deterministas y reproducibles cuando sea posible. Toda aleatoriedad necesaria usa semillas fijas; se evitan estado oculto, recursos externos inestables y dependencia de un orden accidental de ejecución. Con los mismos datos y entorno deben producirse los mismos artefactos de calificación.

Se usan los paquetes ya declarados en `requirements.txt`. No se agregan, eliminan ni modifican dependencias sin aprobación explícita; se prefiere siempre la pila existente.

### Disciplina de implementación

Antes de implementar una actividad se inspecciona su directorio existente, se comprende el caso y su objetivo de aprendizaje, y se preserva la estructura estándar. Se implementa únicamente lo necesario para esa actividad, se generan los artefactos esperados ejecutando la solución, se corren las pruebas pertinentes y se verifica comportamiento determinista. No se modifican actividades no relacionadas ni se rediseña la infraestructura del repositorio.

### Formato y limpieza de notebooks

La primera celda de código de todo notebook de taller comienza con una sola línea en español:

```python
# Problema: <descripción>
```

La descripción no excede 240 caracteres, plantea el problema del caso —no el método ni la solución— y deja exactamente una línea en blanco antes de la primera instrucción ejecutable. Cuando una celda comienza con comentarios, encabezados de sección o una formulación matemática, conserva la misma separación de una línea en blanco antes del código.

No se usan celdas solo de comentarios ni celdas Markdown para explicar el código. Los comentarios de sección explican el concepto analítico o de decisión, no repiten la operación Python.

Las figuras que se construyen progresivamente no se muestran incompletas. Se evita `plt.show()`, `display(fig)` o equivalentes hasta que estén completos paneles, anotaciones, leyendas y elementos interpretativos; la figura final se muestra una sola vez. Las salidas visibles evitan rutas absolutas de la máquina, depuración temporal, variables de construcción y tablas grandes que no aporten al objetivo pedagógico.

Antes de dar una actividad por terminada, el notebook se reinicia desde un kernel limpio y se ejecuta secuencialmente para confirmar ausencia de estado oculto, errores, figuras duplicadas o prematuras, rutas específicas de máquina y salidas de desarrollo.

### Portabilidad

Al evaluar una nueva dependencia aprobada, se verifica que sea compatible con el entorno y requisitos completos del curso, así como con las principales plataformas de estudiantes: macOS Apple Silicon, macOS Intel y Windows; Linux cuando sea práctico. Se prefieren paquetes `pip` con ruedas precompiladas y APIs Python antes que instalaciones dependientes de sistema, ejecutables externos, variables de entorno, licencias o cuentas. Una dependencia frágil o específica de plataforma no se vuelve obligatoria sin aprobación explícita y justificación pedagógica.
