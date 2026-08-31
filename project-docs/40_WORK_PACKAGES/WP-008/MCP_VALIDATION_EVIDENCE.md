# WP-008 MCP Read-Only Validation Evidence

STATUS: MCP RUNTIME PROVEN — READ-ONLY OPERATIONS PENDING CONTROL PLANE AUTHORIZATION

DATE: 2026-08-31

PROFILE: MASTER/CODER review only; no implementation beyond minimum runtime setup.

## Verified Environment

- develop HEAD: 2a890f22889f6afce19db03f6ec7b5027195e4a7
- Issue #28 state: in-progress
- Issue #28 role: coder
- n8n sandbox: LOCAL_TEST
- n8n endpoint: 127.0.0.1:5678
- n8n binary present: YES
- n8n version: 2.36.9
- sqlite3 module: loadable
- n8n process: NOT RUNNING
- Healthz last verified: {"status":"ok"} (from prior test)
- No production connection attempted
- No n8n writes performed
- No external side effects

## MCP Runtime Status

- mcp Python package: INSTALLED / IMPORTABLE
- Python executable/path: /home/allday/.hermes/hermes-agent/venv/bin/python
- venv path: /home/allday/.hermes/hermes-agent/venv
- import test result: SUCCESS
- package/distribution/version: mcp 2.0.0
- module path: /home/allday/.hermes/hermes-agent/venv/lib/python3.11/site-packages/mcp/__init__.py
- minimal command/evidence used:
  - /home/allday/.hermes/hermes-agent/venv/bin/python -m pip show mcp
  - /home/allday/.hermes/hermes-agent/venv/bin/python -c "import mcp"
- mcp_servers configured in ~/.hermes/config.yaml: NO
- No secrets committed to Git

## Read-Only Operation Status

- health/connectivity check: PASS (n8n /healthz OK)
- list workflows: NOT TESTABLE WITHOUT WRITE (empty LOCAL_TEST sandbox)
- read workflow metadata: NOT TESTABLE WITHOUT WRITE
- read workflow definition/configuration: NOT TESTABLE WITHOUT WRITE
- inspect workflow status: NOT TESTABLE WITHOUT WRITE
- inspect execution metadata/history: NOT TESTABLE WITHOUT WRITE

## Conclusion

MCP runtime capability is proven in the existing Hermes WSL2 runtime.
Read-only MCP validation against the empty LOCAL_TEST sandbox is blocked at
the n8n data layer: no workflows/data exist to read, and creating dummy
workflows is forbidden.

REMAINING_BLOCKER: Control Plane must authorize either:
- a non-dummy read-only target/data population path, or
- accept NOT TESTABLE WITHOUT WRITE as final for empty-sandbox cases,
  and proceed to write-capable phases only after explicit authorization.

## Required Next Step

Explicit Control Plane instruction for one of:
- accept NOT TESTABLE WITHOUT WRITE for empty-sandbox read-only operations
- authorize bounded write/dummy workflow creation for read-only validation
- authorize alternative read-only validation approach that does not require n8n writes
