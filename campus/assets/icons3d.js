/** Large isometric icons. Gradients and shadows, one silhouette per track. */

const HUES = ["#ff2fb3", "#2ff7ff", "#d6ff3c", "#b388ff", "#ff8a3d", "#7dffa8", "#ff5a7a", "#8fd4ff"];

const TRACKS = {
  foundations: "prism",
  org: "tower",
  architect: "flow",
  acd: "rings",
  queues: "stack",
  byoc: "globe",
  edge: "server",
  emergency: "beacon",
  wfm: "clock",
  qm: "shield",
  sta: "wave",
  ai: "neural",
  api: "cube",
  crm: "link",
  migration: "bridge",
  ecosystem: "constellation",
  predictive: "radar"
};

export function iconForTrack(id) {
  return TRACKS[id] || "prism";
}

export function isoIcon(kind, index = 0) {
  const hue = HUES[index % HUES.length];
  const hue2 = HUES[(index + 3) % HUES.length];
  const uid = `i${kind}${index}`.replace(/[^a-z0-9]/gi, "");
  const draw = SHAPES[kind] || SHAPES.prism;
  return wrap(uid, hue, hue2, draw(uid, hue, hue2));
}

function wrap(uid, hue, hue2, body) {
  return `<svg class="iso" viewBox="0 0 160 150" aria-hidden="true">
    <defs>
      <linearGradient id="${uid}t" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/>
        <stop offset="0.4" stop-color="${hue}"/>
        <stop offset="1" stop-color="${hue2}"/>
      </linearGradient>
      <linearGradient id="${uid}s" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="${hue2}"/>
        <stop offset="1" stop-color="#140814"/>
      </linearGradient>
      <filter id="${uid}g" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="2.4" result="b"/>
        <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <ellipse cx="80" cy="138" rx="52" ry="8" fill="rgba(0,0,0,.42)"/>
    <g filter="url(#${uid}g)">${body}</g>
  </svg>`;
}

function face(uid, hue, hue2, top, left, right) {
  return `<polygon points="${top}" fill="url(#${uid}t)"/>
    <polygon points="${left}" fill="url(#${uid}s)" opacity="0.95"/>
    <polygon points="${right}" fill="${hue2}"/>`;
}

const SHAPES = {
  prism(uid, hue, hue2) {
    return face(uid, hue, hue2, "80,18 118,40 80,62 42,40", "42,40 80,62 80,118 42,96", "118,40 80,62 80,118 118,96")
      + `<polygon points="80,28 104,42 80,56 56,42" fill="#fff" opacity="0.35"/>`;
  },
  tower(uid, hue, hue2) {
    return face(uid, hue, hue2, "80,8 108,24 80,40 52,24", "52,24 80,40 80,78 52,62", "108,24 80,40 80,78 108,62")
      + face(uid, hue, hue2, "80,70 116,90 80,110 44,90", "44,90 80,110 80,132 44,112", "116,90 80,110 80,132 116,112");
  },
  flow(uid, hue, hue2) {
    return `<polygon points="28,78 52,64 76,78 52,92" fill="url(#${uid}t)"/>
      <polygon points="84,48 112,32 140,48 112,64" fill="${hue2}"/>
      <polygon points="70,108 98,92 126,108 98,124" fill="${hue}"/>
      <path d="M76 78 H90 M112 64 L98 92" fill="none" stroke="#fff" stroke-width="3"/>
      <circle cx="52" cy="78" r="5" fill="#fff"/>
      <circle cx="112" cy="48" r="5" fill="#fff"/>
      <circle cx="98" cy="108" r="5" fill="#fff"/>`;
  },
  rings(uid, hue, hue2) {
    return `<ellipse cx="80" cy="88" rx="46" ry="16" fill="none" stroke="${hue}" stroke-width="8"/>
      <ellipse cx="80" cy="74" rx="34" ry="12" fill="none" stroke="${hue2}" stroke-width="7"/>
      <ellipse cx="80" cy="60" rx="22" ry="8" fill="none" stroke="#fff" stroke-width="6"/>
      <ellipse cx="80" cy="118" rx="40" ry="8" fill="${hue}" opacity="0.35"/>`;
  },
  stack(uid, hue, hue2) {
    return [0, 1, 2].map((n) => {
      const y = 28 + n * 28;
      return `<polygon points="80,${y} 122,${y + 16} 80,${y + 32} 38,${y + 16}" fill="${n === 1 ? hue2 : "url(#" + uid + "t)"}" opacity="${0.95 - n * 0.08}"/>
        <polygon points="38,${y + 16} 80,${y + 32} 80,${y + 40} 38,${y + 24}" fill="#140814" opacity="0.45"/>`;
    }).join("");
  },
  globe(uid, hue, hue2) {
    return `<circle cx="80" cy="70" r="36" fill="url(#${uid}t)"/>
      <ellipse cx="80" cy="70" rx="36" ry="14" fill="none" stroke="#fff" stroke-width="2" opacity="0.7"/>
      <path d="M80 34 V106 M48 70 H112" fill="none" stroke="${hue2}" stroke-width="2"/>
      <ellipse cx="80" cy="122" rx="28" ry="8" fill="${hue}" opacity="0.5"/>`;
  },
  server(uid, hue, hue2) {
    return face(uid, hue, hue2, "80,36 124,58 80,80 36,58", "36,58 80,80 80,118 36,96", "124,58 80,80 80,118 124,96")
      + `<path d="M48 78 H112 M48 90 H112 M48 102 H112" stroke="#fff" stroke-width="3" opacity="0.8"/>
        <circle cx="108" cy="70" r="4" fill="${hue}"/>`;
  },
  beacon(uid, hue, hue2) {
    return `<polygon points="80,22 98,78 62,78" fill="url(#${uid}t)"/>
      <polygon points="62,78 80,92 62,110 48,92" fill="url(#${uid}s)"/>
      <polygon points="98,78 112,92 98,110 80,92" fill="${hue2}"/>
      <circle cx="80" cy="22" r="8" fill="#fff"/>
      <circle cx="80" cy="22" r="16" fill="${hue}" opacity="0.35"/>`;
  },
  clock(uid, hue, hue2) {
    return `<ellipse cx="80" cy="78" rx="36" ry="36" fill="url(#${uid}t)"/>
      <circle cx="80" cy="78" r="26" fill="#120814" opacity="0.35"/>
      <path d="M80 78 L80 58 M80 78 L98 86" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
      <ellipse cx="80" cy="124" rx="30" ry="8" fill="${hue2}" opacity="0.55"/>`;
  },
  shield(uid, hue, hue2) {
    return `<path d="M80 22 L118 40 V78 C118 108 80 128 80 128 C80 128 42 108 42 78 V40 Z" fill="url(#${uid}t)"/>
      <path d="M80 40 L104 52 V76 C104 96 80 110 80 110 C80 110 56 96 56 76 V52 Z" fill="${hue2}" opacity="0.85"/>`;
  },
  wave(uid, hue, hue2) {
    return `<path d="M24 90 C44 60 60 110 80 80 C100 50 116 110 136 78" fill="none" stroke="url(#${uid}t)" stroke-width="10" stroke-linecap="round"/>
      <path d="M24 108 C48 86 64 124 88 100 C112 76 124 120 140 96" fill="none" stroke="${hue2}" stroke-width="6" stroke-linecap="round"/>
      <ellipse cx="80" cy="128" rx="40" ry="7" fill="${hue}" opacity="0.4"/>`;
  },
  neural(uid, hue, hue2) {
    return `<circle cx="48" cy="48" r="12" fill="${hue}"/>
      <circle cx="112" cy="44" r="14" fill="${hue2}"/>
      <circle cx="80" cy="86" r="16" fill="url(#${uid}t)"/>
      <circle cx="46" cy="112" r="10" fill="#fff"/>
      <circle cx="118" cy="108" r="11" fill="${hue}"/>
      <path d="M58 54 L70 76 M100 54 L90 76 M68 96 L54 108 M94 96 L110 104" stroke="#fff" stroke-width="3"/>`;
  },
  cube(uid, hue, hue2) {
    return face(uid, hue, hue2, "80,28 122,50 80,72 38,50", "38,50 80,72 80,116 38,94", "122,50 80,72 80,116 122,94");
  },
  link(uid, hue, hue2) {
    return face(uid, hue, hue2, "48,40 74,54 48,68 22,54", "22,54 48,68 48,96 22,82", "74,54 48,68 48,96 74,82")
      + face(uid, hue, hue2, "112,40 138,54 112,68 86,54", "86,54 112,68 112,96 86,82", "138,54 112,68 112,96 138,82")
      + `<path d="M74 70 H86" stroke="#fff" stroke-width="6"/>`;
  },
  bridge(uid, hue, hue2) {
    return `<path d="M24 100 Q80 20 136 100" fill="none" stroke="url(#${uid}t)" stroke-width="12" stroke-linecap="round"/>
      <path d="M36 100 V124 M80 64 V124 M124 100 V124" stroke="${hue2}" stroke-width="8" stroke-linecap="round"/>
      <path d="M20 124 H140" stroke="#fff" stroke-width="4"/>`;
  },
  constellation(uid, hue, hue2) {
    return `<path d="M36 108 L70 48 L98 86 L132 36" fill="none" stroke="${hue2}" stroke-width="2"/>
      <circle cx="36" cy="108" r="8" fill="${hue}"/>
      <circle cx="70" cy="48" r="10" fill="url(#${uid}t)"/>
      <circle cx="98" cy="86" r="7" fill="#fff"/>
      <circle cx="132" cy="36" r="9" fill="${hue2}"/>
      <circle cx="110" cy="118" r="5" fill="${hue}"/>`;
  },
  radar(uid, hue, hue2) {
    return `<path d="M80 120 L80 40 A40 40 0 0 1 120 80" fill="none" stroke="url(#${uid}t)" stroke-width="6"/>
      <path d="M80 120 A52 52 0 0 1 132 78" fill="none" stroke="${hue2}" stroke-width="4"/>
      <circle cx="80" cy="120" r="8" fill="#fff"/>
      <circle cx="116" cy="58" r="6" fill="${hue}"/>`;
  },
  chart(uid, hue, hue2) {
    return `<polygon points="36,108 52,96 52,124 36,116" fill="${hue}"/>
      <polygon points="64,78 84,64 84,124 64,112" fill="url(#${uid}t)"/>
      <polygon points="96,90 116,76 116,124 96,112" fill="${hue2}"/>
      <path d="M28 124 H136" stroke="#fff" stroke-width="3"/>`;
  },
  sheet(uid, hue, hue2) {
    return `<path d="M48 28 H96 L124 56 V128 H48 Z" fill="url(#${uid}t)"/>
      <path d="M96 28 V56 H124" fill="${hue2}"/>
      <path d="M60 74 H108 M60 90 H108 M60 106 H92" stroke="#120814" stroke-width="4"/>`;
  },
  star(uid, hue, hue2) {
    return `<polygon points="80,24 92,58 128,58 100,80 110,116 80,96 50,116 60,80 32,58 68,58" fill="url(#${uid}t)"/>
      <ellipse cx="80" cy="128" rx="28" ry="8" fill="${hue2}" opacity="0.6"/>`;
  }
};
