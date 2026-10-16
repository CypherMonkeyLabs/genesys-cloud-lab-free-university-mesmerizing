"""Large lab menu shared by standalone download pages."""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = ROOT / "campus" / "downloads"

ITEMS = [
    ("Home", "index.html#/", "Signal Floor, the start of the lab", "home"),
    ("Learn", "index.html#/tracks", "Tracks, lessons, quizzes, and labs", "learn"),
    ("Skills and ACD", "index.html#/track/skills", "How a skill request becomes an agent", "skills"),
    ("Workforce and forecasting", "index.html#/track/forecast", "Short-term weeks that can build a schedule", "forecast"),
    ("Quality and speech analytics", "index.html#/track/quality", "Forms, topics, and program limits", "quality"),
    ("Diagrams", "index.html#/atlas", "Cited teaching sketches", "diagrams"),
    ("Flows", "index.html#/flows", "Animated call and routing pictures", "flows"),
    ("Play", "index.html#/play", "Port game, daily drill, sandbox, badges", "play"),
    ("Listen", "index.html#listen", "Audio desk on the home page", "listen"),
    ("Downloads", "index.html#/downloads", "Sheets, cards, deck, and the zip", "downloads"),
    ("Ecosystem", "index.html#/ecosystem", "Glossary, map, sisters, CRM, and future hooks", "eco"),
    ("Help", "index.html#/help", "Menu, course, bot, and downloads", "help"),
    ("Legal", "index.html#/legal", "Copyright, privacy, and removal", "legal"),
    ("Certifications", "index.html#/certs", "Catalog names, no invented exam codes", "certs"),
    ("Careers", "index.html#/career", "Practice paths, not a job offer", "careers"),
    ("Settings", "index.html#/settings", "Theme, sound, motion, and type size", "settings"),
]

ICONS = {
    "home": '<path d="M4 11 12 4l8 7v9H4z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9 20v-6h6v6" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "learn": '<path d="M5 4h10l4 4v12H5z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M15 4v4h4M8 12h8M8 16h5" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "skills": '<circle cx="12" cy="12" r="7" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="2" fill="currentColor"/>',
    "forecast": '<circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 8v5l3 2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>',
    "quality": '<circle cx="12" cy="12" r="7" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="3" fill="currentColor"/>',
    "diagrams": '<path d="M5 7h5v5H5zM14 12h5v5h-5z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10 9.5 14 14" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "flows": '<path d="M4 7h12M4 12h16M4 17h9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>',
    "play": '<path d="M8 5v14l12-7z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>',
    "listen": '<path d="M4 10v4h3l5 4V6L7 10z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>',
    "downloads": '<path d="M12 4v10M8 10l4 4 4-4M5 19h14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
    "eco": '<circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 12h16M12 4c2 2.2 3 5 3 8s-1 5.8-3 8c-2-2.2-3-5-3-8s1-5.8 3-8z" fill="none" stroke="currentColor" stroke-width="1.6"/>',
    "help": '<circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.8.4-1 .9-1 1.7V14" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M12 17h.01" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
    "legal": '<path d="M7 4h10v16H7z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9 8h6M9 12h6" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "certs": '<path d="M12 3.5 14.2 8l4.8.6-3.6 3.3.9 4.8L12 14.6 7.7 16.7l.9-4.8L5 8.6 9.8 8z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>',
    "careers": '<circle cx="12" cy="8" r="3" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 19c1.4-3 3.8-4.5 7-4.5s5.6 1.5 7 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/>',
    "settings": '<circle cx="12" cy="12" r="3" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 4v2.2M12 17.8V20M4 12h2.2M17.8 12H20M6.4 6.4l1.6 1.6M16 16l1.6 1.6M17.6 6.4 16 8M8 16l-1.6 1.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def menu_html(index_prefix: str) -> str:
    rows = []
    for label, href, blurb, icon in ITEMS:
        rows.append(
            f'<a href="{esc(index_prefix + href)}">'
            f'<span class="lab-ico" aria-hidden="true"><svg viewBox="0 0 24 24">{ICONS[icon]}</svg></span>'
            f'<span class="lab-copy"><strong>{esc(label)}</strong><small>{esc(blurb)}</small></span>'
            "</a>"
        )
    return (
        '<nav class="lab-menu" aria-label="Lab">'
        '<p class="lab-menu-title">Lab menu</p>'
        + "".join(rows)
        + "</nav>"
    )


def stylesheet_link(css_href: str) -> str:
    return f'<link rel="stylesheet" href="{esc(css_href)}">'


def prefixes(path: Path) -> tuple[str, str]:
    depth = len(path.relative_to(DOWNLOADS).parts) - 1
    ups = "../" * (depth + 1)
    css = ("../" * depth) + "lab-menu.css"
    return ups, css


def stamp_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if 'class="lab-menu"' in text:
        return False
    index_prefix, css_href = prefixes(path)
    link = stylesheet_link(css_href)
    if "lab-menu.css" not in text:
        text = text.replace("</head>", link + "</head>", 1)
    if 'rel="icon"' not in text and "rel='icon'" not in text:
        icon_prefix = "../" * (len(path.relative_to(DOWNLOADS).parts))
        icons = (
            f'<link rel="icon" href="{icon_prefix}favicon.ico" sizes="any">'
            f'<link rel="icon" href="{icon_prefix}favicon.svg" type="image/svg+xml">'
        )
        text = text.replace("</head>", icons + "</head>", 1)
    menu = menu_html(index_prefix)
    replaced = text.replace("<body>", "<body>" + menu, 1)
    if replaced == text:
        raise RuntimeError(f"no body tag in {path}")
    path.write_text(replaced, encoding="utf-8")
    return True


def stamp_all() -> int:
    count = 0
    for path in sorted(DOWNLOADS.rglob("*.html")):
        if stamp_html(path):
            count += 1
    return count


if __name__ == "__main__":
    print(f"stamped {stamp_all()} download pages")
