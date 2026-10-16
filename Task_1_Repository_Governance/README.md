# Task 1: GitHub Repository Governance & Collaboration (10 Marks)

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Student Name:** Mehak Joon  
**Batch:** 2024–27  

---

## 🎯 Task Objectives
1. **Repository Structure:** Implement a clean, standardized folder hierarchy for game and media production.
2. **Role-Based Access Control (RBAC):** Configure access permissions for team collaboration (Admin, Maintainer, Contributor, Triage).
3. **Branching Strategy:** Design and implement GitFlow (`main`, `development`, `feature/*`, `asset/*`).
4. **Issue Templates:** Create at least 3 custom Issue Templates (`bug_report`, `feature_request`, `asset_submission`).
5. **Project Board:** Set up a Kanban task tracking board (Backlog, In Progress, Review/QA, Done).
6. **Screenshots:** Capture evidence of repository setup and settings.

---

## 📁 Repository Structure
```
tools-tech/
├── Task_1_Repository_Governance/      # [Task 1] Governance, RBAC, Issue Templates & Board
├── Task_2_Media_Asset_Management/      # [Task 2] Git LFS, Cloud Storage Architecture & Backups
├── Task_3_Media_Security/              # [Task 3] Threat Model, MFA, Watermarking Tool & Security
├── .github/
│   ├── ISSUE_TEMPLATE/                 # Active GitHub Issue Templates
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── asset_submission.md
│   └── pull_request_template.md        # Governed Pull Request checklist
├── assets/                             # Pipeline asset directories (models, textures, audio, vfx)
├── .gitattributes                      # Git LFS tracking rules
├── .gitignore                          # Engine/DCC cache exclusions
└── README.md                           # Main Project Overview
```

---

## 👥 Role-Based Access Control (RBAC) Matrix

| Role | Access Level | Responsibilities |
| :--- | :--- | :--- |
| **Project Lead / Tech Director** | Admin | Manages repository settings, branch protection rules, and team permissions. |
| **Senior Developers / Pipeline TDs** | Maintainer | Reviews code and asset PRs, approves merges into `development`. |
| **3D Artists / Animators** | Write / Contributor | Works on `feature/*` and `asset/*` branches, commits via Git LFS, opens PRs. |
| **QA Testers / Audio Contractors** | Triage / Read | Logs bugs using issue templates, tests builds, reviews documentation. |

---

## 🌿 Branching Strategy (GitFlow)

```
[main]          ─── Production / Release builds (Locked - requires 1 PR approval)
  ▲
  │ (Pull Request with Review Approval)
[development]   ─── Staging & daily integration branch
  ▲
  ├── [feature/player-controller]
  ├── [asset/hero-character-3d]
  └── [fix/texture-seam-artifact]
```

### Rules:
* Direct pushes to `main` and `development` are blocked.
* All changes must go through a Pull Request linked to an open issue.

---

## 📋 Included Issue Templates
Located in `Task_1_Repository_Governance/Issue_Templates/` and `.github/ISSUE_TEMPLATE/`:
1. **`bug_report.md`**: Captures engine version, reproductive steps, and error logs.
2. **`feature_request.md`**: Outlines proposed tool enhancements or gameplay mechanics.
3. **`asset_submission.md`**: Technical checklist for 3D models (polycount budget, UV unwrapping, power-of-two textures, Git LFS verification).

---

## 📌 Project Board (Kanban Workflow)
* **Backlog:** Newly created issues and backlog items.
* **In Progress:** Features/assets currently being developed.
* **Review / QA:** Pull Requests undergoing technical review.
* **Done:** Merged tasks with closed issues.
