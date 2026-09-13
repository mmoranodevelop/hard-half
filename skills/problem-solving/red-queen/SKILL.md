---
name: red-queen
description: >-
  Treat the problem as a player that updates when you move: name their payoff
  and update rule, the half-life of your fix, and either a reachable
  equilibrium or an explicit arms-race budget with a stop rule. Use when a
  competitor, fraudster, regulator, immune system, market, or attacker will
  change strategy after you ship, last quarter's countermeasure already died,
  or they ask for a moat that lasts. NOT competitive-teardown (static feature
  matrix of a named rival now). NOT scenario-planning (worlds for one bet).
  NOT cobra-equilibrium (the measured population games the instrument; here
  the other side has its own objective). NOT cyber-incident-brief (this hour's
  incident). NOT a forecast of "they might respond": the output is an update
  rule, a half-life, and an equilibrium or a budget.
license: MIT
---

# Red Queen

## The problem moves when you do

The default agent ships a static countermeasure. If the "problem" is a player with their own payoff, the countermeasure has a **half-life**. You run to stay in the same place. That is the red queen.

The leading word is **red queen**. You name the other player's payoff and how they update, then you compute how long your move lasts if they update as expected. "They might respond" is the default. An update rule, a half-life, and either an equilibrium or an arms-race budget with a stop, is not.

This is not `cobra-equilibrium`. There, the population's objective *becomes* your instrument. Here they already have an objective; your move is an input to their next action. It is not `competitive-teardown`: that is a static where/how/so-what on a named rival today. It is not `scenario-planning`: those are worlds around a bet, not a player who updates because of *this* move. It is not `cyber-incident-brief`: that is this hour.

## When to stop

- The measured population will eat a KPI you are about to ship → `cobra-equilibrium`
- Named rival, our move on a static map → `competitive-teardown`
- Uncertain worlds for a bet, not a player-update → `scenario-planning`
- This hour's incident → `cyber-incident-brief`
- Joint constraints that cannot coexist, no player → `empty-and`
- Stuck mechanism / floor, no adaptive player → `first-principles`
- Implementation of a countermeasure whose half-life is already accepted
- Two load-bearing intake facts still blank after one ask → issues list, stop

## Mode

| Mode | When | Output |
|---|---|---|
| **Forecast** | Default. You are about to move | Update rule + half-life + equilibrium or budget + one ASK |
| **Autopsy** | Last move already died | The update they ran + what half-life you should have expected + next stance |
| **Budget** | You already know there is no cheap equilibrium | Arms-race spend per cycle, stop rule, what you refuse to race |

Infer. Ask only when Forecast and Autopsy are equally live.

## Protocol

### 0. Intake — name the other player or stop

Load-bearing (two missing after one round → refuse):

1. Who the other player is (a kind of actor, not "the market" or "uncertainty")
2. Their **payoff** — what they are trying to make true, in their words if you have them, else labelled **assumed**

Also collect: what you are about to ship (or what already died); how fast they can change; what they can see of your move; your cost per cycle.

If you cannot name a player, this is not a red queen. It may be a floor (`first-principles`), a ghost, or ordinary uncertainty (`scenario-planning`).

> **Done when:** a named player and a payoff sentence exist, or you have refused.

### 1. Write their update rule

What they **see**, **how fast** they can change, **what they try** given that payoff. An update rule is a function: your move → their next move. One sentence is enough if it is specific ("when we add check C, they shift to the next unverified channel within ~N days"). "They adapt" is not a rule.

Read `references/update-rule.md` **now** if the player is a regulator, a market (many players), a model-using attacker, or you are about to write "they will copy us." It holds how to write rules for slow vs fast players, and when "the market" is allowed.

> **Done when:** see / speed / next-move are all on the page.

### 2. Half-life of your move

If they update as in step 1, when does your move stop buying the intent? A date, a cycle count, or a **hole** with a range. Unlabelled eternity is how static fixes get shipped.

If the last move already died, autopsy: write the realized half-life next to the one you would have forecast. The gap is the finding.

> **Done when:** a half-life or a hole with a range is on the page.

### 3. Equilibrium or arms-race budget

Search for a stance where **neither** of you wants to deviate given the payoffs (a boring product, a shared standard, a detected-and-too-costly fraud, a treaty-like stop). If you find one, write it and what would knock it over.

If you cannot find an affordable one, you are in a race. Then you must write:

- spend per cycle (yours)
- what you get for that spend (time, not victory)
- **stop rule** — the observation that ends the race (including "we lose this channel")
- what you **refuse** to race (the thing you will not match)

An arms race without a stop rule is a cobra you are running on yourself.

ASK, exactly one: `ship knowing half-life` / `seek equilibrium` / `set budget and stop` / `do not move` / `change player assumption`. Owner, date.

Use `assets/one-pager.md` for the page.

Read `references/worked-examples.md` if they asked for a lasting moat, or if the last countermeasure already died.

> **Done when:** equilibrium or budget-with-stop is on the page, half-life is not infinite unless you broke the update rule, one ASK.

## Anti-patterns

- **They-might.** No rule, no half-life.
- **Eternal moat.** A feature that lasts because you wish it.
- **Teardown-in-disguise.** Static matrix of the rival today; no update.
- **Cobra-mix-up.** You invented a KPI and called the users an enemy.
- **Race-without-stop.** Matching forever, no observation that ends it.
- **Incident-in-disguise.** This hour's patch list.

## Bundled references

| File | Read it when |
|---|---|
| `references/update-rule.md` | Regulator, market-as-many, model-using attacker, or you are about to write "they will copy us" |
| `references/worked-examples.md` | They asked for a lasting moat, or the last countermeasure already died |
| `assets/one-pager.md` | You are writing the deliverable |
