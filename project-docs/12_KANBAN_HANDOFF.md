# Kanban and Handoff

## Purpose

Phase 5 provides a durable task workflow for Orbis AI so MASTER, CODER,
REVIEWER, ChatGPT Control Plane, and the Project Owner can coordinate work
without depending on chat-session memory.

GitHub Issues are used instead of creating a custom Kanban system.

## Canonical Task Store

- GitHub Issue = canonical task record
- Issue body = task contract
- `state:*` label = current Kanban state
- `role:*` label = current responsibility
- Issue comments = chronological handoff and audit evidence
- Branch / commit / Pull Request = implementation evidence when applicable

Hermes memory and Telegram chat are not the canonical task state.

## Task Identity

Canonical task ID:

`ORBIS-TASK-#<GitHub-Issue-Number>`

Example:

`ORBIS-TASK-#25`

## Task Contract

Every task must define:

- Objective
- Scope
- Out of Scope
- Acceptance Criteria
- Permission Level
- Required Evidence / Tests
- Rollback
- Stop Conditions

## Kanban States

Exactly one `state:*` label represents the current state.

- `state:ready`
- `state:in-progress`
- `state:runtime-review`
- `state:changes-requested`
- `state:control-review`
- `state:review-pass`
- `state:waiting-approval`
- `state:blocked`
- `state:completed`

## Responsibility Labels

Use at most one:

- `role:master`
- `role:coder`
- `role:reviewer`
- `role:control-plane`
- `role:owner`

The responsibility label identifies who acts next. It does not grant extra authority.

## Normal State Flow

READY
→ IN_PROGRESS
→ RUNTIME_REVIEW

If REVIEWER FAIL:

RUNTIME_REVIEW
→ CHANGES_REQUESTED
→ IN_PROGRESS
→ RUNTIME_REVIEW

If REVIEWER PASS:

RUNTIME_REVIEW
→ CONTROL_REVIEW
→ REVIEW_PASS
→ COMPLETED

If owner approval is required:

REVIEW_PASS
→ WAITING_APPROVAL
→ COMPLETED

`state:blocked` may interrupt any non-terminal state when work cannot safely continue.

## Review Authority

Runtime REVIEWER:

- returns PASS or FAIL evidence
- does not modify implementation under review
- returns failed work to CODER

Runtime REVIEWER PASS does not create repository `REVIEW_PASS`.

Final repository `REVIEW_PASS` belongs to ChatGPT Control Plane.

Merge and Level 3 actions require explicit Project Owner approval.

## Handoff Record

Every role transition must create an Issue comment with:

- Task ID
- From role
- To role
- New state
- Objective / requested action
- Evidence
- Risks / blockers
- Next action
- Stop condition

Never include secrets in a handoff.

## Required Handoff Paths

MASTER → CODER

CODER → REVIEWER

REVIEWER → CODER on FAIL

REVIEWER → CONTROL PLANE on PASS

CONTROL PLANE → MASTER

MASTER → OWNER when approval is required

## Resume After Restart

MASTER must be able to resume from GitHub without relying on old chat history.

Recovery procedure:

1. Query open Orbis task Issues.
2. Read the current `state:*` label.
3. Read the current `role:*` label.
4. Read the task contract.
5. Read recent handoff/review comments.
6. Verify branch, commit, or PR evidence when applicable.
7. Continue only the next authorized action.

If task state and evidence disagree, stop and report the inconsistency.

## Phase 5 Scope Boundary

Phase 5 does not implement:

- custom Kanban UI
- custom task database
- n8n
- MCP
- Kintone
- Project Registry
- Cron
- additional agents
- production deployment automation
