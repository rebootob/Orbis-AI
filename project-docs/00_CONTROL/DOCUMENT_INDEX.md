# Orbis AI — Document Index

> Canonical map of documentation topics. `00_CONTROL` documents are the only mandatory new-session reads.

## Control

| Topic | Canonical document |
|---|---|
| Mandatory startup protocol | `00_CONTROL/START_HERE.md` |
| Current repository/documentation state | `00_CONTROL/CURRENT_STATE.md` |
| Active work-package gate | `00_CONTROL/ACTIVE_TASK.md` |
| Documentation topology | `00_CONTROL/DOCUMENT_INDEX.md` |

## Governance

| Topic | Canonical document |
|---|---|
| Authority, role boundaries, Git/workflow controls | `10_GOVERNANCE/AUTHORITY_MODEL.md` |
| Security policy | `10_GOVERNANCE/SECURITY_POLICY.md` |
| Approval and permission policy | `10_GOVERNANCE/APPROVAL_POLICY.md` |
| Kanban task state and handoff | `10_GOVERNANCE/KANBAN_HANDOFF.md` |
| Change decisions and governance history | `10_GOVERNANCE/CHANGE_GOVERNANCE.md` |

## Architecture

| Topic | Canonical document |
|---|---|
| System/runtime architecture | `20_ARCHITECTURE/SYSTEM_ARCHITECTURE.md` |
| Agent roles | `20_ARCHITECTURE/AGENT_ROLES.md` |
| Skill architecture | `20_ARCHITECTURE/SKILL_ARCHITECTURE.md` |
| Project registry | `20_ARCHITECTURE/PROJECT_REGISTRY.md` |

## Integrations

| Topic | Canonical document |
|---|---|
| n8n / MCP | `30_INTEGRATIONS/N8N.md` |
| Telegram | `30_INTEGRATIONS/TELEGRAM.md` |
| Backup and recovery | `30_INTEGRATIONS/BACKUP_RECOVERY.md` |

## Work-package evidence

| Work package | Canonical directory |
|---|---|
| WP-005 | `40_WORK_PACKAGES/WP-005/` |
| WP-006 | `40_WORK_PACKAGES/WP-006/` |
| WP-007 | `40_WORK_PACKAGES/WP-007/` |
| WP-008 | `40_WORK_PACKAGES/WP-008/` |
| WP-009 | `40_WORK_PACKAGES/WP-009/` |
| WP-010 | `40_WORK_PACKAGES/WP-010/` |

## Planning

| Topic | Canonical document |
|---|---|
| Phase roadmap | `50_PLANNING/ROADMAP.md` |
| Test and acceptance criteria | `50_PLANNING/TEST_ACCEPTANCE.md` |

## Archive

`90_ARCHIVE/` retains superseded historical snapshots and records. It is not a source of current task state or authorization.

## Migration map

| Old path | New canonical path | Action |
|---|---|---|
| `AI_CONTROL_PLANE.md` | `10_GOVERNANCE/AUTHORITY_MODEL.md` | moved/renamed |
| `AI_ACTIVE_TASK.md` | `00_CONTROL/ACTIVE_TASK.md` | replaced; prior snapshot archived |
| `CHAT_HANDOFF.md` | `00_CONTROL/CURRENT_STATE.md` and `00_CONTROL/START_HERE.md` | replaced; prior snapshot archived |
| `00_PROJECT_OVERVIEW.md`, `CHANGELOG.md`, historical incident/audit records | `90_ARCHIVE/` | archived; not current truth |
| `01_`, `03_`, `06_PROJECT_`, `07_` architecture docs | `20_ARCHITECTURE/` | moved/renamed |
| `04_`, `05_`, `12_`, `DECISION_LOG.md` | `10_GOVERNANCE/` | moved/renamed |
| `08_`, `09_`, `10_` integration docs | `30_INTEGRATIONS/` | moved/renamed |
| `WP-005C_*`, `WP-006_*`, `WP-007_*`, `WP-008*`, `WP-009_*` | `40_WORK_PACKAGES/WP-005/` through `WP-009/` | moved/renamed; evidence retained |
| `02_IMPLEMENTATION_ROADMAP.md`, `11_TEST_ACCEPTANCE.md` | `50_PLANNING/` | moved/renamed |
