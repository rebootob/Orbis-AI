# WP-007 Task Contract

WORK PACKAGE:
WP-007 — PROJECT REGISTRY PLANNING

STATUS:
PLANNING ONLY

ISSUE:
#24

BRANCH:
ai/wp-007-project-registry-planning

TARGET:
develop

## Objective

Define the smallest complete Phase 7 Project Registry design required to satisfy:
"Registered-project lookup works."

## Authorization

This planning work is explicitly authorized by ChatGPT Control Plane on
2026-08-31. Issue #24 and the original PR #25 head e094be4 were created before authorization and are
preserved as pre-authorization audit evidence only. The original pre-authorization head does not
constitute current authorization. The reconciled current head b4a60a1 is the authorized
planning evidence. It may proceed only through: Runtime REVIEWER PASS -> Control Plane REVIEW_PASS -> explicit Project Owner approval -> merge.

## Scope

- A. Define one canonical Project Registry source in Git.
- B. Registry lookup fields: project_id, project_name, repository, canonical_branch,
  project_docs_path, status, control_plane, execution_role/model if applicable.
- C. Define lookup behavior: project name/project id -> canonical registry record -> repository/project context.
- D. Registry must not contain secrets, tokens, passwords, private keys, credentials,
  or production connection strings.
- E. Git/repository truth remains authoritative. Chat memory, Telegram, Desktop, Skills,
  or Hermes memory must not silently override registry truth.
- F. Fail closed:
  - unknown project
  - duplicate project_id
  - duplicate ambiguous project name
  - missing required field
  - invalid repository/branch metadata
  must return explicit lookup failure, not guess.
- G. Keep design minimal. Prefer a single version-controlled registry file unless strong evidence requires otherwise.

## Merge authorization rule

A merge may occur only after this exact sequence:
1. Runtime REVIEWER returns PASS.
2. STOP.
3. ChatGPT Control Plane independently reviews the current GitHub repository/PR head SHA.
4. ChatGPT explicitly issues `REVIEWER PASS` / `REVIEW_PASS`.
5. STOP.
6. Project Owner explicitly approves the exact PR merge.
7. The merge may then occur.

No earlier step authorizes a later step. Absence of any step invalidates merge authorization.

## Out of Scope

- database
- web UI
- custom Kanban
- n8n/MCP/Kintone
- project-specific integrations
- runtime deployment
- cron/automation
- Restore/DR
- server migration
- new agents
- broad skill changes
- implementation code or runtime behavior

## Acceptance Criteria

- WP-007_TASK_CONTRACT.md exists and matches approved Phase 7 scope.
- One canonical registry source is defined in Git.
- Lookup behavior is specified and fails closed on invalid input.
- No secrets, tokens, credentials, or connection strings are stored in registry docs.
- AI_ACTIVE_TASK.md reflects WP-007 PLANNING ONLY.

## Permission Level

- Level 0 read: inspect docs, issues, logs, branches, and configuration without modification.
- Level 1 planning/docs write: edit approved planning/docs inside WP-007 scope on branch `ai/wp-007-project-registry-planning`.
- Level 2 integration: push branch, create/update PR, run approved tests.
- Level 3 owner approval: merge, deploy, production change, or runtime behavior introduction.

Level 2 does not authorize merge, deploy, production, Restore/DR, credentials, or any Level 3 action.

## Required Evidence / Tests

- Contract/docs completeness check
- Permission/role consistency check
- Secret exclusion check
- git diff --check

## Rollback

Revert the planning branch or delete the branch if scope drifts.

## Stop Conditions

Stop if:
- scope expands beyond approved Phase 7 planning;
- implementation code or runtime behavior is introduced;
- secrets or credentials are included in registry design;
- lookup behavior is defined as guessing or fallback to non-authoritative sources;
- n8n/MCP/Kintone/database/web UI is introduced;
- PR #25 is merged;
- planning PR is merged without Control Plane and Project Owner authorization.
