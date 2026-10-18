# Lesson 08: Issue / PR の自動操作

## ゴール
- `issues` / `issue_comment` / `pull_request_target` イベントを使える
- `actions/github-script` で GitHub API を JavaScript から叩ける
- `actions/labeler` で変更ファイルに応じて PR にラベルを付けられる

## 見本を動かす
- **Issue を作る** → `triage` ラベルとあいさつコメントが自動で付く（タイトルに「バグ」を含めると `bug` も）
- **PR を作る** → 変更したフォルダに応じて `python` / `node` / `workflow` / `docs` ラベルが付く

見本: [`.github/workflows/l08-issue-automation.yml`](../../.github/workflows/l08-issue-automation.yml)
ラベル設定: [`.github/labeler.yml`](../../.github/labeler.yml)

## ポイント
- `github-script` の中では `github`（APIクライアント）と `context`（イベント情報）がすぐ使える
- `context.repo` は `{ owner, repo }`。スプレッド構文 `...context.repo` で渡すのが定番
- 存在しないラベルを付けると自動で作られる
- `pull_request_target` は **ベースブランチ側の権限** で動くので、フォークのPRにもラベルを付けられる。ただし **PRのコードを checkout して実行してはいけない**（悪意あるコードに書き込み権限を渡すことになる）

## 課題
[`exercise.yml`](exercise.yml) を `.github/workflows/my-08.yml` として完成させる。

- Issue に `/hello` とコメントすると、bot が 👋 リアクションを付けて「こんにちは、◯◯さん！」と返信する
- コメントが PR 上のものでも Issue 上のものでも動いてOK
- bot 自身のコメントには反応しない

## 解答
[`solutions/my-08.yml`](../../solutions/my-08.yml)

## もっと遊ぶ
- `/close` で Issue を閉じるコマンドを作る（`github.rest.issues.update` で `state: "closed"`）
- 7日間動きのない Issue に印を付ける（`actions/stale`）
