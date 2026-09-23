# PRE Specification

## Identification

**Activity:** `PRE_22_streaming_pipeline`

**Week:** 11

**Status:** `READY`

---

## Activity title

**Cerrar ventanas cuando los eventos llegan tarde**

---

## Central engineering insight

Streaming metrics are often calculated over event-time windows.

Because events may arrive out of order, the system must decide:

> How long should a window remain open waiting for late events?

The workshop should answer:

> How can we calculate five-minute sales windows while allowing limited lateness and eventually finalizing each window?

The central progression is:

```text
event arrives
↓
assign event-time window
↓
detect whether it arrived out of order
↓
advance watermark
↓
is the event's window still open?
↓
accept or reject event
↓
update or finalize window state
```

The essential lesson is:

```text
window end
≠
window immediately complete
```

and:

```text
late event
≠
necessarily rejected event
```

---

## Course capability

Introduce only the minimum streaming-processing concepts required by the course:

* event-time window;
* fixed/tumbling window;
* window state;
* out-of-order event;
* late event;
* allowed lateness;
* watermark;
* open window;
* finalized window;
* too-late event.

The practical implementation should use simple deterministic Python.

A distributed streaming framework is not required.

---

## Engineering problem

An online retailer wants:

> Total sales every five minutes.

Events contain:

```text
event_id
event_time
sales_amount
```

but they do not always arrive in event-time order.

If a five-minute interval is finalized immediately when a later event appears, a delayed sale may be omitted.

If windows are never finalized, state grows indefinitely.

Students must implement a simple policy balancing these concerns.

---

## Minimal input stream

Provide:

```text
data/sales_events.jsonl
```

Recommended size:

```text
10–14 events
```

covering approximately:

```text
3 consecutive five-minute windows
```

Required fields:

```text
event_id
event_time
product_id
sales_amount
```

File order represents:

```text
arrival order
```

The complete sequence must remain easy to inspect.

---

## Window definition

Use fixed five-minute event-time windows.

For example:

```text
10:00:00 ≤ event_time < 10:05:00
10:05:00 ≤ event_time < 10:10:00
10:10:00 ≤ event_time < 10:15:00
```

Each event belongs to exactly one window.

Do not introduce:

* sliding windows;
* session windows;
* overlapping windows.

---

## Allowed lateness

Use exactly:

```text
allowed_lateness = 2 minutes
```

Define the classroom watermark as:

```text
watermark
=
maximum event_time observed so far
-
allowed_lateness
```

This is a simplified pedagogical model.

The watermark must never move backwards.

---

## Critical classification rule

For each arriving event, first determine:

```text
event_window
```

from its `event_time`.

Then determine whether the event arrived out of event-time order:

```text
event_time < max_event_time_seen_before_this_event
```

Finally determine whether the event's window is still open.

The canonical classification is:

```text
if event did not arrive out of order:
    ON_TIME

elif window_end > watermark:
    LATE_ACCEPTED

else:
    TOO_LATE
```

Equivalent conceptual rule:

```text
not out of order
→ ON_TIME

out of order
+
window still open
→ LATE_ACCEPTED

window already finalized
→ TOO_LATE
```

This rule must remain explicit in both notebook and tests.

---

## Controlled late-event cases

Include exactly two out-of-order cases.

### Late but accepted

An event arrives after a newer event has already been observed.

Its event-time window is still open because:

```text
window_end > watermark
```

Expected:

```text
LATE_ACCEPTED
```

Its value updates the corresponding window state.

---

### Too late

Another out-of-order event arrives after:

```text
window_end <= watermark
```

for its event-time window.

Expected:

```text
TOO_LATE
```

The window is already final.

The event must not modify its result.

---

## Notebook execution budget

Available teaching allocation:

**approximately 75 minutes**

Hard constraints:

```text
maximum notebook cells: 8
recommended cells: 7

maximum effective code lines per code cell: 12
```

All essential window, watermark, and state logic must remain visible.

---

## Notebook progression

### Cell 1 — Inspect arrival order

Load:

```text
data/sales_events.jsonl
```

Display:

```text
arrival_position
event_id
event_time
sales_amount
```

Students should already recognize from `PRE_16` that:

```text
arrival order
≠
event-time order
```

Do not reteach the entire event-stream model.

---

### Cell 2 — Assign five-minute windows

Derive for every event:

```text
window_start
window_end
```

from:

```text
event_time
```

Show the mapping explicitly.

Example:

```text
10:03:20
→
10:00:00–10:05:00
```

Central discussion:

> Why should the event be assigned according to when it happened rather than when it arrived?

---

### Cell 3 — Make the watermark visible

Process events in arrival order.

Maintain:

```text
max_event_time_seen
```

and calculate:

```text
watermark =
max_event_time_seen - 2 minutes
```

Display the watermark after each event.

Students should observe that:

```text
max_event_time_seen
```

never decreases and therefore the watermark never moves backwards.

Central idea:

> The watermark represents how far event-time processing is allowed to progress under the lateness policy.

---

### Cell 4 — Classify events by arrival and window state

For every arriving event:

1. determine whether it is out of order;
2. identify its event-time window;
3. determine whether that window is still open;
4. classify the event.

Allowed classifications:

```text
ON_TIME
LATE_ACCEPTED
TOO_LATE
```

Students should observe exactly:

```text
one LATE_ACCEPTED event
one TOO_LATE event
```

Central question:

> Why are both events out of order, but only one is allowed to modify state?

Expected answer:

> Because one belongs to a window that is still open, while the other belongs to a window that has already been finalized.

---

### Cell 5 — Maintain window state

For:

```text
ON_TIME
LATE_ACCEPTED
```

events, update:

```text
total_sales by window
```

Do not update state for:

```text
TOO_LATE
```

Students should directly see:

```text
accepted event
→
assigned window
→
window total changes
```

and:

```text
TOO_LATE
→
no state change
```

No additional metric is required.

---

### Cell 6 — Finalize windows

A window becomes final when:

```text
window_end <= watermark
```

Mark it:

```text
FINALIZED
```

Once finalized:

```text
its result no longer changes
```

Students should observe:

```text
OPEN
↓
possible late update
↓
watermark passes window end
↓
FINALIZED
```

Central discussion:

> Why can a streaming system not wait forever for every possible late event?

---

### Cell 7 — Persist and reconcile

Generate:

```text
submission/window_metrics.csv
submission/streaming_report.csv
```

Validate the finalized streaming result against a simple batch reference using exactly the same accepted-event policy.

The comparison should answer:

> Did the streaming state produce the expected final window totals?

---

## Optional eighth cell

Only if classroom time comfortably permits:

replay the same event sequence and demonstrate that the same final window metrics are produced.

No checkpoint recovery or exactly-once implementation is required.

---

## Required code philosophy

Students must directly see:

```text
how a window is assigned
how out-of-order arrival is detected
how the watermark is calculated
how window openness is evaluated
how lateness is classified
how accepted events update state
how a window becomes final
```

Avoid hiding the behavior behind:

```python
stream.window(...).watermark(...)
```

before students understand what those operations mean.

The instructor should explain:

* why windows use event time;
* why events arrive out of order;
* why some late events are accepted;
* why others are rejected;
* why a watermark is needed;
* why state eventually has to be finalized.

---

## Watermark interpretation

For this PRE:

```text
watermark
=
max event time observed
-
allowed lateness
```

The watermark expresses a processing policy:

> Windows whose end is at or before this event-time position may be considered final.

This is not proof that an earlier event can never arrive.

It is a decision about how long the system is willing to wait.

---

## Watermark monotonicity

Because:

```text
max_event_time_seen
```

never decreases:

```text
watermark
```

must never decrease.

The implementation must not recompute the watermark from the current event alone.

---

## Window-state rule

Each window has only two states:

```text
OPEN
FINALIZED
```

The rule is:

```text
window_end > watermark
→ OPEN

window_end <= watermark
→ FINALIZED
```

A `FINALIZED` window must not accept further modifications.

This provides the basis for event acceptance.

---

## Event classification

### `ON_TIME`

The event did not arrive out of event-time order.

Its event-time window receives the event normally.

---

### `LATE_ACCEPTED`

The event arrived out of event-time order, but:

```text
window_end > watermark
```

Its window remains open.

The event updates that window.

---

### `TOO_LATE`

The event belongs to a window satisfying:

```text
window_end <= watermark
```

The window is already final.

The event does not update state.

---

## Important ordering detail

When processing each event, the implementation must avoid making the classification depend accidentally on updating the watermark in the wrong order.

The logic should conceptually preserve:

```text
1. observe current processing state
2. identify event window
3. determine out-of-order status
4. update max event time / watermark consistently
5. determine whether the relevant window remains open
6. classify
7. update state only if accepted
```

The precise implementation may combine steps if behavior remains unambiguous and tests confirm the intended cases.

---

## Window finalization

A window becomes final when:

```text
window_end <= watermark
```

After finalization:

```text
result no longer changes
```

This connects:

```text
watermark progression
→
bounded state lifetime
```

No distributed state-store implementation is required.

---

## Batch reference

The batch reference should remain deliberately simple.

Use only events classified as:

```text
ON_TIME
LATE_ACCEPTED
```

Then calculate:

```text
accepted events
↓
group by event-time window
↓
sum sales_amount
```

Compare this result with the finalized streaming state.

The reference exists only to validate correctness.

It should not become a second analytical exercise.

---

## Structured Streaming

Spark Structured Streaming may be mentioned as an example of a production framework supporting:

```text
windows
watermarks
state
streaming execution
```

but it must not be the core implementation of this PRE.

The transparent Python implementation is pedagogically preferable because the decision logic remains visible.

---

## Expected artifact

### `submission/window_metrics.csv`

Required columns:

```text
window_start
window_end
total_sales
status
```

Submitted windows must have:

```text
status = FINALIZED
```

Each finalized event-time window should appear exactly once.

---

### `submission/streaming_report.csv`

Required columns:

```text
metric
value
```

Required metrics:

```text
event_count
on_time_count
late_accepted_count
too_late_count
finalized_window_count
validation_status
```

Expected controlled counts include:

```text
late_accepted_count = 1
too_late_count = 1
validation_status = PASS
```

---

## Visible validation

Only two validations are required.

### Validation 1 — Lateness policy

Verify exactly:

```text
1 LATE_ACCEPTED
1 TOO_LATE
```

and show that:

```text
LATE_ACCEPTED
→ window updated

TOO_LATE
→ window unchanged
```

### Validation 2 — Window reconciliation

Verify:

```text
streaming finalized totals
=
batch-reference totals
```

under the same accepted-event policy.

---

## Required tests

Repository tests should verify:

1. `data/sales_events.jsonl` exists.
2. `event_id` is unique.
3. Events cover the intended fixed windows.
4. Exactly one controlled event becomes `LATE_ACCEPTED`.
5. Exactly one controlled event becomes `TOO_LATE`.
6. `LATE_ACCEPTED` is out of order and belongs to a window with `window_end > watermark`.
7. `TOO_LATE` belongs to a window with `window_end <= watermark`.
8. Watermark never moves backwards.
9. Accepted events update their correct windows.
10. Too-late event does not modify finalized state.
11. A finalized window is never modified later.
12. Windows finalize according to the defined rule.
13. `submission/window_metrics.csv` exists.
14. Each finalized window appears once.
15. Final window totals match the batch reference.
16. `submission/streaming_report.csv` exists.
17. Report counts match actual event classifications.
18. Validation status is `PASS`.
19. Re-execution produces equivalent logical results.

Tests should validate streaming semantics rather than a particular framework implementation.

---

## What students should observe

The complete workshop should reduce to:

```text
events arrive out of order
↓
assign event-time windows
↓
watermark advances
↓
window remains OPEN
→ late event accepted
↓
watermark passes another window
→ window FINALIZED
↓
late event for finalized window rejected
↓
final metrics reconcile
```

The essential engineering insight is:

> A streaming pipeline uses a watermark to decide when event-time windows can be finalized, balancing late-data tolerance against bounded waiting and bounded state.

---

## Boundaries

Do not introduce:

* Kafka infrastructure;
* Spark Structured Streaming implementation;
* Flink;
* sliding windows;
* session windows;
* triggers;
* checkpoint recovery;
* distributed state stores;
* exactly-once guarantees;
* stream-stream joins;
* event-time skew analysis;
* production watermark tuning.

These concepts are unnecessary for the central lesson.

---

## Relationship with PRE_16

`PRE_16` establishes:

```text
event
event time
arrival order
state
```

`PRE_17` adds:

```text
event-time window
out-of-order event
late event
watermark
window finalization
```

The progression is:

```text
maintain state
↓
maintain time-bounded state
↓
decide when that state is final
```

---

## Relationship with PRE_13

Terminology must remain distinct.

`PRE_13` uses:

```text
checkpoint
source high-water mark
```

to represent batch-incremental source progress.

`PRE_17` uses:

```text
watermark
```

to represent event-time progress under late-arriving streaming data.

Therefore:

```text
source high-water mark
≠
streaming watermark
```

The concepts are related to progress but solve different problems.

---

## Relationship with PRE_18

`PRE_17` produces reliable derived streaming metrics.

`PRE_23_data_serving` asks:

> How should reliable analytical results be exposed for downstream consumers?

Do not introduce serving concerns here.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The complete stream remains visually understandable.
2. Exactly three fixed five-minute windows are sufficient.
3. Exactly one `LATE_ACCEPTED` event is required.
4. Exactly one `TOO_LATE` event is required.
5. The notebook uses no more than 8 cells.
6. Recommended implementation uses approximately 7 cells.
7. No code cell exceeds 12 effective lines.
8. Window assignment is visible.
9. Out-of-order detection is visible.
10. Watermark calculation is visible.
11. Watermark never moves backwards.
12. Window state is explicitly `OPEN` or `FINALIZED`.
13. `LATE_ACCEPTED` occurs only when the event's window remains open.
14. `TOO_LATE` occurs when the event's window has already finalized.
15. Finalized windows cannot change.
16. Window state is visible.
17. Final streaming results reconcile with a batch reference.
18. No production streaming framework is required.
19. The instructor can focus on **why windows need a lateness policy and eventual finalization**, rather than on streaming-framework syntax.
20. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use one tiny deterministic JSONL event stream;
* use exactly three five-minute windows;
* use exactly one `LATE_ACCEPTED` event;
* use exactly one `TOO_LATE` event;
* use exactly two minutes of allowed lateness;
* classify lateness from out-of-order arrival plus window state;
* define window finalization by `window_end <= watermark`;
* ensure finalized windows cannot be modified;
* keep window assignment and watermark logic fully visible;
* use simple Python state;
* do not introduce Spark Structured Streaming;
* do not introduce Kafka;
* do not add additional window types;
* do not hide core logic in helper functions before it has been demonstrated;
* preserve the 8-cell and 12-line hard limits.
