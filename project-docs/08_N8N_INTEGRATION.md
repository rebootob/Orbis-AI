# n8n Integration

n8n is a future automation engine for deterministic workflows and integrations. It is not the system's primary AI orchestrator.

## Current Phase 8 state

Phase 8 = READ-ONLY VALIDATION COMPLETE — EMPTY-SANDBOX READ OPERATIONS = NOT TESTABLE WITHOUT WRITE — OWNER ACCEPTED

## Read-only-first architecture

- Hermes/Orbis → MCP → n8n
- Read-only capability set:
  - list workflows
  - read workflow metadata
  - inspect workflow status
  - read workflow definition/configuration only if confirmed read-only
  - inspect execution metadata/history only if confirmed read-only
- Write/modification capabilities remain disabled until:
  - a proven non-production target exists,
  - read-only testing passes,
  - review succeeds, and
  - the appropriate approval level is satisfied.
- Workflow modifications are Level 2; production-impacting changes may require Level 3 approval.

## Environment separation

- local/dev/test n8n is required for read-only validation.
- production n8n may not be used for validation.
- If only production exists or environment identity is ambiguous: STOP and report blocker.

## Current runtime evidence

- MCP runtime in Hermes/runtime: PROVEN
- MCP package/distribution/version: mcp 2.0.0 + mcp-types 2.0.0
- Python executable: /home/allday/.hermes/hermes-agent/venv/bin/python
- venv: /home/allday/.hermes/hermes-agent/venv
- Import test: SUCCESS
- configured MCP servers: none

## Credential and endpoint policy

- No production credentials may be used for validation.
- No credentials, tokens, or endpoint values are stored in Git.
- Only metadata-level location/type information is recorded in docs.
- All real secrets must remain outside source control.

## Closeout status

- Read-only validation result: EMPTY-SANDBOX READ OPERATIONS = NOT TESTABLE WITHOUT WRITE — OWNER ACCEPTED
- Write-capable phases: NOT AUTHORIZED
- Production integration: NOT COMPLETE
