---
name: make-vs-buy
description: >-
  Use when choosing how to source a capability: make, buy, partner, kill, or do-
  nothing. Transaction-cost and procurement logic. Not a vendor SOW, not a
  business case, not a build-vs-buy blog post.
license: MIT
---

# Make vs Buy

**Sourcing 1-pager:** five options (make / buy / partner / kill / do-nothing), strategic × market tests, TCO bands, hold-up/exit, one recommendation with conditions, review date, kill criteria. Default: venture / program capability.

Method origin: Coase/Williamson public (transaction costs) + public procurement (strategic importance × market capability).

If they want to be taught TCE: one paragraph then produce or stop. Do not invent firm internals.

## When to use

- "Should we build this, buy it, or partner?"
- A capability is failing in-house *or* a vendor is failing
- Vertical integration vs contract manufacturing vs JV
- Software: build / buy / subscribe / open-source-and-maintain
- The room is arguing unit cost without TCO or lock-in

## When not to use

- Writing the SOW / MSA — [Vendor SOW](../../management/vendor-sow/SKILL.md) after the choice
- The capital ask (NPV, payback) — [Business Case](../../strategy/business-case/SKILL.md); this 1-pager is an input
- Deep uncertainty about the world the capability lives in — [Scenario Planning](../../strategy/scenario-planning/SKILL.md)
- Physics of one more unit — [Unit Economics](../../strategy/unit-economics/SKILL.md)
- Dated tests for a bet already chosen — [Kill Criteria](../../strategy/kill-criteria/SKILL.md)
- A vendor bake-off with the make option already dead — not this skill
- Illegal, sanctioned, or outside licence to operate — refuse

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default | Filled sourcing 1-pager |
| **redline** | They pasted "buy" from a vendor deck / cost-only paper | Fail QA; force five options; TCO bands; exit |
| **refuse** | Rubber-stamp a friend's vendor, or they want the MSA drafted here | Issues list. Stop |

## Hard rules

1. **Five options, always.** Make, buy, partner, kill, do-nothing. Missing do-nothing = sales process.
2. **Score:** strategic importance × market capability × internal capability.
3. **TCE flags:** asset specificity, contract uncertainty, frequency. High specificity + uncertainty → make or a very tight partner, not a spot buy.
4. **TCO is a band with unknowns** (integration, attention, switching, quality, IP). Not a vendor quote to two decimals.
5. **Do not outsource the differentiator on a cost slide.** Name what you refuse to give up.
6. **Hold-up and exit:** switching cost, who owns IP/data, kill switch. No exit = you married.
7. **"Buy because we need it fast"** is allowed only if you also say what happens after month one of live.
8. **One recommendation + conditions + review date + kill criteria.** Not "it depends" as the ending.
9. **Do not invent vendor savings.**

## Intake

If **two** of 1–3 are blank after one pass: issues list, not a fake "buy".

1. Capability (the job it does, not a product name) — load-bearing
2. Who decides, by when — load-bearing
3. Current cost and pain (known / unknown) — load-bearing
4. Named vendors or partner candidates (or "none yet")
5. What would be lost if a vendor walked
6. Time constraint (real deadline vs preference)
7. Why now

Refuse to recommend "buy" from a single vendor's deck. Refuse to recommend "make" because engineering prefers it.

## Output shape

```
MAKE VS BUY  |  [capability]  |  [date]
ASK: [choose option] by [date]; review on [date]; kill if [criteria]
Capability (one sentence job): [ ]
Current state (who, pain, known cost): [ ]
Decider / date: [ ]

TESTS
| Test | Call | Evidence |
| Strategic importance | differentiator / table-stakes / waste | [ ] |
| Market capability | strong / thin / none | [ ] |
| Internal capability | can / not yet / never | [ ] |
| Asset specificity | high / low | [ ] |
| Contract uncertainty | high / low | [ ] |

OPTIONS (all five)
| Option | Meaning here | TCO band (known / unknown) | Hold-up / exit | Verdict |
| Make | [ ] | [ ] or [HOLE] | [ ] | [ ] |
| Buy | [ ] | [ ] | [ ] | [ ] |
| Partner | [ ] | [ ] | [ ] | [ ] |
| Kill | [ ] | [ ] | [ ] | [ ] |
| Do-nothing | [ ] | [ ] | [ ] | [ ] |

RECOMMENDATION
Option: [one]
Conditions (control rights, data/IP, SLA): [ ]
Review date: [ ]
Kill criteria: [metric / fact] by [date], called by [role]

Not this paper: SOW → vendor-sow; NPV → business-case
```

TCE detail: `assets/tce-scorecard.md`.

## QA (must pass)

1. ASK + decider + date. Five options present, including do-nothing and kill.
2. Capability named as a job, not a product name.
3. Strategic × market × internal tests called, with evidence or [HOLE].
4. At least one TCE flag in the table.
5. TCO is a band with unknowns, not a fake exact quote.
6. Exit / hold-up addressed for buy or partner.
7. One recommendation with conditions, review date, kill criteria.
8. One page. No invented vendor savings.

If 1, 3, or 7 fail: do not ship.

## Escalate / stop

- They already chose buy and want a contract → [Vendor SOW](../../management/vendor-sow/SKILL.md).
- They want "is this a good investment" → [Business Case](../../strategy/business-case/SKILL.md); bring sourcing options as the cases.
- Single-vendor deck as the only evidence → refuse the rubber-stamp.
- Sanctioned / illegal / licence-to-operate miss → refuse.

## Related

- [Vendor SOW](../../management/vendor-sow/SKILL.md) — the contract after buy
- [Business Case](../../strategy/business-case/SKILL.md) — capital; this is sourcing
- [Unit Economics](../../strategy/unit-economics/SKILL.md) — P&L physics of the operation
- [Scenario Planning](../../strategy/scenario-planning/SKILL.md) — sourcing under deep uncertainty
- [Kill Criteria](../../strategy/kill-criteria/SKILL.md) — dated stop after the choice
