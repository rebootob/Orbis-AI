---
name: code-development
description: Implement approved Orbis work with targeted verification and handoff.
version: 0.1.0
---

# Code Development

## Purpose

Implement an already-approved Work Package with minimum necessary changes and targeted verification.

## When to Use

Use only when the current Work Package authorizes CODER implementation work.

## Applicable Role

CODER only.

## Required Inputs

Approved Work Package, active-task status, target branch, relevant files/components, acceptance criteria, tests, rollback, and stop conditions.

## Scope

Read mandatory governance entrypoints; confirm Active Task and branch; inspect only relevant files; modify approved scope only; prefer existing implementation; run targeted tests; inspect the diff; perform a secret-safety check; commit, push, and prepare review handoff.

## Allowed Tools

Only tools already enabled for the active profile and allowed by the current Work Package and Control Plane may be used. This Skill grants no tools, credentials, permissions, approval authority, or higher permission level.

## Permission Ceiling

Authorized development writes and normal branch push up to Level 2. Any Level 3 action requires Project Owner escalation.

## Procedure

1. Read mandatory governance entrypoints and confirm the Active Task.
2. Confirm branch and approved scope.
3. Implement the minimum necessary change without speculative refactoring, unrelated cleanup, or unnecessary dependencies.
4. Run targeted tests proportional to the change.
5. Inspect the diff and changed files.
6. Run a secret-safety check before push.
7. Commit and push the approved branch, prepare review handoff, set `REVIEW_REQUESTED`, and stop.

## Verification

Record affected tests, `git diff --check`, changed-file inspection, secret-safety result, and expected-versus-actual outcome.

## Audit Output

Record changed files, tests executed, result, branch, commit, known limitations, rollback, and blockers.

## Escalation Conditions

Escalate missing authorization, Level 3 actions, destructive operations, credential or permission changes, security findings, failed verification, branch conflicts, or ambiguous scope.

## Pitfalls

Never approve or mark your own work `REVIEW_PASS`; never merge, deploy, bypass human approval, or force push.
