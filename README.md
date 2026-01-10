## Quickstart (5 minutes)

This repository is a **daily CI/CD warm-up template**.
Follow these steps to complete one full PR → CI → merge cycle.

### 1. Create a feature branch
```bash
git switch main
git pull
git switch -c feature/daily-warmup-YYYYMMDD
2. Make a tiny change

Add one line to README.md (append to the end):
CI daily warm-up: YYYY-MM-DD
3. Commit and push
git add README.md
git commit -m "docs: daily warm-up (YYYY-MM-DD)"
git push -u origin HEAD
4. Open a Pull Request

Base branch: main

Compare branch: your feature branch

Confirm that pr-ci-test runs and becomes green

5. Merge

Click Merge pull request

Delete the feature branch after merge

✅ Done.
You have completed one full CI/CD warm-up cycle.

For troubleshooting and detailed procedures, see:

docs/runbook-pr.md

docs/runbook-conflict.md







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

```bash
git switch main
git pull
git switch -c feature/daily-warmup-YYYYMMDD
```
2. Make a tiny change (docs)

Add exactly one line to README.

Example
```bash
CI daily warm-up: YYYY-MM-DD
```
3. Commit & push
```bash
git add README.md
git commit -m "docs: daily warm-up (YYYY-MM-DD)"
git push -u origin HEAD
```
4. Open PR (GitHub UI)

base: main

compare: your branch

Confirm CI is green

5. Merge PR (GitHub UI)

Click Merge pull request

Deleting the branch is OK

6. Version bump（required）

Before cutting a tag, always bump the version.
```bash
git switch main
git pull
git switch -c feature/bump-version-X.Y.Z
```

Edit pyproject.toml:
version = "X.Y.Z"

Commit & push:
```bash
git add pyproject.toml
git commit -m "chore: bump version to X.Y.Z"
git push -u origin HEAD
```

Open PR → wait for CI → merge

7. Cut tag (GitHub Actions)

This is the only place where tags are created.

GitHub UI steps:

Go to Actions

Select Cut tag on main

Click Run workflow

Input version X.Y.Z or vX.Y.Z

Run

The workflow guarantees:

Tag does not already exist

Tag matches pyproject.toml version

Tag is created on main HEAD only

8. Release (GitHub Actions)

Tag creation automatically triggers the Release workflow.
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


 ## CI / Ruleset 運用メモ（トラブルシューティング）
=======
=======
## CI Failure Log Template

When CI fails, record the following:

- Date:
- PR URL:
- Failed workflow / job:
- Error message (first meaningful line):
- Where I looked first:
- What fixed it (or not fixed yet):
- Lesson (1 line):

Rule:
- Do not retry blindly
- Always identify the first failing job


Troubleshooting memo (2026-01-02)

If multiple rulesets target main, the strictest rules apply.


Keep only one ruleset Active for main.

If a required check stays
Expected — Waiting for status to be reported:

Re-select the required check in the ruleset
(remove → Add checks → select again).

Keep Do not require status checks on creation OFF.

Close and recreate the PR after changing rulesets.

CI / Ruleset 運用メモ（トラブルシューティング）
背景

GitHub の Ruleset は仕様というより実装都合により、
過去に Active だった Ruleset の Required status check が残留する
ことがあります。

その結果、存在しない CI が次のように表示され、PR が merge できなくなる場合があります。

Expected — Waiting for status to be reported

正しい理解（覚えておくべきこと）

Active でない Ruleset は評価されない

ただし、過去に Active だった Ruleset が同じ branch を target していると、
Required check のゴミが残ることがある

運用ルール（超重要）

同じ branch を target する Ruleset は必ず 1 つだけ

使わなくなった Ruleset は Inactive にせず削除する

Required check 名を変更する場合は、必ず次の手順を踏む

Required check 名を変更する正しい手順

Ruleset の Require status checks to pass を一度 OFF

workflow / job 名を変更

Ruleset を再設定（Required check を再追加）

必要であれば PR を作り直す

よくある対処法（詰まったらここを見る）

If a required check stays "Expected — Waiting for status to be reported":

- Re-select the required check in the ruleset (remove → Add checks → select again).
- Keep "Do not require status checks on creation" OFF.
- Close and recreate the PR after changing rulesets.

（ここに日本語補足を残すなら）
補足（日本語）
- Ruleset で Required check を一度削除して再追加

Do not require status checks on creation は OFF のまま

直らない場合は PR を close → 新規作成

CI daily warm-up: Day1 (YYYY-MM-DD)
Goal

Confirm that the required CI check runs exactly once on pull_request.

What I did

Created a feature branch.

Updated README only.

Opened a pull request to main.

What I observed

pr-ci-test ran once.

No ghost / expected checks appeared.

Required check matched the workflow job name.

Result

CI behavior is stable and predictable.

## Troubleshooting memo (2026-01-02)

- If multiple rulesets target `main`, the strictest rules apply.
  - Keep only one ruleset Active for `main`.
- If a required check stays "Expected — Waiting for status to be reported":
  - Re-select the required check in the ruleset (remove → Add checks → select again).
  - Keep "Do not require status checks on creation" OFF.
  - Close and recreate the PR after changing rulesets.


## Runbooks

- docs/runbook-conflict.md
- docs/runbook-pr.md



Daily Log

CI daily warm-up: 2025-12-29
CI daily warm-up: 2025-12-30
CI daily warm-up: 2025-12-31
CI daily warm-up: 2025-12-31 (final)
CI daily warm-up: 2025-12-31 (year end)
CI daily warm-up: 2026-01-01
CI daily warm-up: 2026-01-02
CI daily warm-up: 2026-01-03
CI daily warm-up: 2026-01-03_2
CI daily warm-up: 2026-01-03_3
CI daily warm-up: 2026-01-04
CI daily warm-up: 2026-01-05
CI daily warm-up: 2026-01-06
CI daily warm-up: 2026-01-07
Lesson: Write runbooks for recurring failures to avoid decision fatigue.
CI daily warm-up: 2026-01-08
CI daily warm-up: 2026-01-09
CI daily warm-up: 2026-01-10