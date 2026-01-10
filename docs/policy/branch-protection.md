# Branch Protection / Ruleset Policy

対象: main ブランチ  
目的: 直push防止・CI保証・安全な巡航運用

---

## 基本方針
- **main への直接 push を禁止**
- 変更は **必ず PR 経由**
- Required check が green でない限り merge しない
- 小さく・戻せる変更を積み重ねる

---

## main ブランチの保護内容

### 1. Push 制御
- main への直接 push: **禁止**
- 管理者であっても原則例外なし

### 2. Pull Request 要件
- PR は常に **1本**
- Draft PR は merge 不可
- Required approvals: **0**
  - ※ CI/CD warm-up のため、レビュー必須にはしない

### 3. Required Status Checks
- Required check: **`pr-ci-test` のみ**
- チェックは **最新 commit に対して成功していること**
- 途中でキャンセルされた run は対象外（最新 run を確認）

### 4. マージ方式
- Squash / Rebase / Merge: 運用に合わせて選択可
- マージ後は main が常に green であること

---

## 運用ルール（巡航フェーズ）
- CI が落ちた場合は `docs/runbooks/ci-failure.md` を参照
- 不明点は **設定を変える前に文章を更新**
- 例外対応が発生した場合は、この policy に理由を追記する

---

## Done の定義
- main に直接 push できない
- PR なしでは変更が入らない
- `pr-ci-test` が green でなければ merge できない
