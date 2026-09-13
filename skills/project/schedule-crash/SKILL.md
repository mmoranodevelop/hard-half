---
name: schedule-crash
description: >-
  Use when compressing the critical path: crash vs fast-track options with
  cost/risk, recommended path, one ASK. NOT for critical-path (this week's
  chain), not estimate-confidence, not recovery-plan, not change-control, not
  eac-pulse.
license: MIT
---

# Schedule Crash

**Schedule compression — one page** — crash vs fast-track options on the critical path, cost and risk of each, recommended path, one ASK. Default: delivery recovery when end date must move in without cutting scope; same spine for go-live pulls.

Method origin: PMI schedule compression — **crash** (add cost/resources to critical-path activities for least incremental $/day) vs **fast-track** (overlap sequential work; risk/rework up, cost often flat). Only the critical path shortens the project.

If they want a CPM / compression lecture: one paragraph then produce or stop.

## When to use

- End date must come in; scope stays; you need options not vibes
- Path is late and someone asks "can we crash it?"
- Compare overtime / surge vs overlap before a SteerCo decision
- After [Critical Path](../../project/critical-path/SKILL.md) named the chain — now price the compress

## When not to use

- Name this week's path + float only — [Critical Path](../../project/critical-path/SKILL.md)
- Pre-commit confidence band — [Estimate Confidence](../../project/estimate-confidence/SKILL.md)
- Full recovery narrative (root cause → plan) — [Recovery Plan](../../project/recovery-plan/SKILL.md)
- Baseline / scope / cost change formal CR — [Change Control](../../project/change-control/SKILL.md)
- Cost at complete pulse — [EAC Pulse](../../project/eac-pulse/SKILL.md)
- Cut scope to hit date — say so; that is descope, not compression

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named path + target date | Options page + ASK |
| **redline** | They pasted "add people / work weekends" | Force crash vs fast-track table; kill non-path spend |
| **refuse** | No critical path named, or invent $/days | Issues list. Stop |

## Hard rules

1. **Critical path only.** Compressing float work does not move end date.
2. **Two levers named:** crash (cost↑) and fast-track (risk↑). Hybrid OK if labelled.
3. **Each option:** days saved, incremental cost (or hole), risk/rework, what breaks.
4. **Crash math:** prefer highest days-saved per incremental $ on path activities that are actually resource-bound (not "concrete must cure").
5. **Fast-track math:** name the overlap, the incomplete predecessor assumption, rework owner.
6. **Re-check path after each move** — a parallel path may become critical (crash limit).
7. **One ASK** — pick option A/B/hybrid / hold date / descope via CR. Owner, date.
8. **Never invent** days saved, overtime $, or float. Holes stay holes.
9. **One page.** Not a Primavera rebuild.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake compress.

1. Named project + current end date vs required end date — load-bearing
2. Critical path chain (≤8 nodes) or pointer to last critical-path page — load-bearing
3. Which path activities can take more people / overtime / vendor surge — load-bearing
4. Which sequential pairs can overlap — load-bearing or "none safe"
5. Cost ceiling for crash / risk appetite for fast-track
6. Who has D on date vs cost vs risk
7. As-of date of the schedule

## Output shape

```
SCHEDULE CRASH  |  [PROJECT]  |  as-of: [date]
Current end: [ ]    Required end: [ ]    Gap: [ ] days
Path source: [critical-path page / HOLE]

ASK: [D] to [pick crash / fast-track / hybrid / hold / descope-CR] by [date]

PATH (compress these only)
| # | Activity | Owner | Rem. dur | Crashable? | Overlap-with? |
| 1 |  |  |  |  |  |

OPTIONS
| Opt | Lever | Days saved | +Cost | Risk / rework | Notes |
| A | Fast-track |  | ~0 or HOLE |  | overlap: [ ] |
| B | Crash |  |  |  | resources: [ ] |
| C | Hybrid |  |  |  |  |

RECOMMENDED: [A/B/C] because [≤12 words]
New critical path after move: [same / shifts to: ]    Crash limit hit: y/n

NOT THIS PAGE
This week's path only → critical-path    Full recovery story → recovery-plan
Formal CR → change-control    EAC $ → eac-pulse    Pre-commit band → estimate-confidence

Holes: [ ]
```

Annex: `assets/crash-options.md`.

## QA (must pass)

1. Gap (current vs required) stated or HOLE.
2. Path activities listed; non-path not treated as schedule save.
3. ≥1 crash and ≥1 fast-track option, or explicit "lever unavailable".
4. Days / cost / risk per option — numbers or holes.
5. One ASK with owner, verb, date.
6. No invented days or $. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Path unknown after one ask → stop; run [Critical Path](../../project/critical-path/SKILL.md) first.
- Compression needs scope cut → [Change Control](../../project/change-control/SKILL.md); do not hide descope as crash.
- Cost of crash blows envelope → show option; [EAC Pulse](../../project/eac-pulse/SKILL.md) / contingency owns the money.
- They want the .mpp rebuilt here → refuse; keep the options page.

## Related

- [Critical Path](../../project/critical-path/SKILL.md) — name the chain first
- [Recovery Plan](../../project/recovery-plan/SKILL.md) — broader recovery narrative
- [Change Control](../../project/change-control/SKILL.md) — baseline change when date/scope moves formally
- [EAC Pulse](../../project/eac-pulse/SKILL.md) — cost at complete after crash spend
- [Estimate Confidence](../../project/estimate-confidence/SKILL.md) — pre-commit band
- [Contingency Reserve](../../project/contingency-reserve/SKILL.md) — buffer to fund crash
