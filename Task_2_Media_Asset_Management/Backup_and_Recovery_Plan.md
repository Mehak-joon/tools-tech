# Media Asset Backup & Disaster Recovery Plan

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Task 2 - Backup & Disaster Recovery Plan  

---

## 1. Key Recovery Metrics
* **Recovery Point Objective (RPO):** **1 Hour** (Maximum acceptable data loss measured in time).
* **Recovery Time Objective (RTO):** **4 Hours** (Maximum downtime to restore critical pipeline services).

---

## 2. The 3-2-1 Media Backup Rule

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

1. **3 Copies of Data:** Primary local workstation, on-premises NAS, and Cloud object storage.
2. **2 Different Media Types:** Flash/NVMe storage arrays and Cloud Object Storage.
3. **1 Offsite Replica:** Geographically isolated AWS S3 bucket in another region protected by **S3 Object Lock** in Compliance Mode.

---

## 3. Disaster Recovery Procedures
* **Hardware Failure on Local NAS:** Instant failover to standby secondary NAS; data restored in 45 minutes.
* **Ransomware Outbreak:** Isolate network; restore clean assets from immutable AWS S3 Object Lock vault in 3.5 hours.
* **Accidental Commit/Branch Deletion:** Non-destructive `git revert` or `git reflog` restore completed in under 10 minutes.
