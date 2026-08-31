# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-007 — PROJECT REGISTRY PLANNING

STATUS:
WP-007 = PLANNING ONLY / EXPLICIT CONTROL PLANE AUTHORIZATION
WP-006 = COMPLETE / MERGED PR #22 (merge commit 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8)
WP-005B = COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)
WP-005C Runtime Inventory/Backup Design = COMPLETE / MERGED (merge commit 3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44)
WP-005C External Credential Recovery Verification = COMPLETE / MERGED (merge commit a7789317931894366dba8f8d3e4b04d659ee6d4f)
WP-005C Backup Execution/Manifest Validation = COMPLETE / PASS
PR #25 = OPEN / original head e094be4 preserved as pre-authorization evidence; current reconciled head a1e700b is authorized planning evidence pending standard merge gates

CURRENT PHASE:
Phase 7 — Project Registry = PLANNING ONLY

CURRENT PHASE DETAIL:
Phase 6 — Security Gates, Approvals, Audit Logging = COMPLETE
Issue #20 = state:completed
PR #22 = MERGED
MERGE_COMMIT = 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8
Issue #24 = state:ready / role:master
PR #25 = OPEN / original head e094be4 preserved as pre-authorization evidence; current reconciled head a1e700b is authorized planning evidence pending standard merge gates
WP-005C Restore / DR Rehearsal = DEFERRED

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

WORKING BRANCH:
ai/wp-007-project-registry-planning

TARGET:
develop

## Objective

Define the smallest complete Phase 7 Project Registry design required to satisfy:
"Registered-project lookup works." Planning only. No runtime implementation,
deployment, database, web UI, n8n/MCP/Kintone, or automation is authorized
in this phase.

## Authorization

This planning work is explicitly authorized by ChatGPT Control Plane on
2026-08-31. Issue #24 and the original PR #25 head `e094be4` were created
before authorization and are preserved as pre-authorization audit evidence
only. That original pre-authorization state does not constitute current
authorization. The reconciled current head `a1e700b` on branch
`ai/wp-007-project-registry-planning` is the authorized planning evidence
and may proceed only through the standard merge gates: Runtime REVIEWER
PASS -> Control Plane REVIEW_PASS -> explicit Project Owner approval -> merge.

## Scope

- Define one canonical Project Registry source in Git.
- Registry lookup fields: project_id, project_name, repository, canonical_branch,
  project_docs_path, status, control_plane, execution_role/model if applicable.
- Lookup behavior: project name/project id -> canonical registry record -> repository/project context.
- Registry must not contain secrets, tokens, passwords, private keys, credentials,
  or production connection strings.
- Git/repository truth remains authoritative. Chat memory, Telegram, Desktop, Skills,
  or Hermes memory must not silently override registry truth.
- Fail closed on unknown project, duplicate project_id, duplicate ambiguous project name,
  missing required field, or invalid repository/branch metadata.

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
- implementation code or runtime behavior

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

- Revert the planning branch or delete the branch if scope drifts.
- Repository changes can be reverted through Git.
- Existing valid backups must not be deleted.
- No runtime state is modified by this WP.

## Stop Conditions

Stop if:
- scope expands beyond approved Phase 7 planning;
- implementation code or runtime behavior is introduced;
- secrets or credentials are included in registry design;
- lookup behavior is defined as guessing or fallback to non-authoritative sources;
- n8n/MCP/Kintone/database/web UI is introduced;
- CHAT_HANDOFF resume behavior is broken;
- WP-005C backup semantics are altered;
- Hermes Desktop attempts Windows-local backend bootstrap/installation;
- A second Hermes/Orbis runtime becomes active on Windows;
- PR #25 is merged;
- planning PR is merged without Control Plane and Project Owner authorization.

## Next Step

Await explicit Control Plane review and Project Owner approval for this
planning PR only. Do not start implementation, Restore/DR, or any next WP
without separate explicit authorization.
