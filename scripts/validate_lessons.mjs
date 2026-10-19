// Validates data/lesson-map.json against campus/data/tracks.
// Every lesson needs a level 0-10, at least one outcome, a source id that exists,
// a title that matches the lesson file, and last_verified null or YYYY-MM-DD.
// Run: node scripts/validate_lessons.mjs
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const map = JSON.parse(readFileSync(join(root, "data/lesson-map.json"), "utf8"));
const schema = JSON.parse(readFileSync(join(root, "data/lesson-schema.json"), "utf8"));
const trackDir = join(root, "campus/data/tracks");
const sourceDir = join(root, "campus/data/sources");

const problems = [];
const mapped = new Map(map.lessons.map((lesson) => [lesson.key, lesson]));
const seen = new Set();
const required = schema.required;

for (const name of readdirSync(trackDir).filter((file) => file.endsWith(".json"))) {
  const track = JSON.parse(readFileSync(join(trackDir, name), "utf8"));
  for (const lesson of track.lessons) {
    const key = `${track.id}/${lesson.id}`;
    seen.add(key);
    const row = mapped.get(key);
    if (!row) {
      problems.push(`${key}: not in lesson-map.json`);
      continue;
    }
    for (const field of required) if (!(field in row)) problems.push(`${key}: missing field ${field}`);
    if (!Number.isInteger(row.level) || row.level < 0 || row.level > 10) problems.push(`${key}: level must be 0-10`);
    if (!Array.isArray(row.outcomes) || row.outcomes.length < 1 || row.outcomes.some((item) => typeof item !== "string" || item.length < 8)) {
      problems.push(`${key}: needs at least one outcome`);
    }
    if (!Array.isArray(row.sources) || row.sources.length < 1) problems.push(`${key}: needs at least one source`);
    for (const sourceId of row.sources || []) {
      if (!existsSync(join(sourceDir, `${sourceId}.json`))) problems.push(`${key}: unknown source id ${sourceId}`);
    }
    if (row.title !== lesson.title) problems.push(`${key}: title differs from the lesson file`);
    if (row.minutes !== lesson.minutes) problems.push(`${key}: minutes differ from the lesson file`);
    if (row.last_verified !== null && !/^\d{4}-\d{2}-\d{2}$/.test(row.last_verified)) {
      problems.push(`${key}: last_verified must be null or YYYY-MM-DD`);
    }
  }
}
for (const key of mapped.keys()) if (!seen.has(key)) problems.push(`${key}: in lesson-map.json but no such lesson`);

const perLevel = {};
for (const row of map.lessons) perLevel[row.level] = (perLevel[row.level] || 0) + 1;
for (const problem of problems) console.log("FAIL", problem);
console.log("lessons:", seen.size, "mapped:", mapped.size, "per level:", JSON.stringify(perLevel));
console.log("validate_lessons:", problems.length, "problems");
process.exit(problems.length ? 1 : 0);
