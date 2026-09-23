# PRE Specification

## Identification

**Activity:** `PRE_21_data_formats`

**Week:** 5

**Status:** `READY`

---

## Activity title

**Elegir cómo representar físicamente los datos**

---

## Central engineering insight

The same logical dataset can be stored in different physical formats.

Those formats preserve and expose information differently.

The workshop should answer:

> Why would we choose CSV, JSON, or Parquet if all three can represent the same sales data?

The central lesson is:

```text
same logical data
≠
same physical representation
```

Format choice affects:

```text
schema
types
storage
human readability
column-oriented access
```

---

## Course capability

Introduce the minimum physical-format concepts required by the rest of the course:

* CSV;
* JSON;
* Parquet;
* schema;
* data types;
* text versus binary representation;
* row-oriented versus column-oriented representation;
* compression;
* selective column reads.

The activity is about **engineering tradeoffs**, not file-format internals.

---

## Engineering problem

A sales dataset must be exchanged, inspected, and later processed analytically.

The same dataset can be stored as:

```text
CSV
JSON
Parquet
```

The data team must understand what changes — and what does not — when the physical format changes.

---

## Minimal input dataset

Provide:

```text
data/sales.csv
```

Suggested fields:

```text
transaction_id
transaction_date
customer_id
product_id
quantity
unit_price
sales_amount
```

Recommended size:

```text
2,000–5,000 rows
```

This is still small enough to execute instantly but large enough for file-size differences to be visible.

The first rows must remain easy to inspect.

---

## Notebook execution budget

Available teaching allocation:

**approximately 45–55 minutes**

Hard constraints:

```text
maximum notebook cells: 6
recommended cells: 6

maximum effective code lines per code cell: 12
```

No essential format behavior may be hidden in helper modules.

`src/` is not required.

---

## Notebook progression

### Cell 1 — Load the logical dataset

Read:

```text
data/sales.csv
```

Display:

* a few rows;
* shape;
* data types.

Central discussion:

> What information do we logically have before discussing how it is stored?

---

### Cell 2 — Write the same data in three formats

Generate under `temp/`:

```text
sales.csv
sales.json
sales.parquet
```

Use the same DataFrame as the source.

The code should make the equivalence explicit:

```text
one DataFrame
→ three physical representations
```

No additional formats are required.

---

### Cell 3 — Compare physical representation

Calculate for each file:

```text
file size
human-readable?
```

Students should directly inspect a small portion of:

```text
CSV
JSON
```

and contrast them with Parquet as a binary analytical format.

Central discussion:

> Why might human readability be useful, and why might we accept losing it?

Do not make absolute performance claims from file size alone.

---

### Cell 4 — Read the files back and compare types

Reload the three formats.

Compare the resulting schema/data types.

The activity should expose at least one clear example where text formats require inference or explicit parsing while Parquet preserves analytical type information more directly.

Recommended field:

```text
transaction_date
```

or another deliberately controlled typed field.

Central insight:

```text
values
and
schema information
are not the same thing
```

---

### Cell 5 — Read only selected columns

Request only:

```text
product_id
sales_amount
```

from the Parquet file.

Contrast conceptually with text formats, where reading a row-oriented text representation does not provide the same column-oriented storage behavior.

Do not benchmark execution time.

Central discussion:

> Why is column-oriented storage useful for analytical workloads that frequently read only part of a wide dataset?

---

### Cell 6 — Build the comparison artifact

Generate:

```text
submission/format_comparison.csv
```

Required rows:

```text
CSV
JSON
Parquet
```

Required columns:

```text
format
file_size_bytes
schema_preserved
human_readable
column_selection
primary_use_case
```

The table should summarize the engineering tradeoff demonstrated in the notebook.

---

## Required code philosophy

All format operations must be visible:

```text
read
write
reload
inspect
select columns
compare
```

Do not create utility functions merely to reduce notebook length.

The code should make **what happens** immediately apparent.

Classroom explanation should focus on:

* why physical representation matters;
* why text formats remain useful;
* why analytical formats retain richer schema information;
* why column-oriented storage is useful analytically;
* why there is no universally best format.

---

## Comparison principles

The workshop must avoid simplistic conclusions such as:

```text
Parquet is always better.
```

Instead, students should understand contextual choices.

### CSV

Useful when:

```text
simplicity
interoperability
human inspection
```

are important.

### JSON

Useful when:

```text
structured or nested interchange
```

is important.

The dataset in this PRE may remain flat; nested JSON is addressed elsewhere.

### Parquet

Useful when:

```text
analytical storage
typed schemas
column-oriented access
compression
```

are important.

---

## File-size comparison

File size may be shown because it is directly observable.

However:

```text
smaller file
≠
universally better format
```

The result depends on:

* data;
* encoding;
* compression;
* representation.

Do not generalize beyond the concrete example.

---

## Performance

Do not use timing as a required part of this PRE.

Do not claim:

```text
Parquet is faster than CSV
```

based on a classroom benchmark.

Performance depends on workload and environment.

The activity should establish the structural reason why Parquet can be advantageous for analytical access.

---

## Expected artifact

### `submission/format_comparison.csv`

Required columns:

```text
format
file_size_bytes
schema_preserved
human_readable
column_selection
primary_use_case
```

The artifact must be generated programmatically.

No additional submission file is necessary.

---

## Visible validation

Only one central validation is required.

Reload all three representations and verify that they preserve the same **logical sales values** for the fields required by the exercise.

Students should observe:

```text
physical representation changes
while
logical information remains equivalent
```

---

## Required tests

Repository tests should verify:

1. `data/sales.csv` exists.
2. All three temporary representations can be generated.
3. Reloaded datasets contain the expected row count.
4. Required logical values are preserved.
5. Parquet contains the expected columns.
6. Selected Parquet columns can be read independently.
7. `submission/format_comparison.csv` exists.
8. It contains exactly the required three formats.
9. File-size values correspond to generated files.
10. Output ordering is deterministic.

Tests must not depend on exact execution times.

---

## What students should observe

The complete workshop should reduce to:

```text
one logical dataset
↓
CSV / JSON / Parquet
↓
inspect physical differences
↓
reload
↓
compare schema behavior
↓
select analytical columns
↓
choose format according to use
```

The essential engineering insight is:

> File format is an architectural decision because it affects how data are stored, interpreted, and accessed.

---

## Boundaries

Do not introduce:

* Avro;
* ORC;
* Arrow internals;
* Parquet row groups in depth;
* encoding algorithms;
* compression-codec comparisons;
* performance benchmarking;
* schema evolution;
* data lakes;
* partitioned datasets.

Those topics are either later or outside the central lesson.

---

## Relationship with PRE_04

`PRE_04` asks:

> How should analytical data be logically organized?

`PRE_05` asks:

> How should that data be physically represented?

This establishes the distinction:

```text
logical model
≠
physical format
```

---

## Relationship with PRE_06

`PRE_05` introduces Parquet as an analytical format.

`PRE_22_data_lakehouse` will then ask:

> How can many analytical files be organized into a scalable dataset?

Do not introduce partitioned storage here.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. One dataset is represented in exactly three formats.
2. The notebook uses no more than 6 cells.
3. No code cell exceeds 12 effective lines.
4. All core format operations are visible.
5. File-size differences are directly observable.
6. Schema/type behavior is directly observable.
7. Parquet column selection is demonstrated.
8. No timing benchmark is required.
9. No format is presented as universally superior.
10. `submission/format_comparison.csv` summarizes the demonstrated tradeoffs.
11. The instructor can focus on **why a physical format is chosen**, not on file-format implementation details.
12. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use the smallest dataset for which format differences are clearly observable;
* keep the same logical records across all three formats;
* keep all essential operations visible in the notebook;
* do not add more formats;
* do not introduce timing benchmarks;
* do not introduce partitioning;
* do not hide logic in helper functions;
* preserve the 6-cell and 12-line hard limits;
* report the Parquet dependency requirement before changing repository dependencies.
