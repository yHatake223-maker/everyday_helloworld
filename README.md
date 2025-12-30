
````md
# everyday_helloworld

## Overview
This repository is used for daily CI/CD warm-up practice.  
The goal is to continuously exercise the full flow:

**PR → merge → Release (CD)**

Small, safe, repeatable actions every day to build CI/CD muscle memory.

---

## Daily Warm-up Flow（毎日やる手順）

### Goal
PR → merge → Release (CD) を安全に確認する

---

### Steps

#### 1. Create a branch
```bash
git switch main
git pull
git switch -c feature/daily-warmup-YYYYMMDD
````

---

#### 2. Make a tiny change (docs)

* README に 1 行だけ追加
* 内容は何でも OK（例：日付ログ）

例:

```md
CI daily warm-up: YYYY-MM-DD
```

---

#### 3. Commit & push

```bash
git add README.md
git commit -m "docs: daily warm-up (YYYY-MM-DD)"
git push -u origin HEAD
```

---

#### 4. Open PR (GitHub UI)

* base: `main`
* compare: your branch
* CI が **green** になることを確認

---

#### 5. Merge PR (GitHub UI)

* 「Merge pull request」をクリック
* branch は削除して OK

---

#### 6. Pre-tag check（重要）

**タグを打つ前に必ず確認する**
### ✅ Pre-tag checklist (must)

- [ ] 現在のブランチが `main` である
- [ ] `git pull` 済みである
- [ ] `pyproject.toml` の version を確認した
- [ ] 打とうとしている tag が `vX.Y.Z` 形式である
- [ ] version と tag の数値が一致している
- [ ] この tag は **初出**（既存 tag ではない）
- [ ] 同じ tag がすでに存在しないことを確認した（git tag --list 'vX.Y.Z'）

* `main` に入っている version と、打とうとしている tag が一致していること
* Pre-tag check: `git show main:pyproject.toml | grep '^version'` が打とうとしている tag（例: `v0.1.6`）と一致していることを確認


```bash
git show main:pyproject.toml | grep '^version'
```

---

#### 7. Tag & Release

* tag を push すると GitHub Actions が自動で Release を作成する

```bash
git tag vX.Y.Z
git push origin vX.Y.Z
```

---

#### 8. CD check (Release)

GitHub Releases 画面で以下を確認:

* 新しい tag / release が存在する
* Assets に **最新 version の dist だけ**が attach されている
* Release workflow が **green** で完了している

---

## Release Check（トラブル防止）

* 古い version の dist が Assets に残っていない
* tag と pyproject.toml の version が一致している
* 同じ tag の Release が複数存在しない

---

## Daily Log（履歴・任意）

* CI daily warm-up: 2025-12-29
* CI daily warm-up: 2025-12-30

```
CI daily warm-up: 2025-12-30
