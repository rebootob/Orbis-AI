# ORBIS AI — CODEX ENTRY POINT

## MANDATORY READ ORDER

Before repository work, read:

1. `project-docs/AI_CONTROL_PLANE.md`
2. `project-docs/AI_ACTIVE_TASK.md`
3. Only files explicitly referenced by the Active Task, directly affected files, and additional files when technically necessary.

Do not study the complete repository by default.

## EXECUTION RULE

Codex is the Orbis AI **EXECUTION PLANE**. ChatGPT is the **CONTROL PLANE**, Project Lead, Architect, and Reviewer. Codex executes clearly scoped implementation tasks and does not unnecessarily repeat planning, architecture, analysis, or review already performed by ChatGPT.

## ACTIVE TASK GATE

`project-docs/AI_ACTIVE_TASK.md` is the canonical current instruction. Before implementation, inspect `STATUS`.

Codex may execute only when status is `READY_FOR_CODEX` or `CHANGES_REQUESTED`. If it is `NOT_READY`, `BLOCKED`, `REVIEW_REQUESTED`, `REVIEW_PASS`, or `COMPLETED`, do not start unrelated implementation. Follow the state rules in `AI_CONTROL_PLANE.md`.

## CODEX ECONOMY RULE

Use minimum necessary context, implementation, targeted testing, and concise handoff. Avoid unrelated exploration, optional refactoring, speculative improvements, duplicate analysis, unnecessary full-repository reads/files/dependencies.

## HARD SAFETY RULES

Never expose secrets, commit credentials, force push, silently discard work, bypass human approval, self-approve, deploy production without authorization, or expand scope without necessity.

When implementation is ready for independent review, update `ai-review/REVIEW_HANDOFF.md`, set `REVIEW STATUS: REVIEW_REQUESTED`, then stop.
