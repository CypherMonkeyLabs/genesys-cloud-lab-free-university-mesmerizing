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
  { lesson: "w-map", any: ["workforce"], allow: ["workforce", "management", "wem", "wfm"], block: ["certification", "exam", "cert", "forecast", "business", "unit", "schedule"], topic: "wfm", rank: 11 },
  { lesson: "p-center", all: ["genesys", "api"], allow: ["genesys", "api", "cloud", "platform", "developer", "center", "cx"], block: ["salesforce", "zendesk", "embed"], topic: "api", rank: 12 },
  { lesson: "p-cc", all: ["client", "credential"], allow: ["client", "credentials", "credential", "oauth", "grant", "token"], block: ["salesforce", "zendesk"], topic: "api", rank: 11 },
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

/* Ordinary words that also show up in titles. They do not unlock search. */
const LEXICON_DENY = new Set(`best available phone phones call calls calling user users time work right new method methods type types home page first last name names list set open flat tire smart smartphone output back change off request rule approved plan floor using make need before after both choose cloud score scores priority conversation direct secure common digital virtual engine grant implicit client fair snippet map action goal service template group number numbers voice text data point points based within without during another same different real true false next high low long short small large big full empty start started starting ended ending help article guide sample browser organization interaction created morning everyone history public address location product claim catalog course exam today tomorrow please thanks hello world series flight laptop battery hiking boot capital japan spanish calorie mango faucet diaper stock apple photosynthesis hospital travel photos bake sourdough necktie oslo bread won cheapest recommend nearest painted starry night leaky fix translate calories many who how what when where why the and for with from into over under again still just like this that have been was are not can will your their them only other per via own such than then while about across around through between against email emails chat chats message messages inbound outbound local media pair pairs limit limits wrong defect every normal error queueing center centres centre contact contacts audio people person human thing things question questions which doing answer answers become becomes cannot nothing inside until three seven tried smaller similar showing weeks toward stayed stays watches waits picks reads reason order current system systems create created compare match matches listed documented offered promise prove people person human thing magic mystery disregard pretends widen widens clocks close complicated argue assume beside copying dates faster future hides invent invented inventing invoice lookback neighbor outer owner purpose qualified quick ratio search seconds table target tasks thing three timeout tried units until visitors waits watch weeks weights which`.split(/\s+/));
const KEEP_SHORT = new Set("acd sip rtp ivr wfm wem sta did pbx cx bot e164".split(" "));
const PRODUCT = new Set(`${[...KEEP_SHORT].join(" ")} genesys architect byoc srtp bullseye trunk trunks queue queues skill skills edge division divisions forecast adherence dialog wrap wrapup predictive engagement salesforce zendesk appfoundry scim e911 oauth copilot webrtc callback campaign region regions license licence licenses messenger gamification intraday schedule schedules utilization sentiment empathy transcript journey webhook notification credential credentials premise premises finesse cucm webex pureconnect uccx ucce routing rout ring rings flow flows chat email analytics speech quality coaching recording token tokens host hosts developer platform pkce dtmf sta wem ivrflow numberplan dialplan actionmap inqueue architectflow cisco workforce role`.split(/\s+/));

const words = new Set();
const phrases = new Set();
const glossaryWords = new Set();
const titleCount = new Map();
function stemLoose(word) {
  if (!word || word.length < 4) return word;
  if (word.length === 4) {
    if (word.endsWith("s") && !word.endsWith("ss")) return word.slice(0, -1);
    return word;
  }
  if (word.endsWith("ies") && word.length > 5 && word !== "series") return `${word.slice(0, -3)}y`;
  if (word.endsWith("ing") && word.length > 6) {
    let base = word.slice(0, -3);
    if (base.length > 3 && base.at(-1) === base.at(-2)) base = base.slice(0, -1);
    return base;
  }
  if (word.endsWith("ed") && word.length > 5) return word.slice(0, -2);
  if (/(ches|shes|sses|xes|zes|oes)$/.test(word)) return word.slice(0, -2);
  if (word.endsWith("s") && !word.endsWith("ss") && !word.endsWith("us") && !word.endsWith("is")) return word.slice(0, -1);
  return word;
}
function normalize(raw) {
  return String(raw || "").toLowerCase().replace(/[^a-z0-9+]+/g, " ").replace(/\s+/g, " ").trim();
}
function acceptWord(cleaned) {
  if (!cleaned || LEXICON_DENY.has(cleaned) || LEXICON_DENY.has(stemLoose(cleaned))) return false;
  if (cleaned.length < 3 && !KEEP_SHORT.has(cleaned)) return false;
  if (cleaned.length < 5 && !PRODUCT.has(cleaned) && !KEEP_SHORT.has(cleaned)) return false;
  return true;
}
const addWord = (raw, bucket) => {
  const cleaned = normalize(raw);
  if (!acceptWord(cleaned)) return;
  bucket.add(cleaned);
  const stemmed = stemLoose(cleaned);
  if (stemmed !== cleaned && acceptWord(stemmed)) bucket.add(stemmed);
};
const addText = (raw, asPhrase, bucket) => {
  const phrase = normalize(raw);
  if (!phrase) return;
  const parts = phrase.split(" ").filter(Boolean);
  if (asPhrase && parts.length >= 2 && phrase.length >= 5) phrases.add(phrase);
  if (asPhrase) {
    const compact = phrase.replace(/ /g, "");
    if (compact !== phrase && (KEEP_SHORT.has(compact) || PRODUCT.has(compact))) words.add(compact);
  }
  for (const part of parts) addWord(part, bucket);
};

/* Title phrases whose separate words are ordinary English. The pair is the lab term. */
const PRODUCT_PHRASES = [
  "data action",
  "data actions",
  "participant data",
  "secure call",
  "browser phone",
  "automatic call distribution",
  "short term",
];
for (const phrase of PRODUCT_PHRASES) phrases.add(phrase);
for (const name of PRODUCT) addWord(name, words);
for (const doc of docs) {
  const seen = new Set();
  for (const part of normalize(doc.ti).split(" ").filter(Boolean)) {
    if (seen.has(part)) continue;
    seen.add(part);
    titleCount.set(part, (titleCount.get(part) || 0) + 1);
  }
}
const reference = JSON.parse(readFileSync(join(root, "campus/data/reference.json"), "utf8"));
for (const entry of reference.glossary || []) addText(entry.term, true, glossaryWords);
for (const name of glossaryWords) words.add(name);
for (const [name, count] of titleCount) {
  if (count >= 2) addWord(name, words);
}

const lexicon = {
  words: [...words].sort(),
  phrases: [...phrases].sort(),
};
const index = { v: 2, syn: SYN, seeds, docs, lexicon };
writeFileSync(outPath, `${JSON.stringify(index)}\n`);
console.log(`gccxbot index: ${docs.length} docs, ${seeds.length} seeds, lexicon ${lexicon.words.length} words ${lexicon.phrases.length} phrases -> ${outPath}`);
