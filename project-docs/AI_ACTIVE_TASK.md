# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-005A-KANBAN-HANDOFF-FOUNDATION

STATUS:
REVIEW_REQUESTED

CURRENT PHASE:
Phase 5 — Kanban & Handoff

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution. Codex is not used.

BASE BRANCH:
develop

BASE COMMIT:
53fd0c7089ca5c4e35966d436f6315217fa883c2

WORKING BRANCH:
ai/manual-wp-005a-kanban-handoff

TARGET:
develop

## Objective

Define the minimum complete task-state and handoff foundation so MASTER,
CODER, REVIEWER, ChatGPT Control Plane, and the Project Owner can coordinate
durable work without relying on chat-session memory.

## Foundation Decision

- GitHub Issue = canonical task record.
- Issue body = task contract.
- `state:*` label = canonical task state.
- `role:*` label = current responsibility.
- Issue comments = chronological handoff and audit evidence.
- Branch / commit / Pull Request = implementation evidence when applicable.
- No custom Kanban database or application.

## Scope

- Define task identity and task contract.
- Define Kanban states and transition rules.
- Define responsibility labels.
- Define handoff format between roles.
- Define REVIEWER FAIL return loop.
- Define REVIEWER PASS → Control Plane review flow.
- Define restart/resume procedure.
- Resolve Kanban and handoff `<TO_BE_DEFINED>` documentation.
- Align approval rules with Phase 4 authority model.
- Prepare Issue template.
- Update Core Skills for Phase 5 behavior.
- Prepare independent review handoff.
- Define the Phase 5 Hermes Desktop integration requirement for WP-005B:
  Desktop must operate as an optional operator console connected to the existing
  WSL2 Hermes runtime, not as a separate Orbis runtime.

## Authority Model

- MASTER plans, creates, coordinates, and delegates tasks.
- CODER implements authorized scope and cannot self-approve.
- Runtime REVIEWER returns PASS or FAIL evidence only.
- Runtime REVIEWER PASS moves work to Control Plane review.
- Final repository `REVIEW_PASS` belongs to ChatGPT Control Plane.
- Merge requires explicit Project Owner approval.
- Level 3 actions require explicit Project Owner approval.

## Expected States

- `state:ready`
- `state:in-progress`
- `state:runtime-review`
- `state:changes-requested`
- `state:control-review`
- `state:review-pass`
- `state:waiting-approval`
- `state:blocked`
- `state:completed`

## Out of Scope

- Live Hermes runtime Skill deployment in WP-005A.
- Hermes Desktop installation or runtime connection in WP-005A.
- End-to-end Hermes execution test.
- Custom Kanban UI or database.
- GitHub Projects requirement.
- n8n or MCP.
- Kintone.
- Project Registry.
- Cron / background automation.
- Additional agents or gateways.
- Production deployment.

## Tests Required

- `git diff --check`
- changed-file scope verification
- state-label uniqueness check
- required handoff-path verification
- REVIEWER PASS cannot directly create repository REVIEW_PASS
- merge / Level 3 authority verification
- secret-safety inspection before push

## Rollback

Revert the WP-005A repository commit.

WP-005A performs no Hermes runtime deployment and no production change.

## Next Step

Independent ChatGPT review of the WP-005A Pull Request.

Do not begin WP-005B runtime integration until WP-005A is reviewed and merged.

## Stop Conditions

Stop if:

- custom database or custom Kanban application becomes necessary;
- authority boundaries become ambiguous;
- runtime deployment is required before WP-005A review;
- secret exposure is detected;
- scope expands into Phase 6 or later work.
