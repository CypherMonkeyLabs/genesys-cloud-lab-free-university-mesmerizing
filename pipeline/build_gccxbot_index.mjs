/* Build the offline Genesys guide index from this lab's own track files.
   Usage: node pipeline/build_gccxbot_index.mjs
   Writes campus/data/gccxbot-index.json. Do not edit that file by hand. */
import { readFileSync, writeFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { tokens } from "../campus/shared/pybot-chat/engine.js";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const trackDir = join(root, "campus/data/tracks");
const outPath = join(root, "campus/data/gccxbot-index.json");

const SYN = {
  queues: "queue",
  skills: "skill",
  trunks: "trunk",
  licences: "license",
  licenses: "license",
  signalling: "signal",
  signaling: "signal",
  organisations: "organization",
  organization: "organization",
  premises: "premise",
  premise: "premise",
  bots: "bot",
  edges: "edge",
  regions: "region",
  divisions: "division",
  flows: "flow",
  wrapup: "wrap",
  acw: "wrap",
  routing: "rout",
  routes: "rout",
  routed: "rout",
  bullseye: "bullseye",
  byoc: "byoc",
  webrtc: "webrtc",
  copilot: "copilot",
  architects: "architect",
};

/* Strict seeds for collisions a visitor hits on the suggestion chips.
   Excerpts are filled from the lesson file. how:false keeps a loose how-question off the seed. */
const SEED_RULES = [
  { lesson: "a-types", any: ["architect"], allow: ["architect", "flow", "type", "home", "task", "menu"], block: ["bot", "copilot"], topic: "architect", rank: 6 },
  { lesson: "r-bullseye", any: ["bullseye"], allow: ["bullseye", "rout", "ring", "target", "skill"], topic: "bullseye", rank: 8 },
  { lesson: "b-what", any: ["byoc"], allow: ["byoc", "cloud", "carrier", "trunk", "media"], block: ["premise"], topic: "byoc", rank: 8 },
  { lesson: "e-role", any: ["edge"], allow: ["edge", "premise", "local", "media", "hop"], topic: "edge", rank: 6 },
  { lesson: "w-map", any: ["wfm"], allow: ["wfm", "workforce", "wem", "schedule"], topic: "wfm", rank: 8 },
  { lesson: "f-sip", all: ["sip"], allow: ["sip", "rtp", "trunk", "protocol", "audio", "signal", "difference"], topic: "sip", rank: 7 },
  { lesson: "r-predict", all: ["predictive", "rout"], allow: ["predictive", "rout", "kpi", "timeout", "model"], block: ["engagement", "journey"], topic: "predictive", rank: 10 },
  { lesson: "pe-what", all: ["predictive", "engagement"], allow: ["predictive", "engagement", "site", "visitor", "journey"], block: ["rout"], topic: "engagement", rank: 10 },
  { lesson: "b-gcv", all: ["genesys", "cloud", "voice"], allow: ["genesys", "cloud", "voice", "door"], topic: "voice", rank: 9 },
  { lesson: "k-direct", all: ["direct", "rout"], allow: ["direct", "rout", "queue"], topic: "direct", rank: 9 },
];

function clip(text, max = 340) {
  const clean = String(text || "").replace(/\s+/g, " ").trim();
  if (clean.length <= max) return clean;
  const cut = clean.slice(0, max);
  const stop = Math.max(cut.lastIndexOf(". "), cut.lastIndexOf("? "));
  if (stop > 80) return cut.slice(0, stop + 1);
  return cut.trim();
}

const volatile = /price|priced|token|limit|version|deprecat|allotment|fair use|concurrent|package|cx 4|cx 3|2026|minutes|percent/i;

const docs = [];
const byLesson = new Map();

for (const name of readdirSync(trackDir).filter((file) => file.endsWith(".json")).sort()) {
  const track = JSON.parse(readFileSync(join(trackDir, name), "utf8"));
  for (const lesson of track.lessons) {
    const paras = Array.isArray(lesson.paras) ? lesson.paras.join(" ") : "";
    const summary = String(lesson.summary || "").trim();
    const dated = volatile.test(`${summary} ${paras}`) || String(lesson.uncertainty || "").trim();
    const stamp = dated
      ? " Last checked 2026-10. Unconfirmed if the vendor page has moved."
      : " Last checked 2026-10.";
    const uncertainty = String(lesson.uncertainty || "").trim();
    const ex = clip(`${lesson.title}. ${summary}${uncertainty ? ` Unconfirmed: ${clip(uncertainty, 140)}` : ""}${stamp}`);
    const eg = clip(paras, 180);
    const id = `lesson:${track.id}/${lesson.id}`;
    const body = [lesson.title, summary, paras].join("\n");
    const doc = {
      i: id,
      k: "lesson",
      ti: lesson.title,
      h: `#/lesson/${lesson.id}`,
      s: track.id,
      ex,
      eg,
      w: tokens(body, SYN, 3),
      tw: tokens(lesson.title, SYN, 2),
    };
    docs.push(doc);
    byLesson.set(lesson.id, doc);
  }
}

docs.push({
  i: "page:downloads",
  k: "download",
  ti: "Downloads",
  h: "#/downloads",
  s: "downloads",
  ex: "Cheat sheets and the offline zip are on the downloads page. They link back to the public source.",
  eg: "",
  w: tokens("downloads cheat sheet offline zip export", SYN, 2),
  tw: tokens("Downloads", SYN, 2),
});
docs.push({
  i: "page:play",
  k: "game",
  ti: "Play",
  h: "#/play",
  s: "play",
  ex: "Play holds short games that run in this browser. They are simulations, not a live organization.",
  eg: "",
  w: tokens("play games simulations browser", SYN, 2),
  tw: tokens("Play", SYN, 2),
});

const seeds = [];
for (const rule of SEED_RULES) {
  const doc = byLesson.get(rule.lesson);
  if (!doc) continue;
  seeds.push({
    i: doc.i,
    h: doc.h,
    ti: doc.ti,
    k: "lesson",
    ex: doc.ex,
    eg: doc.eg,
    topic: rule.topic,
    all: rule.all || [],
    any: rule.any || [],
    allow: rule.allow || [],
    block: rule.block || [],
    how: false,
    rank: rule.rank || 1,
  });
}

const index = { v: 2, syn: SYN, seeds, docs };
writeFileSync(outPath, `${JSON.stringify(index)}\n`);
console.log(`gccxbot index: ${docs.length} docs, ${seeds.length} seeds -> ${outPath}`);
