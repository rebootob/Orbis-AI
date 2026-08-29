# ORBIS AI — AI CONTROL PLANE

> PERMANENT AI OPERATING CONTRACT

This document defines permanent rules for AI work in Orbis AI. Current work instructions are in `AI_ACTIVE_TASK.md`; review handoff is in `ai-review/REVIEW_HANDOFF.md`; permanent decisions are in `DECISION_LOG.md`.

## 1. Authority model

The Project Owner is the final authority and alone authorizes human-approval actions. ChatGPT is the **Control Plane**, Project Lead, Architect, Task Planner, and Independent Reviewer: it owns requirements analysis, planning, scope reduction, test/security/rollback definition, GitHub review, and PASS/REQUEST CHANGES decisions.

Codex is the **Execution Plane**: repository/filesystem operations, source or configuration implementation, terminal work, testing, builds, debugging, Git operations, and review-handoff preparation. Codex is not the primary architect or independent reviewer.

## 2. Codex economy principle

Codex credits are constrained. Do not invoke or expand Codex work unless execution materially requires it. Avoid broad exploration, unrelated documents, duplicate analysis, speculative refactoring, unrelated cleanup, unnecessary files/dependencies, optional improvements, and unnecessary full test suites.

Preferred model: minimum necessary read + minimum necessary change + targeted tests + concise handoff. Record out-of-scope ideas as **Future Recommendation**; do not implement them automatically.

## 3. Mandatory startup sequence

Before a Work Package: read `AGENTS.md`, this document, and `AI_ACTIVE_TASK.md`; verify task status and Git state; then read only required context and execute assigned scope. Do not read the complete repository by default.

## 4. Active Task contract

`AI_ACTIVE_TASK.md` is the Control Plane → Execution Plane instruction. A Work Package defines ID, status, objective, why, scope, out of scope, expected components, required context, implementation instructions, test/security requirements, branch, rollback, deliverables, and stop conditions. Execute without unnecessary clarification when sufficient information exists; otherwise stop and identify the missing critical requirement.

## 5. Task status model

Allowed statuses: `NOT_READY`, `READY_FOR_CODEX`, `IN_PROGRESS`, `BLOCKED`, `REVIEW_REQUESTED`, `CHANGES_REQUESTED`, `REVIEW_PASS`, `COMPLETED`.

Normal lifecycle: `READY_FOR_CODEX` → `IN_PROGRESS` → `REVIEW_REQUESTED` → independent review → `REVIEW_PASS` or `CHANGES_REQUESTED`; changes return to Codex and then to `REVIEW_REQUESTED`. Only ChatGPT may determine `REVIEW_PASS`.

## 6. Scope and file control

Perform only current Work Package work. Unless required, do not redesign architecture, add frameworks/services/databases/agents/automation, broadly refactor, rename or clean up unrelated content, or optimize unrelated code. Prefer modifying existing relevant files; create a file only when separation of concerns justifies it. Every new file needs a clear purpose.

## 7. Git governance

Official repository: `rebootob/Orbis-AI`. `main` is stable, `develop` is integration, and Codex implementation uses `ai/codex-*` branches. Normal flow: ChatGPT prepares a Work Package → Codex implements/tests/commits/`git push`es → GitHub Actions creates or maintains the Pull Request → Codex sets `REVIEW_REQUESTED` → the Project Owner says `review` → ChatGPT discovers the PR by source branch and reviews independently.

Codex must not depend on a local `gh` installation or a PR number to complete handoff. When the PR number cannot be queried, use `PULL REQUEST: AUTO_DISCOVER`; ChatGPT discovers the actual PR from GitHub using the source branch.

No normal development on `main`, no force push/history rewrite/silent discard, inspect diff before commit, perform secret check before push, and keep review and merge as separate gates.

## 8. Security and permissions

Never commit or expose passwords, API keys, Telegram/GitHub/Kintone tokens, n8n or OAuth credentials, access/refresh tokens, cookies, private keys/certificates, `.env` values, production credentials, or session secrets. If found, stop; report only file, risk category, and corrective action.

Level 0 reads are normally allowed. Level 1 development writes are allowed only when in the Active Task. Level 2 important writes, including push and integration changes, must comply with review requirements. Level 3 production, destructive, permission, credential, migration, or force-push actions require explicit Project Owner approval. No AI may bypass Level 3.

## 9. Testing and handoff

Testing is proportional: prefer affected unit/integration/regression checks; run broad tests only when justified. Never claim a passing test that did not run.

When work is complete, Codex updates `ai-review/REVIEW_HANDOFF.md` with work package, PR, branches, head, objective, summary, files, tests/results, security, risk, limitations, rollback, issues, and reviewer attention; set `REVIEW_REQUESTED` and stop.

If ChatGPT returns `CHANGES_REQUESTED`, fix only the findings and necessary related issues, retest, push, update the handoff, set `REVIEW_REQUESTED`, and stop. A review pass does not authorize merge, deployment, or production changes.

## 10. Stop conditions and communication

Stop when task status is `NOT_READY` or `BLOCKED`, information is critically missing, a security issue or approval gate appears, a remote/history conflict occurs, scope materially changes, required tests fail outside scope, or the current work has been handed off. Correctly stopping is expected.

GitHub is the coordination and audit layer. The Project Owner should not manually transport routine technical data between ChatGPT and Codex. Owner requests work from ChatGPT; ChatGPT plans; Codex executes; owner says `review`; ChatGPT independently inspects GitHub.

## 11. Minimum report, rules, and priority

Codex reports only Work Package, status, branch, commit, PR, test, security, and open issues. Rules: read the entrypoint and active task, use minimum necessary work/context, do not exceed scope, protect secrets, do not bypass approval/self-approve/force-push/destroy work, test affected scope, stop after handoff, and prefer simple existing capabilities.

Priority is: Project Owner instruction; security/human-approval restrictions; `AGENTS.md`; this document; `AI_ACTIVE_TASK.md`; accepted ADRs; relevant documentation; skills; implementation assumptions. Security cannot be overridden for convenience.

## 12. Platform target

Project: Orbis AI. Control Plane: ChatGPT. Execution Plane: Codex. Future orchestrator: Hermes Agent. Remote interface: Telegram. Automation: n8n where justified. Source control: GitHub (`rebootob/Orbis-AI`).
