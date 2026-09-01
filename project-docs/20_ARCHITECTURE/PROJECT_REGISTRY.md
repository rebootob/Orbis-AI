# Project Registry

The Project Registry lets MASTER identify the correct project, workspace, skills, and deployment restrictions before delegating work. Do not store real secrets in it.

## Required fields

| Field | Value |
|---|---|
| Project Name | Orbis AI |
| Repository | https://github.com/rebootob/Orbis-AI.git |
| Local Working Directory | `/home/allday/Orbis-AI` |
| Default Branch | `develop` |
| Development Branch | `develop` |
| Fallback/History Branch | `main` |
| Relevant Skills | `project-manager`, `code-development`, `code-review`, `git-governance`, `security` |
| Production Environment | `NOT_DEFINED` — no production deployment target authorized |
| Deployment Policy | Level 3 explicit Project Owner approval required |
| Approval Requirement | See Approval Policy |

## Operating rules

- MASTER must identify a registry record before initiating project work. A missing or ambiguous record blocks write actions until the owner clarifies it.
- Registry lookup is implemented and validated.
- `main` is retained as stable/fallback/history only; `develop` is the canonical/integration branch.
- Missing or ambiguous registry still blocks write actions.
