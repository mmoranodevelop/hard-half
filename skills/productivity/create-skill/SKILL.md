---
name: create-skill
description: >-
  Build a new agent skill, or repair one that isn't working. Walks the whole
  construction path: decide whether the thing deserves to be a skill at all, find
  its leading word, write the description as a routing rule with explicit
  anti-triggers, place each piece on the information hierarchy so the body stays
  legible, prune the no-ops, then verify it fires on the requests it should and
  stays silent on the three nearest requests it shouldn't. Use whenever the user
  wants to write, scaffold, review, shorten, split, or debug a SKILL.md or agent
  skill; reports that a skill never triggers, triggers on the wrong things, or has
  grown too long; wants to turn a repeated prompt, checklist, or CLAUDE.md section
  into something reusable; or asks how to structure skill folders, frontmatter,
  progressive disclosure, or bundled references. NOT for invoking an existing
  skill to do its job — this builds skills, it does not run them. NOT for general
  prompt engineering, and NOT for authoring CLAUDE.md or AGENTS.md, which load
  unconditionally and are governed by different rules.
license: MIT
---

# Create Skill

## The root virtue

A skill exists to wrangle determinism out of a stochastic system. What you are buying is **predictability** — the agent taking the same *process* every run. Not the same output: the same path to it.

Every technique below serves that one goal. When two techniques conflict, the one that makes the run more repeatable wins.

The corollary is the discipline: **a line that does not change what the agent does is not free.** It costs tokens on every invocation and dilutes the lines that do work. Most weak skills are not wrong; they are padded.

## Does this deserve to be a skill?

Answer before writing anything. Most candidates should not be skills, and building one anyway spends context forever to say nothing.

| Situation | Where it belongs |
|---|---|
| You keep pasting the same multi-step procedure | **A skill** |
| A section of `CLAUDE.md` has grown from a fact into a process | **A skill** — move it |
| The discipline is reusable across projects | **A skill** |
| A fact about *this* repo ("we use pnpm", "the API lives at…") | `CLAUDE.md` — it's context, not procedure |
| A one-off task, however elaborate | Just ask for it |
| Behaviour the model already does by default | **Nothing.** Writing it down is a no-op |

That last row is the one people get wrong. Before committing, run the **no-op test** on the whole idea: *would the agent behave differently without this?* If you cannot name the difference, you are about to pay context load for a placebo.

## The construction path

Eight steps. Each ends on a **completion criterion** — a condition you can actually check, because a step whose end is vague invites the agent to declare victory early.

### 1. Name the job, and hunt for the leading word

State in one sentence what process this makes repeatable. Not what it's "about" — what it *does*, in order.

Then look for the **leading word**: a compact concept already living in the model's pretraining that the agent can think *with* while running the skill — *tight*, *red*, *fog of war*, *tracer bullet*, *floor*, *ledger*. It recruits priors the model already holds, so it anchors a whole region of behaviour in one token.

A leading word pays twice: in the body it anchors execution (the agent reaches for the same behaviour every time the word appears), and in the description it anchors invocation (when the same word appears in the user's own prompts and docs, the skill fires more reliably).

Read `references/leading-words.md` when nothing obvious presents itself — the hunt has a method, and the payoff is disproportionate.

> **Done when:** you can state the job in one sentence, and you have either a leading word or a deliberate decision that this skill does not need one.

### 2. Choose the invocation mode

Two modes, spending two different budgets:

- **Model-invoked** — the agent can fire it autonomously, and other skills can reach it. Costs **context load**: the description sits in the window every turn, forever.
- **User-invoked** — only the human, typing its name. Costs **cognitive load**: *you* become the index that has to remember it exists. Zero context load. Set `disable-model-invocation: true`.

The test: *must the agent reach this on its own?* Reusable discipline that the user won't know to ask for → model-invoked. Something with side effects, or whose timing you must own → user-invoked.

Reuse is not the test. Reuse is why you extract a skill at all; it says nothing about who fires it.

When user-invoked skills outgrow what you can remember, the cure is a **router skill**: one user-invoked skill that names the others and when to reach for each.

> **Done when:** the mode is chosen, and — if user-invoked — the frontmatter and any `agents/openai.yaml` both say so.

### 3. Write the description before the body

This inverts the instinct, and it is the highest-leverage step in the path. The description is not a title. **It is the routing rule**, and it decides whether anything you write below ever runs. Writing it first also forces the scope question early, while changing your mind is still cheap.

Three parts, in this order:

1. **What it does** — concrete, with the real symptoms named.
2. **When to use it** — explicit triggers, in the words the user would actually type.
3. **When NOT to use it** — the anti-triggers.

Part 3 is the one almost nobody writes, and it is what separates a skill people keep from one they uninstall. A skill that fires on the wrong task costs more trust than a skill that never fires: the first makes the whole set feel unreliable, the second is merely absent.

Keep one trigger per **branch**. Synonyms that rename a single branch are duplication — collapse them.

Mind the budget: `description` + `when_to_use` are **truncated at 1,536 characters combined**, silently, from the end. Since the tail is where the anti-triggers live, overflow deletes exactly the part that protects you.

Full craft, with before/after examples: `references/description-craft.md`.

> **Done when:** the description names concrete symptoms, lists distinct triggers in the user's vocabulary, states at least one anti-trigger, and fits the budget.

### 4. Map the content onto the ladder

A skill is built from **steps** (ordered actions) and **reference** (definitions, rules, facts), mixed freely. The **information hierarchy** ranks where each piece sits, by how immediately the agent needs it:

1. **In-skill step** — an ordered action in `SKILL.md`. The primary tier.
2. **In-skill reference** — a rule or definition in `SKILL.md`, consulted on demand. Often a legitimately flat peer-set; that is an arrangement, not a smell.
3. **External reference** — pushed into a sibling file, reached by a **context pointer**, loaded only when the pointer fires.

**Progressive disclosure** is the move down that ladder. The test that decides it is **branching**: inline what *every* run needs; push behind a pointer what only *some* runs reach.

Push too little down and the body bloats. Push too much and you hide material the agent actually needs. That tension is the entire decision — there is no rule that resolves it for you.

A **context pointer**'s *wording*, not its target, decides whether the agent actually goes there. "See X for details" is a suggestion; "Read X now if the problem cites a theorem" is an instruction with a trigger.

Depth, plus when to split one skill into two: `references/information-architecture.md`.

> **Done when:** every planned piece has a tier, and each disclosed file has a pointer whose wording says *when* to open it.

### 5. Write the body

Steps in order, reference co-located. **Co-location** means a concept's definition, rules, and caveats live under one heading rather than scattered, so reading one part brings its neighbours along.

Give every step a completion criterion that is *checkable* (can the agent tell done from not-done?) and, where it matters, *exhaustive* — "every modified model accounted for" binds; "produce a change list" does not.

Explain **why**, not just what. Instructions carrying their reasoning survive situations the author never imagined; bare commands do not. If you find yourself writing ALWAYS or NEVER in capitals, that is a signal the reasoning is missing — supply it instead.

Prompt the **positive**. Steering by prohibition backfires: *don't think of an elephant* names the elephant and makes it more available. State the target behaviour so the banned one is never spoken. Keep a prohibition only as a hard guardrail you cannot phrase positively — and even then, pair it with what to do instead.

> **Done when:** every step has a checkable completion criterion, and no instruction is a bare command whose reason a reader would have to guess.

### 6. Prune, aggressively

Skills accumulate **sediment** — stale layers that settle because adding feels safe and removing feels risky. Pruning is the only defence, and it has to be deliberate.

Three passes:

- **Single source of truth.** Each meaning lives in exactly one authoritative place, so changing the behaviour is a one-place edit. Duplication also inflates a meaning's apparent rank on the ladder past its real one.
- **Relevance.** Does this line still bear on what the skill does?
- **No-ops, sentence by sentence.** Test each sentence in isolation: *does it change behaviour versus the default?* When one fails, delete the whole sentence rather than trimming words from it. Be aggressive — most prose that fails should go, not be rewritten.

Then hunt for **collapse**: a triad spelled out at three sites, or a sentence gesturing at one idea, is a passage begging to become a single leading word. Assume every draft is carrying restatements that a leading word retires.

> **Done when:** you have deleted something. A pruning pass that removes nothing did not happen.

### 7. Test the routing

Untested skills are recognisable on sight. This is the step that separates useful from plausible, and it is the one that gets skipped.

- **It fires when it should** — on a request phrased the way a *stranger* would phrase it, not the way you would.
- **It stays silent when it shouldn't fire** — try the **three nearest** requests, the ones a keyword match would catch. Near-misses are the only informative negatives; an obviously unrelated prompt tests nothing.
- **The body produces the work, not a description of the work.** If the output explains how one *would* do the thing, the body is under-specified.
- **It works in a repo that isn't yours.**

Protocol, and how to iterate on what fails: `references/testing-and-iteration.md`.

> **Done when:** one stranger-phrased trigger fires it, three near-misses do not, and it has done real work somewhere other than where it was written.

### 8. Iterate on the failure you observed

Match the fix to the symptom rather than rewriting at random — `references/failure-modes.md` maps each observable symptom to its cause and its cheapest defence.

The trap to avoid: strengthening positive triggers is the most common way to silently destroy the anti-triggers. After any description change, **re-run the negatives from step 7.**

> **Done when:** the observed failure is gone and the negatives still pass.

## Mechanics

The contract that decides whether a skill loads at all — required frontmatter, the optional fields worth knowing, directory layout, name/directory agreement, bundled resources, and cross-harness metadata — is in `references/mechanics.md`.

Read it before shipping. Everything above is craft; that file is the part where getting it wrong means nothing runs, usually with no error message.

Starting skeleton: `assets/skill-template.md`.

## Failure modes, in one place

Recognise these by their symptom; each has a defence in `references/failure-modes.md`.

- **Premature completion** — a step ends before it's genuinely done, attention slipping to *being done*.
- **Duplication** — the same meaning in more than one place.
- **Sediment** — stale layers nobody dared remove.
- **Sprawl** — simply too long, even when every line is live.
- **No-op** — a line the model already obeys by default.
- **Negation** — steering by prohibition, which makes the banned thing more available.
- **Silent non-loading** — the skill is perfectly written and never runs, because of a mechanics error.

## Bundled references

Load on demand; each reads on its own.

| File | Read it when |
|---|---|
| `references/description-craft.md` | Step 3 — the routing rule, anti-triggers, the character budget |
| `references/information-architecture.md` | Step 4 — the ladder, disclosure, co-location, when to split |
| `references/leading-words.md` | Step 1 or 6 — finding a leading word, and collapsing prose into one |
| `references/failure-modes.md` | Step 8, or whenever a skill misbehaves — symptom to cause to defence |
| `references/testing-and-iteration.md` | Step 7 — trigger evals, near-miss design, the iteration loop |
| `references/mechanics.md` | Before shipping — frontmatter, layout, budgets, cross-harness |
| `assets/skill-template.md` | Step 5 — the skeleton to fill in |

---

*The conceptual vocabulary here — leading words, the information hierarchy, the no-op test, sediment, sprawl, and prompting the positive — is adapted from [`writing-great-skills`](https://github.com/mattpocock/skills) by Matt Pocock (MIT). The construction path, the description craft, the mechanics, and the testing protocol are additions.*
