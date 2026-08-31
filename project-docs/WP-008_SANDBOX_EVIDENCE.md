# WP-008 Sandbox Provisioning Evidence

STATUS: COMPLETE — LOCAL_TEST SANDBOX PROVEN

DATE: 2026-08-31

PROFILE: Local WSL2 host

## Preflight

- Disk space: sufficient
- Memory: sufficient
- Node/npm/npx: available (`node v26.8.1`, `npm 11.19.0`, `npx 11.19.0`)
- Docker: not installed; not installed for this task
- Port conflicts: none identified
- Public exposure: not performed

## Provisioning Result

METHOD: Node/npm-based local n8n in isolated local test storage at `/home/allday/orbis-wp008-n8n-sandbox`.

RESULT: SUCCESS.

DETAIL: `npm install --ignore-scripts n8n` succeeded. `sqlite3` native bindings missing initially; `npm rebuild sqlite3 --build-from-source` resolved bindings. n8n starts successfully with local-only binding.

N8N_VERSION=2.36.9

## Environment Identity

ENVIRONMENT=LOCAL_TEST
PURPOSE=WP008_READONLY_VALIDATION
PRODUCTION=NO

## Runtime Proof

- Start command: `N8N_ENVIRONMENT=LOCAL_TEST N8N_PURPOSE=WP008_READONLY_VALIDATION N8N_PROTOCOL=http N8N_HOST=127.0.0.1 N8N_PORT=5678 N8N_RUNNERS_ENABLED=true ./node_modules/.bin/n8n start`
- Bind address: 127.0.0.1:5678
- Public exposure: NO
- Test storage: `/home/allday/orbis-wp008-n8n-sandbox` (local, isolated, non-production)
- Real credentials used: NO
- Real data used: NO
- Dummy/no-op workflows: none created yet; sandbox proven empty

## Operational Proof

- n8n process starts successfully: YES
- Version identified: 2.36.9
- Listening address is local-only: YES (127.0.0.1:5678)
- Test data is non-production: YES
- No external side effects: YES
- Shutdown/restart procedure works: YES (SIGTERM clean shutdown tested)

## Governance

- No n8n write-capable operations performed beyond empty sandbox startup.
- No production connection.
- No secrets committed.
- No Phase 9/Start-Restore/DR.
- Local artifacts created outside Git; nothing sensitive to commit.

## Next Step

Await explicit Control Plane instruction before MCP read-only validation or any further sandbox configuration.
