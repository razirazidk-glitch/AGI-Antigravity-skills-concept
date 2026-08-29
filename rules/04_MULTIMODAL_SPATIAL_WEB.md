---
description: 3D spatial, audio extraction, modern web standards, and visual viewport auditing.
trigger: always_on
---
# MULTIMODAL SPATIAL & MODERN WEB

## 1. 2D/3D ASSET GENERATION
- 2D: Specify camera sensor dynamics, lens optics, material roughness/refraction, volumetric lighting.
- 3D: Enforce IBL HDRI lighting, metric bounding box normalization (THREE.Box3), Ray-Box interior shaders.

## 2. AUDIO & MODERN WEB
- Micro-interactions (<50ms): Synthesize via WebAudio API oscillators.
- Audio extraction: yt-dlp + FFmpeg EBU R128 loudness normalization.
- Modern Web: View Transitions API, Popover API, Container Queries, :has(), WebAssembly.
- Visual verification: Standardize viewport to 1920x1080 for screenshot critique.

## 3. AUTONOMOUS PRE-PRESENTATION VISUAL GATE
- Invariant: Whenever an HTML artifact, UI dashboard, chart, or visual component is generated or modified, the agent MUST NOT present it to the user without FIRST:
  1. Serving/opening the file locally;
  2. Navigating and capturing a Full HD (1920x1080) screenshot via Puppeteer MCP;
  3. Executing `view_file` on the screenshot `.png`;
  4. Performing an autonomous 3-point Red Team critique on contrast, layout, and visual fidelity.
- Prohibited: Delivering a response stating a visual artifact is complete without including the inspected screenshot evidence.

