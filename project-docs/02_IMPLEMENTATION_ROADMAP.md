# Implementation Roadmap

| Phase | Outcome | Exit condition |
|---|---|---|
| 0 | Repository, architecture, governance, documentation, Git baseline | Owner approves documentation baseline |
| 1 | Hermes installed on Windows with one configured model | Basic Hermes chat is verified |
| 2 | Private Telegram interface | Authorized-user Telegram → Hermes → Telegram test passes |
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

## Initial skills

`project-manager`, `code-development`, `code-review`, `git-governance`, `security`, `n8n`, and `kintone`. Future project skills may include `MBO2026`, `OrgFlow`, and `COCE`.

## Handoff flow

```mermaid
flowchart LR
  U[USER] --> M[MASTER] --> C[CODER] --> R[REVIEWER] --> M --> U
  R -- FAIL --> C
```
