# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-005C — IMPLEMENTATION — EXTERNAL CREDENTIAL RECOVERY VERIFICATION

STATUS:
IMPLEMENTATION — EXTERNAL CREDENTIAL RECOVERY VERIFICATION
WP-005B = COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)
WP-005C Runtime Inventory/Backup Design = COMPLETE / MERGED (merge commit 3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44)

CURRENT PHASE:
Phase 5 — External Credential Recovery Verification

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

- External Credential Recovery Verification: safely verify external disaster-recovery paths for:
  - GitHub authentication
  - Telegram bot authentication
  - Hermes-required API credentials
  - SSH private key / Desktop SSH access

### WP-005C Scope Guard

This phase is verification and documentation only.
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
- credential reissue/rotation

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

- external credential recovery verification completeness
- GitHub authentication recovery path verified or documented owner action
- Telegram bot authentication recovery path verified or documented owner action
- Hermes API credential recovery path verified or documented owner action
- SSH private key recovery path verified or documented owner action
- secret-safe inspection
- repository diff check
- Windows duplicate runtime guard:
  - `WINDOWS_LOCAL_HERMES_BACKEND_RUNNING=NO`
  - `DUPLICATE_ACTIVE_ORBIS_RUNTIME=NO`
  - `WINDOWS_LOOPBACK_FORWARDING_MECHANISM=UNKNOWN`

STATUS: WP-005C external recovery verification in progress.

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
- Stop any expansion beyond External Credential Recovery Verification and
  return to approved Phase 5 architecture if scope drifts.
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
- credential reissue/rotation
- changing approved Phase 5 architecture unless required by migration

## Stop Conditions

Stop if:
- external recovery verification is incomplete;
- verification requires secret exposure;
- verification requires credential rotation/reissue;
- secrets may be exposed;
- rollback path is unavailable or untested;
- GitHub task state/evidence becomes inconsistent;
- a Level 3 action is reached without explicit Project Owner approval;
- scope expands beyond WP-005C External Credential Recovery Verification;
- Hermes Desktop attempts Windows-local backend bootstrap/installation.
- A second Hermes/Orbis runtime becomes active on Windows.
- `WINDOWS_LOCAL_HERMES_BACKEND_RUNNING=YES` or `DUPLICATE_ACTIVE_ORBIS_RUNTIME=YES`.

## Recovery Readiness

- External credential recovery verification is COMPLETE / PASS.
- RECOVERY_READINESS=YES
- All four required credential categories have external recovery paths verified
  by explicit Project Owner confirmation:
  - GitHub authentication = VERIFIED
  - Telegram bot authentication = VERIFIED
  - Hermes API credentials = VERIFIED
  - SSH private key recovery = VERIFIED
- Documentation alone is no longer the limiting factor; subsequent WP-005C phases
  still require separate approval before execution.

## Next Step

Proceed to the next approved WP-005C phase only after explicit Project Owner
approval for backup execution, migration validation, or cutover planning.

Do not expand scope beyond approved WP-005C phases without explicit approval.
