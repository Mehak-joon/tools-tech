# Git LFS & Rollback Step-by-Step Guide

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Task 2 - Practical Git LFS & Rollback Guide  

---

## 1. What is Git LFS?
Git LFS (Large File Storage) replaces heavy media assets (3D meshes, 4K textures, audio files) with lightweight pointer files (130 bytes).

### Inside a 130-byte LFS Pointer File:
```
version https://git-lfs.github.com/spec/v1
oid sha256:7b42f88d927c44e99f01e1d0092...
size 158492048
```
The pointer stays in Git; the 158 MB binary file is uploaded to the LFS server.

---

## 2. Essential Commands

```bash
# 1. Install Git LFS on your machine
git lfs install

# 2. Track a file type (creates or updates .gitattributes)
git lfs track "*.fbx"
git lfs track "*.png"

# 3. Check what file types are tracked
git lfs track

# 4. Check which files in the repository are tracked by LFS
git lfs ls-files
```

---

## 3. Practical Rollback Demonstration

### Scenario: Reverting a Corrupt 3D Asset
If an artist pushes an FBX file with a broken UV map or deformed rig:

```bash
# Step 1: Check the commit log of the asset
git log -n 3 --oneline assets/models/hero_character.fbx

# Step 2: Use git revert to create a non-destructive rollback commit
git revert <bad-commit-hash> -m "Revert: Restored stable character mesh due to UV issue"

# Step 3: Push the fix to staging
git push origin development
```
*Because `git revert` adds a new commit instead of rewriting history, all team members stay in sync safely.*
