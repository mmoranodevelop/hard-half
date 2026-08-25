#!/usr/bin/env bash
set -euo pipefail

# Dev-only. Not an installer — users install via `npx skills add` or the plugin.
#
# Symlinks every shipped skill into the local harness skill directories:
#   ~/.claude/skills  — Claude Code
#   ~/.agents/skills  — the convergent cross-vendor path: Codex, Cursor, and
#                       the rest of the Agent-Skills ecosystem read it
#
# The point is the edit loop. Each entry is a symlink into this working copy, so
# a change to a SKILL.md is live immediately — no reinstall, no copy step. That
# is what makes it practical to actually use a skill on real work while writing
# it, which is the one test that separates useful skills from plausible ones.
#
# Re-run after adding, renaming, or removing a skill.

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DESTS=("$HOME/.claude/skills" "$HOME/.agents/skills")

# Categories that ship to nobody — kept in the repo, not linked. Mirrors
# UNSHIPPED_CATEGORIES in validate_skills.py.
UNSHIPPED_RE='/skills/(deprecated|wip|draft)/'

names=()
srcs=()
while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  if [[ "$src/" =~ $UNSHIPPED_RE ]]; then
    continue
  fi
  names+=("$(basename "$src")")
  srcs+=("$src")
done < <(find "$REPO/skills" -name SKILL.md -not -path '*/node_modules/*' -print0)

if [ ${#names[@]} -eq 0 ]; then
  echo "no skills found under $REPO/skills" >&2
  exit 1
fi

for DEST in "${DESTS[@]}"; do
  # If $DEST is itself a symlink pointing into this repo, the per-skill links
  # below would be written back into the repo's own tree. Bail out rather than
  # scribble on the working copy.
  if [ -L "$DEST" ]; then
    resolved="$(cd "$(dirname "$DEST")" && cd "$(readlink "$DEST")" 2>/dev/null && pwd || echo "")"
    case "$resolved" in
      "$REPO"|"$REPO"/*)
        echo "error: $DEST is a symlink into this repo ($resolved)." >&2
        echo "Remove it (rm \"$DEST\") and re-run; it will be recreated as a real directory." >&2
        exit 1
        ;;
    esac
  fi

  mkdir -p "$DEST"

  for i in "${!names[@]}"; do
    name="${names[$i]}"
    src="${srcs[$i]}"
    target="$DEST/$name"

    # A real directory here is a previously copied install of the same skill.
    # Replace it with the symlink so there is one source of truth.
    if [ -e "$target" ] && [ ! -L "$target" ]; then
      rm -rf "$target"
    fi

    ln -sfn "$src" "$target"
    echo "linked $name -> ${src#$REPO/} ($DEST)"
  done
done

echo
echo "Done. Restart Claude Code (or run /reload-plugins) to pick up new skills."
