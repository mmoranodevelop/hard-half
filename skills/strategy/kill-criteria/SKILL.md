---
name: kill-criteria
description: >-
  Use when one named venture or bet needs dated kill tests and the next tranche:
  what must be true, the test, the date, who calls kill. Sequential investment.
  NOT for the portfolio gate meeting, not the NPV business case.
license: MIT
---

# Kill Criteria

**Dated kill-test card** for **one** venture: assumptions, cheap tests, next cheque, who calls stop. Default: a venture or an F500 internal bet that still has more money to spend.

Method origin: McGrath & MacMillan discovery-driven planning (HBR 1995) — reverse the P&L, list assumptions, checkpoints; fund in tranches. Amazon 1997: jettison bets that do not earn acceptable returns.

If they want a lecture on real options: one paragraph then produce or stop.

## When to use

- "What would make us stop [named bet]?" before or just after the first cheque
- A live bet with no written kill rule (zombie)
- Sequential investment: this tranche only, next tranche earned
- Convert a hopeful roadmap into tests with dates

## When not to use

- The gate meeting across several bets — [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md)
- The money model (NPV, options table) — [Business Case](../../strategy/business-case/SKILL.md); this card can attach as the kill exhibit
- Enter this geo yes/no — [Market Entry](../../strategy/market-entry/SKILL.md) (that page *uses* a kill test)
- Weekly status of in-flight work — [Operating Review](../../management/operating-review/SKILL.md)
- A pre-mortem of how it might die — [Pre-mortem](../../management/pre-mortem/SKILL.md) (input, not this card)
- Too many live threads — [WIP Limit](../../productivity/wip-limit/SKILL.md)

If they cannot name **one** bet, stop.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | Kill-test card + next-tranche ASK |
| **redline** | They pasted OKRs or a "success plan" | Same facts; turn hopes into dated kill tests |
| **refuse** | No bet, or two load-bearing facts missing | Issues list. Stop |

## Hard rules

1. **One named bet.** Not a portfolio, not "innovation".
2. **Kill is a test, not a vibe.** Metric + threshold + date + caller.
3. **Write the kill before the next cheque.** Moving the goal after a miss is a fail.
4. **Assumptions, not activities.** "Ship v1" is an activity. "Paying customers at ≥X contribution by DATE" is a test.
5. **Few load-bearing assumptions.** A pile is two that should merge or a new bet.
6. **Next cheque is earned.** Amount, what it buys, what evidence releases it. Sunk cost is not a reason to pay it.
7. **Cheap test first.** If the first test requires a plant, a long lease, or a full team, you already spent the option premium.
8. **Caller is a name, not "the committee".** Usually the MD who owns the purse.
9. **Do-nothing is on the page.** What happens if we simply stop now (salvage, people, contracts).
10. **One page.** Reverse-P&L math can sit in a five-line box. Do not invent pilots.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake card.

1. The bet, one sentence, and the owner — load-bearing
2. Money already spent and next cheque (amount, date) — load-bearing
3. What "winning" looks like in a named horizon — load-bearing
4. The things that must be true (they may be guesses — label them) — load-bearing
5. What you will actually observe by when
6. Who is allowed to kill it

## Output shape

```
KILL CRITERIA  |  [BET]  |  [as-of date]
ASK: [caller] to [release / withhold / kill] the next [amount] on [date]
Owner of the bet: [ ]
Spent to date (sunk, ignore for the decision): [ ]
Next cheque: [amount] buys [what] if tests pass

WHAT MUST BE TRUE
| # | Assumption | Test / evidence | Threshold | Date | If false |
| 1 | [ ] | [ ] | [ ] | [ ] | Kill / recycle / smaller |

REVERSE OUTCOME (few lines)
- Target at [date]: [ ]
- Implied volume / price / cost / conversion: [ ]
- What we know vs guess: [ ]

KILL RULE (one sentence)
Stop the next cheque if [metric] [threshold] by [date], called by [name].
Do not move the threshold after a miss.

IF WE KILL NOW
- Salvage / contracts / people: [ ]
- Lesson to keep: [ ]

NEXT SITTING
[date] — evidence in hand — decision: release / withhold / kill
```

## QA (must pass)

1. One named bet.
2. Each kill test: metric, threshold, date, caller.
3. Assumptions are tests, not activities.
4. Next cheque named; released only if tests pass.
5. Sunk cost explicitly excluded from the go-forward call.
6. Cheap test before irreversible spend, or the irreversibility is named.
7. Do-nothing / kill-now path on the page.
8. One ASK.
9. Not a portfolio board, not an NPV novel.
10. No invented pilots.

If 1, 2, 4, or 5 fail: do not ship.

## Escalate / stop

- They want to "keep optionality" with no test → refuse; that is a zombie with a nicer name.
- They want the gate sitting designed for *all* bets → [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md).
- They want NPV / do-nothing options table → [Business Case](../../strategy/business-case/SKILL.md); attach this card.
- Safety / legal / licence-to-operate miss → kill or hold now; do not wait for the date.

## Related

- [Portfolio Stage-Gate](../../management/portfolio-stage-gate/SKILL.md) — the sitting; this is the card for one bet
- [Business Case](../../strategy/business-case/SKILL.md) — capital math; this is the stop rule
- [Market Entry](../../strategy/market-entry/SKILL.md) — geo/segment yes/no that *includes* a kill test
- [Pre-mortem](../../management/pre-mortem/SKILL.md) — imagined failure; this is the dated test
- [RAID Register](../../management/raid-register/SKILL.md) — live risks; a missed kill test becomes an issue
- [WIP Limit](../../productivity/wip-limit/SKILL.md) — too many live threads
