/** Enlarge a diagram. Play, pause, and step move a teaching marker. */

const STOPS = [8, 26, 44, 62, 80];
let step = 0;
let playing = false;
let wired = false;

export function ensureLightbox() {
  if (wired) return;
  const dialog = document.querySelector("#lx");
  if (!dialog) return;
  wired = true;
  document.querySelector("#lx-play")?.addEventListener("click", () => play());
  document.querySelector("#lx-pause")?.addEventListener("click", () => pause());
  document.querySelector("#lx-step")?.addEventListener("click", () => stepOnce());
  document.querySelector("#lx-close")?.addEventListener("click", () => dialog.close());
  dialog.addEventListener("close", () => pause());
  dialog.addEventListener("click", (ev) => {
    if (ev.target === dialog) dialog.close();
  });
}

export function wireLightbox(root) {
  ensureLightbox();
  if (!root || root.dataset.lx === "1") return;
  root.dataset.lx = "1";
  root.addEventListener("click", (ev) => {
    if (ev.target.closest("a")) return;
    const open = ev.target.closest(".lx-open, svg.diagram, .mermaid-svg");
    if (!open) return;
    const card = ev.target.closest(".lx-card");
    if (!card) return;
    ev.preventDefault();
    openLightbox(card);
  });
}

export function openLightbox(card) {
  ensureLightbox();
  const dialog = document.querySelector("#lx");
  const stage = document.querySelector("#lx-stage");
  const why = document.querySelector("#lx-why");
  const legend = document.querySelector("#lx-legend");
  if (!dialog || !stage) return;
  const title = card.querySelector("h3")?.textContent || "Diagram";
  const caption = card.dataset.why || card.querySelector(".lx-why")?.textContent || card.querySelector("p")?.textContent || "";
  const media = card.querySelector("svg.diagram, .mermaid-svg img, img");
  stage.innerHTML = "";
  const heading = document.createElement("h2");
  heading.textContent = title;
  stage.appendChild(heading);
  if (media) {
    const frame = document.createElement("div");
    frame.className = "lx-frame";
    frame.appendChild(media.cloneNode(true));
    const packet = document.createElement("span");
    packet.className = "lx-packet";
    packet.dataset.step = "0";
    frame.appendChild(packet);
    stage.appendChild(frame);
  }
  if (why) why.textContent = "Why this matters: " + caption;
  if (legend) {
    legend.textContent = "Legend · colored nodes are parties on the path (carrier, trunk, Architect, queue, agent, or the labels in the drawing). The dashed stroke is the path. The moving dot is a teaching marker, not a packet capture.";
  }
  step = 0;
  place();
  dialog.showModal();
  play();
}

function packet() {
  return document.querySelector("#lx-stage .lx-packet");
}

function place() {
  const dot = packet();
  if (!dot) return;
  dot.style.left = STOPS[step] + "%";
  dot.dataset.step = String(step);
}

function play() {
  const dot = packet();
  if (!dot) return;
  playing = true;
  dot.classList.add("is-on");
}

function pause() {
  playing = false;
  packet()?.classList.remove("is-on");
}

function stepOnce() {
  pause();
  step = (step + 1) % STOPS.length;
  place();
}
