# productivity

Skills for the work around the work — building and maintaining the tooling you think with, rather than the thing you are shipping.

## Model-invoked

Reachable by you *or* selected automatically by the agent when a task matches.

- [`create-awesome-skills`](create-awesome-skills/SKILL.md) — Build a new agent skill or repair one that isn't working: decide whether it deserves to be a skill, write the description as a routing rule with real anti-triggers, place each piece on the information hierarchy, prune the no-ops, then prove it fires on the right requests and stays silent on the nearest wrong ones.
- [`create-awesome-projects`](create-awesome-projects/SKILL.md) — Scaffold a new project that survives a cold start: interview first, propose a structure that fits what is actually being built, then write the tree, the human-facing docs, and the agentic layer — `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, the first ADR, and a `STATUS.md` that records where the work actually stands.

## User-invoked

*None yet.* These would be reachable only by typing the name, and their job is to orchestrate. See [`.agents/invocation.md`](../../.agents/invocation.md) for the distinction and how each harness enforces it.

---

The conceptual vocabulary in `create-awesome-skills` — leading words, the information hierarchy, the no-op test, sediment, sprawl, prompting the positive — is adapted from [`writing-great-skills`](https://github.com/mattpocock/skills) by Matt Pocock (MIT).
