# CI/CD Template Migration Runbook（他repoへ展開）

目的：
このリポジトリの CI/CD テンプレ（巡航フェーズ完成版）を、別リポジトリへ安全に移植する。

前提：
- 移植先 repo でも **PRベース運用**を前提とする
- Required check は **`pr-ci-test` 1本**で運用する
- 変更は小さく、必ず戻せる（revert可能）

---

## 0. 最短の全体手順（チェックリスト）
1. [ ] workflow をコピー
2. [ ] docs をコピー（runbooks / policy）
3. [ ] `.gitignore` を確認
4. [ ] Branch protection / ruleset を設定
5. [ ] 初回 PR で `pr-ci-test` が green になることを確認
6. [ ] Tag/Release を使う場合のみ、手動で動作確認

---

## 1. コピーするもの（推奨セット）

### GitHub Actions（必須）
- `.github/workflows/ci.yml`
- `.github/workflows/cut_tag.yml`（Tag運用する場合）
- `.github/workflows/release.yml`（Release運用する場合）

移植ポリシー：
- permissions / concurrency / timeout は **そのまま移植**
- Required check 名は **`pr-ci-test` を維持**（移植先のブランチ保護設定が簡単になる）

### docs（必須）
- `docs/README.md`
- `docs/runbooks/ci-failure.md`
- `docs/runbooks/template-summary.md`
- `docs/runbooks/entrypoints.md`
- `docs/policy/branch-protection.md`
- `docs/policy/tests.md`

### 付随ファイル（推奨）
- `.gitignore`（少なくとも `__pycache__/`, `*.egg-info/`, `.venv/` を含む）

---

## 2. 移植先 repo ごとに見直すポイント（最小）

### CI コマンド（最重要）
- `ci.yml` のテスト実行コマンドは移植先に合わせて調整する  
  例：`python -m pytest` / `python -m unittest` / `make test`

> まずは「何もしない」より「最小で通る」ことを優先（巡航の原則）

### Python バージョン
- workflow や devcontainer で固定している場合は、移植先の方針に合わせる

### Tag / Release の有無
- 使わないなら workflow ごと移植しない（運用が増えるだけ）

---

## 3. Branch protection / Ruleset 設定（移植先で必ずやる）
- main 直push禁止
- PR必須
- Required check：`pr-ci-test` のみ
- Required approvals：0（CI/CD warm-up の前提）

Done：
- main に直pushできない
- `pr-ci-test` が green でないと merge できない

---

## 4. 初回検証（移植後の確認手順）
1. 移植先 repo で小さな変更（README 1行）を入れて PR 作成
2. `pr-ci-test` が走ることを確認
3. green を確認して merge
4. docs の導線（docs/README）から runbook が辿れることを確認

---

## 5. 失敗したとき
- まず `docs/runbooks/ci-failure.md` を参照
- ログの「最初のエラー行」＋「失敗した step」をメモ
- 直らない場合は、移植差分を最小に戻して段階導入する
