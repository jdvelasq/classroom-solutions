# PRE Specification

## Identification

**Activity:** `PRE_XX_activity_name`

**Week:** `XX`

**Status:** `DRAFT`

Allowed lifecycle:

```text
DRAFT
↓
READY
↓
IMPLEMENTED
```

`DRAFT` specifications must not be implemented.

---

## Activity title

**<Short student-facing title>**

---

## Central engineering insight

State exactly one central engineering insight.

The workshop should answer:

> <One engineering question>

Express the central progression:

```text
<starting condition>
↓
<engineering mechanism>
↓
<observable result>
```

State the essential distinction if appropriate:

```text
<concept A>
≠
<concept B>
```

If the activity requires several independent insights, reduce its scope.

---

## Course capability

List only the capabilities required to expose the central insight.

Do not turn this section into a catalog of everything related to the topic.

---

## Engineering problem

Describe one concrete problem that motivates the complete activity.

The scenario should make the engineering capability necessary.

Avoid technology-first problem statements.

Prefer:

> The source behaves in this way, therefore the pipeline needs this capability.

over:

> Students will learn technology X.

---

## Minimal input

Specify every canonical input.

For each dataset state:

* file name;
* required fields;
* approximate row count;
* required controlled cases.

Use:

> The smallest deterministic dataset that makes the phenomenon unambiguous.

The complete or nearly complete dataset should normally be visually understandable.

---

## Expected output

State:

* output artifact;
* required grain;
* required fields;
* key semantic properties.

Every output must have an explicit purpose.

---

## Notebook execution budget

Select the appropriate hard maximum.

### Week with three PRE

```text
maximum notebook cells: 6
```

### Week with two PRE

```text
maximum notebook cells: 8
```

### Full-class PRE

```text
maximum notebook cells: 14
```

### Final architecture PRE

```text
maximum notebook cells: 10
```

For every PRE:

```text
maximum effective code lines per code cell: 12
```

These are maximums, not targets.

State a recommended lower cell count whenever possible.

---

## Notebook progression

Design the smallest sequence of cells that exposes the phenomenon.

Use:

### Cell 1 — <purpose>

Describe:

* visible input;
* operation;
* observable result;
* central classroom question.

### Cell 2 — <purpose>

...

Do not add cells simply to demonstrate additional syntax or technology.

Every cell must contribute directly to the central engineering insight.

---

## Core observable phenomenon

State exactly what students must observe.

Examples:

```text
COUNT(*)
vs
COUNT(DISTINCT ...)
```

```text
attempt 1 → FAILED
attempt 2 → SUCCESS
```

```text
window OPEN
→ watermark advances
→ window FINALIZED
```

```text
same batch
+
advanced checkpoint
→
0 eligible rows
```

If the phenomenon is not directly observable, redesign the PRE.

---

## Required code philosophy

All central logic must be visible in the notebook.

Code must be:

* complete;
* explicit;
* readable;
* deterministic;
* self-explanatory.

The instructor should explain **why**, not translate **what** the code does.

Avoid:

* unnecessary lambdas;
* dense one-liners;
* excessive method chaining;
* nested comprehensions;
* premature abstractions;
* unnecessary classes;
* hidden helper logic.

---

## `src/` role

Choose one:

### Not required

```text
src/ is not required for this PRE.
```

or:

### Consolidation after demonstration

Core logic must first be visible in the notebook.

Only afterward may it be consolidated into:

```text
src/<module>.py
```

`src/` must not introduce new central behavior.

Do not use helper modules to circumvent notebook cell or line limits.

---

## Technology

List only the required technology.

State why each nontrivial technology is necessary.

If the same phenomenon can be taught more transparently without a framework, prefer the simpler implementation.

Any classroom-specific configuration must be explicitly identified as pedagogical rather than a production recommendation.

---

## Determinism and reproducibility

The PRE must:

* execute from a clean generated state;
* use relative paths;
* avoid public-network dependencies unless explicitly controlled;
* avoid current timestamps in graded output;
* avoid machine-dependent behavior;
* use deterministic ordering when outputs are compared;
* produce equivalent logical results on re-execution.

Document any environment dependency explicitly.

---

## Controlled failure

If required, describe exactly one controlled failure.

State:

```text
failure
→
expected behavior
→
engineering lesson
```

A second failure case is allowed only when it demonstrates a distinct response.

Do not create failure catalogs.

If no controlled failure is required, state:

```text
No controlled failure is required.
```

---

## Visible validation

Use only the validations required to make the central claim observable.

Recommended:

```text
1–2 validations
```

For each validation state:

### Validation 1 — <name>

```text
<expected invariant>
```

### Validation 2 — <name>

```text
<expected invariant>
```

Extensive guarantees belong in repository tests.

---

## Expected artifacts

For every artifact specify:

### `<path>`

**Purpose:** <why it exists>

**Required grain:** <what one row represents, when applicable>

**Required fields:**

```text
...
```

**Required properties:**

* ...
* ...
* deterministic ordering or logical content.

Do not create artifacts without pedagogical or grading value.

---

## Required tests

Tests should validate observable behavior and semantics.

They should normally verify:

1. required inputs exist;
2. required outputs exist;
3. required schema exists;
4. central engineering invariant holds;
5. controlled failure behaves correctly, when applicable;
6. logical results reconcile;
7. re-execution is reproducible;
8. outputs are deterministic.

Tests should not depend unnecessarily on:

* internal helper-function names;
* exact notebook formatting;
* incidental ordering;
* task identifiers;
* framework-generated filenames;
* exact execution-plan text.

---

## What students should observe

Reduce the complete PRE to one compact progression:

```text
...
↓
...
↓
...
```

State:

> The essential engineering insight is: <one sentence>.

---

## Boundaries

Explicitly list concepts that must **not** be introduced.

Boundaries prevent the implementation agent from expanding the activity.

Examples:

* advanced framework features;
* production infrastructure;
* unrelated algorithms;
* tuning;
* additional data models;
* additional failure cases.

---

## Relationship with previous PRE

State what students already know and therefore must not be retaught.

```text
PRE_XX establishes:
...

This PRE adds:
...
```

---

## Relationship with next PRE

State what this activity deliberately leaves for the next PRE.

```text
This PRE establishes:
...

PRE_XX will add:
...
```

---

## Acceptance criteria

The PRE may become `READY` only when all applicable conditions are satisfied.

Required general criteria:

1. Exactly one central engineering insight is identifiable.
2. One coherent problem drives the complete notebook.
3. Dataset size is minimal.
4. Notebook cell limit is satisfied.
5. Every code cell can remain within 12 effective lines.
6. Core logic is visible.
7. No central logic is hidden in `src/`.
8. Technology is minimal.
9. Controlled failures are minimal.
10. Visible validations are minimal.
11. Required artifact semantics are explicit.
12. Tests validate the intended phenomenon.
13. Execution is deterministic.
14. The PRE is independently reproducible.
15. Boundaries prevent scope expansion.
16. The instructor can focus on **why** rather than explaining obscure code.
17. The activity complies with `AGENTS.md`.

Add PRE-specific acceptance criteria below these when required.

---

## Final compactness check

Before changing:

```text
Status: DRAFT
```

to:

```text
Status: READY
```

answer all of the following:

### Scope

```text
[ ] One central engineering insight
[ ] No independent mini-lessons
[ ] No unnecessary technology
```

### Notebook

```text
[ ] Cell count within hard limit
[ ] Every code cell can remain ≤ 12 effective lines
[ ] Central logic visible
[ ] No code compression used to satisfy limits
```

### Data

```text
[ ] Dataset is minimal
[ ] Required phenomenon is visually obvious
[ ] Artificial scale is absent unless scale is the lesson
```

### Pedagogy

```text
[ ] Student can understand what the completed code does
[ ] Instructor can focus on why it matters
[ ] Observable phenomenon is explicit
```

### Reliability

```text
[ ] Deterministic execution
[ ] Clean-state execution
[ ] Relative paths
[ ] Central outputs validated
[ ] Repository tests specified
```

### Boundaries

```text
[ ] Later-course concepts are not pulled forward
[ ] Production complexity is excluded unless required
[ ] src/ does not hide pedagogical logic
```

If any required box remains unchecked, keep:

```text
Status: DRAFT
```

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When the specification becomes `READY`:

* implement exactly the specified phenomenon;
* do not expand the scope;
* respect notebook cell limits;
* respect the 12-effective-line limit;
* use the specified minimal dataset;
* keep core logic visible;
* preserve deterministic behavior;
* run the notebook from a clean state;
* run repository tests;
* inspect generated artifacts;
* report any specification conflict rather than silently redesigning the activity.

The implementation agent must not reinterpret `READY` as permission to improve the activity by adding technologies, abstractions, examples, or complexity.


Pedagogical cell framing

Cuando una celda de código introduce una nueva decisión de ingeniería, abstracción, fallo controlado o validación, debe comenzar, cuando resulte útil, con uno o dos comentarios breves que indiquen el propósito de la operación.

Los comentarios deben redactarse en tercera persona impersonal.

Ejemplos adecuados:

# Se separan las entidades para evitar la repetición de sus atributos.

# Se verifica que todas las referencias correspondan a productos existentes.

# Se simula una falla transitoria para observar el comportamiento del reintento.

# Se compara el resultado reconstruido con los datos originales.

Se deben evitar comentarios que simplemente traduzcan la sintaxis:

# Se crea una variable.
# Se ejecuta un bucle.
# Se imprime el DataFrame.

El comentario debe explicar la intención del bloque, no describir línea por línea lo que hace el código.

Los comentarios exclusivamente pedagógicos no cuentan dentro del límite de 12 líneas efectivas de código por celda.