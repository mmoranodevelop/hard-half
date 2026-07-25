# Model-invoked vs user-invoked

Every skill in this repo splits on one axis: **who can reach it.** The README declares the taxonomy; this file is how it is actually enforced, in both harnesses.

## The two kinds

**Model-invoked** — reachable by the user *or* selected automatically by the agent when a task matches. These hold **reusable discipline**: the agent should be able to reach for them on its own, because the whole point is that they fire when needed without the user remembering they exist.

The `description` is **model-facing**. Keep the rich trigger phrasing ("Use whenever the user says…, mentions…, asks for…") — that text is what routing reads.

Default. Add nothing.

**User-invoked** — reachable **only by the human typing `/name`**. These **orchestrate**, or have side effects whose timing the user must own.

The `description` becomes **human-facing**: a one-line summary read by someone scrolling a slash-command menu. Strip the trigger lists — nothing is routing on them any more, so they are pure noise.

```yaml
# SKILL.md frontmatter — Claude Code
disable-model-invocation: true
```

```yaml
# agents/openai.yaml — Codex
policy:
  allow_implicit_invocation: false
```

**Both, or neither.** A skill that is user-invoked in one harness and model-invoked in the other behaves differently depending on where it is installed, and nothing surfaces the discrepancy.

## The test

*Could the agent usefully reach for this on its own, without being asked?*

If yes, model-invoked. If reaching for it unprompted would be presumptuous, expensive, or surprising, user-invoked.

Reuse is **not** the test. Reuse is why you extract a skill at all; it says nothing about who should fire it.

## Current state

| Skill | Kind | Why |
|---|---|---|
| `first-principles` | Model-invoked | Reusable discipline. A user describing a stuck problem often does not know this protocol exists — the value depends on the agent reaching for it unprompted. Its own triage section handles the cost of firing when it shouldn't. |

## Composition

A user-invoked skill may invoke model-invoked ones. It may **never** reach another user-invoked skill — that is the human's call by definition, and chaining them would route around the restriction that makes them user-invoked in the first place.

Express dependencies as prose invocation ("run the `/first-principles` skill"), not as `../other-skill/FILE.md` cross-references. Shared reference material lives inside the skill that owns it; other skills reach it by invoking that skill. Deep links across skill folders break the moment either skill is installed standalone — which channel A does routinely, with `--skill=<name>`.

## The other frontmatter fields

Supported by Claude Code, unused here so far, worth knowing:

| Field | What it does |
|---|---|
| `user-invocable: false` | The inverse restriction: only the agent can invoke it. For background knowledge that is not a meaningful user action. |
| `when_to_use` | Extra trigger context, appended to `description` in the listing. **Counts toward the same character budget.** |
| `allowed-tools` | Tools pre-approved for the turn that invokes the skill. |
| `disallowed-tools` | Tools removed from the pool while the skill is active. |
| `model` / `effort` | Override the model or effort level while the skill is active. |
| `context: fork` | Run the skill in a forked subagent. Worth considering for long protocols whose intermediate reasoning does not need to land in the main transcript. |

## The character budget

`description` and `when_to_use` are **truncated at 1,536 characters combined** in the skill listing.

Truncation is silent and lands mid-sentence — and since the tail of a well-written description is the *when NOT to use it* clause, what gets cut is precisely the part that prevents spurious activation. Put the key use case first, and treat the cap as hard. `validate_skills.py` fails the build above it.
