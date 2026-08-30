# ORBIS AI — WP-005C BACKUP DESIGN

WORK PACKAGE: WP-005C
SCOPE: Backup Design only. No production backup is created by this document.
STATUS: IMPLEMENTATION — RUNTIME INVENTORY / BACKUP DESIGN

---

## 1. Backup Objectives

- Preserve recoverability of MASTER, CODER, and REVIEWER runtime state.
- Preserve recoverability of Core Skills and version mapping.
- Preserve GitHub integration, Telegram integration, and Hermes Desktop SSH trust.
- Support restore without chat history, prior conversation memory, or ChatGPT re-instruction.
- Support replacement-server rebuild and rollback to old server.
- Avoid storing secrets in Git, backup archives, or backup manifests.

## 2. Backup Scope

Include:
- Hermes runtime profile/config/SOUL files for root, CODER, and REVIEWER.
- Core Skills runtime copies.
- Runtime SQLite databases: state, kanban, projects, verification evidence.
- Gateway service unit and non-secret runtime metadata.
- SSH authorized public keys and relevant system config.
- Hermes install version/commit reference.
- Skill version matrix and source/runtime SHA256 mapping.

Exclude from archive:
- `.env`
- `auth.json`
- Private keys
- Telegram bot token
- GitHub token
- OAuth credentials
- Session secrets
- Production credentials

## 3. Exclusions from Git

Git is the source of truth for repository files only. All runtime-state files, profile configs, auth JSON, `.env`, DBs, cache, logs, and local install artifacts remain outside Git.

## 4. Backup Storage Model

- Local primary archive on the same host is acceptable for non-disaster scenarios.
- Offline/secondary copy is required for true disaster recovery coverage.
- Backup locations and metadata may reference secret existence, but must not store plaintext secret values.

## 5. Directory Structure

```
backups/wp005c-<YYYYMMDD>-<seq>/
├── manifest.json
├── checksums.sha256
├── runtime/
│   ├── root/
│   ├── coder/
│   └── reviewer/
├── system/
│   ├── sshd_config
│   ├── authorized_keys
│   └── hermes-gateway.service
└── repo/
    └── Orbis-AI/  # optional export for rebuild
```

### 5.1 Exclusions Within the Archive

Paths/files excluded from archive:
- `.env`
- `auth.json`
- `*.lock`
- `*.wal` if inconsistent at backup time; note in manifest if omitted
- session secrets and token caches unless explicitly required

## 6. Manifest

Required manifest fields:
- work_package
- created_at
- host
- platform
- source_commit
- hermes_version
- profiles hash/sha256 summaries
- skill_matrix entries: profile, name, version, runtime_sha256, repo_source_sha256, match
- excluded_paths
- secrets recovery references only, no values
- operator/project owner notes

## 7. Integrity Verification

- Compute SHA256 for every archived file.
- Store checksums in `checksums.sha256`.
- Verify archive with `sha256sum -c checksums.sha256`.
- Reject backup if manifest or checksum verification fails.

## 8. Checksum Strategy

- SHA256 for files.
- Optional manifest signature using approved tooling if audit requirements demand it.
- Record Hermes version and install commit for rebuild traceability.

## 9. Metadata Requirements

- Date-stamped folder naming.
- Sequence number if multiple backups in same day.
- Source commit SHA.
- Hermes upstream/local version string.
- Host/platform identifiers.

## 10. Restore Order

1. Restore or rebuild OS and Hermes runtime.
2. Restore `hermes-gateway.service` and restart.
3. Restore SSH authorized keys and validate key auth.
4. Restore runtime files in dependency order: SOUL/config before DBs.
5. Restore Core Skills runtime copies.
6. Recover secrets from secure stores/vaults per documented recovery procedures.
7. Start profiles and gateway; observe fresh-session startup.
8. Validate GitHub auth, Telegram, and Desktop SSH.
9. Run contract tests and acceptance checklist.
10. Keep old server available as rollback target until post-restore acceptance passes.

## 11. Retention Policy

- Minimum 3 rolling backups.
- One offline/secondary copy for critical milestones.
- Retire old backups only after a newer backup has passed restore validation.
- Do not delete old server until post-cutover acceptance passes.

## 12. Backup Validation Procedure

- After archive creation, run integrity checksum verification.
- Validate manifest JSON schema and required fields.
- Periodically perform a restore dry run in an isolated environment.
- Record results as evidence before treating backup as production-ready.

## 13. Failure / Rollback Handling

- Partial archives must be removed immediately.
- Restore failures must stop the procedure; existing runtime remains authoritative.
- Migration must be reversible at any point before acceptance.
- Old server remains rollback target until post-cutover acceptance passes.

## 14. Offline / Secondary Copy

- Copy verified backup archive to offline/secondary storage.
- Ensure recovery owner has offline access if primary host is unavailable.
- Secondary copy must be refreshed after each successful backup validation.

## 15. Secret Recovery Model

- Secrets are never stored in Git, backup archives, or manifests.
- Recovery uses documented secure sources only.
- Restore procedure explicitly includes secret-recovery steps.
- Migration acceptance fails if any required credential lacks a recoverable secure source.

## 16. Backup Completeness Proof

- Inventory checklist from runtime inventory must be reflected in manifest file list.
- Post-backup report compares manifest inventory to expected source inventory.
- Test restore without chat history is the definitive completeness proof.
