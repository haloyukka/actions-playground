# 🚀 セットアップ手順（受講者向け）

このリポジトリはテンプレートです。**自分のアカウントに複製してから** 学習を始めます。
所要時間はおよそ **10分** です。

---

## 0. 必要なもの

| 必要なもの | 備考 |
| --- | --- |
| GitHub アカウント | 無料プランで OK |
| ブラウザ | これだけでも全レッスン進められます |
| Git とエディタ（任意） | 手元で編集したい場合。VS Code 推奨 |

GitHub Actions の事前知識は不要です。YAML を見たことがある程度で大丈夫です。

---

## 1. テンプレートから自分のリポジトリを作る

1. このリポジトリのトップページ右上の **「Use this template」** → **「Create a new repository」**
2. 次のように入力して **「Create repository」**

   | 項目 | 設定 |
   | --- | --- |
   | Owner | 自分のアカウント |
   | Repository name | 例: `actions-playground` |
   | Visibility | **Public**（推奨） |
   | Include all branches | チェック不要 |

> 💡 **なぜ Public？** Public なら Actions の実行時間が無料で無制限、Pages も無料プランで使えます。
> 中身は教材だけなので公開しても問題ありません。Private にしたい場合は [注意点](#private-で使いたい場合) を確認してください。

> ⚠️ **「Fork」ではなく「Use this template」を使ってください。** フォークだと Actions が既定で無効になり、定期実行（Lesson 06）も動きません。

---

## 2. Actions が有効か確認する

作成したリポジトリの **Actions** タブを開きます。

- ワークフローの一覧（L00〜L10）が表示されていれば OK
- 「Workflows aren't being run on this repository」などと出たら、**「I understand my workflows, go ahead and enable them」** を押す

> 作成直後に L02〜L04 が自動で動いていることがありますが、正常です。

---

## 3. Pages の公開元を設定する（Lesson 07 用）

1. **Settings** → 左メニュー **Pages**
2. **Build and deployment** → **Source** を **「GitHub Actions」** に変更

保存ボタンはありません。選んだ時点で反映されます。

---

## 4. 環境チェックを実行する

1. **Actions** タブ → 左の **「L00 Setup Check」**
2. 右の **「Run workflow」** → **「Run workflow」**
3. 実行が終わったらクリックして、下部の **Summary** を確認

すべて ✅ なら準備完了です。⚠️ があれば、メッセージに従って直してから再実行してください。

> このチェックで、進捗管理用の `progress` ラベルも自動で作られます。

---

## 5. 進捗チェックリストを作る（任意）

1. **Issues** タブ → **New issue** → **「📒 学習の進捗」** を選んで作成
2. レッスンが終わるたびにチェックを入れていく

講師や仲間に進み具合を共有するときにも使えます。

---

## 6. 学習スタート！

[Lesson 01](../lessons/01-hello/) から順番に進めます。各レッスンの流れは次の通りです。

```
見本を Actions タブで動かす
  → README の解説を読む
  → exercise.yml を .github/workflows/my-NN.yml にコピーして TODO を埋める
  → push して ✅ になるまで直す
  → solutions/ の解答と見比べる
```

### ブラウザだけで進める場合

- リポジトリのページで **`.` キー** を押すと、Web 版 VS Code（github.dev）が開きます
- ファイルをコピー・編集したら、左の「ソース管理」からコミット＆プッシュ

### 手元の PC で進める場合

```bash
git clone https://github.com/<あなたのユーザー名>/<リポジトリ名>.git
cd <リポジトリ名>
cp lessons/01-hello/exercise.yml .github/workflows/my-01.yml
# 編集して…
git add .
git commit -m "lesson 01"
git push
```

---

## 知っておくと安心なこと

### 毎朝 bot のコミットが増える
Lesson 06 の見本 **L06 Scheduled Update** が、毎日 9:17（日本時間）に `data/STATUS.md` を更新してコミットします。
止めたいときは **Actions** タブ → L06 → 右上の **「…」** → **Disable workflow**。

### 手元で `git push` が拒否される
bot が先にコミットしているためです。`git pull --rebase` してから push し直してください。

### Private で使いたい場合
- Actions は無料枠（月あたりの実行時間）を消費します。Lesson 05 の matrix は Windows ランナーを使うため消費が大きめです
- Lesson 07（Pages）は無料プランの Private リポジトリでは使えません
- 組織（Organization）のリポジトリでは、管理者が Actions を制限している場合があります

困ったときは [トラブルシューティング](TROUBLESHOOTING.md) を見てください。
