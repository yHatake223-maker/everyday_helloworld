# everyday_helloworld
Creating a development environment from scratch

CI green run trigger.
CI daily warm-up: 2025-12-29

## Daily CI/CD Warm-up (5 minutes)

This repository uses Pull Requests and GitHub Actions for CI/CD.
To avoid forgetting the workflow, run this **5-minute warm-up** at the start of each day.

### Goal

* Create a small change
* Open a Pull Request
* Confirm CI is green
* Merge into `main`
* Confirm CD (Release) runs successfully

---

### Step 1. Create a daily branch

```bash
git switch main
git pull
git switch -c feature/daily-ci-YYYYMMDD
```

---

### Step 2. Make a tiny change

Add **one small line** to `README.md`, for example:

```
Daily warm-up: YYYY-MM-DD
```

---

### Step 3. Commit the change

```bash
git add README.md
git commit -m "docs: daily CI warm-up"
```

---

### Step 4. Push the branch

```bash
git push -u origin HEAD
```

---

### Step 5. Open a Pull Request

* Base branch: `main`
* Compare branch: `feature/daily-ci-YYYYMMDD`
* Title: `docs: daily CI warm-up`

---

### Step 6. Confirm CI

* Ensure **All checks have passed**
* `CI / test (pull_request)` is green

---

### Step 7. Merge the Pull Request

Click **Merge pull request** after CI passes.

---

### Step 8. Confirm CD

* Open the **Actions** tab
* Confirm the **Release** workflow runs successfully
* Verify a new or updated Release is created

---

### Step 9. Cleanup

```bash
git switch main
git pull
git branch -d feature/daily-ci-YYYYMMDD
```

---

✅ Warm-up complete.
Repeat this flow every day to keep CI/CD muscle memory fresh.

Daily warm-up log: 2025-12-29 (b)
