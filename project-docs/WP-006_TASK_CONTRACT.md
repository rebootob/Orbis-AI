# ORBIS AI — WP-006 TASK CONTRACT

WORK PACKAGE:
WP-006 — SECURITY GATES, APPROVALS, AND AUDIT LOGGING

STATUS:
PLANNING ONLY

CURRENT PHASE:
Phase 6 — Security Gates, Approvals, Audit Logging

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

WORKING BRANCH:
ai/wp-006-security-gates-planning

TARGET:
develop

## Objective

Define the smallest complete Phase 6 governance package that makes permission
gates, approval requirements, audit evidence, and role boundary enforcement
explicit and reviewable. This work package is planning/docs-only: no runtime
code changes, no deployment, no automation, and no secret handling are
authorized.

## Scope

- Define the canonical WP-006 task contract in `project-docs/WP-006_TASK_CONTRACT.md`.
- Define the smallest Phase 6 security policy surface in `project-docs/04_SECURITY_POLICY.md`.
- Define approval-record requirements in `project-docs/05_APPROVAL_POLICY.md`.
- Define audit evidence format and retention requirements in a new document
  under `project-docs/`.
- Update `project-docs/12_KANBAN_HANDOFF.md` to record explicit blocked/fail
  behavior when permission/approval gates are bypassed through Telegram,
  Desktop, GitHub comments, or Skills.
- Update `project-docs/AI_ACTIVE_TASK.md` to identify WP-006 as PLANNING ONLY
  and stop all WP-005C restore/migration/cutover/DR work.
- Preserve Phase 5 workflow, WP-005C backup semantics, and CHAT_HANDOFF resume
  behavior.

## Out of Scope

- Runtime code changes
- Hermes skill code changes
- n8n/MCP/Kintone
- Deployment or production changes
- Secret rotation or credential changes
- Restore, migration, cutover, or DR rehearsal
- WP-005D or later
- Force push
- Unrelated refactoring

## Acceptance Criteria

- `project-docs/WP-006_TASK_CONTRACT.md` exists and defines Objective, Scope,
  Out of Scope, Acceptance Criteria, Permission Level, Required Evidence /
  Tests, Rollback, Stop Conditions, Project Owner approval gates, Level 3
  protections, role boundary enforcement, audit evidence requirements, explicit
  blocked/fail behavior, no secret exposure, and no bypass via
  Telegram/Desktop/GitHub comments/Skills.
- `project-docs/AI_ACTIVE_TASK.md` identifies WP-006 as PLANNING ONLY and
  stops all restore/migration/cutover/DR work.
- No repository code, runtime files, or secrets are modified.
- The contract is reviewable as docs-only evidence on the planning branch.

## Permission Level

- Level 0 reads: allowed automatically.
- Level 1 development writes: allowed only inside approved WP-006 planning/docs
  scope on branch `ai/wp-006-security-gates-planning`.
- Level 2 writes: not authorized in this WP.
- Level 3 actions: not authorized in this WP; restore, migration, cutover, DR,
  deployment, and production changes remain explicitly deferred and require
  explicit Project Owner approval per phase.

## Required Evidence / Tests

- Planning docs completeness check: required files exist and cover required
  sections.
- No-secret check: no `.env`, tokens, passwords, private keys, OAuth secrets,
  or session secrets are introduced.
- Diff review: `git diff --check` passes.
- Review handoff updated when contract is finalized.

## Rollback

- Revert the planning branch or delete the branch if scope drifts.
- Repository changes can be reverted through Git.
- Existing valid backups must not be deleted.
- No runtime state is modified by this WP.

## Stop Conditions

Stop if:

- scope expands beyond Phase 6 planning/docs;
- secrets are required or exposed;
- runtime files outside approved docs scope are modified;
- approval language becomes ambiguous or enables bypass;
- a Level 3 action is reached without explicit Project Owner approval;
- restore, migration, cutover, or DR rehearsal is started;
- n8n/MCP/Kintone or automation is started;
- CHAT_HANDOFF resume behavior is broken;
- WP-005C backup semantics are altered.

## Project Owner Approval Gates

- Project Owner approval is required before WP-006 implementation, branch
  creation for implementation, or merge into `develop`.
- Merge requires explicit Project Owner approval even after ChatGPT Control
  Plane `REVIEW_PASS`.
- Approval evidence must record Task ID, requested action, permission/risk
  level, actor, timestamp, and outcome.

## Level 3 Protections

- Restore, migration, cutover, DR rehearsal, deployment, force push, production
  data change, credential/permission change, and destructive actions remain
  Level 3 and require explicit Project Owner approval for the exact action and
  target.
- Runtime REVIEWER PASS and repository `REVIEW_PASS` do not authorize Level 3
  actions.
- No agent, skill, Telegram message, Desktop action, or GitHub comment may
  bypass Level 3 approval.

## Role Boundary Enforcement

- MASTER = coordinator.
- CODER = implementation role; may not self-approve or merge.
- REVIEWER = independent reviewer; may not modify implementation under review.
- ChatGPT Control Plane = determines repository `REVIEW_PASS`.
- Project Owner = final authority for merge and Level 3 actions.
- Skills, labels, task comments, Desktop, and Telegram do not grant additional
  authority.

## Audit Evidence Requirements

- Canonical task record is a GitHub Issue with `state:*` and `role:*` labels.
- Issue body = task contract.
- Issue comments = chronological handoff and audit evidence.
- Branch / commit / Pull Request = implementation evidence when applicable.
- Approval record must include Task ID, target, requested action, permission
  level, runtime reviewer result, ChatGPT Control Plane review decision, Project
  Owner approval where required, actor, timestamp, and outcome.
- During Phase 6 planning, the planning branch commit and PR are the reviewable
  evidence.

## Explicit Blocked / Fail Behavior

- If permission/approval evidence is missing or inconsistent, the task must
  enter `state:blocked`.
- Blocked transition comment must record `BLOCKED_FROM_STATE`,
  `BLOCKED_FROM_ROLE`, `REASON`, `RESOLUTION_REQUIRED`, and
  `NEXT_STATE_AFTER_RESOLUTION`.
- If bypass is attempted through Telegram, Desktop, GitHub comments, or Skills,
  the action must fail closed and be recorded as an audit event.
- If scope, environment, authority, or impact is unclear, stop and request
  clarification; do not infer approval.

## Secret Exposure

- Do not display, copy, commit, or transmit `.env`, tokens, passwords,
  credentials, private keys, OAuth secrets, Telegram IDs, session secrets,
  production credentials, or approval tokens in docs, Issues, comments, or
  handoffs.
- If found, stop and report only file, risk category, and corrective action.
