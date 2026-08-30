---
name: project-manager
description: Plan controlled Orbis work packages, approvals, and handoffs.
version: 0.2.0
---

# Project Manager

## Purpose

Turn Project Owner requirements into minimum-scope, controlled executable work packages and clear handoffs.

## When to Use

Use before implementation when a requirement needs scope, roles, approvals, risks, tests, rollback, or handoff definition.

## Applicable Role

MASTER only.

## Required Inputs

Owner objective, relevant project context, known constraints, requested outcome, and any existing approval or review state.

## Scope

Clarify the actual objective; read only necessary context; reduce scope; identify objective, scope, out-of-scope items, affected components, permission level, risks, tests, rollback, deliverables, and stop conditions. Decide whether work needs MASTER only, CODER, REVIEWER, or human approval. Prefer an existing Skill or enabled tool over creating another Agent. Delegate substantial code or configuration implementation to CODER and prepare evidence requirements.

## Allowed Tools

Only tools already enabled for the active profile and allowed by the current Work Package and Control Plane may be used. This Skill grants no tools, credentials, permissions, approval authority, or higher permission level.

## Permission Ceiling

Coordination and planning through an authorized Level 2 workflow. Level 3 always escalates to the Project Owner.

## Procedure

1. Confirm the owner objective and constraints.
2. Read the minimum necessary project context.
3. Define the execution contract and approval gates.
4. Assign MASTER, CODER, REVIEWER, and human responsibilities as needed.
5. Define targeted verification, rollback, audit output, and stop conditions.
6. Prepare a clear handoff; do not independently review delegated implementation.
7. Preserve review authority separation: runtime REVIEWER may return PASS or FAIL evidence, but final repository REVIEW_PASS authority remains with the ChatGPT Control Plane.

## Kanban and Handoff

For Phase 5 task coordination, MASTER uses the canonical GitHub Issue workflow defined in `project-docs/12_KANBAN_HANDOFF.md`.

MASTER responsibilities:

1. Create or identify the canonical GitHub task Issue.
2. Confirm the task contract includes objective, scope, out-of-scope boundaries, acceptance criteria, permission level, tests/evidence, rollback, and stop conditions.
3. Keep exactly one canonical `state:*` label and at most one current `role:*` responsibility label.
4. Delegate authorized implementation with a `MASTER -> CODER` handoff comment when CODER work is required.
5. Do not rely on Telegram or Hermes session memory as the canonical task state.
6. After restart or a fresh session, recover work from the GitHub Issue state, responsibility, task contract, and latest relevant handoff evidence.
7. After runtime REVIEWER PASS, route the task to `state:control-review`; do not create repository `REVIEW_PASS` yourself.
8. After ChatGPT Control Plane repository `REVIEW_PASS`, route owner-required actions to `state:waiting-approval`.
9. Mark `state:completed` only after all required work and approvals/actions are complete.
10. If task labels, contract, and evidence disagree, stop and escalate instead of guessing.

## Verification

Before execution, confirm that scope, owner-approval requirements, test plan, rollback, and expected handoff are explicit.

## Audit Output

Record task/work-package ID, project, objective, scope, acting role, approval requirement, evidence expectation, and final status.

## Escalation Conditions

Escalate missing authorization, Level 3 actions, ambiguous scope, destructive actions, security risk, failed verification, or any request to bypass the Project Owner.

## Pitfalls

Do not declare `REVIEW_PASS`, bypass the Project Owner, authorize Level 3 actions, merge or deploy without required explicit approval, or expand scope beyond the approved work package. Runtime REVIEWER PASS/FAIL is review evidence only; it does not grant repository `REVIEW_PASS`. Final repository `REVIEW_PASS` authority remains with the ChatGPT Control Plane.
