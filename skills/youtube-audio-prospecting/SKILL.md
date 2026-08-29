---
name: youtube-audio-prospecting
description: >-
  Universal audio asset intelligence, acoustic telemetry, sound design, and normalization. Trigger on: audio, sound effects, sfx, background music, audio asset, audio telemetry, soundscape, audio playback, sound design, extract audio, youtube audio, web audio, yt-dlp audio.
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

### 3. Anti-Synthetic Mandate (Authenticity First - Dual Classification)
- **UI Micro-Interactions / Haptic Feedback (< 50ms):** Procedural Web Audio API (`AudioContext`) oscillators permitted for instant mechanical clicks and tactile interface beeps.
- **Ambience, Production SFX & Domain Telemetry:** Using rudimentary synthetic oscillators is strictly FORBIDDEN. All realistic sound effects, vehicle engines, voices, environmental soundscapes, and domain audio MUST be prospected and extracted from authentic physical recordings via `yt-dlp` and `ffmpeg`.

### 4. Integration & Spatial Audio Rigging
- Place finalized audio assets into `public/audio/` or `assets/audio/`.
- Wire into the application's audio engine (e.g., HTML5 Audio, Web Audio API `AudioBufferSourceNode`, `THREE.AudioListener` with 3D positional panning and distance attenuation).

### 5. Verification & Telemetry
- Verify volume leveling, clean loop transitions (zero popping at loop boundaries), and correct spatial trigger responsiveness.

