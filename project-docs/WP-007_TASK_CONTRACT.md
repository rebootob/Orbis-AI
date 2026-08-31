# WP-007 Task Contract

WORK PACKAGE:
WP-007 — PROJECT REGISTRY IMPLEMENTATION

STATUS:
IMPLEMENTATION AUTHORIZED

ISSUE:
#24

BRANCH:
ai/wp-007-project-registry-implementation

TARGET:
develop

## Objective

Implement the approved Phase 7 Project Registry so registered-project lookup
works. This is the implementation phase. No database, web UI, n8n/MCP/Kintone,
automation/cron, new agents, or broad skill changes are authorized.

## Authorization

This implementation is explicitly authorized by ChatGPT Control Plane on
2026-08-31. WP-007 planning PR #25 is merged (merge commit
d2aa184957dfa4b68087c6c708ec28cc84e5937d). Implementation may proceed only
on branch `ai/wp-007-project-registry-implementation` and only after Runtime
REVIEWER PASS, Control Plane REVIEW_PASS, and explicit Project Owner approval.

## Scope

- Implement one canonical Project Registry source in Git.
- Deterministic lookup by project_id and project_name.
- Required fields: project_id, project_name, repository, canonical_branch,
  project_docs_path, status, control_plane, execution_role/model if applicable.
- Fail closed on unknown project, duplicate project_id, ambiguous duplicate
  project_name, missing required field, or invalid repository/branch metadata.
- Git/repository truth remains authoritative. No secrets or credentials in registry.
- Add focused tests for valid lookup, fail-closed cases, and secret exclusion.

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
- Phase 8 or later work

## Acceptance Criteria

- `scripts/wp007_registry.py` implements deterministic lookup by project_id and project_name.
- `scripts/wp007_registry.txt` provides the canonical registry source.
- Fail-closed behavior covers: unknown project, duplicate project_id, ambiguous duplicate project_name, missing required field, invalid repository/branch metadata.
- `tests/test_wp007_registry.py` covers valid lookups, fail-closed cases, and secret exclusion.
- `git diff --check` passes.
- No secrets/credentials in registry data or code.

## Permission Level

- Level 0 read: inspect docs, issues, logs, branches, and configuration without modification.
- Level 1 implementation/docs write: edit approved implementation/docs inside WP-007 scope on branch `ai/wp-007-project-registry-implementation`.
- Level 2 integration: push branch, create/update PR, run approved tests.
- Level 3 owner approval: merge, deploy, production change, or runtime behavior introduction.

Level 2 does not authorize merge, deploy, production, Restore/DR, credentials, or any Level 3 action.

## Required Evidence / Tests

- Implementation completeness check
- Contract/docs completeness check
- Permission/role consistency check
- Secret exclusion check
- git diff --check
- Focused tests pass:
  - valid lookup by project_id
  - valid lookup by project_name
  - unknown project failure
  - duplicate ID failure
  - ambiguous name failure
  - missing field failure
  - invalid metadata failure
  - secret exclusion

## Rollback

Revert the implementation branch or delete the branch if scope drifts.

## Stop Conditions

Stop if:
- scope expands beyond approved Phase 7 implementation;
- implementation code or runtime behavior is introduced outside approved scripts/tests;
- secrets or credentials are included in registry design;
- lookup behavior is defined as guessing or fallback to non-authoritative sources;
- n8n/MCP/Kintone/database/web UI is introduced;
- implementation PR is merged without Control Plane REVIEW_PASS and Project Owner approval.
