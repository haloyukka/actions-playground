# Lesson 05: matrix で並列実行

## ゴール
- `strategy.matrix` で「OS × バージョン」の組み合わせを一気に回せる
- `include` / `exclude` / `fail-fast` / `continue-on-error` を使い分けられる

## 見本を動かす
Actions タブ → **L05 Matrix** → Run workflow。
Python 4本（Ubuntu×3 + Windows×1）と Node 3本が **並列** で走ります。

見本: [`.github/workflows/l05-matrix.yml`](../../.github/workflows/l05-matrix.yml)

## ポイント
| キー | 役割 |
| --- | --- |
| `matrix.<key>: [...]` | 値の配列。複数キーは **掛け算** の組み合わせになる |
| `exclude` | 掛け算から特定の組み合わせを除く |
| `include` | 組み合わせを足す／特定の組み合わせに値を追加する |
| `fail-fast: false` | 1本落ちても残りを止めない（既定は true で全部止まる） |
| `continue-on-error` | そのジョブが落ちても全体は ✅ 扱い |
| `name: ... ${{ matrix.x }}` | ジョブ名に値を入れると一覧が見やすい |

> 💡 Public リポジトリは標準ランナーの実行時間が無料。matrix をたくさん回しても大丈夫です。

## 課題
[`exercise.yml`](exercise.yml) を `.github/workflows/my-05.yml` として完成させる。

- Python 3.12 / 3.13 × Node 20 / 22 の **4通り** を1つのジョブ定義で回す
- 各ジョブで両方のバージョンを表示し、Python と Node 両方のテストを実行
- Python 3.12 × Node 20 の組み合わせだけ除外（= 3通り）

## 解答
[`solutions/my-05.yml`](../../solutions/my-05.yml)

## もっと遊ぶ
- `max-parallel: 1` にすると何が起きる？
- `os` に `macos-latest` を足してみる
