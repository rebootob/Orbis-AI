# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-004A-HERMES-SKILL-DISCOVERY-AND-DESIGN-GATE

STATUS:
IN_PROGRESS — DISCOVERY

CORE SKILL IMPLEMENTATION:
NOT STARTED

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

- Runtime identity (read-only): Hermes Agent `v0.20.6` (2026.8.27); source checkout `1c5ee5815fe5a3913530ba9d803b5b60bc633766`.
- Required entry file: `SKILL.md` in a skill directory; optional `references/`, `templates/`, `assets/`, and supporting files may accompany it.
- `SKILL.md` uses YAML front matter. `name` is required (maximum 64 characters); `description` is required (maximum 1024 characters). Optional native fields include `version`, `license`, `platforms`, `prerequisites`, `compatibility`, and `metadata`.
- Active skills resolve from the active profile's `HERMES_HOME/skills`. Observed locations are `/home/allday/.hermes/skills` for default/MASTER and `/home/allday/.hermes/profiles/{coder,reviewer}/skills` for worker profiles.
- Bundled skills are seeded into the active profile skill directory. The current default, coder, and reviewer profiles each expose the same 77 enabled built-in skills; no hub or local skills are installed.
- Project-local locations are `<project-root>/.hermes/skills/` and `<project-root>/.agents/skills/`; discovery requires `hermes skills trust` and uses `skills.trusted_project_dirs`.
- Precedence is project-local → profile-local → external. Project-local skills take precedence over same-named lower-tier skills; non-project duplicate candidates are reported as an ambiguity rather than silently selected.
- Native command semantics: `hermes skills inspect` previews a candidate before installation; `hermes skills check` checks installed hub skills for upstream updates; `hermes skills audit` re-scans installed hub skills. These are not generic local custom-skill validators.
- Native discovery/loading tools include `hermes skills list` and explicit session preload via `--skills`.

NAMING COLLISIONS:

- No exact installed-name collision was found for `project-manager`, `code-development`, `code-review`, `git-governance`, or `security`.
- Related built-ins `github-code-review` and `requesting-code-review` exist; `code-review` must therefore remain narrowly scoped to the Orbis REVIEWER governance contract.

RECOMMENDED CORE 5 DESIGN:

- `project-manager` — MASTER task decomposition, status, and handoff preparation.
- `code-development` — CODER approved implementation, tests, and handoff preparation.
- `code-review` — REVIEWER diff, regression, security, and test review with explicit PASS or FAIL.
- `git-governance` — branch, commit, Pull Request, rollback, and audit constraints for all roles.
- `security` — secret handling, permission ceilings, approval gates, and escalation rules for all roles.

SOURCE OF TRUTH AND FUTURE RUNTIME MAPPING:

- Repository `skills/` is the Git/version-controlled source of truth. It is not assumed to be automatically discovered by Hermes.
- A separately authorized future deployment will place or synchronize approved skills into the applicable profile's `HERMES_HOME/skills` directory.
- MASTER: `project-manager`, `git-governance`, `security`.
- CODER: `code-development`, `git-governance`, `security`.
- REVIEWER: `code-review`, `git-governance`, `security`.
- This profile mapping keeps Core governance skills available across registered projects, rather than only when Hermes runs inside the Orbis repository.

FUTURE LOCAL-SKILL VERIFICATION (NOT EXECUTED IN WP-004A):

- Validate the required `SKILL.md` and front matter after a custom skill is created in a separately authorized work package.
- Verify with `hermes -p <profile> skills list --enabled-only` and confirm expected profile visibility.
- Start a fresh session with explicit `--skills <skill-name>`, run a behavioral test, and run a role-boundary negative test where applicable.

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
