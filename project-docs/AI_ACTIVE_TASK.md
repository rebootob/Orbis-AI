# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-006 — SECURITY GATES, APPROVALS, AND AUDIT LOGGING

STATUS:
WP-006 = COMPLETE / MERGED PR #22 (merge commit 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8)
WP-005B = COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)
WP-005C Runtime Inventory/Backup Design = COMPLETE / MERGED (merge commit 3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44)
WP-005C External Credential Recovery Verification = COMPLETE / MERGED (merge commit a7789317931894366dba8f8d3e4b04d659ee6d4f)
WP-005C Backup Execution/Manifest Validation = COMPLETE / PASS
WP-007 = PAUSED / AWAITING CONTROL PLANE AUTHORIZATION

CURRENT PHASE:
Phase 6/7 — Governance Recovery and WP-007 Pause

CURRENT PHASE DETAIL:
Phase 6 — Security Gates, Approvals, Audit Logging = COMPLETE
Issue #20 = state:completed
PR #22 = MERGED
MERGE_COMMIT = 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8
WP-005C Restore / DR Rehearsal = DEFERRED
WP-007 = PAUSED / AWAITING CONTROL PLANE AUTHORIZATION

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

WORKING BRANCH:
ai/wp-006-security-gates-implementation

TARGET:
develop

## Objective

Restore canonical governance merge/approval gates and pause WP-007 without deleting existing evidence.

## Scope

- Record governance incident INCIDENT-2026-08-31-WP006.
- Harden Control Plane review gate in canonical policy docs.
- Harden Project Owner merge gate in canonical policy docs.
- Block next-WP autostart in canonical policy docs.
- Preserve WP-007 Issue #24 and PR #25 as unauthorized-start evidence.
- Update active task state to recovery/paused.

## Out of Scope

- Runtime code changes outside approved docs scope
- n8n/MCP/Kintone implementation or deployment
- Deployment or production changes
- Secret rotation or credential changes
- Restore, migration, cutover, or DR rehearsal
- WP-005D or later work
- Force push
- Unrelated refactoring

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

- Do not display, copy, commit, or transmit `.env`, tokens, passwords, credentials, private keys, OAuth secrets, Telegram IDs, or session secrets.
- Do not bind Hermes backend publicly without a separately approved security decision.
- Use local backups for runtime files.
- Do not enable additional worker gateways unless explicitly required and approved.
- ED25519 key-only authentication is enforced for SSH connections.

## WP-005B Summary

All blocks complete and merged into develop:

- B1: COMPLETE / PASS
- B2: COMPLETE / PASS
- B3: COMPLETE / PASS (Issues #12 closed)
- B4: COMPLETE / PASS (Issue #13 closed)

Merge commit: 5fe175efc4e4f9933299b14151919709c69769b3

## Rollback

- Revert the recovery branch or delete the branch if scope drifts.
- Repository changes can be reverted through Git.
- Existing valid backups must not be deleted.
- No runtime state is modified by this WP.

## Out of Scope

- n8n/MCP
- Kintone
- Project Registry
- Cron/background automation additions
- additional agents
- additional Telegram gateways
- model changes
- custom Kanban UI/database
- production deployment automation
- broad LAN/Internet exposure of Hermes backend
- WP-005D or later work packages
- restore execution
- server migration
- cutover
- credential reissue/rotation
- changing approved Phase 6 architecture unless required by migration

## Stop Conditions

Stop if:
- scope expands beyond approved WP-006 governance recovery scope;
- secrets are required or exposed;
- runtime files outside approved docs scope are modified;
- approval language becomes ambiguous or enables bypass;
- a Level 3 action is reached without explicit Project Owner approval;
- restore, migration, cutover, or DR rehearsal is started;
- n8n/MCP/Kintone or automation is started;
- CHAT_HANDOFF resume behavior is broken;
- WP-005C backup semantics are altered;
- Hermes Desktop attempts Windows-local backend bootstrap/installation;
- A second Hermes/Orbis runtime becomes active on Windows;
- WP-007 implementation continues;
- PR #25 is merged;
- recovery PR is merged without Control Plane and Project Owner authorization.

## Next Step

Await explicit Control Plane instruction after recovery PR review/approval.
