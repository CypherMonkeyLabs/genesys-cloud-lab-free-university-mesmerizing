const POSES = ["listen", "point", "think", "cheer"];

export function mountMascot(el) {
  if (!el || el.dataset.ready === "1") return;
  el.dataset.ready = "1";
  el.innerHTML = markup();
  const svg = el.querySelector("svg");
  let pose = 0;
  const reduce = document.documentElement.dataset.reduce === "1" || window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const apply = () => {
    svg.dataset.pose = POSES[pose];
    const label = el.querySelector("[data-pose-label]");
    if (label) label.textContent = POSES[pose];
  };
  apply();
  if (reduce) return;
  window.setInterval(() => {
    pose = (pose + 1) % POSES.length;
    apply();
  }, 7000);
}

function markup() {
  return `<figure class="mascot">
    <svg viewBox="0 0 220 240" role="img" aria-label="CypherMonkey, the lab mascot, in a headset.">
      <ellipse cx="110" cy="214" rx="54" ry="10" fill="rgba(0,0,0,.28)" />
      <path class="tail" d="M150 150 C190 150 196 90 160 78" fill="none" stroke="#c47a3a" stroke-width="10" stroke-linecap="round" />
      <ellipse cx="110" cy="156" rx="48" ry="40" fill="#e8a15a" />
      <circle cx="110" cy="92" r="48" fill="#f0b56a" />
      <circle cx="74" cy="78" r="16" fill="#e8a15a" />
      <circle cx="146" cy="78" r="16" fill="#e8a15a" />
      <circle cx="74" cy="78" r="8" fill="#f6d7b0" />
      <circle cx="146" cy="78" r="8" fill="#f6d7b0" />
      <ellipse cx="110" cy="108" rx="22" ry="16" fill="#f6d7b0" />
      <path d="M96 78 h28" stroke="#243044" stroke-width="4" fill="none" />
      <path d="M86 70 q-18 -28 -6 -8" stroke="#243044" stroke-width="4" fill="none" />
      <path d="M134 70 q18 -28 6 -8" stroke="#243044" stroke-width="4" fill="none" />
      <circle class="eye left" cx="94" cy="90" r="5" fill="#1a120c" />
      <circle class="eye right" cx="126" cy="90" r="5" fill="#1a120c" />
      <path class="mouth" d="M98 112 Q110 124 122 112" fill="none" stroke="#1a120c" stroke-width="3" stroke-linecap="round" />
      <path class="arm left" d="M68 150 Q40 170 48 196" fill="none" stroke="#e8a15a" stroke-width="12" stroke-linecap="round" />
      <path class="arm right" d="M152 150 Q186 168 176 120" fill="none" stroke="#e8a15a" stroke-width="12" stroke-linecap="round" />
      <circle class="hand" cx="176" cy="116" r="8" fill="#f0b56a" />
      <text x="110" y="168" text-anchor="middle" font-size="11" font-family="ui-sans-serif, Segoe UI, sans-serif" fill="#3a2412">CX</text>
    </svg>
    <figcaption>CypherMonkey · <span data-pose-label>listen</span></figcaption>
  </figure>`;
}
