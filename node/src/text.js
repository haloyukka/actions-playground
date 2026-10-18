// テスト・Lintの練習台になる小さな関数たち

export function slugify(text) {
  return text
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

export function countWords(text) {
  const words = text.trim().split(/\s+/).filter(Boolean);
  return words.length;
}
