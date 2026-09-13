# Leading words

A **leading word** is a compact concept already living in the model's pretraining that the agent thinks *with* while running the skill — *tight*, *red*, *fog of war*, *tracer bullet*, *floor*, *ledger*, *seam*.

It works by recruiting priors the model already holds. Instead of spending forty tokens describing a quality, you spend one that already carries it, and the model arrives with the whole associated region of behaviour attached.

---

## Why it pays twice

**In the body, it anchors execution.** The agent reaches for the same behaviour every time the word appears. Repetition accumulates a distributed definition — though a genuinely strong word may only need to appear once.

**In the description, it anchors invocation.** When the same word lives in the user's prompts, docs, and code, the agent links that shared language to the skill and fires it more reliably. This is why a leading word chosen from the *user's* vocabulary beats a cleverer one from yours.

---

## Finding one

Three routes, in order of yield.

### 1. Look for a restatement begging to collapse

The strongest signal is prose that says one thing three ways.

| Restatement | Collapses to | Why it works |
|---|---|---|
| "fast, deterministic, low-overhead" | a **tight** loop | One pretrained word carrying all three qualities |
| "a loop you believe in" | the loop goes **red** | Converts a fuzzy gate into a binary observable state |
| "the parts of the system you can't see yet" | **fog of war** | Recruits a whole spatial metaphor, including how to dispel it |
| "a thin end-to-end slice that proves the path" | a **tracer bullet** | Carries the purpose *and* the disposability |
| "the theoretical minimum this could cost" | the **floor** | Makes it a number you compute, not an adjective |

Assume every draft is carrying restatements a leading word retires. Go find them — this is the highest-yield pruning move available.

### 2. Steal the domain's own word

If practitioners already say *seam*, *blast radius*, *hot path*, *cutover*, use it. You get the pretrained associations **and** the invocation hook, because the user types it too.

### 3. Invert a fuzzy quality into an observable state

*Be careful about the loop* is unmeasurable. *The loop goes red* is a state the agent can check. Words that name a **state** outperform words that name a **virtue**, because a state has a test and a virtue only has a vibe.

---

## Judging a candidate

Run the **no-op test** on it: does this word change behaviour versus the default?

*Be thorough* fails — the agent is already thorough-ish, so you paid tokens for nothing. The fix is a **stronger word** (*relentless*, *exhaustive*, *every single*), not a different technique. Weak leading words are the most common no-op in skill writing precisely because they feel like they are doing something.

Three more tests:

- **Is it pretrained?** An invented term carries no priors; you must then define it, which costs the tokens the technique was meant to save. Invent only when nothing existing fits, and expect to pay for it.
- **Is it unambiguous here?** A word with a competing meaning in the domain will recruit the wrong region. *Red* in a testing skill is excellent; *red* in a design skill fights the colour.
- **Does it survive repetition?** You will use it a dozen times. A word that grates on the third reading is the wrong word.

---

## Using one well

- **Introduce it once, in context**, so the association is anchored: "the loop goes **red** on the bug — that is the gate."
- **Then just use it.** Re-explaining is duplication, and it signals to the agent that the word cannot be trusted to carry meaning on its own.
- **Put it in the description too**, front-loaded, so it does its invocation work.
- **One leading word per region of behaviour.** Two competing metaphors for the same idea is worse than none — the agent has to reconcile them, and reconciliation is exactly the variance you were trying to remove.

---

## When a skill needs none

Plenty of good skills have no leading word. A skill that is a flat checklist of unrelated rules has nothing to anchor; forcing a metaphor onto it adds a concept the reader must learn for no return.

The decision is legitimate either way — make it deliberately rather than by omission.
