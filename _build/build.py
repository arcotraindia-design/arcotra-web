# -*- coding: utf-8 -*-
"""ARCOTRA site üreticisi.  Çalıştır:  python3 _build/build.py"""
import os, re, sys, html as _h
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SIRKET as S, BOLUMLER

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABAN = "https://arcotratrade.com"
duz = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", _h.unescape(str(s)))).strip()

# ─────────── iskelet ───────────
def head(baslik, aciklama, yol, gorsel=None):
    og = gorsel or "/img/share-card.jpg"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{baslik}</title>
<meta name="description" content="{duz(aciklama)[:158]}">
<link rel="canonical" href="{TABAN}{yol}">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta name="theme-color" content="#173F55">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Arcotra">
<meta property="og:title" content="{duz(baslik)}">
<meta property="og:description" content="{duz(aciklama)[:158]}">
<meta property="og:url" content="{TABAN}{yol}">
<meta property="og:image" content="{TABAN}{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{TABAN}{og}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>'''

def nav(aktif=""):
    def a(y, ad, s):
        c = ' class="on"' if aktif == s else ''
        return f'<a href="{y}"{c}>{ad}</a>'
    return f'''
<nav>
  <div class="wrap">
    <a href="/" aria-label="Arcotra — home"><img src="/img/logo-01.png" width="150" height="36" alt="Arcotra"></a>
    <div class="navlinks" id="navlinks">
      {a("/architecture/","Architecture","architecture")}
      {a("/construction/","Construction","construction")}
      {a("/trade/","Trade","trade")}
      <a class="btn" href="/enquiry/">Enquire</a>
    </div>
    <button class="menu-btn" id="menuBtn" aria-label="Menu" aria-expanded="false" aria-controls="navlinks">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>'''

def crumb(*par):
    p = ['<a href="/">Home</a>']
    for i, (ad, yol) in enumerate(par):
        p.append('<span>/</span>')
        p.append(f'<a href="{yol}">{ad}</a>' if yol else f'<b>{ad}</b>')
    return f'<div class="wrap"><nav class="crumb" aria-label="Breadcrumb">{"".join(p)}</nav></div>'

def footer():
    hiz = "".join(f'<li><a href="/{b["slug"]}/">{b["ad"]}</a></li>' for b in BOLUMLER)
    return f'''
<footer>
  <div class="wrap">
    <div class="top">
      <div>
        <img src="/img/logo-02.png" width="130" height="31" alt="Arcotra">
        <p style="margin:0;max-width:34ch">Architecture, construction and trade.<br>Noida, India &mdash; working internationally.</p>
      </div>
      <div class="cols">
        <div><h4>Divisions</h4><ul>{hiz}</ul></div>
        <div><h4>Enquiries</h4><ul>
          <li><a href="/enquiry/">Request a quotation</a></li>
          <li><a href="{S['wa']}" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><a href="mailto:{S['mail']}">{S['mail']}</a></li>
        </ul></div>
        <div><h4>Office</h4><ul><li>{"<br>".join(S['adres'])}</li>
          <li><a href="tel:+919289480963">{S['tel_goster']}</a></li></ul></div>
      </div>
    </div>
    <div class="legal">
      <span>&copy; 2026 {S['ad']}</span>
      <span>CIN {S['cin']} &nbsp;&middot;&nbsp; GSTIN {S['gstin']}</span>
    </div>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>'''

def cta_blok(baslik, metin, c="", s=""):
    q = []
    if c: q.append("c=" + c)
    if s: q.append("s=" + s)
    yol = "/enquiry/" + ("?" + "&".join(q) if q else "")
    return f'''
<section class="tight">
  <div class="wrap">
    <div class="cta rv">
      <h2>{baslik}</h2>
      <p>{metin}</p>
      <div class="row">
        <a class="btn lg" href="{yol}">Request a quotation</a>
        <a class="btn lg ghost" href="{S['wa']}" target="_blank" rel="noopener">Message on WhatsApp</a>
      </div>
    </div>
  </div>
</section>'''

def yaz(yol, icerik):
    tam = os.path.join(KOK, yol.strip("/"), "index.html") if yol != "/" else os.path.join(KOK, "index.html")
    os.makedirs(os.path.dirname(tam), exist_ok=True)
    open(tam, "w", encoding="utf-8").write(icerik)
    return tam, len(icerik)

# ─────────── ana sayfa ───────────
def ana():
    p = ""
    for b in BOLUMLER:
        p += f'''
    <a class="panel" href="/{b['slug']}/">
      <img src="{b['gorsel']}" alt="{duz(b['ad'])} — {duz(b['kart'])[:70]}" width="900" height="1200" loading="eager">
      <p class="num">{b['num']}</p>
      <h2>{b['ad']}</h2>
      <p>{b['kart']}</p>
      <span class="go">Explore &rarr;</span>
    </a>'''
    return (head("Arcotra — Architecture, Construction &amp; Trade | Noida, India",
                 "ARCOTRA PRIVATE LIMITED — architectural and interior design, construction, and "
                 "export of Indian marble, natural stone and ceramic. Based in Noida, working with "
                 "clients internationally.", "/", "/img/share-card.jpg")
            + nav() + f'<main class="panels">{p}\n  </main>' + footer())

# ─────────── bölüm sayfası ───────────
def bolum(b):
    kartlar = ""
    for h in b["hizmetler"]:
        kartlar += f'''
      <a class="panel" href="/{b['slug']}/{h['slug']}/">
        <img src="{h['gorsel']}" alt="{duz(h['ad'])} — {duz(h['kart'])[:70]}" width="900" height="1200" loading="lazy">
        <p class="num">{h['num']}</p>
        <h2>{h['ad']}</h2>
        <p>{h['kart']}</p>
        <span class="go">View service &rarr;</span>
      </a>'''
    return (head(f"{duz(b['ad'])} — Arcotra | {duz(b['basli'])}", b["giris"],
                 f"/{b['slug']}/", b["gorsel"])
      + nav(b["slug"]) + crumb((b["ad"], None))
      + f'''
<header class="phead">
  <div class="wrap">
    <p class="eyebrow">{b['num']} &mdash; {duz(b['ad']).upper()}</p>
    <h1>{b['basli']}</h1>
    <p>{b['giris']}</p>
  </div>
</header>

<main class="panels of5">{kartlar}
</main>
'''
      + cta_blok("Not sure which one you need?",
                 "Describe the project in a sentence or two and we will tell you where it fits.",
                 b["slug"])
      + footer())

# ─────────── hizmet detay sayfası ───────────
def detay(b, h):
    # süreç yol haritası
    yol = ""
    if h.get("surec"):
        adimlar = "".join(
            f'<div class="step"><p class="n">{i:02d}</p><div><h3>{ad}</h3><p>{ac}</p></div></div>'
            for i, (ad, ac) in enumerate(h["surec"], 1))
        yol = f'''
<section>
  <div class="wrap">
    <div class="sechead rv">
      <p class="eyebrow">How it works</p>
      <h2>The process, step by step.</h2>
    </div>
    <div class="road rv">{adimlar}</div>
  </div>
</section>'''

    # ürün ızgarası (trade)
    urun = ""
    if h.get("urunler"):
        bas, liste = h["urunler"]
        k = "".join(f'''<figure class="pcard">
        <img src="/img/products/{d}.jpg" alt="{duz(ad)} — Indian {'marble' if b['slug']=='trade' else 'tile'}" width="286" height="175" loading="lazy">
        <div class="body"><h3>{ad}</h3><p class="origin">{alt}</p><p>{ac}</p></div>
      </figure>''' for d, ad, alt, ac in liste)
        urun = f'''
<section class="alt">
  <div class="wrap">
    <div class="sechead rv"><p class="eyebrow">{bas}</p><h2>{len(liste)} to choose from.</h2></div>
    <div class="pgrid rv">{k}</div>
  </div>
</section>'''

    # teknik bilgi tablosu
    bilgi = ""
    if h.get("bilgi"):
        satir = "".join(f'<div class="step"><p class="n">&mdash;</p><div><h3>{ad}</h3><p>{ac}</p></div></div>'
                        for ad, ac in h["bilgi"])
        bilgi = f'''
<section>
  <div class="wrap">
    <div class="sechead rv"><p class="eyebrow">Specification</p><h2>What we can supply.</h2></div>
    <div class="road rv">{satir}</div>
  </div>
</section>'''

    # hazırlık listesi
    hazir = ""
    if h.get("hazir"):
        bas, ac, maddeler = h["hazir"]
        li = "".join(f"<li>{m}</li>" for m in maddeler)
        hazir = f'''
<section class="alt tight">
  <div class="wrap">
    <div class="prep rv">
      <h3>{bas}</h3>
      {f'<p>{ac}</p>' if ac else ''}
      <ul>{li}</ul>
    </div>
  </div>
</section>'''

    cta_b, cta_m = h["cta"]
    return (head(f"{duz(h['ad'])} — {duz(b['ad'])} | Arcotra", h["giris"],
                 f"/{b['slug']}/{h['slug']}/", h["gorsel"])
      + nav(b["slug"]) + crumb((b["ad"], f"/{b['slug']}/"), (h["ad"], None))
      + f'''
<header class="phead">
  <div class="wrap">
    <p class="eyebrow">{b['ad']} &nbsp;&mdash;&nbsp; {h['num']}</p>
    <h1>{h['basli']}</h1>
    <p>{h['giris']}</p>
  </div>
</header>
'''
      + yol + urun + bilgi + hazir
      + cta_blok(cta_b, cta_m, b["slug"], h["slug"])
      + footer())

# ─────────── talep formu ───────────
def form():
    alanlar = [
      ("name","Name","text",True,"","Your full name"),
      ("company","Company","text",False,"","Optional"),
      ("email","Email","email",True,"","name@company.com"),
      ("phone","Phone / WhatsApp","tel",False,"","Include country code"),
      ("country","Country","text",False,"","Where you are based"),
      ("location","Project location","text",False,"","City or site address"),
    ]
    f = ""
    for ad, etiket, tip, zorunlu, deger, ipucu in alanlar:
        f += f'''
      <p class="field">
        <label for="f-{ad}">{etiket}{' <em>*</em>' if zorunlu else ''}</label>
        <input id="f-{ad}" name="{etiket}" type="{tip}" {'required' if zorunlu else ''}
               placeholder="{ipucu}" autocomplete="{'name' if ad=='name' else 'email' if ad=='email' else 'tel' if ad=='phone' else 'organization' if ad=='company' else 'country-name' if ad=='country' else 'off'}">
      </p>'''
    return (head("Enquiry — Arcotra",
                 "Tell us about your project. Architecture, construction or trade — we reply from "
                 "Noida, India, usually within one working day.", "/enquiry/")
      + nav() + crumb(("Enquiry", None))
      + f'''
<header class="phead">
  <div class="wrap">
    <p class="eyebrow">Enquiry</p>
    <h1>Tell us about the project.</h1>
    <p>A few lines is enough to start. If you already have drawings, photographs or a
    reference image, mention it and we will ask for them in our reply.</p>
  </div>
</header>

<section class="tight">
  <div class="wrap formwrap">
    <form id="enquiry" class="rv in" method="post" novalidate>

      <div id="ctx-summary" class="ctx" hidden>
        <p class="eyebrow" style="margin:0 0 12px">Your selection</p>
        <dl>
          <div><dt>Division</dt><dd id="ctx-category-label">&mdash;</dd></div>
          <div id="ctx-service-row"><dt>Service</dt><dd id="ctx-service-label">&mdash;</dd></div>
        </dl>
        <p class="ctxnote">Carried over from the page you came from &mdash; no need to repeat it below.</p>
      </div>

      <input type="hidden" id="ctx-category" name="Category" value="">
      <input type="hidden" id="ctx-service"  name="Service"  value="">
      <input type="hidden" id="ctx-page"     name="Source"   value="">
      <input type="hidden" id="ctx-subject"  name="_subject" value="New Website Enquiry">
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"
             style="position:absolute;left:-9999px" aria-hidden="true">

      <div class="grid2">{f}
      </div>

      <p class="field">
        <label for="f-message">Message <em>*</em></label>
        <textarea id="f-message" name="Message" rows="6" required
          placeholder="What are you building, renovating or sourcing? Rough size, timeline and budget all help."></textarea>
      </p>

      <div class="submit">
        <button class="btn lg" type="submit">Send enquiry</button>
        <a class="btn lg ghost" href="{S['wa']}" target="_blank" rel="noopener">Or message on WhatsApp</a>
      </div>
      <p class="ctxnote">We reply from Noida, India &mdash; usually within one working day.</p>
    </form>
  </div>
</section>
'''
      + footer())

# ─────────── çalıştır ───────────
def main():
    import shutil, datetime
    os.makedirs(os.path.join(KOK, "assets"), exist_ok=True)
    shutil.copy(os.path.join(KOK, "_build", "style.css"), os.path.join(KOK, "assets", "site.css"))
    shutil.copy(os.path.join(KOK, "_build", "site.js"),   os.path.join(KOK, "assets", "site.js"))

    sayfalar, yollar = [], []
    def kaydet(yol, icerik, oncelik):
        t, n = yaz(yol, icerik)
        sayfalar.append((yol, n)); yollar.append((yol, oncelik))

    kaydet("/", ana(), "1.0")
    for b in BOLUMLER:
        kaydet(f"/{b['slug']}/", bolum(b), "0.9")
        for h in b["hizmetler"]:
            kaydet(f"/{b['slug']}/{h['slug']}/", detay(b, h), "0.8")
    kaydet("/enquiry/", form(), "0.7")

    bugun = datetime.date.today().isoformat()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for yol, onc in yollar:
        sm += ["  <url>", f"    <loc>{TABAN}{yol}</loc>",
               f"    <lastmod>{bugun}</lastmod>", f"    <priority>{onc}</priority>", "  </url>"]
    sm.append("</urlset>")
    open(os.path.join(KOK, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm))
    open(os.path.join(KOK, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {TABAN}/sitemap.xml\n")

    print(f"  {len(sayfalar)} sayfa üretildi")
    for yol, n in sayfalar:
        print(f"    {yol:<44} {n//1024:>3} KB")
    print(f"  sitemap.xml · robots.txt · assets/site.css · assets/site.js")

if __name__ == "__main__":
    main()
