#!/usr/bin/env python3
"""Write campus/data/sources/<room-id>.json after opening every link."""

import json
import subprocess
from pathlib import Path

from build_downloads import SHEETS
from source_lib import (
    LAST_CHECKED,
    candidate_urls,
    check_urls,
    enrich,
    humanize,
    load_checks,
    norm_url,
    save_checks,
)

ROOT = Path(__file__).resolve().parents[1]
CAMPUS = ROOT / "campus"
OUT = CAMPUS / "data" / "sources"

CERT_ANNOUNCEMENT = (
    "Genesys technical certifications announcement",
    "https://education.genesys.com/explore/announcement/genesys-technical-certifications-important-announcement",
)
MIGRATE_CHAT = (
    "Migrate from web chat to web messaging",
    "https://help.genesys.cloud/articles/migrate-from-web-chat-to-web-messaging-for-digital-user-tracking-and-predictive-engagement/",
)


def load_floor():
    raw = subprocess.check_output(
        [
            "node",
            "--input-type=module",
            "-e",
            "import { DIAGRAMS, PORTS } from './campus/assets/diagrams.js';"
            "process.stdout.write(JSON.stringify({diagrams:DIAGRAMS.map((d)=>({id:d.id,title:d.title,caption:d.caption,cite:d.cite,url:d.url,flow:!!d.flow})),ports:PORTS.map((p)=>({name:p.name,url:p.url,source:p.source}))}));",
        ],
        cwd=ROOT,
    )
    return json.loads(raw)


class Rooms:
    def __init__(self):
        self.rows = {}
        self.titles = {}

    def remember(self, title, url):
        if title and url and url not in self.titles:
            self.titles[url] = title

    def add(self, room_id, title, pairs, blob):
        slot = self.rows.setdefault(
            room_id,
            {"id": room_id, "title": title or room_id, "entries": [], "blob": "", "seen": set()},
        )
        if title and (not slot["title"] or slot["title"] == room_id):
            slot["title"] = title
        for label, url in pairs:
            if not url or not str(url).startswith("https://"):
                continue
            self.remember(label, url)
            key = norm_url(url)
            if key in slot["seen"]:
                continue
            slot["seen"].add(key)
            slot["entries"].append({"title": label or self.titles.get(url) or humanize(url), "url": url})
        slot["blob"] += " " + (blob or "")

    def titled(self, url):
        return self.titles.get(url) or humanize(url)


def lesson_pairs(lesson):
    return [(cite.get("title") or "", cite["url"]) for cite in lesson.get("cites") or [] if cite.get("url")]


def main():
    floor = load_floor()
    diagrams = floor["diagrams"]
    ports = floor["ports"]
    by_id = {item["id"]: item for item in diagrams}
    rooms = Rooms()
    for item in diagrams:
        rooms.remember(item["cite"], item["url"])
    for row in ports:
        rooms.remember(row["source"], row["url"])

    for path in sorted((CAMPUS / "data" / "tracks").glob("*.json")):
        track = json.loads(path.read_text(encoding="utf-8"))
        track_pairs = []
        track_blob = [track.get("title") or "", track.get("summary") or ""]
        for lesson in track["lessons"]:
            pairs = lesson_pairs(lesson)
            track_pairs.extend(pairs)
            blob = " ".join(
                [lesson.get("title") or "", lesson.get("summary") or ""]
                + list(lesson.get("paras") or [])
                + [label for label, _url in pairs]
            )
            rooms.add(lesson["id"], lesson.get("title") or lesson["id"], pairs, blob)
            track_blob.append(blob)
        rooms.add(track["id"], track.get("title") or track["id"], track_pairs, " ".join(track_blob))

    reference = json.loads((CAMPUS / "data" / "reference.json").read_text(encoding="utf-8"))
    gloss_pairs = [(item.get("source") or item.get("term") or "", item["url"]) for item in reference["glossary"]]
    rooms.add(
        "glossary",
        "Glossary",
        gloss_pairs,
        " ".join(item.get("term", "") + " " + item.get("def", "") for item in reference["glossary"]),
    )
    cert_pairs = [(item.get("name") or "Genesys Cloud exams", item["url"]) for item in reference["certs"]]
    cert_pairs.append(CERT_ANNOUNCEMENT)
    rooms.add("certs", "Certifications", cert_pairs, reference.get("certNote") or "certification exam catalog")
    interview_pairs = [(item.get("source") or "Interview source", item["url"]) for item in reference["interviews"]]
    rooms.add(
        "interview",
        "Interview drill",
        interview_pairs,
        " ".join(item.get("q", "") + " " + item.get("source", "") for item in reference["interviews"]),
    )
    boss_pairs = []
    for boss in reference["bosses"]:
        pair = [(boss.get("source") or boss["title"], boss["url"])]
        boss_pairs.extend(pair)
        rooms.add(boss["id"], boss["title"], pair, boss["title"] + " " + boss.get("brief", "") + " " + boss.get("source", ""))
    rooms.add("boss", "Boss incidents", boss_pairs, " ".join(boss["title"] + " " + boss.get("brief", "") for boss in reference["bosses"]))

    manifest = json.loads((CAMPUS / "data" / "manifest.json").read_text(encoding="utf-8"))
    studio_pages = {
        "architect": [
            ("Architect home", "https://help.genesys.cloud/articles/navigate-the-architect-home-page/"),
            ("Create a flow", "https://help.genesys.cloud/articles/create-a-flow/"),
            ("About Architect", "https://help.genesys.cloud/articles/about-architect/"),
        ],
        "routing": [
            ("Bullseye routing overview", "https://help.genesys.cloud/articles/bullseye-routing-overview/"),
            ("Evaluation methods", "https://help.genesys.cloud/articles/acd-evaluation-routing-methods/"),
            ("Advanced routing overview", "https://help.genesys.cloud/articles/advanced-routing-overview/"),
        ],
        "api": [
            ("Client credentials", "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials"),
            ("Create an OAuth client", "https://help.genesys.cloud/articles/create-an-oauth-client/"),
            ("Create queues", "https://help.genesys.cloud/articles/create-queues/"),
            ("AWS regions", "https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/"),
        ],
        "numbers": [
            ("Number plan information", "https://help.genesys.cloud/articles/number-plan-information/"),
        ],
        "migration": [
            ("About Architect", "https://help.genesys.cloud/articles/about-architect/"),
            ("Create queues", "https://help.genesys.cloud/articles/create-queues/"),
            ("Cisco Unified Contact Center Enterprise", "https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html"),
            ("Advanced routing overview", "https://help.genesys.cloud/articles/advanced-routing-overview/"),
            ("Bullseye routing overview", "https://help.genesys.cloud/articles/bullseye-routing-overview/"),
            ("Create a flow", "https://help.genesys.cloud/articles/create-a-flow/"),
            ("Dynamic Cloud Voice", "https://help.genesys.cloud/articles/dynamic-cloud-voice-platform-overview/"),
            ("Genesys Cloud for Salesforce", "https://help.genesys.cloud/articles/about-genesys-cloud-for-salesforce/"),
        ],
    }
    studio_blob = {
        "architect": "architect ivr flow in-queue task builder",
        "routing": "acd bullseye preferred agent routing on queue",
        "api": "oauth client credentials pkce grant token api",
        "numbers": "number plan emergency dial",
        "migration": "architect ivr cisco contact center cutover",
    }
    all_studio = []
    for studio in manifest["studios"]:
        pairs = studio_pages[studio["id"]]
        all_studio.extend(pairs)
        rooms.add(studio["id"], studio["title"], pairs, studio.get("summary", "") + " " + studio_blob[studio["id"]])
    rooms.add("studio", "Studios", all_studio, "studio architect routing api oauth ivr number plan migration")

    for sid, title, summary, lines, urls in SHEETS:
        pairs = [(rooms.titled(url), url) for url in urls]
        rooms.add(sid, title, pairs, " ".join([title, summary] + lines))

    def diagram_pairs(ids):
        pairs = []
        blob = []
        for did in ids:
            spec = by_id.get(did)
            if not spec:
                continue
            pairs.append((spec["cite"], spec["url"]))
            blob.append(spec["title"] + " " + spec["caption"])
        return pairs, " ".join(blob)

    atlas_pairs = [(item["cite"], item["url"]) for item in diagrams]
    rooms.add("atlas", "Diagrams", atlas_pairs, " ".join(item["title"] + " " + item["caption"] for item in diagrams))
    flow_pairs = [(item["cite"], item["url"]) for item in diagrams if item["flow"]]
    rooms.add("flows", "Flows", flow_pairs, " ".join(item["title"] + " sip rtp architect routing" for item in diagrams if item["flow"]))
    rooms.add("map", "Flow map", flow_pairs, "flow map architect routing sip")

    port_pairs = [(row["source"], row["url"]) for row in ports]
    port_pairs.extend(diagram_pairs(["firewall", "sip-ladder", "sip-rtp"])[0])
    rooms.add("ports", "Ports and protocols", port_pairs, "ports sip rtp srtp tls dtmf firewall signaling media")
    rooms.add("game", "Port game", [(item["title"], item["url"]) for item in rooms.rows["ports"]["entries"]], rooms.rows["ports"]["blob"] + " port game")

    arch_pairs, arch_blob = diagram_pairs(["core-region", "voice-path", "digital-path", "byoc-cloud", "byoc-prem", "packages"])
    rooms.add("architecture", "Architecture", arch_pairs, arch_blob + " architecture region byoc edge architect ivr")
    sec_pairs, sec_blob = diagram_pairs(["srtp-lock", "oauth"])
    sec_pairs.extend([
        ("TLS trunk transport", "https://help.genesys.cloud/articles/tls-trunk-transport-protocol-specification/"),
        ("Create an OAuth client", "https://help.genesys.cloud/articles/create-an-oauth-client/"),
        ("Client credentials", "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials"),
        ("Divisions overview", "https://help.genesys.cloud/articles/divisions-overview/"),
    ])
    rooms.add("security", "Security", sec_pairs, sec_blob + " oauth tls srtp security divisions pkce")
    play_pairs, play_blob = diagram_pairs(["acd-gate"])
    rooms.add("playbooks", "Playbooks", play_pairs, play_blob + " troubleshooting acd queue in-queue emergency rtp")
    dep_pairs, dep_blob = diagram_pairs(["cutover"])
    rooms.add("deploy", "Deployment", dep_pairs, dep_blob + " deploy region trunk architect queue emergency")
    rep_pairs, rep_blob = diagram_pairs(["sta-pipe", "wfm-loop"])
    rep_pairs.extend([
        ("Speech and text analytics", "https://help.genesys.cloud/articles/speech-and-text-analytics-overview/"),
        ("Workforce management", "https://help.genesys.cloud/articles/workforce-management/"),
        ("About Predictive Engagement", "https://help.genesys.cloud/articles/about-predictive-engagement/"),
    ])
    rooms.add("reporting", "Reporting", rep_pairs, rep_blob + " reporting analytics workforce quality predictive")
    rooms.add(
        "regions",
        "Regions",
        [
            ("AWS regions for Genesys Cloud", "https://help.genesys.cloud/articles/aws-regions-for-genesys-cloud-deployment/"),
            ("AWS regions for Genesys Cloud Voice", "https://help.genesys.cloud/articles/aws-regions-genesys-cloud-voice/"),
            ("Client credentials", "https://developer.genesys.cloud/api/rest/authorization/use-client-credentials"),
        ],
        "aws regions voice login host",
    )
    rooms.add(
        "topology",
        "Topology",
        [
            ("BYOC Cloud overview", "https://help.genesys.cloud/articles/byoc-cloud-overview/"),
            ("Edge groups", "https://help.genesys.cloud/articles/edge-groups-overview/"),
        ],
        "topology byoc edge region sip voice",
    )
    news_pairs = [
        ("Deprecation: Journey Outcomes", "https://help.genesys.cloud/announcements/genesys-cloud/deprecation-journey-outcomes/"),
        ("Predictive routing custom outcomes", "https://help.genesys.cloud/announcements/genesys-cloud/predictive-routing-supports-customer-defined-business-outcomes-with-custom-kpis/"),
        MIGRATE_CHAT,
        ("Create an OAuth client", "https://help.genesys.cloud/articles/create-an-oauth-client/"),
    ]
    if "pe-sunset" in by_id:
        news_pairs.append((by_id["pe-sunset"]["cite"], by_id["pe-sunset"]["url"]))
    rooms.add(
        "whats-new",
        "What’s new",
        news_pairs,
        "journey outcomes predictive routing web messaging oauth 2026",
    )
    rooms.add(
        "home",
        "Home",
        [
            ("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/"),
            ("About Architect", "https://help.genesys.cloud/articles/about-architect/"),
            ("RFC 3261 SIP", "https://www.rfc-editor.org/rfc/rfc3261"),
            ("Advanced routing overview", "https://help.genesys.cloud/articles/advanced-routing-overview/"),
        ],
        "genesys cloud cx contact center sip architect routing home",
    )
    rooms.add(
        "tracks",
        "Tracks",
        [
            ("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/"),
            ("About Architect", "https://help.genesys.cloud/articles/about-architect/"),
        ],
        "tracks curriculum architect contact center",
    )
    rooms.add(
        "ecosystem",
        "Ecosystem",
        [
            ("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/"),
            ("About Architect", "https://help.genesys.cloud/articles/about-architect/"),
            ("RFC 3261 SIP", "https://www.rfc-editor.org/rfc/rfc3261"),
            ("Genesys Cloud for Salesforce", "https://help.genesys.cloud/articles/about-genesys-cloud-for-salesforce/"),
            ("Genesys Cloud for Zendesk", "https://help.genesys.cloud/articles/about-genesys-cloud-for-zendesk/"),
            ("AppFoundry", "https://appfoundry.genesys.com/"),
        ],
        "ecosystem sip rtp salesforce zendesk architect wem contact center",
    )
    rooms.add("sandbox", "Flow sandbox", [("Create a flow", "https://help.genesys.cloud/articles/create-a-flow/"), ("About Architect", "https://help.genesys.cloud/articles/about-architect/")], "sandbox architect ivr flow")
    rooms.add("daily", "Daily challenge", [("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/")], "daily challenge genesys cloud contact center")
    rooms.add("badges", "Badges", [("Genesys Cloud exams", "https://education.genesys.com/certification/cloud")], "badges certification practice")
    rooms.add("career", "Careers", [("Genesys Cloud exams", "https://education.genesys.com/certification/cloud"), ("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/")], "career certification administrator architect developer")
    rooms.add("roadmap", "Roadmap", [("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/"), ("About Architect", "https://help.genesys.cloud/articles/about-architect/")], "roadmap study architect routing contact center")
    rooms.add("charts", "Charts", [("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/")], "charts counts from this lab not production metrics")
    rooms.add("play", "Play", [("About Architect", "https://help.genesys.cloud/articles/about-architect/"), ("Evaluation methods", "https://help.genesys.cloud/articles/acd-evaluation-routing-methods/")], "play practice port game routing architect")
    rooms.add("help", "Help", [("About Architect", "https://help.genesys.cloud/articles/about-architect/")], "help course architect menu")
    rooms.add("legal", "Legal and credits", [("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/")], "legal credits genesys cloud trademark")
    rooms.add("settings", "Settings", [("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/")], "settings display theme")
    rooms.add("search", "Search", [("Overview of Genesys Cloud", "https://help.mypurecloud.com/articles/overview-of-genesys-cloud/")], "search lessons glossary")
    rooms.add(
        "lab-checklist",
        "Lab checklist",
        [("About Architect", "https://help.genesys.cloud/articles/about-architect/")],
        "checklist architect trunk queue emergency publish",
    )

    sheet_pairs = []
    for _sid, _title, _summary, _lines, urls in SHEETS:
        sheet_pairs.extend((rooms.titled(url), url) for url in urls)
    rooms.add("downloads", "Downloads", sheet_pairs, "downloads cheat sheets html pdf")
    rooms.add("cheat", "Cheat codes", sheet_pairs, "cheat codes sheets download")

    pending = []
    for slot in rooms.rows.values():
        pending.extend(item["url"] for item in slot["entries"])
        pending.extend(candidate_urls(slot["blob"]))
    pending.extend(item["url"] for item in diagrams)
    checks = check_urls(list(dict.fromkeys(pending)), load_checks())
    save_checks(checks)

    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.json"):
        old.unlink()

    confirm = 0
    total = 0
    index = []
    for room_id in sorted(rooms.rows):
        slot = rooms.rows[room_id]
        sources = enrich(slot["entries"], slot["blob"], checks)
        payload = {
            "id": room_id,
            "title": slot["title"],
            "lastChecked": LAST_CHECKED,
            "sources": sources,
        }
        (OUT / f"{room_id}.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        index.append(room_id)
        total += len(sources)
        confirm += sum(1 for item in sources if item["status"] == "confirm")

    (OUT / "index.json").write_text(
        json.dumps({"lastChecked": LAST_CHECKED, "rooms": index}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"rooms {len(index)} links {total} confirm {confirm} checked {len(checks)}")


if __name__ == "__main__":
    main()
