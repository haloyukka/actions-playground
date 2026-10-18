# Lesson 09: ジョブの連携

## ゴール
- `needs` でジョブの順番と依存関係を作れる
- ジョブ間で **値** は `outputs`、**ファイル** は artifact で受け渡せる
- `if: always()` / `failure()` / `needs.<job>.result` で失敗時の動きを決められる

## 見本を動かす
Actions タブ → **L09 Job Pipeline** → Run workflow。
`make_it_fail` にチェックを入れると test が落ち、それでも report が動く様子が見られます。

見本: [`.github/workflows/l09-jobs.yml`](../../.github/workflows/l09-jobs.yml)

## ポイント
- ジョブは **別々のマシン** で動く。ファイルは共有されないので artifact で渡す
- 実行ページの上部に **依存関係のグラフ** が出る
- ステータス関数

| 関数 | 実行される条件 |
| --- | --- |
| （なし）= `success()` | 前が全部成功 |
| `failure()` | 前のどれかが失敗 |
| `always()` | 何があっても |
| `cancelled()` | キャンセルされた |

- `::warning::` / `::error::` / `::notice::` はログに注釈を出すコマンド

## 課題
[`exercise.yml`](exercise.yml) を `.github/workflows/my-09.yml` として完成させる。

```
generate ──▶ count ──▶ notify (失敗時のみ)
```

- `generate`: 1〜100 のランダムな行数のテキストを作り artifact に
- `count`: artifact を受け取って行数を数え、ジョブ出力 `lines` にする。50行より多ければ失敗させる
- `notify`: `count` が失敗したときだけ動き、`::error::` で知らせる

## 解答
[`solutions/my-09.yml`](../../solutions/my-09.yml)

## もっと遊ぶ
- `timeout-minutes: 1` を付けて、`sleep 90` するステップがどうなるか見る
- Actions タブ右上の **Re-run failed jobs** を試す
