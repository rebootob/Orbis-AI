# n8n Integration

n8n is a future automation engine for deterministic workflows and integrations. It is not the system's primary AI orchestrator.

## Current Phase 8 state

Phase 8 is in read-only validation, but is currently blocked because no proven local/dev/test n8n environment exists yet.

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

- MCP references in Hermes/runtime: FOUND
- MCP runtime capability: UNKNOWN
- MCP version: UNKNOWN
- MCP Python package: not importable in current runtime
- configured MCP servers: none

## Credential and endpoint policy

- No production credentials may be used for validation.
- No credentials, tokens, or endpoint values are stored in Git.
- Only metadata-level location/type information is recorded in docs.
- All real secrets must remain outside source control.

## Next step

The next safe step is sandbox provisioning only after explicit Control Plane authorization:

- provision an isolated LOCAL_TEST n8n sandbox on the approved WSL2 host,
- bind to loopback/local interface only,
- use dummy/no-op test workflows,
- then proceed to harmless read-only MCP validation.

Do not auto-start sandbox work from this document.
