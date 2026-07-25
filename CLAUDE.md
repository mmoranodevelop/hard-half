The operating rules for this repository live in [AGENTS.md](./AGENTS.md) — structure, the frontmatter contract, how to write a `description`, and the changes that break existing users. Read it before touching anything.

**Standing rule, no prompting required:** whenever you add a skill, rename one, or materially change a `description` or a completion criterion, update `local-testing-scripts.md` — the E2E prompt library — as part of the same work. It is gitignored, so **create it if it is missing**; the template and the full requirements are in [AGENTS.md](./AGENTS.md) under *Maintenance of the E2E tests*.

Deeper references, loaded only when relevant:

- [`.agents/invocation.md`](./.agents/invocation.md) — user-invoked vs model-invoked, and how each harness enforces it
- [`.agents/adr/`](./.agents/adr/) — why the repo is shaped the way it is. Read the relevant ADR before "fixing" the plugin layout, the category structure, or the gitignore.
- [`CONTEXT.md`](./CONTEXT.md) — shared vocabulary
- [`.out-of-scope/`](./.out-of-scope/) — things deliberately rejected, so they aren't re-litigated

Before pushing:

```bash
python3 scripts/validate_skills.py --repo-root . && python3 scripts/compliance_check.py --repo-root . && claude plugin validate . --strict
```
