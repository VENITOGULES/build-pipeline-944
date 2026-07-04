"""Transcribe the Portuguese voice memo with faster-whisper (runs on a CI runner
with open internet so the model can be fetched from the Hugging Face Hub)."""
import json
import os
import subprocess

from faster_whisper import WhisperModel

SRC = "audio/voice-memo.m4a"
WAV = "audio16k.wav"
OUT_DIR = "transcription"
MODEL_SIZE = os.environ.get("WHISPER_MODEL", "medium")

os.makedirs(OUT_DIR, exist_ok=True)

# Decode to 16 kHz mono wav for the model.
subprocess.run(
    ["ffmpeg", "-y", "-i", SRC, "-ar", "16000", "-ac", "1", WAV],
    check=True,
)

model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")
segments, info = model.transcribe(
    WAV, language="pt", beam_size=5, vad_filter=True
)
print(f"detected language: {info.language} (p={info.language_probability:.2f}), "
      f"duration: {info.duration:.1f}s, model: {MODEL_SIZE}")

seg_list = []
timestamped_lines = []
plain_parts = []
for seg in segments:
    text = seg.text.strip()
    ts = f"[{int(seg.start // 60):02d}:{int(seg.start % 60):02d}]"
    print(f"{ts} {text}", flush=True)
    timestamped_lines.append(f"{ts} {text}")
    plain_parts.append(text)
    seg_list.append({"start": seg.start, "end": seg.end, "text": text})

plain_text = " ".join(plain_parts).strip()

with open(os.path.join(OUT_DIR, "transcript.txt"), "w") as f:
    f.write(plain_text + "\n")

with open(os.path.join(OUT_DIR, "transcript_timestamped.txt"), "w") as f:
    f.write("\n".join(timestamped_lines) + "\n")

with open(os.path.join(OUT_DIR, "transcript.json"), "w") as f:
    json.dump(
        {
            "model": MODEL_SIZE,
            "language": info.language,
            "language_probability": info.language_probability,
            "duration": info.duration,
            "segments": seg_list,
        },
        f,
        ensure_ascii=False,
        indent=2,
    )

print(f"\nWrote transcript ({len(plain_text)} chars) to {OUT_DIR}/")
