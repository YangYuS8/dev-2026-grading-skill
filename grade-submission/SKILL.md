---
name: grade-submission
description: Main entry skill for dev-2026 grading. Use when running a command like /grade <issue-number> or grading a GitHub issue submission in OpenCode or OpenClaw. Reads the issue with gh, detects the task repo, chooses the correct grading skill, posts the result back to the issue, updates results/grades.csv, and closes the issue.
---

# grade-submission

Use this as the main entry skill for the grading workflow.

## Trigger

Use this skill when the operator says things like:

- `/grade 12`
- `grade issue 12`
- `处理第 12 个提交 issue`

## Expected workflow

1. Parse the issue number from the request.
2. Use `gh issue view <number> --json number,title,body,url` to read the issue.
3. Extract these fields from the issue body:
   - GitHub username
   - task repo name
   - submission repo URL
   - notes
4. Choose the grading skill by repo name:
   - `dev-2026-01` -> `assessment-html-css-beginner`
   - `dev-2026-02` -> `assessment-js-api-beginner`
   - `dev-2026-03` -> `assessment-python-data-cleaning-beginner`
   - `dev-2026-04` -> `assessment-python-deepseek-cli-beginner`
   - `dev-2026-05` -> `assessment-python-tcp-beginner`
5. Clone the student repo to a temp directory.
6. Read and apply the selected grading skill.
7. Produce the standard grading output.
8. Post the grading result back to the issue with `gh issue comment`.
9. Update `results/grades.csv` by calling:
   - `node scripts/update_grades_csv.js '<json>'`
10. Close the issue with `gh issue close`.

## Partial submissions

If the repository is incomplete but still gradable:

- grade what exists
- mention missing parts clearly
- use `status=partial`

If the repository is invalid or inaccessible:

- leave a visible issue reply
- write a CSV row with `status=invalid` or `status=error`
- close the issue only after writing the result

## CSV payload format

Read before writing:

- `references/results-format.md`

## Important rule

This skill is the orchestration entrypoint.

It should not replace the per-task grading skills. It must route to them.
