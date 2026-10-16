# Cloud Storage Cost Optimization Report for Media Pipelines

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Item 10 - Cost Optimization Report  

---

## 1. Problem Statement & Financial Background

Digital game and VFX productions routinely generate between **50 Terabytes (TB)** to **500 Terabytes (TB)** of binary data over an 18-month production cycle. 

If a studio blindly stores 100 TB of assets on default high-performance cloud storage (such as AWS S3 Standard) for an entire year without lifecycle management, the storage cost alone becomes financially crippling:

$$\text{Monthly Cost (Unoptimized)} = 100,000 \text{ GB} \times \$0.023/\text{GB} = \$2,300 \text{ per month} \ (\approx ₹1,90,000/\text{month})$$
$$\text{Annual Cost (Unoptimized)} = \$27,600 \text{ per year} \ (\approx ₹23,00,000/\text{year})$$

By designing an automated **Tiered Cloud Storage Lifecycle Strategy**, studios can cut annual cloud infrastructure expenditures by **up to 75%–85%** without impacting artists' daily speed.

---

## 2. AWS S3 Storage Tier Comparison Matrix

| Storage Class | Cost per GB/Month | Retrieval Fee | Typical Production Use Case | Latency |
| :--- | :--- | :--- | :--- | :--- |
| **S3 Standard (Hot)** | **$0.023** | $0.00 | Active sprint assets, current character models, ongoing build outputs | Milliseconds |
| **S3 Standard-IA (Warm)** | **$0.0125** (-46%) | $0.01 / GB | Prior sprint milestone builds, stabilized environment sets, review renders | Milliseconds |
| **S3 Glacier Flexible (Cold)** | **$0.0036** (-84%) | $0.03 / GB | Completed project assets, raw plate footage, offline audio archives | 1–5 Hours |
| **S3 Glacier Deep Archive (Archive)** | **$0.00099** (-95.7%) | $0.02 / GB | Raw photogrammetry scans, simulation caches (.vdb), final gold masters | 12 Hours |

---

## 3. Real-World Scenario: 100 TB Studio Pipeline Model

Consider a mid-scale Game & VFX studio generating **100 TB (102,400 GB)** of total project data distributed over time:
* **Active Working Assets (Hot):** 15 TB (Current character models, active texture maps, nightly builds)
* **Milestone / Staging Assets (Warm):** 25 TB (Alpha/Beta engine builds, approved audio tracks, textures from prior levels)
* **Raw Archival / Sim Data (Cold Archive):** 60 TB (Raw 8K photogrammetry scans, Houdini fire/smoke simulation caches, gold masters)

### Cost Analysis Comparison Table

```
+---------------------------------------------------------------------------------------+
|                   ANNUAL STORAGE COST COMPARISON: 100 TB DATASET                      |
+------------------------------+-------------------+----------------+-------------------+
| Architecture Strategy        | Storage Breakdown | Monthly Bill   | Annual Expense    |
+------------------------------+-------------------+----------------+-------------------+
| **Strategy 1: Unoptimized**  | 100 TB in         | $2,300.00      | $27,600.00        |
| (Everything in S3 Standard)  | S3 Standard       |                | (₹23,00,000)      |
+------------------------------+-------------------+----------------+-------------------+
| **Strategy 2: Optimized**    | • 15 TB Standard: | $345.00        |                   |
| (Automated Multi-Tier        | • 25 TB S3-IA:    | $312.50        | $716.90 / month   |
| Lifecycle Policy)            | • 60 TB Deep Arc: | $59.40         |                   |
|                              | **Total:**        | **$716.90**    | **$8,602.80**     |
|                              |                   |                | (₹7,15,000)       |
+------------------------------+-------------------+----------------+-------------------+
| **NET SAVINGS PER YEAR**     |                   | **$1,583.10/mo | **$18,997.20 / yr |
|                              |                   | (-68.8%)**     | (-68.8% Saved)**  |
+------------------------------+-------------------+----------------+-------------------+
```

---

## 4. Automated AWS S3 Lifecycle Configuration Policy

To enforce this optimization programmatically without manual human intervention, we apply an XML/JSON S3 Lifecycle Rule to the media bucket:

```json
{
  "Rules": [
    {
      "ID": "GameVFXAssetLifecycleOptimization",
      "Status": "Enabled",
      "Filter": {
        "Prefix": "production-assets/"
      },
      "Transitions": [
        {
          "Days": 60,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 180,
          "StorageClass": "GLACIER"
        },
        {
          "Days": 365,
          "StorageClass": "DEEP_ARCHIVE"
        }
      ],
      "NoncurrentVersionTransitions": [
        {
          "NoncurrentDays": 30,
          "StorageClass": "DEEP_ARCHIVE"
        }
      ],
      "AbortIncompleteMultipartUpload": {
        "DaysAfterInitiation": 7
      }
    }
  ]
}
```

### Operational Highlights of the Policy:
1. **Day 0–59:** Assets remain in **S3 Standard** for zero-latency artist edits.
2. **Day 60:** Assets automatically transition to **S3 Standard-IA**, cutting holding costs in half.
3. **Day 180:** Assets transition to **S3 Glacier**, reducing cost by 84%.
4. **Day 365:** Milestone gold masters settle into **Glacier Deep Archive** at $0.00099/GB/month.
5. **Incomplete Upload Purge:** Multipart binary uploads that failed or were cancelled are purged after 7 days, preventing abandoned multi-gigabyte files from accumulating charges.

---

## 5. Conclusion & Recommendations

By implementing automated lifecycle tiering:
1. The studio saves **$19,000 (~₹15.8 Lakhs) annually** on every 100 TB of storage.
2. Artists maintain peak read/write speeds for active tasks without having to manually manage file archives.
3. Financial risk and storage runaways are completely eliminated through programmatic governance.
