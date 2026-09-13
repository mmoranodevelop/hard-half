---
name: tsa-schedule
description: >-
  Use when the seller is the bridge after a carve-out or close: TSA catalog,
  monthly cost and markup, exit test plus date per service. Seller-as-bridge.
  Not a vendor SOW for a supplier you chose.
license: MIT
---

# TSA Schedule

**TSA one-pager + catalog annex** — services in force on Day 1, monthly cost / markup, exit test + date per service, exit owner, top leakage lines, one ASK (terminate / extend / step-up). Default: carve-out; same spine for full merge.

Method origin: PwC public TSA-as-bridge (catalog, markup) + Deloitte public IT-TSA constraints (governance tax, lock-in, dual opex).

If they want a TSA lecture: one paragraph then produce or stop.

## When to use

- Seller still runs payroll, identity, ERP, or helpdesk after close
- "TSA until ERP is done" has no date
- One blanket term covers payroll and identity
- Markup / dual-stack cost is invisible next to synergies

## When not to use

- A supplier you **chose** — [Vendor SOW](../../management/vendor-sow/SKILL.md)
- Kill-old-path after the landing zone exists — [Integration 100](../../management/integration-100/SKILL.md)
- Hour-by-hour of the replacement cutover — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Synergy run-rate vs leakage dollars — [Synergy Tracker](../../ma/synergy-tracker/SKILL.md)
- Close go/no-go (is the TSA *executable* Day 1) — [Day-1 Continuity](../../ma/day1-continuity/SKILL.md)

A TSA is a counterparty you just bought from, time-boxed. It is not an outsourcer.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Named services or "seller still runs X" | One-pager + catalog rows + ASK |
| **redline** | They pasted a TSA or "IT support" blob | Split services; force dates, markup, exit tests |
| **refuse** | Two load-bearing facts missing, or a vendor-SOW lecture | Issues list. Stop |

## Hard rules

1. **Catalog:** named services, in/out of scope, SLA, volume. No "IT support" blob.
2. **Term per service**, not one date for everything.
3. **Pricing:** cost-plus vs fixed vs pass-through. Markup and extension step-ups are leakage. Label unknown; do not invent.
4. **Exit per service:** owner, replacement path, **test**, no-later-than date. Dual-run may slip on defect thresholds; it does not delete the date.
5. **Governance:** weekly service review, true-up rules. Seller is not your outsourcer.
6. Stranded cost is the **seller's** leftover unless the SPA allocated it. Buyer leakage = markup + dual stack + delayed synergy.
7. **One ASK:** terminate / extend / accept step-up, named service, date.

## Intake

If **two** of 1, 3, 5 are missing after one round: issues list, not a fake catalog.

1. Named services the seller will still run (or "unknown blob") — load-bearing
2. Carve-out vs full merge
3. Monthly cost / markup per service, or "unknown" — load-bearing
4. Replacement path (system, owner) per service
5. Exit date per service, or they said "until ERP" — load-bearing
6. Exit owner (buyer name)
7. Step-up / extension terms already in the paper?

## Output shape

```
TSA SCHEDULE  |  [deal]  |  [as-of date]
Seller: [ ]     Buyer exit owner (overall): [ ]     Term model: [per service]
D: [name]

ASK: [D] to [terminate / extend / accept step-up] on [service] by [date] at [monthly $ / markup].
Owner of ASK: [ ]    Decide-by: [ ]

IN FORCE ON DAY 1
| Service | Monthly cost | Markup | Exit test | No-later-than | Exit owner | Replacement |
| [payroll / IdP / ERP / helpdesk / …] | [ ] | [ ] | [ ] | [date] | [name] | [ ] |

TOP 5 LEAKAGE LINES
| Line | $/month | Why it is leakage | Kill-by |
| [markup / dual stack / stranded / scope creep] | [ ] | [ ] | [ ] |

WEEKLY GOVERNANCE: [slot]     True-up: [rule]     Dual-run defect threshold: [ ]

NOT A VENDOR SOW. Seller is the bridge. Blanket term = fail.
NOT THIS PAGE
Chosen supplier → vendor-sow    Replacement hours → cutover-plan    Synergy $ → synergy-tracker

Holes: [ ]
```

## QA (must pass)

1. ASK (terminate / extend / step-up, service, date).
2. Named services, not "IT support" blob.
3. No one blanket term for unlike services (payroll + identity).
4. Exit has a test and a date (or date labelled hole).
5. Cost / markup present or labelled unknown.
6. Exit owner named.
7. Not a vendor-sow or a cutover runbook.
8. No invented amounts.

If 1, 2, 4, or 8 fail: do not ship.

## Escalate / stop

- Two of named services / cost-or-unknown / exit date missing after one ask → issues list.
- "TSA until ERP is done" with no date → refuse.
- They want you to write a supplier SOW → [Vendor SOW](../../management/vendor-sow/SKILL.md).
- They want hour-by-hour of the replacement → [Cutover Plan](../../project/cutover-plan/SKILL.md).

## Related

- [Vendor SOW](../../management/vendor-sow/SKILL.md) — chosen supplier; this is seller-as-bridge
- [Integration 100](../../management/integration-100/SKILL.md) — kill-old-path tests once landing exists
- [Synergy Tracker](../../ma/synergy-tracker/SKILL.md) — TSA markup and dual stack as leakage
- [Day-1 Continuity](../../ma/day1-continuity/SKILL.md) — TSA must be executable at close
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — hours of the replacement event
