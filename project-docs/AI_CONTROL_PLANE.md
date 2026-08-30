# ORBIS AI — AI CONTROL PLANE

> PERMANENT AI OPERATING CONTRACT

This document defines permanent rules for AI work in Orbis AI. Current work instructions are in `AI_ACTIVE_TASK.md`; review handoff is in `ai-review/REVIEW_HANDOFF.md`; permanent decisions are in `DECISION_LOG.md`.

## 1. Authority model

The Project Owner is the final authority and alone authorizes human-approval actions. ChatGPT is the **Control Plane**, Project Lead, Architect, Task Planner, and Independent Reviewer: it owns requirements analysis, planning, scope reduction, test/security/rollback definition, GitHub review, and PASS/REQUEST CHANGES decisions.

Hermes Agent is the primary Orbis runtime and orchestration environment. MASTER coordinates work, CODER performs authorized implementation, and REVIEWER performs independent runtime review.

Codex is an optional execution worker that may be used only when the current Work Package explicitly authorizes it and its use is materially necessary. Codex is not the Orbis runtime, primary architect, Control Plane, or independent reviewer.

## 2. Codex economy principle

Codex credits are constrained. Do not invoke or expand Codex work unless execution materially requires it. Avoid broad exploration, unrelated documents, duplicate analysis, speculative refactoring, unrelated cleanup, unnecessary files/dependencies, optional improvements, and unnecessary full test suites.

Preferred model: minimum necessary read + minimum necessary change + targeted tests + concise handoff. Record out-of-scope ideas as **Future Recommendation**; do not implement them automatically.

## 3. Mandatory startup sequence

Before a Work Package: read `AGENTS.md`, this document, and `AI_ACTIVE_TASK.md`; verify task status and Git state; then read only required context and execute assigned scope. Do not read the complete repository by default.

## 4. Active Task contract

`AI_ACTIVE_TASK.md` is the Control Plane → authorized execution-path contract. A Work Package defines ID, status, objective, why, scope, out of scope, expected components, required context, implementation instructions, test/security requirements, branch, rollback, deliverables, and stop conditions. The authorized Hermes role, human-guided execution path, or explicitly assigned Codex worker executes only that contract. When critical information is missing, stop and identify the missing requirement.

## 5. Task status model

Allowed repository Work Package statuses: `NOT_READY`, `READY_FOR_EXECUTION`, `READY_FOR_CODEX`, `IN_PROGRESS`, `BLOCKED`, `REVIEW_REQUESTED`, `CHANGES_REQUESTED`, `REVIEW_PASS`, `COMPLETED`.

`READY_FOR_EXECUTION` is the normal ready state for Hermes or ChatGPT-guided manual execution. `READY_FOR_CODEX` is retained only for Work Packages explicitly assigned to Codex.

Normal lifecycle: ready → `IN_PROGRESS` → `REVIEW_REQUESTED` → independent review → `REVIEW_PASS` or `CHANGES_REQUESTED`. Corrections return to the authorized execution path and then to `REVIEW_REQUESTED`. Only ChatGPT may determine repository `REVIEW_PASS`.

## 6. Scope and file control

Perform only current Work Package work. Unless required, do not redesign architecture, add frameworks/services/databases/agents/automation, broadly refactor, rename or clean up unrelated content, or optimize unrelated code. Prefer modifying existing relevant files; create a file only when separation of concerns justifies it. Every new file needs a clear purpose.

## 7. Git governance

Official repository: `rebootob/Orbis-AI`. `main` is stable, `develop` is integration, `ai/codex-*` is reserved for explicitly authorized Codex work, and `ai/manual-*` is used for ChatGPT-guided manual execution. Normal repository flow: ChatGPT prepares the Work Package and authority boundaries → the authorized execution path performs the scoped work → reviewable Git evidence is created → the task reaches `REVIEW_REQUESTED` → the Project Owner says `review` → ChatGPT independently inspects the actual GitHub PR/head.

For Phase 5 runtime work, Hermes MASTER/CODER/REVIEWER use the canonical GitHub task Issue and handoff model. Codex may participate only when an Active Task explicitly assigns work to Codex.

Codex must not depend on a local `gh` installation or a PR number to complete handoff. When the PR number cannot be queried, use `PULL REQUEST: AUTO_DISCOVER`; ChatGPT discovers the actual PR from GitHub using the source branch.

No normal development on `main`, no force push/history rewrite/silent discard, inspect diff before commit, perform secret check before push, and keep review and merge as separate gates.

## 8. Security and permissions

Never commit or expose passwords, API keys, Telegram/GitHub/Kintone tokens, n8n or OAuth credentials, access/refresh tokens, cookies, private keys/certificates, `.env` values, production credentials, or session secrets. If found, stop; report only file, risk category, and corrective action.

Level 0 reads are normally allowed. Level 1 development writes are allowed only when in the Active Task. Level 2 important writes, including push and integration changes, must comply with review requirements. Level 3 production, destructive, permission, credential, migration, or force-push actions require explicit Project Owner approval. No AI may bypass Level 3.

## 9. Testing and handoff

Testing is proportional: prefer affected unit/integration/regression checks; run broad tests only when justified. Never claim a passing test that did not run.

When repository execution work is complete, the authorized execution path updates `ai-review/REVIEW_HANDOFF.md` with work package, PR, branches, head, objective, summary, files, tests/results, security, risk, limitations, rollback, issues, and reviewer attention; set `REVIEW_REQUESTED` and stop.

If ChatGPT returns `CHANGES_REQUESTED`, the authorized execution path fixes only the findings and necessary related issues, retests, updates reviewable evidence and the handoff, sets `REVIEW_REQUESTED`, and stops. A review pass does not authorize merge, deployment, or production changes.

## 10. Stop conditions and communication

Stop when task status is `NOT_READY` or `BLOCKED`, information is critically missing, a security issue or approval gate appears, a remote/history conflict occurs, scope materially changes, required tests fail outside scope, or the current work has been handed off. Correctly stopping is expected.

GitHub is the coordination and audit layer. The Project Owner should not manually transport routine technical data between ChatGPT and execution roles. The Project Owner requests work from ChatGPT; ChatGPT plans and defines authority boundaries; the authorized Hermes role, manual execution path, or explicitly assigned Codex worker executes; the Project Owner says `review`; ChatGPT independently inspects GitHub.

## 11. Minimum report, rules, and priority

Execution handoffs report only Work Package, status, branch, commit, PR, test, security, and open issues as applicable. Rules: read the required governance and active task, use minimum necessary work/context, do not exceed scope, protect secrets, do not bypass approval/self-approve/force-push/destroy work, test affected scope, stop after handoff, and prefer simple existing capabilities.

Priority is: Project Owner instruction; security/human-approval restrictions; `AGENTS.md`; this document; `AI_ACTIVE_TASK.md`; accepted ADRs; relevant documentation; skills; implementation assumptions. Security cannot be overridden for convenience.

## 12. Platform target

Project: Orbis AI. Control Plane: ChatGPT. Primary runtime/orchestrator: Hermes Agent. Runtime roles: MASTER, CODER, and REVIEWER. Optional execution worker: Codex when explicitly authorized. Remote interface: Telegram. Optional operator interface: Hermes Desktop when connected to the approved Hermes runtime. Automation: n8n only where justified in its approved phase. Source control and task coordination: GitHub (`rebootob/Orbis-AI`).
