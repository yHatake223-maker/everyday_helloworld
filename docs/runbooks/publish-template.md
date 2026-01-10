# Publish as Template Repo（配布用テンプレとして公開・運用）

目的：
このリポジトリを “テンプレ” として配布できる状態にし、利用者が安全に使い始められるようにする。

---

## 0. 成功条件（Done）
- GitHub 上で **「Use this template」**が使える（Template repo 有効）
- 新repo作成後に PR を作ると **`pr-ci-test` が走る**
- main 直push禁止・PR必須・Required check = `pr-ci-test` の運用が成立
- docs/README から runbook / policy に辿れる

---

## 1. 公開形態を決める
- Public：社外/コミュニティ配布向け
- Private：社内限定・個人利用向け

推奨：
- “配布テンプレ”は **Public**（ただし機密が無いこと）
- 社内限定なら Private でOK（利用者を招待）

---

## 2. Template repo を有効化する（状態）
- リポジトリが **Template として有効**になっていること
- 利用者が **テンプレから新repoを作成**できること

確認：
- GitHub 画面で「Use this template」が表示される

---

## 3. README / docs の入口を整える（最小）
必須：
- `docs/README.md` が入口として機能
- 以下に導線がある
  - Runbooks（CI failure / migration / ruleset checklist / new repo scenario）
  - Policies（branch protection / tests）

推奨：
- `docs/runbooks/template-summary.md` を読めば全体像が分かる

---

## 4. “移植後に必ずやること”を明記する
テンプレから repo を作った直後は、次を必ず行う：

- Branch protection / Ruleset を設定する
  - チェックリスト：`docs/runbooks/ruleset-checklist.md`

最小要件：
- main 直push禁止
- PR必須
- Required check は `pr-ci-test` のみ
- approvals = 0（warm-up前提）

---

## 5. 初回検証（テンプレ利用者が必ず行う）
1. テンプレから新repo作成
2. README を 1行変更して PR を作る
3. `pr-ci-test` が走ることを確認
4. green → merge（main が green）

---

## 6. よくある落とし穴
- Required check 名が repo によって変わる
  - 対策：CI job 名は `pr-ci-test` を維持する
- Branch protection を忘れて直pushしてしまう
  - 対策：チェックリストで “必須” を先に確認
- docs がコピーされていない
  - 対策：`docs/README.md` を入口として必ず含める

---

## 7. 運用（テンプレ本体側）
- 1日1改善、1PR=1論点
- 変更前に “配布テンプレとして後方互換か？” を確認
- 例外を入れたら docs に理由を書く

---

## 参照
- Template summary：`docs/runbooks/template-summary.md`
- Migration：`docs/runbooks/template-migration.md`
- Ruleset checklist：`docs/runbooks/ruleset-checklist.md`
- New repo scenario：`docs/runbooks/new-repo-scenario.md`
