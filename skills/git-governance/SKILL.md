---
name: git-governance
description: Enforce Orbis branch safety, review separation, rollback, and auditability.
version: 0.2.0
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

Use `rebootob/Orbis-AI`; treat `main` as stable/approved, `develop` as integration, `ai/codex-*` as explicitly authorized Codex execution work, `ai/manual-*` as ChatGPT-guided manual execution work, `feature/*` as human feature work, and `hotfix/*` as emergency only. Significant changes use Pull Requests targeting `develop`; inspect diff before commit and perform a secret check before push.

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

## Role Identity Preservation

This shared Skill provides governance guidance only; it does not assign or combine runtime roles.

- The active Hermes profile/role remains authoritative.
- MASTER must identify as MASTER only.
- CODER must identify as CODER only.
- REVIEWER must identify as REVIEWER only.
- A role may describe another role's responsibilities without adopting that role.
- Never combine role labels such as `MASTER / REVIEWER` or `CODER / REVIEWER`.
- Using a shared Skill does not change the active role or grant another role's authority.

## Authority Separation

- Runtime REVIEWER may return PASS or FAIL review evidence.
- Runtime REVIEWER does not set repository `REVIEW_PASS`.
- Final repository `REVIEW_PASS` authority belongs to the ChatGPT Control Plane.
- Merge authorization belongs to the Project Owner and requires explicit approval.
- Level 3 authorization belongs to the Project Owner and requires explicit approval.
- Review PASS, including runtime REVIEWER PASS, never authorizes merge or deployment by itself.

## Kanban Task Linkage

For Phase 5, Git evidence must remain traceable to the canonical GitHub task Issue defined in `project-docs/12_KANBAN_HANDOFF.md`.

Git governance requirements:

1. Every implementation branch used for an Orbis task must be traceable to its canonical `ORBIS-TASK-#<issue-number>`.
2. Handoff evidence must record the exact branch and relevant commit SHA.
3. When a Pull Request exists, record its number or URL in the task handoff evidence.
4. REVIEWER must review the actual PR/head SHA or exact commit identified in the handoff.
5. A later commit invalidates an earlier review verdict for changed content and requires review of the new head.
6. Runtime REVIEWER PASS must record the reviewed SHA before routing to `state:control-review`.
7. ChatGPT Control Plane repository review must use the actual current PR head as authoritative.
8. Merge authorization is separate from review and requires explicit Project Owner approval.
9. Do not force-push or rewrite reviewed history to make evidence appear consistent.
10. If Task ID, branch, commit, PR head, or handoff evidence disagree, stop and report the mismatch instead of guessing.
11. After merge, record the resulting merge commit or final integrated SHA in the task outcome when applicable.
12. Git history and task comments are audit evidence; do not silently delete or rewrite them.

## Verification

Confirm branch model, reviewed SHA, review status, final repository REVIEW_PASS authority, owner merge approval when applicable, and rollback readiness.

## Audit Output

Record repository, source branch, target branch, head SHA, reviewed SHA, merge approval, merge result, and rollback reference.

## Escalation Conditions

Escalate force-push requests, destructive history actions, missing merge approval, reviewed-head changes, security findings, branch conflicts, or unclear rollback.

## Pitfalls

Never force push, rewrite history, silently discard work, merge without explicit owner approval, or treat `REVIEW_PASS` as merge authorization. A stale self-referential `REVIEW_HANDOFF` head is a NOTE unless it creates substantive ambiguity.
