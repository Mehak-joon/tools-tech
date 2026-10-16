---
name: Asset Submission & Review
about: Submit a new 3D model, animation, texture pack, or VFX asset for pipeline review
title: "[ASSET] <Asset Name> - <Asset Category>"
labels: ["asset-review", "qa-pending"]
assignees: ""
---

### Asset Metadata
- **Asset Name:** `e.g., hero_character_warrior`
- **Asset Type:**
  - [ ] 3D Model (High-Poly / Low-Poly)
  - [ ] Rig & Animation
  - [ ] PBR Texture Set (Albedo, Normal, Roughness, Metallic, AO)
  - [ ] VFX Particle System / Shader Graph
  - [ ] Audio / Foley / BGM
- **Target LOD (Level of Detail):** LOD0 / LOD1 / LOD2 / Cinematic
- **File Format:** `.fbx` / `.obj` / `.blend` / `.exr` / `.png` / `.wav`

### Technical Validation Checklist
Before submitting, please ensure the asset complies with technical specifications:
- [ ] Pivot point centered at origin `(0, 0, 0)`
- [ ] Scale and rotation frozen / applied `(Scale: 1.0, 1.0, 1.0)`
- [ ] Polycount within budget (Triangles: `_____` / Budget: `_____`)
- [ ] UVs unwrapped within 0-1 space without overlapping (unless mirrored intentionally)
- [ ] PBR textures are power-of-two (e.g., 2048x2048 or 4096x4096)
- [ ] Files committed using **Git LFS** (verify with `git lfs ls-files`)
- [ ] Naming conventions followed (e.g., `SM_PropName_01`, `T_PropName_BC`)

### Asset Location in Repository
`assets/<category>/<asset_folder>/`

### Preview Renders / Viewport Captures
Attach turntables, clay renders, or engine viewport captures here.
