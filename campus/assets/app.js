import { mountMascot } from "./mascot.js";
import { attachSources } from "./sources.js";
import { applyLang, pack, LANGS } from "./i18n.js";
import { isoIcon, iconForTrack } from "./icons3d.js";
import { heading } from "./headings.js";
import { ensureLightbox } from "./lightbox.js";

const SETTINGS_KEY = "gccx-settings";
const PROGRESS_KEY = "gccx-progress";
const THEMES = ["bloom", "neon", "holographic", "cyberpunk", "sunset", "light", "futuristic", "gaming", "night", "contrast"];
const EXTRA = ["atlas", "ports", "game", "map", "sandbox", "daily", "badges", "cheat", "downloads", "flows", "charts", "play", "roadmap", "security", "career", "whats-new", "playbooks", "deploy", "architecture", "reporting", "regions", "help", "legal"];
const CRUMB = {
  atlas: "Diagrams",
  flows: "Flows",
  charts: "Charts",
  cheat: "Cheat Codes",
  downloads: "Downloads",
  play: "Play",
  career: "Careers",
  ecosystem: "Ecosystem",
  ports: "Ports",
  game: "Play",
  map: "Flows",
  sandbox: "Play",
  daily: "Play",
  badges: "Play",
  roadmap: "Roadmap",
  security: "Security",
  "whats-new": "What’s new",
  help: "Help",
  legal: "Legal",
  playbooks: "Playbooks",
  deploy: "Deployment",
  architecture: "Architecture",
  reporting: "Reporting",
  regions: "Regions"
};

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
window.gccxSettings = {
  patch(partial) {
    Object.assign(state.settings, partial);
    saveSettings();
  },
  get() {
    return state.settings;
  }
};
bindChrome();
window.addEventListener("hashchange", () => render());
init().catch((err) => showFatal(err));

async function init() {
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("./sw.js", { scope: "./" }).catch(() => {});
  }
  state.manifest = await fetchJson("data/manifest.json");
  ensureLightbox();
  syncChrome();
  paintRail();
  paintHomeStats();
  mountMascot(document.querySelector("#mascot-slot"));
  bindDeskAudio();
  await prepareVoices();
  render();
}

function bindDeskAudio() {
  document.querySelectorAll("#clip-tour, #clip-practice").forEach((audio) => {
    audio.addEventListener("error", () => {
      const src = audio.getAttribute("src");
      if (!src || audio.dataset.fallback === "1") {
        if (!audio.nextElementSibling?.classList.contains("clip-missing")) {
          const note = document.createElement("span");
          note.className = "muted clip-missing";
          note.textContent = " This clip did not load. The written script is still in the lab.";
          audio.insertAdjacentElement("afterend", note);
        }
        return;
      }
      audio.dataset.fallback = "1";
      fetch(src).then((res) => {
        if (!res.ok) throw new Error("missing");
        return res.blob();
      }).then((blob) => {
        audio.src = URL.createObjectURL(blob);
      }).catch(() => {
        const note = document.createElement("span");
        note.className = "muted clip-missing";
        note.textContent = " This clip did not load. The written script is still in the lab.";
        audio.insertAdjacentElement("afterend", note);
      });
    });
  });
}

function fetchJson(url) {
  return fetch(url).then((res) => {
    if (!res.ok) throw new Error("Could not load " + url);
    return res.json();
  });
}

function loadSettings() {
  const base = {
    theme: document.documentElement.dataset.theme || "bloom",
    darkTheme: "night",
    ink: "",
    pitch: 1,
    font: document.documentElement.dataset.font || "md",
    lang: "en",
    sound: true,
    narrate: false,
    rate: 1,
    voiceURI: "",
    reduce: document.documentElement.dataset.reduce === "1"
  };
  try {
    const saved = Object.assign(base, JSON.parse(localStorage.getItem(SETTINGS_KEY) || "{}"));
    if (saved.theme === "paper" || saved.theme === "harbor") saved.theme = "bloom";
    if (!THEMES.includes(saved.theme)) saved.theme = "bloom";
    return saved;
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
  const theme = THEMES.includes(s.theme) ? s.theme : "bloom";
  s.theme = theme;
  if (theme !== "light" && theme !== "bloom") s.darkTheme = theme;
  document.documentElement.dataset.theme = theme;
  if (s.ink && /^#[0-9a-fA-F]{6}$/.test(s.ink)) document.documentElement.style.setProperty("--cc-ink", s.ink);
  else document.documentElement.style.removeProperty("--cc-ink");
  document.documentElement.dataset.font = s.font || "md";
  const osReduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.documentElement.dataset.reduce = (s.reduce || osReduce) ? "1" : "0";
  const words = pack(s.lang || "en");
  applyLang(s.lang || "en");
  const tone = document.querySelector("#tone-toggle");
  if (tone) tone.textContent = theme === "light" ? words.dark : words.light;
  const menuTheme = $("#menu-theme");
  if (menuTheme) menuTheme.value = theme;
  const menuLang = $("#menu-lang");
  if (menuLang) menuLang.value = s.lang || "en";
  const themeColor = getComputedStyle(document.documentElement).getPropertyValue("--cc-bg").trim();
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta && themeColor) meta.content = themeColor;
  document.dispatchEvent(new CustomEvent("gccx-theme", { detail: { theme } }));
}

function setLen(name, px) {
  const cur = parseFloat(getComputedStyle(document.documentElement).getPropertyValue(name)) || 0;
  if (Math.abs(cur - px) <= 4) return;
  document.documentElement.style.setProperty(name, Math.round(px) + "px");
}

function syncChrome() {
  const chrome = document.querySelector("#chrome");
  const h = chrome ? chrome.offsetHeight : 0;
  if (h) setLen("--chrome-h", h);
  const bar = document.querySelector(".bottom-nav");
  const shown = bar && getComputedStyle(bar).display !== "none";
  setLen("--bar-h", shown ? bar.offsetHeight : 0);
}

function motionReduced() {
  return document.documentElement.dataset.reduce === "1" || window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function narrowScreen() {
  return window.matchMedia("(max-width: 820px), (pointer: coarse)").matches;
}

function whenQuiet(fn, timeout) {
  const ric = window.requestIdleCallback || ((cb) => setTimeout(cb, timeout || 600));
  ric(() => fn(), { timeout: timeout || 1600 });
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
  const learn = $("#nav-learn");
  if (learn) {
    learn.addEventListener("click", () => {
      if (window.matchMedia("(min-width: 701px) and (max-width: 980px)").matches) railEl.classList.toggle("open");
    });
  }
  wireMenu();
  document.body.addEventListener("click", (ev) => {
    const a = ev.target.closest("a[href^='#/']");
    if (a) railEl.classList.remove("open");
  });
  const offline = $("#offline-sky");
  if (offline) offline.addEventListener("click", () => cacheAll());
  watchTheme($("#theme-switch"));
  watchTheme($("#menu-theme"));
  watchLang($("#lang-switch"));
  watchLang($("#menu-lang"));
  const tone = $("#tone-toggle");
  if (tone) {
    tone.addEventListener("click", () => {
      if (state.settings.theme === "light") state.settings.theme = state.settings.darkTheme || "neon";
      else {
        state.settings.darkTheme = state.settings.theme;
        state.settings.theme = "light";
      }
      if (themeSwitch) themeSwitch.value = state.settings.theme;
      saveSettings();
    });
  }
  syncChrome();
  window.addEventListener("resize", syncChrome);
  const reduceMq = window.matchMedia("(prefers-reduced-motion: reduce)");
  reduceMq.addEventListener?.("change", () => applySettings(state.settings));
  $("#guide-launch")?.addEventListener("click", () => {
    import("./guide.js").then((mod) => mod.toggleGuide()).catch(() => {});
  });
  document.addEventListener("keydown", (ev) => {
    if (ev.key !== "ArrowRight" && ev.key !== "ArrowLeft") return;
    const nav = ev.target.closest?.(".primary-nav");
    if (!nav) return;
    const links = [...nav.querySelectorAll("a")];
    const index = links.indexOf(document.activeElement);
    if (index < 0) return;
    ev.preventDefault();
    const next = ev.key === "ArrowRight" ? (index + 1) % links.length : (index + links.length - 1) % links.length;
    links[next].focus();
  });
  const eggClose = $("#egg-close");
  if (eggClose) eggClose.addEventListener("click", () => { $("#egg").hidden = true; });
  const konami = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown", "ArrowLeft", "ArrowRight", "ArrowLeft", "ArrowRight", "b", "a"];
  let konamiAt = 0;
  document.addEventListener("keydown", (ev) => {
    const key = ev.key.length === 1 ? ev.key.toLowerCase() : ev.key;
    if (key === konami[konamiAt]) {
      konamiAt += 1;
      if (konamiAt === konami.length) {
        konamiAt = 0;
        state.progress.konami = true;
        saveProgress();
        $("#egg").hidden = false;
        blip(880, 0.12);
      }
    } else {
      konamiAt = key === konami[0] ? 1 : 0;
    }
  });
}

function roomId(route) {
  const [head, id] = route.parts;
  if (!head) return "home";
  if (id && (head === "lesson" || head === "track" || head === "boss" || head === "studio")) return id;
  return head;
}

function parseRoute() {
  const raw = (location.hash || "#/").replace(/^#/, "");
  const [path, qs] = raw.split("?");
  const parts = path.split("/").filter(Boolean);
  return { parts, query: new URLSearchParams(qs || "") };
}

function sectionMatch(href, hashPrefix) {
  if (!hashPrefix || !href.startsWith("#/")) return false;
  if (href === hashPrefix) return true;
  if (href === "#/tracks" && (hashPrefix.startsWith("#/track") || hashPrefix.startsWith("#/lesson"))) return true;
  if (href === "#/play" && ["#/game", "#/sandbox", "#/daily", "#/badges", "#/topology"].includes(hashPrefix)) return true;
  if (href === "#/atlas" && hashPrefix === "#/map") return true;
  return false;
}

function setCurrent(hashPrefix) {
  document.querySelectorAll(".bottom-nav a, .rail a, .primary-nav a, .menu-nav a").forEach((a) => {
    const href = a.getAttribute("href") || "";
    const on = sectionMatch(href, hashPrefix);
    if (on) a.setAttribute("aria-current", "page");
    else a.removeAttribute("aria-current");
  });
}

let menuPushed = false;

function openMenu() {
  const menu = $("#floor-menu");
  const backdrop = $("#menu-backdrop");
  if (!menu || menu.classList.contains("is-in")) return;
  menu.hidden = false;
  if (backdrop) backdrop.hidden = false;
  document.body.classList.add("menu-open");
  $("#menu-open")?.setAttribute("aria-expanded", "true");
  requestAnimationFrame(() => {
    menu.classList.add("is-in");
    backdrop?.classList.add("is-in");
  });
  if (!history.state || !history.state.floorMenu) {
    history.pushState({ floorMenu: 1 }, "");
    menuPushed = true;
  }
  document.dispatchEvent(new CustomEvent("gccx-visibility", { detail: { run: false } }));
  $("#menu-close")?.focus();
}

function hideMenu() {
  const menu = $("#floor-menu");
  const backdrop = $("#menu-backdrop");
  menu?.classList.remove("is-in");
  backdrop?.classList.remove("is-in");
  document.body.classList.remove("menu-open");
  $("#menu-open")?.setAttribute("aria-expanded", "false");
  window.setTimeout(() => {
    if (menu && !menu.classList.contains("is-in")) menu.hidden = true;
    if (backdrop && !backdrop.classList.contains("is-in")) backdrop.hidden = true;
  }, 280);
  document.dispatchEvent(new CustomEvent("gccx-visibility", { detail: { run: true } }));
}

function closeMenu(fromPop) {
  const menu = $("#floor-menu");
  if (!menu || menu.hidden) return;
  hideMenu();
  if (fromPop) {
    menuPushed = false;
    return;
  }
  if (menuPushed) {
    menuPushed = false;
    history.back();
  }
}

function wireMenu() {
  $("#menu-open")?.addEventListener("click", openMenu);
  $("#quick-menu")?.addEventListener("click", openMenu);
  $("#menu-close")?.addEventListener("click", () => closeMenu(false));
  $("#menu-backdrop")?.addEventListener("click", () => closeMenu(false));
  $("#floor-menu")?.addEventListener("click", (ev) => {
    const link = ev.target.closest("a");
    if (!link || !$("#floor-menu").contains(link)) return;
    const href = link.getAttribute("href") || "";
    if (href.startsWith("#")) {
      ev.preventDefault();
      hideMenu();
      menuPushed = false;
      if (history.state && history.state.floorMenu) history.replaceState(null, "");
      if (location.hash === href) render();
      else location.hash = href;
      return;
    }
    hideMenu();
    menuPushed = false;
    if (history.state && history.state.floorMenu) history.replaceState(null, "");
  });
  $("#menu-search")?.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const q = $("#menu-q").value.trim();
    hideMenu();
    menuPushed = false;
    if (history.state && history.state.floorMenu) history.replaceState(null, "");
    location.hash = "#/search?q=" + encodeURIComponent(q);
  });
  $("#nav-listen")?.addEventListener("click", (ev) => {
    ev.preventDefault();
    const behavior = motionReduced() ? "auto" : "smooth";
    if ((location.hash || "#/") !== "#/" && location.hash !== "") {
      sessionStorage.setItem("gccx-listen", "1");
      location.hash = "#/";
      return;
    }
    document.getElementById("listen")?.scrollIntoView({ behavior, block: "start" });
  });
  $("#floor-menu")?.addEventListener("keydown", (ev) => {
    if (ev.key !== "Tab") return;
    const items = [...$("#floor-menu").querySelectorAll("a, button, input, select")].filter((el) => !el.disabled);
    if (!items.length) return;
    const first = items[0];
    const last = items[items.length - 1];
    if (ev.shiftKey && document.activeElement === first) {
      ev.preventDefault();
      last.focus();
    } else if (!ev.shiftKey && document.activeElement === last) {
      ev.preventDefault();
      first.focus();
    }
  });
  window.addEventListener("popstate", () => {
    if ($("#floor-menu") && !$("#floor-menu").hidden) closeMenu(true);
  });
  document.addEventListener("keydown", (ev) => {
    if (ev.key === "Escape" && $("#floor-menu") && !$("#floor-menu").hidden) closeMenu(false);
  });
}

function watchTheme(select) {
  if (!select) return;
  select.value = state.settings.theme || "bloom";
  select.addEventListener("change", () => {
    state.settings.theme = select.value;
    saveSettings();
  });
}

function watchLang(select) {
  if (!select) return;
  select.value = state.settings.lang || "en";
  select.addEventListener("change", () => {
    state.settings.lang = select.value;
    saveSettings();
    render();
  });
}

let revealObserver = null;

function armReveal(root) {
  if (!root) return;
  const nodes = [...root.querySelectorAll(".card, .cheat-banner, .audio-dock, #home-flows, #home-charts")];
  if (motionReduced()) {
    nodes.forEach((el) => el.classList.add("is-in"));
    return;
  }
  if (!revealObserver) {
    revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12 });
  }
  nodes.forEach((el) => {
    el.classList.add("reveal");
    revealObserver.observe(el);
  });
}

function crumbs(parts) {
  const bits = parts.map((part, index) => {
    if (index === parts.length - 1) return `<span aria-current="page">${esc(part[1])}</span>`;
    return `<a href="${part[0]}">${esc(part[1])}</a>`;
  });
  return `<nav class="crumbs" aria-label="Breadcrumb">${bits.join('<span aria-hidden="true">/</span>')}</nav>`;
}

async function render() {
  stopRuntime();
  if (sessionStorage.getItem("gccx-listen") !== "1") window.scrollTo(0, 0);
  const route = parseRoute();
  document.body.dataset.room = roomId(route);
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
    if (head === "search") return await showSearch(route.query.get("q") || "");
    if (EXTRA.includes(head)) return await showExtra(head);
    showMissing();
  } catch (err) {
    showFatal(err);
  }
}

function showHome() {
  homeEl.hidden = false;
  viewEl.hidden = true;
  document.body.dataset.home = "1";
  document.title = "Genesys Cloud CX Lab";
  setCurrent("#/");
  syncChrome();
  paintHomeStats();
  const host = $("#home-dynamic");
  const wings = [
    ["#/architecture", "Architecture"],
    ["#/deploy", "Deployment"],
    ["#/ports", "Ports"],
    ["#/playbooks", "Playbooks"],
    ["#/reporting", "Reporting"],
    ["#/security", "Security"],
    ["#/roadmap", "Roadmap"],
    ["#/whats-new", "What’s new"],
    ["#/career", "Career"],
    ["#/regions", "Regions"],
    ["#/daily", "Daily challenge"],
    ["#/badges", "Badges"],
    ["#/game", "Port game"]
  ];
  host.innerHTML = `
    <div class="dl-bar" data-dl-scope="home"><span class="dl-kicker">Download</span><button type="button" class="dl-mini" data-export="html">HTML</button><button type="button" class="dl-mini" data-export="svg">SVG</button><button type="button" class="dl-mini" data-export="png">PNG</button><a class="dl-mini" href="downloads/genesys-cx-offline-bundle.zip">Bundle</a></div>
    <h2 data-dl="1">Wings <button type="button" class="dl-mini" data-export="html">Download</button></h2>
    <div class="chips">${wings.map(([href, label]) => `<a class="btn" href="${href}">${label}</a>`).join("")}</div>
    <h2 data-dl="1">Studios <button type="button" class="dl-mini" data-export="html">Download</button></h2>
    <div class="grid">${studioCards()}</div>
    <h2 data-dl="1">Chapters <button type="button" class="dl-mini" data-export="html">Download</button></h2>
    <div class="grid">${state.manifest.tracks.filter((track) => ["skills", "forecast", "quality", "ecosystem"].includes(track.id)).map(trackCard).join("")}</div>
    <h2 data-dl="1">Tracks <button type="button" class="dl-mini" data-export="html">Download</button></h2>
    <div class="grid">${state.manifest.tracks.map(trackCard).join("")}</div>`;
  mountHomeViz();
  window.gccxDecorate?.(document.getElementById("home"));
  attachSources(homeEl);
  armReveal($("#home"));
  if (sessionStorage.getItem("gccx-listen") === "1") {
    sessionStorage.removeItem("gccx-listen");
    document.getElementById("listen")?.scrollIntoView({ behavior: motionReduced() ? "auto" : "smooth", block: "start" });
  }
  status("Home");
}

function scheduleHero() {
  const canvas = $("#hero-canvas");
  if (!canvas || homeEl.hidden) return;
  const fb = canvas.parentElement?.querySelector(".hero-fallback");
  const showStill = () => {
    canvas.classList.add("is-fallback");
    canvas.parentElement?.classList.remove("hero-live");
    if (fb) fb.hidden = false;
  };
  if (motionReduced()) {
    showStill();
    return;
  }
  const start = () => {
    if (homeEl.hidden || canvas.dataset.live === "1" || canvas.dataset.booting === "1") return;
    import("./hero3d.js").then((mod) => mod.mountHero(canvas, state.settings.reduce)).catch(() => showStill());
  };
  if (narrowScreen()) {
    showStill();
    const play = $("#hero-play");
    if (play && play.dataset.bound !== "1") {
      play.dataset.bound = "1";
      play.hidden = false;
      play.addEventListener("click", () => {
        play.hidden = true;
        start();
      }, { once: true });
    } else if (play) {
      play.hidden = false;
    }
    return;
  }
  whenQuiet(start, 1800);
}

function scheduleHomeViz() {
  const host = $("#home-flows");
  if (!host || host.dataset.armed === "1") return;
  host.dataset.armed = "1";
  const run = async () => {
    if (homeEl.hidden) return;
    try {
      const { DIAGRAMS, renderDiagram } = await import("./diagrams.js");
      if (homeEl.hidden) return;
      const flowCount = DIAGRAMS.filter((item) => item.flow).length;
      paintIcons($("#home-icons"), null, { diagrams: DIAGRAMS.length, flows: flowCount, charts: 6, sheets: 13 });
      const picks = DIAGRAMS.filter((item) => item.flow).slice(0, 3);
      const flows = $("#home-flows");
      if (flows) {
        flows.innerHTML = `<h2 data-dl="1">Flows <button type="button" class="dl-mini" data-export="html">Download</button></h2>
          <p class="muted"><a href="#/flows">All ${flowCount} animated flows</a> · <a href="#/atlas">${DIAGRAMS.length} diagrams</a> · <a href="#/cheat">Cheat codes</a></p>
          <div class="flow-strip">${picks.map((spec) => `<article class="card">${renderDiagram(spec)}<h3>${esc(spec.title)}</h3></article>`).join("")}</div>`;
      }
      const charts = $("#home-charts");
      if (charts && !charts.dataset.drawn) {
        charts.dataset.drawn = "1";
        charts.innerHTML = `<h2 data-dl="1">Charts <button type="button" class="dl-mini" data-export="html">Download</button></h2><div id="home-chart-root" class="chart-hold"></div>`;
        const mod = await import("./floorviz.js");
        if (!homeEl.hidden) await mod.mountFloor($("#home-chart-root"), state.manifest, null);
      }
    } catch (err) {
      status(err.message || "Charts did not draw");
    }
    armReveal($("#home"));
  };
  const target = $("#home-charts");
  if (target && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      if (!entries.some((entry) => entry.isIntersecting)) return;
      io.disconnect();
      run();
    }, { rootMargin: "160px" });
    io.observe(target);
    return;
  }
  whenQuiet(run, 2000);
}

async function mountHomeViz() {
  if (homeEl.hidden) return;
  scheduleHero();
  paintIcons($("#home-icons"), null);
  try {
    const { DIAGRAMS } = await import("./diagrams.js");
    if (!homeEl.hidden) {
      paintIcons($("#home-icons"), null, {
        diagrams: DIAGRAMS.length,
        flows: DIAGRAMS.filter((item) => item.flow).length,
        charts: 6,
        sheets: 13
      });
    }
  } catch (err) {
    status(err.message || "Icon counts did not load");
  }
  scheduleHomeViz();
}

function paintIcons(host, track, counts = {}) {
  if (!host || !state.manifest) return;
  const lessons = track ? track.lessons : state.manifest.tracks.flatMap((item) => item.lessons);
  const minutes = lessons.reduce((sum, lesson) => sum + (lesson.minutes || 0), 0);
  const done = track
    ? track.lessons.filter((lesson) => state.progress.lessons[lesson.id]?.done).length
    : Object.values(state.progress.lessons).filter((item) => item.done).length;
  const tiles = host.id === "home-icons"
    ? [
      ["#/atlas", "Diagrams", counts.diagrams ?? "—", "diagram", "Atlas"],
      ["#/flows", "Flows", counts.flows ?? "—", "flow", "Animated"],
      ["#/charts", "Charts", counts.charts ?? 6, "chart", "From this lab"],
      ["#/cheat", "Cheat codes", counts.sheets ?? 13, "cheat", "HTML PDF PNG"],
      ["#/downloads", "Downloads", "ZIP", "download", "Sheets and bundle"],
      ["#/play", "Play", "GO", "play", "Games and drills"]
    ]
    : [
      ["#/atlas", "Diagrams", counts.diagrams ?? "—", "diagram", "Atlas"],
      ["#/flows", "Flows", counts.flows ?? "—", "flow", "Animated"],
      ["#/charts", "Charts", counts.charts ?? 6, "chart", "From this lab"],
      ["#/cheat", "Cheat codes", counts.sheets ?? 13, "cheat", "HTML PDF PNG"],
      ["#/tracks", track ? ht(track.id, track.title) : "Lessons", lessons.length, "prism", `${minutes} min`],
      ["#/tracks", "Finished", done, "star", track ? "This track" : "This browser"]
    ];
  host.innerHTML = tiles.map(([href, label, num, kind, note], index) => `<a class="icon-tile" href="${href}">${iconStage(kind, index)}<span class="tile-copy"><b data-count="${esc(num)}">${esc(num)}</b><span class="tile-label">${esc(label)}</span><span class="tile-note">${esc(note)}</span></span></a>`).join("");
  host.querySelectorAll("[data-count]").forEach((el) => countUp(el, el.dataset.count));
  refreshLive();
}

function showTracks() {
  mount(`${crumbs([["#/", "Home"], ["#/tracks", "Tracks"]])}<p class="kicker">Curriculum</p><h1>Tracks</h1><p>${state.manifest.tracks.length} paths from organization setup through Predictive Engagement and migration. Open one track at a time.</p><div class="grid">${state.manifest.tracks.map(trackCard).join("")}</div>`);
  setCurrent("#/tracks");
}

async function showTrack(id) {
  const track = await loadTrack(id);
  if (!track) return showMissing();
  const items = track.lessons.map((lesson, index) => {
    const prog = state.progress.lessons[lesson.id];
    const mark = prog && prog.done ? "Finished" : "Open";
    return `<a class="card" href="#/lesson/${lesson.id}"><div class="stripe a${track.accent}"></div><p class="kicker">${esc(ht(track.id, track.title))} · ${index + 1}</p><h3>${esc(ht(lesson.id, lesson.title))}</h3><p>${esc(lesson.summary)}</p><p class="muted">${esc(lesson.level)} · ${lesson.minutes} min · ${mark}</p></a>`;
  }).join("");
  mount(`${crumbs([["#/", "Home"], ["#/tracks", "Tracks"], ["#/track/" + id, ht(track.id, track.title)]])}
    <p class="kicker">${esc(track.kicker)}</p><h1>${esc(ht(track.id, track.title))}</h1><p>${esc(track.summary)}</p>
    <div id="track-icons" class="icon-parade" aria-label="Track counters"></div>
    <p class="spot-links"><a class="btn" href="#track-charts">Charts</a><a class="btn" href="#/flows">Flows</a><a class="btn" href="#/cheat">Cheat codes</a><a class="btn" href="#/atlas">Diagrams</a></p>
    <div class="grid">${items}</div>
    <h2 id="track-charts">Charts</h2>
    <div id="track-chart-root"></div>`);
  const { DIAGRAMS } = await import("./diagrams.js");
  paintIcons($("#track-icons"), track, {
    diagrams: DIAGRAMS.length,
    flows: DIAGRAMS.filter((item) => item.flow).length,
    charts: 6,
    sheets: 13
  });
  const viz = await import("./floorviz.js");
  await viz.mountFloor($("#track-chart-root"), state.manifest, id);
  document.title = ht(track.id, track.title) + " · Genesys Cloud CX Lab";
  setCurrent("#/track/" + id);
}

async function showLesson(id) {
  const stub = findLesson(id);
  if (!stub) return showMissing();
  const track = await loadTrack(stub.trackId);
  const lesson = track.lessons.find((item) => item.id === id);
  mount(renderLesson(track, lesson));
  wireLesson(lesson);
  document.title = ht(lesson.id, lesson.title) + " · Genesys Cloud CX Lab";
  setCurrent("#/lesson/" + id);
  if (state.settings.narrate) say(lesson.summary);
}

function renderLesson(track, lesson) {
  const cites = lesson.cites.map((cite) => `<li><a href="${esc(cite.url)}" rel="noopener noreferrer">${esc(cite.title)}</a></li>`).join("");
  const paras = lesson.paras.map((p) => `<p>${esc(p)}</p>`).join("");
  const uncertainty = lesson.uncertainty ? `<aside class="uncertainty"><strong>Confirm on the vendor page. </strong>${esc(lesson.uncertainty)}</aside>` : "";
  return `
    ${crumbs([["#/", "Home"], ["#/tracks", "Tracks"], ["#/track/" + track.id, ht(track.id, track.title)], ["#/lesson/" + lesson.id, ht(lesson.id, lesson.title)]])}
    <div class="read-layout">
      <article>
        <p class="kicker"><a href="#/track/${track.id}">${esc(ht(track.id, track.title))}</a> · ${esc(lesson.level)} · ${lesson.minutes} min</p>
        <div class="lesson-head"><h1>${esc(ht(lesson.id, lesson.title))}</h1></div>
        <p class="lede">${esc(lesson.summary)}</p>
        ${downloadBar(lesson.title)}
        ${learnFive(lesson)}
        <div id="sec-figure">${figureSvg(lesson.figure)}</div>
        <div id="sec-read">${paras}</div>
        ${uncertainty}
        <h2 id="sec-worked">Worked example</h2>
        <div class="panel"><p>${esc(lesson.lab?.title || lesson.summary)}</p><ol>${(lesson.lab?.steps || []).map((step) => `<li>${esc(step)}</li>`).join("")}</ol><p class="muted">${esc(lesson.lab?.success || "Paper lab. Nothing is sent to an organization.")}</p></div>
        <h2 id="sec-sources">Sources</h2>
        <ul>${cites}</ul>
        <h2 id="sec-flow">Step-through</h2>
        <div class="panel" id="flow-player">${flowPlayer(lesson.flow)}</div>
        <h2 id="sec-quiz">Quiz</h2>
        <div class="panel" id="quiz">${quizShell(lesson)}</div>
        <h2 id="sec-cards">Flashcards</h2>
        <div class="panel" id="cards">${cardShell(lesson)}</div>
        <h2 id="sec-lab">Lab</h2>
        <div class="panel">${labShell(lesson)}</div>
        <h2 id="sec-fault">Fault and fix</h2>
        <div class="panel">${faultShell(lesson)}</div>
        ${ecosystemBlock()}
        <p><a class="btn" href="#/track/${track.id}">Back to ${esc(ht(track.id, track.title))}</a></p>
      </article>
      <nav class="onpage" aria-label="On this page">
        <a href="#sec-learn5">5 minutes</a>
        <a href="#sec-figure">Figure</a>
        <a href="#sec-worked">Example</a>
        <a href="#sec-eco">Ecosystem</a>
        <a href="#sec-read">Reading</a>
        <a href="#sec-sources">Sources</a>
        <a href="#sec-sources-deeper">Go deeper</a>
        <a href="#sec-flow">Step-through</a>
        <a href="#sec-quiz">Quiz</a>
        <a href="#sec-cards">Flashcards</a>
        <a href="#sec-lab">Lab</a>
        <a href="#sec-fault">Fault</a>
      </nav>
    </div>`;
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
    return `<line class="dash" x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="currentColor" stroke-opacity="0.55" stroke-width="2" stroke-dasharray="6 6"/>`;
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
          if (correct >= 5) {
            prog.done = true;
            if (!state.settings.reduce) {
              import("../vendor/confetti.js").then((mod) => {
                const fire = mod.default;
                if (typeof fire === "function") fire({ particleCount: 90, spread: 70, origin: { y: 0.65 }, disableForReducedMotion: true });
              }).catch(() => {});
            }
          }
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
  const tracks = state.manifest.tracks.map((track) => `<a class="card" href="#/track/${track.id}"><div class="stripe a${track.accent}"></div><h3>${esc(ht(track.id, track.title))}</h3><p>${esc(track.summary)}</p></a>`).join("");
  mount(`${crumbs([["#/", "Home"], ["#/ecosystem", "Ecosystem"]])}<p class="kicker">Map</p><h1>Ecosystem</h1>
    <p>Genesys Cloud CX is the conversation platform. WEM, recording, emergency calling, CRM, and bots sit on documented edges of that platform. Each lesson keeps its own citation. If a vendor page disagrees, the page wins.</p>
    <p class="muted">Lucky is a lifelong student and an AI enthusiast, from systems, networking, voice, and the contact center, growing into AI omni-channel agents. This floor is the notebook.</p>
    <h2>Glossary</h2>
    <p>Short definitions, each with the page it came from. The glossary does not win an argument with that page.</p>
    <p><a class="btn primary" href="#/glossary">Open the glossary</a></p>
    <h2>Mind map</h2>
    <div class="markmap-host"><svg id="eco-map" role="img" aria-label="Mind map of the tracks"></svg></div>
    <h2>Sister technologies</h2>
    <div class="grid">
      <a class="card" href="#/track/wfm"><h3>Workforce management</h3><p>Schedules and adherence. Forecasting is its own chapter.</p></a>
      <a class="card" href="#/track/quality"><h3>Quality and speech</h3><p>Forms, topics, and programs.</p></a>
      <a class="card" href="#/track/emergency"><h3>Emergency calling</h3><p>A classification, a route, and a test.</p></a>
      <a class="card" href="#/track/byoc"><h3>SIP and RTP</h3><p>Signaling is not the audio. BYOC Cloud is the cited telephony door.</p></a>
    </div>
    <h2>Integration map</h2>
    <div class="card" aria-hidden="true">
      <svg viewBox="0 0 360 160">
        <path d="M40 80 H120 L180 40 H250 L310 80" fill="none" stroke="#2ff7ff" stroke-width="2"></path>
        <path d="M180 40 V120 H250" fill="none" stroke="#b388ff" stroke-width="2"></path>
        <circle cx="40" cy="80" r="8" fill="#ff2fb3"></circle>
        <circle cx="120" cy="80" r="8" fill="#2ff7ff"></circle>
        <circle cx="180" cy="40" r="8" fill="#d6ff3c"></circle>
        <circle cx="250" cy="40" r="8" fill="#b388ff"></circle>
        <circle cx="310" cy="80" r="8" fill="#ff2fb3"></circle>
        <circle cx="180" cy="120" r="8" fill="#7dffa8"></circle>
        <g fill="#f4fbff" font-size="12" font-family="Palatino, Georgia, serif">
          <text x="16" y="104">Carrier</text>
          <text x="96" y="104">BYOC</text>
          <text x="156" y="28">Flow</text>
          <text x="228" y="28">Queue</text>
          <text x="286" y="104">Agent</text>
          <text x="150" y="146">CRM / bot</text>
        </g>
      </svg>
    </div>
    <div class="grid">
      <a class="card" href="#/lesson/z-cpaas"><h3>BYOC bridge</h3><p>The telephony door this lab can cite. The article does not say CPaaS.</p></a>
      <a class="card" href="#/lesson/z-crm"><h3>CRM bridge</h3><p>Salesforce and Zendesk pages that were opened. Other CRMs stay on AppFoundry.</p></a>
      <a class="card" href="#/lesson/z-agents"><h3>AI agents</h3><p>Dialog Engine, Virtual Agent, and Copilot are three different assists.</p></a>
      <a class="card" href="#/track/api"><h3>Platform API</h3><p>Samples stay in the browser. Nothing is sent.</p></a>
    </div>
    <h2>Future hooks</h2>
    <div class="grid">
      <a class="card" href="#/lesson/z-hooks"><h3>Dated announcements</h3><p>Journey Outcomes 2026-06-29. Salesforce Open CTI 2028-02-28. Re-open both.</p></a>
      <a class="card" href="#/track/predictive"><h3>Predictive Engagement</h3><p>Not the ACD method named predictive routing.</p></a>
    </div>
    <div class="toolbar">
      <a class="btn" href="#/glossary">Glossary</a>
      <a class="btn" href="#/certs">Certifications</a>
      <a class="btn" href="#/interview">Interview drill</a>
      <a class="btn" href="#/boss">Boss incidents</a>
      <a class="btn" href="#/topology">3D topology</a>
      <a class="btn" href="#/architecture">Architecture</a>
      <a class="btn" href="#/map">Flow map</a>
      <a class="btn" href="#/security">Security</a>
      <a class="btn" href="#/career">Career</a>
    </div>
    <h2>Sister systems inside the tracks</h2>
    <div class="grid">${tracks}</div>`);
  document.title = "Ecosystem · Genesys Cloud CX Lab";
  setCurrent("#/ecosystem");
  mountMindmap();
}

async function mountMindmap() {
  const svg = $("#eco-map");
  if (!svg) return;
  try {
    const { Transformer, Markmap } = await import("../vendor/markmap.js");
    const lines = ["# Genesys Cloud CX"];
    state.manifest.tracks.forEach((track) => {
      lines.push(`## ${track.title.replace(/[#>`]/g, "")}`);
      track.lessons.slice(0, 4).forEach((lesson) => {
        lines.push(`- ${lesson.title.replace(/[#>`]/g, "")}`);
      });
    });
    const { root } = new Transformer().transform(lines.join("\n"));
    Markmap.create(svg, { duration: motionReduced() ? 0 : 400 }, root);
  } catch (err) {
    svg.insertAdjacentHTML("afterend", `<p class="uncertainty">The mind map did not draw in this browser. The track cards are the same map.</p>`);
  }
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
        ${THEMES.map((theme) => `<label class="choice"><input type="radio" name="theme" value="${theme}" ${s.theme === theme ? "checked" : ""}> ${theme}</label>`).join("")}
      </fieldset>
      <label>Language <select name="lang">${LANGS.map(([code, label]) => `<option value="${code}" ${s.lang === code ? "selected" : ""}>${label}</option>`).join("")}</select></label>
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
    state.settings.lang = data.get("lang") || "en";
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
  try {
  const cache = await caches.open("gccx-lab-v7");
  const urls = ["index.html", "assets/app.js", "assets/studios.js", "assets/topology.js", "assets/routing-model.js", "assets/university.css", "assets/mascot.js", "assets/diagrams.js", "assets/pages.js", "assets/floorviz.js", "assets/hero3d.js", "assets/icons3d.js", "assets/liveicons.js", "assets/headings.js", "assets/i18n.js", "assets/lightbox.js", "vendor/d3.js", "vendor/anime.js", "vendor/rough.js", "vendor/confetti.js", "data/manifest.json", "data/reference.json", "manifest.webmanifest", "downloads/catalog.json", "downloads/flashcards.json", "downloads/flashcards.html", "audio/tour.mp3", "audio/practice.mp3"];
  state.manifest.tracks.forEach((track) => urls.push(track.file));
  await cache.addAll(urls.map((url) => new URL(url, location.href).toString()));
  state.progress.offlineSaved = true;
  saveProgress();
  status("Tracks cached for offline use");
  } catch (err) {
    status(err.message || "Offline cache failed");
  }
}

async function showSearch(q) {
  const needle = q.trim().toLowerCase();
  const hits = [];
  state.manifest.tracks.forEach((track) => {
    track.lessons.forEach((lesson) => {
      const blob = (lesson.title + " " + lesson.summary).toLowerCase();
      if (!needle || blob.includes(needle)) hits.push({ track, lesson });
    });
  });
  const ref = await loadReference();
  const terms = ref.glossary.filter((item) => !needle || (item.term + " " + item.def).toLowerCase().includes(needle)).slice(0, 12);
  const cards = hits.slice(0, 40).map(({ track, lesson }) => `<a class="card" href="#/lesson/${lesson.id}"><p class="kicker">${esc(ht(track.id, track.title))}</p><h3>${esc(ht(lesson.id, lesson.title))}</h3><p>${esc(lesson.summary)}</p></a>`).join("");
  const gloss = terms.map((item) => `<article class="card"><h3>${esc(item.term)}</h3><p>${esc(item.def)}</p><p><a href="${esc(item.url)}">${esc(item.source)}</a></p></article>`).join("");
  mount(`${crumbs([["#/", "Home"], ["#/search", "Search"]])}<p class="kicker">Search</p><h1>${needle ? "Results" : "Browse"}</h1><p>${hits.length} lesson${hits.length === 1 ? "" : "s"}${needle ? " for “" + esc(q) + "”" : ""}. ${terms.length} glossary hits.</p><div class="grid">${cards || "<p>No lesson title or summary uses that phrase.</p>"}</div><h2>Glossary</h2><div class="grid">${gloss}</div>`);
  document.title = "Search · Genesys Cloud CX Lab";
}

async function showExtra(name) {
  try {
    mount(`<div id="extra-root"><p>Opening ${esc(name)}.</p></div>`);
    const mod = await import("./pages.js");
    await mod.mountPage(name, {
      root: $("#extra-root"),
      esc,
      state,
      blip,
      saveProgress,
      status,
      setTitle: (title) => { document.title = title + " · Genesys Cloud CX Lab"; }
    });
    const label = CRUMB[name] || name;
    $("#extra-root")?.insertAdjacentHTML("afterbegin", crumbs([["#/", "Home"], ["#/" + name, label]]));
    setCurrent("#/" + name);
  } catch (err) {
    showFatal(err);
  }
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

function downloadBar(label) {
  const name = esc(label || "This room");
  return `<div class="dl-bar" data-dl-scope="${name}"><span class="dl-kicker">Download</span><button type="button" class="dl-mini" data-export="html">HTML</button><button type="button" class="dl-mini" data-export="svg">SVG</button><button type="button" class="dl-mini" data-export="png">PNG</button><a class="dl-mini" href="downloads/genesys-cx-offline-bundle.zip">Bundle</a></div>`;
}

function learnFive(lesson) {
  const bits = [lesson.summary, ...(lesson.paras || []).slice(0, 3)].filter(Boolean);
  return `<section class="learn5" id="sec-learn5"><h2>Learn it in 5 minutes</h2><ol>${bits.map((bit) => `<li>${esc(bit)}</li>`).join("")}</ol><p class="muted">Confirm before relying on any sentence this lab marks as uncertain. The cited page wins.</p></section>`;
}

function ecosystemBlock() {
  return `<section class="eco-panel" id="sec-eco"><h2>Ecosystem</h2>
    <h3>Glossary</h3><p>Short definitions, each with a source, are on the <a href="#/glossary">glossary</a>.</p>
    <h3>Mind map</h3><p>Organization, Architect, queues, trunks, the Edge, WEM, and APIs. Open the <a href="#/ecosystem">ecosystem map</a>.</p>
    <h3>Sister technologies</h3><p>SIP sets up the call. RTP moves the audio. The port table in this lab is only the rows it opened. Confirm the firewall article before you open a range.</p>
    <h3>Config and troubleshooting</h3><p>Publish the flow. A draft does not answer. No audio after a healthy flow is a media problem. An empty offer is tracking, schedule, or eligibility.</p>
    <h3>Integration maps</h3><p>Salesforce and Zendesk have their own embed articles. Other products stay on AppFoundry. This lab did not install them.</p>
    <h3>Cross-platform bridges</h3><p>Engage, PureConnect, and Cisco UCCE / UCCX are rebuild notes, not converters. CUCM appears as a learning bridge with Cisco citations.</p>
    <h3>Bridges</h3><p>CRM: the Salesforce and Zendesk articles. Telephony: BYOC, which this lab does not rename to CPaaS. AI agents: Dialog Engine, Virtual Agent, and Copilot. <a href="#/ecosystem">Open the map</a>.</p>
    <h3>Future hooks</h3><p>Journey Outcomes listed a planned effective date of 2026-06-29. Salesforce Open CTI listed 2028-02-28. If a page moves, the page wins.</p>
  </section>`;
}

function mount(html) {
  delete document.body.dataset.home;
  homeEl.hidden = true;
  viewEl.hidden = false;
  viewEl.innerHTML = html;
  window.gccxDecorate?.(viewEl);
  attachSources(viewEl);
  status("Ready");
  syncChrome();
  refreshLive();
  armReveal(viewEl);
}

function status(text) {
  statusEl.textContent = text;
}

function paintRail() {
  const links = state.manifest.tracks.map((track) => `<a href="#/track/${track.id}">${esc(ht(track.id, track.title))} <span class="muted">${track.lessons.length}</span></a>`).join("");
  railEl.innerHTML = `<h2>Floor</h2><a href="#/">Home</a><a href="#/atlas">Diagram atlas</a><a href="#/regions">Regions</a><a href="#/ports">Ports</a><a href="#/cheat">Cheat codes</a><a href="#/map">Flow map</a><a href="#/studio">Studios</a><a href="#/sandbox">Flow sandbox</a><a href="#/topology">3D topology</a><a href="#/ecosystem">Ecosystem</a><a href="#/certs">Certifications</a><a href="#/whats-new">What’s new</a><a href="#/boss">Boss incidents</a><a href="#/badges">Badges</a><h2>Tracks</h2>${links}`;
}

const countTokens = new WeakMap();

function countUp(el, target) {
  if (!el) return;
  const next = Number(target);
  if (!Number.isFinite(next)) {
    el.textContent = String(target);
    return;
  }
  if (document.documentElement.dataset.reduce === "1") {
    el.textContent = String(next);
    el.dataset.n = String(next);
    return;
  }
  const token = (countTokens.get(el) || 0) + 1;
  countTokens.set(el, token);
  const from = Number(el.dataset.n || 0);
  const t0 = performance.now();
  const step = (now) => {
    if (countTokens.get(el) !== token) return;
    const p = Math.min(1, (now - t0) / 900);
    const eased = 1 - Math.pow(1 - p, 3);
    el.textContent = String(Math.round(from + (next - from) * eased));
    if (p < 1) requestAnimationFrame(step);
    else el.dataset.n = String(next);
  };
  requestAnimationFrame(step);
}

function paintHomeStats() {
  if (!state.manifest) return;
  const lessons = state.manifest.tracks.reduce((sum, track) => sum + track.lessons.length, 0);
  const done = Object.values(state.progress.lessons).filter((item) => item.done).length;
  countUp($("#stat-tracks"), state.manifest.tracks.length);
  countUp($("#stat-lessons"), lessons);
  countUp($("#stat-quiz"), state.manifest.quizCount);
  countUp($("#stat-done"), done);
  const pct = lessons ? Math.round((done / lessons) * 100) : 0;
  const ring = $("#progress-ring");
  const label = $("#stat-pct");
  if (ring) ring.style.setProperty("--p", String(pct));
  if (label) label.textContent = pct + "%";
}

function ht(id, fallback) {
  return heading(id, state.settings.lang || "en", fallback);
}

function iconStage(kind, accent) {
  return `<div class="iso-stage" data-kind="${esc(kind)}" data-accent="${esc(accent)}">${isoIcon(kind, Number(accent) || 0)}<canvas class="live-icon" width="360" height="320" aria-hidden="true"></canvas></div>`;
}

function refreshLive() {
  if (motionReduced() || narrowScreen()) return;
  whenQuiet(() => {
    import("./liveicons.js").then((mod) => mod.scan(document)).catch(() => {});
  }, 2400);
}

function trackCard(track) {
  return `<a class="card iso-card" href="#/track/${track.id}">${iconStage(iconForTrack(track.id), track.accent || 0)}<p class="kicker">${esc(track.kicker)}</p><h3>${esc(ht(track.id, track.title))}</h3><p>${esc(track.summary)}</p><p class="muted">${track.lessons.length} lessons</p></a>`;
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
