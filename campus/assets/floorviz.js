/** Charts from this lab’s own manifest, diagram atlas, and port table. Not production Genesys metrics. */
import * as d3 from "../vendor/d3.js";
import rough from "../vendor/rough.js";
import { animate } from "../vendor/anime.js";
import { DIAGRAMS, PORTS } from "./diagrams.js";

const REPO = "https://github.com/cipher0x9/genesys-cloud-lab-free-university-mesmerizing";
const PORTS_DOC = "https://help.genesys.cloud/articles/genesys-cloud-ports-services/";

export const CHARTS = [
  { id: "lessons", title: "Lessons per track", note: "Counted from this lab’s manifest. Not a production metric.", source: REPO },
  { id: "minutes", title: "Minutes per track", note: "Sum of the minutes field on each lesson stub in this repo.", source: REPO },
  { id: "levels", title: "Lesson levels", note: "Foundation, Core, and Advanced labels in the manifest.", source: REPO },
  { id: "quizzes", title: "Quiz items per track", note: "Each lesson ships six quiz items. Counted here, not from an exam vendor.", source: REPO },
  { id: "kinds", title: "Diagram kinds", note: "Counted from the diagram atlas in this repo.", source: REPO },
  { id: "ports", title: "Ports by protocol", note: "Rows in this lab’s port table, which cites the firewall article. Not a full firewall matrix.", source: PORTS_DOC }
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
    { spec: CHARTS[0], node: radial(CHARTS[0].title, lessonRows, highlightId) },
    { spec: CHARTS[1], node: areaChart(CHARTS[1].title, minuteRows, highlightId) },
    { spec: CHARTS[2], node: donut(CHARTS[2].title, [...levels.entries()].map(([label, value]) => ({ label, value }))) },
    { spec: CHARTS[3], node: lollipop(CHARTS[3].title, quizRows, highlightId) },
    { spec: CHARTS[4], node: rose(CHARTS[4].title, [...kinds.entries()].map(([label, value]) => ({ id: label, label, value }))) },
    { spec: CHARTS[5], node: radial(CHARTS[5].title, [...protos.entries()].map(([label, value]) => ({ id: label, label, value })), null) }
  ];

  host.innerHTML = `<div class="chart-grid">${blocks.map((block) => `<article class="card chart-card"><h3>${escapeHtml(block.spec.title)}</h3><div class="chart-svg"></div><p class="muted">${escapeHtml(block.spec.note)}</p><p class="muted"><a href="${escapeHtml(block.spec.source)}">Source</a></p></article>`).join("")}</div>`;
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

function radial(title, rows, highlightId) {
  const w = 980;
  const h = 760;
  const svg = d3.create("svg").attr("class", "radial-chart").attr("viewBox", `0 0 ${w} ${h}`).attr("role", "img").attr("aria-label", title);
  const node = svg.node();
  sketchFrame(node, w, h);
  const max = d3.max(rows, (row) => row.value) || 1;
  const cx = w / 2;
  const cy = h / 2 + 8;
  const inner = 46;
  const outer = 168;
  const arc = d3.arc().innerRadius(inner);
  const step = (Math.PI * 2) / Math.max(1, rows.length);
  rows.forEach((row, i) => {
    const start = i * step;
    const end = start + step * 0.72;
    const radius = inner + (outer - inner) * (row.value / max);
    const on = highlightId && row.id === highlightId;
    svg.append("path")
      .attr("class", "radial-bar")
      .attr("transform", `translate(${cx},${cy})`)
      .attr("data-label", row.label)
      .attr("data-value", String(row.value))
      .attr("d", arc.outerRadius(radius).startAngle(start).endAngle(end)())
      .attr("fill", on ? "#ff5a36" : PALETTE[i % PALETTE.length])
      .attr("opacity", 0.92);
    const labelArc = d3.arc().innerRadius(outer + 96).outerRadius(outer + 96);
    const [lx, ly] = labelArc.centroid({ startAngle: start, endAngle: end });
    const anchor = lx > 20 ? "start" : lx < -20 ? "end" : "middle";
    const nudge = anchor === "start" ? 8 : anchor === "end" ? -8 : 0;
    svg.append("text")
      .attr("x", cx + lx + nudge)
      .attr("y", cy + ly)
      .attr("text-anchor", anchor)
      .attr("fill", "currentColor")
      .attr("font-size", 18)
      .text(row.label);
  });
  return node;
}

function areaChart(title, rows, highlightId) {
  const w = 680;
  const h = 340;
  const svg = d3.create("svg").attr("viewBox", `0 0 ${w} ${h}`).attr("role", "img").attr("aria-label", title);
  const node = svg.node();
  sketchFrame(node, w, h);
  const max = d3.max(rows, (row) => row.value) || 1;
  const x = d3.scalePoint().domain(rows.map((row) => row.label)).range([56, w - 28]).padding(0.3);
  const y = d3.scaleLinear().domain([0, max]).range([h - 64, 28]);
  const area = d3.area().x((row) => x(row.label)).y0(y(0)).y1((row) => y(row.value)).curve(d3.curveCatmullRom.alpha(0.5));
  const line = d3.line().x((row) => x(row.label)).y((row) => y(row.value)).curve(d3.curveCatmullRom.alpha(0.5));
  svg.append("path").attr("class", "area-fill").attr("d", area(rows)).attr("fill", "#2ff7ff").attr("opacity", 0.38);
  svg.append("path").attr("d", line(rows)).attr("fill", "none").attr("stroke", "#ff2fb3").attr("stroke-width", 3);
  rows.forEach((row, i) => {
    const on = highlightId && row.id === highlightId;
    svg.append("circle")
      .attr("class", "plot-dot")
      .attr("cx", x(row.label))
      .attr("cy", y(row.value))
      .attr("r", on ? 9 : 7)
      .attr("data-r", on ? "9" : "7")
      .attr("data-label", row.label)
      .attr("data-value", String(row.value))
      .attr("fill", on ? "#ff5a36" : PALETTE[i % PALETTE.length]);
    svg.append("text")
      .attr("x", x(row.label))
      .attr("y", h - 28)
      .attr("text-anchor", "end")
      .attr("fill", "currentColor")
      .attr("font-size", 10)
      .attr("transform", `rotate(-55 ${x(row.label)} ${h - 28})`)
      .text(row.label);
  });
  return node;
}

function lollipop(title, rows, highlightId) {
  const w = 680;
  const h = 360;
  const svg = d3.create("svg").attr("viewBox", `0 0 ${w} ${h}`).attr("role", "img").attr("aria-label", title);
  const node = svg.node();
  sketchFrame(node, w, h);
  const max = d3.max(rows, (row) => row.value) || 1;
  const x = d3.scalePoint().domain(rows.map((row) => row.label)).range([40, w - 24]).padding(0.4);
  const y = d3.scaleLinear().domain([0, max]).range([h - 72, 24]);
  rows.forEach((row, i) => {
    const on = highlightId && row.id === highlightId;
    const color = on ? "#ff5a36" : PALETTE[i % PALETTE.length];
    svg.append("line")
      .attr("class", "lolli")
      .attr("x1", x(row.label))
      .attr("x2", x(row.label))
      .attr("y1", y(0))
      .attr("y2", y(row.value))
      .attr("stroke", color)
      .attr("stroke-width", 3)
      .attr("data-label", row.label)
      .attr("data-value", String(row.value));
    svg.append("circle")
      .attr("class", "lolli-dot")
      .attr("cx", x(row.label))
      .attr("cy", y(row.value))
      .attr("r", 8)
      .attr("data-r", "8")
      .attr("data-label", row.label)
      .attr("data-value", String(row.value))
      .attr("fill", color);
    svg.append("text")
      .attr("x", x(row.label))
      .attr("y", h - 36)
      .attr("text-anchor", "end")
      .attr("fill", "currentColor")
      .attr("font-size", 10)
      .attr("transform", `rotate(-55 ${x(row.label)} ${h - 36})`)
      .text(row.label);
  });
  return node;
}

function rose(title, rows) {
  const w = 640;
  const h = 420;
  const svg = d3.create("svg").attr("viewBox", `0 0 ${w} ${h}`).attr("role", "img").attr("aria-label", title);
  const node = svg.node();
  sketchFrame(node, w, h);
  const max = d3.max(rows, (row) => row.value) || 1;
  const pie = d3.pie().sort(null).value(() => 1);
  const arc = d3.arc().innerRadius(36);
  const g = svg.append("g").attr("transform", "translate(210,210)");
  pie(rows).forEach((slice, i) => {
    const outer = 48 + 120 * (slice.data.value / max);
    g.append("path")
      .attr("class", "rose")
      .attr("data-label", slice.data.label)
      .attr("data-value", String(slice.data.value))
      .attr("d", arc.outerRadius(outer)(slice))
      .attr("fill", PALETTE[i % PALETTE.length]);
    svg.append("rect").attr("x", 430).attr("y", 36 + i * 22).attr("width", 12).attr("height", 12).attr("fill", PALETTE[i % PALETTE.length]);
    svg.append("text").attr("x", 450).attr("y", 46 + i * 22).attr("fill", "currentColor").attr("font-size", 12).text(`${slice.data.label} · ${slice.data.value}`);
  });
  return node;
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
  const marks = host.querySelectorAll(".radial-bar, .rose, .area-fill, .slice");
  marks.forEach((el) => { el.style.opacity = "0"; });
  const dots = host.querySelectorAll(".plot-dot, .lolli-dot");
  dots.forEach((el) => el.setAttribute("r", "0"));
  const stems = host.querySelectorAll(".lolli");
  stems.forEach((el) => {
    el.dataset.y2 = el.getAttribute("y2");
    el.setAttribute("y2", el.getAttribute("y1"));
  });
  try {
    if (marks.length) {
      animate(marks, { opacity: 1, duration: 700, ease: "out(3)", delay: (_el, i) => (i % 24) * 28 });
    }
    if (dots.length) {
      animate(dots, {
        r: (_el, i) => Number(dots[i].dataset.r || 7),
        duration: 800,
        ease: "out(3)",
        delay: (_el, i) => i * 24
      });
    }
    if (stems.length) {
      animate(stems, {
        y2: (_el, i) => Number(stems[i].dataset.y2),
        duration: 800,
        ease: "out(3)",
        delay: (_el, i) => i * 20
      });
    }
  } catch (err) {
    marks.forEach((el) => { el.style.opacity = "1"; });
    dots.forEach((el) => el.setAttribute("r", el.dataset.r || "7"));
    stems.forEach((el) => el.setAttribute("y2", el.dataset.y2));
  }
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
}
