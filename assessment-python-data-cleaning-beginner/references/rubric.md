# Rubric

Total score: 100

## 1. Data loading and runnability, 20

Check:
- Whether the program can run
- Whether the dataset can be read correctly

Suggested scoring:
- 16-20: runs and reads data correctly
- 10-15: mostly works
- 0-9: major running or reading issues

## 2. Required cleaning completion, 40

Check:
- remove duplicates
- remove rows with empty Customer ID
- remove rows with Quantity <= 0
- remove rows with Price <= 0

Suggested scoring:
- 32-40: required cleaning is mostly complete
- 20-31: partial completion
- 0-19: many missing steps

## 3. Date processing and export, 15

Check:
- Whether InvoiceDate is converted correctly
- Whether cleaned output is exported

Suggested scoring:
- 12-15: both done well
- 7-11: partial completion
- 0-6: missing or broken

## 4. Summary statistics output, 15

Check:
- Whether summary info is output
- Whether the numbers are basically reasonable

Suggested scoring:
- 12-15: summary is complete and reasonable
- 7-11: some summary exists
- 0-6: missing or unclear

## 5. Code quality and README, 10

Check:
- Whether code is basically readable
- Whether README explains the solution

Suggested scoring:
- 8-10: readable and explained
- 5-7: acceptable
- 0-4: messy or undocumented
