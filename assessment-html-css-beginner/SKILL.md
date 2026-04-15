---
name: assessment-html-css-beginner
description: Grade beginner HTML+CSS assessment submissions for dev-2026 style tasks. Use when evaluating a student's static page repo for structure, layout, styling, responsiveness, README quality, and obvious template-copy risks, then produce a score breakdown and concise feedback.
---

# assessment-html-css-beginner

Use this skill when grading beginner front-end submissions for the HTML + CSS assessment.

## What to grade

Evaluate the submission against these dimensions:

1. HTML structure and basic semantics, 20 points
2. CSS layout ability, 25 points
3. Styling completeness, 20 points
4. Responsive adaptation, 20 points
5. Code quality, 10 points
6. README quality, 5 points

Read the detailed rubric before grading:

- `references/rubric.md`

## How to grade

1. Read the student's `README.md` if present.
2. Read the main HTML and CSS files.
3. Verify the page structure exists:
   - top area
   - navigation area
   - main content
   - cards
   - task list
   - extra info block
4. Check whether flex or grid is used.
5. Check whether hover/focus styles exist.
6. Look for signs of responsive handling, such as:
   - media queries
   - stacked layout on small screens
   - width rules that avoid overflow
7. Note obvious risks:
   - copied template traces
   - chaotic structure
   - no mobile adaptation
8. Produce a score using the output format in `references/output-format.md`.

## Grading principles

- This assessment targets true beginners, so do not score like a senior front-end code review.
- Reward clear completion of basics.
- Do not over-penalize visual plainness if the structure and layout are correct.
- Penalize broken pages, unreadable structure, or obvious template copying.
- Keep feedback concrete and short.

## When uncertain

If part of the repo is missing or the page cannot be fully previewed, say what was verifiable from source inspection and score conservatively.
