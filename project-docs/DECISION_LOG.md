# Decision Log

| ID | Decision | Status |
|---|---|---|
| ADR-001 | Hermes Agent is the primary orchestrator. | Accepted |
| ADR-002 | Telegram is the primary remote control interface. | Accepted |
| ADR-003 | n8n is an automation engine, not the primary AI orchestrator. | Accepted |
| ADR-004 | Initial agent count is limited to MASTER, CODER, and REVIEWER. | Accepted |
| ADR-005 | Prefer Skills and Tools over unnecessary Agents. | Accepted |
| ADR-006 | Git is mandatory. | Accepted |
| ADR-007 | Production/destructive actions require explicit human approval. | Accepted |
| ADR-008 | Prefer Hermes native capabilities before custom development. | Accepted |
| ADR-009 | V1 prioritizes simplicity and reliability over maximum automation. | Accepted |
| ADR-010 | GitHub repository `rebootob/Orbis-AI` is the official source-control repository for Orbis AI. | Accepted |
| ADR-011 | `main` is the stable branch and `develop` is the integration branch. | Accepted |
| ADR-012 | Secrets and runtime credentials must never be stored in GitHub. | Accepted |
| ADR-013 | Important sensitive/runtime data uses secure local backup rather than public Git storage. | Accepted |
| ADR-014 | Codex Economy Principle | Accepted |
| ADR-015 | Mandatory AI Control Plane | Accepted |
| ADR-016 | WSL2 Ubuntu is the primary Hermes runtime for Orbis AI. Windows Native Hermes is retained only as fallback because the Telegram gateway proved unstable on the current Windows-native runtime. | Accepted |

### ADR-014 — Codex Economy Principle

**Decision:** Codex is an execution resource and must be used only when repository, terminal, implementation, testing, or Git operations are materially required.

Planning, architecture, analysis, review, task decomposition, prompt preparation, governance, and decision-making should be performed by ChatGPT whenever possible.

Every Codex work package should:

- have a clearly defined objective;
- specify exact scope;
- specify affected files/components when known;
- specify tests;
- specify stop conditions;
- avoid unnecessary repository exploration;
- avoid unrelated refactoring; and
- avoid duplicate analysis already completed by ChatGPT.

**Default decision:** Do not invoke Codex unless execution is necessary.

**Goal:** Minimize Codex credit consumption without reducing implementation quality or safety.

### ADR-015 — Mandatory AI Control Plane

**Decision:** All AI implementation work must follow the permanent governance in `AGENTS.md` and `project-docs/AI_CONTROL_PLANE.md`. Current implementation scope is defined by `project-docs/AI_ACTIVE_TASK.md`; completed implementation is handed to the independent reviewer through `ai-review/REVIEW_HANDOFF.md`.

**Status:** Accepted

### ADR-016 — Primary Hermes Runtime

**Decision:** WSL2 Ubuntu is the primary Hermes runtime for Orbis AI. Windows Native Hermes is retained only as fallback because the Telegram gateway proved unstable on the current Windows-native runtime.

**Status:** Accepted

Future decisions should include context, alternatives, consequences, owner, and date. No implementation decision changes an accepted ADR without owner review.
