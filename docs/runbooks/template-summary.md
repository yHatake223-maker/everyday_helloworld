# CI/CD Template Summary（巡航フェーズ完成版）

目的：
「壊さない。止めない。毎日回す。」を前提にした  
**PRベース CI/CD テンプレの完成形**を共有・配布可能にする。

---

## 運用の原則（固定）
- **main 直push禁止**
- **PRベース運用（PRは常に1本）**
- Required check は **`pr-ci-test` のみ**
- 変更は小さく、必ず戻せる（revert可能）
- **README は入口、docs/runbooks が手順の正**

---

## CI/CD 設計の要点

### GitHub Actions permissions（Day8）
- workflow ごとに必要最小限を明示
  - CI：`contents: read`
  - tag：`contents: write`
  - workflow dispatch：`actions: write`

### concurrency（Day9 / Day13）
- CI（PR）  
  - 同一PRの古い run は **cancel**
- Tag / Release  
  - **cancel しない**
  - tag：`group: cut-tag`
  - release：`group: release-${{ github.ref }}`

### timeout（Day14）
- CI / tag：10分
- release：15分  
→ ハングによる巡航停止を防止

---

## ドキュメント構成

### docs/README.md（入口）
- Runbooks / Policies / Dev Container への導線

### Runbooks
- CI failure：`docs/runbooks/ci-failure.md`
  - 原因分類＋具体例
- Entrypoints：`docs/runbooks/entrypoints.md`
  - `main.py` と `__main__` の役割整理

### Policies
- Branch protection：`docs/policy/branch-protection.md`
- Tests policy：`docs/policy/tests.md`

---

## Python 構成（Day17）
- `src/` レイアウト前提
- `__pycache__` / `*.egg-info` は `.gitignore` で排除
- テンプレとして差分が汚れない設計

---

## Done（テンプレ完成の定義）
- main に直pushできない
- PRなしで変更が入らない
- `pr-ci-test` が green でないと merge できない
- CI failure は runbook で復旧可能
- Tag / Release が二重実行されても事故らない
- docs が入口として機能する

---

## 利用者向け：最初に読む順番
1. `docs/README.md`
2. `docs/runbooks/ci-failure.md`
3. `docs/runbooks/template-summary.md`
4. `docs/policy/branch-protection.md`
5. `docs/policy/tests.md`
