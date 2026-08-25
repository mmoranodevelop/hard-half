# The repository root is the plugin

The repo ships through two channels off one `skills/` tree. Channel B (the Claude Code plugin) needs a plugin directory, and there are two ways to arrange that.

## The rejected layout

The obvious one, and the one the original plan specified:

```
.claude-plugin/marketplace.json
plugins/hard-half/.claude-plugin/plugin.json
skills/<category>/<name>/SKILL.md
```

This does not work. The plugin's root would be `plugins/hard-half/`, so reaching the skills means `../../skills/` — and **every plugin path field must be relative to the plugin root and start with `./`**. There is no supported way to point a plugin at a directory above itself.

The failure is quiet: the manifest is valid, the plugin installs, and it contains no skills.

## Decision

Both manifests live at the repository root, and the plugin's `source` is the repo itself:

```
.claude-plugin/
  marketplace.json     # the catalog
  plugin.json          # the plugin manifest
skills/                # reachable from the plugin root as ./skills/...
```

```json
{ "name": "hard-half", "source": "./" }
```

One tree, one source of truth, reachable by both channels. This is a documented pattern, not a workaround, and it is what [`mattpocock/skills`](https://github.com/mattpocock/skills) does.

## Consequences

- `plugin.json` and `marketplace.json` sit in the same directory. That is fine — they are different files with different schemas.
- Components are declared in **`plugin.json` only**. With `strict: true` (the default), a component declared in both the manifest and the marketplace entry is a conflict and the plugin refuses to load.
- The marketplace entry stays metadata-only: name, source, description, category, tags.
- Repo tooling (`scripts/`) sits inside the plugin root. It is not a recognised plugin component, so it is ignored at load time and costs nothing.

## Do not

Move the manifests under `plugins/`. It reads tidier and ships an empty plugin.
