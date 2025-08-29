# Concatenate original and cloned into a 30s A/B WAV
import soundfile as sf, numpy as np, librosa, argparse, os
parser = argparse.ArgumentParser()
parser.add_argument("--original", required=True, help="Path to a reference/original wav")
parser.add_argument("--cloned", required=True, help="Path to a cloned/generated wav")
parser.add_argument("--out", default="ab_30s.wav")
parser.add_argument("--sr", type=int, default=22050)
args = parser.parse_args()

def load_pad(path, sr, secs):
    y, _ = librosa.load(path, sr=sr, mono=True)
    need = secs*sr
    if len(y) >= need:
        return y[:need]
    pad = np.zeros(need)
    pad[:len(y)] = y
    return pad

a = load_pad(args.original, args.sr, 15)
b = load_pad(args.cloned, args.sr, 15)
beep = 0.2*np.sin(2*np.pi*880*np.arange(int(0.25*args.sr))/args.sr)
sil = np.zeros(int(0.25*args.sr))
mix = np.concatenate([a, sil, beep, sil, b])
sf.write(args.out, mix, args.sr)
print("Wrote:", args.out)
