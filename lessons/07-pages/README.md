# Lesson 07: ビルドして GitHub Pages にデプロイ

## ゴール
- 「build ジョブ → deploy ジョブ」の2段構成がわかる
- `environment` と `permissions: pages / id-token` の意味がわかる

## 事前準備（1回だけ）
**Settings → Pages → Build and deployment → Source** を **GitHub Actions** に変更。

## 見本を動かす
Actions タブ → **L07 Deploy Pages** → Run workflow。
完了すると deploy ジョブに公開URL（`https://haloyukka.github.io/actions-playground/`）が出ます。

見本: [`.github/workflows/l07-pages.yml`](../../.github/workflows/l07-pages.yml)
ビルド: [`scripts/build_site.mjs`](../../scripts/build_site.mjs) が [`site/index.html`](../../site/index.html) を `dist/` に書き出す

## ポイント
- `upload-pages-artifact` でビルド結果を渡し、`deploy-pages` が公開する
- `needs: build` で順番を保証
- `environment: github-pages` にすると、Settings → Environments でデプロイ履歴や承認ルールが使える
- `id-token: write` は OIDC（パスワードを使わない本人確認）用。GCP / AWS へのデプロイでも同じ仕組みを使う

## 課題
見本をコピーして `.github/workflows/my-07.yml` を作り、次を足す。（`exercise.yml` は見本との差分だけ TODO にしてあります）

- `site/**` が変わった main への push でも自動デプロイ
- ページに表示する文言を変えて push → 数十秒後にサイトが更新されるのを確認

> ⚠️ 見本と自分の両方が同じ `pages` concurrency を使うので、同時には走りません（順番待ちになる）

## 解答
[`solutions/my-07.yml`](../../solutions/my-07.yml)

## もっと遊ぶ
- `site/` に CSS や別ページを足す
- `data/STATUS.md` を HTML に変換して表示する（Lesson 06 と組み合わせ）
