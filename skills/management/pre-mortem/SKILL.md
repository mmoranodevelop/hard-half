---
name: pre-mortem
description: >-
  Use when a plan is about to launch and the room is too invested to dissent:
  imagine it already failed, harvest why, change the plan. Produces a
  strengthened-plan record. Not an AAR (after). Not RAID (live).
license: MIT
---

# Pre-mortem

**Strengthened-Plan Record** — one page: past-tense failure reasons, plan-change table with owner and date, RAID promotions, ASK the plan owner to apply the changes before the next gate. Default: venture launch; same spine for F500 (often the hour before a stage-gate).

Method origin: Klein, HBR 2007 (prospective hindsight). Opposite of a postmortem in time.

If they want a pre-mortem lecture: one paragraph then produce or stop.

## When to use

- A plan is about to launch and the room is too invested to dissent
- Before a Type 1 / hard-to-reverse decision
- A "risk workshop" is still "what might go wrong"

## When not to use

- The work is over — [After Action Review](../../management/after-action-review/SKILL.md)
- A living risk list — [RAID Register](../../management/raid-register/SKILL.md) (this record *feeds* RAID)
- No one has the D — [Decision Rights](../../management/decision-rights/SKILL.md)
- No briefable plan — [Program Charter](../../management/program-charter/SKILL.md) first
- The room that *takes* the decision — [Decision Meeting](../../management/decision-meeting/SKILL.md)
- Later Go/Kill of a live bet — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)
- How a KPI / bonus / agent reward will be eaten after it ships — that is `cobra-equilibrium`, not a past-tense plan failure

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Plan exists | Strengthened-plan record + leader prompt + ASK |
| **redline** | They pasted a risk workshop | Force past tense; force plan-change rows |
| **refuse** | Two load-bearing facts missing, or no plan | Issues list. Stop |

## Hard rules

1. **No plan, no pre-mortem.** Do not premortem a slogan.
2. **Past tense, spectacular failure.** The prompt *is* the method. "What might go wrong" is not this skill.
3. **Independent writing before sharing.** Round-robin from the owner. No live rebuttal during harvest.
4. **Reasons specific enough to change a plan.** "Communication" fails.
5. **The plan actually changes** — or an explicit accept-and-watch with an early-warning.
6. **Attack the plan, not a named person.** Do not invent reasons the room did not give.
7. **Session sits inside a working meeting.** Then the owner applies the table.

## Intake

If **the plan** and **horizon date** are both missing after one round: issues list.

1. The plan — one sentence plus paste or link — load-bearing
2. Horizon — "already failed as of [date]" — load-bearing
3. Who owns the plan
4. Who is in the room (people who know the work, including dissenters)
5. Next gate and its date
6. What must not stay unsaid (optional)

## Output shape

```
STRENGTHENED-PLAN RECORD  |  [project]  |  session: [date]  |  owner: [name]
Horizon (failed as of): [date]
Participants: [names]
Plan in one sentence: [ ]
Failure premise: By [horizon] this has failed spectacularly.

LEADER SAYS (verbatim): It is [horizon]. This has failed spectacularly. Write every reason that *did* go wrong — especially the ones you would not normally say. Silent. Then round-robin starting with [owner]: one unused reason each. Do not debate.

REASONS (past tense, specific — not "communication")
1. [reason] — harvested from: [name]
2. [reason]
3. [reason]

PLAN CHANGES
| Change to the plan | Addresses # | Owner | Date |
| [scope / sequence / kill-criterion / workaround] | [#] | [name] | [date] |

If no change: Accept [reason]. Why: [ ]. Watch: [early-warning].

RAID PROMOTIONS (after, not instead)
| Item | R/A/I/D | Owner |
| [ ] | [ ] | [name] |

EARLY-WARNING: [observable] — owner: [name] — first check: [date]

NOT THIS PAGE
After → after-action-review    Living list → raid-register

ASK: [plan owner] applies the table before [gate] on [date].
Holes: [ ]
```

## QA (must pass)

1. ASK + plan owner + gate date.
2. Prompt is past-tense failure, not "what might go wrong."
3. Reasons are specific; each has a plan-change row or accept-and-watch.
4. Plan-change table is not empty without explicit accepts.
5. Not substituted for AAR or RAID.
6. No blame theatre against a named person.
7. No invented reasons.
8. One page.

If 1, 2, 3, or 7 fail: do not ship.

## Escalate / stop

- No briefable plan → [Program Charter](../../management/program-charter/SKILL.md).
- They want a 5×5 heat map → refuse; that is not a pre-mortem.
- Work already over → [After Action Review](../../management/after-action-review/SKILL.md).

## Related

- [After Action Review](../../management/after-action-review/SKILL.md) — after; actual vs plan
- [RAID Register](../../management/raid-register/SKILL.md) — where surviving items live
- [Decision Meeting](../../management/decision-meeting/SKILL.md) — optional last hour before a Type 1
- [Program Charter](../../management/program-charter/SKILL.md) — the plan you brief
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — natural slot before go
