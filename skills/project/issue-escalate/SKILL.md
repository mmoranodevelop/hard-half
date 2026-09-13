---
name: issue-escalate
description: >-
  Use for ONE named issue: impact, options tried, escalate ladder, one ASK. NOT
  for raid-register, not client-escalation, not severity-customer, not decision-
  meeting.
license: MIT
---

# Issue Escalate

**One Named Issue — Escalate Card** — one page: impact if we do nothing, options already tried, escalate ladder (who / when), one ASK. Default: venture / PS delivery; same spine for F500 programs.

Method origin: Manage-by-exception / escalation-path public (raise when tolerance or authority is exceeded) + ITIL hierarchical escalation high-level (management authority, not a sev taxonomy).

If they want an ITIL / exception-report lecture: one paragraph then produce or stop.

## When to use

- One named issue the current owner cannot close inside their authority / time / resources
- Need a clean escalate ask: impact, tried, who next, by when
- "We've been circling" and someone must decide or unlock
- Tolerance breach forecast (time / cost / scope / quality) needs a dated ladder

## When not to use

- Living RAID list — [RAID Register](../../management/raid-register/SKILL.md)
- Angry client this week (relationship / political) — [Client Escalation](../../accounts/client-escalation/SKILL.md)
- Customer-facing severity / incident sev taxonomy — [Severity Customer](../../delivery/severity-customer/SKILL.md)
- Room needs a decision facilitated — [Decision Meeting](../../management/decision-meeting/SKILL.md)
- ONE named *dependency* object to unblock — [Dependency Unblock](../../project/dependency-unblock/SKILL.md)
- Formal change to baseline — [Change Control](../../project/change-control/SKILL.md)
- Whole-project RYG — [Project Health](../../project/project-health/SKILL.md)
- Turning a new client ask into a tracker ticket — `client-ticket`

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. One named issue | Escalate card + ASK |
| **redline** | They pasted a ticket / RAID I-row dump | Force impact + tried + ladder; kill the vent |
| **refuse** | Two load-bearing facts missing, or blame theatre with no ASK | Issues list. Stop |

## Hard rules

1. **One named issue.** Symptom + object. Not a tour of I-rows.
2. **Impact if we do nothing** — dated, on delivery / cost / customer / compliance. No invented numbers.
3. **Options tried ≥1** with result. Escalation without attempted local fix is a fail unless authority was never local.
4. **Escalate ladder** — next 1–3 named roles/people, trigger (time or impact), and what you need from each (decide / resource / waive).
5. **One ASK** at the correct rung. Owner, verb, date. Not "please be aware."
6. **Escalate for decision or authority, not for cover.** Blame-only pages refuse.
7. **Do not invent sev labels** from a house taxonomy you were not given — describe impact in plain words.
8. **Not a RAID list, not a client anger pack, not a decision-meeting agenda.**
9. **One page.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake escalate.

1. Named issue (one sentence) — load-bearing
2. Impact if nothing by [date] — load-bearing
3. Current owner + what they already tried — load-bearing
4. Tolerance / authority limit that is exceeded or about to be
5. Candidate ladder (who has the next D)
6. The ASK at that rung
7. As-of date / when it opened

## Output shape

```
ISSUE ESCALATE  |  [PROJECT]  |  as-of: [date]
ASK: [rung owner] to [decide / resource / waive / unblock] by [date]

ISSUE
Name: [one sentence]
Opened: [date]    Current owner: [ ]    Authority limit hit: [time / cost / scope / quality / other]

IMPACT IF NOTHING
By [date]: [delivery / cost / customer / compliance effect — no invented $]
Evidence: [ ]

OPTIONS TRIED
1. [action] — result: [ ] — date: [ ]
2. [action] — result: [ ] — date: [ ]

ESCALATE LADDER
| Rung | Who | Trigger | Need from them |
| 1 (now) | [ ] | [ ] | [ ]
| 2 | [ ] | [ ] | [ ]
| 3 | [ ] | [ ] | [ ]

RECOMMEND RUNG: [n] because [≤12 words]

NOT THIS PAGE
RAID list → raid-register    Client anger → client-escalation    Sev taxonomy → severity-customer    Facilitate a room → decision-meeting

Holes: [ ]
```

## QA (must pass)

1. One named issue, current owner, opened/as-of.
2. Impact if nothing with a date (or hole) — no invented numbers.
3. ≥1 option tried with result (or explicit "authority never local").
4. Ladder with named next rung and need.
5. One ASK at the correct rung: owner, verb, date.
6. No blame-only; no invented sev taxonomy.
7. Not RAID, not client-escalation, not severity-customer, not decision-meeting.
8. One page.

If 1, 2, 5, or 6 fail: do not ship.

## Escalate / stop

- Client is the angry party and relationship is the job → [Client Escalation](../../accounts/client-escalation/SKILL.md).
- Baseline must change to resolve → [Change Control](../../project/change-control/SKILL.md); this card can be the exhibit.
- Many issues, no single object → [RAID Register](../../management/raid-register/SKILL.md) first.
- No impact statement after one ask → refuse.
- They want a sev taxonomy debate → [Severity Customer](../../delivery/severity-customer/SKILL.md) or refuse.

## Related

- [RAID Register](../../management/raid-register/SKILL.md) — living list
- [Dependency Unblock](../../project/dependency-unblock/SKILL.md) — dependency object, not issue
- [Client Escalation](../../accounts/client-escalation/SKILL.md) — angry client this week
- [Severity Customer](../../delivery/severity-customer/SKILL.md) — customer sev framing
- [Decision Meeting](../../management/decision-meeting/SKILL.md) — facilitate the room
- [Change Control](../../project/change-control/SKILL.md) — baseline delta
- [Project Health](../../project/project-health/SKILL.md) — period RYG
