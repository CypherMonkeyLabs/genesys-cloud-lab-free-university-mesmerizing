/** Build-time Mermaid SVGs. The runtime never loads mermaid. */
import { mkdirSync, writeFileSync } from "node:fs";
import { spawn } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const outDir = join(root, "campus/assets/mermaid");
const mermaidJs = "/tmp/gccx-vendor/node_modules/mermaid/dist/mermaid.min.js";

const diagrams = [
  {
    id: "sip-sequence",
    title: "SIP success path",
    caption: "Teaching sketch of a call that is answered. Real traces also use 183 and PRACK. RTP is not a SIP response.",
    def: `sequenceDiagram
    participant Caller
    participant Cloud
    Caller->>Cloud: INVITE
    Cloud-->>Caller: 100 Trying
    Cloud-->>Caller: 180 Ringing
    Cloud-->>Caller: 200 OK
    Caller->>Cloud: ACK
    Note over Caller,Cloud: RTP media is a different path
    Caller->>Cloud: BYE
    Cloud-->>Caller: 200 OK`
  },
  {
    id: "acd-flow",
    title: "ACD eligibility",
    caption: "Teaching sketch. On Queue, utilization, and skills decide who can be alerted. Bullseye can widen later.",
    def: `flowchart TD
    A[Interaction waiting] --> B{Agent On Queue?}
    B -->|No| W[Keep waiting]
    B -->|Yes| C{Under utilization?}
    C -->|No| W
    C -->|Yes| D{Skills still required?}
    D -->|Match| E[Alert that agent]
    D -->|Miss| W`
  },
  {
    id: "deploy-flow",
    title: "Deployment order",
    caption: "Teaching checklist. Region and roles, then trunk or Edge, then a published flow and a queue.",
    def: `flowchart LR
    R[Core region] --> T[Trunk or Edge]
    T --> F[Publish the flow]
    F --> Q[Queue and skills]
    Q --> N[Number and emergency owner]`
  },
  {
    id: "cutover-flow",
    title: "Cutover",
    caption: "Teaching sequence. One number, then the queue, then the people. Keep a rollback if media fails.",
    def: `flowchart LR
    O[Old path still answers] --> P[Parallel test call]
    P --> C[Move one DID]
    C --> M[Watch the queue]
    M --> R[Roll back if audio fails]`
  },
  {
    id: "trouble-flow",
    title: "No-audio branch",
    caption: "Teaching tree. A flow that runs with silence is a media problem. An unpublished flow never starts.",
    def: `flowchart TD
    S[Caller hears nothing] --> Q{Architect flow ran?}
    Q -->|Yes| M[Check outbound RTP]
    Q -->|No| P[Publish inbound and in-queue]
    M --> F[Signaling port is not the media range]`
  },
  {
    id: "data-flow",
    title: "Data action",
    caption: "Teaching sketch. A data action leaves the flow. Participant data can carry a value to the agent.",
    def: `flowchart LR
    F[Architect flow] --> D[Data action]
    D --> X[Outside system]
    X --> P[Participant data]
    P --> A[Agent script]`
  }
];

const page = `<!doctype html>
<meta charset="utf-8">
<body>
<div id="out"></div>
<script src="${mermaidJs}"></script>
<script>
const items = ${JSON.stringify(diagrams.map((item) => ({ id: item.id, def: item.def })))};
mermaid.initialize({
  startOnLoad: false,
  securityLevel: "loose",
  theme: "dark",
  flowchart: { htmlLabels: false },
  sequence: { useMaxWidth: false }
});
setTimeout(() => {
  (async () => {
    const out = document.getElementById("out");
    for (const item of items) {
      const rendered = await mermaid.render("mmd-" + item.id.replace(/[^a-z0-9]/g, ""), item.def);
      const wrap = document.createElement("div");
      wrap.id = item.id;
      wrap.innerHTML = rendered.svg + "<!--END " + item.id + "-->";
      out.appendChild(wrap);
    }
    document.body.dataset.done = "yes";
  })().catch((err) => {
    document.body.dataset.done = "err";
    document.body.dataset.msg = String(err && (err.stack || err.message) || err);
  });
}, 50);
</script>
</body>`;

const htmlPath = "/tmp/gccx-mermaid.html";
writeFileSync(htmlPath, page);
mkdirSync(outDir, { recursive: true });

const chrome = spawn("/usr/local/bin/google-chrome", [
  "--headless=new",
  "--disable-gpu",
  "--no-sandbox",
  "--allow-file-access-from-files",
  "--remote-debugging-port=9333",
  "--user-data-dir=/tmp/chrome-mermaid-profile",
  "about:blank"
], { stdio: "ignore" });

async function waitVersion() {
  for (let i = 0; i < 50; i += 1) {
    try {
      const res = await fetch("http://127.0.0.1:9333/json/version");
      if (res.ok) return;
    } catch (err) {
      /* chrome still booting */
    }
    await new Promise((resolve) => setTimeout(resolve, 200));
  }
  throw new Error("Chrome DevTools did not open");
}

await waitVersion();
const created = await fetch("http://127.0.0.1:9333/json/new", { method: "PUT" });
const tab = await created.json();
const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {
  ws.addEventListener("open", resolve);
  ws.addEventListener("error", reject);
});
let rpc = 0;
function cdp(method, params = {}) {
  const id = ++rpc;
  return new Promise((resolve, reject) => {
    const onMessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.id !== id) return;
      ws.removeEventListener("message", onMessage);
      if (data.error) reject(new Error(JSON.stringify(data.error)));
      else resolve(data.result);
    };
    ws.addEventListener("message", onMessage);
    ws.send(JSON.stringify({ id, method, params }));
  });
}
await cdp("Page.enable");
await cdp("Page.navigate", { url: "file://" + htmlPath });
let done = "";
for (let i = 0; i < 80; i += 1) {
  const result = await cdp("Runtime.evaluate", { expression: "document.body && document.body.dataset.done || ''", returnByValue: true });
  done = result.result?.value || "";
  if (done) break;
  await new Promise((resolve) => setTimeout(resolve, 250));
}
if (done !== "yes") {
  const msg = await cdp("Runtime.evaluate", { expression: "document.body && document.body.dataset.msg || document.body.innerText || 'empty'", returnByValue: true });
  chrome.kill("SIGKILL");
  throw new Error("mermaid render " + done + " " + (msg.result?.value || ""));
}
const html = await cdp("Runtime.evaluate", { expression: "document.getElementById('out').innerHTML", returnByValue: true });
const dom = html.result?.value || "";
ws.close();
chrome.kill("SIGKILL");

let wrote = 0;
for (const item of diagrams) {
  const start = dom.indexOf(`id="${item.id}"`);
  const end = dom.indexOf(`<!--END ${item.id}-->`);
  if (start < 0 || end < 0) {
    console.error("missing", item.id);
    process.exit(1);
  }
  const chunk = dom.slice(start, end);
  const svgStart = chunk.indexOf("<svg");
  const svgEnd = chunk.lastIndexOf("</svg>");
  if (svgStart < 0 || svgEnd < 0) {
    console.error("no svg", item.id);
    process.exit(1);
  }
  const svg = chunk.slice(svgStart, svgEnd + 6);
  const file = join(outDir, item.id + ".svg");
  writeFileSync(file, svg);
  wrote += 1;
  console.log(item.id, svg.length);
}
writeFileSync(join(outDir, "catalog.json"), JSON.stringify(diagrams.map(({ id, title, caption }) => ({ id, title, caption })), null, 2));
console.log("wrote", wrote);
