# Lesson 06: 定期実行と自動コミット

## ゴール
- `schedule` の cron を書ける（**UTC** に注意）
- `permissions` で GITHUB_TOKEN に書き込み権限を与えられる
- 変更があるときだけ bot としてコミット＆push できる

## 見本を動かす
- 毎日 **09:17 JST** に自動実行され、[`data/STATUS.md`](../../data/STATUS.md) を更新します
- 待てないときは Actions タブ → **L06 Scheduled Update** → Run workflow
- 実行後、コミット履歴に `github-actions[bot]` のコミットが増えます

見本: [`.github/workflows/l06-scheduled-update.yml`](../../.github/workflows/l06-scheduled-update.yml)
スクリプト: [`scripts/update_status.py`](../../scripts/update_status.py)

## ポイント
- cron は `分 時 日 月 曜日`、時刻は **UTC**。日本時間 9:00 → `0 0 * * *`
- 毎時ちょうどは混み合って遅延しやすいので、`17` のように半端な分にする
- 既定の `GITHUB_TOKEN` は読み取りのみ。push するには `permissions: contents: write`
- `GITHUB_TOKEN` で push したコミットは **他のワークフローを起動しない**（無限ループ防止の仕様）
- Public リポジトリで **60日間活動がないと schedule は自動で無効化** されます（Actions タブから再有効化できる）
- `concurrency` で同時実行を防止

## 課題
[`exercise.yml`](exercise.yml) を `.github/workflows/my-06.yml` として完成させる。

- **毎週月曜 日本時間 8:30** に実行（＋手動実行）
- `practice/heartbeat.txt` に現在の日本時間を書いてコミット＆push

> ヒント: `TZ=Asia/Tokyo date "+%F %T"`

## 解答
[`solutions/my-06.yml`](../../solutions/my-06.yml)

## もっと遊ぶ
- [crontab.guru](https://crontab.guru/) で式を確認する習慣をつける
- 天気APIや為替APIを叩いて、結果を Markdown に残すスクリプトに改造する
