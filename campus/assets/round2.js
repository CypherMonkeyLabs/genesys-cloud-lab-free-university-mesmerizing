/* Room downloads, display controls, and the short quiz on Help and Legal. */
const DISCLAIMER = "This is an independent, free, learning-only student project. It respects every company and vendor, and every trademark belongs to its owner. It is not affiliated with or endorsed by any of them. If anyone has a concern, the content will be removed or corrected promptly via the contact form at https://cyphermonkeylabs.com/#contact. Nothing here is sold, and I am happy to volunteer for any organization.";

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
}

function sectionOf(node) {
  const heading = node.closest("h2");
  if (heading) {
    const range = document.createElement("div");
    range.appendChild(heading.cloneNode(true));
    let sib = heading.nextElementSibling;
    while (sib && sib.tagName !== "H2") {
      range.appendChild(sib.cloneNode(true));
      sib = sib.nextElementSibling;
    }
    return range;
  }
  return (node.closest("section, article, .panel, main") || document.getElementById("main")).cloneNode(true);
}

function standaloneHtml(title, inner) {
  return `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>${esc(title)}</title>
<style>
body{font:18px/1.5 Georgia,serif;margin:32px auto;max-width:760px;color:#1b1230;background:#fff7fb}
.disclaimer-panel{border:2px solid #0f766e;border-radius:16px;padding:16px;background:linear-gradient(135deg,#dcfce7,#dbeafe);color:#0b1f2a}
.sources-deeper{margin-top:28px;padding:16px;border:2px solid #0f766e;border-radius:16px;background:#f0fdfa;color:#042f2e}
.sources-deeper a{color:#08306b}
.src-flag{background:#fde68a;color:#422006;font-weight:800;padding:0 6px;border-radius:999px}
a{color:#5b21b6}
</style></head><body>
<h1>${esc(title)}</h1>
${inner}
<aside class="disclaimer-panel"><h2>A note from the student behind this lab</h2><p>${esc(DISCLAIMER)}</p></aside>
<p>CypherMonkey Labs</p>
<p><a href="https://cyphermonkeylabs.com">Website</a> · <a href="https://github.com/CypherMonkeyLabs">GitHub organization</a> · <a href="https://linktr.ee/cypherMonkey">Linktree</a></p>
<p>© 2026 CypherMonkeyLabs</p>
</body></html>`;
}

function downloadBlob(name, blob) {
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = name;
  link.click();
  setTimeout(() => URL.revokeObjectURL(link.href), 1500);
}

function slug(text) {
  return String(text || "room").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 40) || "room";
}

function liveSources() {
  const home = document.getElementById("home");
  const view = document.getElementById("view");
  const root = home && !home.hidden ? home : view;
  return root?.querySelector(".sources-deeper") || document.querySelector(".sources-deeper");
}

function ensureSources(scope) {
  if (scope.querySelector(".sources-deeper")) return;
  const block = liveSources();
  if (block) scope.appendChild(block.cloneNode(true));
}

function svgBox(svg) {
  const viewBox = svg.getAttribute("viewBox");
  if (viewBox) {
    const parts = viewBox.split(/[\s,]+/).map(Number);
    if (parts.length === 4 && parts[2] > 0 && parts[3] > 0) return { w: parts[2], h: parts[3] };
  }
  return {
    w: parseFloat(svg.getAttribute("width")) || 800,
    h: parseFloat(svg.getAttribute("height")) || 360
  };
}

function svgWithSources(svg, title) {
  const block = liveSources();
  const links = block ? [...block.querySelectorAll("a")] : [];
  const box = svg ? svgBox(svg) : { w: 640, h: 120 };
  const head = 72;
  const picture = svg ? box.h + 16 : 80;
  const height = head + picture + 56 + links.length * 22 + 48;
  const width = Math.max(720, box.w || 720);
  const pictureMarkup = svg
    ? `<g transform="translate(24,${head})">${svg.outerHTML}</g>`
    : `<text x="24" y="${head + 28}" font-size="16" fill="#3d3358">${esc(DISCLAIMER.slice(0, 180))}</text>`;
  const rows = links.map((link, index) => {
    const flag = link.parentElement?.querySelector(".src-flag") ? " confirm" : "";
    const label = `${link.textContent.trim()} ${link.getAttribute("href") || ""}${flag}`.slice(0, 140);
    const y = head + picture + 36 + index * 22;
    return `<text x="24" y="${y}" font-size="14" fill="#08306b">${esc(label)}</text>`;
  }).join("");
  const checkedY = head + picture + 16;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
<rect width="${width}" height="${height}" fill="#f0fdfa"/>
<text x="24" y="42" font-size="22" fill="#042f2e">${esc(title)}</text>
${pictureMarkup}
<text x="24" y="${checkedY}" font-size="18" fill="#042f2e">Sources and go deeper</text>
<text x="320" y="${checkedY}" font-size="14" fill="#042f2e">Last checked 2026-10</text>
${rows}
</svg>`;
}

async function exportNode(node, kind) {
  if (window.gccxSourcesReady) {
    try { await window.gccxSourcesReady; } catch (err) { /* the export still carries the disclaimer */ }
  }
  const scope = sectionOf(node);
  scope.querySelectorAll("button, .dl-bar, .dl-mini").forEach((el) => el.remove());
  ensureSources(scope);
  const title = scope.querySelector("h1, h2")?.textContent?.trim() || document.title;
  if (kind === "svg") {
    const body = svgWithSources(scope.querySelector("svg"), title);
    downloadBlob(slug(title) + ".svg", new Blob([body], { type: "image/svg+xml" }));
    return;
  }
  if (kind === "png") {
    const canvas = document.createElement("canvas");
    canvas.width = 960;
    canvas.height = 540;
    const g = canvas.getContext("2d");
    g.fillStyle = "#fff7fb";
    g.fillRect(0, 0, 960, 540);
    g.fillStyle = "#7c3aed";
    g.fillRect(0, 0, 960, 12);
    g.fillStyle = "#1b1230";
    g.font = "28px Georgia, serif";
    g.fillText(title.slice(0, 48), 32, 64);
    g.font = "16px Georgia, serif";
    const words = (scope.innerText || title).replace(/\s+/g, " ").slice(0, 280).split(" ");
    let line = "";
    let y = 110;
    words.forEach((word) => {
      const trial = line ? line + " " + word : word;
      if (trial.length > 70) {
        if (y < 430) g.fillText(line, 32, y);
        y += 26;
        line = word;
      } else line = trial;
    });
    if (line && y < 430) g.fillText(line, 32, y);
    g.font = "bold 18px Georgia, serif";
    g.fillText("Sources and go deeper", 32, 470);
    g.font = "16px Georgia, serif";
    g.fillText("Last checked 2026-10", 32, 498);
    if (scope.querySelector(".src-flag")) g.fillText("confirm", 280, 498);
    const blob = await new Promise((resolve) => canvas.toBlob(resolve, "image/png"));
    if (blob) downloadBlob(slug(title) + ".png", blob);
    return;
  }
  const html = standaloneHtml(title, scope.innerHTML);
  downloadBlob(slug(title) + ".html", new Blob([html], { type: "text/html" }));
}

function decorate(root) {
  if (!root) return;
  root.querySelectorAll("h2").forEach((heading) => {
    if (heading.dataset.dl === "1" || heading.closest(".floor-menu, .site-footer, .bot-panel, .disclaimer-panel")) return;
    heading.dataset.dl = "1";
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "dl-mini";
    btn.dataset.export = "html";
    btn.textContent = "Download";
    heading.appendChild(btn);
  });
  if (!root.querySelector(".dl-bar")) {
    const bar = document.createElement("div");
    bar.className = "dl-bar";
    bar.innerHTML = `<span class="dl-kicker">Download</span><button type="button" class="dl-mini" data-export="html">HTML</button><button type="button" class="dl-mini" data-export="svg">SVG</button><button type="button" class="dl-mini" data-export="png">PNG</button><a class="dl-mini" href="downloads/genesys-cx-offline-bundle.zip">Bundle</a>`;
    const heading = root.querySelector("h1");
    if (heading) heading.insertAdjacentElement("afterend", bar);
    else root.prepend(bar);
  }
  if (root.id === "view" && !root.querySelector(".learn5")) {
    const block = document.createElement("section");
    block.className = "learn5";
    block.id = "sec-learn5";
    block.innerHTML = `<h2 data-dl="1">Learn it in 5 minutes</h2>
      <ol>
        <li>This is a study room in the Genesys Cloud CX lab. It does not sign in to an organization.</li>
        <li>Figures are teaching sketches. The cited page wins when they disagree.</li>
        <li>A saved Architect draft does not answer a live call. Publish the flow.</li>
        <li>Use the download button if you want a standalone copy with the disclaimer.</li>
        <li>Confirm before relying on any sentence marked uncertain.</li>
      </ol>`;
    const bar = root.querySelector(".dl-bar");
    if (bar) bar.insertAdjacentElement("afterend", block);
  }
  if (root.id === "view" && !root.querySelector(".eco-panel")) {
    const eco = document.createElement("section");
    eco.className = "eco-panel";
    eco.id = "sec-eco";
    eco.innerHTML = `<h2>Ecosystem</h2>
      <h3>Glossary</h3><p><a href="#/glossary">Glossary</a> terms each link to a source.</p>
      <h3>Mind map</h3><p>Open the <a href="#/ecosystem">ecosystem map</a> for organization, Architect, queues, trunks, and WEM.</p>
      <h3>Sister technologies</h3><p>SIP and RTP are different. Confirm the firewall article before opening a port range.</p>
      <h3>Config and troubleshooting</h3><p>Publish the flow. No audio after a healthy flow is media. Confirm before relying.</p>
      <h3>Integration maps</h3><p>Salesforce and Zendesk have their own articles. Other products stay on AppFoundry.</p>
      <h3>Cross-platform bridges</h3><p>Engage, PureConnect, and Cisco UCCE / UCCX are rebuild notes, not converters.</p>
      <h3>Future hooks</h3><p>Journey Outcomes listed a planned effective date of 2026-06-29. If the page moves, the page wins.</p>
      <h3>Worked example</h3><p>Read the figure, then the lab steps on a Foundations lesson. The studio does not call Genesys.</p>
      <form class="panel mini-quiz" data-mini-quiz data-answer="0">
        <p>Does a saved Architect draft answer a live call?</p>
        <label><input type="radio" name="roomq" value="0"> No. Publish the flow.</label>
        <label><input type="radio" name="roomq" value="1"> Yes, as soon as you save.</label>
        <button type="button" class="btn" data-quiz-check>Check</button>
        <p class="muted" data-quiz-note></p>
      </form>
      <p>Source: <a href="https://help.genesys.cloud/articles/create-a-flow/">Create a flow</a></p>`;
    root.appendChild(eco);
  }
}

function setFont(size) {
  document.querySelectorAll("[data-font-set]").forEach((btn) => {
    btn.setAttribute("aria-pressed", btn.dataset.fontSet === size ? "true" : "false");
  });
  window.gccxSettings?.patch({ font: size });
}

function setInk(value) {
  if (!/^#[0-9a-fA-F]{6}$/.test(value)) return;
  window.gccxSettings?.patch({ ink: value });
  document.querySelectorAll('input[type="color"]').forEach((input) => { input.value = value; });
}

function wireDisplay() {
  const btn = document.getElementById("display-btn");
  const panel = document.getElementById("display-panel");
  btn?.addEventListener("click", (ev) => {
    ev.stopPropagation();
    const open = panel.hidden;
    panel.hidden = !open;
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
  document.addEventListener("click", (ev) => {
    const fontBtn = ev.target.closest("[data-font-set]");
    if (fontBtn) setFont(fontBtn.dataset.fontSet);
    if (panel && !panel.hidden && !panel.contains(ev.target) && ev.target !== btn) {
      panel.hidden = true;
      btn?.setAttribute("aria-expanded", "false");
    }
  });
  document.addEventListener("input", (ev) => {
    if (ev.target instanceof HTMLInputElement && ev.target.type === "color") setInk(ev.target.value);
  });
  document.addEventListener("click", (ev) => {
    const link = ev.target.closest("a[href='#listen']");
    if (!link) return;
    ev.preventDefault();
    sessionStorage.setItem("gccx-listen", "1");
    if ((location.hash || "#/") === "#/") document.getElementById("listen")?.scrollIntoView({ block: "start" });
    else location.hash = "#/";
  });
}

document.addEventListener("click", async (ev) => {
  const quiz = ev.target.closest("[data-quiz-check]");
  if (quiz) {
    const form = quiz.closest("[data-mini-quiz]");
    const picked = form?.querySelector("input:checked")?.value;
    const note = form?.querySelector("[data-quiz-note]");
    if (!note) return;
    note.textContent = picked === form.dataset.answer ? "That's the note in this lab." : "Check the lesson again. Confirm before relying.";
    return;
  }
  const btn = ev.target.closest("[data-export]");
  if (!btn || btn.tagName === "A") return;
  ev.preventDefault();
  await exportNode(btn, btn.dataset.export || "html");
});

document.addEventListener("click", async (ev) => {
  if (!ev.target.closest(".open-app")) return;
  const prompt = window.gccxInstall;
  if (prompt) {
    prompt.prompt();
    await prompt.userChoice;
    window.gccxInstall = null;
    return;
  }
  location.hash = "#/";
});
window.addEventListener("beforeinstallprompt", (ev) => {
  ev.preventDefault();
  window.gccxInstall = ev;
});

function startAtmosphere() {
  const hero = document.getElementById("hero-bleed");
  if (!hero || hero.querySelector(".fx-field")) return;
  const field = document.createElement("div");
  field.className = "fx-field";
  field.setAttribute("aria-hidden", "true");
  for (let i = 0; i < 16; i += 1) {
    const dot = document.createElement("i");
    dot.style.left = (6 + ((i * 17) % 88)) + "%";
    dot.style.top = (8 + ((i * 23) % 62)) + "%";
    dot.style.animationDelay = (-(i * 0.7)) + "s";
    dot.style.animationDuration = (7 + (i % 5)) + "s";
    field.appendChild(dot);
  }
  const stage = document.createElement("div");
  stage.className = "hero-3d";
  stage.setAttribute("aria-hidden", "true");
  stage.innerHTML = '<div class="obj o1"><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="obj o2"><i></i><i></i><i></i></div><div class="obj o3"><i></i><i></i><i></i></div>';
  hero.appendChild(field);
  hero.appendChild(stage);
  if (document.documentElement.dataset.reduce === "1" || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  let frame = 0;
  window.addEventListener("scroll", () => {
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      const y = Math.min(window.scrollY, 360);
      field.style.transform = "translate3d(0," + (y * 0.16) + "px,0)";
      const canvas = document.getElementById("hero-canvas");
      if (canvas) canvas.style.transform = "translate3d(0," + (y * 0.07) + "px,0)";
    });
  }, { passive: true });
}

window.gccxDecorate = decorate;
wireDisplay();
decorate(document.getElementById("home"));
startAtmosphere();
