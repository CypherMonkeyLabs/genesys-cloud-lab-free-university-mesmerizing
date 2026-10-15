/** Charts from this lab’s own manifest, diagram atlas, and port table. Not production Genesys metrics. */
import * as d3 from "../vendor/d3.js";
import rough from "../vendor/rough.js";
import { animate } from "../vendor/anime.js";
import { DIAGRAMS, PORTS } from "./diagrams.js";

export const CHARTS = [
  { id: "lessons", title: "Lessons per track", note: "Counted from this lab’s manifest." },
  { id: "minutes", title: "Minutes per track", note: "Sum of the minutes field on each lesson stub." },
  { id: "levels", title: "Lesson levels", note: "Foundation, Core, and Advanced labels in the manifest." },
  { id: "quizzes", title: "Quiz items per track", note: "Each lesson ships six quiz items." },
  { id: "kinds", title: "Diagram kinds", note: "Counted from the diagram atlas in this repo." },
  { id: "ports", title: "Ports by protocol", note: "Rows in the cited port table. Not a full firewall matrix." }
];

const SHORT = {
  foundations: "Foundations",
  org: "Org",
  architect: "Architect",
  acd: "ACD",
  queues: "Queues",
  byoc: "BYOC",
  edge: "Edge",
  emergency: "Emergency",
  wfm: "WFM",
  qm: "Quality",
  sta: "Analytics",
  ai: "AI",
  api: "APIs",
  crm: "CRM",
  migration: "Migration",
  ecosystem: "Ecosystem",
  predictive: "Predictive"
};

const PALETTE = ["#ff5a36", "#8fd4ff", "#d6f25c", "#b3a6ff", "#ff7ad9", "#ffc14d"];

export async function mountFloor(host, manifest, highlightId) {
  if (!host || !manifest) return;
  const tracks = manifest.tracks;
  const lessonRows = tracks.map((track) => ({
    id: track.id,
    label: SHORT[track.id] || track.title,
    value: track.lessons.length
  }));
  const minuteRows = tracks.map((track) => ({
    id: track.id,
    label: SHORT[track.id] || track.title,
    value: track.lessons.reduce((sum, lesson) => sum + (lesson.minutes || 0), 0)
  }));
  const quizRows = tracks.map((track) => ({
    id: track.id,
    label: SHORT[track.id] || track.title,
    value: track.lessons.length * 6
  }));
  const levels = new Map();
  tracks.forEach((track) => {
    track.lessons.forEach((lesson) => {
      const key = lesson.level || "Unlabeled";
      levels.set(key, (levels.get(key) || 0) + 1);
    });
  });
  const kinds = new Map();
  DIAGRAMS.forEach((item) => kinds.set(item.kind, (kinds.get(item.kind) || 0) + 1));
  const protos = new Map();
  PORTS.forEach((item) => protos.set(item.proto, (protos.get(item.proto) || 0) + 1));

  const blocks = [
    { spec: CHARTS[0], node: bars(CHARTS[0].title, lessonRows, highlightId) },
    { spec: CHARTS[1], node: bars(CHARTS[1].title, minuteRows, highlightId) },
    { spec: CHARTS[2], node: donut(CHARTS[2].title, [...levels.entries()].map(([label, value]) => ({ label, value }))) },
    { spec: CHARTS[3], node: bars(CHARTS[3].title, quizRows, highlightId) },
    { spec: CHARTS[4], node: bars(CHARTS[4].title, [...kinds.entries()].map(([label, value]) => ({ id: label, label, value })), null) },
    { spec: CHARTS[5], node: bars(CHARTS[5].title, [...protos.entries()].map(([label, value]) => ({ id: label, label, value })), null) }
  ];

  host.innerHTML = `<div class="chart-grid">${blocks.map((block) => `<article class="card chart-card"><h3>${escapeHtml(block.spec.title)}</h3><div class="chart-svg"></div><p class="muted">${escapeHtml(block.spec.note)}</p></article>`).join("")}</div>`;
  host.querySelectorAll(".chart-svg").forEach((slot, index) => {
    slot.appendChild(blocks[index].node);
  });
  grow(host);
  wireTips(host);
}

function wireTips(host) {
  host.querySelectorAll(".chart-card").forEach((card) => {
    const tip = document.createElement("div");
    tip.className = "chart-tip";
    tip.hidden = true;
    card.appendChild(tip);
    card.addEventListener("pointermove", (ev) => {
      const hit = ev.target.closest ? ev.target.closest("[data-label]") : null;
      if (!hit) {
        tip.hidden = true;
        return;
      }
      tip.hidden = false;
      tip.textContent = `${hit.dataset.label}: ${hit.dataset.value}`;
      const bounds = card.getBoundingClientRect();
      tip.style.left = Math.max(8, ev.clientX - bounds.left + 14) + "px";
      tip.style.top = Math.max(8, ev.clientY - bounds.top + 14) + "px";
    });
    card.addEventListener("pointerleave", () => { tip.hidden = true; });
  });
}

function bars(title, rows, highlightId) {
  const w = 640;
  const rowH = 22;
  const h = 28 + rows.length * rowH;
  const labelW = 108;
  const svg = d3.create("svg").attr("viewBox", `0 0 ${w} ${h}`).attr("role", "img").attr("aria-label", title);
  const node = svg.node();
  sketchFrame(node, w, h);
  const max = d3.max(rows, (row) => row.value) || 1;
  const x = d3.scaleLinear().domain([0, max]).range([0, w - labelW - 36]);
  rows.forEach((row, i) => {
    const y = 16 + i * rowH;
    const width = Math.max(2, x(row.value));
    const on = highlightId && row.id === highlightId;
    svg.append("text")
      .attr("x", 10)
      .attr("y", y + 12)
      .attr("fill", "currentColor")
      .attr("font-size", 11)
      .attr("font-weight", on ? 700 : 400)
      .text(row.label);
    svg.append("rect")
      .attr("class", "bar")
      .attr("data-w", String(width))
      .attr("data-label", row.label)
      .attr("data-value", String(row.value))
      .attr("x", labelW)
      .attr("y", y)
      .attr("height", 14)
      .attr("width", width)
      .attr("rx", 4)
      .attr("fill", on ? "#ff5a36" : PALETTE[i % PALETTE.length]);
    svg.append("text")
      .attr("x", labelW + width + 6)
      .attr("y", y + 12)
      .attr("fill", "currentColor")
      .attr("font-size", 11)
      .text(String(row.value));
  });
  return node;
}

function donut(title, rows) {
  const w = 420;
  const h = 240;
  const svg = d3.create("svg").attr("viewBox", `0 0 ${w} ${h}`).attr("role", "img").attr("aria-label", title);
  const node = svg.node();
  sketchFrame(node, w, h);
  const pie = d3.pie().sort(null).value((row) => row.value);
  const arc = d3.arc().innerRadius(52).outerRadius(86);
  const g = svg.append("g").attr("transform", "translate(120,120)");
  pie(rows).forEach((slice, i) => {
    g.append("path")
      .attr("class", "slice")
      .attr("data-label", slice.data.label)
      .attr("data-value", String(slice.data.value))
      .attr("d", arc(slice))
      .attr("fill", PALETTE[i % PALETTE.length]);
  });
  rows.forEach((row, i) => {
    svg.append("rect").attr("x", 230).attr("y", 48 + i * 28).attr("width", 14).attr("height", 14).attr("fill", PALETTE[i % PALETTE.length]);
    svg.append("text").attr("x", 252).attr("y", 60 + i * 28).attr("fill", "currentColor").attr("font-size", 14).text(`${row.label} · ${row.value}`);
  });
  return node;
}

function sketchFrame(node, w, h) {
  const rc = rough.svg(node, { options: { roughness: 1.15, bowing: 0.6 } });
  const frame = rc.rectangle(3, 3, w - 6, h - 6, { stroke: "#b3a6ff", strokeWidth: 1.4, roughness: 1.2 });
  node.insertBefore(frame, node.firstChild);
}

function grow(host) {
  const barsEls = host.querySelectorAll(".bar");
  barsEls.forEach((el) => {
    el.dataset.full = el.dataset.w;
    el.setAttribute("width", "0");
  });
  try {
    animate(barsEls, {
      width: (_el, i) => Number(barsEls[i].dataset.full),
      duration: 900,
      ease: "out(3)",
      delay: (_el, i) => (i % 17) * 18
    });
  } catch (err) {
    barsEls.forEach((el) => el.setAttribute("width", el.dataset.full));
  }
  setTimeout(() => {
    barsEls.forEach((el) => {
      if (Number(el.getAttribute("width")) < 1) el.setAttribute("width", el.dataset.full);
    });
  }, 1400);
  const slices = host.querySelectorAll(".slice");
  try {
    animate(slices, { opacity: [0, 1], duration: 500, delay: (_el, i) => i * 90 });
  } catch (err) {
    slices.forEach((el) => { el.style.opacity = "1"; });
  }
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
}
