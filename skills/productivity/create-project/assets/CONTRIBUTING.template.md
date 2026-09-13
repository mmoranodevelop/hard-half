# Contributing

<!--
  Write this ONLY for a team or public project. A solo repository does not
  need contribution guidelines, and adding them anyway produces a document
  nobody reads and nobody updates — the cargo-cult scaffold in miniature.

  Everything here must be true today. Do not describe a review process that
  does not exist or a CI pipeline that has not been set up.
-->

## Getting set up

```bash
[clone, install, and whatever else is genuinely required]
```

```bash
[the command that proves the setup worked]
```

[Anything that commonly goes wrong on a fresh machine, and its fix. This
paragraph saves more time than the rest of the file combined.]

## Making a change

1. [Branch naming, if there is a convention worth following]
2. Make the change. [AGENTS.md](./AGENTS.md) has the structure and conventions.
3. [The test command that must pass]
4. Update [STATUS.md](./STATUS.md) if the change moves the work forward.

## What gets a pull request accepted

<!-- State the real bar rather than a generic one. Specific expectations are
     actionable; "write good code" is not. -->

- [the actual standard — tests for new behaviour, a changelog entry, a
  migration that runs both directions, whatever genuinely applies]

## Reporting a problem

[Where to open it, and the detail that makes a report actionable here —
usually a reproduction, the version, and what was expected instead.]

## Decisions

Before proposing a structural change, check [`.agents/adr/`](./.agents/adr/)
and [`.out-of-scope/`](./.out-of-scope/) — the reasoning may already be
recorded, and if it is out of date that is a more interesting conversation
than the proposal itself.
