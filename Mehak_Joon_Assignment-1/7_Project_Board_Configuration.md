# Project Board Configuration & Task Tracking

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Item 7 - GitHub Project Board  

---

## 1. Project Board Methodology

To manage tasks, asset handoffs, and bug fixes across our Game & VFX pipeline, we implement an agile **Kanban Project Board** on GitHub Projects titled:  
**`Game & VFX Production Sprint 1`**

```
+------------------+------------------+------------------+------------------+
|    📋 BACKLOG    | ⏳ IN PROGRESS   | 🔍 REVIEW / QA   |    ✅ DONE       |
+------------------+------------------+------------------+------------------+
| #104             | #102             | #101             | #100             |
| Foliage shader   | Hero character   | Dungeon boss     | Initialize Git   |
| wind sway script | UV unwrapping &  | 4K PBR texture   | LFS & repository |
|                  | texturing        | set audit        | governance       |
| [Feature]        | [Asset]          | [Asset Review]   | [Governance]     |
+------------------+------------------+------------------+------------------+
| #105             | #103             |                  |                  |
| Sound effects    | Fix dark seam on |                  |                  |
| for spell cast   | normal map       |                  |                  |
| [Audio]          | [Bug]            |                  |                  |
+------------------+------------------+------------------+------------------+
```

---

## 2. Column Definitions & Workflows

1. **Backlog (To-Do):**
   * Newly submitted issues, feature requests, and planned asset models awaiting prioritization.
   * Tasks are assigned labels: `enhancement`, `asset-review`, `bug`.
2. **In Progress:**
   * Tasks currently being worked on by a developer, 3D modeler, or sound designer on their respective `feature/*` or `asset/*` branch.
   * WIP (Work In Progress) limit: Maximum 3 active tasks per contributor to prevent pipeline bottlenecks.
3. **Review / QA:**
   * Pull Requests submitted against `development`.
   * Assets undergo technical checklist verification:
     * Polycount budget audit
     * Texture format power-of-two check
     * Git LFS pointer validation
     * Code review for pipeline tools
4. **Done:**
   * Completed tasks whose PRs have successfully merged into `development` or `main`.
   * Issue is closed automatically via commit message (`Closes #102`).

---

## 3. Sample Issue Cards Configured

### Card 1: Asset Review (#101)
* **Title:** `[ASSET] Dungeon Boss - 3D Mesh & 4K PBR Set`
* **Assignee:** Mehak Joon (Lead TD)
* **Labels:** `asset-review`, `qa-pending`
* **Checklist:**
  - [x] Triangle budget verified (< 45,000 tris)
  - [x] Textures packed into ORM map (Occlusion, Roughness, Metallic)
  - [x] Tracked via Git LFS

### Card 2: Bug Fix (#103)
* **Title:** `[BUG] Normal map seam artifact on torso UV border`
* **Assignee:** 3D Environment Artist
* **Labels:** `bug`, `high-priority`
* **Resolution:** Re-baked tangent space normals in Blender 4.2 with MikkTSpace tangent basis.

### Card 3: Feature Implementation (#104)
* **Title:** `[FEATURE] Automated Digital Watermarking Script for Dailies`
* **Assignee:** Mehak Joon
* **Labels:** `enhancement`, `pipeline-tool`
* **Resolution:** Implemented `scripts/watermark_tool.py` supporting visible and forensic metadata embedding.
