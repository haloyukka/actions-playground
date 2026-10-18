# Lesson 03: Python の CI

## ゴール
- `actions/checkout` と `actions/setup-python` を使える
- 依存キャッシュで実行を速くできる
- Lint とテストが落ちたら ❌ になる体験をする

## 見本を動かす
`python/` 配下を変更して push（または Actions タブから手動実行）。

見本: [`.github/workflows/l03-python-ci.yml`](../../.github/workflows/l03-python-ci.yml)
対象コード: [`python/src/playground/calc.py`](../../python/src/playground/calc.py)

## ポイント
- ランナーは毎回まっさらなVM。**まず `checkout` しないとコードが無い**
- `defaults.run.working-directory` で `cd python` を毎回書かずに済む
- `ruff check --output-format=github` にすると、PR の差分画面にエラー注釈が付く
- `cache: pip` は2回目以降の実行で効く（ログの「Cache restored」を見てみよう）

## 課題
1. [`exercise.yml`](exercise.yml) を `.github/workflows/my-03.yml` として完成させる
2. **わざと壊す**: ブランチを切って `calc.py` の `add` を `a - b` に変える → PR を作る → ❌ を確認
3. ログからどのテストが落ちたか読み取り、直して ✅ に戻す

## 解答
[`solutions/my-03.yml`](../../solutions/my-03.yml)

## もっと遊ぶ
- `import os` だけ書いて使わない行を足すと ruff が何と言う？
- Settings → Branches でブランチ保護ルールを作り、CI が通らないとマージできないようにする
