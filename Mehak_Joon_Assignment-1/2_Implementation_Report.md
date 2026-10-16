# SEAMEDU SCHOOL OF PRO-EXPRESSIONISM
## Department of BCA MIT | Tools & Techniques of Game and VFX-II
### ASSIGNMENT - 1: COMPREHENSIVE IMPLEMENTATION REPORT

---

**Student Name:** Mehak Joon  
**Batch:** 2024–27  
**Department:** BCA MIT  
**Subject:** Tools & Techniques of Game and VFX-II  
**Task Name:** Assignment - 1 (Media Pipeline Governance, Cloud Storage & Digital Asset Protection)  
**Submission Date:** October 2026  
**Repository Link:** [https://github.com/Mehak-joon/tools-tech](https://github.com/Mehak-joon/tools-tech)  

---

## Table of Contents
1. [Objectives of the Project](#1-objectives-of-the-project)
2. [Repository Governance Strategy Adopted](#2-repository-governance-strategy-adopted)
3. [Role-Based Access Control (RBAC) Implementation](#3-role-based-access-control-rbac-implementation)
4. [Branching Strategy Used for Media Pipeline Management](#4-branching-strategy-used-for-media-pipeline-management)
5. [Git LFS Concepts for Handling Large Media Files](#5-git-lfs-concepts-for-handling-large-media-files)
6. [Cloud Storage Architecture & Secure Sharing Strategy](#6-cloud-storage-architecture--secure-sharing-strategy)
7. [File Versioning, Rollback, Backup, and Disaster Recovery Planning](#7-file-versioning-rollback-backup-and-disaster-recovery-planning)
8. [Compliance and Data Privacy Considerations](#8-compliance-and-data-privacy-considerations)
9. [Threat Modelling for Media and Game Applications](#9-threat-modelling-for-media-and-game-applications)
10. [Source Code and Digital Asset Protection Mechanisms](#10-source-code-and-digital-asset-protection-mechanisms)
11. [Multi-Factor Authentication (MFA) Implementation](#11-multi-factor-authentication-mfa-implementation)
12. [Secure Authentication Practices](#12-secure-authentication-practices)
13. [Digital Watermarking Concepts](#13-digital-watermarking-concepts)

---

## 1. Objectives of the Project

The modern Game Development and Visual Effects (VFX) industries are characterized by massive multidisciplinary teams, high-velocity iteration, and the continuous generation of petabytes of proprietary binary assets. Managing code, high-resolution textures, 3D meshes, simulations, and cinematic audio requires an infrastructure that transcends basic version control.

The core objectives of this project are:
1. **Establish Enterprise Repository Governance:** Implement a structured collaborative environment in GitHub with standardized folder hierarchies, issue triage templates, and automated review gates.
2. **Implement Binary Asset Lifecycle Management:** Deploy Git Large File Storage (Git LFS) alongside cloud storage solutions to eliminate repository bloat while preserving full historical traceability.
3. **Architect Resilient Cloud Storage & Backup Workflows:** Design a multi-tiered hybrid storage topology incorporating local artist caching, active cloud synchronization (Hot Tier), and automated archive lifecycle policies (Cold/Glacier Tier) obeying the 3-2-1 backup paradigm.
4. **Enforce Comprehensive Digital Asset Protection:** Formulate a STRIDE-based threat model, enforce strict Multi-Factor Authentication (MFA) and Role-Based Access Control (RBAC), and deploy invisible and visible digital watermarking systems to detect and trace intellectual property leaks.

---

## 2. Repository Governance Strategy Adopted

Repository governance defines the rules, conventions, and operational workflows that regulate how team members interact with the project codebase and digital assets. 

### Key Pillars of the Adopted Governance Model:
* **Standardized Folder Taxonomy:** The repository structure strictly isolates source code, DCC tool files, binary assets, and documentation.
* **Automated Linting and Validation:** Pre-commit hooks verify that no uncommitted temporary files (`.blend1`, `.spp.bak`, cache folders) or credentials (`.env`, `.pem`) enter the commit history.
* **Pull Request (PR) Quality Gates:** Direct commits to core branches (`main`, `development`) are restricted. Merges require at least one verified peer review and passing automated technical checklist audits.
* **Structured Issue Tracking:** Development tasks, bugs, and artist submissions must follow standardized markdown templates to capture environment specs, reproductive steps, and technical budgets.

---

## 3. Role-Based Access Control (RBAC) Implementation

In collaborative studio environments, granting indiscriminate administrative or write privileges introduces severe operational risks, including accidental file deletions, rogue branch merges, and credential exposure. 

We implement a least-privilege Role-Based Access Control (RBAC) model across four functional tiers:

```
+-------------------------------------------------------------------------+
|                  ORGANIZATIONAL ROLES & ACCESS MATRIX                   |
+-------------------+-----------------+-----------------------------------+
| Role              | Access Tier     | Assigned Responsibilities         |
+-------------------+-----------------+-----------------------------------+
| Project Lead / TD | Administrator   | Branch protection rules, repo     |
|                   |                 | settings, secrets, audit logs.    |
+-------------------+-----------------+-----------------------------------+
| Senior Developer  | Maintainer      | Code & asset review approval,     |
| & Pipeline TD     |                 | LFS quota management, PR merging. |
+-------------------+-----------------+-----------------------------------+
| 3D Artists /      | Contributor     | Feature/asset branch creation,    |
| Animators         | (Write)         | LFS asset commits, PR creation.   |
+-------------------+-----------------+-----------------------------------+
| QA Testers /      | Reporter        | Bug reporting, issue tracking,    |
| Audio Contractors | (Triage / Read) | documentation review.             |
+-------------------+-----------------+-----------------------------------+
```

### GitHub RBAC Policy Configuration:
1. **Base Permissions:** Set to `Read` for all organization members.
2. **Team Allocations:** Team groups (`art-team`, `dev-team`, `qa-team`) map members directly to their respective privileges.
3. **Temporary Contractor Isolation:** External sound or VFX contractors are provisioned with repository-scoped, time-limited outside collaborator tokens with write access confined strictly to their dedicated feature branch.

---

## 4. Branching Strategy Used for Media Pipeline Management

Because game engines and VFX render pipelines can break when incompatible assets are checked in, our branching strategy adopts an adapted **GitFlow Pipeline** designed for high-asset churn.

```
[main] (Production / Milestones / Golden Master)
   ▲
   │ (Protected PR: Requires 2 Approvals, QA Signoff, Signed Commits)
   │
[development] (Nightly Integration / Shared Staging)
   ▲
   ├──────────────────────────────┬──────────────────────────────┐
   │                              │                              │
[feature/hero-rig]      [asset/dungeon-props]           [fix/shader-seam]
(DCC Rigging & Weights) (3D Meshes & 4K PBR)          (Normal map artifact)
```

### Operational Rules:
1. **`main` Branch:** Always represents release-ready or milestone builds (Alpha, Beta, Gold Master). Direct pushes are strictly forbidden.
2. **`development` Branch:** Serves as the central staging ground where artists and engineers integrate assets. Automated daily/nightly builds pull from this branch.
3. **`feature/*` & `asset/*` Branches:** Short-lived branches created by individual artists or programmers. Naming follows `<type>/<task-description>` (e.g., `asset/forest-props`, `feature/inventory-ui`).
4. **Release & Hotfix Branches:** Triggered for milestone stabilization or critical production bugs.

---

## 5. Git LFS Concepts for Handling Large Media Files

### The Problem with Native Git for Binary Assets
Git was inherently architected for plain-text source code using delta compression (storing differences between file revisions). However, media assets—such as 4K EXR textures, Maya `.mb` scenes, Blender `.blend` files, and uncompressed `.wav` audio—are pre-compressed or high-entropy binaries. Small edits in a binary file cause the entire file to be stored anew in the `.git` packfile history, causing exponential repository bloat and rendering `git clone` prohibitively slow.

### How Git LFS Solves the Problem
Git Large File Storage (Git LFS) replaces large binary files inside the Git tree with tiny, lightweight **text pointers** (typically ~130 bytes), while storing the actual multi-gigabyte binary payload on a dedicated LFS object server (e.g., AWS S3 or GitHub LFS storage).

```
+-------------------------------------------------------------+
|                      GIT LFS POINTER                        |
+-------------------------------------------------------------+
| version https://git-lfs.github.com/spec/v1                  |
| oid sha256:7b42f88d927c44e99f01e1d0092...                    |
| size 158492048                                              |
+-------------------------------------------------------------+
```

### Git LFS Implementation in this Repository:
The `.gitattributes` file explicitly captures all media formats:
```ini
*.fbx filter=lfs diff=lfs merge=lfs -text
*.obj filter=lfs diff=lfs merge=lfs -text
*.blend filter=lfs diff=lfs merge=lfs -text
*.exr filter=lfs diff=lfs merge=lfs -text
*.psd filter=lfs diff=lfs merge=lfs -text
*.wav filter=lfs diff=lfs merge=lfs -text
```
Whenever an artist commits a `.fbx` file:
1. Git computes the SHA-256 hash.
2. Git LFS transfers the binary directly to the LFS server.
3. The commit contains only the 130-byte pointer, keeping clones instantaneous.

---

## 6. Cloud Storage Architecture & Secure Sharing Strategy

While Git LFS manages assets linked directly to engine commits, raw uncompressed capture footage, photogrammetry scans, simulation caches, and finished render sequences exceed repository storage limits. 

We architect a three-tiered hybrid cloud storage topology:

```
[Local Artist Workstation]
        │  (High-speed 10GbE LAN)
        ▼
[On-Premises High-Performance NAS Cache]
        │
        │  (Encrypted TLS 1.3 Synchronization / AWS S3 CLI)
        ▼
+---------------------------------------------------------------------+
|                    CLOUD STORAGE TIERING (AWS)                      |
+---------------------------------------------------------------------+
|  TIER 1: S3 STANDARD (Hot Tier)                                     |
|  • Active project assets, current sprint textures, engine builds    |
|  • Millisecond latency, continuous replication                      |
+---------------------------------------------------------------------+
        │
        │  (Lifecycle Policy: 60 Days Inactivity)
        ▼
+---------------------------------------------------------------------+
|  TIER 2: S3 STANDARD-INFREQUENT ACCESS (Warm Tier)                 |
|  • Completed episode assets, prior sprint milestone renders         |
|  • Lower storage cost, immediate access upon demand                 |
+---------------------------------------------------------------------+
        │
        │  (Lifecycle Policy: 180 Days Inactivity)
        ▼
+---------------------------------------------------------------------+
|  TIER 3: S3 GLACIER FLEXIBLE / DEEP ARCHIVE (Cold Tier)              |
|  • Raw camera footage, simulation caches (.vdb), final gold masters |
|  • Ultra-low cost ($0.00099/GB/month), 3-5 hour retrieval SLA       |
+---------------------------------------------------------------------+
```

### Secure Sharing Strategy:
* **Pre-signed URLs:** Time-limited (e.g., 60 minutes) cryptographic links for external review stakeholders.
* **IAM Least Privilege:** Role-based access keys for automated build and render agents.
* **Server-Side Encryption:** Mandatory AES-256 / AWS KMS encryption for all buckets at rest.

---

## 7. File Versioning, Rollback, Backup, and Disaster Recovery Planning

### File Versioning and Semantic Tagging
Every asset release milestone is tagged in Git using Semantic Versioning (`vMAJOR.MINOR.PATCH`, e.g., `v1.0.0-alpha`). Within DCC tools (Blender/Maya), files adhere to iterative nomenclature: `SM_HeroArmor_LOD0_v004.fbx`.

### Rollback Strategy (Practical & Conceptual)
If a defective asset or corrupt shader is pushed to `development`:
* **Non-destructive Rollback (`git revert`):**
  ```bash
  git revert <commit-hash>
  git push origin development
  ```
  Creates a new commit reversing the changes without rewriting shared commit history.
* **Emergency LFS Asset Rollback:**
  ```bash
  git checkout <previous-stable-commit> -- assets/models/hero_character.fbx
  git commit -m "Rollback: Restored v003 character mesh due to UV seam artifact"
  git push origin development
  ```

### 3-2-1 Disaster Recovery Architecture
* **3 Copies of Data:** Primary local workstation, on-premises NAS, and Cloud object storage.
* **2 Different Media Types:** NVMe/SSD local storage and Cloud S3 object storage.
* **1 Offsite Replica:** Geographically isolated AWS S3 bucket in another availability zone.
* **Recovery Point Objective (RPO):** Maximum 1 hour of work loss.
* **Recovery Time Objective (RTO):** Pipeline operational within 4 hours post-disaster.

---

## 8. Compliance and Data Privacy Considerations

Media and game development workflows must comply with international privacy regulations and entertainment industry security guidelines:

1. **General Data Protection Regulation (GDPR) & CCPA:** Player telemetry data, voice recordings, and beta-tester information must be segregated from artist asset repositories. No Personally Identifiable Information (PII) is committed to version control.
2. **Motion Picture Association (MPA) Content Security Best Practices:**
   * Air-gapped or DMZ-isolated render nodes.
   * Disabling USB mass-storage on artist workstations.
   * Complete audit trails tracking who downloaded pre-release dailies.
3. **Non-Disclosure Agreement (NDA) IP Segregation:** Sub-contractors only receive read access to submodules relevant to their specific contracted deliverable.

---

## 9. Threat Modelling for Media and Game Applications

We perform a **STRIDE** threat model analysis customized for game production environments:

```
+--------------------+--------------------------------+---------------------------------+
| STRIDE Category    | Specific Media Threat          | Implemented Countermeasure      |
+--------------------+--------------------------------+---------------------------------+
| **S**poofing       | Impersonating an artist to     | SSH key verification, mandatory |
|                    | push malicious dependencies    | GPG commit signing, 2FA/MFA.    |
+--------------------+--------------------------------+---------------------------------+
| **T**ampering      | Modifying source scripts or 3D | Branch protection, PR review    |
|                    | assets with hidden exploits    | approvals, SHA-256 checksums.   |
+--------------------+--------------------------------+---------------------------------+
| **R**epudiation    | Artist denies leaking an       | Tamper-proof Git audit logs and |
|                    | unreleased cinematic trailer   | invisible digital watermarks.   |
+--------------------+--------------------------------+---------------------------------+
| **I**nformation    | Pre-release game asset or plot | AES-256 cloud encryption, RBAC, |
| Disclosure         | leak to public forums          | pre-signed expiring links.      |
+--------------------+--------------------------------+---------------------------------+
| **D**enial of      | Ransomware encrypting shared   | Immutable S3 Object Lock, air-  |
| Service (DoS)      | studio NAS render cache        | gapped offsite backup snapshots.|
+--------------------+--------------------------------+---------------------------------+
| **E**levation of   | Freelancer gaining repository  | Least-privilege IAM policies,   |
| Privilege          | administrative settings        | outside-collaborator isolation. |
+--------------------+--------------------------------+---------------------------------+
```

---

## 10. Source Code and Digital Asset Protection Mechanisms

Protecting intellectual property requires defense-in-depth across the entire asset pipeline:

1. **GitHub Secret Scanning & Push Protection:** Blocks commits containing hardcoded API keys, private certificates, or cloud access tokens before they leave the artist's computer.
2. **GPG Commit Signing:** Guarantees that every commit merged into `main` originates cryptographically from an authenticated developer workstation.
3. **Binary DRM and Packaging:** Production builds compile game code into obfuscated binaries and pack media assets into encrypted archives (e.g., Unreal `.pak` / `.utoc` files with AES-256 encryption keys).
4. **Environment Configuration Protection:** Configuration files and secrets are injected strictly via CI/CD environment secrets, keeping repositories credential-free.

---

## 11. Multi-Factor Authentication (MFA) Implementation

Passwords alone are inadequate against phishing and credential stuffing attacks. In our repository governance:
* **Organization-Wide MFA Enforcement:** All contributors are mandated to configure Multi-Factor Authentication before accessing repository contents.
* **Authentication Factors Utilized:**
  * **Primary Factor:** Hardware-backed SSH Key (`ed25519`) or OAuth 2.0 Web Authentication.
  * **Secondary Factor:** Time-based One-Time Password (TOTP) via authenticator apps (e.g., Google Authenticator, 1Password) or FIDO2/WebAuthn hardware security keys (YubiKey).
* **Automated Removal:** Accounts that disable 2FA are automatically evicted from repository write teams by GitHub enterprise compliance policy.

---

## 12. Secure Authentication Practices

To prevent unauthorized shell and pipeline access:
1. **Deprecation of Password Authentication:** Direct HTTPS password pushes are disabled. Developers authenticate solely via SSH keys or Fine-Grained Personal Access Tokens (PAT).
2. **Short-Lived Fine-Grained Personal Access Tokens:** Tokens are scoped strictly to individual repositories with minimum permissions (e.g., `contents:read`, `issues:write`) and expire every 30 to 90 days.
3. **SSH Key Hardening:** Recommended cryptographic standard is `ssh-ed25519`, offering superior side-channel attack resistance compared to deprecated RSA keys.

---

## 13. Digital Watermarking Concepts

Digital watermarking is the practice of embedding identifiable information into media signals to establish copyright, verify authenticity, and trace leak sources.

### Comparison of Watermarking Techniques
| Dimension | Visible Watermarking (Burn-In) | Invisible / Forensic Watermarking |
| :--- | :--- | :--- |
| **Primary Goal** | Visual deterrence against leaks | Forensic traceability after a leak occurs |
| **Human Perception** | Easily noticeable (e.g., timestamp, artist name overlay) | Imperceptible to the naked eye |
| **Resilience** | Can be cropped or blurred if not placed strategically | Resists cropping, downsampling, and color grading |
| **Implementation** | Alpha-composited typography across review frames | LSB steganography, DCT/DWT frequency manipulation, or metadata injection |
| **Production Use Case** | Daily review reels, screener cuts for executives | Pre-release alpha gameplay builds, NDA review copies |

### Practical Demonstration in this Repository:
The included automation script (`scripts/watermark_tool.py`) demonstrates:
* **Visible Watermarking:** Renders a semi-transparent, diagonal verification stamp (`CONFIDENTIAL - MEHAK JOON`) across texture and render frames.
* **Forensic Metadata Injection:** Embeds tracking identifiers (`Watermark-Forensic-ID`, `Authorized-Recipient`) into image header chunks, allowing forensic investigators to pinpoint the exact leak origin.

---

## Summary & Conclusion
By combining rigorous repository governance, Git LFS asset handling, a 3-2-1 hybrid cloud architecture, STRIDE threat mitigation, and digital watermarking, this project demonstrates an enterprise-grade, secure, and highly scalable pipeline for Game Development and VFX production.
