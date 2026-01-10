# GitHub Ruleset / Branch Protection Checklist

目的：
GitHub UI の変更に依存せず、**満たすべき状態**で設定の正否を確認できるようにする。

---

## 必須チェック（テンプレ要件）

- [ ] main ブランチに **直接 push できない**
  - 確認方法：`git push origin main` が拒否される

- [ ] **PR なし**では main に変更を入れられない
  - 確認方法：PR を作らない変更が拒否される

- [ ] Required status check が **`pr-ci-test` のみ**
  - 確認方法：PR の **Checks** タブを確認

- [ ] Required approvals が **0**
  - 確認方法：レビュー無しでも merge 可能（CI green 前提）

- [ ] CI が **red の状態では merge できない**
  - 確認方法：CI failure の PR がブロックされる

---

## 推奨チェック（巡航フェーズ）

- [ ] PR の CI は **最新 run のみが有効**
  - 確認方法：同一PRで再pushすると古い run が cancelled になる

- [ ] Tag / Release は **キャンセルされず直列実行**
  - 確認方法：同時起動で queued / waiting になる

- [ ] workflow に **timeout** が設定されている
  - 確認方法：`.github/workflows/*.yml` に `timeout-minutes` がある

- [ ] workflow の **permissions が最小化**されている
  - 確認方法：各 workflow に `permissions:` が明示されている

---

## 例外対応ルール
- 例外を設けた場合は **理由と期限**を docs に追記する
- 一時対応が恒久化しないよう、必ず見直す

---

## Done の定義
- 上記の **必須チェックがすべて Yes**
- 推奨チェックに **明確な理由**がある
