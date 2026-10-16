/** Scripted Guide Bot. Answers come from data/guide-kb.json. It does not invent facts. */

const STOP = new Set(["the", "and", "for", "what", "how", "does", "this", "lab", "with", "from", "that", "are", "you", "can", "about", "tell", "please", "show", "where", "when", "who", "why", "its", "into"]);

const STARTER = [
  { label: "Tour the floor", ask: "tour the floor" },
  { label: "Quiz me", ask: "quiz me" },
  { label: "Ports", ask: "ports and rtp" },
  { label: "Routing", ask: "how does bullseye routing work" },
  { label: "Cheat codes", ask: "cheat codes" },
  { label: "Who is Lucky", ask: "who is lucky" }
];

let kb = null;
let kbPromise = null;
let open = false;
let quiz = null;
let tour = null;
let chipGen = 0;

function $(sel) {
  return document.querySelector(sel);
}

function motionOff() {
  return document.documentElement.dataset.reduce === "1" || window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function loadKb() {
  if (!kbPromise) {
    kbPromise = fetch("data/guide-kb.json").then((res) => {
      if (!res.ok) throw new Error("guide knowledge base");
      return res.json();
    }).then((data) => {
      kb = data;
      return data;
    });
  }
  return kbPromise;
}

export function toggleGuide() {
  const panel = $("#guide-panel");
  const launch = $("#guide-launch");
  if (!panel || !launch) return;
  open = panel.hidden;
  panel.hidden = !open;
  launch.setAttribute("aria-expanded", open ? "true" : "false");
  if (!open) return;
  $("#guide-q")?.focus();
  if (!$("#guide-log")?.childElementCount) greet();
}

function greet() {
  wire();
  say("I answer from this lab’s own pages. If a question is not in those notes, I will say so instead of guessing.", STARTER);
}

function wire() {
  if (wire.done) return;
  wire.done = true;
  $("#guide-close")?.addEventListener("click", () => {
    const panel = $("#guide-panel");
    if (panel) panel.hidden = true;
    open = false;
    $("#guide-launch")?.setAttribute("aria-expanded", "false");
    $("#guide-launch")?.focus();
  });
  $("#guide-form")?.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const input = $("#guide-q");
    const text = input?.value.trim();
    if (!input || !text) return;
    input.value = "";
    ask(text);
  });
  document.addEventListener("keydown", (ev) => {
    if (ev.key === "Escape" && open) $("#guide-close")?.click();
  });
}

function bubble(kind, html) {
  const log = $("#guide-log");
  if (!log) return null;
  const el = document.createElement("div");
  el.className = `bubble ${kind}`;
  el.innerHTML = html;
  log.appendChild(el);
  log.scrollTop = log.scrollHeight;
  return el;
}

function setChips(chips) {
  const host = $("#guide-chips");
  if (!host) return;
  host.innerHTML = "";
  (chips || []).forEach((chip) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = chip.label;
    btn.addEventListener("click", () => ask(chip.ask));
    host.appendChild(btn);
  });
}

function say(text, chips, href, source) {
  const mine = ++chipGen;
  const el = bubble("bot", motionOff() ? "" : '<p class="typing" aria-hidden="true"><i></i><i></i><i></i></p>');
  const finish = () => {
    if (mine === chipGen) setChips(chips);
  };
  const paint = () => {
    if (!el) return;
    const link = href ? `<p><a href="${escapeHtml(href)}">Open this page</a></p>` : "";
    const cite = source ? `<p class="muted">Source: ${escapeHtml(source)}</p>` : "";
    el.innerHTML = `<p></p>${link}${cite}`;
    const p = el.querySelector("p");
    if (!p) return;
    if (motionOff()) {
      p.textContent = text;
      finish();
      return;
    }
    let i = 0;
    const step = () => {
      if (!p) return;
      i += 2;
      p.textContent = text.slice(0, i);
      const log = $("#guide-log");
      if (log) log.scrollTop = log.scrollHeight;
      if (i < text.length) window.setTimeout(step, 16);
      else finish();
    };
    step();
  };
  if (motionOff()) paint();
  else window.setTimeout(paint, 280);
}

function ask(raw) {
  bubble("user", `<p>${escapeHtml(raw)}</p>`);
  setChips([]);
  loadKb().then((data) => route(raw, data)).catch(() => {
    say("The guide notes did not load, so I will not guess. Use Search, or open Diagrams, Flows, Charts, or Cheat Codes.");
  });
}

function route(raw, data) {
  const text = raw.trim();
  const lower = text.toLowerCase();
  if (lower.startsWith("open #")) {
    location.hash = text.replace(/^open\s+/i, "").trim();
    say("That page is open on the floor. I stay in this panel.", STARTER);
    return;
  }
  if (quiz && handleQuiz(lower, text)) return;
  if (tour && handleTour(lower, data)) return;
  if (/^(stop|cancel|quit)$/.test(lower)) {
    quiz = null;
    tour = null;
    say("Stopped. Ask about a page, or pick a chip.", STARTER);
    return;
  }
  const tourHit = data.tours.find((item) => lower.includes(item.title.toLowerCase()) || lower.includes(item.id.replace(/-/g, " ")));
  if (tourHit || /\btour\b/.test(lower)) {
    const chosen = tourHit || data.tours[0];
    beginTour(chosen);
    return;
  }
  if (/\bquiz\b/.test(lower)) {
    const chosen = data.quizzes.find((item) => lower.includes(item.id)) || data.quizzes[0];
    beginQuiz(chosen);
    return;
  }
  answer(text, data);
}

function beginTour(item) {
  tour = { item, step: 0 };
  quiz = null;
  showTourStep();
}

function showTourStep() {
  const step = tour.item.steps[tour.step];
  const last = tour.step >= tour.item.steps.length - 1;
  if (step.href) location.hash = step.href;
  say(step.text, last
    ? [{ label: "Done", ask: "stop" }, { label: "Quiz me", ask: "quiz me" }]
    : [{ label: "Next", ask: "next" }, { label: "Stop tour", ask: "stop" }], step.href, step.source);
}

function handleTour(lower) {
  if (lower === "next" || lower.startsWith("next ")) {
    tour.step += 1;
    if (tour.step >= tour.item.steps.length) {
      tour = null;
      say("Tour finished. Every stop was a page already on this floor.", STARTER);
      return true;
    }
    showTourStep();
    return true;
  }
  return false;
}

function beginQuiz(item) {
  quiz = { item, index: 0, score: 0, locked: false };
  tour = null;
  say(`${item.title}. ${item.questions.length} questions. I only score answers that match the notes.`, [
    { label: "Stop quiz", ask: "stop" }
  ]);
  window.setTimeout(() => askQuestion(), motionOff() ? 0 : 400);
}

function askQuestion() {
  const q = quiz.item.questions[quiz.index];
  quiz.locked = false;
  const chips = q.choices.map((choice, index) => ({ label: choice, ask: String(index + 1) }));
  chips.push({ label: "Stop quiz", ask: "stop" });
  say(`Question ${quiz.index + 1} of ${quiz.item.questions.length}. ${q.q}`, chips, null, q.source);
}

function handleQuiz(lower, text) {
  if (lower === "stop" || lower === "stop quiz") return false;
  if (quiz.locked) {
    if (lower === "next" || lower.startsWith("next ")) routeNextAfterQuiz();
    return true;
  }
  const q = quiz.item.questions[quiz.index];
  if (quiz.locked) return true;
  let pick = -1;
  if (/^[1-4]$/.test(lower)) pick = Number(lower) - 1;
  else {
    const idx = q.choices.findIndex((choice) => choice.toLowerCase() === text.toLowerCase());
    if (idx >= 0) pick = idx;
  }
  if (pick < 0) {
    say("Reply with a chip, or 1 through 4. I will not grade a guess I cannot match.", q.choices.map((choice, index) => ({ label: choice, ask: String(index + 1) })));
    return true;
  }
  quiz.locked = true;
  const right = pick === q.answer;
  if (right) quiz.score += 1;
  const verdict = right ? "That matches the note." : `The note says: ${q.choices[q.answer]}.`;
  say(`${verdict} ${q.why}`, [{ label: "Next", ask: "next" }], q.href, q.source);
  return true;
}

function routeNextAfterQuiz() {
  quiz.index += 1;
  quiz.locked = false;
  if (quiz.index >= quiz.item.questions.length) {
    const total = quiz.item.questions.length;
    const score = quiz.score;
    quiz = null;
    say(`Score ${score} out of ${total}. That only counts answers checked against this lab’s notes.`, [
      { label: "Try another quiz", ask: "quiz me" },
      { label: "Tour the floor", ask: "tour the floor" }
    ]);
    return;
  }
  askQuestion();
}

function answer(text, data) {
  const local = matchEntries(text, data.entries);
  const endpoint = cloudEndpoint(data);
  if (!endpoint) {
    speakMatch(local);
    return;
  }
  consultCloud(endpoint, text, local).then((cloud) => {
    if (!cloud) {
      speakMatch(local);
      return;
    }
    say(cloud.answer, followChips(cloud.href), cloud.href, cloud.source);
  });
}

function speakMatch(local) {
  if (!local) {
    say("I don’t have that in this lab’s notes, so I won’t guess. Try Diagrams, Flows, Charts, Cheat Codes, or the search box.", [
      { label: "Diagrams", ask: "diagrams" },
      { label: "Flows", ask: "flows" },
      { label: "Charts", ask: "charts" },
      { label: "Cheat codes", ask: "cheat codes" },
      { label: "Search lessons", ask: "how do I search" }
    ]);
    return;
  }
  const chips = followChips(local.entry.href);
  if (local.runner) chips.unshift({ label: local.runner.title, ask: local.runner.title });
  say(local.entry.answer, chips, local.entry.href, local.entry.source);
}

function followChips(href) {
  const chips = [];
  if (href) chips.push({ label: "Open the page", ask: "open " + href });
  chips.push({ label: "Quiz me", ask: "quiz me" }, { label: "Tour the floor", ask: "tour the floor" });
  return chips;
}

function cloudEndpoint(data) {
  const fromWindow = typeof window.GCCX_GUIDE_ENDPOINT === "string" ? window.GCCX_GUIDE_ENDPOINT.trim() : "";
  const fromKb = typeof data.endpoint === "string" ? data.endpoint.trim() : "";
  const url = fromWindow || fromKb;
  if (!url) return "";
  try {
    const parsed = new URL(url);
    if (parsed.protocol !== "https:") return "";
    return parsed.toString();
  } catch (err) {
    return "";
  }
}

function consultCloud(endpoint, question, local) {
  const body = {
    question,
    matches: local ? [{ id: local.entry.id, title: local.entry.title, href: local.entry.href }] : []
  };
  return fetch(endpoint, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body)
  }).then((res) => (res.ok ? res.json() : null)).then((payload) => {
    if (!payload || payload.grounded !== true) return null;
    if (typeof payload.answer !== "string" || !payload.answer.trim()) return null;
    if (typeof payload.source !== "string" || !payload.source.startsWith("https://")) return null;
    return {
      answer: payload.answer.trim(),
      href: typeof payload.href === "string" ? payload.href : "",
      source: payload.source
    };
  }).catch(() => null);
}

function matchEntries(query, entries) {
  const tokens = tokenize(query);
  if (!tokens.length) return null;
  const ranked = entries.map((entry) => ({ entry, score: scoreEntry(tokens, entry) }))
    .filter((row) => row.score >= 3)
    .sort((a, b) => b.score - a.score);
  if (!ranked.length) return null;
  const runner = ranked[1] && ranked[1].score >= ranked[0].score * 0.72 ? ranked[1].entry : null;
  return { entry: ranked[0].entry, runner };
}

function tokenize(value) {
  return norm(value).split(" ").filter((token) => token.length > 2 && !STOP.has(token));
}

function norm(value) {
  return String(value || "").toLowerCase().replace(/[^a-z0-9+# ]/g, " ").replace(/\s+/g, " ").trim();
}

function scoreEntry(tokens, entry) {
  const bag = [...entry.keywords, ...(entry.synonyms || [])].map(norm).filter(Boolean);
  let score = 0;
  tokens.forEach((token) => {
    bag.forEach((word) => {
      if (word === token) score += 3;
      else if (word.includes(token) || token.includes(word)) score += 2;
      else if (token.length > 4 && word.length > 4 && editDistance(token, word) <= (token.length > 7 ? 2 : 1)) score += 1;
    });
  });
  const title = norm(entry.title);
  if (title && tokens.every((token) => title.includes(token))) score += 2;
  return score;
}

function editDistance(a, b) {
  if (Math.abs(a.length - b.length) > 2) return 9;
  const row = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i += 1) {
    let prev = row[0];
    row[0] = i;
    for (let j = 1; j <= b.length; j += 1) {
      const cur = row[j];
      row[j] = a[i - 1] === b[j - 1] ? prev : Math.min(prev, row[j], row[j - 1]) + 1;
      prev = cur;
    }
  }
  return row[b.length];
}

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
}
