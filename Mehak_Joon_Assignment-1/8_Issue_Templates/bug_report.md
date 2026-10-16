---
name: Bug Report
about: Create a report to help us fix asset defects, pipeline crashes, or shader bugs
title: "[BUG] <Brief Description>"
labels: ["bug", "triage"]
assignees: ""
---

### Bug Overview
A clear and concise description of the bug encountered in the Game/VFX pipeline.

### Category
- [ ] 3D Model / Topology / Rigging
- [ ] Textures / Shaders / Material Graph
- [ ] Animation / Rigging Issue
- [ ] Lighting / Render Engine (Cycles / Arnold / Lumen)
- [ ] Engine Crash / Script Error (Python / C++ / C#)
- [ ] Pipeline Tooling / Git LFS Issue

### Steps to Reproduce
1. Open the project in DCC tool / Engine version: `________`
2. Navigate to asset path: `assets/___________`
3. Execute action: `___________`
4. Notice the error / anomaly.

### Expected Behavior
A concise description of what was expected to happen (e.g., normal map aligns with UV space without seam artifacts).

### Actual Behavior
What actually happened (e.g., normal map causes dark seam artifact at UV border, or engine crashes with fatal out-of-bounds error).

### Environment Details
- **DCC Tool / Engine:** Blender 4.x / Maya 2024 / Unreal Engine 5.x / Unity 2023.x
- **OS:** Windows 11 / macOS / Linux
- **GPU & Driver:** NVIDIA RTX / AMD Radeon (Driver Version: `____`)
- **Git Branch:** `development` / `feature/____`
- **Git LFS Installed:** Yes / No

### Screenshots / Error Logs
Attach screenshots, render snippets, or terminal log outputs below.
