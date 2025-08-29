# Voice Cloning Assignment (Colab + GPU)

This repo gives you a **fully structured, Colab-friendly pipeline** to complete the assignment:

**Tutorial reference:** `https://www.youtube.com/watch?v=3iqvBEGS2So`  
(Title via search: *Fine-tune Orpheus or Sesame CSM‑1B with Unsloth (Voice Cloning)*.)

> ⚠️ Ethics reminder: Only clone voices you have the right to use (your own voice or with explicit permission). Clearly label synthetic audio.

---

## What’s inside
- **notebooks/Voice_Cloning_Assignment.ipynb** — one-click Colab notebook with:
  - GPU check, environment setup
  - Data upload + preprocessing (resample, normalize, segment)
  - Optional **Whisper** transcription to create text–audio pairs
  - **Baseline**: zero-shot cloning with **Coqui XTTS‑v2**
  - **Path A (TTS fine‑tune)**: Example config + commands for **XTTS‑v2** fine‑tuning (aligns with “3h audio” recommendation)
  - **Path B (Voice conversion)**: **RVC** training + inference (works with minutes of data, no transcripts)
  - **Evaluation**: A/B 30‑second WAV (original vs cloned), speaker‑sim similarity metric, WER (if transcripts)
  - **Logging**: sections for errors, timings, GPU/memory
- **scripts/** — small helper utilities (data prep, A/B generator).
- **config/** — starter configs to tweak.
- **reports/templates/** — Error log, Brief report, Resource log skeletons.
- **.gitignore**, **LICENSE (MIT)**

## Quick Start (Colab)
1. Open **notebooks/Voice_Cloning_Assignment.ipynb** in Colab (GPU **T4/A100** preferred).
2. Run cells **top to bottom**. Use **Path A** (XTTS fine-tune) **or** **Path B** (RVC).  
   - If you only have ~10–30 minutes of audio, *Path B (RVC)* is faster.  
   - If you have **≥ 2–3 hours** of clean audio + transcripts (or Whisper), try *Path A*.
3. Collect deliverables from `/content/outputs/`:
   - `github_repo/` (generated bundle you can push)
   - `logs/error_log.md` (you fill in)
   - `samples/ab_30s.wav` (original vs cloned demo)
   - `report/brief_report.md` (fill in template)

## Deliverables mapping
- **GitHub repo with your code** → push this repo (plus any trained weights links).
- **Error log document** → fill `reports/templates/Error_Log_Template.md` as you go.
- **30-second audio (original vs cloned)** → created by notebook in `outputs/samples/ab_30s.wav`.
- **Brief report** → fill `reports/templates/Brief_Report_Template.md`.

## Notes on data size
- Tutorial mentions ~**3 hours** of audio. That’s typical for **TTS fine‑tuning** quality.
- With **≤ 30 min** audio, document artifacts and quality changes. RVC often works decently with 10–30 min.

## License
MIT — see `LICENSE`.

---

## Safety & consent
Only use speech recordings you have a right to use. Do **not** impersonate others.
