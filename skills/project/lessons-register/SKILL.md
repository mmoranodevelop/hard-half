---
name: lessons-register
description: >-
  Use when maintaining a living cross-project lessons register: lesson, source
  project, action, owner, due, status, reuse. Not after-action-review (one
  event), not pre-mortem, not raid-register, not decision-log, not project-close
  alone.
license: MIT
---

# Lessons Register

**Living cross-project lessons register** — lesson, source project, action, owner, due, status, reuse tag. AAR is one event; this is the durable index the next PM actually searches. Default: PMO / multi-project shop; same spine for one long program with many phases.

Method origin: PMI lessons learned register (living project document → OPA updates) + NASA LLIS-style capture (validate, recommend, closed-loop infusion) — public concepts only.

If they want a KM / LLIS lecture: one paragraph then produce or stop.

## When to use

- Standing up or refreshing the shop's searchable lessons index
- After an AAR: promote 2–5 actions into the durable register
- Before kickoff: pull reuse lessons for a named new project
- Status of open lesson-actions is stale or orphaned

## When not to use

- One event's no-blame learning record — [After Action Review](../../management/after-action-review/SKILL.md)
- Pre-launch failure imagination — [Pre-mortem](../../management/pre-mortem/SKILL.md)
- Living R/A/I/D list — [RAID Register](../../management/raid-register/SKILL.md)
- Settled decision audit trail — [Decision Log](../../project/decision-log/SKILL.md)
- Close ceremony for one project — [Project Close](../../project/project-close/SKILL.md)
- Personal decision journal — stop; not this skill

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Register refresh or kickoff pull | Register page + one ASK |
| **redline** | They pasted a wiki dump or "lessons" slide | Force action/owner/due/status/reuse; kill essays |
| **refuse** | They want an AAR facilitated here, or no projects named | Issues list. Stop |

## Hard rules

1. **Living index, not one ceremony.** Each row: lesson → action → owner → due → status.
2. **Source project named.** Anonymous folklore fails.
3. **Reuse tag:** apply on [project types] / do not repeat / context-only.
4. **Open actions have dates.** "Monitor" is not a status.
5. **One ASK this period:** close orphan / promote AAR rows / pull for kickoff / retire stale. Owner, date.
6. **Do not invent impact $ or "industry benchmarks."** Hole them.
7. **Not an AAR writeup, not RAID, not decision log, not project-close pack.**
8. **Prefer ≤12 active rows on the page;** archive the rest by reference.
9. **Positive and negative lessons both welcome;** all-green registers are not credible.
10. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake KM system.

1. Scope of register (shop / program / named projects) — load-bearing
2. Candidate lessons (from AAR, close, or ops) with source project — load-bearing
3. Owners for open actions — load-bearing
4. Reuse context (upcoming kickoffs)
5. Last review date of the register
6. The ASK

## Output shape

```
LESSONS REGISTER  |  [shop / program]  |  as-of: [date]  |  last review: [date]
ASK: [owner] to [close orphan / promote AAR / pull for kickoff / retire] by [date]

ACTIVE LESSONS
| ID | Lesson (≤15 words) | Source project | Action | Owner | Due | Status | Reuse |

KICKOFF PULL (if any)
| Upcoming project | Lessons to apply | Owner |

RETIRED / ARCHIVED (count only): [n]  pointer: [ ]

NOT THIS PAGE
One event → after-action-review    Pre-launch → pre-mortem    RAID → raid-register    Close pack → project-close

Holes: [ ]
```

## QA (must pass)

1. Scope + as-of + last review.
2. Each active row has source project, action, owner, due, status, reuse.
3. No "monitor" without a date.
4. One ASK, owner, date.
5. ≤12 active rows on page (or justified).
6. No invented $ impact.
7. Not an AAR, RAID, decision log, or close pack.
8. One page.

If 2, 4, or 6 fail: do not ship.

## Escalate / stop

- They need the event facilitated → [After Action Review](../../management/after-action-review/SKILL.md).
- Register is empty and no sources after one ask → refuse fake rows.
- Legal / safety lesson needs formal LLIS-style clearance → flag specialist; do not publish raw.
- They want a novel knowledge platform built → refuse; this is the operator index.

## Related

- [After Action Review](../../management/after-action-review/SKILL.md) — one event record
- [Pre-mortem](../../management/pre-mortem/SKILL.md) — before launch
- [RAID Register](../../management/raid-register/SKILL.md) — live risks/issues
- [Decision Log](../../project/decision-log/SKILL.md) — settled decisions
- [Project Close](../../project/project-close/SKILL.md) — close ceremony; points here
- [Kickoff Pack](../../project/kickoff-pack/SKILL.md) — apply pull at start
- [Operating Review](../../management/operating-review/SKILL.md) — shop exceptions; lessons may feed
