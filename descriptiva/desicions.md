# Decisions — Analítica Descriptiva

This file records explicit design decisions for the Analítica Descriptiva course.

These decisions should not be reopened by agents or future chats unless explicitly requested.

---

## D-001 — Course duration

The official course duration is 8 weeks.

Each weekly session lasts approximately 5 hours.

---

## D-002 — Planning unit

The canonical planning unit is:

- 1 block = 50 minutes
- 6 blocks per weekly session
- 48 blocks across the 8-week course

Blocks are planning units only.

They do not imply that classroom activities must stop exactly every 50 minutes.

---

## D-003 — PRE duration

The minimum planned duration of a PRE is 1 block, approximately 50 minutes.

A PRE may occupy multiple consecutive blocks.

A PRE may extend from one weekly session into the next.

If an activity consistently requires substantially less than 50 minutes, it should normally be reconsidered as part of another PRE rather than maintained as an independent PRE.

---

## D-004 — PRE identity is independent of the weekly schedule

A PRE is an independent pedagogical and repository unit.

Its identity and numbering are not tied to:

- a specific week
- a specific session
- a specific planning block

The repository stores the ordered sequence of PREs.

The schedule maps that sequence onto the available course time.

---

## D-005 — Repository representation of long PREs

A PRE that requires several planning blocks remains a single PRE and a single directory.

Do not split a long PRE into artificial parts such as:

- Vuelos I
- Vuelos II
- Vuelos III
- Vuelos IV

only because it spans multiple blocks or sessions.

---

## D-006 — Word Count family

The Word Count sequence consists of four independent PREs:

1. Word Count — MapReduce
2. Word Count — Pandas
3. Word Count — SQLite
4. Word Count — LLM

They must remain separate PREs.

In particular, SQLite and LLM must not be merged into the same PRE.

The sequence is pedagogically intentional:

MapReduce → Pandas → SQLite → LLM

It shows different computational and analytical abstractions applied to the same underlying problem.

---

## D-007 — Word Count minimum planning allocation

The initial planning assumption is 1 block per Word Count PRE.

Therefore:

- MapReduce: 1 block
- Pandas: 1 block
- SQLite: 1 block
- LLM: 1 block

These are initial estimates and may be revised after explicit review of each PRE.

---

## D-008 — SQLite Word Count design

The SQLite Word Count PRE must receive whole text lines as input.

The input must not be pretokenized into words using Python before reaching SQLite.

The intended conceptual progression is:

Pandas:
split → explode → groupby

SQLite:
split/array representation → json_each() → GROUP BY

SQLite JSON1 / `json_each()` is preferred over an advanced recursive CTE for this PRE.

---

## D-009 — Vuelos

Vuelos is one integral PRE.

It is not divided into separate EDA, temporal, KPI, BI, or visualization PREs.

Its intended role is to be the main comprehensive EDA case of the course.

It may occupy several planning blocks.

Its final duration must be determined after explicit review of its content.

---

## D-010 — Vuelos expected role

The Vuelos PRE should support an integral descriptive workflow that may include:

- understanding the analytical problem
- understanding the dataset and unit of observation
- descriptive statistics
- distributions
- group comparisons
- multivariate relationships
- temporal descriptive analysis
- patterns
- anomalies
- relevant KPIs
- visualization
- interpretation
- descriptive synthesis

The exact scope and duration must be calibrated when the PRE is reviewed in detail.

---

## D-011 — Limpieza

The visible PRE name is:

`Limpieza`

Do not rename it to `Limpieza y profiling`.

Profiling may be part of the internal workflow, but it is not part of the visible PRE name.

The PRE should focus on how data-quality problems affect descriptive interpretation.

It must not expand into a full Data Engineering or ETL activity.

---

## D-012 — Anonimización

The visible PRE name is:

`Anonimización`

Do not rename it to `Anonimización y reidentificación`.

The PRE may internally include:

- direct identifiers
- quasi-identifiers
- sensitive attributes
- naive identifier removal
- reidentification attack
- pseudonymization
- generalization
- repeated attack
- utility considerations

Its final duration must be determined after explicit review.

---

## D-013 — Superstore

Superstore is a core PRE.

The visible name is simply:

`Superstore`

Do not overload the visible title with terms such as BI, KPI, dashboard, or business intelligence.

Its pedagogical role is distinct from Vuelos.

Vuelos is the main integral EDA case.

Superstore should emphasize business performance synthesis, KPIs, comparisons, compact reporting/dashboarding, and executive interpretation.

---

## D-014 — Nightingale and Minard

Nightingale and Minard are independent PREs.

They must remain consecutive because they form a pedagogical visualization family.

Their intended progression is:

Nightingale:
visualization as evidence and argument

Minard:
multivariate integrated representation

---

## D-015 — Nightingale duration

Nightingale is planned as:

- 1 block
- approximately 50 minutes

This duration is considered feasible.

---

## D-016 — Minard duration

Minard is planned as:

- 1 block
- approximately 50 minutes

This duration is considered feasible.

---

## D-017 — Scopus visualization

Scopus remains one PRE.

Do not split geographic visualization and network visualization into separate PREs.

The intended progression is:

raw bibliographic data
→ countries
→ frequencies
→ geographic visualization
→ country relationships/co-occurrence
→ network visualization
→ interpretation

---

## D-018 — Data Storytelling position

Data Storytelling must remain near the end of the core sequence.

It should occur after students have completed the major EDA, business synthesis, and visualization cases.

Its role is to transform analytical evidence into communication appropriate for a target audience.

Its exact structure and duration remain to be reviewed.

---

## D-019 — Core versus reserve PREs

The repository should retain both:

- core PREs used in the official 8-week course
- reserve/specialized/legacy PREs

Reserve PREs are not a discard area.

They form an ordered extended curriculum and may be used for:

- fast cohorts
- replacement activities
- company-specific training
- specialized offerings
- deepening
- LAB derivation
- future course redesign
- derivation into Fundamentos

---

## D-020 — Timing of reserve PREs

Time estimates for reserve PREs may be less strict than for core PREs.

They do not constrain the official 8-week schedule.

Core PRE timing must be calibrated carefully because the official course is limited to 48 planning blocks.

---

## D-021 — Sequential affinity

PREs that form a pedagogical family should remain consecutive when reordered.

Examples include:

- Word Count:
  MapReduce → Pandas → SQLite → LLM

- Visualization:
  Nightingale → Minard

- Historical drivers/timesheet reserve family:
  Pandas → SQLite → LLM

---

## D-022 — Core design target

The goal is not to maximize topic count.

The course should prioritize depth in its central descriptive competencies.

The main core competencies are:

- integral EDA
- univariate exploration
- multivariate exploration
- distributions
- group comparisons
- patterns
- anomalies
- descriptive temporal analysis
- analytical visualization
- KPIs and baselines
- dashboards/reports
- evidence communication
- data storytelling
- interpretation for technical and nontechnical audiences

---

## D-023 — Boundary with other courses

Analítica Descriptiva should not absorb content whose primary home is another course.

In particular, avoid expanding the core into:

- formal statistical inference
- hypothesis testing
- confidence intervals
- predictive modeling
- causal inference
- optimization
- heavy ETL
- data architecture
- production DataOps

Supporting elements may appear only insofar as they are necessary for descriptive analysis.

---

## D-024 — Course architecture target

The current architecture is considered capable of reaching a 10/10 design if the individual PREs are calibrated correctly.

Reaching that target depends on explicit review of each PRE for:

- pedagogical purpose
- content
- new concepts
- prior knowledge reused
- professional problem
- expected artifact
- estimated duration
- unnecessary content
- missing content
- completion criterion

The course should not be considered fully closed until this PRE-by-PRE audit is complete.

---

## D-025 — Duration estimation process

Each PRE should eventually receive an explicit time estimate expressed in planning blocks.

The estimate should be based on classroom activity, not only on:

- number of notebooks
- number of code cells
- lines of code

The estimate should account for:

- guided execution
- explanation of new concepts
- student work
- interpretation
- discussion
- expected classroom friction

---

## D-026 — Repository is the persistent source of truth

Important decisions reached in ChatGPT, Work, Claude Code, Codex, Gemini, Copilot, or other working sessions must be written back to the repository.

Chat history is not the canonical long-term memory.

The repository is the persistent project memory.

---

## D-027 — PRE_01: verificación del entorno de trabajo

PRE_01 queda cerrado con una duración de 1 bloque de 50 minutos.

Su función es verificar un entorno reproducible común mediante la ejecución
de un caso de comprobación proporcionado por el curso y el registro de la
evidencia de ejecución.

No debe emplearse para enseñar herramientas ni para resolver instalaciones
individuales extensas. Esas incidencias deben atenderse antes o fuera del
bloque, de modo que PRE_02 pueda comenzar con el grupo en condiciones de
trabajo comparables.
