# 🧑‍🏫 配布者・講師向けガイド

このリポジトリを **テンプレートとして配布し、勉強会や自習教材として使う** ための手順とノウハウです。

---

## 1. 配布の準備（最初の1回だけ）

### テンプレートリポジトリにする
1. 配布元リポジトリの **Settings** → **General**
2. **Template repository** にチェック

これで受講者側に **「Use this template」** ボタンが表示されます。

### 配布前のチェックリスト
- [ ] Actions タブで **L00 Setup Check** を実行し、すべて ✅
- [ ] L01〜L10 の見本を一通り手動実行し、すべて ✅（L08 は Issue と PR を1つずつ作って確認）
- [ ] [docs/SETUP.md](SETUP.md) の手順を、別アカウントまたは別リポジトリで一度通してみる
- [ ] README のロードマップと各レッスンのリンクが切れていない
- [ ] （任意）ライセンスファイル（`LICENSE`）を置く。社外配布なら必須に近い

### 配布元の L06 について
配布元でも L06 が毎日 `data/STATUS.md` をコミットします。テンプレートの中身が日々変わって困る場合は、配布元だけ L06 を Disable しておきましょう（複製先には影響しません）。

---

## 2. 受講者への案内文（コピペ用）

```text
GitHub Actions のハンズオン教材です。以下の手順で自分用のリポジトリを作ってから始めてください。

1. 次のURLを開き、右上の「Use this template」→「Create a new repository」
   https://github.com/<配布元>/<リポジトリ名>
2. Visibility は Public を選んで作成（Fork ではなく Use this template でお願いします）
3. 作成したリポジトリの docs/SETUP.md の手順に沿って準備（10分程度）
4. Actions タブの「L00 Setup Check」がすべて ✅ になったら準備完了です

当日までに 4 まで済ませておいてください。
```

---

## 3. 進め方と時間の目安

| # | レッスン | 目安 | 合格ライン（ここまでできればOK） |
| --- | --- | --- | --- |
| 00 | セットアップ | 10分 | L00 Setup Check がすべて ✅ |
| 01 | はじめてのワークフロー | 20分 | my-01 を手動実行し、Summary に一言が出る |
| 02 | トリガーとフィルター | 30分 | `.txt` の push では動き、`.md` だけの push では動かない |
| 03 | Python の CI | 30分 | わざと壊した PR が ❌、直して ✅ |
| 04 | Node.js の CI | 30分 | 未使用関数で Lint が ❌、直して ✅ |
| 05 | matrix | 20分 | 3つのジョブが並列で走る |
| 06 | 定期実行 | 30分 | 手動実行で heartbeat.txt が bot によりコミットされる |
| 07 | Pages デプロイ | 30分 | `site/` の変更が公開URLに反映される |
| 08 | Issue / PR 自動操作 | 30分 | `/hello` コメントに bot が返信する |
| 09 | ジョブの連携 | 30分 | 行数が多いときだけ notify が動く |
| 10 | 再利用 | 40分 | 自作 composite action を2回呼べる |
| | **合計** | **約5時間** | |

### おすすめの分け方
- **半日×2回**: 1日目 00〜05（基礎とCI）、2日目 06〜10（自動化と応用）
- **1時間×5回**: 2レッスンずつ。各回の冒頭10分で前回の振り返り
- **自習＋質問会**: 各自で進め、週1回30分の質問会

### 進行のコツ
- **最初に「わざと失敗させる」体験を入れる**と、ログの読み方が身につきます（Lesson 03・04・09）
- 解答（`solutions/`）は最初から見えています。**「5分詰まったら見てOK」** などルールを決めておくと進行が揃います
- 受講者に **進捗 Issue**（Issues → New issue → 📒 学習の進捗）を作ってもらうと、リポジトリURLを見るだけで進み具合がわかります

---

## 4. つまずきやすいポイント

経験上、以下で手が止まりやすいので、事前に一言添えると効果的です。

| ポイント | 一言 |
| --- | --- |
| YAML のインデント | 「タブ禁止、スペース2つ」 |
| `${{ }}` と `$VAR` の違い | 「`${{ }}` は GitHub が先に置換、`$VAR` はシェルの変数」 |
| cron の時刻 | 「UTC。日本時間から9時間引く」 |
| ローカルと bot のコミットの衝突 | 「push 前に `git pull --rebase`」 |
| `pull_request` と `pull_request_target` | 「後者はフォークのPRでも書き込み権限がある。だからPRのコードを動かしてはダメ」 |

詳しくは [トラブルシューティング](TROUBLESHOOTING.md) にまとめています。

---

## 5. 教材を更新したとき

「Use this template」で作ったリポジトリは **配布元の履歴を引き継がない** ため、更新は自動では届きません。

- 軽微な修正 → 変更点を案内し、必要なら受講者に手動で反映してもらう
- 大きな改訂 → 配布元でリリース（タグ）を切り、新しく複製し直してもらう

更新履歴は [CHANGELOG.md](../CHANGELOG.md) に記録してください。

---

## 6. 環境別の注意

| 環境 | 注意点 |
| --- | --- |
| 個人アカウント・Public | 推奨。制約なし |
| 個人アカウント・Private | Actions の無料枠を消費（matrix の Windows ランナーは消費が大きい）。Pages は有料プランが必要 |
| Organization のリポジトリ | 管理者が Actions や外部 Action の利用を制限している場合あり。`actions/*` の許可が必要 |
| GitHub Enterprise Server | `runs-on` のランナー名や Action のバージョンが異なる場合あり。事前検証必須 |

---

## 7. 構成ファイルの役割（カスタマイズする人向け）

| パス | 役割 |
| --- | --- |
| `.github/workflows/l00〜l10-*.yml` | 見本ワークフロー |
| `.github/workflows/_reusable-ci.yml` | Lesson 10 の再利用ワークフロー（部品） |
| `.github/actions/setup-both/` | Lesson 10 の composite action |
| `.github/labeler.yml` | Lesson 08 の PR 自動ラベル設定 |
| `.github/ISSUE_TEMPLATE/progress.md` | 進捗チェックリスト |
| `lessons/NN-*/` | 解説（README.md）と課題（exercise.yml） |
| `solutions/` | 課題の解答 |
| `python/` `node/` | CI の練習台になるサンプルコード |
| `scripts/` | Lesson 06（定期更新）と Lesson 07（サイトビルド）のスクリプト |
| `site/` | Pages で公開するページ |

レッスンを追加するときは、`lessons/11-xxx/` と `.github/workflows/l11-xxx.yml`、`solutions/my-11.yml` を作り、README のロードマップと進捗 Issue テンプレートに1行足してください。
