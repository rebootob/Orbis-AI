---
name: Orbis Task
about: Canonical task record for Orbis AI work
title: "[ORBIS-TASK] "
labels: ""
assignees: ""
---

# Orbis Task Contract

## Objective

Describe the exact outcome required.

## Scope

-

## Out of Scope

-

## Acceptance Criteria

- [ ] Required outcome is implemented or completed.
- [ ] Scope boundaries are respected.
- [ ] Required tests or evidence are recorded.
- [ ] Security and permission requirements are satisfied.
- [ ] Rollback path is known.

## Permission Level

Specify the highest expected level:

`L0 / L1 / L2 / L3`

If L3 is involved, explicit Project Owner approval is required before that action.

## Required Evidence / Tests

-

## Rollback

Describe how the task can be safely reverted or recovered.

## Stop Conditions

Stop and escalate if:

- scope becomes materially ambiguous;
- required authorization is missing;
- a secret or security issue is found;
- a Level 3 action is reached without explicit Project Owner approval;
- required evidence cannot be produced;
- continuing would expand beyond the approved task.

## Initial State

`state:ready`

## Initial Responsibility

`role:master`

## Handoff Rule

Progress and role transitions must be recorded through GitHub Issue comments.

Runtime REVIEWER PASS is evidence only.

Final repository `REVIEW_PASS` belongs to ChatGPT Control Plane.

Merge and Level 3 authorization remain Project Owner decisions.

Do not place passwords, tokens, credentials, `.env` values, private keys,
Telegram IDs, or other secrets in this Issue.
