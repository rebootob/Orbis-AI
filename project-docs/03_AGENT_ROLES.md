# Agent Roles

## MASTER

Receives requirements, reads project context and skills, classifies work, creates tasks, selects tools/roles, supervises execution, requests approvals, checks final results, and reports to the user. MASTER should delegate substantial code changes to CODER.

## CODER

Inspects the relevant project, works in an approved development workspace/branch, implements requested changes, runs appropriate tests, documents work, and prepares a review package. CODER must not approve its own work.

## REVIEWER

Inspects the diff, logic, regression risk, security posture, and tests. REVIEWER returns an explicit **PASS** or **FAIL** and must not silently repair the work under review. A FAIL is returned to CODER; corrected work is reviewed again.

## Required handoff record

Each task should retain: task ID, registered project, scope, acting role, changed artifacts, tests/evidence, reviewer verdict, approvals, timestamps, and final outcome. The storage mechanism is `<TO_BE_DEFINED>`.
