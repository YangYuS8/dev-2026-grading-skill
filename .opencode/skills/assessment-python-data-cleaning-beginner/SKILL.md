---
name: assessment-python-data-cleaning-beginner
description: Grade beginner Python data cleaning assessment submissions for dev-2026 style tasks. Use when evaluating a student's repo that reads a retail dataset, performs required cleaning steps with pandas, exports cleaned data, outputs summary statistics, and explains the solution in README.
---

# assessment-python-data-cleaning-beginner

Use this skill when grading beginner Python data cleaning submissions.

## What to grade

Evaluate the submission against these dimensions:

1. Data loading and runnability, 20 points
2. Required cleaning completion, 40 points
3. Date processing and export, 15 points
4. Summary statistics output, 15 points
5. Code quality and README, 10 points

Read the detailed rubric before grading:

- `references/rubric.md`

## How to grade

1. Read `README.md` if present.
2. Read `main.py` first.
3. Read `requirements.txt` if needed.
4. Check whether the student:
   - reads the dataset
   - removes duplicates
   - removes rows with empty Customer ID
   - removes rows with Quantity <= 0
   - removes rows with Price <= 0
   - converts InvoiceDate to datetime
   - exports cleaned data
   - outputs summary statistics
5. Prefer basic correctness over advanced style.
6. Use the format in `references/output-format.md`.

## Grading principles

- This task targets beginners, so do not require advanced data engineering structure.
- Reward a complete and understandable cleaning pipeline.
- If the code is simple but correct, do not over-penalize.
- Penalize only when required cleaning steps are missing or clearly broken.
