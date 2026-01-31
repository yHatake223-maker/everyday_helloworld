# CD Procedure (Version bump → Tag → Release)

This runbook describes the **safe and repeatable CD flow**  
after completing one CI warm-up cycle.

---

## Start here (最短導線)

Before starting CD:

- CI warm-up PR is already merged
- You are on `main`
- Working tree is clean

```bash
git switch main
git pull
git status
```
## 1. Version bump (required)

- Before cutting a tag, always bump the version.
```bash
git switch -c feature/bump-version-X.Y.Z
```
Edit `pyproject.toml`:

```toml
version = "X.Y.Z"
```

Commit & push:
```bash
git add pyproject.toml
git commit -m "chore: bump version to X.Y.Z"
git push -u origin HEAD
```

### Done when
- Version bump PR is merged
- `main` contains the new version


## 2. Cut tag (GitHub Actions)

⚠️ This is the only place where tags are created.

### GitHub UI steps
- Go to Actions
- Select **Cut tag on main**
- Click **Run workflow**
- Input `X.Y.Z` or `vX.Y.Z`
- Click **Run**


### The workflow guarantees
- Tag does not already exist
- Tag matches `pyproject.toml` version
- Tag is created on `main` HEAD only


- Tag is created on main HEAD only

### Done when
- New tag vX.Y.Z exists on main

## 3. Release (GitHub Actions)

Tag creation automatically triggers the Release workflow.
No manual operation required.

### Done when
- Exactly one Release exists for the tag
- Assets are attached correctly
- Release workflow is green


## If something fails

### Version / tag mismatch
- Fix `pyproject.toml`
- Open a new version bump PR
- Merge → retry tag workflow

### Tag already exists
- Do **not** reuse the tag
- Bump version again (`X.Y.(Z+1)`)


### Rules (重要)

- ❌ Local git tag is forbidden
- ✅ Tags are created only by GitHub Actions
- ❌ Version and tag mismatch must fail
- ❌ Duplicate tags must never be created