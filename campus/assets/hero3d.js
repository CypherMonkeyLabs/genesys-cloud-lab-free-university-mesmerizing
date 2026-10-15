/** Full-bleed call-path globe. three.js is loaded only when this module runs. */

const LABELS = ["Carrier", "Trunk", "Architect", "Queue", "Agent"];
let canvasEl = null;
let renderer = null;
let scene = null;
let camera = null;
let clock = null;
let rig = null;
let orbit = null;
let satellites = null;
let paints = [];
let labelSprites = [];
let gridMat = null;
let running = false;
let frame = 0;
const mouse = { x: 0, y: 0 };
let scrollY = 0;
let listeners = false;

export function mountHero(canvas, reduce) {
  canvasEl = canvas;
  if (!canvas) return;
  if (canvas.dataset.live === "1" || canvas.dataset.booting === "1") {
    canvas.classList.remove("is-fallback");
    hideFallback(canvas);
    start();
    return;
  }
  const motionOff = reduce || document.documentElement.dataset.reduce === "1" || window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (motionOff || !hasWebGL()) {
    showFallback(canvas);
    return;
  }
  canvas.dataset.booting = "1";
  import("../vendor/three.module.js")
    .then((THREE) => boot(THREE, canvas))
    .catch(() => showFallback(canvas));
}

function hasWebGL() {
  try {
    const probe = document.createElement("canvas");
    return !!(probe.getContext("webgl2") || probe.getContext("webgl"));
  } catch (err) {
    return false;
  }
}

function showFallback(canvas) {
  canvas.classList.add("is-fallback");
  const fb = canvas.parentElement?.querySelector(".hero-fallback");
  if (fb) fb.hidden = false;
  stop();
}

function hideFallback(canvas) {
  const fb = canvas.parentElement?.querySelector(".hero-fallback");
  if (fb) fb.hidden = true;
}

function cssHex(name, fallback) {
  const raw = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  if (!raw) return fallback;
  const probe = cssHex.ctx || (cssHex.ctx = document.createElement("canvas").getContext("2d"));
  probe.fillStyle = "#000000";
  probe.fillStyle = raw;
  const hex = probe.fillStyle;
  if (typeof hex === "string" && /^#[0-9a-f]{6}$/i.test(hex)) return parseInt(hex.slice(1), 16);
  return fallback;
}

function palette() {
  return {
    bg: cssHex("--cc-bg", 0x05060a),
    accent: cssHex("--cc-accent-1", 0xff2fb3),
    accent2: cssHex("--cc-accent-2", 0x2ff7ff),
    accent3: cssHex("--cc-accent-3", 0xd6ff3c),
    accent4: cssHex("--cc-accent-4", 0xb388ff)
  };
}

function inkFor(bg) {
  const r = (bg >> 16) & 255;
  const g = (bg >> 8) & 255;
  const b = bg & 255;
  const lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255;
  return lum > 0.62 ? "#1b140f" : "#f7fbff";
}

function boot(THREE, canvas) {
  try {
    renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false, powerPreference: "high-performance" });
  } catch (err) {
    showFallback(canvas);
    return;
  }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
  renderer.setClearColor(palette().bg, 1);
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(52, 1, 0.1, 80);
  camera.position.set(1.8, 1.15, 5.4);
  clock = new THREE.Clock();
  rig = new THREE.Group();
  scene.add(rig);

  const colors = palette();
  scene.fog = new THREE.Fog(colors.bg, 9, 24);
  scene.add(new THREE.AmbientLight(0xffffff, 0.35));
  const key = new THREE.PointLight(colors.accent2, 18, 30);
  key.position.set(4, 6, 6);
  scene.add(key);
  paints.push({ mat: key, role: "accent2", light: true });

  gridMat = new THREE.ShaderMaterial({
    transparent: true,
    depthWrite: false,
    uniforms: {
      color: { value: new THREE.Color(colors.accent2) },
      color2: { value: new THREE.Color(colors.accent) },
      time: { value: 0 }
    },
    vertexShader: `
      varying vec2 vUv;
      void main() {
        vUv = uv * 22.0;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,
    fragmentShader: `
      varying vec2 vUv;
      uniform vec3 color;
      uniform vec3 color2;
      uniform float time;
      void main() {
        float gx = abs(fract(vUv.x) - 0.5);
        float gy = abs(fract(vUv.y) - 0.5);
        float line = smoothstep(0.455, 0.5, max(gx, gy));
        float d = length(vUv / 22.0 - 0.5);
        float fade = 1.0 - smoothstep(0.2, 0.72, d);
        float pulse = 0.65 + 0.35 * sin(d * 28.0 - time * 2.2);
        vec3 col = mix(color, color2, 0.5 + 0.5 * sin(vUv.x * 0.35 + time));
        gl_FragColor = vec4(col * 1.4, line * fade * pulse);
      }
    `
  });
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(36, 36), gridMat);
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -1.7;
  rig.add(floor);

  const globe = new THREE.Mesh(
    new THREE.IcosahedronGeometry(1.25, 1),
    new THREE.MeshBasicMaterial({ color: colors.accent2, wireframe: true, transparent: true, opacity: 0.72 })
  );
  paints.push({ mat: globe.material, role: "accent2" });
  rig.add(globe);
  globe.userData.spin = true;
  const core = new THREE.Mesh(
    new THREE.SphereGeometry(0.42, 24, 24),
    new THREE.MeshBasicMaterial({ color: colors.accent })
  );
  paints.push({ mat: core.material, role: "accent" });
  rig.add(core);
  const coreHalo = halo(THREE, colors.accent, 3.4);
  paints.push({ mat: coreHalo.material, role: "accent" });
  rig.add(coreHalo);

  const ringGeo = [
    [4.4, 0.03, Math.PI / 2.15, 0.2],
    [5.3, 0.02, Math.PI / 2.8, 0.9],
    [3.2, 0.035, Math.PI / 1.7, 0.4]
  ];
  ringGeo.forEach(([radius, tube, tilt, spin], index) => {
    const role = index === 1 ? "accent" : "accent2";
    const mesh = new THREE.Mesh(
      new THREE.TorusGeometry(radius, tube, 12, 96),
      new THREE.MeshBasicMaterial({ color: colors[role], transparent: true, opacity: 0.85 })
    );
    mesh.rotation.x = tilt;
    mesh.userData.spinZ = 0.15 + index * 0.07;
    paints.push({ mat: mesh.material, role });
    rig.add(mesh);
  });

  orbit = new THREE.Group();
  rig.add(orbit);
  const haloTex = new THREE.CanvasTexture(haloTexture());
  haloTex.channel = 0;
  LABELS.forEach((name, index) => {
    const role = ["accent", "accent2", "accent3", "accent4", "accent"][index];
    const node = new THREE.Group();
    const mesh = new THREE.Mesh(
      new THREE.IcosahedronGeometry(0.28, 0),
      new THREE.MeshStandardMaterial({
        color: colors[role],
        emissive: colors[role],
        emissiveIntensity: 0.85,
        roughness: 0.25,
        metalness: 0.35
      })
    );
    paints.push({ mat: mesh.material, role, emissive: true });
    node.add(mesh);
    const glow = new THREE.Sprite(new THREE.SpriteMaterial({
      map: haloTex,
      color: colors[role],
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    }));
    glow.scale.set(1.7, 1.7, 1);
    paints.push({ mat: glow.material, role });
    node.add(glow);
    const sprite = textSprite(THREE, name);
    sprite.position.y = 0.62;
    node.add(sprite);
    labelSprites.push(sprite);
    const angle = (index / LABELS.length) * Math.PI * 2;
    node.position.set(Math.cos(angle) * 4.6, Math.sin(angle * 2) * 0.55, Math.sin(angle) * 4.6);
    orbit.add(node);
    const lineGeo = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(0, 0, 0),
      node.position.clone()
    ]);
    const line = new THREE.Line(lineGeo, new THREE.LineBasicMaterial({ color: colors.accent2, transparent: true, opacity: 0.45 }));
    paints.push({ mat: line.material, role: "accent2" });
    orbit.add(line);
  });

  satellites = new THREE.Group();
  rig.add(satellites);
  for (let i = 0; i < 10; i += 1) {
    const role = i % 2 ? "accent3" : "accent";
    const sat = new THREE.Mesh(
      new THREE.SphereGeometry(0.08, 10, 10),
      new THREE.MeshBasicMaterial({ color: colors[role] })
    );
    const angle = (i / 10) * Math.PI * 2;
    sat.position.set(Math.cos(angle) * 2.05, Math.sin(i) * 0.25, Math.sin(angle) * 2.05);
    paints.push({ mat: sat.material, role });
    satellites.add(sat);
  }

  const count = 900;
  const positions = new Float32Array(count * 3);
  for (let i = 0; i < count; i += 1) {
    positions[i * 3] = (Math.random() - 0.5) * 18;
    positions[i * 3 + 1] = (Math.random() - 0.5) * 8;
    positions[i * 3 + 2] = (Math.random() - 0.5) * 14;
  }
  const pointsGeo = new THREE.BufferGeometry();
  pointsGeo.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  const points = new THREE.Points(pointsGeo, new THREE.PointsMaterial({
    color: colors.accent2,
    size: 0.16,
    transparent: true,
    opacity: 0.85,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  }));
  paints.push({ mat: points.material, role: "accent2" });
  rig.add(points);

  bind();
  recolor();
  resize();
  canvas.dataset.live = "1";
  canvas.classList.remove("is-fallback");
  hideFallback(canvas);
  canvas._resume = start;
  start();
}

function haloTexture() {
  const c = document.createElement("canvas");
  c.width = 128;
  c.height = 128;
  const g = c.getContext("2d");
  const grd = g.createRadialGradient(64, 64, 2, 64, 64, 62);
  grd.addColorStop(0, "rgba(255,255,255,0.95)");
  grd.addColorStop(0.22, "rgba(255,255,255,0.45)");
  grd.addColorStop(1, "rgba(255,255,255,0)");
  g.fillStyle = grd;
  g.fillRect(0, 0, 128, 128);
  return c;
}

function halo(THREE, color, scale) {
  const tex = new THREE.CanvasTexture(haloTexture());
  tex.channel = 0;
  const sprite = new THREE.Sprite(new THREE.SpriteMaterial({
    map: tex,
    color,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  }));
  sprite.scale.set(scale, scale, 1);
  return sprite;
}

function textSprite(THREE, text) {
  const c = document.createElement("canvas");
  c.width = 512;
  c.height = 128;
  const tex = new THREE.CanvasTexture(c);
  tex.channel = 0;
  const mat = new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false });
  const sprite = new THREE.Sprite(mat);
  sprite.scale.set(2.15, 0.54, 1);
  sprite.userData.canvas = c;
  sprite.userData.text = text;
  return sprite;
}

function paintLabel(sprite, color) {
  const c = sprite.userData.canvas;
  const g = c.getContext("2d");
  g.clearRect(0, 0, c.width, c.height);
  g.font = "700 64px sans-serif";
  g.textAlign = "center";
  g.textBaseline = "middle";
  g.lineWidth = 10;
  g.strokeStyle = "rgba(0,0,0,0.45)";
  g.strokeText(sprite.userData.text, c.width / 2, c.height / 2);
  g.fillStyle = color;
  g.shadowColor = color;
  g.shadowBlur = 16;
  g.fillText(sprite.userData.text, c.width / 2, c.height / 2);
  sprite.material.map.needsUpdate = true;
}

function recolor() {
  if (!scene) return;
  const colors = palette();
  renderer.setClearColor(colors.bg, 1);
  scene.fog.color.setHex(colors.bg);
  if (gridMat) {
    gridMat.uniforms.color.value.setHex(colors.accent2);
    gridMat.uniforms.color2.value.setHex(colors.accent);
  }
  paints.forEach((item) => {
    const hex = colors[item.role] || colors.accent;
    if (item.light) item.mat.color.setHex(hex);
    else if (item.mat.color) item.mat.color.setHex(hex);
    if (item.emissive && item.mat.emissive) item.mat.emissive.setHex(hex);
  });
  const ink = inkFor(colors.bg);
  labelSprites.forEach((sprite) => paintLabel(sprite, ink));
}

function resize() {
  if (!renderer || !canvasEl) return;
  const parent = canvasEl.parentElement;
  const w = parent?.clientWidth || window.innerWidth;
  const h = parent?.clientHeight || window.innerHeight;
  if (w < 2 || h < 2) return;
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
}

function bind() {
  if (listeners) return;
  listeners = true;
  window.addEventListener("pointermove", (ev) => {
    mouse.x = (ev.clientX / window.innerWidth) * 2 - 1;
    mouse.y = (ev.clientY / window.innerHeight) * 2 - 1;
  });
  window.addEventListener("scroll", () => { scrollY = window.scrollY; }, { passive: true });
  window.addEventListener("resize", resize);
  document.addEventListener("gccx-theme", () => recolor());
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) stop();
    else start();
  });
}

function homeVisible() {
  const home = document.querySelector("#home");
  return !!(home && !home.hidden && canvasEl && !canvasEl.classList.contains("is-fallback"));
}

function start() {
  if (running || !renderer) return;
  running = true;
  clock.start();
  const loop = () => {
    if (!running) return;
    frame = requestAnimationFrame(loop);
    if (!homeVisible()) return;
    const t = clock.getElapsedTime();
    if (gridMat) gridMat.uniforms.time.value = t;
    if (orbit) orbit.rotation.y = t * 0.22;
    if (satellites) satellites.rotation.y = -t * 0.45;
    rig.children.forEach((child) => {
      if (child.userData?.spin) child.rotation.y = t * 0.35;
      if (child.userData?.spinZ) child.rotation.z = t * child.userData.spinZ;
    });
    const drift = Math.sin(t * 0.18) * 0.35;
    rig.rotation.y += (mouse.x * 0.22 + drift * 0.04 - rig.rotation.y) * 0.04;
    rig.rotation.x += (-mouse.y * 0.1 - rig.rotation.x) * 0.04;
    const pull = Math.min(scrollY * 0.003, 2.2);
    const wide = (canvasEl?.clientWidth || 800) > 860;
    const aimX = wide ? 0.85 : 0.1;
    camera.position.x += (aimX + mouse.x * 0.35 - camera.position.x) * 0.04;
    camera.position.y += (1.05 + Math.sin(t * 0.15) * 0.18 - mouse.y * 0.2 - camera.position.y) * 0.04;
    camera.position.z += (5.1 + pull - camera.position.z) * 0.04;
    camera.lookAt(aimX * 0.35, 0.1, 0);
    renderer.render(scene, camera);
  };
  loop();
}

function stop() {
  running = false;
  if (frame) cancelAnimationFrame(frame);
  frame = 0;
}
