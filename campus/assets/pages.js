import { DIAGRAMS, PORTS, renderDiagram } from "./diagrams.js";
import { wireLightbox } from "./lightbox.js";

export const PAGE_CITES = [
  ...new Set([
    ...DIAGRAMS.map((item) => item.url),
    ...PORTS.map((item) => item.url),
    "https://help.genesys.cloud/articles/about-predictive-engagement/",
    "https://help.genesys.cloud/announcements/genesys-cloud/deprecation-journey-outcomes/",
    "https://help.genesys.cloud/announcements/genesys-cloud/predictive-routing-supports-customer-defined-business-outcomes-with-custom-kpis/",
    "https://help.genesys.cloud/articles/create-an-oauth-client/",
    "https://help.genesys.cloud/articles/workforce-management/",
    "https://help.genesys.cloud/articles/work-with-forecasts/",
    "https://help.genesys.cloud/articles/about-genesys-cloud-for-salesforce/",
    "https://help.genesys.cloud/articles/about-genesys-cloud-for-zendesk/",
    "https://appfoundry.genesys.com/",
    "https://education.genesys.com/certification/cloud",
    "https://help.genesys.cloud/articles/genesys-cloud-ports-services/",
    "https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/",
    "https://help.genesys.cloud/articles/aws-regions-genesys-cloud-voice/",
    "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials"
  ])
];

const HANDLERS = {
  atlas: showAtlas,
  flows: showFlows,
  charts: showCharts,
  play: showPlay,
  downloads: showCheat,
  ports: showPorts,
  game: showGame,
  map: showMap,
  sandbox: showSandbox,
  daily: showDaily,
  badges: showBadges,
  cheat: showCheat,
  roadmap: showRoadmap,
  security: showSecurity,
  career: showCareer,
  "whats-new": showNews,
  playbooks: showPlaybooks,
  deploy: showDeploy,
  architecture: showArchitecture,
  reporting: showReporting,
  regions: showRegions,
  help: showHelp,
  legal: showLegal
};

export function mountPage(name, ctx) {
  const handler = HANDLERS[name];
  if (!handler) {
    ctx.root.innerHTML = `<h1>That wing is not on the floor</h1>`;
    return undefined;
  }
  return handler(ctx);
}

function showFlows(ctx) {
  ctx.setTitle("Flows");
  const flows = DIAGRAMS.filter((item) => item.flow);
  const mermaid = [
    ["sip-sequence", "SIP success path", "Teaching sketch of a call that is answered. Real traces also use 183 and PRACK."],
    ["acd-flow", "ACD eligibility", "Teaching sketch. On Queue, utilization, and skills decide who can be alerted."],
    ["deploy-flow", "Deployment order", "Teaching checklist from region and trunk through a published flow and a queue."],
    ["cutover-flow", "Cutover", "Teaching sequence. One number, then the queue, then the people."],
    ["trouble-flow", "No-audio branch", "Teaching tree. A flow that runs with silence is a media problem."],
    ["data-flow", "Data action", "Teaching sketch. A data action leaves the flow."]
  ];
  const generated = mermaid.map(([id, title, caption]) => `<article class="card lx-card" data-why="${ctx.esc(caption)}"><h3>${ctx.esc(title)}</h3><figure class="mermaid-svg"><img alt="${ctx.esc(caption)}" src="assets/mermaid/${id}.svg"></figure><p class="lx-why">${ctx.esc(caption)}</p><p><button class="btn tiny lx-open" type="button">Enlarge</button></p><p class="muted">Built with Mermaid at generation time. The runtime does not load Mermaid.</p></article>`).join("");
  const cards = flows.map((spec) => `<article class="card lx-card" id="f-${spec.id}" data-why="${ctx.esc(spec.caption)}">${renderDiagram(spec)}<h3>${ctx.esc(spec.title)}</h3><p class="lx-why">${ctx.esc(spec.caption)}</p><p><button class="btn tiny lx-open" type="button">Enlarge</button> <a href="${ctx.esc(spec.url)}">${ctx.esc(spec.cite)}</a></p></article>`).join("");
  ctx.root.innerHTML = `<p class="kicker">Flows</p><h1>${flows.length} animated flows</h1>
    <p>Ladders, routing, architecture, deployment, cutover, and troubleshooting trees from the atlas, plus sequence drawings generated with Mermaid. Enlarge a picture to play the marker.</p>
    <div class="grid atlas-grid">${generated}</div>
    <h2>Atlas flows</h2>
    <div class="grid atlas-grid">${cards}</div>`;
  wireLightbox(ctx.root);
}

async function showCharts(ctx) {
  ctx.setTitle("Charts");
  ctx.root.innerHTML = `<p class="kicker">Charts</p><h1>Counts from this lab</h1>
    <p>These pictures count lessons, minutes, levels, quiz items, diagram kinds, and port-table rows. They are not Genesys production metrics.</p>
    <div id="chart-root"></div>`;
  const mod = await import("./floorviz.js");
  await mod.mountFloor(ctx.root.querySelector("#chart-root"), ctx.state.manifest, null);
}

function showPlay(ctx) {
  ctx.setTitle("Play");
  ctx.root.innerHTML = `<p class="kicker">Play</p><h1>Games on the floor</h1>
    <p>Scores stay in this browser. Nothing here dials a real number.</p>
    <div class="grid">
      <a class="card" href="#/game"><h3>Port game</h3><p>Eight questions from the firewall and trunk articles.</p></a>
      <a class="card" href="#/daily"><h3>Daily challenge</h3><p>One question, seeded by the UTC date.</p></a>
      <a class="card" href="#/sandbox"><h3>Call-flow sandbox</h3><p>Place Architect actions and watch the path.</p></a>
      <a class="card" href="#/badges"><h3>Badges</h3><p>Lessons, the port game, and the Konami code.</p></a>
      <a class="card" href="#/topology"><h3>3D topology</h3><p>Core, BYOC, Edge, and a failure toggle.</p></a>
      <a class="card" href="#/studio/routing"><h3>Routing studio</h3><p>Bullseye, preferred agent, and conversation score.</p></a>
    </div>`;
}

function showAtlas(ctx) {
  ctx.setTitle("Diagram atlas");
  const cards = DIAGRAMS.map((spec) => `
    <article class="card lx-card" id="d-${spec.id}" data-why="${ctx.esc(spec.caption)}">
      ${renderDiagram(spec)}
      <h3>${ctx.esc(spec.title)}</h3>
      <p class="lx-why">${ctx.esc(spec.caption)}</p>
      <p><button class="btn tiny lx-open" type="button">Enlarge</button> <a href="${ctx.esc(spec.url)}">${ctx.esc(spec.cite)}</a></p>
      <p class="dl-bar"><a class="dl-mini" href="downloads/diagrams/${ctx.esc(spec.id)}.svg">SVG</a> <a class="dl-mini" href="downloads/diagrams/${ctx.esc(spec.id)}.png">PNG</a> <a class="dl-mini" href="downloads/diagrams/${ctx.esc(spec.id)}.html">HTML</a></p>
    </article>`).join("");
  ctx.root.innerHTML = `<p class="kicker">Atlas</p><h1>${DIAGRAMS.length} live diagrams</h1>
    <p>Each picture is a teaching sketch. The caption names the limit of the drawing. The link is the source. Enlarge to play, pause, or step the marker.</p>
    <div class="grid atlas-grid">${cards}</div>`;
  wireLightbox(ctx.root);
}

function showRegions(ctx) {
  ctx.setTitle("Regions");
  ctx.root.innerHTML = `<p class="kicker">Residency</p><h1>Regions and the voice boundary</h1>
    <p>An organization is created in one core AWS region. People sign in at that region’s login URL. Satellite regions carry media and cannot host the org. This page names only the hosts this lab has already checked. Every other row stays on the regions article.</p>
    <div class="grid">
      <article class="card">
        <p class="kicker">US East · us-east-1</p>
        <p class="region-num">login.mypurecloud.com</p>
        <p>N. Virginia. The client-credentials guide pairs this login with api.mypurecloud.com. Do not swap the login host and the API host.</p>
      </article>
      <article class="card">
        <p class="kicker">US West · us-west-2</p>
        <p class="region-num">login.usw2.pure.cloud</p>
        <p>Oregon. Confirm the API host on the regions article before a client is configured. This lab does not invent one.</p>
      </article>
      <article class="card">
        <p class="kicker">FedRAMP · us-east-2</p>
        <p class="region-num">login.use2.us-gov-pure.cloud</p>
        <p>US East 2 (Ohio). A different cloud from the commercial login. Confirm the API host on the regions article.</p>
      </article>
    </div>
    <h2>Voice coverage is a second table</h2>
    <p>Genesys Cloud Voice country tables restrict DID, toll-free, domestic, and international calling. FedRAMP voice services on that page are US-only. The European Sovereign region does not extend its sovereignty commitment to calls that leave the boundary. Reload the page before you promise a country.</p>
    <svg class="region-map" viewBox="0 0 720 220" role="img" aria-label="Three cited US login hosts. Other marks are examples, not coverage.">
      <rect width="720" height="220" rx="18" fill="#120818"/>
      <text x="24" y="36" fill="#f4fbff" font-size="16">Cited login hosts</text>
      <g fill="#ff2fb3"><circle cx="180" cy="110" r="16"/><text x="150" y="150" font-size="13">US East</text></g>
      <g fill="#2ff7ff"><circle cx="300" cy="90" r="16"/><text x="270" y="150" font-size="13">US West</text></g>
      <g fill="#d6ff3c"><circle cx="240" cy="150" r="12"/><text x="200" y="186" font-size="13">FedRAMP</text></g>
      <g fill="#b388ff" opacity="0.45"><circle cx="520" cy="80" r="8"/><circle cx="580" cy="130" r="8"/><text x="470" y="170" font-size="13">Example dots, not coverage</text></g>
    </svg>
    <p class="uncertainty"><strong>Not a carrier map. </strong>The purple dots are decoration. They are not countries, not PSTN coverage, and not a list of carriers. Confirm every other login host on the regions article.</p>
    <p><a href="https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/">AWS regions for Genesys Cloud</a> · <a href="https://help.genesys.cloud/articles/aws-regions-genesys-cloud-voice/">AWS regions for Genesys Cloud Voice</a> · <a href="https://developer.genesys.cloud/api/rest/authorization/use-client-credentials">Client credentials grant</a></p>`;
}

function showArchitecture(ctx) {
  ctx.setTitle("Architecture");
  const ids = ["core-region", "voice-path", "digital-path", "byoc-cloud", "byoc-prem", "packages"];
  ctx.root.innerHTML = `<p class="kicker">Architecture</p><h1>Where a conversation lives</h1>
    <p>An organization is born in one core AWS region. Satellite regions carry media and do not host the org. Voice enters through Genesys Cloud Voice or BYOC. Digital enters through Architect without a SIP trunk. CX packages stack voice, then digital and quality, then WEM, then Copilot.</p>
    ${gallery(ctx, ids)}
    <p class="uncertainty"><strong>Unverified as a network diagram. </strong>This is a teaching map. Region hosts other than the ones named in the interview drill stay on the regions article. This lab does not paste carrier IP addresses.</p>`;
}

function showPorts(ctx) {
  ctx.setTitle("Ports and protocols");
  const rows = PORTS.map((row) => `<tr><td>${ctx.esc(row.name)}</td><td>${ctx.esc(row.proto)}</td><td>${ctx.esc(row.port)}</td><td>${ctx.esc(row.dir)}</td><td>${ctx.esc(row.note)}</td><td><a href="${ctx.esc(row.url)}">${ctx.esc(row.source)}</a></td></tr>`).join("");
  ctx.root.innerHTML = `<p class="kicker">Mastery</p><h1>Ports and protocols</h1>
    <p>The firewall articles are the list that changes. This table keeps only the rows this lab opened. Signaling addresses and media addresses are different. Do not type an IP from memory.</p>
    ${one(ctx, "firewall")}
    ${one(ctx, "sip-ladder")}
    ${one(ctx, "sip-rtp")}
    <div class="scroll"><table><thead><tr><th>Use</th><th>Protocol</th><th>Port</th><th>Direction</th><th>What the page says</th><th>Source</th></tr></thead><tbody>${rows}</tbody></table></div>
    <p><a class="btn primary" href="#/game">Play the port game</a> <a class="btn" href="downloads/ports.html">Cheat sheet</a></p>`;
}

function showGame(ctx) {
  ctx.setTitle("Port game");
  const bank = [
    ["TLS trunk signaling commonly uses which TCP port?", "5061", ["5060", "443", "16384"], "The TLS article puts listeners on 5061."],
    ["UDP or TCP trunk signaling commonly uses which port?", "5060", ["5061", "443", "80"], "The transport article names 5060 for UDP and TCP."],
    ["Managed BYOC Cloud phones signal on which TCP port?", "8061", ["5060", "443", "3478"], "The VoIP phone article says 8061 for managed phones."],
    ["Unmanaged phone SIPS uses which TCP port?", "5061", ["8061", "80", "22"], "The same article says 5061 for unmanaged phones."],
    ["RTP and SRTP media use which UDP range?", "16384-65535", ["5060-5061", "80-443", "1024-2048"], "The phone article and the RTP FAQ name that range."],
    ["That media range must be open in which direction, per the FAQ?", "Outbound", ["Inbound only", "Neither", "ICMP only"], "The FAQ says outbound connections."],
    ["BYOC Cloud secure trunks use IPsec?", "No. SIP TLS and SRTP.", ["Yes", "Only on premises Edges", "Only for 911"], "The TLS specification says IPsec is not supported."],
    ["Signaling IPs and media IPs are:", "Different. SDP names the media.", ["Always the same host", "RFC 5737 addresses", "The login host"], "The public SIP article separates them."]
  ];
  let index = 0;
  let correct = 0;
  const root = ctx.root;
  const draw = () => {
    if (index >= bank.length) {
      const best = Math.max(ctx.state.progress.gameBest || 0, correct);
      ctx.state.progress.gameBest = best;
      ctx.saveProgress();
      root.innerHTML = `<p class="kicker">Port game</p><h1>${correct} of ${bank.length}</h1>
        <p>Best in this browser: ${best}. Seven or more earns the Port ace badge.</p>
        <div class="toolbar"><button class="btn primary" type="button" id="again">Play again</button><button class="btn" type="button" id="share">Download result card</button></div>
        <p><a href="#/ports">Back to the table</a></p>`;
      root.querySelector("#again").addEventListener("click", () => { index = 0; correct = 0; draw(); });
      root.querySelector("#share").addEventListener("click", () => shareCard({
        title: "Port mastery",
        score: `${correct} / ${bank.length}`,
        detail: "Genesys Cloud CX · Signal Floor"
      }));
      return;
    }
    const [q, answer, wrongs, why] = bank[index];
    const choices = shuffle([answer, ...wrongs], index);
    root.innerHTML = `<p class="kicker">Port game · ${index + 1} / ${bank.length}</p><h1>${ctx.esc(q)}</h1><div class="choice-grid"></div><p class="muted" id="why"></p>`;
    const grid = root.querySelector(".choice-grid");
    choices.forEach((choice) => {
      const btn = document.createElement("button");
      btn.className = "btn";
      btn.type = "button";
      btn.textContent = choice;
      btn.addEventListener("click", () => {
        const good = choice === answer;
        if (good) correct += 1;
        ctx.blip(good ? 660 : 220, 0.08);
        grid.querySelectorAll("button").forEach((el) => { el.disabled = true; });
        btn.classList.add(good ? "good" : "bad");
        root.querySelector("#why").textContent = (good ? "Correct. " : "Not this one. ") + why;
        const next = document.createElement("button");
        next.className = "btn primary";
        next.type = "button";
        next.textContent = "Next";
        next.addEventListener("click", () => { index += 1; draw(); });
        root.querySelector("#why").after(next);
      });
      grid.appendChild(btn);
    });
  };
  draw();
}

function showMap(ctx) {
  ctx.setTitle("Flow map");
  const nodes = [
    ["carrier", "Carrier / PSTN", "#/track/byoc", 70, 150],
    ["edge", "Edge", "#/track/edge", 190, 70],
    ["arch", "Architect", "#/track/architect", 320, 150],
    ["queue", "Queue", "#/track/queues", 460, 70],
    ["agent", "Agent", "#/track/acd", 600, 150],
    ["pe", "Web journey", "#/track/predictive", 190, 220],
    ["wem", "WEM", "#/track/wfm", 460, 220]
  ];
  const dots = nodes.map(([id, label, href, x, y]) => `
    <a href="${href}"><g class="map-node">
      <rect x="${x - 58}" y="${y - 22}" width="116" height="44" rx="14" fill="#d6f25c" />
      <text x="${x}" y="${y + 5}" text-anchor="middle" font-size="13" fill="#1a0c08">${ctx.esc(label)}</text>
    </g></a>`).join("");
  ctx.root.innerHTML = `<p class="kicker">Explorer</p><h1>Flow map</h1>
    <p>Click a node to open the track. The 3D floor is a different view.</p>
    <figure><svg class="diagram" viewBox="0 0 700 280" role="img" aria-label="Clickable map from the carrier through Architect to an agent, with the website and WEM beside the path.">
      <rect width="700" height="280" rx="20" fill="#10203a" />
      <path d="M70 150 H320 H600 M190 70 V150 M460 70 V220" stroke="#fff" stroke-dasharray="6 6" fill="none" class="dash" />
      ${dots}
    </svg></figure>
    <p><a class="btn" href="#/topology">Open the 3D floor</a> <a class="btn" href="#/sandbox">Build a call flow</a></p>`;
}

function showSandbox(ctx) {
  ctx.setTitle("Call flow sandbox");
  const actions = ["Play audio", "Collect digits", "Menu", "Call bot", "Data action", "Secure flow", "Transfer to queue", "Disconnect"];
  const flow = [];
  const root = ctx.root;
  const draw = () => {
    root.innerHTML = `<p class="kicker">Sandbox</p><h1>Build a learning flow</h1>
      <p>This is a vertical task list for practice. The JSON it exports is marked not importable. Architect in a live org is the product.</p>
      <div class="split"><div class="sandbox-list">${actions.map((name) => `<button class="action" type="button" data-add="${ctx.esc(name)}">${ctx.esc(name)}</button>`).join("")}</div>
      <div><h2>Task list</h2><ol id="tasks">${flow.map((name) => `<li>${ctx.esc(name)}</li>`).join("") || "<li>Empty. Add a way for the caller to leave.</li>"}</ol>
      <pre id="export"></pre>
      <button class="btn" type="button" id="clear">Clear</button></div></div>`;
    root.querySelectorAll("[data-add]").forEach((btn) => btn.addEventListener("click", () => {
      flow.push(btn.dataset.add);
      ctx.state.progress.sandbox = Math.max(ctx.state.progress.sandbox || 0, flow.length);
      ctx.saveProgress();
      ctx.blip(520, 0.05);
      draw();
    }));
    const blob = { lab: "signal-floor", importable: false, tasks: flow };
    root.querySelector("#export").textContent = JSON.stringify(blob, null, 2);
    root.querySelector("#clear").addEventListener("click", () => { flow.length = 0; draw(); });
  };
  draw();
}

function showDaily(ctx) {
  ctx.setTitle("Daily challenge");
  const bank = [
    ["A published flow is required because:", "A saved draft does not run", ["Drafts run at night", "Live Now publishes flows", "The Edge publishes them"], "Create a flow."],
    ["Conversation score treats one priority point as:", "60,000 milliseconds", ["One hour", "One ring", "Five skills"], "Create queues."],
    ["Bullseye allows up to:", "5 rings", ["50 rings", "200 rings", "1 ring"], "Bullseye routing overview."],
    ["Client credentials cannot call:", "/api/v2/users/me", ["/api/v2/routing/queues", "The login host", "OAuth"], "Client credentials guide."],
    ["Journey Outcomes were planned to end on:", "2026-06-29", ["2026-05-25", "2024-01-01", "Never"], "Deprecation announcement. Re-open it."],
    ["Short-term forecasts can:", "Generate a schedule", ["Replace Architect", "Open port 5061", "Last two years only"], "Work with forecasts."],
    ["BYOC emergency is provided by:", "Your carrier, not Genesys", ["A satellite region", "Agent Copilot", "AppFoundry"], "BYOC emergency article."],
    ["Web messaging tracking belongs on:", "The Messenger snippet", ["Both snippets at once", "The Edge", "A number plan"], "Migration article."]
  ];
  const today = new Date().toISOString().slice(0, 10);
  const index = [...today].reduce((sum, ch) => sum + ch.charCodeAt(0), 0) % bank.length;
  const [q, answer, wrongs, why] = bank[index];
  const choices = shuffle([answer, ...wrongs], index);
  const root = ctx.root;
  root.innerHTML = `<p class="kicker">UTC ${ctx.esc(today)}</p><h1>Daily challenge</h1><h2>${ctx.esc(q)}</h2><div class="choice-grid"></div>`;
  const grid = root.querySelector(".choice-grid");
  choices.forEach((choice) => {
    const btn = document.createElement("button");
    btn.className = "btn";
    btn.type = "button";
    btn.textContent = choice;
    btn.addEventListener("click", () => {
      const good = choice === answer;
      grid.querySelectorAll("button").forEach((el) => { el.disabled = true; });
      btn.classList.add(good ? "good" : "bad");
      const daily = ctx.state.progress.daily || { last: "", streak: 0 };
      if (daily.last !== today) {
        const yesterday = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
        daily.streak = daily.last === yesterday ? daily.streak + 1 : 1;
        daily.last = today;
        daily.correct = good;
      }
      ctx.state.progress.daily = daily;
      ctx.saveProgress();
      root.insertAdjacentHTML("beforeend", `<p>${good ? "Correct." : "Not this one."} ${ctx.esc(why)}</p><p>Streak in this browser: ${daily.streak} UTC day${daily.streak === 1 ? "" : "s"}.</p><button class="btn" type="button" id="share">Result card</button>`);
      root.querySelector("#share").addEventListener("click", () => shareCard({
        title: "Daily challenge",
        score: good ? "Correct" : "Reviewed",
        detail: today + " · streak " + daily.streak
      }));
    });
    grid.appendChild(btn);
  });
}

function showBadges(ctx) {
  ctx.setTitle("Badges");
  const done = Object.values(ctx.state.progress.lessons || {}).filter((item) => item.done).length;
  const badges = [
    ["First light", done >= 1, "Finish a lesson quiz at 5 of 6 or complete its lab after that."],
    ["Five deep", done >= 5, "Finish five lessons."],
    ["Port ace", (ctx.state.progress.gameBest || 0) >= 7, "Score at least 7 on the port game."],
    ["Streak", ((ctx.state.progress.daily || {}).streak || 0) >= 2, "Answer the daily challenge on two UTC days in a row."],
    ["Sandbox", (ctx.state.progress.sandbox || 0) >= 4, "Add four actions in the call-flow sandbox."],
    ["Konami", Boolean(ctx.state.progress.konami), "The classic code, on this page."],
    ["Offline", Boolean(ctx.state.progress.offlineSaved), "Use Save for offline in the top bar or Settings."]
  ];
  ctx.root.innerHTML = `<p class="kicker">This browser</p><h1>Badges</h1>
    <p>${done} lessons finished. Badges stay in localStorage on this device.</p>
    <div class="grid">${badges.map(([name, on, how]) => `<article class="card badge"><div><h3>${ctx.esc(name)}</h3><p>${ctx.esc(how)}</p></div><em>${on ? "Earned" : "Locked"}</em></article>`).join("")}</div>`;
}

async function showCheat(ctx) {
  ctx.setTitle("Cheat codes");
  let catalog = { sheets: [] };
  try {
    const res = await fetch("downloads/catalog.json");
    if (res.ok) catalog = await res.json();
  } catch (err) {
    catalog = { sheets: [], error: true };
  }
  const cards = (catalog.sheets || []).map((sheet) => `<article class="card"><h3>${ctx.esc(sheet.title)}</h3><p>${ctx.esc(sheet.summary)}</p>
    <p><a href="${ctx.esc(sheet.html)}">HTML</a> · <a href="${ctx.esc(sheet.pdf)}">PDF</a> · <a href="${ctx.esc(sheet.png)}">PNG</a> · <a href="${ctx.esc(sheet.svg)}">SVG</a></p>
    <p class="muted">${(sheet.sources || []).map((url) => `<a href="${ctx.esc(url)}">${ctx.esc(hostOf(url))}</a>`).join(" · ")}</p></article>`).join("");
  ctx.root.innerHTML = `<p class="kicker">Downloads</p><h1>Cheat codes</h1>
    <p>One-page sheets, a printable flashcard deck, and a zip of this lab. Each file carries the lab footer. They summarize and link. They are not copies of the Resource Center.</p>
    <div class="dl-bar" data-dl-scope="downloads"><span class="dl-kicker">Download</span><button type="button" class="dl-mini" data-export="html">HTML</button><a class="dl-mini" href="downloads/genesys-cx-offline-bundle.zip">Bundle</a></div>
    <div class="toolbar">
      <a class="btn primary" href="downloads/flashcards.html">Flashcards HTML</a>
      <a class="btn" href="downloads/flashcards.json">JSON</a>
      <a class="btn" href="downloads/flashcards.pdf">PDF</a>
      <a class="btn" href="downloads/genesys-cx-deck.pptx">PPTX deck</a>
      <a class="btn" href="downloads/templates/lab-checklist.docx">DOCX</a>
      <a class="btn" href="downloads/templates/lab-checklist.pdf">Template PDF</a>
      <a class="btn" href="downloads/templates/lab-checklist.html">Template HTML</a>
      <a class="btn" href="downloads/test-table.html">Test table</a>
      <a class="btn" href="downloads/genesys-cx-offline-bundle.zip">Offline bundle</a>
      <button type="button" class="btn open-app">Open app</button>
      <a class="btn" href="https://github.com/CypherMonkeyLabs/genesys-cloud-lab-free-university-mesmerizing">View repo</a>
    </div>
    <div class="grid">${cards || "<p>The download catalog has not been generated.</p>"}</div>`;
}

function showRoadmap(ctx) {
  ctx.setTitle("Roadmap");
  ctx.root.innerHTML = `<p class="kicker">Study plan, not a vendor roadmap</p><h1>30 days on this floor</h1>
    <p>This sequence is the lab’s suggestion. Genesys does not publish it. Product changes for 2026 are on What’s new, with the pages named.</p>
    <ol class="ladder">
      <li><a href="#/track/foundations">Days 1–4 · Foundations</a></li>
      <li><a href="#/track/org">Days 5–8 · Organization and licensing</a></li>
      <li><a href="#/track/architect">Days 9–12 · Architect</a></li>
      <li><a href="#/track/acd">Days 13–16 · ACD and queues</a></li>
      <li><a href="#/track/byoc">Days 17–20 · BYOC, Edge, emergency, ports</a></li>
      <li><a href="#/track/wfm">Days 21–24 · WEM, quality, analytics</a></li>
      <li><a href="#/track/predictive">Days 25–27 · Predictive Engagement and AI</a></li>
      <li><a href="#/track/api">Days 28–30 · APIs, CRM, migration, interview</a></li>
    </ol>
    ${one(ctx, "certs-path")}
    <p><a class="btn" href="#/certs">Certification catalog</a> <a class="btn" href="#/whats-new">What’s new</a></p>`;
}

function showSecurity(ctx) {
  ctx.setTitle("Security");
  ctx.root.innerHTML = `<p class="kicker">Security and compliance</p><h1>Close the doors you actually have</h1>
    <p>Secure BYOC Cloud trunks use TLS 1.2 on TCP 5061 and SRTP. The TLS article says IPsec is not the method. Secure call flows keep payment digits out of the recording. Divisions plus role pairs are the permission boundary. Client-credentials tokens have no user, so <code>/api/v2/users/me</code> is the wrong call. The OAuth article dates Token Implicit Grant as deprecated after 25 May 2026.</p>
    <p>The About Predictive Engagement page points at Genesys Cloud and GDPR material. This lab does not restate that legal page. It also does not claim a certification such as SOC 2 or HIPAA; those words are absent here on purpose.</p>
    ${one(ctx, "srtp-lock")}
    ${one(ctx, "oauth")}
    <p><a href="https://help.genesys.cloud/articles/tls-trunk-transport-protocol-specification/">TLS trunk transport</a> ·
      <a href="https://help.genesys.cloud/articles/create-an-oauth-client/">OAuth client</a> ·
      <a href="https://developer.genesys.cloud/api/rest/authorization/use-client-credentials">Client credentials</a> ·
      <a href="https://help.genesys.cloud/articles/divisions-overview/">Divisions</a></p>
    <p class="uncertainty"><strong>Unverified. </strong>Compliance scope for a real organization is a contract and a questionnaire, not this page.</p>`;
}

function showCareer(ctx) {
  ctx.setTitle("Career paths");
  ctx.root.innerHTML = `<p class="kicker">Practice, not a job offer</p><h1>Paths through the tracks</h1>
    <div class="grid">
      <article class="card"><h3>Administrator</h3><p>Organization, queues, divisions, licensing. Then GC-GCP if the catalog still matches your job.</p><p><a href="#/track/org">Org</a> · <a href="#/certs">Certs</a></p></article>
      <article class="card"><h3>Flow designer</h3><p>Architect, bots, in-queue, secure flows. The Architect specialist row is a name, not a code this lab invents.</p><p><a href="#/track/architect">Architect</a> · <a href="#/sandbox">Sandbox</a></p></article>
      <article class="card"><h3>Telephony</h3><p>BYOC, Edge, number plans, emergency, and the port table.</p><p><a href="#/ports">Ports</a> · <a href="#/track/emergency">Emergency</a></p></article>
      <article class="card"><h3>WEM analyst</h3><p>Forecasts, schedules, quality, speech and text analytics.</p><p><a href="#/track/wfm">WFM</a> · <a href="#/reporting">Reporting</a></p></article>
      <article class="card"><h3>Developer</h3><p>Grants, the API explorer, AppFoundry. GC-GCD is the developer exam the catalog names.</p><p><a href="#/track/api">APIs</a> · <a href="#/studio/api">API studio</a></p></article>
    </div>
    <p><a class="btn primary" href="#/interview">Interview drill</a></p>
    <p class="muted">Nothing here promises a role, a certificate, or that a package includes a product. Read the overview and the catalog.</p>`;
}

function showNews(ctx) {
  ctx.setTitle("What’s new");
  ctx.root.innerHTML = `<p class="kicker">Read on 15 October 2026</p><h1>What’s new, as the pages said</h1>
    <article class="card"><h3>Journey Outcomes deprecation</h3><p>Announced 2026-05-18. Planned effective date 2026-06-29. After that date the announcement says outcomes are not processed, do not trigger action maps, and reporting goes away. Customer Outcomes is described as under development and will not include outcome scoring.</p><p><a href="https://help.genesys.cloud/announcements/genesys-cloud/deprecation-journey-outcomes/">Announcement</a></p></article>
    <article class="card"><h3>Predictive Routing custom outcomes</h3><p>A separate announcement describes a future framework for customer-defined KPIs, including metrics outside Genesys Cloud. It says existing predictive-routing configurations need no change until you migrate. This lab has not confirmed that the framework has shipped.</p><p><a href="https://help.genesys.cloud/announcements/genesys-cloud/predictive-routing-supports-customer-defined-business-outcomes-with-custom-kpis/">Announcement</a></p></article>
    <article class="card"><h3>Web chat toward web messaging</h3><p>The about page encourages web messaging. The migration article says remove the legacy tracking snippet when Messenger is tracking, or you double-count.</p><p><a href="https://help.genesys.cloud/articles/migrate-from-web-chat-to-web-messaging-for-digital-user-tracking-and-predictive-engagement/">Migration</a></p></article>
    <article class="card"><h3>Implicit grant</h3><p>The OAuth client article documents Token Implicit Grant as deprecated after 25 May 2026. Move user-facing apps to authorization code with PKCE.</p><p><a href="https://help.genesys.cloud/articles/create-an-oauth-client/">OAuth client</a></p></article>
    <p class="uncertainty"><strong>Unverified in a live org. </strong>Dates are the ones printed on those pages when this lab was built. If a page moved a date, the page wins.</p>
    ${one(ctx, "pe-sunset")}`;
}

function showPlaybooks(ctx) {
  ctx.setTitle("Playbooks");
  const rows = [
    ["No audio, flow still runs", "Media or the trunk. Architect Insights can be healthy while RTP is not.", "#/boss", "BYOC and the RTP FAQ"],
    ["Menu works, silence on hold", "The in-queue flow is unpublished or empty.", "#/track/architect", "In-queue flows"],
    ["Agent never alerts", "On Queue, utilization, skills, or a bullseye ring that has not opened.", "#/studio/routing", "Evaluation methods"],
    ["Screen pop dead, call fine", "The CRM embed failed. The queue did not.", "#/track/crm", "Salesforce and Zendesk about pages"],
    ["Website offers never fire", "Live Now is empty, the segment is too tight, or a schedule group hid the offer.", "#/track/predictive", "Messenger and action maps"],
    ["Emergency test", "Do not place a live emergency call as a demo. Confirm class, route, and owner.", "#/track/emergency", "BYOC emergency"]
  ];
  ctx.root.innerHTML = `<p class="kicker">Troubleshooting</p><h1>Playbooks</h1>
    <p>Synthetic logs in the boss incidents use RFC 5737 addresses. Start with the symptom, then open the track. Do not paste a lab address into a carrier ACL.</p>
    <div class="grid">${rows.map(([title, body, href, source]) => `<article class="card"><h3>${ctx.esc(title)}</h3><p>${ctx.esc(body)}</p><p><a href="${href}">Open</a> · ${ctx.esc(source)}</p></article>`).join("")}</div>
    ${one(ctx, "acd-gate")}`;
}

function showDeploy(ctx) {
  ctx.setTitle("Deployment");
  ctx.root.innerHTML = `<p class="kicker">Configuration walkthrough</p><h1>A first deployment, in order</h1>
    <p>This is a checklist of objects the existing lessons already teach. It is not a statement that every org needs every row.</p>
    <ol>
      <li><a href="#/track/org">Place the org in a core region. Create divisions and role pairs. Pick CX 1, 2, 3, or 4 on purpose.</a></li>
      <li><a href="#/track/byoc">For BYOC Cloud: location, trunk, outbound route, number plan. Match the transport on both ends.</a></li>
      <li><a href="#/track/edge">For premises: Edge group, phone trunk, site, and a failover site that actually has the resource.</a></li>
      <li><a href="#/ports">Open the signaling port you chose and outbound UDP 16384-65535. Copy IPs from the current regional article.</a></li>
      <li><a href="#/track/emergency">Name the emergency owner before the first DID. Class, route, and a test plan that is not a surprise 911 call.</a></li>
      <li><a href="#/track/architect">Publish the inbound flow and the in-queue flow. Add a bot only with a failure queue.</a></li>
      <li><a href="#/track/queues">Create the queue in a division, members, skills, wrap-up, service level.</a></li>
      <li><a href="#/track/wfm">If the package is CX 3 or higher: business unit, forecast, schedule.</a></li>
      <li><a href="#/track/predictive">If you sell on the web: one snippet, segments, an action map that survives the outcome deprecation.</a></li>
    </ol>
    ${one(ctx, "cutover")}`;
}

function showReporting(ctx) {
  ctx.setTitle("Reporting");
  ctx.root.innerHTML = `<p class="kicker">Reporting and analytics</p><h1>Three clocks</h1>
    <p>Queue service level is a percentage inside a target number of seconds, on the queue. Workforce intraday compares forecast to actual. Speech and text analytics reads the conversation after the channel has it. Predictive Engagement adds Live Now, visitor activity, and action-map performance. Outcome columns on that last set age out with the Journey Outcomes deprecation.</p>
    ${one(ctx, "sta-pipe")}
    ${one(ctx, "wfm-loop")}
    <p><a href="https://help.genesys.cloud/articles/speech-and-text-analytics-overview/">STA overview</a> ·
      <a href="https://help.genesys.cloud/articles/workforce-management/">Workforce management</a> ·
      <a href="https://help.genesys.cloud/articles/about-predictive-engagement/">Predictive Engagement</a> ·
      <a href="#/track/qm">Quality track</a></p>
    <p class="uncertainty"><strong>Unverified. </strong>The use case names action-map performance for web chat, content offers, and Architect flow. Confirm a web-messaging column on the live report before you call it missing.</p>`;
}

function gallery(ctx, ids) {
  return `<div class="grid">${ids.map((id) => one(ctx, id)).join("")}</div>`;
}

function one(ctx, id) {
  const spec = DIAGRAMS.find((item) => item.id === id);
  if (!spec) return "";
  return `<article class="card">${renderDiagram(spec)}<h3>${ctx.esc(spec.title)}</h3><p>${ctx.esc(spec.caption)}</p><p><a href="${ctx.esc(spec.url)}">${ctx.esc(spec.cite)}</a></p></article>`;
}

function showHelp(ctx) {
  ctx.setTitle("Help");
  ctx.root.innerHTML = `<p class="kicker">How to use this lab</p><h1>Help</h1>
    ${ctx.downloadBar ? "" : ""}
    <div class="dl-bar" data-dl-scope="help"><span class="dl-kicker">Download</span><button type="button" class="dl-mini" data-export="html">HTML</button><a class="dl-mini" href="downloads/genesys-cx-offline-bundle.zip">Bundle</a></div>
    <section class="learn5" id="sec-learn5"><h2>Learn it in 5 minutes</h2>
      <ol>
        <li>Menu, at the top left, opens every room. Esc or a tap outside closes it.</li>
        <li>Learn opens the tracks. Each lesson has a figure, a worked example, a quiz, and sources.</li>
        <li>Diagrams, Play, Listen, and Downloads are on the banner. On a phone they sit in the bottom bar with Guide.</li>
        <li>The monkey reads a room aloud, takes a question, and can listen if the browser allows a microphone.</li>
        <li>Downloads stay on this device. Nothing is sent to an organization.</li>
      </ol>
    </section>
    <h2>Menu</h2><p>One drawer lists the rooms with an icon, a name, and a one-line description. Search inside the drawer looks at lesson titles.</p>
    <h2>Course</h2><p>Start with Foundations, then Architect, routing, and the trunk. The roadmap is a study order, not a vendor plan.</p>
    <h2>Bot</h2><p>After the first-open tour, the guide offers a 10-minute path, the full course, or a download. It docks on the right. Drag it if you want it elsewhere. Idle offers stop when you choose Stop offering.</p>
    <p><button type="button" class="btn primary" data-replay-tour>Replay the tour</button></p>
    <h2>Downloads</h2><p>Every room has a download button. Sheets are HTML, PDF, PNG, and SVG. Flashcards are HTML, JSON, and PDF. The checklist template is DOCX, PDF, and HTML. The deck is PPTX. The test table lists what was generated.</p>
    <h2>Worked example</h2><p>Open Menu, choose Learn, open Foundations, and finish the first quiz. The score stays in this browser.</p>
    <h2>Quiz</h2>
    <form class="panel" data-mini-quiz data-answer="0">
      <p>Where do you reopen the first-open tour?</p>
      <label><input type="radio" name="hq" value="0"> Help, Replay the tour</label>
      <label><input type="radio" name="hq" value="1"> A vendor support case</label>
      <button type="button" class="btn" data-quiz-check>Check</button>
      <p class="muted" data-quiz-note></p>
    </form>
    <h2>Sources</h2><ul><li><a href="https://help.genesys.cloud/articles/about-architect/">About Architect</a></li></ul>
    <section class="eco-panel" id="sec-eco"><h2>Ecosystem</h2><p>The same glossary, mind map, sister technologies, troubleshooting notes, integration map, cross-platform bridge, and future-hook notes appear on each lesson. Confirm before relying.</p><p><a href="#/ecosystem">Open the ecosystem map</a></p></section>`;
}

function showLegal(ctx) {
  ctx.setTitle("Legal and credits");
  ctx.root.innerHTML = `<p class="kicker">Credits</p><h1>Legal and credits</h1>
    <div class="dl-bar" data-dl-scope="legal"><span class="dl-kicker">Download</span><button type="button" class="dl-mini" data-export="html">HTML</button></div>
    <section class="learn5" id="sec-learn5"><h2>Learn it in 5 minutes</h2>
      <ol>
        <li>Code in this repository is MIT.</li>
        <li>The study prose is CC BY-NC-SA 4.0.</li>
        <li>Three.js stays under the license in vendor/THREE-LICENSE.txt.</li>
        <li>Vendor names and marks belong to their owners.</li>
        <li>This lab does not track you. Progress stays in this browser.</li>
      </ol>
    </section>
    <h2>Copyright</h2><p>© 2026 CypherMonkeyLabs. The lab text and figures are study notes. They are not copies of the Genesys Cloud Resource Center.</p>
    <h2>Trademark</h2><p>Genesys, Genesys Cloud, Architect, AppFoundry, and other product names belong to their owners. Cisco names belong to Cisco. This project is not affiliated with or endorsed by any of them.</p>
    <h2>Third-party licences</h2>
    <ul>
      <li>MIT for this repository’s code. See the LICENSE file.</li>
      <li>CC BY-NC-SA 4.0 for the educational prose.</li>
      <li>Three.js is MIT. The notice is vendor/THREE-LICENSE.txt.</li>
      <li>Anime.js, D3, Rough.js, canvas-confetti, and Markmap stay under the notices in vendor/LICENSES.txt. Confirm before relying if a bundled file’s header and that list ever disagree.</li>
    </ul>
    <h2>Privacy</h2><p>No account, no analytics beacon, and no call to a Genesys organization. Settings, tour state, and quiz scores use localStorage on this device. The optional microphone and speech features use the browser APIs and do not upload audio.</p>
    <h2>Accessibility</h2><p>Display controls set font size and font colour. A dark theme is optional. The drawer and the tour work from the keyboard. Reduced motion follows the operating system and the Reduce motion control when it is present.</p>
    <h2>Removal request</h2><p>If a rightsholder wants something removed or corrected, use the contact form at <a href="https://cyphermonkeylabs.com/#contact">https://cyphermonkeylabs.com/#contact</a>. This lab will remove or correct the content. Nothing here is sold.</p>
    <h2>Worked example</h2><p>A diagram download includes the same disclaimer as this page. The file is a teaching sketch plus the source link, not a pasted vendor document.</p>
    <h2>Quiz</h2>
    <form class="panel" data-mini-quiz data-answer="1">
      <p>Where does quiz progress live?</p>
      <label><input type="radio" name="lq" value="0"> A Genesys organization</label>
      <label><input type="radio" name="lq" value="1"> This browser only</label>
      <button type="button" class="btn" data-quiz-check>Check</button>
      <p class="muted" data-quiz-note></p>
    </form>
    <h2>Sources</h2><ul>
      <li><a href="https://help.mypurecloud.com/articles/overview-of-genesys-cloud/">Overview of Genesys Cloud</a></li>
      <li><a href="vendor/LICENSES.txt">vendor/LICENSES.txt</a></li>
      <li><a href="vendor/THREE-LICENSE.txt">vendor/THREE-LICENSE.txt</a></li>
    </ul>
    <section class="eco-panel" id="sec-eco"><h2>Ecosystem</h2><p>Sister technologies in the notes are SIP, RTP, and the documented embeds. Confirm before relying.</p></section>`;
}

function hostOf(url) {
  try { return new URL(url).hostname; } catch (err) { return url; }
}

function shuffle(list, seed) {
  const copy = list.slice();
  let state = seed + 17;
  for (let i = copy.length - 1; i > 0; i -= 1) {
    state = (state * 1103515245 + 12345) % 2147483648;
    const j = state % (i + 1);
    const tmp = copy[i];
    copy[i] = copy[j];
    copy[j] = tmp;
  }
  return copy;
}

export function shareCard({ title, score, detail }) {
  const canvas = document.createElement("canvas");
  canvas.width = 1200;
  canvas.height = 630;
  const g = canvas.getContext("2d");
  g.fillStyle = "#07101c";
  g.fillRect(0, 0, 1200, 630);
  g.fillStyle = "#3ee0ff";
  g.fillRect(0, 0, 18, 630);
  g.fillStyle = "#f4fbff";
  g.font = "64px Georgia, serif";
  g.fillText("Signal Floor", 64, 140);
  g.font = "42px Georgia, serif";
  g.fillText(title, 64, 230);
  g.fillStyle = "#d6f25c";
  g.font = "80px Georgia, serif";
  g.fillText(score, 64, 360);
  g.fillStyle = "#b7c6e6";
  g.font = "28px sans-serif";
  g.fillText(detail, 64, 440);
  g.fillText("https://cyphermonkeylabs.com", 64, 540);
  const link = document.createElement("a");
  link.href = canvas.toDataURL("image/png");
  link.download = "signal-floor-result.png";
  link.click();
}
