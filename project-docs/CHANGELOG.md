# Changelog

All notable repository changes will be recorded here.

## [Unreleased]

### Added
- Documentation consolidation for new-chat resume: `project-docs/CHAT_HANDOFF.md` updated to exact current repository truth through Phase 8 blocker.
- `project-docs/08_N8N_INTEGRATION.md` updated to current Phase 8 read-only-first state and local-test requirement.
- WP-008 sandbox provisioning: LOCAL_TEST sandbox proven (`127.0.0.1:5678`, n8n 2.36.9). Awaiting explicit Control Plane authorization for read-only MCP validation.

### Changed
- `project-docs/AI_ACTIVE_TASK.md` reflects merged PR #29/PR #30, current blocker, and await-next-instruction state.
- `project-docs/CHAT_HANDOFF.md` rewritten as authoritative new-chat snapshot; removed stale Phase 5 current/WP-005C not-started references.
- `project-docs/CHAT_HANDOFF.md` updated to sandbox-proven status and exact current gate.

### Fixed
- Stale WP-008 planning state and outdated chat-handoff resume points replaced with current Phase 8 truth.
- Roadmap reconciled through Phase 8; backup/recovery document reconciled to partial-complete / Restore-DR deferred; final documentation sync for new-chat handoff.

## [WP-008] - 2026-08-31

### Added
- WP-008 planning docs: `project-docs/WP-008_TASK_CONTRACT.md`
- WP-008 planning branch: `ai/wp-008-n8n-via-mcp-planning`
- PR #29 merged at `2eec0883cff47456960983d062bbce8b52c77c89`

## [WP-008 Evidence] - 2026-08-31

### Added
- Issue #28 canonical truth updated to IMPLEMENTATION — READ-ONLY VALIDATION / BLOCKED AWAITING ENVIRONMENT.
- `project-docs/WP-008_TASK_CONTRACT.md` Section F updated with explicit MCP availability/version/mechanism evidence.
- PR #30 merged at `ae9dc212bcc0e4fad78179e37e51a23625808261`
