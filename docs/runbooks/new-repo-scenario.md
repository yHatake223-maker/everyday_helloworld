# New Repo Scenario（Template を使った新repo立ち上げ）

目的：
このテンプレの CI/CD・docs・運用方針を使って、新しい repo を安全に立ち上げる。

前提：
- GitHub 上で新規 repo を作成できる
- main 直push禁止、PR運用、Required check は `pr-ci-test` のみ

---

## 0. 成功条件（最初に確認）
- 新repoで PR を作ると `pr-ci-test` が走る
- green にならないと merge できない（main 保護が効いている）
- docs/README から runbook / policy に辿れる

---

## 1. 新repoを作る（GitHub）
- リポジトリを作成（Public/Private は用途に合わせる）
- main ブランチを使う（デフォルトでOK）

---

## 2. テンプレを移植する（最短）
この repo の runbook に従って移植する：
- `docs/runbooks/template-migration.md`

推奨：
- まずは **CI と docs のみ**を入れて PR を1本通す
- Tag/Release は後で（運用が増えるため）

---

## 3. 初回 PR（最小で green にする）
例：`docs/README.md` に 1行追加して PR を作る。

確認すること：
- PR の Checks に `pr-ci-test` が出る
- green になる
- merge できる

---

## 4. Branch protection / Ruleset を有効化
確認用チェックリスト：
- `docs/runbooks/ruleset-checklist.md`

必須：
- main 直push禁止
- PR 必須
- Required check は `pr-ci-test` のみ
- approvals は 0（テンプレ運用）

---

## 5. 運用開始（daily warm-up の型）
- 1日1改善、1PR=1論点
- 迷ったら runbook を正にする
  - CI failure：`docs/runbooks/ci-failure.md`
  - ポリシー：`docs/policy/*.md`

---

## 6. トラブル時
- `docs/runbooks/ci-failure.md` を参照
- 直せないときは変更を小さく戻して green を維持

---

## 最短のゴール（Day1 完了）
- PR が通る
- merge できる
- main が常に green
