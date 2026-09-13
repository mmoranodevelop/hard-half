---
name: change-adoption
description: >-
  Use when a program is shipping a change and people must do the new behaviour:
  one-pager with owners, ADKAR barrier by role, leading indicators, one ASK. Not
  a 50-slide change strategy, not the business case, not the vendor SOW.
license: MIT
---

# Change Adoption

**Behaviour-change one-pager** — observable behaviour, receiving-manager owners, ADKAR barrier by role, leading indicators, this week's ASK. Default: venture program at go-live; same spine for F500.

Method origin: Kotter public (remove barriers, institute) + Prosci ADKAR public (barrier point by role). Do not dump *Leading Change*.

If they want a Kotter 8 / ADKAR lecture: one paragraph then produce or stop.

## When to use

- A system, process, or vendor deliverable is about to hit users
- "They're not using it" / utilisation is low / workarounds are high
- Sponsor asked for "the change plan" and meant *this release*

## When not to use

- Whether to do the program — [Business Case](../../strategy/business-case/SKILL.md)
- The vendor contract / definition of done — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Weekly KPI pack — [Operating Review](../../management/operating-review/SKILL.md)
- Senior belief before a decision — [Stakeholder Alignment](../../management/stakeholder-alignment/SKILL.md)
- First authorisation — [Program Charter](../../management/program-charter/SKILL.md)
- Cascade / all-hands script — [Cascade Script](../../comms/cascade-script/SKILL.md)
- Kickoff pack for the delivery team — [Kickoff Pack](../../project/kickoff-pack/SKILL.md)

Change-adoption ≠ vendor-sow ≠ business-case. Case = buy. SOW = vendor done. Adoption = people do the new thing.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default, before or at go-live | One-pager + role table |
| **redline** | They pasted a 50-slide "change strategy" | Strip to behaviour, owners, indicators; list slides you killed |
| **refuse** | No behaviour, no receiving owner, or they want a culture essay | Issues list. Stop |

Diagnose (allowed): low use after go-live → barrier point by role + this week's actions. Same page.

## Hard rules

1. **Name the behaviour:** who does what differently by when. "Digital transformation" is not a behaviour.
2. **Owner is a receiving manager.** Sponsor owns the definition of success. Comms is not the owner.
3. **ADKAR in order.** Barrier point = first element that is the hole. Do not train when Awareness or Desire is the hole.
4. **Structural first.** If the KPI, access, or old path punishes the new behaviour, remove the barrier. Dual-run forever kills utilisation. Decommission the old path.
5. **Leading indicators:** speed of adoption, utilisation, proficiency (the operational KPI the case assumed). Comms sent and training completed are activities, not leading indicators.
6. **Resistance is information:** ADKAR gap vs structural barrier. Not a personality campaign.
7. **One ASK, this week.**
8. **Do not invent utilisation %.** Holes stay holes.

## Intake

If **two** of 1, 3, 4 are missing after one round: issues list, not a fake plan.

1. Observable behaviour and go-live / kill-old-path dates — load-bearing
2. Impacted roles and counts
3. Named receiving-manager owners (not PMO) — load-bearing
4. What the business case assumed for utilisation — load-bearing
5. What you already know about A/D/K/A/R (or "unknown")
6. Structural barriers already visible — access, dual run, conflicting KPIs

## Output shape

```
ADOPTION  |  [program / release]  |  [date]  |  Go-live: [ ]  Old path dies: [ ]
ASK: [receiving manager] to [action] by [date]. Cost of delay: [utilisation / benefit at risk].

BLUF
[Role] will [behaviour] by [date]. Barrier today: [ADKAR element] for [role].

BEHAVIOUR AND OWNERS
Behaviour (observable): [ ]
Impacted: [roles, n]
Sponsor (success definition): [ ]
Receiving managers (adoption): [ ]

ADKAR BARRIER BY ROLE
| Role | A | D | K | Ab | R | Barrier | This week's move |
| [ ] | 1-5 | | | | | | |

Do not train past a Desire hole. Preferred senders: [exec why / manager WIIFM].

STRUCTURAL
Urgency is: [true sentence]
Barriers to remove this week: [access / dual path / conflicting KPI]
Win in 2–4 weeks: [operational, visible]
Institute: [which old report/KPI/tool dies]

LEADING INDICATORS
| Indicator | Baseline | D10 | D30 | Target (case) | Owner |
| Speed (% on new path) |  |  |  |  |  |
| Utilisation (users / impacted) |  |  |  |  |  |
| Proficiency [named KPI] |  |  |  |  |  |
| Workaround rate |  |  |  |  |  |

RESISTANCE AS INFORMATION
| What they said / did | ADKAR or structural? | We will |
| [ ] | [ ] | [ ]

NOT THIS PAGE
Buy/don't → business-case    Vendor done → vendor-sow    Weekly pack → operating-review

Holes: [ ]
```

## QA (must pass)

1. Behaviour is observable, not a slogan.
2. Named receiving-manager owner (not PMO / comms only).
3. ASK with owner, verb, date.
4. ADKAR barrier by at least one role.
5. Indicators include speed / utilisation / proficiency (or "unknown") — not only comms/training counts.
6. Old path has a kill date, or dual-run risk is explicit.
7. Resistance is not a list of "resistors".
8. Not a 50-slide strategy essay.
9. One page.

If 1, 2, 3, or 8 fail: do not ship.

## Escalate / stop

- No behaviour / no receiving owner after one question → refuse.
- They want 50 slides → refuse; offer this page.
- Case assumed high utilisation and leadership will not decommission the old path → say the case is already broken.
- Desire hole that is a true disagreement with the strategy → sponsor; do not "overcome" with training.
- Safety / union / employment-consequence → HR/IR/counsel.

## Related

- [Vendor SOW](../../management/vendor-sow/SKILL.md) — the vendor ships; this skill adopts
- [Business Case](../../strategy/business-case/SKILL.md) — utilisation was an assumption; this defends it
- [Stakeholder Alignment](../../management/stakeholder-alignment/SKILL.md) — senior belief before the decision
- [Operating Review](../../management/operating-review/SKILL.md) — weekly home for the leading indicators
- [Program Charter](../../management/program-charter/SKILL.md) — success tests this release must hit
- [Cascade Script](../../comms/cascade-script/SKILL.md) — the words; this is the behaviour
- [Cash Runway](../../management/cash-runway/SKILL.md) — if non-adoption burns extra opex
