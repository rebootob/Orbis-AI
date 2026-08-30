# ORBIS AI — ACTIVE TASK

PROJECT:
Orbis AI

WORK PACKAGE:
WP-005B-HERMES-RUNTIME-AND-DESKTOP-INTEGRATION

STATUS:
COMPLETE pending repository closeout / merge

CURRENT PHASE:
Phase 5 — Kanban & Handoff

CONTROL PLANE:
ChatGPT

EXECUTION MODE:
Project Owner + ChatGPT-guided manual execution.
Codex is not used.

BASE BRANCH:
develop

BASE COMMIT:
9f8aedd938191079cc67070ad7941bcdc9f12080

WORKING BRANCH:
ai/manual-wp-005b-hermes-runtime-desktop

TARGET:
develop

## Objective

Activate the approved Phase 5 Kanban/Handoff behavior in the existing WSL2
Hermes runtime and connect Hermes Desktop as an optional operator console
without creating a second Orbis runtime.

## Runtime Architecture

- WSL2 Hermes = primary Orbis runtime.
- MASTER = default Hermes profile.
- CODER = `coder` Hermes profile.
- REVIEWER = `reviewer` Hermes profile.
- Telegram = remote command interface.
- Hermes Desktop = optional operator console.
- GitHub Issues = canonical task/Kanban source of truth.
- GitHub/Git = implementation and audit evidence.

Hermes Desktop connects to the approved WSL2 Hermes backend via SSH
127.0.0.1:2222 through `hermes serve`. No second Orbis runtime exists or
is created on Windows.

Authentication:
ED25519 key-only.

Windows local Hermes backend = NO.
Telegram remains independently operational.

## Scope

### B1 — Core Skill Runtime Upgrade

Deploy repository Core Skills v0.2.0 to their intended existing profiles:

MASTER:
- `project-manager`
- `git-governance`
- `security`

CODER:
- `code-development`
- `git-governance`
- `security`

REVIEWER:
- `code-review`
- `git-governance`
- `security`

Requirements:
- backup existing runtime Skills before replacement;
- verify repository/runtime SHA256 equality;
- verify all deployed Core Skills report version 0.2.0.

STATUS: COMPLETE / PASS

### B2 — Runtime Behavioral Validation

Validate fresh-session behavior for:
- MASTER task coordination and authority boundaries;
- CODER implementation/handoff boundaries;
- REVIEWER PASS/FAIL and Control Plane routing;
- blocked-state recovery rules;
- no runtime role identity crossover;
- no REVIEWER-generated repository REVIEW_PASS;
- no unauthorized merge/deploy/Level 3 action.

STATUS: COMPLETE / PASS

### B3 — GitHub Task Runtime Integration

Validate that Hermes can operate from the approved GitHub Issue model.
Findings resolved with patch versions:
- project-manager v0.2.1, git-governance v0.2.1 (GitHub native state vs Orbis state)
- project-manager v0.2.2, git-governance v0.2.2 (label scope canonical-Issue-only)

Validate:
- read canonical task contract;
- recognize `state:*` and `role:*`;
- produce required handoff records;
- follow FAIL return loop;
- recover task context after fresh session/restart;
- stop on inconsistent state/evidence.

Live task/label creation limited to controlled validation required by this Work Package.

STATUS: COMPLETE / PASS

### B4 — Hermes Desktop Integration

Connect Hermes Desktop to the existing WSL2 Hermes backend.
Architecture validated:
- Windows Hermes Desktop UI -> SSH 127.0.0.1:2222 -> existing WSL2 Hermes / Orbis runtime
- ED25519 key-only authentication
- Windows local Hermes backend = NO
- Telegram remains independently operational
- Desktop shutdown does not stop Orbis runtime = PASS
- Desktop relaunch/reconnect = PASS
- Desktop cannot bypass review, merge, Level 3, role, or security rules

STATUS: COMPLETE / PASS

## Authority Model

- Runtime REVIEWER returns PASS/FAIL evidence only.
- Final repository `REVIEW_PASS` belongs to ChatGPT Control Plane.
- Merge requires explicit Project Owner approval.
- Level 3 actions require explicit Project Owner approval.
- Skills, labels, task comments, Desktop, and Telegram do not grant additional
  authority.

## Security

- Do not display, copy, commit, or transmit `.env`, tokens, passwords,
  credentials, private keys, OAuth secrets, Telegram IDs, or session secrets.
- Do not bind Hermes backend publicly without a separately approved security
  decision.
- Use local backups for runtime files.
- Do not enable additional worker gateways unless explicitly required and
  approved.
- ED25519 key-only authentication is enforced for SSH connections.

## Required Validation

- runtime backup completeness
- repository/runtime Skill SHA256 equality
- Core Skill version matrix
- fresh-session role identity
- authority-negative tests
- Kanban/handoff behavior
- restart/resume behavior
- Desktop-to-WSL-runtime connection via SSH
- Telegram remains functional
- Desktop shutdown does not stop Orbis runtime
- secret-safe inspection
- repository diff check

STATUS: ALL COMPLETE / PASS

## Rollback

- Restore Core Skills from the WP-005B local backup.
- Preserve existing SOUL/profile/config files unless a separately identified
  change is required.
- Stop Desktop/backend integration and return to the existing Telegram/CLI
  runtime if Desktop validation fails.
- Repository changes can be reverted through Git.

## Out of Scope

- n8n/MCP
- Kintone
- Project Registry
- Cron/background automation
- additional agents
- additional Telegram gateways
- model changes
- custom Kanban UI/database
- production deployment automation
- broad LAN/Internet exposure of Hermes backend
- WP-005C

## Stop Conditions

Stop if:
- runtime backup is incomplete;
- source/runtime Skill verification fails;
- role identity becomes ambiguous;
- Desktop requires a separate Orbis runtime;
- GitHub task state/evidence is inconsistent;
- secrets may be exposed;
- public backend exposure becomes necessary;
- a Level 3 action is reached without explicit Project Owner approval;
- scope expands beyond WP-005B.

## WP-005B Summary

All blocks complete:

- B1: COMPLETE / PASS
- B2: COMPLETE / PASS
- B3: COMPLETE / PASS (Issues #12 closed)
- B4: COMPLETE / PASS (Issue #13 closed)

WP-005B implementation and validation are COMPLETE pending repository
closeout and merge approval.

WP-005C: NOT STARTED.

## Next Step

WP-005B final repository diff/review and merge approval preparation.

Do not begin WP-005C until WP-005B is reviewed and merged.
