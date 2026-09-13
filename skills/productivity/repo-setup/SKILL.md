---
name: repo-setup
description: >-
  Configure this repository to use The Hard Half: where generated one-pagers
  and memos are saved, which categories matter here, and the default audience.
  Run once per repo, by name. NOT for writing a new skill, NOT for choosing
  which skill should handle a live problem (use find-skill), and NOT for
  scaffolding a brand-new project (use create-project).
disable-model-invocation: true
license: MIT
---

# Repo Setup

One-time, per repository. The agent interviews; nothing is written until you confirm the path.

The point is to stop every later skill from asking where the page goes. A skill that produces a one-pager and then dumps it in chat has not finished the job.

## When to stop

If this repo already has a `.hard-half.md` and the user is not asking to change it, say so and stop. If they want a new software project scaffolded, run `create-project` instead. If they want to know *which* skill to run, run `find-skill` instead.

## Interview

Ask only what you will write down. One round.

1. **Artifact directory** — where generated pages live (`docs/hard-half/`, `notes/`, a path they name). Default: `docs/hard-half/`.
2. **Default audience** — who most pages in *this* repo are for (internal delivery, sponsor, board, personal). One word.
3. **Categories in play** — which of the catalog buckets this repo will actually use. Offer the list; they pick. Unused categories stay installed but are not the default reach.
4. **Tracker (optional)** — GitHub / Linear / local files, only if they want issues created. Most Hard Half skills produce pages, not tickets.

Do not invent a category they did not pick. Do not write until they confirm the path and the four answers.

## Write

Create or update `.hard-half.md` at the repo root, and nothing else unless they asked:

```markdown
# Hard Half — this repo

artifact_dir: docs/hard-half/
default_audience: internal-delivery
categories: project, comms, management
tracker: none
```

If `AGENTS.md` or `CLAUDE.md` exists, add one line pointing at `.hard-half.md` so a cold session finds it. Do not rewrite those files.

## Done when

- `.hard-half.md` exists and the four fields are filled from the interview, not from guesses
- The user confirmed the path before the write
- You did not produce a weekly-status, a memo, or a skill
