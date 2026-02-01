## Runbooks
- Template migration: `runbooks/template-migration.md`
- Ruleset checklist: `runbooks/ruleset-checklist.md`
- New repo scenario: `runbooks/new-repo-scenario.md`
- Publish template: `runbooks/publish-template.md`
- [cd-procedure.md](./cd-procedure.md)  
  Version bump → Tag → Release の正式手順



## Policies
- Branch protection / ruleset: `policy/branch-protection.md`
- Tests policy: `policy/tests.md`
- Entrypoints: `runbooks/entrypoints.md`

## Dev Container

このリポジトリは Dev Container（VS Code）で再現可能な開発環境を提供します。

### 前提
- VS Code
- Docker
- 拡張機能: Dev Containers

### 起動手順（最短）
1. リポジトリを開く
2. コマンドパレット → **Dev Containers: Reopen in Container**
3. 初回はビルドが走る（数分）
4. コンテナ内ターミナルが開いたら準備完了

### 動作確認
```bash
python --version



- CI failure: `runbooks/ci-failure.md`（Required check: `pr-ci-test`）


# Docs

This directory contains operational documents for this repository.

## Runbooks

- [Pull Request Runbook](runbook-pr.md)
- [Conflict Resolution Runbook](runbook-conflict.md)

## Purpose

- README.md provides a quick entry point
- Detailed procedures and troubleshooting live here under `docs/`
- Runbooks are written to be followed step by step, without decision making
> Runbooks are step-by-step procedures. Follow them as written, without improvising.
