# WP-008 Task Contract

WORK PACKAGE:
WP-008 — N8N VIA MCP READ-ONLY VALIDATION

STATUS:
IMPLEMENTATION AUTHORIZED — READ-ONLY VALIDATION ONLY

ISSUE:
#28

BRANCH:
ai/wp-008-n8n-mcp-readonly-implementation

TARGET:
develop

## Objective

Validate read-only n8n via MCP capability safely. If environment identity cannot be proven, implementation is BLOCKED and must stop.

## Scope

A. Connection architecture
- Hermes/Orbis -> MCP -> n8n
- identify MCP server/client responsibility
- no duplicate Hermes runtime
- no public exposure unless separately approved

B. Read-only first capability set
- list workflows
- read workflow metadata
- read workflow definition/configuration only if safely supported
- inspect workflow status
- inspect execution metadata/history only if read-only and safe

C. Write gate
- all n8n write operations disabled/not authorized:
  - create/update/delete workflow
  - activate/deactivate workflow
  - execute workflow with side effects
  - credential changes
  - webhook creation/change
  - production changes

D. Security
- no credentials/tokens/secrets committed to Git
- credential source/location documented only at metadata level
- least privilege
- fail closed if MCP/n8n identity, endpoint, permissions, or environment is ambiguous
- no secret values in logs/reports/issues/PRs

E. Environment separation
- local/dev/test n8n required for read-only validation
- production n8n may not be used for validation
- If only production exists or environment is ambiguous: STOP and report blocker

F. Evidence
- MCP availability/version
- n8n environment identity
- authentication method metadata
- read-only permission proof
- successful harmless read test
- evidence that writes remain unavailable/not authorized
- rollback/disconnect procedure

G. Governance
- Runtime REVIEWER = evidence only
- ChatGPT Control Plane = repository REVIEW_PASS
- Project Owner approval required for merge and any future write-capable/production-impacting action

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

## Stop Conditions

- STOP if environment separation cannot be satisfied
- STOP if write capability is requested before read-only validation
- STOP if secrets are discovered or required
- STOP if scope expands beyond this contract
- MASTER must STOP after merge/closeout; next WP requires new explicit Control Plane instruction

## Approval

- Runtime REVIEWER PASS required
- ChatGPT Control Plane REVIEW_PASS required
- explicit Project Owner approval required for merge
