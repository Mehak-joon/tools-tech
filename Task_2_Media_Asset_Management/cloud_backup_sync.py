"""
Cloud Asset Storage, Lifecycle Tiering & 3-2-1 Backup Simulator
Subject: Tools & Techniques of Game and VFX-II (BCA MIT)
Author: Mehak Joon
Task 2: Media Asset Management & Cloud Storage

Description:
This script simulates the complete Game & VFX cloud media pipeline:
1. Git LFS Pointer & Hash Generation (SHA-256 asset checksums).
2. Multi-Tier Cloud Storage Simulation (Hot S3 -> Warm S3-IA -> Cold Glacier).
3. Real-Time Cloud Storage Cost Optimization Calculator.
4. 3-2-1 Backup Verification & Automated Disaster Recovery Simulator.
"""

import os
import hashlib
import time

# AWS S3 Storage Pricing (USD per GB / Month)
PRICING_PER_GB = {
    "S3_Standard_Hot": 0.023,
    "S3_Standard_IA_Warm": 0.0125,
    "S3_Glacier_Deep_Archive_Cold": 0.00099
}

def compute_sha256(filepath):
    """Computes SHA-256 hash, mimicking Git LFS oid pointer calculation."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return f"ERROR: {e}"

def simulate_git_lfs_tracking(repo_root):
    """Simulates how Git LFS tracks large binary assets with text pointers."""
    print("\n[+] 1. Git LFS Asset Ingestion & Pointer Generation:")
    print("-" * 65)
    assets_dir = os.path.join(repo_root, "assets")
    
    tracked_assets = []
    if os.path.exists(assets_dir):
        for root, _, files in os.walk(assets_dir):
            for file in files:
                if file == ".gitkeep":
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, repo_root)
                size_bytes = os.path.getsize(full_path)
                sha = compute_sha256(full_path)
                tracked_assets.append({
                    "path": rel_path,
                    "size_bytes": size_bytes,
                    "sha256": sha
                })
                print(f"  • Asset: {rel_path}")
                print(f"    Size: {size_bytes} bytes | LFS OID: sha256:{sha[:16]}...")
    
    if not tracked_assets:
        # Create virtual demo assets for simulation
        demo_assets = [
            {"path": "assets/models/SM_HeroCharacter_LOD0.fbx", "size_bytes": 158 * 1024 * 1024, "sha256": "7b42f88d927c44e99f01e1d0092..."},
            {"path": "assets/textures/T_Hero_Albedo_4K.png", "size_bytes": 42 * 1024 * 1024, "sha256": "a983ef12019b882c81720ea1901..."},
            {"path": "assets/audio/SFX_DragonRoar_Stereo.wav", "size_bytes": 28 * 1024 * 1024, "sha256": "c3140ab921a8849c99182312019..."}
        ]
        print("  [i] Simulating production assets currently tracked via Git LFS:")
        for a in demo_assets:
            print(f"  • Asset: {a['path']}")
            print(f"    Size: {a['size_bytes'] / (1024*1024):.1f} MB | LFS Pointer OID: sha256:{a['sha256']}")
        return demo_assets
    return tracked_assets

def calculate_cloud_cost_optimization(total_data_tb=100.0):
    """Calculates annual savings when using S3 Lifecycle policies vs unoptimized storage."""
    print(f"\n[+] 2. Cloud Storage Cost Optimization Model ({total_data_tb} TB Dataset):")
    print("-" * 65)
    
    total_gb = total_data_tb * 1024
    
    # Unoptimized: 100% in S3 Standard
    monthly_unoptimized = total_gb * PRICING_PER_GB["S3_Standard_Hot"]
    annual_unoptimized = monthly_unoptimized * 12

    # Optimized Tiering Distribution:
    # 15% Hot (Active sprint assets)
    # 25% Warm (Milestone builds in S3-IA)
    # 60% Cold (Deep Archive for raw footage, sims, gold masters)
    hot_gb = total_gb * 0.15
    warm_gb = total_gb * 0.25
    cold_gb = total_gb * 0.60

    cost_hot = hot_gb * PRICING_PER_GB["S3_Standard_Hot"]
    cost_warm = warm_gb * PRICING_PER_GB["S3_Standard_IA_Warm"]
    cost_cold = cold_gb * PRICING_PER_GB["S3_Glacier_Deep_Archive_Cold"]

    monthly_optimized = cost_hot + cost_warm + cost_cold
    annual_optimized = monthly_optimized * 12
    annual_savings = annual_unoptimized - annual_optimized
    savings_percent = (annual_savings / annual_unoptimized) * 100

    print(f"  • Unoptimized Monthly Cost (100% S3 Standard): ${monthly_unoptimized:,.2f} / month")
    print(f"  • Unoptimized Annual Bill:                     ${annual_unoptimized:,.2f} / year (~₹{annual_unoptimized * 83:,.0f})")
    print("\n  • Optimized Tiered Distribution:")
    print(f"    - Hot Tier (15 TB S3 Standard):             ${cost_hot:,.2f}/mo")
    print(f"    - Warm Tier (25 TB S3 Standard-IA):         ${cost_warm:,.2f}/mo")
    print(f"    - Cold Tier (60 TB Glacier Deep Archive):   ${cost_cold:,.2f}/mo")
    print(f"  • Optimized Monthly Total:                    ${monthly_optimized:,.2f} / month")
    print(f"  • Optimized Annual Total:                     ${annual_optimized:,.2f} / year (~₹{annual_optimized * 83:,.0f})")
    print("  " + "=" * 45)
    print(f"  [✓] NET ANNUAL SAVINGS:                      ${annual_savings:,.2f} / year ({savings_percent:.1f}% SAVED!)")
    print(f"      Estimated INR Savings:                   ~₹{annual_savings * 83:,.0f} per year")

def simulate_321_backup_recovery():
    """Demonstrates 3-2-1 backup verification and disaster recovery."""
    print("\n[+] 3. 3-2-1 Media Backup & Disaster Recovery Verification:")
    print("-" * 65)
    print("  [✓] COPY 1 (Primary Live):      Local NVMe Fast Storage Pool (RPO: 1 Hour)")
    print("  [✓] COPY 2 (Secondary Backup):  On-Premises ZFS Studio NAS Cache (Hourly Snapshot)")
    print("  [✓] COPY 3 (Offsite Immutable): AWS S3 Glacier Vault with Object Lock (WORM)")
    print("\n  [!] Simulating Disaster Recovery Drill: Total Local NAS Failure")
    print("  [>] Step 1: Detect hardware loss -> Trigger failover to standby mirror (10 mins)")
    print("  [>] Step 2: Authenticate to offsite AWS immutable S3 vault (15 mins)")
    print("  [>] Step 3: Stream Git LFS binary pointers to clean workstations (2 hrs)")
    print("  [✓] Total Recovery Time: 2h 25m (Well within Studio RTO limit of 4 Hours!)")

if __name__ == "__main__":
    print("=" * 65)
    print(" Media Asset Management & Cloud Backup Simulator")
    print(" Subject: Tools & Techniques of Game and VFX-II | Mehak Joon")
    print("=" * 65)
    
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    simulate_git_lfs_tracking(repo_root)
    calculate_cloud_cost_optimization(100.0)
    simulate_321_backup_recovery()
    
    print("\n" + "=" * 65)
    print(" [✓] Task 2 Media Management Simulation Completed Successfully")
    print("=" * 65)
