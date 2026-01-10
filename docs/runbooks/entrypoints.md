# Entrypoints Runbook

目的: 「どのコマンドを叩けば何が動くか」を1枚で明確にする

---

## 結論（まずこれだけ覚える）
- 最小の実行確認：`python --version`
- パッケージとして実行（src レイアウト）：`PYTHONPATH=src python -m everyday_helloworld`

---

## どのファイルが何を担当しているか
- `src/everyday_helloworld/__main__.py`
  - `python -m everyday_helloworld` の入口（推奨の最小エントリ）
- `src/main.py`（存在する場合）
  - 単体スクリプトの入口（過渡的・実験用途になりがち）

---

## 推奨ルール（巡航フェーズ）
- “配布テンプレ”としては `__main__.py` を正にする
- `main.py` を使う場合は目的を docs に明記する
- CI の失敗時は `docs/runbooks/ci-failure.md` を参照

---

## 例：Dev Container での確認
```bash
python --version
PYTHONPATH=src python -m everyday_helloworld
