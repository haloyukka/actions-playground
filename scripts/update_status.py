"""定期実行（Lesson 06）で呼ばれるスクリプト。

リポジトリの状態を集計して data/STATUS.md を書き換える。
外部APIに依存しないので、どこで動かしても同じように動く。
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JST = timezone(timedelta(hours=9))


def count(pattern: str) -> int:
    return len(list(ROOT.glob(pattern)))


def main() -> None:
    now = datetime.now(JST).strftime("%Y-%m-%d %H:%M JST")
    run_id = os.environ.get("GITHUB_RUN_ID", "local")
    event = os.environ.get("GITHUB_EVENT_NAME", "local")

    rows = [
        ("レッスン数", count("lessons/*/README.md")),
        ("見本ワークフロー数", count(".github/workflows/*.yml")),
        ("あなたのワークフロー数 (my-*.yml)", count(".github/workflows/my-*.yml")),
        ("Pythonテストファイル数", count("python/tests/test_*.py")),
        ("Nodeテストファイル数", count("node/test/*.test.js")),
    ]

    lines = [
        "# 📊 Playground Status",
        "",
        "このファイルは `l06-scheduled-update.yml` が自動で書き換えています。",
        "",
        "| 項目 | 値 |",
        "| --- | --- |",
        *[f"| {k} | {v} |" for k, v in rows],
        "",
        f"- 最終更新: {now}",
        f"- トリガー: `{event}` / Run ID: `{run_id}`",
        "",
    ]
    out = ROOT / "data" / "STATUS.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
