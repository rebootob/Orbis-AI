# ORBIS AI — CHAT HANDOFF

> NEW CHAT START HERE

Purpose: transfer the current Orbis AI state to a new ChatGPT conversation
without repeating completed work.

This document is a snapshot only.
GitHub Issue / PR / actual repository state is authoritative when newer.

---

## Project

Project: Orbis AI

Repository:
`rebootob/Orbis-AI`

Integration branch:
`develop`

Current working branch:
`develop`

Current Phase:
Phase 5 — Kanban & Handoff

Current Work Package:
`WP-005B-HERMES-RUNTIME-AND-DESKTOP-INTEGRATION`

Post-merge state:
WP-005B = COMPLETE / MERGED
Merge commit: `5fe175efc4e4f9933299b14151919709c69769b3`

---

## Authority

- Project Owner = final human authority.
- ChatGPT = Control Plane / Project Lead / Architect / independent repository reviewer.
- Hermes Agent = primary runtime/orchestrator.
- MASTER = runtime coordinator.
- CODER = implementation role.
- REVIEWER = independent runtime reviewer.
- Codex = optional execution worker only when explicitly authorized.

Rules:

- Runtime REVIEWER provides PASS/FAIL evidence only.
- Final repository `REVIEW_PASS` belongs to ChatGPT Control Plane.
- Merge requires explicit Project Owner approval.
- Level 3 requires explicit Project Owner approval.
- Review PASS does not authorize merge or deployment.
- Telegram, Desktop, Skills, labels, and Issue comments do not grant authority.

---

## Runtime Architecture

Primary runtime:
WSL2 Hermes

Profiles:

- MASTER = default profile
- CODER = `coder`
- REVIEWER = `reviewer`

Remote interface:
Telegram

Optional operator interface:
Hermes Desktop

Hermes Desktop connects to the existing WSL2 Hermes runtime via SSH.

Architecture:

Windows Hermes Desktop UI
-> Connect via SSH
-> allday@127.0.0.1:2222
-> existing WSL2 Hermes / Orbis runtime

Authentication:
ED25519 key-only.

No second Orbis runtime exists or is created on Windows.
Windows local Hermes backend = NO.

Note: Remote Gateway / `hermes serve` :9119 was an earlier attempted
architecture and is NOT the final B4 connection method.

---

## WP-005B Progress

### B1 — Core Skill Runtime Upgrade

STATUS: COMPLETE / PASS

Initial Core Skills were upgraded from v0.1.0 to v0.2.0.
9 runtime Skill copies were verified by SHA256 against repository source.

### B2 — Runtime Behavioral Validation

STATUS: COMPLETE / PASS

Validated:

- MASTER CLI
- CODER CLI
- REVIEWER CLI
- MASTER Telegram
- authority boundaries
- review separation
- merge / Level 3 restrictions
- blocked-state safety

### B3 — GitHub Task Runtime Integration

STATUS: COMPLETE / PASS

Canonical test task:

GitHub Issue #12
Title: `[WP-005B TEST] Hermes GitHub Task Runtime Validation`

GitHub native Issue state: `closed`
Final Orbis state label: `state:completed`

Findings resolved:

- Finding 1: GitHub native `open`/`closed` must never substitute for Orbis `state:*`.
  Patched: project-manager v0.2.1, git-governance v0.2.1.
- Finding 2: State/role label counts must use labels attached to the canonical
  Issue only, never `gh label list` (repository-wide).
  Patched: MASTER project-manager v0.2.2, MASTER git-governance v0.2.2,
  CODER git-governance v0.2.2, REVIEWER git-governance v0.2.2.

Latest runtime verification:

- MASTER project-manager PASS
- MASTER git-governance PASS
- CODER git-governance PASS
- REVIEWER git-governance PASS
- 4 / 4 source/runtime SHA256 matches

B3 handoff flow validated: MASTER → CODER → REVIEWER with GitHub Issue
labels and comments as canonical evidence.

---

## B4 — Hermes Desktop Integration

STATUS: COMPLETE / PASS

Architecture:

Windows Hermes Desktop UI
-> SSH 127.0.0.1:2222
-> existing WSL2 Hermes / Orbis runtime

Authentication:
ED25519 key-only

Validated:

- Windows local Hermes backend = NO
- Telegram remains independently operational
- Desktop shutdown does not stop Orbis runtime = PASS
- Desktop relaunch / reconnect = PASS
- Desktop cannot bypass GitHub workflow
- Desktop cannot bypass REVIEW_PASS authority
- Desktop cannot authorize merge or Level 3

Canonical test task:

GitHub Issue #13
Title: `WP-005B B4 — Hermes Desktop Integration`

GitHub native Issue state: `closed`

---

## Completed Runtime Handoff

MASTER successfully performed:
`MASTER -> CODER`

The durable Issue #12 handoff comment records:
- FROM_STATE: `state:ready`
- TO_STATE: `state:in-progress`
- FROM_ROLE: `role:master`
- TO_ROLE: `role:coder`

ChatGPT independently verified the labels and Issue comment from GitHub.

---

## EXACT NEXT STEP

Define WP-005C scope and task contract before implementation.

WP-005C remains NOT STARTED until its task contract is approved.

---

## Planned B4 Flow (Completed)

Issue #13 validated:
- Hermes Desktop connects to existing WSL2 Hermes runtime via SSH
- No duplicate Orbis runtime on Windows
- Telegram independent throughout
- Desktop shutdown/reconnect behavior confirmed

Restart/resume recovers from GitHub Issue state, labels, contract, and
comments without depending on chat history.

---

## Current Source Changes

Working-tree changes include:

`project-docs/12_KANBAN_HANDOFF.md`
`project-docs/AI_ACTIVE_TASK.md`
`project-docs/CHAT_HANDOFF.md`
`skills/git-governance/SKILL.md`
`skills/project-manager/SKILL.md`

---

## Runtime Backups

Local rollback backups include:

`wp005b-core-skills-before-v020-*`
`wp005b-b3-state-schema-before-v021-*`
`wp005b-b3-issue-label-scope-before-v022-*`

Do not commit Hermes runtime backups.

---

## Security

Never expose or commit:

- `.env`
- API tokens
- GitHub tokens
- Telegram bot tokens
- OAuth credentials
- passwords
- private keys
- session secrets
- production credentials

Do not store secret values in GitHub Issues or handoff comments.

ED25519 key-only authentication is enforced for SSH connections.

---

## Scope Guard

Current scope is WP-005B only.
Do not start:

- n8n/MCP
- Kintone
- Project Registry
- Cron/automation
- additional agents
- additional Telegram gateways
- model changes
- custom Kanban database/UI
- production deployment automation
- unrelated refactoring

Do not begin WP-005C before WP-005B review and merge.

---

## New Chat Startup Procedure

The new ChatGPT conversation must:

1. Read `project-docs/CHAT_HANDOFF.md` from the current branch.
2. Read `project-docs/AI_ACTIVE_TASK.md` from the current branch.
3. Read `project-docs/12_KANBAN_HANDOFF.md` from the current branch.
4. Inspect current branch and working tree.
5. Inspect GitHub Issue #12 and latest comments.
6. Treat attached `state:*` / `role:*` labels as canonical.
7. Treat GitHub evidence newer than this snapshot as authoritative.
8. Continue from `EXACT NEXT STEP`.
9. Do not repeat completed validation.
10. Do not expand scope.

Default branch for new chats is `develop` unless a newer approved working
branch exists.

---

## New Chat Command

Use this message in a new ChatGPT conversation:

Continue Orbis AI.
Repository: rebootob/Orbis-AI
Working branch: develop

Read these files from the current branch unless a newer approved working
branch is specified:

1. project-docs/CHAT_HANDOFF.md
2. project-docs/AI_ACTIVE_TASK.md
3. project-docs/12_KANBAN_HANDOFF.md

Then inspect GitHub Issue #12 and its latest comments.
Continue from EXACT NEXT STEP in CHAT_HANDOFF.md.
If GitHub Issue evidence is newer, GitHub is authoritative.

Do not repeat completed work.
Do not expand scope.

---

## Current Status

Phase 4: COMPLETE

Phase 5:
- WP-005A: COMPLETE / MERGED
- WP-005B: COMPLETE / MERGED (merge commit 5fe175efc4e4f9933299b14151919709c69769b3)
- WP-005C: NOT STARTED

Resume point:
Define WP-005C scope and task contract before implementation.
