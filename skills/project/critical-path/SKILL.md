---
name: critical-path
description: >-
  Use when naming this week's critical path + slips + float + one ASK to protect
  the path. Not a full MS Project file, not sponsor-status, not milestone-burn,
  not go-live-readiness, not cutover-plan.
license: MIT
---

# Critical Path

**This Week's Critical Path** — one page: the longest zero-float chain that still sets end date, what slipped, remaining float off-path, one ASK to protect the path. Default: venture / PS delivery; same spine for F500 cutovers in flight.

Method origin: Critical Path Method (CPM) public — longest dependent sequence with zero total float sets finish; float off the path is slack you may borrow only with eyes open. Goldratt/CCPM high-level if resource contention is the real constraint.

If they want a CPM / CCPM lecture: one paragraph then produce or stop.

## When to use

- "What is on the critical path *this week*?" and what protects end date
- A slip just landed and you need the path, not a Gantt tour
- Before go-live / cutover, to name the chain that still bites
- Resource fight: is the path task-order or a named scarce person

## When not to use

- Client-facing status letter — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Milestone burn / earned vs planned only — [Milestone Burn](../../project/milestone-burn/SKILL.md)
- Go-live gate checklist — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Cutover hour-by-hour runbook — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Whole-project RYG health — [Project Health](../../project/project-health/SKILL.md)
- One named dependency off-path to unblock — [Dependency Unblock](../../project/dependency-unblock/SKILL.md)
- Full schedule rebuild in MS Project / Primavera — stop; not this skill

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | This-week path page + ASK |
| **redline** | They pasted a Gantt / MS Project export | Extract path + float; kill the wallpaper |
| **refuse** | Two load-bearing facts missing, or they want the .mpp file | Issues list. Stop |

## Hard rules

1. **Clock is this week.** Not the whole WBS novel.
2. **Name the path as a short chain** (≤8 nodes): task → task → milestone. Each node: owner, need-by, remaining duration (or hole).
3. **Zero float on the path.** Any delay on a path node moves end date unless you crash / fast-track with a named trade.
4. **Float off-path is a number or a hole.** Do not pretend non-critical work is free — say remaining float in days.
5. **Slips: what moved, by how much, why** — evidence date. Do not invent days.
6. **One ASK to protect the path.** Hold / swap / crash / escalate / freeze non-path. Owner, date.
7. **If a scarce resource is the real constraint,** say so (CCPM lens) — path may be resource-chain, not just precedence.
8. **Not a go-live pack, not a cutover runbook, not a sponsor letter.**
9. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake path.

1. Named project + target end / next gate date — load-bearing
2. Current plan of record (baseline or last agreed schedule) — load-bearing
3. This week's path candidates or the live schedule export — load-bearing
4. Known slips since last week
5. Named scarce resources on the chain
6. The ASK (what must be true by when)
7. As-of date

## Output shape

```
CRITICAL PATH  |  [PROJECT]  |  week of: [date]  |  as-of: [date]
Target end / next gate: [date]    PM: [ ]
ASK: [owner] to [hold / swap / crash / escalate / freeze-non-path] by [date]

PATH (≤8, zero float)
| # | Node | Owner | Need-by | Rem. duration | Slip vs last week |
| 1 | [ ] | [ ] | [ ] | [ ] | [ ]
| … |  |  |  |  |  |

END DATE MATH
Plan end: [ ]    Forecast end: [ ]    Delta: [days or hole]
Driver: [path node that sets the date]

OFF-PATH FLOAT (≤5 that matter)
| Work | Owner | Float (days) | May borrow? |
| [ ] | [ ] | [ ] | yes/no + why |

RESOURCE LENS (if material)
Constraint: [named person / vendor / env]  Contention: [ ]

NOT THIS PAGE
Sponsor letter → sponsor-status    Go-live gate → go-live-readiness    Cutover runbook → cutover-plan    Full .mpp → refuse

Holes: [ ]
```

## QA (must pass)

1. Named project, week, target end / next gate.
2. Path ≤8 nodes with owners and need-bys (or holes).
3. Zero-float claim explicit; off-path float numbered or holed.
4. Slips stated with evidence date — no invented days.
5. One ASK, owner, date, verb that protects the path.
6. Not an MS Project file, not a sponsor letter, not a cutover runbook.
7. One page.

If 1, 2, 4, or 5 fail: do not ship.

## Escalate / stop

- Path red *and* baseline must move → [Change Control](../../project/change-control/SKILL.md) / [Steering Pack](../../project/steering-pack/SKILL.md).
- Cutover this weekend is the artifact → [Cutover Plan](../../project/cutover-plan/SKILL.md).
- Go / no-go checklist is the job → [Go-Live Readiness](../../project/go-live-readiness/SKILL.md).
- No end date and no schedule after one ask → refuse.
- They want the full .mpp rebuilt here → refuse.

## Related

- [Project Health](../../project/project-health/SKILL.md) — period RYG of the whole project
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — client-facing exceptions
- [Milestone Burn](../../project/milestone-burn/SKILL.md) — earned vs planned milestones
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — gate checklist
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hour-by-hour
- [Dependency Unblock](../../project/dependency-unblock/SKILL.md) — one named off-path or on-path dep
- [Change Control](../../project/change-control/SKILL.md) — when end date must move
