/* Landing-page guide. It reads the words already on this page. No cloud call. */
(function () {
  "use strict";

  var speaking = false;
  var queue = [];
  var index = 0;

  function monkeySvg() {
    return '<svg viewBox="0 0 200 230" aria-hidden="true">' +
      "<defs><radialGradient id='home-fur' cx='38%' cy='28%'><stop offset='0' stop-color='#fde68a'/><stop offset='1' stop-color='#f59e0b'/></radialGradient></defs>" +
      '<circle cx="100" cy="108" r="78" fill="none" stroke="#fbbf24" stroke-width="5"/>' +
      '<ellipse class="ear" cx="36" cy="86" rx="22" ry="28" fill="#f59e0b" stroke="#9a3412" stroke-width="3"/>' +
      '<ellipse class="ear" cx="164" cy="86" rx="22" ry="28" fill="#f59e0b" stroke="#9a3412" stroke-width="3"/>' +
      '<ellipse cx="100" cy="188" rx="48" ry="30" fill="#7c3aed" stroke="#4c1d95" stroke-width="3"/>' +
      '<g class="arm-r"><path d="M148 168c28 6 40 28 28 40-16 10-40-2-42-20z" fill="#f59e0b" stroke="#9a3412" stroke-width="3"/></g>' +
      '<circle cx="100" cy="102" r="58" fill="url(#home-fur)" stroke="#b45309" stroke-width="3"/>' +
      '<ellipse cx="100" cy="118" rx="36" ry="30" fill="#fff7ed"/>' +
      '<ellipse cx="78" cy="104" rx="14" ry="16" fill="#fff" stroke="#1e1b4b" stroke-width="3"/>' +
      '<ellipse cx="122" cy="104" rx="14" ry="16" fill="#fff" stroke="#1e1b4b" stroke-width="3"/>' +
      '<circle cx="80" cy="108" r="6" fill="#1e1b4b"/>' +
      '<circle cx="124" cy="108" r="6" fill="#1e1b4b"/>' +
      '<path d="M78 136c12 12 32 12 44 0" fill="none" stroke="#9a3412" stroke-width="4" stroke-linecap="round"/>' +
      "</svg>";
  }

  var dock = document.createElement("div");
  dock.className = "bot-dock";
  dock.innerHTML =
    '<section class="readalong-panel" id="readalongPanel" hidden aria-label="Read along">' +
    "<p>I read the words already on this page. I do not invent a fact.</p>" +
    '<div class="readalong-actions">' +
    '<button type="button" data-read>Read along</button>' +
    '<button type="button" data-stop>Stop</button>' +
    "</div>" +
    '<label>Rate <input data-rate type="range" min="0.8" max="1.2" step="0.05" value="1" aria-label="Speaking rate"></label>' +
    "</section>" +
    '<button type="button" class="monkey-btn" data-pose="wave" aria-expanded="false" aria-controls="readalongPanel" aria-label="Genesys guide. Read this page aloud.">' +
    monkeySvg() +
    "</button>";
  document.body.appendChild(dock);

  var monkey = dock.querySelector(".monkey-btn");
  var panel = dock.querySelector(".readalong-panel");
  var rate = dock.querySelector("[data-rate]");

  function pose(name) { monkey.setAttribute("data-pose", name); }

  function setOpen(open) {
    panel.hidden = !open;
    dock.classList.toggle("is-open", open);
    monkey.setAttribute("aria-expanded", open ? "true" : "false");
    pose(open ? "wave" : "idle");
    park();
  }

  monkey.addEventListener("click", function () { setOpen(panel.hidden); });

  function clearMarks() {
    document.querySelectorAll(".is-spoken").forEach(function (el) { el.classList.remove("is-spoken"); });
  }

  function sentences(text) {
    return text.split(/(?<=[.!?])\s+/).map(function (part) { return part.trim(); }).filter(function (part) { return part.length > 1; });
  }

  function collect() {
    var root = document.querySelector("main") || document.body;
    var nodes = [];
    root.querySelectorAll("h1, .lede, h2, p, li").forEach(function (el) {
      if (el.closest(".bot-dock, footer, .disclaimer-panel")) return;
      if (el.querySelector("h1, h2, p, li") && el.tagName !== "LI") return;
      var text = (el.textContent || "").replace(/\s+/g, " ").trim();
      if (text.length < 8) return;
      sentences(text).forEach(function (sentence) { nodes.push({ el: el, sentence: sentence }); });
    });
    return nodes;
  }

  function stop() {
    speaking = false;
    queue = [];
    index = 0;
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    clearMarks();
    pose(panel.hidden ? "idle" : "wave");
  }

  function speakNext() {
    if (!speaking) return;
    if (index >= queue.length) {
      stop();
      return;
    }
    var item = queue[index];
    index += 1;
    clearMarks();
    item.el.classList.add("is-spoken");
    var phone = window.matchMedia("(max-width: 700px)").matches;
    if (phone && item.el.tagName !== "H1" && overlaps(dock.getBoundingClientRect(), item.el.getBoundingClientRect())) {
      item.el.scrollIntoView({ block: "nearest", behavior: "auto" });
    }
    park();
    var dwell = Math.min(8000, 700 + item.sentence.length * 28);
    var started = Date.now();
    var finished = false;
    function finish() {
      if (finished || !speaking) return;
      finished = true;
      var wait = Math.max(0, dwell - (Date.now() - started));
      window.setTimeout(function () {
        if (speaking) speakNext();
      }, wait);
    }
    if (!window.speechSynthesis) {
      window.setTimeout(finish, 0);
      return;
    }
    var utter = new SpeechSynthesisUtterance(item.sentence);
    utter.rate = Number(rate.value) || 1;
    utter.onend = finish;
    utter.onerror = finish;
    pose("read");
    window.speechSynthesis.speak(utter);
    window.setTimeout(function () {
      if (!speaking || finished) return;
      if (window.speechSynthesis.speaking || window.speechSynthesis.pending) return;
      finish();
    }, 250);
  }

  function readAlong() {
    stop();
    queue = collect().slice(0, 24);
    index = 0;
    if (!queue.length) return;
    speaking = true;
    setOpen(true);
    speakNext();
  }

  dock.querySelector("[data-read]").addEventListener("click", readAlong);
  dock.querySelector("[data-stop]").addEventListener("click", stop);

  function overlaps(a, b) {
    return !(a.right < b.left + 1 || a.left > b.right - 1 || a.bottom < b.top + 1 || a.top > b.bottom - 1);
  }

  function guards() {
    var nodes = [];
    document.querySelectorAll("main h1, main .kicker, main .lede").forEach(function (el) { nodes.push(el); });
    var first = document.querySelector("main h1");
    if (first) {
      var sib = first.nextElementSibling;
      var count = 0;
      while (sib && count < 2) {
        if (sib.matches && sib.matches("p, .lede")) nodes.push(sib);
        sib = sib.nextElementSibling;
        count += 1;
      }
    }
    return nodes;
  }

  function park() {
    dock.style.top = "";
    dock.style.bottom = "";
    var box = dock.getBoundingClientRect();
    var covered = false;
    var floor = 0;
    guards().forEach(function (el) {
      var rect = el.getBoundingClientRect();
      if (rect.width < 8 || rect.height < 8) return;
      if (rect.top < window.innerHeight && rect.bottom > floor) floor = rect.bottom;
      if (overlaps(box, rect)) covered = true;
    });
    if (!covered) return;
    var top = Math.round(Math.min(window.innerHeight - box.height - 8, Math.max(8, floor + 12)));
    dock.style.top = top + "px";
    dock.style.bottom = "auto";
    box = dock.getBoundingClientRect();
    var still = false;
    guards().forEach(function (el) {
      var rect = el.getBoundingClientRect();
      if (rect.width < 8 || rect.height < 8) return;
      if (overlaps(box, rect)) still = true;
    });
    if (still) {
      dock.style.top = "";
      dock.style.bottom = "8px";
    }
  }

  window.addEventListener("resize", park);
  window.addEventListener("scroll", park, { passive: true });
  window.addEventListener("load", park);
  park();
})();
