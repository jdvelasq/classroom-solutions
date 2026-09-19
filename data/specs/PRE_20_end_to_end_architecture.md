# PRE Specification

## Identification

**Activity:** `PRE_20_end_to_end_architecture`

**Week:** 13

**Status:** `READY`

---

## Activity title

**Diseñar una arquitectura de datos de extremo a extremo**

---

## Central engineering insight

A data architecture is not a diagram containing fashionable technologies.

It is a set of connected engineering decisions derived from:

* source characteristics;
* consumer needs;
* processing requirements;
* reliability requirements;
* scale;
* latency;
* governance;
* operational constraints.

The workshop should answer:

> Given a realistic set of data sources, requirements, and failures, what architecture should connect sources to reliable consumer-facing data, and why?

The central progression is:

```text
requirements
↓
data flows
↓
engineering capabilities
↓
components
↓
controls
↓
serving
↓
tradeoffs
↓
requirement coverage
```

The essential lesson is:

```text
architecture component
must exist because of a requirement
```

not because a technology was covered in the course.

---

## Role in the course

This is the final integration activity.

It must:

* reuse concepts already introduced;
* connect them into one coherent architecture;
* force students to justify design choices;
* expose tradeoffs;
* close the course.

It must not teach a new technical capability.

---

## Course capability

Integrate the course capabilities:

* relational and semistructured sources;
* batch ingestion;
* API ingestion;
* streaming;
* raw and curated storage;
* analytical formats;
* partitioning;
* transformation;
* analytical modeling;
* data quality;
* data contracts;
* incremental processing;
* pipeline operation;
* distributed processing;
* serving;
* metadata;
* lineage;
* privacy and access.

Not every capability must become a separate component.

Several may be implemented by the same architectural element.

---

## Business scenario

A retailer operates several digital and physical sales channels.

Its data ecosystem contains four source types.

### Operational sales database

Contains:

```text
orders
customers
products
```

Characteristics:

```text
structured
transactional
continuously updated
```

---

### Supplier files

Daily files contain product and inventory information.

Characteristics:

```text
batch
CSV / Parquet
one delivery per day
```

---

### External reviews API

Provides product reviews.

Characteristics:

```text
JSON
paginated
external availability
possible transient failures
```

---

### Web events

The e-commerce site produces:

```text
page views
cart events
purchases
```

Characteristics:

```text
continuous events
high arrival rate
event time may differ from arrival time
```

---

## Consumer needs

The architecture must support exactly four consumer needs.

### Operational analytics

Daily reliable sales dataset.

---

### Management dashboard

Monthly and daily aggregated sales metrics.

---

### Digital analytics

Near-real-time web-event metrics.

---

### Data science

Historical curated data for exploratory and predictive work.

---

## Architectural requirements

Provide a compact file such as:

```text
data/requirements.csv
```

containing requirements such as:

```text
R1 daily sales data available reproducibly
R2 API failure must not silently create incomplete data
R3 customer identifiers must remain unique
R4 changes in customer data should be processed incrementally
R5 web events require near-real-time processing
R6 historical analytical processing may exceed single-machine scale
R7 dashboard consumers require stable serving schemas
R8 restricted customer information must not reach public analytical outputs
R9 upstream changes must be traceable to downstream datasets
R10 pipeline failures must be observable and recoverable
```

Use approximately:

```text
8–10 requirements
```

No larger requirements catalog is necessary.

---

## Current architecture

Provide a deliberately weak starting architecture.

For example:

```text
source systems
↓
individual analyst scripts
↓
shared CSV files
↓
dashboards
```

Known characteristics:

* manual execution;
* duplicated extraction logic;
* no raw layer;
* no explicit contracts;
* no automated quality gate;
* full reloads;
* weak failure handling;
* no lineage;
* unrestricted propagation of some sensitive fields.

---

## Controlled incidents

Provide approximately four short incidents.

### Incident 1 — Duplicate customer

A complete reload creates multiple current versions of the same customer.

---

### Incident 2 — Incomplete API load

One API page fails but downstream processing continues.

---

### Incident 3 — Dashboard break

An upstream column is renamed without identifying affected consumers.

---

### Incident 4 — Sensitive data exposure

`customer_email` reaches a serving dataset that does not require it.

These incidents motivate architectural requirements already studied in previous PREs.

---

## Notebook execution budget

Available teaching allocation:

**approximately 110–130 minutes**

with remaining class time reserved for:

```text
course synthesis
discussion
closure
```

Hard constraints:

```text
maximum notebook cells: 10
recommended cells: 8–9

maximum effective code lines per code cell: 12
```

The notebook should contain more reasoning than code.

---

## Notebook progression

### Cell 1 — Read the scenario

Inspect:

```text
sources
consumer needs
requirements
current architecture
incidents
```

Central question:

> What is wrong with the current architecture, and which requirements expose those weaknesses?

Students should begin from the problem rather than from technologies.

---

### Cell 2 — Diagnose the current architecture

Create a compact diagnosis such as:

```text
problem
consequence
required capability
```

Examples:

```text
full reload
→ unnecessary work / duplicates
→ incremental processing

silent API failure
→ incomplete dataset
→ validation + bounded retry

unknown downstream dependencies
→ unsafe upstream change
→ metadata + lineage
```

The objective is to connect failures with engineering capabilities learned during the course.

---

### Cell 3 — Separate the major data flows

Classify the sources into:

```text
batch
stream
```

Recommended result:

### Batch

```text
operational database
supplier files
reviews API
```

### Stream

```text
web events
```

Central discussion:

> Why should all sources not be forced through the same ingestion pattern?

This establishes the two principal architecture paths.

---

### Cell 4 — Design the storage and processing path

Define the main batch path:

```text
sources
↓
ingestion
↓
raw
↓
staging / transformation
↓
curated
↓
serving
```

Define the streaming path:

```text
web events
↓
event stream
↓
windowed processing
↓
streaming metrics
↓
serving
```

Both paths should converge conceptually on reliable consumer-facing data.

No implementation is required.

---

### Cell 5 — Define the architecture components

Create:

```text
submission/architecture_components.csv
```

Required columns:

```text
component
role
input
output
course_capability
```

Suggested components may include:

```text
batch_ingestion
api_ingestion
event_ingestion
raw_storage
transformation
curated_storage
quality_gate
contract_validation
incremental_update
pipeline_orchestration
distributed_processing
stream_processing
serving_layer
metadata_lineage
```

Do not require one component for every course topic.

Only justified components should appear.

---

### Cell 6 — Define the data flows

Create:

```text
submission/data_flows.csv
```

Required columns:

```text
source
target
data
mode
purpose
```

Example modes:

```text
BATCH
STREAM
```

The flow table should be sufficient to reconstruct the architecture logically.

Central discussion:

> What moves where, in what mode, and for what purpose?

---

### Cell 7 — Add cross-cutting controls

Place previously studied controls at the correct architectural boundaries.

Required reasoning should include:

```text
contracts
→ source / consumer interface

quality
→ before unreliable data become curated

incremental state
→ changing operational entities

orchestration
→ batch task execution

metadata + lineage
→ across the complete architecture

privacy
→ restrict unnecessary sensitive fields

watermark / lateness policy
→ streaming path
```

Central lesson:

> Controls belong at specific boundaries because they mitigate specific risks.

Do not create a new governance layer simply to collect these concepts.

---

### Cell 8 — Record architectural decisions and tradeoffs

Create:

```text
submission/architecture_decisions.csv
```

Required columns:

```text
decision
choice
alternative
rationale
tradeoff
```

Use approximately:

```text
5–7 decisions
```

Recommended decisions include:

```text
batch vs streaming ingestion
full rebuild vs incremental update
local vs distributed processing
CSV vs Parquet for analytical storage
raw vs direct-to-curated ingestion
detail vs aggregated serving
```

Students must state both:

```text
why the choice fits
```

and:

```text
what cost or limitation it introduces
```

---

### Cell 9 — Verify requirement coverage

Create:

```text
submission/requirement_coverage.csv
```

Required columns:

```text
requirement_id
requirement
architecture_element
coverage
evidence
```

Allowed values:

```text
COVERED
PARTIAL
NOT_COVERED
```

The final architecture is acceptable only when every requirement has an explicit disposition.

Central question:

> Can every architectural component be traced to a requirement, and can every requirement be traced to an architectural response?

---

## Optional Cell 10 — Final architecture view

If useful, create one compact architecture representation from:

```text
architecture_components.csv
+
data_flows.csv
```

The representation may be:

* a simple text diagram;
* Mermaid source;
* another transparent structured view.

Example logical architecture:

```text
                 ┌─────────────────┐
DB ─────────────►│ Batch ingestion │
Files ──────────►│                 │
API ────────────►│                 │
                 └────────┬────────┘
                          ↓
                         Raw
                          ↓
                 Contracts / Quality
                          ↓
                      Curated
                          ↓
              ┌───────────┴───────────┐
              ↓                       ↓
         Detail serving          Aggregated mart


Web events
    ↓
Event stream
    ↓
Windowed processing
    ↓
Streaming metrics
    ↓
Serving
```

Metadata and lineage span both paths.

This visualization must not introduce new components or decisions.

---

## Architecture-design philosophy

The required sequence is:

```text
requirement
↓
capability
↓
component
↓
data flow
↓
control
↓
consumer
```

Avoid:

```text
technology
↓
find a reason to use it
```

Students should be able to justify every component with:

> This exists because requirement Rn needs it.

---

## Batch versus stream

Students must explicitly justify why:

```text
supplier files
```

use batch ingestion while:

```text
web events
```

use streaming.

The decision should follow from:

```text
arrival pattern
latency requirement
processing semantics
```

not from technological preference.

---

## Local versus distributed processing

Distributed processing must appear only where justified by scale.

For example:

```text
small reference-data transformations
→ local processing is sufficient

large historical analytical transformation
→ distributed processing may be justified
```

The final architecture must not imply:

```text
Spark everywhere
```

The lesson from `PRE_15` is architectural selectivity.

---

## Raw storage

Raw storage should provide a controlled boundary between:

```text
external source
```

and:

```text
internal processing
```

It supports:

* reproducibility;
* replay;
* source preservation;
* investigation.

Do not present raw storage as mandatory for every imaginable data product.

It is justified here by the scenario requirements.

---

## Analytical storage

Use concepts already studied:

```text
Parquet
partitioned datasets
curated analytical data
```

No new table format or cloud data warehouse should be introduced.

---

## Incremental processing

Use incremental processing where entities change over time.

Recommended:

```text
customers
products
```

Do not apply incremental logic merely because it was taught.

The architectural justification is:

```text
existing current state
+
new changes
```

---

## Distributed processing

Distributed processing is justified for:

```text
high-volume historical processing
```

if the scenario requires it.

It is not needed for every source or every transformation.

---

## Streaming

Streaming should remain focused on:

```text
web events
```

because their:

```text
continuous arrival
+
latency requirement
```

justify that mode.

Do not redesign batch systems as streams.

---

## Serving

Serving should expose consumer-oriented representations.

Examples:

```text
detailed analytical dataset
aggregated dashboard mart
streaming metrics
```

Do not expose:

```text
raw
staging
internal operational tables
```

directly as final consumer interfaces unless specifically justified.

---

## Quality and contracts

The final architecture must preserve the distinction established earlier.

### Contract

```text
Does incoming data satisfy the expected interface?
```

### Quality

```text
Are the data values acceptable for downstream use?
```

They may occur near each other in the architecture but serve different purposes.

---

## Metadata and lineage

Metadata and lineage should span the architecture rather than appear only at the end.

They should support:

```text
discoverability
ownership
classification
provenance
impact analysis
```

No enterprise catalog implementation is required.

---

## Privacy

Use exactly one controlled example:

```text
customer_email
```

The architecture should show that this field may exist in restricted upstream layers but should not automatically propagate into serving datasets.

The principle is:

```text
collecting a field
≠
every consumer should receive it
```

---

## Expected artifacts

### `submission/architecture_components.csv`

Required columns:

```text
component
role
input
output
course_capability
```

---

### `submission/data_flows.csv`

Required columns:

```text
source
target
data
mode
purpose
```

---

### `submission/architecture_decisions.csv`

Required columns:

```text
decision
choice
alternative
rationale
tradeoff
```

---

### `submission/requirement_coverage.csv`

Required columns:

```text
requirement_id
requirement
architecture_element
coverage
evidence
```

No additional graded artifact is required.

---

## Visible validation

The final PRE should validate architecture rather than data values.

### Validation 1 — Requirement coverage

Verify:

```text
every requirement
→
has a coverage status
```

No requirement may disappear from the design process.

---

### Validation 2 — Component justification

Verify:

```text
every architecture component
→
maps to at least one requirement or risk
```

An unjustified component should be removed.

This is the architectural equivalent of avoiding unnecessary code.

---

## Required tests

Repository tests should verify:

1. All four required submission artifacts exist.
2. Required columns exist in every artifact.
3. Every declared requirement appears in `requirement_coverage.csv`.
4. Every requirement has a valid coverage value.
5. Every architecture component is referenced by a requirement, flow, or decision.
6. Required batch sources appear.
7. Required streaming source appears.
8. Raw, curated, and serving concepts are represented where justified.
9. Quality and contract capabilities remain distinct.
10. Incremental processing is represented for a changing entity.
11. Operational task control is represented.
12. Distributed processing is not assigned indiscriminately to all workloads.
13. Streaming is not assigned indiscriminately to batch sources.
14. Metadata and lineage span downstream dependencies.
15. Sensitive data are not exposed unnecessarily to serving consumers.
16. At least five architectural decisions contain explicit tradeoffs.
17. Output ordering is deterministic.

Tests should validate architectural consistency rather than exact component names.

---

## What students should observe

The complete course should collapse into one coherent sequence:

```text
sources
↓
ingestion
↓
storage
↓
transformation
↓
quality + contracts
↓
incremental / distributed / streaming processing
↓
operation
↓
serving
↓
metadata + lineage
↓
reliable consumers
```

But students should also understand:

```text
not every pipeline needs every capability
```

Architecture means selecting the capabilities required by the problem.

---

## Course closure

The final discussion should return to the course's central boundary:

### Database course

Primarily asks:

```text
How should data be stored and queried correctly?
```

### Data Engineering foundations

Primarily asks:

```text
How do data move from heterogeneous sources
to reliable, reproducible, operable
consumer-facing data?
```

### Analytics

Primarily asks:

```text
What can we learn or decide from the data?
```

### Data Products

Will later ask:

```text
How do we turn reliable analytical capabilities
into a product that delivers sustained value
to users?
```

This PRE should make those boundaries explicit.

---

## Boundaries

Do not introduce:

* cloud-provider architecture;
* Kubernetes;
* Terraform;
* CI/CD;
* service meshes;
* Delta Lake;
* Iceberg;
* Hudi;
* dbt;
* Kafka infrastructure;
* Airflow implementation;
* lakehouse implementation;
* MLOps;
* API product development;
* platform engineering;
* cost optimization frameworks.

No new technology should appear in the final week.

---

## Relationship with the complete PRE sequence

The final architecture should allow students to identify where each prior capability belongs:

```text
PRE_01  relational representation
PRE_02  SQL integration
PRE_03  transformation
PRE_04  analytical organization
PRE_05  physical formats
PRE_06  lake-style organization
PRE_07  semistructured data
PRE_08  batch ingestion
PRE_09  API ingestion
PRE_10  pipelines
PRE_11  quality
PRE_12  contracts
PRE_13  incremental processing
PRE_14  operations
PRE_15  distributed processing
PRE_16  events
PRE_17  streaming processing
PRE_18  serving
PRE_19  metadata and lineage
PRE_20  architectural integration
```

This list is for synthesis.

The architecture must not mechanically contain twenty separate components.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. No new technical capability is introduced.
2. A realistic scenario drives all architecture decisions.
3. Sources, consumers, requirements, and incidents are explicit.
4. The notebook uses no more than 10 cells.
5. Recommended implementation uses approximately 8–9 cells.
6. No code cell exceeds 12 effective lines.
7. Batch and streaming flows are distinguished.
8. Storage and processing choices are justified.
9. Quality and contracts remain conceptually distinct.
10. Incremental processing is applied selectively.
11. Distributed processing is applied selectively.
12. Serving is consumer-oriented.
13. Metadata and lineage support impact analysis.
14. Privacy is represented through one concrete restricted field.
15. At least five architectural decisions contain explicit tradeoffs.
16. Every requirement has explicit coverage.
17. Every architecture component has explicit justification.
18. The architecture does not use technology merely because it appeared earlier in the course.
19. The instructor can spend the class discussing **why the architecture has each element**, rather than explaining new code.
20. The activity provides a coherent closure to the complete course.
21. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use one compact deterministic business scenario;
* keep source and requirement counts small;
* generate all architecture artifacts programmatically;
* keep architectural reasoning visible in the notebook;
* do not introduce new technologies;
* do not force every previous concept into the design;
* remove any component that lacks a requirement or risk justification;
* keep tradeoffs explicit;
* keep coverage mechanically verifiable;
* preserve the 10-cell and 12-line hard limits.
