/* Scope is the campus directory that contains this file.
   The page registers it with { scope: "./" }. */
const CACHE = "gccx-lab-v16";
const SHELL = [
  "./",
  "./index.html",
  "./offline.html",
  "./manifest.webmanifest",
  "./favicon.svg",
  "./icon-192.png",
  "./icon-512.png",
  "./icon-maskable-512.png",
  "./assets/app.js",
  "./assets/university.css",
  "./assets/css/frame.css",
  "./assets/css/wow.css",
  "./assets/css/footer.css",
  "./assets/round2.css",
  "./assets/round2.js",
  "./assets/sources.js",
  "./assets/js/frame.js",
  "./assets/js/university.js",
  "./assets/mascot.js",
  "./assets/diagrams.js",
  "./assets/pages.js",
  "./assets/i18n.js",
  "./assets/icons3d.js",
  "./assets/headings.js",
  "./assets/lightbox.js",
  "./assets/studios.js",
  "./assets/routing-model.js",
  "./guide/guide.css",
  "./guide/guide.js",
  "./guide/dragbot.js",
  "./shared/pybot-chat/engine.js",
  "./shared/pybot-chat/ui.js",
  "./shared/pybot-chat/chat.css",
  "./data/gccxbot-index.json",
  "./data/manifest.json",
  "./data/reference.json",
  "./data/tracks/acd.json",
  "./data/tracks/ai.json",
  "./data/tracks/api.json",
  "./data/tracks/architect.json",
  "./data/tracks/byoc.json",
  "./data/tracks/crm.json",
  "./data/tracks/ecosystem.json",
  "./data/tracks/edge.json",
  "./data/tracks/emergency.json",
  "./data/tracks/forecast.json",
  "./data/tracks/foundations.json",
  "./data/tracks/migration.json",
  "./data/tracks/org.json",
  "./data/tracks/predictive.json",
  "./data/tracks/qm.json",
  "./data/tracks/quality.json",
  "./data/tracks/queues.json",
  "./data/tracks/skills.json",
  "./data/tracks/sta.json",
  "./data/tracks/wfm.json",
];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key)))).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;
  event.respondWith((async () => {
    const cached = await caches.match(request);
    try {
      const response = await fetch(request);
      if (response && response.ok) {
        const copy = response.clone();
        const cache = await caches.open(CACHE);
        await cache.put(request, copy);
      }
      return response;
    } catch (err) {
      if (cached) return cached;
      if (request.mode === "navigate") {
        const fallback = await caches.match("./offline.html");
        if (fallback) return fallback;
      }
      return new Response("offline", { status: 503, headers: { "Content-Type": "text/plain" } });
    }
  })());
});
