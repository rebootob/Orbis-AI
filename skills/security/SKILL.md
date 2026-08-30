---
name: security
description: Protect Orbis secrets, permission ceilings, approvals, and safe escalation.
version: 0.1.0
---

# Security

## Purpose

Protect credentials, enforce permission ceilings, identify approval gates, and stop unsafe work.

## When to Use

Use for any task that reads, changes, reviews, pushes, or reports security-sensitive artifacts or permissions.

## Applicable Role

MASTER, CODER, and REVIEWER.

## Required Inputs

Work Package, affected artifacts, permission classification, approval state, intended actions, security tests, and rollback plan.

## Scope

Protect passwords, API keys, Telegram/GitHub/Kintone tokens, n8n credentials, OAuth access/refresh tokens, cookies/session secrets, private keys/certificates, `.env` values, and production credentials. If a secret is discovered, stop exposing content and report only affected file/location, risk category, and corrective action.

## Allowed Tools

Only tools already enabled for the active profile and allowed by the current Work Package and Control Plane may be used. This Skill grants no tools, credentials, permissions, approval authority, or higher permission level.

## Permission Ceiling

Security inspection and evidence collection only. This Skill does not authorize credential, permission, or production changes.

## Procedure

1. Classify the action: L0 reads, L1 explicitly authorized development writes, L2 important writes/push/integration under review controls, or L3 production, destructive, permission, credential, migration, force-push, or equivalent sensitive action.
2. Confirm explicit authorization required by the classification.
3. Perform secret-safe diff and evidence inspection without revealing secret values.
4. Stop and report safe metadata if a secret or unsafe condition is found.
5. Escalate all L3 actions to the Project Owner.

## Role Identity Preservation

This shared Skill provides governance guidance only; it does not assign or combine runtime roles.

- The active Hermes profile/role remains authoritative.
- MASTER must identify as MASTER only.
- CODER must identify as CODER only.
- REVIEWER must identify as REVIEWER only.
- A role may describe another role's responsibilities without adopting that role.
- Never combine role labels such as `MASTER / REVIEWER` or `CODER / REVIEWER`.
- Using a shared Skill does not change the active role or grant another role's authority.

## Authority Separation

Security-sensitive workflow must preserve these authority boundaries:

- MASTER coordinates work but does not grant itself approval authority.
- CODER implements authorized work but cannot self-approve.
- Runtime REVIEWER may return PASS or FAIL evidence but cannot set repository `REVIEW_PASS`.
- Final repository `REVIEW_PASS` authority belongs to the ChatGPT Control Plane.
- Merge authorization belongs to the Project Owner.
- All Level 3 authorization belongs to the Project Owner.
- No Skill, Agent, or runtime verdict may substitute for these authorities.

## Verification

Record secret-safe diff result, permission classification, final repository REVIEW_PASS authority, approval evidence when applicable, and security-related tests actually executed.

## Audit Output

Record risk category, affected artifact, permission level, approval status, verification result, and unresolved blockers.

## Escalation Conditions

Escalate missing authorization, destructive action, credentials or permission changes, production changes, ambiguous security scope, failed security verification, unexpected secret exposure, or any Level 3 action.

## Pitfalls

Block rather than invent a workaround when an approval or security requirement is unmet. No AI or Skill may bypass Level 3 controls.
