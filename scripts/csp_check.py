#!/usr/bin/env python3
"""CSP readiness check for the Genesys Cloud CX Lab.

Fails (exit 1) if a loaded URL (script/img/iframe/src, stylesheet link, css url(),
js import, fetch, Worker) points off-origin. Citation anchors are not loads.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [ROOT / "index.html", ROOT / "campus" / "index.html", ROOT / "campus" / "offline.html"]
for folder in (
    ROOT / "campus" / "assets",
    ROOT / "campus" / "guide",
    ROOT / "campus" / "shared",
    ROOT / "guide",
):
    if folder.exists():
        FILES.extend(sorted(p for p in folder.rglob("*") if p.suffix in {".js", ".css", ".html"}))

PATTERNS = [
    (r'<(?:script|img|iframe|source|video|audio)[^>]+\bsrc="(https?://[^"]+)"', "html src"),
    (r'url\(\s*["\']?(https?://[^)"\']+)', "css url()"),
    (r'@import\s+["\'](https?://[^"\']+)', "css @import"),
    (r'\bimport\s*(?:\(|[^;]*from\s*)["\'](https?://[^"\']+)', "js import"),
    (r'\bfetch\(\s*["\'`](https?://[^"\'`]+)', "js fetch"),
    (r'new (?:Worker|WebSocket|EventSource)\(\s*["\'`](https?://[^"\'`]+)', "js net"),
]
# canonical and author links are not fetched as subresources.
LINK = re.compile(r'<link\b[^>]*>', re.I)
HREF = re.compile(r'href="(https?://[^"]+)"', re.I)
REL = re.compile(r'rel="([^"]+)"', re.I)

fail = []
seen = set()
for path in FILES:
    if not path.is_file():
        continue
    key = path.resolve()
    if key in seen:
        continue
    seen.add(key)
    text = path.read_text(errors="replace")
    for tag in LINK.findall(text):
        rels = set((REL.search(tag).group(1) if REL.search(tag) else "").lower().split())
        if rels & {"canonical", "author", "me"}:
            continue
        href = HREF.search(tag)
        if href:
            fail.append(f"{path.relative_to(ROOT)}: off-origin html link: {href.group(1)}")
    for pattern, kind in PATTERNS:
        for match in re.finditer(pattern, text):
            fail.append(f"{path.relative_to(ROOT)}: off-origin {kind}: {match.group(1)}")

for item in fail:
    print("FAIL", item)
print("csp_check:", len(fail), "off-origin loads")
sys.exit(1 if fail else 0)
