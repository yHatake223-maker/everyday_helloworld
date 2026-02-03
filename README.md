
# CI/CD daily warm-up template　

## How to use this README

- **First time here?** → Start with **Quickstart (Onboarding)**
- **Daily user?** → Go to **Daily Use**
- **Something feels off?** → Check **Runbooks**

このリポジトリは、**CI/CD を「毎日・自然に回せる状態」にするための GitHub Template** です。  
実装そのものではなく、**運用の型・導線・判断基準**を提供します。

> 📌 This README is a **daily entry point**.
>  
> - Quick actions and links for daily use live here  
> - Detailed procedures and troubleshooting are in `docs/runbooks/`

## Dev Container の表示名について

このテンプレートでは、Dev Container の表示名を  
`.devcontainer/devcontainer.json` の `name` フィールドで明示的に指定しています。

VS Code Dev Containers では、  
**「Use this template」で作成したリポジトリ名や、clone 後のフォルダ名を  
自動的に Dev Container の表示名として使用する仕組みがありません。**

そのため、`name` を指定しない場合、  
すべてのコンテナが同じ表示名（例: `開発コンテナー @ DESKTOP-LINUX`）となり、
複数の Dev Container を同時に使うと区別が困難になります。

#### 表示名を変更したい場合

複数の Dev Container を区別したい場合は、  
`.devcontainer/devcontainer.json` の `name` を任意の名前に変更してください。

```json
{
  "name": "my-project-devcontainer"
}
```


## Daily Use（毎日ここを見る）

- ▶ PR を出す / 迷ったら  
  docs/runbooks/runbook-pr.md

- ▶ コンフリクト対応  
  docs/runbooks/runbook-conflict.md

- ▶ Runbook 一覧  
  docs/runbooks/README.md

- ▶ Dev Container behavior and policies:
  docs/runbooks/template-migration.md

## Template Usage Principles

- This template is maintained with **VS Code + Dev Containers** in mind to reduce setup friction  and make formatting / tooling behavior predictable.

- However, **VS Code is not required**.  
You may use any editor or environment as long as the documented steps are followed.


このテンプレを実プロジェクト（例: `csv-sum-cli`）で利用する際は、  
以下の原則を一貫して適用します。

- **実装PR** は、題材となるプロジェクト側のリポジトリに出す  
  （例: csv-sum-cli の機能追加・テスト追加）
- **導線・運用・仕組みの改善PR** は、このテンプレ（everyday_helloworld）に還元する
- 題材側で「便利機能・仕組み」を思いついたら、まず **テンプレとして一般化できるか？** を考える  
  - Yes → Issue / PR としてこのテンプレに還元する  
  - No（題材固有）→ 題材リポジトリに残す

このリポジトリは、  
**「読むと分かる」ではなく「触ると正解へ導かれる」CI/CD テンプレ**を目指して、  
実運用からのフィードバックによって継続的に改善されます。




## Quickstart (Onboarding)

This section is for first-time users to experience one full PR → CI → merge cycle.
Follow these steps to complete one full PR → CI → merge cycle.

### 1. Create a feature branch
```bash
git switch main
git pull
git switch -c feature/daily-warmup-YYYYMMDD
```

2. Make a tiny change　
Add one line to README.md (append to the end):
CI daily warm-up: YYYY-MM-DD

3. Commit and push
```bash
git add README.md
git commit -m "docs: daily warm-up (YYYY-MM-DD)"
git push -u origin HEAD
```

4. Open a Pull Request
Base branch: main
Compare branch: your feature branch
Confirm that pr-ci-test runs and becomes green

5. Merge
Click Merge pull request
Delete the feature branch after merge

### ✅ Done.
You have completed one full CI warm-up cycle.
This is the daily baseline for this template.

👉 CD（Version bump / Tag / Release）の手順は  
→ [CD Procedure](docs/runbooks/cd-procedure.md) を参照

# Daily Log　

- CI daily warm-up: 2025-12-29
- CI daily warm-up: 2025-12-30
- CI daily warm-up: 2025-12-31
- CI daily warm-up: 2025-12-31 (final)
- CI daily warm-up: 2025-12-31 (year end)
- CI daily warm-up: 2026-01-01
- CI daily warm-up: 2026-01-02
- CI daily warm-up: 2026-01-03
- CI daily warm-up: 2026-01-03_2
- CI daily warm-up: 2026-01-03_3
- CI daily warm-up: 2026-01-04
- CI daily warm-up: 2026-01-05
- CI daily warm-up: 2026-01-06
- CI daily warm-up: 2026-01-07
- Lesson: Write runbooks for recurring failures to avoid decision fatigue.
- CI daily warm-up: 2026-01-08
- CI daily warm-up: 2026-01-09
- CI daily warm-up: 2026-01-10
- CI daily warm-up: 2026-01-11
- CI daily warm-up: 2026-01-12
- CI daily warm-up: 2026-01-13
- CI daily warm-up: 2026-01-14
- CI daily warm-up: 2026-01-15
- CI daily warm-up: 2026-01-16
- CI daily warm-up: 2026-01-17
- CI daily warm-up: 2026-01-18
- CI daily warm-up: 2026-01-19
- CI daily warm-up: 2026-01-20
- CI daily warm-up: 2026-01-21
- CI daily warm-up: 2026-01-21-2
- CI daily warm-up: 2026-01-22
- CI daily warm-up: 2026-01-23
- CI daily warm-up: 2026-01-24
- CI daily warm-up: 2026-01-25
- CI daily warm-up: 2026-01-26
- CI daily warm-up: 2026-01-27
- CI daily warm-up: 2026-01-29
- CI daily warm-up: 2026-01-30
- CI daily warm-up: 2026-01-31
- CI daily warm-up: 2026-02-01
- CI daily warm-up: 2026-02-02