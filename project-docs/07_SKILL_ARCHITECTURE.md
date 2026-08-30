# Skill Architecture

Skills package reusable operating guidance and tool procedures. They are preferred over creating a new agent when the work does not require an independent role, authority boundary, or review loop.

## Verified Hermes native behavior

Hermes skills are directories whose required entry file is `SKILL.md`. The file uses YAML front matter followed by Markdown instructions. Native required metadata is `name` (maximum 64 characters) and `description` (maximum 1024 characters); `version`, `license`, `platforms`, `prerequisites`, `compatibility`, and `metadata` are optional. A skill may include `references/`, `templates/`, `assets/`, and other support files.

The active profile loads skills from `HERMES_HOME/skills`. For Orbis AI, this is `/home/allday/.hermes/skills` for default/MASTER and `/home/allday/.hermes/profiles/{coder,reviewer}/skills` for worker profiles. Bundled skills are seeded into the active profile directory; the observed default, coder, and reviewer profiles each expose the same enabled built-ins.

Trusted project-local skills have the highest discovery precedence, followed by active-profile skills and then configured external directories. A project-local skill can override a same-named lower-tier skill. Other duplicate candidates are treated as ambiguous rather than silently selected. New Orbis names must be unique, stable, lowercase kebab-case identifiers; native `name` and directory names must not use path traversal.

Native inspection and validation commands are `hermes skills list`, `hermes skills inspect <identifier>`, `hermes skills audit [name]`, and `hermes skills check [name]`. A session can explicitly preload skills with `--skills`.

## CORE NOW — design only

No custom skill is created by this architecture gate.

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

No deferred skill is created or installed by WP-004A.

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
