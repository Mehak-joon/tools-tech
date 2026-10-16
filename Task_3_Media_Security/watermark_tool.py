"""
Digital Watermarking Demonstration Script for Media Assets
Subject: Tools & Techniques of Game and VFX-II (BCA MIT)
Author: Mehak Joon

Task 3: Media Security & Digital Asset Protection
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

def apply_visible_watermark(input_image_path, output_image_path, watermark_text="CONFIDENTIAL - MEHAK JOON"):
    """
    Applies a semi-transparent, diagonal visible watermark across a media asset frame
    to prevent unauthorized distribution during pre-production reviews.
    """
    if not os.path.exists(input_image_path):
        print(f"[!] Error: Input image {input_image_path} does not exist.")
        return False

    base_image = Image.open(input_image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    font = ImageFont.load_default()
    width, height = base_image.size
    
    step_x = max(150, width // 4)
    step_y = max(80, height // 5)
    
    for x in range(20, width, step_x):
        for y in range(20, height, step_y):
            draw.text((x, y), watermark_text, fill=(255, 255, 255, 70), font=font)
    
    watermarked = Image.alpha_composite(base_image, txt_layer)
    watermarked.convert("RGB").save(output_image_path, "PNG")
    print(f"[✓] Visible watermark applied successfully: {output_image_path}")
    return True

def apply_invisible_watermark_metadata(input_image_path, output_image_path, secret_tracking_id="ASSET-SEC-ID-7829-USER-MEHAK"):
    """
    Applies an invisible forensic watermark by embedding a proprietary tracking payload
    into the image metadata headers.
    """
    if not os.path.exists(input_image_path):
        print(f"[!] Error: Input image {input_image_path} does not exist.")
        return False

    from PIL.PngImagePlugin import PngInfo
    
    img = Image.open(input_image_path)
    metadata = PngInfo()
    metadata.add_text("Watermark-Forensic-ID", secret_tracking_id)
    metadata.add_text("Security-Classification", "Tier-1 Proprietary VFX Asset")
    metadata.add_text("Authorized-Recipient", "Mehak Joon - BCA MIT")
    
    img.save(output_image_path, pnginfo=metadata)
    print(f"[✓] Invisible forensic watermark embedded in metadata: {output_image_path}")
    return True

def inspect_forensic_metadata(image_path):
    """
    Reads embedded invisible watermark metadata from an asset for forensic audit.
    """
    if not os.path.exists(image_path):
        print(f"[!] Error: Image {image_path} not found.")
        return
        
    img = Image.open(image_path)
    print(f"\n--- Forensic Metadata Analysis: {os.path.basename(image_path)} ---")
    found = False
    for k, v in img.info.items():
        print(f"  • {k}: {v}")
        found = True
    if not found:
        print("  [!] No embedded forensic metadata found.")

if __name__ == "__main__":
    print("=" * 60)
    print(" Game & VFX Digital Asset Watermarking Tool")
    print(" Tools & Techniques of Game and VFX-II | Mehak Joon")
    print("=" * 60)
    
    sample_asset = "sample_texture_diffuse.png"
    if not os.path.exists(sample_asset):
        dummy_img = Image.new("RGB", (512, 512), color=(73, 109, 137))
        d = ImageDraw.Draw(dummy_img)
        d.text((160, 240), "3D Prop Texture - PBR Albedo", fill=(255, 255, 255))
        dummy_img.save(sample_asset)
        print(f"[+] Created sample asset for demonstration: {sample_asset}")
        
    vis_out = "sample_texture_watermarked_visible.png"
    invis_out = "sample_texture_watermarked_invisible.png"
    
    apply_visible_watermark(sample_asset, vis_out)
    apply_invisible_watermark_metadata(sample_asset, invis_out)
    inspect_forensic_metadata(invis_out)
    print("\n[✓] Watermarking workflow demonstration complete.")
