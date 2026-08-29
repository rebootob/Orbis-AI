# Security Policy

## Principles

Least privilege, explicit scope, separation of duties, traceable actions, and human control of irreversible or production-impacting work govern this system. Secrets are never committed to source control or exposed in task output.

## Permission levels

| Level | Name | Examples | Default authorization |
|---|---|---|---|
| 0 | Read | Read files/logs/docs; inspect Git and n8n | Automatic |
| 1 | Development Write | Create/modify development files, create branch, run tests | Automatic in approved development workspace |
| 2 | Important Write | Push, merge, modify n8n workflows/configuration, significant integration changes | Successful REVIEWER validation required |
| 3 | Human Approval | Deploy, delete, permission/credential change, production data change, migration, force push, destructive commands | Explicit user approval required |

No agent may bypass Level 3 approval. A reviewer PASS does not replace a Level 3 approval.

## Controls

- Scope every task to a registered project and workspace.
- Use development branches before important changes.
- Validate external integration identity and permissions before action.
- Begin integrations read-only where practical.
- Record approval evidence and reviewer outcomes.
- Redact secrets from logs and documentation.
