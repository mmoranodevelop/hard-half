# Mechanics

The contract that decides whether a skill loads **at all**. Everything else in this skill is craft; this is the part where a mistake means nothing runs, usually with no error message anywhere.

Read before shipping.

**Contents**
- [Frontmatter](#frontmatter)
- [Directory layout](#directory-layout)
- [Bundled resources](#bundled-resources)
- [Plugin distribution](#plugin-distribution)
- [Cross-harness metadata](#cross-harness-metadata)
- [Names are permanent](#names-are-permanent)
- [Silent failure catalogue](#silent-failure-catalogue)

---

## Frontmatter

YAML between `---` markers, at the very top of `SKILL.md`.

```yaml
---
name: skill-name
description: >-
  What it does, when to use it, and when NOT to use it.
---
```

**`name`** — lowercase kebab-case. Make it equal the directory name. Tooling that reads the directory and tooling that reads the field will otherwise resolve the same skill under two identifiers.

**`description`** — the routing rule. See `description-craft.md`.

Under the [Agent Skills](https://agentskills.io) standard these two are what make a skill discoverable. Some installers require both and **skip a skill that lacks them without reporting anything**.

### Optional fields worth knowing

| Field | What it does |
|---|---|
| `disable-model-invocation: true` | Only the human can invoke it. For side effects, or timing you must own. |
| `user-invocable: false` | The inverse: only the agent. For background knowledge that is not a meaningful user action. |
| `when_to_use` | Extra trigger context. **Shares the 1,536-character budget with `description`.** |
| `allowed-tools` | Tools pre-approved for the turn that invokes the skill. |
| `disallowed-tools` | Tools removed from the pool while the skill is active. |
| `argument-hint` | Autocomplete hint, e.g. `[issue-number]`. |
| `model` / `effort` | Override model or effort level while the skill is active. |
| `context: fork` | Run the skill in a forked subagent — worth considering for long protocols whose intermediate reasoning need not land in the main transcript. |

Boolean fields accept `true`/`false`, and also `yes`, `no`, `on`, `off`, `1`, `0` in any case.

---

## Directory layout

```
skill-name/
├── SKILL.md          # required
├── references/       # loaded on demand via context pointers
├── assets/           # templates and files used in the output
├── scripts/          # executed without being read into context
└── agents/
    └── openai.yaml   # cross-harness display metadata
```

`scripts/` is the underrated one. A script **executes without its source entering the context window**, so deterministic and repetitive work belongs there rather than in prose the agent must read and then imitate. If three runs of a skill all end with the agent writing the same helper, that helper should have shipped with the skill.

---

## Bundled resources

**`references/`** — reference material reached by a **context pointer**. The pointer's wording decides whether the agent goes: "See X" is a suggestion, "Read X now if the problem cites a theorem" is an instruction with a trigger.

Every referenced path must exist. A dangling pointer sends the agent nowhere and produces no error — it simply proceeds without the material it was told to load.

Give a reference file over ~300 lines a table of contents.

**`assets/`** — templates, skeletons, and files that end up in the output rather than in the reasoning.

**`scripts/`** — executables. Ship the helper instead of describing it.

---

## Plugin distribution

If the skill ships inside a Claude Code plugin, two things bite:

**Skills at `skills/<name>/SKILL.md`** are found by the plugin's default scan. Skills nested deeper — under a category folder, say `skills/<category>/<name>/` — **are not**. The default scan looks one level down, finds the category folder, and stops.

Nested skills load only when declared explicitly:

```json
"skills": ["./skills/productivity/create-skill"]
```

Each skill needs its own full path. No globs, no category-level includes, no recursion.

**List the slug in `skills.sh.json`** at the repo root, in the matching group. That file only changes how the catalog appears on skills.sh — not how the CLI installs. An unlisted skill still ships; it just lands in "Other skills".

**Declare components in one place.** With `strict: true` (the default), a component declared in both `plugin.json` and the marketplace entry is a conflict and the plugin refuses to load.

**A `CLAUDE.md` inside a plugin is ignored.** It is not a recognised component. Instructions ship as skills.

**Version pins updates.** Users receive a change only when `plugin.json`'s `version` string moves. Ship without bumping it and every existing install silently keeps the old copy.

---

## Cross-harness metadata

`agents/openai.yaml`, beside the `SKILL.md`:

```yaml
interface:
  display_name: "Create Skill"
  short_description: "Build a skill that actually fires, and prove it"
```

Codex and other Agent-Skills harnesses read this for the skill picker. Without it the skill appears there as a bare slug with no description.

For a user-invoked skill, add the Codex half of the restriction:

```yaml
policy:
  allow_implicit_invocation: false
```

**Both harnesses, or neither.** A skill restricted in one and open in the other behaves differently depending on where it was installed, and nothing surfaces the discrepancy at runtime.

---

## Names are permanent

Once published, these are immutable:

- **The skill's `name`** — it is the invocation path. Renaming breaks every reference and every user's muscle memory.
- **The plugin slug** — users installed with it; renaming breaks their installation with *plugin-not-found*.
- **The marketplace name** — same reasoning.

To change a display label, use `displayName`. Choose the real names as if you cannot change them, because you cannot.

---

## Silent failure catalogue

Every one of these produces a skill that looks fine and does nothing. None of them reports an error.

| Cause | Symptom |
|---|---|
| Missing `name` or `description` | Installer skips the skill entirely |
| `name` ≠ directory name | Resolves under two different identifiers |
| Nested under a category, not declared in `plugin.json` | Valid, installs, invisible to every plugin user |
| Description over 1,536 characters | Tail truncated — the anti-triggers are what's lost |
| Dangling `references/…` path | Agent proceeds without the material |
| `version` not bumped | Existing installs keep the old copy forever |
| Trigger prose left on a user-invoked skill | Context paid every turn, read by nobody |

The common thread: **the skill system fails quietly.** Build the checks into CI, because review does not reliably catch an absence.
