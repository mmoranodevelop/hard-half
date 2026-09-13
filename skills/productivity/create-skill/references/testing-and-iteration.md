# Testing and iteration

Step 7 and 8. Untested skills are recognisable on sight — generic, unconstrained, missing the exceptions only someone who has been burned would know. This is the step that gets skipped, and skipping it is why most published skills do not work.

---

## The four tests

### 1. It fires when it should

Write the trigger prompt **as a stranger would phrase it**, not as you would. You know the skill exists and will unconsciously use its vocabulary; a real user will not.

Concretely: do not name the skill, do not use its leading word, and describe the situation rather than the request. "The integration worked yesterday and now every call comes back 403" beats "help me debug an integration".

### 2. It stays silent when it should

**Three near-misses.** This is the test with the most information in it, and the design of the negatives is what makes it worth anything.

A useful negative is a request that **shares vocabulary or concepts** with the skill but needs something else. A useless negative is obviously unrelated — "write me a haiku" tests nothing about a code-review skill.

For a skill about diagnosing third-party API failures:

| Prompt | Should fire? | Why it is a good test |
|---|---|---|
| "Our partner's API started returning 403 this morning" | ✅ | The real case |
| "My own service returns 403 to the frontend" | ❌ | Same status code, wrong side of the boundary |
| "How do I set up OAuth with this vendor?" | ❌ | Same vendor, configuration not diagnosis |
| "The webhook handler throws on malformed JSON" | ❌ | Same integration, ordinary local bug |

Each negative isolates one dimension the description must discriminate on. That is what makes the failure informative: when one fires, you know *which* boundary is weak.

### 3. The body produces work, not a description of work

The failure looks like: *"To compute the floor, you would identify the irreducible inputs and price them at commodity rates."*

That is the skill explaining itself instead of running. It means the body reads as exposition rather than instruction. Fix by converting the explanatory sentence into an imperative with a completion criterion.

### 4. It works in a repo that isn't yours

Test from a different project. Inside the repo where the skill was written, its `SKILL.md` is just a file in context — you are testing your own reading, not the skill's activation.

This also surfaces hidden dependencies on your setup: a tool you have installed, a directory convention only your projects follow, a `CLAUDE.md` supplying context the skill assumed.

---

## Running it

The fast loop is a symlink from the local skill directory into your working copy, so an edit is live with no reinstall. Then, in a *different* project, run the trigger prompt and the three negatives in **fresh conversations** — a skill already loaded earlier in a conversation contaminates the test, because the model has seen it and will reach for it.

Record what happened, not what you concluded:

| Prompt | Expected | Actual | Notes |
|---|---|---|---|
| stranger-phrased trigger | fires | fires | reached for references/x.md unprompted |
| near-miss 1 | silent | **fired** | "403" alone is pulling it in |

The "actual" column is the data. "It seemed fine" is not.

---

## Scaling up

When a skill matters enough to justify it, replace the four hand-run tests with a set of ~20 realistic queries — roughly half should-trigger, half should-not — and measure the trigger rate across several runs each, since activation is stochastic and a single run tells you little.

Two rules make such a set worth building:

- **The queries must be realistic.** Concrete, specific, with the detail real requests carry — file paths, column names, a bit of backstory, lowercase, abbreviations, the occasional typo. "Format this data" tests nothing.
- **Focus on edge cases.** Clear-cut examples pass regardless of description quality, so they discriminate nothing. The near-misses are where the signal is.

Split the set: tune on one half, measure on the other. Optimising a description against the same queries you measure with produces a description that fits those twenty queries and nothing else.

---

## The iteration loop

1. **Observe a specific failure.** Not "it's not great" — which prompt, what happened.
2. **Name the failure mode.** `failure-modes.md` maps symptom → cause → cheapest defence.
3. **Apply the cheapest defence first.** Sharpen a criterion before splitting a skill; add an anti-trigger before rewriting a description.
4. **Re-run the negatives.** Always.
5. **Stop when the failure is gone**, rather than continuing to polish.

### Generalise, don't overfit

You are iterating on three or four examples, but the skill will run on thousands. A fix that makes those examples pass by naming them is worse than no fix — it looks like progress and buys nothing.

The tell is specificity creeping into the skill: a rule that mentions the exact scenario from your test, an exception carved for one prompt. When a problem resists two attempts, try a different metaphor or a different leading word rather than piling on constraints. It is cheap to try and occasionally lands something much better.

### Keep it lean while iterating

Iteration is additive by default, so pair every fix with a pruning pass. If a run shows the agent doing unproductive work, look for the line that caused it and delete that line — do not add a line telling it to stop.

---

## When to stop

- The observed failures are gone and the negatives pass.
- You are making changes you cannot justify with an observation.
- The next improvement would require overfitting to your test cases.

Then use it on real work for a while. The failures that matter most show up in use, not in tests — and they are the ones worth the next iteration.
