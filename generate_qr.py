"""
QR Code Generator with Logo
Creates a printable QR code with embedded design/logo
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def create_qr_with_logo(url, output_filename='qr_code.png', logo_path=None):
    """
    Generate a QR code with optional logo in the center
    
    Args:
        url: The URL to encode in the QR code
        output_filename: Output file name for the QR code
        logo_path: Path to logo image (optional)
    """
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size in boxes
    )
    
    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create QR code image with colors
    qr_img = qr.make_image(fill_color="#667eea", back_color="white").convert('RGB')
    
    # If logo is provided, add it to the center
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        
        # Calculate logo size (should be about 1/5 of QR code size)
        qr_width, qr_height = qr_img.size
        logo_size = qr_width // 5
        
        # Resize logo
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Create a white background for logo (for better contrast)
        logo_bg_size = logo_size + 20
        logo_bg = Image.new('RGB', (logo_bg_size, logo_bg_size), 'white')
        
        # Paste logo on white background
        logo_pos = ((logo_bg_size - logo_size) // 2, (logo_bg_size - logo_size) // 2)
        if logo.mode == 'RGBA':
            logo_bg.paste(logo, logo_pos, logo)
        else:
            logo_bg.paste(logo, logo_pos)
        
        # Calculate position to paste logo (center of QR code)
        logo_pos = ((qr_width - logo_bg_size) // 2, (qr_height - logo_bg_size) // 2)
        qr_img.paste(logo_bg, logo_pos)
    
    # Save QR code
    qr_img.save(output_filename, quality=95, dpi=(300, 300))
    print(f"✓ QR code saved as: {output_filename}")
    print(f"  URL: {url}")
    print(f"  Size: {qr_img.size[0]}x{qr_img.size[1]} pixels")
    
    return qr_img


def create_simple_logo(filename='logo.png'):
    """
    Create a simple logo for the QR code center
    """
    # Create a 200x200 image with gradient background
    size = 200
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw a circular gradient background
    for i in range(size // 2):
        color_val = int(102 + (153 - 102) * (i / (size / 2)))
        draw.ellipse(
            [size // 2 - i, size // 2 - i, size // 2 + i, size // 2 + i],
            fill=(102, 126, 234)
        )
    
    # Draw a trophy emoji or star shape
    # Draw a star
    center_x, center_y = size // 2, size // 2
    radius_outer = 60
    radius_inner = 25
    points = []
    
    import math
    for i in range(10):
        angle = math.pi / 2 + (2 * math.pi * i / 10)
        if i % 2 == 0:
            radius = radius_outer
        else:
            radius = radius_inner
        x = center_x + radius * math.cos(angle)
        y = center_y - radius * math.sin(angle)
        points.append((x, y))
    
    draw.polygon(points, fill='#FFD700', outline='#FFA500')
    
    # Save logo
    img.save(filename)
    print(f"✓ Logo created: {filename}")
    return filename


if __name__ == "__main__":
    print("=" * 60)
    print("QR CODE GENERATOR")
    print("=" * 60)
    
    # Use local file path by default
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_dir, 'index.html')
    user_url = f"file:///{index_path.replace(os.sep, '/')}"
    
    print(f"\nGenerating QR code for: {user_url}")
    print("\n⚠️  IMPORTANTE: Para sa printed QR codes na gumagana kahit saan:")
    print("   I-host ang index.html sa GitHub Pages, Netlify, o Vercel")
    print("   Tapos i-edit ang URL sa line 87 ng generate_qr.py")
    
    # Create logo first
    print("\n" + "-" * 60)
    logo_path = create_simple_logo('logo.png')
    
    # Generate QR code with logo
    print("-" * 60)
    create_qr_with_logo(user_url, 'qr_code_with_logo.png', logo_path)
    
    # Generate QR code without logo (backup)
    create_qr_with_logo(user_url, 'qr_code_simple.png', None)
    
    print("\n" + "=" * 60)
    print("DONE! ✓")
    print("=" * 60)
    print("\nFiles created:")
    print("  1. qr_code_with_logo.png - QR code with star logo")
    print("  2. qr_code_simple.png - QR code without logo")
    print("  3. logo.png - The star logo design")
    print("\nBoth QR codes are high-resolution and print-ready!")
    print("\nTo test locally:")
    print("  1. Scan the QR code with your phone")
    print("  2. Should open index.html in browser")
    print("\nTo use for PRINTED QR codes:")
    print("  1. Upload index.html to GitHub Pages/Netlify")
    print("  2. Edit this script (line 87) with your online URL")
    print("  3. Run again: py generate_qr.py")
