# Threat Model & Media Cybersecurity Analysis

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Task 3 - Threat Model & Security Implementation  

---

## 1. Threat Landscape in Media & Game Production

Game studios and VFX houses operate hybrid multi-site pipelines with high numbers of external contractors. This makes them prime targets for:
1. **Ransomware Extortion:** Cybercriminals breach studio servers, exfiltrate pre-release source code/builds, and encrypt active render caches.
2. **Third-Party Contractor Leaks:** Pre-release footage, character models, or plot points leaked to social media.
3. **Supply-Chain Attacks:** Tampered Python DCC plugins or malicious packages pushed into the pipeline.

---

## 2. STRIDE Threat Model

```
[ EXTERNAL THREATS ]
   • Ransomware Operators
   • Leakers & Social Engineers
   • Credential Stuffing Bots
   │
   ▼
[ LAYER 1: AUTHENTICATION & IDENTITY ]
   • Mandatory Organization Multi-Factor Authentication (MFA)
   • Cryptographic SSH-ed25519 Keys (No passwords allowed)
   • GPG Signed Commits
   │
   ▼
[ LAYER 2: REPOSITORY & CODE PROTECTION ]
   • Branch Protection (Direct pushes to main/dev blocked)
   • Secret Scanning (Blocks accidental push of API keys or credentials)
   • Role-Based Access Control (RBAC)
   │
   ▼
[ LAYER 3: ASSET PACKAGING & STORAGE ]
   • AES-256 Server-Side Encryption at Rest
   • S3 Immutable Object Lock (Protects backups from ransomware deletion)
   • Visible & Invisible Digital Watermarks on review assets
```

---

## 3. Defense Against the Top 3 Cyber Attacks

### 1. Ransomware Mitigation
* Store all offsite backups in AWS S3 buckets with **S3 Object Lock** in Compliance Mode. WORM (Write-Once-Read-Many) guarantees backups cannot be encrypted or deleted by malware.

### 2. Supply-Chain Security
* Lock Python dependencies using SHA-256 hashes in lockfiles and utilize GitHub Dependabot to automatically detect vulnerable packages.

### 3. Leak Prevention
* Enforce dynamic watermarking (burning reviewer identity into daily renders) and embed invisible forensic metadata.
