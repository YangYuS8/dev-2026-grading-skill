# results/grades.csv format

The CSV file should contain these columns:

- student_username
- task_repo
- submission_repo
- score
- graded_at
- issue_number
- status
- notes

## status values

Use one of:

- graded
- partial
- invalid
- error

## Notes

- `score` can be 0 when submission is invalid.
- `notes` should be short and machine-friendly when possible.
- If a student submits multiple times, append a new row instead of deleting old rows.
