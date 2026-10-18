# 🛝 actions-playground

GitHub Actions を **手を動かして** 学ぶためのハンズオン教材です。
各レッスンは「見本を動かす → 解説を読む → 課題の TODO を埋める → 解答と見比べる」の流れで進みます。

## 🏁 はじめに

このリポジトリは **テンプレート** です。まず自分用に複製してください。

1. 右上の **「Use this template」→「Create a new repository」**（Public 推奨・Fork は不可）
2. [📘 セットアップ手順](docs/SETUP.md) に沿って準備（約10分）
3. Actions タブの **L00 Setup Check** がすべて ✅ になったら [Lesson 01](lessons/01-hello/) へ

## 📚 ドキュメント

| ドキュメント | 対象 | 内容 |
| --- | --- | --- |
| [セットアップ手順](docs/SETUP.md) | 受講者 | 複製〜環境チェックまで |
| [トラブルシューティング](docs/TROUBLESHOOTING.md) | 受講者 | よくあるエラーと対処 |
| [配布者・講師向けガイド](docs/FACILITATOR.md) | 配布者 | 配布手順・時間配分・合格ライン・つまずきポイント |
| [更新履歴](CHANGELOG.md) | 全員 | 教材のバージョン |

## 🗺️ ロードマップ

| # | レッスン | 学ぶこと | 見本 | 起動方法 | 目安 |
| --- | --- | --- | --- | --- | --- |
| 00 | [セットアップ](docs/SETUP.md) | 複製・Pages 設定・環境チェック | `l00-setup-check.yml` | 手動 | 10分 |
| 01 | [はじめてのワークフロー](lessons/01-hello/) | 構文・コンテキスト・出力・サマリー | `l01-hello.yml` | 手動 | 20分 |
| 02 | [トリガーとフィルター](lessons/02-triggers/) | push / PR / 手動入力 / paths / if | `l02-triggers.yml` | `practice/` 変更・手動 | 30分 |
| 03 | [Python の CI](lessons/03-python-ci/) | checkout / setup-python / キャッシュ / ruff / pytest | `l03-python-ci.yml` | `python/` 変更・手動 | 30分 |
| 04 | [Node.js の CI](lessons/04-node-ci/) | setup-node / npm ci / ESLint / node --test | `l04-node-ci.yml` | `node/` 変更・手動 | 30分 |
| 05 | [matrix で並列実行](lessons/05-matrix/) | matrix / include / exclude / fail-fast | `l05-matrix.yml` | 手動 | 20分 |
| 06 | [定期実行と自動コミット](lessons/06-schedule/) | cron(UTC) / permissions / bot コミット | `l06-scheduled-update.yml` | 毎日 9:17 JST・手動 | 30分 |
| 07 | [Pages にデプロイ](lessons/07-pages/) | build → deploy / environment / OIDC | `l07-pages.yml` | 手動 | 30分 |
| 08 | [Issue / PR の自動操作](lessons/08-issue-pr/) | github-script / labeler / スラッシュコマンド | `l08-issue-automation.yml` | Issue・PR 作成 | 30分 |
| 09 | [ジョブの連携](lessons/09-jobs/) | needs / outputs / artifact / always() | `l09-jobs.yml` | 手動 | 30分 |
| 10 | [再利用](lessons/10-reusable/) | reusable workflow / composite action | `l10-reusable.yml` | 手動 | 40分 |

合計 **約5時間**。進捗は Issues → New issue → **📒 学習の進捗** で管理できます。

## 🎮 遊び方

1. レッスンの README を開く
2. **Actions** タブで見本ワークフローを動かしてログを眺める
3. `lessons/NN-*/exercise.yml` を `.github/workflows/my-NN.yml` にコピーして `TODO` を埋める
4. push（または手動実行）して ✅ になるまで直す
5. `solutions/` の解答と見比べる

```bash
git clone https://github.com/<あなたのユーザー名>/<リポジトリ名>.git
cd <リポジトリ名>
cp lessons/01-hello/exercise.yml .github/workflows/my-01.yml
# 編集して…
git add . && git commit -m "lesson 01" && git push
```

ブラウザだけで進めたい場合は、GitHub 上で `.` キーを押すと Web 版 VS Code が開きます。

## 📁 構成

```
.github/
  workflows/       見本 (l00〜l10) と、あなたの my-*.yml
  actions/         composite action (Lesson 10)
  ISSUE_TEMPLATE/  進捗チェックリスト
  labeler.yml      PR 自動ラベル設定 (Lesson 08)
docs/              セットアップ手順・講師ガイド・トラブルシューティング
lessons/           解説・課題
solutions/         解答
python/            テスト・Lint の練習台 (pytest / ruff)
node/              テスト・Lint の練習台 (node --test / ESLint)
scripts/           定期実行・ビルド用スクリプト
site/              Pages で公開するページ
data/STATUS.md     Lesson 06 が毎日自動更新
practice/          課題で自由に使うフォルダ
```

## 🛠️ 便利ツール

- **actionlint**: ワークフローの文法チェッカー。push 前にローカルで確認できる（`brew install actionlint`）
- **VS Code 拡張「GitHub Actions」**: YAML の補完と実行状況の表示
- **act**: ワークフローをローカルの Docker で動かす（一部機能は非対応）

困ったときは [トラブルシューティング](docs/TROUBLESHOOTING.md) へ。
