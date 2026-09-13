---
name: contingency-reserve
description: >-
  Use when governing the contingency/risk reserve: amount, unlock owner,
  triggers, remaining balance, draws, one ASK. RAID lists risks; this governs
  the money buffer. NOT for raid-register, not business-case, not budget-
  baseline, not eac-pulse, not estimate-confidence.
license: MIT
---

# Contingency Reserve

**Contingency / risk reserve — one page** — amount, unlock owner, triggers, remaining balance, draws this period, one ASK. Default: project/program risk money inside the cost baseline; management reserve called out separately if present. RAID lists risks; **this** governs the buffer.

Method origin: PMI contingency vs management reserve — contingency = money (or time) in the baseline for **known** risks with responses; management reserve = outside baseline for unknown-unknowns, released by senior D. Operator focus: drawdown practice with triggers, not a reserve lecture.

If they want a reserves / EMV lecture: one paragraph then produce or stop.

## When to use

- "How much contingency is left, who can unlock it, and on what trigger?"
- A risk is firing and someone wants to draw without a trail
- SteerCo / sponsor asks remaining buffer vs VAC / path risk
- Size or re-size the buffer after a CR or risk refresh

## When not to use

- Living R/A/I/D list — [RAID Register](../../management/raid-register/SKILL.md)
- Invest / NPV case that *sets* contingency % — [Business Case](../../strategy/business-case/SKILL.md)
- Signed cost baseline buckets — [Budget Baseline](../../project/budget-baseline/SKILL.md)
- EAC / ETC / VAC pulse — [EAC Pulse](../../project/eac-pulse/SKILL.md)
- Pre-commit estimate band — [Estimate Confidence](../../project/estimate-confidence/SKILL.md)
- Company cash runway — [Cash Runway](../../management/cash-runway/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named reserve + owner | Reserve page + ASK |
| **redline** | They pasted "we have 10% contingency" with no triggers | Force amount, owner, triggers, draws; kill vibes |
| **refuse** | No amount and no unlock owner, or invent draws | Issues list. Stop |

## Hard rules

1. **Name the pot:** contingency (in baseline) vs management reserve (outside). Do not conflate.
2. **Opening / drawn / remaining** on the page. Missing → HOLE.
3. **Unlock owner (D)** and **triggers** (risk id / event / threshold). No trigger = theatre.
4. **Draws this period:** amount, risk/issue id, approver, date. Trail or hole.
5. **Linked risks** ≤5 material — from RAID; this page does not replace RAID.
6. **One ASK** — draw / top-up / release unused / hold / escalate to Mgmt Reserve. Owner, date.
7. **Never invent** reserve $, EMV, or draw history. Holes stay holes.
8. **One page.** Money buffer board, not a risk novel.

## Intake

If **two** of 1–4 are missing after one round: issues list, not a fake pot.

1. Named project + contingency amount (opening or current) — load-bearing
2. Unlock owner (D) — load-bearing
3. Triggers / policy for draw — load-bearing
4. Drawn to date + remaining — load-bearing
5. Management reserve (if any) + its D
6. Material risks the pot covers (RAID ids)
7. As-of date / currency

## Output shape

```
CONTINGENCY RESERVE  |  [PROJECT]  |  as-of: [date]  |  Currency: [ ]
ASK: [D] to [draw / top-up / release / hold / escalate-MR] by [date]

POTS
| Pot | Opening | Drawn | Remaining | Inside baseline? | Unlock D |
| Contingency |  |  |  | YES |  |
| Mgmt Reserve |  |  |  | NO |  |

TRIGGERS (when D may unlock)
| Trigger | Linked risk/issue | Threshold | Evidence |
|  |  |  |  |

DRAWS THIS PERIOD
| Date | Amount | Risk/Issue | Approver | Remaining after |
|  |  |  |  |  |

COVERED RISKS (≤5 material)
| RAID id | Risk | Residual $ / HOLE | Covered y/n |
|  |  |  |  |

NOT THIS PAGE
RAID list → raid-register    Baseline buckets → budget-baseline
EAC/VAC → eac-pulse    Invest case → business-case
Pre-commit band → estimate-confidence

Holes: [ ]
```

Annex: `assets/reserve-drawdown.md`.

## QA (must pass)

1. Contingency opening/drawn/remaining — or HOLE each.
2. Unlock D named.
3. ≥1 trigger or explicit "no policy — theatre".
4. Draws trail this period or "none".
5. Contingency vs Mgmt Reserve distinguished.
6. One ASK with owner, verb, date.
7. No invented $. Not a RAID dump. One page.

If 1, 2, 6, or 7 fail: do not ship.

## Escalate / stop

- Amount and D both missing after one ask → refuse.
- Draw without trigger / approver → refuse the silent draw; escalate.
- Remaining << residual risk $ → show the hole; [EAC Pulse](../../project/eac-pulse/SKILL.md) / [Change Control](../../project/change-control/SKILL.md) may follow.
- They want the full RAID on this page → [RAID Register](../../management/raid-register/SKILL.md).

## Related

- [RAID Register](../../management/raid-register/SKILL.md) — risks; this is the money
- [Budget Baseline](../../project/budget-baseline/SKILL.md) — PMB including contingency line
- [EAC Pulse](../../project/eac-pulse/SKILL.md) — VAC vs remaining reserve
- [Business Case](../../strategy/business-case/SKILL.md) — where contingency % was born
- [Estimate Confidence](../../project/estimate-confidence/SKILL.md) — pre-commit uncertainty
- [Change Control](../../project/change-control/SKILL.md) — when top-up needs a CR
- [Schedule Crash](../../project/schedule-crash/SKILL.md) — crash spend may draw the pot
