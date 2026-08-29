# Skill Architecture

Skills package reusable operating guidance and tool procedures. They should be preferred over creating new agents when the work does not require an independent role, authority boundary, or review loop.

## Initial categories

| Skill | Purpose |
|---|---|
| project-manager | Task breakdown, status, handoffs, registry lookup |
| code-development | Development workflow, branching, tests, documentation |
| code-review | Diff, regression, security, and test review |
| git-governance | Branching, commit, merge, rollback, audit rules |
| security | Permissions, secrets handling, approvals, logging |
| n8n | Read-only-first workflow inspection and change controls |
| kintone | Future least-privilege Kintone procedures |

Future project-specific skills: `MBO2026`, `OrgFlow`, `COCE`, and other approved internal projects.

Each skill should state its scope, allowed tools, required inputs, permission ceiling, verification steps, audit output, and escalation conditions.
