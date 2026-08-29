# V1 Acceptance Tests

V1 is accepted only when each result is evidenced and reviewed.

| # | Criterion | Evidence |
|---|---|---|
| 1 | Telegram communicates with Hermes | Successful round-trip record |
| 2 | Telegram is limited to authorized users | Authorized/unauthorized test results |
| 3 | Hermes identifies a registered project | Registry lookup record |
| 4 | MASTER creates a task | Task record |
| 5 | CODER works in a development workspace | Branch/workspace and change evidence |
| 6 | REVIEWER reviews the result | Explicit PASS/FAIL report |
| 7 | REVIEWER FAIL returns work to CODER | Failed-review handoff and re-review evidence |
| 8 | Dangerous production actions require human approval | Approval-gate test record |
| 9 | Restart preserves important task state | Restart test record |
| 10 | Backup/recovery is tested | Restore and validation record |

All failures require a corrective task, re-test, and retained evidence before acceptance.
