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
| `value-problem-solver` | Model-invoked | Reusable discipline. "Is this worth building?" and "does this create value?" are asked without knowing a protocol of seven filters exists. Triage hands off to first-principles, issue-tree, and prd-spec. |
| `verified-hard-problem` | Model-invoked | Reusable discipline. "Solve this unsolved / Millennium / unsolvable claim" arrives without a lock. The value is forcing claim-lock, lemma attack, and a verification gate instead of a confident essay. |
| `ghost-problem` | Model-invoked | Reusable discipline. A sliding "real problem" or a shipped fix that changed nobody's Monday arrives as a request to solve the ticket. The value is a load-bearing vs displaced verdict, not another solution against a ghost. |
| `cobra-equilibrium` | Model-invoked | Reusable discipline. "Add a KPI / bonus / agent reward" arrives without the eat-path. The value is the three-cycle playbook and a survive-or-refuse, not a warning that people might game it. |
| `empty-and` | Model-invoked | Reusable discipline. Locally-green workstreams arrive as a both-and. The value is the empty intersection (or an exhibited point), not a stapled Gantt. |
| `red-queen` | Model-invoked | Reusable discipline. A countermeasure against a competitor, fraudster, or attacker arrives as a static fix. The value is an update rule, a half-life, and an equilibrium or a stop, not a lasting-moat essay. |
| `missing-axis` | Model-invoked | Reusable discipline. "All the options feel the same" / "we're looking in the wrong place" arrives as a rebuild on the current line. The value is one measurable coordinate plus a kill test, not a brainstorm. |
| `create-skill` | Model-invoked | "Write me a skill that…" is an unambiguous trigger, and the whole point is that the discipline gets applied without the user having to know it exists. The upstream skill it derives from is user-invoked; that choice buys zero context load at the cost of remembering it — a trade that makes sense in a set of twenty user-invoked skills, less so here. |
| `create-project` | Model-invoked | Filesystem side effects would normally argue for user-invocation. What makes autonomous firing safe is that the skill's **first action is an interview, not a write**: a spurious activation produces questions, which are cheap to dismiss. The body carries a hard gate — nothing reaches disk before the user confirms the path and the tree — and that gate, not the invocation mode, is what protects the user's disk. |
| `client-ticket` | Model-invoked | Tracker writes would normally argue for user-invocation. Safe to fire autonomously because the first action is **schema discovery and a preview**, not create. A spurious activation asks or shows a preview. Create only when the bind is clean and they asked to file, or the spec is complete. |
| `signal-vs-noise` | Model-invoked | Daily cut. The user who is busy-but-not-productive will not think to type a skill name. |
| Catalog skills (`weekly-status`, `issue-tree`, …) | Model-invoked | One job, one page. The description's negative space is what keeps two hundred skills from all firing at once. |
| `find-skill` | Model-invoked | "Which skill / is there a skill for / I don't know where to start" must fire without the user remembering a slash command. It names a skill or a gap; it does not do the job. A spurious activation is a recommendation, which is cheap to dismiss. |
| `repo-setup` | User-invoked | Writes a config file. Timing and path must be the human's. |

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
