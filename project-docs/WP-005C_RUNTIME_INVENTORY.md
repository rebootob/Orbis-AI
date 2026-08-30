# ORBIS AI — WP-005C RUNTIME INVENTORY

WORK PACKAGE: WP-005C
SCOPE: Runtime Inventory / Backup Design — discovery and documentation only
STATUS: IMPLEMENTATION — RUNTIME INVENTORY / BACKUP DESIGN

---

## 1. Runtime Host / Platform

| Field | Value |
|---|---|
| Platform | WSL2 |
| OS | Ubuntu 26.04.1 LTS (Resolute Raccoon) |
| Kernel | 6.18.33.2-microsoft-standard-WSL2 |
| Architecture | x86_64 |
| Hostname | sleep-cat |
| Primary user | allday (uid=1000, gid=1000) |
| Runtime paths | `~/.hermes/` (root/default/runtime home) <br> `~/.hermes/profiles/coder/` <br> `~/.hermes/profiles/reviewer/` <br> `~/.local/bin/hermes` |
| Repo path | `/home/allday/Orbis-AI/` |

Observations:
- No Windows-local Hermes backend is installed on the Windows side from the WSL2 perspective.
- Desktop-ssh directories under `~/.hermes/desktop-ssh/` exist because Hermes Desktop sessions have connected to the WSL2 Hermes backend. These contain backend lock/log artifacts from those sessions.
- All discovery below is non-destructive read-only inspection.

---

## 2. Hermes Installation

| Field | Value |
|---|---|
| Version | Hermes Agent v0.20.6 (2026.8.27) |
| Upstream commit | dce2ecb8 |
| Local patch | +1 carried commit (`1c5ee581`) |
| Executable path | `/home/allday/.local/bin/hermes` |
| Install directory | `/home/allday/.hermes/hermes-agent` |
| Install method | git |
| Python | 3.11.16 (`venv` under install directory) |
| System Python | 3.14.4 at `/usr/bin/python3` |
| OpenAI SDK | 2.24.0 |
| Dependency mechanism | Python venv + Hermes-managed bundled dependencies |
| Service/process startup | systemd user unit + CLI sessions |
| Non-secret config paths | `~/.hermes/config.yaml`, `~/.hermes/profiles/*/config.yaml` |

Update channel:
- Installed version is older than upstream by multiple commits; `hermes update` was observed available. Updates should be performed through approved Hermes update mechanisms, not ad hoc file edits.

---

## 3. Profiles

### 3.1 MASTER / default

- Identity: Hermes default profile = Orbis AI MASTER role.
- Profile location: `/home/allday/.hermes/`
- SOUL: `/home/allday/.hermes/SOUL.md` — defines MASTER role boundary, approval gates, and authority model.
- Config: `/home/allday/.hermes/config.yaml`
- Skills: `/home/allday/.hermes/skills/`
- Auth: `/home/allday/.hermes/auth.json`
- State: `/home/allday/.hermes/state.db`, `/home/allday/.hermes/kanban.db`
- Gateway: systemd unit `hermes-gateway.service`

### 3.2 CODER

- Profile path: `/home/allday/.hermes/profiles/coder/`
- SOUL: `/home/allday/.hermes/profiles/coder/SOUL.md`
- Config: `/home/allday/.hermes/profiles/coder/config.yaml`
- .env: `/home/allday/.hermes/profiles/coder/.env`
- Skills: `/home/allday/.hermes/profiles/coder/skills/`
  - `code-development` v0.2.0
  - `git-governance` v0.2.2
  - `security` v0.2.0
  - `orbi-work-package-planning` v0.1.0
  - `repository-closeout` v0.1.0
- Auth: `/home/allday/.hermes/profiles/coder/auth.json`
- State: `/home/allday/.hermes/profiles/coder/state.db`
- Runtime DBs: `projects.db`, `verification_evidence.db`
- Process scope: empty in current snapshot (`[]`)

### 3.3 REVIEWER

- Profile path: `/home/allday/.hermes/profiles/reviewer/`
- SOUL: `/home/allday/.hermes/profiles/reviewer/SOUL.md`
- Config: `/home/allday/.hermes/profiles/reviewer/config.yaml`
- .env: `/home/allday/.hermes/profiles/reviewer/.env`
- Skills: `/home/allday/.hermes/profiles/reviewer/skills/`
  - `code-review` v0.2.0
  - `git-governance` v0.2.2
  - `security` v0.2.0
- Auth: `/home/allday/.hermes/profiles/reviewer/auth.json`
- State: `/home/allday/.hermes/profiles/reviewer/state.db`
- Runtime DBs: `projects.db`
- Process scope: 1 active Hermes session in current snapshot (`hermes -p coder chat`)

---

## 4. Core Skills

Deployed Core Skills vs repository source.

| Profile | Skill | Version | Runtime Path | Repo Source Path | Runtime SHA256 | Repo SHA256 | MATCH |
|---|---|---|---|---|---|---|---|
| MASTER | project-manager | v0.2.2 | `/home/allday/.hermes/skills/project-manager/SKILL.md` | `/home/allday/Orbis-AI/skills/project-manager/SKILL.md` | `4f75cf3f6b605d8c` | `b781d9cdc471dd15` | NO |
| MASTER | git-governance | v0.2.2 | `/home/allday/.hermes/skills/git-governance/SKILL.md` | `/home/allday/Orbis-AI/skills/git-governance/SKILL.md` | `3f9ae819632ab765` | `3f9ae819632ab765` | YES |
| MASTER | security | v0.2.0 | `/home/allday/.hermes/skills/security/SKILL.md` | `/home/allday/Orbis-AI/skills/security/SKILL.md` | `47afcf8b764113e2` | `47afcf8b764113e2` | YES |
| CODER | code-development | v0.2.0 | `/home/allday/.hermes/profiles/coder/skills/code-development/SKILL.md` | `/home/allday/Orbis-AI/skills/code-development/SKILL.md` | `aa8e9c7e1aba5620` | `aa8e9c7e1aba5620` | YES |
| CODER | git-governance | v0.2.2 | `/home/allday/.hermes/profiles/coder/skills/git-governance/SKILL.md` | `/home/allday/Orbis-AI/skills/git-governance/SKILL.md` | `3f9ae819632ab765` | `3f9ae819632ab765` | YES |
| CODER | security | v0.2.0 | `/home/allday/.hermes/profiles/coder/skills/security/SKILL.md` | `/home/allday/Orbis-AI/skills/security/SKILL.md` | `47afcf8b764113e2` | `47afcf8b764113e2` | YES |
| REVIEWER | code-review | v0.2.0 | `/home/allday/.hermes/profiles/reviewer/skills/code-review/SKILL.md` | `/home/allday/Orbis-AI/skills/code-review/SKILL.md` | `74dbfdb517b01473` | `74dbfdb517b01473` | YES |
| REVIEWER | git-governance | v0.2.2 | `/home/allday/.hermes/profiles/reviewer/skills/git-governance/SKILL.md` | `/home/allday/Orbis-AI/skills/git-governance/SKILL.md` | `3f9ae819632ab765` | `3f9ae819632ab765` | YES |
| REVIEWER | security | v0.2.0 | `/home/allday/.hermes/profiles/reviewer/skills/security/SKILL.md` | `/home/allday/Orbis-AI/skills/security/SKILL.md` | `47afcf8b764113e2` | `47afcf8b764113e2` | YES |

Note:
- MASTER `project-manager` shows MATCH=NO because runtime SHA differs from repo SHA. Root/skills runtime source may be an earlier patched version, or repo/runtime source divergence exists. This must be resolved before migration acceptance.

---

## 5. Git / GitHub Integration

| Field | Value |
|---|---|
| Repository path | `/home/allday/Orbis-AI/` |
| Remote origin | `https://github.com/rebootob/Orbis-AI.git` (fetch/push) |
| Git auth state | PRESENT — `gh auth status` reports logged in as `rebootob` over HTTPS |
| Git credential mechanism | `gh` HTTPS token stored in Hermes-managed auth store; token value is never printed here |
| In-repo GPG/signing | Not recorded from read-only discovery |
| Branch model | `develop` integration, feature branches under `ai/*` |
| Git source of truth | Repository files only; runtime state outside Git requires documented backup source |

---

## 6. Telegram Integration

| Field | Value |
|---|---|
| Gateway/service | Hermes Agent Gateway via systemd user unit `hermes-gateway.service` |
| Runtime env source | Root `.env` at `/home/allday/.hermes/.env` |
| Telegram credential reference | `TELEGRAM_BOT_TOKEN` key present in `.env`; value not documented here |
| Allowed users reference | `TELEGRAM_ALLOWED_USERS` key present in `.env` |
| Home channel reference | `TELEGRAM_HOME_CHANNEL` key present in `.env` |
| Channel directory | `/home/allday/.hermes/channel_directory.json` |
| Bot relay dirs | `/home/allday/.hermes/bot_relay/{claimed,outbox,replies}` — empty in current snapshot |
| Sensitive IDs | Telegram platform IDs from `channel_directory.json` are treated as sensitive per project rules and are not reproduced here |

Observation:
- Telegram integration is operational through the Hermes gateway. Recovery requires the bot token and home-channel binding, both referenced in `.env`.

---

## 7. Hermes Desktop / SSH

| Field | Value |
|---|---|
| SSH daemon status | active |
| WSL-side listener observation | `ss` output captured during this inventory did not list `:22` or `:2222` listeners; this is a sampled observation, not proof that port 2222 is absent. |
| Windows-side loopback/forwarding mechanism | UNKNOWN — not proven by safe read-only WSL-side discovery. |
| Desktop target | `127.0.0.1:2222` per approved Phase 5 architecture and WP-005B evidence |
| Authentication method | ED25519 key-only |
| Authorized keys | `/home/allday/.ssh/authorized_keys` |
| Desktop SSH sessions | `/home/allday/.hermes/desktop-ssh/` contains session dirs: `1c2c...`, `b5568...`, `f89bea...` |
| Desktop session artifacts | Each session contains `backend.lock.json` + log file. Lock fields present: ownershipId, spawnNonce, pid, port, profile, hermesPath, hermesHome, logPath, tokenFingerprint, protocolVersion, startedAt, creationTime, schemaVersion. |
| Windows local backend state | NO detected Windows-local Hermes backend in this inspection. Desktop sessions point to WSL2 Hermes home and executable path. |
| Windows duplicate runtime | NO second Orbis runtime detected. |
| Last validated Desktop-to-WSL connection | PASS — WP-005B B4 evidence |

Required guard values:
- `WINDOWS_LOCAL_HERMES_BACKEND_RUNNING=NO`
- `DUPLICATE_ACTIVE_ORBIS_RUNTIME=NO`
- `WINDOWS_LOOPBACK_FORWARDING_MECHANISM=UNKNOWN`

If Windows-local bootstrap/install is detected in later phases:
- STOP
- Do not complete local backend installation
- Escalate to investigation

---

## 8. Services / Persistence

| Service | Mechanism | Config / Unit Path |
|---|---|---|
| Hermes gateway | systemd user unit | `/home/allday/.config/systemd/user/hermes-gateway.service` |
| SSH daemon | systemd service | `/etc/ssh/sshd_config` |
| Hermes runtime | CLI/systemd/manual | ExecStart uses venv python `hermes_cli.main gateway run` |
| Cron jobs | Hermes cron dir | `~/.hermes/cron/`, `~/.hermes/profiles/*/cron/` |
| Desktop SSH sessions | Hermes Desktop SSH lock dirs | `~/.hermes/desktop-ssh/<session>/` |

Non-secret startup facts:
- Gateway environment sets `HERMES_HOME=/home/allday/.hermes` and PATH.
- Gateway uses WAL-mode SQLite databases (`state.db`, `kanban.db`).
- `Restart=always` with `RestartSec=5`; stop/post commands include cgroup cleanup script.

---

## 9. Non-Git State

Classification for runtime-critical items not recoverable from Git alone.

| Item | Path/Reference | Classification |
|---|---|---|
| Hermes root SOUL | `/home/allday/.hermes/SOUL.md` | BACKUP_REQUIRED |
| Hermes root config | `/home/allday/.hermes/config.yaml` | BACKUP_REQUIRED |
| Root auth JSON | `/home/allday/.hermes/auth.json` | SECRET_RECOVERY_REQUIRED |
| Root .env | `/home/allday/.hermes/.env` | SECRET_RECOVERY_REQUIRED |
| Root state DB | `/home/allday/.hermes/state.db` | BACKUP_REQUIRED |
| Root kanban DB | `/home/allday/.hermes/kanban.db` | BACKUP_REQUIRED |
| Root projects DB | `/home/allday/.hermes/projects.db` | BACKUP_REQUIRED |
| Root verification DB | `/home/allday/.hermes/verification_evidence.db` | BACKUP_REQUIRED |
| Root skills runtime | `/home/allday/.hermes/skills/` | BACKUP_REQUIRED |
| Root skills prompt snapshot | `/home/allday/.hermes/.skills_prompt_snapshot.json` | BACKUP_REQUIRED |
| Gateway service unit | `/home/allday/.config/systemd/user/hermes-gateway.service` | BACKUP_REQUIRED |
| Gateway lock/pid/sock | `/home/allday/.hermes/gateway.{lock,pid,sock}` | BACKUP_REQUIRED |
| Gateway state | `/home/allday/.hermes/gateway_state.json` | BACKUP_REQUIRED |
| Gateway logs | `/home/allday/.hermes/logs/gateway.log` | BACKUP_REQUIRED |
| CODER SOUL | `/home/allday/.hermes/profiles/coder/SOUL.md` | BACKUP_REQUIRED |
| CODER config | `/home/allday/.hermes/profiles/coder/config.yaml` | BACKUP_REQUIRED |
| CODER .env | `/home/allday/.hermes/profiles/coder/.env` | SECRET_RECOVERY_REQUIRED |
| CODER auth | `/home/allday/.hermes/profiles/coder/auth.json` | SECRET_RECOVERY_REQUIRED |
| CODER state DB | `/home/allday/.hermes/profiles/coder/state.db` | BACKUP_REQUIRED |
| CODER projects DB | `/home/allday/.hermes/profiles/coder/projects.db` | BACKUP_REQUIRED |
| CODER verification DB | `/home/allday/.hermes/profiles/coder/verification_evidence.db` | BACKUP_REQUIRED |
| CODER runtime dir | `/home/allday/.hermes/profiles/coder/runtime/` | BACKUP_REQUIRED |
| CODER cron | `/home/allday/.hermes/profiles/coder/cron/` | BACKUP_REQUIRED |
| CODER skills runtime | `/home/allday/.hermes/profiles/coder/skills/` | BACKUP_REQUIRED |
| CODER processes | `/home/allday/.hermes/profiles/coder/processes.json` | BACKUP_REQUIRED |
| REVIEWER SOUL | `/home/allday/.hermes/profiles/reviewer/SOUL.md` | BACKUP_REQUIRED |
| REVIEWER config | `/home/allday/.hermes/profiles/reviewer/config.yaml` | BACKUP_REQUIRED |
| REVIEWER .env | `/home/allday/.hermes/profiles/reviewer/.env` | SECRET_RECOVERY_REQUIRED |
| REVIEWER auth | `/home/allday/.hermes/profiles/reviewer/auth.json` | SECRET_RECOVERY_REQUIRED |
| REVIEWER state DB | `/home/allday/.hermes/profiles/reviewer/state.db` | BACKUP_REQUIRED |
| REVIEWER projects DB | `/home/allday/.hermes/profiles/reviewer/projects.db` | BACKUP_REQUIRED |
| REVIEWER cron | `/home/allday/.hermes/profiles/reviewer/cron/` | BACKUP_REQUIRED |
| REVIEWER skills runtime | `/home/allday/.hermes/profiles/reviewer/skills/` | BACKUP_REQUIRED |
| REVIEWER processes | `/home/allday/.hermes/profiles/reviewer/processes.json` | BACKUP_REQUIRED |
| SSH authorized keys | `/home/allday/.ssh/authorized_keys` | BACKUP_REQUIRED |
| SSH host keys | `/etc/ssh/ssh_host_*_key` | REGENERATABLE |
| Desktop SSH trust state | `/home/allday/.hermes/desktop-ssh/` | BACKUP_REQUIRED |
| Hermes install dir | `/home/allday/.hermes/hermes-agent/` | REGENERATABLE |
| Venv | `/home/allday/.hermes/hermes-agent/venv/` | REGENERATABLE |
| Channel directory | `/home/allday/.hermes/channel_directory.json` | BACKUP_REQUIRED |
| Install ID | `/home/allday/.hermes/install_id` | BACKUP_REQUIRED |
| Cron configs | `~/.hermes/cron/` and profile cron dirs | BACKUP_REQUIRED |
| Models cache files | `models_dev_cache.json`, `provider_models_cache.json`, etc. | REGENERATABLE |

Notes:
- Classification is based on current repository/architecture facts, not on whether a file is recoverable by chance.
- If a new canonical repository source is later approved for any item here, its classification may change.
- Secure-recovery items are tracked separately in Section 10.

---

## 10. Secure Credential Recovery Inventory

All credentials are referenced by purpose and secure storage reference only. No secret values are documented.

### 10.1 GitHub Authentication

| Field | Value |
|---|---|
| Credential purpose/name | GitHub HTTPS token for Git operations and `gh` CLI |
| Authoritative secure storage | Hermes auth JSON at `/home/allday/.hermes/auth.json`; `gh` host config at `/home/allday/.config/gh/hosts.yml` |
| Recovery owner | Project Owner / primary operator (`allday`) |
| Recovery procedure | Re-authenticate `gh` via `gh auth login` with approved scopes; restore token into Hermes auth JSON using Hermes auth management rather than manual `.env` editing |
| Verification method | `gh auth status` reports logged-in state; Git remote operations succeed |
| Recovery readiness | Documented, executable |

### 10.2 Telegram Bot Authentication

| Field | Value |
|---|---|
| Credential purpose/name | Telegram bot token |
| Authoritative secure storage | Hermes root `.env` at `/home/allday/.hermes/.env`, key: `TELEGRAM_BOT_TOKEN` |
| Recovery owner | Project Owner / primary operator |
| Recovery procedure | Retrieve token from approved secure store/vault and write back to Hermes root `.env`; restart `hermes-gateway.service` |
| Verification method | Hermes gateway reports telegram platform active; Telegram round-trip succeeds |
| Recovery readiness | Documented, executable |

### 10.3 Hermes-Required API Credentials

| Field | Value |
|---|---|
| Credential purpose/name | Nous provider access token and related agent/tls settings |
| Authoritative secure storage | `/home/allday/.hermes/auth.json` provider `nous` section |
| Recovery owner | Project Owner / primary operator |
| Recovery procedure | Re-run Hermes Nous auth flow to obtain tokens; restore auth JSON via Hermes auth management |
| Verification method | Hermes chat/model queries succeed against configured Nous base URL |
| Recovery readiness | Documented, executable |

### 10.4 SSH Private Key / Authorized-Key Recovery

| Field | Value |
|---|---|
| Credential purpose/name | ED25519 SSH private key for Hermes Desktop client; authorized public key for server trust |
| Authoritative secure storage | Private key on Windows host in Hermes Desktop SSH trust store; public key in `/home/allday/.ssh/authorized_keys` on WSL2 |
| Recovery owner | Project Owner / primary operator |
| Recovery procedure | Restore key pair from approved secure store; place public key in `authorized_keys`; verify key-based auth without password |
| Verification method | `ssh -i <key> allday@127.0.0.1 -p 2222` succeeds from Windows Hermes Desktop |
| Recovery readiness | Documented, executable |

### 10.5 Additional Runtime Credentials Discovered

| Field | Value |
|---|---|
| Credential purpose/name | `TELEGRAM_ALLOWED_USERS`, `TELEGRAM_HOME_CHANNEL` |
| Authoritative secure storage | Hermes root `.env` |
| Recovery owner | Project Owner / primary operator |
| Recovery procedure | Restore from approved secure store into Hermes root `.env` |
| Verification method | Channel directory and allowed-user behavior match expected bindings |
| Recovery readiness | Documented, executable |

Overall recovery readiness:
- `RECOVERY_READINESS=FAIL` unless Project Owner confirms the above secure stores exist and are accessible. Documentation alone does not prove recoverability; actual recovery sources must be verified before migration acceptance.

---

## 11. Backup Design

### 11.1 What Must Be Backed Up

- Hermes root profile/config/SOUL and runtime directories under `~/.hermes/`
- Hermes profile directories for CODER and REVIEWER
- Core Skills runtime copies and version mapping
- GitHub auth presence metadata, never secret values
- Telegram integration identifiers and binding state references
- Hermes Desktop SSH trust/key state references
- System/service config needed to restore runtime behavior:
  - `~/.config/systemd/user/hermes-gateway.service`
  - `/etc/ssh/sshd_config`
  - `/home/allday/.ssh/authorized_keys`

### 11.2 What Must NOT Be Stored in Git

- `.env`
- API tokens
- GitHub tokens / auth JSON secret fields
- Telegram bot token / channel secrets
- OAuth credentials
- Passwords
- Private keys
- Session secrets
- Production credentials

### 11.3 What Must NOT Be Stored in Plaintext Backup Archives

Same categories as Git exclusion. Backup archives must store references/placeholders for secrets; actual recovery uses secure stores/vaults.

### 11.4 Backup Directory Structure

```
backups/wp005c-<YYYYMMDD>-<seq>/
├── manifest.json
├── checksums.sha256
├── runtime/
│   ├── root/
│   │   ├── SOUL.md
│   │   ├── config.yaml
│   │   ├── state.db*
│   │   ├── kanban.db*
│   │   ├── projects.db*
│   │   ├── verification_evidence.db*
│   │   ├── skills/
│   │   ├── cron/
│   │   └── ...
│   ├── coder/
│   │   ├── SOUL.md
│   │   ├── config.yaml
│   │   ├── state.db*
│   │   ├── projects.db*
│   │   ├── verification_evidence.db*
│   │   ├── skills/
│   │   └── ...
│   └── reviewer/
│       ├── SOUL.md
│       ├── config.yaml
│       ├── state.db*
│       ├── projects.db*
│       ├── skills/
│       └── ...
├── system/
│   ├── sshd_config
│   ├── authorized_keys
│   └── hermes-gateway.service
└── repo/
    └── Orbis-AI/  (optional export for offline rebuild)
```

Explicitly omitted from archive:
- `.env`, `auth.json`, private keys, tokens, session secrets

### 11.5 Manifest Structure

```json
{
  "work_package": "WP-005C",
  "created_at": "<ISO-8601>",
  "host": "sleep-cat",
  "platform": "WSL2 Ubuntu 26.04",
  "source_commit": "<git sha>",
  "profiles": {
    "root": { "soul_sha256": "...", "config_sha256": "...", "skills_count": N },
    "coder": { "soul_sha256": "...", "config_sha256": "...", "skills_count": N },
    "reviewer": { "soul_sha256": "...", "config_sha256": "...", "skills_count": N }
  },
  "skill_matrix": [
    { "profile": "...", "name": "...", "version": "...", "sha256": "..." }
  ],
  "non_git_state_classification": "<path/to/file>",
  "secrets": {
    "github": { "recovery_ref": "Hermes auth JSON + gh host config", "owner": "allday" },
    "telegram": { "recovery_ref": "/home/allday/.hermes/.env", "owner": "allday" },
    "ssh": { "recovery_ref": "Windows Hermes Desktop SSH trust + /home/allday/.ssh/authorized_keys", "owner": "allday" }
  },
  "excluded": [
    ".env", "auth.json", "private keys", "session secrets"
  ]
}
```

### 11.6 Integrity Verification Method

- SHA256 checksums for every archived file in `checksums.sha256`.
- Verify with `sha256sum -c checksums.sha256` before treating backup as valid.
- Manifest JSON should be validated against expected schema during restore.

### 11.7 Hash / Checksum Strategy

- Use SHA256 for files and SKILL.md artifacts.
- Record both source-runtime and repo-source skill SHA256s to detect drift.
- Record Hermes install commit hash for code rebuild reference.

### 11.8 Version / Date Metadata

- Backup folder name includes date and sequence.
- Manifest captures created_at, host, platform, source commit, Hermes version.
- Skill matrix captures exact deployed versions.

### 11.9 Restore Order

1. Restore OS/platform prerequisites if rebuilding.
2. Install Hermes runtime or extract hermes-agent directory from backup.
3. Restore system configs: `hermes-gateway.service`, `sshd_config`, `authorized_keys`.
4. Restore root SOUL/config and profile directories.
5. Restore runtime DBs only if acceptable data loss otherwise; otherwise start fresh and rebuild from Git/runtime source.
6. Restore Core Skills runtime copies and verify versions.
7. Recover secrets via secure stores/vaults per Section 10 procedures.
8. Start Hermes gateway and profiles; run fresh-session validation.
9. Validate GitHub auth, Telegram connectivity, Desktop SSH trust.
10. Run acceptance tests from WP-005C contract.

### 11.10 Retention Proposal

- Keep at least 3 rolling backups.
- One offline/secondary copy per month for critical milestones.
- Retain backup manifest history for audit.
- Retire old backups only after successful newer restore validation.

### 11.11 Backup Validation Procedure

- After creating backup, run `sha256sum -c checksums.sha256`.
- Validate manifest JSON parse and required fields.
- Perform dry-run restore in isolated environment for at least one backup per quarter.

### 11.12 Failure / Rollback Handling

- If backup creation fails mid-run, remove partial archive before retrying.
- If restore fails, stop and preserve existing running runtime; use prior known-good backup.
- Old server remains rollback target during migration phases; never delete until acceptance passes.

### 11.13 Offline / Secondary-Copy Recommendation

- Copy verified backup archive to a separate offline medium or host.
- Ensure recovery owner can access offline copy if primary runtime host is unavailable.

### 11.14 How Secrets Are Recovered Separately

- Secrets are never stored in backup archives or manifests.
- Secret recovery uses documented secure sources from Section 10.
- Restore procedure explicitly invokes secret recovery steps after runtime files are restored.

### 11.15 How to Prove Backup Completeness

- Manifest includes file inventory counts and checksums.
- Post-backup script compares archive file list to expected source inventory.
- Test restore proves recoverability without chat history.

---

## 12. Validation Summary

| Check | Result |
|---|---|
| SECRET_VALUE_EXPOSED | NO |
| RUNTIME_MODIFIED | NO |
| WINDOWS_LOCAL_HERMES_BACKEND_RUNNING | NO |
| DUPLICATE_ACTIVE_ORBIS_RUNTIME | NO |
| WP005C_SCOPE_EXPANDED | NO |
| RECOVERY_READINESS | FAIL until Project Owner confirms secure recovery sources exist and are accessible |
