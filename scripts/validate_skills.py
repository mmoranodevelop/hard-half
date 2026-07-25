#!/usr/bin/env python3
"""Validate the repo against both distribution channels.

Channel A (`npx skills add mmoranodevelop/skills`) needs every SKILL.md to carry
`name` and `description` in YAML frontmatter — without them the skill is simply
invisible to the CLI, with no error.

Channel B (Claude Code plugin) needs `.claude-plugin/marketplace.json` and
`.claude-plugin/plugin.json` to be valid, and needs skills to sit at
`skills/<name>/SKILL.md` so the default plugin scan finds them.

Stdlib only, so CI needs no dependency install.

Usage:
    python3 scripts/validate_skills.py [--repo-root .]

Exit code 0 = clean, 1 = at least one error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# A skill body longer than this is a signal to move detail into references/.
# Not fatal — the loader has no limit — but long bodies burn context on every
# invocation, which is the actual cost.
BODY_LINE_WARN = 500

# Descriptions do the routing. Anything this short cannot carry
# what-it-does + when-to-use + when-NOT-to-use.
DESCRIPTION_MIN_CHARS = 120
DESCRIPTION_MAX_CHARS = 2000

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Phrases that indicate the description states its own negative space. A
# description without one of these will over-trigger, which is the fastest way
# to get a skill set uninstalled.
NEGATIVE_SPACE_MARKERS = ("not for", "not a", "don't use", "do not use", "never use", "not when")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def parse_frontmatter(text: str) -> tuple[dict[str, str], int] | tuple[None, int]:
    """Extract a flat YAML frontmatter block.

    Deliberately a minimal parser rather than PyYAML: the frontmatter we care
    about is flat `key: value` with support for `>-`/`|` block scalars, and
    avoiding the dependency keeps CI to a bare `actions/setup-python`.

    Returns (mapping, body_start_line) or (None, 0) when there is no block.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, 0

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, 0

    data: dict[str, str] = {}
    key: str | None = None
    block_lines: list[str] = []
    block_indent: int | None = None

    def flush() -> None:
        nonlocal key, block_lines, block_indent
        if key is not None:
            data[key] = " ".join(l.strip() for l in block_lines if l.strip()).strip()
        key, block_lines, block_indent = None, [], None

    for raw in lines[1:end]:
        if not raw.strip():
            if key is not None and block_indent is not None:
                block_lines.append("")
            continue

        indent = len(raw) - len(raw.lstrip())
        # Continuation of a block scalar or a wrapped value.
        if key is not None and block_indent is not None and indent >= block_indent:
            block_lines.append(raw)
            continue

        m = re.match(r"^([A-Za-z0-9_.-]+):\s*(.*)$", raw)
        if not m:
            continue
        flush()
        key = m.group(1)
        value = m.group(2).strip()
        if value in (">", ">-", "|", "|-", ">+", "|+"):
            block_lines = []
            block_indent = indent + 1
        else:
            block_lines = [value]
            block_indent = indent + 1
    flush()

    return data, end + 1


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def validate_skill(skill_md: Path, repo_root: Path, report: Report, seen: dict[str, Path]) -> None:
    where = str(skill_md.relative_to(repo_root))
    text = skill_md.read_text(encoding="utf-8")
    fm, body_start = parse_frontmatter(text)

    if fm is None:
        report.error(where, "no YAML frontmatter block (file must start with '---')")
        return

    name = strip_quotes(fm.get("name", "")).strip()
    description = strip_quotes(fm.get("description", "")).strip()

    if not name:
        report.error(where, "frontmatter is missing required field 'name'")
    else:
        if not NAME_RE.match(name):
            report.error(where, f"name '{name}' must be lowercase kebab-case")
        dir_name = skill_md.parent.name
        if name != dir_name:
            report.error(
                where,
                f"name '{name}' does not match its directory '{dir_name}' — "
                "the two must agree or invocation paths differ between channels",
            )
        if name in seen:
            report.error(where, f"duplicate skill name '{name}', already used by {seen[name]}")
        else:
            seen[name] = skill_md.relative_to(repo_root)

    if not description:
        report.error(where, "frontmatter is missing required field 'description'")
    else:
        n = len(description)
        if n < DESCRIPTION_MIN_CHARS:
            report.error(
                where,
                f"description is {n} chars — under {DESCRIPTION_MIN_CHARS} it cannot state "
                "what it does, when to use it, and when NOT to, so routing will be unreliable",
            )
        if n > DESCRIPTION_MAX_CHARS:
            report.warn(where, f"description is {n} chars, over the {DESCRIPTION_MAX_CHARS} soft cap")
        low = description.lower()
        if not any(m in low for m in NEGATIVE_SPACE_MARKERS):
            report.warn(
                where,
                "description never says when NOT to use the skill — expect spurious activation",
            )

    # Layout: skills/<category>/<name>/SKILL.md. Categories are organisational
    # only — the plugin loader does not infer them, which is why every skill has
    # to be declared explicitly in plugin.json (checked in validate_manifests).
    try:
        rel = skill_md.relative_to(repo_root / "skills")
    except ValueError:
        report.warn(where, "SKILL.md lives outside skills/ — the plugin default scan will not see it")
    else:
        if len(rel.parts) != 3:
            report.error(
                where,
                "must be exactly skills/<category>/<name>/SKILL.md — the category folder is "
                "required so the set stays organised as it grows",
            )

    body_lines = len(text.splitlines()) - body_start
    if body_lines > BODY_LINE_WARN:
        report.warn(
            where,
            f"body is {body_lines} lines (soft limit {BODY_LINE_WARN}) — "
            "move detail into references/ so it loads only when needed",
        )

    # Referenced sibling files must exist, or the skill sends the agent nowhere.
    body = "\n".join(text.splitlines()[body_start:])
    for ref in re.findall(r"(?:references|assets|scripts)/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+", body):
        if not (skill_md.parent / ref).exists():
            report.error(where, f"references a bundled file that does not exist: {ref}")


def load_json(path: Path, report: Report) -> dict | None:
    where = path.name
    if not path.exists():
        report.error(where, f"missing required file at {path}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.error(where, f"invalid JSON: {exc}")
        return None


# Categories deliberately excluded from the plugin: kept in the repo for channel A
# and for history, but not shipped in the managed bundle.
UNSHIPPED_CATEGORIES = {"deprecated", "wip", "draft"}


def validate_skill_declarations(
    repo_root: Path, plugin: dict, report: Report, skill_names: dict[str, Path]
) -> None:
    """Every skill must be listed in plugin.json's `skills` array.

    This is the one check that matters most. Because skills live at
    skills/<category>/<name>/, the plugin's default `skills/` scan does not reach
    them — it looks for <name>/SKILL.md one level down and finds category folders
    instead. The explicit `skills` array is what makes them load.

    Forget to add the path and the skill is perfectly valid, installs fine, and is
    simply absent on channel B, with no error anywhere. That silence is the whole
    reason this check exists.
    """
    declared_raw = plugin.get("skills", [])
    if isinstance(declared_raw, str):
        declared_raw = [declared_raw]

    declared: set[Path] = set()
    for entry in declared_raw:
        if not isinstance(entry, str):
            report.error("plugin.json", f"skills entry is not a string: {entry!r}")
            continue
        if not entry.startswith("./"):
            report.error("plugin.json", f"skills path '{entry}' must start with './'")
            continue
        target = repo_root / entry
        if not target.exists():
            report.error("plugin.json", f"skills path '{entry}' does not exist")
            continue
        if not (target / "SKILL.md").exists():
            report.error("plugin.json", f"skills path '{entry}' contains no SKILL.md")
            continue
        declared.add(target.resolve())

    for name, skill_md_rel in sorted(skill_names.items()):
        skill_dir = (repo_root / skill_md_rel).parent.resolve()
        if skill_dir in declared:
            continue
        try:
            category = skill_md_rel.parts[1]
        except IndexError:
            category = ""
        rel_path = "./" + str(skill_dir.relative_to(repo_root))
        if category in UNSHIPPED_CATEGORIES:
            report.warn(
                "plugin.json",
                f"skill '{name}' is in '{category}/' and not shipped in the plugin — "
                "intentional, but it is invisible to channel B users",
            )
        else:
            report.error(
                "plugin.json",
                f"skill '{name}' is not declared in the 'skills' array — it will be "
                f"silently missing for every plugin user. Add \"{rel_path}\"",
            )


def validate_manifests(repo_root: Path, report: Report, skill_names: dict[str, Path]) -> None:
    market = load_json(repo_root / ".claude-plugin" / "marketplace.json", report)
    plugin = load_json(repo_root / ".claude-plugin" / "plugin.json", report)

    if market is not None:
        for field in ("name", "owner", "plugins"):
            if field not in market:
                report.error("marketplace.json", f"missing required field '{field}'")
        if isinstance(market.get("owner"), dict) and "name" not in market["owner"]:
            report.error("marketplace.json", "owner.name is required")
        name = market.get("name", "")
        if name and not NAME_RE.match(name):
            report.error("marketplace.json", f"marketplace name '{name}' must be kebab-case")

        for entry in market.get("plugins", []):
            label = f"marketplace.json[{entry.get('name', '?')}]"
            if "name" not in entry:
                report.error(label, "plugin entry missing 'name'")
            if "source" not in entry:
                report.error(label, "plugin entry missing 'source'")
            source = entry.get("source")
            if isinstance(source, str):
                if not source.startswith("./"):
                    report.error(label, f"relative source '{source}' must start with './'")
                elif not (repo_root / source).exists():
                    report.error(label, f"source path '{source}' does not exist")

    if plugin is not None:
        if "name" not in plugin:
            report.error("plugin.json", "missing required field 'name'")
        pname = plugin.get("name", "")
        if pname and not NAME_RE.match(pname):
            report.error("plugin.json", f"plugin name '{pname}' must be kebab-case")

        validate_skill_declarations(repo_root, plugin, report, skill_names)

    # The plugin slug is public and immutable once installed; a mismatch between
    # the two manifests means /plugin install resolves one name and the runtime
    # registers another.
    if market and plugin:
        entries = [p.get("name") for p in market.get("plugins", [])]
        if plugin.get("name") not in entries:
            report.error(
                "manifests",
                f"plugin.json name '{plugin.get('name')}' is not listed in marketplace.json "
                f"plugins {entries}",
            )
        for entry in market.get("plugins", []):
            if entry.get("name") == plugin.get("name"):
                for shared in ("version", "description"):
                    a, b = entry.get(shared), plugin.get(shared)
                    if a and b and a != b:
                        report.warn("manifests", f"'{shared}' differs between marketplace.json and plugin.json")

    if not skill_names:
        report.error("skills/", "no skills found — both channels would install an empty plugin")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="repository root (default: cwd)")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    report = Report()
    seen: dict[str, Path] = {}

    skill_files = sorted(repo_root.glob("skills/**/SKILL.md"))
    for skill_md in skill_files:
        validate_skill(skill_md, repo_root, report, seen)

    validate_manifests(repo_root, report, seen)

    print(f"Validated {len(skill_files)} skill(s) in {repo_root}")
    for name in sorted(seen):
        print(f"  - {name}")

    if report.warnings:
        print(f"\n{len(report.warnings)} warning(s):")
        for w in report.warnings:
            print(f"  ! {w}")

    if report.errors:
        print(f"\n{len(report.errors)} error(s):")
        for e in report.errors:
            print(f"  x {e}")
        return 1

    print("\nOK — valid for both distribution channels.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
