/* Rewrite the SHELL list in campus/sw.js from the lab shell and a size budget. */
import fs from "node:fs";
import path from "node:path";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const campus = path.join(root, "campus");
const budget = 3_500_000;

const required = [
  "index.html",
  "offline.html",
  "manifest.webmanifest",
  "favicon.svg",
  "icon-192.png",
  "icon-512.png",
  "icon-maskable-512.png",
  "assets/app.js",
  "assets/university.css",
  "assets/css/frame.css",
  "assets/css/wow.css",
  "assets/css/footer.css",
  "assets/round2.css",
  "assets/round2.js",
  "assets/sources.js",
  "assets/js/frame.js",
  "assets/js/university.js",
  "assets/mascot.js",
  "assets/diagrams.js",
  "assets/pages.js",
  "assets/i18n.js",
  "assets/icons3d.js",
  "assets/headings.js",
  "assets/lightbox.js",
  "assets/studios.js",
  "assets/routing-model.js",
  "guide/guide.css",
  "guide/guide.js",
  "guide/dragbot.js",
  "shared/pybot-chat/engine.js",
  "shared/pybot-chat/ui.js",
  "shared/pybot-chat/chat.css",
  "data/gccxbot-index.json",
  "data/manifest.json",
  "data/reference.json",
];

for (const folder of ["data/tracks", "data/sources"]) {
  for (const name of fs.readdirSync(path.join(campus, folder))) {
    if (name.endsWith(".json")) required.push(`${folder}/${name}`);
  }
}

const chosen = [];
let total = 0;
function consider(rel) {
  const abs = path.join(campus, rel);
  if (!fs.existsSync(abs) || chosen.includes(rel)) return;
  const size = fs.statSync(abs).size;
  if (total + size > budget) {
    console.log("skip over budget", rel, size);
    return;
  }
  chosen.push(rel);
  total += size;
}
for (const rel of required) consider(rel);

const body = chosen.map((rel) => `  "./${rel}",`).join("\n");
const swPath = path.join(campus, "sw.js");
let sw = fs.readFileSync(swPath, "utf8");
if (!sw.includes("const SHELL = [")) {
  console.error("campus/sw.js has no SHELL list");
  process.exit(1);
}
sw = sw.replace(/const SHELL = \[[\s\S]*?\];/, `const SHELL = [\n  "./",\n${body}\n];`);
sw = sw.replace(/gccx-lab-v\d+/, "gccx-lab-v19");
fs.writeFileSync(swPath, sw);
console.log(`precache ${chosen.length + 1} files, ${total} bytes, budget ${budget}`);
