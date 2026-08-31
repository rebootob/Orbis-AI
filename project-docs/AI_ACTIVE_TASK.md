# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-008 — N8N VIA MCP READ-ONLY VALIDATION

STATUS:
WP-008 = IMPLEMENTATION BLOCKED / AWAITING ENVIRONMENT
WP-008 Planning = COMPLETE / MERGED PR #29 (merge commit 2eec0883cff47456960983d062bbce8b52c77c89)
WP-007 = COMPLETE / MERGED PR #27 (merge commit 6ed9a3ef1c2b7d0eed95728150315ccf7a9e3ccb)
WP-006 = COMPLETE / MERGED PR #22 (merge commit 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8)
WP-005B = COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)
WP-005C Runtime Inventory/Backup Design = COMPLETE / MERGED (merge commit 3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44)
WP-005C External Credential Recovery Verification = COMPLETE / MERGED (merge commit a7789317931894366dba8f8d3e4b04d659ee6d4f)
WP-005C Backup Execution/Manifest Validation = COMPLETE / PASS

CURRENT PHASE:
Phase 8 — n8n via MCP = READ-ONLY VALIDATION BLOCKED

CURRENT PHASE DETAIL:
Phase 7 — Project Registry = COMPLETE
Issue #24 = CLOSED / COMPLETED
PR #27 = MERGED
MERGE_COMMIT = 6ed9a3ef1c2b7d0eed95728150315ccf7a9e3ccb
Phase 6 — Security Gates, Approvals, Audit Logging = COMPLETE
Issue #20 = state:completed
PR #22 = MERGED
MERGE_COMMIT = 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8
WP-005C Restore / DR Rehearsal = DEFERRED

BLOCKER:
n8n target environment cannot be identified. No n8n installation or configuration found on the runtime. Environment identity is UNKNOWN. Cannot prove local/dev/test target exists. Environment gate triggered: STOP before connection.

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

WORKING BRANCH:
ai/wp-008-n8n-mcp-readonly-implementation

TARGET:
develop

## Objective

Validate read-only n8n via MCP capability safely. BLOCKED: environment identity cannot be proven.

## Authorization

This read-only validation phase is explicitly authorized by ChatGPT Control Plane on 2026-08-31. Implementation may proceed only on branch `ai/wp-008-n8n-mcp-readonly-implementation` and only after Runtime REVIEWER PASS, Control Plane REVIEW_PASS, and explicit Project Owner approval.

## Scope

- Inventory MCP capability in Hermes/runtime
- Inventory n8n installation/configuration
- Identify n8n environment as local/dev/test/production/UNKNOWN
- Document endpoint/auth method metadata only
- If non-production target proven safe: implement minimum read-only MCP connection
- If environment ambiguous or only production exists: STOP and record blocker

## Read-Only Capability Set (if environment proven)

- list workflows
- read workflow metadata
- inspect workflow status
- read workflow definition/configuration only if confirmed read-only
- inspect execution metadata/history only if confirmed read-only

## Write Gate

All n8n write operations remain disabled/not authorized:
- create/update/delete workflow
- activate/deactivate workflow
- execute workflow with side effects
- credential changes
- webhook creation/change
- production changes

## Security

- Follow project-docs/04_SECURITY_POLICY.md.
- Follow project-docs/05_APPROVAL_POLICY.md.
- Do not expose secrets/credentials in docs, issues, comments, or code.
- No mutable current HEAD SHAs in tracked docs; GitHub PR metadata is authoritative.
- Preserve audit evidence; distinguish pre-authorization state from authorized state.

## Environment Separation

- local/dev/test n8n required for read-only validation
- production n8n may not be used for validation
- If only production exists or environment is ambiguous: STOP and report blocker

## Blocker

- n8n installation: NOT FOUND
- n8n process: NOT RUNNING
- n8n configuration: NOT FOUND
- n8n environment: UNKNOWN
- MCP references in Hermes: REFERENCE FOUND; runtime capability UNKNOWN (mcp Python package not importable; no MCP servers configured in config.yaml)
- Action: STOP. Cannot connect without proven safe non-production target.

## Next Step

Await explicit Control Plane instruction to provide a proven local/dev/test n8n target or alternative validation approach.
