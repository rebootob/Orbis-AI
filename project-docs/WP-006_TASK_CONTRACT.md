# ORBIS AI — WP-006 TASK CONTRACT

WORK PACKAGE:
WP-006 — Security Gates, Approvals, and Audit Logging

STATUS:
IMPLEMENTATION APPROVED

CURRENT PHASE:
Phase 6 — Security Gates, Approvals, Audit Logging — Implementation

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

WORKING BRANCH:
ai/wp-006-security-gates-implementation

TARGET:
develop

## Objective

Execute the approved Phase 6 security gates, approvals, audit evidence,
and role boundary enforcement package. No runtime code changes, deployment,
automation, or secret handling are authorized outside the defined docs scope.

## Scope

- Define `project-docs/06_SECURITY_GATES_AUDIT_POLICY.md` for audit evidence,
  retention, and fail-closed behavior.
- Update `project-docs/04_SECURITY_POLICY.md` with the minimum Phase 6 security
  policy surface.
- Update `project-docs/05_APPROVAL_POLICY.md` with approval-record requirements.
- Update `project-docs/12_KANBAN_HANDOFF.md` to record explicit blocked/fail
  behavior when permission/approval gates are bypassed through Telegram,
  Desktop, GitHub comments, or Skills.
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

- `project-docs/WP-006_TASK_CONTRACT.md` defines Objective, Scope, Out of Scope,
  Acceptance Criteria, Permission Level, Required Evidence / Tests, Rollback,
  Stop Conditions, Project Owner approval gates, Level 3 protections, role
  boundary enforcement, audit evidence requirements, explicit blocked/fail
  behavior, no secret exposure, and no bypass via Telegram/Desktop/GitHub
  comments/Skills.
- `project-docs/06_SECURITY_GATES_AUDIT_POLICY.md` exists and defines audit
  evidence format, retention, and fail-closed behavior.
- `project-docs/AI_ACTIVE_TASK.md` identifies WP-006 as active implementation
  and stops all restore/migration/cutover/DR work.
- No repository code, runtime files, or secrets are modified outside approved docs
  scope.
- The contract is reviewable as docs-only evidence on the implementation branch.

## Permission Level

- Level 0 reads: allowed automatically.
- Level 1 development writes: allowed only inside approved WP-006 docs/implementation scope on branch `ai/wp-006-security-gates-implementation`.
- Level 2 integration writes: authorized only for the following
  implementation actions on branch `ai/wp-006-security-gates-implementation`:
  - push the implementation branch,
  - create/update PR #22,
  - run approved tests,
  - record Issue #20 audit/handoff evidence.
- Level 2 does NOT authorize merge, deploy, production change, credential change,
  restore, migration, cutover, DR rehearsal, or any Level 3 action.
- Level 3 actions: not authorized in this WP; restore, migration, cutover, DR,
  deployment, and production changes remain explicitly deferred and require
  explicit Project Owner approval per phase.

## Required Evidence / Tests

- Implementation/docs completeness check: required files exist and cover required
  sections.
- No-secret check: no `.env`, tokens, passwords, private keys, OAuth secrets,
  or session secrets are introduced.
- Diff review: `git diff --check` passes.
- Review handoff updated when contract is finalized.

## Rollback

- Revert the implementation branch or delete the branch if scope drifts.
- Repository changes can be reverted through Git.
- Existing valid backups must not be deleted.
- No runtime state is modified by this WP.

## Stop Conditions

Stop if:

- scope expands beyond approved WP-006 implementation scope;
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
- During Phase 6 implementation, the implementation branch commit and PR are the reviewable evidence.

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

## Project Owner Approval Record

- Task ID: 20
- Action: WP-006 implementation
- Branch: ai/wp-006-security-gates-implementation
- Approval: Project Owner approved implementation via chat authorization.
- Timestamp: 2026-08-31
- Outcome: APPROVED
