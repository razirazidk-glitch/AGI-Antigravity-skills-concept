---
name: interactive-kinetic-media-engine
description: >-
  Scroll-driven video scrubbing, parallax effects, and kinetic UI animations. Trigger on: animation, scroll animation, parallax, hover effect, micro interactions, cursor tilt, smooth scroll, interactive UI, kinetic media, video scrubbing.
---
# 🎬 Interactive Kinetic Media, Scrollytelling & 3D Icon Synthesis Engine

> **AGI/ASI DOGMA:** Delivering websites with inert media, abrupt transitions, or generic flat icons when contemporary high-standard interactivity is required is STRICTLY PROHIBITED. The system must implement fluid interpolation physics (Linear Interpolation / RAF), frame-accurate scroll video scrubbing, multi-layer parallax depth, cursor-driven 3D perspective transforms, and bespoke 3D tactile icons generated with alpha channel isolation.

---

## 1. Frame-Accurate Scroll Video Scrubbing (Canvas & Video Pipeline)

Enables video frames to advance or rewind in lockstep with the user's scroll speed, with damped physical inertia and zero browser decoder stutter.

### A. HTML5 Structure & Sticky Viewport
```html
<section class="scrub-scroll-track" id="scrub-container">
  <div class="scrub-sticky-viewport">
    <video 
      id="scrubVideo" 
      class="scrub-video-layer" 
      src="assets/videos/product_spatial_spin.mp4" 
      preload="auto" 
      muted 
      playsinline>
    </video>
    <canvas id="scrubCanvas" class="scrub-canvas-fallback"></canvas>
    
    <!-- Optical Scrollytelling HUD Overlays -->
    <div class="scrub-hud-overlay">
      <div class="scrub-chapter" data-start="0.0" data-end="0.3">
        <span class="hud-phase-tag">[ PHASE 01 : CHASSIS ]</span>
        <h2 class="hud-headline">Monolithic Basalt Shell</h2>
        <p class="hud-sub">Cold-forged composite casing engineered for structural acoustic dampening.</p>
      </div>
      <div class="scrub-chapter" data-start="0.3" data-end="0.7">
        <span class="hud-phase-tag">[ PHASE 02 : CORE ]</span>
        <h2 class="hud-headline">Quantum Optical Prism</h2>
        <p class="hud-sub">Dual refraction chambers aligning photon trajectories with sub-micron precision.</p>
      </div>
      <div class="scrub-chapter" data-start="0.7" data-end="1.0">
        <span class="hud-phase-tag">[ PHASE 03 : INTERFACE ]</span>
        <h2 class="hud-headline">Tactile Liquid Surface</h2>
        <p class="hud-sub">Hermetically sealed optical boundary delivering dynamic biometric feedback.</p>
      </div>
    </div>
  </div>
</section>
```

### B. High-Fidelity CSS Styling
```css
.scrub-scroll-track {
  position: relative;
  height: 450vh; /* Scroll track length */
  background: #06080a;
}

.scrub-sticky-viewport {
  position: sticky;
  top: 0;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.scrub-video-layer {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.scrub-canvas-fallback {
  display: none;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.scrub-hud-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 0 8vw;
}

.scrub-chapter {
  position: absolute;
  max-width: 480px;
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1), transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.scrub-chapter.is-active {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.hud-phase-tag {
  font-family: var(--font-mono, 'Geist Mono', monospace);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  color: #c4a482;
  display: block;
  margin-bottom: 0.75rem;
}

.hud-headline {
  font-family: var(--font-display, 'Syne', sans-serif);
  font-size: clamp(2rem, 4vw, 3.5rem);
  font-weight: 800;
  line-height: 1.05;
  color: #ffffff;
  margin-bottom: 1rem;
}

.hud-sub {
  font-family: var(--font-editorial, 'Plus Jakarta Sans', sans-serif);
  font-size: 1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.65);
}
```

### C. JavaScript Scrubbing Engine with Linear Interpolation (Lerp)
```javascript
class VideoScrollEngine {
  constructor(trackSelector, videoSelector, chaptersSelector) {
    this.track = document.querySelector(trackSelector);
    this.video = document.querySelector(videoSelector);
    this.chapters = document.querySelectorAll(chaptersSelector);
    
    this.targetProgress = 0;
    this.currentProgress = 0;
    this.lerpRate = 0.075; // Inertial damping rate
    this.isReady = false;

    this.bind();
  }

  bind() {
    if (!this.track || !this.video) return;

    this.video.addEventListener('loadedmetadata', () => {
      this.isReady = true;
      this.updateScroll();
      this.tick();
    });

    window.addEventListener('scroll', () => this.updateScroll(), { passive: true });
    window.addEventListener('resize', () => this.updateScroll(), { passive: true });
  }

  updateScroll() {
    const rect = this.track.getBoundingClientRect();
    const scrollableDistance = this.track.scrollHeight - window.innerHeight;
    const currentScrolled = -rect.top;
    
    const rawProgress = currentScrolled / scrollableDistance;
    this.targetProgress = Math.min(Math.max(rawProgress, 0), 1);
  }

  tick() {
    if (!this.isReady) return;

    // Interpolation formula: P_t = P_t + (P_target - P_t) * lambda
    this.currentProgress += (this.targetProgress - this.currentProgress) * this.lerpRate;

    // Update video frame
    if (this.video.duration) {
      const targetTime = this.currentProgress * this.video.duration;
      // Prevent micro-jitter if delta is negligible
      if (Math.abs(this.video.currentTime - targetTime) > 0.005) {
        this.video.currentTime = targetTime;
      }
    }

    // Update narrative chapters
    this.chapters.forEach(chapter => {
      const start = parseFloat(chapter.dataset.start);
      const end = parseFloat(chapter.dataset.end);
      if (this.currentProgress >= start && this.currentProgress < end) {
        chapter.classList.add('is-active');
      } else {
        chapter.classList.remove('is-active');
      }
    });

    requestAnimationFrame(() => this.tick());
  }
}

// Initialization:
// document.addEventListener('DOMContentLoaded', () => {
//   new VideoScrollEngine('#scrub-container', '#scrubVideo', '.scrub-chapter');
// });
```

---

## 2. Scrollytelling with Pinned Media (Sticky Storytelling Pin)

Ideal for architectural showcases, luxury hardware presentations, or visual essays where side-by-side narrative progresses while the center media transmutes:

```css
.scrolly-split-section {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  min-height: 100vh;
  position: relative;
  max-width: 1600px;
  margin: 0 auto;
}

.scrolly-media-pin {
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3rem;
}

.scrolly-media-stage {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 10;
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 32px 64px -16px rgba(0, 0, 0, 0.6);
}

.scrolly-media-slide {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transform: scale(1.06);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.scrolly-media-slide.is-visible {
  opacity: 1;
  transform: scale(1);
}

.scrolly-text-track {
  padding: 40vh 4rem 40vh 2rem;
}

.scrolly-card-step {
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  opacity: 0.25;
  transform: translateY(20px);
  transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.scrolly-card-step.is-active {
  opacity: 1;
  transform: translateY(0);
}
```

---

## 3. Multi-Layer Parallax & Mask Morphing (`clip-path`)

### A. Differential Multi-Plane Parallax Physics
Distribute elements across depth planes with calibrated velocity multipliers to synthesize optical 3D depth:

```javascript
class DifferentialParallax {
  constructor() {
    this.layers = [
      { el: document.querySelector('.plx-bg'), speed: 0.12 },
      { el: document.querySelector('.plx-mid'), speed: 0.38 },
      { el: document.querySelector('.plx-hero-img'), speed: 0.65 },
      { el: document.querySelector('.plx-fore-text'), speed: -0.22 } // Counter-flow kinetic layer
    ];
    this.scrollY = window.scrollY;
    this.currentY = window.scrollY;
    this.init();
  }

  init() {
    window.addEventListener('scroll', () => {
      this.scrollY = window.scrollY;
    }, { passive: true });
    this.loop();
  }

  loop() {
    this.currentY += (this.scrollY - this.currentY) * 0.1;
    
    this.layers.forEach(layer => {
      if (layer.el) {
        const offset = this.currentY * layer.speed;
        layer.el.style.transform = `translate3d(0, ${offset.toFixed(2)}px, 0)`;
      }
    });

    requestAnimationFrame(() => this.loop());
  }
}
```

### B. Expanding Mask Transition (`clip-path` Cinema Reveal)
As the user scrolls, media expands smoothly from a contained card to full viewport:

```css
.cinema-expand-container {
  height: 250vh;
  position: relative;
}

.cinema-expand-sticky {
  position: sticky;
  top: 0;
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cinema-expand-media {
  width: 100%;
  height: 100%;
  object-fit: cover;
  clip-path: inset(14% 18% round 32px);
  will-change: clip-path;
}
```

```javascript
// Clip-path update based on scroll progress
function updateCinemaMask(progress) {
  const media = document.querySelector('.cinema-expand-media');
  if (!media) return;
  
  const insetY = (14 * (1 - progress)).toFixed(2);
  const insetX = (18 * (1 - progress)).toFixed(2);
  const radius = (32 * (1 - progress)).toFixed(2);
  
  media.style.clipPath = `inset(${insetY}% ${insetX}% round ${radius}px)`;
}
```

---

## 4. Cursor 3D Tilt, Magnetic Pull & Optical Spotlight

### A. 3D Perspective Card Tilt with Dynamic Spotlight
```javascript
function applyKineticTilt(cardsSelector) {
  const cards = document.querySelectorAll(cardsSelector);
  
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      // Maximum rotation: 14 degrees
      const rotateX = ((y - centerY) / centerY) * -14;
      const rotateY = ((x - centerX) / centerX) * 14;

      card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) scale3d(1.02, 1.02, 1.02)`;
      card.style.setProperty('--mouse-x', `${((x / rect.width) * 100).toFixed(1)}%`);
      card.style.setProperty('--mouse-y', `${((y / rect.height) * 100).toFixed(1)}%`);
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
    });
  });
}
```

```css
.kinetic-tilt-card {
  position: relative;
  background: rgba(18, 22, 28, 0.7);
  backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  overflow: hidden;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s ease;
  transform-style: preserve-3d;
}

.kinetic-tilt-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
    rgba(255, 255, 255, 0.12),
    transparent 45%
  );
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.kinetic-tilt-card:hover::before {
  opacity: 1;
}
```

### B. Magnetic Attraction Physics for Buttons & Icons
```javascript
function applyMagneticPull(elementsSelector) {
  const elements = document.querySelectorAll(elementsSelector);

  elements.forEach(el => {
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - (rect.left + rect.width / 2);
      const y = e.clientY - (rect.top + rect.height / 2);

      // Magnetic displacement (force = 0.35)
      el.style.transform = `translate3d(${x * 0.35}px, ${y * 0.35}px, 0)`;
    });

    el.addEventListener('mouseleave', () => {
      el.style.transform = 'translate3d(0px, 0px, 0px)';
    });
  });
}
```

---

## 5. 3D Icon & Liquid Glass Synthesis Protocol (Nano Banana Engine)

When generating icons for products, features, navigation, or telemetry indicators:

### A. Master Prompt Formula for 3D Icons with Background Isolation
$$\text{Prompt} = \text{3D Isometric Object} + \text{Material Physics (Liquid Glass / Titanium / Champagne Gold)} + \text{Studio Lighting & Rim Light} + \text{Pure Solid White Background or Green Screen} + \text{100MP Macro Sensor}$$

- **Example 1 (Security / Shield Icon):**
  > `Prompt:` `"Minimalist 3D isometric emblem of a biometric vault shield, sculpted in heavy frosted translucent optical glass with an internal glowing amber laser core, dark brushed titanium rim, isolated on pure solid white background, soft studio ground contact shadow, macro Hasselblad 100MP, ultra-crisp edges, 1:1 aspect ratio"`
  > `ImageName:` `"icon_security_shield"`
  > `AspectRatio:` `"1:1"`

- **Example 2 (Processing / Quantum Speed Icon):**
  > `Prompt:` `"Minimalist 3D isometric icon of an optical quantum prism accelerator, layered refraction glass slices with iridescent rainbow caustics, matte obsidian base, isolated on pure solid white background, studio softbox lighting, ultra-sharp silhouette, 1:1 aspect ratio"`
  > `ImageName:` `"icon_quantum_speed"`
  > `AspectRatio:` `"1:1"`

- **Example 3 (Architecture / Spatial Icon):**
  > `Prompt:` `"Minimalist 3D isometric icon of an architectural cantilever pavilion, raw honed travertine stone and smoked glass panel, warm 3000K internal spotlight, isolated on pure solid white background, clean studio catalog render, 1:1 aspect ratio"`
  > `ImageName:` `"icon_spatial_living"`
  > `AspectRatio:` `"1:1"`

### B. Background Removal / Alpha Thresholding Script (`scratch/extract_icon_alpha.py`)
```python
import sys
from PIL import Image
import numpy as np

def extract_white_background(input_path, output_path, tolerance=240):
    img = Image.open(input_path).convert("RGBA")
    data = np.array(img)
    
    # Mask of white or near-white pixels
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    white_mask = (r >= tolerance) & (g >= tolerance) & (b >= tolerance)
    
    # Convert background to transparent
    data[:,:,3][white_mask] = 0
    
    result = Image.fromarray(data)
    result.save(output_path, "PNG")
    print(f"Icon saved with transparent alpha: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        extract_white_background(sys.argv[1], sys.argv[2])
```

### C. Tactile Icon CSS Wrapper
```css
.tactile-3d-icon {
  width: 64px;
  height: 64px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), filter 0.3s ease;
}

.tactile-3d-icon img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 12px 24px rgba(0, 0, 0, 0.45));
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), filter 0.3s ease;
}

.tactile-3d-icon:hover img {
  transform: translateY(-6px) scale(1.1) rotate(3deg);
  filter: drop-shadow(0 20px 32px rgba(196, 164, 130, 0.35));
}
```
