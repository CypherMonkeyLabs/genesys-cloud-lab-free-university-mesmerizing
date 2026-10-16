/* Renders campus/data/sources/<room>.json at the end of the open room. */

const KIND_LABEL = {
  "resource-center": "Resource Center",
  developer: "Developer docs",
  rfc: "RFC",
  community: "Community",
  wikipedia: "Wikipedia",
  official: "Official page"
};

function kindLabel(kind) {
  switch (kind) {
    case "resource-center":
      return KIND_LABEL["resource-center"];
    case "developer":
      return KIND_LABEL.developer;
    case "rfc":
      return KIND_LABEL.rfc;
    case "community":
      return KIND_LABEL.community;
    case "wikipedia":
      return KIND_LABEL.wikipedia;
    case "official":
      return KIND_LABEL.official;
    default: {
      const unexpected = kind;
      return unexpected ? KIND_LABEL.official : KIND_LABEL.official;
    }
  }
}

function renderSources(data) {
  const section = document.createElement("section");
  section.className = "sources-deeper";
  section.id = "sec-sources-deeper";
  const heading = document.createElement("h2");
  heading.textContent = "Sources and go deeper";
  const intro = document.createElement("p");
  const checked = data.lastChecked || "";
  intro.textContent = `Each link was opened for this lab. Last checked ${checked}. A confirm flag means the lab could not verify that link.`;
  const list = document.createElement("ul");
  for (const src of data.sources || []) {
    const item = document.createElement("li");
    const kind = document.createElement("span");
    kind.className = "src-kind";
    kind.textContent = kindLabel(src.kind);
    const link = document.createElement("a");
    link.href = src.url;
    link.rel = "noopener noreferrer";
    link.textContent = src.title || src.url;
    const when = document.createElement("span");
    when.className = "src-checked";
    when.textContent = `Last checked ${src.lastChecked || checked}`;
    item.append(kind, document.createTextNode(" "), link, document.createTextNode(" "), when);
    if (src.status === "confirm") {
      const flag = document.createElement("strong");
      flag.className = "src-flag";
      flag.textContent = "confirm";
      item.append(document.createTextNode(" "), flag);
    }
    if (src.note) {
      const note = document.createElement("span");
      note.className = "src-note";
      note.textContent = src.note;
      item.append(document.createTextNode(" "), note);
    }
    list.append(item);
  }
  section.append(heading, intro, list);
  return section;
}

let ticket = 0;

export function attachSources(root) {
  if (!root) return Promise.resolve();
  const mine = String(++ticket);
  root.dataset.sourcesTicket = mine;
  const room = document.body.dataset.room || "";
  const job = (async () => {
    root.querySelectorAll(":scope > .sources-deeper").forEach((el) => el.remove());
    if (!room) return;
    let data = null;
    try {
      const response = await fetch(`data/sources/${encodeURIComponent(room)}.json`);
      if (!response.ok) return;
      data = await response.json();
    } catch (err) {
      return;
    }
    if (!root.isConnected || root.dataset.sourcesTicket !== mine || document.body.dataset.room !== room) return;
    if (!data || !Array.isArray(data.sources) || !data.sources.length) return;
    root.appendChild(renderSources(data));
  })();
  window.gccxSourcesReady = job;
  return job;
}
