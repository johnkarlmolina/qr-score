# Paano Gumamit ng Bit.ly URL Shortener

## Quick Steps:

### 1. Pumunta sa Bit.ly
- Website: https://bit.ly
- Click **"Sign up"** o **"Get Started for Free"**
- Pwede mag-sign up gamit ang Google/Email

### 2. I-shorten ang URLs

Para sa bawat point (1-20), i-shorten mo ang URL:

**Original URL:**
```
https://johnkarlmolina.github.io/qr-score/points_1.html
```

**Sa Bit.ly:**
1. I-paste ang URL sa "Paste a link" box
2. Click **"Create"**
3. I-customize (optional): Click **"Customize"** → type: `score-1`
4. Copy ang shortened URL: `https://bit.ly/score-1`

**Ulitin para sa lahat ng 20 URLs!**

### 3. I-paste sa shortened_urls.txt

Example:
```
1=https://bit.ly/score-1
2=https://bit.ly/score-2
3=https://bit.ly/score-3
...
20=https://bit.ly/score-20
```

### 4. Generate QR Codes

Run sa terminal:
```
py generate_qr_shortened.py
```

---

## Alternative: TinyURL (No account needed!)

### Website: https://tinyurl.com

1. I-paste ang URL
2. Click **"Make TinyURL!"**
3. Copy ang result
4. I-paste sa `shortened_urls.txt`

Example:
```
1=https://tinyurl.com/score-pt1
2=https://tinyurl.com/score-pt2
```

---

## Bonus: Batch URL Shortener

Para sa mas mabilis, pwede ka gumamit ng:
- **Bitly API** (free account, 50 links/month)
- **Short.io** (free, 1000 links/month)
- **Rebrandly** (free custom domain)

---

Tapos na! Pag naka-shorten na lahat, walang makikita na "johnkarlmolina" sa QR codes! 🎉
