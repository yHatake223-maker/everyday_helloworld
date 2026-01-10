# CI Failure Runbook (pr-ci-test)

対象: GitHub Actions の Required check `pr-ci-test` が失敗したとき  
目的: 「原因特定 → 最小修正 → 再実行 → green → merge」までを最短で通す

---

## 0. 原則
- まず **ログを読む**（推測で直さない）
- 修正は **最小**、1PR=1論点
- 直せない/再現できない場合は **止めずに切り分け**（情報を増やすPRを出す）

---

## 1. 最初に確認する（GitHub UI）
1. PR を開く
2. Checks → `pr-ci-test` を開く
3. 失敗した **step の直前から**ログを読む  
   - エラーの先頭行
   - stacktrace の最初の例外
   - “permission denied / command not found / no such file” 等のキーワード

---

## 2. まず分類する（よくある原因）
### A. テスト失敗（assert / exit code 1）
- 変更内容とテストの意図が一致しているか確認
- 期待値の更新が必要か、実装が不足しているかを判断

### B. 依存関係/環境（pip / python / import error）
- requirements / pyproject / python-version の変更有無
- ロックファイルやキャッシュ由来の可能性
- ローカルで再現 → 依存追加/修正を最小で

### C. フォーマット/静的解析（lint / type）
- ルールの自動修正があるなら先に適用
- 変更箇所だけ直す（全体整形は別PR）

### D. GitHub Actions/Workflow設定（yml / permissions / concurrency）
- 最近触った workflow を疑う
- `permissions` 不足のときはログに権限エラーが出る
- concurrency でキャンセルされた場合は「最新run」を見る

---

## 3. ローカル再現（できる範囲で）
- 手元で同等のコマンドがある場合はそれを実行
- ない場合は「失敗ログのコマンド」をコピペして実行

メモ:
- 再現できない場合でも、ログの情報量を増やす変更（echo / version表示）で切り分けする

---

## 4. 修正方針（最小修正の型）
- 原因が1つなら: その1点だけ直す
- 原因が不明なら: 情報を増やす（バージョン表示、ファイル存在確認）  
  ※デバッグ出力を増やすだけのPRはOK（止めないため）

---

## 5. 再実行の作法
- 直したら push → 新しい run が走る（concurrencyで古いrunはキャンセルされる）
- 直前の run を見ず、**最新run** を見る
- 失敗が同じならログの行番号/メッセージを比較して進展を確認

---

## 6. それでも直らないとき
- 失敗ログの「最初のエラー行」＋「直前のコマンド」＋「環境情報（Python/OS）」をメモ
- いったん PR を小さく戻して（revertまたは修正取り下げ）、CI を green に戻す
- 別PRで原因切り分けを続ける

---

## Doneの定義
- `pr-ci-test` が green
- 失敗原因と対処がこのrunbookに追記されている（1〜2行でOK）
