---
name: product-sunset
description: >-
  Use to kill or sunset a product or SKU: customers, revenue, migration, date,
  message. NOT for deprecation-notice (tech API), not portfolio-keep-kill (M&A
  asset), not kill-criteria (invest thesis kill).
license: MIT
---

# Product Sunset

**Sunset decision + comms pack** — what ends, who is affected ($ and logos), migration path, end-of-sale / end-of-support / hard-off dates, message spine, one ASK. Default: venture product/SKU; same spine for F500 line retirement.

Method origin: Pragmatic Institute public EOL / sunsetting — assess, announce, end-of-sale, end-of-maintenance, end-of-support, deliberate comms with marketing. Public sunset communication patterns (Atlassian server EOS / Google deprecation-style timelines) — dated phases, migration path, same-day multi-channel announce.

If they want a product-lifecycle lecture: one paragraph then produce or stop.

## When to use

- Leadership will stop selling or supporting a named product / SKU / plan
- Need customers, revenue at risk, and migration before the announce date
- End-of-sale vs end-of-support vs hard-off must be three dates, not "soon"
- Message must ship with a path (migrate / replace / refund rule)
- Finance / CS / Legal need one page before the public note

## When not to use

- Tech API / feature deprecation notice only — [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md)
- M&A hold/divest/shut asset choice — [Portfolio Keep Kill](../../ma/portfolio-keep-kill/SKILL.md)
- Dated kill tests on an investment thesis — [Kill Criteria](../../strategy/kill-criteria/SKILL.md)
- Packaging collision between SKUs still alive — [Packaging Collision](../../ma/packaging-collision/SKILL.md)
- Incident / sev comms — [Severity Customer](../../delivery/severity-customer/SKILL.md)
- Portfolio stage-gate meeting for many bets — [Portfolio Stage Gate](../../management/portfolio-stage-gate/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Product named; impact listable or HOLE | Impact + dates + migration + message + ASK |
| **redline** | They pasted "we're sunsetting X soon" | Force dates, $ / logos, migration; kill vagueness |
| **refuse** | No product name, no dates, and they want a soft leak | Issues list. Stop |

## Hard rules

1. **Name what dies.** Product / SKU / plan / edition — exact commercial object. Feature-only API kill is [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md).
2. **Three clocks.** End-of-sale (stop selling), end-of-support / maintenance, hard-off / data deletion. Missing clock = HOLE.
3. **Impact is logos + $.** Paying customers affected, ARR/MRR (or revenue) at risk, segments. Do not invent counts.
4. **Migration path required.** Move to [product], export, refund/credit rule, or "no successor — wind-down terms." Empty path = refuse to announce.
5. **Message spine before channels.** What ends, why (customer-safe), dates, what to do, who helps. Pragmatic: marketing owns wording with product.
6. **Same-day multi-channel on announce.** Email, in-app, docs, status/changelog as applicable — no customer learns from a competitor first.
7. **Contract / notice obligations.** MSA notice periods, enterprise side letters — list or HOLE; counsel if material.
8. **One ASK.** Approve sunset package (dates + migration + message) — not "explore sunsetting."

## Intake

If **product/SKU** and **target hard-off or announce intent** are both missing after one round: issues list.

1. Exact product / SKU / plan ending
2. Successor or wind-down path
3. Customers affected (n, $) or HOLE
4. Candidate dates (EOS / EOSupport / hard-off) or "need design"
5. Contractual notice constraints or unknown
6. Top accounts needing white-glove
7. Approver (CEO / CPO / GM) + decide-by

## Output shape

```
PRODUCT SUNSET  |  [product/SKU]  |  as-of: [date]
ASK: approve sunset package (dates + migration + message) — Owner: [ ] — Decide-by: [ ]

WHAT ENDS: [exact object]    SUCCESSOR / PATH: [migrate to X / export / refund / none]

IMPACT
Paying logos: [n or HOLE]    Revenue at risk: [$ or HOLE]    Segments: [ ]
Top-touch accounts: [names or n] — owner [ ]

DATES
| Milestone | Date | Notes |
| Announce (same-day multi-channel) | [ ] | |
| End of sale | [ ] | |
| End of support / maintenance | [ ] | |
| Hard-off / data deadline | [ ] | export by [ ] |

MIGRATION
Steps: [ ]    Tooling/docs: [or HOLE]    Credits/refunds: [policy or HOLE]
Contract notice: [days / HOLE] — counsel: [Y/N]

MESSAGE SPINE
1. What is ending (exact)
2. Why (customer-safe, not internal drama)
3. Dates (three clocks)
4. What to do (migration / export)
5. Help: [named contact / office hours]
6. What happens to data

NOT THIS PAGE
API/feature only → deprecation-notice | M&A asset → portfolio-keep-kill | Thesis kill tests → kill-criteria
HOLES: [ ]
```

## QA (must pass)

1. Exact product/SKU named.
2. Three dates present or labelled HOLE — no "soon."
3. Impact logos/$ present or HOLE — not invented.
4. Migration / wind-down path non-empty.
5. Message spine has what / why / dates / do-next / help.
6. One ASK + owner + date.
7. Not deprecation-notice, portfolio-keep-kill, or kill-criteria.
8. One page.

If 1, 4, 6, or 7 fail: do not ship.

## Escalate / stop

- Announce without migration path → refuse.
- Enterprise contracts with notice the dates violate → counsel before ASK.
- Regulated data deletion / residency → legal + security.
- They actually need API deprecation only — [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md).
- They actually need M&A keep/kill — [Portfolio Keep Kill](../../ma/portfolio-keep-kill/SKILL.md).

## Related

- [Deprecation Notice](../../delivery/deprecation-notice/SKILL.md) — tech API/feature retirement
- [Portfolio Keep Kill](../../ma/portfolio-keep-kill/SKILL.md) — M&A asset choice
- [Kill Criteria](../../strategy/kill-criteria/SKILL.md) — invest thesis kill tests
- [Packaging Collision](../../ma/packaging-collision/SKILL.md) — live SKU collision
- [Customer CEO Letter](../../comms/customer-ceo-letter/SKILL.md) — executive letter for top logos
- [Launch Brief](../../delivery/launch-brief/SKILL.md) — if successor needs a launch pack
