# Fuentes de diseño — Productos de Datos

Este mapa convierte el material disponible en `curriculum/` en decisiones para el curso. No son lecturas obligatorias por defecto ni sustituyen el currículo: cada fuente se usa por el aporte indicado.

| Fuente | Aporte verificable | Decisión para Productos de Datos |
|---|---|---|
| `dataops-01-the-problem.pdf`, `dataops-08-data-scientids.pdf`, `dataops-09-data-quality.pdf` | DataOps presupone versionado, pruebas automáticas de datos y código, ambientes, parametrización, contenerización y orquestación. | Unidad 0 obligatoria antes de DataOps/MLOps; prácticas de calidad y operación en las unidades 5–10. |
| `acm-computing-competencies-undergraduate-data-science-2021.pdf` | Incluye programación, desarrollo y mantenimiento de software, y pruebas como competencias de ciencia de datos. | El diagnóstico evalúa modularidad, integración, seguridad elemental y pruebas; no exige un grado de ingeniería. |
| `berkeley-data-c101-data-engineering.pdf` | La operación confiable y escalable de datos para analítica/ML tiene prerrequisitos explícitos de programación y ciencia de datos. | Funciona como contraste: Productos no puede copiar esos prerrequisitos. La unidad 0 construye un mínimo guiado y el resto del curso evita asumir formación previa. |
| `informs-analytics-framework-2024.pdf` y blueprints CAP | Distinguen encuadre del problema, encuadre analítico, datos, despliegue y gestión del ciclo de vida. | Las unidades 1–4 parten de consumidor, problema, métricas, riesgos y validación de negocio antes de automatizar una solución. |
| `mit-designing-and-building-ai-products-and-services.pdf` | El diseño de productos de IA incluye HCI y una asignación deliberada de participación humana. | La unidad 3 incorpora supervisión humana, explicaciones, confianza apropiada y validación de utilidad. |
| `berkeley-data-c102-data-inference-and-decisions.pdf` | El ciclo de decisiones con datos tiene implicaciones humanas, sociales y éticas. | Gobierno operacional no se limita a permisos: incluye límites de uso, auditoría y condiciones de retiro. |
| `mit-cloud-and-devops.pdf` | DevOps vincula automatización con métricas de desempeño operativo: tiempo de espera, frecuencia de despliegue, restauración y tasa de fallas. | La unidad 8 mide confiabilidad de servicio junto con adopción y valor; las herramientas son medios, no resultados. |
| `mit-digital-platforms.pdf` | APIs, estándares, arquitectura abierta y hoja de ruta conectan capacidades técnicas con ecosistemas y consumidores. | La unidad 6 trata contratos de entrada/salida y evolución compatible de una capacidad analítica. |
| `mit-rapid-prototyping-methodologies.pdf` y `mit-quantitative-methods-in-systems-engineering.pdf` | Prototipar y comparar alternativas exige criterios explícitos de valor, costo, desempeño e incertidumbre. | Los microproyectos deben justificar hipótesis de valor, alternativa elegida y criterio de aceptación, no solo demostrar una tecnología. |

## Accesibilidad sin prerrequisitos

El curso es de posgrado sin prerrequisitos. Cada caso incluye datos, problema, métrica y componente analítico deliberadamente simples, solo en la medida necesaria para comprenderlo. Los artefactos iniciales pueden estar entregados o construirse guiados; el aprendizaje se concentra en la práctica de programación, DataOps o MLOps que el caso quiere exponer y en convertir el resultado en una oferta útil y operable. La nivelación técnica es diagnóstica y con recuperación, nunca un filtro de matrícula.

## Principio de selección

El curso prioriza las capacidades que permiten entregar y sostener valor para un consumidor. Por ello, MLflow, Docker, GitHub, APIs, orquestadores o plataformas cloud se introducen únicamente cuando el caso exige trazabilidad, repetibilidad, calidad, entrega u operación. Ninguna herramienta define por sí misma una unidad ni una evidencia de aprendizaje.

## Consecuencia para los `PRE_*` heredados

Los `PRE_mlflow_*` se conservan como práctica de trazabilidad, ambientes, registro y evaluación una vez aprobada la unidad 0. Para cubrir el currículo, se requieren nuevos `PRE_BASE` sobre: encuadre con consumidor y contrato; pruebas de datos y lógica; entrega mediante contrato; monitoreo, incidente y deriva; gobierno operacional; y un caso de IA con supervisión humana. La selección y diseño de esos nuevos `PRE_*` debe usar este mapa y no intentar cubrir todo el curso con una secuencia de MLflow.
