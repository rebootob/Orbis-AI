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

Create and validate three isolated Hermes roles on the established WSL2 Ubuntu runtime.

WHY:

Establish isolated role boundaries before agent-to-agent automation, Kanban, MCP, n8n, or project execution is introduced.

SCOPE:

- Default Hermes profile remains MASTER.
- Create blank Hermes profile `coder`.
- Create blank Hermes profile `reviewer`.
- Define MASTER, CODER, REVIEWER role boundaries.
- Validate profile isolation and role behavior.
- Verify Telegram remains MASTER-only.
- Record validation evidence.

IMPORTANT EXECUTION DESIGN:

- Never use `--clone` or `--clone-all`.
- Do not copy MASTER `.env`, Telegram credentials, or other secrets.
- Do not install coder/reviewer gateways or enable multiplex profile gateway.
- Only MASTER/default gateway may remain active.
- Runtime commands are performed interactively on the owner's WSL2 host under ChatGPT guidance; Codex repository work is limited to governance/evidence recording.

OUT OF SCOPE:

- Agent-to-agent automation, Kanban, n8n, MCP, Kintone, Project Registry, production automation, additional Telegram bots, additional gateways, changing the current MASTER model, and Hermes upgrade.

EXPECTED COMPONENTS:

- `default` = MASTER
- `coder` = CODER
- `reviewer` = REVIEWER

REQUIRED CONTEXT:

- `AGENTS.md`
- `project-docs/AI_CONTROL_PLANE.md`
- `project-docs/03_AGENT_ROLES.md`

IMPLEMENTATION INSTRUCTIONS:

- Record only verified, non-secret runtime evidence from the owner-authorized Phase 3 profile work.
- Do not create additional profiles or modify MASTER/default, coder, gateways, credentials, or runtime configuration.

TEST REQUIREMENTS:

Record only tests actually performed: `hermes profile list`; independent profile-state checks; worker gateway-state checks; absence of reviewer Telegram/gateway configuration; CODER and REVIEWER role-boundary tests; and verification that `default` remains MASTER.

SECURITY REQUIREMENTS:

- No Telegram token/user ID, `.env` value, credential cloning, worker messaging-gateway credential, or secret in Git/review handoff.

BASE BRANCH:
develop

WORKING BRANCH:
ai/codex-wp-003-reviewer-evidence

TARGET:
develop

ROLLBACK:

If Phase 3 validation fails, delete only the newly created `coder` and `reviewer` profiles. Do not touch the default MASTER profile.

DELIVERABLES:

- Approved WP-003 execution gate.
- Validation evidence recorded after interactive runtime work.

CODER VALIDATION EVIDENCE:

- Profile path: `/home/allday/.hermes/profiles/coder`
- Configured model: `stepfun/step-3.7-flash:free`
- Coder setup: PASS
- Profile isolation: PASS
- Coder gateway: not running
- Default MASTER gateway: running
- `ORBIS-CODER-OK` test: PASS
- Blocker: NONE

REVIEWER STATUS:

REVIEWER VALIDATION EVIDENCE:

- Reviewer setup: PASS
- Profile path: `/home/allday/.hermes/profiles/reviewer`
- Configured model: `stepfun/step-3.7-flash:free`
- Profile isolation: PASS
- Reviewer gateway: not running
- Coder gateway: not running
- Default MASTER gateway: running
- Telegram/gateway configuration in reviewer: not found
- REVIEWER role-boundary test: PASS — reviewer refused to directly repair code and stated that it reviews and reports findings only.
- `ORBIS-REVIEWER-OK` test: PASS
- Blocker: NONE

STOP CONDITIONS:

- Stop this Codex task after the reviewer evidence is committed, pushed, and handed off for independent review.
- Do not create additional profiles or modify runtime further in this task.
