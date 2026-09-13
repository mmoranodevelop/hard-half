---
name: decision-log
description: >-
  Use for a short project/program audit trail of settled decisions: D, date,
  alternatives killed, revisit trigger; one ASK if stale. NOT for the room pack,
  not meeting-notes extract, not personal decision journal, not RAPID map.
license: MIT
---

# Decision Log

**Project/program decision log — one page** — settled choices that shape the work: decision sentence, D, date, alternatives killed, revisit trigger, status. One ASK if entries are stale or missing D. Default: venture program; same spine for F500.

Method origin: project decision-log craft (six-field entry: title, date, owner, summary, alternatives, revisit trigger) + DACI/RAPID capture (record Approver/Decide + outcome; prevent re-litigation) + RAID-family decision register (audit trail, not meeting minutes). Reconstruct the operator index. Do not invent who decided.

If they want a DACI / RAPID / ADR lecture: one paragraph then produce or stop.

## When to use

- "Didn't we decide this?" — need the audit trail, not Slack archaeology
- Program needs a scannable list of settled forks (scope, vendor, sequence, kill)
- Onboarding a new PM / sponsor mid-flight
- Revisit triggers are due or missing

## When not to use

- Pack for a room that must decide *this week* — [Decision Meeting](../../management/decision-meeting/SKILL.md)
- Extract decisions from messy notes after the fact — [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md)
- Who has the D across recurring decision types — [Decision Rights](../../management/decision-rights/SKILL.md)
- Personal learning entry before the outcome (process vs outcome) — [Decision Journal](../../learning/decision-journal/SKILL.md)
- Living R/A/I/D period page — [RAID Register](../../management/raid-register/SKILL.md) (this library's D = Dependencies, not Decisions)

If nothing has been settled and no decision is on the table, stop — empty log is not an artifact.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Settled decisions exist or just landed | One-page log + ASK |
| **redline** | They pasted minutes or a wiki dump | Force decision sentences, D, alternatives, triggers |
| **refuse** | No settled decision, or invent D / dates | Issues list. Stop |

## Hard rules

1. **Settled only.** Discussion without a D and a date is not a row. "Leaning toward" fails.
2. **Verb sentence.** "Pricing" is a topic. "Ship one pricing tier at launch" is a decision.
3. **Named D** (Approver / Decide). Committee needs the written rule that made it a decision (chair / majority) — or HOLE.
4. **Alternatives killed** with one-line why. Missing alternatives = incomplete entry; mark HOLE — do not invent options.
5. **Revisit trigger** is observable (metric, date, event) or "stands until [gate/project end]". Vibes fail.
6. **Log at the moment of decision.** Retroactive Friday fiction is a fail; label reconstructions.
7. **One decision per row.** Bundle = split or refuse.
8. **Stale = trigger passed or D left with no successor** → ASK, do not silently refresh.
9. **Never invent** names, dates, or alternatives. Holes stay holes.
10. **One ASK** when something must be confirmed, reopened, or assigned a D — else "note only".
11. **One page** (± short annex of older closed rows by ID only).

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake log.

1. Program / outcome the log serves — load-bearing
2. Settled decisions to capture (or the one that just landed) — load-bearing
3. Who was D (or HOLE) — load-bearing
4. Alternatives on the table when decided
5. Revisit triggers / review dates due
6. Where the log must live (project home)

## Output shape

```
DECISION LOG  |  [program]  |  as-of [date]  |  curator: [PM]
ASK: [D/sponsor] to [confirm D# / reopen D# / assign D successor] by [date] — or note only

| ID | Decision (verb sentence) | D | Date | Alternatives killed (why) | Revisit trigger | Status |
| D1 | [ ] | [name] | [YYYY-MM-DD] | [B — why; C — why / HOLE] | [event/metric/date / stands until …] | stands / triggered / superseded |

TRIGGERED / STALE
- [ID]: trigger hit → reopen via decision-meeting / rights / journal as fits

NOT THIS PAGE
Room this week → decision-meeting    Notes extract → meeting-notes-to-decisions
RAPID operating model → decision-rights    Personal before-outcome log → decision-journal
Period R/A/I/Dependencies → raid-register

Holes: [ ]
```

## QA (must pass)

1. Every row is a settled verb sentence with a date.
2. D named or HOLE (never invented).
3. Alternatives killed present or HOLE.
4. Revisit trigger on every row.
5. One ASK if stale/missing D; else explicit note only.
6. Not a meeting pack, notes dump, rights matrix, personal journal, or RAID page.
7. No invented names/dates/options.
8. One page.

If 1, 2, 5, or 7 fail: do not ship.

## Escalate / stop

- Safety / legal decision with no D on record → stop; name a D before acting.
- Trigger hit and work continues as if nothing changed → ASK to reopen via [Decision Meeting](../../management/decision-meeting/SKILL.md).
- They want process-vs-outcome learning on one bet → [Decision Journal](../../learning/decision-journal/SKILL.md).
- They want who-has-D for a class of decisions → [Decision Rights](../../management/decision-rights/SKILL.md).

## Related

- [Decision Meeting](../../management/decision-meeting/SKILL.md) — take the decision in a room; then log it here
- [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md) — mine notes into candidate rows
- [Decision Rights](../../management/decision-rights/SKILL.md) — recurring RAPID/DACI map
- [Decision Journal](../../learning/decision-journal/SKILL.md) — personal before-outcome learning entry
- [RAID Register](../../management/raid-register/SKILL.md) — R/A/I/Dependencies; not this audit trail
