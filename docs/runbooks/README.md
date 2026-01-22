# Runbooks Index

Find the best runbook for your situation quickly.
## Quick index (by situation)

| Situation | Use this | Why |
|---|---|---|
| PR を作って merge する手順を確認したい | [runbook-pr.md](./runbook-pr.md) | PR の標準手順とチェックリスト |
| conflict が起きた / 解消手順を見たい | [runbook-conflict.md](./runbook-conflict.md) | conflict 解消の手順 |
| CI が落ちた時の調べ方を知りたい | [ci-failure.md](./ci-failure.md) | CI failure の記録と切り分け |
| git config で詰まった | [git-config-troubleshoot.md](./git-config-troubleshoot.md) | git config 系のトラブル対応 |
| 新規リポ / template 初回導入の流れを確認したい | [new-repo-scenario.md](./new-repo-scenario.md) | 初回導入のシナリオ |
| template を公開・配布する手順を確認したい | [publish-template.md](./publish-template.md) | template publish の手順 |
| ruleset / required checks の運用を確認したい | [ruleset-checklist.md](./ruleset-checklist.md) | ruleset のチェック観点 |
| template を既存 repo に移植する | [template-migration.md](./template-migration.md) | migration 手順 |
| template の全体方針を見たい | [template-summary.md](./template-summary.md) | 方針 / P0-P2 のバックログ |
| entrypoints（どこから読むか）を知りたい | [entrypoints.md](./entrypoints.md) | 最初の導線 |

## Rules

- If unsure, start with [runbook-pr.md](./runbook-pr.md).
- If you hit the same confusion twice, write it down and open an issue.

# Runbooks Index

このディレクトリには、CI/CD daily warm-up および
テンプレ運用中に発生しがちな「迷い・トラブル」を解消する runbook を集約しています。

「今なにで困っているか？」から、最短で辿れることを目的としています。

---

## Pull Request / Daily Warm-up

- **runbook-pr.md**  
  PR 作成、CI 確認、merge 手順で迷ったとき  
  daily warm-up の基本導線はこちら

---

## Git / Conflict / Recovery

- **runbook-conflict.md**  
  コンフリクト、誤って main に push した場合など  
  Git 操作のトラブル対応用

---

## CI / Ruleset（運用メモ）

- **runbook-ci.md（予定）**  
  Required checks / Ruleset の ghost 問題など  
  CI が「緑なのに merge できない」時の切り分け

