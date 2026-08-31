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

Canonical branch:
`develop`

Current develop baseline:
`ae9dc212bcc0e4fad78179e37e51a23625808261`

---

## Authority

- Project Owner = final human authority.
- ChatGPT = Control Plane / Project Lead / Architect / independent repository reviewer.
- Hermes Agent = primary runtime/orchestrator.
- MASTER = coordinator.
- CODER = implementation.
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
architecture and is NOT the final connection method.

---

## Completed Work Summary

### WP-005B — Core Skill Runtime Upgrade, Runtime Behavioral Validation, GitHub Task Runtime Integration, Hermes Desktop Integration

STATUS: COMPLETE / MERGED
Merge commit: `5fe175efc4e4f9933299b14151919709c69769b3`

Issue #12 = completed
Issue #13 = completed

### WP-005C — Backup / Recovery

STATUS: PARTIAL COMPLETE

Completed:

- Runtime inventory / backup design
- external credential recovery verification
- backup execution / manifest validation

Merged PRs:

- PR #17 → `3e7b990f1fb88724f0266f5bd2fbcb7d6303bb44`
- PR #18 → `a7789317931894366dba8f8d3e4b04d659ee6d4f`
- PR #19 → `6ca8d28ee43bb20569a9e328204aa1c9ff003753`

Restore / DR:
DEFERRED BY PROJECT OWNER

RESTORE_VALIDATION=NOT_STARTED
MIGRATION=NOT_STARTED
CUTOVER=NOT_STARTED

Do not claim full DR validation.

### WP-006 — Security Gates / Approval / Audit

STATUS: COMPLETE / MERGED

Planning:
PR #21 → `cf6372f9e359e409a10f895f4781b6a793e3b7c0`

Implementation:
PR #22 → `41fc3d270b6837bdfe88d39cdfdcdace1a839ac8`

Governance recovery:
PR #26 → `102a07dc3ba0460c71df7474eff272bacdd41ba1`

Permanent lesson:
documented governance != runtime-enforced governance

Runtime must never infer human approval from:
- GitHub author_association
- labels
- comments
- Hermes/Telegram/Desktop identity

### WP-007 — Project Registry

STATUS: COMPLETE / MERGED

Planning:
PR #25 → `d2aa184957dfa4b68087c6c708ec28cc84e5937d`

Implementation:
PR #27 → `6ed9a3ef1c2b7d0eed95728150315ccf7a9e3ccb`

Issue #24 = CLOSED / COMPLETED

### WP-008 — n8n via MCP

Planning:
PR #29 → `2eec0883cff47456960983d062bbce8b52c77c89`

Read-only validation inventory/evidence:
PR #30 → `ae9dc212bcc0e4fad78179e37e51a23625808261`

Current status:
SANDBOX PROVEN / AWAITING READ-ONLY VALIDATION AUTHORIZATION

Issue #28 current phase:
IMPLEMENTATION — READ-ONLY VALIDATION

Sandbox evidence:
- n8n installation = FOUND
- n8n process = PROVEN STARTABLE
- n8n configuration = LOCAL_TEST
- n8n target environment = LOCAL_TEST
- n8n version = 2.36.9
- Listen address = 127.0.0.1:5678
- Public exposure = NO
- MCP references in Hermes = FOUND
- MCP runtime capability = UNKNOWN
- MCP Python package = not importable
- MCP version = UNKNOWN
- no mcp_servers configured

Security result:
- n8n connection attempted = NO
- production touched = NO
- n8n write executed = NO
- deployment = NO

Phase 8 exit condition:
Read-only capabilities must actually pass testing before any write capability.

Next safe step:
Explicit Control Plane authorization for read-only MCP validation against proven LOCAL_TEST sandbox.

PHASE8_COMPLETE=NO

---

## Exact Current Gate

A proven LOCAL_TEST n8n sandbox exists at 127.0.0.1:5678.

Next safe work package:
WP-008 READ-ONLY MCP VALIDATION AGAINST LOCAL_TEST SANDBOX

Required authorization:
Explicit Control Plane authorization for read-only MCP validation.

Important:
THIS SANDBOX WORK IS COMPLETE.
Do not automatically start read-only MCP validation from documentation.

Future validation constraints:

- loopback/local binding only
- no public/LAN exposure
- no production workflows
- no production data
- no production credentials
- dummy/no-op test workflows only
- no Kintone
- no Telegram side effects
- no external HTTP side effects
- no cron/automation
- no Phase 9
- no Restore/DR

---

## New Chat Startup Procedure

The new ChatGPT conversation must:

1. Read `project-docs/CHAT_HANDOFF.md` from the current branch.
2. Read `project-docs/AI_ACTIVE_TASK.md` from the current branch.
3. Read `project-docs/WP-008_TASK_CONTRACT.md` from the current branch.
4. Read `project-docs/08_N8N_INTEGRATION.md` from the current branch.
5. Read `project-docs/02_IMPLEMENTATION_ROADMAP.md` from the current branch.
6. Read `project-docs/10_BACKUP_RECOVERY.md` from the current branch.
7. Read `project-docs/12_KANBAN_HANDOFF.md` from the current branch.
8. Read `project-docs/04_SECURITY_POLICY.md` from the current branch.
9. Read `project-docs/05_APPROVAL_POLICY.md` from the current branch.
10. Inspect current branch and working tree.
11. Inspect GitHub Issue #28 and latest comments.
12. Treat attached `state:*` / `role:*` labels as canonical.
13. Treat GitHub evidence newer than this snapshot as authoritative.
14. Continue from `## Exact Current Gate` / `## Next Step`.
15. Do not repeat completed validation.
16. Do not expand scope.
17. Do not start read-only MCP validation unless Control Plane explicitly authorizes it.

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
3. project-docs/WP-008_TASK_CONTRACT.md
4. project-docs/08_N8N_INTEGRATION.md
5. project-docs/02_IMPLEMENTATION_ROADMAP.md
6. project-docs/10_BACKUP_RECOVERY.md
7. project-docs/12_KANBAN_HANDOFF.md
8. project-docs/04_SECURITY_POLICY.md
9. project-docs/05_APPROVAL_POLICY.md

Then inspect GitHub Issue #28 and its latest comments.
Continue from `Exact Current Gate` in CHAT_HANDOFF.md.
If GitHub Issue evidence is newer, GitHub is authoritative.

Do not repeat completed work.
Do not expand scope.
Do not auto-start WP-008 read-only MCP validation.
Wait for explicit Control Plane instruction.

---

## Current Status Summary

- Phase 4: COMPLETE
- Phase 5:
  - WP-005A: COMPLETE / MERGED
  - WP-005B: COMPLETE / MERGED
  - WP-005C: PARTIAL COMPLETE / DEFERRED Restore-DR
- Phase 6: COMPLETE / MERGED
- Phase 7: COMPLETE / MERGED
- Phase 8: SANDBOX PROVEN / AWAITING READ-ONLY VALIDATION AUTHORIZATION
- Phase 9: NOT STARTED
- Restore/DR: NOT STARTED

Resume point:
Wait for explicit Control Plane instruction for WP-008 read-only MCP validation against proven LOCAL_TEST sandbox.
