#!/usr/bin/env python3
"""Emit campus/data JSON from the track modules and the reference pack."""

import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lessonlib import _ERRORS  # noqa: E402
from reference_data import REFERENCE  # noqa: E402

MODULES = [
    "t01_foundations",
    "t02_org",
    "t03_architect",
    "t04_acd",
    "t05_queues",
    "t06_byoc",
    "t07_edge",
    "t08_emergency",
    "t09_wfm",
    "t10_qm",
    "t11_sta",
    "t12_ai",
    "t13_api",
    "t14_crm",
    "t15_migration",
    "t16_ecosystem",
    "t17_predictive",
]

STUDIOS = [
    {"id": "architect", "title": "Architect-style flow builder", "summary": "A vertical task list that exports learning JSON. It is not an import file for a live org.", "accent": 3},
    {"id": "routing", "title": "Routing simulator", "summary": "Conversation score, bullseye rings, preferred agents, and evaluation methods as the articles describe them.", "accent": 1},
    {"id": "api", "title": "Platform API explorer", "summary": "Sample requests and JSON for grants and queues. The page never sends them.", "accent": 4},
    {"id": "numbers", "title": "Number plan desk", "summary": "Classify a dial string with the documented default plans. Not the in-product call simulator.", "accent": 2},
    {"id": "migration", "title": "Migration mapper", "summary": "A learning bridge from Engage, PureConnect, and Cisco UCCE to objects you rebuild.", "accent": 1},
]


def main():
    root = Path(__file__).resolve().parents[1]
    data = root / "campus" / "data"
    tracks_dir = data / "tracks"
    tracks_dir.mkdir(parents=True, exist_ok=True)
    seen = set()
    manifest_tracks = []
    quiz = 0
    for name in MODULES:
        track = importlib.import_module(name).TRACK
        if track["id"] in {item["id"] for item in manifest_tracks}:
            raise SystemExit(f"duplicate track {track['id']}")
        for lesson in track["lessons"]:
            if lesson["id"] in seen:
                raise SystemExit(f"duplicate lesson {lesson['id']}")
            seen.add(lesson["id"])
            quiz += len(lesson["quiz"])
        (tracks_dir / f"{track['id']}.json").write_text(json.dumps(track, indent=2) + "\n", encoding="utf-8")
        manifest_tracks.append({
            "id": track["id"],
            "title": track["title"],
            "kicker": track["kicker"],
            "accent": track["accent"],
            "summary": track["summary"],
            "file": f"data/tracks/{track['id']}.json",
            "lessons": [
                {
                    "id": lesson["id"],
                    "title": lesson["title"],
                    "level": lesson["level"],
                    "minutes": lesson["minutes"],
                    "summary": lesson["summary"],
                }
                for lesson in track["lessons"]
            ],
        })
    manifest = {
        "title": "Genesys Cloud CX Lab",
        "updated": "2026-10-15",
        "quizCount": quiz,
        "tracks": manifest_tracks,
        "studios": STUDIOS,
    }
    (data / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (data / "reference.json").write_text(json.dumps(REFERENCE, indent=2) + "\n", encoding="utf-8")
    lessons = len(seen)
    print(f"tracks {len(manifest_tracks)} lessons {lessons} quizzes {quiz}")
    if _ERRORS:
        print("\n".join(_ERRORS))
        raise SystemExit(f"{len(_ERRORS)} lesson shape errors")


if __name__ == "__main__":
    main()
