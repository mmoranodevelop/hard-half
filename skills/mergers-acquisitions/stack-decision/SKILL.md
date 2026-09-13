---
name: stack-decision
description: >-
  Use after a close to pick, per domain, keep-buyer / keep-target / dual-run /
  rewrite. Dual-run is the week-1 default. NOT for make-vs-buy, not the cutover
  night, not the go-live gate.
license: MIT
---

# Stack Decision

**Stack decision (per domain)** — buyer / target / dual-run with a kill date / rewrite. One label each. Default: venture close.

Method origin: Deloitte public Converge / Combine / Coexist / Continue + BCG software PMI (pragmatic IT; dramatic stack swaps steal from revenue).

If they want an integrate-vs-federate lecture: one paragraph then produce or stop.

**Clock.** Week 1 = dual-run for customer-facing. Access, identity, security. **No rewrite.** Quarter 1 = one label per domain; dual-run has a kill date and a test.

## When to use

- Two stacks now exist (CRM, billing, product, identity, data, ITSM)
- "We'll run both until we know" with no date
- Day 30–60: need a label before anyone books a cutover

## When not to use

- Source a **capability** (make / buy / partner) — [Make vs Buy](../../strategy/make-vs-buy/SKILL.md)
- Hour-by-hour night — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Go / no-go gate — [Go-Live Readiness](../../project/go-live-readiness/SKILL.md)
- 100-day outcomes + kill-old-path — [Integration 100](../../management/integration-100/SKILL.md)
- Hold / absorb / merge the **company** — [Operating Model Choice](../../ma/operating-model-choice/SKILL.md)
- What is a customer / who may edit the record — [Cutover Plan](../../project/cutover-plan/SKILL.md)
- Day-1 payroll / bank / access go-no-go — [Day-1 Continuity](../../ma/day1-continuity/SKILL.md)

This page is the **choice**. Integration 100 then owns the kill date. Cutover runs the hours.

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. Domains named | One label per domain + dual-run kill date + ASK |
| **redline** | They pasted "best of breed later" | Force a label + date; kill forever-dual |
| **refuse** | Week-1 rewrite; no kill date on dual-run; two facts missing | Issues list. Stop |

## Hard rules

1. **Four labels.** Keep buyer (absorb). Keep target (reverse — you bought the platform). Dual-run (coexist) **with a kill date and a test**. Rewrite (greenfield) — longest, dearest; only if that *is* the thesis.
2. **Week 1 dual-run is the default** for customer-facing. Do not rewrite, do not big-bang CRM, do not "best of breed later" with no date.
3. **Indefinite dual-run is a decision to burn cash.** No date = refuse the row.
4. **Christensen public:** if you bought a disruptive model, federation (dual-run / keep target) until the model is proven; absorb kills it.
5. **Customer-visible?** Y/N on every row. Visible changes need the named-account script.
6. **Do not confuse with the night or the gate.** Pointers only.
7. **Do not invent TCO or synergy $.** Hole stays hole.
8. Cyber found post-close: name it or hole it. Do not hide it.

## Intake

If **two** of 1, 2, 3 are missing after one round: issues list, not a fake architecture.

1. Deal + close date / Day n — load-bearing
2. Domains in scope — load-bearing
3. What runs today (buyer now / target now) — load-bearing
4. Customer-facing vs internal
5. Any already-sold rewrite / platform thesis
6. Dual-run cost known? (or hole)
7. Owner of ASK (CIO + CPO) and decide-by (default Day 30–60)

## Output shape

```
STACK DECISION  |  [deal]  |  domains: [CRM / billing / product / identity / data / ITSM]  |  as-of: [date]
ASK: [CIO + CPO] approve one label per domain + dual-run kill date by [Day 30–60].
Owner of ASK: [CIO + CPO]    Decide-by: [Day 30–60]
Clock: week-1 dual-run default | Q1 labels

WEEK-1 (if Day 0–7): dual-run all customer-facing. No rewrite. Access/identity/security only.

| Domain | Buyer now | Target now | Label (buyer/target/dual/rewrite) | Why (one line) | Dual-run kill date + test | Customer-visible? | Owner |
| [ ] | [ ] | [ ] | keep-buyer / keep-target / dual-run / rewrite | [ ] | [date + test, or n/a] | Y/N | [name] |

Cyber found post-close: [Y/N + what / hole]
Do not: "best of breed later" with no date. That is dual-run forever.

NOT THIS PAGE
Source a capability → make-vs-buy    The night → cutover-plan    The gate → go-live-readiness    Company archetype → operating-model-choice

Holes: [ ]
```

## QA (must pass)

1. Every domain has a label, not "TBD".
2. Every dual-run row has a kill date **and** a test.
3. No week-1 rewrite or CRM big-bang.
4. ASK + owner + date.
5. Not a make-vs-buy, a cutover runbook, or a go/no-go.
6. No invented synergy $.
7. One page.

If 1, 2, 3, or 4 fail: do not ship.

## Escalate / stop

- Rewrite the platform in week 1 → refuse.
- "Best of breed, decide later" → refuse; that is dual-run with no date.
- They want the hours → [Cutover Plan](../../project/cutover-plan/SKILL.md).
- They want the gate → [Go-Live Readiness](../../project/go-live-readiness/SKILL.md).
- Customer-record grain / editor / survivorship → [Cutover Plan](../../project/cutover-plan/SKILL.md).

## Related

- [Make vs Buy](../../strategy/make-vs-buy/SKILL.md) — source a capability; this is two stacks that already exist
- [Cutover Plan](../../project/cutover-plan/SKILL.md) — the night after this choice
- [Go-Live Readiness](../../project/go-live-readiness/SKILL.md) — the gate
- [Integration 100](../../management/integration-100/SKILL.md) — owns the kill date once labelled
- [Operating Model Choice](../../ma/operating-model-choice/SKILL.md) — company archetype
- [Day-1 Continuity](../../ma/day1-continuity/SKILL.md) — control, not the platform choice
