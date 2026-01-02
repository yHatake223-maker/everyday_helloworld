# everyday_helloworld

## Overview
This repository is used for daily CI/CD warm-up practice.  
The goal is to continuously exercise the full flow:

**PR → merge → Tag → Release (CD)**

Small, safe, repeatable actions every day to build CI/CD muscle memory.

---

## Daily Warm-up Flow（毎日やる手順）

### Goal
PR → merge → **GitHub Actions による Tag & Release** を安全に確認する

> ⚠️ Important  
> **Do NOT create tags locally**  
> Tag creation is handled only by GitHub Actions

---

## Steps

### 1. Create a branch

git switch main
git pull
git switch -c feature/daily-warmup-YYYYMMDD

2. Make a tiny change (docs)

Add exactly one line to README.

Example:
CI daily warm-up: YYYY-MM-DD

3. Commit & push
git add README.md
git commit -m "docs: daily warm-up (YYYY-MM-DD)"
git push -u origin HEAD

4. Open PR (GitHub UI)

base: main

compare: your branch

Confirm CI is green

5. Merge PR (GitHub UI)

Click Merge pull request

Deleting the branch is OK

6. Version bump（required）

Before cutting a tag, always bump the version.
git switch main
git pull
git switch -c feature/bump-version-X.Y.Z
Edit pyproject.toml:
version = "X.Y.Z"
git add pyproject.toml
git commit -m "chore: bump version to X.Y.Z"
git push -u origin HEAD

Open PR → wait for CI → merge

7. Cut tag (GitHub Actions)

This is the only place where tags are created.
GitHub UI steps:

Go to Actions

Select Cut tag on main

Click Run workflow

Input version X.Y.Z (or vX.Y.Z)

Run

The workflow guarantees:

Tag does not already exist

Tag matches pyproject.toml version

Tag is created on main HEAD only

8. Release (GitHub Actions)

Tag creation automatically triggers Release workflow.
No manual operation required.

9. CD check (Release)

Verify on GitHub:

New tag vX.Y.Z exists

Exactly one Release exists

Assets are attached correctly

Release workflow is green

Rules（重要）

❌ Local git tag is forbidden

✅ Tags are created only by GitHub Actions

❌ Version and tag mismatch must fail

❌ Duplicate tags must never be created

Daily Log

CI daily warm-up: 2025-12-29
CI daily warm-up: 2025-12-30
CI daily warm-up: 2025-12-31
CI daily warm-up: 2025-12-31 (final)
CI daily warm-up: 2025-12-31 (year end)
CI daily warm-up: 2026-01-01
CI daily warm-up: 2026-01-02

