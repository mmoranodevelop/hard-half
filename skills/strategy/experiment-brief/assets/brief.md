# EXPERIMENT BRIEF  |  [name]  |  [date]

Owner: [ ]  
Analyst: [ ]  
Decision-maker on kill/scale: [ ]  
Type: randomized A/B | pilot / quasi (claim lowered)

## Hypothesis

If we [change] for [who], [OEC] will [↑/↓] by [MDE] because [mechanism].

## Metrics

OEC (one): [ ]  
Baseline: [known / hole]  
MDE: [ ]  
SECONDARY (no vote): [ ]  
GUARDRAILS (veto): [metric, red line]

## Design

Unit: [ ]  
Split: [ ]  
Min duration: [whole weeks]  
n target: [computed / hole]  
Power / confidence: 80% / 95% unless stated  
First analysis: [date] when n AND duration met.  
Peek to ship: no.

## Kill (pre-registered)

- OEC down or < MDE at analysis date → kill, revert by [owner]
- Guardrail red → stop now, even if OEC is up
- Underpowered at [latest date] → kill or re-power, do not "extend until green"

## Scale

- OEC ≥ MDE, guardrails hold → [rollout plan, owner, date]

## Not this test

- [HiPPO, the OKR, the PR]

## Holes

- [baseline, n, instrumentation]
