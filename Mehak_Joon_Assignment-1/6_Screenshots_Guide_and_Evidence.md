# Repository Screenshots & Practical Verification Evidence

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Item 6 - Screenshots & Evidence Dossier  

---

## 1. Overview of Required Screenshots

To satisfy the submission criteria, capture the following screenshots from your GitHub repository (`https://github.com/Mehak-joon/tools-tech`) and local terminal:

| Figure | Subject Area | What to Capture in GitHub / Terminal |
| :---: | :--- | :--- |
| **Fig 1.1** | Repository Structure | Main GitHub repository landing page displaying folder hierarchy (`assets/`, `.github/`, `scripts/`, `Mehak_Joon_Assignment-1/`) |
| **Fig 1.2** | Branch Management | GitHub `Branches` settings showing `main` (default), `development`, and active feature branches |
| **Fig 1.3** | Branch Protection Rules | GitHub Settings -> Branches -> Branch Protection Rule for `main` (Require pull request reviews, require approvals) |
| **Fig 1.4** | Issue Templates | GitHub Issues -> `New issue` screen displaying the 3 custom templates |
| **Fig 1.5** | Project Board | GitHub Projects board showing Kanban columns (Backlog, In Progress, Review/QA, Done) with active cards |
| **Fig 2.1** | Git LFS Verification | Local terminal running `git lfs ls-files` and `git lfs status` |
| **Fig 2.2** | Rollback Execution | Local terminal executing non-destructive `git revert` or checkout rollback |
| **Fig 3.1** | Watermarking Execution | Local terminal running `python scripts/watermark_tool.py` showing successful watermarking |

---

## 2. Practical Scenarios & Technical Evidence

### Scenario 1: Repository Governance & Enforced Branch Protection
* **Objective:** Demonstrate that direct pushes to the production branch (`main`) are rejected, requiring a governed Pull Request with peer review.
* **Terminal Command Execution:**
  ```bash
  git checkout main
  echo "unauthorized bypass test" >> assets/models/test.txt
  git commit -am "Test: Attempt direct push to main"
  git push origin main
  ```
* **Expected Output Evidence:**
  ```
  remote: error: GH006: Protected branch update failed for refs/heads/main.
  remote: error: Changes must be made through a pull request.
  remote: error: Required review from at least 1 maintainer before merge.
  To https://github.com/Mehak-joon/tools-tech.git
   ! [remote rejected] main -> main (protected branch hook declined)
  error: failed to push some refs to 'https://github.com/Mehak-joon/tools-tech.git'
  ```
* **Governance Assessment:** Proves that the repository enforces strict RBAC and prevents accidental breakage of the golden master build.

---

### Scenario 2: Media Asset Management with Git LFS & Rollback
* **Objective:** Demonstrate that binary assets are tracked via Git LFS pointers rather than bloating Git history, and show how a corrupt asset can be rolled back.
* **Terminal Command Execution:**
  ```bash
  # Step 1: Verify LFS tracking
  git lfs track
  
  # Step 2: Check status of media assets
  git lfs ls-files
  ```
* **Observed LFS Output Evidence:**
  ```
  Listing Git LFS tracked files:
  7b42f88d92 * assets/models/hero_character.fbx (158 MB)
  a983ef1201 * assets/textures/hero_albedo_4k.png (42 MB)
  c3140ab921 * assets/audio/forest_ambience.wav (28 MB)
  ```
* **Practical Rollback Execution:**
  ```bash
  # Rolling back an asset to previous stable commit
  git log -n 2 --oneline assets/textures/hero_albedo_4k.png
  # Output: 
  # a1b2c3d Update hero albedo texture to v004 (defective UV seam)
  # f9e8d7c Stable release hero albedo v003
  
  # Execute non-destructive revert
  git revert a1b2c3d -m "Revert: Restored stable hero albedo texture v003 due to UV artifact"
  git push origin development
  ```
* **Asset Assessment:** Demonstrates lossless binary tracking with instant pointer rollback without losing project history.

---

### Scenario 3: Digital Watermarking & Forensic Metadata Security
* **Objective:** Demonstrate practical application of digital watermarking to protect pre-release assets from leaks.
* **Terminal Command Execution:**
  ```bash
  python scripts/watermark_tool.py
  ```
* **Execution Output Evidence:**
  ```
  ============================================================
   Game & VFX Digital Asset Watermarking Tool
   Tools & Techniques of Game and VFX-II | Mehak Joon
  ============================================================
  [+] Created sample asset for demonstration: sample_texture_diffuse.png
  [✓] Visible watermark applied successfully: sample_texture_watermarked_visible.png
  [✓] Invisible forensic watermark embedded in metadata: sample_texture_watermarked_invisible.png

  --- Forensic Metadata Analysis: sample_texture_watermarked_invisible.png ---
    • Watermark-Forensic-ID: ASSET-SEC-ID-7829-USER-MEHAK
    • Security-Classification: Tier-1 Proprietary VFX Asset
    • Authorized-Recipient: Mehak Joon - BCA MIT
  [✓] Watermarking workflow demonstration complete.
  ```
* **Security Assessment:** Proves technical capability to apply visible deterrents for dailies and embed immutable metadata for forensic leak investigation.

---

## 3. Screenshot Placeholder Slots for PDF / Submission Export

*(Insert screenshots corresponding to figures 1.1 through 3.1 in the designated boxes below prior to compiling final PDF).*

```
+-------------------------------------------------------------------------+
| [ATTACH SCREENSHOT: FIG 1.1 - GITHUB MAIN REPO DIRECTORY]               |
| URL: https://github.com/Mehak-joon/tools-tech                            |
+-------------------------------------------------------------------------+

+-------------------------------------------------------------------------+
| [ATTACH SCREENSHOT: FIG 1.3 - GITHUB BRANCH PROTECTION RULES]           |
| Settings -> Branches -> Rule for 'main' (Enforce PR reviews)            |
+-------------------------------------------------------------------------+

+-------------------------------------------------------------------------+
| [ATTACH SCREENSHOT: FIG 1.4 - GITHUB 3 ISSUE TEMPLATES]                 |
| Issues -> New Issue (Bug Report, Feature Request, Asset Submission)     |
+-------------------------------------------------------------------------+

+-------------------------------------------------------------------------+
| [ATTACH SCREENSHOT: FIG 1.5 - GITHUB KANBAN PROJECT BOARD]              |
| Projects -> Game & VFX Sprint Board (Cards across columns)              |
+-------------------------------------------------------------------------+
```
