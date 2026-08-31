# Orbis AI

Orbis AI is a planned personal AI Control Center. Its first release will use Hermes as the primary orchestrator, Telegram as the remote command interface, and Git for traceable, reversible project work.

This repository is currently **documentation only**. No software, integrations, credentials, or deployments are included.

## Current state

- Phase: **0 — Project Foundation**
- Status: **In progress**
- Next checkpoint: project-owner review of the documentation

## Operating model

```mermaid
flowchart TD
  U[User] --> T[Telegram]
  T --> M[MASTER Hermes]
  M --> C[CODER]
  C --> R[REVIEWER]
  R --> M
  M --> U
  M --> S[Skills and tools]
  M --> G[Git]
  M --> K[Kanban]
```

## Documentation index

- [Start here](project-docs/00_CONTROL/START_HERE.md) · [Current state](project-docs/00_CONTROL/CURRENT_STATE.md) · [Document index](project-docs/00_CONTROL/DOCUMENT_INDEX.md)
- [Architecture](project-docs/20_ARCHITECTURE/SYSTEM_ARCHITECTURE.md)
- [Implementation roadmap](project-docs/50_PLANNING/ROADMAP.md)
- [Agent roles](project-docs/20_ARCHITECTURE/AGENT_ROLES.md)
- [Security policy](project-docs/10_GOVERNANCE/SECURITY_POLICY.md)
- [Approval policy](project-docs/10_GOVERNANCE/APPROVAL_POLICY.md)
- [Project registry](project-docs/20_ARCHITECTURE/PROJECT_REGISTRY.md)
- [Skill architecture](project-docs/20_ARCHITECTURE/SKILL_ARCHITECTURE.md)
- [n8n integration](project-docs/30_INTEGRATIONS/N8N.md)
- [Telegram design](project-docs/30_INTEGRATIONS/TELEGRAM.md)
- [Backup and recovery](project-docs/30_INTEGRATIONS/BACKUP_RECOVERY.md)
- [Acceptance tests](project-docs/50_PLANNING/TEST_ACCEPTANCE.md)
- [Active task](project-docs/00_CONTROL/ACTIVE_TASK.md) · [Current state](project-docs/00_CONTROL/CURRENT_STATE.md) · [Document index](project-docs/00_CONTROL/DOCUMENT_INDEX.md)

## Boundaries

V1 does not include a custom dashboard, large agent fleet, complex model voting or routing, custom memory/Kanban systems, unnecessary custom MCP servers, or production integrations. See the roadmap for the staged scope.

## Git governance

- `main` is the stable, approved, and recoverable branch.
- `develop` is the integration branch.
- Implementation work uses `feature/*`, `ai/codex-*`, or `hotfix/*` branches; significant changes are not made directly on `main` or normally on `develop`.
- Reviewable changes go through a Pull Request targeting `develop`; review approval and merge authorization are separate actions.
- Production or destructive actions require explicit human approval.
