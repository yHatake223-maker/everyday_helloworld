
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

7. Cut tag (GitHub Actions)    【KEEP】

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

8. Release (GitHub Actions) 【KEEP】

Tag creation automatically triggers the Release workflow.
No manual operation required.

9. CD check (Release) 【KEEP】

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


