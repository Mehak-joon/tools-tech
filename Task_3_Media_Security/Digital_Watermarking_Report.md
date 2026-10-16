# Digital Watermarking & IP Protection Report

**Subject:** Tools & Techniques of Game and VFX-II (BCA MIT)  
**Author:** Mehak Joon  
**Deliverable:** Task 3 - Digital Watermarking Report  

---

## 1. Visible vs. Invisible Watermarking

| Feature | Visible Watermark (Burn-In) | Invisible / Forensic Watermark |
| :--- | :--- | :--- |
| **Appearance** | Obvious text/logo overlaid on frame | Completely imperceptible to human eye |
| **Objective** | Deterrence (discourage screenshotting) | Forensic tracking (identify who leaked) |
| **VFX Pipeline Stage** | Dailies, review cuts, playtests | Master textures, final renders, release builds |
| **Robustness** | Can be cropped if poorly positioned | Resists cropping, downsampling, and color changes |

---

## 2. Watermarking Techniques

1. **Visible Alpha-Blend Burn-In:** Composites recipient username, IP, and timecode across viewport.
2. **Spatial Domain (LSB):** Least Significant Bit modification in image color channels.
3. **Frequency Domain (DWT / DCT):** Embeds tracking codes into Discrete Wavelet Transform sub-bands, resisting heavy compression.
4. **Header Metadata Injection:** Injects signed cryptographic chunks into image and video headers (`PNG`, `EXR`, `MP4`).

---

## 3. Practical Tool Demonstration
The Python script [`watermark_tool.py`](watermark_tool.py) demonstrates both:
* **Visible Watermarking:** Renders `"CONFIDENTIAL - MEHAK JOON"` across image frames.
* **Forensic Metadata:** Embeds tracking ID (`ASSET-SEC-ID-7829-USER-MEHAK`) into file headers for audit inspection.
