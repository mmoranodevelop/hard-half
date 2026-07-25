# AGENTS.md

Rules that apply to any agent working in this repository. These are conventions the CI enforces or the distribution channels require — not style preferences.

## What this repo is

A public catalog of agent skills, distributed through two independent channels:

- **Channel A** — the `skills` CLI (`npx skills add mmoranodevelop/skills`), which copies files into a user's project.
- **Channel B** — a Claude Code plugin marketplace, which installs a managed read-only bundle.

Both read the same `skills/` directory. Anything that breaks one channel silently breaks half the distribution, so the structural rules below are not negotiable.

## Structure

```
.claude-plugin/
  marketplace.json      # channel B catalog — must be at repo root
  plugin.json           # plugin manifest; the repo root IS the plugin (source "./")
skills/
  <category>/           # problem-solving, delivery, comms, …
    <skill-name>/
      SKILL.md          # required
      references/       # optional, loaded on demand
      assets/           # optional, used in output
      scripts/          # optional, executed without being read into context
scripts/                # repo tooling (validation, compliance) — not shipped as a skill
.github/workflows/
```

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

## Before committing

```bash
python3 scripts/validate_skills.py --repo-root .
```

```bash
python3 scripts/compliance_check.py --repo-root .
```

Both run in CI. The second one matters more than it looks: this repo turns delivery experience into public material, so the characteristic failure is publishing a client name or an internal identifier — and git history preserves it after deletion. Run the term layer locally (see `CONTRIBUTING.md`); CI can only run the pattern layer, because the term list is deliberately gitignored.

## Things that will break users

- **Renaming the plugin.** `mmorano-skills` is an immutable public slug. Users installed with it; changing it breaks their installation with *plugin-not-found*. Change `displayName` instead.
- **Renaming the marketplace.** Same reasoning for `mmorano`.
- **Renaming a skill.** Same again — the invocation path changes.
- **Adding `CLAUDE.md` inside the plugin.** Not a recognized plugin component; it is silently ignored. Instructions ship as skills.
- **Adding a skill without listing it in `plugin.json`'s `skills` array.** It ships to nobody on channel B, silently. CI catches this.
- **Nesting deeper than `skills/<category>/<name>/`.** Two levels is the contract; the validator enforces it.
- **Declaring components in both `plugin.json` and the marketplace entry.** With `strict: true` (the default) that is a conflict and the plugin fails to load. Components are declared in `plugin.json` only.

## Never publish

Client and employer brand names, internal endpoints and hostnames, data schemas, interface identifiers and their prefixes, colleague or contact names, screenshots of real tickets, pricing, contract terms.

Write skills in the abstract from the first draft. Anonymizing afterwards is slower than writing it right, and it leaves traces in the history.

Planning documents (`plan.md` and similar) are gitignored on purpose — they contain employer context and launch strategy. Do not add them to git.
