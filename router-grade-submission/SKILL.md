---
name: router-grade-submission
description: Route a student submission issue to the correct dev-2026 grading skill by inspecting the submitted repo name, then post the score back to the issue, append a row to results/grades.csv, and close the issue. Use when handling GitHub issue based submission intake for dev-2026 tasks.
---

# router-grade-submission

Use this skill when grading student submissions that arrive through GitHub issues.

## What this skill does

1. Read the submission issue.
2. Extract:
   - student GitHub username
   - task repo name
   - student submission repo URL
   - optional notes
3. Choose the grading skill by task repo name:
   - `dev-2026-01` -> `assessment-html-css-beginner`
   - `dev-2026-02` -> `assessment-js-api-beginner`
   - `dev-2026-03` -> `assessment-python-data-cleaning-beginner`
   - `dev-2026-04` -> `assessment-python-deepseek-cli-beginner`
   - `dev-2026-05` -> `assessment-python-tcp-beginner`
4. Clone or inspect the student repo.
5. Grade it with the selected skill.
6. Reply to the issue with the grading result.
7. Append the result to `results/grades.csv`.
8. Close the issue.

## Required workflow

### Step 1
Use `gh issue view` or equivalent to read the issue content.

### Step 2
Determine the correct grading skill from the submitted task repo name.

### Step 3
Inspect the student repository.

### Step 4
Run the matching grading process and produce the standard score output.

### Step 5
Post the result back to the issue.

### Step 6
Update `results/grades.csv`.

Read the CSV rules before updating:

- `references/results-format.md`

### Step 7
Close the issue after writing the result.

## Partial submissions

If the student clearly left some work unfinished:

- still grade what exists
- mark missing parts in the issue reply
- write `status=partial` in the CSV if the repo is incomplete but gradable

If the repository is invalid or inaccessible:

- write a short failure reason
- use `status=invalid` or `status=error`
- still record the attempt in the CSV

## Important notes

- Do not fail silently.
- Always leave a visible issue reply.
- Always try to write a CSV row, even for invalid submissions.
- Keep output format consistent with the grading skills.
