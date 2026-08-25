# AGENTS.md

Rules that apply to any agent working in this repository. These are conventions the CI enforces or the distribution channels require — not style preferences.

## What this repo is

A public catalog of agent skills, distributed through two independent channels:

- **Channel A** — the `skills` CLI (`npx skills add mmoranodevelop/hard-half`), which copies files into a user's project.
- **Channel B** — a Claude Code plugin marketplace, which installs a managed read-only bundle.

Both read the same `skills/` directory. Anything that breaks one channel silently breaks half the distribution, so the structural rules below are not negotiable.

## Structure

```
.claude-plugin/
  marketplace.json      # channel B catalog — must be at repo root
  plugin.json           # plugin manifest; the repo root IS the plugin (source "./")
.agents/
  invocation.md         # user-invoked vs model-invoked, and how each harness enforces it
  adr/                  # why the repo is shaped this way — read before "fixing" it
.out-of-scope/          # deliberately rejected, so it isn't re-litigated
skills/
  <category>/           # problem-solving, delivery, comms, …
    README.md           # the bucket index, grouped by invocation
    <skill-name>/
      SKILL.md          # required
      agents/
        openai.yaml     # Codex display metadata — cross-harness
      references/       # optional, loaded on demand
      assets/           # optional, used in output
      scripts/          # optional, executed without being read into context
scripts/                # repo tooling — not shipped as a skill
.github/workflows/
```

`AGENTS.md` and `CLAUDE.md` load every session, so they stay short and link out. Depth lives in `.agents/` — the same progressive-disclosure trick the skills use, applied to the repo's own meta-work.

**Skills live at exactly `skills/<category>/<name>/SKILL.md`.**

The category folder has a consequence that is easy to get wrong: **the plugin's default `skills/` scan does not reach into it.** That scan looks for `<name>/SKILL.md` one level down and finds category folders instead. What makes nested skills load is the explicit `skills` array in `plugin.json`:

```json
"skills": ["./skills/problem-solving/first-principles"]
```

Every skill needs its own full path in that array. Forget one and the skill is perfectly valid, installs without complaint, and is **simply absent for every channel-B user** — no error, anywhere. `validate_skills.py` fails the build on exactly this, and prints the line to add.

A category listed nowhere in the array ships to nobody. That is the intended way to stage work: `deprecated/`, `wip/` and `draft/` are recognised as deliberately unshipped and downgraded to a warning.

## The frontmatter contract

Every `SKILL.md` starts with YAML frontmatter containing `name` and `description`. Both are required — **without them the skill is invisible to the `skills` CLI, with no error message.**

```yaml
---
name: skill-name          # lowercase kebab-case, must equal the directory name
description: >-
  What it does, when to use it, and when NOT to use it.
---
```

`name` must equal the directory name. If they diverge, the skill resolves under different identifiers on the two channels.

**The description has a hard budget: `description` + `when_to_use` are truncated at 1,536 characters combined** in the skill listing. The cut is silent and takes from the end — which is where the "NOT for…" clause lives, so truncation removes exactly the part that prevents spurious activation. Put the key use case first. CI fails above the limit and warns from 1,200 so there is room to add `when_to_use` later.

Optional fields worth knowing — `disable-model-invocation`, `user-invocable`, `when_to_use`, `allowed-tools`, `model`, `effort`, `context: fork` — are covered in [`.agents/invocation.md`](./.agents/invocation.md).

## Invocation mode

Every skill is model-invoked (default, add nothing) or user-invoked. User-invoked needs **both** harnesses set, or the skill behaves differently depending on where it is installed:

```yaml
disable-model-invocation: true          # SKILL.md — Claude Code
```
```yaml
policy:
  allow_implicit_invocation: false      # agents/openai.yaml — Codex
```

The test, the doctrine, and the composition rule are in [`.agents/invocation.md`](./.agents/invocation.md). CI does not check the two agree — that one is on review.

## `agents/openai.yaml`

Every skill carries one. Channel A installs into Codex and other Agent-Skills harnesses, where without it the skill appears as a bare slug with no description:

```yaml
interface:
  display_name: "First Principles"
  short_description: "Rebuild a stuck problem up from its invariants"
```

## Writing a `description`

The description is the routing rule. Most systems decide whether to activate a skill primarily from it, so it does 70% of the technical work and deserves more time than the body.

Three parts, in order:

1. **What it does** — concrete, with the real symptoms named.
2. **When to use it** — explicit triggers, in the words a user would actually type.
3. **When NOT to use it** — the part almost nobody writes, and the part that prevents spurious activation. A skill that fires when it shouldn't is the fastest way to get the whole set uninstalled.

Be slightly pushy on the positive triggers: skills under-trigger far more often than they over-trigger. But never at the cost of part 3.

CI warns when a description contains no negative-space marker and fails when it is under 120 characters, because below that it cannot carry all three parts.

## Writing a body

- **Keep it under ~500 lines.** The body loads on every invocation; depth belongs in `references/`, which loads only when the skill says to read it. CI warns past the limit.
- **Explain why, don't just command.** Instructions carrying their reasoning survive situations the author didn't anticipate. Prefer a stated rationale to an all-caps MUST — if you find yourself writing ALWAYS or NEVER, ask whether an explanation would do more work.
- **Structure**: what it's for → when to stop → the procedure → calibration → anti-patterns → bundled references.
- **Every referenced file must exist.** CI fails on dangling `references/…` and `assets/…` paths, because a broken pointer sends the agent nowhere with no error.
- **Say when the skill is the wrong tool.** Every skill should be able to conclude that and stop.

## Maintenance of the E2E tests — do this without being asked

**Whenever you add a skill, rename one, or materially change a `description` or a completion criterion, update `local-testing-scripts.md` in the same piece of work.** It is not a separate task and it does not wait for the user to request it.

That file is the E2E prompt library: per skill, the prompts that must make it fire, the near-misses that must leave it silent, and the output checks. It is **gitignored**, so a fresh clone will not have it — **if it is missing, create it.** This rule is committed precisely so the file can be reconstructed by any agent, in any session, on any harness.

What each skill's section needs — the file itself carries a copyable template at the bottom:

- **A. Must fire** — 2–4 prompts, half Italian and half English, phrased as a *stranger* would: no skill name, no leading word, describing the situation rather than the request. Cover distinct branches, not synonyms of one.
- **B. Must stay silent** — 3+ near-misses that share vocabulary or concepts with the skill but need something else. One must be the nearest neighbour, the one a keyword match would certainly catch. An obviously unrelated prompt tests nothing and is worse than no test, because it reads as coverage.
- **C. Output quality** — a checklist derived from the skill's own completion criteria, checkable at a glance.
- **D. Domain-specific failure** — the characteristic way *this* skill goes wrong. A reasoning skill: can it say no? A generative one: can it decline to produce? Write "none" and justify it if there isn't one.

Also update the header count (`Skill coperte: n / n`) and the date.

Test prompts in **both languages**. The descriptions are English; the user prompts in Italian. Cross-language matching is a real and non-obvious break point.

`validate_skills.py` warns locally about a skill with no section. The check is suppressed when `CI` is set, because CI never has the file.

## Working on a skill

Link every skill into the local harness directories so the working copy *is* your installed skill set — edits go live with no reinstall:

```bash
./scripts/link-skills.sh
```

Re-run after adding, renaming, or removing a skill. This is what makes it practical to use a skill on real work while writing it, which is the one test that separates useful skills from plausible ones.

## Before committing

```bash
python3 scripts/validate_skills.py --repo-root .
```

```bash
python3 scripts/compliance_check.py --repo-root .
```

```bash
claude plugin validate . --strict
```

Both run in CI. The second one matters more than it looks: this repo turns delivery experience into public material, so the characteristic failure is publishing a client name or an internal identifier — and git history preserves it after deletion. Run the term layer locally (see `CONTRIBUTING.md`); CI can only run the pattern layer, because the term list is deliberately gitignored.

## Things that will break users

- **Renaming the plugin.** `hard-half` is an immutable public slug. Users installed with it; changing it breaks their installation with *plugin-not-found*. Change `displayName` instead.
- **Renaming the marketplace.** Same reasoning for `hard-half`.
- **Renaming a skill.** Same again — the invocation path changes.
- **Adding `CLAUDE.md` inside the plugin.** Not a recognized plugin component; it is silently ignored. Instructions ship as skills.
- **Adding a skill without listing it in `plugin.json`'s `skills` array.** It ships to nobody on channel B, silently. CI catches this.
- **Nesting deeper than `skills/<category>/<name>/`.** Two levels is the contract; the validator enforces it.
- **Declaring components in both `plugin.json` and the marketplace entry.** With `strict: true` (the default) that is a conflict and the plugin fails to load. Components are declared in `plugin.json` only.

## Never publish

Client and employer brand names, internal endpoints and hostnames, data schemas, interface identifiers and their prefixes, colleague or contact names, screenshots of real tickets, pricing, contract terms.

Write skills in the abstract from the first draft. Anonymizing afterwards is slower than writing it right, and it leaves traces in the history.

Planning documents (`plan.md` and similar) are gitignored on purpose — they contain employer context and launch strategy. Do not add them to git.
