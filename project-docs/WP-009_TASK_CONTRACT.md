# WP-009 — Automation / Cron Planning

WORK PACKAGE:
WP-009 — AUTOMATION / CRON PLANNING ONLY

STATUS:
PLANNING ONLY — NO IMPLEMENTATION AUTHORIZED

ISSUE:
#38

BRANCH:
ai/wp-009-automation-cron-planning

TARGET:
develop

## Objective

Define the minimum safe automation/cron architecture for Orbis AI.
This document is planning only. No automation is created, activated, or executed.

## Authority

- Phase 9 PLANNING ONLY is explicitly authorized.
- Any implementation requires a separate explicit Project Owner authorization.
- Level 3 actions always require exact Project Owner approval.

## Scope

A. Inventory
- Enumerate existing scheduling/automation capabilities in Hermes, GitHub Actions, n8n, and systemd/cron.
- Identify what is already proven and what remains theoretical.

B. Minimum automation needs
- Scheduling: periodic repository/runtime checks and evidence collection.
- Monitoring: health checks for Hermes runtime, n8n LOCAL_TEST sandbox, GitHub connectivity.
- Retry/failure handling: bounded retry with exponential backoff; fail-closed on ambiguity.
- Notification: structured evidence comments on GitHub Issues; no Telegram side effects unless separately authorized.
- Approval-gated execution: Level 2/3 actions require approval evidence before execution.
- Audit logging: every scheduled run, outcome, and approval decision is recorded.

C. Ownership model
- Hermes cronjobs: runtime-bound automation tied to Hermes session lifecycle.
- GitHub Actions: repository-event automation and CI evidence.
- n8n: reserved for future approved Phase 9+ integrations after write-capability authorization.
- Native cron/systemd timers: fallback only if Hermes runtime is unavailable.
- GitHub Issues/comments: canonical audit and evidence layer.

D. Preferred architecture
- Use Hermes cronjobs as the primary scheduler for runtime-bound jobs.
- Use GitHub Actions as the primary scheduler for repository-bound jobs.
- Avoid duplicate schedulers.
- Prefer existing proven capabilities over new frameworks/services.

E. Fail-closed behavior
- Missing approval evidence blocks execution.
- Missing runtime/runtime dependency blocks execution.
- Ambiguous environment identity blocks execution.
- Network failure blocks execution unless explicit offline tolerance is configured.
- No silent skip; every skipped execution is audited.

F. Level behavior for scheduled jobs
- Level 0 reads: automatic.
- Level 1 writes: automatic within approved scope.
- Level 2: requires review evidence before execution.
- Level 3: requires exact valid Owner authorization before execution; otherwise `OWNER_APPROVAL_REQUIRED`.

G. Job lifecycle
- Inspect: list all jobs and their current status.
- Pause: temporarily suspend without deletion.
- Resume: re-enable paused job.
- Disable: permanently disable; retained in audit history.
- Audit: every change is recorded in GitHub Issue evidence.

H. Offline behavior
- Hermes/Desktop/WSL/n8n offline: job records missed run; retry on next scheduled execution; failure is audited.
- No hidden side effects; no recovery execution that bypasses approval gates.

I. Startup/restart persistence
- Job registry persists in repository documentation.
- Pending approvals and failed runs survive restart via GitHub Issue evidence.
- Runtime state is re-derived from GitHub canonical state on restart.

J. Minimum health monitoring
- Hermes runtime presence.
- n8n LOCAL_TEST sandbox health.
- GitHub connectivity.
- Connectivity results are recorded; failures do not auto-recover.

K. Test strategy
- LOCAL_TEST only.
- Dry-run mode for all automation.
- No dummy production-like data.
- No writes to production or external systems.

## Recommended Architecture

### Primary scheduler: Hermes cronjobs
- Runtime-bound periodic jobs.
- Uses existing Hermes cron infrastructure.
- Local-only by default.
- Outbound only; no inbound port exposure.

### Repository scheduler: GitHub Actions
- Repository-event automation.
- Proven CI/CD evidence collection.
- No additional runtime dependency.

### Reserved: n8n
- n8n automation remains NOT AUTHORIZED until write-capability is separately approved.
- Planning only; no n8n workflow creation or activation.

### Fallback: native cron/systemd timers
- Used only if Hermes runtime is unavailable.
- Does not bypass approval gates.
- Does not execute Level 2/3 actions without evidence.

### Canonical audit layer: GitHub Issues
- Every job run, approval decision, and failure is recorded as an Issue comment.
- GitHub Issues remain the durable task/audit store.

## Minimum Safe Implementation Scope

1. Job registry documentation.
2. Dry-run test job in Hermes cron.
3. Health-check job with LOCAL_TEST target only.
4. Approval-gated action schema for future Level 2/3 jobs.
5. Audit logging via GitHub Issue comments.
6. Pause/resume/disable inspection commands.
7. Fail-closed test coverage.

## Test Matrix

| Test | Target | Expected Result |
|---|---|---|
| Hermes cron dry run | LOCAL_TEST | PASS / evidence recorded |
| Health check | LOCAL_TEST | PASS or FAIL; failure audited |
| Approval gate | simulated Level 2 | BLOCKED without approval evidence |
| Level 3 gate | simulated Level 3 | `OWNER_APPROVAL_REQUIRED` |
| Offline Hermes | cron stopped | missed run audited; retry next cycle |
| Offline n8n | sandbox down | health check FAIL; no recovery action |
| Pause/resume | any approved job | state change audited |
| Disable | any approved job | job disabled; history retained |
| Fail-closed | missing approval | execution blocked; audited |

## Security / Permission Gates

- Secrets remain outside Git.
- No production credentials in planning docs.
- Level 3 actions require exact Owner approval for exact action and target.
- Approval evidence must include: Task ID, action, permission level, actor, timestamp, outcome.
- Fail-closed on missing/ambiguous approval/authority/identity/scope.

## Rollback / Disable Plan

- Disable any job via documented pause/disable command.
- Delete job from Hermes cron registry or GitHub Actions.
- Retain audit history in GitHub Issues.
- No runtime rollback beyond disabling the job.

## Out of Scope

- Production automation
- Live cron creation/activation
- n8n writes or workflow execution
- Deployment automation
- Credential changes
- Kintone changes
- Telegram side effects unless separately authorized
- Restore/DR
- Phase 9 implementation
- Autonomous Level 3 execution

## Next Implementation Gate

Any implementation requires:
1. Separate explicit Project Owner authorization for Phase 9 implementation.
2. A new dedicated implementation branch from current develop.
3. Runtime REVIEWER PASS on exact branch HEAD.
4. ChatGPT Control Plane REVIEW_PASS.
5. Explicit Project Owner approval for merge.

STOP here. Do not start implementation.
