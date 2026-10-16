const CACHE = "gccx-lab-v11";
const SHELL = [
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./assets/app.js",
  "./assets/university.css",
  "./assets/css/frame.css",
  "./assets/css/wow.css",
  "./assets/css/footer.css",
  "./assets/round2.css",
  "./assets/round2.js",
  "./assets/js/frame.js",
  "./assets/js/university.js",
  "./guide/guide.css",
  "./guide/guide.js",
  "./data/guide-kb.json",
  "./assets/mascot.js",
  "./assets/diagrams.js",
  "./assets/pages.js",
  "./assets/floorviz.js",
  "./assets/hero3d.js",
  "./assets/icons3d.js",
  "./assets/liveicons.js",
  "./assets/headings.js",
  "./assets/i18n.js",
  "./assets/lightbox.js",
  "./assets/studios.js",
  "./assets/topology.js",
  "./assets/routing-model.js",
  "./data/manifest.json",
  "./data/reference.json"
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
  event.respondWith(
    caches.match(request).then((cached) => {
      const network = fetch(request).then((response) => {
        if (response && response.ok) {
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(request, copy));
        }
        return response;
      }).catch(() => cached);
      return network || cached;
    })
  );
});
