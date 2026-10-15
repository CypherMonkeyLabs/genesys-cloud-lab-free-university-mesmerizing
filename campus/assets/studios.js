import { decide } from "./routing-model.js";

const APIS = [
  {
    id: "token",
    title: "Client credentials token",
    method: "POST",
    path: "/oauth/token",
    hostKey: "login",
    cite: "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials",
    note: "Documented for a headless app. The token is not a user, so /api/v2/users/me is unavailable. Send client id and secret only as a Basic header, never in the lab UI.",
    request: "POST /oauth/token HTTP/1.1\nHost: login.mypurecloud.com\nAuthorization: Basic base64(client_id:client_secret)\nContent-Type: application/x-www-form-urlencoded\n\ngrant_type=client_credentials",
    response: "{\n  \"access_token\": \"<returned by the region login host>\",\n  \"token_type\": \"bearer\",\n  \"expires_in\": \"<seconds, from the response>\"\n}"
  },
  {
    id: "users",
    title: "List users",
    method: "GET",
    path: "/api/v2/users",
    hostKey: "api",
    cite: "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials",
    note: "The client-credentials guide shows this call with a bearer token against api.mypurecloud.com for the US East region.",
    request: "GET /api/v2/users?pageSize=25 HTTP/1.1\nHost: api.mypurecloud.com\nAuthorization: Bearer <access_token>\nContent-Type: application/json",
    response: "{\n  \"entities\": [],\n  \"pageSize\": 25,\n  \"pageNumber\": 1,\n  \"total\": 0\n}"
  },
  {
    id: "me",
    title: "users/me with the wrong grant",
    method: "GET",
    path: "/api/v2/users/me",
    hostKey: "api",
    cite: "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials",
    note: "A client-credentials token has no user context. This sample is a lab illustration of that documented limit, not a captured error body.",
    request: "GET /api/v2/users/me HTTP/1.1\nHost: api.mypurecloud.com\nAuthorization: Bearer <client-credentials token>",
    response: "{\n  \"labIllustration\": true,\n  \"status\": 403,\n  \"message\": \"Client-credentials tokens cannot call /api/v2/users/me. Use an authorization-code grant when the call must run as a user.\"\n}"
  },
  {
    id: "queue",
    title: "Create a queue (learning sample)",
    method: "POST",
    path: "/api/v2/routing/queues",
    hostKey: "api",
    cite: "https://help.genesys.cloud/articles/create-queues/",
    note: "Alerting timeout in the admin UI is 7 to 59 seconds. Re-check the Queue schema in the API Explorer before sending this body. The lab does not call the API.",
    request: "POST /api/v2/routing/queues HTTP/1.1\nHost: api.mypurecloud.com\nAuthorization: Bearer <access_token>\nContent-Type: application/json\n\n{\n  \"name\": \"Billing voice\",\n  \"description\": \"Learning sample for Signal Floor\",\n  \"mediaSettings\": {\n    \"call\": { \"alertingTimeoutSeconds\": 8 }\n  }\n}",
    response: "{\n  \"labIllustration\": true,\n  \"name\": \"Billing voice\",\n  \"id\": \"<uuid returned by the platform>\"\n}"
  },
  {
    id: "oauth-grants",
    title: "Grant types to choose",
    method: "NOTE",
    path: "Admin > Integrations > OAuth",
    hostKey: "login",
    cite: "https://help.genesys.cloud/articles/create-an-oauth-client/",
    note: "Documented grants include Client Credentials, Code Authorization with PKCE, and SAML2 Bearer. Token Implicit Grant is documented as deprecated after 25 May 2026.",
    request: "No request. Pick the grant in the OAuth client, then assign only the role and division pairs this integration needs.",
    response: "{\n  \"clientCredentials\": \"services and data actions\",\n  \"authorizationCode\": \"apps that act as a user\",\n  \"implicit\": \"deprecated after 2026-05-25\"\n}"
  }
];

const REGIONS = [
  { id: "use1", label: "Americas (US East) us-east-1", login: "login.mypurecloud.com", api: "api.mypurecloud.com", documentedApi: true },
  { id: "usw2", label: "Americas (US West) us-west-2", login: "login.usw2.pure.cloud", api: "", documentedApi: false },
  { id: "fedramp", label: "FedRAMP us-east-2", login: "login.use2.us-gov-pure.cloud", api: "", documentedApi: false }
];

const BLOCKS = [
  { type: "playAudio", label: "Play Audio", fields: ["prompt"] },
  { type: "collectInput", label: "Collect Input", fields: ["prompt", "digits"] },
  { type: "decision", label: "Decision", fields: ["expression"] },
  { type: "transferAcd", label: "Transfer to ACD", fields: ["queue"] },
  { type: "setData", label: "Set Participant Data", fields: ["name", "value"] },
  { type: "dataAction", label: "Call Data Action", fields: ["action", "inputs"] },
  { type: "callBot", label: "Call Bot Flow", fields: ["bot"] },
  { type: "disconnect", label: "Disconnect", fields: ["reason"] }
];

export function mountStudio(id, root, ctx) {
  const studios = {
    architect: architect,
    routing: routing,
    api: api,
    numbers: numbers,
    migration: migration
  };
  const fn = studios[id];
  if (!fn) {
    ctx.setTitle("Unknown studio");
    root.innerHTML = `<p>That studio is not on the floor. <a href="#/studio">All studios</a></p>`;
    return;
  }
  fn(root, ctx);
}

function architect(root, ctx) {
  ctx.setTitle("Architect-style flow builder");
  const flow = {
    name: "Billing inbound",
    type: "inboundCall",
    division: "Home",
    language: "en-US",
    actions: [
      { type: "playAudio", prompt: "Thanks for calling billing." },
      { type: "collectInput", prompt: "For a bill, press 1.", digits: "1" },
      { type: "transferAcd", queue: "Billing voice" }
    ]
  };
  let selected = 0;
  const draw = () => {
    root.innerHTML = `
      <p>This builder follows Architect’s task list: ordered actions, not a freeform graph. The export is a learning file. It is not an import package for a Genesys org. Flow names must be unique within a type and are limited to 200 characters.</p>
      <div class="builder">
        <div class="panel">
          <h2>Add an action</h2>
          ${BLOCKS.map((block) => `<button class="btn" type="button" data-add="${block.type}">${block.label}</button>`).join("")}
          <p><a href="https://help.genesys.cloud/articles/navigate-the-architect-home-page/">Architect home</a></p>
        </div>
        <div class="panel" id="stack"></div>
        <form class="panel" id="meta">
          <h2>Flow</h2>
          <label>Name <input name="name" maxlength="200" value="${esc(flow.name)}"></label>
          <label>Type <select name="type">
            ${["inboundCall", "inboundMessage", "inboundEmail", "inQueueCall", "bot", "secureCall", "commonModule"].map((type) => `<option ${flow.type === type ? "selected" : ""}>${type}</option>`).join("")}
          </select></label>
          <label>Division <input name="division" value="${esc(flow.division)}"></label>
          <label>Default language <input name="language" value="${esc(flow.language)}"></label>
          <div id="inspector"></div>
          <p id="issues"></p>
          <button class="btn primary" type="button" id="export">Export learning JSON</button>
          <button class="btn" type="button" id="play">Step through</button>
          <pre id="export-out" hidden></pre>
        </form>
      </div>`;
    const stack = root.querySelector("#stack");
    stack.innerHTML = `<h2>Task</h2>` + flow.actions.map((action, index) => {
      const meta = BLOCKS.find((block) => block.type === action.type);
      return `<button class="action ${index === selected ? "sel" : ""}" type="button" data-sel="${index}"><strong>${index + 1}. ${meta.label}</strong><br><span class="muted">${esc(summary(action))}</span></button>`;
    }).join("") || `<p>Add an action to start the task.</p>`;
    stack.querySelectorAll("[data-sel]").forEach((btn) => btn.addEventListener("click", () => { selected = Number(btn.dataset.sel); draw(); }));
    root.querySelectorAll("[data-add]").forEach((btn) => btn.addEventListener("click", () => {
      const type = btn.dataset.add;
      const blank = { type };
      BLOCKS.find((block) => block.type === type).fields.forEach((field) => { blank[field] = ""; });
      flow.actions.push(blank);
      selected = flow.actions.length - 1;
      draw();
    }));
    const action = flow.actions[selected];
    const inspector = root.querySelector("#inspector");
    if (action) {
      const meta = BLOCKS.find((block) => block.type === action.type);
      inspector.innerHTML = `<h2>${meta.label}</h2>` + meta.fields.map((field) => `<label>${field} <input data-field="${field}" value="${esc(action[field] || "")}"></label>`).join("") +
        `<button class="btn" type="button" id="remove">Remove action</button>`;
      inspector.querySelectorAll("[data-field]").forEach((input) => input.addEventListener("input", () => { action[input.dataset.field] = input.value; }));
      inspector.querySelector("#remove").addEventListener("click", () => { flow.actions.splice(selected, 1); selected = 0; draw(); });
    }
    const form = root.querySelector("#meta");
    form.addEventListener("input", () => {
      flow.name = form.name.value;
      flow.type = form.type.value;
      flow.division = form.division.value;
      flow.language = form.language.value;
      root.querySelector("#issues").textContent = issues(flow).join(" ");
    });
    root.querySelector("#issues").textContent = issues(flow).join(" ");
    root.querySelector("#export").addEventListener("click", () => {
      const out = root.querySelector("#export-out");
      out.hidden = false;
      out.textContent = JSON.stringify({
        learningExport: "genesys-cloud-cx-lab",
        notImportable: true,
        modeledOn: "Architect task actions",
        source: "https://help.genesys.cloud/articles/create-a-flow/",
        flow
      }, null, 2);
    });
    root.querySelector("#play").addEventListener("click", () => {
      const out = root.querySelector("#export-out");
      out.hidden = false;
      out.textContent = flow.actions.map((item, index) => `${index + 1}. ${item.type}: ${summary(item)}`).join("\n");
    });
  };
  draw();
}

function issues(flow) {
  const list = [];
  if (!flow.name.trim()) list.push("A flow needs a name.");
  if (flow.name.length > 200) list.push("Names are limited to 200 characters.");
  if (!flow.actions.some((action) => action.type === "transferAcd" || action.type === "disconnect" || action.type === "callBot")) {
    list.push("Give the caller a way out: Transfer to ACD, a bot, or Disconnect.");
  }
  const transfer = flow.actions.find((action) => action.type === "transferAcd");
  if (transfer && !transfer.queue) list.push("Transfer to ACD needs a queue name.");
  return list;
}

function summary(action) {
  return Object.entries(action).filter(([key]) => key !== "type").map(([, value]) => value).filter(Boolean).join(" · ") || "(empty)";
}

function routing(root, ctx) {
  ctx.setTitle("Routing simulator");
  const model = {
    scoring: "conversation",
    evaluation: "all",
    prefer: true,
    elapsedMs: 0,
    rings: [
      { delayMs: 8000, remove: [] },
      { delayMs: 20000, remove: ["Spanish"] }
    ],
    interactions: [{ id: "call-1842", skills: ["Billing", "Spanish"], priority: 0, arrivedMs: 0 }],
    agents: [
      { name: "Amina", onQueue: true, utilized: false, preferred: true, idleMs: 40000, skills: { Billing: 5 } },
      { name: "Leo", onQueue: true, utilized: false, preferred: false, idleMs: 120000, skills: { Billing: 2, Spanish: 4 } },
      { name: "Noor", onQueue: false, utilized: false, preferred: false, idleMs: 300000, skills: { Billing: 5, Spanish: 5 } }
    ]
  };
  const draw = () => {
    const result = decide(model);
    root.innerHTML = `
      <p>Standard and bullseye behavior from the routing articles: On Queue, utilization, all-skills or best-available, and preferred agents considered even when a skill is missing. Five rings and a 2 second to 72 hour delay are the documented limits. This run uses two rings.</p>
      <div class="split">
        <form class="panel" id="queue-form">
          <h2>Queue</h2>
          <label>Scoring <select name="scoring"><option value="conversation">Conversation score</option><option value="priority">Priority score</option></select></label>
          <label>Evaluation <select name="evaluation"><option value="all">All skills matching</option><option value="best">Best available skills</option><option value="disregard">Disregard skills</option></select></label>
          <label class="choice"><input type="checkbox" name="prefer" checked> Preferred agents bypass missing skills</label>
          <label>Elapsed in ring 1 (seconds) <input name="elapsed" type="number" min="0" max="259200" value="0"></label>
          <label>Interaction priority <input name="priority" type="number" min="0" max="10" value="0"></label>
          <p class="muted"><a href="https://help.genesys.cloud/articles/bullseye-routing-overview/">Bullseye routing overview</a></p>
        </form>
        <div class="panel" id="agents"></div>
        <div class="panel"><h2>Trace</h2><pre>${esc(result.trace.join("\n"))}</pre><p><strong>${result.winner ? result.winner.name + " is offered the interaction." : "The interaction keeps waiting."}</strong></p></div>
      </div>`;
    root.querySelector("[name=scoring]").value = model.scoring;
    root.querySelector("[name=evaluation]").value = model.evaluation;
    root.querySelector("[name=prefer]").checked = model.prefer;
    root.querySelector("[name=elapsed]").value = String(model.elapsedMs / 1000);
    root.querySelector("[name=priority]").value = String(model.interactions[0].priority);
    root.querySelector("#queue-form").addEventListener("input", () => {
      const form = root.querySelector("#queue-form");
      model.scoring = form.scoring.value;
      model.evaluation = form.evaluation.value;
      model.prefer = form.prefer.checked;
      model.elapsedMs = Number(form.elapsed.value) * 1000;
      model.interactions[0].priority = Number(form.priority.value);
      draw();
    });
    root.querySelector("#agents").innerHTML = `<h2>Agents</h2>` + model.agents.map((agent, index) => `
      <fieldset><legend>${esc(agent.name)}</legend>
        <label class="choice"><input data-agent="${index}" data-key="onQueue" type="checkbox" ${agent.onQueue ? "checked" : ""}> On Queue</label>
        <label class="choice"><input data-agent="${index}" data-key="utilized" type="checkbox" ${agent.utilized ? "checked" : ""}> Fully utilized</label>
        <label class="choice"><input data-agent="${index}" data-key="preferred" type="checkbox" ${agent.preferred ? "checked" : ""}> Preferred</label>
      </fieldset>`).join("");
    root.querySelectorAll("[data-agent]").forEach((box) => box.addEventListener("change", () => {
      const agent = model.agents[Number(box.dataset.agent)];
      agent[box.dataset.key] = box.checked;
      draw();
    }));
  };
  draw();
}

function api(root, ctx) {
  ctx.setTitle("Platform API explorer");
  let region = REGIONS[0];
  let current = APIS[0];
  const draw = () => {
    const host = current.hostKey === "api" && !region.documentedApi ? region.login : (region[current.hostKey] || region.login);
    const request = current.request.replaceAll("login.mypurecloud.com", region.login);
    const caution = current.hostKey === "api" && !region.documentedApi
      ? "The login host for this region is documented. Confirm the matching API host on the AWS regions article before you send a request. The sample below still shows the US East API host from the client-credentials guide."
      : "";
    root.innerHTML = `
      <p>Samples follow the public client-credentials guide and the queue admin limits. This page never sends them.</p>
      <div class="split">
        <div class="panel">${APIS.map((item) => `<button class="btn" type="button" data-api="${item.id}">${item.method} ${esc(item.title)}</button>`).join("")}</div>
        <div class="panel">
          <h2>${esc(current.title)}</h2>
          <label>Region <select id="region">${REGIONS.map((item) => `<option value="${item.id}">${esc(item.label)}</option>`).join("")}</select></label>
          <p>Host shown for this sample: <strong>${esc(host)}</strong></p>
          ${caution ? `<aside class="uncertainty">${esc(caution)}</aside>` : ""}
          <p>${esc(current.note)}</p>
          <h3>Request</h3>
          <pre>${esc(request)}</pre>
          <h3>Sample JSON</h3>
          <pre>${esc(current.response)}</pre>
          <p><a href="${esc(current.cite)}">Source</a> · <a href="https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/">AWS regions</a></p>
        </div>
      </div>`;
    root.querySelector("#region").value = region.id;
    root.querySelector("#region").addEventListener("change", (ev) => {
      region = REGIONS.find((item) => item.id === ev.target.value);
      draw();
    });
    root.querySelectorAll("[data-api]").forEach((btn) => btn.addEventListener("click", () => {
      current = APIS.find((item) => item.id === btn.dataset.api);
      draw();
    }));
  };
  draw();
}

function numbers(root, ctx) {
  ctx.setTitle("Number plan desk");
  root.innerHTML = `
    <p>Genesys Cloud ships default classifications, including Emergency, Extension, National, International, Network, and a Suicide Prevention plan for 988. A site can hold up to 200 number plans. DIDs route without a custom plan. This desk classifies a dial string with those documented ideas. It is not the in-product call simulator.</p>
    <form class="panel" id="num-form">
      <label>Dialed string <input name="digits" value="911"></label>
      <button class="btn primary" type="submit">Classify</button>
    </form>
    <pre id="num-out"></pre>
    <p><a href="https://help.genesys.cloud/articles/number-plan-information/">Number plan information</a></p>`;
  const form = root.querySelector("#num-form");
  const run = () => {
    const raw = form.digits.value.trim();
    root.querySelector("#num-out").textContent = classify(raw);
  };
  form.addEventListener("submit", (ev) => { ev.preventDefault(); run(); });
  run();
}

function classify(raw) {
  const digits = raw.replace(/[^\d+]/g, "");
  if (digits === "911" || digits === "933") return `${raw}\nClassification: Emergency\nDocumented default for the United States and Canada includes 911 and 933.\nNext: an Emergency outbound route on the site. With BYOC, Genesys is not the emergency provider.`;
  if (digits === "142") return `${raw}\nClassification: Emergency\n142 is the documented Swiss emergency example on the number-plan page.`;
  if (digits === "988") return `${raw}\nClassification: Suicide Prevention\nThe documented default routes 988 to +18002738255. Confirm the live plan before you rely on it.`;
  if (/^\d{4,6}$/.test(digits)) return `${raw}\nClassification: Extension\nDigit length plans match 4 to 6 digits and do not normalize.`;
  if (digits.startsWith("+") && digits.length >= 8 && digits.length <= 16) return `${raw}\nClassification: E.164 number list shape\nAn E.164 list entry keeps the + and is not normalized again.`;
  if (/^\d{10,11}$/.test(digits)) return `${raw}\nClassification: likely Intra-Country or National\nIntra-country matches are normalized to E.164 using the site country code. Test it in the product call simulator.`;
  return `${raw}\nNo default classification matched.\nCustom plans can use a number list or a regular expression. A site allows 200 plans.`;
}

function migration(root, ctx) {
  ctx.setTitle("Migration mapper");
  const rows = [
    ["Genesys Engage routing strategy / IRD", "Architect inbound, in-queue, and common module flows", "Rebuild. This lab has not found a documented one-click import of IRD into Genesys Cloud Architect.", "https://help.genesys.cloud/articles/about-architect/"],
    ["PureConnect / CIC handlers and queues", "Architect flows and Genesys Cloud queues", "Confirm current PureConnect lifecycle on Genesys notices before you pick a cutover date. Do not treat a community date as a contract.", "https://help.genesys.cloud/articles/create-queues/"],
    ["Cisco UCCE routing script", "Architect flow published on a call route", "Concept bridge only. UCCE still owns its own scripting guide.", "https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html"],
    ["UCCE skill group", "Queue membership plus ACD skills", "A skill group is not a Genesys queue. Membership and skills are separate objects.", "https://help.genesys.cloud/articles/advanced-routing-overview/"],
    ["UCCE precision queue", "Bullseye rings and proficiency", "Both expand a target over time. The ring limits (5 rings, 50 skills, 2 seconds to 72 hours) are Genesys settings.", "https://help.genesys.cloud/articles/bullseye-routing-overview/"],
    ["CVP or UCCX IVR", "Architect voice tasks and Audio", "Prompts, menus, and data dips are rebuilt as Architect actions.", "https://help.genesys.cloud/articles/create-a-flow/"],
    ["CUCM / Webex Calling trunk", "BYOC PBX or BYOC Carrier trunk", "Genesys does not replace the CUCM cluster. New BYOC Cloud trunks should use Dynamic Cloud Voice.", "https://help.genesys.cloud/articles/dynamic-cloud-voice-platform-overview/"],
    ["Finesse desktop", "Genesys Cloud workspace, or a CRM embed such as Salesforce or Zendesk", "Screen pop and click-to-dial are features of those documented embeds, not of Finesse itself.", "https://help.genesys.cloud/articles/about-genesys-cloud-for-salesforce/"]
  ];
  root.innerHTML = `<p>A learning bridge. Each row names the object you are leaving and the Genesys object you design instead.</p><div class="scroll"><table><thead><tr><th>From</th><th>Genesys Cloud CX</th><th>What does not move by itself</th><th>Read</th></tr></thead><tbody>
    ${rows.map((row) => `<tr><td>${esc(row[0])}</td><td>${esc(row[1])}</td><td>${esc(row[2])}</td><td><a href="${esc(row[3])}">Doc</a></td></tr>`).join("")}
  </tbody></table></div>`;
}

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
}
