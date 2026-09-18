# PRE Catalog — Analítica Descriptiva

Este archivo contiene el inventario canónico y ordenado de los PRE de
Analítica Descriptiva.

La numeración de los PRE representa su secuencia pedagógica.

La numeración no determina:

- la semana en que se dicta el PRE;
- el bloque de la sesión en que comienza;
- el número de bloques que ocupa.

La asignación temporal se mantiene en `schedule.md`.

---

## Unidad de tiempo

La unidad de planificación es:

- 1 bloque = 50 minutos;
- 6 bloques = una sesión semanal de 5 horas.

La duración mínima planificada de un PRE es 1 bloque.

Un PRE puede ocupar varios bloques y puede continuar de una semana a otra.

---

# PRE core

Estos PRE forman parte del diseño de las 8 semanas oficiales del curso.

| PRE | Nombre | Función principal | Bloques | Estado |
|---|---|---|---:|---|
| PRE_01 | Verificación del entorno de trabajo | Verificar un entorno reproducible común para ejecutar los PRE iniciales | 1 | cerrado |
| PRE_02 | Word Count: MapReduce | Introducir explícitamente map → agrupación → reduce | 1 | por revisar |
| PRE_03 | Word Count: Pandas | Resolver el mismo problema mediante abstracción tabular | 1 | por revisar |
| PRE_04 | Word Count: SQLite | Resolver el mismo problema mediante consulta declarativa | 1 | por revisar |
| PRE_05 | Word Count: LLM | Resolver el mismo problema mediante interfaz en lenguaje natural | 1 | por revisar |
| PRE_06 | Limpieza | Mostrar cómo problemas de calidad afectan la evidencia descriptiva | TBD | por revisar |
| PRE_07 | Anonimización | Introducir privacidad, cuasi-identificadores y riesgo de reidentificación | TBD | por revisar |
| PRE_08 | Vuelos | Caso principal de análisis descriptivo integral y EDA | TBD | por revisar |
| PRE_09 | Superstore | Síntesis de desempeño, KPIs y lectura gerencial | TBD | por diseñar |
| PRE_10 | Nightingale | Visualización como evidencia y argumento | 1 | por diseñar |
| PRE_11 | Minard | Representación multivariada integrada | 1 | por diseñar |
| PRE_12 | Scopus: visualización geográfica y red | Representación geográfica y relacional de actividad científica | TBD | por revisar |
| PRE_13 | Data Storytelling | Convertir evidencia analítica en comunicación para una audiencia | TBD | por diseñar |

---

## Secuencia core

PRE_01 — Verificación del entorno de trabajo

PRE_02 — Word Count: MapReduce

PRE_03 — Word Count: Pandas

PRE_04 — Word Count: SQLite

PRE_05 — Word Count: LLM

PRE_06 — Limpieza

PRE_07 — Anonimización

PRE_08 — Vuelos

PRE_09 — Superstore

PRE_10 — Nightingale

PRE_11 — Minard

PRE_12 — Scopus: visualización geográfica y red

PRE_13 — Data Storytelling

---

# PRE de reserva

Estos PRE pertenecen al currículo extendido pero no condicionan la
programación oficial de las 8 semanas.

Sus tiempos pueden permanecer sin definir hasta que sean revisados o
seleccionados para uso real.

| PRE | Nombre | Tipo | Bloques | Estado |
|---|---|---|---:|---|
| PRE_14 | Refactorización y herramientas de desarrollo | reserva | TBD | por revisar |
| PRE_15 | CSV → JSON | reserva | TBD | por revisar |
| PRE_16 | Enriquecimiento de datos | reserva | TBD | por revisar |
| PRE_17 | Normalización y resolución de entidades | especializado | TBD | por revisar |
| PRE_18 | ETL asistido por agentes | reserva | TBD | por diseñar |
| PRE_19 | Supplier Quality | reserva | TBD | por diseñar |
| PRE_20 | Factory Performance | reserva | TBD | por diseñar |
| PRE_21 | HVAC | especializado | TBD | por diseñar |
| PRE_22 | CTA / movilidad urbana | reserva | TBD | por diseñar |
| PRE_23 | Clickstream | especializado | TBD | por diseñar |
| PRE_24 | Logs de servidores | especializado | TBD | por diseñar |
| PRE_25 | Market Basket | especializado | TBD | por diseñar |
| PRE_26 | Análisis descriptivo de texto | especializado | TBD | por diseñar |
| PRE_27 | Pandas clásico: drivers/timesheet | legacy | TBD | por revisar |
| PRE_28 | SQLite clásico: drivers/timesheet | legacy | TBD | por revisar |
| PRE_29 | LLM clásico: drivers/timesheet | legacy | TBD | por revisar |
| PRE_30 | Enigma | reserva / legacy | TBD | por revisar |
| PRE_31 | Visualización especializada / profundización | reserva | TBD | por diseñar |

---

# Restricciones de secuencia

Las siguientes familias deben permanecer consecutivas.

## Word Count

PRE_02 — MapReduce  
PRE_03 — Pandas  
PRE_04 — SQLite  
PRE_05 — LLM

## Visualización histórica

PRE_10 — Nightingale  
PRE_11 — Minard

## Drivers/timesheet

PRE_27 — Pandas  
PRE_28 — SQLite  
PRE_29 — LLM

---

# Estados

Los estados utilizados en este archivo son:

- `por diseñar`: el PRE está identificado pero todavía no tiene especificación completa;
- `por revisar`: existe material previo o una definición suficientemente concreta, pero debe auditarse;
- `cerrado`: contenido, duración y función pedagógica ya fueron revisados y aceptados.

No se debe marcar un PRE como `cerrado` hasta terminar explícitamente su
revisión.

---

# Regla de actualización

Después de revisar cada PRE se actualizan únicamente:

1. su función principal, si cambia;
2. su número de bloques;
3. su estado.

Si cambia la duración de un PRE core, también debe actualizarse
`schedule.md`.

Las decisiones pedagógicas permanentes deben registrarse en `decisions.md`,
no desarrollarse dentro de este catálogo.
