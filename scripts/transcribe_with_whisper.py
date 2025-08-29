import os, csv
from faster_whisper import WhisperModel
from pathlib import Path

def transcribe_dir(wav_dir, out_csv, model_size="small"):
    model = WhisperModel(model_size, device="auto")
    rows = [("audio_path","text")]
    for f in sorted(Path(wav_dir).glob("*.wav")):
        segments, info = model.transcribe(str(f))
        txt = " ".join([s.text.strip() for s in segments])
        rows.append((str(f), txt))
        print(f.name, "->", txt[:80], "...")
    with open(out_csv, "w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerows(rows)
    return out_csv

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--wav_dir", required=True)
    ap.add_argument("--out_csv", default="dataset.csv")
    ap.add_argument("--model_size", default="small")
    args = ap.parse_args()
    transcribe_dir(args.wav_dir, args.out_csv, args.model_size)
