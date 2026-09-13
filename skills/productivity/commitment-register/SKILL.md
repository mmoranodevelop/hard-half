---
name: commitment-register
description: >-
  Use when tracking promises an MD made to board, customers, or the team, with
  owners and dates — an integrity register. Not raid-register, not meeting-
  notes-to-decisions, not okr-cascade, not a task manager.
license: MIT
---

# Commitment Register

**Commitment Register — Integrity List** — one page: every live row has customer, performer, observable deliverable, date, status; Hot 3 + renegotiation ASK. Default: venture MD's personal guarantee list; same spine for F500 program chair.

Method origin: execution as a network of promises (Sull/Spinosa, HBR 2007 public); horizontal commitments are the ones that fail (HBR 2015 public). Reconstruct the four fields. Do not lecture promise theory.

If they want a commitments lecture: one paragraph then produce or stop.

## When to use

- "What did I actually promise the board / that customer / the works council?"
- After a board, QBR, all-hands, or messy week — extract the promises
- New chair inheriting verbal commitments; horizontal delivery slipping
- Weekly close needs a list; pre-board: done / slipped / renegotiated

## When not to use

- Program risks, issues, dependencies — [RAID Register](../../management/raid-register/SKILL.md)
- Decisions from a meeting (not always a promise) — [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md)
- Goals — [OKR Cascade](../../strategy/okr-cascade/SKILL.md)
- How many promises may be in flight — [WIP Limit](../../productivity/wip-limit/SKILL.md)
- Designing the meeting — [Decision Meeting](../../management/decision-meeting/SKILL.md)
- The close that inspects this register — [Weekly Cadence](../../productivity/weekly-cadence/SKILL.md)
- Metrics sitting that may reveal a broken promise — [Operating Review](../../management/operating-review/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Notes dump | Register + hot 3 + ASK |
| **redline** | "We already track actions" | Fail QA: tasks without a customer of the promise |
| **refuse** | Two load-bearing facts missing, strategy slide with no dates, or hide a miss | Issues list. Stop |
| **diagnose** | Weekly close or pre-board | Status every open row; do not rewrite history |

## Hard rules

1. **A promise has customer, performer, observable deliverable, date.** Missing any one = wish. Extract; do not mint a fake date.
2. **Status closed set:** on track / at risk / renegotiate / done / broke / candidate. No "ongoing". Date passed with no delivery or renegotiation = **broke**.
3. **Renegotiate before the date.** Silence past the date is a broken promise.
4. **Tag vertical / horizontal.** Horizontal needs named accepter, date, and what happens if it slips.
5. **Do not duplicate RAID or OKRs.** "Legal might block us" is a risk; "I told the board we would file by 15 Sep" is a promise.
6. **The MD's register is this chair's hook** — including guarantees on behalf of the org. "Someone in ops will…" is not a row unless the MD is performer or guarantor.
7. **Open MD-guaranteed rows > ~7** → next start is a renegotiation or a kill, not a new promise. Link [WIP Limit](../../productivity/wip-limit/SKILL.md).
8. **One page for the live register.** History appendix. Board-facing: the 5 directors would recognise.
9. **Do not invent dates or counterparties.**

## Intake

If **two** of 1–2 are missing after one round: issues list, not a fake list.

1. Whose register (this MD / this program chair) — load-bearing
2. Sources (paste minutes, mails, notes) with a customer + date — load-bearing
3. Known board / customer dates
4. Existing action log? (so we don't fork)
5. WIP cap they will honour (or default 7)
6. Language
7. As-of date for the close

## Output shape

```
COMMITMENT REGISTER  |  [role]  |  as-of: [date]
Owner: [MD]
Open (MD-guaranteed): [n]    Horizontal of those: [n]    WIP warning if open > 7: Y/N

| ID | Promise (observable) | Customer | Performer | Date | V/H | Status | Source | Next move |
| [ ] | [ ] | [ ] | [ ] | [YYYY-MM-DD] | V/H | on track/at risk/renegotiate/done/broke/candidate | [ ] | [ ]

INTEGRITY THIS WEEK
Hot 3:
1. [ ]
2. [ ]
3. [ ]
Renegotiations to have (who, by when): [ ]
Broke (do not relabel): [ ]
Will not promise until open WIP drops: [ ]

EXTRACTED AND DISCARDED (not promises)
- wish: [ ]
- decision without obligation: [ ]
- risk → RAID: [ ]

ASK: [MD] renegotiates [named promise] with [customer] before [date], and will not add a new guarantee until open ≤ [n].
Holes: [ ]
```

## QA (must pass)

1. Every live row has customer, performer, deliverable, calendar date.
2. Status is the closed set. Broke is used if the date passed silently.
3. RAID risks and OKRs were not smuggled in. Candidates marked, not invented.
4. Horizontal rows tagged. Sources cited.
5. Hot 3 named if anything is at risk or broke.
6. Open count visible; cap or warning if bloated.
7. ASK has owner + date (renegotiation conversation).
8. One page (history appendix).
9. No invented dates.

If 1, 2, 3, or 7 fail: do not ship.

## Escalate / stop

- Jira dump of 200 tasks labelled "commitments" → refuse; extract the 10 with an external or board customer.
- Hide a miss from the board in this artefact → refuse. You may help write the renegotiation.
- Legal/contractual dispute → counsel; this register does not replace the contract.
- No sources, only vibes → stop. Four-field template, not a fake list.
- Personal to-do app or slogan strategy ("we will be #1") → refuse.

## Related

- [Weekly Cadence](../../productivity/weekly-cadence/SKILL.md) — the close inspects this register
- [WIP Limit](../../productivity/wip-limit/SKILL.md) — too many open promises *is* WIP
- [RAID Register](../../management/raid-register/SKILL.md) — risk, not obligation
- [OKR Cascade](../../strategy/okr-cascade/SKILL.md) — goals, not promises
- [Decision Meeting](../../management/decision-meeting/SKILL.md) — decisions; promote here only if someone accepted an obligation
- [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md) — decided/pending/parked; not an integrity register
- [Operating Review](../../management/operating-review/SKILL.md) — metrics; a miss may reveal a broken promise
