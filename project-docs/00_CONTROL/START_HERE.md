# Orbis AI — Start Here

> Mandatory first read for every new ChatGPT or Hermes session.

## Project

- **Repository:** `rebootob/Orbis-AI`
- **Canonical branch:** `develop`
- **Authoritative current state:** `project-docs/00_CONTROL/CURRENT_STATE.md`

## Authority summary

- **Project Owner** is the final human authority and alone authorizes Level 3 actions and merges.
- **ChatGPT** is the Control Plane, project lead, architect, and independent repository reviewer.
- **Hermes Agent** is the primary runtime/orchestrator; MASTER, CODER, and REVIEWER retain their defined role boundaries.
- **Runtime REVIEWER** supplies evidence only; only ChatGPT Control Plane can issue repository `REVIEW_PASS`.

Read `project-docs/10_GOVERNANCE/AUTHORITY_MODEL.md` only when governance detail is relevant.

## Mandatory read order

Every new session must read exactly these documents first:

1. `project-docs/00_CONTROL/START_HERE.md`
2. `project-docs/00_CONTROL/CURRENT_STATE.md`
3. `project-docs/00_CONTROL/ACTIVE_TASK.md`
4. `project-docs/00_CONTROL/DOCUMENT_INDEX.md`

Then read **only** documents directly relevant to the active task. If `ACTIVE_WORK_PACKAGE: NONE`, do not begin work.

## Repository-truth precedence

GitHub Issue/PR metadata, comments, and the checked-out repository state are authoritative when newer than documentation. Reconcile documentation to newer repository truth; never infer approval from a stale document.

## STOP and approval rules

- Do not begin a work package without explicit Project Owner authorization recorded through the governing workflow.
- Do not merge, deploy, make production connections, perform n8n writes, change credentials, or execute Restore/DR without the required separate authorization.
- Treat the exact current gate in `CURRENT_STATE.md` and `ACTIVE_TASK.md` as binding.
- If repository evidence, task state, PR head, or approval status conflicts, STOP and escalate rather than guessing.

## Closeout rule

After each work-package merge: update `CURRENT_STATE.md`; clear or update `ACTIVE_TASK.md`; update `50_PLANNING/ROADMAP.md` only if phase state changed; update `DOCUMENT_INDEX.md` only if topology changed; retain qualifications/blockers; then STOP.
