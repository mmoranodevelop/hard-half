---
name: ops-handover
description: >-
  Use when a project must hand to BAU: run owners, runbooks, SLAs, open defects,
  hypercare exit, one ASK. Not project-close alone, not acceptance, not M&A
  control handover, not cutover hour-by-hour, not go/no-go.
license: MIT
---

# Ops Handover

**Project → BAU handover + one ASK** — run owners, runbooks, SLAs / OLAs, open defects with owners, hypercare window and exit criteria. Control of day-to-day ops, not the close ceremony. Default: venture / product / IT delivery; same spine for F500.

Method origin: ITIL-aligned service transition / knowledge transfer public (run ownership and artefacts as entry criteria for live ops) + public hypercare practice (time-bound elevated support with pre-defined exit criteria, not endless project shadowing) + operator runbook craft. Reconstruct the operator board. Do not invent SLAs or defect counts.

If they want an ITIL / AMS lecture: one paragraph then produce or stop.

## When to use

- Go-live happened or is imminent and BAU must take the wheel
- Hypercare is running with no exit test
- Ops asks "who owns run, what's the runbook, what's still open?"
- Project team is the unofficial help desk with no end date

## When not to use

- Sponsor authorises project close / release people — [Project Close](../../project/project-close/SKILL.md)
- Client UAT accept / reject deliverables — [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md)
- M&A control register (bank, IdP, repos) at close — [Control Handover](../../ma/control-handover/SKILL.md)
- Hour-by-hour cutover sequence — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Go / no-go gate — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- Close Day-1 continuity (payroll, entity, bank) — [Day-1 Continuity](../../ma/day1-continuity/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Service/system named; ops counterpart exists or HOLE | One-pager handover + ASK |
| **redline** | They pasted "BAU will take it" with no owners/runbooks | Force owners, defects, hypercare exit; kill vibes |
| **refuse** | No BAU receiver named, or invent SLAs to close | Issues list. Stop |

## Hard rules

1. **Named run owners** (BAU person / team) for each critical run surface — or HOLE. Functions without names fail.
2. **Runbooks exist or are listed as holes** — link/location, not "we'll write later" as done.
3. **SLAs / OLAs are sourced** from contract or ops standard — never invented for the page.
4. **Open defects:** severity, owner, target; P1/P2 cannot be "known issues" without owners.
5. **Hypercare:** start, planned end, exit criteria (conditions, not only a calendar). Endless hypercare = failed handover.
6. **One ASK** — named ops lead / sponsor to accept run ownership (or refuse with holes) by date.
7. **Never invent** ticket counts, SLA numbers, or green RAG. Holes stay holes.
8. **One page** (+ optional defect annex).

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake handover.

1. Service / system / process being handed, as-of date — load-bearing
2. Named BAU receiver (ops lead) — load-bearing or HOLE
3. Runbook inventory (exist / missing) — load-bearing
4. Open defects / known errors with severity — load-bearing or "none evidenced"
5. Contract or standard SLA/OLA source (or "none")
6. Hypercare window and who staffs it
7. What project close still needs ([Project Close](../../project/project-close/SKILL.md) is sibling)

## Output shape

```
OPS HANDOVER  |  [service/system]  |  as-of: [date]  |  BAU D: [name or HOLE]
ASK: [BAU D / sponsor] to [accept run ownership / refuse until holes closed] by [date]

BLUF
Ready to hand: [yes / conditional / no]. Blockers: [run owners / runbooks / P1s / SLA source].

RUN OWNERS
| Surface (job/batch/queue/on-call) | BAU owner | Backup | Notes |
|  |  |  |  |

RUNBOOKS
| Topic | Location / link | Status exist/missing | Owner to finish |
|  |  |  |  |

SLAs / OLAs
Source: [contract / ops standard / HOLE]
Targets in force: [quoted or HOLE — do not invent]

OPEN DEFECTS
| ID/sev | Summary | Owner | Target | Blocks handover? |
| P1/P2… |  |  |  | Y/N |

HYPERCARE
Window: [start → planned end]   Staffing: [ ]
Exit criteria (all must hold): [conditions — not calendar alone]
Next review: [date]

NOT THIS PAGE
Close ceremony → project-close    UAT accept → acceptance-signoff
M&A controls → control-handover    Hour-by-hour → cutover-plan
Go/no-go → go-live-readiness    Close Day-1 → day1-continuity

Holes: [ ]
```

Annex: `assets/defect-annex.md`.

## QA (must pass)

1. BAU run owners named or HOLE — no anonymous "ops."
2. Runbooks listed with exist/missing.
3. SLA/OLA sourced or HOLE — not invented.
4. Open P1/P2 have owners or explicit none.
5. Hypercare has exit criteria (conditions).
6. One ASK with owner, verb, date.
7. Not close, UAT, control register, cutover, or go/no-go.
8. No invented ticket/SLA numbers.
9. One page (+ optional annex).

If 1, 6, or 8 fail: do not ship.

## Escalate / stop

- No BAU receiver will put a name on run → refuse; escalate to sponsor.
- P1 open with no owner → do not claim handover complete.
- M&A identity/bank/repo control → [Control Handover](../../ma/control-handover/SKILL.md).
- Still pre-go-live gate → [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) / [Cutover Plan](../../project/cutover-plan/SKILL.md).

## Related

- [Project Close](../../project/project-close/SKILL.md) — sponsor closes; this hands run
- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — client accept deliverables
- [Control Handover](../../ma/control-handover/SKILL.md) — M&A control register
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hour-by-hour
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — go/no-go
- [Day-1 Continuity](../../ma/day1-continuity/SKILL.md) — close continuity card
