# WP-008A — ChatGPT ↔ Hermes Control Plane Bridge

STATUS: PLANNING + MINIMUM SAFE PROTOTYPE
TASK_ID: 28
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

Architecture:

```
ChatGPT Control Plane
-> authenticated task bridge
-> existing WSL2 Hermes MASTER
-> CODER / REVIEWER when required
-> structured evidence/result
-> ChatGPT Control Plane
```

## Security Model

- authenticated requests only
- explicit permission/approval gates
- no approval inference from ChatGPT/GitHub/Telegram/Hermes Desktop identity
- Level 3 operations blocked without explicit Project Owner approval
- secrets must remain outside Git
- audit all bridge task submissions/results
- fail closed on unknown/ambiguous action

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
  "approval_evidence": "Owner authorization comment URL or explicit approval reference",
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

## Approval Enforcement

- Level 0/1/2: Control Plane may autonomously issue after review
- Level 3: STOP and return OWNER_APPROVAL_REQUIRED
- Fail-closed on unknown permission_level

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

Local-only by default.
No public inbound exposure.
No LAN exposure unless explicitly authorized.

## Authentication

Reuse existing Hermes runtime authentication.
Bridge requests must carry explicit approval_evidence.
No anonymous task submission.

## Audit Mechanism

Every task submission and result is recorded with:
- task_id
- timestamp
- requested_action
- permission_level
- status
- result/evidence
- failure_reason if any

## Test Evidence Location

`project-docs/WP-008A_TEST_EVIDENCE.md`

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
