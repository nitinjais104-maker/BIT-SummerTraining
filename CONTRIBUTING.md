# How to Submit an Assignment

Follow this process for every assignment. Create one branch and one Pull Request for one assignment day only.

## 1. Clone the Repository

```bash
git clone https://github.com/z-pandeyji/BIT-SummerTraining.git
cd BIT-SummerTraining
```

## 2. Start From the Latest Main Branch

Always start a new assignment from the latest teacher repository branch.

First, check your remotes:

```bash
git remote -v
```

If `origin` points to your own GitHub fork, add the teacher repository as `upstream`. You only need to add it once:

```bash
git remote add upstream https://github.com/z-pandeyji/BIT-SummerTraining.git
```

Download the latest teacher repository changes and create your new branch from `upstream/main`:

```bash
git fetch upstream
git switch -c day-12-your-name upstream/main
```

If you cloned the teacher repository directly and `origin` already points to `z-pandeyji/BIT-SummerTraining`, use:

```bash
git checkout main
git pull origin main
git switch -c day-12-your-name
```

Example:

```bash
git switch -c day-12-rahul
```

Do not create a Day 12 branch from your Day 11 branch. That can cause old files to appear in the new Pull Request.

## 3. Create Only Your Submission Files

Use the submission helper from the repository root. It creates the correct
folder and `solution.py` without overwriting existing work:

```bash
python3 scripts/create_submission.py --day 6 --batch a --name your-name
```

Change the day, batch, and name to match your assignment. Use the same student
folder spelling you used for earlier assignments. Names cannot contain spaces;
use `rahul-singh` or `rahul_singh` instead.

The command creates:

```txt
assignments/day-06/submissions/batch-a/your-name/solution.py
```

For Batch B, use `--batch b`:

```txt
assignments/day-06/submissions/batch-b/your-name/solution.py
```

Example:

```txt
assignments/day-06/submissions/batch-a/rahul/solution.py
```

Most assignments need only `solution.py`. If an assignment specifically asks for a data file, such as Day 7, keep that file inside your own folder too:

```txt
assignments/day-07/submissions/batch-a/rahul/solution.py
assignments/day-07/submissions/batch-a/rahul/sales_data.csv
```

The helper prints every additional required filename:

- Day 7 requires `sales_data.csv`.
- Day 10 requires the five chart images listed in `assignments/day-10/questions.md`.
- Day 11 requires the six chart images listed in `assignments/day-11/questions.md`.

Do not rename `solution.py`, add a space before `.py`, or place the file
directly inside `batch-a` or `batch-b`.

## 4. Run Your Program

Run the file before committing it:

```bash
python3 assignments/day-06/submissions/batch-a/your-name/solution.py
```

Check that every required question runs and that printed values match the expected output in `questions.md`.

## 5. Stage Only Your Files

Do not use `git add .`. Stage only your own submission files.

```bash
git add assignments/day-06/submissions/batch-a/your-name/solution.py
git commit -m "Add Day 6 assignment by Your Name"
git push origin day-06-your-name
```

For Day 7, stage both files:

```bash
git add assignments/day-07/submissions/batch-a/your-name/solution.py
git add assignments/day-07/submissions/batch-a/your-name/sales_data.csv
git commit -m "Add Day 7 assignment by Your Name"
git push origin day-07-your-name
```

## 6. Create the Pull Request

On GitHub, create a Pull Request from your branch to `main`.

Use this title format:

```txt
Day 6 Assignment - Rahul
```

## Before You Create the Pull Request

Run this command:

```bash
git status --short
```

The output should show only files inside your own submission folder for one assignment day.

GitHub automatically runs the `assignment-structure` check after the Pull
Request is created. The check must pass before the assignment can be merged.
If it fails, open the check details: the message lists the missing, unexpected,
or incorrectly located files.

Do not include:

- Another student's folder or solution file.
- Files from an earlier or later assignment day.
- `README.md`, `CONTRIBUTING.md`, `.gitignore`, or `questions.md`.
- `resources/`, generated files, temporary files, or editor backup files.
- Assignment files from more than one day, even when they belong to you.

## If Your Pull Request Contains Wrong Files

Create a clean branch instead of adding more files to the old branch:

```bash
git checkout main
git pull origin main
git checkout -b day-06-your-name-clean
```

Copy only your correct `solution.py` into the required folder, commit it, push it, and create a new Pull Request.

## Troubleshooting Git Problems

Before trying a fix, run these commands:

```bash
git status
git branch --show-current
git remote -v
git log --oneline -5
```

Read the matching problem below. Do not randomly delete files or run `git reset --hard`.

### The Push Succeeded—What Do I Do Next?

Messages such as these mean the push worked:

```text
[new branch] day-05-your-name -> day-05-your-name
Create a pull request for 'day-05-your-name' on GitHub by visiting:
```

Open the Pull Request link printed in the terminal. On GitHub:

1. Set the base repository to `z-pandeyji/BIT-SummerTraining`.
2. Set the base branch to `main`.
3. Set the compare branch to your assignment branch.
4. Open the **Files changed** tab.
5. Confirm that it contains only your files for one assignment.
6. Create the Pull Request.

The screenshot may look like a problem because Git prints a lot of text, but a completed push without an `error` or `rejected` message is successful.

### `src refspec ... does not match any`

This usually means the branch name in the push command does not match your current branch, or you have not created a commit.

Check the branch and commits:

```bash
git branch --show-current
git log --oneline -1
```

Push the current branch without retyping its name:

```bash
git push -u origin HEAD
```

If Git reports that you have no commits, stage and commit your assignment first:

```bash
git add assignments/day-12/submissions/batch-a/your-name/solution.py
git commit -m "Add Day 12 assignment by Your Name"
git push -u origin HEAD
```

Change the day, batch, and name to match your assignment.

### Push Rejected or `non-fast-forward`

First check whether you are pushing a new assignment branch or directly pushing `main`.

```bash
git branch --show-current
```

Students should push their own assignment branch:

```bash
git push -u origin HEAD
```

Do not use `--force` to fix a rejected push. If the same branch already exists on your fork and contains different work, create a clearly named clean branch from the latest teacher code and submit that branch instead.

### Old or Unrelated Files Appear in the Pull Request

This usually happens when a new assignment branch was created from an older assignment branch instead of from the latest `main`.

Keep the old branch as a backup, then create a clean branch:

```bash
git branch day-12-your-name-backup
git fetch upstream
git switch -c day-12-your-name-clean upstream/main
```

Copy only your intended assignment file from the old branch:

```bash
git checkout day-12-your-name-backup -- assignments/day-12/submissions/batch-a/your-name/solution.py
```

Check, commit, and push:

```bash
git status --short
git add assignments/day-12/submissions/batch-a/your-name/solution.py
git commit -m "Add Day 12 assignment by Your Name"
git push -u origin day-12-your-name-clean
```

Create a new Pull Request from the clean branch and close the incorrect Pull Request.

If `upstream` does not exist, add it first:

```bash
git remote add upstream https://github.com/z-pandeyji/BIT-SummerTraining.git
git fetch upstream
```

### Git Says `nothing to commit`

Run:

```bash
git status
```

Possible meanings:

- the file was not saved in the editor;
- you edited a different copy of the repository;
- the change was already committed;
- you created the file outside the repository folder.

Confirm your terminal is inside `BIT-SummerTraining`, save the file, and run `git status` again.

### The File Is Listed Under `Untracked files`

The file exists, but Git is not tracking it yet. Stage the exact assignment file:

```bash
git add assignments/day-12/submissions/batch-a/your-name/solution.py
git status
```

The file should now appear under `Changes to be committed`. Then commit and push it.

### Changes Do Not Appear on GitHub

Check whether you committed and pushed the same branch:

```bash
git status
git branch --show-current
git log --oneline -3
```

If the commit appears locally, push the current branch:

```bash
git push -u origin HEAD
```

Then select that same branch when creating the Pull Request.

### Merge Conflict After Pulling

Run:

```bash
git status
```

Git lists every conflicted file. Open each file and look for the three conflict-marker lines:

- a line beginning with seven `<` characters;
- a divider line containing seven `=` characters;
- a line beginning with seven `>` characters.

Keep the correct content and remove all three marker lines. Then run:

```bash
git add path/to/resolved-file
git commit -m "Resolve merge conflict"
```

If another student's submission is conflicted or you are unsure which content is correct, stop and ask the instructor before committing.

### `origin` and `upstream` Are Confusing

Run:

```bash
git remote -v
```

For a fork-based workflow:

- `origin` should normally be your GitHub fork;
- `upstream` should be `https://github.com/z-pandeyji/BIT-SummerTraining.git`.

Use `upstream/main` as the starting point for a new assignment branch, then push your branch to `origin`.

### I Accidentally Worked on `main`

If you have not committed yet, create your assignment branch now:

```bash
git switch -c day-12-your-name
```

Your unsaved and uncommitted changes move with you. Stage, commit, and push them from the new branch.

If you already committed on `main`, do not push `main`. Create a branch pointing to that commit:

```bash
git switch -c day-12-your-name
git push -u origin HEAD
```

Then create the Pull Request from the new branch.

## How to Ask for Git Help

Send:

1. the exact command you entered;
2. the complete error message—not only the last line;
3. what you expected to happen;
4. a screenshot or copied output from:

```bash
git status
git branch --show-current
git remote -v
git log --oneline -5
```

Also include the assignment day, your batch, and your branch name.

Never share:

- a GitHub password;
- a personal access token;
- an SSH private key;
- the contents of a `.env` file;
- any other secret.
