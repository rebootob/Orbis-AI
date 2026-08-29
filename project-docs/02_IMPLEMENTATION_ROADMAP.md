# Implementation Roadmap

| Phase | Outcome | Exit condition |
|---|---|---|
| 0 | Repository, architecture, governance, documentation, Git baseline | Owner approves documentation baseline |
| 1 | Hermes runtime baseline validated on WSL2 Ubuntu | systemd, `hermes doctor`, and basic chat validation pass |
| 2 | Private allowlisted Telegram interface validated on WSL2 | Authorized-user Telegram → Hermes → Telegram round-trip passes |
| 3 | MASTER, CODER, REVIEWER profiles | Role boundaries are exercised |
| 4 | Skill architecture | Initial skills are documented and available |
| 5 | Kanban and handoff | MASTER → CODER → REVIEWER → MASTER flow works |
| 6 | Security gates, approvals, audit logging | Permission and evidence checks work |
| 7 | Project Registry | Registered-project lookup works |
| 8 | n8n via MCP | Read-only capabilities pass testing before writes |
| 9 | Automation/Cron | Approved operational jobs are monitored |
| 10 | Backup/Recovery | Recovery procedure is tested |

## Phase 0 deliverables

The documents in this repository, an initial decision log, a gitignore policy, and a safe-to-initialize repository structure. No implementation work is authorized by Phase 0.

## Validated runtime baseline

**Phase 1 — Complete:** Hermes is operational on WSL2 Ubuntu with systemd. `hermes doctor` and the `ORBIS-WSL-OK` basic chat test passed using the baseline model `stepfun/step-3.7-flash:free`. Windows Native Hermes is retained only as fallback.

**Phase 2 — Complete:** A private, explicitly allowlisted Telegram bot completed validated Telegram → Hermes → Telegram round trips on the WSL2 systemd gateway. `ORBIS-WSL-TELEGRAM-OK`, `TEST-1`, model query, and `ORBIS-READY` passed. The Windows Native Telegram Gateway is not the primary runtime because it was unstable.

## Initial skills

`project-manager`, `code-development`, `code-review`, `git-governance`, `security`, `n8n`, and `kintone`. Future project skills may include `MBO2026`, `OrgFlow`, and `COCE`.

## Handoff flow

```mermaid
flowchart LR
  U[USER] --> M[MASTER] --> C[CODER] --> R[REVIEWER] --> M --> U
  R -- FAIL --> C
```
