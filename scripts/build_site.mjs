// Lesson 07 (Pages デプロイ) で呼ばれるビルドスクリプト。
// site/index.html のプレースホルダーを置き換えて dist/ に出力する。
import { mkdirSync, readFileSync, writeFileSync, cpSync, existsSync } from "node:fs";

const sha = (process.env.GITHUB_SHA ?? "local").slice(0, 7);
const runNumber = process.env.GITHUB_RUN_NUMBER ?? "-";
const builtAt = new Date().toLocaleString("ja-JP", { timeZone: "Asia/Tokyo" });

mkdirSync("dist", { recursive: true });
const html = readFileSync("site/index.html", "utf8")
  .replaceAll("{{SHA}}", sha)
  .replaceAll("{{RUN_NUMBER}}", runNumber)
  .replaceAll("{{BUILT_AT}}", builtAt);
writeFileSync("dist/index.html", html);
if (existsSync("data/STATUS.md")) cpSync("data/STATUS.md", "dist/STATUS.md");
console.log(`built dist/index.html (sha=${sha}, run=${runNumber})`);
