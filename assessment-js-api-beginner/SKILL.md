---
name: assessment-js-api-beginner
description: Grade beginner JavaScript API interaction assessment submissions for dev-2026 style tasks. Use when evaluating a student's repo that must complete DOM handling, GET and POST API calls, list rendering, filtering, user feedback, and README explanation.
---

# assessment-js-api-beginner

Use this skill when grading beginner JavaScript assessment submissions for the API interaction task.

## What to grade

Evaluate the submission against these dimensions:

1. DOM selection and event binding, 20 points
2. GET request and list rendering, 25 points
3. POST request and submission handling, 20 points
4. Data handling and filtering, 15 points
5. Error handling and user feedback, 10 points
6. Code quality and README, 10 points

Read the detailed rubric before grading:

- `references/rubric.md`

## How to grade

1. Read `README.md` if present.
2. Read `scripts/main.js` first.
3. Read related HTML only as needed to confirm DOM ids/classes.
4. Check whether the student:
   - selects needed DOM nodes
   - binds load/click/submit/change events
   - sends GET requests
   - renders list data into the page
   - sends POST requests with the correct payload
   - filters tasks by status
   - shows success or error messages
5. Prefer scoring by working logic over code style perfection.
6. Use the format in `references/output-format.md`.

## Grading principles

- This task targets beginners, so do not require advanced abstractions.
- If the basic workflow is complete, reward it.
- If code is plain but understandable, do not over-penalize.
- Penalize only when logic is missing, clearly broken, or copied with no understanding.
