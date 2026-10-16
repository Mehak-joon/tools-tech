"""
Pipeline Governance & Repository Validator
Subject: Tools & Techniques of Game and VFX-II (BCA MIT)
Author: Mehak Joon
Task 1: GitHub Repository Governance & Collaboration

Description:
This script validates repository governance rules before artists or developers
can merge assets or code into staging/production branches:
1. Verifies mandatory repository folder taxonomy.
2. Enforces studio naming conventions (e.g., SM_ for meshes, T_ for textures).
3. Ensures high-density binary files are registered in .gitattributes (Git LFS).
4. Detects unwanted DCC autosave/cache files (.blend1, .tmp, .spp.bak).
"""

import os
import sys

# Studio Asset Naming Standards
NAMING_CONVENTIONS = {
    ".fbx": ["SM_", "SK_"],         # Static Mesh / Skeletal Mesh
    ".obj": ["SM_"],
    ".blend": ["SCENE_", "PROP_"],
    ".png": ["T_", "TEX_"],          # Texture map
    ".exr": ["HDR_", "TEX_"],
    ".wav": ["SFX_", "BGM_", "VO_"], # Sound FX / Background Music / Voiceover
}

# Forbidden Junk / Cache Extensions
FORBIDDEN_EXTENSIONS = [
    ".blend1", ".blend2", ".tmp", ".spp.bak", ".sbsar.bak",
    ".autosave", ".crash", ".stackdump", "Thumbs.db"
]

def check_folder_structure(repo_root):
    """Verifies that the mandatory pipeline directory taxonomy exists."""
    print("\n[+] Checking Repository Folder Structure...")
    required_dirs = [
        "Task_1_Repository_Governance",
        "Task_2_Media_Asset_Management",
        "Task_3_Media_Security",
        ".github/ISSUE_TEMPLATE",
        "assets/models",
        "assets/textures",
        "assets/audio",
        "assets/vfx"
    ]
    all_passed = True
    for d in required_dirs:
        path = os.path.join(repo_root, d)
        if os.path.exists(path):
            print(f"  [✓] Found: {d}")
        else:
            print(f"  [✗] MISSING: {d}")
            all_passed = False
    return all_passed

def check_git_lfs_attributes(repo_root):
    """Verifies that .gitattributes is configured for Git LFS tracking."""
    print("\n[+] Validating Git LFS Tracking Rules (.gitattributes)...")
    gitattributes_path = os.path.join(repo_root, ".gitattributes")
    if not os.path.exists(gitattributes_path):
        print("  [✗] .gitattributes file not found in repository root!")
        return False
    
    with open(gitattributes_path, "r", encoding="utf-8") as f:
        content = f.read()

    required_lfs_types = ["*.fbx", "*.blend", "*.exr", "*.psd", "*.wav"]
    all_tracked = True
    for ext in required_lfs_types:
        if ext in content and "filter=lfs" in content:
            print(f"  [✓] LFS tracking confirmed for: {ext}")
        else:
            print(f"  [!] Missing LFS tracking pattern for: {ext}")
            all_tracked = False
    return all_tracked

def scan_assets(repo_root):
    """Scans all assets for naming convention compliance and cache junk."""
    print("\n[+] Auditing Asset Directory for Pipeline Governance...")
    assets_dir = os.path.join(repo_root, "assets")
    if not os.path.exists(assets_dir):
        print("  [!] assets/ directory not found.")
        return True

    warnings = 0
    scanned_count = 0

    for root, _, files in os.walk(assets_dir):
        for file in files:
            scanned_count += 1
            file_lower = file.lower()
            _, ext = os.path.splitext(file_lower)

            # Check for forbidden files
            if any(file_lower.endswith(bad) for bad in FORBIDDEN_EXTENSIONS):
                print(f"  [✗] VIOLATION: Forbidden temporary/cache file detected: {file}")
                warnings += 1

            # Check naming conventions for known media extensions
            if ext in NAMING_CONVENTIONS:
                valid_prefixes = NAMING_CONVENTIONS[ext]
                has_valid_prefix = any(file.startswith(prefix) for prefix in valid_prefixes)
                if not has_valid_prefix:
                    print(f"  [!] CONVENTION WARNING: '{file}' does not start with standard prefix {valid_prefixes}")
                    warnings += 1

    print(f"\n[i] Asset Audit Complete: Scanned {scanned_count} files with {warnings} governance warnings.")
    return warnings == 0

def run_governance_audit():
    print("=" * 65)
    print(" Game & VFX Pipeline Repository Governance Validator")
    print(" Subject: Tools & Techniques of Game and VFX-II | Mehak Joon")
    print("=" * 65)

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    s1 = check_folder_structure(repo_root)
    s2 = check_git_lfs_attributes(repo_root)
    s3 = scan_assets(repo_root)

    print("\n" + "=" * 65)
    if s1 and s2 and s3:
        print(" [✓] PIPELINE GOVERNANCE CHECK: ALL CHECKS PASSED SUCCESSFULLY")
    else:
        print(" [!] PIPELINE GOVERNANCE CHECK: COMPLETED WITH WARNINGS / ADVICE")
    print("=" * 65)

if __name__ == "__main__":
    run_governance_audit()
