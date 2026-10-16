# Task 2: Media Asset Management & Cloud Storage (10 Marks)

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Student Name:** Mehak Joon  
**Batch:** 2024–27  

---

## 🎯 Task Objectives
1. **Media Asset Hierarchy:** Design an industry-standard folder hierarchy for 3D meshes, textures, audio, and visual effects.
2. **Git LFS (Large File Storage):** Configure and demonstrate Git LFS tracking for heavy binary files.
3. **File Versioning Strategy:** Implement semantic versioning and asset naming conventions.
4. **Git Rollback Demonstration:** Demonstrate how to revert corrupt assets non-destructively in Git history.
5. **Backup & Disaster Recovery Plan:** Design a 3-2-1 backup strategy with RPO and RTO metrics.
6. **Cloud Storage Architecture:** Prepare a multi-tier cloud storage topology (Hot, Warm, Cold/Glacier) and cost optimization analysis.

---

## 📁 1. Media Asset Folder Hierarchy

Located in the root `assets/` directory:
```
assets/
├── models/      # 3D meshes (.fbx, .obj, .blend, .usd) [Tracked by Git LFS]
├── textures/    # PBR maps (.png, .tga, .exr, .psd) [Tracked by Git LFS]
├── audio/       # Sound effects, dialogue, foley (.wav, .ogg) [Tracked by Git LFS]
└── vfx/         # Particle flipbooks, shader graphs, simulations (.vdb) [Tracked by Git LFS]
```

---

## 📦 2. Git LFS Tracking Configuration

Git stores binary files inefficiently by re-saving the entire file for every small change. **Git LFS** solves this by replacing binary files in the repository with a 130-byte text pointer while storing the actual file on an external object storage server.

The project root `.gitattributes` tracks all binary media files:
```ini
# 3D Models
*.fbx filter=lfs diff=lfs merge=lfs -text
*.obj filter=lfs diff=lfs merge=lfs -text
*.blend filter=lfs diff=lfs merge=lfs -text

# Textures
*.png filter=lfs diff=lfs merge=lfs -text
*.exr filter=lfs diff=lfs merge=lfs -text
*.psd filter=lfs diff=lfs merge=lfs -text

# Audio
*.wav filter=lfs diff=lfs merge=lfs -text
*.ogg filter=lfs diff=lfs merge=lfs -text
```

### Helpful Commands:
```bash
# Verify tracked files
git lfs track

# List all files currently managed by LFS
git lfs ls-files
```

---

## ⏪ 3. Practical Rollback Demonstration

When an asset is corrupted or pushed with a defective UV map:
```bash
# View recent asset commits
git log -n 3 --oneline assets/textures/hero_albedo.png

# Revert the defective commit non-destructively
git revert <commit-hash> -m "Revert: Restored stable hero albedo texture"
git push origin development
```

---

## ☁️ 4. Cloud Storage Architecture (Hot, Warm, Cold)

```
[Artist Workstation]
       │ (10 GbE Local LAN)
       ▼
[Local Studio NAS Cache] (Fast local editing)
       │ (TLS 1.3 Sync)
       ▼
[AWS S3 Standard (Hot Tier)] (Active sprint assets - $0.023/GB)
       │ (60 Days Idle)
       ▼
[AWS S3 Standard-IA (Warm Tier)] (Milestone builds - $0.0125/GB)
       │ (180 Days Idle)
       ▼
[AWS S3 Glacier Deep Archive (Cold Tier)] (Raw footage, sim caches - $0.00099/GB)
```

---

## 📑 Detailed Reports Included in this Folder
1. **[`Cloud_Storage_Architecture_Diagram.md`](Cloud_Storage_Architecture_Diagram.md)**: Full topology, Mermaid diagrams, and IAM security.
2. **[`Backup_and_Recovery_Plan.md`](Backup_and_Recovery_Plan.md)**: 3-2-1 backup strategy, RPO (1 hr), RTO (4 hrs), and ransomware recovery.
3. **[`Cost_Optimization_Report.md`](Cost_Optimization_Report.md)**: Pricing analysis saving **68.8% annually** on a 100 TB media dataset.
4. **[`Git_LFS_and_Rollback_Guide.md`](Git_LFS_and_Rollback_Guide.md)**: Step-by-step commands for Git LFS and non-destructive rollbacks.
