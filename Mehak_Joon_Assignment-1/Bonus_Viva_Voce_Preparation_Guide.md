# Viva Voce Preparation Guide (10 Questions & Model Answers)

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Student Name:** Mehak Joon  
**Evaluation:** Task 4 - Viva Presentation (Comprehensive Question & Answer Bank)  

---

### Question 1: Explain the repository governance model implemented in your project.
**Model Answer:**  
> "Our repository governance model establishes structured control over how code and binary assets are introduced, tested, and merged. It relies on four core pillars:
> 1. **Standardized Folder Taxonomy:** Clean separation of assets (`models`, `textures`, `audio`, `vfx`), pipeline scripts, and documentation.
> 2. **Pull Request Quality Gates:** Direct commits to `main` and `development` are blocked using GitHub branch protection rules. Merges require at least one approved peer review and passing checklists.
> 3. **Structured Issue Templates:** Standardized templates for bug reports, feature requests, and 3D asset submissions to enforce technical budgets (polycount, power-of-two textures).
> 4. **Automated Hygiene:** `.gitignore` excludes temporary engine caches, and pre-commit checks prevent secrets or uncompressed cache files from entering the Git tree."

---

### Question 2: Demonstrate Role-Based Access Control (RBAC) in GitHub.
**Model Answer:**  
> "RBAC enforces the principle of least privilege. In our GitHub repository, we configure four distinct permission tiers:
> * **Admin (Lead Technical Director):** Full administrative control, managing branch protection rules, repository secrets, and member access.
> * **Maintainer (Senior Devs / Pipeline TDs):** Reviewing and approving Pull Requests, managing Git LFS storage thresholds, and managing project milestones.
> * **Contributor / Write (3D Artists & Animators):** Pushing to dedicated `feature/*` and `asset/*` branches, committing LFS assets, and opening PRs. Direct pushes to `main` are blocked.
> * **Triage / Read (QA Testers & Sound Contractors):** Reading code, opening issues, and validating test builds without write access to production branches."

---

### Question 3: Describe your branching strategy and project management workflow.
**Model Answer:**  
> "We use an adapted **GitFlow model** tailored for media production:
> * `main` represents production-ready milestone builds (Alpha, Beta, Golden Master).
> * `development` is the nightly integration and staging branch.
> * Individual developers and artists work in short-lived branches prefixed by task type (e.g., `feature/character-rig`, `asset/dungeon-props`, `fix/shader-seam`).
> For project management, we use a **GitHub Projects Kanban Board** with four columns: *Backlog*, *In Progress*, *Review/QA*, and *Done*. Each issue card is tagged with labels and linked to pull requests so that issues close automatically when a PR merges."

---

### Question 4: Explain the use of Git LFS and media asset management techniques.
**Model Answer:**  
> "Standard Git is designed for plain text and uses delta compression. If you commit a 100 MB 3D model or 4K texture and make a small change, Git stores the entire new 100 MB binary in the `.git` directory, causing massive repository bloat.
> **Git LFS** solves this by replacing binary assets inside the Git tree with a lightweight 130-byte text pointer containing a SHA-256 hash (`oid`) and file size. The actual heavy binary is uploaded to a dedicated LFS object store.
> In our repository, `.gitattributes` tracks all media formats (`.fbx`, `.obj`, `.blend`, `.exr`, `.png`, `.wav`). Team members can clone instantaneously, and rolling back a corrupted asset is as simple as reverting the pointer commit."

---

### Question 5: Justify your cloud storage architecture and backup strategy.
**Model Answer:**  
> "A Game/VFX pipeline generates terabytes of data. Keeping everything in hot cloud storage is financially unviable. We designed a **Hybrid Multi-Tier Architecture**:
> * **Local Edge NAS (NVMe):** Provides ultra-fast 10 GbE local bandwidth for daily artist editing.
> * **AWS S3 Standard (Hot Tier):** High-throughput storage for active sprint assets and automated build machines.
> * **AWS S3 Standard-IA & Glacier Deep Archive:** Automated lifecycle policies transition assets idle for 60 days to Infrequent Access and 365 days to Deep Archive ($0.00099/GB/month), saving over **68% annually**.
> For backups, we follow the **3-2-1 rule**: 3 copies of data, across 2 different storage media types (local NVMe and Cloud Object Storage), with 1 offsite immutable replica protected by S3 Object Lock (WORM) against ransomware."

---

### Question 6: Explain secure authentication and Multi-Factor Authentication (MFA).
**Model Answer:**  
> "Password authentication over HTTPS has been deprecated by GitHub due to vulnerabilities to credential stuffing and phishing.
> We implement:
> 1. **Mandatory Organization-Wide MFA:** Requires TOTP authenticator apps or FIDO2 hardware keys (YubiKey) for all account logins.
> 2. **Cryptographic SSH Keys:** Artists and developers interact with Git via hardened `ssh-ed25519` key pairs.
> 3. **GPG Commit Signing:** Commits are cryptographically signed with private GPG keys so GitHub displays the 'Verified' badge, ensuring that committed code cannot be spoofed."

---

### Question 7: Demonstrate knowledge of digital watermarking and source code protection.
**Model Answer:**  
> "Digital watermarking protects pre-release assets from unauthorized leaks:
> * **Visible Watermarks (Burn-Ins):** Semi-transparent visual stamps (e.g., artist name, timestamp, SMPTE timecode) rendered diagonally across daily review renders to deter leaking.
> * **Invisible / Forensic Watermarks:** Cryptographic tracking payloads embedded imperceptibly into frequency sub-bands (DWT/DCT) or metadata headers. If an asset leaks online, the payload reveals the exact workstation and user responsible.
> In our project, [`scripts/watermark_tool.py`](file:///c:/Users/hp/Desktop/tools-tech/scripts/watermark_tool.py) demonstrates both visible burn-in compositing and invisible metadata steganography.
> For source code protection, we enforce secret scanning, branch protection, and binary obfuscation."

---

### Question 8: Analyze threat models and common cyber attacks in media applications.
**Model Answer:**  
> "We applied the **STRIDE** methodology to analyze attack vectors:
> * **Spoofing & Tampering:** Mitigated by MFA, SSH keys, GPG signing, and branch protection.
> * **Information Disclosure:** Mitigated by AES-256 KMS encryption and short-lived pre-signed URLs.
> * **Denial of Service & Ransomware:** Addressed by S3 Immutable Object Lock vaults.
> The top cyber attacks targeting studios today are **Ransomware extortion** (e.g., Insomniac Games leak), **Credential Stuffing**, and **Third-Party Contractor Leaks**. Our defense-in-depth model isolates contractors and enforces automated audit logs."

---

### Question 9: Discuss compliance, privacy, and industry best practices.
**Model Answer:**  
> "Our pipeline complies with:
> * **Motion Picture Association (MPA) Content Security Guidelines:** Requiring network isolation for production assets, audit trails for file downloads, and watermarked dailies.
> * **Data Privacy (GDPR / CCPA):** Strictly barring player telemetry or personal data (PII) from entering art repositories.
> * **Studio NDAs:** Sub-contractors receive repository access strictly limited to their relevant submodules and feature branches, terminating immediately upon milestone completion."

---

### Question 10: How do you handle accidental asset deletion or pipeline failure during a live sprint?
**Model Answer:**  
> "We have defined strict Recovery Time Objectives (RTO = 4 hours) and Recovery Point Objectives (RPO = 1 hour):
> * If an artist pushes a corrupted shader or broken FBX, we execute a non-destructive `git revert <commit-hash>` to immediately restore the last working pointer without rewriting branch history.
> * If a branch is accidentally deleted, we use `git reflog` to locate the HEAD commit and restore the branch in seconds.
> * If local hardware suffers total failure, our offsite S3 immutable replica can be restored within 3.5 hours, keeping data loss under 1 hour."
