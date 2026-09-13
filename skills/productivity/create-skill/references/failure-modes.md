# Failure modes

Diagnostic. Find the symptom, get the cause and the cheapest defence.

Reach for this when a skill is misbehaving in use — not while drafting, where it becomes a checklist that slows you down for no return.

---

## Quick index

| Symptom you observe | Failure mode |
|---|---|
| Steps end half-done; output is thinner than the instruction asked for | [Premature completion](#premature-completion) |
| Editing behaviour requires changing two places | [Duplication](#duplication) |
| The skill has grown and nobody knows which lines still matter | [Sediment](#sediment) |
| Long, every line defensible, still unwieldy | [Sprawl](#sprawl) |
| The skill seems to change nothing | [No-op](#no-op) |
| The agent does the exact thing you told it not to | [Negation](#negation) |
| Perfectly written, never runs | [Silent non-loading](#silent-non-loading) |
| Fires on the wrong tasks | [Over-triggering](#over-triggering) |
| Never fires unless typed by name | [Under-triggering](#under-triggering) |

---

## Premature completion

**What it is.** A step ends before it is genuinely done, the agent's attention slipping from *doing* to *being done*.

**Defence, in order:**

1. **Sharpen the completion criterion.** Cheap and local, and it fixes most cases. Make it checkable and, where it matters, exhaustive — "every modified model accounted for", not "produce a change list".
2. **Only if the criterion is irreducibly fuzzy *and* you have observed the rush**, split by sequence so the later steps are out of view. Steps still ahead exert a pull toward finishing; hiding them removes it.

Do not reach for the split first. It costs a permanent load and usually was not the problem.

---

## Duplication

**What it is.** The same meaning in more than one place.

**Why it costs more than tokens.** Maintenance becomes a two-place edit, and it will eventually be a one-place edit that misses. Duplication also inflates a meaning's apparent rank on the ladder past its real one — say it three times and it reads as three times as important.

**Defence.** One **single source of truth** per meaning. When the same idea appears in the description *and* the body, the body usually loses: the description is doing routing work the body is not.

---

## Sediment

**What it is.** Stale layers that settle because adding feels safe and removing feels risky.

**Why it is the default.** Every edit is additive under uncertainty. Nobody is ever punished for a line that turned out to be unnecessary; everybody remembers the deletion that broke something.

**Defence.** A deliberate pruning pass, not vigilance during editing. **A pruning pass that removes nothing did not happen** — treat that as the signal it is, and look harder.

---

## Sprawl

**What it is.** Simply too long, even when every line is live and unique. Hurts readability and maintainability, wastes tokens on every invocation.

**Defence, in order:**

1. **Disclose reference** behind context pointers — depth becomes nearly free.
2. **Split by branch** so each path carries only what it needs.
3. **Prune** what neither of the above justified keeping.

Note the trap: disclosure moves the cost, pruning removes it. A skill whose every branch needs all thousand lines does not have a disclosure problem.

---

## No-op

**What it is.** A line the model already obeys by default, so you pay load to say nothing.

**The test.** Does it change behaviour versus the default? Run it on each sentence *in isolation*. When one fails, delete the whole sentence — trimming words from a no-op produces a shorter no-op.

**Common offenders:** "be thorough", "think carefully", "consider all options", "use best practices", "be mindful of edge cases". Each feels like instruction and is scenery.

**The fix for a weak leading word is a stronger word, not a different technique.** *Be thorough* fails because the agent is already thorough-ish; *relentless* or *every single one* changes behaviour.

---

## Negation

**What it is.** Steering by prohibition, which backfires: *don't think of an elephant* names the elephant and makes it more available, not less.

**Defence.** Prompt the **positive** — state the target behaviour so the banned one is never spoken.

| Instead of | Write |
|---|---|
| "Don't write vague acceptance criteria" | "Write acceptance criteria a tester could execute without asking a question" |
| "Never skip the schema check" | "Begin by reading the schema; every later step depends on it" |
| "Avoid long functions" | "Each function does one thing its name states" |

Keep a prohibition only as a hard guardrail you cannot phrase positively — and even then, pair it with what to do instead. `NOT for…` in a description is the legitimate case: it is an exclusion boundary, not a behavioural instruction.

---

## Silent non-loading

**What it is.** The skill is well written and never runs, because of a mechanics error rather than a craft one.

**Defence.** `references/mechanics.md` has the full catalogue. The usual causes: missing `name` or `description`, `name` disagreeing with the directory, or a nested skill never declared in `plugin.json`.

**Diagnostic first move:** confirm the skill is *loaded* before diagnosing why it does not *fire*. Check the `/` menu or the installed skill list. Hours get spent tuning descriptions for skills that were never present.

---

## Over-triggering

**What it is.** The skill fires on tasks it should stay out of.

**Why it is the expensive failure.** It costs more trust than never firing. A skill that fires wrongly makes the entire set feel unreliable and gets everything uninstalled; a skill that never fires is merely absent.

**Defence:**

1. **Add anti-triggers** aimed at the nearest neighbours by name.
2. **Narrow the symptoms** — a description written in categories ("helps with performance") catches everything adjacent; one written in symptoms ("N+1 queries, lock contention on a hot table") catches its own cases.
3. **Consider user-invocation.** If it should only ever run when asked, `disable-model-invocation: true` ends the problem permanently.

---

## Under-triggering

**What it is.** It never fires unless typed by name.

**Diagnose in this order** — the causes are ranked by how often they are the real one:

1. **Is it loaded at all?** See silent non-loading.
2. **Is it user-invoked?** Then it *cannot* fire automatically. Working as configured.
3. **Is the description truncated?** Over 1,536 characters and the tail is gone.
4. **Are the triggers in your vocabulary rather than the user's?** The most common real cause. Rewrite them as the words a stranger would type.
5. **Is the task one the agent handles without help?** Skills are consulted for work the model cannot already do easily. A simple one-step task will not pull one in regardless of the description.

**The trap:** strengthening positive triggers is the most common way to silently destroy the anti-triggers. After any description change, re-run the negatives.
