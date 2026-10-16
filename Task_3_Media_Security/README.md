# Task 3: Media Security & Digital Asset Protection (10 Marks)

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Student Name:** Mehak Joon  
**Batch:** 2024–27  

---

## 🎯 Task Objectives
1. **Security Threats in Media Projects:** Identify key vulnerabilities (pre-release asset leaks, ransomware, source code tampering, credential stuffing).
2. **Secure Authentication & MFA:** Enforce Multi-Factor Authentication (TOTP / FIDO2) and cryptographic SSH-ed25519 key access.
3. **Threat Model:** Build a complete **STRIDE** threat model for a game and VFX media studio.
4. **Source Code & Asset Protection:** Implement branch protection rules, GPG commit signing, secret scanning, and binary packaging.
5. **Digital Watermarking:** Explain and demonstrate visible review burn-in watermarking and invisible forensic metadata embedding.
6. **Cyber Attack Analysis & Mitigation:** Recommend mitigation strategies for ransomware, supply chain poisoning, and third-party contractor leaks.

---

## 🛡️ 1. STRIDE Threat Model Summary

```
+--------------------+--------------------------------+---------------------------------+
| STRIDE Category    | Specific Media Threat          | Implemented Countermeasure      |
+--------------------+--------------------------------+---------------------------------+
| **S**poofing       | Impersonating an artist to     | SSH-ed25519 keys, GPG commit    |
|                    | push malicious dependencies    | signing, mandatory 2FA/MFA.     |
+--------------------+--------------------------------+---------------------------------+
| **T**ampering      | Modifying source scripts or 3D | Branch protection, PR review    |
|                    | assets with hidden exploits    | approvals, SHA-256 checksums.   |
+--------------------+--------------------------------+---------------------------------+
| **R**epudiation    | Artist denies leaking an       | Cryptographic Git audit logs,   |
|                    | unreleased cinematic trailer   | forensic digital watermarks.    |
+--------------------+--------------------------------+---------------------------------+
| **I**nformation    | Pre-release game asset or plot | AES-256 cloud encryption, RBAC, |
| Disclosure         | leak to public forums          | short-lived pre-signed URLs.    |
+--------------------+--------------------------------+---------------------------------+
| **D**enial of      | Ransomware encrypting shared   | Immutable S3 Object Lock (WORM),|
| Service (DoS)      | studio NAS render cache        | air-gapped offsite snapshots.   |
+--------------------+--------------------------------+---------------------------------+
| **E**levation of   | Freelancer gaining repository  | Least-privilege IAM policies,   |
| Privilege          | administrative settings        | outside-collaborator isolation. |
+--------------------+--------------------------------+---------------------------------+
```

---

## 💧 2. Digital Watermarking Demonstration

In this folder, you have a working Python script: [`watermark_tool.py`](watermark_tool.py).

### How to Run:
```bash
python Task_3_Media_Security/watermark_tool.py
```

### What It Demonstrates:
1. **Visible Watermarking:** Alpha-blends a semi-transparent `"CONFIDENTIAL - MEHAK JOON"` stamp across the image so dailies and review footage cannot be leaked without showing the reviewer's name.
2. **Invisible Forensic Watermarking:** Injects hidden metadata (`Watermark-Forensic-ID`, `Authorized-Recipient`) inside the file headers. If an unreleased texture or frame is posted online, the inspector reveals the exact user ID responsible!

---

## 📑 Detailed Reports Included in this Folder
1. **[`Threat_Model_and_Security.md`](Threat_Model_and_Security.md)**: Full STRIDE model, attack trees, and cyber attack mitigations.
2. **[`Digital_Watermarking_Report.md`](Digital_Watermarking_Report.md)**: Theory of visible vs. invisible watermarking, frequency transforms (DWT/DCT), and 3D mesh watermarking.
3. **[`watermark_tool.py`](watermark_tool.py)**: Python automation tool implementing visible and invisible forensic watermarks.
