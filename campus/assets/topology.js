const NODES = [
  { id: "carrier", label: "Carrier", kind: "voice", x: -6, y: 0.4, z: 2 },
  { id: "sbc", label: "SBC", kind: "voice", x: -4, y: 0.2, z: 1 },
  { id: "byoc", label: "BYOC Cloud", kind: "voice", x: -2, y: 1.2, z: 0 },
  { id: "edge", label: "Premises Edge", kind: "voice", x: -2, y: -1.1, z: 1.2 },
  { id: "media", label: "Media tier", kind: "core", x: 0, y: 0.4, z: 0 },
  { id: "architect", label: "Architect", kind: "core", x: 2, y: 1.3, z: -0.4 },
  { id: "acd", label: "ACD", kind: "core", x: 3.4, y: 0.2, z: 0.2 },
  { id: "queue", label: "Queue", kind: "core", x: 4.6, y: -0.6, z: 0.6 },
  { id: "agent", label: "Agent", kind: "people", x: 6.2, y: -0.2, z: 0.2 },
  { id: "bot", label: "Bot", kind: "ai", x: 2.2, y: -1.2, z: -0.8 },
  { id: "wem", label: "WEM", kind: "ai", x: 4.2, y: 1.5, z: -1 },
  { id: "crm", label: "CRM", kind: "people", x: 6, y: 1.2, z: -0.6 }
];

const LINKS = [
  ["carrier", "sbc"],
  ["sbc", "byoc"],
  ["sbc", "edge"],
  ["byoc", "media"],
  ["edge", "media"],
  ["media", "architect"],
  ["architect", "acd"],
  ["architect", "bot"],
  ["acd", "queue"],
  ["queue", "agent"],
  ["agent", "wem"],
  ["agent", "crm"]
];

const FAILURES = [
  { id: "trunk", label: "BYOC trunk down", cuts: [["sbc", "byoc"], ["byoc", "media"]], note: "Cloud media stops hearing the carrier. Premises Edge phones can still talk to the media tier if that path is healthy. Dynamic Cloud Voice moves require the carrier ACL to trust the current ingress addresses." },
  { id: "edge", label: "Local Edge offline", cuts: [["sbc", "edge"], ["edge", "media"]], note: "Documented local-site routing uses another site only when local Edges are offline, at capacity, or do not hold the resource. Callers on cloud trunks are unaffected." },
  { id: "queue", label: "No agent On Queue", cuts: [["queue", "agent"]], note: "ACD will not alert an agent who is off queue or at utilization. The in-queue flow keeps playing only if that flow was published." },
  { id: "bot", label: "Bot flow misses", cuts: [["architect", "bot"]], note: "A Call Bot Flow action that fails needs an Architect failure path, usually Transfer to ACD. The bot does not replace the queue." },
  { id: "crm", label: "Data action timeout", cuts: [["agent", "crm"]], note: "The conversation still routes. Screen pop and the Salesforce or Zendesk log are what stall. Client-credentials roles must include the division that owns the data action." }
];

export async function mountTopology(root, options) {
  const reduce = options.reduce || window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  root.innerHTML = `<div class="toolbar" id="fails"></div><div id="stage"></div><p id="fail-note"></p><p><a href="https://help.genesys.cloud/articles/byoc-cloud-overview/">BYOC Cloud overview</a> · <a href="https://help.genesys.cloud/articles/edge-groups-overview/">Edge groups</a></p>`;
  const fails = root.querySelector("#fails");
  fails.innerHTML = FAILURES.map((item) => `<button class="btn tiny" type="button" data-fail="${item.id}" aria-pressed="false">${item.label}</button>`).join("") +
    `<button class="btn tiny" type="button" id="flat">Flat map</button>`;
  const active = new Set();
  const note = root.querySelector("#fail-note");
  const stage = root.querySelector("#stage");
  let mode = reduce ? "flat" : "webgl";
  let destroy = () => {};

  const render = async () => {
    destroy();
    if (mode === "flat") {
      stage.innerHTML = flatSvg(active);
      destroy = () => {};
      return;
    }
    try {
      destroy = await webgl(stage, active);
    } catch (err) {
      mode = "flat";
      stage.innerHTML = flatSvg(active);
    }
  };

  fails.addEventListener("click", (ev) => {
    const btn = ev.target.closest("[data-fail]");
    if (!btn) return;
    const id = btn.dataset.fail;
    if (active.has(id)) active.delete(id);
    else active.add(id);
    btn.setAttribute("aria-pressed", active.has(id) ? "true" : "false");
    const texts = FAILURES.filter((item) => active.has(item.id)).map((item) => item.note);
    note.textContent = texts.length ? texts.join(" ") : "All drawn paths are up.";
    render();
  });
  root.querySelector("#flat").addEventListener("click", () => {
    mode = mode === "flat" ? "webgl" : "flat";
    if (reduce) mode = "flat";
    render();
  });
  note.textContent = "All drawn paths are up.";
  await render();
}

function cutSet(active) {
  const cuts = new Set();
  FAILURES.forEach((item) => {
    if (!active.has(item.id)) return;
    item.cuts.forEach((pair) => cuts.add(pair.slice().sort().join("|")));
  });
  return cuts;
}

function flatSvg(active) {
  const cuts = cutSet(active);
  const pos = {
    carrier: [40, 180], sbc: [120, 150], byoc: [210, 70], edge: [210, 210],
    media: [300, 140], architect: [400, 70], acd: [480, 140], queue: [560, 190],
    agent: [680, 150], bot: [400, 220], wem: [560, 60], crm: [680, 60]
  };
  const lines = LINKS.map(([a, b]) => {
    const cut = cuts.has([a, b].sort().join("|"));
    const [x1, y1] = pos[a];
    const [x2, y2] = pos[b];
    return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${cut ? "#ff5a36" : "#8fd4ff"}" stroke-width="${cut ? 3 : 2}" stroke-dasharray="${cut ? "6 6" : "0"}"/>`;
  }).join("");
  const dots = Object.entries(pos).map(([id, [x, y]]) => `<g><circle cx="${x}" cy="${y}" r="16" fill="#d6f25c"/><text x="${x}" y="${y + 32}" text-anchor="middle" fill="#f6f1e8" font-size="12">${id}</text></g>`).join("");
  return `<svg viewBox="0 0 740 280" role="img" aria-label="Flat topology of carrier, BYOC, Edge, media, Architect, queue, agent, bot, WEM, and CRM." style="background:#071018;border-radius:16px;width:100%">${lines}${dots}</svg>`;
}

async function webgl(stage, active) {
  const THREE = await import("../vendor/three.module.js");
  const cuts = cutSet(active);
  stage.innerHTML = `<div class="topo-wrap"><canvas id="floor" aria-label="Three.js topology. Drag to orbit. Failure buttons change which links glow."></canvas><div class="topo-labels" id="labels"></div></div>`;
  const canvas = stage.querySelector("#floor");
  const mobile = window.matchMedia("(max-width: 820px), (pointer: coarse)").matches;
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: !mobile, alpha: true, powerPreference: mobile ? "low-power" : "high-performance" });
  const dpr = window.devicePixelRatio || 1;
  renderer.setPixelRatio(mobile ? Math.min(dpr, 1) : Math.min(dpr, 1.5));
  renderer.setSize(canvas.clientWidth || 800, 520);
  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x071018, 0.045);
  const camera = new THREE.PerspectiveCamera(45, (canvas.clientWidth || 800) / 520, 0.1, 100);
  camera.position.set(8, 6, 10);
  scene.add(new THREE.AmbientLight(0xffffff, 0.55));
  const key = new THREE.PointLight(0xff5a36, 18, 30);
  key.position.set(-3, 4, 4);
  scene.add(key);
  const fill = new THREE.PointLight(0x8fd4ff, 12, 30);
  fill.position.set(4, 3, -2);
  scene.add(fill);
  const byId = {};
  const colors = { voice: 0xff5a36, core: 0xd6f25c, people: 0x8fd4ff, ai: 0xb3a6ff };
  NODES.forEach((node) => {
    const mesh = new THREE.Mesh(
      new THREE.SphereGeometry(0.28, 24, 16),
      new THREE.MeshStandardMaterial({ color: colors[node.kind], emissive: colors[node.kind], emissiveIntensity: 0.45, roughness: 0.35 })
    );
    mesh.position.set(node.x, node.y, node.z);
    scene.add(mesh);
    byId[node.id] = mesh;
  });
  LINKS.forEach(([a, b]) => {
    const cut = cuts.has([a, b].sort().join("|"));
    const start = byId[a].position;
    const end = byId[b].position;
    const points = [start.clone(), end.clone()];
    const geo = new THREE.BufferGeometry().setFromPoints(points);
    const mat = new THREE.LineBasicMaterial({ color: cut ? 0xff5a36 : 0x9ad7ff });
    scene.add(new THREE.Line(geo, mat));
  });
  const floor = new THREE.Mesh(
    new THREE.CircleGeometry(9, 48),
    new THREE.MeshStandardMaterial({ color: 0x101820, roughness: 1 })
  );
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -2;
  scene.add(floor);

  let frame = 0;
  let running = true;
  const target = new THREE.Vector3(1, 0, 0);
  let theta = 0.6;
  let phi = 1.05;
  let radius = 14;
  let dragging = false;
  let lastX = 0;
  let lastY = 0;
  const place = () => {
    camera.position.set(
      target.x + radius * Math.sin(phi) * Math.cos(theta),
      target.y + radius * Math.cos(phi),
      target.z + radius * Math.sin(phi) * Math.sin(theta)
    );
    camera.lookAt(target);
  };
  place();
  const onDown = (ev) => { dragging = true; lastX = ev.clientX; lastY = ev.clientY; };
  const onUp = () => { dragging = false; };
  const onMove = (ev) => {
    if (!dragging) return;
    theta -= (ev.clientX - lastX) * 0.008;
    phi = Math.min(1.4, Math.max(0.35, phi - (ev.clientY - lastY) * 0.008));
    lastX = ev.clientX;
    lastY = ev.clientY;
    place();
  };
  const onWheel = (ev) => {
    radius = Math.min(22, Math.max(8, radius + Math.sign(ev.deltaY) * 0.6));
    place();
  };
  canvas.addEventListener("pointerdown", onDown);
  window.addEventListener("pointerup", onUp);
  window.addEventListener("pointermove", onMove);
  canvas.addEventListener("wheel", onWheel, { passive: true });

  const labels = stage.querySelector("#labels");
  const labelEls = {};
  NODES.forEach((node) => {
    const span = document.createElement("span");
    span.textContent = node.label;
    labels.appendChild(span);
    labelEls[node.id] = span;
  });
  let last = 0;
  const tick = (now) => {
    if (!running) return;
    frame = requestAnimationFrame(tick);
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    if (mobile && now - last < 34) return;
    last = now;
    const width = canvas.clientWidth || 800;
    const height = 520;
    if (canvas.width !== Math.floor(width * renderer.getPixelRatio())) renderer.setSize(width, height, false);
    renderer.render(scene, camera);
    const rect = canvas.getBoundingClientRect();
    NODES.forEach((node) => {
      const vector = byId[node.id].position.clone().project(camera);
      const el = labelEls[node.id];
      el.style.left = `${(vector.x * 0.5 + 0.5) * rect.width}px`;
      el.style.top = `${(-vector.y * 0.5 + 0.5) * rect.height}px`;
      el.style.display = vector.z < 1 ? "block" : "none";
    });
  };
  tick(0);
  return () => {
    running = false;
    cancelAnimationFrame(frame);
    canvas.removeEventListener("pointerdown", onDown);
    window.removeEventListener("pointerup", onUp);
    window.removeEventListener("pointermove", onMove);
    canvas.removeEventListener("wheel", onWheel);
    renderer.dispose();
  };
}
