# Skills live in category folders, and every one must be declared explicitly

Skills are at `skills/<category>/<name>/SKILL.md` — `problem-solving/` today, `delivery/` and `comms/` planned. Categories keep the set navigable as it grows past a handful.

This has a consequence that is easy to get wrong twice, in opposite directions.

## What the loader actually does

The plugin's default scan of `skills/` looks for `<name>/SKILL.md` **one level down**. With categories in the way it finds `problem-solving/`, sees no `SKILL.md` inside it, and moves on. **The default scan never reaches a categorised skill.**

What loads them is the explicit array in `plugin.json`:

```json
"skills": ["./skills/problem-solving/first-principles"]
```

Each skill needs its own full path. There is no glob, no category-level include, no recursion.

## The two wrong turns

**Flattening the tree** (`skills/<name>/`) to satisfy the default scan. It works, and it throws away the organisation for a problem that has a supported solution. This was the first implementation and it was wrong.

**Adding a categorised skill and forgetting the array entry.** The skill is valid. It passes frontmatter checks. `npx skills add` installs it, because channel A searches recursively and does not care. And it is **absent for every channel-B user, with no error emitted anywhere** — not at build, not at install, not at runtime. Nobody finds out until someone asks why `/skills-that-matter:the-skill` does not exist.

## Decision

Keep the categories. Declare every skill's full path in `plugin.json`'s `skills` array. **Enforce it in CI**, because the failure mode is silence and silence is not something review catches reliably.

`scripts/validate_skills.py` fails the build on an undeclared skill and prints the exact line to add.

## Consequences

- Adding a skill is two steps, and the second is not optional. `CONTRIBUTING.md` states it; CI enforces it.
- A category that appears in no declaration ships to nobody. That is the supported way to stage work: `deprecated/`, `wip/` and `draft/` are recognised as deliberately unshipped and downgraded from error to warning.
- Channel A and channel B can disagree about what exists. Channel A ships whatever is on disk; channel B ships exactly what is declared. When they must agree, the declaration is the authority.

## Prior art

[`mattpocock/skills`](https://github.com/mattpocock/skills) uses this structure with 22 hand-maintained paths and no automated check — his `CLAUDE.md` carries the rule as prose. At that count the check is worth more than the convention, which is why we added it.
