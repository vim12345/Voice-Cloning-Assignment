import os, librosa, soundfile as sf
from pydub import AudioSegment, silence
from pathlib import Path

def ensure_sr_mono(in_path, out_path, sr=22050):
    y, s = librosa.load(in_path, sr=sr, mono=True)
    sf.write(out_path, y, sr)

def split_by_silence(in_path, out_dir, min_silence_len=500, silence_thresh=-40, keep_silence=200):
    audio = AudioSegment.from_file(in_path)
    chunks = silence.split_on_silence(audio,
                                      min_silence_len=min_silence_len,
                                      silence_thresh=silence_thresh,
                                      keep_silence=keep_silence)
    stems = []
    for i, c in enumerate(chunks):
        out = Path(out_dir) / f"chunk_{i:04d}.wav"
        c.export(out, format="wav")
        stems.append(str(out))
    return stems

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="Input WAV/MP3/FLAC file or folder")
    ap.add_argument("--out", required=True, help="Output folder for 10–20s chunks")
    ap.add_argument("--sr", default=22050, type=int)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    files = []
    p = Path(args.src)
    if p.is_dir():
        for f in p.rglob("*.*"):
            if f.suffix.lower() in [".wav",".mp3",".flac",".m4a"]:
                files.append(str(f))
    else:
        files = [str(p)]

    for f in files:
        tmp = Path(args.out) / ("_tmp_sr.wav")
        ensure_sr_mono(f, tmp, sr=args.sr)
        stems = split_by_silence(tmp, args.out)
        os.remove(tmp)
        print(f, "->", len(stems), "chunks")
