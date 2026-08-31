# ORBIS AI — PHASE 10 TASK CONTRACT

WORK PACKAGE: WP-010
SCOPE: Phase 10 Backup/Recovery validation planning only. No restore, migration, cutover, or production writes.
STATUS: PLANNING — NOT STARTED

---

## 1. Objective

Prepare a safe, staged recovery-validation plan for Phase 10 that proves
restore/recovery completeness without disrupting the current WSL2 Hermes runtime,
production integrations, or any live environment.

## 2. Boundary: Planning vs. Implementation

This contract defines four distinct boundaries:

| Boundary | Description | Authorization |
|---|---|---|
| A. Planning | Document the plan, assets, sequence, evidence, and stop conditions. | Project Owner authorizes planning only. |
| B. Isolated restore rehearsal | Execute restore/disaster-recovery rehearsal in an isolated disposable target. | Separate Project Owner authorization required. |
| C. Migration | Any migration of live workload or data. | Separate Project Owner authorization required. |
| D. Cutover | Switch production or canonical runtime to restored target. | Separate Project Owner authorization required. |

This PR/work covers **Boundary A only**.

## 3. Prohibited During Planning

- Production restore
- Production writes
- Migration
- Cutover
- Replacement of current WSL2 runtime
- Credential rotation/change
- n8n production connection
- Deployment
- External side effects

## 4. Assets to Restore (Planned)

Targeted for isolated rehearsal only:

| Asset | Source | Notes |
|---|---|---|
| Hermes runtime profiles | `~/.hermes/profiles/coder/`, `~/.hermes/profiles/reviewer/`, `~/.hermes/` | Config/SOUL/non-secret files only |
| Core Skills runtime copies | `~/.hermes/profiles/*/skills/` | Version matrix preserved |
| Runtime databases | `state.db`, `kanban.db`, `projects.db`, `verification_evidence.db` | SQLite; may be empty or seeded |
| Gateway service unit | `hermes-gateway.service` | Systemd user unit |
| SSH authorized keys | `~/.ssh/authorized_keys` | Public keys only |
| Repository export | `/home/allday/Orbis-AI/` | Optional; Git source of truth |

Excluded from restore rehearsal:
- `.env`
- `auth.json`
- Private keys and tokens
- Session secrets
- Production credentials

## 5. Test Environment

- Isolated LOCAL_TEST/disposable target
- Separate WSL2 instance, VM, or container approved by Project Owner
- No overwrite of existing Hermes runtime on `sleep-cat` or any production-equivalent host
- Network-isolated unless explicitly approved for integration validation
- Rehearsal target must be destroyable without data loss to primary runtime

## 6. Isolation Requirements

- Rehearsal target is not the primary WSL2 Hermes runtime
- Rehearsal target has no access to production n8n, Telegram bot token, or production GitHub credentials
- Secrets required by the target must come from approved secure-store recovery procedures, not copied from primary runtime plaintext files
- Any rehearsal-induced changes must be fully reversible or disposable

## 7. Backup Set to Use

- Latest validated backup set from WP-005C backup execution/manifest validation
- Backup manifest must include:
  - `work_package`
  - `created_at`
  - `host`
  - `platform`
  - `source_commit`
  - `hermes_version`
  - `profiles` hash/sha256 summaries
  - `skill_matrix` entries: profile, name, version, runtime_sha256, repo_source_sha256, match
  - `excluded_paths`
  - secrets recovery references only, no values
- If no validated backup set exists, restore rehearsal is NOT STARTED until one is created and validated

## 8. Restore Sequence (Planned)

1. Provision isolated disposable target environment.
2. Install Hermes runtime at validated version/commit.
3. Restore system config: `hermes-gateway.service`, `sshd_config`, `authorized_keys`.
4. Restore runtime files in dependency order: SOUL/config before DBs.
5. Restore Core Skills runtime copies.
6. Verify skill version matrix and SHA256 mapping.
7. Recover secrets from secure stores/vaults per documented recovery procedures.
8. Start profiles and gateway; observe fresh-session startup.
9. Run validation checks.
10. Record evidence or failure.
11. Tear down / dispose rehearsal target.

## 9. Validation Checks (Planned)

- `hermes doctor` passes on rehearsal target
- Basic chat validation passes
- MASTER/CODER/REVIEWER role boundaries observable
- Core Skills version matrix matches expected source/runtime SHAs
- Gateway service starts and accepts connections
- SSH key auth validated without passwords
- Kanban/handoff flow observable: MASTER → CODER → REVIEWER → MASTER
- No secret values exposed in logs, exports, or manifest
- Rehearsal target can be destroyed without affecting primary runtime

## 10. Expected Evidence

- Rehearsal runbook/log with timestamp, operator, target environment, backup set used
- Validation checklist with PASS/FAIL per item
- Screenshot or terminal log of `hermes doctor`
- Skill version matrix comparison before/after restore
- Incident-style record: what was restored, what failed, what was learned
- Retention: evidence retained in repository docs; no secrets stored

## 11. Rollback/Cleanup

- If any validation fails, stop and preserve existing running runtime.
- Rehearsal target must be destroyable without affecting primary runtime.
- Prior known-good backup remains authoritative until newer restore validation passes.
- No migration, cutover, or production switch occurs during rehearsal.

## 12. Stop Conditions

Halt Phase 10 immediately if:
- Any step risks overwriting or disrupting the primary WSL2 Hermes runtime
- Secret values are exposed or improperly handled
- n8n production connection is attempted or triggered
- External side effects occur
- Validation cannot be completed in isolated environment
- Project Owner has not explicitly authorized Boundary B, C, or D
- Local_test health remains FAIL / HTTP 000 and sandbox is unavailable unless isolated target is used instead

## 13. Approval Gates

| Gate | Required approval |
|---|---|
| Phase 10 planning | Project Owner |
| Boundary B: isolated restore rehearsal | Project Owner + Control Plane |
| Boundary C: migration | Project Owner explicit Level 3 |
| Boundary D: cutover | Project Owner explicit Level 3 |
| Any production/n8n write | Project Owner explicit Level 3 |
| Any credential change | Project Owner explicit Level 3 |

## 14. Resume Condition

A Project Owner decision must explicitly authorize Boundary B with:
- approved isolated target environment
- approved backup set identifier
- operator assignment
- validation criteria
- stop conditions

Until then, Phase 10 remains planning only. ACTIVE_WORK_PACKAGE remains NONE.
