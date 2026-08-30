# ORBIS AI — WP-005C TASK CONTRACT

PROJECT:
Orbis AI

WORK PACKAGE:
WP-005C — HERMES RUNTIME RESILIENCE, BACKUP / RESTORE, AND SERVER MIGRATION READINESS

STATUS:
PLANNING / NOT STARTED

BASE BRANCH:
develop

BASE COMMIT:
86f04140b110f446b5321eebf7f034f4d7ed0836

WORKING BRANCH:
ai/wp-005c-runtime-resilience-planning

TARGET:
develop

---

## 1. Objective

Make the Orbis AI Hermes runtime recoverable, portable, and migration-ready without
relying on chat history, while preserving all required integrations, profiles,
Core Skills, and authentication state.

## 2. Current Runtime Architecture

- WSL2 Hermes = primary Orbis runtime.
- MASTER = default Hermes profile.
- CODER = `coder` Hermes profile.
- REVIEWER = `reviewer` Hermes profile.
- Telegram = remote command interface.
- Hermes Desktop = optional operator console connected via SSH.
- GitHub Issues = canonical task/Kanban source of truth.
- GitHub/Git = implementation and audit evidence.

Hermes Desktop connects to the WSL2 Hermes backend via SSH:

Windows Hermes Desktop UI
-> Connect via SSH
-> allday@127.0.0.1:2222
-> existing WSL2 Hermes / Orbis runtime

Authentication:
ED25519 key-only.

No second Orbis runtime exists or is created on Windows.
Windows local Hermes backend = NO.
Telegram remains independently operational.

## 3. Runtime Inventory Requirements

Document and verify recoverability for:

- MASTER, CODER, REVIEWER Hermes profiles
- Hermes config/profile/SOUL files
- Core Skills in their intended runtime profile locations
- GitHub auth state usable by runtime
- Telegram bot/chat bindings and channel IDs
- Hermes Desktop SSH access and key trust state
- Cron/automation configs if any exist
- Any non-Git runtime state that must be restored

Inventory must identify what is inside Git and what requires separate
backup/restore handling.

## 4. Backup Scope

Backup must cover:

- Git repositories
- Hermes runtime profile/config/SOUL files
- Core Skill runtime copies and version mapping
- GitHub token auth state (presence only; never secret values)
- Telegram integration identifiers and binding state
- Hermes Desktop SSH trust/key state
- System/service config needed to restore runtime behavior

Explicitly exclude from backups and Git:

- `.env`
- API tokens
- GitHub tokens
- Telegram bot tokens
- OAuth credentials
- passwords
- private keys
- session secrets
- production credentials

## 5. Secret-Handling Rules

- Do not display, copy, commit, or transmit secrets.
- Use secret references/placeholders in documentation.
- Backup locations and metadata may reference secret existence, but
  must not store plaintext secret values.
- ED25519 key-only authentication is enforced for SSH connections.
- If secrets are required for restore, restore procedure must rely on
  secure existing stores/vaults, not chat history.

## 6. Restore Requirements

Restore must be possible without:

- chat history
- prior conversation memory
- manual re-instruction from ChatGPT

Restore targets:

- MASTER, CODER, REVIEWER profiles
- Core Skills and runtime version matrix
- GitHub task integration behavior
- Telegram integration
- Hermes Desktop SSH access
- Authority boundaries and role separation

Restore verification must include:

- fresh-session behavior
- identity and authority boundaries
- GitHub Issue state/role recognition
- blocked-state safety
- secret-safe state

## 7. Server Migration Strategy

- Existing Hermes server remains available during migration validation.
- No destructive migration.
- No server deletion.
- New server must be validated before cutover.
- Old server remains rollback target until post-cutover acceptance passes.
- Migration must be reversible at any point before acceptance.
- Network, SSH, and service discovery for the new server must be documented.

## 8. Parallel Validation Strategy

- Run new server validation alongside the existing server.
- Do not decommission or reconfigure production path until validation passes.
- Validate:
  - profile startup
  - Core Skill versions
  - GitHub task behavior
  - Telegram connectivity
  - Hermes Desktop SSH access
  - authority/role separation
  - restore/recovery completeness

## 9. Cutover Plan Requirements

- Approval gate before cutover.
- Explicit success/failure criteria.
- Time-boxed validation window.
- Rollback trigger conditions.
- Communication path for cutover status.
- Post-cutover acceptance test checklist.

## 10. Rollback Requirements

- Old server remains a valid rollback target.
- Rollback path must be documented step-by-step.
- Rollback must restore previous working runtime state.
- Rollback must preserve task history/evidence/Git history.

## 11. Disaster Recovery Rehearsal

- A disaster recovery rehearsal must prove the restore procedure works.
- Rehearsal must run in a non-production or approved isolated environment.
- Rehearsal must validate:
  - full profile restore
  - Core Skill restore and version verification
  - GitHub integration recovery
  - Telegram recovery
  - Hermes Desktop recovery
  - authority boundary recovery
  - secret-handling compliance
- Rehearsal results must be recorded before production use.

## 12. Acceptance Criteria

- All runtime inventory items documented.
- Backup procedure documented and tested for all required scope items.
- Restore procedure documented and proven without chat history.
- Parallel migration validation passes on new server.
- Cutover plan approved and executable.
- Rollback path documented and tested.
- Disaster recovery rehearsal recorded and successful.
- No secrets committed to Git.
- WP-005C task contract approved by Project Owner before implementation.

## 13. Permission Level

- Planning/documentation: Project Owner + ChatGPT Control Plane guidance.
- Backup/restore execution: Project Owner approval required.
- Migration/cutover: Project Owner approval required.
- Level 3 actions require explicit Project Owner approval.

## 14. Tests

- Runtime inventory completeness check
- Backup creation and verification test
- Restore test without chat history
- Fresh-session role/identity test
- GitHub task integration recovery test
- Telegram recovery test
- Hermes Desktop SSH recovery test
- Parallel new-server validation test
- Cutover dry-run or rehearsal
- Disaster recovery rehearsal

## 15. Out of Scope

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
- changing approved Phase 5 architecture unless required by migration

## 16. Stop Conditions

Stop if:

- runtime backup/inventory is incomplete;
- restore procedure requires chat history;
- secrets may be exposed;
- new server validation fails;
- old server must be deleted before acceptance;
- rollback path is unavailable or untested;
- GitHub task state/evidence becomes inconsistent;
- a Level 3 action is reached without explicit Project Owner approval;
- scope expands beyond WP-005C.

---

## Next Step

Define and approve the WP-005C task contract before implementation.

Required task contract elements:
- objective
- scope
- out-of-scope
- acceptance criteria
- permission level
- tests
- rollback
- stop conditions

Do not begin WP-005C implementation until its task contract is approved.
