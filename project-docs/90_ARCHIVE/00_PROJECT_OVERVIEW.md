# Project Overview

**Project:** Orbis AI
**Official source-control repository:** `https://github.com/rebootob/Orbis-AI.git`

## Purpose

Orbis AI will provide a small, auditable personal AI operating model. Hermes will orchestrate work; Telegram will provide remote commands; Git will preserve source history, reviewability, and rollback.

## V1 principles

1. Simplicity before feature breadth.
2. Reliability and security before autonomy.
3. Maintainable, documented decisions.
4. Reversible changes through Git and backups.
5. Gradual expansion after tested foundations.

## V1 scope

Hermes, Telegram, MASTER/CODER/REVIEWER roles, Skills, Git, Kanban, security and approval policies, auditability, and backup/recovery procedures.

## Deferred scope

V1.5 may add n8n, MCP, Cron, and monitoring. V2 may add Kintone, multi-model analysis, advanced routing/automation, and a dashboard only if justified.

## Repository conventions

- Documentation is the source of truth for governance and architecture.
- `main` is the stable, reviewed, recoverable branch; `develop` is the integration branch.
- Major work must use `feature/*`, `ai/codex-*`, or `hotfix/*` branches as appropriate, not direct development on `main`.
- Never force-push `main`; inspect the Git diff before each commit and document significant changes with a rollback path.
- Unknown deployment, identity, repository, and credential values remain `<TO_BE_DEFINED>`.
- Never store secrets, tokens, IDs, or environment-specific production data in the repository.
