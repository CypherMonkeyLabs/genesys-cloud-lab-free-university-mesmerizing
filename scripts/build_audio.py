#!/usr/bin/env python3
"""Build campus/audio/tour.mp3 and practice.mp3 with Kokoro.

Kokoro-82M and kokoro-onnx are Apache-2.0. Voices are am_michael (Architect, line A)
and af_heart (Apprentice, line B). The ONNX graph is not committed. Download the
v1.0 model files from the kokoro-onnx release into KOKORO_DIR (default /tmp/kokoro).

Phonemes use the espeak-ng frontend shipped with kokoro-onnx. The waveform is Kokoro,
with a quiet generated pad underneath. This is not a recording of a person.
"""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

ROOT = Path(__file__).resolve().parents[1]
AUDIO = ROOT / "campus" / "audio"
MODEL_DIR = Path(os.environ.get("KOKORO_DIR", "/tmp/kokoro"))
VOICES = {"A": "am_michael", "B": "af_heart"}
GAP = 0.42


def dialogue(path: Path) -> list[tuple[str, str]]:
    lines = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        text = raw.strip()
        if len(text) < 4 or not text.startswith("- "):
            continue
        speaker = text[2]
        if speaker in VOICES and text[3:4] == ":":
            lines.append((VOICES[speaker], text[4:].strip()))
    if len(lines) < 4:
        raise SystemExit(f"{path} has too few spoken lines")
    return lines


def bed(n: int, sr: int) -> np.ndarray:
    rng = np.random.default_rng(7)
    noise = rng.standard_normal(n).astype(np.float32)
    out = np.empty_like(noise)
    acc = np.float32(0)
    for i, sample in enumerate(noise):
        acc += np.float32(0.02) * (sample - acc)
        out[i] = acc
    t = np.arange(n, dtype=np.float32) / sr
    tone = 0.2 * np.sin(2 * np.pi * 110 * t) + 0.1 * np.sin(2 * np.pi * 164.81 * t)
    pad = (out * 0.25 + tone.astype(np.float32)) * np.float32(0.03)
    fade = min(n // 4, int(sr * 0.45))
    ramp = np.linspace(0, 1, fade, dtype=np.float32)
    pad[:fade] *= ramp
    pad[-fade:] *= ramp[::-1]
    return pad


def render(kokoro: Kokoro, lines: list[tuple[str, str]]) -> tuple[np.ndarray, int]:
    parts: list[np.ndarray] = []
    rate = 24000
    gap = np.zeros(int(rate * GAP), dtype=np.float32)
    for voice, text in lines:
        audio, rate = kokoro.create(text, voice=voice, speed=0.96, lang="en-us")
        parts.append(np.asarray(audio, dtype=np.float32))
        parts.append(gap)
    speech = np.concatenate(parts)
    peak = float(np.max(np.abs(speech))) or 1.0
    speech *= np.float32(0.9 / peak)
    mixed = speech + bed(len(speech), rate)
    peak = float(np.max(np.abs(mixed))) or 1.0
    if peak > 0.98:
        mixed *= np.float32(0.98 / peak)
    return mixed, rate


def write_mp3(samples: np.ndarray, rate: int, dest: Path, title: str) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as handle:
        wav = Path(handle.name)
    sf.write(wav, samples, rate)
    subprocess.run(
        [
            "ffmpeg", "-y", "-i", str(wav),
            "-codec:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "1",
            "-metadata", f"title={title}",
            "-metadata", "artist=Signal Floor",
            "-metadata", "comment=Kokoro Apache-2.0 voices am_michael and af_heart. Not a Genesys recording.",
            str(dest),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    wav.unlink(missing_ok=True)


def main() -> None:
    model = MODEL_DIR / "kokoro-v1.0.onnx"
    voices = MODEL_DIR / "voices-v1.0.bin"
    kokoro = Kokoro(str(model), str(voices))
    jobs = (
        (AUDIO / "scripts" / "tour.md", AUDIO / "tour.mp3", "How to view the floor"),
        (AUDIO / "scripts" / "practice.md", AUDIO / "practice.mp3", "How to practise and share"),
    )
    for script, dest, title in jobs:
        lines = dialogue(script)
        print(f"{script.name}: {len(lines)} lines")
        samples, rate = render(kokoro, lines)
        write_mp3(samples, rate, dest, title)
        print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
