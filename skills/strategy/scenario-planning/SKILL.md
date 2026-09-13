---
name: scenario-planning
description: >-
  Use when a material bet faces genuine uncertainty: 3-4 plausible worlds,
  implications for THIS bet, early indicators. Shell-style, not a forecast, not
  a competitive-teardown, not a business-case base/upside/downside.
license: MIT
---

# Scenario Planning

**Worlds One-Pager — 3–4 Named Scenarios** — implications for THIS bet, robust vs contingent moves, early indicators with owners. Not a prediction. Default: venture / program bet.

Method origin: Shell public (scenarios are not forecasts) + Wack (predetermined vs critical uncertainties).

If they want a scenario-planning lecture: one paragraph then produce or stop.

## When to use

- A material bet hinges on uncertainties you cannot assign an honest probability to
- The room is arguing about *the* future; you need which bets survive which worlds
- Pre-board / pre-IC: "what worlds did you consider?"

## When not to use

- Forecast, budget, or base / upside / downside around a model — [Business Case](../../strategy/business-case/SKILL.md)
- Named-rival features now — [Competitive Teardown](../../strategy/competitive-teardown/SKILL.md)
- One imagined failure — [Pre-mortem](../../management/pre-mortem/SKILL.md)
- Tracked risks with mitigations — [RAID Register](../../management/raid-register/SKILL.md)
- Later Go/Kill of a live bet — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)
- Weekly exceptions — [Operating Review](../../management/operating-review/SKILL.md)

Wild-card entertainment with no implication for a bet → refuse.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. A named bet | 3–4 worlds + implications + indicators + ASK |
| **redline** | They pasted three costumes of the official future | Rebuild worlds; drop probabilities |
| **refuse** | Two load-bearing facts missing, or they want probability-weighted EV as the output | Issues list. Stop |

## Hard rules

1. **Bet first.** Sentence 1 names the bet. Industry tourism fails.
2. **Not a forecast.** Probability on each world is a disguised forecast — fail.
3. **Predetermined (already in the pipeline) listed and not used as axes.**
4. **3–4 named worlds with causal logic.** Not good/base/bad. Not 12. Do not steal Shell's energy worlds onto their product.
5. **Implications differ.** If every world implies stay-the-course, the uncertainty was decoration.
6. **Robust moves (all worlds) vs contingent (trigger → action).**
7. **Early indicators are observable facts, owned, cadenced.** "Sentiment shifts" is not an indicator.
8. **Do not invent TAM per scenario.**

## Intake

If **two** of 1–3 are missing after one round: issues list, not wallpaper.

1. The bet (verb + object + date) — load-bearing
2. Horizon — load-bearing
3. Who must use this (MD, board, IC) — load-bearing
4. What is already in the pipeline (predetermined)
5. What they are arguing about (candidate uncertainties)
6. Numbers they actually have

## Output shape

```
SCENARIOS  |  [BET]  |  as-of: [date]  |  owner: [name]
Horizon: [ ]     Not a forecast.
ASK: [owner] watches [indicator] on [cadence]; contingent move [X] if it fires by [date]
Bet (one sentence): [ ]

PREDETERMINED (true in every world): [ ]

WORLDS
| Name | Logic (5 lines max) | What we do to THIS bet |
| [ ] | [ ] | accelerate / hedge / kill / reshape — specify |
| [ ] | [ ] | [ ]
| [ ] | [ ] | [ ]

Robust moves (all worlds): [ ]
Contingent moves (if indicator → then action): [ ]

EARLY INDICATORS
| World | Indicator (observable) | Threshold | Now | Owner | Cadence | If it fires, we |
| [ ] | [ ] | [ ] | [ ] or HOLE | [ ] | [ ] | [ ]

DISCARDED UNCERTAINTIES (why they do not change the bet): [ ]

NOT THIS PAGE
Capital math → business-case    One imagined failure → pre-mortem    Tracked risks → raid-register
Holes: [ ]
```

## QA (must pass)

1. ASK + owner + date. Bet named in sentence 1.
2. Explicit "not a forecast". No probabilities on worlds.
3. Predetermined listed and not used as axes.
4. 3–4 named worlds with causal logic (not good/base/bad).
5. Implications differ; at least one world would change the bet.
6. Robust vs contingent split.
7. Indicators observable, owned, cadenced. Numbers or HOLE.
8. One page. Not a teardown in costume.

If 1, 4, 5, or 7 fail: do not ship.

## Escalate / stop

- They want probability-weighted EV as the scenario output → [Business Case](../../strategy/business-case/SKILL.md).
- No bet after one ask → refuse.
- Relabel Shell worlds onto this product → refuse.

## Related

- [Business Case](../../strategy/business-case/SKILL.md) — capital math; this pressure-tests the world the math assumes
- [Competitive Teardown](../../strategy/competitive-teardown/SKILL.md) — rivals now; may feed an uncertainty
- [Pre-mortem](../../management/pre-mortem/SKILL.md) — one imagined failure
- [RAID Register](../../management/raid-register/SKILL.md) — tracked risks, not worlds
- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — a world may kill the bet at a gate
