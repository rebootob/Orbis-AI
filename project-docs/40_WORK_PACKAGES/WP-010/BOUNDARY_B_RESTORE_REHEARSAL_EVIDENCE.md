# ORBIS AI — WP-010 Boundary B Restore Rehearsal Evidence

WORK PACKAGE: WP-010
BOUNDARY: B — isolated restore rehearsal
REPOSITORY: rebootob/Orbis-AI
BRANCH: ai/wp-010-boundary-b-restore-rehearsal
BASE: origin/develop

---

## 1. Boundary B Authorization State

- Boundary B authorization state: AUTHORIZED for evidence recording/review; rehearsal execution proceeds only after credential isolation gate is satisfied.
- ACTIVE_WORK_PACKAGE after this record: WP-010

## 2. Operator/Target

- Operator: Hermes MASTER in Orbis-Recovery-Test
- Host: sleep-cat
- WSL distro: Orbis-Recovery-Test
- Primary runtime restriction: no modification to primary Ubuntu runtime
- Target scope: rehearsal documentation and evidence only

## 3. Backup Set Validation

- Validated backup set: 20260830-231125
- Backup root: /home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125
- Manifest: /home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125/manifests/BACKUP_MANIFEST.txt
- Checksums: /home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125/checksums/SHA256SUMS.txt
- Secondary copy: /mnt/d/Orbis-AI-Backup/WP-005C/20260830-231125
- Manifest ID field: 20260830-231125
- Created at: 2026-08-30T23:14:13.081472
- Host: sleep-cat
- Platform: Ubuntu 26.04.1 LTS (WSL2)
- Hermes version: v0.20.6 (2026.8.27)
- Source develop commit at backup time: a7789317931894366dba8f8d3e4b04d659ee6d4f
- Recovery readiness: YES
- Secret recovery required: GitHub auth, Telegram bot auth, Hermes API creds, SSH private key
- SHA256 of manifest: b516a75606789ff56f8e5c6ea5d849624150b9cd68dd0cc915c2e6e7c03bc94a
- SHA256 of checksum file: c920674d7fd8c63389630737cf12bee30923ee4f13f817c53d8a9851a7d1f4f4
- Manifest checksum verify: PASS
- Checksum file verify: PASS
- Backup checksum verification: PASS
- Secondary checksum file checksum match: PASS

## 4. Backup Set Identity

- Backup set identity accepted: 20260830-231125
- Rejected earlier set observed: 20260830-224459
- Use only validated accepted set for rehearsal: 20260830-231125

## 5. Recovery Target Credential Isolation

- Scope: presence/path only inside Orbis-Recovery-Test
- Active credential/session paths before quarantine:
  - /home/allday/.hermes/.env: PRESENT
  - /home/allday/.hermes/auth.json: PRESENT
  - /home/allday/.hermes/profiles/coder/.env: PRESENT
  - /home/allday/.hermes/profiles/reviewer/.env: PRESENT
  - /home/allday/.hermes/profiles/coder/auth.json: PRESENT
  - /home/allday/.hermes/profiles/reviewer/auth.json: PRESENT
  - /home/allday/.orbis-wp008-n8n-sandbox/.env: PRESENT
  - /home/allday/.hermes/desktop-ssh: PRESENT
- Quarantine location: /home/allday/.hermes/quarantine/boundary-b-recovery-target
- Quarantine mode: 700
- Quarantined files:
  - /home/allday/.hermes/.env -> /home/allday/.hermes/quarantine/boundary-b-recovery-target/.env.quarantined
  - /home/allday/.hermes/auth.json -> /home/allday/.hermes/quarantine/boundary-b-recovery-target/auth.json.quarantined
  - /home/allday/.hermes/profiles/coder/.env -> /home/allday/.hermes/quarantine/boundary-b-recovery-target/.env.quarantined
  - /home/allday/.hermes/profiles/reviewer/.env -> /home/allday/.hermes/quarantine/boundary-b-recovery-target/.env.quarantined
  - /home/allday/.hermes/profiles/coder/auth.json -> /home/allday/.hermes/quarantine/boundary-b-recovery-target/auth.json.quarantined
  - /home/allday/.hermes/profiles/reviewer/auth.json -> /home/allday/.hermes/quarantine/boundary-b-recovery-target/auth.json.quarantined
- Post-quarantine active path presence check:
  - /home/allday/.hermes/.env: ABSENT
  - /home/allday/.hermes/auth.json: ABSENT
  - /home/allday/.hermes/profiles/coder/.env: ABSENT
  - /home/allday/.hermes/profiles/reviewer/.env: ABSENT
  - /home/allday/.hermes/profiles/coder/auth.json: ABSENT
  - /home/allday/.hermes/profiles/reviewer/auth.json: ABSENT
- Credential isolation gate: SATISFIED for active production-capable credential files
- Secret values: NOT exposed
- Secret hashes/checksums: NOT recorded

## 6. Rehearsal Actions Executed

- Read WP-010 TASK_CONTRACT: COMPLETED
- Inspect WP-005C backup evidence:
  - BACKUP_DESIGN.md: reviewed
  - BACKUP_EXECUTION_RECORD.md: reviewed
  - EXTERNAL_RECOVERY_VERIFICATION.md: reviewed
- Verify backup-set identity: PASS
- Presence-only forbidden credential check: INITIALLY FAIL -> PASS AFTER QUARANTINE
- Quarantine/neutralize cloned production credentials in Orbis-Recovery-Test: COMPLETED
- Re-run targeted presence checks: COMPLETED
- Isolated restore rehearsal execution: COMPLETED in /tmp/orbis-wp010-rehearsal
- Recovery criteria validation: COMPLETED

## 7. Boundary B Isolated Restore Rehearsal

- Rehearsal target: /tmp/orbis-wp010-rehearsal
- Restored assets:
  - profiles/CODER/SOUL.md: COPIED
  - profiles/REVIEWER/SOUL.md: COPIED
  - profiles/CODER/config.yaml: COPIED
  - profiles/REVIEWER/config.yaml: COPIED
  - runtime/databases/state.db: COPIED
  - runtime/databases/kanban.db: COPIED
  - runtime/databases/projects.db: COPIED
  - runtime/.skills_prompt_snapshot.json: COPIED
- Missing in accepted backup set:
  - profiles/MASTER/SOUL.md: MISSING_IN_BACKUP
  - services/hermes-gateway.service: MISSING_IN_BACKUP
  - system/authorized_keys: MISSING_IN_BACKUP
  - runtime/databases/verification_evidence.db: NOT_MISSING_IN_BACKUP; accepted manifest contains `profiles/CODER/verification_evidence.db`; rehearsal evidence path mismatch causes recorded FAIL.

## 8. Recovery Criteria Validation

### 8.1 Authoritative Disposition

Resolved against WP-010 TASK_CONTRACT, WP-005C BACKUP_DESIGN, WP-005C BACKUP_EXECUTION_RECORD, and accepted backup manifest for backup set `20260830-231125`:

| Item | Authoritative disposition | Canonical evidence |
|---|---|---|
| `MASTER_SOUL_RESTORED` | REQUIRED_BY_WP010_AND_MISSING_FROM_BACKUP | TASK_CONTRACT §4 lists Hermes runtime profiles for root/MASTER; BACKUP_DESIGN §2/§5 includes root/MASTER profile coverage; accepted backup structure and rehearsal evidence show no `profiles/MASTER/SOUL.md` in the accepted backup tree. |
| `GATEWAY_SERVICE_RESTORED` | REQUIRED_BY_WP010_AND_MISSING_FROM_BACKUP | TASK_CONTRACT §4/§8 and BACKUP_DESIGN §2/§5/§10 explicitly include `hermes-gateway.service`; accepted backup tree does not include `services/hermes-gateway.service`. |
| `AUTHORIZED_KEYS_RESTORED` | REQUIRED_BY_WP010_AND_MISSING_FROM_BACKUP | TASK_CONTRACT §4/§8 and BACKUP_DESIGN §2/§5/§10 explicitly include SSH `authorized_keys`; accepted backup tree does not include `system/authorized_keys`. |
| `VERIFICATION_EVIDENCE_DB_RESTORED` | INTENTIONALLY_EXCLUDED_BY_CANONICAL_BACKUP_DESIGN | BACKUP_EXECUTION_RECORD §3/§5/§6 documents `verification_evidence.db` under runtime profile databases and shows the accepted backup contains `profiles/CODER/verification_evidence.db`; the rehearsal `MISSING_IN_BACKUP` note is incorrect/contradicts the accepted manifest. Canonical backup design treats this asset as included, so rehearsal FAIL indicates an internal consistency defect in the evidence record, not a design exclusion. |

Minimum corrective follow-up required:
- Re-run restore rehearsal against accepted backup set `20260830-231125` using the actual restored file paths from the manifest (`profiles/CODER/verification_evidence.db`).
- Correct rehearsal evidence so `verification_evidence.db` is checked at the actual restored path.
- Treat `MASTER_SOUL_RESTORED`, `GATEWAY_SERVICE_RESTORED`, and `AUTHORIZED_KEYS_RESTORED` as backup coverage gaps against the accepted backup manifest; do not mark PASS without restoring those assets or updating canonical backup design to explicitly exclude them.

### 8.2 Validation Checklist

| Check | Result |
|---|---|
| CODER_SOUL_RESTORED | PASS |
| REVIEWER_SOUL_RESTORED | PASS |
| CODER_CONFIG_RESTORED | PASS |
| REVIEWER_CONFIG_RESTORED | PASS |
| STATE_DB_RESTORED | PASS |
| KANBAN_DB_RESTORED | PASS |
| PROJECTS_DB_RESTORED | PASS |
| SKILL_SNAPSHOT_RESTORED | PASS |
| MASTER_SOUL_RESTORED | FAIL |
| GATEWAY_SERVICE_RESTORED | FAIL |
| AUTHORIZED_KEYS_RESTORED | FAIL |
| VERIFICATION_EVIDENCE_DB_RESTORED | FAIL |
| RECOVERY_TARGET_CREDENTIAL_ISOLATION | PASS |
| NO_SECRETS_COMMITTED | PASS |

## 9. Rehearsal Stop Conditions

- Rehearsal completed within isolated disposable target.
- No primary WSL2 Hermes runtime disruption.
- No secret values exposed.
- No production Telegram/n8n connection.
- No n8n writes.
- No migration/cutover/deployment.
- No credential rotation/change.

## 10. Final State

- Exact HEAD at time of initial submission: c6f53720adacb8a7615f7955fc614ee598ff6ee2
- Current exact PR HEAD is authoritative from GitHub PR metadata and must be resolved at review time; do not store a mutable current HEAD in this evidence file.
- Working branch: ai/wp-010-boundary-b-restore-rehearsal
- Unsaved working tree changes: NONE after commit
- Merge state: open PR only, no merge
- Production Telegram/n8n connection: NONE
- n8n writes: NONE
- Migration/cutover/deployment: NONE
- Credential rotation/change: NONE
- Primary Ubuntu modification: NONE

## 11. Next Step

- Await Runtime REVIEWER review against exact final HEAD.
- Then STOP for ChatGPT Control Plane review.
- DO NOT MERGE.
