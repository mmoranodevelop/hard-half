---
name: experiment-brief
description: >-
  Use when briefing one experiment: hypothesis, primary metric, sample, kill and
  scale rules, owner, and dates. NOT for a PR/FAQ and NOT for an OKR cascade.
license: MIT
---

# Experiment Brief

**One experiment brief** — hypothesis, OEC, sample / MDE, guardrails, kill and scale rules, owner, dates. Default: venture product/growth test; same spine for an F500 program pilot.

Public method. Kohavi et al. 2009 (public PDF): controlled experiment, **OEC** (overall evaluation criterion), 95% confidence / ~80–90% power, sample-size before you start. HiPPO is not a design. Guardrails so you do not "win" the OEC while breaking cash or safety. Pre-register; do not peek. Reconstruct. Do not dump the 2020 book.

If they want "teach me A/B testing", one paragraph then produce or stop.

## When to use

- One test is about to run (or should): product, price, funnel, ops pilot
- "Let's just ship it" / "the CEO likes variant B"
- You need kill / scale rules **before** the first look at results
- A pilot in a plant, geo, or segment (same spine; say if not randomized)

## When not to use

- Working-backwards product narrative — [PR FAQ](../../strategy/pr-faq/SKILL.md)
- Goal cascade for the year — [OKR Cascade](../../strategy/okr-cascade/SKILL.md)
- Price **architecture** — [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md)
- A one-off discount — [Discount Exception](../../strategy/discount-exception/SKILL.md)
- After-action on a test already bungled — [After-Action Review](../../management/after-action-review/SKILL.md)

## Modes

| Mode | When | Output |
|---|---|---|
| **produce** | Default. One idea to test | Filled brief |
| **redline** | They pasted a "test plan" or a dashboard | Kill multi-metric soup, peeking, no-kill |
| **refuse** | No hypothesis, no metric, and they want a "learnings" essay | Issues list. Stop |

## Hard rules

1. **One primary metric (OEC).** Kohavi: a single criterion forces the tradeoff **before** you see the data. Secondary metrics do not get a vote on ship. Guardrails can **veto**.
2. **Hypothesis is causal and falsifiable.** "If we [change] for [who], [OEC] will [direction] by [MDE] because [mechanism]." "Make it better" is not a hypothesis.
3. **Sample and MDE before start.** n (or duration), baseline, MDE, power ~80%, confidence 95% unless they choose otherwise **in writing**. If you cannot compute n, the brief still ships only with a **labelled hole** and a kill-on-underpower rule — not with a fake n.
4. **Randomization unit named** (user, account, store, day). If this is not a randomized test, say **pilot / quasi** and lower the claim. Do not dress a rollout as an A/B.
5. **No peeking to ship.** Analysis date is when n **and** minimum duration (whole weeks) are met. Early look is for **harm** (guardrail), not for "it's winning, ship".
6. **Kill and scale are written in advance.** Kill: OEC down / guardrail red / underpowered at the date. Scale: OEC up by ≥ MDE, guardrails hold, owner of the rollout. "We'll see how we feel" is a fail.
7. **Guardrails include the thing you could break** (revenue, latency, safety, complaints, SRM). Empty guardrails are a fail on anything that can hurt people or cash.
8. **Do not invent baselines, conversion rates, or n.** Holes stay holes.

## Intake

If **the change** and **the primary metric** are both missing after one round: issues list.

1. The change, the audience, why now
2. Primary metric (OEC) and the MDE that would make you care
3. Baseline you actually have (or "unknown")
4. Unit of randomization (or "this is a pilot, not randomized")
5. What must not get worse (guardrails)
6. Kill / scale owners and the latest end date
7. Venture or F500 (venture default)

## Output shape

```
EXPERIMENT BRIEF  |  [name]  |  [date]
Owner: [ ]    Analyst: [ ]    Decision-maker on kill/scale: [ ]
Type: randomized A/B | pilot / quasi (claim lowered)

HYPOTHESIS
If we [change] for [who], [OEC] will [↑/↓] by [MDE] because [mechanism].

OEC (one): [ ]    Baseline: [known / hole]    MDE: [ ]
SECONDARY (no vote): [ ]
GUARDRAILS (veto): [metric, red line]

DESIGN
Unit: [ ]    Split: [ ]    Min duration: [whole weeks]
n target: [computed / hole]    Power / confidence: 80% / 95% unless stated
First analysis: [date] when n AND duration met. Peek to ship: no.

KILL (pre-registered)
- OEC down or < MDE at analysis date → kill, revert by [owner]
- Guardrail red → stop now, even if OEC is up
- Underpowered at [latest date] → kill or re-power, do not "extend until green"

SCALE
- OEC ≥ MDE, guardrails hold → [rollout plan, owner, date]

NOT THIS TEST
- [HiPPO, the OKR, the PR]

HOLES
- [baseline, n, instrumentation]
```

## QA (must pass)

1. Hypothesis is one causal sentence with a mechanism.
2. Exactly one OEC.
3. MDE stated.
4. n or a labelled hole plus underpower-kill.
5. Guardrails non-empty if cash or people can be hurt.
6. Kill and scale written before start.
7. Analysis date is not "when it looks good".
8. Not a PR/FAQ. Not an OKR set.
9. No invented baseline or n.
10. One page.

If 1, 2, or 6 fail: do not ship.

## Escalate / stop

- They want five primary metrics → refuse; pick one OEC, rest are secondary/guardrail.
- They want to ship because an early p-value is cute → refuse peek-to-ship.
- Safety / clinical / credit-risk experiment — specialist + compliance; this page can still hold the spine with holes.
- They wanted a press narrative — PR/FAQ.
- They wanted quarterly goals — OKR cascade.

## Related

- [PR FAQ](../../strategy/pr-faq/SKILL.md) — working backwards; not a test
- [OKR Cascade](../../strategy/okr-cascade/SKILL.md) — goals; a test may serve an KR
- [Pricing One-Pager](../../strategy/pricing-one-pager/SKILL.md) — architecture; a price test can use this brief
- [Decision Journal](../../learning/decision-journal/SKILL.md) — log the kill/scale
- [After-Action Review](../../management/after-action-review/SKILL.md) — after the test, if the process failed
