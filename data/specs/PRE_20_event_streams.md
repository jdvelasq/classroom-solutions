# PRE Specification

## Identification

**Activity:** `PRE_24_event_streams`

**Week:** 11

**Status:** `READY`

---

## Activity title

**De eventos a estado**

---

## Central engineering insight

A stream is a sequence of events that arrive over time.

An event records something that happened.

State is derived by processing those events.

The workshop should answer:

> How can a sequence of individual sales events be consumed to maintain an evolving business state?

The central progression is:

```text
event
↓
consume
↓
update state
↓
next event
↓
update state again
```

The essential lesson is:

```text
event
≠
state
```

and:

```text
arrival order
≠
event-time order
```

---

## Course capability

Introduce only the minimum event-stream concepts required for the next PRE:

* event;
* event stream;
* immutable event;
* producer;
* topic/log intuition;
* consumer;
* event time;
* arrival order;
* derived state;
* running aggregation.

No real streaming infrastructure is required.

---

## Engineering problem

An online store produces one event whenever a sale occurs.

Each event contains information such as:

```text
event_id
event_time
product_id
quantity
sales_amount
```

The analytical system receives events one at a time.

Students must maintain:

```text
running total sales
```

as the events are consumed.

One event arrives later than another event that actually occurred after it.

Students must distinguish:

```text
when something happened
```

from:

```text
when the consumer received it
```

---

## Minimal input stream

Provide:

```text
data/sales_events.jsonl
```

Recommended size:

```text
8–12 events
```

Suggested fields:

```text
event_id
event_time
product_id
quantity
sales_amount
```

Use:

```text
3–4 products
```

The complete event stream should remain understandable.

---

## JSON Lines representation

Use one JSON object per line.

Example:

```json
{"event_id":"E001","event_time":"2026-09-16T10:00:02","product_id":"P01","quantity":1,"sales_amount":120.0}
```

The file order represents:

```text
arrival order
```

not necessarily:

```text
event-time order
```

---

## Controlled delayed event

Include exactly one delayed event.

Example arrival sequence:

```text
E001  event_time 10:00:02
E002  event_time 10:00:05
E003  event_time 10:00:03
```

Thus:

```text
E003
```

arrives after `E002` even though it occurred earlier.

This single case is sufficient.

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

All central stream-processing logic must remain visible.

---

## Notebook progression

### Cell 1 — Inspect the event log

Read:

```text
data/sales_events.jsonl
```

and display the events in file order.

State explicitly:

```text
file order
=
arrival order
```

Central question:

> What does each row represent?

The answer should be:

> One immutable occurrence.

---

### Cell 2 — Consume one event at a time

Iterate through the event sequence.

For each event, display only essential information such as:

```text
event_id
event_time
sales_amount
```

Students should observe:

```text
event 1
event 2
event 3
...
```

rather than loading the problem conceptually as one static analytical table.

Central discussion:

> What changes when we process records sequentially rather than assuming the complete dataset already exists?

---

### Cell 3 — Maintain running state

Initialize:

```text
total_sales = 0
```

For each event:

```text
total_sales += sales_amount
```

Show the state after each event.

Students should directly observe:

```text
event
→
state changes
```

Central lesson:

> State is produced by processing events.

---

### Cell 4 — Maintain keyed state

Extend the same idea to:

```text
sales by product
```

Use a small dictionary keyed by:

```text
product_id
```

Each event updates only the corresponding product state.

Example:

```text
P01 → 240
P02 → 180
P03 → 90
```

Central discussion:

> Why must a streaming system remember state across events?

---

### Cell 5 — Compare arrival order and event-time order

Display:

```text
arrival order
```

and:

```text
sorted by event_time
```

for the same events.

Highlight the single delayed event.

Students should observe directly:

```text
arrival position
≠
time when event occurred
```

Central question:

> Which time should be used if we later want to calculate metrics for real-world time windows?

Do not introduce watermark mechanics yet.

---

### Cell 6 — Map the local example to streaming architecture

Represent conceptually:

```text
producer
↓
topic / event log
↓
consumer
↓
state
```

Map the classroom components:

```text
sales system
→ producer

sales_events.jsonl
→ topic/log analogue

Python loop
→ consumer

running totals
→ state
```

No messaging server should be introduced.

Generate:

```text
submission/consumed_events.csv
```

containing the events in consumption order.

---

### Cell 7 — Generate the stream summary

Create:

```text
submission/stream_summary.csv
```

Required columns:

```text
metric
value
```

Required metrics:

```text
event_count
unique_products
total_sales
delayed_event_count
```

Expected:

```text
delayed_event_count = 1
```

The final totals must match the complete event sequence.

---

## Optional eighth cell

Only if class time comfortably permits:

replay the event log from the beginning and recompute the final state.

Students should observe:

```text
same immutable event log
↓
same derived final state
```

This provides a useful intuition for event replay.

Do not implement checkpointing or exactly-once semantics here.

---

## Required code philosophy

Students must directly see:

```text
how an event is read
how one event updates state
how keyed state is maintained
how arrival order is represented
how event time differs
```

Do not begin with a streaming framework abstraction.

Avoid:

```python
stream.process(...)
```

when the behavior can be shown transparently with a short loop.

Classroom explanation should focus on:

* why an event represents an occurrence;
* why events are often treated as immutable;
* why state must be maintained separately;
* why arrival order can differ from event time;
* why streaming architecture separates producer and consumer.

---

## Event versus state

This distinction must remain explicit.

### Event

Example:

```text
E005:
P02 sold $80 at 10:02:14
```

It describes something that happened.

### State

Example:

```text
P02 total sales = $340
```

It summarizes the result of several previously consumed events.

The state may change.

The historical event should not.

---

## Producer concept

Introduce producer as:

> The component that emits events when something happens.

No producer implementation is required beyond the supplied event stream.

Do not create separate processes.

---

## Topic/log concept

Use the JSONL file as a transparent analogue for:

```text
ordered event log
```

Explain that production streaming platforms may maintain named streams or topics.

Do not claim that:

```text
JSONL file = Kafka
```

The file is only a pedagogical representation of an ordered event sequence.

---

## Consumer concept

The Python iteration represents:

> A consumer reading events from the stream and applying processing logic.

No consumer-group or partition-assignment concepts are required.

---

## Event time

`event_time` means:

> When the business event occurred.

It must not be replaced by file position.

---

## Arrival order

Arrival order means:

> The order in which the consumer observes events.

One controlled delayed event is sufficient to establish that:

```text
event time
and
arrival order
```

may differ.

---

## Processing time

Processing time may be mentioned conceptually as:

> When the processing system actually handles the event.

Do not add timestamps generated during notebook execution because that would make the exercise less deterministic.

---

## Running aggregation

Use only two forms of state:

```text
total sales
sales by product
```

Do not add:

* averages;
* top-N;
* counts by several dimensions;
* sessions;
* windows.

Windows belong to `PRE_17`.

---

## Event replay

If discussed, introduce replay simply as:

```text
read the immutable event log again
→
rebuild derived state
```

No event-sourcing architecture is required.

---

## Expected artifacts

### `submission/consumed_events.csv`

Required fields:

```text
arrival_position
event_id
event_time
product_id
quantity
sales_amount
```

Required properties:

* one row per event;
* preserves arrival order;
* unique `event_id`;
* deterministic content.

---

### `submission/stream_summary.csv`

Required columns:

```text
metric
value
```

Required metrics:

```text
event_count
unique_products
total_sales
delayed_event_count
```

No additional submission artifacts are required.

---

## Visible validation

Only two validations are required.

### Validation 1 — Event preservation

Verify:

```text
input event count
=
consumed event count
```

and:

```text
event_id is unique
```

### Validation 2 — State reconciliation

Verify:

```text
final running total
=
sum of all event sales_amount
```

---

## Detecting the delayed event

Keep detection simple.

One event is delayed if:

```text
its event_time
<
the maximum event_time already observed
```

during arrival-order processing.

This makes the phenomenon directly observable.

No allowed-lateness policy is required yet.

---

## Required tests

Repository tests should verify:

1. `data/sales_events.jsonl` exists.
2. Each line represents one valid event.
3. `event_id` is unique.
4. Exactly one controlled delayed event exists.
5. Every input event is consumed exactly once.
6. Running total ends at the correct total sales value.
7. Per-product state reconciles with event data.
8. `submission/consumed_events.csv` exists.
9. Consumption order matches source-file order.
10. `submission/stream_summary.csv` exists.
11. Summary metrics match source events.
12. Re-execution produces equivalent logical results.

Tests should validate event semantics rather than implementation framework.

---

## What students should observe

The complete workshop should reduce to:

```text
immutable events
↓
consume sequentially
↓
update state
↓
maintain state by key
↓
observe delayed event
↓
event time ≠ arrival order
↓
stream architecture
```

The essential engineering insight is:

> Streaming systems process an evolving sequence of events and maintain state as those events arrive.

---

## Boundaries

Do not introduce:

* Kafka installation;
* Kafka brokers;
* consumer groups;
* Kafka partitions;
* offsets in depth;
* Spark Structured Streaming;
* Flink;
* window aggregation;
* watermarks;
* allowed lateness;
* exactly-once guarantees;
* distributed streaming infrastructure.

Those concepts are unnecessary here or belong to `PRE_17`.

---

## Relationship with PRE_15

`PRE_15` processes:

```text
bounded dataset
```

even though the computation may be distributed.

`PRE_16` introduces:

```text
events arriving over time
```

The distinction is:

```text
distributed
≠
streaming
```

---

## Relationship with PRE_17

`PRE_16` establishes:

```text
event
event time
arrival order
state
```

`PRE_21_streaming_pipeline` will add:

```text
time windows
late events
allowed lateness
watermark intuition
window finalization
```

Those concepts must not be implemented prematurely here.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The complete event sequence is small enough to inspect.
2. Exactly one delayed event is sufficient.
3. The notebook uses no more than 8 cells.
4. Recommended implementation uses approximately 7 cells.
5. No code cell exceeds 12 effective lines.
6. Sequential event consumption is visible.
7. Running state is visible.
8. Keyed state is visible.
9. Event time and arrival order are explicitly distinguished.
10. Producer/topic/consumer concepts are mapped without external infrastructure.
11. No real streaming framework is required.
12. No windows or watermarks are implemented.
13. The instructor can focus on **why events and state are different**, rather than on messaging-system syntax.
14. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use one tiny deterministic JSONL event sequence;
* include exactly one delayed event;
* keep event consumption explicit;
* use only simple Python state;
* do not introduce Kafka or another broker;
* do not introduce windows;
* do not introduce watermarks;
* do not hide the event loop in helpers before it has been demonstrated;
* preserve the 8-cell and 12-line hard limits.
