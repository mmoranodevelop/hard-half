---
name: span-of-control
description: >-
  Use when deciding managerial density / layers vs throughput this quarter —
  rightsize spans by work type, flag over/under-management, one ASK. NOT for
  org-one-pager (structure picture), not headcount-plan (hire plan), not
  staffing-mix (delivery mix).
license: MIT
---

# Span of Control

**Spans & layers decision pack** — baseline spans by manager archetype / work type, layer count top→front, over/under-management flags, throughput implication this quarter, one ASK (widen / add layer / freeze manager hire / flatten). Default: venture function; same spine for F500.

Method origin: McKinsey public managerial archetypes (player/coach, coach, supervisor, facilitator, coordinator) — span fit to work complexity, not a universal ratio. Bain public spans-and-layers — baseline first; skills-based vs task-based targets; best-in-class leaner layers. Deloitte public supervisory-burden — too-wide and too-narrow both destroy throughput.

If they want an org-design lecture: one paragraph then produce or stop.

## When to use

- "Are we over-managed?" / too many layers between CEO and front line
- Managers with span=1–2 (assistant-with-a-title) or spans that crush coaching
- Throughput this quarter is blocked by approval hops or manager load
- Before adding a manager layer or freezing manager hires
- Post-growth: headcount grew, spans and layers never re-baselined

## When not to use

- Draw who reports where for a named team — [Org One-Pager](../../management/org-one-pager/SKILL.md)
- Roles, start dates, fully-loaded cost, freeze vs hire — [Headcount Plan](../../management/headcount-plan/SKILL.md)
- Delivery bench mix (FTE / contractor / partner) — [Staffing Mix](../../delivery/staffing-mix/SKILL.md)
- Who has the D on a named decision — [Decision Rights](../../management/decision-rights/SKILL.md)
- Post-deal hold/absorb/merge per function — [Operating Model Choice](../../ma/operating-model-choice/SKILL.md)
- A 40-box enterprise operating-model redesign (slice to the function changing this quarter)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Managers + directs listable or HOLE | Baseline table + flags + one ASK |
| **redline** | They pasted "ideal span is 7" or a flatness slide | Kill magic numbers; force archetype + baseline |
| **refuse** | No managers named, no N, and they want "best practice spans" | Issues list. Stop |

## Hard rules

1. **No universal span.** McKinsey: span depends on managerial archetype and work complexity. Bain: skills-based vs task-based differ. Never ship "industry average = X" as a target without their baseline.
2. **Baseline before preach.** Count current solid-line spans and layers top→front. If the count does not exist, label HOLE — do not invent.
3. **Archetype on every manager row.** Player/coach, coach, supervisor, facilitator, coordinator (McKinsey) or skills vs task (Bain). Mismatch of archetype to span is the flag.
4. **Layers are a number.** Distance from named top to front line. Flag extra layers that add approval hops without coaching value.
5. **Both tails fail.** Too narrow → Deloitte supervisory burden / micromanagement / ghost layers. Too wide → no 1:1 capacity, quality drop. Name which tail.
6. **Throughput this quarter, not org theory.** Link each flag to a decision hop, coaching gap, or manager hire you would freeze/open.
7. **This is not the org picture.** Boxes and names live on [Org One-Pager](../../management/org-one-pager/SKILL.md). Costed roles live on [Headcount Plan](../../management/headcount-plan/SKILL.md).
8. **Do not invent spans, layer counts, or savings %.** Cite public method only as method; holes stay holes.

## Intake

If **manager list** and **what is changing this quarter** are both missing after one round: issues list.

1. Named top of scope + function / team
2. Manager list with solid-line direct counts (or HOLE)
3. Work type per manager (skills / task / archetype) or "unknown"
4. Layers top→front if known
5. Throughput symptom this quarter (slow decisions / coaching collapse / duplicate work)
6. Constraint (cannot fire, union, location, "keep titles")
7. ASK candidate (widen / flatten / freeze manager hire / add lead layer)

## Output shape

```
SPAN OF CONTROL  |  [function]  |  [date]  |  top: [name/role]
ASK: [widen spans / flatten layer / freeze manager hire / add lead] — Owner: [ ] — Decide-by: [ ]

BASELINE
Layers (top → front): [n or HOLE]
Managers counted: [n]    ICs / front line in scope: [n or HOLE]

| Manager | Archetype / work type | Span (solid) | Directs (n) | Flag (narrow/wide/ok) | Throughput link |
| [ ] | player-coach / coach / supervisor / facilitator / coordinator | [ ] | [ ] | [ ] | decision hop / no 1:1 / ok |

TAIL SUMMARY
Narrow (over-managed): [managers]. Wide (under-coached): [managers].
Layer flags: [extra hop / missing lead / ok]

NOT THIS PAGE
Org picture → org-one-pager    Costed hires → headcount-plan    Bench mix → staffing-mix

HOLES: [ ]
```

## QA (must pass)

1. Baseline spans or labelled HOLE — no invented averages.
2. Archetype / work type on each manager row (or unknown labelled).
3. Layers stated or HOLE.
4. Each flag ties to throughput this quarter.
5. One ASK + owner + date.
6. Not an org chart, not a hire plan, not a staffing-mix page.
7. No invented savings %, no "ideal span = 7" as gospel.
8. One page.

If 1, 5, or 7 fail: do not ship.

## Escalate / stop

- They want "best practice spans" with no managers named → refuse.
- They want to hide span=1 titles "for politics" → show the span; say so.
- Legal / works-council / TUPE on delayering → HR/counsel.
- They actually need the drawn boxes — [Org One-Pager](../../management/org-one-pager/SKILL.md).
- They actually need costed roles — [Headcount Plan](../../management/headcount-plan/SKILL.md).

## Related

- [Org One-Pager](../../management/org-one-pager/SKILL.md) — hardware picture; this page is density vs throughput
- [Headcount Plan](../../management/headcount-plan/SKILL.md) — freeze/hire $ and dates
- [Staffing Mix](../../delivery/staffing-mix/SKILL.md) — delivery FTE/contractor mix
- [Decision Rights](../../management/decision-rights/SKILL.md) — RAPID, not spans
- [Operating Model Choice](../../ma/operating-model-choice/SKILL.md) — post-deal cells
- [Skip-Level](../../management/skip-level/SKILL.md) — conversation two layers down
