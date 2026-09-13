---
name: cobra-equilibrium
description: >-
  Before a metric, incentive, SLA, policy, ranking, or agent reward ships,
  compute the cobra — how the measured system will adapt to eat the fix, the
  post-adaptation equilibrium after two or three cycles, and whether the
  original intent still holds once the number is gamed. Use when they are about
  to add a KPI, bonus, quota, leaderboard, auto-moderation rule, or "the agent
  will optimize for X", or they say people are gaming the number, Goodhart,
  cobra effect, perverse incentive. NOT a pre-mortem of how a plan fails. NOT
  kill-criteria for a funding tranche. NOT experiment-brief for one A/B. NOT
  red-queen (an opponent with its own payoff — this is the measured population
  adapting to the instrument). NOT value-problem-solver integrity as a side
  filter: this run is the exploitation path and the equilibrium, or a refuse
  to ship the instrument.
license: MIT
---

# Cobra Equilibrium

## The fix is food

The default agent ships the metric. The people (or the model) being measured then eat it. A **cobra** is the post-adaptation state: after two or three cycles of optimizing the instrument, the original intent is gone and the number looks healthy.

The name is the colonial bounty on cobras that produced cobra farms. The leading word is **cobra**. You write the exploitation path *before* the instrument ships — or, in autopsy, you write the path they already ran. A warning that "people might game this" is the default. The path, the equilibrium, and a survive-or-refuse are not.

This is not `red-queen`. There the other side has its own objective and updates when you move. Here the population's objective *becomes* the instrument you pointed at them. It is not `pre-mortem` (plan failure in past tense). It is not `kill-criteria` (dated tests for a bet). It is not the integrity filter inside `value-problem-solver` — that vetoes a product; this prosecutes one instrument.

## When to stop

- An opponent with their own payoff will change strategy when you ship → `red-queen`
- Imagined failure of a launch plan → `pre-mortem`
- Dated kill tests for the next cheque → `kill-criteria`
- One experiment: hypothesis, OEC, sample → `experiment-brief`
- Worth building, who pays → `value-problem-solver`
- The stated problem may not be the problem → `ghost-problem`
- They want a dashboard built, not an instrument judged → say so and stop
- Two load-bearing intake facts still blank after one ask → issues list, stop

## Mode

| Mode | When | Output |
|---|---|---|
| **Forecast** | Default. Instrument not yet live, or about to change | Exploitation path + equilibrium + survive-or-refuse + one ASK |
| **Autopsy** | The number already looks good and the intent is dead | The path they ran + what to retire or replace |
| **Refuse** | They want a single number that cannot survive being the objective | Why, and what would have to be true for any instrument to work |

Infer. Ask only when Forecast and Autopsy are equally live.

## Protocol

### 0. Intake — name the instrument or stop

Load-bearing (two missing after one round → refuse):

1. The instrument (exact metric, bonus formula, SLA, policy trigger, reward the agent maximizes)
2. The **intent** in one mechanism-free sentence (what should be true in the world if this works)

Also collect: who is measured; what they can change without changing the intent; review cadence; what happens to a person (or a model) who wins the number.

Restate intent without the instrument inside it. "Raise NPS" is not an intent. "Fewer customers leave because they could not get help" might be.

> **Done when:** instrument and intent are separate sentences, or you have refused.

### 1. Name the measured party and their legal moves

Who is scored. What they can legally (or cheaply) change that moves the instrument **without** moving the intent. List actual moves, not "they might cheat."

If the measured party is an agent or a model, the legal moves are the actions in its tool loop. "It will be aligned" is not a move list.

> **Done when:** a named party and at least two legal moves that decouple instrument from intent — or an explicit claim that no such move exists, which you must then try to break.

### 2. Write the exploitation playbook

Write it as instructions the measured party would follow. Three cycles, not one trick:

1. First response (the obvious optimize)
2. Counter (what the instrument-owner does when they notice)
3. Second response (how the measured party adapts to the counter)

Read `references/exploitation-playbook.md` **now** if the instrument is a composite score, a ranking, a model reward, or you are about to stop at cycle one. It holds the common eat-patterns (threshold huddling, definition drift, leftover dumping, proxy substitution, reward hacking) and how to write cycle three.

The playbook is the work. A bullet titled "gaming risk" is not.

> **Done when:** three cycles are on the page, each with an actor and a move.

### 3. Name the cobra (the equilibrium)

After those cycles: what the number shows, what the intent shows, who is rewarded. The cobra is that pair — healthy instrument, dead intent — or a rarer pair where both still move together.

If you cannot say what the number will show, you have not finished the playbook.

> **Done when:** instrument-at-equilibrium and intent-at-equilibrium are both stated.

### 4. Survive or refuse

Only these exits:

| Exit | When it is honest |
|---|---|
| **Change the instrument** | A different measure whose legal-move list does not decouple from intent |
| **Companion that cannot be eaten the same way** | A second measure on a different actor or time scale; name how they fail *together* or they are two cobras |
| **Change the payoff** | Winning the number is no longer what the person/model is paid or promoted for |
| **Do not ship** | No surviving instrument is available at this review cadence |

"Add more metrics" without a joint-failure story is how you get a dashboard of cobras.

ASK, exactly one: `do not ship` / `change instrument` / `add companion` / `change payoff` / `retire live instrument`. Owner, date.

Use `assets/one-pager.md` for the page.

Read `references/worked-examples.md` if they want you to bless the KPI, or if the measured party is "the AI".

> **Done when:** one exit is named, the cobra is on the page, and the original instrument is not shipped unchanged unless you have broken the claim that a legal move decouples it from intent.

## Anti-patterns

- **Warning-without-path.** "May be gamed." No playbook.
- **One-trick.** Cycle one only; the cobra lives in cycle three.
- **Moralizing.** The measured party is doing what you paid them to do.
- **Metric salad.** Five more numbers, no joint-failure story.
- **Red-queen mix-up.** A competitor's response is a different skill.
- **Bless-and-ship.** The equilibrium is ugly; the recommendation is to monitor.

## Bundled references

| File | Read it when |
|---|---|
| `references/exploitation-playbook.md` | Composite scores, rankings, model rewards, or you are about to stop at cycle one |
| `references/worked-examples.md` | They want the KPI blessed, or the measured party is an agent |
| `assets/one-pager.md` | You are writing the deliverable |
