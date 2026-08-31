# ORBIS AI — WP-005C BACKUP EXECUTION RECORD

WORK PACKAGE: WP-005C
SCOPE: Backup execution and manifest validation only.
STATUS: IMPLEMENTATION — BACKUP EXECUTION / MANIFEST VALIDATION

---

## 1. Backup Attempts Summary

| Attempt | Backup ID | Acceptance | Reason |
|---|---|---|---|
| 1 | `20260830-224459` | REJECTED | Canonical `*.lock` exclusion mismatch |
| 2 | `20260830-231125` | PASS | Corrected exclusion set enforced |

Attempt 1 backup was preserved without modification for audit evidence:
- Path: `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-224459/`
- Manifest: preserved
- Checksums: preserved
- No alteration to source backup files.

Attempt 2 backup created with canonical exclusions enforced and accepted.

## 2. Backup Destination

| Field | Value |
|---|---|
| Backup root | `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125/` |
| Manifest | `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125/manifests/BACKUP_MANIFEST.txt` |
| Checksums | `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125/checksums/SHA256SUMS.txt` |
| Secondary copy | `/mnt/d/Orbis-AI-Backup/WP-005C/20260830-231125/` |

## 3. Backup Structure

```
20260830-231125/
├── checksums/SHA256SUMS.txt
├── manifests/BACKUP_MANIFEST.txt
├── profiles/
│   ├── CODER/
│   ├── MASTER/
│   └── REVIEWER/
├── repo/                        (empty; Git is source of truth)
├── runtime/
│   ├── .skills_prompt_snapshot.json
│   └── databases/
│       ├── state.db
│       ├── kanban.db
│       ├── projects.db
│       ├── verification_evidence.db
│       ├── coder_state.db
│       ├── reviewer_state.db
│       ├── coder_projects.db
│       └── reviewer_projects.db
├── services/
│   ├── gateway_state.json
│   └── hermes-gateway.service
└── system/
    └── authorized_keys
```

Excluded per canonical design:
- `gateway.lock` (`*.lock`)
- `gateway.log` (runtime log, NOT_REQUIRED_BY_DESIGN)
- `.env`, `auth.json`, private keys, tokens, session secrets, production credentials

## 4. Backup Validation Matrix

| Check | Result |
|---|---|
| MASTER_BACKUP | PASS |
| CODER_BACKUP | PASS |
| REVIEWER_BACKUP | PASS |
| SKILLS_BACKUP | PASS |
| DATABASE_BACKUP | PASS |
| SERVICE_CONFIG_BACKUP | PASS |
| SECRET_EXCLUSION | PASS |
| CHECKSUM_VERIFY | PASS |
| INVENTORY_ITEMS_UNACCOUNTED_FOR | 0 |
| LOCK_FILE_COUNT | 0 |
| ENV_FILE_COUNT | 0 |
| AUTH_JSON_COUNT | 0 |
| PRIVATE_KEY_COUNT | 0 |
| SECRET_FILE_POLICY | PASS |

## 5. Secondary Copy

| Field | Value |
|---|---|
| SECONDARY_COPY_STATUS | COPY_COMPLETE |
| SECONDARY_BACKUP_ID | `20260830-231125` |
| WINDOWS_DRIVE_SELECTED | `D:` |
| WINDOWS_DESTINATION | `D:\Orbis-AI-Backup\WP-005C\20260830-231125\` |
| WSL_DESTINATION | `/mnt/d/Orbis-AI-Backup/WP-005C/20260830-231125/` |
| SOURCE_FILE_COUNT | 248542 |
| SECONDARY_FILE_COUNT | 248542 |
| FILE_COUNT_MATCH | YES |
| SOURCE_TOTAL_BYTES | 5445543502 |
| SECONDARY_TOTAL_BYTES | 5445543502 |
| SIZE_MATCH | YES |
| SECONDARY_CHECKSUM_VERIFY | PASS |
| LOCK_FILE_COUNT | 0 |
| ENV_FILE_COUNT | 0 |
| AUTH_JSON_COUNT | 0 |
| PRIVATE_KEY_COUNT | 0 |
| SECRET_FILE_POLICY | PASS |
| OUTSIDE_WSL_COPY | YES |
| SEPARATE_PHYSICAL_DEVICE_VERIFIED | UNKNOWN |
| INDEPENDENT_OFFLINE_DR_COPY | NO_OR_UNKNOWN |
| SOURCE_BACKUP_MODIFIED | NO |
| ATTEMPT1_MODIFIED | NO |
| SERVICE_STOPPED | NO |
| SERVICE_RESTARTED | NO |
| RUNTIME_MODIFIED | NO |
| SECRET_VALUE_EXPOSED | NO |
| RESTORE_STARTED | NO |
| MIGRATION_STARTED | NO |

## 6. Restoration Status

- Restore execution: NOT STARTED
- Migration: NOT STARTED
- Cutover: NOT STARTED
- Rollback execution: NOT STARTED

## 7. Evidence

### Attempt 1 (REJECTED)
- Backup ID: `20260830-224459`
- Path: `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-224459/`
- Manifest: `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-224459/manifests/BACKUP_MANIFEST.txt`
- Checksum file: `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-224459/checksums/SHA256SUMS.txt`
- Checksum verification: PASS
- Total manifest items: 36
- Backed up items: 32
- Secret recovery required items: 4
- Inventory items unaccounted for: 0
- BACKUP_ACCEPTANCE=REJECTED
- REJECTION_REASON=CANONICAL_EXCLUSION_MISMATCH
- SOURCE_BACKUP_PRESERVED=YES

### Attempt 2 (Accepted)
- Backup ID: `20260830-231125`
- Path: `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125/`
- Manifest: `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125/manifests/BACKUP_MANIFEST.txt`
- Checksum file: `/home/allday/.hermes/backups/wp005c-runtime-backup/20260830-231125/checksums/SHA256SUMS.txt`
- Checksum verification: PASS (recomputed after removing excluded files)
- Lock files included: 0
- Secret files included: 0
- BACKUP_ACCEPTANCE=PASS

### Secondary Copy
- Backup ID: `20260830-231125`
- Path: `/mnt/d/Orbis-AI-Backup/WP-005C/20260830-231125/`
- Manifest: present
- Checksum file: present
- File count match: YES
- Secondary checksum verification: PASS
- Logical payload size match: YES
- LOCK files in secondary copy: 0
- ENV files in secondary copy: 0
- AUTH_JSON files in secondary copy: 0
- PRIVATE_KEY files in secondary copy: 0

## 8. Owner Actions Required

1. Provide/approve an offline/secondary backup destination outside this host
   if stronger disaster coverage is required, and copy the backup archive there
   with checksum verification.
2. Periodically validate backup completeness by test restore in an isolated
   environment.
3. Do not delete old server until post-cutover acceptance passes.

## 9. Stop Conditions Met

- No secret values were exposed.
- No runtime files were deleted or modified outside the approved backup scope.
- No service restart was required or performed.
- No credential rotation was performed.
- No migration, restore, or cutover was started.
- Backup exists locally and on Windows D: drive.
- Secondary checksum verification completed with 0 failures.
