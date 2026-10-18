import { test } from "node:test";
import assert from "node:assert/strict";
import { slugify, countWords } from "../src/text.js";

test("slugify", () => {
  assert.equal(slugify("  Hello GitHub Actions!  "), "hello-github-actions");
});

test("countWords", () => {
  assert.equal(countWords("one two  three"), 3);
  assert.equal(countWords("   "), 0);
});
