---
name: wip-limit
description: >-
  Use when too much is in flight: personal or program work-in-progress. Stop
  starting, finish. Not a RAID log, not a portfolio stage-gate, not a weekly
  cadence.
license: MIT
---

# WIP Limit

**WIP 1-pager** — unit, in-flight count, numeric cap below current, stop rule, named illegal start, this week's finish-or-kill. ASK: who has authority to stop starts this week. Default: venture MD's personal loops + one program unless they say F500.

Method origin: CT ≈ WIP / throughput (Little's Law, public); the system produces only as much as the bottleneck (Goldratt public). Reconstruct the cap. Do not quote *The Goal*.

If they want a Kanban lecture: one paragraph then produce or stop.

## When to use

- "We started seven things and finished none"
- MD's personal board has too many open loops; cycle time blowing out
- After a cut-list freed hours that immediately refilled with new starts
- Someone asks for a WIP cap, a stop-the-line rule, or to name the bottleneck

## When not to use

- Risks, assumptions, issues, dependencies — [RAID Register](../../management/raid-register/SKILL.md)
- Go/kill **funding** across a portfolio — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)
- Repeating weekly meetings — [Weekly Cadence](../../productivity/weekly-cadence/SKILL.md)
- Freeing hours on the calendar — [Calendar Audit](../../productivity/calendar-audit/SKILL.md)
- Promises as integrity — [Commitment Register](../../productivity/commitment-register/SKILL.md) (a promise can *be* a WIP item)
- Sprint-ritual religion, headcount cuts dressed as "focus"

If the problem is "we don't know what to fund", route to stage-gate. If "we funded too much and none of it finishes", stay here.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | Cap, in-flight list, bottleneck, stop rule, ASK |
| **redline** | "We already have a board" | Fail QA: a board without a cap is a status display |
| **refuse** | No in-flight count, or no authority and they want a fake program cap | Issues list. Stop |

## Hard rules

1. A board without a numeric cap is a mural. The cap is the mechanism.
2. Unit of WIP is one kind of item (decision, project, feature, customer commitment). Mix = you cannot cap.
3. Count what is actually in motion this week — not the roadmap, not "approved".
4. First cap is below current count. Cap the queue in front of the constraint first.
5. Stop rule, one sentence: if [stage] is at cap, nobody starts; finish, swarm the constraint, or kill. Starting the next thing is the failure.
6. Name one item that is now illegal to start. Parking in a "backlog" everyone still treats as active is cheating.
7. Personal and program are different boards. Do not mix columns. Throughput unknown → still cap, write "unknown". No invented precision.

## Intake

If **in-flight list** and **who can stop starts** are both missing after one round: issues list, not a fake cap.

1. Personal, program, or both
2. The unit (what we count) — load-bearing
3. List of in-flight items (paste; do not invent) — load-bearing
4. What finished in the last 4–6 weeks
5. Where work waits (hypothesis is fine)
6. Who has authority to stop starts — load-bearing

## Output shape

```
WIP  |  [personal | program]  |  [date]
Owner (stop-starts): [ ]

Unit: [one]
In flight now: [n]
Throughput last 4–6 weeks: [n] / unknown
Snapshot: CT ≈ [n] / [throughput] = [ ]  (or "not in steady state")

IN FLIGHT (actual motion this week)
| ID | Item | Stage | Owner | Age | Blocked by |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

Constraint: [stage or person] because [wait evidence] / unknown — cap starts anyway
Cap: [number] on [where]   Current: [n]   Hit?: Y/N
Stop rule: If [stage] is at cap, we do not start. We finish, swarm [constraint], or kill.

Will finish or kill this week:
1. [item] — finish / kill by [date] — owner [ ]
2. [ ]

Will not start (named, now illegal):
- [ ]

NOT THIS PAGE
RAID items → raid-register    Gated funding → portfolio-stage-gate    Hours → calendar-audit

ASK: [authority] enforces the cap and will not start [named item] this week, by [date]. Enforce / personal-cap-only / refuse (no count).
Holes: [ ]
```

## QA (must pass)

1. Unit defined. In-flight list is actual, not the roadmap.
2. Numeric cap exists and is below current count (first pass) or is being hit.
3. Stop rule is behavioural. ≥1 named item is now illegal to start.
4. ASK has owner + date (who stops starts).
5. Constraint named or "unknown — cap starts anyway".
6. RAID / stage-gate not duplicated. Personal vs program labelled.
7. No fake precision. One page.

If 1, 2, 3, or 4 fail: do not ship.

## Escalate / stop

- Story-point velocity / SAFe / tool migration → refuse; give the cap and the stop rule.
- "Raise utilisation at every stage" → name the bottleneck; do not flood it.
- Go/kill funding decision → [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md).
- MD is not the constraint's boss → cap *personal* WIP; name the org constraint as escalate, not a fake program cap.

## Related

- [Weekly Cadence](../../productivity/weekly-cadence/SKILL.md) — when the finish-or-kill happens
- [Calendar Audit](../../productivity/calendar-audit/SKILL.md) — hours; this is items
- [Commitment Register](../../productivity/commitment-register/SKILL.md) — promises; a promise can be a WIP item
- [RAID Register](../../management/raid-register/SKILL.md) — risks, not flow
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — funding gates, not WIP
