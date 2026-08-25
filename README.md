<!--
  BANNER — add before launch.
  Export light and dark variants to assets/banner-light.png / assets/banner-dark.png,
  then uncomment. GitHub picks the variant from the reader's theme.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.png">
  <img alt="Skills That Matter" src="assets/banner-light.png">
</picture>
-->

# Skills for problems where the standard answer is why you're stuck

[![skills.sh](https://skills.sh/b/mmoranodevelop/skills-that-matter)](https://skills.sh/mmoranodevelop/skills-that-matter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Ask a coding agent a hard question and it will give you the consensus answer. That is what it is good at — consensus is what its training data is dense in, and most of the time consensus is exactly what you want.

But on a problem that is genuinely stuck, **the consensus answer is the thing that is stuck.** The industry standard is the reason the metric hasn't moved in four years. The architecture everyone uses is the architecture that makes the cost impossible. Retrieval, applied to a problem where retrieval has already been tried by everybody, returns the wall you were already standing in front of.

These skills are for that case.

## The declared enemy

There are a lot of agent frameworks now that try to help by **owning your process** — a pipeline you enter at one end and exit at the other, with the reasoning happening inside a box you don't control. When the process is wrong, you can't debug it, because the process is the product.

The bet here is the opposite: **small, legible, composable disciplines** that you can read in full in ten minutes, disagree with, edit, and compose. Every skill in this repo states its reasoning, states when *not* to use it, and hands you back the wheel. If you think a step is wrong, you can see the step.

The second enemy is softer and more expensive: **AI-assisted work that accelerates you toward the average.** A faster path to the standard answer is enormously valuable right up until the standard answer is the problem. Nothing in this repo helps you go faster. It helps you go somewhere else.

<!--
  EMAIL CAPTURE — add before launch, above the quickstart.
  Plan §5 point 4: this belongs before the install instructions, not after.
  Replace with a real list URL; a dead link here costs more than no link.

> **Get new skills as they ship** — [subscribe](https://YOUR-LIST-URL)
-->

## Quickstart

### Channel A — `skills` CLI (works with ~45 agents)

```bash
npx skills@latest add mmoranodevelop/skills-that-matter
```

It detects the agents you have installed and writes the skills into each one's directory. Preview first without installing:

```bash
npx skills@latest add mmoranodevelop/skills-that-matter --list
```

Install everything, everywhere, without prompts:

```bash
npx skills@latest add mmoranodevelop/skills-that-matter --all
```

### Channel B — Claude Code plugin

```bash
claude plugin marketplace add mmoranodevelop/skills-that-matter
```

```bash
claude plugin install skills-that-matter@skills-that-matter
```

Or from inside Claude Code: `/plugin marketplace add mmoranodevelop/skills-that-matter` then `/plugin install skills-that-matter@skills-that-matter`.

### Which channel

They are not redundant — they are two different relationships with the code.

| | Channel A (`skills` CLI) | Channel B (Claude Code plugin) |
|---|---|---|
| **Works with** | ~45 agents | Claude Code only |
| **What happens** | Files are **copied** into your project | A **managed bundle** is installed |
| **Editing** | Yours. Fork it, rewrite it, delete half of it | Read-only, always current |
| **Updates** | `npx skills update` when you want them | Automatic |
| **Invocation** | `/first-principles` | `/skills-that-matter:first-principles` |
| **Choose it when** | You want these as a starting point for your own | You want them to just work and stay updated |

Channel A is for people who will make them theirs. Channel B is for people who want to subscribe rather than fork. Both are supported deliberately.

### Where these run

These follow the [Agent Skills](https://agentskills.io) open standard — a `SKILL.md` carrying `name` and `description`, with optional `references/`, `assets/`, and `scripts/`. Any tool implementing the standard can load them, and [a lot of them do](https://agentskills.io/clients): Claude Code and the Claude apps, ChatGPT and Codex, Cursor, GitHub Copilot and VS Code, Gemini CLI, Amp, OpenCode, Goose, Kiro, Roo Code, Factory, Letta, JetBrains Junie, Mistral Vibe, and others.

**Worth knowing before you go looking for a store: Claude Code is the only one that has one.** Every other harness is directory-based — it scans a folder and loads whatever `SKILL.md` files it finds. `~/.agents/skills/` (user) and `.agents/skills/` (project) are the convergent cross-vendor paths, and they are where the `skills` CLI writes.

So "is it available on the Cursor store" is the wrong question everywhere except Claude Code. The right one is whether the files land in the directory that harness reads — which is Channel A's whole job.

## Why these skills exist

### "The agent gave me the industry-standard answer to a problem where the industry standard is the reason I'm stuck"

> "you must not fool yourself — and you are the easiest person to fool."
> — Richard Feynman, Caltech commencement address, 1974

**The problem.** You bring a hard problem — a cost that won't come down, a latency floor nobody can beat, a research program that has stalled, an integration everyone says can't be done at that scale. You get back a competent summary of what the field already does. Which you already knew, because you're in the field. Worse, when you push, you get creative-sounding variations built on the same buried assumption, because nothing ever went back and asked which assumptions were load-bearing.

Meanwhile the actual answer, when someone eventually finds it, is almost never cleverness. It's someone noticing that a constraint everybody treated as physics was written down in 2019 by a person who has since left.

**The fix.** Refuse to retrieve before deriving. Classify *why* the thing is called impossible — a proved theorem and an unexamined habit demand completely different attacks. Compute the floor the invariants actually imply, and measure the gap between that floor and today. Then rebuild upward, and red-team the result until it either produces a falsifiable experiment or admits it is rhetoric.

That discipline is not new. It's how a first-principles engineer works, and it's slow, and it is very hard to do to yourself — which is exactly the kind of thing worth writing down and handing to an agent that doesn't get tired or attached.

→ [`first-principles`](skills/problem-solving/first-principles/SKILL.md)

### "I wrote a skill and the agent never uses it"

> "The best modules are those whose interfaces are much simpler than their implementations."
> — John Ousterhout, *A Philosophy of Software Design*

**The problem.** You wrote the skill. It's good — the instructions are right, you'd follow them yourself. The agent ignores it. So you make the description punchier, and now it fires on everything, including the three tasks it has no business touching. You turn it off.

The failure was never in the body. A skill is a deep module, and the `description` is its interface: almost every system decides whether to activate a skill from that field alone. It isn't a title — **it's a routing rule**, doing most of the technical work in a file where most people spend the least of their time. The other half of the failure is that nobody writes the *anti*-triggers, and a skill that fires on the wrong task costs more trust than one that never fires at all.

**The fix.** Treat the description as the artifact: three parts, written before the body, with the nearest neighbours excluded by name. Put depth behind pointers so the body stays legible. Delete every line the model already obeys. Then actually test it — one trigger phrased the way a stranger would phrase it, and the **three nearest** requests that must stay silent.

→ [`create-awesome-skills`](skills/productivity/create-awesome-skills/SKILL.md)

### Why so few skills

Because six mediocre skills is worse than two that work, and twenty is worse than six. A repo you can evaluate in three minutes gets installed. A repo that makes you choose from a menu of things you can't assess gets closed.

The next three failure modes are already scoped, and each ships when it has been used on real work — not before:

| Failure mode | The fix | Skill |
|---|---|---|
| "The agent wrote the wrong spec because nobody told it what *not* to build" | Explicit non-goals and acceptance criteria | `to-spec` *(next)* |
| "It worked in sandbox" | A disciplined loop for third-party integration debugging | `integration-debug` *(next)* |
| "The stakeholder didn't understand the status" | One voice per audience, not one voice for all audiences | `client-update` *(planned)* |

## Reference

Skills divide on one axis: **who can invoke them.**

- **Model-invoked** — reachable by you *or* selected automatically by the agent when the task matches. These hold reusable discipline.
- **User-invoked** — reachable only by typing the name. These *orchestrate*.

The rule: a user-invoked skill may call model-invoked ones, never another user-invoked one. That keeps composition acyclic and makes the set designed rather than accumulated.

Skills are grouped by category on disk (`skills/<category>/<name>/`), so the set stays navigable as it grows.

| Skill | Category | Type | Use it when |
|---|---|---|---|
| [`first-principles`](skills/problem-solving/first-principles/SKILL.md) | `problem-solving` | Model-invoked | A problem is called impossible, a metric has been flat for years, an industry does it one way for reasons nobody can state, or a target is far from what current approaches deliver |
| [`create-awesome-skills`](skills/productivity/create-awesome-skills/SKILL.md) | `productivity` | Model-invoked | You're writing a skill, or one you wrote never fires, fires on the wrong things, or has grown too long to read |
| [`create-awesome-projects`](skills/productivity/create-awesome-projects/SKILL.md) | `productivity` | Model-invoked | You're starting a new project and want the folder, the structure, and the agent-facing files set up before any code exists |
| [`signal-vs-noise`](skills/productivity/signal-vs-noise/SKILL.md) | `productivity` | Model-invoked | You have too much on, feel busy but not productive, or are about to automate something nobody has used yet |

### Inside `first-principles`

The body is a seven-phase protocol; the depth loads only when the problem needs it.

| File | What it holds |
|---|---|
| [`SKILL.md`](skills/problem-solving/first-principles/SKILL.md) | The protocol, calibration rules, anti-patterns |
| [`references/impossibility-classes.md`](skills/problem-solving/first-principles/references/impossibility-classes.md) | Six classes of impossibility, and the premise-attack table for CAP, FLP, Arrow, Shannon, Carnot, Landauer, halting, no-cloning, Abbe — plus the walls that have no door |
| [`references/constraint-ledger.md`](skills/problem-solving/first-principles/references/constraint-ledger.md) | Ledger format, interrogation questions, Chesterton's fence protocol |
| [`references/computing-the-floor.md`](skills/problem-solving/first-principles/references/computing-the-floor.md) | Floor techniques per domain, the gap ratio, how floors go wrong |
| [`references/reconstruction-moves.md`](skills/problem-solving/first-principles/references/reconstruction-moves.md) | The deletion move and ten substitution moves |
| [`references/dfx-passes.md`](skills/problem-solving/first-principles/references/dfx-passes.md) | Design for Cost, Manufacturing, Simplicity, Production rate, Verification, Reversibility |
| [`references/worked-examples.md`](skills/problem-solving/first-principles/references/worked-examples.md) | Three full runs — including one where the honest answer is *no* |
| [`assets/report-template.md`](skills/problem-solving/first-principles/assets/report-template.md) | The deliverable structure |

## Design principles

Every skill here follows the same rules, and they are worth stating because they are what make the set composable:

1. **The `description` is a routing rule, not a title.** It says what the skill does, when to use it, and — the part almost nobody writes — when *not* to. A skill that fires when it shouldn't is the fastest route to being uninstalled.
2. **Progressive disclosure.** The body is what the agent needs every time. Depth lives in `references/` and loads only on demand, so a skill that is occasionally deep is not expensive to have installed.
3. **Explain why, don't just command.** Instructions that carry their reasoning survive contact with situations the author didn't imagine. Rules without reasons don't.
4. **Say when to stop.** Every skill can conclude that it is the wrong tool. That is a feature.
5. **Falsifiable output.** If nothing a skill produces could be shown wrong by an experiment, it produced rhetoric.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version: skills come from work actually done, CI enforces the frontmatter contract, and the plugin slug is immutable.

Repo conventions live in [AGENTS.md](AGENTS.md); shared vocabulary in [CONTEXT.md](CONTEXT.md).

## License

MIT — see [LICENSE](LICENSE).
