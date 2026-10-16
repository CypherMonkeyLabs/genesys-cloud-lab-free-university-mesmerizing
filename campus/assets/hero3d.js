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
let composer = null;
let upper = null;
let trailMats = [];
let running = false;
let frame = 0;
const mouse = { x: 0, y: 0 };
let scrollY = 0;
let listeners = false;
let heroSeen = true;

function narrowScreen() {
  return window.matchMedia("(max-width: 820px), (pointer: coarse)").matches;
}

function motionOff(extra) {
  return !!(extra || document.documentElement.dataset.reduce === "1" || window.matchMedia("(prefers-reduced-motion: reduce)").matches);
}

function cappedRatio() {
  const dpr = window.devicePixelRatio || 1;
  return narrowScreen() ? Math.min(dpr, 1) : Math.min(dpr, 1.5);
}

export function mountHero(canvas, reduce) {
  canvasEl = canvas;
  if (!canvas) return;
  if (motionOff(reduce)) {
    showFallback(canvas);
    stop();
    return;
  }
  if (canvas.dataset.live === "1" || canvas.dataset.booting === "1") {
    canvas.classList.remove("is-fallback");
    hideFallback(canvas);
    start();
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
  canvas.parentElement?.classList.remove("hero-live");
  const fb = canvas.parentElement?.querySelector(".hero-fallback");
  if (fb) fb.hidden = false;
  stop();
}

function hideFallback(canvas) {
  canvas.parentElement?.classList.add("hero-live");
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
  const mobile = narrowScreen();
  try {
    renderer = new THREE.WebGLRenderer({
      canvas,
      antialias: !mobile,
      alpha: false,
      powerPreference: mobile ? "low-power" : "high-performance"
    });
  } catch (err) {
    showFallback(canvas);
    return;
  }
  renderer.setPixelRatio(cappedRatio());
  renderer.setClearColor(palette().bg, 1);
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(52, 1, 0.1, 80);
  camera.position.set(-0.7, 1.15, 5.2);
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

  const count = narrowScreen() ? 80 : 420;
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

  fillUpperRight(THREE, colors);
  attachBloom(THREE);

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
  trailMats.forEach((mat) => {
    const hex = colors[mat.userData.role] || colors.accent2;
    mat.uniforms.color.value.setHex(hex);
  });
}

function resize() {
  if (!renderer || !canvasEl) return;
  const parent = canvasEl.parentElement;
  const w = parent?.clientWidth || window.innerWidth;
  const h = parent?.clientHeight || window.innerHeight;
  if (w < 2 || h < 2) return;
  renderer.setPixelRatio(cappedRatio());
  renderer.setSize(w, h, false);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  if (composer) composer.setSize(w, h);
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
    if (document.hidden || !heroSeen) stop();
    else start();
  });
  document.addEventListener("gccx-visibility", (ev) => {
    if (ev.detail && ev.detail.run === false) stop();
    else if (!document.hidden && heroSeen) start();
  });
  const watch = canvasEl?.parentElement || canvasEl;
  if (watch && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      heroSeen = entries.some((entry) => entry.isIntersecting);
      if (!heroSeen || document.hidden) stop();
      else start();
    }, { threshold: 0 });
    io.observe(watch);
  }
}

const UPPER = ["Edge", "Bot", "WEM", "CRM", "Media", "Satellite"];

function fillUpperRight(THREE, colors) {
  upper = new THREE.Group();
  upper.position.set(1.8, 2.15, -0.2);
  rig.add(upper);

  const ring = new THREE.Mesh(
    new THREE.TorusGeometry(1.85, 0.028, 12, 96),
    new THREE.MeshBasicMaterial({ color: colors.accent, transparent: true, opacity: 0.9 })
  );
  ring.rotation.x = Math.PI / 2.4;
  paints.push({ mat: ring.material, role: "accent" });
  upper.add(ring);

  const haloTex = new THREE.CanvasTexture(haloTexture());
  haloTex.channel = 0;
  UPPER.forEach((name, index) => {
    const role = ["accent", "accent2", "accent3", "accent4", "accent2", "accent3"][index];
    const node = new THREE.Group();
    const mesh = new THREE.Mesh(
      index % 2 ? new THREE.OctahedronGeometry(0.28, 0) : new THREE.IcosahedronGeometry(0.26, 0),
      new THREE.MeshStandardMaterial({
        color: colors[role],
        emissive: colors[role],
        emissiveIntensity: 1.1,
        roughness: 0.2,
        metalness: 0.4
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
    glow.scale.set(1.6, 1.6, 1);
    paints.push({ mat: glow.material, role });
    node.add(glow);
    const sprite = textSprite(THREE, name);
    sprite.scale.set(1.7, 0.42, 1);
    sprite.position.y = 0.55;
    node.add(sprite);
    labelSprites.push(sprite);
    const angle = (index / UPPER.length) * Math.PI * 2;
    node.position.set(Math.cos(angle) * 1.85, Math.sin(angle * 2) * 0.36, Math.sin(angle) * 1.15);
    upper.add(node);
  });

  const mainTrail = lightTrail(THREE, 4.6, 0.15, colors.accent2, "accent2", 96);
  trailMats.push(mainTrail.material);
  rig.add(mainTrail);

  const skyTrail = lightTrail(THREE, 2.35, 0.1, colors.accent, "accent", 80);
  trailMats.push(skyTrail.material);
  upper.add(skyTrail);

  addDepth(THREE, colors, 520, 0.045, -14, -4, 16, 9, "accent2");
  addDepth(THREE, colors, 180, 0.22, 2.2, 5.4, 8, 5, "accent");
  addDepth(THREE, colors, 260, 0.16, -2.5, 2.2, 14, 4.2, "accent3");
  fillSkyBand(THREE, colors);

  for (let i = 0; i < 28; i += 1) {
    const role = i % 3 === 0 ? "accent" : i % 3 === 1 ? "accent3" : "accent2";
    const spark = new THREE.Mesh(
      new THREE.SphereGeometry(0.07 + (i % 4) * 0.03, 8, 8),
      new THREE.MeshBasicMaterial({ color: colors[role] })
    );
    const angle = (i / 28) * Math.PI * 2;
    spark.position.set(1.4 + Math.cos(angle) * 2.1, 1.15 + Math.sin(angle * 1.7) * 1.15, Math.sin(angle) * 0.8);
    paints.push({ mat: spark.material, role });
    rig.add(spark);
  }
}

function fillSkyBand(THREE, colors) {
  const band = new THREE.Group();
  band.position.set(0.2, 2.28, 0.15);
  rig.add(band);
  const arc = new THREE.Mesh(
    new THREE.TorusGeometry(6.4, 0.04, 10, 90, Math.PI),
    new THREE.MeshBasicMaterial({ color: colors.accent2, transparent: true, opacity: 0.95 })
  );
  arc.rotation.z = Math.PI;
  paints.push({ mat: arc.material, role: "accent2" });
  band.add(arc);
  const haloTex = new THREE.CanvasTexture(haloTexture());
  haloTex.channel = 0;
  for (let i = 0; i < 16; i += 1) {
    const role = ["accent", "accent2", "accent3", "accent4"][i % 4];
    const bead = new THREE.Mesh(
      new THREE.SphereGeometry(0.22 + (i % 3) * 0.05, 12, 12),
      new THREE.MeshBasicMaterial({ color: colors[role] })
    );
    bead.position.set(-6.2 + i * 0.82, Math.sin(i * 0.7) * 0.22, Math.cos(i) * 0.25);
    paints.push({ mat: bead.material, role });
    band.add(bead);
    const glow = new THREE.Sprite(new THREE.SpriteMaterial({
      map: haloTex,
      color: colors[role],
      transparent: true,
      blending: THREE.AdditiveBlending,
      depthWrite: false
    }));
    glow.scale.set(0.85, 0.85, 1);
    glow.position.copy(bead.position);
    paints.push({ mat: glow.material, role });
    band.add(glow);
  }
}

function lightTrail(THREE, radius, y, color, role, count) {
  const positions = new Float32Array(count * 3);
  const phases = new Float32Array(count);
  for (let i = 0; i < count; i += 1) {
    const angle = (i / count) * Math.PI * 2;
    positions[i * 3] = Math.cos(angle) * radius;
    positions[i * 3 + 1] = Math.sin(angle * 2) * 0.22 + y;
    positions[i * 3 + 2] = Math.sin(angle) * radius * 0.78;
    phases[i] = i / count;
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  geo.setAttribute("phase", new THREE.BufferAttribute(phases, 1));
  const mat = new THREE.ShaderMaterial({
    transparent: true,
    depthWrite: false,
    blending: THREE.AdditiveBlending,
    uniforms: {
      color: { value: new THREE.Color(color) },
      time: { value: 0 }
    },
    vertexShader: `
      attribute float phase;
      varying float vPhase;
      void main() {
        vPhase = phase;
        vec4 mv = modelViewMatrix * vec4(position, 1.0);
        gl_PointSize = 14.0 * (1.2 / max(0.2, -mv.z));
        gl_Position = projectionMatrix * mv;
      }
    `,
    fragmentShader: `
      uniform vec3 color;
      uniform float time;
      varying float vPhase;
      void main() {
        float d = length(gl_PointCoord - 0.5);
        if (d > 0.5) discard;
        float head = fract(vPhase - time);
        float glow = smoothstep(0.28, 0.0, head);
        float alpha = (1.0 - smoothstep(0.05, 0.5, d)) * (0.12 + glow);
        gl_FragColor = vec4(color * (1.2 + glow), alpha);
      }
    `
  });
  mat.userData.role = role;
  return new THREE.Points(geo, mat);
}

function addDepth(THREE, colors, count, size, z0, z1, spread, rise, role) {
  const positions = new Float32Array(count * 3);
  for (let i = 0; i < count; i += 1) {
    const bias = Math.random();
    positions[i * 3] = -2 + bias * spread;
    positions[i * 3 + 1] = -1.2 + Math.pow(Math.random(), 0.65) * rise;
    positions[i * 3 + 2] = z0 + Math.random() * (z1 - z0);
  }
  const geo = new THREE.BufferGeometry();
  geo.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  const mat = new THREE.PointsMaterial({
    color: colors[role],
    size,
    transparent: true,
    opacity: 0.9,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  });
  paints.push({ mat, role });
  rig.add(new THREE.Points(geo, mat));
}

function attachBloom(THREE) {
  if (narrowScreen() || motionOff()) return;
  const arm = () => Promise.all([
    import("../vendor/three-post/postprocessing/EffectComposer.js"),
    import("../vendor/three-post/postprocessing/RenderPass.js"),
    import("../vendor/three-post/postprocessing/UnrealBloomPass.js")
  ]).then(([composerMod, renderMod, bloomMod]) => {
    if (!renderer || !scene || !camera) return;
    const next = new composerMod.EffectComposer(renderer);
    next.addPass(new renderMod.RenderPass(scene, camera));
    const pass = new bloomMod.UnrealBloomPass(
      new THREE.Vector2(canvasEl.clientWidth || 256, canvasEl.clientHeight || 256),
      0.85,
      0.48,
      0.28
    );
    next.addPass(pass);
    composer = next;
    resize();
  }).catch(() => {
    composer = null;
  });
  const ric = window.requestIdleCallback || ((cb) => setTimeout(cb, 600));
  ric(() => arm(), { timeout: 1800 });
}

function paintFrame() {
  try {
    if (composer) composer.render();
    else renderer.render(scene, camera);
  } catch (err) {
    composer = null;
    renderer.render(scene, camera);
  }
}

function homeVisible() {
  const home = document.querySelector("#home");
  return !!(home && !home.hidden && canvasEl && !canvasEl.classList.contains("is-fallback"));
}

function start() {
  if (running || !renderer) return;
  if (motionOff()) {
    showFallback(canvasEl);
    return;
  }
  running = true;
  clock.start();
  let last = 0;
  const loop = (now) => {
    if (!running) return;
    frame = requestAnimationFrame(loop);
    if (motionOff()) {
      showFallback(canvasEl);
      return;
    }
    if (!homeVisible() || !heroSeen || document.hidden) return;
    const minGap = narrowScreen() ? 34 : 16;
    if (now - last < minGap) return;
    last = now;
    const t = clock.getElapsedTime();
    if (gridMat) gridMat.uniforms.time.value = t;
    if (orbit) orbit.rotation.y = t * 0.22;
    if (upper) upper.rotation.y = -t * 0.32;
    if (satellites) satellites.rotation.y = -t * 0.45;
    trailMats.forEach((mat, index) => { mat.uniforms.time.value = t * (0.18 + index * 0.04); });
    rig.children.forEach((child) => {
      if (child.userData?.spin) child.rotation.y = t * 0.35;
      if (child.userData?.spinZ) child.rotation.z = t * child.userData.spinZ;
    });
    const drift = Math.sin(t * 0.18) * 0.35;
    rig.rotation.y += (mouse.x * 0.22 + drift * 0.04 - rig.rotation.y) * 0.04;
    rig.rotation.x += (-mouse.y * 0.1 - rig.rotation.x) * 0.04;
    const pull = Math.min(scrollY * 0.003, 2.2);
    const wide = (canvasEl?.clientWidth || 800) > 860;
    const aimX = wide ? -0.95 : 0.05;
    camera.position.x += (aimX + mouse.x * 0.35 - camera.position.x) * 0.04;
    camera.position.y += (0.55 + Math.sin(t * 0.15) * 0.1 - mouse.y * 0.16 - camera.position.y) * 0.04;
    camera.position.z += (5.1 + pull - camera.position.z) * 0.04;
    camera.lookAt(0.15, -0.7, 0);
    paintFrame();
  };
  loop();
}

function stop() {
  running = false;
  if (frame) cancelAnimationFrame(frame);
  frame = 0;
}
