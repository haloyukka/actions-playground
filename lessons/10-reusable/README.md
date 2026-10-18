# Lesson 10: 再利用（reusable workflow / composite action）

## ゴール
- 同じ処理をコピペせずに部品化できる
- **reusable workflow**（ジョブ単位の部品）と **composite action**（ステップ単位の部品）を使い分けられる

## 見本を動かす
Actions タブ → **L10 Reusable** → Run workflow。
1つの部品 `_reusable-ci.yml` が python 用・node 用の2回呼ばれます。

- 呼ぶ側: [`.github/workflows/l10-reusable.yml`](../../.github/workflows/l10-reusable.yml)
- 呼ばれる側: [`.github/workflows/_reusable-ci.yml`](../../.github/workflows/_reusable-ci.yml)
- composite action: [`.github/actions/setup-both/action.yml`](../../.github/actions/setup-both/action.yml)

## ポイント
| | reusable workflow | composite action |
| --- | --- | --- |
| 単位 | ジョブ（`runs-on` ごと） | ステップの束 |
| 置き場所 | `.github/workflows/` | どこでも（慣習は `.github/actions/<名前>/action.yml`） |
| 呼び方 | `jobs.<id>.uses:` | `steps[].uses:` |
| トリガー | `on: workflow_call` | なし |
| 向いている用途 | CI一式の共通化、他リポジトリから呼ぶ | セットアップ手順の共通化 |

- composite の `run` には `shell:` 指定が必須
- 他リポジトリから呼ぶときは `uses: owner/repo/.github/workflows/x.yml@main`
- Secrets を渡すときは `secrets: inherit` か個別指定

## 課題
自分で composite action を作って使う。

1. `.github/actions/greet/action.yml` に、入力 `who` を受け取り「Hello, ◯◯!」と表示し、出力 `message` を返す composite action を作る（[`exercise-action.yml`](exercise-action.yml) を完成させる）
2. [`exercise.yml`](exercise.yml) を `.github/workflows/my-10.yml` として完成させ、action を2回呼んで出力を表示する

## 解答
- [`solutions/greet-action.yml`](../../solutions/greet-action.yml)（→ `.github/actions/greet/action.yml` に置く）
- [`solutions/my-10.yml`](../../solutions/my-10.yml)

## 🎓 修了！次の一歩
- **Secrets / Variables**: Settings → Secrets and variables → Actions に登録して `${{ secrets.X }}` / `${{ vars.X }}` で使う
- **クラウドへのデプロイ**: OIDC で GCP（`google-github-actions/auth`）や AWS（`aws-actions/configure-aws-credentials`）にキー無しで認証
- **自分の既存リポジトリに導入**: event-post-gen の Lint、cabinet 系の定期取り込み など
