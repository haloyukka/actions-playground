# Lesson 02: トリガーとフィルター

## ゴール
- `push` / `pull_request` / `workflow_dispatch` の違いがわかる
- `branches` / `paths` で「関係ある変更のときだけ」動かせる
- `if:` でイベントごとに処理を切り替えられる

## 見本を動かす
- **push で起動**: `practice/` 内のファイルを編集して main に push
- **PR で起動**: ブランチを切って `practice/` を変更 → PR を作る
- **手動で起動**: Actions タブから level / dry_run を選んで実行

見本: [`.github/workflows/l02-triggers.yml`](../../.github/workflows/l02-triggers.yml)

## ポイント
- `paths` を付けないと、README を直しただけでも全部のワークフローが動いてしまう
- `paths-ignore` で逆指定もできる（`paths` と同時には使えない）
- 手動実行の入力は `inputs.<名前>`。`type: choice` / `boolean` / `string` / `number` など
- 🔐 **PRタイトルやコミットメッセージは外部入力**。`run:` に `${{ }}` で直接埋め込むとコマンドを注入される恐れがあるので、見本のように `env:` 経由で渡す

## 課題
[`exercise.yml`](exercise.yml) を `.github/workflows/my-02.yml` として完成させる。

- `practice/*.txt` が変わった push と、手動実行で動く
- 手動実行の入力 `mood`（`happy` / `sleepy` の選択式）
- `mood` が `sleepy` のときだけ「☕ コーヒーを淹れよう」と表示

確認: `practice/hello.txt` を作って push → 動く。`practice/README.md` だけ変えたら → 動かない。

## 解答
[`solutions/my-02.yml`](../../solutions/my-02.yml)

## もっと遊ぶ
- `on.push.tags: ["v*"]` にして `git tag v0.1 && git push --tags` してみる
- `issues` や `release` など、ほかのイベントは [Events that trigger workflows](https://docs.github.com/actions/reference/events-that-trigger-workflows) に一覧があります
