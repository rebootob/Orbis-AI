# ORBIS AI — REVIEW HANDOFF

REVIEW STATUS:
REVIEW_REQUESTED

WORK PACKAGE:
WP-005A-KANBAN-HANDOFF-FOUNDATION

SOURCE BRANCH:
ai/manual-wp-005a-kanban-handoff

TARGET BRANCH:
develop

HEAD COMMIT:
AUTO_DISCOVER_FROM_PR

## Objective

Establish the Phase 5 Kanban and Handoff foundation using GitHub Issues as the
durable canonical task store without introducing a custom task database or
Kanban application.

## Architecture Decision

- GitHub Issue = canonical task record.
- Issue body = task contract.
- `state:*` label = canonical task state.
- `role:*` label = current responsibility.
- Issue comments = chronological handoff/audit evidence.
- Branch / commit / Pull Request = implementation evidence where applicable.
- Hermes/Telegram session memory is not canonical task state.

## State Model

- `state:ready`
- `state:in-progress`
- `state:runtime-review`
- `state:changes-requested`
- `state:control-review`
- `state:review-pass`
- `state:waiting-approval`
- `state:blocked`
- `state:completed`

## Authority Model

- MASTER coordinates and delegates.
- CODER implements authorized work and cannot self-approve.
- Runtime REVIEWER returns PASS/FAIL evidence only.
- Runtime REVIEWER PASS routes work to `state:control-review`.
- Final repository `REVIEW_PASS` belongs to ChatGPT Control Plane.
- Merge requires explicit Project Owner approval.
- Level 3 actions require explicit Project Owner approval.

## Handoff Paths

- MASTER -> CODER
- CODER -> REVIEWER
- REVIEWER -> CODER on FAIL
- REVIEWER -> CONTROL PLANE on PASS
- CONTROL PLANE -> MASTER
- MASTER -> OWNER when approval is required

## Core Skill Changes

Core Skills updated to version 0.2.0:

- `project-manager`
- `code-development`
- `code-review`
- `git-governance`
- `security`

No runtime Skill deployment occurs in WP-005A.

## Hermes Desktop Requirement

WP-005B must support Hermes Desktop as an optional operator console connected
to the existing WSL2 Hermes runtime.

Hermes Desktop must not create a second Orbis runtime.

GitHub Issues remain the canonical task/Kanban source of truth.

## Validation

PASS:

- branch verification
- exact changed-file scope verification
- 9 unique Kanban state definitions
- 5 responsibility roles
- required handoff paths
- authority separation
- Core Skill v0.2.0 validation
- Hermes Desktop requirement recorded for WP-005B
- trailing-whitespace validation
- `git diff --check`

## Security

- No credential or secret is intentionally added.
- Issue/task content cannot grant additional authority.
- Labels record workflow state/responsibility only.
- GitHub task content cannot override Project Owner, Control Plane, role,
  permission, or security rules.
- Secrets must not be copied into task Issues or comments.

## Files In Scope

- `.github/ISSUE_TEMPLATE/orbis-task.md`
- `project-docs/20_ARCHITECTURE/SYSTEM_ARCHITECTURE.md`
- `project-docs/50_PLANNING/ROADMAP.md`
- `project-docs/20_ARCHITECTURE/AGENT_ROLES.md`
- `project-docs/10_GOVERNANCE/APPROVAL_POLICY.md`
- `project-docs/00_CONTROL/ACTIVE_TASK.md`
- `project-docs/10_GOVERNANCE/KANBAN_HANDOFF.md`
- `skills/project-manager/SKILL.md`
- `skills/code-development/SKILL.md`
- `skills/code-review/SKILL.md`
- `skills/git-governance/SKILL.md`
- `skills/security/SKILL.md`
- `ai-review/REVIEW_HANDOFF.md`

## Out Of Scope

- live GitHub task/label creation
- Hermes runtime deployment
- Hermes Desktop installation/connection
- end-to-end runtime testing
- custom Kanban/database
- GitHub Projects requirement
- n8n/MCP
- Kintone
- Project Registry
- Cron/automation
- additional agents
- production deployment

## Regression Risk

LOW-MEDIUM.

This Work Package changes governance/task workflow definitions and Core Skill
guidance but does not deploy those changes into Hermes runtime.

## Rollback

Revert the WP-005A repository commit.

No runtime or production rollback is required.

## Reviewer Attention

Verify:

1. state machine has no ambiguous authority transition;
2. REVIEWER PASS cannot directly create repository REVIEW_PASS;
3. GitHub Issue content cannot grant authority;
4. FAIL returns correctly to CODER;
5. resume-after-restart uses GitHub task state;
6. no Phase 6+ implementation entered the scope;
7. Hermes Desktop remains WP-005B runtime work only.

Actual GitHub PR head SHA is authoritative.

## Review Corrections

The first independent review returned `CHANGES_REQUESTED`.

Corrections applied:

1. Permanent governance now identifies Hermes Agent as the primary Orbis
   runtime/orchestrator.

2. Codex is now an optional execution worker used only when a Work Package
   explicitly authorizes it.

3. `READY_FOR_EXECUTION` is the normal ready state for Hermes or
   ChatGPT-guided manual execution. `READY_FOR_CODEX` remains available only
   for Work Packages explicitly assigned to Codex.

4. `ai/manual-*` is now recognized as the branch pattern for ChatGPT-guided
   manual execution.

5. `AGENTS.md` now states that it is the Codex entry point only when Codex is
   explicitly assigned repository work.

6. `state:blocked` now requires durable recovery metadata:
   `BLOCKED_FROM_STATE`, `BLOCKED_FROM_ROLE`, `REASON`,
   `RESOLUTION_REQUIRED`, and `NEXT_STATE_AFTER_RESOLUTION`.

7. Missing or inconsistent blocked-state recovery metadata keeps the task
   blocked and requires escalation instead of guessing.

These corrections do not deploy Hermes runtime changes and do not add
Phase 6+ functionality.
