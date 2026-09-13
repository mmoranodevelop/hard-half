---
name: capacity-demand
description: >-
  Use when PS/delivery needs a 13-week sold-demand vs capacity view and a
  hire/sub decision. NOT for staffing-mix, not utilization-bench, not headcount-
  plan, not cash-runway.
license: MIT
---

# Capacity Demand

**13-week capacity vs demand — one page** — sold + weighted pipeline demand by week/role vs available capacity; gap; hire / subcontract / decline / re-sequence; one ASK. Default: professional services / delivery org; same spine for internal product delivery squads with sold commitments.

Method origin: SPI Research PS maturity / PSA practice (service execution: resource management + capacity planning tied to delivery) + TSIA / PSA public demand–supply–performance signal pattern + McKinsey public workforce/resource-allocation emphasis (match supply to prioritized demand; contractors as explicit capacity) + common PS 13-week rolling horizon (public capacity-planning practice). Reconstruct the operator board. Do not invent utilization targets as staffing decisions.

If they want a utilization lecture: one paragraph then produce or stop.

## When to use

- Next 13 weeks of sold work will overrun or under-run known capacity
- Pipeline is converting and nobody has a hire vs sub vs decline call
- Delivery is accepting work without a capacity check
- A weekly or biweekly capacity board is missing or is a vibe
- Role/skill bottlenecks (not named idle people) block commits

## When not to use

- Onshore / contractor / vendor **mix on one named program** for margin — [Staffing Mix](../../delivery/staffing-mix/SKILL.md)
- Named people idle this week + date back on billable — [Utilization Bench](../../delivery/utilization-bench/SKILL.md)
- Annual / quarterly HC plan (roles, start dates, cost) — [Headcount Plan](../../management/headcount-plan/SKILL.md)
- Bank cash / 13-week liquidity — [Cash Runway](../../management/cash-runway/SKILL.md)
- Rate list to quote — [Rate Card](../../delivery/rate-card/SKILL.md)
- WIP too high on live work — [WIP Limit](../../productivity/wip-limit/SKILL.md)

If sold demand and capacity sources are both missing, stop.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Roster capacity + sold book exist | 13-week board + gap actions + ASK |
| **redline** | They pasted "we're busy" or util % only | Force week×role hours; kill % as plan |
| **refuse** | No capacity base, or invent hours to close a gap | Issues list. Stop |

## Hard rules

1. **Horizon is 13 weeks rolling.** Not annual HC; not "this Monday's bench".
2. **Demand = sold first, then weighted pipeline.** Separate columns. Do not treat Stage-1 logos as sold hours.
3. **Capacity = available hours by role/skill** after known PTO, training, and already-assigned work — or HOLE. Do not invent headcount.
4. **Gap is hours (or FTE-weeks) by role**, not a feeling. Over = hire / sub / re-sequence / decline. Under = sell / bench plan (hand names to utilization-bench).
5. **Hire vs sub is an explicit choice** with lead time. Sub is capacity, not a mix card ([Staffing Mix](../../delivery/staffing-mix/SKILL.md) owns blend on one SOW).
6. **Decline / slip is allowed.** Accepting sold work without capacity is a fail.
7. **One ASK** — named delivery lead / MD to approve hire-req / sub ceiling / decline by date.
8. **Never invent** util %, margin %, or hours. Holes stay holes. Industry util benchmarks (SPI public recaps) are context only — not this week's staffing decision.
9. **One page** (+ optional week grid annex).

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake board.

1. Org / practice in scope and as-of Monday — load-bearing
2. Sold bookings with hours (or $→hours via rate card) by week — load-bearing
3. Capacity base: people × role × available hours (PTO known) — load-bearing
4. Pipeline with stage weights the org actually uses — load-bearing if over/under hinges on it
5. Role/skill taxonomy (same as staffing)
6. Subcontractor pool / MSA already available or "none"
7. Hire lead time (weeks) for scarce roles
8. Who has D on accept / decline / hire

## Output shape

```
CAPACITY vs DEMAND  |  [practice]  |  13 weeks from [Monday]  |  D: [name]
ASK: [D] to [approve hire-req / set sub ceiling / decline or slip X] by [date]

DEMAND (hours)
| Week | Sold | Pipeline (weighted) | Total demand |
| W1–W13 |  |  |  |

CAPACITY (hours)
| Role/skill | Available (after PTO/assigned) | Notes |
|  |  |  |

GAP
| Role | Hours gap (+over / −under) | Peak week | Action: hire / sub / re-seq / decline / sell |
|  |  |  |  |

ACTIONS
Hire: [role, FTE, start earliest]     Sub ceiling: [hours/$ or HOLE]
Decline / slip: [engagement, reason]     Bench handoff: → utilization-bench for names

NOT THIS PAGE
Program mix/margin → staffing-mix    Named idle → utilization-bench
Annual HC → headcount-plan    Bank 13-week → cash-runway

Holes: [ ]
```

Annex: `assets/week-grid.md`.

## QA (must pass)

1. 13-week horizon stated with as-of date.
2. Sold separated from weighted pipeline.
3. Capacity by role with source or HOLE — no invented people.
4. Gaps quantified; actions named (hire/sub/decline/re-seq).
5. One ASK with owner, verb, date.
6. Not a mix card, not a bench list, not annual HC, not cash.
7. No invented util% as the decision.
8. One page (+ optional grid).

If 1, 2, 4, or 5 fail: do not ship.

## Escalate / stop

- They want to hire from a util % with no 13-week hours → refuse; route % curiosity to [Utilization Bench](../../delivery/utilization-bench/SKILL.md) only for names.
- Sold work already accepted beyond capacity with no decline path → escalate to MD; page still shows the gap.
- Cash cannot fund hire/sub → note; [Cash Runway](../../management/cash-runway/SKILL.md) owns liquidity, not this board.
- Mix/margin on one SOW → [Staffing Mix](../../delivery/staffing-mix/SKILL.md).

## Related

- [Staffing Mix](../../delivery/staffing-mix/SKILL.md) — blend on one program; this is firm/practice 13-week supply/demand
- [Utilization Bench](../../delivery/utilization-bench/SKILL.md) — named idle people this week
- [Headcount Plan](../../management/headcount-plan/SKILL.md) — annual/quarter HC after this board says hire
- [Cash Runway](../../management/cash-runway/SKILL.md) — whether hire/sub is fundable
- [Rate Card](../../delivery/rate-card/SKILL.md) — converts $ bookings to hours
- [WIP Limit](../../productivity/wip-limit/SKILL.md) — too much in flight; capacity board still needed
