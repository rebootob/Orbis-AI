# ORBIS AI — ACTIVE TASK

WORK PACKAGE:
WP-003-HERMES-ROLE-PROFILES

STATUS:
READY_FOR_CODEX

CURRENT PHASE:
Phase 3 — MASTER / CODER / REVIEWER Profiles

OBJECTIVE:

Define and validate three isolated Hermes roles: MASTER, CODER, REVIEWER.

ARCHITECTURE:

- Default/main Hermes profile acts as MASTER.
- Create separate `coder` and `reviewer` profiles.
- Telegram Gateway remains MASTER-only.
- CODER and REVIEWER must NOT have Telegram gateway credentials.
- No agent-to-agent automation yet.
- No Kanban orchestration yet.
- No n8n / MCP / Kintone yet.

ACCEPTANCE:

- MASTER role boundary validated.
- CODER role boundary validated.
- REVIEWER role boundary validated.
- CODER cannot self-approve.
- REVIEWER reviews only and does not silently modify work.
- Profile state is isolated.
- No duplicate Telegram credentials in worker profiles.
