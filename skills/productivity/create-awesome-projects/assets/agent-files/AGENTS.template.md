# AGENTS.md

<!--
  Loaded every session — length is a permanent tax. Keep it short and point
  into .agents/ for depth. Delete every section that does not apply; an
  unfilled heading is worse than an absent one.
  Everything here must be TRUE TODAY. Aspiration written as fact teaches the
  reader the file is unreliable, and they stop trusting all of it.
-->

## What this is

[One or two sentences. What the project does and who runs it. Enough that
someone who opened the repo by accident knows whether to keep reading.]

## Commands

<!-- The highest-value section: what an agent needs in its first 30 seconds,
     and what it will otherwise guess wrong. Exact, working commands only. -->

```bash
[install]
```

```bash
[run]
```

```bash
[test]
```

```bash
[lint / typecheck / format]
```

## Structure

```
[tree, one line per directory saying what goes in it]
```

[Anything non-obvious about where new code goes.]

## Conventions

<!-- Only what is NOT self-evident from reading the code, and NOT already
     enforced by a linter or formatter — those are no-ops here. -->

- [naming, error handling, where new modules go, layering rules]

## What breaks things

<!-- The costly-mistake list. This is the section people thank you for. -->

- [migrations that must run in order; a config that must stay in sync with X;
  a generated file that must not be hand-edited; a test that is slow for a
  reason and must not be "optimised"]

## Depth

- [`.agents/adr/`](./.agents/adr/) — why the project is shaped this way
- [`CONTEXT.md`](./CONTEXT.md) — domain vocabulary
- [`STATUS.md`](./STATUS.md) — what is done, what is next

## Before committing

```bash
[the check that must pass]
```
