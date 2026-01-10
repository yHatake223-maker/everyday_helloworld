# How to Use This Repository as a Template

This repository is a **daily CI/CD warm-up template**.
It is designed to be safe, repeatable, and easy to operate.

## Option A (Recommended): GitHub Template

1. Click **Use this template**
2. Create a new repository
3. Update the repository name and README title if needed
4. Run the first warm-up using the **Quickstart (5 minutes)** section in README

## Option B: Fork (for learning)

Forking keeps the full commit history.
Use this option if you want to learn from the history or contribute back.

## What to customize

- Repository name
- README title (project name)
- Required check name:
  - Keep `pr-ci-test` unless you change the workflow job name
- Secrets:
  - See `docs/policy-secrets.md`

## Recommended daily warm-up rules

- One small change per day (5–15 minutes)
- One PR at a time
- Merge only when CI is green
- Never push directly to `main`
