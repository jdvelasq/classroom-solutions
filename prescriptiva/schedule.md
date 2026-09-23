# Secuencia curricular candidata — Analítica Prescriptiva

## Estado de esta secuencia

El propósito actual es decidir **qué debe integrar el curso** y en qué progresión conceptual. Esta tabla no es todavía una programación de sesiones: no asigna tiempos, no clasifica actividades como `BASE` u `OPT` y no fuerza una duración total. Esas decisiones se tomarán cuando el inventario y las prioridades curriculares estén cerrados.

La secuencia se organiza como **Analytics para decidir**, no como un temario de Investigación de Operaciones. Cada taller debe responder una pregunta de acción mediante evidencia, alternativas, valor, restricciones e incertidumbre. Optimización o simulación pueden ser instrumentos, pero no son el resultado de aprendizaje por sí mismos.

## Secuencia propuesta

| Orden | Actividad | Pregunta analítica prescriptiva | Estado |
|---:|---|---|---|
| 1 | `PRE_01_encuadre_analitico_de_decisiones` | ¿Qué decisión debe tomarse, quién responde por ella y cómo se definirá su valor? | Esqueleto creado |
| 2 | `PRE_02_air_france_447` | ¿Cómo distribuir una búsqueda cuando la evidencia es incompleta y el costo de errar es alto? | Desarrollado |
| 3 | `PRE_03_politica_desde_evidencia_y_restricciones` | ¿Qué política conviene entre alternativas con evidencia, valor y restricciones explícitas? | Esqueleto creado |
| 4 | `PRE_04_airline_revenue_management` | ¿Cómo usar capacidad limitada ante demanda y valor heterogéneos? | Desarrollado |
| 5 | `PRE_05_covid_hospital_capacity` | ¿Qué capacidad preparar ante escenarios inciertos de demanda? | Desarrollado |
| 6 | `PRE_06_politicas_y_supervision_humana` | ¿Cuándo automatizar, escalar o requerir revisión humana? | Esqueleto creado |
| 7 | `PRE_07_annie_moore_refugee_resettlement` | ¿Cómo asignar familias respetando resultados esperados y restricciones? | Desarrollado |
| 8 | `PRE_08_tax_inspections` | ¿A quién inspeccionar cuando la capacidad es limitada y la evidencia es probabilística? | Desarrollado |
| 9 | `PRE_09_monte_carlo_para_politicas` | ¿Qué política domina al comparar resultados y riesgos bajo escenarios simulados? | Esqueleto creado |
| 10 | `PRE_10_wildfire_resource_positioning` | ¿Dónde ubicar y cómo reasignar recursos frente al riesgo cambiante? | Desarrollado |
| 11 | `PRE_11_humanitarian_food_aid` | ¿Qué ayuda entregar y cómo abastecerla bajo restricciones humanitarias? | Desarrollado |
| 12 | `PRE_12_evaluacion_de_politicas_por_simulacion` | ¿Cómo evaluar una política cuando la dinámica del sistema no admite una respuesta cerrada? | Esqueleto creado |
| 13 | `PRE_13_flood_protection_investment` | ¿Qué inversión reduce mejor el riesgo dentro de un presupuesto? | Desarrollado |
| 14 | `PRE_14_hydrothermal_planning` | ¿Qué plan equilibra energía, agua, costos y restricciones temporales? | Desarrollado |
| 15 | `PRE_15_sensibilidad_y_tradespace` | ¿Qué supuestos, umbrales y trade-offs cambian la recomendación? | Esqueleto creado |
| 16 | `PRE_16_credit_campaign_targeting` | ¿Cómo convertir probabilidades en una política de focalización con capacidad limitada? | Desarrollado |
| 17 | `PRE_17_decision_informada_por_pronosticos` | ¿Cómo cambia una decisión al propagar la incertidumbre de un pronóstico? | Esqueleto creado |
| 18 | `PRE_18_catalog_assortment` | ¿Qué surtido conviene dadas capacidad, valor y riesgo? | Desarrollado |
| 19 | `PRE_19_delivery_fleet_capacity` | ¿Qué política de capacidad y tercerización conviene bajo demanda incierta? | Desarrollado |
| 20 | `PRE_20_equidad_y_responsabilidad_prescriptiva` | ¿Qué impactos distributivos produce una política y qué salvaguardas requiere? | Esqueleto creado |
| 21 | `PRE_21_storm_response_crews` | ¿Cómo reservar y asignar cuadrillas ante eventos extremos? | Desarrollado |
| 22 | `PRE_22_comunicacion_y_seguimiento_de_politicas` | ¿Cómo documentar una recomendación, sus supuestos y sus gatillos de revisión? | Esqueleto creado |
| 23 | `PRE_23_valor_de_informacion_y_experimentacion` | ¿Conviene actuar, esperar, medir o experimentar antes de adoptar una política? | Esqueleto creado |

## Candidatos aún no incorporados

| Candidato | Aporte potencial | Decisión pendiente |
|---|---|---|
| Evaluación financiera de proyectos por escenarios | Construye un flujo de caja deliberadamente simple: inversión inicial, ingresos totales, costos variables, costos fijos e impuesto/tasa si se requiere; compara escenarios y decide financiar, posponer, rediseñar o descartar. | Definir si reemplaza o complementa un caso de escenarios existente. |
| Evaluación financiera de proyectos con Monte Carlo | Convierte ingresos, costos o adopción en variables inciertas del mismo flujo; estima distribución de valor, probabilidad de pérdida y sensibilidad antes de recomendar una acción. | Definir si se convierte en la instancia concreta de PRE_09 o PRE_12. |

## Fuentes de casos admisibles

Los ejemplos de **DecisionSuite de Lumivero** pueden utilizarse como fuentes de problemas, decisiones, escenarios y progresiones pedagógicas. CLASSROOM no depende de Excel ni de los complementos de DecisionSuite: cada adaptación debe reconstruirse en Python con datos, cálculo, visualización, pruebas y artefactos reproducibles dentro de la estructura estándar de un `PRE_*`.
