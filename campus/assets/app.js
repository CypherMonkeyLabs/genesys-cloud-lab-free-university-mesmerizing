const SETTINGS_KEY = "gccx-settings";
const PROGRESS_KEY = "gccx-progress";

const state = {
  manifest: null,
  reference: null,
  tracks: new Map(),
  settings: loadSettings(),
  progress: loadProgress(),
  timers: [],
  audio: null
};

const $ = (sel, root = document) => root.querySelector(sel);
const homeEl = $("#home");
const viewEl = $("#view");
const railEl = $("#rail");
const statusEl = $("#status");

applySettings(state.settings);
bindChrome();
window.addEventListener("hashchange", () => render());
init().catch((err) => showFatal(err));

async function init() {
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("./sw.js").catch(() => {});
  }
  state.manifest = await fetchJson("data/manifest.json");
  paintRail();
  paintHomeStats();
  await prepareVoices();
  render();
}

function fetchJson(url) {
  return fetch(url).then((res) => {
    if (!res.ok) throw new Error("Could not load " + url);
    return res.json();
  });
}

function loadSettings() {
  const base = {
    theme: document.documentElement.dataset.theme || "night",
    font: document.documentElement.dataset.font || "md",
    sound: true,
    narrate: false,
    rate: 1,
    voiceURI: "",
    reduce: document.documentElement.dataset.reduce === "1"
  };
  try {
    return Object.assign(base, JSON.parse(localStorage.getItem(SETTINGS_KEY) || "{}"));
  } catch (e) {
    return base;
  }
}

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{"lessons":{}}');
  } catch (e) {
    return { lessons: {} };
  }
}

function saveSettings() {
  localStorage.setItem(SETTINGS_KEY, JSON.stringify(state.settings));
  applySettings(state.settings);
}

function saveProgress() {
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(state.progress));
  paintHomeStats();
}

function applySettings(s) {
  document.documentElement.dataset.theme = s.theme || "night";
  document.documentElement.dataset.font = s.font || "md";
  document.documentElement.dataset.reduce = s.reduce ? "1" : "0";
  const themeColor = getComputedStyle(document.documentElement).getPropertyValue("--cc-bg").trim();
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta && themeColor) meta.content = themeColor;
}

function lessonProg(id) {
  if (!state.progress.lessons[id]) state.progress.lessons[id] = { best: 0, lab: {}, done: false };
  return state.progress.lessons[id];
}

function stopRuntime() {
  state.timers.forEach((id) => clearInterval(id));
  state.timers = [];
  if (window.speechSynthesis) window.speechSynthesis.cancel();
}

function say(text) {
  if (!state.settings.narrate || !window.speechSynthesis || !text) return;
  const synth = window.speechSynthesis;
  const utter = new SpeechSynthesisUtterance(text);
  utter.rate = Number(state.settings.rate) || 1;
  const voices = synth.getVoices();
  const chosen = voices.find((v) => v.voiceURI === state.settings.voiceURI);
  if (chosen) utter.voice = chosen;
  else return;
  synth.cancel();
  synth.speak(utter);
}

function prepareVoices() {
  return new Promise((resolve) => {
    if (!window.speechSynthesis) return resolve([]);
    const synth = window.speechSynthesis;
    const finish = () => {
      const voices = rankVoices(synth.getVoices());
      if (!state.settings.voiceURI && voices[0]) state.settings.voiceURI = voices[0].voiceURI;
      if (state.settings.voiceURI && !voices.some((v) => v.voiceURI === state.settings.voiceURI)) {
        state.settings.voiceURI = voices[0] ? voices[0].voiceURI : "";
      }
      resolve(voices);
    };
    const existing = synth.getVoices();
    if (existing.length) return finish();
    synth.addEventListener("voiceschanged", finish, { once: true });
    setTimeout(finish, 1200);
  });
}

function rankVoices(list) {
  return list
    .map((v) => ({ v, score: voiceScore(v) }))
    .filter((row) => row.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((row) => row.v);
}

function voiceScore(v) {
  const name = v.name || "";
  if (/microsoft (david|zira|mark)\b/i.test(name)) return -1;
  if (/desktop/i.test(name) && /microsoft/i.test(name)) return -1;
  let score = 1;
  if (/natural|neural|premium|enhanced/i.test(name)) score += 50;
  if (/samantha|daniel|karen|moira|serena|fiona|google/i.test(name)) score += 15;
  if (/^en/i.test(v.lang || "")) score += 8;
  return score;
}

function blip(freq = 520, dur = 0.06) {
  if (!state.settings.sound) return;
  const Ctx = window.AudioContext || window.webkitAudioContext;
  if (!Ctx) return;
  if (!state.audio) state.audio = new Ctx();
  const ctx = state.audio;
  if (ctx.state === "suspended") ctx.resume();
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();
  osc.frequency.value = freq;
  osc.type = "sine";
  gain.gain.setValueAtTime(0.0001, ctx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.05, ctx.currentTime + 0.01);
  gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + dur);
  osc.connect(gain).connect(ctx.destination);
  osc.start();
  osc.stop(ctx.currentTime + dur + 0.02);
}

function bindChrome() {
  $("#search-form").addEventListener("submit", (ev) => {
    ev.preventDefault();
    const q = $("#q").value.trim();
    location.hash = "#/search?q=" + encodeURIComponent(q);
  });
  $("#open-tracks").addEventListener("click", () => railEl.classList.toggle("open"));
  $("#nav-learn").addEventListener("click", () => {
    if (window.matchMedia("(max-width: 980px)").matches) {
      railEl.classList.toggle("open");
    }
  });
  document.body.addEventListener("click", (ev) => {
    const a = ev.target.closest("a[href^='#/']");
    if (a) railEl.classList.remove("open");
  });
}

function parseRoute() {
  const raw = (location.hash || "#/").replace(/^#/, "");
  const [path, qs] = raw.split("?");
  const parts = path.split("/").filter(Boolean);
  return { parts, query: new URLSearchParams(qs || "") };
}

function setCurrent(hashPrefix) {
  document.querySelectorAll(".bottom-nav a, .rail a").forEach((a) => {
    const href = a.getAttribute("href") || "";
    const on = hashPrefix && href === hashPrefix;
    if (on) a.setAttribute("aria-current", "page");
    else a.removeAttribute("aria-current");
  });
}

async function render() {
  stopRuntime();
  const route = parseRoute();
  const [head, id] = route.parts;
  status("Loading");
  try {
    if (!head) return showHome();
    if (head === "tracks") return showTracks();
    if (head === "track" && id) return showTrack(id);
    if (head === "lesson" && id) return showLesson(id);
    if (head === "studio") return showStudio(id || "");
    if (head === "topology") return showTopology();
    if (head === "glossary") return showGlossary();
    if (head === "certs") return showCerts();
    if (head === "ecosystem") return showEcosystem();
    if (head === "boss") return showBoss(id || "");
    if (head === "interview") return showInterview();
    if (head === "settings") return showSettings();
    if (head === "search") return showSearch(route.query.get("q") || "");
    showMissing();
  } catch (err) {
    showFatal(err);
  }
}

function showHome() {
  homeEl.hidden = false;
  viewEl.hidden = true;
  document.title = "Genesys Cloud CX Lab";
  setCurrent("#/");
  paintHomeStats();
  const host = $("#home-dynamic");
  host.innerHTML = `
    <h2>Studios</h2>
    <div class="grid">${studioCards()}</div>
    <h2>Tracks</h2>
    <div class="grid">${state.manifest.tracks.map(trackCard).join("")}</div>`;
  status("Home");
}

function showTracks() {
  mount(`<p class="kicker">Curriculum</p><h1>Tracks</h1><p>Sixteen paths from organization setup through migration. Open one track at a time.</p><div class="grid">${state.manifest.tracks.map(trackCard).join("")}</div>`);
  setCurrent("#/tracks");
}

async function showTrack(id) {
  const track = await loadTrack(id);
  if (!track) return showMissing();
  const items = track.lessons.map((lesson, index) => {
    const prog = state.progress.lessons[lesson.id];
    const mark = prog && prog.done ? "Finished" : "Open";
    return `<a class="card" href="#/lesson/${lesson.id}"><div class="stripe a${track.accent}"></div><p class="kicker">${track.title} · ${index + 1}</p><h3>${esc(lesson.title)}</h3><p>${esc(lesson.summary)}</p><p class="muted">${esc(lesson.level)} · ${lesson.minutes} min · ${mark}</p></a>`;
  }).join("");
  mount(`<p class="kicker">${esc(track.kicker)}</p><h1>${esc(track.title)}</h1><p>${esc(track.summary)}</p><div class="grid">${items}</div>`);
  document.title = track.title + " · Genesys Cloud CX Lab";
  setCurrent("#/track/" + id);
}

async function showLesson(id) {
  const stub = findLesson(id);
  if (!stub) return showMissing();
  const track = await loadTrack(stub.trackId);
  const lesson = track.lessons.find((item) => item.id === id);
  mount(renderLesson(track, lesson));
  wireLesson(lesson);
  document.title = lesson.title + " · Genesys Cloud CX Lab";
  setCurrent("#/lesson/" + id);
  if (state.settings.narrate) say(lesson.summary);
}

function renderLesson(track, lesson) {
  const cites = lesson.cites.map((cite) => `<li><a href="${esc(cite.url)}" rel="noopener noreferrer">${esc(cite.title)}</a></li>`).join("");
  const paras = lesson.paras.map((p) => `<p>${esc(p)}</p>`).join("");
  const uncertainty = lesson.uncertainty ? `<aside class="uncertainty"><strong>Confirm on the vendor page. </strong>${esc(lesson.uncertainty)}</aside>` : "";
  return `
    <p class="kicker"><a href="#/track/${track.id}">${esc(track.title)}</a> · ${esc(lesson.level)} · ${lesson.minutes} min</p>
    <div class="lesson-head"><h1>${esc(lesson.title)}</h1></div>
    <p class="lede">${esc(lesson.summary)}</p>
    ${figureSvg(lesson.figure)}
    ${paras}
    ${uncertainty}
    <h2>Sources</h2>
    <ul>${cites}</ul>
    <h2>Step-through</h2>
    <div class="panel" id="flow-player">${flowPlayer(lesson.flow)}</div>
    <h2>Quiz</h2>
    <div class="panel" id="quiz">${quizShell(lesson)}</div>
    <h2>Flashcards</h2>
    <div class="panel" id="cards">${cardShell(lesson)}</div>
    <h2>Lab</h2>
    <div class="panel">${labShell(lesson)}</div>
    <h2>Fault and fix</h2>
    <div class="panel">${faultShell(lesson)}</div>
    <p><a class="btn" href="#/track/${track.id}">Back to ${esc(track.title)}</a></p>`;
}

function figureSvg(fig) {
  const w = 640;
  const h = 280;
  const nodes = fig.nodes.map((node) => {
    const x = (node.x / 100) * (w - 80) + 40;
    const y = (node.y / 100) * (h - 70) + 28;
    return { ...node, x, y };
  });
  const byId = Object.fromEntries(nodes.map((node) => [node.id, node]));
  const colors = { carrier: "#ff5a36", trunk: "#8fd4ff", edge: "#d6f25c", region: "#b3a6ff", architect: "#d6f25c", queue: "#ff5a36", agent: "#8fd4ff", bot: "#b3a6ff", wem: "#d6f25c", crm: "#ff5a36", phone: "#8fd4ff" };
  const lines = fig.edges.map((edge) => {
    const a = byId[edge.a];
    const b = byId[edge.b];
    if (!a || !b) return "";
    return `<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="currentColor" stroke-opacity="0.45" stroke-width="2"/>`;
  }).join("");
  const dots = nodes.map((node) => {
    const fill = colors[node.kind] || "#ff5a36";
    return `<g><rect x="${node.x - 54}" y="${node.y - 18}" width="108" height="36" rx="12" fill="${fill}"/><text x="${node.x}" y="${node.y + 4}" text-anchor="middle" font-size="12" font-family="Palatino, Georgia, serif" fill="#1a0c08">${esc(node.label)}</text></g>`;
  }).join("");
  return `<figure><svg viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(fig.caption)}">${lines}${dots}</svg><figcaption>${esc(fig.caption)}</figcaption></figure>`;
}

function flowPlayer(flow) {
  const rows = flow.steps.map((step, index) => `
    <div class="step" data-step="${index}">
      <div class="party">${esc(step.from)}</div>
      <div><div class="wire"></div><strong>${esc(step.title)}</strong><div class="muted">${esc(step.detail)}</div></div>
      <div class="party">${esc(step.to)}</div>
    </div>`).join("");
  return `<h3>${esc(flow.title)}</h3>
    <div class="toolbar" role="group" aria-label="Flow controls">
      <button class="btn tiny" type="button" id="flow-play">Play</button>
      <button class="btn tiny" type="button" id="flow-pause">Pause</button>
      <button class="btn tiny" type="button" id="flow-step">Step</button>
      <button class="btn tiny" type="button" id="flow-inspect">Inspect</button>
    </div>
    <div class="ladder" id="ladder">${rows}</div>
    <pre id="inspect" hidden></pre>`;
}

function wireLesson(lesson) {
  const steps = lesson.flow.steps;
  let index = -1;
  let timer = null;
  const nodes = [...viewEl.querySelectorAll(".step")];
  const inspect = $("#inspect", viewEl);
  const show = (i) => {
    index = i;
    nodes.forEach((node, n) => node.classList.toggle("is-on", n === i));
    if (inspect && !inspect.hidden) inspect.textContent = steps[i] ? steps[i].inspect : "";
    blip(440 + i * 30, 0.05);
    if (state.settings.narrate && steps[i]) say(steps[i].title + ". " + steps[i].detail);
  };
  const stepOnce = () => show((index + 1) % steps.length);
  $("#flow-step", viewEl).addEventListener("click", stepOnce);
  $("#flow-play", viewEl).addEventListener("click", () => {
    if (timer) return;
    stepOnce();
    timer = setInterval(stepOnce, state.settings.reduce ? 1400 : 1600);
    state.timers.push(timer);
  });
  $("#flow-pause", viewEl).addEventListener("click", () => {
    if (timer) clearInterval(timer);
    timer = null;
  });
  $("#flow-inspect", viewEl).addEventListener("click", () => {
    if (index < 0) show(0);
    inspect.hidden = false;
    inspect.textContent = steps[index].inspect;
  });

  const quiz = lesson.quiz;
  let qIndex = 0;
  let correct = 0;
  const host = $("#quiz", viewEl);
  const drawQ = () => {
    const item = quiz[qIndex];
    host.innerHTML = `<p>Question ${qIndex + 1} of ${quiz.length}</p><h3>${esc(item.q)}</h3>` +
      item.choices.map((choice, i) => `<button class="btn choice" type="button" data-choice="${i}">${esc(choice)}</button>`).join("");
    host.querySelectorAll("[data-choice]").forEach((btn) => btn.addEventListener("click", () => {
      const pick = Number(btn.dataset.choice);
      const good = pick === item.answer;
      if (good) correct += 1;
      blip(good ? 660 : 220, 0.08);
      host.querySelectorAll("[data-choice]").forEach((el) => {
        el.disabled = true;
        const n = Number(el.dataset.choice);
        if (n === item.answer) el.classList.add("good");
        else if (n === pick) el.classList.add("bad");
      });
      host.insertAdjacentHTML("beforeend", `<p><strong>${good ? "Correct." : "Not this one."}</strong> ${esc(item.why)}</p><button class="btn primary" type="button" id="quiz-next">${qIndex + 1 === quiz.length ? "See score" : "Next"}</button>`);
      $("#quiz-next", host).addEventListener("click", () => {
        if (qIndex + 1 === quiz.length) {
          const prog = lessonProg(lesson.id);
          prog.best = Math.max(prog.best || 0, correct);
          if (correct >= 5) prog.done = true;
          saveProgress();
          host.innerHTML = `<h3>${correct} of ${quiz.length}</h3><p>${correct >= 5 ? "This lesson counts as finished." : "Five correct marks the lesson finished. You can retake it."}</p><button class="btn" type="button" id="quiz-retry">Retry</button>`;
          $("#quiz-retry", host).addEventListener("click", () => { qIndex = 0; correct = 0; drawQ(); });
        } else {
          qIndex += 1;
          drawQ();
        }
      });
    }));
  };
  drawQ();

  let card = 0;
  let flipped = false;
  const cards = $("#cards", viewEl);
  const drawCard = () => {
    const item = lesson.cards[card];
    cards.innerHTML = `<p>${card + 1} of ${lesson.cards.length}</p><button class="flip" type="button" id="flip">${flipped ? esc(item.back) : esc(item.front)}</button><div class="toolbar"><button class="btn tiny" type="button" id="card-prev">Previous</button><button class="btn tiny" type="button" id="card-next">Next</button></div>`;
    $("#flip", cards).addEventListener("click", () => { flipped = !flipped; drawCard(); });
    $("#card-prev", cards).addEventListener("click", () => { card = (card + lesson.cards.length - 1) % lesson.cards.length; flipped = false; drawCard(); });
    $("#card-next", cards).addEventListener("click", () => { card = (card + 1) % lesson.cards.length; flipped = false; drawCard(); });
  };
  drawCard();

  viewEl.querySelectorAll("[data-lab]").forEach((box) => {
    const prog = lessonProg(lesson.id);
    const key = box.dataset.lab;
    box.checked = Boolean(prog.lab[key]);
    box.addEventListener("change", () => {
      prog.lab[key] = box.checked;
      const all = [...viewEl.querySelectorAll("[data-lab]")].every((el) => el.checked);
      if (all && (prog.best || 0) >= 5) prog.done = true;
      saveProgress();
    });
  });
}

function quizShell() {
  return `<p>Loading question.</p>`;
}
function cardShell() {
  return `<p>Loading card.</p>`;
}
function labShell(lesson) {
  const steps = lesson.lab.steps.map((step, i) => `<label class="choice"><input type="checkbox" data-lab="${i}"> <span>${esc(step)}</span></label>`).join("");
  return `<h3>${esc(lesson.lab.title)}</h3>${steps}<p class="muted">${esc(lesson.lab.success)}</p>`;
}
function faultShell(lesson) {
  const fault = lesson.fault;
  return `<h3>${esc(fault.title)}</h3><p>${esc(fault.symptom)}</p><pre>${esc(fault.log)}</pre><details><summary>Cause</summary><p>${esc(fault.cause)}</p></details><details><summary>Fix</summary><p>${esc(fault.fix)}</p></details>`;
}

function showStudio(id) {
  if (!id) {
    mount(`<p class="kicker">Interactive</p><h1>Studios</h1><p>Builders and simulators. They stay in the browser. Nothing here calls a live Genesys organization.</p><div class="grid">${studioCards()}</div>`);
    setCurrent("#/studio");
    return;
  }
  mount(`<p class="kicker">Studio</p><h1 id="studio-title">Opening studio</h1><div id="studio-root"></div>`);
  setCurrent("#/studio/" + id);
  import("./studios.js").then((mod) => mod.mountStudio(id, $("#studio-root"), {
    settings: state.settings,
    blip,
    say,
    manifest: state.manifest,
    setTitle: (title) => {
      $("#studio-title").textContent = title;
      document.title = title + " · Genesys Cloud CX Lab";
    }
  })).catch((err) => showFatal(err));
}

async function showTopology() {
  mount(`<p class="kicker">Topology</p><h1>Cloud floor</h1><p>Core region, BYOC, the Edge, Architect, ACD, and the systems beside the conversation. Toggle a failure to see which path drops.</p><div id="topo-root"></div>`);
  document.title = "Topology · Genesys Cloud CX Lab";
  setCurrent("#/topology");
  const mod = await import("./topology.js");
  mod.mountTopology($("#topo-root"), { reduce: state.settings.reduce });
}

async function showGlossary() {
  const ref = await loadReference();
  const rows = ref.glossary.map((item) => `<article class="card"><h3>${esc(item.term)}</h3><p>${esc(item.def)}</p><p><a href="${esc(item.url)}">${esc(item.source)}</a></p></article>`).join("");
  mount(`<p class="kicker">Ecosystem</p><h1>Glossary</h1><div class="grid">${rows}</div>`);
  document.title = "Glossary · Genesys Cloud CX Lab";
}

async function showCerts() {
  const ref = await loadReference();
  const cards = ref.certs.map((cert) => `<article class="card"><div class="stripe"></div><h3>${esc(cert.name)}</h3><p>${esc(cert.detail)}</p><p><a href="${esc(cert.url)}">Catalog entry</a></p></article>`).join("");
  mount(`<p class="kicker">Genesys Education</p><h1>Certifications</h1><aside class="uncertainty">${esc(ref.certNote)}</aside><div class="grid">${cards}</div>`);
  document.title = "Certifications · Genesys Cloud CX Lab";
}

function showEcosystem() {
  const tracks = state.manifest.tracks.map((track) => `<a class="card" href="#/track/${track.id}"><div class="stripe a${track.accent}"></div><h3>${esc(track.title)}</h3><p>${esc(track.summary)}</p></a>`).join("");
  mount(`<p class="kicker">Map</p><h1>Ecosystem</h1>
    <p>Genesys Cloud CX is the conversation platform. WEM, recording, emergency calling, CRM, and bots sit on documented edges of that platform.</p>
    <div class="toolbar">
      <a class="btn" href="#/glossary">Glossary</a>
      <a class="btn" href="#/certs">Certifications</a>
      <a class="btn" href="#/interview">Interview drill</a>
      <a class="btn" href="#/boss">Boss incidents</a>
      <a class="btn" href="#/topology">3D topology</a>
    </div>
    <h2>Sister systems inside the tracks</h2>
    <div class="grid">${tracks}</div>`);
  document.title = "Ecosystem · Genesys Cloud CX Lab";
}

async function showBoss(id) {
  const ref = await loadReference();
  if (!id) {
    const cards = ref.bosses.map((boss) => `<a class="card" href="#/boss/${boss.id}"><p class="kicker">${esc(boss.severity)}</p><h3>${esc(boss.title)}</h3><p>${esc(boss.brief)}</p></a>`).join("");
    mount(`<p class="kicker">On call</p><h1>Boss incidents</h1><p>Synthetic logs use documentation addresses from RFC 5737. They are not captures from a customer org.</p><div class="grid">${cards}</div>`);
    return;
  }
  const boss = ref.bosses.find((item) => item.id === id);
  if (!boss) return showMissing();
  mount(`<p class="kicker">${esc(boss.severity)}</p><h1>${esc(boss.title)}</h1><p>${esc(boss.brief)}</p><div id="boss-root"></div><p><a href="#/boss">All incidents</a></p>`);
  wireBoss(boss);
  document.title = boss.title + " · Genesys Cloud CX Lab";
}

function wireBoss(boss) {
  const root = $("#boss-root");
  let step = 0;
  const draw = () => {
    const item = boss.steps[step];
    root.innerHTML = `<pre>${esc(item.log)}</pre><h2>${esc(item.ask)}</h2>` +
      item.choices.map((choice, i) => `<button class="btn choice" type="button" data-choice="${i}">${esc(choice)}</button>`).join("");
    root.querySelectorAll("[data-choice]").forEach((btn) => btn.addEventListener("click", () => {
      const pick = Number(btn.dataset.choice);
      const good = pick === item.answer;
      blip(good ? 700 : 180, 0.08);
      root.insertAdjacentHTML("beforeend", `<p><strong>${good ? "That matches the log." : "Look again."}</strong> ${esc(item.why)}</p>`);
      if (!good) return;
      if (step + 1 < boss.steps.length) {
        root.insertAdjacentHTML("beforeend", `<button class="btn primary" type="button" id="boss-next">Next evidence</button>`);
        $("#boss-next").addEventListener("click", () => { step += 1; draw(); });
      } else {
        root.insertAdjacentHTML("beforeend", `<h2>Fix</h2><p>${esc(boss.fix)}</p><p><a href="${esc(boss.url)}">${esc(boss.source)}</a></p>`);
      }
    }));
  };
  draw();
}

async function showInterview() {
  const ref = await loadReference();
  const items = ref.interviews.map((item, i) => `<article class="card"><h3>${esc(item.q)}</h3><details><summary>Model answer</summary><p>${esc(item.a)}</p><p><a href="${esc(item.url)}">${esc(item.source)}</a></p></details></article>`).join("");
  mount(`<p class="kicker">Practice</p><h1>Interview drill</h1><p>${ref.interviews.length} questions a hiring panel actually asks an implementation engineer. Open an answer only after you try it.</p><div class="grid">${items}</div>`);
  document.title = "Interview drill · Genesys Cloud CX Lab";
}

function showSettings() {
  const s = state.settings;
  mount(`<p class="kicker">Local only</p><h1>Settings</h1>
    <form id="settings-form" class="panel">
      <fieldset><legend>Theme</legend>
        ${["night", "paper", "harbor", "contrast"].map((theme) => `<label class="choice"><input type="radio" name="theme" value="${theme}" ${s.theme === theme ? "checked" : ""}> ${theme}</label>`).join("")}
      </fieldset>
      <label>Font size <select name="font">${["sm", "md", "lg", "xl"].map((size) => `<option ${s.font === size ? "selected" : ""}>${size}</option>`).join("")}</select></label>
      <label class="choice"><input type="checkbox" name="sound" ${s.sound ? "checked" : ""}> Sound effects</label>
      <label class="choice"><input type="checkbox" name="narrate" ${s.narrate ? "checked" : ""}> Narration</label>
      <label>Voice <select name="voiceURI" id="voice-select"></select></label>
      <p class="muted" id="voice-note"></p>
      <label>Narration speed <input name="rate" type="range" min="0.8" max="1.3" step="0.05" value="${s.rate}"></label>
      <label class="choice"><input type="checkbox" name="reduce" ${s.reduce ? "checked" : ""}> Reduced motion</label>
      <div class="toolbar"><button class="btn primary" type="submit">Save</button><button class="btn" type="button" id="offline">Cache tracks for offline</button><button class="btn" type="button" id="reset-progress">Reset progress</button></div>
      <p class="muted">Settings and progress stay in this browser. Narration uses the Web Speech API and waits for voiceschanged. Robotic Microsoft David, Zira, and Mark voices are never selected.</p>
    </form>`);
  const select = $("#voice-select");
  const voices = window.speechSynthesis ? rankVoices(window.speechSynthesis.getVoices()) : [];
  if (!voices.length) {
    select.innerHTML = `<option value="">No high-quality voice yet</option>`;
    $("#voice-note").textContent = "No natural or enhanced voice is available. Narration stays silent rather than using a robotic desktop voice.";
  } else {
    select.innerHTML = voices.map((voice) => `<option value="${esc(voice.voiceURI)}" ${voice.voiceURI === s.voiceURI ? "selected" : ""}>${esc(voice.name)} (${esc(voice.lang)})</option>`).join("");
  }
  $("#settings-form").addEventListener("submit", (ev) => {
    ev.preventDefault();
    const data = new FormData(ev.target);
    state.settings.theme = data.get("theme");
    state.settings.font = data.get("font");
    state.settings.sound = data.get("sound") === "on";
    state.settings.narrate = data.get("narrate") === "on";
    state.settings.reduce = data.get("reduce") === "on";
    state.settings.rate = Number(data.get("rate"));
    state.settings.voiceURI = data.get("voiceURI") || "";
    saveSettings();
    blip(520, 0.07);
    status("Settings saved");
  });
  $("#offline").addEventListener("click", cacheAll);
  $("#reset-progress").addEventListener("click", () => {
    state.progress = { lessons: {} };
    saveProgress();
    status("Progress cleared");
  });
  document.title = "Settings · Genesys Cloud CX Lab";
  setCurrent("#/settings");
}

async function cacheAll() {
  if (!("caches" in window)) return status("Cache API unavailable");
  const cache = await caches.open("gccx-lab-v1");
  const urls = ["index.html", "assets/app.js", "assets/studios.js", "assets/topology.js", "assets/routing-model.js", "data/manifest.json", "data/reference.json", "manifest.webmanifest"];
  state.manifest.tracks.forEach((track) => urls.push(track.file));
  await cache.addAll(urls.map((url) => new URL(url, location.href).toString()));
  status("Tracks cached for offline use");
}

function showSearch(q) {
  const needle = q.trim().toLowerCase();
  const hits = [];
  state.manifest.tracks.forEach((track) => {
    track.lessons.forEach((lesson) => {
      const blob = (lesson.title + " " + lesson.summary).toLowerCase();
      if (!needle || blob.includes(needle)) hits.push({ track, lesson });
    });
  });
  const cards = hits.slice(0, 40).map(({ track, lesson }) => `<a class="card" href="#/lesson/${lesson.id}"><p class="kicker">${esc(track.title)}</p><h3>${esc(lesson.title)}</h3><p>${esc(lesson.summary)}</p></a>`).join("");
  mount(`<p class="kicker">Search</p><h1>${needle ? "Results" : "Browse lessons"}</h1><p>${hits.length} lesson${hits.length === 1 ? "" : "s"}${needle ? " for “" + esc(q) + "”" : ""}.</p><div class="grid">${cards || "<p>No lesson title or summary uses that phrase.</p>"}</div>`);
  document.title = "Search · Genesys Cloud CX Lab";
}

function showMissing() {
  mount(`<h1>That path is not on the floor</h1><p>The lab can take you back to a real view.</p><p><a class="btn primary" href="#/">Home</a> <a class="btn" href="#/tracks">Tracks</a></p>`);
  document.title = "Not found · Genesys Cloud CX Lab";
}

function showFatal(err) {
  mount(`<h1>The lab could not load this view</h1><p>${esc(err.message || String(err))}</p><p><button class="btn" type="button" id="retry">Retry</button></p>`);
  $("#retry").addEventListener("click", () => render());
  status(err.message || "Error");
}

function mount(html) {
  homeEl.hidden = true;
  viewEl.hidden = false;
  viewEl.innerHTML = html;
  status("Ready");
}

function status(text) {
  statusEl.textContent = text;
}

function paintRail() {
  const links = state.manifest.tracks.map((track) => `<a href="#/track/${track.id}">${esc(track.title)} <span class="muted">${track.lessons.length}</span></a>`).join("");
  railEl.innerHTML = `<h2>Floor</h2><a href="#/">Home</a><a href="#/studio">Studios</a><a href="#/topology">3D topology</a><a href="#/ecosystem">Ecosystem</a><a href="#/certs">Certifications</a><a href="#/boss">Boss incidents</a><h2>Tracks</h2>${links}`;
}

function paintHomeStats() {
  if (!state.manifest) return;
  const lessons = state.manifest.tracks.reduce((sum, track) => sum + track.lessons.length, 0);
  $("#stat-tracks").textContent = String(state.manifest.tracks.length);
  $("#stat-lessons").textContent = String(lessons);
  $("#stat-quiz").textContent = String(state.manifest.quizCount);
  const done = Object.values(state.progress.lessons).filter((item) => item.done).length;
  $("#stat-done").textContent = String(done);
}

function trackCard(track) {
  return `<a class="card" href="#/track/${track.id}"><div class="stripe a${track.accent}"></div><p class="kicker">${esc(track.kicker)}</p><h3>${esc(track.title)}</h3><p>${esc(track.summary)}</p><p class="muted">${track.lessons.length} lessons</p></a>`;
}

function studioCards() {
  return state.manifest.studios.map((studio) => `<a class="card" href="#/studio/${studio.id}"><div class="stripe a${studio.accent}"></div><h3>${esc(studio.title)}</h3><p>${esc(studio.summary)}</p></a>`).join("");
}

function findLesson(id) {
  for (const track of state.manifest.tracks) {
    if (track.lessons.some((lesson) => lesson.id === id)) return { trackId: track.id };
  }
  return null;
}

async function loadTrack(id) {
  if (state.tracks.has(id)) return state.tracks.get(id);
  const meta = state.manifest.tracks.find((track) => track.id === id);
  if (!meta) return null;
  const track = await fetchJson(meta.file);
  state.tracks.set(id, track);
  return track;
}

async function loadReference() {
  if (state.reference) return state.reference;
  state.reference = await fetchJson("data/reference.json");
  return state.reference;
}

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
}
