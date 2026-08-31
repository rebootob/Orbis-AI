# Changelog

All notable repository changes will be recorded here.

## [Unreleased]

### Added
- Documentation consolidation for new-chat resume: `project-docs/90_ARCHIVE/CHAT_HANDOFF_PRE_REORGANIZATION.md` updated to exact current repository truth through Phase 8 blocker.
- `project-docs/30_INTEGRATIONS/N8N.md` updated to current Phase 8 read-only-first state and local-test requirement.
- WP-008 sandbox provisioning: LOCAL_TEST sandbox proven (`127.0.0.1:5678`, n8n 2.36.9). Awaiting explicit Control Plane authorization for read-only MCP validation.

### Changed
- `project-docs/00_CONTROL/ACTIVE_TASK.md` reflects merged PR #29/PR #30, current blocker, and await-next-instruction state.
- `project-docs/90_ARCHIVE/CHAT_HANDOFF_PRE_REORGANIZATION.md` rewritten as authoritative new-chat snapshot; removed stale Phase 5 current/WP-005C not-started references.
- `project-docs/90_ARCHIVE/CHAT_HANDOFF_PRE_REORGANIZATION.md` updated to sandbox-proven status and exact current gate.

### Fixed
- Stale WP-008 planning state and outdated chat-handoff resume points replaced with current Phase 8 truth.
- Roadmap reconciled through Phase 8; backup/recovery document reconciled to partial-complete / Restore-DR deferred; final documentation sync for new-chat handoff.

## [WP-008] - 2026-08-31

### Added
- WP-008 planning docs: `project-docs/40_WORK_PACKAGES/WP-008/TASK_CONTRACT.md`
- WP-008 planning branch: `ai/wp-008-n8n-via-mcp-planning`
- PR #29 merged at `2eec0883cff47456960983d062bbce8b52c77c89`

## [WP-008 Closeout] - 2026-08-31

### Added
- WP-008 read-only validation evidence docs: `project-docs/40_WORK_PACKAGES/WP-008/MCP_VALIDATION_EVIDENCE.md`
- WP-008 MCP runtime proven in Hermes venv: mcp 2.0.0 + mcp-types 2.0.0
- PR #35 merged at `7fa62e1f38583d703782f14907faa2238f2a3c22`

### Changed
- `project-docs/00_CONTROL/ACTIVE_TASK.md` updated to READ-ONLY VALIDATION COMPLETE with Owner-accepted empty-sandbox qualification.
- `project-docs/90_ARCHIVE/CHAT_HANDOFF_PRE_REORGANIZATION.md` updated to closeout state.
- `project-docs/30_INTEGRATIONS/N8N.md` updated to reflect proven MCP runtime and read-only validation closeout.

### Fixed
- Stale MCP runtime evidence reconciled across canonical docs.
