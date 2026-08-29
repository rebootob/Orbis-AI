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

- After this gate is merged, execute the validation sequence on the owner's WSL2 host under ChatGPT guidance only.
- Codex must not access or modify WSL, local Hermes, runtime configuration, or credentials.

TEST REQUIREMENTS:

After this gate is merged, perform: `hermes profile list`; create blank `coder`; create blank `reviewer`; verify independent home/state; verify MASTER Telegram; verify coder/reviewer have no Telegram gateway credentials; test CODER and REVIEWER role boundaries; and verify `default` remains MASTER.

SECURITY REQUIREMENTS:

- No Telegram token/user ID, `.env` value, credential cloning, worker messaging-gateway credential, or secret in Git/review handoff.

BASE BRANCH:
develop

WORKING BRANCH:
ai/codex-wp-003-coder-evidence

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

- NOT TESTED — reviewer profile has not been created.

STOP CONDITIONS:

- Stop this Codex task after the CODER evidence is committed, pushed, and handed off for independent review.
- Do not create reviewer or modify runtime in this task.
