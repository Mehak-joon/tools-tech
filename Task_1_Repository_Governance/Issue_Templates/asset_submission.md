---
name: Asset Submission & Review
about: Submit a new 3D model, animation, texture pack, or VFX asset for pipeline review
title: "[ASSET] <Asset Name> - <Asset Category>"
labels: ["asset-review", "qa-pending"]
assignees: ""
---

### Asset Details
- **Asset Name:** `e.g. hero_sword_01`
- **Asset Type:** 3D Model / Texture / Audio / VFX
- **Format:** `.fbx` / `.obj` / `.blend` / `.png` / `.wav`

### Technical Validation Checklist
- [ ] Pivot point centered at origin `(0, 0, 0)`
- [ ] Transforms (Scale: 1.0, Rotation: 0) frozen/applied
- [ ] Polycount within budget (Triangles: `______`)
- [ ] UVs unwrapped without overlapping in 0-1 UV space
- [ ] Textures are power-of-two (e.g. 2048x2048)
- [ ] Large files tracked using Git LFS
