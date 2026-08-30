# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-004A-HERMES-SKILL-DISCOVERY-AND-DESIGN-GATE

STATUS:
IN_PROGRESS — DISCOVERY

CONTROL PLANE:
ChatGPT

EXECUTION PLANE:
Codex

CURRENT PHASE:
Phase 4 — Skills

OBJECTIVE:

Determine the native Hermes skill format, loading behavior, naming rules, and profile behavior before any custom Orbis skill is created.

WHY:

Use verified native Hermes behavior to design a minimal, role-appropriate initial Orbis skill set without creating or installing skills prematurely.

SCOPE:

- Read-only Hermes skill discovery.
- Document the native skill architecture and the recommended Core 5 design.
- Prepare this discovery/design gate for independent review.

OUT OF SCOPE:

- Creating, installing, copying, deleting, or configuring Hermes skills.
- Runtime, profile, SOUL.md, gateway, Telegram, credential, model, or `.env` changes.
- n8n, Kintone, project-specific skills, and all Phase 4 execution.

EXPECTED COMPONENTS:

- Native Hermes `SKILL.md` contract and skill locations.
- Core 5 design: `project-manager`, `code-development`, `code-review`, `git-governance`, and `security`.

REQUIRED CONTEXT:

- `AGENTS.md`
- `project-docs/AI_CONTROL_PLANE.md`
- `project-docs/02_IMPLEMENTATION_ROADMAP.md`
- `project-docs/07_SKILL_ARCHITECTURE.md`
- `skills/README.md`

VERIFIED NATIVE HERMES SKILL ARCHITECTURE:

- Required entry file: `SKILL.md` in a skill directory; optional `references/`, `templates/`, `assets/`, and supporting files may accompany it.
- `SKILL.md` uses YAML front matter. `name` is required (maximum 64 characters); `description` is required (maximum 1024 characters). Optional native fields include `version`, `license`, `platforms`, `prerequisites`, `compatibility`, and `metadata`.
- Active skills resolve from the active profile's `HERMES_HOME/skills`. Observed locations are `/home/allday/.hermes/skills` for default/MASTER and `/home/allday/.hermes/profiles/{coder,reviewer}/skills` for worker profiles.
- Bundled skills are seeded into the active profile skill directory. The current default, coder, and reviewer profiles each expose the same 77 enabled built-in skills; no hub or local skills are installed.
- Trusted project-local skill directories are discovered first, then active-profile skills, then configured external skill directories. Project-local skills take precedence over same-named lower-tier skills; non-project duplicate candidates are reported as an ambiguity rather than silently selected.
- Native discovery/loading tools: `hermes skills list`, `hermes skills inspect`, `hermes skills audit`, `hermes skills check`, and explicit session preload via `--skills`.

NAMING COLLISIONS:

- No exact installed-name collision was found for `project-manager`, `code-development`, `code-review`, `git-governance`, or `security`.
- Related built-ins `github-code-review` and `requesting-code-review` exist; `code-review` must therefore remain narrowly scoped to the Orbis REVIEWER governance contract.

RECOMMENDED CORE 5 DESIGN:

- `project-manager` — MASTER task decomposition, status, and handoff preparation.
- `code-development` — CODER approved implementation, tests, and handoff preparation.
- `code-review` — REVIEWER diff, regression, security, and test review with explicit PASS or FAIL.
- `git-governance` — branch, commit, Pull Request, rollback, and audit constraints for all roles.
- `security` — secret handling, permission ceilings, approval gates, and escalation rules for all roles.

IMPLEMENTATION INSTRUCTIONS:

- Runtime modification is NOT AUTHORIZED.
- Record non-secret discovery evidence and architecture only.
- Do not create actual skill implementations in this work package.

TEST REQUIREMENTS:

- Run `git diff --check`.
- Confirm the changed-file list is limited to this work package.
- Run a changed-file secret-safety scan.

SECURITY REQUIREMENTS:

- Do not record credentials, tokens, `.env` values, Telegram IDs, OAuth data, or runtime secrets.
- Read-only runtime inspection only.

BASE BRANCH:
develop

WORKING BRANCH:
ai/codex-wp-004a-skill-discovery

TARGET:
develop

ROLLBACK:

Revert the documentation changes only. No runtime rollback is necessary because no runtime modification is authorized.

DELIVERABLES:

- Verified native Hermes skill discovery record.
- Core 5 skill architecture and required contract.
- Independent-review handoff.

NEXT STEP:

After independent review and explicit authorization, prepare a separate work package to define the first custom Orbis skill. Do not execute that step here.

STOP CONDITIONS:

- Stop after documentation is committed, pushed, and handed off for independent review.
- Do not create, install, or modify any Hermes skill or runtime component.
