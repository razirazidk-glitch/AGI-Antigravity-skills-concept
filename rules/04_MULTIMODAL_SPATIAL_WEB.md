---
description: Modern web standards, interface styling, and autonomous pre-presentation visual gate.
trigger: always_on
---
# MULTIMODAL SPATIAL & MODERN WEB

## 1. MODERN WEB STANDARDS & RESPONSIVE ARCHITECTURE
- Modern CSS & Layouts: View Transitions API, Popover API, Container Queries, :has(), CSS Grid, Flexbox.
- High-Performance Web: WebAssembly, Web Audio API for tactile audio micro-interactions (<50ms).
- Zero-External Assets: When images or visual assets are required, synthesize them locally via `generate_image`.

## 2. AUTONOMOUS PRE-PRESENTATION VISUAL GATE
- Invariant: Whenever an HTML artifact, UI dashboard, chart, or visual component is generated or modified, the agent MUST NOT present it to the user without FIRST:
  1. Serving/opening the file locally;
  2. Navigating and capturing a Full HD (1920x1080) screenshot via Puppeteer MCP;
  3. Executing `view_file` on the screenshot `.png`;
  4. Performing an autonomous 3-point Red Team critique on contrast, layout, and visual fidelity.
- Prohibited: Delivering a response stating a visual artifact is complete without including the inspected screenshot evidence.


