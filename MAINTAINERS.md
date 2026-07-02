# Assignment Pull Request Maintenance

## Refresh the Open PR Audit

Authenticate the GitHub CLI with a maintainer account, then run:

```bash
gh auth status
python3 scripts/audit_open_prs.py \
  --repo z-pandeyji/BIT-SummerTraining \
  --output audits/open-prs.csv
```

The audit records every open PR, changed path, structure result, duplicate group,
completion decision, review notes, and action. Refreshing the file preserves
rows already marked complete or incomplete while adding new PRs and removing
closed PRs.

## Review Rules

1. Group submissions by `day`, `batch`, and `student`.
2. Review only the newest PR in each duplicate group; close older duplicates as
   superseded.
3. Compare `solution.py` with every numbered requirement in that day's
   `questions.md`.
4. Confirm required CSV or chart files are present for Days 7, 10, and 11.
5. Compile the Python file before merging.
6. If runtime verification is needed, use a disposable environment with no
   repository credentials, no network access, a short timeout, and
   `MPLBACKEND=Agg`. Never run student code in the maintainer checkout.

Use these audit values:

- `completion_status`: `complete`, `incomplete`, or `pending-review`.
- `action`: `merge`, `repair`, `close-incomplete`, `close-obsolete`, or the
  generated duplicate action.
- `review_notes`: the exact missing question, runtime problem, or repair reason.

## Merge and Repair

- Merge a clean, complete PR with the repository's normal merge-commit method.
- For a complete PR with bad paths, create a clean branch from the latest
  `main`, copy only that assignment's approved files into the canonical folder,
  open a repair PR that links the original PR, merge it, and close the original.
- Split a complete multi-day PR into one repair PR per day.
- Comment with exact missing work and the expected path before closing an
  incomplete PR.
- Refresh `audits/open-prs.csv` after every merge batch.

## Required Check

After `.github/workflows/validate-assignment-pr.yml` has run successfully on
`main`, edit the `main` branch protection rule in GitHub:

1. Enable **Require status checks to pass before merging**.
2. Select the `assignment-structure` check.
3. Keep pull requests required before merging.

Inspect the existing branch protection rule first and retain all unrelated
settings.
