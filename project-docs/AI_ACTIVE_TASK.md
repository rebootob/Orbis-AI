# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-008 — N8N VIA MCP PLANNING

STATUS:
WP-008 = PLANNING AUTHORIZED
WP-007 = COMPLETE / MERGED PR #27 (merge commit 6ed9a3ef1c2b7d0eed95728150315ccf7a9e3ccb)
WP-006 = COMPLETE / MERGED PR #22 (merge commit 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8)
WP-005B = COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)
WP-005C Runtime Inventory/Backup Design = COMPLETE / MERGED (merge commit 3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44)
WP-005C External Credential Recovery Verification = COMPLETE / MERGED (merge commit a7789317931894366dba8f8d3e4b04d659ee6d4f)
WP-005C Backup Execution/Manifest Validation = COMPLETE / PASS

CURRENT PHASE:
Phase 8 — n8n via MCP = PLANNING

CURRENT PHASE DETAIL:
Phase 7 — Project Registry = COMPLETE
Issue #24 = state:runtime-review / role:control-plane
PR #27 = MERGED
MERGE_COMMIT = 6ed9a3ef1c2b7d0eed95728150315ccf7a9e3ccb
Phase 6 — Security Gates, Approvals, Audit Logging = COMPLETE
Issue #20 = state:completed
PR #22 = MERGED
MERGE_COMMIT = 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8
WP-005C Restore / DR Rehearsal = DEFERRED

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

WORKING BRANCH:
ai/wp-008-n8n-via-mcp-planning

TARGET:
develop

## Objective

Plan the minimum safe n8n via MCP integration with read-only validation before any write capability is considered.

## Authorization

This planning phase is explicitly authorized by ChatGPT Control Plane on 2026-08-31. WP-008 planning may proceed only on branch `ai/wp-008-n8n-via-mcp-planning` and only after Runtime REVIEWER PASS, Control Plane REVIEW_PASS, and explicit Project Owner approval.

## Scope

- Define connection architecture: Hermes/Orbis -> MCP -> n8n.
- Identify MCP server/client responsibility.
- Define minimum read-only capability set: list workflows, read metadata, inspect status, inspect executions.
- Define write gate: all writes disabled/not authorized until explicit future authorization.
- Define security requirements: no secrets in Git, least privilege, fail closed on ambiguity.
- Define environment separation requirements: local/dev/test vs production.
- Define required evidence for future implementation.
- Define governance and approval requirements for future implementation.

## Out of Scope

- actual n8n write operations
- workflow creation/editing
- workflow execution with side effects
- Kintone integration
- cron/automation
- production deployment
- credential rotation
- Restore/DR
- server migration/cutover
- new agents
- broad skill refactor
- Phase 9+

## Runtime Architecture

- WSL2 Hermes = primary Orbis runtime.
- MASTER = default Hermes profile.
- CODER = `coder` Hermes profile.
- REVIEWER = `reviewer` Hermes profile.
- Telegram = remote command interface.
- Hermes Desktop = optional operator console connected via SSH.
- GitHub Issues = canonical task/Kanban source of truth.
- GitHub/Git = implementation and audit evidence.

Hermes Desktop connects to the approved WSL2 Hermes backend via SSH:

Windows Hermes Desktop UI
-> Connect via SSH
-> allday@127.0.0.1:2222
-> existing WSL2 Hermes / Orbis runtime

Authentication:
ED25519 key-only.

No second Orbis runtime exists or is created on Windows.
Windows local Hermes backend = NO.
Telegram remains independently operational.

## Authority Model

- Runtime REVIEWER returns PASS/FAIL evidence only.
- Final repository `REVIEW_PASS` belongs to ChatGPT Control Plane.
- Merge requires explicit Project Owner approval for the exact PR and head SHA.
- Level 3 actions require explicit Project Owner approval.
- Skills, labels, task comments, Desktop, and Telegram do not grant additional authority.

## Security

- Follow project-docs/04_SECURITY_POLICY.md.
- Follow project-docs/05_APPROVAL_POLICY.md.
- Do not expose secrets/credentials in docs, issues, comments, or code.
- No mutable current HEAD SHAs in tracked docs; GitHub PR metadata is authoritative.
- Preserve audit evidence; distinguish pre-authorization state from authorized state.

## Next Step

Await explicit Control Plane instruction after planning PR review/approval.
