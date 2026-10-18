# Lesson 01: はじめてのワークフロー

## ゴール
- ワークフロー / ジョブ / ステップ の関係がわかる
- `${{ }}` 式でコンテキスト（`github.*` など）を読める
- ステップ間で値を受け渡し、実行結果ページにサマリーを書ける

## 見本を動かす
1. GitHub の **Actions** タブ → 左の **L01 Hello Actions**
2. **Run workflow** → name を入れて実行
3. 実行ログと、実行ページ下部の Summary を確認

見本: [`.github/workflows/l01-hello.yml`](../../.github/workflows/l01-hello.yml)

## ポイント
| 要素 | 意味 |
| --- | --- |
| `on:` | いつ動くか（トリガー）。`workflow_dispatch` は手動実行ボタン |
| `jobs.<id>.runs-on` | どのマシン（ランナー）で動くか |
| `steps[].run` | シェルコマンド。`|` で複数行 |
| `steps[].uses` | 他人が作った Action を使う（Lesson 03〜） |
| `$GITHUB_OUTPUT` | ステップの出力。`steps.<id>.outputs.<name>` で読める |
| `$GITHUB_STEP_SUMMARY` | Markdown を書くと実行ページに表示される |

> 💡 `${{ }}` は **GitHub側でYAMLを展開** してからシェルに渡ります。`$VAR` は **シェルの環境変数**。似ているけど別物です。

## 課題
[`exercise.yml`](exercise.yml) の `TODO` を埋めて、`.github/workflows/my-01.yml` としてコミットしてください。

- 手動実行で動く
- 実行した人（actor）と曜日を表示する
- Summary に「今日の一言」を書く

```bash
cp lessons/01-hello/exercise.yml .github/workflows/my-01.yml
# TODO を埋めて
git add . && git commit -m "lesson01" && git push
```

GitHub のWeb画面で直接ファイルを作っても OK です。

## 解答
[`solutions/my-01.yml`](../../solutions/my-01.yml)

## もっと遊ぶ
- `runs-on: windows-latest` にすると何が変わる？（`run` の既定シェルが PowerShell になる）
- `echo "::notice::メモ"` を書くとどう表示される？
