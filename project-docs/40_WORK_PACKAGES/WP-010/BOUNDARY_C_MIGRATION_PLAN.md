# ORBIS AI — WP-010 Boundary C Migration Plan

WORK PACKAGE: WP-010
BOUNDARY: C — migration planning only
SCOPE: Planning/documentation only. No migration execution, cutover, deployment, or production writes.
STATUS: PLANNING — MIGRATION PLANNING AUTHORIZED; EXECUTION NOT AUTHORIZED

---

## 1. Objective

Define a safe, staged migration plan for Phase 10 that preserves recoverability of MASTER, CODER, and REVIEWER runtime state while minimizing disruption to the current WSL2 Hermes runtime, production integrations, and any live environment.

## 2. Boundary: Planning vs. Execution

This plan defines four distinct boundaries:

| Boundary | Description | Authorization |
|---|---|---|
| A. Planning | Document the plan, assets, sequence, evidence, and stop conditions. | Project Owner authorizes planning only. |
| B. Isolated restore rehearsal | Execute restore/disaster-recovery rehearsal in an isolated disposable target. | Separate Project Owner authorization required. |
| C. Migration | Any migration of live workload or data to a new target runtime. | Separate Project Owner authorization required. |
| D. Cutover | Switch production or canonical runtime to migrated target. | Separate Project Owner authorization required. |

This document covers **Boundary C planning only**.

## 3. Prohibited During Planning

- Live workload migration
- Production writes
- Cutover
- Replacement of current WSL2 runtime
- Credential rotation/change
- n8n production connection/write
- Telegram production change
- Deployment
- External side effects
- Service start/stop for migration purposes

## 4. Source Runtime

| Field | Value |
|---|---|
| Source host | `sleep-cat` |
| Source OS | Ubuntu 26.04.1 LTS (WSL2) |
| Hermes version | v0.20.6 (2026.8.27) |
| Source develop commit at backup time | `a7789317931894366dba8f8d3e4b04d659ee6d4f` |
| Canonical branch | `develop` |
| Current role boundary | MASTER, CODER, REVIEWER |
| Integration status | MCP runtime proven; n8n LOCAL_TEST proven; production writes NOT AUTHORIZED |

## 5. Proposed Target Runtime

| Field | Value |
|---|---|
| Target environment | To be specified by Owner |
| Target type | Separate WSL distro / VM / physical server / cloud host |
| Requirement | Must be approved isolated target; no overwrite of primary runtime |
| Network | Network-isolated unless explicitly approved for integration validation |
| Destruction | Target must be destroyable without data loss to primary runtime |

## 6. Workload/Data/Assets In Scope

| Asset | Source | Notes |
|---|---|---|
| Hermes runtime profiles | `~/.hermes/profiles/coder/`, `~/.hermes/profiles/reviewer/`, `~/.hermes/` | Config/SOUL/non-secret files only |
| Core Skills runtime copies | `~/.hermes/profiles/*/skills/` | Version matrix preserved |
| Runtime databases | `state.db`, `kanban.db`, `projects.db`, `verification_evidence.db` | SQLite; may be empty or seeded |
| Gateway service unit | `hermes-gateway.service` | Systemd user unit |
| SSH authorized keys | `~/.ssh/authorized_keys` | Public keys only |
| Repository export | `/home/allday/Orbis-AI/` | Optional; Git source of truth |

## 7. Assets Explicitly Excluded

- `.env`
- `auth.json`
- Private keys and tokens
- Session secrets
- Production credentials
- n8n production connection configs
- Telegram bot token
- GitHub token/OAuth credentials
- Quarantine content

## 8. Prerequisites

1. Boundary B isolated restore rehearsal COMPLETE with PASS results.
2. Validated backup set exists and is checksum-verified.
3. Corrective backup coverage completed for any identified gaps.
4. Target environment approved by Owner.
5. Owner explicitly authorizes Boundary C migration execution.
6. Secrets recovery procedure documented and approved.
7. Rollback point confirmed: prior known-good backup remains authoritative until post-migration acceptance passes.

## 9. Backup/Recovery Prerequisite and Rollback Point

- Accepted backup set: `20260830-231125`
- Corrective backup set: `20260830-231125-corrective`
- Secondary copy: `/mnt/d/Orbis-AI-Backup/WP-005C/20260830-231125`
- Old server remains rollback target until post-cutover acceptance passes.
- Do not delete old server until post-cutover acceptance passes.

## 10. Credential Handling Approach

- Secrets are never stored in Git, backup archives, manifests, or migration payloads.
- Recovery uses documented secure sources only.
- Migration procedure explicitly includes secret-recovery steps after non-secret assets are restored.
- Migration acceptance fails if any required credential lacks a recoverable secure source.
- No credential values are copied from primary runtime plaintext files into migration artifacts.

## 11. Dependency Order

1. Provision isolated target environment.
2. Install Hermes runtime at validated version/commit.
3. Restore system config: `hermes-gateway.service`, `sshd_config`, `authorized_keys`.
4. Restore runtime files in dependency order: SOUL/config before DBs.
5. Restore Core Skills runtime copies.
6. Recover secrets from secure stores/vaults per documented recovery procedures.
7. Start profiles and gateway; observe fresh-session startup.
8. Validate GitHub auth, Telegram, and Desktop SSH.
9. Run contract tests and acceptance checklist.
10. Keep old server available as rollback target until post-restore acceptance passes.

## 12. Migration Sequence

1. Freeze/prepare primary runtime for snapshot if required.
2. Create final pre-migration validated backup.
3. Provision target runtime.
4. Restore non-secret assets from validated backup.
5. Recover secrets via approved secure procedures.
6. Perform read-only integration validation if explicitly approved.
7. Run validation checks.
8. Record evidence.
9. Await Owner authorization for Boundary D cutover.
10. If cutover authorized, switch production/canonical runtime.
11. Run post-migration verification.
12. Retire old server only after post-cutover acceptance passes.

## 13. Pre-flight Checks

- `hermes doctor` passes on target runtime
- Basic chat validation passes
- MASTER/CODER/REVIEWER role boundaries observable
- Core Skills version matrix matches expected source/runtime SHAs
- Gateway service starts and accepts connections
- SSH key auth validated without passwords
- Kanban/handoff flow observable: MASTER → CODER → REVIEWER → MASTER
- No secret values exposed in logs, exports, or manifests
- Target runtime can be destroyed without affecting primary runtime

## 14. Validation Criteria

- All Boundary B restore checks remain PASS
- Target runtime boots cleanly with restored non-secret assets
- Skill version matrix matches expected source/runtime SHAs
- Gateway service starts and accepts connections
- SSH key auth validated without passwords
- Kanban/handoff flow observable
- No secret values exposed in logs, exports, or manifests
- Target runtime destroyable without affecting primary runtime

## 15. Rollback Procedure

- If any validation fails, stop and preserve existing running runtime.
- Target runtime must be destroyable without affecting primary runtime.
- Prior known-good backup remains authoritative until newer restore validation passes.
- No migration, cutover, or production switch occurs during planning or unauthorized execution.
- Old server remains rollback target until post-cutover acceptance passes.

## 16. Failure/Stop Conditions

Halt Phase 10 immediately if:
- Any step risks overwriting or disrupting the primary WSL2 Hermes runtime
- Secret values are exposed or improperly handled
- n8n production connection is attempted or triggered
- External side effects occur
- Validation cannot be completed in isolated environment
- Project Owner has not explicitly authorized Boundary B, C, or D
- LOCAL_TEST health remains FAIL / HTTP 000 and sandbox is unavailable unless isolated target is used instead

## 17. Production Side-Effect Controls

- No production n8n connection/write during migration planning or execution unless explicitly authorized.
- No Telegram production change.
- No GitHub credential change.
- No deployment.
- No service start/stop on primary runtime for migration purposes.
- Any target-runtime integration must be read-only unless explicitly authorized.

## 18. Integration Boundaries

| Integration | Boundary C Planning | Boundary C Execution | Boundary D Cutover |
|---|---|---|---|
| n8n | Read-only docs only | NOT AUTHORIZED without explicit approval | NOT AUTHORIZED without explicit approval |
| Telegram | No production change | NOT AUTHORIZED | NOT AUTHORIZED |
| GitHub | No credential change | NOT AUTHORIZED | NOT AUTHORIZED |

## 19. Downtime / Service Interruption Considerations

- Migration planning targets zero disruption to primary runtime.
- Any migration execution must be scheduled and approved with explicit downtime/interruption acknowledgment.
- If target runtime validation requires network integration, it must be isolated or explicitly approved.
- Post-migration verification must pass before any cutover is considered.

## 20. Post-Migration Verification

- Target runtime `hermes doctor` passes
- Role boundaries observable
- Skill version matrix validated
- Gateway service operational
- SSH auth validated
- Kanban/handoff flow observable
- No secret exposure
- Old server still available as rollback target

## 21. Evidence Required

- Migration runbook/log with timestamp, operator, target environment, backup set used
- Validation checklist with PASS/FAIL per item
- Screenshot or terminal log of `hermes doctor`
- Skill version matrix comparison before/after migration
- Incident-style record: what was migrated, what failed, what was learned
- Retention: evidence retained in repository docs; no secrets stored

## 22. Approval Gates

| Gate | Required approval |
|---|---|
| Phase 10 planning | Project Owner |
| Boundary B: isolated restore rehearsal | Project Owner + Control Plane |
| Boundary C: migration | Project Owner explicit authorization required |
| Boundary D: cutover | Project Owner explicit Level 3 authorization required |
| Any production/n8n write | Project Owner explicit Level 3 authorization required |
| Any credential change | Project Owner explicit Level 3 authorization required |

## 23. Resume Condition

A Project Owner decision must explicitly authorize Boundary C execution with:
- approved target environment
- approved backup set identifier
- operator assignment
- validation criteria
- stop conditions
- explicit acknowledgment of any expected downtime/service interruption

Until then, Phase 10 remains planning only. ACTIVE_WORK_PACKAGE remains WP-010 in planning state.
