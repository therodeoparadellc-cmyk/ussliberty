# Liberty_Letter_2026 — Production Plan

Manual execution plan for a human operator running everything directly in the
Runway web app (no MCP, no API key). This is the source feeding
`manifest/shot_manifest.json`; the manifest already reflects everything below.

Runway generation settings (apply to every `generated` row unless noted):
- Aspect ratio: 16:9
- Model: your choice of available video model (seedance-2 or gen-4.5 recommended for mood/landscape work)
- Duration: generate at the nearest Runway-supported duration (5s or 10s); trim/conform to the `est_duration_s` below during edit — Runway does not generate arbitrary fractional lengths
- Content policy: every prompt below is written to stay mood/landscape/symbolic only — no depictions of the attack, casualties, identifiable real people, or contemporary conflict imagery, per project compliance rules. Runway's own content filter may still reject or alter a prompt at its discretion; if a generation is refused, do not rewrite it to work around the filter — stop and report which shot failed.

---

## Stage 1 — Voice test (do this first)

Generate beat B04's line in 3 candidate voices via Runway's Generate Audio (Seed Audio) tool:

Text: "There were 294 personnel aboard. Because the Liberty was a United States Navy technical research ship, she was crewed not by soldiers but predominantly by U.S. Navy sailors, alongside a small contingent of U.S. Marines and civilian intelligence personnel from the National Security Agency."

| Voice | Save as |
|---|---|
| Clint | `test_B04_v1.wav` |
| Mark | `test_B04_v2.wav` |
| Bernard | `test_B04_v3.wav` |

Pick one before continuing.

## Stage 2 — Full VO (all 10 beats, chosen voice)

| File | Text |
|---|---|
| `vo_B01.wav` | Dear Fellow Americans, This Fourth of July, as we celebrate our nation's independence and honor the sacrifices of those in uniform, we must look past the comfortable narratives and confront a stark, unresolved reality. |
| `vo_B02.wav` | True patriotism demands that we do not look away from uncomfortable truths, especially when the blood of American service members and innocent civilians is involved. Today, we demand accountability for the crew of the USS Liberty (AGTR-5) — and we demand a reckoning for the broader history of state violence that this tragedy exposed. |
| `vo_B03.wav` | On June 8, 1967, the USS Liberty — a clearly marked American naval vessel operating in international waters — was targeted in a relentless, two-hour assault by Israeli air and naval forces during the Six-Day War. |
| `vo_B04.wav` | There were 294 personnel aboard. Because the Liberty was a United States Navy technical research ship, she was crewed not by soldiers but predominantly by U.S. Navy sailors, alongside a small contingent of U.S. Marines and civilian intelligence personnel from the National Security Agency. |
| `vo_B05.wav` | Israeli fighter jets and torpedo boats battered the ship with rockets, napalm, and torpedoes. Thirty-four Americans were killed — 31 sailors, 2 Marines, and 1 NSA civilian. One hundred seventy-one more were wounded. In all, roughly seventy percent of the ship's crew was killed or injured in the two-hour attack. |
| `vo_B06.wav` | The crew fought with unimaginable bravery to save their ship, only to return home to a government that chose geopolitical expediency over the lives of its own men. The attack was hastily labeled a "tragic accident" — a narrative fiercely rejected by the survivors. The United States government orchestrated a cover-up, silencing the crew and denying their families the justice they deserved. Israel faced no meaningful consequences. |
| `vo_B07.wav` | The tragedy of the USS Liberty is not an isolated anomaly; it was a glaring warning. When a foreign military is permitted to slaughter American troops without consequence, impunity becomes policy. For decades, the Israeli government and its military apparatus have operated with a documented pattern of unchecked aggression and a profound lack of restraint. The same disregard for innocent life that rained down on American sailors in 1967 has been a continuous thread in the region, borne most heavily and devastatingly by Palestinian civilians subjected to decades of military occupation, disproportionate force, and systemic displacement. |
| `vo_B08.wav` | A history of violence, when met with silence and unconditional financial and military backing, only breeds further tragedy. We cannot claim to stand for liberty and justice while simultaneously writing blank checks to a state that demonstrates no resolve to protect the innocent, whether they are navigating the Mediterranean under an American flag or struggling to survive in Gaza and the West Bank. |
| `vo_B09.wav` | Awareness is no longer enough; it is time for action. This Independence Day, we must demand an end to the impunity. We must demand that our elected officials launch a full, unredacted congressional investigation into the attack on the USS Liberty. Furthermore, we must demand that all U.S. military aid and diplomatic support be strictly conditioned on absolute accountability, adherence to international law, and the preservation of human life. |
| `vo_B10.wav` | Let us honor the 34 men who perished on the USS Liberty not just with empty words, but with the courage to demand the truth and the resolve to hold the perpetrators accountable. In pursuit of truth, justice, and accountability, Michael Shaddox, United States Citizen, July 4th, 2026. |

---

## Stage 3 — Visuals (Runway generated shots only)

`text_card` and `archival` rows below are **not** Runway jobs — cards render locally from Pillow (stage 4) and archival stills need to be manually sourced from NARA/US Navy public-domain imagery (also stage 4). Only `generated` rows go into Runway. One generation per row; if one fails, stop and report rather than retrying with a modified prompt.

### B01 — Dear Fellow Americans (13.6s)
- **B01A** `generated`, 7.0s — "Wide cinematic shot of a single American flag on a tall pole, waving slowly against an overcast grey-white sky. Muted desaturated color, no sun visible, contemplative and solemn rather than triumphant. Slow, steady shot, minimal camera movement." — slow push in, 4% over duration
- **B01B** `generated`, 6.6s — "Empty small-town American Main Street at dawn, red-white-blue bunting hanging quietly along storefronts, nobody in frame, soft flat morning light, slight fog. Slow forward dolly down the center of the empty street." — slow dolly forward, constant speed

### B02 — True patriotism / USS Liberty (AGTR-5) (21.6s)
- **B02A** `text_card`, 5.0s — "USS LIBERTY (AGTR-5)"
- **B02B** `generated`, 8.0s — "Calm open ocean under overcast sky, no vessels or land in frame, subtle swell, muted grey-blue color palette, slow drone shot pushing forward low over the water surface. Empty, isolated, quiet." — slow forward push, low altitude
- **B02C** `archival`, 8.6s — asset `uss_liberty_at_sea.jpg`, source NARA/US Navy public-domain photo of USS Liberty (AGTR-5) underway, pre-attack, American flag visible — slow push in, 6% over duration

### B03 — June 8, 1967 (14.4s)
- **B03A** `text_card`, 5.0s — "JUNE 8, 1967"
- **B03B** `archival`, 9.4s — asset `uss_liberty_flag_closeup.jpg`, source NARA/US Navy photo showing USS Liberty's American flag/hull markings clearly — slow push in, 5% over duration

### B04 — 294 personnel aboard (17.6s)
- **B04A** `text_card`, 6.0s — "294 PERSONNEL ABOARD"
- **B04B** `archival`, 11.6s — asset `uss_liberty_crew.jpg`, source NARA/US Navy crew or dockside photo, respectful, non-graphic — slow push in, 5% over duration

### B05 — Casualties (20.0s)
- **B05A** `text_card`, 10.0s — "34 KILLED / 31 SAILORS · 2 MARINES · 1 NSA CIVILIAN / 171 WOUNDED"
- **B05B** `generated`, 10.0s — "An American flag at half-mast against a flat grey overcast sky, very slow motion, solemn and still, no other elements in frame. Memorial mood, no depiction of any vessel, conflict, or people." — static hold, minimal movement

### B06 — Cover-up (26.8s)
- **B06A** `generated`, 9.0s — "Close, shallow-depth-of-field shot of sunlight moving slowly across engraved names on a weathered stone memorial wall, no readable specific names, generic granite texture, contemplative and quiet." — slow lateral pan across surface
- **B06B** `text_card`, 8.0s — "“A TRAGIC ACCIDENT” / A COVER-UP, NOT AN ACCIDENT"
- **B06C** `generated`, 9.8s — "Wide distant exterior shot of a generic neoclassical federal government building in Washington D.C. style, overcast sky, no people or flags identifiable as a specific real building, symbolic of institutional silence." — slow push in, 4% over duration

### B07 — Pattern of impunity (38.4s)
- **B07A** `generated`, 10.0s — "Abstract symbolic image: old bronze scales of justice, slightly tarnished, sitting motionless in soft directional light against a plain dark background. No text, no figures." — slow push in, 4% over duration
- **B07B** `generated`, 9.0s — "Silhouette of a plain barbed-wire fence line against a muted sunset sky, no people, no identifiable flags, borders, or location markers, purely symbolic and abstract composition." — slow lateral pan, low horizon
- **B07C** `generated`, 9.4s — "Empty arid landscape at dusk, rolling bare hills, no people, no structures, no identifiable geographic or national markers, wide symbolic composition suggesting displacement and continuity." — slow pan right to left
- **B07D** `generated`, 10.0s — "Extreme close-up of a single candle flame burning steadily against a black background, soft flicker, no other elements, memorial and continuity mood." — static hold, subtle flicker only
- **Caution:** this beat's VO is the most politically sensitive in the letter (extends the argument to Palestinian civilians / decades of occupation). Every prompt above is deliberately abstract/symbolic with no flags, maps, or identifiable geography of the region, per the project's compliance rule against contemporary conflict imagery. Runway's content filter may still flag or refuse a generation here — if so, stop and report rather than trying to route around the filter with a reworded prompt.

### B08 — Blank checks (25.2s)
- **B08A** `generated`, 8.0s — "Abstract close-up of a stack of American currency bound with a plain paper band, softly lit, shallow depth of field, no text or numbers readable, symbolic of unconditional financial backing." — slow push in
- **B08B** `text_card`, 7.0s — "UNCONDITIONAL AID. / NO ACCOUNTABILITY."
- **B08C** `generated`, 10.2s — "Open Mediterranean-style sea at dusk, calm water reflecting a faint American flag silhouette rippling on the surface, no vessels or people, quiet and symbolic." — static hold, slow water motion only

### B09 — Demand for investigation (27.6s)
- **B09A** `generated`, 9.0s — "Wide exterior shot of a generic U.S. Capitol-style domed government building under a dramatic, heavy sky, no people visible, symbolic of pending congressional action." — slow push in, 4% over duration
- **B09B** `text_card`, 9.6s — "DEMAND: / A FULL, UNREDACTED / CONGRESSIONAL INVESTIGATION"
- **B09C** `generated`, 9.0s — "Close-up of a hand writing with a pen on plain paper on a wooden desk, only hand and forearm visible, no identifiable face, warm desk-lamp lighting, symbolic of formal written demand." — static hold, natural hand motion only

### B10 — Closing / signature (19.2s)
- **B10A** `generated`, 8.0s — "An American flag being ceremonially folded by two pairs of hands only (no faces visible), soft warm light, slow and respectful motion, solemn memorial tone." — static hold, slow natural motion
- **B10B** `text_card`, 6.2s — "IN PURSUIT OF TRUTH, / JUSTICE, AND ACCOUNTABILITY"
- **B10C** `text_card`, 5.0s — "MICHAEL SHADDOX / UNITED STATES CITIZEN / JULY 4, 2026"

---

## After Runway generation

Save each `generated` output as `assets/generated/{shot_id}.mp4` (e.g. `B01A.mp4`), matching the manifest exactly. Do not regenerate a shot that already exists unless explicitly asked. Once media is in hand, stages 4–5 (text cards, archival motion, FCPXML assembly) proceed as documented in CLAUDE.md.
