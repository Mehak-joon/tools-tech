# Cloud Storage Architecture Diagram & Infrastructure Specification

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Task 2 - Cloud Storage Architecture  

---

## 1. Multi-Tier Hybrid Storage Topology

```
+-------------------------------------------------------------------------------+
|                       STUDIO LOCAL NETWORK (ON-PREMISES)                      |
|                                                                               |
|  [3D Workstations]          [Texture Workstations]       [VFX Simulation Node]|
|          │                            │                            │          |
|          └──────────────────────┬─────┴────────────────────────────┘          |
|                                 ▼ (10 GbE Internal LAN)                       |
|                 +──────────────────────────────────────+                      |
|                 |    Studio Edge NAS (Local Cache)     |                      |
|                 |  100 TB High-Speed ZFS NVMe Pool     |                      |
|                 +──────────────────────────────────────+                      |
+------------------------------------│------------------------------------------+
                                     │ (Automated Sync via TLS 1.3 / AWS S3 CLI)
                                     ▼
+-------------------------------------------------------------------------------+
|                           AWS CLOUD STORAGE FABRIC                            |
|                                                                               |
|  +─────────────────────────────────────────────────────────────────────────+  |
|  | TIER 1: AWS S3 STANDARD (HOT TIER)                                      |  |
|  | - Daily active working assets, uncompressed textures, sound masters     |  |
|  | - Build artifacts for CI/CD, game engine imports                        |  |
|  | - Latency: Milliseconds | Availability: 99.99%                         |  |
|  +─────────────────────────────────────────────────────────────────────────+  |
|                                     │                                         |
|                                     │ (Lifecycle Transition: 60 Days Idle)    |
|                                     ▼                                         |
|  +─────────────────────────────────────────────────────────────────────────+  |
|  | TIER 2: AWS S3 STANDARD-INFREQUENT ACCESS (WARM TIER)                  |  |
|  | - Milestone builds (Alpha, Beta), completed sprint footage              |  |
|  | - Latency: Milliseconds | Cost: ~50% savings compared to Standard      |  |
|  +─────────────────────────────────────────────────────────────────────────+  |
|                                     │                                         |
|                                     │ (Lifecycle Transition: 180 Days Idle)   |
|                                     ▼                                         |
|  +─────────────────────────────────────────────────────────────────────────+  |
|  | TIER 3: AWS S3 GLACIER DEEP ARCHIVE (COLD TIER)                         |  |
|  | - Raw camera footage, simulation point caches (.vdb), gold masters      |  |
|  | - Latency: 3 to 12 Hours | Cost: $0.00099 / GB / Month (~95% savings)  |  |
|  +─────────────────────────────────────────────────────────────────────────+  |
+-------------------------------------------------------------------------------+
```

---

## 2. Storage Tier Specifications

| Parameter | Tier 1: S3 Standard (Hot) | Tier 2: S3 Standard-IA (Warm) | Tier 3: Glacier Deep Archive (Cold) |
| :--- | :--- | :--- | :--- |
| **Data Types** | Active `.fbx`, `.blend`, 4K `.png`, `.wav` | Milestone builds, archived sprint renders | Raw footage, `.vdb` smoke caches, final release gold |
| **Latency** | Milliseconds | Milliseconds | 3–12 Hours |
| **Durability** | 99.999999999% (11 9s) | 99.999999999% (11 9s) | 99.999999999% (11 9s) |
| **Storage Cost** | ~$0.023 per GB/mo | ~$0.0125 per GB/mo | ~$0.00099 per GB/mo |
