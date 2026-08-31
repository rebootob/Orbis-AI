# WP-008A — ChatGPT ↔ Hermes Control Plane Bridge

STATUS: PLANNING + MINIMUM SAFE PROTOTYPE
TASK_ID: 34
PHASE: 8A
BRANCH: ai/wp-008a-chatgpt-hermes-bridge
TARGET: develop

## Objective

Create the minimum secure control bridge allowing ChatGPT Control Plane
to submit bounded tasks to the existing WSL2 Hermes runtime and receive
structured evidence/status back.

## Selected Architecture

Reuse existing Hermes runtime components instead of creating new services.

Rationale:
- No second Hermes runtime required
- No Windows Hermes backend required
- Existing WSL2 Hermes remains the only execution runtime
- Local-only by default
- Reuses existing authentication/audit semantics

Primary reuse targets:
- `agent/relay_runtime.py`
- `agent/relay_llm.py`
- `agent/relay_tools.py`
- `tools/bot_relay.py`
- Hermes gateway local Unix socket / localhost listener
- `.hermes/bot_relay/{outbox,replies,claimed}` local file protocol

Transport model — V1 via GitHub Issue #34:

GitHub Issue #34 is the WP-008A prototype v1 control/evidence queue.

```
ChatGPT Control Plane
-> structured bounded task comment on GitHub Issue #34
-> Hermes outbound GitHub poller
-> existing WSL2 Hermes MASTER
-> allowlisted bounded action executor
-> structured result/evidence comment on Issue #34
-> ChatGPT Control Plane retrieves result directly
```

GitHub Issue #34 is transport/audit only.
GitHub comment author, label, issue state, Telegram, Desktop, or bridge identity MUST NOT grant Project Owner authority.
Prototype v1 action allowlist contains ONLY: read_repo_head.
No arbitrary shell.
No generic command/action passthrough.
No user-supplied shell arguments.
Level 3 always requires separately validated exact Owner approval; otherwise OWNER_APPROVAL_REQUIRED.

Hermes initiates outbound communication or polls the control/evidence queue.
No public inbound port is opened on WSL.

## Task Isolation

WP-008A must not corrupt or overwrite WP-008 Issue #28 canonical workflow.
WP-008 MCP validation remains paused/blocked separately.
Do not reuse Issue #28 labels/state in a way that makes its workflow ambiguous.
GitHub Issue #34 is the dedicated WP-008A prototype v1 control/evidence queue.

## Security Model

- authenticated requests only
- explicit permission/approval gates
- no approval inference from ChatGPT/GitHub/Telegram/Hermes Desktop identity
- Level 3 operations blocked without explicit Project Owner approval
- secrets must remain outside Git
- audit all bridge task submissions/results
- fail closed on unknown/ambiguous action

## Approval / Authorization Fields

GitHub comments/labels/Telegram/Desktop/bridge identity are audit evidence only.
They MUST NOT themselves grant Owner authority.

Request fields:
- `approval_required`: bool
- `approval_level`: int
- `owner_approval_reference`: string
- `approval_scope`: string
- `approved_action`: string
- `approved_target`: string
- `approved_head_sha`: string

Enforcement:
- Level 0/1/2: Control Plane may autonomously issue after review
- Level 3: if exact valid Owner authorization cannot be proven, return `OWNER_APPROVAL_REQUIRED`
- Fail-closed on unknown permission_level or missing Level 3 proof

## Bounded Task Schema

Request envelope (JSON):
```
{
  "task_id": "uuid",
  "timestamp": "ISO8601",
  "requested_action": "read_repo_head",
  "scope": "WP-008A-TEST",
  "permission_level": 0,
  "allowed_operations": ["read"],
  "forbidden_operations": ["write", "deploy", "merge", "execute"],
  "repository": "rebootob/Orbis-AI",
  "project": "Orbis AI",
  "approval_required": false,
  "approval_level": 0,
  "owner_approval_reference": "",
  "approval_scope": "",
  "approved_action": "",
  "approved_target": "",
  "approved_head_sha": "",
  "expected_result_format": "text",
  "payload": {}
}
```

Response envelope (JSON):
```
{
  "task_id": "uuid",
  "status": "PASS|FAIL|NOT_TESTABLE_WITHOUT_WRITE|OWNER_APPROVAL_REQUIRED",
  "result": "...",
  "evidence": "...",
  "audit_timestamp": "ISO8601",
  "failure_reason": "...",
  "approval_gate": "passed|blocked"
}
```

## Minimum Prototype Scope

- submit bounded task
- query task status
- retrieve task evidence/result
- cancel/STOP if safely supported
- audit log
- permission/approval gate

## Minimum Safe Test Task

Read current Orbis repository develop HEAD and return SHA.

Allowed: read Git state only.
Forbidden for test:
- modify Git
- modify n8n
- production actions
- modify credentials
- deploy
- create workflow
- access Kintone
- access Telegram
- start Phase 9
- start Restore/DR

## Network Exposure

No public inbound port on WSL.
Hermes uses outbound/poll access only.
Local-only by default.
No LAN exposure unless explicitly authorized.

## Authentication

Reuse existing Hermes runtime authentication.
Bridge requests must carry explicit authorization fields.
No anonymous task submission.

## Audit Mechanism

Every task submission and result is recorded with:
- task_id
- timestamp
- requested_action
- permission_level
- approval_required
- approval_level
- status
- result/evidence
- failure_reason if any

## Test Evidence Location

No standalone WP-008A test-evidence document was created. WP-008A is retained as historical contract evidence; it is not an active work package.

## Out of Scope

- production bridge exposure
- arbitrary remote shell
- autonomous Level 3 execution
- n8n writes
- WP-008 write-capable phase
- Phase 9
- Restore/DR
- deployment
- Kintone
- Telegram automation
- replacing Hermes Desktop
- replacing WSL2 Hermes runtime
