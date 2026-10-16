/* Genesys guide. Facts come from data/guide-kb.json. The cloud endpoint stays unset. */
const STOP_KEY = "gccx-bot-stop";
const TOUR_KEY = "gccx-tour";
const GREET_KEY = "gccx-greet";
const POS_KEY = "gccx-bot-pos";
const OFFER_MAX = 3;
const IDLE_MS = [150000, 180000, 240000];

const STEPS = [
  { n: "1", title: "Home", text: "Home is the signal floor. Start here, then open Learn.", sel: ["#nav-home"] },
  { n: "2", title: "Menu", text: "Menu sits at the top left. It slides in. Esc or a tap outside closes it.", sel: ["#menu-open"] },
  { n: "3", title: "Learn", text: "Learn opens the tracks, from Foundations through migration.", sel: ["#tour-learn", "#nav-learn"] },
  { n: "4", title: "Diagrams", text: "Diagrams are teaching sketches. Each one names the page it came from.", sel: ["#tour-diagrams", "#nav-diagrams"] },
  { n: "5", title: "Play", text: "Play holds the games. Downloads is the export room, on this same bar.", sel: ["#tour-play", "#nav-play"], also: ["#tour-downloads"] },
  { n: "6", title: "Listen", text: "Listen is the audio desk. The monkey guide can read a room aloud.", sel: ["#tour-listen", "#nav-listen"], also: ["#bot-launcher"] }
];

const ROUTES = [
  [/download|cheat|sheet|export/, "#/downloads"],
  [/diagram|atlas/, "#/atlas"],
  [/flow/, "#/flows"],
  [/chart/, "#/charts"],
  [/play|game|badge/, "#/play"],
  [/listen|audio/, "#listen"],
  [/help|how do i/, "#/help"],
  [/legal|credit|licen|privacy/, "#/legal"],
  [/port/, "#/ports"],
  [/ecosystem|glossary/, "#/ecosystem"],
  [/learn|track|course|lesson|architect|routing/, "#/tracks"],
  [/home|start/, "#/"]
];

let kb = null;
let offers = 0;
let idleTimer = 0;
let speaking = false;
let paused = false;
let recog = null;
let stepIndex = 0;
let ambient = null;

function monkeySvg(id) {
  return `<svg class="monkey-svg" viewBox="0 0 200 230" role="img" aria-hidden="true">
    <defs>
      <radialGradient id="${id}-fur" cx="38%" cy="28%"><stop offset="0" stop-color="#fde68a"/><stop offset="1" stop-color="#f59e0b"/></radialGradient>
    </defs>
    <circle class="halo" cx="100" cy="108" r="92" fill="none" stroke="#fbbf24" stroke-width="5"/>
    <ellipse class="ear" cx="36" cy="86" rx="26" ry="32" fill="#f59e0b" stroke="#9a3412" stroke-width="3"/>
    <ellipse class="ear" cx="164" cy="86" rx="26" ry="32" fill="#f59e0b" stroke="#9a3412" stroke-width="3"/>
    <ellipse cx="36" cy="90" rx="12" ry="16" fill="#fb7185"/>
    <ellipse cx="164" cy="90" rx="12" ry="16" fill="#fb7185"/>
    <ellipse cx="100" cy="188" rx="54" ry="34" fill="#7c3aed" stroke="#4c1d95" stroke-width="3"/>
    <ellipse cx="100" cy="172" rx="26" ry="14" fill="#fde68a"/>
    <g class="arm-l"><path d="M52 168c-28 6-40 28-28 40 16 10 40-2 42-20z" fill="#f59e0b" stroke="#9a3412" stroke-width="3"/></g>
    <g class="arm-r"><path d="M148 168c28 6 40 28 28 40-16 10-40-2-42-20z" fill="#f59e0b" stroke="#9a3412" stroke-width="3"/></g>
    <circle cx="100" cy="102" r="64" fill="url(#${id}-fur)" stroke="#b45309" stroke-width="3"/>
    <ellipse cx="100" cy="118" rx="42" ry="36" fill="#fff7ed"/>
    <path class="brow" d="M58 78c10-8 22-8 32 0" fill="none" stroke="#9a3412" stroke-width="4" stroke-linecap="round"/>
    <path class="brow" d="M110 78c10-8 22-8 32 0" fill="none" stroke="#9a3412" stroke-width="4" stroke-linecap="round"/>
    <ellipse cx="76" cy="104" rx="16" ry="18" fill="#fff" stroke="#1e1b4b" stroke-width="3"/>
    <ellipse cx="124" cy="104" rx="16" ry="18" fill="#fff" stroke="#1e1b4b" stroke-width="3"/>
    <circle cx="78" cy="108" r="7" fill="#1e1b4b"/>
    <circle cx="126" cy="108" r="7" fill="#1e1b4b"/>
    <circle cx="81" cy="105" r="2.4" fill="#fff"/>
    <circle cx="129" cy="105" r="2.4" fill="#fff"/>
    <circle cx="76" cy="104" r="22" fill="none" stroke="#312e81" stroke-width="4"/>
    <circle cx="124" cy="104" r="22" fill="none" stroke="#312e81" stroke-width="4"/>
    <path d="M98 104h4" stroke="#312e81" stroke-width="4" stroke-linecap="round"/>
    <ellipse cx="100" cy="124" rx="9" ry="7" fill="#ea580c"/>
    <path class="mouth" d="M74 136c14 16 38 16 52 0" fill="none" stroke="#9a3412" stroke-width="4" stroke-linecap="round"/>
  </svg>`;
}

const root = document.createElement("div");
root.className = "bot-root";
root.id = "bot-root";
root.innerHTML = `
<button type="button" class="bot-launcher" id="bot-launcher" data-pose="idle" aria-expanded="false" aria-controls="bot-panel" aria-label="Genesys guide, a monkey">
  ${monkeySvg("bot")}
</button>
<div class="bot-nudge" id="bot-nudge" hidden>
  <p>Need a hand with this room?</p>
  <button type="button" data-nudge="help">Help</button>
  <button type="button" data-nudge="later">Not now</button>
  <button type="button" data-nudge="stop">Stop offering</button>
</div>
<section class="bot-panel" id="bot-panel" hidden aria-label="Genesys guide">
  <div class="sheet-handle" id="sheet-handle" aria-hidden="true"></div>
  <header class="bot-head"><span class="bot-head-monkey">${monkeySvg("sheet")}</span><strong>Genesys guide</strong> <button type="button" data-bot-close>Close</button></header>
  <div class="bot-offers">
    <button type="button" data-path="ten">Finish in 10 minutes</button>
    <button type="button" data-path="full">Full course</button>
    <button type="button" data-path="down">Just download</button>
  </div>
  <div class="bot-cards" id="bot-cards"></div>
  <div class="bot-voice-row">
    <label>Voice <select id="bot-voice" aria-label="Speaking voice"></select></label>
  </div>
  <div class="bot-log" id="bot-log" role="log" aria-live="polite"></div>
  <details class="bot-more" id="bot-more">
    <summary>Rate, pitch, and sound</summary>
    <div class="bot-voice">
      <label>Rate <input id="bot-rate" type="range" min="0.8" max="1.2" step="0.05" value="1" aria-label="Speaking rate"></label>
      <label>Pitch <input id="bot-pitch" type="range" min="0.8" max="1.2" step="0.05" value="1" aria-label="Speaking pitch"></label>
      <button type="button" id="bot-read">Read along</button>
      <button type="button" id="bot-pause">Pause</button>
      <button type="button" id="bot-stop">Stop</button>
      <label class="check"><input id="bot-ambient" type="checkbox"> Soft sound, off until you turn it on</label>
    </div>
  </details>
  <form class="bot-form" id="bot-form">
    <button type="button" id="bot-mic" aria-label="Voice input">Mic</button>
    <input id="bot-q" type="text" maxlength="240" autocomplete="off" aria-label="Ask about this lab" placeholder="Ask, or type if the mic is unavailable">
    <button type="submit">Send</button>
  </form>
  <p class="muted" id="bot-mic-note"></p>
</section>`;

const greet = document.createElement("div");
greet.className = "bot-greet";
greet.hidden = true;
greet.innerHTML = `<div class="bot-greet-card" role="dialog" aria-modal="true" aria-labelledby="greet-title">
  ${monkeySvg("greet")}
  <h2 id="greet-title">Welcome to CypherMonkey Labs</h2>
  <p>I'm your Genesys Cloud CX guide. I only answer from this lab's notes.</p>
  <div class="bot-offers">
    <button type="button" data-path="ten">Finish in 10 minutes</button>
    <button type="button" data-path="full">Full course</button>
    <button type="button" data-path="down">Just download</button>
    <button type="button" data-path="dock">Not now</button>
  </div>
</div>`;

const tour = document.createElement("div");
tour.className = "tour";
tour.id = "tour";
tour.hidden = true;
tour.innerHTML = `<div class="tour-spot" id="tour-spot"></div><div class="tour-spot tour-spot-b" id="tour-spot-b" hidden></div>
<div class="tour-card" role="dialog" aria-modal="true" aria-label="Tour">
  <p class="tour-kicker">Lab tour</p>
  <p class="tour-step" id="tour-step"><span class="tour-badge" id="tour-badge">1</span><span id="tour-step-label"></span></p>
  <p id="tour-copy"></p>
  <div class="tour-actions">
    <button type="button" id="tour-back">Back</button>
    <button type="button" id="tour-next">Next</button>
    <button type="button" id="tour-skip">Skip</button>
  </div>
</div>`;

const caption = document.createElement("p");
caption.className = "read-caption";
caption.hidden = true;

document.body.appendChild(root);
document.body.appendChild(greet);
document.body.appendChild(tour);
document.body.appendChild(caption);

const launcher = root.querySelector("#bot-launcher");
const panel = root.querySelector("#bot-panel");
const log = root.querySelector("#bot-log");
const cards = root.querySelector("#bot-cards");
const voiceSel = root.querySelector("#bot-voice");
const form = root.querySelector("#bot-form");
const input = root.querySelector("#bot-q");
const micNote = root.querySelector("#bot-mic-note");

function reduced() {
  return document.documentElement.dataset.reduce === "1" || window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}
function pose(name) {
  launcher.dataset.pose = name;
}
function sayLine(text) {
  const p = document.createElement("p");
  p.textContent = text;
  log.appendChild(p);
  log.scrollTop = log.scrollHeight;
}
function visible(selectors) {
  for (const sel of selectors) {
    const el = document.querySelector(sel);
    if (!el) continue;
    const style = getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    if (style.display === "none" || style.visibility === "hidden") continue;
    if (rect.width < 8 || rect.height < 8) continue;
    return el;
  }
  return null;
}
function placeSpot(box, el) {
  if (!el) {
    box.hidden = true;
    return;
  }
  const rect = el.getBoundingClientRect();
  box.hidden = false;
  box.style.left = Math.max(4, rect.left - 6) + "px";
  box.style.top = Math.max(4, rect.top - 6) + "px";
  box.style.width = rect.width + 12 + "px";
  box.style.height = rect.height + 12 + "px";
}
function showStep() {
  const step = STEPS[stepIndex];
  document.getElementById("tour-badge").textContent = step.n;
  document.getElementById("tour-step-label").textContent = "of 6 · " + step.title;
  document.getElementById("tour-copy").textContent = step.text;
  document.getElementById("tour-back").disabled = stepIndex === 0;
  document.getElementById("tour-next").textContent = stepIndex === STEPS.length - 1 ? "Finish" : "Next";
  placeSpot(document.getElementById("tour-spot"), visible(step.sel));
  placeSpot(document.getElementById("tour-spot-b"), step.also ? visible(step.also) : null);
  const card = tour.querySelector(".tour-card");
  const target = visible(step.sel);
  if (target && target.getBoundingClientRect().top < window.innerHeight * 0.45) card.style.bottom = "calc(var(--bar-h, 0px) + 16px)";
  else card.style.bottom = "auto", card.style.top = "calc(var(--chrome-h, 64px) + 12px)";
}
function startTour() {
  panel.hidden = true;
  greet.hidden = true;
  stepIndex = 0;
  tour.hidden = false;
  pose("wave");
  showStep();
}
function endTour(skip) {
  tour.hidden = true;
  try { localStorage.setItem(TOUR_KEY, "done"); } catch (err) { /* storage off */ }
  pose("idle");
  if (!skip) showGreet();
  else dock();
}
function showGreet() {
  if (localStorage.getItem(GREET_KEY) === "1") {
    dock();
    return;
  }
  pose("greet");
  greet.hidden = false;
  document.body.classList.add("greet-open");
}
function dock() {
  greet.hidden = true;
  document.body.classList.remove("greet-open");
  try { localStorage.setItem(GREET_KEY, "1"); } catch (err) { /* storage off */ }
  pose("idle");
  restorePos();
}
function restorePos() {
  try {
    const saved = JSON.parse(localStorage.getItem(POS_KEY) || "null");
    if (!saved || !saved.left) return;
    root.style.left = saved.left;
    root.style.top = saved.top;
    root.style.right = "auto";
    root.style.bottom = "auto";
  } catch (err) { /* keep the dock */ }
}
function lift() {
  const phone = window.matchMedia("(max-width: 700px)").matches;
  const bar = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--bar-h")) || (phone ? 72 : 0);
  if (!root.style.left && !phone) root.style.bottom = (bar + 10) + "px";
  const footer = document.querySelector(".site-footer");
  const docked = launcher.getBoundingClientRect();
  let cover = false;
  if (footer) {
    const rect = footer.getBoundingClientRect();
    cover = rect.top < docked.bottom && rect.bottom > docked.top && rect.left < docked.right && rect.right > docked.left;
  }
  root.classList.toggle("is-clear", cover);
}
function armIdle() {
  window.clearTimeout(idleTimer);
  if (localStorage.getItem(STOP_KEY) === "1" || offers >= OFFER_MAX) return;
  idleTimer = window.setTimeout(() => {
    offers += 1;
    pose("wave");
    root.querySelector("#bot-nudge").hidden = false;
  }, IDLE_MS[Math.min(offers, IDLE_MS.length - 1)]);
}
function rankVoices(list) {
  return list.map((voice) => {
    const name = voice.name || "";
    let score = 1;
    if (/microsoft (david|zira|mark)\b/i.test(name)) score = -1;
    if (/natural|neural|premium|enhanced/i.test(name)) score += 80;
    if (/aria|jenny|guy/i.test(name)) score += 40;
    if (/google|samantha|daniel|karen/i.test(name)) score += 18;
    if (/^en/i.test(voice.lang || "")) score += 8;
    return { voice, score };
  }).filter((row) => row.score > 0).sort((a, b) => b.score - a.score).map((row) => row.voice);
}
function fillVoices() {
  if (!window.speechSynthesis) return;
  const voices = rankVoices(window.speechSynthesis.getVoices());
  voiceSel.replaceChildren();
  voices.forEach((voice) => {
    const opt = document.createElement("option");
    opt.value = voice.voiceURI;
    opt.textContent = voice.name;
    voiceSel.appendChild(opt);
  });
  if (!voices.length) {
    const opt = document.createElement("option");
    opt.textContent = "Browser default";
    voiceSel.appendChild(opt);
  }
}
function chosenVoice() {
  const voices = window.speechSynthesis ? window.speechSynthesis.getVoices() : [];
  return voices.find((voice) => voice.voiceURI === voiceSel.value) || rankVoices(voices)[0] || null;
}
function glowNav() {
  const hash = location.hash || "#/";
  document.querySelectorAll(".primary-nav a, .bottom-nav a").forEach((link) => {
    const href = link.getAttribute("href") || "";
    const on = href === hash || (hash.startsWith("#/lesson") && (link.id === "tour-learn" || link.id === "nav-learn")) || (hash.startsWith("#/track") && (link.id === "tour-learn" || link.id === "nav-learn"));
    link.classList.toggle("is-reading", on);
  });
}
function readingBlock(el) {
  const block = el.closest(".panel, .learn5, .eco-panel, .worked, .lesson-head, .uncertainty, #sec-figure, #sec-read, .hero-copy, .cheat-banner, .audio-dock, .who-band, .card");
  if (block) return block;
  const section = el.closest("section, article");
  if (section && section.id !== "view" && section.id !== "home" && section.id !== "main") return section;
  return el;
}
function clearSpoken() {
  document.querySelectorAll(".is-spoken").forEach((node) => node.classList.remove("is-spoken"));
  document.querySelectorAll(".is-reading-sec").forEach((node) => node.classList.remove("is-reading-sec"));
}
function highlightSentence(el, sentence) {
  clearSpoken();
  el.classList.add("is-spoken");
  readingBlock(el).classList.add("is-reading-sec");
  caption.hidden = false;
  caption.textContent = sentence;
  glowNav();
  const phone = window.matchMedia("(max-width: 700px)").matches;
  el.scrollIntoView({ block: phone ? "start" : "center", behavior: reduced() ? "auto" : "smooth" });
}
function collectSentences() {
  const scope = document.getElementById("view")?.hidden ? document.getElementById("home") : document.getElementById("view");
  const out = [];
  if (!scope) return out;
  scope.querySelectorAll("h1, h2, p, li").forEach((el) => {
    if (el.closest(".bot-root, .floor-menu, .site-footer, .tour, .bot-greet")) return;
    const text = (el.innerText || "").trim();
    if (text.length < 8) return;
    text.split(/(?<=[.!?])\s+/).forEach((sentence) => {
      const clean = sentence.trim();
      if (clean) out.push({ el, sentence: clean });
    });
  });
  return out;
}
function speakQueue(items) {
  if (!window.speechSynthesis) {
    sayLine("This browser has no speech synthesis. The text stays on the page.");
    return;
  }
  window.speechSynthesis.cancel();
  speaking = true;
  paused = false;
  pose("read");
  let index = 0;
  const next = () => {
    if (!speaking || index >= items.length) {
      speaking = false;
      pose("idle");
      caption.hidden = true;
      clearSpoken();
      return;
    }
    const item = items[index];
    highlightSentence(item.el, item.sentence);
    const utter = new SpeechSynthesisUtterance(item.sentence);
    utter.rate = Number(root.querySelector("#bot-rate").value) || 1;
    utter.pitch = Number(root.querySelector("#bot-pitch").value) || 1;
    const voice = chosenVoice();
    if (voice) utter.voice = voice;
    utter.onend = () => {
      index += 1;
      next();
    };
    window.speechSynthesis.speak(utter);
  };
  next();
}
function readAlong() {
  const items = collectSentences().slice(0, 24);
  if (!items.length) {
    sayLine("This room has no paragraph to read yet.");
    return;
  }
  speakQueue(items);
}
async function loadKb() {
  if (kb) return kb;
  const res = await fetch("data/guide-kb.json");
  if (!res.ok) throw new Error("guide notes");
  kb = await res.json();
  return kb;
}
function tokens(text) {
  return text.toLowerCase().split(/[^a-z0-9]+/).filter((word) => word.length > 2);
}
async function answer(question) {
  const route = ROUTES.find(([re]) => re.test(question.toLowerCase()));
  if (route && /^(go|open|show|take me|navigate)/i.test(question)) {
    location.hash = route[1] === "#listen" ? "#/" : route[1];
    if (route[1] === "#listen") sessionStorage.setItem("gccx-listen", "1");
    return "Opening that room. The export for it is on the download row.";
  }
  pose("think");
  const notes = await loadKb();
  const words = new Set(tokens(question));
  let best = null;
  let score = 0;
  const pages = notes.pages || notes.entries || [];
  const list = Array.isArray(pages) ? pages : [];
  const pool = list.length ? list : Object.values(notes).flat().filter((item) => item && item.answer);
  for (const item of pool) {
    const bag = tokens([item.title, item.answer, ...(item.keywords || []), ...(item.synonyms || [])].join(" "));
    let hit = 0;
    bag.forEach((word) => { if (words.has(word)) hit += 1; });
    if (hit > score) {
      score = hit;
      best = item;
    }
  }
  pose("idle");
  if (!best || score < 1) return "I don't have that in this lab's notes. Confirm before relying, and check the cited page.";
  return best.answer;
}
function exportChip() {
  const hash = location.hash || "#/";
  cards.replaceChildren();
  const make = (label, run) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = label;
    btn.addEventListener("click", run);
    cards.appendChild(btn);
  };
  if (hash.startsWith("#/downloads") || hash.startsWith("#/cheat")) make("Offline bundle", () => { location.href = "downloads/genesys-cx-offline-bundle.zip"; });
  else if (hash.startsWith("#/atlas") || hash.startsWith("#/flows")) make("Diagram downloads", () => { location.hash = "#/downloads"; });
  else make("Download this room", () => document.querySelector(".dl-mini[data-export='html']")?.click());
  make("Read along", () => readAlong());
}
function openPanel() {
  panel.hidden = false;
  root.classList.add("is-open");
  launcher.setAttribute("aria-expanded", "true");
  pose("wave");
  exportChip();
  if (!log.childElementCount) sayLine("Ask about a page in this lab. I will say when the notes do not have it.");
  input.focus();
}
function closePanel() {
  panel.hidden = true;
  panel.style.transform = "";
  root.classList.remove("is-open");
  launcher.setAttribute("aria-expanded", "false");
  pose("idle");
}
function goPath(kind) {
  dock();
  if (kind === "dock") return;
  if (kind === "ten") {
    location.hash = "#/track/foundations";
    sayLine("Ten-minute path: Foundations. Read the first lesson, then the quiz. Confirm before relying.");
  } else if (kind === "full") {
    location.hash = "#/tracks";
    sayLine("Full course: twenty tracks. Start at Foundations and follow the roadmap.");
  } else if (kind === "down") {
    location.hash = "#/downloads";
    sayLine("Downloads are on this page. The bundle is the zip.");
  }
  openPanel();
}
function wireDrag() {
  let startX = 0;
  let startY = 0;
  let baseL = 0;
  let baseT = 0;
  let dragged = false;
  launcher.addEventListener("pointerdown", (ev) => {
    if (ev.button !== 0) return;
    const rect = root.getBoundingClientRect();
    startX = ev.clientX;
    startY = ev.clientY;
    baseL = rect.left;
    baseT = rect.top;
    dragged = false;
    const move = (e) => {
      const dx = e.clientX - startX;
      const dy = e.clientY - startY;
      if (Math.abs(dx) + Math.abs(dy) < 8) return;
      dragged = true;
      const phone = window.matchMedia("(max-width: 700px)").matches;
      const bar = phone ? (parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--bar-h")) || 72) : 0;
      const tall = phone ? 72 : 168;
      root.style.left = Math.max(8, Math.min(window.innerWidth - (phone ? 72 : 148), baseL + dx)) + "px";
      root.style.top = Math.max(8, Math.min(window.innerHeight - tall - bar - 8, baseT + dy)) + "px";
      root.style.right = "auto";
      root.style.bottom = "auto";
    };
    const up = () => {
      window.removeEventListener("pointermove", move);
      window.removeEventListener("pointerup", up);
      if (dragged) {
        try { localStorage.setItem(POS_KEY, JSON.stringify({ left: root.style.left, top: root.style.top })); } catch (err) { /* storage off */ }
      } else if (panel.hidden) openPanel();
      else closePanel();
    };
    window.addEventListener("pointermove", move);
    window.addEventListener("pointerup", up);
  });
}
function wireMic() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) {
    micNote.textContent = "Type your question. This browser has no speech recognition.";
    return;
  }
  root.querySelector("#bot-mic").addEventListener("click", () => {
    if (recog) {
      recog.stop();
      return;
    }
    recog = new SR();
    recog.lang = "en-US";
    pose("listen");
    micNote.textContent = "Listening. If this fails, type the question.";
    recog.onresult = (ev) => {
      input.value = ev.results[0][0].transcript;
      form.requestSubmit();
    };
    recog.onerror = () => {
      micNote.textContent = "The microphone did not return text. Type the question.";
      pose("idle");
    };
    recog.onend = () => {
      recog = null;
      if (launcher.dataset.pose === "listen") pose("idle");
    };
    recog.start();
  });
}
function setAmbient(on) {
  if (!on) {
    if (ambient) {
      ambient.osc.forEach((node) => node.stop());
      ambient.ctx.close();
      ambient = null;
    }
    return;
  }
  const Ctx = window.AudioContext || window.webkitAudioContext;
  if (!Ctx) return;
  const ctx = new Ctx();
  const gain = ctx.createGain();
  gain.gain.value = 0.012;
  gain.connect(ctx.destination);
  const osc = [196, 247].map((freq) => {
    const node = ctx.createOscillator();
    node.type = "sine";
    node.frequency.value = freq;
    node.connect(gain);
    node.start();
    return node;
  });
  ambient = { ctx, osc };
}

launcher.addEventListener("click", (ev) => ev.preventDefault());
wireDrag();
wireMic();
root.querySelector("[data-bot-close]").addEventListener("click", closePanel);
root.querySelector("#bot-read").addEventListener("click", () => readAlong());
root.querySelector("#bot-pause").addEventListener("click", () => {
  if (!window.speechSynthesis) return;
  if (paused) {
    window.speechSynthesis.resume();
    paused = false;
    pose("read");
  } else {
    window.speechSynthesis.pause();
    paused = true;
  }
});
root.querySelector("#bot-stop").addEventListener("click", () => {
  speaking = false;
  paused = false;
  window.speechSynthesis?.cancel();
  caption.hidden = true;
  pose("idle");
});
root.querySelector("#bot-ambient").addEventListener("change", (ev) => setAmbient(ev.target.checked));
form.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  const q = input.value.trim();
  if (!q) return;
  sayLine(q);
  input.value = "";
  try {
    sayLine(await answer(q));
  } catch (err) {
    sayLine("The notes did not load. Confirm before relying.");
  }
  exportChip();
});
document.addEventListener("click", (ev) => {
  const btn = ev.target.closest("[data-path]");
  if (!btn || !btn.closest(".bot-greet, .bot-panel")) return;
  goPath(btn.dataset.path);
});
root.querySelector("#sheet-handle").addEventListener("pointerdown", (ev) => {
  if (!window.matchMedia("(max-width: 700px)").matches) return;
  const startY = ev.clientY;
  const move = (e) => {
    const dy = Math.max(0, e.clientY - startY);
    panel.style.transform = "translateY(" + dy + "px)";
  };
  const up = (e) => {
    window.removeEventListener("pointermove", move);
    window.removeEventListener("pointerup", up);
    panel.style.transform = "";
    if (e.clientY - startY > 72) closePanel();
  };
  window.addEventListener("pointermove", move);
  window.addEventListener("pointerup", up);
});
root.querySelector("#bot-nudge").addEventListener("click", (ev) => {
  const btn = ev.target.closest("[data-nudge]");
  if (!btn) return;
  root.querySelector("#bot-nudge").hidden = true;
  if (btn.dataset.nudge === "stop") {
    try { localStorage.setItem(STOP_KEY, "1"); } catch (err) { /* storage off */ }
    offers = OFFER_MAX;
    return;
  }
  if (btn.dataset.nudge === "help") openPanel();
  armIdle();
});
document.getElementById("tour-next").addEventListener("click", () => {
  if (stepIndex >= STEPS.length - 1) endTour(false);
  else {
    stepIndex += 1;
    showStep();
  }
});
document.getElementById("tour-back").addEventListener("click", () => {
  if (stepIndex === 0) return;
  stepIndex -= 1;
  showStep();
});
document.getElementById("tour-skip").addEventListener("click", () => endTour(true));
window.addEventListener("resize", () => { if (!tour.hidden) showStep(); lift(); });
window.addEventListener("scroll", lift, { passive: true });
document.getElementById("nav-guide")?.addEventListener("click", () => { panel.hidden ? openPanel() : closePanel(); });
document.addEventListener("click", (ev) => {
  if (ev.target.closest("[data-replay-tour]")) {
    try { localStorage.removeItem(TOUR_KEY); } catch (err) { /* storage off */ }
    startTour();
  }
});
["pointerdown", "keydown"].forEach((name) => window.addEventListener(name, () => {
  if (root.querySelector("#bot-nudge").hidden) armIdle();
}, { passive: true }));
window.addEventListener("hashchange", () => { glowNav(); exportChip(); });
if (window.speechSynthesis) {
  fillVoices();
  window.speechSynthesis.addEventListener("voiceschanged", fillVoices);
}
window.addEventListener("load", () => {
  restorePos();
  lift();
  glowNav();
  if (reduced()) launcher.classList.add("is-still");
  if (!localStorage.getItem(TOUR_KEY)) startTour();
  else dock();
  armIdle();
});
window.gccxGuide = { startTour, readAlong, openPanel };
