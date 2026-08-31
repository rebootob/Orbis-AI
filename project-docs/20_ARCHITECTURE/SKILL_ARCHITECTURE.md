# Skill Architecture

Skills package reusable operating guidance and tool procedures. They are preferred over creating a new agent when the work does not require an independent role, authority boundary, or review loop.

## Verified Hermes native behavior

Read-only runtime identity: Hermes Agent `v0.20.6` (2026.8.27), source checkout `1c5ee5815fe5a3913530ba9d803b5b60bc633766`.

Hermes skills are directories whose required entry file is `SKILL.md`. The file uses YAML front matter followed by Markdown instructions. Native required metadata is `name` (maximum 64 characters) and `description` (maximum 1024 characters); `version`, `license`, `platforms`, `prerequisites`, `compatibility`, and `metadata` are optional. A skill may include `references/`, `templates/`, `assets/`, and other support files.

The active profile loads skills from `HERMES_HOME/skills`. For Orbis AI, this is `/home/allday/.hermes/skills` for default/MASTER and `/home/allday/.hermes/profiles/{coder,reviewer}/skills` for worker profiles. Bundled skills are seeded into the active profile directory; the observed default, coder, and reviewer profiles each expose the same enabled built-ins.

Native project-local locations are `<project-root>/.hermes/skills/` and `<project-root>/.agents/skills/`. They require `hermes skills trust`; trusted directories are recorded through `skills.trusted_project_dirs`. Their precedence is project-local → profile-local → external. A project-local skill can override a same-named lower-tier skill. Other duplicate candidates are treated as ambiguous rather than silently selected. New Orbis names must be unique, stable, lowercase kebab-case identifiers; native `name` and directory names must not use path traversal.

`hermes skills inspect <identifier>` previews a candidate before installation. `hermes skills check [name]` checks installed hub skills for upstream updates, and `hermes skills audit [name]` re-scans installed hub skills. They are not generic local custom-skill validators. `hermes skills list` reports installed/enabled skills; a session can explicitly preload skills with `--skills`.

## Source of truth and validated runtime deployment

Repository `skills/` is the Git/version-controlled source of truth for Orbis skill definitions. It is not assumed to be automatically discovered by Hermes. WP-004C deployed the reviewed Core Skills into the appropriate profile-local `HERMES_HOME/skills` directories and verified source/runtime equality.

| Profile | Intended Core skills |
|---|---|
| MASTER | `project-manager`, `git-governance`, `security` |
| CODER | `code-development`, `git-governance`, `security` |
| REVIEWER | `code-review`, `git-governance`, `security` |

This mapping keeps Core governance skills available across registered projects, not only when Hermes runs inside the Orbis repository. WP-004C validated the mapping in the live WSL2 Hermes runtime.

## CORE — implemented and runtime validated

Core skill implementation: COMPLETE FOR PHASE 4 — repository definitions exist, intended profile deployment is complete, and role/authority behavior has been validated.

| Skill | Applicable role | Purpose |
|---|---|---|
| `project-manager` | MASTER | Task decomposition, status, approvals, and handoff preparation |
| `code-development` | CODER | Approved implementation, targeted tests, and implementation handoff |
| `code-review` | REVIEWER | Diff, regression, security, and test review with explicit PASS or FAIL |
| `git-governance` | MASTER, CODER, REVIEWER | Branch, commit, Pull Request, rollback, and audit controls |
| `security` | MASTER, CODER, REVIEWER | Secret protection, permission ceilings, approval gates, and escalation |

There is no exact installed-name collision with the Core 5. The built-ins `github-code-review` and `requesting-code-review` have related scope; `code-review` must remain focused on the Orbis independent-review boundary.

## DEFERRED

- `n8n` — Phase 8 only.
- `kintone` — future approved integration work.
- Project-specific skills — later approved projects only.

No deferred Skill is implemented by Phase 4.

## Runtime verification executed in WP-004C

The Core Skills were validated using:

1. `SKILL.md` structure/front-matter verification.
2. Profile-local visibility checks.
3. Source/runtime SHA256 comparison.
4. Fresh-session behavioral tests for CODER, REVIEWER, and MASTER.
5. Negative authority-boundary tests.
6. Telegram fresh-session MASTER identity and governance tests.
7. Final Skill-matrix consistency verification across all three profiles.

## Role identity versus Skills

Role identity and reusable Skill guidance are separate concerns.

- Persistent MASTER/CODER/REVIEWER identity belongs to the active Hermes profile, with role boundary guidance in its profile `SOUL.md`.
- Skills describe how the active role performs applicable work.
- Loading a shared Skill does not assign, combine, or change roles.
- MASTER identifies only as MASTER, CODER only as CODER, and REVIEWER only as REVIEWER.
- Runtime REVIEWER PASS/FAIL is review evidence only; final repository `REVIEW_PASS` remains with the ChatGPT Control Plane.
- Merge and all Level 3 authorization remain with the Project Owner.

## Required Orbis skill contract

Every custom Orbis skill must define:

| Contract item | Requirement |
|---|---|
| Purpose | The specific outcome and when the skill is applicable |
| Applicable role | MASTER, CODER, REVIEWER, or an explicitly approved combination |
| Scope | In-scope actions and clear exclusions |
| Allowed tools | Least-privilege tools and permitted commands/integrations |
| Required inputs | Minimum context, artifacts, and approvals required before use |
| Permission ceiling | Highest action level allowed; actions above it require escalation |
| Verification | Concrete evidence and tests required before completion |
| Audit output | Concise record of changed artifacts, evidence, approvals, and outcome |
| Escalation conditions | Secrets, missing approval, destructive actions, runtime/config changes, ambiguous scope, or failed verification |

The contract must preserve existing role boundaries: CODER does not self-approve, REVIEWER does not silently repair, and MASTER does not bypass owner approvals.
