import { readFileSync } from "node:fs";
import { join } from "node:path";
import { decide } from "../campus/assets/routing-model.js";

const root = join(import.meta.dirname, "..");
const manifest = JSON.parse(readFileSync(join(root, "campus/data/manifest.json"), "utf8"));
const reference = JSON.parse(readFileSync(join(root, "campus/data/reference.json"), "utf8"));

const ALLOW = new Set([
  "help.genesys.cloud",
  "help.mypurecloud.com",
  "developer.genesys.cloud",
  "education.genesys.com",
  "appfoundry.genesys.com",
  "www.rfc-editor.org",
  "www.cisco.com",
  "www.genesys.com",
  "genesys.com"
]);

const problems = [];
let lessons = 0;
let quizzes = 0;
let labs = 0;
let faults = 0;
const ids = new Set();

function checkUrl(url, where) {
  let parsed;
  try {
    parsed = new URL(url);
  } catch {
    problems.push(`${where} bad url ${url}`);
    return;
  }
  if (parsed.protocol !== "https:") problems.push(`${where} not https ${url}`);
  if (!ALLOW.has(parsed.hostname)) problems.push(`${where} host ${parsed.hostname}`);
}

for (const stub of manifest.tracks) {
  const track = JSON.parse(readFileSync(join(root, "campus", stub.file), "utf8"));
  if (track.id !== stub.id) problems.push(`manifest id ${stub.id}`);
  for (const lesson of track.lessons) {
    lessons += 1;
    if (ids.has(lesson.id)) problems.push(`duplicate ${lesson.id}`);
    ids.add(lesson.id);
    quizzes += lesson.quiz.length;
    labs += 1;
    faults += 1;
    for (const key of ["figure", "flow", "quiz", "cards", "lab", "fault"]) {
      if (!lesson[key]) problems.push(`${lesson.id} missing ${key}`);
    }
    if (!lesson.figure?.nodes?.length || !lesson.flow?.steps?.length) problems.push(`${lesson.id} empty figure or flow`);
    if (lesson.quiz.length !== 6) problems.push(`${lesson.id} quiz ${lesson.quiz.length}`);
    if (lesson.cards.length !== 4) problems.push(`${lesson.id} cards`);
    if (lesson.lab.steps.length < 3) problems.push(`${lesson.id} lab`);
    if (lesson.flow.steps.length < 4) problems.push(`${lesson.id} flow`);
    for (const item of lesson.quiz) {
      if (item.answer < 0 || item.answer > 3 || item.choices.length !== 4) problems.push(`${lesson.id} choice`);
    }
    for (const cite of lesson.cites) checkUrl(cite.url, lesson.id);
  }
}

for (const item of reference.glossary) checkUrl(item.url, item.term);
for (const item of reference.certs) checkUrl(item.url, item.name);
for (const item of reference.interviews) checkUrl(item.url, item.q.slice(0, 24));
for (const boss of reference.bosses) {
  checkUrl(boss.url, boss.id);
  if (boss.steps.length < 2) problems.push(`${boss.id} steps`);
}

const shellFiles = ["campus/index.html", "campus/assets/app.js", "campus/data/manifest.json", "campus/manifest.webmanifest"];
const shellBytes = shellFiles.reduce((sum, file) => sum + readFileSync(join(root, file)).length, 0);
if (shellBytes > 500000) problems.push(`shell ${shellBytes} exceeds 500000`);

if (manifest.tracks.length < 15) problems.push("tracks");
if (lessons < 100) problems.push("lessons");
if (quizzes < 600) problems.push("quizzes");
if (labs < 20) problems.push("labs");
if (faults < 30) problems.push("faults");
if (reference.glossary.length < 40) problems.push("glossary");
if (reference.bosses.length < 8) problems.push("bosses");
if (reference.interviews.length < 24) problems.push("interviews");

function agent(name, extra) {
  return {
    name,
    onQueue: true,
    utilized: false,
    preferred: false,
    idleMs: 10000,
    skills: { Billing: 3, Spanish: 3 },
    ...extra
  };
}

const preferred = decide({
  scoring: "conversation",
  evaluation: "all",
  prefer: true,
  elapsedMs: 0,
  interactions: [{ id: "c", skills: ["Billing", "Spanish"], priority: 0, arrivedMs: 0 }],
  agents: [
    agent("Amina", { preferred: true, idleMs: 40000, skills: { Billing: 5 } }),
    agent("Leo", { idleMs: 120000, skills: { Billing: 2, Spanish: 4 } })
  ]
});
if (preferred.winner?.name !== "Amina") problems.push("preferred did not win");

const idle = decide({
  scoring: "conversation",
  evaluation: "all",
  prefer: false,
  elapsedMs: 0,
  interactions: [{ id: "c", skills: ["Billing"], priority: 0, arrivedMs: 0 }],
  agents: [
    agent("Short", { idleMs: 10000, skills: { Billing: 5 } }),
    agent("Long", { idleMs: 90000, skills: { Billing: 1 } })
  ]
});
if (idle.winner?.name !== "Long") problems.push("all-skills idle");

const ring = decide({
  scoring: "conversation",
  evaluation: "all",
  prefer: false,
  elapsedMs: 8000,
  rings: [{ delayMs: 8000, remove: [] }, { delayMs: 20000, remove: ["Spanish"] }],
  interactions: [{ id: "c", skills: ["Billing", "Spanish"], priority: 0, arrivedMs: 0 }],
  agents: [agent("OnlyBilling", { skills: { Billing: 4 } })]
});
if (ring.winner?.name !== "OnlyBilling" || !ring.required?.includes("Billing") || ring.required?.includes("Spanish")) {
  problems.push("bullseye removal");
}

const scored = decide({
  scoring: "conversation",
  evaluation: "disregard",
  prefer: false,
  elapsedMs: 0,
  interactions: [
    { id: "low", skills: [], priority: 0, arrivedMs: 0 },
    { id: "high", skills: [], priority: 5, arrivedMs: 240000 }
  ],
  agents: [agent("Ada", { skills: {} })]
});
if (!scored.trace?.[0]?.includes("high")) problems.push("conversation score");

const gated = decide({
  scoring: "conversation",
  evaluation: "all",
  prefer: false,
  elapsedMs: 0,
  interactions: [{ id: "c", skills: ["Billing"], priority: 0, arrivedMs: 0 }],
  agents: [
    agent("Busy", { utilized: true, idleMs: 999999 }),
    agent("Away", { onQueue: false, idleMs: 999999 }),
    agent("Ready", { idleMs: 1000 })
  ]
});
if (gated.winner?.name !== "Ready") problems.push("utilization or queue filter");

const report = {
  tracks: manifest.tracks.length,
  lessons,
  quizzes,
  labs,
  faults,
  glossary: reference.glossary.length,
  bosses: reference.bosses.length,
  interviews: reference.interviews.length,
  studios: manifest.studios.length,
  shellBytes,
  problems
};
console.log(JSON.stringify(report, null, 2));
if (problems.length) process.exit(1);
