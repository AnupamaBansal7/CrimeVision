import os
import math
import struct
import wave
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def generate_forensic_samples():
    samples_dir = Path(__file__).resolve().parent
    samples_dir.mkdir(parents=True, exist_ok=True)

    # 1. Generate CCTV Surveillance Image with HUD Overlay
    img_path = samples_dir / "sample_surveillance_cam02.jpg"
    w, h = 1280, 720
    # Dark convenience store background simulation
    img = Image.new("RGB", (w, h), color=(18, 24, 38))
    draw = ImageDraw.Draw(img)

    # Grid / perspective floor lines
    for y in range(350, h, 40):
        draw.line([(0, y), (w, y)], fill=(28, 38, 58), width=1)
    for x in range(0, w, 80):
        draw.line([(x, 350), (x - 200, h)], fill=(28, 38, 58), width=1)

    # Counter partition
    draw.rectangle([300, 420, 980, 520], fill=(35, 45, 68), outline=(60, 80, 120), width=2)
    # Register till
    draw.rectangle([550, 380, 700, 430], fill=(20, 25, 35), outline=(100, 140, 180), width=2)

    # Suspect bounding box simulation (Red Box)
    draw.rectangle([420, 240, 580, 600], outline=(239, 68, 68), width=3)
    draw.rectangle([420, 215, 580, 240], fill=(239, 68, 68))
    draw.text((430, 220), "SUSPECT ALPHA [98%]", fill=(255, 255, 255))

    # Weapon target box (Yellow Box)
    draw.rectangle([540, 360, 620, 420], outline=(245, 158, 11), width=2)
    draw.text((545, 345), "WEAPON: GLOCK 19 [96%]", fill=(245, 158, 11))

    # Clerk bounding box simulation (Blue Box)
    draw.rectangle([740, 260, 890, 580], outline=(56, 189, 248), width=2)
    draw.rectangle([740, 235, 890, 260], fill=(56, 189, 248))
    draw.text((750, 240), "VICTIM (CLERK) [99%]", fill=(15, 23, 42))

    # Camera HUD text
    draw.text((40, 30), "CAM-02 INTERIOR REGISTER 1", fill=(0, 255, 180))
    draw.text((40, 55), "2026-10-24 22:45:12 UTC - 30.00 FPS - 1080p RAW", fill=(180, 200, 220))
    draw.text((1050, 30), "REC ● LIVE FORENSIC", fill=(255, 60, 60))
    draw.text((40, 670), "SHA-256 INTEGRITY VALIDATED | SECTOR 4B DISPATCH", fill=(120, 140, 170))

    img.save(img_path, "JPEG", quality=92)
    print(f"Generated sample image: {img_path}")

    # 2. Generate Sample Audio WAV file
    audio_path = samples_dir / "dispatch_counter_mic01.wav"
    sample_rate = 16000
    duration_sec = 4.0
    num_samples = int(sample_rate * duration_sec)

    with wave.open(str(audio_path), "w") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)

        # Generate realistic audio modulation (chirps + pulses simulating radio dispatch audio)
        frames = bytearray()
        for i in range(num_samples):
            t = float(i) / sample_rate
            # 800Hz beep + 440Hz vocal simulation carrier + noise
            val = 0.3 * math.sin(2.0 * math.pi * 880.0 * t) if t < 0.2 else 0.0
            val += 0.4 * math.sin(2.0 * math.pi * 320.0 * t) * math.sin(2.0 * math.pi * 8.0 * t)
            # Clip and pack
            sample_val = int(max(-1.0, min(1.0, val)) * 32767)
            frames.extend(struct.pack("<h", sample_val))

        wav_file.writeframes(frames)
    print(f"Generated sample audio: {audio_path}")

    # 3. Create Sample Video file
    video_path = samples_dir / "cctv_exterior_getaway.mp4"
    if not video_path.exists():
        # Minimal valid MP4 container header
        with open(video_path, "wb") as f:
            f.write(b"\x00\x00\x00\x20ftypisom\x00\x00\x02\x00isomiso2avc1mp41\x00\x00\x00\x08free")
    print(f"Generated sample video: {video_path}")

if __name__ == "__main__":
    generate_forensic_samples()
