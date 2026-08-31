# AI Review Gateway

This directory is the permanent GitHub-based communication gateway between Codex (implementation/execution) and the independent ChatGPT Reviewer (project lead, architect, and reviewer). It contains review metadata only; source changes remain reviewable through Git commits and pull requests.

Before executing a Work Package, Codex must read `AGENTS.md` → `project-docs/00_CONTROL/START_HERE.md` → `project-docs/00_CONTROL/CURRENT_STATE.md` → `project-docs/00_CONTROL/ACTIVE_TASK.md` → `project-docs/00_CONTROL/DOCUMENT_INDEX.md`, then execute only the assigned scope.

## Normal workflow

1. Codex implements and tests a work package on `ai/codex-<work-package>`.
2. Codex inspects the diff, runs security/secret checks, commits, and pushes the branch.
3. Codex pushes the branch; GitHub Actions creates or maintains its Pull Request to `develop`.
4. Codex updates [REVIEW_HANDOFF.md](REVIEW_HANDOFF.md) truthfully and sets `REVIEW STATUS` to `REVIEW_REQUESTED`. If a PR number is not available locally, use `PULL REQUEST: AUTO_DISCOVER`; ChatGPT discovers it by source branch.
5. The project owner says only `review`.
6. ChatGPT inspects GitHub directly: this handoff, the active task, the referenced pull request and diff, relevant architecture/security policies, tests, and branch/commit state.
7. ChatGPT returns `REVIEW PASS`, `REQUEST CHANGES`, or `BLOCKED`.

The project owner does not need to manually copy routine terminal output, screenshots, diffs, or implementation reports between Codex and ChatGPT.

## Review contract

Before requesting review, Codex must finish scope, run relevant tests, inspect the diff, run security checks, commit, push, and update the handoff. GitHub Actions creates or maintains the Pull Request. Codex may set only `NOT_READY`, `REVIEW_REQUESTED`, or `CHANGES_REQUESTED`; only the independent reviewer may set `REVIEW_PASS`.

The reviewer uses these severities: **BLOCKER** (must fix before merge), **MAJOR** (normally must fix), **MINOR**, and **NOTE**. A review can pass only with zero BLOCKER and zero MAJOR findings.

On failure: ChatGPT requests changes; Codex fixes, retests, pushes, updates the handoff, and requests review again. Repeat until pass.

## Security

Never place passwords, API keys, Telegram/Kintone/GitHub tokens, OAuth credentials, cookies, private keys, `.env` values, credentials, production secrets, or sensitive runtime data here. Keep summaries concise and point reviewers to the relevant source and pull request instead of pasting large logs.
