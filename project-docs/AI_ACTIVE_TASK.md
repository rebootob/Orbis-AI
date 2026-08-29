# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-003-HERMES-ROLE-PROFILES

STATUS:
REVIEW_REQUESTED

CONTROL PLANE:
ChatGPT

EXECUTION PLANE:
Codex

CURRENT PHASE:
Phase 3 — MASTER / CODER / REVIEWER Profiles

OBJECTIVE:

Define and validate three isolated Hermes roles: MASTER, CODER, REVIEWER.

WHY:

Establish role boundaries before any agent delegation or orchestration is introduced.

SCOPE:

- Prepare the WP-003 role-profile contract and review metadata only.
- Preserve MASTER as the default/main Hermes profile and define separate `coder` and `reviewer` profiles for future execution after approval.

OUT OF SCOPE:

- Creating Hermes profiles or modifying runtime configuration.
- Hermes, Telegram, WSL, model, credential, or secret changes.
- Agent-to-agent automation, Kanban orchestration, n8n, MCP, Kintone, application implementation, and production changes.

EXPECTED COMPONENTS:

- Default/main Hermes profile as future MASTER.
- Future isolated `coder` and `reviewer` profiles.
- MASTER-only Telegram Gateway.

REQUIRED CONTEXT:

- `AGENTS.md`
- `project-docs/AI_CONTROL_PLANE.md`
- `project-docs/03_AGENT_ROLES.md`
- `project-docs/04_SECURITY_POLICY.md`
- `project-docs/05_APPROVAL_POLICY.md`

IMPLEMENTATION INSTRUCTIONS:

- This Pull Request is preparation only.
- Do not begin Phase 3 execution until independent review passes, the Pull Request is merged, and a subsequent Active Task authorizes execution.
- CODER and REVIEWER must not receive Telegram gateway credentials.
- No agent-to-agent automation, Kanban orchestration, n8n, MCP, or Kintone work is authorized.

TEST REQUIREMENTS:

- Validate this documentation contract and changed-file secret scan only.
- Phase 3 role-boundary validation is deferred until explicit execution authorization.

SECURITY REQUIREMENTS:

- Do not record or duplicate Telegram credentials, user IDs, tokens, OAuth data, `.env` values, or runtime secrets.
- Worker profiles must remain isolated and must not receive Telegram gateway credentials when Phase 3 is authorized.

BASE BRANCH:
develop

WORKING BRANCH:
ai/codex-wp-003-prep

TARGET:
develop

ROLLBACK:

Close this Pull Request without merging, or revert its documentation commits. No runtime state is changed.

DELIVERABLES:

- Complete WP-003 preparation contract.
- Updated review handoff for independent review.
- Explicit Phase 1–2 runtime baseline documentation.

STOP CONDITIONS:

- Stop after this Pull Request is prepared for independent review.
- Do not create Hermes profiles, modify runtime, or begin Phase 3 execution.
