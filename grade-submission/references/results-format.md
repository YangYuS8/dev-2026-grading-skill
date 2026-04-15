# results/grades.csv payload format

Use these fields when calling `node scripts/update_grades_csv.js`:

```json
{
  "student_username": "student-name",
  "task_repo": "dev-2026-01",
  "submission_repo": "https://github.com/student/dev-2026-01",
  "score": 88,
  "graded_at": "2026-04-16T00:00:00Z",
  "issue_number": 12,
  "status": "graded",
  "notes": "README missing mobile screenshot"
}
```

## status values

- `graded`
- `partial`
- `invalid`
- `error`
