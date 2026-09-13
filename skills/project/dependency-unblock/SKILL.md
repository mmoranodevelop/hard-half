---
name: dependency-unblock
description: >-
  Use for ONE named dependency (internal/external/vendor): owner, need-by,
  unblock options, one ASK. NOT for raid-register (list), not issue-escalate
  (issue not dependency), not vendor-sow, not raci-delivery.
license: MIT
---

# Dependency Unblock

**One Named Dependency — Unblock Card** — one page: what we need, from whom, by when, options to unblock, one ASK. Default: venture / PS program; same spine for F500 cross-team deps.

Method origin: Program dependency management public (owner + need-by on every external/cross-team link) + RACI accountable-owner practice — exactly one A per dependency decision.

If they want a RACI / dependency-matrix lecture: one paragraph then produce or stop.

## When to use

- One named dependency is blocking or about to block a need-by
- Internal team, external partner, or vendor owes a deliverable / decision / access
- "Who owns this dep?" is fuzzy and the clock is real
- Before escalating a person fight — first name the dependency object

## When not to use

- Living list of many R/A/I/D rows — [RAID Register](../../management/raid-register/SKILL.md)
- ONE named *issue* (impact + options tried + ladder) — [Issue Escalate](../../project/issue-escalate/SKILL.md)
- Buying / rewriting the vendor engagement — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Full responsibility map for the project — [RACI Delivery](../../project/raci-delivery/SKILL.md)
- Whole-project RYG — [Project Health](../../project/project-health/SKILL.md)
- This week's critical path chain — [Critical Path](../../project/critical-path/SKILL.md)
- Client anger this week — [Client Escalation](../../accounts/client-escalation/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. One named dep | Unblock card + ASK |
| **redline** | They pasted a dep log / RAID D-rows | Force one row; kill the list tour |
| **refuse** | Two load-bearing facts missing, or they want the whole matrix | Issues list. Stop |

## Hard rules

1. **One named dependency.** Object + provider + consumer. Not a tour of D-rows.
2. **Type it:** internal / external / vendor. Mandatory vs discretionary if known.
3. **Exactly one Accountable** for the unblock decision (RACI A). Name a person, not a team.
4. **Need-by date is load-bearing.** What slips if we miss it (path impact or hole).
5. **Unblock options ≥2** with trade-offs (workaround / swap / escalate / accept slip / change scope). "Monitor" is not an option.
6. **One ASK** — the smallest move that unblocks or forces a dated decision. Owner, date.
7. **Do not invent dates, SLAs, or contract clauses.** Hole them.
8. **Not a RAID list, not an issue card, not a new SOW.**
9. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake unblock.

1. Named dependency object (deliverable / decision / access / data) — load-bearing
2. Provider (who owes it) + consumer (who is blocked) — load-bearing
3. Need-by date + what breaks if late — load-bearing
4. Type: internal / external / vendor
5. Options already tried
6. Who has the A today (or "unknown")
7. The ASK candidate

## Output shape

```
DEPENDENCY UNBLOCK  |  [PROJECT]  |  as-of: [date]
ASK: [owner] to [provide / decide / workaround / escalate / accept-slip] by [date]

DEPENDENCY
Object: [deliverable / decision / access / data]
Type: internal / external / vendor    Mandatory / discretionary: [ ]
Provider (owes): [name + role]    Consumer (blocked): [name + role]
Accountable (A): [one person]    Need-by: [date]

IF LATE
Path / milestone hit: [ ]    Days at risk: [or hole]

OPTIONS TRIED
1. [ ] — result: [ ]
2. [ ] — result: [ ]

UNBLOCK OPTIONS (pick / recommend one)
| Option | Trade-off | Owner | By |
| Work around | [ ] | [ ] | [ ]
| Swap / resequence | [ ] | [ ] | [ ]
| Escalate for decision | [ ] | [ ] | [ ]
| Accept slip / change | [ ] | [ ] | [ ]

RECOMMEND: [option] because [≤12 words]

NOT THIS PAGE
RAID list → raid-register    Issue card → issue-escalate    New SOW → vendor-sow    Full RACI map → raci-delivery

Holes: [ ]
```

## QA (must pass)

1. One named dependency object, provider, consumer.
2. Need-by + if-late impact (or hole).
3. Exactly one Accountable named (or hole labelled).
4. ≥2 real unblock options; no "monitor."
5. One ASK, owner, date.
6. No invented dates / SLAs / contract text.
7. Not a RAID list, not an issue escalate, not a vendor SOW.
8. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Provider will not move and authority is above PM → [Issue Escalate](../../project/issue-escalate/SKILL.md) with this card as exhibit.
- Contract / SOW rewrite is required → [Vendor SOW](../../management/vendor-sow/SKILL.md).
- Many deps, no single object → [RAID Register](../../management/raid-register/SKILL.md) first; then return for the top one.
- No need-by after one ask → refuse.
- They want the whole RACI redrawn → [RACI Delivery](../../project/raci-delivery/SKILL.md).

## Related

- [RAID Register](../../management/raid-register/SKILL.md) — living list including D-rows
- [Issue Escalate](../../project/issue-escalate/SKILL.md) — issue, not dependency object
- [RACI Delivery](../../project/raci-delivery/SKILL.md) — full responsibility map
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — commercial engagement
- [Critical Path](../../project/critical-path/SKILL.md) — whether this dep sits on the path
- [Project Health](../../project/project-health/SKILL.md) — period RYG
- [Client Escalation](../../accounts/client-escalation/SKILL.md) — angry client this week
