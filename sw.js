const CACHE = "cfo-cockpit-shell-v3";
const ASSETS = ["./", "./index.html", "./styles.css", "./config.js", "./app.js", "./manifest.webmanifest", "./icon.svg"];

self.addEventListener("install", e => e.waitUntil(
  caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting())
));

// Cancella le vecchie copie salvate, comprese le notizie rimaste "congelate".
self.addEventListener("activate", e => e.waitUntil(
  caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim())
));

self.addEventListener("fetch", e => {
  const r = e.request, u = new URL(r.url);
  // Gestisce solo i file dell'app. Notizie, cambi e prezzi (altri siti) vanno sempre in rete.
  if (r.method !== "GET" || u.origin !== location.origin || u.search) return;
  // Prima la rete, così le modifiche arrivano subito; la copia salvata serve solo offline.
  e.respondWith(
    fetch(r)
      .then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(r, copy)); return res; })
      .catch(() => caches.match(r).then(m => m || caches.match("./index.html")))
  );
});
