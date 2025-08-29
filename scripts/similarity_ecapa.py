# Simple speaker similarity using SpeechBrain ECAPA embeddings
import argparse, torch, torchaudio
from speechbrain.pretrained import EncoderClassifier
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--a", required=True)
ap.add_argument("--b", required=True)
args = ap.parse_args()

classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb")
def emb(path):
    signal, fs = torchaudio.load(path)
    if signal.shape[0] > 1: signal = torch.mean(signal, dim=0, keepdim=True)
    with torch.no_grad():
        e = classifier.encode_batch(signal)
    return e.squeeze().cpu().numpy()

ea, eb = emb(args.a), emb(args.b)
cos = np.dot(ea, eb)/(np.linalg.norm(ea)*np.linalg.norm(eb)+1e-9)
print("Cosine similarity:", float(cos))
