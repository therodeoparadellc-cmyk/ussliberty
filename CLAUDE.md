# CLAUDE.md — Liberty_Letter_2026

## Project
A ~5-minute letter-format documentary video essay: "A Letter to the American People on the Fourth of July, 2026." The full script is `liberty_letter_revised.md` (final — do not alter VO text without being asked). Production rules live in `liberty_letter_production_plan.md`. The single source of truth for all shots, VO text, and timing is `manifest/shot_manifest.json`.

## Deliverable spec
- 1920x1080, 24 fps, 16:9
- VO ≈ 3:45, final runtime ≈ 4:45–5:15
- Voice: Runway Seed Audio, single consistent voice across all beats (chosen in Phase 1; record the voice ID here once selected: ______)

## Directory conventions
- `manifest/shot_manifest.json` — source of truth; commit after every change
- `audio/vo/` — VO files named vo_B01.wav … vo_B10.wav; tests named test_B{n}_v{n}.wav
- `assets/generated/` — Runway video outputs named {shot_id}.mp4 (e.g. B01A.mp4)
- `assets/archival/` — manually sourced Navy/NARA imagery, named per manifest `asset` fields
- `audio/guide.wav` — optional 30s human guide read used as Seed Audio reference
- `assets/cards/` — rendered text-card PNGs named {shot_id}.png
- `assets/archival_motion/` — archival stills baked into zoompan MP4s named {shot_id}.mp4
- `package/` — final handoff: flat media + Assembly_v1.fcpxml, zipped for iPad transfer

## Pipeline stages (run in order; stop between stages for review)
1. **Voice test:** generate beat 4 VO in 2–3 voices → human picks → record choice above
2. **Full VO:** generate all beats with chosen voice → measure real durations with ffprobe → update every `est_duration_s` in the manifest → redistribute shot durations within each beat proportionally → commit
3. **Visuals:** generate all `source_type: "generated"` rows via Runway MCP (prompt, 16:9, conformed duration) → save as {shot_id}.mp4 → human reviews before any regeneration
4. **Text cards & still motion:** render every `text_card` manifest row as a 1920x1080 PNG (Pillow; white type on black, clean sans-serif, generous margins) into assets/cards/ named {shot_id}.png. Convert each archival still into a motion clip at its manifest duration using ffmpeg zoompan (slow push/pan per the row's treatment note) into assets/archival_motion/ named {shot_id}.mp4
5. **Timeline export:** write scripts/build_fcpxml.py that reads the conformed manifest and generates package/Assembly_v1.fcpxml — 1920x1080, 24fps; vo_B01–B10 placed sequentially on the audio lane; every shot placed at its beat start time on video, in manifest order, using text-card PNGs, archival_motion MP4s, and generated MP4s. Copy ALL referenced media flat into package/ with exact filenames matching the FCPXML references. Validate the XML parses before finishing. Zip package/ for SFTP transfer to the iPad

## Hard rules
- Never generate VO or video without reading the current manifest first
- Never regenerate a shot that already exists unless explicitly asked (credits are real money)
- One Runway generation per manifest row — no batch retries on failure; report and stop
- Do not modify VO text, the letter, or shot prompts on your own initiative
- `text_card` and `archival` rows are NOT Runway jobs — they are handled locally in stage 4, never sent to Runway
- Generated shots are mood/landscape/symbolic only: no depictions of the attack, casualties, identifiable real people, or contemporary conflict imagery (Runway content policy + project compliance notes)
- After any duration change, print a beat-by-beat timing table for human review before proceeding

## Environment notes
- There is NO desktop Resolve and NO Resolve MCP in this pipeline. Final edit happens in DaVinci Resolve for iPad (Cut + Color pages only — no Fusion, no Fairlight, no scripting). The handoff artifact is package/ containing all media plus Assembly_v1.fcpxml, which the operator imports on the iPad (media first, then FCPXML)
- Because iPad Resolve lacks Fusion, all typography must be delivered as rendered PNG media (stage 4) — never assume Text+ is available
- If the Runway MCP does not expose speech/audio generation (Seed Audio shipped 2026-06-30 and may postdate the MCP), write a minimal script calling the Runway API audio endpoint directly using $RUNWAY_API_KEY; save it as `scripts/gen_vo.py` and use it for all VO stages
- Operator works from iPad via SSH (Termius); keep output concise and avoid interactive prompts that require GUI access
