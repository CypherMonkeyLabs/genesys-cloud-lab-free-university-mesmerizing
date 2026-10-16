#!/usr/bin/env python3
"""One-page cheat sheets, flashcards, and an offline zip. No vendor paste."""

import json
import shutil
import struct
import subprocess
import time
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAMPUS = ROOT / "campus"
OUT = CAMPUS / "downloads"
REPO = "https://github.com/CypherMonkeyLabs/genesys-cloud-lab-free-university-mesmerizing"
PDF_REPO = "https://github.com/cipher0x9/genesys-cloud-lab-free-university-mesmerizing"
COPYRIGHT = "© 2026 CypherMonkeyLabs"
FOOT = [
    "CypherMonkey Labs · Signal Floor",
    COPYRIGHT,
    "https://cyphermonkeylabs.com",
    "https://linktr.ee/cyphermonkey",
    REPO,
    "Independent educational project. Not affiliated with or endorsed by any vendor.",
    "Trademarks belong to their owners. MIT code. CC BY-NC-SA content.",
    "Concerns: https://cyphermonkeylabs.com/#contact",
]

# 5x7 glyphs, each row is 5 bits.
FONT = {
    " ": [0, 0, 0, 0, 0, 0, 0],
    "A": [14, 17, 17, 31, 17, 17, 17],
    "B": [30, 17, 17, 30, 17, 17, 30],
    "C": [14, 17, 16, 16, 16, 17, 14],
    "D": [30, 17, 17, 17, 17, 17, 30],
    "E": [31, 16, 16, 30, 16, 16, 31],
    "F": [31, 16, 16, 30, 16, 16, 16],
    "G": [14, 17, 16, 23, 17, 17, 14],
    "H": [17, 17, 17, 31, 17, 17, 17],
    "I": [31, 4, 4, 4, 4, 4, 31],
    "J": [7, 2, 2, 2, 2, 18, 12],
    "K": [17, 18, 20, 24, 20, 18, 17],
    "L": [16, 16, 16, 16, 16, 16, 31],
    "M": [17, 27, 21, 21, 17, 17, 17],
    "N": [17, 25, 21, 19, 17, 17, 17],
    "O": [14, 17, 17, 17, 17, 17, 14],
    "P": [30, 17, 17, 30, 16, 16, 16],
    "Q": [14, 17, 17, 17, 21, 18, 13],
    "R": [30, 17, 17, 30, 20, 18, 17],
    "S": [15, 16, 16, 14, 1, 1, 30],
    "T": [31, 4, 4, 4, 4, 4, 4],
    "U": [17, 17, 17, 17, 17, 17, 14],
    "V": [17, 17, 17, 17, 17, 10, 4],
    "W": [17, 17, 17, 21, 21, 21, 10],
    "X": [17, 17, 10, 4, 10, 17, 17],
    "Y": [17, 17, 10, 4, 4, 4, 4],
    "Z": [31, 1, 2, 4, 8, 16, 31],
    "0": [14, 17, 19, 21, 25, 17, 14],
    "1": [4, 12, 4, 4, 4, 4, 14],
    "2": [14, 17, 1, 6, 8, 16, 31],
    "3": [30, 1, 1, 14, 1, 1, 30],
    "4": [2, 6, 10, 18, 31, 2, 2],
    "5": [31, 16, 30, 1, 1, 17, 14],
    "6": [6, 8, 16, 30, 17, 17, 14],
    "7": [31, 1, 2, 4, 8, 8, 8],
    "8": [14, 17, 17, 14, 17, 17, 14],
    "9": [14, 17, 17, 15, 1, 2, 12],
    ".": [0, 0, 0, 0, 0, 12, 12],
    ",": [0, 0, 0, 0, 4, 4, 8],
    ":": [0, 12, 12, 0, 12, 12, 0],
    ";": [0, 12, 12, 0, 4, 4, 8],
    "-": [0, 0, 0, 31, 0, 0, 0],
    "/": [1, 2, 4, 4, 4, 8, 16],
    "(": [2, 4, 8, 8, 8, 4, 2],
    ")": [8, 4, 2, 2, 2, 4, 8],
    "+": [0, 4, 4, 31, 4, 4, 0],
    "#": [10, 31, 10, 10, 31, 10, 0],
    "?": [14, 17, 1, 2, 4, 0, 4],
    "'": [4, 4, 8, 0, 0, 0, 0],
}


def pdf_escape(text):
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def wrap(text, width):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if len(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def write_pdf(path, title, lines):
    body = ["BT", "/F1 16 Tf", "48 760 Td", f"({pdf_escape(title)}) Tj", "/F1 10 Tf"]
    y_shift = -22
    body.append(f"0 {y_shift} Td")
    for line in lines:
        body.append(f"({pdf_escape(line)}) Tj")
        body.append("0 -14 Td")
    body.append("ET")
    stream = "\n".join(body).encode("latin-1", "replace")
    objects = []
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(b"<< /Type /Pages /Count 1 /Kids [3 0 R] >>")
    objects.append(b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>")
    objects.append(b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    blob = b"%PDF-1.4\n"
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(blob))
        blob += f"{i} 0 obj\n".encode() + obj + b"\nendobj\n"
    xref = len(blob)
    blob += f"xref\n0 {len(objects)+1}\n".encode()
    blob += b"0000000000 65535 f \n"
    for off in offsets[1:]:
        blob += f"{off:010d} 00000 n \n".encode()
    blob += f"trailer << /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF".encode()
    path.write_bytes(blob)


def chunk(tag, data):
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)


def write_png(path, title, lines):
    width, height = 900, 1200
    scale = 3
    rows = [bytearray([245, 241, 232]) * width for _ in range(height)]

    def pix(x, y, rgb):
        if 0 <= x < width and 0 <= y < height:
            i = x * 3
            rows[y][i:i + 3] = bytes(rgb)

    def rect(x, y, w, h, rgb):
        for yy in range(y, y + h):
            for xx in range(x, x + w):
                pix(xx, yy, rgb)

    rect(0, 0, width, 70, (7, 16, 28))
    text(rows, 24, 22, title.upper(), 3, (255, 90, 54), width)
    y = 100
    for line in lines:
        text(rows, 24, y, line.upper(), 2, (26, 12, 8), width)
        y += 18
        if y > height - 40:
            break
    raw = b"".join(b"\x00" + bytes(row) for row in rows)
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    path.write_bytes(png)


def text(rows, x, y, line, scale, rgb, width):
    cursor = x
    for ch in line:
        glyph = FONT.get(ch, FONT.get(ch.upper(), FONT["?"]))
        for gy, bits in enumerate(glyph):
            for gx in range(5):
                if bits & (1 << (4 - gx)):
                    for sy in range(scale):
                        for sx in range(scale):
                            px, py = cursor + gx * scale + sx, y + gy * scale + sy
                            if 0 <= px < width and 0 <= py < len(rows):
                                i = px * 3
                                rows[py][i:i + 3] = bytes(rgb)
        cursor += 6 * scale


def visible_foot():
    lines = []
    for line in FOOT:
        lines.append(line + " 🐒" if line == COPYRIGHT else line)
    return lines


def write_html(path, title, paragraphs, sources):
    body = "\n".join(f"<p>{p}</p>" for p in paragraphs)
    links = "\n".join(f'<li><a href="{url}">{url}</a></li>' for url in sources)
    foot = "\n".join(f"<p>{line}</p>" for line in visible_foot())
    path.write_text(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="../favicon.ico" sizes="any">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<title>{title}</title>
<style>
body {{ font: 16px/1.45 Georgia, serif; margin: 32px auto; max-width: 720px; color: #1b140f; background: #f7f4ef; }}
h1 {{ font-size: 28px; }}
a {{ color: #8d1d08; }}
footer {{ margin-top: 28px; border-top: 1px solid #ccc; padding-top: 12px; font-size: 13px; }}
@media print {{ body {{ background: #fff; }} }}
</style></head><body>
<h1>{title}</h1>
{body}
<h2>Sources</h2>
<ul>{links}</ul>
<footer>{foot}</footer>
</body></html>
""", encoding="utf-8")


def write_png_from_html(html_path, png_path):
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    if not chrome:
        return False
    if png_path.exists():
        png_path.unlink()
    proc = subprocess.Popen(
        [chrome, "--headless=new", "--no-sandbox", "--disable-gpu",
         f"--user-data-dir=/tmp/gccx-sheet-{html_path.stem}",
         "--window-size=840,1200", f"--screenshot={png_path}",
         "--virtual-time-budget=4000", html_path.as_uri()],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(40):
        time.sleep(0.25)
        if png_path.exists() and png_path.stat().st_size > 40000:
            proc.kill()
            proc.wait(timeout=5)
            return True
    proc.kill()
    proc.wait(timeout=5)
    return png_path.exists() and png_path.stat().st_size > 40000


def write_svg(path, title, lines, sources):
    tspans = []
    y = 86
    for line in lines[:28]:
        tspans.append(f'<text x="40" y="{y}" font-size="16" fill="#1b140f">{xml(line)}</text>')
        y += 22
    foot = f'<text x="40" y="760" font-size="12" fill="#4d4338">{xml(" · ".join(FOOT[:4]))}</text>'
    src = f'<text x="40" y="780" font-size="12" fill="#8d1d08">{xml(sources[0] if sources else "")}</text>'
    path.write_text(f"""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="1000" viewBox="0 0 800 1000">
<rect width="800" height="1000" fill="#f7f4ef"/>
<rect width="800" height="64" fill="#07101c"/>
<text x="40" y="42" fill="#ff5a36" font-size="24" font-family="Georgia, serif">{xml(title)}</text>
{''.join(tspans)}
{foot}
{src}
</svg>
""", encoding="utf-8")


def xml(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


SHEETS = [
    ("ports", "Ports and protocols", "Signaling and media for BYOC Cloud, from the firewall and trunk articles.",
     ["TLS trunks: TCP 5061. UDP or TCP trunks: commonly 5060. Both ends must match.",
      "Managed phones signal on TCP 8061. Unmanaged phones use TCP 5061.",
      "Media is UDP 16384-65535, opened outbound, RTP or SRTP.",
      "Phone provisioning uses TCP 443, and the phone article also lists TCP 80.",
      "Secure BYOC Cloud does not use IPsec. Use SIP TLS 1.2 and SRTP.",
      "Signaling addresses and SDP media addresses are different. Copy the current region table.",
      "Do not paste an address from this lab. Synthetic logs use RFC 5737."],
     ["https://help.genesys.cloud/articles/choose-a-trunk-transport-protocol/",
      "https://help.genesys.cloud/articles/tls-trunk-transport-protocol-specification/",
      "https://help.genesys.cloud/articles/ports-and-services-for-voip-phones-under-byoc-cloud/",
      "https://help.genesys.cloud/faqs/why-does-the-port-range-16384-32767-rtp-media-need-to-be-opened-up-for-genesys-cloud-voice-byoc-cloud/",
      "https://help.genesys.cloud/articles/byoc-cloud-public-sip-ip-addresses/"]),
    ("call-flow", "Voice call flow", "The short path a voice conversation takes.",
     ["Enter through Genesys Cloud Voice or a BYOC trunk. Premises calls can hit an Edge first.",
      "A published Architect flow decides. A draft does not answer.",
      "Transfer to a queue. The in-queue flow is the hold experience and must be published too.",
      "ACD offers an agent who is On Queue, under utilization, and acceptable to the evaluation method.",
      "Digital conversations skip the trunk and still need a flow and a queue."],
     ["https://help.genesys.cloud/articles/about-architect/",
      "https://help.genesys.cloud/articles/create-a-flow/",
      "https://help.genesys.cloud/articles/advanced-routing-overview/"]),
    ("architect", "Architect checklist", "Publish the flow the runtime will actually run.",
     ["Pick the flow type before you draw. Inbound, in-queue, bot, and secure are different types.",
      "Give every path a transfer, a handoff, or a disconnect.",
      "Call a bot from the inbound flow. Bind no-match, timeout, and error to a queue.",
      "A secure flow keeps payment audio out of the recording. It is not a place to store the digits.",
      "Save is a draft. Publish is what answers."],
     ["https://help.genesys.cloud/articles/create-a-flow/",
      "https://help.genesys.cloud/articles/queue-call-flows/",
      "https://help.genesys.cloud/articles/about-genesys-dialog-engine-bot-flows/"]),
    ("routing", "Routing troubleshooting", "Why an agent did not alert.",
     ["Are they On Queue, a member, and under utilization?",
      "All-skills matching needs every required skill, then the longest idle.",
      "Bullseye: up to five rings. A long delay means the outer ring is still closed.",
      "Preferred agents are first only if they are members and On Queue.",
      "One conversation-score priority point is 60,000 ms.",
      "Predictive routing is the queue method. Predictive Engagement is the website product."],
     ["https://help.genesys.cloud/articles/acd-evaluation-routing-methods/",
      "https://help.genesys.cloud/articles/bullseye-routing-overview/",
      "https://help.genesys.cloud/articles/create-queues/"]),
    ("byoc", "BYOC and PSTN", "Cloud carrier, premises Edge, or Genesys Cloud Voice.",
     ["BYOC Cloud: your carrier, Genesys media, no customer Edge on that path.",
      "Quick start order: location, trunk, outbound route, number plan.",
      "New cloud trunks use Dynamic Cloud Voice. Copy allowlists from the current article.",
      "BYOC Premises keeps phones and trunks on your Edge. Another site is failover only.",
      "Genesys Cloud Voice is the door where Genesys is the carrier."],
     ["https://help.genesys.cloud/articles/about-byoc-cloud/",
      "https://help.genesys.cloud/articles/byoc-cloud-configuration-overview/",
      "https://help.genesys.cloud/articles/edge-groups-overview/"]),
    ("emergency", "Emergency calling", "Name the owner before the first DID.",
     ["On BYOC, Genesys is not the emergency provider. You classify, route, and test.",
      "The default Emergency plan matches patterns such as 911 and 933 in the US and Canada, and still needs a route.",
      "The location is a physical place.",
      "A live emergency test is a carrier and public-safety conversation, not a demo."],
     ["https://help.genesys.cloud/articles/set-up-emergency-services-with-byoc/",
      "https://help.genesys.cloud/articles/number-plan-information/"]),
    ("wfm", "WFM forecast and schedule", "Short-term forecasts can build a schedule. Long-term forecasts cannot.",
     ["WFM is part of WEM and arrives with CX 3 on the overview.",
      "Short-term: interval data, up to six weeks, can generate a schedule.",
      "Long-term: day and week data, up to two years, seasonality only.",
      "Schedule with a forecast, without one, or blank. Maximum six weeks.",
      "The schedule dates must sit inside the short-term forecast. One generation per business unit at a time.",
      "Swapping the forecast does not move agent shifts until you reschedule."],
     ["https://help.genesys.cloud/articles/workforce-management/",
      "https://help.genesys.cloud/articles/work-with-forecasts/",
      "https://help.genesys.cloud/articles/work-with-workforce-management-schedules/"]),
    ("quality", "Recording and quality", "A policy decides which calls are kept. A form decides the score.",
     ["Quality management evaluates. It does not build the schedule.",
      "Recording policies choose calls and retention.",
      "A secure flow can suppress a payment segment. It does not replace the policy.",
      "AI scoring needs speech and text analytics, quality management, and AI Experience tokens.",
      "A score the agent cannot see and cannot dispute is not a quality program."],
     ["https://help.genesys.cloud/50540/",
      "https://help.genesys.cloud/articles/about-recording/",
      "https://help.genesys.cloud/faqs/category/speech-and-text-analytics/"]),
    ("api", "API and security", "The grant has to match who the call runs as.",
     ["Client credentials are for a service. The token cannot call /api/v2/users/me.",
      "User-facing apps use authorization code with PKCE.",
      "Token Implicit Grant is documented as deprecated after 25 May 2026.",
      "A role works only in the divisions it is paired with.",
      "This lab’s API explorer never sends the sample."],
     ["https://help.genesys.cloud/articles/create-an-oauth-client/",
      "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials"]),
    ("predictive", "Predictive Engagement", "The website product. Not ACD predictive routing.",
     ["Track web messaging with Messenger. Remove the legacy snippet or you double-count.",
      "A segment needs at least one condition. More conditions match fewer visitors.",
      "Action types: web messaging, web chat, content offer, or an Architect flow.",
      "Journey Outcomes: announced 2026-05-18, planned effective date 2026-06-29.",
      "Customer Outcomes, as described then, will not include outcome scoring.",
      "This sheet was written 15 October 2026 without signing in to an org."],
     ["https://help.genesys.cloud/articles/about-predictive-engagement/",
      "https://help.genesys.cloud/announcements/genesys-cloud/deprecation-journey-outcomes/"]),
    ("migration", "Migration cutover", "Rebuild the behavior. This lab has not found a converter.",
     ["Read the old flow as behavior, then draw Architect tasks and queues.",
      "UCCE skill groups are membership plus skills, not one Genesys object.",
      "CUCM can stay. BYOC is the door, not a replacement cluster.",
      "Cut over one number, then the queue, then the people.",
      "Test emergency before the rest of the staff arrives."],
     ["https://help.genesys.cloud/articles/about-architect/",
      "https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html"]),
    ("certs", "Certification path", "Say the catalog names. Do not invent a GCX- code.",
     ["GC-GCP is the professional exam. GC-GCD is the developer exam.",
      "Specialist rows are names: Architect, Workforce Management, Scripting, Quality, Outbound, Speech and Text Analytics.",
      "Two AI exams are named separately: AI – GPE & GPR, and AI – Digital Bots & Knowledge.",
      "Re-open the catalog and the announcement before you enroll or book.",
      "This lab’s quiz is not Genesys’ practice exam."],
     ["https://education.genesys.com/certification/cloud",
      "https://education.genesys.com/explore/announcement/genesys-technical-certifications-important-announcement"]),
    ("whats-new", "What’s new, 2026", "Dates as printed on the pages this lab opened.",
     ["Journey Outcomes deprecation announced 2026-05-18, planned effective 2026-06-29.",
      "Outcome-only action maps stop qualifying. getJourneyOutcome branches are skipped.",
      "A future Predictive Routing framework is announced for customer-defined outcomes. Shipment was not confirmed here.",
      "Web messaging is encouraged over web chat. Do not leave both snippets on the page.",
      "Implicit grant: deprecated after 25 May 2026, per the OAuth article.",
      "Unverified in a live organization. If a page moved, the page wins."],
     ["https://help.genesys.cloud/announcements/genesys-cloud/deprecation-journey-outcomes/",
      "https://help.genesys.cloud/announcements/genesys-cloud/predictive-routing-supports-customer-defined-business-outcomes-with-custom-kpis/",
      "https://help.genesys.cloud/articles/create-an-oauth-client/"]),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    catalog = []
    for sid, title, summary, lines, sources in SHEETS:
        prose = lines + ["Sources: " + " ".join(sources)] + FOOT
        html_path = OUT / f"{sid}.html"
        write_html(html_path, title, lines, sources)
        write_pdf(OUT / f"{sid}.pdf", title, wrap(" ".join(lines), 90) + [""] + ["Sources:"] + sources + [""] + FOOT + [PDF_REPO])
        png_path = OUT / f"{sid}.png"
        if not write_png_from_html(html_path, png_path):
            write_png(png_path, title, lines + [""] + FOOT)
        write_svg(OUT / f"{sid}.svg", title, lines + FOOT, sources)
        catalog.append({
            "id": sid,
            "title": title,
            "summary": summary,
            "html": f"downloads/{sid}.html",
            "pdf": f"downloads/{sid}.pdf",
            "png": f"downloads/{sid}.png",
            "svg": f"downloads/{sid}.svg",
            "sources": sources,
        })

    cards = []
    for path in sorted((CAMPUS / "data" / "tracks").glob("*.json")):
        track = json.loads(path.read_text(encoding="utf-8"))
        for lesson in track["lessons"]:
            for card in lesson["cards"]:
                cards.append({
                    "track": track["title"],
                    "lesson": lesson["title"],
                    "front": card["front"],
                    "back": card["back"],
                    "sources": [cite["url"] for cite in lesson["cites"]],
                })
    deck = {"title": "Signal Floor flashcards", "footer": FOOT, "cards": cards}
    (OUT / "flashcards.json").write_text(json.dumps(deck, indent=2) + "\n", encoding="utf-8")
    blocks = []
    for card in cards:
        blocks.append(f"<article><h2>{xml(card['front'])}</h2><p>{xml(card['back'])}</p><p>{xml(card['track'])} · {xml(card['lesson'])}</p></article>")
    (OUT / "flashcards.html").write_text(
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><title>Flashcards</title>"
        "<link rel='icon' href='../favicon.ico' sizes='any'><link rel='icon' href='../favicon.svg' type='image/svg+xml'>"
        "<style>body{font:15px/1.4 Georgia,serif;margin:24px;background:#f7f4ef;color:#1b140f}"
        "article{break-inside:avoid;border:1px solid #ccc;padding:12px;margin:8px 0;background:#fff}"
        "footer{margin-top:24px;font-size:13px}</style></head><body><h1>Signal Floor flashcards</h1>"
        + "\n".join(blocks)
        + "<footer>" + "\n".join(f"<p>{xml(line)}</p>" for line in visible_foot()) + "</footer></body></html>",
        encoding="utf-8",
    )
    (OUT / "catalog.json").write_text(json.dumps({"sheets": catalog, "cards": len(cards), "footer": FOOT}, indent=2) + "\n", encoding="utf-8")

    import zipfile
    zip_path = OUT / "genesys-cx-offline-bundle.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file in CAMPUS.rglob("*"):
            if not file.is_file() or file == zip_path:
                continue
            zf.write(file, file.relative_to(ROOT).as_posix())
    print(f"sheets {len(catalog)} cards {len(cards)} zip {zip_path.stat().st_size}")


if __name__ == "__main__":
    main()
