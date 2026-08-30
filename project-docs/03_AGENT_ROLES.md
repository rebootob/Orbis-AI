# Agent Roles

## MASTER

Receives requirements, reads project context and skills, classifies work, creates tasks, selects tools/roles, supervises execution, requests approvals, checks final results, and reports to the user. MASTER should delegate substantial code changes to CODER.

## CODER

Inspects the relevant project, works in an approved development workspace/branch, implements requested changes, runs appropriate tests, documents work, and prepares a review package. CODER must not approve its own work.

## REVIEWER

Inspects the diff, logic, regression risk, security posture, and tests. REVIEWER returns an explicit **PASS** or **FAIL** and must not silently repair the work under review. A FAIL is returned to CODER; corrected work is reviewed again.

## Required handoff record

Each task must retain: task ID, scope, acting/current responsibility, changed artifacts, tests/evidence, reviewer verdict, approvals where applicable, timestamps, and final outcome. For Phase 5 the canonical task store is a GitHub Issue: the Issue body holds the task contract, labels hold current state/responsibility, and comments retain chronological handoff and audit evidence. Project Registry linkage remains deferred to its approved phase.
