/** Small wireframe in the hero. Loaded after first paint. CSS constellation stays if WebGL does not start. */

export async function mountHero(canvas, reduce) {
  if (!canvas || reduce) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  if (canvas.dataset.live === "1") {
    if (canvas.dataset.paused === "1") {
      canvas.dataset.paused = "0";
      canvas._resume?.();
    }
    return;
  }
  const THREE = await import("../vendor/three.module.js");
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(42, 1.6, 0.1, 20);
  camera.position.set(0, 0.2, 3.4);
  const group = new THREE.Group();
  const shell = new THREE.Mesh(
    new THREE.IcosahedronGeometry(1.15, 0),
    new THREE.MeshBasicMaterial({ color: 0xff5a36, wireframe: true })
  );
  const core = new THREE.Mesh(
    new THREE.OctahedronGeometry(0.45, 0),
    new THREE.MeshBasicMaterial({ color: 0xd6f25c, wireframe: true })
  );
  const ring = new THREE.Mesh(
    new THREE.TorusGeometry(1.55, 0.015, 8, 48),
    new THREE.MeshBasicMaterial({ color: 0x8fd4ff })
  );
  ring.rotation.x = 1.1;
  group.add(shell, core, ring);
  scene.add(group);
  const fit = () => {
    const w = canvas.clientWidth || 640;
    const h = canvas.clientHeight || 260;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  };
  fit();
  const tick = () => {
    if (!canvas.isConnected) return;
    const home = canvas.closest("#home");
    if (home && home.hidden) {
      canvas.dataset.paused = "1";
      return;
    }
    group.rotation.y += 0.008;
    group.rotation.x += 0.003;
    renderer.render(scene, camera);
    requestAnimationFrame(tick);
  };
  canvas._resume = tick;
  canvas.dataset.live = "1";
  canvas.dataset.paused = "0";
  tick();
  window.addEventListener("resize", fit);
}
