---
name: competitive-teardown
description: >-
  Use when tearing down a named rival to decide our move: where they play, how
  they win, activity-system fit, durable power if citable — then a so-what we
  will do or refuse. Not a SWOT, not issue-tree, not business-case until the
  move is named.
license: MIT
---

# Competitive Teardown

**Competitive Teardown — Named Rival, Our Move** — one page: where they play, how they win, what they refuse, activity-system fit, durable power if citable, gap vs us, so-what we will do or refuse. Default: venture / program vs one named rival; same spine for F500.

Method origin: Porter public (position, trade-offs, activity fit) + Playing-to-Win where/how + Helmer Power = benefit + barrier. Not a book dump. No invented McKinsey cost curves.

If they want a five-forces lecture: one paragraph then produce or stop.

## When to use

- "Tear down [named company / product line] — what should we do?"
- Before enter / price-war / copy / partner / avoid
- To kill "we should be more like them" with evidence
- To show why an advantage is (or is not) imitable

## When not to use

- Our P&L miss — [Issue Tree](../../strategy/issue-tree/SKILL.md)
- Capital to spend after the move is named — [Business Case](../../strategy/business-case/SKILL.md)
- Customer-back invention — [PR/FAQ](../../strategy/pr-faq/SKILL.md)
- Board paper — [Executive Board Memo](../../management/executive-board-memo/SKILL.md)
- Jobs of our customer — [Jobs to Be Done](../../strategy/jobs-to-be-done/SKILL.md)
- Scenario worlds — [Scenario Planning](../../strategy/scenario-planning/SKILL.md)
- If the move is price — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)
- The rival (or fraudster, regulator, attacker) *updates when we move* and we need a half-life — that is `red-queen`, not a static teardown

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. One named rival | 1-pager: system + power + our move + ASK |
| **redline** | They pasted a SWOT / "landscape" | Extract one rival; write the move; throw the collage |
| **refuse** | Two load-bearing facts missing, or clone without trade-offs | Issues list. Stop |

## Hard rules

1. **Named rival, named line of business.** "Tech" is not an industry. "US analog insulin" is.
2. **Reconstruct their where-to-play and how-to-win from evidence.** Name what they refuse.
3. **Activity system: 4–8 activities that fit.** A feature list is a fail. Copying two activities and ignoring the rest is how clones die.
4. **Power = benefit (cash) + barrier** (why a competent rival cannot arbitrage in 24 months). Name a Helmer power only if evidenced. "They grew 40%" is not power.
5. **Public evidence or `[HOLE]`.** Cite URL / filing. Do not invent share, margin, or culture.
6. **Closing line is our move:** a disagreeable complete sentence + first action + owner + date. "They are formidable" has failed.
7. **One page.** Trade-offs they cannot unwind cheaply are the attack surface (or the reason to stay out).
8. **If they want "the market":** pick the one rival that constrains the decision, or refuse.

## Intake

If **two** of 1–3 are missing after one round: issues list, not a fake landscape.

1. Rival (legal name + line of business) and us (same altitude) — load-bearing
2. Decision this serves (enter, price, copy, avoid, partner, kill a workstream) and by when — load-bearing
3. Where we currently play (or the candidate) — load-bearing
4. Public sources they already trust (10-K year, letter, product URL)
5. Constraints on our move (capital, licence, brand, time)
6. What would make this a waste (decision already taken)
7. As-of date / owner of the ASK

## Output shape

```
COMPETITIVE TEARDOWN  |  [Rival], [line of business]  |  as-of: [date]
ASK / our move: [complete-sentence recommendation]
Decision this serves / owner / date: [ ]
Arena: [line of business, geo, customer]

HOW THEY WIN (not a SWOT)
- Where they play: [ ]
- How they win: [ ]
- What they refuse (trade-offs): [ ]

ACTIVITY SYSTEM (fit)
- [Activity 1] → reinforces [activity 2]
Public evidence: [10-K / letter / URL] or HOLE

POWER (persistent returns — or not)
| Claimed advantage | Benefit (cash) | Barrier (why it lasts) | Power name if evidenced | Confidence |
| [ ] | [ ] | [ ] | scale / network / switching / brand / other / none | high/med/low |

GAP VS US
| | Them | Us | So what |
| Position | [ ] | [ ] | [ ]
| System | [ ] | [ ] | [ ]
| Economics (public) | [ ] | [ ] | [ ]

OUR MOVE
- Do: [ ]
- Do not: [ ] (including: do not clone activities without the system)
- First action / owner / date: [ ]

NOT THIS PAGE
Our miss → issue-tree    Cheque → business-case    Customer-back → pr-faq    SWOT collage → refuse

Holes: [ ]
```

## QA (must pass)

1. ASK / our move + owner + date. Rival and line of business named.
2. Not a SWOT. Not a five-forces homework.
3. Trade-offs named. Activity system shows fit (4–8), not a feature list.
4. Power claims have benefit + barrier, or "not power".
5. Load-bearing facts have a public URL or filing; holes stay holes.
6. Closing line is a disagreeable complete sentence.
7. One page. No book prose. No fake industry cost curve.
8. No invented share, margin, or internals.

If 1, 3, 5, or 8 fail: do not ship.

## Escalate / stop

- No named rival after one ask → refuse.
- Five forces of an industry with no named rival and no our-move → homework; stop.
- They want a clone without the trade-offs → refuse; kill-copy line: what they would have to copy and the cost.
- Gossip file or non-public data you have no rights to → refuse.
- SWOT / PESTLE / four-box collage as the job → refuse.

## Related

- [Issue Tree](../../strategy/issue-tree/SKILL.md) — our problem; this is their system
- [Business Case](../../strategy/business-case/SKILL.md) — money on the move
- [PR/FAQ](../../strategy/pr-faq/SKILL.md) — customer-back, not competitor-back
- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) — if the move is price
- [Jobs to Be Done](../../strategy/jobs-to-be-done/SKILL.md) — our customer's jobs
- [Scenario Planning](../../strategy/scenario-planning/SKILL.md) — worlds, not one rival
- [Make vs Buy](../../strategy/make-vs-buy/SKILL.md) — if the move is build or buy
