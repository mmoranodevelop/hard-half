# Codex marketplace lives at repo root, same as the Claude plugin

## Context

Codex and ChatGPT now read a plugin marketplace at `.agents/plugins/marketplace.json`, plus a plugin identity at `.codex-plugin/plugin.json`. The documented happy path stores plugins under `plugins/<name>/`. That layout is the same trap [ADR 0001](0001-repo-root-is-the-plugin.md) already rejected for Claude: the skills tree would sit *above* the plugin root, and every plugin path must start with `./`.

## Decision

Keep the repository root as the plugin for Codex too.

```
.agents/plugins/marketplace.json   # catalog; source.path = "./"
.codex-plugin/plugin.json          # Codex identity; skills = "./skills/"
.claude-plugin/                    # unchanged; Codex also accepts this as a legacy catalog
skills/                            # one tree, three channels
```

## Consequences

- Three manifests, one tree. The Claude `skills[]` array stays the source of truth for nested skills on channel B. Codex's `skills` field is a directory string (`./skills/`); if its scanner is one level deep, channel A (`npx skills add`) is still the reliable install path for Codex users.
- Do not create `plugins/hard-half/` and copy the tree. Two copies will drift.
- Do not declare Claude components on the marketplace entry. `strict: true` still applies to channel B.
