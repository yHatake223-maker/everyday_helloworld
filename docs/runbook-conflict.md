# Conflict Runbook

This document describes the **standard procedure** to resolve Git conflicts
during daily CI/CD warm-up.

This is a **runbook**, not a design document.  
Follow the steps as written. Do not improvise.

---

## When to use this runbook

- Pull request shows **"This branch has conflicts"**
- `git merge origin/main` fails
- Conflict markers like `<<<<<<< HEAD` appear

---

## Basic policy (no thinking required)

- `main` branch is always the source of truth
- Resolve conflicts **on the feature branch**
- Never push directly to `main`

---

## Standard resolution steps (CLI)

```bash
# 1. Update remote information
git fetch origin

# 2. Merge main into the current feature branch
git merge origin/main

# 3. Resolve conflicts in files
# - Remove conflict markers
# - Keep the intended final content

# 4. Stage resolved files
git add .

# 5. Commit the resolution
git commit -m "chore: resolve merge conflict"

# 6. Push updated branch
git push
```

If conflict resolution becomes messy
Close the pull request

Create a new feature branch from main

Re-apply the intended changes

Open a new pull request

Things you must NOT do
Do NOT push directly to main

Do NOT leave conflict markers in files

Do NOT retry blindly without checking the first failing file

Expected result
Pull request no longer shows conflicts

CI runs automatically

pr-ci-test becomes green