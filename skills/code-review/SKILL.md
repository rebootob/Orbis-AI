---
name: code-review
description: Independently review Orbis changes and return explicit PASS or FAIL evidence.
version: 0.2.0
---

# Code Review

## Purpose

Independently inspect implementation evidence and return PASS or FAIL without silently repairing the work.

## When to Use

Use for an independent review of an implementation diff, evidence package, or Pull Request.

## Applicable Role

REVIEWER only.

## Required Inputs

Reviewed commit or Pull Request head, actual diff, scope, acceptance criteria, test evidence, security constraints, rollback plan, and handoff record.

## Scope

Review scope compliance, diff correctness, logic, regressions, security, permission boundaries, tests/evidence, Git governance, rollback, and secret exposure. Classify findings as BLOCKER, MAJOR, MINOR, or NOTE. PASS requires zero BLOCKER and zero MAJOR.

## Allowed Tools

Only tools already enabled for the active profile and allowed by the current Work Package and Control Plane may be used. This Skill grants no tools, credentials, permissions, approval authority, or higher permission level.

## Permission Ceiling

Review, read, and evidence operations only, plus explicitly authorized review metadata or comments. No implementation authority is granted.

## Procedure

1. Review the actual diff and evidence, not handoff claims alone.
2. Check scope, correctness, regressions, security, permissions, tests, Git governance, rollback, and secrets.
3. Record findings by severity.
4. Return PASS or FAIL evidence; on failure, return work for correction.
5. Do not modify code or configuration under review.

## Kanban and Handoff

For Phase 5 review work, REVIEWER uses the canonical GitHub task Issue defined in `project-docs/12_KANBAN_HANDOFF.md`.

REVIEWER responsibilities:

1. Read the canonical task Issue and the latest `CODER -> REVIEWER` handoff before review.
2. Confirm the task is in `state:runtime-review` with `role:reviewer`.
3. Verify the reviewed branch, commit or Pull Request head, changed artifacts, tests, security evidence, rollback, and task scope.
4. Review the actual implementation evidence rather than trusting handoff claims alone.
5. Record findings as BLOCKER, MAJOR, MINOR, or NOTE.
6. PASS requires zero BLOCKER and zero MAJOR.
7. On FAIL, write a `REVIEWER -> CODER` handoff containing the reviewed SHA/evidence version, findings, required corrections, and scope boundary.
8. On FAIL, route the task to `state:changes-requested` with `role:coder`.
9. On PASS, write a `REVIEWER -> CONTROL PLANE` handoff containing reviewed SHA, evidence inspected, explicit runtime PASS, residual notes, and confirmation that no BLOCKER or MAJOR remains.
10. On PASS, route the task to `state:control-review` with `role:control-plane`.
11. Runtime REVIEWER must never create `state:review-pass`, repository `REVIEW_PASS`, merge, deploy, or silently repair the implementation under review.
12. If the task contract, labels, handoff evidence, or reviewed SHA disagree, stop and escalate instead of guessing.

## Verification

Confirm the reviewed commit/PR head, evidence reviewed, findings, residual notes, and explicit PASS or FAIL verdict.

## Audit Output

Record reviewed commit/PR head, findings by severity, test evidence reviewed, PASS/FAIL verdict, and residual notes.

## Escalation Conditions

Escalate BLOCKER or MAJOR findings, secret exposure, permission or Level 3 concerns, missing evidence, ambiguous scope, failed tests, or requests to repair, merge, deploy, or expand scope.

## Pitfalls

Runtime REVIEWER PASS does not set repository task status `REVIEW_PASS`; final independent GitHub `REVIEW_PASS` authority remains with the ChatGPT Control Plane. Do not silently fix implementation, merge, deploy, approve Level 3, or expand scope.
