---
name: youtube-audio-prospecting
description: >-
  Universal audio asset intelligence, acoustic telemetry, sound design, and normalization. Trigger on: audio, sound, sfx, sound effect, music, background audio, play sound, sound design, audio file, extract audio, web audio, youtube audio.
---
# Universal Audio & Acoustic Intelligence Protocol

This skill outlines the process for researching, vetting, extracting, and integrating authentic audio assets, acoustic telemetry, and sound design into software systems, simulations, multimedia apps, and games.

## Workflow

### 1. Acoustic Reference Search & Grounding
- Determine the acoustic requirements (e.g., "Turbofan jet engine thrust harmonics", "Martian atmospheric wind recordings", "Relational database transaction chime", "Subtle UI tactile clicks").
- Use the `research` subagent (`invoke_subagent` with `TypeName: "research"`, `Role: "Acoustic Intelligence Researcher"`) or `search_web` to prospect authentic reference sources across open multimedia databases (YouTube, Freesound, OpenAudio, NASA Open Audio):
  ```json
  {
    "TypeName": "research",
    "Role": "Acoustic Intelligence Researcher",
    "Prompt": "AUDIO PROSPECTING: Search authentic high-fidelity YouTube recordings for [ACOUSTIC CONCEPT]. Extract video IDs and URLs for signal processing via yt-dlp and ffmpeg."
  }
  ```

### 2. Multi-Source Extraction & Signal Processing
- Use Python scripts utilizing `yt-dlp`, `ffmpeg`, `pydub`, or `librosa` to extract and process the audio stream.
- Convert and optimize to web-compatible standards (`.ogg` for seamless looping, `.mp3` for compressed playback, `.wav` for uncompressed low-latency cues).
- Apply normalization, DC offset removal, and trim silence/noise if needed.

### 3. Absolute Anti-Synthetic Audio Law (Zero Synthesizer Exceptions)
- Generating procedural oscillators, Beep APIs, or synthetic sine wave proxies is STRICTLY PROHIBITED for any UI component, alert, or telemetry.
- 100% of sound effects, tactile micro-clicks, notification chimes, and transaction cues MUST be authentic physical audio assets (.wav, .mp3, .ogg) extracted and normalized from genuine high-fidelity recordings via yt-dlp and ffmpeg.

### 4. Integration & Spatial Audio Rigging
- Place finalized audio assets into `public/audio/` or `assets/audio/`.
- Wire into the application's audio engine (e.g., HTML5 Audio, Web Audio API `AudioBufferSourceNode`, `THREE.AudioListener` with 3D positional panning and distance attenuation).

### 5. Verification & Telemetry

