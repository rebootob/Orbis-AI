# Project Registry

The Project Registry lets MASTER identify the correct project, workspace, skills, and deployment restrictions before delegating work. Do not store real secrets in it.

## Required fields

| Field | Initial value |
|---|---|
| Project Name | Orbis AI |
| Repository | https://github.com/rebootob/Orbis-AI.git |
| Local Working Directory | `<TO_BE_DEFINED>` |
| Default Branch | main |
| Development Branch | develop |
| Relevant Skills | project-manager, code-development, code-review, git-governance, security |
| Production Environment | `<TO_BE_DEFINED>` |
| Deployment Policy | Level 3 explicit human approval |
| Approval Requirement | See Approval Policy |

## Operating rule

MASTER must identify a registry record before initiating project work. A missing or ambiguous record blocks write actions until the owner clarifies it.
