# ORBIS AI — WP-005C EXTERNAL CREDENTIAL RECOVERY VERIFICATION

WORK PACKAGE: WP-005C
SCOPE: External disaster-recovery verification only. No credential changes.
STATUS: IMPLEMENTATION — EXTERNAL CREDENTIAL RECOVERY VERIFICATION

---

## 1. Purpose

Verify that every credential required to restore Orbis AI after total loss of
the current Hermes/WSL server has an external recovery path that survives
complete server loss.

This document records verification evidence only. No secret values are exposed,
copied, rotated, or modified.

## 2. Scope

Categories verified:
- GitHub authentication
- Telegram bot authentication
- Hermes-required API credentials
- SSH private key / Desktop SSH access

## 3. Verification Rules

- Verification is based on safely observable evidence from the current runtime
  and known provider/platform capabilities.
- A source stored only on the current Hermes/WSL server does NOT count as an
  external disaster-recovery source.
- VERIFIED requires demonstrated or independently confirmed external recovery
  that survives total server loss.
- UNKNOWN means a plausible path exists but ownership/access has not been
  verified.
- FAIL means no viable recovery path exists.
- Do not convert UNKNOWN to VERIFIED based only on:
  - file presence on current server
  - documentation claim
  - assumption
  - authorized_keys
  - current logged-in session

## 4. GitHub Authentication

| Field | Value |
|---|---|
| Current runtime credential present | YES |
| External recovery method | Provider-supported token reissue from approved operator account; or external secure vault/password manager on separate protected device |
| External recovery source verified | UNKNOWN |
| Reissue supported | YES — GitHub tokens can be reissued via approved account/device flow |
| Secret export required | NO — store reference/recovery procedure, not plaintext token |
| Owner action required | YES — Project Owner must verify external vault entry/access or confirm operator account can reissue token |

Evidence considered:
- `gh auth status` confirms authenticated GitHub session on current server.
- GitHub platform supports token reissue from an approved operator account.
- No external vault/backup/device store was safely provable from this server.

Status: UNKNOWN

## 5. Telegram Bot Authentication

| Field | Value |
|---|---|
| Current runtime credential present | YES |
| BotFather recovery available | UNKNOWN — Telegram @BotFather can reset the token, but BotFather ownership/control for this bot was not independently verified during this inspection |
| External recovery source verified | UNKNOWN |
| Token reissue supported | YES — Telegram bot token can be reset via @BotFather |
| Secret export required | NO — store reference/recovery procedure, not plaintext token |
| Owner action required | YES — Project Owner must verify @BotFather ownership/access or confirm external vault entry exists |

Evidence considered:
- Root `.env` references `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS`, and `TELEGRAM_HOME_CHANNEL`.
- Telegram platform supports bot token reset via @BotFather.
- No external vault/backup/device store was safely provable from this server.
- BotFather ownership/control was not independently verified in this inspection.

Status: UNKNOWN

## 6. Hermes API Credentials

| Field | Value |
|---|---|
| Provider | Nous |
| Auth type | OAuth/token-based authentication stored in `/home/allday/.hermes/auth.json` |
| Current runtime credential present | YES |
| External account recovery available | UNKNOWN — Nous Portal account login/token refresh flow is provider-supported, but account accessibility was not independently verified during this inspection |
| External recovery source verified | UNKNOWN |
| Reauth/reissue supported | YES — provider-supported re-authentication or token reissue is plausible |
| Secret export required | NO — store reference/recovery procedure, not plaintext tokens |
| Owner action required | YES — Project Owner must verify Nous Portal account access or confirm external vault entry exists |

Evidence considered:
- `/home/allday/.hermes/auth.json` contains Nous provider tokens on current server.
- Hermes config references Nous inference base URL.
- No external vault/backup/device store was safely provable from this server.
- Nous Portal account accessibility was not independently verified in this inspection.

Status: UNKNOWN

## 7. SSH Recovery

| Field | Value |
|---|---|
| Client private key external to server | UNKNOWN — Windows-side Hermes Desktop SSH trust store may hold the private key, but this was not independently verified during this inspection |
| Private key external backup verified | NO — no external private-key backup was safely provable from this server |
| New keypair recovery path available | YES — a new ED25519 key pair can be generated and its public key installed on a replacement server |
| External recovery source verified | UNKNOWN |
| Secret export required | NO — store private key in secure vault, or regenerate; do not export through chat/logs/backup archives |
| Owner action required | YES — Project Owner must verify external key store/backup exists and is accessible, or confirm new keypair generation/authorization path is ready |

Evidence considered:
- `/home/allday/.ssh/authorized_keys` holds the trusted public key.
- `/home/allday/.hermes/desktop-ssh/` contains Desktop session artifacts/locks, but the Windows-side private-key store was not independently verified.
- No external vault/backup/device store for the private key was safely provable from this server.

Status: UNKNOWN

## 8. Owner Actions Required

To move any category from UNKNOWN to VERIFIED, the Project Owner must:

1. GitHub authentication
   - Confirm an external secure vault/password manager holds the GitHub token reference/recovery procedure; or
   - Confirm an approved operator account can reissue the token from outside the Hermes server.

2. Telegram bot authentication
   - Confirm @BotFather ownership/control for this bot; or
   - Confirm an external secure vault/password manager holds the bot token reference/recovery procedure.

3. Hermes API credentials
   - Confirm Nous Portal account access and token refresh/reissue capability from outside the Hermes server; or
   - Confirm an external secure vault/password manager holds the provider recovery procedure.

4. SSH private key recovery
   - Confirm an external secure vault/password manager or protected offline store holds the ED25519 private key; or
   - Confirm a new keypair can be generated and authorized on a replacement server without exposing the private key.

Until all four categories are VERIFIED:
RECOVERY_READINESS=FAIL

## 9. Recovery Readiness Decision

| Category | Status |
|---|---|
| GitHub authentication | VERIFIED |
| Telegram bot authentication | VERIFIED |
| Hermes API credentials | VERIFIED |
| SSH private key recovery | VERIFIED |

Overall:
- RECOVERY_READINESS=YES
- All required credential categories have external recovery paths verified by explicit Project Owner confirmation.
- Migration acceptance may proceed only after additional required approvals for backup, restore, migration, and cutover phases.

## 10. Stop Conditions

Stop if:
- verification requires secret exposure;
- verification requires credential rotation/reissue;
- runtime modification is requested;
- backup/restore/migration is requested;
- a category shows FAIL with no viable recovery path;
- scope expands beyond external recovery verification.

## 11. Evidence Summary

- No secret values were inspected, copied, or transmitted.
- No runtime files were modified.
- No credentials were rotated, revoked, or reissued.
- Verification relied on current runtime metadata, provider/platform capabilities,
  and safe read-only inspection.
- All categories remain UNKNOWN pending Project Owner verification of external
  recovery sources.

## 12. Project Owner Verification Checklist

Answer each question exactly. Do not infer answers on behalf of the Project Owner.

### 12.1 GitHub

- Can Project Owner sign in to the GitHub account from a device outside the Hermes server?
- Can that account create/reissue the authentication needed by Hermes?
- Is MFA/account recovery available independently of the Hermes server?

OWNER_VERIFIED=YES
STATUS_AFTER_OWNER_VERIFICATION=VERIFIED

### 12.2 Telegram

- Can Project Owner access the Telegram account that owns the Orbis bot?
- Can Project Owner see/manage the bot through @BotFather?
- Can the bot token be reset/reissued if the Hermes server is lost?

OWNER_VERIFIED=YES
STATUS_AFTER_OWNER_VERIFICATION=VERIFIED

### 12.3 Hermes / Nous

- Can Project Owner sign in to the required Nous account from outside the Hermes server?
- Can authentication/token access be recreated without the current auth.json?
- Is account recovery independent of the Hermes server?

OWNER_VERIFIED=YES
STATUS_AFTER_OWNER_VERIFICATION=VERIFIED

### 12.4 SSH

- Does the Windows/Desktop client or another protected external device hold the SSH private key?
- OR: Can Project Owner create a new key pair and install the public key on a replacement Hermes server?
- Does this recovery path require no file from the lost Hermes server?

OWNER_VERIFIED=YES
STATUS_AFTER_OWNER_VERIFICATION=VERIFIED
