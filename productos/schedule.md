# Inventario heredado — Productos de Datos

## Programación confirmada

El curso tiene ocho sesiones. Las tres primeras son de fundamentación; las cinco restantes son talleres presenciales de 5 a 5,5 horas cada uno. Esta estructura es específica de Productos de Datos.

| Sesión | Tipo | Base o propósito |
|---:|---|---|
| 1 | Fundamentación | Estrategia de datos e iniciativas analíticas/ML — `curriculum/dataops-02-data-strategy.pdf`. |
| 2 | Fundamentación | Metodologías para ejecutar una iniciativa analítica — `curriculum/dataops-03-methodologies.pdf`. |
| 3 | Fundamentación | Teoría de DataOps y MLOps. Presentación pendiente de diseño con el material DataKitchen en `curriculum/`. |
| 4–8 | Talleres | Cinco sesiones prácticas de 5 a 5,5 horas; cada una articula una secuencia de `PRE_*` autocontenidos de distinta duración para explicar y llevar DataOps/MLOps a la práctica. |

Las duraciones individuales de las sesiones 4–8 y la selección de `PRE_BASE` se definirán después de discutir la secuencia de talleres. Por ello no se asignan todavía tiempos de diseño ni se declara una carga práctica total exacta.

## Propósito y lectura

Además de registrar la programación confirmada, este archivo inventaría material heredado de `PRE_*`; no propone todavía la selección de talleres ni modifica actividades. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. Las actividades encontradas se concentran en MLflow. Varias usan una estructura legado distinta de la estructura estándar de `PRE_*`; esta observación se registra, pero no autoriza reorganizarlas.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

## Preparación necesaria para reutilizar el material heredado

Los talleres heredados de MLflow asumen, sin enseñarlas de forma gradual, prácticas de programación y conocimientos mínimos de experimentación: estructura de paquetes, módulos, ejecución desde terminal, dependencias, pruebas y en algunos casos Docker o GitHub. Como el curso no tiene prerrequisitos, antes de usar cualquiera como actividad `BASE` se debe ofrecer la unidad de fundamentos y nivelación definida en `curriculum.md`. Estos talleres pueden servir como evidencia diagnóstica o como práctica posterior, pero no como mecanismo para introducir desde cero dichas habilidades ni los conceptos básicos de modelos y métricas.

El tiempo estimado incluye presentar datos, problema, razonamiento y solución; se registra solo para material desarrollado y se redondea a múltiplos de 5 minutos.

| Orden inferido | Actividad | Ideas o conceptos inferidos | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---|---:|
| 1 | `PRE_mlflow_template` | plantilla y punto de partida para MLflow | Parcial legado (datos/pruebas; sin notebook, `src/` o `submission/` estándar visibles) | OPT | — |
| 2 | `PRE_mlflow_ambiente_local` | entorno local de MLflow | Parcial legado | OPT | — |
| 3 | `PRE_mlflow_tracking_basico` | tracking de experimentos | Parcial legado | BASE | — |
| 4 | `PRE_mlflow_tracking_local` | tracking con servidor local | Parcial legado | OPT | — |
| 5 | `PRE_mlflow_ambiente_docker` | ejecución en Docker | Parcial legado | OPT | — |
| 6 | `PRE_mlflow_ambiente_github` | integración con GitHub | Enunciado legado (pruebas sin datos visibles) | OPT | — |
| 7 | `PRE_mlflow_registry` | registro y ciclo de vida de modelos | Parcial legado | BASE | — |
| 8 | `PRE_mlflow_evaluacion` | evaluación de modelos | Parcial legado | BASE | — |

Los PRE `BASE` se podrán usar como componentes de trazabilidad y ciclo de vida al completarse y revisarse; no definen por sí mismos el curso. La oferta requiere nuevos PRE `BASE` sobre descubrimiento, usuario, adopción, entrega, operación, DataOps/MLOps y gobierno operacional; MLflow es una práctica de soporte, no el eje organizador.

## Cobertura frente a `curriculum.md`

| Unidad curricular | Evidencia heredada | Estado de cobertura |
|---|---|---|
| Productos de datos y productos analíticos | No hay actividad inequívoca. | Pendiente. |
| Descubrimiento y encuadre de producto | No hay actividad inequívoca. | Pendiente. |
| Interacción humano–IA y adopción | No hay actividad inequívoca. | Pendiente. |
| Ciclo de vida de capacidad analítica | Registro y evaluación MLflow lo sugieren. | Parcial. |
| Reproducibilidad y trazabilidad | Template y tracking MLflow. | Inventariada. |
| Empaquetamiento y entrega | Docker y GitHub lo sugieren. | Parcial. |
| Calidad y pruebas | Evaluación MLflow y pruebas de actividad. | Parcial. |
| Operación, observabilidad y evolución | Registry/tracking lo sugieren. | Parcial; monitoreo y deriva no verificables. |
| Gobierno y seguridad operacional | No hay actividad inequívoca. | Pendiente. |
| Lean, Agile y DataOps | No hay actividad inequívoca. | Pendiente. |
| Tendencias LLM/RAG/agentes | No hay actividad inequívoca. | Pendiente. |
| Microproyectos de producto y operación | Ocho casos acotados de MLflow. | Parcial; estructura legado. |

## Observación de inventario

El material heredado se concentra en una herramienta y cubre parte de trazabilidad, registro, ambientes y ciclo de vida de modelos. No debe interpretarse como cobertura suficiente del currículo de Productos de Datos ni como definición del curso por MLflow.
