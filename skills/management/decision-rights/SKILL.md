---
name: decision-rights
description: >-
  Use when a named decision is stuck: one-page RAPID map with one D. RAPID is
  not RACI and not a stakeholder map. Not an org chart, not a decision meeting,
  not a status review.
license: MIT
---

# Decision Rights

**One-page RAPID map** for **one decision** (Recommend, Agree, Perform, Input, Decide). Repeating-type skin only when they named a class (hire / change-request / vendor). Default: venture; same spine for F500.

Method origin: Bain RAPID public (Rogers & Blenko, HBR 2006). One line, not a book dump.

If they want a RAPID / RACI lecture: one paragraph then produce or stop.

## When to use

- A decision is stuck, revisited, or "everyone thought they decided"
- "Who has the D?" on a program or workstream
- A RACI cannot tell Recommend from Decide
- A committee "decides" with no decision rule

## When not to use

- Who believes what, and who talks — [Stakeholder Alignment](../../management/stakeholder-alignment/SKILL.md)
- The room that takes the call today — [Decision Meeting](../../management/decision-meeting/SKILL.md)
- Period exceptions / status — [Operating Review](../../management/operating-review/SKILL.md)
- Standing D for a program — [Program Charter](../../management/program-charter/SKILL.md)
- Board resolution paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- Task assignment (who does the work) is a RACI row — if they only need a task RACI, say so and stop; do not emit RAPID wallpaper. [RACI Delivery](../../project/raci-delivery/SKILL.md)

RACI ≠ RAPID ≠ stakeholder map. RACI = work. RAPID = who decides. Map = belief + conversation.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named decision | One-page RAPID map + ASK |
| **redline** | They pasted a RACI / "governance model" | Same people, one decision, one D; list extra A's you killed |
| **refuse** | No decision sentence, two D's for harmony, or org-chart request | Issues list. Stop |

Named a stream and not a call → still produce one live decision, plus `assets/workstream-r-d-p.md`.

## Hard rules

1. Write the sentence. Two verbs = two maps.
2. Place **one D** first. Test: after this person speaks, does the org move? If a group must hold D, pre-write the rule (majority / chair-break).
3. One **R**. Named **P** (not "the team"). **I** time-boxed. **A** only with written grounds (legal / regulatory / policy). Extra A's die.
4. Conflict: R vs A → D. I dissent is recorded, not a veto. Pocket veto after "you decide" is not RAPID.
5. Push Type 2 D's down. MD does not silently keep every workstream D.
6. Defaults if they have no facts (override, do not invent names): local Type 2 → stream lead; money / kill / extra time vs charter → sponsor; PM is R and usually P, not D.
7. **Do not invent RAPID names.**

## Intake

If **two** of 1, 3, 4 are missing after one round: issues list, not a fake map. "Improve governance" is not an input.

1. The decision, one sentence, with a verb — load-bearing
2. By when, and what breaks if late
3. Who they think the D is today (often two names — that is the bug) — load-bearing
4. Who will implement (P) — load-bearing
5. Whose facts are required (I) and any real constraint-holder (A) with grounds
6. One-off or repeating type

Cannot state the decision in one sentence after one ask → stop. Split the clump; do not RAPID a fog.

## Output shape

```
RAPID MAP
Decision (one sentence, verb): [ ]
By when: [ ]    Cost of delay: [ ]
Type: 1 irreversible | 2 reversible    One-off | repeating: [ ]

ASK: [D name] to [verb + object] by [date].

| Role | Name / title | Notes |
| D Decide | [one person] | Commits the org. Group rule: [none / majority / chair-break] |
| R Recommend | [one person] | Criteria agreed with D: [ ] |
| P Perform | [person] | Starts [date]. Also I? yes/no |
| I Input (time-boxed) | [names] — due [date] | Not a vote |
| A Agree (scarce) | [name or "none"] | Grounds: [policy/legal]. If R≠A, D decides |

Process: R gathers I (and A) by [date] → recommendation to D by [date] → D closes by [date] → P from [date].
Dissent from I: recorded; not a veto. Pocket veto: not allowed.

NOT DECIDING
- [split-off → its own map]

CUT
- Extra A's refused: [ ]
- Org-chart / RACI wallpaper refused: [ ]
```

Workstream add-on: `assets/workstream-r-d-p.md`.

## QA (must pass)

1. Decision sentence with a verb.
2. Exactly one D (or a group with a written rule).
3. Named P, not "the team".
4. ASK (D, verb, date).
5. A is not a crowd with no grounds.
6. Not an org chart or a RACI of tasks.
7. Not a stakeholder map (beliefs / conversations).
8. No invented names. One page.

If 1, 2, 3, or 4 fail: do not ship.

## Escalate / stop

- Two D's for harmony → refuse; offer I + one D.
- MD keeps a silent veto → refuse; that is not giving up the D.
- "The committee decides" with no rule → stop.
- Org redesign → stop.
- Board resolution needed → [Executive Board Memo](../../management/executive-board-memo/SKILL.md); RAPID may still name the D.
- They want a 2x2 of who is upset → [Stakeholder Alignment](../../management/stakeholder-alignment/SKILL.md).

## Related

- [Stakeholder Alignment](../../management/stakeholder-alignment/SKILL.md) — belief + conversation; not who has the D
- [Decision Meeting](../../management/decision-meeting/SKILL.md) — RAPID *today, in the room*
- [Program Charter](../../management/program-charter/SKILL.md) — standing D for the program
- [Operating Review](../../management/operating-review/SKILL.md) — where exceptions surface
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — gatekeepers are resource-owner D's
- [RAID Register](../../management/raid-register/SKILL.md) — many items exist because D/P was unnamed
