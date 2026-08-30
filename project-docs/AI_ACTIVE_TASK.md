# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-004B-CORE-SKILLS-REPOSITORY-IMPLEMENTATION

STATUS:
REVIEW_REQUESTED

CORE SKILL IMPLEMENTATION:
REPOSITORY DEFINITIONS CREATED

RUNTIME DEPLOYMENT:
NOT STARTED

CONTROL PLANE:
ChatGPT

EXECUTION PLANE:
Codex

CURRENT PHASE:
Phase 4 — Skills

OBJECTIVE:

Create the approved Core 5 skill definitions in repository `skills/` as Git/version-controlled source of truth only.

SCOPE:

- Create `SKILL.md` for `project-manager`, `code-development`, `code-review`, `git-governance`, and `security`.
- Update only the repository skill documentation and review handoff needed for WP-004B.

OUT OF SCOPE:

- Hermes runtime deployment, installation, synchronization, enablement, or project trust.
- Hermes profile, SOUL.md, gateway, Telegram, model, credential, or `.env` changes.
- Deferred skills, roadmap changes, automation, merge, and deployment.

ROLE MAPPING:

- MASTER: `project-manager`, `git-governance`, `security`.
- CODER: `code-development`, `git-governance`, `security`.
- REVIEWER: `code-review`, `git-governance`, `security`.

IMPLEMENTATION EVIDENCE:

- Five repository skill files created under `skills/`.
- No Hermes runtime or profile changes.
- No skill deployment, Telegram/gateway change, or model change.

TEST REQUIREMENTS:

- Validate all five front matters, unique names, directory-name match, and required contract headings.
- Verify required role-boundary text.
- Run `git diff --check`, changed-file inspection, and changed-file secret scan.

SECURITY REQUIREMENTS:

- No credential, token, `.env` value, Telegram ID, OAuth value, private key, personal runtime data, or invented tool/command.

BASE BRANCH:
develop

WORKING BRANCH:
ai/codex-wp-004b-core-skills

TARGET:
develop

ROLLBACK:

Revert the repository definition commit only. No runtime rollback is needed because no runtime change is authorized.

DELIVERABLES:

- Five Core `SKILL.md` repository definitions.
- Updated source-of-truth and architecture documentation.
- Independent-review handoff.

NEXT STEP:

Independent ChatGPT review. If approved and merged, prepare a separate deployment/validation Work Package; do not authorize deployment in WP-004B.

STOP CONDITIONS:

- Stop after commit, push, and review handoff.
- Do not deploy or modify Hermes runtime.
