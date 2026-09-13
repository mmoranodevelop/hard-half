---
name: change-control
description: >-
  Use for one scope, cost, or time change against a signed baseline: baseline vs
  proposed, impact, approve/defer/reject, ASK the sponsor. NOT for raid-
  register, not project-charter, not sponsor-status.
license: MIT
---

# Change Control

**Change Request — One Named Delta** — one page: one scope / cost / time change against a signed baseline, integrated impact, approve / defer / reject, ASK the sponsor. Default: venture program; same spine for F500.

Method origin: PMI integrated change control public (review change requests against baselines; approve / defer / reject). Operator cut: one CR, not a CCB textbook.

If they want an ICC / change-log lecture: one paragraph then produce or stop.

## When to use

- Client or team wants something not on the signed charter / SOW / baseline
- Need impact on scope, cost, *and* time before anyone says yes
- A verbal "just add this" must become a signed delta

## When not to use

- First authorisation of the project — [Project Charter](../../project/project-charter/SKILL.md)
- Living risks / issues / deps — [RAID Register](../../management/raid-register/SKILL.md)
- Who has the D on changes (the map) — [Decision Rights](../../management/decision-rights/SKILL.md)
- Steering sitting with several decisions — [Steering Pack](../../project/steering-pack/SKILL.md)
- Weekly client status — [Sponsor Status](../../project/sponsor-status/SKILL.md)
- Buying the change as a new SOW — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Filing the ask as a tracker ticket (fields, list, checklists) — `client-ticket`

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. One named change | One-page CR + ASK |
| **redline** | They pasted an email thread or a 12-page CCB form | Baseline vs proposed; one ASK |
| **refuse** | Two load-bearing facts missing, or they want the log as the artifact | Issues list. Stop |

## Hard rules

1. **One named delta.** Two changes on one page without admitting they are two is a fail.
2. **Baseline vs proposed as two columns.** If you cannot name the baseline (version/date), you cannot change it — route to [Project Charter](../../project/project-charter/SKILL.md).
3. **Impact is integrated:** scope *and* cost *and* time *and* residual risk. A CR that only adds scope with "TBD days" is an issues list.
4. **Options:** approve as written / approve with a cut / defer to [date] / reject. Recommendation is one of those, with a named D.
5. **If approved, the baseline updates** (new version, new envelope, new date). Silent yes is how baselines die.
6. **If rejected, what happens** is on the page.
7. **Below-threshold tweaks** (inside the charter's written tolerance) are not this artifact — note and move. Above threshold = this page.
8. **Do not invent days or money.** Unknown is allowed if labelled.
9. **Do not bury the delta in RAID.** Do not rewrite the original charter as if the old fence never existed.

## Intake

If **two** of 1, 2, 5 are missing after one round: issues list, not a fake CR.

1. Baseline — charter / SOW / plan of record (date, version) — load-bearing
2. The change, one sentence — load-bearing
3. Why now
4. Requested by (name)
5. Impact they actually have — days, money, scope out, risk — or "unknown" — load-bearing
6. Who has the D (sponsor default)
7. If rejected, what happens

## Output shape

```
CHANGE REQUEST  |  [project]  |  CR-[n]  |  as-of: [date]
Client: [ ]     Baseline: [charter/SOW version / date]
Requested by: [name]     Class: SCOPE | COST | TIME | mixed
ASK: [sponsor / D] to APPROVE / DEFER to [date] / REJECT [CR-n] by [date]

BASELINE (today)
Scope in: [ ]     Out: [ ]
End date: [ ]     Envelope: [ ]     Success test: [ ]

PROPOSED
What changes: [one sentence]
Scope in (new): [ ]     Scope out (new or still): [ ]
End date: [ ]     Envelope: [ ]     Success test (if moved): [ ]

IMPACT (do not invent)
| Lens | Delta | Evidence / "unknown" |
| Time | [+n days / none / unknown] | [ ]
| Cost | [+amount / none / unknown] | [ ]
| Scope | [add / cut / none] | [ ]
| Risk residual | [inside / outside appetite / unknown] | [ ]
| Benefits / success tests | [hold / slip / unknown] | [ ]

If we say no: [what happens]
If we say yes: baseline becomes version [n+1] on [date]
Recommendation: [Approve as written / Approve with cut / Defer / Reject] because [one line]

NOT THIS PAGE
Original fence → project-charter    Living list → raid-register    Weekly status → sponsor-status

Holes: [ ]
```

## QA (must pass)

1. Named baseline (version/date).
2. ASK (D, approve/defer/reject, date).
3. Impact has a number where a number is required (or labelled unknown).
4. Scope, cost, and time are all addressed (not blank).
5. Not a RAID row or a charter rewrite.
6. No invented days or money.
7. One change, or two admitted as two.
8. "If we say no" is on the page.
9. One page.

If 1, 2, 4, or 6 fail: do not ship.

## Escalate / stop

- No baseline after one ask → [Project Charter](../../project/project-charter/SKILL.md).
- They want a 100-row change log as the MD pack → one CR or stop.
- "Just add it, we'll true-up later" → refuse silent baseline death.
- They want RAPID for who holds D → [Decision Rights](../../management/decision-rights/SKILL.md); this page still needs a named D.
- Safety / legal / data-residency change → counsel; still write the CR as a hole.

## Related

- [Project Charter](../../project/project-charter/SKILL.md) — the baseline this deltas
- [RAID Register](../../management/raid-register/SKILL.md) — living list; a CR is a decision, not a risk
- [Steering Pack](../../project/steering-pack/SKILL.md) — sitting that may take this CR
- [Decision Rights](../../management/decision-rights/SKILL.md) — who has the D
- [Vendor SOW](../../management/vendor-sow/SKILL.md) — priced change clause when buying
- [Sponsor Status](../../project/sponsor-status/SKILL.md) — reports after the baseline moved
- [Acceptance Signoff](../../project/acceptance-signoff/SKILL.md) — if conditions from UAT move the baseline
