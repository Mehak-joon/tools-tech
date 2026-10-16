# Cloud Storage Cost Optimization Report for Media Pipelines

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Task 2 - Cost Optimization Report  

---

## 1. Storage Tiers & Cost Comparison (100 TB Dataset)

A studio storing 100 TB on AWS S3 Standard without lifecycle tiering spends:
$$\text{Annual Cost (Unoptimized)} = 100,000 \text{ GB} \times \$0.023/\text{GB} \times 12 = \$27,600 \text{ / year} \ (\approx ₹23,00,000/\text{year})$$

By applying automated S3 Lifecycle rules:
* **Active Working Assets (15 TB):** Stored in **S3 Standard** ($0.023/GB) = $345.00/month
* **Warm Sprint Builds (25 TB):** Transitioned to **S3-IA** ($0.0125/GB) = $312.50/month
* **Cold Caches & Footage (60 TB):** Transitioned to **Glacier Deep Archive** ($0.00099/GB) = $59.40/month

### Financial Results:
* **Optimized Monthly Bill:** **$716.90 / month** (down from $2,300.00/month)
* **Optimized Annual Expense:** **$8,602.80 / year** (down from $27,600.00/year)
* **Net Annual Savings:** **$18,997.20 / year (~68.8% Saved)** (~₹15.8 Lakhs saved annually)

---

## 2. Automated S3 Lifecycle Rule
* **Day 0 to 59:** S3 Standard (Hot)
* **Day 60:** Transition to S3 Standard-IA (Warm)
* **Day 180:** Transition to S3 Glacier Flexible (Cold)
* **Day 365:** Transition to Glacier Deep Archive (Archive)
