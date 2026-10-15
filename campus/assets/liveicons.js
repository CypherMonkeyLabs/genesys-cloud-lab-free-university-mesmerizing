/** One shared WebGL context. Each track card gets its own mesh, blitted onto a 2D canvas. */

const entries = [];
let THREE = null;
let renderer = null;
let scene = null;
let camera = null;
let glCanvas = null;
let frame = 0;
let booting = null;
let reduce = false;

export function scan(root = document) {
  reduce = document.documentElement.dataset.reduce === "1" || window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const stages = [...root.querySelectorAll(".iso-stage[data-kind]")];
  if (!stages.length || reduce || !hasWebGL()) return;
  boot().then(() => {
    stages.forEach(register);
    start();
  }).catch(() => {});
}

function hasWebGL() {
  try {
    const probe = document.createElement("canvas");
    return !!(probe.getContext("webgl2") || probe.getContext("webgl"));
  } catch (err) {
    return false;
  }
}

function boot() {
  if (renderer) return Promise.resolve();
  if (booting) return booting;
  booting = import("../vendor/three.module.js").then((mod) => {
    THREE = mod;
    glCanvas = document.createElement("canvas");
    glCanvas.width = 160;
    glCanvas.height = 150;
    renderer = new THREE.WebGLRenderer({ canvas: glCanvas, antialias: true, alpha: true, preserveDrawingBuffer: true });
    renderer.setPixelRatio(1);
    renderer.setSize(160, 150, false);
    renderer.setClearColor(0x000000, 0);
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(32, 160 / 150, 0.1, 20);
    camera.position.set(0.4, 0.7, 3.4);
    camera.lookAt(0, 0, 0);
    scene.add(new THREE.AmbientLight(0xffffff, 0.55));
    const key = new THREE.PointLight(0xffffff, 12, 12);
    key.position.set(2, 3, 3);
    scene.add(key);
  });
  return booting;
}

function register(stage) {
  if (stage.dataset.live === "1") return;
  const face = stage.querySelector("canvas.live-icon");
  if (!face) return;
  const kind = stage.dataset.kind || "prism";
  const group = build(kind, stageColor(stage));
  scene.add(group);
  group.visible = false;
  stage.dataset.live = "1";
  entries.push({ stage, face, group, spin: 0.5 + (entries.length % 5) * 0.12 });
}

function stageColor(stage) {
  const accent = Number(stage.dataset.accent || 0);
  const roles = [0xff2fb3, 0x2ff7ff, 0xd6ff3c, 0xb388ff, 0xff8a3d, 0x7dffa8];
  return roles[Math.abs(accent) % roles.length];
}

function build(kind, color) {
  const group = new THREE.Group();
  const mat = () => new THREE.MeshStandardMaterial({
    color,
    emissive: color,
    emissiveIntensity: 0.45,
    roughness: 0.28,
    metalness: 0.42
  });
  const wire = () => new THREE.MeshBasicMaterial({ color, wireframe: true });
  const add = (mesh) => { group.add(mesh); return mesh; };
  switch (kind) {
    case "prism":
      add(new THREE.Mesh(new THREE.OctahedronGeometry(0.72, 0), mat()));
      break;
    case "tower":
      [-0.45, 0, 0.45].forEach((y, i) => {
        const box = new THREE.Mesh(new THREE.BoxGeometry(0.7 - i * 0.12, 0.32, 0.7 - i * 0.12), mat());
        box.position.y = y;
        group.add(box);
      });
      break;
    case "flow":
      [-0.7, 0, 0.7].forEach((x, i) => {
        const box = new THREE.Mesh(new THREE.BoxGeometry(0.38, 0.28, 0.22), mat());
        box.position.set(x, i === 1 ? 0.25 : -0.05, 0);
        group.add(box);
      });
      break;
    case "rings":
      [0.55, 0.78, 1.02].forEach((radius, i) => {
        const ring = new THREE.Mesh(new THREE.TorusGeometry(radius, 0.045, 8, 28), wire());
        ring.rotation.x = Math.PI / 2.2 + i * 0.2;
        group.add(ring);
      });
      break;
    case "stack":
      [0, 1, 2].forEach((i) => {
        const slab = new THREE.Mesh(new THREE.BoxGeometry(0.95, 0.18, 0.62), mat());
        slab.position.y = -0.4 + i * 0.32;
        group.add(slab);
      });
      break;
    case "globe":
      add(new THREE.Mesh(new THREE.SphereGeometry(0.62, 18, 14), wire()));
      add(new THREE.Mesh(new THREE.TorusGeometry(0.9, 0.03, 8, 32), wire())).rotation.x = Math.PI / 2.4;
      break;
    case "server":
      add(new THREE.Mesh(new THREE.BoxGeometry(1.1, 0.7, 0.55), mat()));
      [-0.18, 0, 0.18].forEach((y) => {
        const slot = new THREE.Mesh(new THREE.BoxGeometry(0.7, 0.06, 0.08), new THREE.MeshBasicMaterial({ color: 0x041018 }));
        slot.position.set(0, y, 0.3);
        group.add(slot);
      });
      break;
    case "beacon":
      add(new THREE.Mesh(new THREE.ConeGeometry(0.28, 0.7, 6), mat())).position.y = 0.2;
      add(new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.55, 8), mat())).position.y = -0.4;
      break;
    case "clock":
      add(new THREE.Mesh(new THREE.TorusGeometry(0.62, 0.08, 8, 28), mat()));
      add(new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.45, 0.08), mat())).position.y = 0.12;
      break;
    case "shield":
      add(new THREE.Mesh(new THREE.SphereGeometry(0.62, 12, 10, 0, Math.PI * 2, 0, Math.PI * 0.65), mat()));
      break;
    case "wave":
      for (let i = 0; i < 7; i += 1) {
        const bead = new THREE.Mesh(new THREE.SphereGeometry(0.1, 8, 8), mat());
        bead.position.set(-0.75 + i * 0.25, Math.sin(i) * 0.28, 0);
        group.add(bead);
      }
      break;
    case "neural":
      [[-0.4, 0.3], [0.45, 0.25], [0, -0.35], [-0.5, -0.2], [0.4, -0.15]].forEach(([x, y]) => {
        const node = new THREE.Mesh(new THREE.SphereGeometry(0.12, 8, 8), mat());
        node.position.set(x, y, 0);
        group.add(node);
      });
      break;
    case "cube":
      add(new THREE.Mesh(new THREE.BoxGeometry(0.85, 0.85, 0.85), wire()));
      break;
    case "link":
      [-0.4, 0.4].forEach((x) => {
        const ball = new THREE.Mesh(new THREE.SphereGeometry(0.28, 12, 12), mat());
        ball.position.x = x;
        group.add(ball);
      });
      add(new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 0.7, 8), mat())).rotation.z = Math.PI / 2;
      break;
    case "bridge":
      [-0.7, 0.7].forEach((x) => {
        const pier = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.7, 0.22), mat());
        pier.position.set(x, -0.1, 0);
        group.add(pier);
      });
      add(new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.12, 0.28), mat())).position.y = 0.28;
      break;
    case "constellation":
      for (let i = 0; i < 8; i += 1) {
        const star = new THREE.Mesh(new THREE.SphereGeometry(0.08, 6, 6), mat());
        const angle = (i / 8) * Math.PI * 2;
        star.position.set(Math.cos(angle) * 0.7, Math.sin(angle * 2) * 0.35, Math.sin(angle) * 0.5);
        group.add(star);
      }
      break;
    case "radar":
      add(new THREE.Mesh(new THREE.ConeGeometry(0.7, 0.28, 16, 1, true), wire())).rotation.x = Math.PI / 2;
      add(new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.5, 0.06), mat())).rotation.z = -0.6;
      break;
    case "chart":
      [0.3, 0.55, 0.85].forEach((h, i) => {
        const bar = new THREE.Mesh(new THREE.BoxGeometry(0.22, h, 0.22), mat());
        bar.position.set(-0.4 + i * 0.4, h / 2 - 0.45, 0);
        group.add(bar);
      });
      break;
    case "sheet":
      add(new THREE.Mesh(new THREE.BoxGeometry(0.9, 1.1, 0.06), mat()));
      break;
    case "star":
      add(new THREE.Mesh(new THREE.OctahedronGeometry(0.55, 0), mat()));
      add(new THREE.Mesh(new THREE.TorusGeometry(0.85, 0.03, 6, 24), wire()));
      break;
    default: {
      const unknown = kind;
      add(new THREE.Mesh(new THREE.OctahedronGeometry(0.6, 0), mat()));
      if (unknown) break;
    }
  }
  return group;
}

function start() {
  if (frame || !renderer) return;
  const loop = () => {
    frame = requestAnimationFrame(loop);
    const t = performance.now() * 0.001;
    const live = entries.filter((entry) => entry.stage.isConnected);
    if (!live.length || document.hidden) return;
    live.forEach((entry) => {
      entries.forEach((other) => { other.group.visible = false; });
      entry.group.visible = true;
      entry.group.rotation.y = t * entry.spin;
      entry.group.rotation.x = Math.sin(t * 0.7) * 0.18;
      renderer.render(scene, camera);
      const ctx = entry.face.getContext("2d");
      if (!ctx) return;
      ctx.clearRect(0, 0, entry.face.width, entry.face.height);
      ctx.drawImage(glCanvas, 0, 0, entry.face.width, entry.face.height);
      entry.stage.classList.add("has-live");
    });
  };
  loop();
}
