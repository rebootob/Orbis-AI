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

Future decisions should include context, alternatives, consequences, owner, and date. No implementation decision changes an accepted ADR without owner review.
