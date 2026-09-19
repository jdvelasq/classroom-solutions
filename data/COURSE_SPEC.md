# COURSE_SPEC.md

## Course

**Datos para Analítica**

Undergraduate course.

Duration: **13 weeks**.

The course belongs to the Analytics curriculum and provides the data-engineering foundations required to make data reliably available for analytical use.

---

## Course purpose

The course develops the principles and practical skills required to acquire, represent, store, integrate, transform, validate, operate, scale, and serve data for analytics.

The course is not intended to form a separate specialization in database systems or data engineering.

Its purpose is to strengthen the Analytics curriculum by giving students the engineering capabilities required to produce reliable analytical data.

The central question of the course is:

> How can data be transformed from heterogeneous sources into reliable, reproducible, and usable inputs for analytics?

---

## Position in the curriculum

The course complements the existing Analytics sequence.

Relevant courses include:

* Fundamentos de Analítica
* Analítica Descriptiva y Visualización de Datos
* Analítica Predictiva
* Productos de Datos

Fundamentos de Analítica is considered a fixed course. Its syllabus is not modified to accommodate this course.

Datos para Analítica must therefore complement Fundamentos de Analítica without requiring changes to its approved content.

The course should also provide useful preparation for Productos de Datos.

---

## Relationship with Bases de Datos I

Some students will have completed Bases de Datos I before taking this course.

Other students from different undergraduate programs may not have taken an equivalent database course.

Therefore:

* the course must be self-contained enough for students without prior database coursework;
* it may introduce the minimum relational concepts required for subsequent activities;
* it must not become a replacement for Bases de Datos I;
* formal database theory is not a central objective;
* normalization may be reviewed only at the level necessary to support the practical activities;
* SQL receives greater emphasis because practical SQL proficiency cannot be assumed.

The course uses database systems as components of data pipelines rather than treating database theory as its main object of study.

---

## Relationship with Fundamentos de Analítica

Fundamentos de Analítica and Datos para Analítica address complementary questions.

Conceptually:

```text
Datos para Analítica
source
→ ingestion
→ storage
→ transformation
→ validation
→ reliable data
```

```text
Fundamentos de Analítica
problem
→ data
→ analysis
→ evidence
→ interpretation or decision
```

Some technologies or concepts may appear in both courses, but with different purposes.

Examples:

* SQL in Fundamentos de Analítica may be used for analysis.

* SQL in Datos para Analítica is used primarily for integration and transformation.

* MapReduce in Fundamentos de Analítica introduces a computational paradigm.

* Distributed processing in Datos para Analítica develops the engineering implications of scaling data processing.

* Privacy in Fundamentos de Analítica may focus on anonymization and reidentification.

* Privacy in Datos para Analítica is treated primarily as a system, access, metadata, and governance requirement.

Overlap should be used only when it provides a different engineering perspective.

---

## Relationship with Productos de Datos

Datos para Analítica ends when reliable data have been made available to downstream analytical consumers.

Productos de Datos addresses subsequent concerns such as:

* analytical products;
* users;
* product requirements;
* deployment;
* interfaces;
* operation of complete data products;
* product lifecycle;
* value delivery.

Datos para Analítica must not become a preliminary version of Productos de Datos.

---

## Pedagogical architecture

The course follows the same general pedagogical architecture used in the Analytics curriculum.

### Weeks 1–2

The first two weeks provide conceptual foundations.

These weeks establish the map of the discipline and the vocabulary required for the practical sequence.

They are not divided into PRE activities.

### Weeks 3–13

The remaining eleven weeks are predominantly practical.

The practical sequence consists of in-class workshops identified by the prefix:

```text
PRE_
```

A class may contain one, two, or occasionally three PRE activities depending on their complexity.

A PRE is not defined by a fixed duration.

A short PRE may introduce a problem or concept that immediately enables a larger PRE.

A complex PRE may occupy an entire class.

The second block of the final week is reserved for course closure.

---

## Practical activity philosophy

Each PRE is a complete practical case.

Activities are organized around an engineering problem rather than around a software tool.

Prefer:

```text
problem
→ engineering limitation
→ principle
→ implementation
→ validation
→ artifact
```

Do not organize the course as:

```text
SQL tutorial
→ Parquet tutorial
→ Airflow tutorial
→ Spark tutorial
→ streaming tutorial
```

Technologies are introduced because they solve an engineering problem.

The practical sequence should progressively build a coherent mental model of the data lifecycle.

---

## Approved course sequence

The following sequence is frozen.

Activity names, ordering, and intended capability must not be changed during implementation unless explicitly approved.

### Week 1 — Foundations I

**Data engineering for analytics**

Topics:

* role of data engineering;
* data lifecycle;
* data sources and consumers;
* data architecture;
* operational and analytical systems;
* batch and streaming;
* reliability;
* scalability;
* relationship with databases, analytics, and data products.

---

### Week 2 — Foundations II

**Modern data platform**

Topics:

* formats and schemas;
* relational, NoSQL, and object storage;
* OLTP and OLAP;
* data warehouse;
* data lake;
* lakehouse;
* ETL and ELT;
* pipelines;
* data quality;
* orchestration;
* distributed processing;
* streaming;
* metadata;
* lineage;
* security;
* governance;
* cloud concepts.

---

### Week 3

#### PRE_01_relational_data

**From flat files to relational data**

Capability:

* tables;
* keys;
* relationships;
* minimum relational integrity required for subsequent activities.

Purpose:

Provide accelerated relational level-setting for students who have not completed a previous database course.

---

#### PRE_02_sql_integration

**Integrating data with SQL**

Capability:

* queries;
* filtering;
* aggregation;
* joins;
* subqueries;
* common table expressions.

SQL is treated as a practical data-engineering language.

---

### Week 4

#### PRE_03_sql_transformation

**Transforming data with SQL**

Capability:

* CASE;
* type conversion;
* missing values;
* CTEs;
* window functions;
* deduplication;
* views;
* derived tables.

---

#### PRE_04_analytical_warehouse

**From operational data to analytical storage**

Capability:

* facts;
* dimensions;
* star schemas;
* data marts;
* warehouse concepts.

---

### Week 5

#### PRE_05_data_formats

**Choosing data formats**

Capability:

* CSV;
* JSON;
* Parquet;
* schemas;
* data types;
* compression;
* row-oriented versus column-oriented storage.

---

#### PRE_06_data_lakehouse

**Organizing analytical data at scale**

Capability:

* object storage;
* partitioning;
* selective reads;
* data lakes;
* lakehouse concepts.

---

#### PRE_07_nosql_data

**Data that do not naturally fit relational tables**

Capability:

* semistructured data;
* document-oriented representation;
* basic criteria for SQL versus NoSQL.

---

### Week 6

#### PRE_08_batch_ingestion

**Batch ingestion**

Capability:

* files as sources;
* databases as sources;
* extraction;
* persistence;
* error handling.

---

#### PRE_09_api_ingestion

**API ingestion**

Capability:

* REST;
* JSON;
* pagination;
* parameters;
* authentication concepts;
* retries;
* persistence.

---

### Week 7

#### PRE_10_data_pipeline

**Building a reproducible end-to-end data pipeline**

This activity occupies the complete class when necessary.

Capability:

* extract;
* transform;
* load;
* ETL versus ELT;
* raw layer;
* staging layer;
* curated layer;
* configuration;
* reproducibility;
* logging.

---

### Week 8

#### PRE_11_data_quality

**Automating data quality**

Capability:

* completeness;
* validity;
* uniqueness;
* consistency;
* freshness;
* automated validation;
* tests.

---

#### PRE_12_data_contracts

**Making pipelines fail correctly**

Capability:

* schemas;
* data contracts;
* schema changes;
* validation;
* quarantine;
* controlled failure.

---

### Week 9

#### PRE_13_incremental_pipeline

**Processing only what changed**

Capability:

* full refresh;
* incremental loads;
* append;
* upsert;
* idempotency;
* fundamentals of change data capture.

---

#### PRE_14_pipeline_operations

**Operating a data pipeline**

Capability:

* dependencies;
* DAGs;
* scheduling;
* retries;
* backfill;
* logging;
* monitoring;
* basic observability.

---

### Week 10

#### PRE_15_distributed_processing

**From local processing to distributed processing**

This activity may occupy the complete class.

Capability:

* limitations of a single machine;
* partitioning;
* distributed execution;
* Spark DataFrames;
* Spark SQL.

The objective is distributed data processing, not Spark administration.

---

### Week 11

#### PRE_16_event_streams

**Thinking about data as events**

Capability:

* events;
* producers;
* consumers;
* brokers;
* event time;
* batch versus streaming.

---

#### PRE_17_streaming_pipeline

**Building a streaming pipeline**

Capability:

* continuous ingestion;
* windows;
* state;
* processing;
* delivery of results.

---

### Week 12

#### PRE_18_data_serving

**Serving data for analytics**

Capability:

* curated datasets;
* data marts;
* tables;
* views;
* analytical files;
* downstream analytical consumers.

---

#### PRE_19_metadata_lineage

**Knowing what the data are, where they came from, and who can use them**

Capability:

* metadata;
* catalogs;
* lineage;
* ownership;
* access;
* privacy;
* technical governance.

---

### Week 13

#### PRE_20_end_to_end_architecture

**Diagnosing and redesigning an end-to-end data architecture**

Capability:

Integrate the concepts developed throughout the course:

* sources;
* ingestion;
* storage;
* transformation;
* quality;
* pipeline operation;
* scale;
* serving;
* metadata;
* lineage;
* governance;
* architectural trade-offs.

The activity should require students to identify weaknesses in a data architecture and propose technically justified improvements.

---

### Final course block

The final block of Week 13 is reserved for course closure.

Its purpose is to integrate the complete conceptual journey and connect the course with:

* Analítica Descriptiva y Visualización de Datos;
* Analítica Predictiva;
* Productos de Datos.

No additional core technical topic should be introduced in this final block.

---

## Core progression

The approved practical progression is:

```text
relational foundations
↓
SQL integration
↓
SQL transformation
↓
analytical storage
↓
formats
↓
lake/lakehouse organization
↓
NoSQL
↓
batch ingestion
↓
API ingestion
↓
reproducible pipelines
↓
quality
↓
contracts
↓
incremental processing
↓
pipeline operations
↓
distributed processing
↓
events
↓
streaming
↓
serving
↓
metadata and lineage
↓
end-to-end architecture
```

Implementation must preserve this progression.

---

## Technologies

The curriculum specifies capabilities, not vendors.

Potential technologies may include:

* Python;
* SQL;
* SQLite or another approved relational database;
* Parquet;
* APIs;
* an approved orchestration tool;
* Spark;
* an approved mechanism for event streaming.

Technology selection must follow the rules established in `AGENTS.md`.

Do not introduce a technology merely because it is widely used in industry.

The simplest technology that exposes the intended engineering principle is preferred.

---

## Cloud

Cloud concepts should be visible throughout the course where relevant.

Cloud computing is not a standalone vendor-specific module.

The course should remain provider-neutral whenever practical.

Local execution is preferred for core activities.

AWS, Azure, Google Cloud, or other providers may be mentioned as production equivalents, but students should not normally require commercial cloud accounts to complete the practical sequence.

---

## Explicitly outside the core scope

The following topics are not core course objectives unless explicitly approved for a specific activity:

* advanced database administration;
* formal normalization theory beyond required level-setting;
* advanced transaction theory;
* cluster administration;
* advanced Spark tuning;
* Kubernetes;
* infrastructure as code;
* Terraform;
* advanced CI/CD;
* platform engineering;
* advanced Kafka administration;
* advanced change-data-capture infrastructure;
* Debezium deployment;
* advanced Flink;
* advanced dbt;
* MLOps;
* model deployment;
* full software-product development;
* complete API-product development;
* cloud certification content;
* vendor-specific infrastructure training.

These topics may be mentioned when necessary to explain the broader ecosystem, but they must not displace the approved learning sequence.

---

## PRE activities

`PRE_` activities are developed in class with the instructor.

They should support incremental live development.

The instructor should be able to explain the reasoning while constructing the solution progressively.

The completed repository contains the full solution.

The implementation must comply with `AGENTS.md`.

---

## LAB activities

`LAB_` activities, when created, are completed independently by students.

LAB activities should evaluate transfer of previously introduced capabilities.

A LAB should normally change the case, data, or engineering context sufficiently to require independent reasoning.

A LAB should not simply reproduce a PRE with renamed variables or different input values.

The LAB sequence will be defined separately.

The absence of a LAB associated with a PRE does not imply that the PRE is incomplete.

---

## Source of truth

This file defines the approved curriculum and activity sequence.

`AGENTS.md` defines implementation and repository rules.

Individual activity specifications, when created, define the detailed pedagogical and technical contract for a particular activity.

The precedence is:

```text
COURSE_SPEC.md
↓
AGENTS.md
↓
activity specification
↓
implementation
```

An implementation agent must not alter curriculum decisions.

If an implementation appears to require changing:

* an activity objective;
* activity order;
* activity boundary;
* course scope;
* curriculum progression;

the agent must stop and report the conflict rather than silently changing the course.
