# manifest/shot_manifest.json — field reference

Top level:
- `video` — output spec (1920x1080, 24fps, fixed)
- `voice_id` — Runway Seed Audio voice ID, set after Phase 1 voice test
- `beats` — ordered array, one entry per VO beat (B01–B10)

Per beat:
- `beat_id` — e.g. `"B01"`
- `vo_text` — the exact VO line(s) for this beat, copied verbatim from `liberty_letter_revised.md`
- `vo_file` — path to the rendered VO audio, e.g. `audio/vo/vo_B01.wav`
- `est_duration_s` — measured via ffprobe after VO is generated (stage 2); do not hand-estimate
- `shots` — ordered array of shots covering this beat's runtime

Per shot (element of `beats[].shots`):
- `shot_id` — e.g. `"B01A"`, `"B01B"` (beat + letter suffix)
- `source_type` — one of `"generated"` (Runway), `"text_card"` (Pillow PNG, stage 4), `"archival"` (sourced still, animated in stage 4)
- `prompt` — Runway prompt text; required only when `source_type == "generated"`
- `text` — card copy; required only when `source_type == "text_card"`
- `asset` — filename under `assets/archival/`; required only when `source_type == "archival"`
- `treatment` — free-text note on motion (e.g. "slow push in, 4% over duration") used by stage 4 zoompan and by Runway prompts
- `est_duration_s` — this shot's slice of the beat's runtime; set/redistributed in stage 2

## Prerequisites not yet in this repo

This manifest is currently scaffolded with empty beats and no shots. Before Phase 1 (voice test) can run, the repo needs:

- `liberty_letter_revised.md` — the final letter script (source of all `vo_text`)
- `liberty_letter_production_plan.md` — shot list / treatment notes (source of all `shots` entries)

Once those exist, populate `vo_text` per beat and the `shots` array per beat (with `source_type`, `prompt`/`text`/`asset`, and `treatment`), then proceed to Stage 1.
