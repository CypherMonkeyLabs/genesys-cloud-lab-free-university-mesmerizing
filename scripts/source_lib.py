"""Shared source records for rooms and downloads.

URLs come from the lab's existing citations plus a fixed set of homes,
RFCs, and Wikipedia articles. Nothing here invents a Genesys article slug.
A link that does not return HTTP 200-399 stays in the list with status
"confirm".
"""

import json
import re
import urllib.error
import urllib.request
import zlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = ROOT / "campus" / "data" / "source-checks.json"
LAST_CHECKED = "2026-10"
USER_AGENT = "Mozilla/5.0 (compatible; GenesysLabSourceCheck/1.0)"

DEVELOPER_HOME = "https://developer.genesys.cloud/"
RESOURCE_HOME = "https://help.genesys.cloud/"
COMMUNITY_HOME = "https://community.genesys.com/"
WIKI_COMPANY = "https://en.wikipedia.org/wiki/Genesys_(company)"

RFC_RULES = [
    (
        "https://www.rfc-editor.org/rfc/rfc3261",
        "RFC 3261 SIP",
        ("sip", "invite", "session initiation", "rfc 3261", "rfc3261"),
    ),
    (
        "https://www.rfc-editor.org/rfc/rfc3550",
        "RFC 3550 RTP",
        ("rtp", "real-time transport", "realtime transport", "rfc 3550", "rfc3550"),
    ),
    (
        "https://www.rfc-editor.org/rfc/rfc3711",
        "RFC 3711 SRTP",
        ("srtp", "secure rtp", "rfc 3711", "rfc3711"),
    ),
    (
        "https://www.rfc-editor.org/rfc/rfc4733",
        "RFC 4733 DTMF",
        ("dtmf", "telephone-event", "telephone event", "rfc 4733", "rfc4733"),
    ),
]

WIKI_RULES = [
    (
        "https://en.wikipedia.org/wiki/Session_Initiation_Protocol",
        "Session Initiation Protocol",
        ("sip", "invite", "session initiation"),
    ),
    (
        "https://en.wikipedia.org/wiki/Real-time_Transport_Protocol",
        "Real-time Transport Protocol",
        ("rtp", "real-time transport", "realtime transport"),
    ),
    (
        "https://en.wikipedia.org/wiki/Secure_Real-time_Transport_Protocol",
        "Secure Real-time Transport Protocol",
        ("srtp", "secure rtp"),
    ),
    (
        "https://en.wikipedia.org/wiki/OAuth",
        "OAuth",
        ("oauth", "client credential", "pkce", "grant type"),
    ),
    (
        "https://en.wikipedia.org/wiki/Automatic_call_distributor",
        "Automatic call distributor",
        ("acd", "automatic call", "bullseye", "on queue"),
    ),
    (
        "https://en.wikipedia.org/wiki/Transport_Layer_Security",
        "Transport Layer Security",
        ("tls", "transport layer security"),
    ),
    (
        "https://en.wikipedia.org/wiki/Call_centre",
        "Call centre",
        ("contact center", "contact centre", "call centre", "call center"),
    ),
    (
        "https://en.wikipedia.org/wiki/WebRTC",
        "WebRTC",
        ("webrtc", "web rtc"),
    ),
    (
        "https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling",
        "Dual-tone multi-frequency signaling",
        ("dtmf", "telephone-event"),
    ),
    (
        "https://en.wikipedia.org/wiki/Interactive_voice_response",
        "Interactive voice response",
        ("ivr", "architect flow", "in-queue"),
    ),
]

KIND_LABEL = {
    "resource-center": "Resource Center",
    "developer": "Developer docs",
    "rfc": "RFC",
    "community": "Community",
    "wikipedia": "Wikipedia",
    "official": "Official page",
}

CONFIRM_NOTE = "The lab opened this URL in 2026-10 and could not verify it. Confirm before relying."


def xml(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def classify(url):
    host = (urlparse(url).hostname or "").lower()
    if host in ("help.genesys.cloud", "help.mypurecloud.com"):
        return "resource-center"
    if host == "developer.genesys.cloud":
        return "developer"
    if host == "www.rfc-editor.org":
        return "rfc"
    if host == "community.genesys.com":
        return "community"
    if host == "en.wikipedia.org":
        return "wikipedia"
    return "official"


def humanize(url):
    path = urlparse(url).path.strip("/").split("/")[-1]
    if not path:
        return urlparse(url).netloc or url
    words = path.replace("_", " ").replace("-", " ")
    return words[:1].upper() + words[1:]


def norm_url(url):
    text = str(url or "").strip()
    if text.endswith("/") and urlparse(text).path not in ("", "/"):
        return text[:-1]
    return text


def ok_code(code):
    return isinstance(code, int) and 200 <= code <= 399


def status_for(code):
    if ok_code(code):
        return "ok"
    return "confirm"


def note_for(status, extra=""):
    parts = [part.strip() for part in (extra, CONFIRM_NOTE if status == "confirm" else "") if part and part.strip()]
    return " ".join(parts)


CHECK_RULE = "body-v1"


def load_checks():
    if not CACHE_PATH.exists():
        return {}
    raw = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    checks = {}
    for url, item in raw.items():
        if isinstance(item, dict) and item.get("rule") == CHECK_RULE:
            checks[url] = int(item.get("status") or 0)
    return checks


def save_checks(checks):
    payload = {
        url: {"status": int(code), "lastChecked": LAST_CHECKED, "rule": CHECK_RULE}
        for url, code in sorted(checks.items())
    }
    CACHE_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _decode_body(raw):
    if raw[:2] == b"\x1f\x8b":
        try:
            return zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        except zlib.error:
            return b""
    return raw


def _title(text):
    match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()


def _visible_len(text):
    visible = re.sub(r"<script[\s\S]*?</script>", " ", text, flags=re.I)
    visible = re.sub(r"<style[\s\S]*?</style>", " ", visible, flags=re.I)
    visible = re.sub(r"<[^>]+>", " ", visible)
    return len(re.sub(r"\s+", " ", visible).strip())


def _assess(url, http_status, raw):
    """Return an HTTP-like code. 200-399 means the body identified the page."""
    if not (200 <= http_status <= 399):
        return http_status
    body = _decode_body(raw)
    text = body.decode("utf-8", "replace")
    low = text.lower()
    title = _title(text).lower()
    host = (urlparse(url).hostname or "").lower()
    path = urlparse(url).path or "/"
    if "page not found" in low and (not title or "not found" in title or "404" in title):
        return 404
    if host in ("help.genesys.cloud", "help.mypurecloud.com"):
        if not title or "not found" in title:
            return 404
        return http_status
    if host == "developer.genesys.cloud":
        # Every path returns the same short shell, including paths that do not exist.
        if path in ("", "/") and "developer" in title:
            return http_status
        return 0
    if host == "education.genesys.com":
        if _visible_len(text) < 80:
            return 0
        return http_status
    if host == "en.wikipedia.org":
        if not title or "wikipedia" not in title:
            return 404
        return http_status
    if host == "www.rfc-editor.org":
        if "rfc" not in title and "rfc" not in low[:4000]:
            return 0
        return http_status
    if host == "appfoundry.genesys.com":
        return http_status if "appfoundry" in low else 0
    if host == "community.genesys.com":
        return http_status if "genesys" in low else 0
    return http_status


def _fetch_once(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            raw = response.read()
            return _assess(url, int(response.status), raw)
    except urllib.error.HTTPError as exc:
        return int(exc.code)
    except Exception:
        return 0


def fetch_status(url):
    code = _fetch_once(url)
    if code == 0 or code >= 500:
        code = _fetch_once(url)
    return code


def check_urls(urls, cached=None):
    checks = dict(cached or {})
    pending = [url for url in urls if url not in checks]
    if not pending:
        return checks
    print(f"opening {len(pending)} links ({len(checks)} already cached)", flush=True)
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch_status, url): url for url in pending}
        done = 0
        for future in as_completed(futures):
            url = futures[future]
            checks[url] = int(future.result())
            done += 1
            if done % 25 == 0 or done == len(pending):
                print(f"opened {done}/{len(pending)}", flush=True)
    return checks


def _entry(title, url, code, extra_note=""):
    status = status_for(code)
    host = (urlparse(url).hostname or "").lower()
    path = urlparse(url).path or "/"
    if status == "confirm" and host == "developer.genesys.cloud" and path not in ("", "/"):
        extra_note = (extra_note + " " if extra_note else "") + "The response was the Developer Center shell, which is the same page for a missing path."
    if status == "confirm" and host == "education.genesys.com":
        extra_note = (extra_note + " " if extra_note else "") + "The HTML shell did not include the catalog or announcement text."
    return {
        "title": title or humanize(url),
        "url": url,
        "kind": classify(url),
        "lastChecked": LAST_CHECKED,
        "status": status,
        "note": note_for(status, extra_note),
    }


def matching_rfcs(blob):
    low = blob.lower()
    found = []
    for url, title, keys in RFC_RULES:
        if any(key in low for key in keys):
            found.append((title, url))
    return found


def pick_wiki(blob, checks):
    low = blob.lower()
    ranked = []
    for index, (url, title, keys) in enumerate(WIKI_RULES):
        hits = sum(1 for key in keys if key in low)
        if hits:
            ranked.append((hits, index, url, title))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    for _hits, _index, url, title in ranked:
        if ok_code(checks.get(url, 0)):
            return title, url
    return "Genesys (company)", WIKI_COMPANY


def enrich(base, blob, checks):
    """Return the room's own links, then developer, Resource Center, community, RFCs, and one Wikipedia article."""
    sources = []
    seen = set()

    def push(title, url, extra=""):
        if not url or not url.startswith("https://"):
            return
        key = norm_url(url)
        if key in seen:
            return
        seen.add(key)
        sources.append(_entry(title, url, checks.get(url, 0), extra))

    for item in base:
        push(item.get("title") or "", item["url"])

    if not any(item["kind"] == "developer" and item["status"] == "ok" for item in sources):
        push(
            "Genesys Cloud Developer Center",
            DEVELOPER_HOME,
            "General developer docs. This is the Developer Center home, not a page written for this room alone.",
        )
    if not any(item["kind"] == "resource-center" and item["status"] == "ok" for item in sources):
        push(
            "Genesys Cloud Resource Center",
            RESOURCE_HOME,
            "Resource Center home. Confirm the matching article for this room.",
        )
    push(
        "Genesys Community",
        COMMUNITY_HOME,
        "Community home, not a thread about this room.",
    )
    for title, url in matching_rfcs(blob):
        push(title, url, "Protocol specification.")
    wiki_title, wiki_url = pick_wiki(blob, checks)
    push(wiki_title, wiki_url, "Background article. It is not a Genesys Cloud product page.")
    return sources


def candidate_urls(blob):
    urls = [DEVELOPER_HOME, RESOURCE_HOME, COMMUNITY_HOME, WIKI_COMPANY]
    urls.extend(url for url, _title, _keys in RFC_RULES)
    urls.extend(url for url, _title, _keys in WIKI_RULES)
    return urls


def html_block(sources):
    items = []
    for src in sources:
        flag = ""
        if src.get("status") == "confirm":
            flag = ' <strong class="src-flag">confirm</strong>'
        note = ""
        if src.get("note"):
            note = f' <span class="src-note">{xml(src["note"])}</span>'
        kind = KIND_LABEL.get(src.get("kind"), "Official page")
        items.append(
            "<li>"
            f'<span class="src-kind">{xml(kind)}</span> '
            f'<a href="{xml(src["url"])}">{xml(src["title"])}</a> '
            f'<span class="src-checked">Last checked {xml(src["lastChecked"])}</span>'
            f"{flag}{note}</li>"
        )
    checked = sources[0]["lastChecked"] if sources else LAST_CHECKED
    return (
        '<section class="sources-deeper" id="sec-sources-deeper">'
        "<h2>Sources and go deeper</h2>"
        f"<p>Each link was opened for this lab. Last checked {xml(checked)}. "
        "A confirm flag means the lab could not verify that link.</p>"
        f"<ul>{''.join(items)}</ul></section>"
    )


def text_lines(sources):
    lines = ["Sources and go deeper", f"Last checked {LAST_CHECKED}"]
    for src in sources:
        flag = " confirm" if src.get("status") == "confirm" else ""
        kind = KIND_LABEL.get(src.get("kind"), "Official page")
        lines.append(f"{src['title']} ({kind}) {src['url']} Last checked {src['lastChecked']}{flag}")
        if src.get("note"):
            lines.append("  " + src["note"])
    return lines


def png_tail(sources):
    tail = ["SOURCES AND GO DEEPER", f"LAST CHECKED {LAST_CHECKED}"]
    if any(src.get("status") == "confirm" for src in sources):
        tail.append("CONFIRM")
    return tail


def normalize(sources):
    if not sources:
        return []
    if isinstance(sources[0], str):
        return [
            _entry(humanize(url), url, 0, "Listed before a completed check.")
            for url in sources
        ]
    return sources
