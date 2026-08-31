# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-007 — PROJECT REGISTRY IMPLEMENTATION

STATUS:
WP-007 = IMPLEMENTATION AUTHORIZED
WP-007 Planning = COMPLETE / MERGED PR #25 (merge commit d2aa184957dfa4b68087c6c708ec28cc84e5937d)
WP-006 = COMPLETE / MERGED PR #22 (merge commit 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8)
WP-005B = COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)
WP-005C Runtime Inventory/Backup Design = COMPLETE / MERGED (merge commit 3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44)
WP-005C External Credential Recovery Verification = COMPLETE / MERGED (merge commit a7789317931894366dba8f8d3e4b04d659ee6d4f)
WP-005C Backup Execution/Manifest Validation = COMPLETE / PASS

CURRENT PHASE:
Phase 7 — Project Registry = IMPLEMENTATION

CURRENT PHASE DETAIL:
Phase 6 — Security Gates, Approvals, Audit Logging = COMPLETE
Issue #20 = state:completed
PR #22 = MERGED
MERGE_COMMIT = 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8
Issue #24 = state:in-progress / role:coder
PR #25 = MERGED
MERGE_COMMIT = d2aa184957dfa4b68087c6c708ec28cc84e5937d
WP-005C Restore / DR Rehearsal = DEFERRED

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

WORKING BRANCH:
ai/wp-007-project-registry-implementation

TARGET:
develop

## Objective

Implement the approved Phase 7 Project Registry so registered-project lookup
works. This is the implementation phase. No database, web UI, n8n/MCP/Kintone,
automation/cron, new agents, or broad skill changes are authorized.

## Authorization

This implementation is explicitly authorized by ChatGPT Control Plane on
2026-08-31. WP-007 planning PR #25 is merged (merge commit
d2aa184957dfa4b68087c6c708ec28cc84e5937d). Implementation may proceed only
on branch `ai/wp-007-project-registry-implementation` and only after Runtime
REVIEWER PASS, Control Plane REVIEW_PASS, and explicit Project Owner approval.

## Scope

- Implement one canonical Project Registry source in Git.
- Deterministic lookup by project_id and project_name.
- Required fields: project_id, project_name, repository, canonical_branch,
  project_docs_path, status, control_plane, execution_role/model if applicable.
- Fail closed on unknown project, duplicate project_id, ambiguous duplicate
  project_name, missing required field, or invalid repository/branch metadata.
- Git/repository truth remains authoritative. No secrets or credentials in registry.
- Add focused tests for valid lookup, fail-closed cases, and secret exclusion.

## Out of Scope

- database
- web UI
- custom Kanban
- n8n/MCP/Kintone
- project-specific integrations
- runtime deployment
- cron/automation
- Restore/DR
- server migration
- new agents
- broad skill changes
- Phase 8 or later work

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

- Do not display, copy, commit, or transmit `.env`, tokens, passwords,
  credentials, private keys, OAuth secrets, Telegram IDs, or session secrets.
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

- Revert the implementation branch or delete the branch if scope drifts.
- Repository changes can be reverted through Git.
- Existing valid backups must not be deleted.
- No runtime state is modified by this WP.

## Stop Conditions

Stop if:
- scope expands beyond approved Phase 7 implementation;
- secrets are required or exposed;
- runtime files outside approved docs/scripts scope are modified;
- approval language becomes ambiguous or enables bypass;
- a Level 3 action is reached without explicit Project Owner approval;
- restore, migration, cutover, or DR rehearsal is started;
- n8n/MCP/Kintone or automation is started;
- CHAT_HANDOFF resume behavior is broken;
- WP-005C backup semantics are altered;
- Hermes Desktop attempts Windows-local backend bootstrap/installation;
- A second Hermes/Orbis runtime becomes active on Windows;
- implementation PR is merged without Control Plane and Project Owner authorization.

## Next Step

Await explicit Control Plane review and Project Owner approval for this
implementation PR only. Do not start Phase 8, Restore/DR, or any next WP
without separate explicit authorization.
