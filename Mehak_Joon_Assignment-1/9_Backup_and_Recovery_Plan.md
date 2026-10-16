# Media Asset Backup & Disaster Recovery Plan

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Item 9 - Backup & Disaster Recovery Plan  

---

## 1. Executive Summary & Purpose

A single catastrophic data loss event (such as a NAS storage controller failure, ransomware outbreak, or accidental deletion of master project files) can cause millions of rupees in losses and delay release dates by months. 

This Disaster Recovery (DR) Plan establishes the operational protocols, automated scheduling, and recovery procedures required to protect all Game & VFX production data.

---

## 2. Key Recovery Metrics

* **Recovery Point Objective (RPO):** **1 Hour**  
  * *Definition:* The maximum acceptable amount of data loss measured in time. In our pipeline, automated delta backups ensure no artist loses more than 1 hour of active work.
* **Recovery Time Objective (RTO):** **4 Hours**  
  * *Definition:* The maximum acceptable downtime to restore critical production services (Git repository, active S3 asset cache, and build machines) following a disaster.

---

## 3. The 3-2-1 Media Backup Architecture

We implement the internationally recognized **3-2-1 Backup Strategy** adapted for large media pipelines:

```
                                  [PRODUCTION DATA]
                             (Active Workstations / DCCs)
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
         [COPY 1: PRIMARY]                              [COPY 2: SECONDARY]
     High-Speed NVMe Studio NAS                    Direct Cloud Mirror (Hot S3)
   (Local On-Premises ZFS Pool)                  (Encrypted Object Storage - Tier 1)
                  │
                  ▼
         [COPY 3: OFFSITE & IMMUTABLE]
         AWS S3 Glacier Deep Archive
   (Cross-Region Isolated Vault with WORM Lock)
```

1. **3 Copies of Data:**
   * Copy 1: Live production files on local artist NVMe workstations and internal 10GbE studio NAS.
   * Copy 2: Local hourly snapshot image stored on an isolated on-premises secondary backup server.
   * Copy 3: Encrypted, immutable cloud backup hosted on AWS S3 in a separate geographical region.
2. **2 Different Media Types:**
   * Flash/NVMe ZFS storage arrays (for high IOPS daily operations).
   * Cloud Object Storage / Cold Cloud Vaults (for immutable resilience).
3. **1 Offsite Replica:**
   * Geographically distinct cloud facility (e.g., Primary studio in Mumbai -> Offsite disaster recovery bucket in AWS Frankfurt or Singapore) protected by **S3 Object Lock** in Compliance Mode.

---

## 4. Backup Scheduling & Automation Matrix

| Data Classification | Backup Type | Frequency | Target Destination | Retention Policy |
| :--- | :--- | :--- | :--- | :--- |
| **Git Repositories (Code & LFS)** | Incremental Mirror | Every 15 Minutes | GitHub Cloud + S3 Mirror | 90 Days Daily / Infinite Tagged Releases |
| **Active 3D Assets & Textures** | Differential Snapshot | Hourly | Studio NAS Cache (ZFS) | 14 Days rolling hourly snapshots |
| **Unreal/Unity Nightly Builds** | Full Build Archive | Daily at 02:00 AM | AWS S3 Standard (Hot) | 30 Days before S3-IA transition |
| **Raw Footage & Sim Caches (.vdb)**| Cumulative Batch | Weekly on Sunday | S3 Glacier Deep Archive | 3 Years (Post-release golden master) |

---

## 5. Step-by-Step Disaster Recovery Scenarios

### Scenario A: Local Studio NAS Hardware Failure
1. **Detection:** Monitoring alerts via Prometheus/Grafana detect drive pool degradation on local NAS.
2. **Failover:** Lead TD redirects workstations via local DNS alias to the secondary on-premises standby NAS.
3. **Restoration:** New NVMe drives installed; automated ZFS pool rebuild initiates from secondary snapshot. Artists resume within **45 minutes**.

### Scenario B: Studio Ransomware Infection
1. **Containment:** Immediately sever all external internet links and uncouple 10GbE network switches to isolate infected workstations.
2. **Sanitization:** Wipe affected workstations and re-image using clean PXE operating system deployment images.
3. **Recovery:** Primary backups on local network might be compromised. The studio activates the **AWS S3 Immutable Object Lock Vault**. Because WORM (Write-Once-Read-Many) compliance mode prohibits file modification or deletion even by root admins, cloud assets remain completely uninfected.
4. **Resync:** Pull clean LFS pointers and active assets from AWS S3 via Gigabit recovery pipe. Recovery complete within **3.5 hours** (under the 4-hour RTO).

### Scenario C: Accidental Deletion of Critical Asset Branch
1. **Detection:** Artist accidentally force-deletes `development` branch or overwrites master FBX file.
2. **Restoration:**
   ```bash
   # Retrieve commit hash from Git Reflog
   git reflog show origin/development
   
   # Re-create and restore branch
   git checkout -b development-recovered <safe-commit-hash>
   git push origin development-recovered:development --force-with-lease
   ```
3. **Downtime:** Less than **10 minutes**.

---

## 6. Audit & Recovery Drill Schedule
* **Monthly:** Automated restoration test of 100 randomly selected Git LFS asset pointers from S3 Glacier.
* **Bi-Annual:** Simulated full studio failover drill to test complete pipeline recovery from offsite cloud archives.
