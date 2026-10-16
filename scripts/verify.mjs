import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { join } from "node:path";
import { decide } from "../campus/assets/routing-model.js";
import { DIAGRAMS, PORTS } from "../campus/assets/diagrams.js";
import { PAGE_CITES } from "../campus/assets/pages.js";
import { CHARTS } from "../campus/assets/floorviz.js";

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
const flowDiagrams = DIAGRAMS.filter((item) => item.flow);
if (DIAGRAMS.length < 60) problems.push(`diagrams ${DIAGRAMS.length}`);
if (flowDiagrams.length < 30) problems.push(`flows ${flowDiagrams.length}`);
if (CHARTS.length < 6) problems.push(`charts ${CHARTS.length}`);
for (const item of DIAGRAMS) checkUrl(item.url, item.id);
for (const item of PORTS) checkUrl(item.url, item.name);
for (const url of PAGE_CITES) checkUrl(url, "page");
const seenDiagram = new Set();
for (const item of DIAGRAMS) {
  if (seenDiagram.has(item.id)) problems.push(`duplicate diagram ${item.id}`);
  seenDiagram.add(item.id);
  if (!item.title || !item.caption) problems.push(`${item.id} blank`);
}

const html = readFileSync(join(root, "campus/index.html"), "utf8");
const brandLinks = [
  "https://cyphermonkeylabs.com",
  "https://github.com/CypherMonkeyLabs",
  "https://linktr.ee/cypherMonkey",
];
for (const needle of [...brandLinks, "learning-only", "© 2026 CypherMonkeyLabs", "CC BY-NC-SA"]) {
  if (!html.includes(needle)) problems.push(`chrome missing ${needle}`);
}
const forbidden = ["dev.to", "linkedin.com", "huggingface.co", "x.com/", "mailto:", "github.com/cipher0x9", "twitter.com"];
for (const needle of forbidden) {
  if (html.toLowerCase().includes(needle)) problems.push(`chrome forbids ${needle}`);
}
for (const id of ["menu-open", "nav-home", "tour-learn", "tour-diagrams", "tour-play", "tour-listen", "tour-downloads", "nav-guide", "font-color", "menu-font-color"]) {
  if (!html.includes(`id="${id}"`)) problems.push(`missing ${id}`);
}
for (const label of ["Diagrams", "Flows", "Charts", "Play", "Ecosystem", "Downloads", "Careers", "Help"]) {
  if (!html.includes(`>${label}<`) && !html.includes(`>${label} `)) problems.push(`menu ${label}`);
}
if (!html.includes("cyphermonkeylabs.com/")) problems.push("github.io strip");
if (!html.includes('id="theme-switch"')) problems.push("theme switcher");
for (const file of ["campus/vendor/d3.js", "campus/vendor/anime.js", "campus/vendor/rough.js", "campus/vendor/confetti.js", "campus/vendor/markmap.js", "campus/vendor/three.module.js", "campus/assets/floorviz.js", "campus/assets/hero3d.js"]) {
  if (!existsSync(join(root, file))) problems.push(`missing ${file}`);
}
const mermaidDir = join(root, "campus/assets/mermaid");
const mermaidSvgs = existsSync(mermaidDir) ? readdirSync(mermaidDir).filter((name) => name.endsWith(".svg")) : [];
if (mermaidSvgs.length < 5) problems.push(`mermaid svgs ${mermaidSvgs.length}`);

const downloadDir = join(root, "campus/downloads");
if (!existsSync(downloadDir)) problems.push("downloads missing");
else {
  const catalog = JSON.parse(readFileSync(join(downloadDir, "catalog.json"), "utf8"));
  if (catalog.sheets.length < 10) problems.push(`sheets ${catalog.sheets.length}`);
  for (const sheet of catalog.sheets) {
    for (const key of ["html", "pdf", "png"]) {
      const rel = sheet[key];
      if (!rel || !existsSync(join(root, "campus", rel))) problems.push(`${sheet.id || sheet.title} missing ${key}`);
    }
    if (sheet.html && existsSync(join(root, "campus", sheet.html))) {
      const text = readFileSync(join(root, "campus", sheet.html), "utf8");
      for (const needle of ["learning-only", "https://cyphermonkeylabs.com", "https://github.com/CypherMonkeyLabs", "https://linktr.ee/cypherMonkey"]) {
        if (!text.includes(needle)) problems.push(`${sheet.html} missing ${needle}`);
      }
      for (const needle of forbidden) {
        if (text.toLowerCase().includes(needle)) problems.push(`${sheet.html} forbids ${needle}`);
      }
    }
  }
  const cards = JSON.parse(readFileSync(join(downloadDir, "flashcards.json"), "utf8"));
  if (cards.cards.length < 400) problems.push("flashcards");
  for (const extra of ["flashcards.pdf", "genesys-cx-deck.pptx", "test-table.html", "templates/lab-checklist.docx", "templates/lab-checklist.pdf", "templates/lab-checklist.html"]) {
    if (!existsSync(join(downloadDir, extra))) problems.push(`missing downloads/${extra}`);
  }
  const diagramDir = join(downloadDir, "diagrams");
  const diagramHtml = existsSync(diagramDir) ? readdirSync(diagramDir).filter((name) => name.endsWith(".html")) : [];
  if (diagramHtml.length < 60) problems.push(`diagram html ${diagramHtml.length}`);
  for (const name of diagramHtml) {
    for (const ext of [".png", ".svg"]) {
      if (!existsSync(join(diagramDir, name.replace(/\.html$/, ext)))) problems.push(`diagram missing ${name} ${ext}`);
    }
  }
  if (statSync(join(downloadDir, "genesys-cx-offline-bundle.zip")).size < 1000) problems.push("zip");
  function walkDownloads(dir) {
    for (const name of readdirSync(dir)) {
      const file = join(dir, name);
      if (statSync(file).isDirectory()) {
        walkDownloads(file);
        continue;
      }
      if (!/\.(html|svg|json)$/.test(name)) continue;
      const text = readFileSync(file, "utf8");
      for (const needle of forbidden) {
        if (text.toLowerCase().includes(needle)) problems.push(`${file} forbids ${needle}`);
      }
      if (!text.includes("cyphermonkeylabs.com")) problems.push(`${name} footer`);
      if (!text.includes("linktr.ee/cypherMonkey")) problems.push(`${name} linktree`);
    }
  }
  walkDownloads(downloadDir);
  const predictive = manifest.tracks.find((track) => track.id === "predictive");
  if (!predictive || predictive.lessons.length < 7) problems.push("predictive track");
}

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
  diagrams: DIAGRAMS.length,
  flows: flowDiagrams.length,
  charts: CHARTS.length,
  mermaid: mermaidSvgs.length,
  sheets: existsSync(downloadDir) ? JSON.parse(readFileSync(join(downloadDir, "catalog.json"), "utf8")).sheets.length : 0,
  shellBytes,
  problems
};
console.log(JSON.stringify(report, null, 2));
if (problems.length) process.exit(1);
