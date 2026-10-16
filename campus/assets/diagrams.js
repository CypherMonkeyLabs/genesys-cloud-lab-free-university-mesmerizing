/** Animated teaching diagrams. Labels restate public docs; they are not a second source of truth. */

const C = {
  regions: ["AWS regions", "https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/"],
  sip: ["RFC 3261 SIP", "https://www.rfc-editor.org/rfc/rfc3261"],
  rtp: ["RFC 3550 RTP", "https://www.rfc-editor.org/rfc/rfc3550"],
  srtp: ["RFC 3711 SRTP", "https://www.rfc-editor.org/rfc/rfc3711"],
  dtmf: ["RFC 4733 DTMF", "https://www.rfc-editor.org/rfc/rfc4733"],
  byoc: ["About BYOC Cloud", "https://help.genesys.cloud/articles/about-byoc-cloud/"],
  transport: ["Choose a trunk transport protocol", "https://help.genesys.cloud/articles/choose-a-trunk-transport-protocol/"],
  tls: ["TLS trunk transport for BYOC Cloud", "https://help.genesys.cloud/articles/tls-trunk-transport-protocol-specification/"],
  phones: ["VoIP phone ports under BYOC Cloud", "https://help.genesys.cloud/articles/ports-and-services-for-voip-phones-under-byoc-cloud/"],
  rtpFaq: ["RTP port range FAQ", "https://help.genesys.cloud/faqs/why-does-the-port-range-16384-32767-rtp-media-need-to-be-opened-up-for-genesys-cloud-voice-byoc-cloud/"],
  sipIp: ["BYOC Cloud public SIP IP addresses", "https://help.genesys.cloud/articles/byoc-cloud-public-sip-ip-addresses/"],
  fw: ["Ports and services for your firewall", "https://help.genesys.cloud/articles/genesys-cloud-ports-services/"],
  edge: ["BYOC Premises Edge groups", "https://help.genesys.cloud/articles/edge-groups-overview/"],
  arch: ["About Architect", "https://help.genesys.cloud/articles/about-architect/"],
  flow: ["Create a flow", "https://help.genesys.cloud/articles/create-a-flow/"],
  inq: ["In-queue flows", "https://help.genesys.cloud/articles/queue-call-flows/"],
  route: ["Advanced routing overview", "https://help.genesys.cloud/articles/advanced-routing-overview/"],
  bull: ["Bullseye routing", "https://help.genesys.cloud/articles/bullseye-routing-overview/"],
  pref: ["Preferred agent routing", "https://help.genesys.cloud/articles/preferred-agent-routing-behavior/"],
  evalm: ["Evaluation methods", "https://help.genesys.cloud/articles/acd-evaluation-routing-methods/"],
  queue: ["Create queues", "https://help.genesys.cloud/articles/create-queues/"],
  util: ["Agent utilization", "https://help.genesys.cloud/articles/utilization/"],
  emerg: ["BYOC emergency", "https://help.genesys.cloud/articles/set-up-emergency-services-with-byoc/"],
  numbers: ["Number plans", "https://help.genesys.cloud/articles/number-plan-information/"],
  wem: ["About WEM", "https://help.genesys.cloud/articles/about-workforce-engagement-management-wem/"],
  wfm: ["Workforce management", "https://help.genesys.cloud/articles/workforce-management/"],
  forecasts: ["Work with forecasts", "https://help.genesys.cloud/articles/work-with-forecasts/"],
  qm: ["About quality management", "https://help.genesys.cloud/50540/"],
  rec: ["About recording", "https://help.genesys.cloud/articles/about-recording/"],
  sta: ["Speech and text analytics", "https://help.genesys.cloud/articles/speech-and-text-analytics-overview/"],
  bot: ["Dialog Engine bot flows", "https://help.genesys.cloud/articles/about-genesys-dialog-engine-bot-flows/"],
  copilot: ["Agent Copilot", "https://help.genesys.cloud/articles/agent-copilot-overview/"],
  oauth: ["Create an OAuth client", "https://help.genesys.cloud/articles/create-an-oauth-client/"],
  cc: ["Client credentials", "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials"],
  sf: ["Genesys Cloud for Salesforce", "https://help.genesys.cloud/articles/about-genesys-cloud-for-salesforce/"],
  zd: ["Genesys Cloud for Zendesk", "https://help.genesys.cloud/articles/about-genesys-cloud-for-zendesk/"],
  appf: ["AppFoundry", "https://appfoundry.genesys.com/"],
  pe: ["About Predictive Engagement", "https://help.genesys.cloud/articles/about-predictive-engagement/"],
  pemap: ["Action maps overview", "https://help.genesys.cloud/articles/action-maps-overview-2/"],
  pedep: ["Deprecation: Journey Outcomes", "https://help.genesys.cloud/announcements/genesys-cloud/deprecation-journey-outcomes/"],
  div: ["Divisions overview", "https://help.genesys.cloud/articles/divisions-overview/"],
  overview: ["Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/"],
  dcvp: ["Dynamic Cloud Voice", "https://help.genesys.cloud/articles/dynamic-cloud-voice-platform-overview/"],
  certs: ["Genesys Cloud exams", "https://education.genesys.com/certification/cloud"]
};

const FLOW_IDS = new Set([
  "sip-ladder", "sip-rtp", "srtp-lock", "dtmf", "voice-path", "digital-path",
  "byoc-cloud", "byoc-prem", "edge-fail", "inqueue", "data-action", "bullseye",
  "preferred", "acd-gate", "emergency", "wfm-loop", "sta-pipe", "bot-escape",
  "pe-journey", "pe-qualify", "cutover", "migration", "firewall", "recording",
  "trouble-tree", "deploy-tree",
  "tls-path", "satellite-media", "queue-media", "schedule-gen",
  "screen-pop", "pkce-grant", "topic-pipe", "action-priority"
]);

function row(id, title, caption, citeKey, kind, data) {
  const cite = C[citeKey];
  return { id, title, caption, cite: cite[0], url: cite[1], kind, data, flow: FLOW_IDS.has(id) };
}

export const DIAGRAMS = [
  row("core-region", "Core region and satellite media", "The organization is created in one core region. Satellites carry media.", "regions", "orbit", { center: "Core org", satellites: ["Media A", "Media B", "Media C"] }),
  row("sip-ladder", "A basic SIP call", "INVITE through BYE for a call that is answered. Real traces also use 183 and PRACK. This is the simple success path.", "sip", "ladder", { left: "Caller", right: "Cloud", msgs: [["L", "INVITE"], ["R", "100 Trying"], ["R", "180 Ringing"], ["R", "200 OK"], ["L", "ACK"], ["R", "RTP"], ["L", "BYE"], ["R", "200 OK"]] }),
  row("sip-rtp", "Signaling is not audio", "SIP sets the call up. RTP moves the sound. The public SIP article says media addresses in SDP differ from signaling addresses.", "rtp", "split", { left: "SIP signaling", right: "RTP media", leftItems: ["UDP/TCP 5060", "TLS 5061"], rightItems: ["UDP 16384-65535", "SRTP when secured"] }),
  row("srtp-lock", "Secure BYOC Cloud", "TLS 1.2 on 5061 for signaling. SRTP for audio. IPsec is not the secure-trunk method.", "tls", "chain", ["Carrier", "TLS 5061", "SRTP", "Media tier"]),
  row("dtmf", "Digits are a named event", "RFC 4733 carries DTMF as telephone events. A secure flow is still an Architect choice about recording.", "dtmf", "chain", ["Caller", "RFC 4733", "Secure flow", "No recording"]),
  row("voice-path", "Voice path across the floor", "Carrier or Genesys Cloud Voice, then Architect, queue, and an On Queue agent.", "byoc", "chain", ["Carrier", "Trunk", "Architect", "Queue", "Agent"]),
  row("digital-path", "Digital skips the trunk", "Message, email, and chat still need a published flow and a queue.", "arch", "chain", ["Channel", "Architect", "Queue", "Agent"]),
  row("byoc-cloud", "BYOC Cloud", "Your carrier contract. Genesys media in AWS. No customer Edge on that path.", "byoc", "chain", ["Your carrier", "Public SIP", "AWS media", "Architect"]),
  row("byoc-dcvp", "Dynamic Cloud Voice", "New BYOC Cloud trunks start on this platform. Copy allowlists from the current article.", "dcvp", "chain", ["Old trunk", "DCVP", "New ACL", "Test call"]),
  row("byoc-prem", "BYOC Premises", "An Edge on your network terminates local phones and trunks.", "edge", "chain", ["Phone", "Edge", "Site", "Cloud"]),
  row("edge-fail", "Local Edge first", "Another site is the exception, when the local Edge is offline, full, or missing the resource.", "edge", "split", { left: "Same site", right: "Other site", leftItems: ["Preferred", "Has the trunk"], rightItems: ["Failover", "Only if it has the resource"] }),
  row("architect-types", "Pick the flow type first", "Inbound, in-queue, bot, secure, and common module are different Architect types.", "flow", "stack", ["Inbound call", "In-queue", "Bot flow", "Secure flow", "Common module"]),
  row("publish", "Drafts do not answer", "The runtime uses the published version.", "flow", "chain", ["Edit", "Save draft", "Publish", "Runtime"]),
  row("inqueue", "Hold is its own flow", "The caller is already queued. The in-queue flow is what they hear.", "inq", "chain", ["Queued", "In-queue flow", "Music or message", "Agent answer"]),
  row("data-action", "A data action leaves the flow", "It calls another system. Participant data can carry a value to the agent.", "arch", "chain", ["Flow", "Data action", "Outside system", "Participant data"]),
  row("routing-methods", "Five routing methods", "Standard, predictive, bullseye, preferred agent, and conditional group routing.", "route", "stack", ["Standard", "Predictive", "Bullseye", "Preferred", "Conditional"]),
  row("bullseye", "Rings widen the target", "Up to five rings. A delay can run from 2 seconds to 72 hours. Up to 50 skills can be removed.", "bull", "rings", ["All skills", "Drop one", "Wider", "Widest"]),
  row("preferred", "Preferred agents go first", "They can be offered without the skill if they belong to the queue and are On Queue.", "pref", "chain", ["Preferred", "On Queue", "Member", "Then everyone else"]),
  row("evaluation", "How “has the skills” is decided", "All skills matching, best available skills, or disregard skills.", "evalm", "stack", ["All skills", "Best available", "Disregard"]),
  row("conversation-score", "One priority point is one minute", "Conversation score subtracts priority times 60,000 ms from arrival time.", "queue", "chain", ["Arrived", "Priority × 60s", "Score", "Offer order"]),
  row("utilization", "A full agent is skipped", "Utilization caps how many interactions of each media an agent may hold.", "util", "split", { left: "Under the cap", right: "At the cap", leftItems: ["Eligible"], rightItems: ["Skipped"] }),
  row("acd-gate", "Three gates before a ring", "On Queue, under utilization, and a skill result the evaluation method accepts.", "evalm", "chain", ["On Queue", "Utilization", "Skills", "Alert"]),
  row("emergency", "BYOC emergency is yours", "Genesys is not the emergency provider on a BYOC trunk. Classify, route, and test.", "emerg", "chain", ["Dial 911", "Emergency class", "Your route", "Your provider"]),
  row("number-plan", "Plans classify what was dialed", "A site can hold 200 plans. Emergency, extension, and 988 exist as defaults.", "numbers", "stack", ["Emergency", "Extension", "National", "E.164"]),
  row("packages", "CX 1 through CX 4", "Voice, then digital and quality, then WEM, then Copilot. Read the overview before you buy the wrong row.", "overview", "stack", ["CX 1 voice", "CX 2 digital + QM", "CX 3 WEM", "CX 4 Copilot"]),
  row("divisions", "Objects sit in one division", "Home cannot be deleted. A role opens objects only where it is paired with a division.", "div", "split", { left: "Home", right: "Your division", leftItems: ["Cannot delete"], rightItems: ["Queues, users, flows"] }),
  row("wfm-views", "Two forecast clocks", "Short-term can build a schedule. Long-term is seasonality and cannot.", "forecasts", "split", { left: "Short-term", right: "Long-term", leftItems: ["Up to 6 weeks", "Generates schedules"], rightItems: ["Up to 2 years", "No schedule"] }),
  row("wfm-loop", "Plan, staff, compare", "Forecast, schedule, adherence, intraday. The overview lists that loop.", "wfm", "chain", ["Forecast", "Schedule", "Adherence", "Intraday"]),
  row("qm-loop", "Quality is a loop", "Policy, form, score, coach. AI scoring also needs STA and tokens.", "qm", "chain", ["Record", "Form", "Score", "Coach"]),
  row("recording", "A policy chooses the call and the retention", "A secure flow can suppress a segment. It does not replace the policy.", "rec", "chain", ["Policy", "ACD call", "Keep or drop", "Export"]),
  row("sta-pipe", "Analytics reads after the channel has the conversation", "Transcript, sentiment, topics. It is not a second ACD.", "sta", "chain", ["Interaction", "Transcript", "Topics", "Search"]),
  row("bot-escape", "Every bot needs a queue", "No-match, timeout, and error are normal exits.", "bot", "chain", ["Inbound", "Bot", "No match", "Queue"]),
  row("copilot", "Copilot talks to the agent", "The bot talks to the customer. Copilot is the other product.", "copilot", "split", { left: "Bot", right: "Copilot", leftItems: ["Customer"], rightItems: ["Agent"] }),
  row("oauth", "Match the grant to who the call runs as", "Client credentials, authorization code with PKCE, or SAML2 bearer. Implicit is the one leaving.", "oauth", "stack", ["Client credentials", "Auth code + PKCE", "SAML2 bearer", "Implicit (leaving)"]),
  row("users-me", "Client credentials have no user", "The token cannot call /api/v2/users/me.", "cc", "chain", ["Client", "Token", "API", "Not users/me"]),
  row("salesforce", "The embed is not the data action", "Screen pop can fail while the queue is healthy. Data actions have their own OAuth migration.", "sf", "chain", ["Call", "Embed", "Screen pop", "Log"]),
  row("zendesk", "Zendesk has its own page", "Do not paste the Salesforce field list onto it.", "zd", "split", { left: "Salesforce", right: "Zendesk", leftItems: ["Own about page"], rightItems: ["Own about page"] }),
  row("appfoundry", "A listing is not an install", "The app exists in the org only after someone installs it.", "appf", "chain", ["Marketplace", "Install", "Configure", "Agent sees it"]),
  row("pe-journey", "Predictive Engagement", "The site, then a segment, then an action map, then an offer.", "pe", "chain", ["Website", "Segment", "Action map", "Offer"]),
  row("pe-qualify", "Qualified is not shown", "Priority picks among qualified maps. A schedule group can hide the offer.", "pemap", "chain", ["Trigger", "Qualified", "Priority", "Offer"]),
  row("pe-sunset", "Journey Outcomes end", "Announced 2026-05-18. Planned effective date 2026-06-29. Segment triggers can remain.", "pedep", "split", { left: "Leaving", right: "Stays", leftItems: ["Outcome scores", "Outcome triggers"], rightItems: ["Segments", "Activity triggers"] }),
  row("cutover", "One number, then the queue, then the people", "A weekend big-bang is how an untested emergency route meets a full staff.", "emerg", "chain", ["One DID", "Queue", "People", "Next number"]),
  row("migration", "Rebuild, do not hope for a converter", "Engage, PureConnect, and UCCE become flows, queues, and trunks you draw again.", "arch", "chain", ["Old behavior", "Read it", "New flow", "Published"]),
  row("certs-path", "Two named codes, then specialist names", "GC-GCP and GC-GCD are catalog codes. Specialist rows are names.", "certs", "stack", ["GC-GCP", "GC-GCD", "Architect", "WFM", "QM"]),
  row("firewall", "Open signaling and outbound media", "TCP 5061 for TLS trunks. UDP 16384-65535 outbound for RTP. Read the firewall set before you add a port from memory.", "fw", "split", { left: "Signaling", right: "Media", leftItems: ["TCP 5061 TLS", "TCP/UDP 5060"], rightItems: ["UDP 16384-65535", "Outbound"] }),
  row("trouble-tree", "Troubleshooting tree", "Start with the symptom. A healthy Architect run with no audio is media. An empty Live Now view is tracking.", "fw", "tree", { root: "Symptom", left: "No audio", right: "No offer", leftKids: ["Flow ran?", "RTP outbound"], rightKids: ["Live Now", "Schedule group"] }),
  row("deploy-tree", "Deployment order", "Region and roles, then the trunk or Edge, then a published flow and a queue. Emergency has an owner before the DID.", "byoc", "tree", { root: "First week", left: "Telephony", right: "Experience", leftKids: ["Location", "Trunk"], rightKids: ["Publish", "Queue"] }),
  row("tls-path", "TLS trunk path", "Secure BYOC Cloud signaling uses TLS 1.2 on 5061. IPsec is not the secure-trunk method.", "tls", "chain", ["Carrier", "TCP 5061", "TLS 1.2", "Media tier"]),
  row("satellite-media", "Satellite media path", "The organization is created in one core region. A satellite region carries media. It does not host the org.", "regions", "chain", ["Core org", "Satellite", "Media", "Agent"]),
  row("queue-media", "Queue medias", "Voice, chat, email, and message are tracked separately. A flow type has to match the media.", "arch", "stack", ["Voice", "Chat", "Email", "Message"]),
  row("schedule-gen", "Short-term forecast to a schedule", "Short-term can generate a schedule. Long-term is seasonality and cannot.", "forecasts", "chain", ["Short-term", "Forecast", "Schedule", "Agents"]),
  row("screen-pop", "Salesforce screen pop", "The embed can fail while the queue is healthy. The about page is the source, not this sketch.", "sf", "chain", ["Call", "Embed", "Screen pop", "Log"]),
  row("pkce-grant", "Authorization code with PKCE", "A user-context grant is a different token from client credentials. Client credentials cannot call users/me.", "oauth", "chain", ["User", "PKCE", "Token", "API"]),
  row("topic-pipe", "Topics after the transcript", "Speech and text analytics reads the conversation. It is not a second ACD.", "sta", "chain", ["Interaction", "Transcript", "Topics", "Search"]),
  row("action-priority", "Action map priority", "Qualified is not the same as shown. Priority picks among qualified maps.", "pemap", "chain", ["Trigger", "Qualified", "Priority", "Offer"]),
  row("home-lock", "Home division stays", "Home cannot be deleted. A role opens objects only where it is paired with a division.", "div", "stack", ["Home", "Cannot delete", "Pair a role", "Objects"]),
  row("extension-plan", "Default number plans", "Emergency, extension, and 988 exist as defaults. A site can hold 200 plans. Confirm the live list.", "numbers", "stack", ["Emergency", "Extension", "988", "E.164"]),
  row("site-edge", "Site and Edge", "BYOC Premises puts an Edge on your network. Another site is the exception.", "edge", "chain", ["Site", "Edge", "Phones", "Cloud"]),
  row("transport-choice", "Trunk transport", "UDP or TCP 5060, or TLS on 5061. Match the far end. Do not invent a port from memory.", "transport", "stack", ["UDP 5060", "TCP 5060", "TLS 5061", "Match the far end"]),
  row("secure-suppress", "Secure flow and recording", "A secure flow can suppress a segment. It does not replace the recording policy.", "rec", "chain", ["Policy", "Secure flow", "Suppress", "Keep the rest"]),
  row("common-module", "Common module", "A common module is its own Architect type. It is not a published inbound flow.", "flow", "stack", ["Inbound", "In-queue", "Bot", "Common module"]),
  row("implicit-grant", "Implicit grant is leaving", "The OAuth article names the grants. Implicit is the one leaving. Confirm before relying on a client you already built.", "oauth", "split", { left: "Use", right: "Leaving", leftItems: ["Client credentials", "Auth code + PKCE"], rightItems: ["Implicit"] }),
  row("zendesk-embed", "Zendesk embed", "Zendesk has its own about page. Do not paste the Salesforce field list onto it.", "zd", "chain", ["Call", "Zendesk embed", "Ticket", "Log"])
];

export const PORTS = [
  { name: "BYOC trunk TLS", proto: "TCP", port: "5061", dir: "Both ends use TLS", note: "Common firewall port. TLS listeners are on 5061. TLS 1.2.", url: C.tls[1], source: C.tls[0] },
  { name: "BYOC trunk UDP or TCP", proto: "UDP or TCP", port: "5060", dir: "Match the far end", note: "Common firewall port when the trunk transport is UDP or TCP.", url: C.transport[1], source: C.transport[0] },
  { name: "Managed phone signaling", proto: "TCP", port: "8061", dir: "Phone to media tier", note: "SIPS for managed phones under BYOC Cloud.", url: C.phones[1], source: C.phones[0] },
  { name: "Unmanaged phone signaling", proto: "TCP", port: "5061", dir: "Phone to media tier", note: "SIPS for unmanaged phones under BYOC Cloud.", url: C.phones[1], source: C.phones[0] },
  { name: "Phone media", proto: "UDP", port: "16384-65535", dir: "Outbound", note: "RTP or SRTP to the media tier. The FAQ says the range is for outbound connections.", url: C.rtpFaq[1], source: C.rtpFaq[0] },
  { name: "Phone provisioning", proto: "TCP", port: "443", dir: "Outbound", note: "The VoIP phone article also lists TCP 80 and TCP 443 for configuration provisioning.", url: C.phones[1], source: C.phones[0] },
  { name: "Secure trunk VPN", proto: "IPsec", port: "—", dir: "Not used", note: "BYOC Cloud secure trunks do not use IPsec. Use SIP TLS and SRTP.", url: C.tls[1], source: C.tls[0] },
  { name: "SIP versus media addresses", proto: "SDP", port: "—", dir: "Different hosts", note: "Signaling addresses and the media addresses in SDP are different services. Copy them from the current regional article.", url: C.sipIp[1], source: C.sipIp[0] }
];

const INK = "#1a0c08";

function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));
}

function blurb(caption) {
  const sentence = String(caption || "").split(". ")[0];
  return sentence.length > 86 ? sentence.slice(0, 83) + "…" : sentence;
}

function frame(spec, inner) {
  const id = spec.id;
  const label = spec.title;
  return `<svg class="diagram" data-diagram="${esc(id)}" viewBox="0 0 720 372" role="img" aria-label="${esc(label)}">
    <defs>
      <linearGradient id="g-${esc(id)}" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#3e8fd4" />
        <stop offset="0.48" stop-color="#4d63c9" />
        <stop offset="1" stop-color="#8a4cae" />
      </linearGradient>
    </defs>
    <rect width="720" height="372" rx="22" fill="#f3f7ff" />
    <rect width="720" height="372" rx="22" fill="url(#g-${esc(id)})" opacity="0.92" />
    <circle cx="78" cy="36" r="88" fill="#b9f3ff" opacity="0.28" />
    <circle cx="650" cy="210" r="120" fill="#ffd0ef" opacity="0.22" />
    <g fill="none" stroke="rgba(255,255,255,.28)" stroke-width="1">
      <path d="M0 46 H720 M0 276 H720" />
    </g>
    ${inner}
    <g class="callout">
      <rect x="16" y="286" width="688" height="70" rx="14" fill="rgba(255,255,255,0.96)" />
      <text x="30" y="314" font-size="16" font-weight="700" font-family="ui-sans-serif, Segoe UI, sans-serif" fill="#102033">${esc(label)}</text>
      <text x="30" y="338" font-size="13" font-family="ui-sans-serif, Segoe UI, sans-serif" fill="#1c3d5a">${esc(blurb(spec.caption))}</text>
    </g>
  </svg>`;
}

function packet(path, dur = "4.2s") {
  return `<g class="packet">
    <circle r="16" fill="#2ff7ff" opacity="0.35"><animateMotion dur="${dur}" repeatCount="indefinite" path="${path}" /></circle>
    <circle r="8" fill="#ffffff"><animateMotion dur="${dur}" repeatCount="indefinite" path="${path}" /></circle>
    <circle r="8" fill="#ff2fb3" opacity="0.9"><animateMotion dur="${dur}" begin="1.3s" repeatCount="indefinite" path="${path}" /></circle>
  </g>`;
}

function chip(x, y, text, fill) {
  const w = Math.max(96, text.length * 8 + 28);
  return `<g class="chip-pop">
    <rect x="${x - w / 2}" y="${y - 20}" width="${w}" height="40" rx="14" fill="${fill}" />
    <text x="${x}" y="${y + 5}" text-anchor="middle" font-size="14" font-family="ui-sans-serif, Segoe UI, sans-serif" fill="${INK}">${esc(text)}</text>
  </g>`;
}

function chain(spec) {
  const labels = spec.data;
  const n = labels.length;
  const gap = 620 / n;
  let d = "";
  labels.forEach((label, i) => {
    const x = 50 + gap * i + gap / 2;
    d += chip(x, 140, label, i % 2 ? "#d6f25c" : "#8fd4ff");
    if (i < n - 1) d += `<line x1="${x + 54}" y1="140" x2="${x + gap - 54}" y2="140" stroke="#fff" stroke-width="3" stroke-dasharray="7 7" class="dash" />`;
  });
  const start = 50 + gap / 2;
  const end = 50 + gap * (n - 1) + gap / 2;
  d += packet(`M${start},108 H${end}`);
  return frame(spec, d);
}

function stack(spec) {
  const labels = spec.data;
  let d = "";
  labels.forEach((label, i) => {
    const y = 58 + i * 40;
    d += `<rect x="180" y="${y}" width="360" height="32" rx="10" fill="${i === labels.length - 1 ? "#ff5a36" : "#d6f25c"}" opacity="${0.55 + i * 0.1}" />
      <text x="360" y="${y + 21}" text-anchor="middle" font-size="14" font-family="ui-sans-serif, Segoe UI, sans-serif" fill="${INK}">${esc(label)}</text>`;
  });
  d += packet("M120,70 V230", "3.4s");
  return frame(spec, d);
}

function rings(spec) {
  const labels = spec.data;
  let d = "";
  labels.forEach((label, i) => {
    const r = 108 - i * 22;
    d += `<circle cx="250" cy="145" r="${r}" fill="none" stroke="#fff" stroke-width="3" opacity="${0.35 + i * 0.15}" class="ring" />
      <text x="400" y="${70 + i * 42}" font-size="15" fill="#fff" font-family="ui-sans-serif, Segoe UI, sans-serif">${esc(label)}</text>`;
  });
  d += `<circle cx="250" cy="145" r="8" fill="#ff5a36" class="pulse-dot" />`;
  return frame(spec, d);
}

function split(spec) {
  const { left, right, leftItems, rightItems } = spec.data;
  const col = (x, title, items, fill) => {
    let out = `<rect x="${x}" y="48" width="280" height="190" rx="18" fill="rgba(0,0,0,.25)" stroke="${fill}" />
      <text x="${x + 140}" y="78" text-anchor="middle" fill="${fill}" font-size="16" font-family="ui-sans-serif, Segoe UI, sans-serif">${esc(title)}</text>`;
    items.forEach((item, i) => {
      out += `<text x="${x + 24}" y="${112 + i * 32}" fill="#fff" font-size="14" font-family="ui-sans-serif, Segoe UI, sans-serif">${esc(item)}</text>`;
    });
    return out;
  };
  return frame(spec, col(40, left, leftItems, "#8fd4ff") + col(400, right, rightItems, "#ff7ad9") + packet("M320,140 H400", "2.8s"));
}

function ladder(spec) {
  const { left, right, msgs } = spec.data;
  let d = `<text x="140" y="42" text-anchor="middle" fill="#8fd4ff" font-size="14" font-family="ui-sans-serif, Segoe UI, sans-serif">${esc(left)}</text>
    <text x="560" y="42" text-anchor="middle" fill="#d6f25c" font-size="14" font-family="ui-sans-serif, Segoe UI, sans-serif">${esc(right)}</text>
    <line x1="140" y1="52" x2="140" y2="250" stroke="rgba(255,255,255,.35)" />
    <line x1="560" y1="52" x2="560" y2="250" stroke="rgba(255,255,255,.35)" />`;
  msgs.forEach((msg, i) => {
    const y = 70 + i * 24;
    const fromLeft = msg[0] === "L";
    const x1 = fromLeft ? 140 : 560;
    const x2 = fromLeft ? 560 : 140;
    d += `<line x1="${x1}" y1="${y}" x2="${x2}" y2="${y}" stroke="${msg[1] === "RTP" ? "#ff5a36" : "#fff"}" stroke-width="2" />
      <polygon points="${x2},${y} ${x2 + (fromLeft ? -8 : 8)},${y - 4} ${x2 + (fromLeft ? -8 : 8)},${y + 4}" fill="#fff" />
      <text x="350" y="${y - 4}" text-anchor="middle" fill="#fff" font-size="12" font-family="ui-monospace, monospace">${esc(msg[1])}</text>`;
  });
  return frame(spec, d);
}

function orbit(spec) {
  const { center, satellites } = spec.data;
  let d = `<g class="spin">
    <circle cx="360" cy="150" r="92" fill="none" stroke="rgba(255,255,255,.4)" stroke-dasharray="4 8" />
    ${satellites.map((label, i) => {
      const a = (Math.PI * 2 * i) / satellites.length - Math.PI / 2;
      const x = 360 + Math.cos(a) * 92;
      const y = 150 + Math.sin(a) * 92;
      return chip(x, y, label, "#b3a6ff");
    }).join("")}
  </g>`;
  d += chip(360, 150, center, "#ff5a36");
  return frame(spec, d);
}

function tree(spec) {
  const { root, left, right, leftKids, rightKids } = spec.data;
  const kid = (x, labels) => labels.map((label, i) => chip(x, 168 + i * 48, label, i ? "#8fd4ff" : "#d6f25c")).join("");
  const inner = chip(360, 48, root, "#ff5a36")
    + chip(180, 112, left, "#b3a6ff")
    + chip(540, 112, right, "#ff7ad9")
    + kid(180, leftKids)
    + kid(540, rightKids)
    + `<path d="M360 68 V90 H180 V92 M360 90 H540 V92 M180 132 V148 M540 132 V148" fill="none" stroke="#fff" stroke-width="2" class="dash" stroke-dasharray="6 6"/>`
    + packet("M360,70 V100 H180 V150", "5s");
  return frame(spec, inner);
}

const DRAW = { chain, stack, rings, split, ladder, orbit, tree };

export function renderDiagram(spec) {
  const draw = DRAW[spec.kind];
  if (!draw) return "";
  return draw(spec);
}

export function diagramById(id) {
  return DIAGRAMS.find((item) => item.id === id) || null;
}
