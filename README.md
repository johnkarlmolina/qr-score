# QR-Score: QR Code with Random Points Generator

Isang proyekto na gumagawa ng QR code na may kasamang logo/design. Kapag na-scan, magbubukas ng web page na nagpapakita ng random points (1-20).

## 📁 Files

1. **index.html** - Web page na nagpapakita ng random points
2. **generate_qr.py** - Python script para gumawa ng QR code
3. **README.md** - Documentation (itong file)

## 🚀 Paano Gamitin

### Step 1: I-install ang Python dependencies

Buksan ang terminal at i-run:

```bash
pip install qrcode[pil] pillow
```

### Step 2: I-host ang HTML file online (IMPORTANTE para sa printed QR codes)

Para gumana ang QR code kahit naka-print, kailangan mo i-host ang `index.html` sa internet.

**Opsyon 1: GitHub Pages (Pinakarekomenado)**

1. Gumawa ng GitHub repository
2. I-upload ang `index.html`
3. I-enable ang GitHub Pages sa Settings
4. Makakakuha ka ng URL tulad ng: `https://username.github.io/qr-score/`

**Opsyon 2: Netlify (Madali)**

1. Pumunta sa [netlify.com](https://netlify.com)
2. Drag and drop ang `index.html` file
3. Makakakuha ng URL tulad ng: `https://random-name.netlify.app/`

**Opsyon 3: Vercel**

1. Pumunta sa [vercel.com](https://vercel.com)
2. I-deploy ang folder
3. Makakakuha ng URL

### Step 3: Gumawa ng QR Code

I-run ang Python script:

```bash
python generate_qr.py
```

Tatanungin ka ng URL. I-type ang URL ng iyong hosted HTML file (halimbawa: `https://username.github.io/qr-score/index.html`)

### Step 4: I-print ang QR Code

Ang script ay gagawa ng dalawang QR code files:

- **qr_code_with_logo.png** - May star logo sa gitna
- **qr_code_simple.png** - Walang logo

Pareho high-resolution (300 DPI) at maganda sa print!

## 📱 Paano Gumana

1. I-scan ang printed QR code gamit ang smartphone
2. Automatic mag-oopen sa browser
3. Makikita ang random points (1-20) kasama ang mensahe:
   **"Congratulations! You got X points!"**

## ✨ Features

- ✅ **Random Points** - 1 hanggang 20 points bawat scan
- ✅ **Magandang Design** - May animation at gradient colors
- ✅ **Works Offline** - Self-contained HTML, walang external dependencies
- ✅ **Print-Ready** - High-resolution QR code (300 DPI)
- ✅ **May Logo** - Star design sa gitna ng QR code
- ✅ **Mobile-Friendly** - Responsive design para sa lahat ng screen sizes

## 🎨 Customization

### Para baguhin ang color scheme:

Buksan ang `index.html` at baguhin ang mga kulay sa `<style>` section:

```css
/* Current gradient: Purple to Blue */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Para baguhin ang range ng points:

Sa `index.html`, hanapin ang line na ito:

```javascript
const points = Math.floor(Math.random() * 20) + 1;  // 1-20
```

Baguhin ang `20` sa desired maximum number.

### Para baguhin ang logo:

I-edit ang `create_simple_logo()` function sa `generate_qr.py` o gumamit ng sariling image file.

## 🔧 Troubleshooting

**Q: Hindi ma-scan ang QR code?**
- Siguraduhing malinaw ang print
- Subukan ang QR code na walang logo (`qr_code_simple.png`)
- Check kung tama ang URL

**Q: Hindi gumagana offline?**
- Ang HTML file ay dapat nakabukas locally (file://) o naka-host online
- Para sa offline access, kailangan na-download na sa device

**Q: Hindi mag-load ang page?**
- Check kung naka-host ba online ang HTML file
- Verify kung accessible ang URL sa browser

## 📄 License

Free to use and modify!

---

Enjoy your QR Score system! 🎉
