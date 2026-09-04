# ORBIS AI — CODEX ENTRY POINT

## MANDATORY READ ORDER

Before repository work, read:

1. `project-docs/00_CONTROL/START_HERE.md`
2. `project-docs/00_CONTROL/CURRENT_STATE.md`
3. `project-docs/00_CONTROL/ACTIVE_TASK.md`
4. `project-docs/00_CONTROL/DOCUMENT_INDEX.md`
5. Only files directly relevant to an authorized Active Task, directly affected files, and additional files when technically necessary.

Do not study the complete repository by default.

## EXECUTION RULE

This file is the mandatory entry point when Codex is explicitly assigned repository work.

ChatGPT remains the Orbis AI **CONTROL PLANE**, Project Lead, Architect, and independent repository reviewer. Hermes Agent is the primary Orbis runtime/orchestrator. Codex is an optional execution worker for explicitly authorized, clearly scoped tasks and must not replace MASTER, CODER, REVIEWER, or the Control Plane.

## ACTIVE TASK GATE
ฝ
`project-docs/00_CONTROL/ACTIVE_TASK.md` is the canonical current instruction. Before implementation, inspect `STATUS`.

Codex may execute only when status is `READY_FOR_CODEX` or `CHANGES_REQUESTED`. If it is `IDLE`, `NOT_READY`, `BLOCKED`, `REVIEW_REQUESTED`, `REVIEW_PASS`, or `COMPLETED`, do not start unrelated implementation. Follow the state rules in `project-docs/10_GOVERNANCE/AUTHORITY_MODEL.md`.

## CODEX ECONOMY RULE

Use minimum necessary context, implementation, targeted testing, and concise handoff. Avoid unrelated exploration, optional refactoring, speculative improvements, duplicate analysis, unnecessary full-repository reads/files/dependencies.

## HARD SAFETY RULES

Never expose secrets, commit credentials, force push, silently discard work, bypass human approval, self-approve, deploy production without authorization, or expand scope without necessity.

When implementation is ready for independent review, update `ai-review/REVIEW_HANDOFF.md`, set `REVIEW STATUS: REVIEW_REQUESTED`, then stop.






## HERMES ROUTING POLICY

Hermes primary model is the Control Plane assistant.

Use the primary model for:
- conversation with the Owner
- planning
- architecture
- review
- summarization
- deciding whether execution is materially necessary

Antigravity is the bounded execution worker for tasks that materially require:
- repository inspection
- code investigation
- implementation
- running tests, build, or lint
- bounded technical execution

Do not delegate for:
- greetings
- simple questions
- explanations answerable from current context
- summaries that do not require new repository inspection
- repeated status checks when no new execution is required

The primary Hermes agent MUST NOT perform live repository execution itself
when the task requires new repository inspection or technical execution.

For any task requiring:
- git status / git log / git diff inspection
- repository file inspection not already available in current context
- code investigation
- implementation
- running tests, build, or lint
- other live terminal-based repository work

the primary Hermes agent MUST delegate the bounded task to the configured
Antigravity execution worker.

The primary Hermes agent remains responsible for:
- understanding the Owner request
- defining the smallest necessary execution task
- enforcing READ-ONLY or implementation boundaries
- reviewing the worker result
- reporting the conclusion to the Owner

The primary Hermes agent MUST NOT substitute its own terminal execution
for a task that requires delegation.

Do not delegate when the answer can be produced from current context
without new repository or terminal access.

### EXECUTION FAILURE SAFETY GUARD

If a delegated execution worker fails because of:
- quota exhaustion
- authentication failure
- provider error
- timeout
- unavailable model
- connection failure
- other execution-worker failure

the primary Hermes agent MUST NOT perform the blocked repository execution itself.

Instead, the primary agent must:
1. report the worker failure clearly to the Owner
2. preserve the requested execution boundary
3. avoid terminal or repository execution as a substitute
4. wait for Owner instruction, worker recovery, or an explicitly authorized alternative worker

A failed delegated execution MUST NOT silently fall back to primary-agent execution.

For READ-ONLY tasks:
- do not substitute primary-agent terminal inspection after worker failure

For implementation tasks:
- do not modify files after worker failure

For commit, push, merge, deploy, production, destructive, credential, or security actions:
- explicit Owner approval is always required

### IMPLEMENTATION AUTHORIZATION GUARD

Repository inspection may be performed when allowed by the current task boundary.

Implementation is NOT authorized merely because repository inspection is allowed.

Before any implementation, file modification, test modification, generated source change,
or other write operation, the execution worker MUST inspect:

`project-docs/00_CONTROL/ACTIVE_TASK.md`

Implementation is permitted only when the canonical task status explicitly allows execution,
including:

- `READY_FOR_CODEX`
- `CHANGES_REQUESTED`

If the status is any non-execution state, including:

- `IDLE`
- `NOT_READY`
- `BLOCKED`
- `REVIEW_REQUESTED`
- `REVIEW_PASS`
- `COMPLETED`

the execution worker MUST NOT modify repository files.

When implementation is not authorized:
1. stop before any file write
2. report the current task status to the primary agent
3. report that implementation is not authorized
4. do not create a workaround task
5. do not change the task status
6. do not edit ACTIVE_TASK.md to authorize itself
7. wait for explicit Owner-authorized task state or instruction

READ-ONLY inspection does not imply implementation authorization.

The primary Hermes agent MUST NOT bypass this guard by performing implementation itself.


### READ-ONLY

For READ-ONLY tasks:
- inspection only
- do not modify files
- do not create files
- do not change branches
- do not commit
- do not push
- do not merge
- do not deploy

### OWNER APPROVAL REQUIRED

Explicit Owner approval is required before:
- commit
- push
- merge
- deploy
- production changes
- destructive commands
- credential or security changes

### ECONOMY RULE

Use Antigravity only when materially necessary.
Prefer one delegated worker at a time.
Minimize delegated turns, context, and token usage.
