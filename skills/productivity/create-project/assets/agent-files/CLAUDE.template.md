<!--
  A POINTER, not a second copy of AGENTS.md. Two copies of the same rules
  drift apart, and the reader cannot tell which is authoritative.
  Add standing rules here only when they must survive across sessions.
-->

The operating rules for this project live in [AGENTS.md](./AGENTS.md) — structure, commands, conventions, and what breaks things. Read it before changing anything.

**Standing rule, no prompting required:** update [STATUS.md](./STATUS.md) as part of any change that moves the work — what now works, what is half-finished and how far it got, what the next action is. A status file updated at the end of a session is one that gets skipped when the session runs long, which is exactly when it mattered.

Depth, loaded only when relevant:

- [`.agents/adr/`](./.agents/adr/) — why the project is shaped this way. Read the relevant ADR before "fixing" the structure.
- [`CONTEXT.md`](./CONTEXT.md) — domain vocabulary, when a word here means something specific
- [`.out-of-scope/`](./.out-of-scope/) — deliberately rejected, so it is not re-litigated

Before committing:

```bash
[the check that must pass]
```
