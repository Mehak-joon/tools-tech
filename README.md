# Game & VFX Production Pipeline Repository

**Subject:** Tools & Techniques of Game and VFX-II  
**Department:** BCA MIT | Seamedu School of Pro-Expressionism  
**Student Name:** Mehak Joon  
**Batch:** 2024–27  
**Assignment:** Assignment - 1  

---

## 1. Project Overview
This repository serves as a centralized, enterprise-grade production pipeline template designed for Game Development and VFX projects. It incorporates industry-standard repository governance, Git LFS (Large File Storage) asset handling, cloud storage tiering, threat modeling, and digital asset security.

```
tools-tech/
├── Task_1_Repository_Governance/      # [Task 1 - 10 Marks] RBAC, Branching, Issue Templates, Project Board
├── Task_2_Media_Asset_Management/      # [Task 2 - 10 Marks] Git LFS, Cloud Storage Architecture, Backups
├── Task_3_Media_Security/              # [Task 3 - 10 Marks] Threat Model, MFA, Watermarking Tool
├── Mehak_Joon_Assignment-1/            # Complete 12-item Assignment Submission Dossier
├── .github/
│   ├── ISSUE_TEMPLATE/                 # Active GitHub Issue Templates
│   └── pull_request_template.md        # Governed Pull Request checklist
├── assets/                             # Pipeline asset storage (models, textures, audio, vfx)
├── .gitattributes                      # Git LFS tracking rules
├── .gitignore                          # Engine/DCC cache exclusions
└── README.md                           # Main repository documentation
```

---

## 2. Repository Governance & Branching Strategy

Our studio workflow follows a modified **GitFlow** model customized for iterative game and visual effects pipelines:

```
[main]          (Production / Release builds only - Protected branch)
   ▲
   │ (Pull Request with 2 Approvals & QA verification)
[development]   (Active Integration & Staging environment)
   ▲
   ├────── [feature/character-rig]
   ├────── [asset/environment-props]
   └────── [fix/normal-map-artifact]
```

### Role-Based Access Control (RBAC) Matrix
| Role | Access Level | Responsibilities |
| :--- | :--- | :--- |
| **Lead Technical Director (Admin)** | Full Admin | Branch rule enforcement, secrets management, repository settings |
| **Senior Developers & Pipeline TDs (Maintainer)** | Write & Approve | Review PRs, manage Git LFS thresholds, merge into `development` |
| **3D Artists & Animators (Write/Contributor)** | Branch & LFS Write | Create feature/asset branches, submit PRs using issue templates |
| **QA Testers & Sound Designers (Triage/Read)** | Issue Creation & Read | Log bugs via issue templates, verify builds, review documentation |

---

## 3. Git LFS (Large File Storage) Setup

Large binary files (e.g., 4K EXR textures, high-poly FBX/OBJ meshes, uncompressed WAV audio) are managed via **Git LFS** to prevent repository bloat and ensure fast cloning operations.

### Quick Commands for Team Members
```bash
# 1. Install Git LFS locally
git lfs install

# 2. Check which files are tracked by LFS
git lfs track

# 3. View status of locked or tracked LFS assets
git lfs status

# 4. Pull all binary LFS pointers
git lfs pull
```

---

## 4. Issue Templates & Project Board
Repository collaboration is tracked using GitHub Projects (Kanban) and three structured issue templates:
1. **Bug Report (`bug_report.md`)**: Identifies mesh anomalies, texture artifacting, shader crashes, or pipeline tool failures.
2. **Feature Request (`feature_request.md`)**: Proposes pipeline automation, new shader capabilities, or engine integrations.
3. **Asset Submission & Review (`asset_submission.md`)**: Technical quality audit checklist (polycount budget, UV overlapping checks, power-of-two textures) before merging into staging.

---

## 5. Security & Digital Asset Protection
- **Multi-Factor Authentication (MFA)**: Mandatory 2FA enforced for all repository collaborators.
- **Branch Protection Rules**: Direct pushes to `main` and `development` are blocked. Requires signed commits (`GPG`) and passing pull request reviews.
- **Digital Watermarking**: Visible dailies burn-in and invisible forensic metadata tracking implemented via `Task_3_Media_Security/watermark_tool.py`.

---

## 6. Assignment Deliverables
The complete submission portfolio containing all 12 required reports, architecture diagrams, and viva preparation materials is located in the [`Mehak_Joon_Assignment-1/`](file:///c:/Users/hp/Desktop/tools-tech/Mehak_Joon_Assignment-1/) directory.
