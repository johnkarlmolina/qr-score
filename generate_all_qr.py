"""
QR Code Generator - Creates 20 QR codes (1 point to 20 points each)
"""

import qrcode
from PIL import Image, ImageDraw
import os
import math

def create_simple_logo(filename='logo.png'):
    """Create a simple star logo"""
    size = 200
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw circular background
    for i in range(size // 2):
        draw.ellipse(
            [size // 2 - i, size // 2 - i, size // 2 + i, size // 2 + i],
            fill=(102, 126, 234)
        )
    
    # Draw star
    center_x, center_y = size // 2, size // 2
    radius_outer = 60
    radius_inner = 25
    points = []
    
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
    img.save(filename)
    return filename


def create_qr_with_logo(url, output_filename, logo_path=None):
    """Generate QR code with logo"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#667eea", back_color="white").convert('RGB')
    
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        qr_width, qr_height = qr_img.size
        logo_size = qr_width // 5
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        logo_bg_size = logo_size + 20
        logo_bg = Image.new('RGB', (logo_bg_size, logo_bg_size), 'white')
        logo_pos = ((logo_bg_size - logo_size) // 2, (logo_bg_size - logo_size) // 2)
        
        if logo.mode == 'RGBA':
            logo_bg.paste(logo, logo_pos, logo)
        else:
            logo_bg.paste(logo, logo_pos)
        
        logo_pos = ((qr_width - logo_bg_size) // 2, (qr_height - logo_bg_size) // 2)
        qr_img.paste(logo_bg, logo_pos)
    
    qr_img.save(output_filename, quality=95, dpi=(300, 300))
    return qr_img


def create_html_file(points):
    """Create HTML file for specific points"""
    html_content = f"""<!DOCTYPE html>
<html lang="tl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Congratulations - {points} Points!</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        
        .container {{
            background: white;
            border-radius: 20px;
            padding: 60px 40px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            text-align: center;
            max-width: 500px;
            width: 100%;
            animation: fadeIn 0.6s ease-in;
        }}
        
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(-20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .emoji {{
            font-size: 80px;
            margin-bottom: 20px;
            animation: bounce 1s ease infinite;
        }}
        
        @keyframes bounce {{
            0%, 100% {{
                transform: translateY(0);
            }}
            50% {{
                transform: translateY(-10px);
            }}
        }}
        
        h1 {{
            color: #333;
            font-size: 32px;
            margin-bottom: 30px;
            line-height: 1.4;
        }}
        
        .points {{
            font-size: 120px;
            font-weight: bold;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 30px 0;
            animation: pulse 2s ease infinite;
        }}
        
        @keyframes pulse {{
            0%, 100% {{
                transform: scale(1);
            }}
            50% {{
                transform: scale(1.05);
            }}
        }}
        
        .label {{
            font-size: 24px;
            color: #666;
            margin-bottom: 20px;
        }}
        
        .footer {{
            margin-top: 30px;
            color: #999;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">🎉</div>
        <h1>Congratulations!</h1>
        <div class="points">{points}</div>
        <div class="label">points!</div>
        <div class="footer">You got {points} points!</div>
    </div>
</body>
</html>
"""
    
    filename = f"points_{points}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filename


if __name__ == "__main__":
    print("=" * 70)
    print("QR CODE GENERATOR - 20 QR CODES (1-20 POINTS)")
    print("=" * 70)
    
    # Create logo
    print("\nCreating logo...")
    logo_path = create_simple_logo('logo.png')
    print(f"✓ Logo created: {logo_path}")
    
    # Create output folder
    if not os.path.exists('qr_codes'):
        os.makedirs('qr_codes')
    
    print("\n" + "-" * 70)
    print("Creating HTML files and QR codes...")
    print("-" * 70)
    
    # Generate 20 HTML files and QR codes
    for points in range(1, 21):
        # Create HTML file
        html_file = create_html_file(points)
        
        # Create URL (online GitHub Pages URL)
        url = f"https://johnkarlmolina.github.io/qr-score/points_{points}.html"
        
        # Generate QR code
        qr_filename = f"qr_codes/QR_{points:02d}_points.png"
        create_qr_with_logo(url, qr_filename, logo_path)
        
        print(f"✓ Created: {html_file} → {qr_filename} ({points} points)")
    
    print("\n" + "=" * 70)
    print("TAPOS NA! ✓")
    print("=" * 70)
    print("\nNa-create:")
    print("  • 20 HTML files (points_1.html to points_20.html)")
    print("  • 20 QR codes sa folder 'qr_codes/'")
    print("  • 1 logo file (logo.png)")
    print("\nBawat QR code:")
    print("  QR_01_points.png = 1 point")
    print("  QR_02_points.png = 2 points")
    print("  ...")
    print("  QR_20_points.png = 20 points")
    print("\n⚠️  Para gumana ang printed QR codes kahit saan:")
    print("  1. I-upload lahat ng HTML files sa web hosting")
    print("  2. I-edit ang URL sa script (line 115)")
    print("  3. I-run ulit: py generate_all_qr.py")
