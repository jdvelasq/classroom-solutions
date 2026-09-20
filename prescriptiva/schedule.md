# Inventario heredado — Analítica Prescriptiva

## Propósito y lectura

Este archivo inventaría material heredado de `PRE_*`; no propone una programación nueva ni modifica actividades. El orden es numérico. Los `LAB_*` son actividades de evaluación y quedan fuera de este inventario y de la matriz de cobertura curricular. **Desarrollado** indica presencia observable de datos, notebook, pruebas y artefactos en `submission/`; no certifica todavía la formulación, el solver ni el cumplimiento semántico de la recomendación.

La unidad básica de este archivo es cada `PRE_*`. La matriz final solo agrega los conceptos de los `PRE_*` para comprobar cobertura de `curriculum.md`; no convierte las unidades curriculares en sesiones.

El tiempo estimado incluye presentar datos, problema, razonamiento y solución; se registra solo para material desarrollado y se redondea a múltiplos de 5 minutos.

| Orden | Actividad | Ideas o conceptos inferidos | Nivel observable | Clasificación | Tiempo estimado |
|---:|---|---|---|---|---:|
| 1 | `PRE_01_air_france_447` | planeación de búsqueda bajo incertidumbre | Desarrollado | BASE | 75 min |
| 2 | `PRE_02_airline_revenue_management` | capacidad, asignación y gestión de ingresos | Desarrollado | BASE | 75 min |
| 3 | `PRE_03_covid_hospital_capacity` | capacidad hospitalaria y escenarios de demanda | Desarrollado | BASE | 75 min |
| 4 | `PRE_04_annie_moore_refugee_resettlement` | reasentamiento y asignación con restricciones | Desarrollado | BASE | 70 min |
| 5 | `PRE_05_tax_inspections` | priorización de inspecciones y recuperación esperada | Desarrollado | BASE | 70 min |
| 6 | `PRE_06_wildfire_resource_positioning` | posicionamiento de recursos ante incendios | Desarrollado | OPT | 70 min |
| 7 | `PRE_07_humanitarian_food_aid` | asignación de ayuda humanitaria | Desarrollado | OPT | 70 min |
| 8 | `PRE_08_flood_protection_investment` | inversión y trade-offs de protección | Desarrollado | BASE | 65 min |
| 9 | `PRE_09_hydrothermal_planning` | planeación hidrotermal | Desarrollado | OPT | 80 min |
| 10 | `PRE_10_credit_campaign_targeting` | focalización de campaña de crédito | Desarrollado | BASE | 70 min |
| 11 | `PRE_11_catalog_assortment` | selección de surtido | Desarrollado | BASE | 70 min |
| 12 | `PRE_12_delivery_fleet_capacity` | capacidad de flota de entrega | Desarrollado | BASE | 70 min |
| 13 | `PRE_13_storm_response_crews` | asignación de cuadrillas de respuesta | Desarrollado | OPT | 70 min |

Los PRE `BASE` heredados suman aproximadamente **11 h 10 min**. La capacidad de 30–33 horas se completa con nuevos PRE `BASE` para formulación explícita, simulación, sensibilidad, responsabilidad y comunicación/seguimiento, después de la auditoría semántica de los materiales.

## Cobertura frente a `curriculum.md`

| Unidad curricular | Evidencia heredada | Estado de cobertura |
|---|---|---|
| Encuadre de decisiones | Todos los casos tienen un contexto de asignación, capacidad o selección. | Parcial, inferida. |
| Formulación de modelos prescriptivos | Los casos sugieren optimización; formulaciones deben revisarse en notebooks. | Parcial. |
| Optimización determinista | Revenue management, reasentamiento, ayuda, surtido, flota y cuadrillas. | Inventariada. |
| Reglas, políticas y automatización | Focalización de crédito e inspecciones lo sugieren. | Parcial. |
| Decisión bajo incertidumbre | Air France, COVID, incendios y tormentas. | Inventariada. |
| Simulación | Air France, COVID y planeación hidrotermal podrían incluirla. | Pendiente de lectura de notebooks. |
| Sensibilidad y tradespace | Inversión en inundaciones e hidrotermal lo sugieren. | Parcial, inferida. |
| Prescripción informada por datos | Crédito, impuestos y COVID combinan datos y decisión. | Parcial. |
| Equidad, comportamiento y responsabilidad | Reasentamiento y ayuda humanitaria ofrecen contexto; tratamiento explícito no verificable. | Pendiente. |
| Comunicación y seguimiento de políticas | Entregables de decisión visibles; comunicación/seguimiento requiere revisión. | Parcial. |

## Observación de inventario

El conjunto heredado presenta una colección sólida y diversa de casos prescriptivos. La siguiente fase por curso deberá auditar, sin rediseñarlos todavía, la formulación matemática, el hilo incremental, los tests y la correspondencia con las unidades curriculares.
