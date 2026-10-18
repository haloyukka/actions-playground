# 🧯 トラブルシューティング

症状から探してください。見つからないときは、Actions の実行ログ（赤くなったステップを開いた中身）を読むのが一番の近道です。

## ワークフローが出てこない・動かない

| 症状 | 原因と対処 |
| --- | --- |
| Actions タブに自分のワークフローが出ない | `.github/workflows/` の直下に置いているか確認。サブフォルダは不可。拡張子は `.yml` か `.yaml` |
| 出てくるけど「This run likely failed because of a workflow file issue」 | YAML の文法エラー。インデントはスペース2つ（タブ不可）、`:` の後ろにスペースがあるか確認 |
| 「Run workflow」ボタンが無い | `on:` に `workflow_dispatch:` が無い、または default ブランチ（main）にまだ push されていない |
| push しても動かない | `branches` / `paths` フィルターに合っていない。変更したファイルが `paths` の対象か確認 |
| PR を作っても動かない | `on: pull_request` が無い、または `paths` が合っていない |
| schedule が動かない | cron の時刻は **UTC**。また 60日間リポジトリに動きが無いと自動停止する（Actions タブから再有効化） |
| schedule が数分〜数十分遅れる | 仕様です。混雑時は遅延します。毎時0分を避けると多少ましになります |

## 権限エラー

| エラー | 対処 |
| --- | --- |
| `Permission to ... denied to github-actions[bot]` / 403 | ワークフローの `permissions:` に必要な権限を書く（例: push なら `contents: write`） |
| `Resource not accessible by integration` | 同上。Issue なら `issues: write`、PR なら `pull-requests: write` |
| Pages デプロイで `Get Pages site failed` | Settings → Pages → Source が「GitHub Actions」になっていない |
| Pages デプロイで `Missing environment` / 保護ルールで止まる | Settings → Environments → `github-pages` のデプロイ元ブランチに `main` が許可されているか確認 |

## よくある書き間違い

```yaml
# ❌ uses と run を1つのステップに書いている
- uses: actions/checkout@v7
  run: echo hi

# ✅ 別々のステップにする
- uses: actions/checkout@v7
- run: echo hi
```

```yaml
# ❌ 式の外で比較している（常に true になる）
if: ${{ inputs.mood }} == 'sleepy'

# ✅ 式の中で比較する（if では ${{ }} を省略できる）
if: inputs.mood == 'sleepy'
```

```yaml
# ❌ 引用符なしの値に ": "（コロン＋スペース）があると YAML が壊れる
run: echo 結果: OK

# ✅ 迷ったらブロック形式に
run: |
  echo "結果: OK"
```

```yaml
# ❌ バージョン番号が数値として解釈される（3.10 → 3.1 になる）
python-version: 3.10

# ✅ 引用符で囲む
python-version: "3.10"
```

## レッスン別

| レッスン | 症状 | 対処 |
| --- | --- | --- |
| 03 | `ModuleNotFoundError: playground` | `working-directory: python` が抜けている（`pyproject.toml` の設定が読まれない） |
| 04 | `npm ci` が `package-lock.json` が無いと言う | `working-directory: node` が抜けている |
| 06 | `nothing to commit` で失敗 | 変更が無いのに `git commit` している。見本のように `git diff --quiet` で判定する |
| 06 | 手元で `git push` が `rejected` | bot が先にコミットしている。`git pull --rebase` してから push |
| 07 | 公開URLを開くと 404 | 初回は反映まで1〜2分かかることがある。deploy ジョブが ✅ か確認 |
| 08 | `/hello` に反応しない | ワークフローが default ブランチ（main）に入っているか確認。`issue_comment` は main の定義で動く |
| 09 | `Unable to find any artifacts` | upload と download の `name` が一致しているか確認 |
| 10 | `Can't find 'action.yml'` | ローカル action を使う前に `actions/checkout` していない |

## 手元で事前にチェックする

push する前に [actionlint](https://github.com/rhysd/actionlint) で文法チェックすると、往復が減ります。

```bash
# macOS
brew install actionlint
# リポジトリのルートで
actionlint
```

## それでも解決しないとき

- 実行ページ右上の **「Re-run jobs」→「Enable debug logging」** で詳細ログを出す
- 公式ドキュメント: [GitHub Actions ドキュメント](https://docs.github.com/ja/actions)
