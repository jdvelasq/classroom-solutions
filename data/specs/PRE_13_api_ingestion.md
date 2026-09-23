# PRE Specification

## Identification

**Activity:** `PRE_21_api_ingestion`

**Week:** 6

**Status:** `READY`

---

## Activity title

**Ingerir datos desde una API**

---

## Central engineering insight

An API is a data source whose complete dataset may require several requests and whose availability is not fully controlled by the consumer.

The workshop should answer:

> How can we retrieve a complete dataset from a paginated API when one request may fail temporarily?

The central progression is:

```text
request
↓
validate response
↓
follow pagination
↓
retry transient failure
↓
persist complete result
```

The key lesson is:

```text
one successful HTTP response
≠
complete successful ingestion
```

---

## Course capability

Introduce only the minimum API-ingestion concepts required later:

* request;
* response;
* status code;
* JSON payload;
* query parameters;
* pagination;
* transient failure;
* bounded retry;
* response validation;
* persistence;
* ingestion report.

Authentication should be introduced conceptually but must not add infrastructure to the workshop.

---

## Engineering problem

The retailer obtains product reviews from an external API.

The API returns only a limited number of reviews per request.

The complete dataset therefore requires several pages.

During ingestion, one page fails temporarily.

Students must retrieve all pages without:

* silently losing records;
* retrying forever;
* duplicating pages;
* persisting an incomplete result as if it were complete.

---

## Deterministic local API

The core activity must not depend on public internet access.

Use a tiny deterministic API simulator included with the activity.

The simulator should behave like an HTTP API but remain completely local and transparent.

It should expose responses containing:

```text
status_code
JSON payload
```

and accept parameters such as:

```text
page
page_size
```

The simulation logic must remain simple enough to read.

Do not create a real web server unless there is a compelling implementation reason.

---

## Minimal API dataset

Use exactly:

```text
3 pages
```

with approximately:

```text
4–6 reviews per page
```

for a total of roughly:

```text
12–18 reviews
```

Suggested review fields:

```text
review_id
product_id
rating
review_date
review_text
```

The complete logical dataset should remain understandable.

---

## Response structure

A successful response should resemble:

```python
{
    "page": 1,
    "page_size": 5,
    "total_pages": 3,
    "items": [...]
}
```

Pagination information must come from the response.

Do not hard-code:

```text
3 pages
```

inside the ingestion loop merely because the classroom fixture contains three pages.

---

## Controlled transient failure

Use one deterministic failure:

```text
page 2
attempt 1 → status 500
attempt 2 → status 200
```

This is sufficient to teach retry behavior.

No additional transient-failure cases are required.

---

## Retry policy

Use:

```text
max_attempts = 3
```

A successful retry should make visible:

```text
temporary failure
→ retry
→ recovery
```

Retries must be bounded.

Do not implement:

* exponential backoff;
* jitter;
* circuit breakers;
* complex retry libraries.

These are unnecessary for the central lesson.

---

## Notebook execution budget

Available teaching allocation:

**approximately 75–80 minutes**

Hard constraints:

```text
maximum notebook cells: 8
recommended cells: 7

maximum effective code lines per code cell: 12
```

All essential API-ingestion logic must first be visible in the notebook.

---

## Notebook progression

### Cell 1 — Make one request

Request:

```text
page = 1
```

and inspect:

```text
status code
payload metadata
items
```

Central discussion:

> What information tells us whether the request succeeded and whether more data remain?

---

### Cell 2 — Follow pagination

Use the metadata from page 1 to retrieve all required pages.

The loop should remain short and readable.

Students should see:

```text
page 1
page 2
page 3
```

being requested.

At this point, page 2 should expose the controlled transient failure.

---

### Cell 3 — Add bounded retry

Add the smallest possible retry logic around one page request.

The behavior should visibly become:

```text
page 1 → SUCCESS
page 2 → FAIL
page 2 → SUCCESS
page 3 → SUCCESS
```

Central discussion:

> Why should we retry some failures but not retry indefinitely?

---

### Cell 4 — Validate the complete response set

Combine the page results and validate:

```text
all expected pages received
review_id unique
required fields present
```

Do not perform broader data-quality analysis.

The central question is:

> Do we have a complete ingestible API result?

---

### Cell 5 — Persist the ingested data

Write:

```text
submission/reviews.parquet
```

only after successful complete retrieval.

Students should see the principle:

```text
complete validated ingestion
→ persist canonical result
```

rather than persisting an incomplete collection silently.

---

### Cell 6 — Consolidate the ingestion logic

Move the already visible logic into:

```text
src/ingest_api.py
```

Suggested simple responsibilities:

```text
request_page(...)
fetch_all_pages(...)
```

No classes are required.

The notebook should execute the consolidated version once.

`src/` consolidates the visible lesson; it must not hide new logic.

---

### Cell 7 — Generate the ingestion report

Generate:

```text
submission/api_ingestion_report.csv
```

Required columns:

```text
source_name
pages_requested
records_retrieved
retry_count
status
output_path
```

Expected canonical row:

```text
product_reviews
3
<record count>
1
SUCCESS
submission/reviews.parquet
```

---

## Optional eighth cell

Only if class time comfortably permits:

demonstrate one permanent malformed response, for example:

```text
status 200
but missing "items"
```

Expected behavior:

```text
FAIL
no canonical output produced from that run
```

This cell is optional.

The transient retry is the required diagnostic case.

---

## Required code philosophy

Students must directly see:

```text
how a page is requested
how success is checked
how pagination advances
how retry works
how results are combined
when output is persisted
```

Do not hide these mechanics behind an API-client library abstraction.

Prefer readable logic such as:

```python
response = request_page(page)

if response.status_code != 200:
    ...
```

over a generic call such as:

```python
reviews = client.fetch_everything()
```

before the mechanics have been demonstrated.

Classroom explanation should focus on:

* why APIs paginate;
* why request success must be checked;
* why transient failures occur;
* why retries must be bounded;
* why partial ingestion must not masquerade as complete ingestion.

---

## Authentication concept

Introduce authentication briefly as part of the API request model.

For example:

```text
Authorization: Bearer <token>
```

or:

```text
API key
```

The workshop must not use real credentials.

A fake value may appear only if useful to show where authentication information belongs.

Do not teach:

* OAuth flows;
* token refresh;
* secret-management infrastructure.

---

## Query parameters

Pagination should make query parameters visible conceptually:

```text
?page=2&page_size=5
```

The exact simulator interface may use Python arguments while preserving the same idea.

No additional filtering parameters are required.

---

## Failure classification

Only a minimal distinction is needed.

### Retryable example

```text
500
```

for the controlled transient failure.

### Non-retryable example

A malformed successful payload or a client-side error may simply fail immediately.

Do not build a full HTTP status-code taxonomy.

---

## Idempotency scope

Re-running the canonical ingestion should overwrite or recreate:

```text
submission/reviews.parquet
```

with equivalent logical content.

It must not append duplicate reviews.

Full incremental/idempotent pipeline semantics belong to `PRE_13`.

---

## Expected artifacts

### `submission/reviews.parquet`

Required properties:

* contains all reviews from all pages;
* one row per `review_id`;
* no missing page;
* no duplicate page ingestion;
* deterministic logical content.

### `submission/api_ingestion_report.csv`

Required columns:

```text
source_name
pages_requested
records_retrieved
retry_count
status
output_path
```

No additional submission artifact is required.

---

## Visible validation

Two validations are sufficient.

### Validation 1 — Completeness

Verify:

```text
records retrieved
=
records represented by all API pages
```

### Validation 2 — Uniqueness

Verify:

```text
review_id
```

is unique after page consolidation.

---

## Required tests

Repository tests should verify:

1. The local API simulator is deterministic.
2. Page 1 succeeds.
3. Pagination metadata are available.
4. Page 2 fails on the controlled first attempt.
5. Page 2 succeeds on the controlled retry.
6. Retry count is bounded.
7. All pages are retrieved exactly once successfully.
8. All expected review records are present.
9. `review_id` is unique.
10. Required fields are present.
11. `submission/reviews.parquet` exists.
12. `submission/api_ingestion_report.csv` exists.
13. Report counts match actual ingestion.
14. Re-execution produces equivalent logical output.
15. No public internet connection is required.

Tests should verify API-ingestion behavior rather than internal implementation structure.

---

## What students should observe

The complete workshop should reduce to:

```text
one API request
↓
pagination
↓
temporary failure
↓
bounded retry
↓
complete page set
↓
persist
↓
report
```

The essential engineering insight is:

> API ingestion must handle source behavior that is outside the direct control of the data pipeline.

---

## Boundaries

Do not introduce:

* real public APIs as a dependency;
* OAuth;
* async HTTP;
* concurrency;
* rate-limit optimization;
* exponential backoff;
* GraphQL;
* webhooks;
* streaming APIs;
* incremental API synchronization;
* orchestration.

Those concerns are unnecessary for this PRE.

---

## Relationship with PRE_08

`PRE_08` establishes ingestion from stable sources:

```text
file
database
```

`PRE_09` adds a source that may require:

```text
multiple requests
+
failure handling
```

The conceptual progression is:

```text
stable source ingestion
↓
unreliable external source ingestion
```

---

## Relationship with PRE_10

`PRE_09` still addresses only:

```text
source
→ raw/canonical ingestion
```

`PRE_22_data_pipeline` will integrate:

```text
extract
→ transform
→ load
```

into one reproducible workflow.

Do not build a full pipeline here.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. Exactly three pages are sufficient.
2. The complete API dataset remains visually understandable.
3. The notebook uses no more than 8 cells.
4. No code cell exceeds 12 effective lines.
5. One successful request is inspected explicitly.
6. Pagination is driven by response metadata.
7. Exactly one transient failure is required.
8. Retry behavior is bounded and visible.
9. Complete ingestion is validated before persistence.
10. Core logic appears visibly before consolidation into `src/`.
11. No external network dependency exists.
12. Authentication is introduced only conceptually.
13. `submission/reviews.parquet` contains the complete result.
14. `submission/api_ingestion_report.csv` summarizes observable ingestion behavior.
15. The instructor can focus on **why external-source ingestion requires pagination and failure handling**.
16. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use exactly three deterministic pages;
* use only one controlled transient failure;
* keep pagination and retry code fully visible before consolidation;
* do not use a public API;
* do not introduce asynchronous requests;
* do not introduce retry libraries;
* do not add authentication infrastructure;
* keep `src/ingest_api.py` minimal and functional;
* preserve the 8-cell and 12-line hard limits.
