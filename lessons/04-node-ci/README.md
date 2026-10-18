# Lesson 04: Node.js の CI

## ゴール
- `actions/setup-node` と `npm ci` を使える
- `package-lock.json` とキャッシュの関係がわかる

## 見本を動かす
`node/` 配下を変更して push（または手動実行）。

見本: [`.github/workflows/l04-node-ci.yml`](../../.github/workflows/l04-node-ci.yml)
対象コード: [`node/src/text.js`](../../node/src/text.js)

## ポイント
- CI では `npm install` ではなく **`npm ci`**。lock ファイル通りに入れるので再現性が高い
- `cache: npm` のキャッシュキーは `package-lock.json` のハッシュ。サブフォルダにあるときは `cache-dependency-path` を指定
- テストは Node 標準の `node --test`、Lint は ESLint（`eslint.config.js`）

## 課題
1. [`exercise.yml`](exercise.yml) を `.github/workflows/my-04.yml` として完成させる
2. `node/src/text.js` に `function unused() {}` を足して PR → Lint で ❌ になるのを確認
3. 新しい関数（例: `reverse(text)`）とそのテストを追加して ✅ にする

## 解答
[`solutions/my-04.yml`](../../solutions/my-04.yml)

## もっと遊ぶ
- `node-version-file: .nvmrc` を使ってバージョンをファイル管理にしてみる
