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
`ai/manual-wp-005b-hermes-runtime-desktop`

Current Phase:
Phase 5 — Kanban & Handoff

Current Work Package:
`WP-005B-HERMES-RUNTIME-AND-DESKTOP-INTEGRATION`

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

Hermes Desktop must connect to the existing WSL2 Hermes runtime through
`hermes serve`.

Do not create a second Orbis runtime on Windows.

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

STATUS: IN PROGRESS

Canonical test task:

GitHub Issue #12

Title:

`[WP-005B TEST] Hermes GitHub Task Runtime Validation`

Current canonical Issue labels:

`state:in-progress`

`role:coder`

GitHub native Issue lifecycle remains:

`open`

These are different concepts.

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

## B3 Finding 1 — Fixed

Problem:

Hermes incorrectly used GitHub native Issue state:

`open`

as Orbis current task state.

Correct rule:

- GitHub native state = `open` / `closed`
- Orbis state = exact attached `state:*` label
- Orbis responsibility = exact attached `role:*` label

Patch produced:

- project-manager v0.2.1
- git-governance v0.2.1

Regression confirmed:

`CURRENT_STATE=state:in-progress`

Finding fixed.

---

## B3 Finding 2 — Patch Deployed

Problem:

Hermes correctly read the task state/role but incorrectly counted:

`STATE_LABEL_COUNT=9`

`ROLE_LABEL_COUNT=6`

Cause:

It used repository-wide:

`gh label list`

instead of labels attached to Issue #12.

Correct rule:

State/role counts and uniqueness must use labels attached to the current
canonical Issue only.

Never use repository-wide label definitions as task-state evidence.

Patch versions:

- MASTER project-manager = v0.2.2
- MASTER git-governance = v0.2.2
- CODER git-governance = v0.2.2
- REVIEWER git-governance = v0.2.2

Latest runtime verification:

- MASTER project-manager PASS
- MASTER git-governance PASS
- CODER git-governance PASS
- REVIEWER git-governance PASS
- 4 / 4 source/runtime SHA256 matches

---

## EXACT NEXT STEP

Do NOT start CODER recovery yet.

First perform the final MASTER regression for the v0.2.2 label-scope patch.

Required sequence:

1. Restart `hermes-gateway.service`.
2. Confirm gateway is active.
3. Telegram: `/reset now`
4. MASTER must re-read GitHub Issue #12.
5. Do not tell MASTER expected state, role, or counts.

Required result:

ROLE=MASTER
TASK_ID=12
GITHUB_NATIVE_STATE=open
CURRENT_STATE=state:in-progress
CURRENT_ROLE=role:coder
STATE_LABEL_COUNT=1
ROLE_LABEL_COUNT=1
LAST_HANDOFF_FROM=MASTER
LAST_HANDOFF_TO=CODER
VERDICT=PASS

If STATE_LABEL_COUNT or ROLE_LABEL_COUNT is not 1:

STOP B3 and investigate.

If this regression passes:

Proceed to CODER fresh-session recovery from GitHub Issue #12.

---

## Planned B3 Flow

Current:

Issue #12
`state:in-progress`
`role:coder`

Next:

CODER recovery
→ CODER -> REVIEWER
→ `state:runtime-review`
→ `role:reviewer`

Then validate:

REVIEWER FAIL
→ `state:changes-requested`
→ `role:coder`

and later:

REVIEWER PASS
→ `state:control-review`
→ `role:control-plane`

Restart/resume must recover from GitHub Issue state, labels, contract, and
comments without depending on chat history.

---

## B4 — Hermes Desktop

STATUS: NOT STARTED

Approved architecture:

Hermes Desktop
→ `hermes serve`
→ existing WSL2 Hermes runtime

Requirements:

- no duplicate Orbis runtime;
- Telegram remains independently operational;
- Desktop cannot bypass GitHub workflow;
- Desktop cannot bypass REVIEW_PASS authority;
- Desktop cannot authorize merge;
- Desktop cannot authorize Level 3;
- backend should remain local/private unless explicitly approved.

Do not start B4 until required B3 validation is complete.

---

## Current Source Changes

Expected working-tree changes currently include:

`project-docs/AI_ACTIVE_TASK.md`

`project-docs/12_KANBAN_HANDOFF.md`

`skills/project-manager/SKILL.md`

`skills/git-governance/SKILL.md`

This file adds:

`project-docs/CHAT_HANDOFF.md`

Do not commit or merge simply because this document exists.
Finish WP-005B validation first.

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

1. Read `project-docs/CHAT_HANDOFF.md`.
2. Read `project-docs/AI_ACTIVE_TASK.md`.
3. Read `project-docs/12_KANBAN_HANDOFF.md`.
4. Inspect current branch and working tree.
5. Inspect GitHub Issue #12 and latest comments.
6. Treat attached `state:*` / `role:*` labels as canonical.
7. Treat GitHub evidence newer than this snapshot as authoritative.
8. Continue from `EXACT NEXT STEP`.
9. Do not repeat completed validation.
10. Do not expand scope.

---

## New Chat Command

Use this message in a new ChatGPT conversation:

Continue Orbis AI.

Repository: rebootob/Orbis-AI
Working branch: ai/manual-wp-005b-hermes-runtime-desktop

Read these files from branch ai/manual-wp-005b-hermes-runtime-desktop,
NOT from develop:

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
- WP-005B B1: COMPLETE
- WP-005B B2: COMPLETE
- WP-005B B3: IN PROGRESS
- WP-005B B4: NOT STARTED
- WP-005C: NOT STARTED

Resume point:

Final MASTER regression after v0.2.2 Issue-label-scope patch.
