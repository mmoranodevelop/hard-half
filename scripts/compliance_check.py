#!/usr/bin/env python3
"""Scan the repo for material that should never be published.

This repo turns delivery experience into public skills, which means the failure
mode is not a bug — it is leaking a client name, an internal hostname, or a
credential into a public repository. That leak survives deletion because it
stays in git history, so it has to be caught before the commit.

Two layers:

1. **Pattern layer** (always on) — credentials, private hostnames, internal IPs,
   absolute local paths, phone numbers. These are catchable without knowing
   anything about your employer.

2. **Term layer** (opt-in) — the names you personally must not publish: client
   brands, your employer, interface ID prefixes, colleague names, internal
   domains. These live in `compliance-terms.txt`, which is gitignored, because a
   committed list of forbidden words *is itself* the leak.

Create the term list from the template:

    cp scripts/compliance-terms.example.txt compliance-terms.txt

Usage:
    python3 scripts/compliance_check.py [--repo-root .] [--terms compliance-terms.txt]
    python3 scripts/compliance_check.py --history      # also scan git history

Exit code 0 = clean, 1 = something needs review.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SCAN_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".txt", ".py", ".sh", ".js", ".ts", ".toml"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".idea", ".vscode"}

# Literals that are meant to be public, or are documented identifiers that merely
# share a shape with something sensitive.
ALLOWED_LITERALS = {
    "m.morano.develop@gmail.com",
    "devtools@example.com",
    "author@example.com",
    # A documented Claude Code frontmatter field, not a hostname.
    "metadata.internal",
}

PATTERNS: list[tuple[str, re.Pattern[str], str]] = [
    (
        "credential",
        re.compile(
            r"(?i)\b(?:api[_-]?key|secret|passwd|password|client[_-]?secret|access[_-]?token|"
            r"authorization)\b\s*[:=]\s*['\"]?[A-Za-z0-9_\-\.]{12,}"
        ),
        "looks like a hardcoded credential",
    ),
    (
        "token",
        re.compile(r"\b(?:sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|xox[baprs]-[A-Za-z0-9-]{10,})\b"),
        "looks like a provider token",
    ),
    (
        "bearer",
        re.compile(r"(?i)\bBearer\s+[A-Za-z0-9\-_\.]{20,}"),
        "looks like a bearer token",
    ),
    (
        "private-ip",
        re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"),
        "internal IP address",
    ),
    (
        "internal-host",
        re.compile(r"\b[a-z0-9][a-z0-9.-]*\.(?:local|internal|intranet|lan|corp|test)\b"),
        "internal hostname",
    ),
    (
        "local-path",
        re.compile(r"(?:/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+|[A-Z]:\\\\Users\\\\)"),
        "absolute path from a personal machine",
    ),
    (
        "email",
        re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
        "email address",
    ),
    (
        "phone",
        re.compile(r"(?<![\d.])\+\d{1,3}[\s.-]?\d{2,4}[\s.-]?\d{3,4}[\s.-]?\d{3,4}(?![\d.])"),
        "phone number",
    ),
]


def iter_files(repo_root: Path):
    """Yield the files that would actually be published.

    In a git repo this is tracked files plus untracked-but-not-ignored ones —
    which is precisely the set that a push would expose. Scanning everything on
    disk instead produces false positives from local planning notes and, worse,
    trains you to ignore the output.
    """
    candidates: list[Path] | None = None

    if (repo_root / ".git").exists():
        try:
            out = subprocess.run(
                ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                cwd=repo_root,
                capture_output=True,
                text=True,
                timeout=60,
            )
            if out.returncode == 0:
                candidates = [repo_root / line for line in out.stdout.splitlines() if line]
        except (OSError, subprocess.TimeoutExpired):
            candidates = None

    if candidates is None:
        candidates = [p for p in repo_root.rglob("*")]

    for path in sorted(set(candidates)):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(repo_root).parts):
            continue
        if path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        yield path


def load_terms(path: Path | None) -> list[str]:
    if path is None or not path.exists():
        return []
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            terms.append(line)
    return terms


def scan_files(repo_root: Path, terms: list[str]) -> list[str]:
    findings: list[str] = []
    lowered = [t.lower() for t in terms]

    for path in iter_files(repo_root):
        rel = path.relative_to(repo_root)
        # This file defines the patterns; matching itself is noise.
        if rel == Path("scripts/compliance_check.py"):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue

        for lineno, line in enumerate(lines, start=1):
            for label, pattern, why in PATTERNS:
                for match in pattern.finditer(line):
                    hit = match.group(0)
                    if hit in ALLOWED_LITERALS:
                        continue
                    findings.append(f"{rel}:{lineno} [{label}] {why}: {hit[:80]}")

            low = line.lower()
            for term, term_low in zip(terms, lowered):
                if term_low in low:
                    findings.append(f"{rel}:{lineno} [term] forbidden term '{term}'")

    return findings


def scan_history(repo_root: Path, terms: list[str]) -> list[str]:
    """A removed line is still published if it ever landed in a commit."""
    if not (repo_root / ".git").exists():
        return ["(no git repository — history scan skipped)"]
    if not terms:
        return ["(no term list — history scan needs compliance-terms.txt to be useful)"]

    findings: list[str] = []
    for term in terms:
        try:
            out = subprocess.run(
                ["git", "log", "-p", "-i", "-S", term, "--oneline"],
                cwd=repo_root,
                capture_output=True,
                text=True,
                timeout=120,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            findings.append(f"[history] could not scan for '{term}': {exc}")
            continue
        if out.stdout.strip():
            first = out.stdout.strip().splitlines()[0]
            findings.append(f"[history] '{term}' appears in history, first hit: {first[:100]}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--terms", default="compliance-terms.txt")
    parser.add_argument("--history", action="store_true", help="also scan git history")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    terms_path = repo_root / args.terms
    terms = load_terms(terms_path)

    if terms:
        print(f"Loaded {len(terms)} forbidden term(s) from {terms_path.name}")
    else:
        print(
            f"No term list at {terms_path.name} — running pattern checks only.\n"
            "  Client and employer names are NOT being checked. To enable:\n"
            "    cp scripts/compliance-terms.example.txt compliance-terms.txt"
        )

    findings = scan_files(repo_root, terms)
    if args.history:
        findings += [f for f in scan_history(repo_root, terms) if not f.startswith("(")]

    if findings:
        print(f"\n{len(findings)} item(s) need review:")
        for f in findings:
            print(f"  ! {f}")
        print("\nEach one is either a real leak or a false positive worth confirming by hand.")
        return 1

    print("\nClean — no leak patterns found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
