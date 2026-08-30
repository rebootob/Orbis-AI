# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-005C — IMPLEMENTATION — RUNTIME INVENTORY / BACKUP DESIGN

STATUS:
IMPLEMENTATION — RUNTIME INVENTORY / BACKUP DESIGN
WP-005B = COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)

CURRENT PHASE:
Phase 5 — Kanban & Handoff

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

WORKING BRANCH:
ai/wp-005c-runtime-inventory-backup-design

TARGET:
develop

## Objective

Document the current Hermes/Orbis runtime state and design the backup/restore
architecture for WP-005C without modifying runtime behavior, creating backups,
or starting migration.

Current approved implementation scope is limited to:
- Runtime Inventory
- Backup Design

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

## Scope

### Current WP-005C Scope

- Runtime Inventory: non-destructive discovery of host, installation, profiles,
  Core Skills, Git/GitHub, Telegram, Desktop/SSH, services, and non-Git state.
- Backup Design: architecture, manifest, integrity, restore order, retention,
  secret recovery separation, validation procedure, and completeness proof.

### WP-005C Scope Guard

The current approved implementation boundary ends at documentation.
Do not start:
- backup execution
- restore execution
- server migration
- cutover
- runtime modification
- secret rotation
- Windows Hermes backend installation
- PowerShell policy changes
- deployment

## Authority Model

- Runtime REVIEWER returns PASS/FAIL evidence only.
- Final repository `REVIEW_PASS` belongs to ChatGPT Control Plane.
- Merge requires explicit Project Owner approval.
- Level 3 actions require explicit Project Owner approval.
- Skills, labels, task comments, Desktop, and Telegram do not grant additional
  authority.

## Security

- Do not display, copy, commit, or transmit `.env`, tokens, passwords,
  credentials, private keys, OAuth secrets, Telegram IDs, or session secrets.
- Do not bind Hermes backend publicly without a separately approved security
  decision.
- Use local backups for runtime files.
- Do not enable additional worker gateways unless explicitly required and
  approved.
- ED25519 key-only authentication is enforced for SSH connections.

## Required Validation

- runtime inventory completeness
- repository/runtime Skill SHA256 equality
- Core Skill version matrix
- fresh-session role identity
- authority-negative tests
- Kanban/handoff behavior
- restart/resume behavior
- Desktop-to-WSL-runtime connection via SSH
- Telegram remains functional
- Desktop shutdown does not stop Orbis runtime
- secret-safe inspection
- repository diff check
- Windows duplicate runtime guard:
  - `WINDOWS_LOCAL_HERMES_BACKEND_RUNNING=NO`
  - `DUPLICATE_ACTIVE_ORBIS_RUNTIME=NO`
  - `WINDOWS_LOOPBACK_FORWARDING_MECHANISM=UNKNOWN`

STATUS: ALL COMPLETE / PASS for WP-005B.
WP-005C validation continues under current limited scope.

## WP-005B Summary

All blocks complete and merged into develop:

- B1: COMPLETE / PASS
- B2: COMPLETE / PASS
- B3: COMPLETE / PASS (Issues #12 closed)
- B4: COMPLETE / PASS (Issue #13 closed)

Merge commit: 5fe175efc4e4f9933299b14151919709c69769b3

## Rollback

- Preserve existing SOUL/profile/config files unless a separately identified
  change is required.
- Stop any expansion beyond Runtime Inventory / Backup Design and return to
  approved Phase 5 architecture if scope drifts.
- Repository changes can be reverted through Git.

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
- backup execution
- restore execution
- server migration
- cutover
- changing approved Phase 5 architecture unless required by migration

## Stop Conditions

Stop if:
- runtime inventory is incomplete;
- backup design is incomplete;
- restore procedure requires chat history;
- secrets may be exposed;
- new server validation is reached;
- old server must be deleted before acceptance;
- rollback path is unavailable or untested;
- GitHub task state/evidence becomes inconsistent;
- a Level 3 action is reached without explicit Project Owner approval;
- scope expands beyond WP-005C Runtime Inventory / Backup Design;
- Hermes Desktop attempts Windows-local backend bootstrap/installation.
- A second Hermes/Orbis runtime becomes active on Windows.
- `WINDOWS_LOCAL_HERMES_BACKEND_RUNNING=YES` or `DUPLICATE_ACTIVE_ORBIS_RUNTIME=YES`.

## Recovery Readiness

- Secure credential recovery inventory is documented.
- Recovery readiness remains FAIL until Project Owner confirms the documented
  secure recovery sources exist and are accessible.
- Do not treat documentation alone as proof of recoverability.

## Next Step

Complete Project Owner review of:
- runtime inventory
- backup design
- credential recovery sources

Only after approval proceed to backup execution, migration validation, or cutover planning.

Do not expand scope beyond Runtime Inventory / Backup Design without explicit approval.
