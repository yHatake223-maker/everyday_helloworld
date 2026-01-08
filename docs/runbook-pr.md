# Pull Request Runbook

This document describes the **standard procedure** for creating
and merging a pull request during daily CI/CD warm-up.

This is a **runbook**, not a design guide.  
Follow the steps in order. Do not skip checks.

---

## When to use this runbook

- Creating a pull request for daily warm-up
- Unsure whether the branch is ready for PR
- PR shows no diff or unexpected status

---

## Pre-flight checks (before opening PR)

Run these commands **every time** before opening a PR.

### 1. Confirm current branch
```bash
git branch --show-current

Expected:
feature/daily-warmup-YYYYMMDD

2. Check working tree status
git status

OK states:

nothing to commit, working tree clean

or Changes to be committed

3. Confirm latest commit
git log --oneline -1

The latest commit must be today's warm-up

Standard PR creation steps
1. Push the feature branch
git push -u origin HEAD

Open the PR link shown in the output

Base branch: main

Compare branch: current feature branch

PR checklist

pr-ci-test runs exactly once

No unexpected required checks

Diff matches today's intended change only

Merge procedure

Wait for CI to become green

Merge via GitHub UI

Delete the feature branch after merge

If something looks wrong

Do NOT merge in a hurry

Re-check:

branch name

git status

latest commit

If necessary:

Close the PR

Fix locally

Push again

Expected result

PR is merged cleanly

main is updated via PR only

Daily warm-up completes without confusion