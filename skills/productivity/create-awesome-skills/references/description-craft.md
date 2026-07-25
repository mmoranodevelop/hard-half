# Description craft

Step 3. The `description` is not a title — it is the **routing rule**. Most systems decide whether to activate a skill primarily from it, so it does the majority of the technical work in a skill and deserves more time than the body.

A perfect body behind a bad description never runs.

---

## The three parts

Write them in this order. The order matters because truncation cuts from the end, and because the agent reads for relevance before it reads for exclusions.

### 1. What it does — concretely

Name the real symptoms, not the category.

```yaml
# Weak — will never fire
description: Helps debug API integrations
```

```yaml
# Strong — the symptoms are the hooks
description: >-
  Diagnose a failing third-party API integration — 401/403 auth failures, 404 on
  documented endpoints, silent payload rejections, webhook retry storms,
  sandbox-versus-production drift.
```

The second version fires because a user in trouble types *those words*. "Helps debug API integrations" matches nothing anyone actually says while their integration is down.

### 2. When to use it — in the user's vocabulary

Explicit triggers, phrased the way a stranger would phrase them. You are not writing a summary for a colleague who already knows what the skill is; you are writing the words a stressed person types at 19:00 on a Friday.

Two disciplines:

- **One trigger per branch.** Synonyms that rename a single branch are duplication. "build features using TDD" and "asks for test-first development" are one branch written twice — collapse them and spend the tokens on a branch you haven't covered.
- **Be slightly pushy.** Skills under-trigger far more often than they over-trigger, because the agent only consults a skill for tasks it cannot already handle. "Use whenever the user mentions…" beats "Can be used for…". But never buy pushiness by cutting part 3.

### 3. When NOT to use it — the anti-triggers

The part almost nobody writes.

A skill that fires on the wrong task costs more trust than one that never fires. The first makes the entire set feel unreliable and gets everything uninstalled; the second is merely absent. Anti-triggers are cheap insurance against the expensive failure.

Write them against the **nearest neighbours**, not against obviously unrelated work:

```yaml
# Useless — nobody was going to confuse these
NOT for writing poetry or booking flights.

# Useful — these are the actual collisions
NOT for debugging your own internal services, where you control both sides and
can read the logs. NOT for first-time integration setup, which is a
configuration task rather than a diagnosis.
```

The test: *what is the closest task this should stay out of?* That is your anti-trigger. If you cannot name one, the skill is not scoped yet — go back to step 1.

---

## The character budget

`description` and `when_to_use` are **truncated at 1,536 characters combined** in the skill listing.

Three consequences:

1. **Truncation is silent.** No error, no warning at runtime. You find out because the skill misbehaves.
2. **It cuts from the end** — where the anti-triggers live. Overflow deletes exactly the part protecting you from spurious activation.
3. **Put the key use case first.** If anything must survive a cut, it is what the skill does.

Target 1,000–1,400 characters. Below ~120 you cannot fit three parts at all. Above 1,400 you have no room to add `when_to_use` later.

---

## Model-facing vs human-facing

The mode chosen in step 2 changes what the description is *for*.

**Model-invoked** → the description is **model-facing**. It is routing input. Keep the rich trigger phrasing; it is doing work every turn.

**User-invoked** → the description is **human-facing**. Nothing routes on it — the agent cannot fire the skill at all. It is a one-line summary read by a person scrolling a slash-command menu. **Strip the trigger lists.** They are pure context load with no reader.

```yaml
# User-invoked: one line, for a human
description: Reference for writing and editing skills — the vocabulary and
  principles that make a skill predictable.
```

Leaving model-facing trigger prose on a user-invoked skill is one of the most common wasted-token mistakes.

---

## Worked revision

**Before** — a real shape of first draft:

```yaml
description: A skill for doing code reviews. It helps you review code carefully
  and thoroughly, looking at many aspects of the code to find issues.
```

Everything wrong at once: no symptoms, no trigger vocabulary, no anti-triggers, and "carefully and thoroughly" is a **no-op** — the agent is already trying to be careful.

**After:**

```yaml
description: >-
  Review a diff for defects that tests would not catch — race conditions,
  N+1 queries, unhandled error paths, missing authorization checks, migrations
  that lock a hot table. Use when the user asks for a review of a branch, pull
  request, or staged changes, says "does this look right", or wants a second
  pair of eyes before merging. NOT for style or formatting, which the linter
  owns. NOT for reviewing a design or plan that has no code yet — that is a
  design discussion, and reviewing prose as if it were a diff produces noise.
```

What changed: the symptoms became the hooks; the triggers use words people actually type ("does this look right"); the two nearest collisions are excluded by name; and "carefully and thoroughly" is gone, because it was never changing behaviour.

---

## Checklist

- [ ] Names concrete symptoms, not a category
- [ ] Triggers are phrased in the user's vocabulary, not yours
- [ ] One trigger per branch — no synonym pairs
- [ ] At least one anti-trigger, aimed at the **nearest** neighbour
- [ ] Under 1,536 characters including `when_to_use`; ideally under 1,400
- [ ] Key use case is first, so truncation would cost the least
- [ ] Human-facing and stripped of triggers, if the skill is user-invoked
- [ ] No line that fails the no-op test ("carefully", "thoroughly", "as needed")
