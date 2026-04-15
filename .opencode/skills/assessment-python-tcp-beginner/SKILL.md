---
name: assessment-python-tcp-beginner
description: Grade beginner Python TCP protocol assessment submissions for dev-2026 style tasks. Use when evaluating a student's repo that must implement a simple TCP server/client flow, follow a given protocol, pass core tests, and explain usage in README.
---

# assessment-python-tcp-beginner

Use this skill when grading beginner Python TCP submissions.

## What to grade

Evaluate the submission against these dimensions:

1. Environment setup and runnability, 20 points
2. Protocol understanding and implementation, 30 points
3. TCP communication ability, 20 points
4. Test results and correctness, 20 points
5. Code quality and README, 10 points

Read the detailed rubric before grading:

- `references/rubric.md`

## How to grade

1. Read `README.md` if present.
2. Read `TASK.md` and protocol-related files to understand expected behavior.
3. Read `server.py` first.
4. Read tests if needed.
5. Check whether the student:
   - can run the server
   - follows the required protocol
   - handles basic request/response flow
   - supports expected client/server communication
   - passes core tests or clearly matches expected behavior
6. Prefer basic correctness over advanced abstraction.
7. Use the format in `references/output-format.md`.

## Grading principles

- This task targets beginners, so do not require advanced socket engineering patterns.
- Reward a clear and working basic implementation.
- If the logic is understandable and mostly correct, do not over-penalize simple code.
- Penalize broken protocol handling, failure to run, or missing core behavior.
