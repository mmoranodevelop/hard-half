---
name: your-skill-name
description: >-
  [WHAT IT DOES — concrete, with the real symptoms named. Not the category:
  the words a user in that situation would actually say.]
  Use when [EXPLICIT TRIGGERS in the user's vocabulary, one per branch — no
  synonym pairs]. NOT for [THE NEAREST NEIGHBOUR this should stay out of, and
  why]. NOT for [a second collision, if there is one].
---

<!--
  BUDGET: description + when_to_use are truncated at 1,536 characters combined,
  silently, from the end — which is where the "NOT for" clauses live.
  Target 1,000–1,400. Key use case first.

  USER-INVOKED? Add `disable-model-invocation: true` above, strip the trigger
  lists from the description (nothing routes on them), and add
  `policy.allow_implicit_invocation: false` to agents/openai.yaml.
-->

# [Skill Name]

## [What this is for]

[One or two paragraphs. Lead with the job the skill does. Then state the
defining constraint — the single fact that makes this behave differently from
the obvious default. That line is the most valuable on the page.]

[If the skill has a leading word, introduce it once here, in context, so the
association anchors. Then just use it — re-explaining is duplication.]

## [When to stop / when this is the wrong tool]

[Every skill should be able to conclude it does not apply. State the cases
plainly, so the agent stops instead of forcing the procedure onto a task that
does not fit. Cheap to write, and it prevents the expensive failure.]

## [The procedure]

[Ordered steps, if the skill has them. Delete this section if the skill is all
reference — that is a legitimate shape.]

### 1. [Imperative verb + object]

[What the agent does. Explain why it matters — instructions carrying their
reasoning survive situations you did not imagine.]

[Prompt the positive: state the target behaviour rather than banning its
opposite.]

> **Done when:** [a checkable condition. Can the agent tell done from not-done?
> Where it matters, make it exhaustive — "every X accounted for", not
> "produce a list of X".]

### 2. [...]

> **Done when:** [...]

## [Reference material]

[Flat rules, definitions, and facts consulted on demand. A flat peer-set is
fine — not every skill is a sequence.]

[Co-locate: keep a concept's definition, rules, and caveats under one heading,
so reading one part brings its neighbours along.]

## [Anti-patterns]

[The failure modes specific to *this* skill's domain — what going wrong looks
like here. Delete if the skill has none worth naming; do not pad.]

## Bundled references

[Delete if the skill has no bundled files.]

[Pointer wording decides whether the agent goes. Include an imperative, a
trigger condition, and a payoff — "Read X now if Y, it holds Z" — not
"see X for details".]

| File | Read it when |
|---|---|
| `references/[name].md` | [the condition that should send the agent there] |
| `assets/[name].md` | [when it is used in the output] |

<!--
  BEFORE SHIPPING
  - name equals the directory name, lowercase kebab-case
  - description has all three parts and fits the budget
  - every referenced path exists
  - agents/openai.yaml has display_name and short_description
  - if nested under a category folder, the full path is declared in plugin.json
  - one stranger-phrased trigger fires it; three near-misses do not
  - it has done real work in a repo that is not this one
-->
