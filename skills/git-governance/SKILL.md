---
name: git-governance
description: Enforce Orbis branch safety, review separation, rollback, and auditability.
version: 0.1.0
---

# Git Governance

## Purpose

Enforce the Orbis Git workflow, branch safety, review separation, rollback, and auditability.

## When to Use

Use for branch selection, commit/push preparation, Pull Request handoff, review state, merge approval, or rollback decisions.

## Applicable Role

MASTER, CODER, and REVIEWER.

## Required Inputs

Repository, source branch, target branch, current head SHA, Work Package, review state, approval state, and rollback plan.

## Scope

Use `rebootob/Orbis-AI`; treat `main` as stable/approved, `develop` as integration, `ai/codex-*` as Codex execution work, `feature/*` as human feature work, and `hotfix/*` as emergency only. Significant changes use Pull Requests targeting `develop`; inspect diff before commit and perform a secret check before push.

## Allowed Tools

Only tools already enabled for the active profile and allowed by the current Work Package and Control Plane may be used. This Skill grants no tools, credentials, permissions, approval authority, or higher permission level.

## Permission Ceiling

Normal authorized branch, commit, and push workflow up to Level 2. Force push, destructive history actions, and other Level 3 actions are not authorized.

## Procedure

1. Confirm repository, source/target branches, Work Package, and current head.
2. Keep normal work off `main` and normal implementation off `develop`.
3. Inspect diff and run secret-safety checks before push.
4. Use a Pull Request for significant changes and keep review separate from merge.
5. Re-review if the reviewed PR head changes; the actual GitHub PR head is authoritative over a stale handoff SHA.
6. Merge only with explicit owner approval; treat deployment as separate authorization.
7. Prefer commit/PR revert or documented branch rollback without destroying unrelated history.

## Verification

Confirm branch model, reviewed SHA, review status, owner merge approval when applicable, and rollback readiness.

## Audit Output

Record repository, source branch, target branch, head SHA, reviewed SHA, merge approval, merge result, and rollback reference.

## Escalation Conditions

Escalate force-push requests, destructive history actions, missing merge approval, reviewed-head changes, security findings, branch conflicts, or unclear rollback.

## Pitfalls

Never force push, rewrite history, silently discard work, merge without explicit owner approval, or treat `REVIEW_PASS` as merge authorization. A stale self-referential `REVIEW_HANDOFF` head is a NOTE unless it creates substantive ambiguity.
