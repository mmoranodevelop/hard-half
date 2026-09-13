---
name: resource-collision
description: >-
  Use when the same scarce people or skills are contended across ≥2 projects
  this horizon: collision table, priority rule, resolve ASK. NOT for capacity-
  demand (13w sold vs capacity), not staffing-mix, not utilization-bench.
license: MIT
---

# Resource Collision

**Cross-project resource collision — one page** — named scarce people/skills hit by ≥2 live projects this horizon; collision table; resolve options (sequence / substitute / slip / decline / buy); one ASK. Default: PS / delivery org; same spine for internal multi-program delivery.

Method origin: Critical Chain multi-project (drum / scarce resource subordination; stagger starts; priority over politics) + PSA resource-conflict practice (central visibility, prioritization rules, leveling / substitution / negotiate timeline). Reconstruct the operator collision board. Do not invent hours or names.

If they want a CCPM / fever-chart lecture: one paragraph then produce or stop.

## When to use

- Same named specialist or scarce skill is booked on ≥2 projects in the same window
- Two PMs are fighting over one person; no written priority rule
- Soft-booked pipeline and hard-booked delivery collide on one head
- "We'll multitask" is the plan — call it a collision

## When not to use

- Practice-wide 13-week sold vs capacity (no named collision yet) — [Capacity Demand](../../delivery/capacity-demand/SKILL.md)
- Onshore / contractor / vendor **mix on one SOW** for margin — [Staffing Mix](../../delivery/staffing-mix/SKILL.md)
- Named idle people + date back on billable — [Utilization Bench](../../delivery/utilization-bench/SKILL.md)
- Annual / quarterly HC plan — [Headcount Plan](../../management/headcount-plan/SKILL.md)
- Too many starts, WIP cap — [WIP Limit](../../productivity/wip-limit/SKILL.md)

If there is only one project in scope, stop — not a collision.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. ≥2 projects + scarce names/skills | Collision table + resolve options + ASK |
| **redline** | They pasted "we're stretched" or util % | Force person/skill × project × window; kill vibes |
| **refuse** | No second project, or invent names/hours to close | Issues list. Stop |

## Hard rules

1. **Collision = same scarce person or skill, ≥2 projects, overlapping window.** One overworked person on one project is staffing-mix / WIP — not this page.
2. **Name the scarce unit.** Person and/or skill code. "The team" fails.
3. **Table shows demand vs availability in the window** — hours or % from a source, or HOLE. Do not invent bookings.
4. **Priority rule is written before the resolve.** Profit / client tier / contractual date / strategic tag — pick the org's rule; do not invent a score.
5. **Resolve options are verbs:** sequence (who waits) / substitute (named alt or HOLE) / slip date / decline or stop-start / buy (sub/hire — hand to capacity-demand for practice gap).
6. **Multitask is not a resolve** unless both projects accept the split and the split is dated. Default: one primary.
7. **One ASK** — named delivery lead / resource manager / MD to award the scarce unit by date.
8. **Never invent** util %, margin, or headcount. Holes stay holes.
9. **One page.**

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake board.

1. Horizon window (weeks / dates) — load-bearing
2. Scarce people or skills in collision — load-bearing
3. Projects contending (≥2) with what they need and when — load-bearing
4. Who has D on award / slip / decline — load-bearing
5. Org priority rule if any (or "none — hole")
6. Substitute pool / sub MSA available or not
7. Hard vs soft bookings labeled

## Output shape

```
RESOURCE COLLISION  |  [practice / program set]  |  window [dates]  |  D: [name]
ASK: [D] to [award scarce unit to Project X / slip Y / decline Z / approve sub] by [date]

SCARCE UNITS
| Person / skill | Available in window | Source | Notes |
| [ ] | [h or % / HOLE] | roster / PSA | |

COLLISIONS
| ID | Scarce unit | Project A need | Project B need | Overlap | Hard/soft |
| C1 | [ ] | [h, dates] | [h, dates] | [ ] | |

PRIORITY RULE (one line)
[profit / tier / contractual / strategic / none→HOLE]

RESOLVE OPTIONS (per collision)
| ID | Sequence | Substitute | Slip | Decline / stop-start | Buy (→ capacity-demand) |
| C1 | [who waits] | [name or HOLE] | [new date or HOLE] | [ ] | [ ]

NOT THIS PAGE
13w sold vs capacity → capacity-demand    One-SOW mix → staffing-mix
Named idle → utilization-bench    Annual HC → headcount-plan    Too many starts → wip-limit

Holes: [ ]
```

## QA (must pass)

1. ≥2 projects named; scarce unit named.
2. Overlap window stated; demand from source or HOLE.
3. Priority rule written or HOLE.
4. Resolve options are verbs; multitask not default.
5. One ASK with owner, verb, date.
6. Not capacity board, mix card, bench list, HC plan, or WIP cap.
7. No invented hours/util%/names.
8. One page.

If 1, 2, 5, or 7 fail: do not ship.

## Escalate / stop

- Contractual commit already sold beyond capacity with no decline path → escalate to MD; page still shows the collision.
- Safety-critical skill with no substitute → do not "split 50/50"; sequence or buy.
- Practice-wide hours gap without named collision → [Capacity Demand](../../delivery/capacity-demand/SKILL.md).
- They want util % as the decision → refuse; % is scoreboard not award.

## Related

- [Capacity Demand](../../delivery/capacity-demand/SKILL.md) — 13w sold vs capacity; hire/sub/decline at practice level
- [Staffing Mix](../../delivery/staffing-mix/SKILL.md) — blend on one named program
- [Utilization Bench](../../delivery/utilization-bench/SKILL.md) — named idle + date back
- [Headcount Plan](../../management/headcount-plan/SKILL.md) — annual/quarterly HC
- [WIP Limit](../../productivity/wip-limit/SKILL.md) — stop starting; finish
