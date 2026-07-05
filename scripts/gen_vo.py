#!/usr/bin/env python3
"""Generate VO audio via the Runway text_to_speech API (not exposed by Runway MCP).

Usage:
  # Stage 1 — voice test: generate one beat in several candidate voices
  python scripts/gen_vo.py test --beat B04 --voices Maya Arjun Serene

  # Stage 2 — full VO: generate one beat (or all beats) in the chosen voice
  python scripts/gen_vo.py final --voice Maya --beat B04
  python scripts/gen_vo.py final --voice Maya

Requires RUNWAYML_API_SECRET in the environment. Runs one generation per
manifest row; on any failure it reports the error and stops (no retries).
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / "manifest" / "shot_manifest.json"
VO_DIR = REPO_ROOT / "audio" / "vo"

API_BASE = "https://api.dev.runwayml.com"
API_VERSION = "2024-11-06"
TTS_MODEL = "eleven_multilingual_v2"
POLL_INTERVAL_S = 5


def load_manifest():
    return json.loads(MANIFEST_PATH.read_text())


def save_manifest(manifest):
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n")


def get_beat(manifest, beat_id):
    for beat in manifest["beats"]:
        if beat["beat_id"] == beat_id:
            return beat
    raise SystemExit(f"beat {beat_id!r} not found in manifest")


def api_headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "X-Runway-Version": API_VERSION,
        "Content-Type": "application/json",
    }


def generate_speech(api_key, prompt_text, voice_preset_id):
    """POST /v1/text_to_speech, poll the task, return the output audio bytes."""
    headers = api_headers(api_key)
    body = {
        "model": TTS_MODEL,
        "promptText": prompt_text,
        "voice": {"type": "runway-preset", "presetId": voice_preset_id},
    }
    resp = requests.post(f"{API_BASE}/v1/text_to_speech", headers=headers, json=body)
    if not resp.ok:
        raise RuntimeError(f"text_to_speech request failed: {resp.status_code} {resp.text}")
    task_id = resp.json()["id"]
    print(f"    task {task_id} submitted, waiting...")

    while True:
        time.sleep(POLL_INTERVAL_S)
        poll = requests.get(f"{API_BASE}/v1/tasks/{task_id}", headers=headers)
        if not poll.ok:
            raise RuntimeError(f"task poll failed: {poll.status_code} {poll.text}")
        data = poll.json()
        status = data["status"]
        if status in ("PENDING", "THROTTLED", "RUNNING"):
            continue
        if status == "FAILED":
            raise RuntimeError(f"task {task_id} failed: {data.get('failure')} ({data.get('failureCode')})")
        if status == "CANCELLED":
            raise RuntimeError(f"task {task_id} was cancelled")
        if status == "SUCCEEDED":
            output_url = data["output"][0]
            audio = requests.get(output_url)
            if not audio.ok:
                raise RuntimeError(f"failed to download output: {audio.status_code}")
            return audio.content
        raise RuntimeError(f"unexpected task status: {status}")


def run_one(api_key, beat, voice_preset_id, out_path):
    print(f"  [{beat['beat_id']} / {voice_preset_id}] -> {out_path.relative_to(REPO_ROOT)}")
    audio = generate_speech(api_key, beat["vo_text"], voice_preset_id)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(audio)
    print(f"    wrote {len(audio)} bytes")


def cmd_test(args, api_key):
    manifest = load_manifest()
    beat = get_beat(manifest, args.beat)
    print(f"Voice test for {beat['beat_id']}: {len(args.voices)} candidate voice(s)")
    mapping = []
    for idx, voice in enumerate(args.voices, start=1):
        out_path = VO_DIR / f"test_{beat['beat_id']}_v{idx}.wav"
        try:
            run_one(api_key, beat, voice, out_path)
        except Exception as e:
            print(f"FAILED on voice {idx} ({voice}): {e}", file=sys.stderr)
            print("Stopping — no retries. Generations completed before this one are kept.", file=sys.stderr)
            sys.exit(1)
        mapping.append((idx, voice, str(out_path.relative_to(REPO_ROOT))))

    print("\nVoice index -> preset mapping:")
    for idx, voice, path in mapping:
        print(f"  v{idx} = {voice}  ({path})")
    print("\nListen and report back which index/voice to use.")


def cmd_final(args, api_key):
    manifest = load_manifest()
    beats = [get_beat(manifest, args.beat)] if args.beat else manifest["beats"]
    print(f"Generating final VO for {len(beats)} beat(s) in voice {args.voice!r}")
    for beat in beats:
        out_path = REPO_ROOT / beat["vo_file"]
        try:
            run_one(api_key, beat, args.voice, out_path)
        except Exception as e:
            print(f"FAILED on {beat['beat_id']}: {e}", file=sys.stderr)
            print("Stopping — no retries. Beats completed before this one are kept.", file=sys.stderr)
            sys.exit(1)

    manifest["voice_id"] = args.voice
    save_manifest(manifest)
    print(f"\nUpdated manifest voice_id to {args.voice!r}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_test = sub.add_parser("test", help="generate one beat in several candidate voices")
    p_test.add_argument("--beat", required=True, help="beat_id, e.g. B04")
    p_test.add_argument("--voices", required=True, nargs="+", help="2-3 Runway preset voice IDs, e.g. Maya Arjun Serene")

    p_final = sub.add_parser("final", help="generate final VO in the chosen voice")
    p_final.add_argument("--voice", required=True, help="Runway preset voice ID, e.g. Maya")
    p_final.add_argument("--beat", help="single beat_id; omit to generate all beats")

    args = parser.parse_args()

    api_key = os.environ.get("RUNWAYML_API_SECRET")
    if not api_key:
        raise SystemExit("RUNWAYML_API_SECRET is not set")

    if args.cmd == "test":
        cmd_test(args, api_key)
    elif args.cmd == "final":
        cmd_final(args, api_key)


if __name__ == "__main__":
    main()
