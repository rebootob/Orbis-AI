# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-008 — N8N VIA MCP READ-ONLY VALIDATION

STATUS:
WP-008 = SANDBOX PROVEN / AWAITING READ-ONLY VALIDATION AUTHORIZATION
WP-008 Planning = COMPLETE / MERGED PR #29 (merge commit 2eec0883cff47456960983d062bbce8b52c77c89)
WP-008 Read-Only Evidence = COMPLETE / MERGED PR #30 (merge commit ae9dc212bcc0e4fad78179e37e51a23625808261)
WP-007 = COMPLETE / MERGED PR #27 (merge commit 6ed9a3ef1c2b7d0eed95728150315ccf7a9e3ccb)
WP-006 = COMPLETE / MERGED PR #22 (merge commit 41fc3d270b6837bdfe88d39cdfdcdace1a839ac8)
WP-005B = COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)
WP-005C Runtime Inventory/Backup Design = COMPLETE / MERGED (merge commit 3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44)
WP-005C External Credential Recovery Verification = COMPLETE / MERGED (merge commit a7789317931894366dba8f8d3e4b04d659ee6d4f)
WP-005C Backup Execution/Manifest Validation = COMPLETE / PASS

CURRENT PHASE:
Phase 8 — n8n via MCP = SANDBOX PROVEN / AWAITING READ-ONLY VALIDATION

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

SANDBOX_PROVISIONING:
Local Node/npm-based n8n sandbox provisioned and proven.
Status: COMPLETE
Environment: LOCAL_TEST
Bind: 127.0.0.1:5678
Version: 2.36.9
Storage: /home/allday/orbis-wp008-n8n-sandbox
Production target used: NO
Real credentials used: NO
Real data used: NO
Dummy workflows created: NO
External side effects: NONE
SANDBOX_PROVISIONING_STARTED=YES
SANDBOX_PROVISIONING_COMPLETE=YES

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

TARGET:
develop

## Objective

Validate read-only n8n via MCP capability safely. Local sandbox proven; awaiting explicit authorization for read-only MCP validation.

## Authorization

This read-only validation phase is explicitly authorized by ChatGPT Control Plane on 2026-08-31. Implementation may proceed only after Runtime REVIEWER PASS, Control Plane REVIEW_PASS, and explicit Project Owner approval.

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

## Sandbox Evidence

- n8n installation: FOUND
- n8n process: PROVEN STARTABLE
- n8n configuration: LOCAL_TEST
- n8n environment: LOCAL_TEST
- n8n version: 2.36.9
- Listen address: 127.0.0.1:5678
- Public exposure: NO
- MCP references in Hermes: REFERENCE FOUND; runtime capability UNKNOWN (mcp Python package not importable; no MCP servers configured in config.yaml)
- Action: SANDBOX PROVEN. Await explicit Control Plane authorization for read-only MCP validation.

## Next Step

Await explicit Control Plane authorization for read-only MCP validation against proven LOCAL_TEST sandbox.
Do not auto-start MCP validation from this document.
