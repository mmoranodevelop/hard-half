---
name: decision-journal
description: >-
  Use when logging a consequential decision before the outcome: situation,
  options, pick, expected, review date. Not an after-action review, not a pre-
  mortem, not a decision-rights matrix.
license: MIT
---

# Decision Journal

**Timestamped decision entry** — situation, real options (incl. do-nothing), pick, observable expected by a calendar review date. On review: process vs outcome, original block untouched. Default: venture MD logging a hire / bet / vendor / go-no-go unless they say F500.

Method origin: write the bet before the world answers (Farnam Street public template; Duke public on resulting).

If they want a resulting / decision-journal lecture: one paragraph then produce or stop.

## When to use

- "Log this decision" / review date is due
- Hire, bet, vendor, pricing, go/no-go, scope cut they will still care about in months
- They keep learning the wrong lesson from lucky wins

## When not to use

- After the event, "what did we learn?" — [After-Action Review](../../management/after-action-review/SKILL.md)
- Group "imagine it failed" — [Pre-mortem](../../management/pre-mortem/SKILL.md)
- Who gets to decide / RAPID / RACI — [Decision Rights](../../management/decision-rights/SKILL.md)
- Recap of a room's call — [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md)
- Board recommendation paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- Seconds-to-act operational calls; diary of feelings; low-stakes reversible choices — stop

If the outcome is already known: **review** a real old entry, or label a reconstruction. Do not back-fill "expected".

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Decision not yet (or just) taken | Complete entry + review date + ASK |
| **redline** | They pasted a journal | Fail vague expected, missing options, back-fill |
| **refuse** | Outcome known and no original; or pick with no options | Issues list. Stop |

Review date hit: same page, process vs outcome; do not edit the original.

## Hard rules

1. Before the outcome. Result already known + no original → refuse a fake log.
2. Five mandatory fields: situation · options · pick · expected · review date. Missing any = not an entry.
3. Options are real alternatives, including do-nothing. Note why rejects lost.
4. Expected is observable by the review date (range or probability if they have one). "It will go well" fails.
5. Review date is a calendar day, not "later".
6. Do not result. Good process can lose. Never update the original expected line.
7. One decision per entry. Plain words. Do not invent probabilities.
8. Private by default. Keep names at the level they can store.

## Intake

If **options** and **expected** are both missing after one round: issues list, not a fake log.

1. Situation (who, stakes, deadline)
2. Options on the table (incl. do-nothing) — load-bearing
3. Pick (they own it — you may structure, not choose)
4. Expected: what we will *see* by when — load-bearing
5. Review date (calendar day)
6. What must stay private / if review: original entry + what happened

## Output shape

```
DECISION JOURNAL  |  [short name]  |  [YYYY-MM-DD]
Time: [ ]   Owner: [name]   Status: logged | review
Review date: [YYYY-MM-DD]

SITUATION
[context a stranger needs]

OPTIONS
1. [ ] — rejected because [ ]
2. [ ] — rejected because [ ]
3. Do nothing — [kept / rejected because]

PICK
[choice]. Takes effect: [date]. Owner: [ ]

EXPECTED (observable by review date)
- We will see: [ ]
- Range / probability (if given, else "none given"): [ ]
- If this is wrong we will notice: [ ]

OPTIONAL
State: [ ]   Kill criteria: [ ]

ASK: [owner] confirms pick and files review on [date]. File / rewrite expected / refuse (outcome already known).
Holes: [ ]

REVIEW (only when reviewing — do not edit above)
Outcome (facts): [ ]
Knowable then: [ ]
Process: sound / mixed / unsound — [one reason]
Luck / other: [ ]
Calibration: [expected vs actual, one line]
Next time: hold / one change: [ ]
```

Also `assets/entry.md` and `assets/review.md`.

## QA (must pass)

1. Written as if outcome unknown (produce) or clearly split (review).
2. All five mandatory fields present. Review date is a calendar day.
3. ≥2 real options plus do-nothing, or an explicit reason there was no alternative.
4. Expected is observable — not a vibe.
5. ASK has owner + date.
6. No invented probabilities. Original block immutable on review.
7. One decision, not a bundle.
8. Not an AAR and not a pre-mortem.

If 1–5 fail: do not ship.

## Escalate / stop

- Outcome known, no original → refuse fake log; labelled reconstruction or [After-Action Review](../../management/after-action-review/SKILL.md).
- Journal as press release for a sold decision → refuse.
- Group premortem → [Pre-mortem](../../management/pre-mortem/SKILL.md).
- Fire-ground / seconds-to-act → do not journal.
- They want you to pick → structure options; they still own the pick.

## Related

- [Pre-mortem](../../management/pre-mortem/SKILL.md) — imagine failure of a plan; cousin, not a journal
- [After-Action Review](../../management/after-action-review/SKILL.md) — after the event
- [Decision Rights](../../management/decision-rights/SKILL.md) — who decides
- [Ninety-Day Onboarding](../../learning/ninety-day-onboarding/SKILL.md) — may log a few bets; this skill owns the entry
- [Meeting Notes to Decisions](../../writing/meeting-notes-to-decisions/SKILL.md) — what a room decided; not a personal bet log
