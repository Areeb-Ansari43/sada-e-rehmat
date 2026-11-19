#!/usr/bin/env python3
"""Builds every page of the Sada-e-Rehmat site into the repository root.

    python3 _src/build.py

Edit the copy here or the package data in data.py, run the script, commit the
generated .html files. GitHub Pages (Jekyll) ignores folders starting with "_",
so this folder is never published.
"""
import json
import os
import re
from html import escape

from data import COLLECTIONS, PACKAGES, AZIZIYA_PRIVATE, INCLUDED, TERMS, RATE_NOTE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.dirname(os.path.abspath(__file__))
BASE = "https://areeb-ansari43.github.io/sada-e-rehmat/"
EMAIL = "info@sada-e-rehmat.com"
PHONE_PK = ("+92 333 9999200", "+923339999200")
PHONE_UK = ("+44 20 3002 2999", "+442030022999")
COLL = {c["id"]: c for c in COLLECTIONS}


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------
def img(name, alt, sizes="100vw", eager=False, cls=""):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="assets/img/{name}-2000.webp" '
            f'srcset="assets/img/{name}-1000.webp 1000w, assets/img/{name}-2000.webp 2000w" '
            f'sizes="{sizes}" width="2000" height="1500" alt="{escape(alt)}" {load}>')


def lines(*parts):
    """Masked line-by-line headline reveal."""
    return "".join(f'<span class="ln"><span>{p}</span></span>' for p in parts)


ARROW = '<span class="arr" aria-hidden="true">→</span>'

ICONS = {
    "train": '<rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M8 20l2-4M16 20l-2-4"/><circle cx="9" cy="13" r=".8"/><circle cx="15" cy="13" r=".8"/>',
    "tent": '<path d="M3 20 12 4l9 16H3Z"/><path d="m9 20 3-6 3 6"/>',
    "sofa": '<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3"/><rect x="2" y="11" width="20" height="6" rx="2"/><path d="M5 17v2M19 17v2"/>',
    "bus": '<rect x="4" y="3" width="16" height="14" rx="2"/><path d="M4 10h16M7 17v3M17 17v3"/><circle cx="8" cy="13.5" r=".8"/><circle cx="16" cy="13.5" r=".8"/>',
    "meal": '<path d="M7 3v18M5 3v4a2 2 0 0 0 4 0V3M17 21V3c-2 0-3 2-3 6s1 4 3 4"/>',
    "snow": '<path d="M12 2v20M2 12h20M5 5l14 14M19 5 5 19"/>',
    "cup": '<path d="M5 9h11v5a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5V9Z"/><path d="M16 11h1.5a2.5 2.5 0 0 1 0 5H16M9 3v3M12 3v3"/>',
    "bath": '<path d="M3 12h18v3a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5v-3Z"/><path d="M6 12V5.5a2 2 0 0 1 4 0M7 20l-1 2M17 20l1 2"/>',
    "kit": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M3 11h18M9 7V4h6v3"/>',
    "pin": '<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12Z"/><circle cx="12" cy="9" r="2.5"/>',
    "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h7a3.5 3.5 0 0 0 0-7H9a3.5 3.5 0 0 1 0-7h7"/>',
    "check": '<path d="m5 12 5 5L20 7"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/>',
}


def icon(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def pkr(n):
    s = str(n)
    if len(s) <= 3:
        return "Rs " + s
    head, tail = s[:-3], s[-3:]
    groups = []
    while len(head) > 2:
        groups.insert(0, head[-2:])
        head = head[:-2]
    if head:
        groups.insert(0, head)
    return "Rs " + ",".join(groups) + "," + tail


def gbp(n):
    return "£" + f"{n:,}"


def usd(n):
    return "$" + f"{n:,}"


def pkg_name(p):
    c = COLL[p["tier"]]
    return f'{c["name"]} {p["days"].split("–")[-1]}'


def route_label(p):
    return "Madinah first" if p["route"] == "madinah" else "Makkah first"


# --------------------------------------------------------------------------
# Shell
# --------------------------------------------------------------------------
NAV = [("index.html", "Home"), ("packages.html", "Hajj 2027"), ("gallery.html", "Sacred sites"),
       ("guides.html", "Guides"), ("about-us.html", "About")]


OG_MANIFEST = []
PAGES_BUILT = []


def slug_of(page):
    return "home" if page == "index.html" else page[:-5]


def head(page, title, desc, extra="", og=None, og_type="website"):
    url = BASE + ("" if page == "index.html" else page)
    slug = slug_of(page)
    og = og or {}
    og_img = f"{BASE}assets/og/{slug}.jpg"
    og_alt = escape(og.get("alt") or title)
    if og.get("title"):
        OG_MANIFEST.append({"slug": slug, **og})
    else:
        og_img = f"{BASE}assets/og/home.jpg"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#0b1424">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-gb" href="{url}">
<link rel="alternate" hreflang="en-pk" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<link rel="icon" type="image/png" sizes="512x512" href="assets/favicon.png">
<link rel="shortcut icon" href="assets/favicon.ico">
<link rel="apple-touch-icon" href="assets/favicon.png">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Sada-e-Rehmat">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{og_img}">
<meta name="twitter:image:alt" content="{og_alt}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri&family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script>document.documentElement.classList.add('js')</script>
{extra}</head>
"""


def nav(page, dark=False):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{h}"{cur if h == page else ""}>{t}</a>' for h, t in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="nav{' on-dark' if dark else ''}">
  <div class="wrap nav-in">
    <a href="index.html" class="brand" aria-label="Sada-e-Rehmat home">
      <img class="logo-ink" src="assets/img/logo-ink.png" alt="" width="637" height="405">
      <img class="logo-white" src="assets/img/logo-white.png" alt="" width="637" height="405">
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span></button>
    <nav class="nav-links" id="nav-links" aria-label="Main">
      {links}
      <a class="btn btn-sm" href="contact.html">Enquire {ARROW}</a>
    </nav>
  </div>
</header>
"""


def footer(cta=True):
    big = ('<p class="footer-big" data-lines>' + lines("Here I am,", "O Allah, <em>here I am.</em>") + '</p>') if cta else ""
    return f"""<footer class="footer">
  <div class="wrap">
    {big}
    <div class="footer-grid">
      <div>
        <a href="index.html" class="brand"><img src="assets/img/logo-white.png" alt="Sada-e-Rehmat" width="637" height="405" loading="lazy"></a>
        <p>Hajj and Umrah journeys from the United Kingdom and Pakistan, planned by people who have walked them.</p>
      </div>
      <div>
        <h4>Journeys</h4>
        <a href="packages.html#sakinah">Sakinah</a>
        <a href="packages.html#noor">Noor</a>
        <a href="packages.html#rahmah">Rahmah</a>
        <a href="packages.html#firdaus">Firdaus</a>
        <a href="packages.html#umrah">Umrah</a>
      </div>
      <div>
        <h4>Explore</h4>
        <a href="gallery.html">Sacred sites</a>
        <a href="guides.html">Guides</a>
        <a href="about-us.html">About us</a>
        <a href="contact.html">Contact</a>
      </div>
      <div>
        <h4>Talk to us</h4>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="tel:{PHONE_UK[1]}">UK {PHONE_UK[0]}</a>
        <a href="tel:{PHONE_PK[1]}">Pakistan {PHONE_PK[0]}</a>
        <span>Mon–Fri · 09:00–17:00</span>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Sada-e-Rehmat Ltd · Company no. 16043621</span>
      <nav aria-label="Legal"><a href="privacy-policy.html">Privacy</a><a href="cookie-policy.html">Cookies</a></nav>
    </div>
  </div>
</footer>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie notice">
  <div><strong>Your privacy matters</strong><p>We only use essential browser storage to remember choices like this one. Read our <a href="cookie-policy.html">Cookie Policy</a>.</p></div>
  <div class="actions"><button class="btn btn-sm btn-light" data-cookie="accepted">Accept</button><button class="btn btn-sm btn-ghost-dark" data-cookie="declined">Decline</button></div>
</div>
<script src="script.js" defer></script>
</body>
</html>
"""


def breadcrumbs(fname, name, parent=None):
    items = [("Home", BASE)]
    if parent:
        items.append((parent[0], BASE + parent[1]))
    items.append((name, BASE + fname))
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def ld(*objs):
    return "".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>\n' for o in objs)


def page(fname, title, desc, body, dark_nav=False, extra_head="", cta=True, og=None, crumb=None, og_type="website", index=True, priority=0.6):
    if crumb and fname != "index.html":
        extra_head = ld(breadcrumbs(fname, crumb[0], crumb[1] if len(crumb) > 1 else None)) + extra_head
    if index:
        PAGES_BUILT.append((fname, priority))
    html = head(fname, title, desc, extra_head, og, og_type) + "<body>\n" + nav(fname, dark_nav) + \
        f'<main id="main">\n{body}\n</main>\n' + footer(cta)
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("built", fname)


def cta_band(title, text, img_name, primary=("Plan my Hajj", "contact.html"), secondary=("See the journeys", "packages.html")):
    return f"""<section class="section-tight">
  <div class="wrap">
    <div class="cta">
      <div class="bg">{img(img_name, "", "100vw")}</div>
      <div data-reveal>
        <h2 class="display-l">{title}</h2>
        <p>{text}</p>
        <div class="actions"><a class="btn btn-light" href="{primary[1]}">{primary[0]} {ARROW}</a><a class="btn btn-ghost-dark" href="{secondary[1]}">{secondary[0]}</a></div>
      </div>
    </div>
  </div>
</section>"""


def offices(maps=True):
    map_uk = '<iframe title="Map of the Feltham office" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=685+Staines+Rd%2C+Feltham+TW14+8PA%2C+United+Kingdom&amp;output=embed"></iframe>'
    map_pk = '<iframe title="Map of the Rawalpindi office" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=20D+Mini+Commercial+Phase+7%2C+Bahria+Sector+F+Town%2C+Rawalpindi%2C+44000&amp;output=embed"></iframe>'
    return f"""<div class="offices" data-stagger>
  <article class="office" data-reveal>
    <div class="office-top">
      <span class="flag">United Kingdom</span>
      <h3>Feltham</h3>
      <p>685 Staines Road, Feltham TW14 8PA</p>
      <div class="office-links"><a class="link" href="tel:{PHONE_UK[1]}">{PHONE_UK[0]}</a><a class="link" href="https://www.google.com/maps/dir/?api=1&amp;destination=685+Staines+Rd+Feltham+TW14+8PA" target="_blank" rel="noopener">Directions ↗</a></div>
    </div>
    {map_uk if maps else ""}
  </article>
  <article class="office" data-reveal>
    <div class="office-top">
      <span class="flag">Pakistan</span>
      <h3>Rawalpindi</h3>
      <p>20D Mini Commercial, Phase 7, Bahria Town Sector F, Rawalpindi</p>
      <div class="office-links"><a class="link" href="tel:{PHONE_PK[1]}">{PHONE_PK[0]}</a><a class="link" href="https://www.google.com/maps/dir/?api=1&amp;destination=20D+Mini+Commercial+Phase+7+Bahria+Town+Rawalpindi" target="_blank" rel="noopener">Directions ↗</a></div>
    </div>
    {map_pk if maps else ""}
  </article>
</div>"""


from guides_a import GUIDES_A
from guides_b import GUIDES_B

ALL_GUIDES = GUIDES_A + GUIDES_B
GUIDE = {g["slug"]: g for g in ALL_GUIDES}
CATS = {"umrah": "Umrah", "hajj": "Hajj", "planning": "Planning", "health": "Health"}
GUIDE_ORDER = ["guide-first-umrah", "guide-hajj-step-by-step", "guide-ihram", "guide-miqat", "guide-duas",
               "guide-umrah-visa", "guide-hajj-uk", "guide-hajj-pakistan", "guide-women", "guide-madinah",
               "guide-best-time-umrah", "guide-health", "guide-packing", "guide-types-of-hajj",
               "guide-ziyarat-makkah", "guide-documents", "guide-choosing", "guide-safety"]
UPDATED = "2026-11-19"


def strip(html):
    return re.sub(r"<[^>]+>", "", html).replace("&amp;", "&")


def short_title(g):
    return strip(g["h1"]).rstrip(".")


def guide_cards(slugs, filterable=False):
    out = []
    for slug in slugs:
        g = GUIDE[slug]
        cat = f' data-cat="{g["cat"]}"' if filterable else ""
        out.append(f"""<a class="guide-card" href="{slug}.html"{cat} data-reveal>
  <div class="media">{img(g["image"], "", "(max-width: 640px) 100vw, 33vw")}</div>
  <div class="body"><div class="meta"><small>{g["eyebrow"]}</small><span>{g["minutes"]} min read</span></div><h3>{short_title(g)}</h3><p>{g["og"]}</p><span class="link">Read the guide {ARROW}</span></div>
</a>""")
    return '<div class="guide-grid" data-stagger>' + "".join(out) + "</div>"


def scrolly(steps, dark=False, aria="Story"):
    """steps: (label, k, h3, p, frame, facts). frame = ("img", name) | ("type", arabic, sub)."""
    frames, items = [], []
    for i, (label, k, h3, p, frame, facts) in enumerate(steps):
        if frame[0] == "img":
            frames.append(f'<div class="scrolly-frame">{img(frame[1], "", "(max-width: 860px) 100vw, 50vw")}</div>')
        else:
            frames.append(f'<div class="scrolly-frame type"><span class="ar" lang="ar">{frame[1]}</span><span class="sub">{frame[2]}</span></div>')
        chips = "".join(f"<span>{f}</span>" for f in (facts or []))
        hud = "" if frame[0] == "type" else strip(label)
        items.append(f"""<article class="scrolly-step" data-label="{escape(hud)}">
  <span class="k">{k}</span><h3>{h3}</h3><p>{p}</p>{f'<div class="facts">{chips}</div>' if chips else ''}
</article>""")
    n = len(steps)
    return f"""<div class="scrolly" aria-label="{escape(aria)}">
  <div class="scrolly-pin"><div class="scrolly-stage">
    {"".join(frames)}
    <div class="scrolly-bar" aria-hidden="true"><span></span></div>
    <div class="scrolly-hud" aria-hidden="true"><span class="count"><b>01</b><small>/{n:02d}</small></span><span class="label"></span></div>
  </div></div>
  <div class="scrolly-steps">{"".join(items)}</div>
</div>"""


KIND_FRAME = {"arrive": ("img", "madinah"), "madinah": ("img", "madinah"), "makkah": ("img", "holy-kaaba"),
              "aziziya": ("img", "mina-tents"), "hajj": ("img", "arafat"), "depart": ("img", "kaaba-tawaf")}


def journey_scrolly(pkg_id, dark=False):
    """Scrolly built from a real itinerary in data.py."""
    p = next(x for x in PACKAGES if x["id"] == pkg_id)
    steps = []
    for i, st in enumerate(p["stops"]):
        kind = st["kind"]
        frame = KIND_FRAME[kind]
        if kind == "arrive" and "Makkah" in st["label"]:
            frame = ("img", "kaaba-tawaf")
        if kind == "depart":
            frame = ("type", "رِحْلَةٌ مُبَارَكَة", "A blessed journey home")
        facts = [f'{st["greg"]} 2027', st["hijri"]]
        text = {
            "arrive": "Our team meets you at the airport and takes you to your hotel. " + ("Madinah first: no Ihram needed on the flight." if "Madinah" in st["label"] else "You land in Ihram and perform your Umrah."),
            "madinah": f'Nights at {p["madinah"][0][0]} on {p["madinah"][1].lower()}, a short walk from Masjid an-Nabawi, with time for the Rawdah, Quba and Uhud.',
            "makkah": (f'Nights at {p["makkah"][0][0]} on {p["makkah"][1].lower()}, beside Masjid al-Haram, so you can pray in the Haram before the days of Hajj.' if p["makkah"] else ""),
            "aziziya": "Aziziya, close to Mina, on full board, in rooms with attached bathrooms and hot and cold drinks around the clock.",
            "hajj": "Maktab A in Zone 1: gypsum-walled tents with sofa-beds in Mina, A/C marquees in Arafat, the Muzdalifah kit, and the shortest walk to the Jamarat.",
            "depart": "Tawaf al-Wada' and home, " + ("from Jeddah." if "Jeddah" in st["label"] else "from Madinah, after your days at the Prophet's Mosque ﷺ."),
        }[kind]
        short = {"arrive": "Arrival", "madinah": "Madinah", "makkah": "Makkah", "aziziya": "Aziziya",
                 "hajj": "The days of Hajj", "depart": "Departure"}[kind]
        steps.append((short, f'{st["greg"]} · {st["hijri"]}', st["label"], text, frame, facts))
    return scrolly(steps, dark, aria=f"{pkg_name(p)} itinerary")


FAQ = [
    ("What is the difference between Hajj and Umrah?", "Hajj is the annual pilgrimage with fixed dates in Dhul Hijjah and is obligatory once for those able. Umrah is shorter and can be performed at any time of the year."),
    ("What does Maktab A, Zone 1 mean?", "Maktabs are the official service categories in Mina and Arafat. Category A is the highest standard, and Zone 1 is the closest area to the Jamarat, which means shorter walks on the days of stoning."),
    ("Are flights included?", "No. Every Hajj 2027 price is per person and excludes airfare and Qurbani, so you can fly from the UK or Pakistan on the airline that suits you. Our team can advise on flights that fit your arrival date."),
    ("What is the difference between Madinah first and Makkah first?", "Madinah first means you visit the Prophet's Mosque before Hajj and fly home from Jeddah. Makkah first means you begin in Makkah, perform Hajj, then travel to Madinah by the Haramain train and fly home from Madinah."),
    ("Is the Aziziya room shared?", "Yes, by default. Aziziya rooms have five beds, are gender-segregated and have attached bathrooms. You can add a private quad, triple or double room for an extra charge."),
    ("Can the dates change?", "The itinerary follows the Saudi Hijri calendar, so dates may move by one day with the moon sighting and flight schedules. We confirm everything in writing at booking."),
    ("Do you arrange Umrah too?", "Yes, year-round, including Ramadan. Umrah journeys are shaped around your dates, hotel preference and group size, so we quote each one individually."),
]


def faq_block():
    items = "".join(
        f'<details><summary>{q}<span class="plus" aria-hidden="true"></span></summary><div class="ans"><p>{a}</p></div></details>'
        for q, a in FAQ)
    return f'<div class="faq" data-reveal>{items}</div>'


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------
def build_home():
    mins = {}
    for p in PACKAGES:
        m = mins.setdefault(p["tier"], {"gbp": 10**12, "usd": 10**9, "days": set()})
        m["gbp"] = min(m["gbp"], p["gbp"][0])
        m["usd"] = min(m["usd"], p["usd"][0])
        m["days"].add(p["days"])

    stack = []
    for i, c in enumerate(COLLECTIONS):
        m = mins[c["id"]]
        days = sorted(m["days"], key=lambda d: int(d.split("–")[-1]))
        meta = "".join(f"<span>{d} days</span>" for d in days)
        stack.append(f"""<article class="stack-card tier-{c['id']}" style="--i:{i}">
  <div class="stack-copy">
    <span class="tier-ar arabic" lang="ar">{c['arabic']}</span>
    <div><span class="eyebrow">{c['meaning']}</span></div>
    <h3>{c['name']}</h3>
    <p>{c['line']}</p>
    <div class="stack-meta">{meta}</div>
    <div class="stack-price">
      <div><small>From, per person</small><strong>{gbp(m['gbp'])}<span>≈ {usd(m['usd'])}</span></strong></div>
      <a class="btn" href="packages.html#{c['id']}">Explore {c['name']} {ARROW}</a>
    </div>
  </div>
  <div class="stack-media">{img(c['image'], "", "(max-width: 860px) 100vw, 50vw")}</div>
</article>""")

    body = f"""
<section class="cine" aria-label="Introduction">
  <div class="cine-sticky">
    <div class="cine-frame">{img("kaaba-tawaf", "Pilgrims performing Tawaf around the Kaaba at dusk", "100vw", eager=True)}</div>
    <div class="cine-copy">
      <div class="wrap cine-a" data-enter>
        <span class="arabic" lang="ar">لَبَّيْكَ ٱللَّٰهُمَّ لَبَّيْكَ</span>
        <h1 class="display-xl">Hajj 2027, arranged with <em>care.</em></h1>
        <p class="lead">Category A tents in Zone 1, the Haramain train between the holy cities, and a team in Feltham and Rawalpindi who pick up when you call.</p>
        <div class="actions"><a class="btn btn-light" href="packages.html">See the 2027 journeys {ARROW}</a><a class="btn btn-ghost-dark" href="contact.html">Speak to us</a></div>
      </div>
    </div>
    <div class="cine-b"><p>Twelve journeys. Four collections. One calling.<small>The Hajj 2027 collection</small></p></div>
    <span class="scroll-cue" aria-hidden="true"></span>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Hajj 2027 · Category A</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("Four collections,", "<em>one standard.</em>")}</h2></div>
      <p class="lead" data-reveal>Every journey includes Maktab A in Zone 1, Aziziya on full board and the Haramain train. What changes is where you sleep, and for how long.</p>
    </div>
    <div class="stack">{"".join(stack)}</div>
  </div>
</section>

<section class="section sand" aria-label="A real Hajj 2027 itinerary">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Noor 17 · Madinah first</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("Seventeen days,", "<em>one at a time.</em>")}</h2></div>
      <p class="lead" data-reveal>A real 2027 itinerary, stop by stop.</p>
    </div>
    {journey_scrolly("noor-17-madinah")}
    <div class="actions" style="margin-top:8px"><a class="btn" href="packages.html#noor-17-madinah">See Noor 17 {ARROW}</a><a class="btn btn-ghost" href="packages.html#compare">Compare journeys</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Included in every journey</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("The comfort you", "<em>don't have to ask for.</em>")}</h2></div>
      <p class="lead" data-reveal>Standard on every 2027 journey.</p>
    </div>
    <div class="bento" data-stagger>
      <article class="tile tile-dark span-2 row-2" data-reveal>
        <span class="big" style="color:var(--gold-2)">A</span>
        <h3>Maktab A, Zone 1</h3>
        <p>The top category, closest to the Jamarat.</p>
      </article>
      <article class="tile tile-photo span-4" data-reveal>
        {img("madinah", "Masjid an-Nabawi in Madinah", "(max-width: 960px) 100vw, 66vw")}
        <div><h3>Haramain high-speed train</h3><p>Makkah to Madinah in under three hours.</p></div>
      </article>
      <article class="tile span-2" data-reveal><span class="ico">{icon("tent")}</span><h3>Gypsum-walled Mina tents</h3><p>Sofa-beds and private washrooms.</p></article>
      <article class="tile span-2" data-reveal><span class="ico">{icon("snow")}</span><h3>A/C marquees in Arafat</h3><p>Cool, with sofa mattresses.</p></article>
      <article class="tile tile-gold span-3" data-reveal><span class="ico" style="background:#fff">{icon("meal")}</span><h3>Buffet meals, and drinks all day</h3><p>Buffets in Mina, Arafat and Aziziya, drinks 24/7.</p></article>
      <article class="tile span-3" data-reveal><span class="ico">{icon("bus")}</span><h3>Private air-conditioned buses</h3><p>For every transfer.</p></article>
      <article class="tile span-3" data-reveal><span class="ico">{icon("bath")}</span><h3>Aziziya, with attached baths</h3><p>Close to Mina, on full board.</p></article>
      <article class="tile span-3" data-reveal><span class="ico">{icon("kit")}</span><h3>The Muzdalifah kit</h3><p>Mats, sleeping bags, snacks.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="media" data-parallax data-clip>{img("arafat", "Pilgrims on the plain of Arafat", "(max-width: 860px) 100vw, 50vw")}</div>
    <div class="split-copy">
      <span class="eyebrow" data-reveal>Why families choose us</span>
      <h2 class="display-m" data-lines>{lines("We name the hotel.", "<em>Then we keep our word.</em>")}</h2>
      <p data-reveal>Hotels, board, rooms and dates in writing before you pay. No "or similar". And the team that plans your journey is with you on the ground.</p>
      <div data-reveal><a class="btn btn-ghost" href="about-us.html">Our story {ARROW}</a></div>
    </div>
  </div>
  <div class="wrap" style="margin-top:clamp(72px,9vw,120px)">
    <div class="stats" data-stagger>
      <div class="stat" data-reveal><strong data-count="15000" data-suffix="+">15,000+</strong><span>Pilgrims guided</span></div>
      <div class="stat" data-reveal><strong data-count="12">12</strong><span>Years of service</span></div>
      <div class="stat" data-reveal><strong data-count="98" data-suffix="%">98%</strong><span>Would recommend us</span></div>
      <div class="stat" data-reveal><strong>24/7</strong><span>Support on the ground</span></div>
    </div>
  </div>
</section>

<section class="section sand" id="offices">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Two offices, one team</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("Feltham to Rawalpindi,", "<em>then to the Haram.</em>")}</h2></div>
      <p class="lead" data-reveal>Call in, or call us. English and Urdu.</p>
    </div>
    {offices(maps=False)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Guides</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("Prepare with", "<em>a calm mind.</em>")}</h2></div>
      <p class="lead" data-reveal>Short, practical, and checked for 2026–27.</p>
    </div>
    {guide_cards(["guide-first-umrah", "guide-hajj-step-by-step", "guide-umrah-visa"])}
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap-narrow">
    <div class="head center"><span class="eyebrow" data-reveal style="justify-self:center">Questions</span><h2 class="display-m" data-lines>{lines("Asked, and answered.")}</h2></div>
    {faq_block()}
  </div>
</section>

{cta_band("Begin your <em>Hajj 2027</em> journey.", "Places in Maktab A are limited each season. Tell us your dates and who is travelling, and we will hold the right journey for you.", "holy-kaaba")}
"""
    ld_org = {
        "@context": "https://schema.org", "@type": "TravelAgency", "name": "Sada-e-Rehmat",
        "url": BASE, "logo": BASE + "assets/sada-e-rehmat-logo.png", "image": BASE + "assets/img/kaaba-tawaf-2000.webp",
        "description": "Hajj and Umrah packages from the United Kingdom and Pakistan. Hajj 2027 Category A journeys with Maktab A in Zone 1.",
        "areaServed": ["United Kingdom", "Pakistan"], "email": EMAIL,
        "address": [
            {"@type": "PostalAddress", "streetAddress": "685 Staines Road", "addressLocality": "Feltham", "postalCode": "TW14 8PA", "addressCountry": "GB"},
            {"@type": "PostalAddress", "streetAddress": "20D Mini Commercial Phase 7, Bahria Sector F Town", "addressLocality": "Rawalpindi", "postalCode": "44000", "addressCountry": "PK"}],
        "telephone": [PHONE_UK[1], PHONE_PK[1]],
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    site_ld = {"@context": "https://schema.org", "@type": "WebSite", "name": "Sada-e-Rehmat", "url": BASE, "inLanguage": "en-GB"}
    page("index.html", "Hajj 2027 & Umrah Packages from the UK and Pakistan | Sada-e-Rehmat",
         "Hajj 2027 Category A packages from the UK and Pakistan: Maktab A in Zone 1, Aziziya on full board, Swissôtel Makkah, Maysan Al Harithia Madinah and the Haramain train.",
         body, dark_nav=True, extra_head=ld(ld_org, site_ld, faq_ld), priority=1.0,
         og=dict(image="kaaba-tawaf", eyebrow="Hajj 2027 · Category A", title="Hajj 2027, arranged with care.",
                 detail="Maktab A · Zone 1 · Feltham & Rawalpindi", chips=["Sakinah", "Noor", "Rahmah", "Firdaus"], theme="hero"))


# --------------------------------------------------------------------------
# Packages
# --------------------------------------------------------------------------
KIND_ICON = {"arrive": "Arrive", "madinah": "Madinah", "makkah": "Makkah", "aziziya": "Aziziya", "hajj": "Hajj", "depart": "Depart"}


def pkg_card(p):
    c = COLL[p["tier"]]
    stays = []
    if p["makkah"]:
        (h, _), board = p["makkah"]
        stays.append(("Makkah", h.split(" or ")[0], board))
    else:
        stays.append(("Makkah", "Aziziya", "Full board"))
    (h, _), board = p["madinah"]
    stays.append(("Madinah", h, board))
    dl = "".join(f'<div><dt>{a}</dt><dd>{b}<small>{x}</small></dd></div>' for a, b, x in stays)
    tl = "".join(
        f'<li class="{s["kind"]}" style="--i:{i}"><b>{s["label"]}</b><span>{s["greg"]} 2027 · <span class="hijri">{s["hijri"]}</span></span></li>'
        for i, s in enumerate(p["stops"]))
    attrs = " ".join(
        f'data-{room}-{cur}="{val}"'
        for cur in ("gbp", "usd")
        for room, val in zip(("quad", "triple", "double"), p[cur]))
    first, last = p["stops"][0], p["stops"][-1]
    return f"""<article class="pkg" id="{p['id']}" data-route="{p['route']}" data-price {attrs} data-reveal>
  <div class="pkg-top">
    <div><span class="pkg-tag">{route_label(p)}</span><h3>{pkg_name(p)}</h3></div>
    <div class="pkg-days"><strong>{p['days']}</strong><span>days</span></div>
  </div>
  <div class="pkg-route">{icon("route")}<span><b>{first['greg']}</b> {first['label'].replace('Arrive in ', '')} → <b>{last['greg']}</b> {last['label'].replace('Depart from ', '')}</span></div>
  <dl class="pkg-stays">{dl}</dl>
  <details>
    <summary>Itinerary <span class="plus" aria-hidden="true"></span></summary>
    <ol class="timeline">{tl}</ol>
  </details>
  <div class="pkg-price">
    <div><small class="room-label">Quad room · per person</small><div class="amount">{gbp(p['gbp'][0])}</div><div class="alt">≈ {usd(p['usd'][0])}</div></div>
  </div>
  <div class="pkg-actions"><a class="btn" href="contact.html?package={p['id']}">Enquire {ARROW}</a><button class="btn btn-ghost" type="button" data-compare="{p['id']}">Compare</button></div>
</article>"""


def seg(name, options, label):
    btns = "".join(f'<button type="button" data-value="{v}" aria-pressed="{str(i == 0).lower()}">{t}</button>' for i, (v, t) in enumerate(options))
    return f'<div class="seg" data-name="{name}" role="group" aria-label="{label}">{btns}</div>'


def compare_data():
    out = []
    for p in PACKAGES:
        c = COLL[p["tier"]]
        def stay(kind):
            st = [x for x in p["stops"] if x["kind"] == kind]
            return " & ".join(x["greg"] for x in st)
        mk = (f'{p["makkah"][0][0].split(" or ")[0]} · {p["makkah"][1]}' if p["makkah"] else "No hotel stay (Aziziya)")
        out.append(dict(
            id=p["id"], name=pkg_name(p), tier=c["name"], tid=c["id"], route=route_label(p), days=p["days"] + " days",
            arrive=f'{p["stops"][0]["greg"]} · {p["stops"][0]["label"].replace("Arrive in ", "")}',
            depart=f'{p["stops"][-1]["greg"]} · {p["stops"][-1]["label"].replace("Depart from ", "")}',
            makkah=mk, makkahDates=stay("makkah") or "—",
            madinah=f'{p["madinah"][0][0]} · {p["madinah"][1]}', madinahDates=stay("madinah"),
            aziziya=stay("aziziya"), train=p["train"],
            gbp=list(p["gbp"]), usd=list(p["usd"]),
            upgrade=("Maysan upgrade available" if p["upgrade"] else ("Already Maysan Al Harithia" if "Maysan" in p["madinah"][0][0] else "—")),
        ))
    return out


def build_packages():
    tabs = "".join(f'<a href="#{c["id"]}" style="--dot:var(--t-{c["id"]})">{c["name"]}</a>' for c in COLLECTIONS)
    tabs += '<a href="#compare" style="--dot:var(--gold)">Compare</a>'
    controls = (seg("route", [("all", "All"), ("madinah", "Madinah first"), ("makkah", "Makkah first")], "Route")
                + seg("room", [("quad", "Quad"), ("triple", "Triple"), ("double", "Double")], "Room")
                + seg("cur", [("gbp", "GBP"), ("usd", "USD")], "Currency"))

    secs = []
    for c in COLLECTIONS:
        pk = [p for p in PACKAGES if p["tier"] == c["id"]]
        cards = "".join(pkg_card(p) for p in pk)
        chips = "".join(f'<span class="chip chip-ink">{h}</span>' for h in c["hotels"])
        secs.append(f"""<section class="tier-sec t-{c['id']}" id="{c['id']}">
  <div class="wrap">
    <div class="tier-intro">
      <div>
        <div class="tier-word"><h2 class="display-l">{c['name']}</h2><span class="arabic" lang="ar">{c['arabic']}</span></div>
        <span class="meaning">{c['meaning']} · {len(pk)} journeys</span>
      </div>
      <div data-reveal><p>{c['line']}</p><div class="tier-hotels">{chips}</div></div>
    </div>
    <div class="pkg-grid" data-stagger>{cards}</div>
    <p class="empty-note">No {c['name']} journey on this route. Switch the route to <b>All</b>.</p>
  </div>
</section>""")

    rows = []
    for c in COLLECTIONS:
        for p in [x for x in PACKAGES if x["tier"] == c["id"]]:
            cells = "".join(
                f'<td class="num" data-cell="{room}" data-gbp="{p["gbp"][i]}" data-usd="{p["usd"][i]}">{gbp(p["gbp"][i])}</td>'
                for i, room in enumerate(("quad", "triple", "double")))
            mk = p["makkah"][0][0].split(" or ")[0] if p["makkah"] else "Aziziya"
            rows.append(f'<tr data-route="{p["route"]}" style="--dot:var(--t-{c["id"]})"><td><i></i><a href="#{p["id"]}">{pkg_name(p)}</a></td><td>{route_label(p)}</td><td>{p["days"]} days</td><td>{p["stops"][0]["greg"]}</td><td>{mk}</td><td>{p["madinah"][0][0]}</td>{cells}</tr>')
    opts = "".join(f'<optgroup label="{c["name"]}">' + "".join(
        f'<option value="{p["id"]}">{pkg_name(p)} · {route_label(p)}</option>' for p in PACKAGES if p["tier"] == c["id"]) + "</optgroup>"
        for c in COLLECTIONS)
    defaults = ["sakinah-14-madinah", "noor-17-madinah", "firdaus-14-madinah"]
    selects = "".join(f'<label class="cmp-pick"><span>Journey {i+1}</span><select data-slot="{i}">{opts.replace(f"value=\"{d}\"", f"value=\"{d}\" selected")}</select></label>' for i, d in enumerate(defaults))
    compare = f"""<section class="section" id="compare">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Compare</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("Side by side,", "<em>line by line.</em>")}</h2></div>
      <p class="lead" data-reveal>Pick three journeys. A gold dot marks what differs.</p>
    </div>
    <div class="cmp" data-reveal>
      <div class="cmp-picks">{selects}</div>
      <div class="cmp-grid" aria-live="polite"></div>
    </div>
    <details class="all-table">
      <summary>All twelve journeys in one table <span class="plus" aria-hidden="true"></span></summary>
      <div class="compare-wrap">
        <table class="compare">
          <thead><tr><th>Journey</th><th>Route</th><th>Length</th><th>Arrive</th><th>Makkah</th><th>Madinah</th><th class="num" data-room="quad">Quad</th><th class="num" data-room="triple">Triple</th><th class="num" data-room="double">Double</th></tr></thead>
          <tbody>{"".join(rows)}</tbody>
        </table>
      </div>
    </details>
    <p class="muted" style="font-size:14px;margin-top:20px">Per person, excluding airfare and Qurbani. {RATE_NOTE}</p>
  </div>
</section>
<script type="application/json" id="cmp-data">{json.dumps(compare_data(), ensure_ascii=False)}</script>"""

    def addon_rows(d):
        return "".join(
            f'<tr><td>{room}</td><td data-addon data-gbp="{d["gbp"][i]}" data-usd="{d["usd"][i]}">{gbp(d["gbp"][i])}</td></tr>'
            for i, room in enumerate(("Quad", "Triple", "Double")))
    upg = [p for p in PACKAGES if p["upgrade"]]
    upg_rows = "".join(
        f'<tr><td><a href="#{p["id"]}">{pkg_name(p)}</a> <span class="muted">· {route_label(p).split()[0]}</span></td>'
        + "".join(f'<td data-addon data-gbp="{p["upgrade"]["gbp"][i]}" data-usd="{p["upgrade"]["usd"][i]}">{gbp(p["upgrade"]["gbp"][i])}</td>' for i in range(3))
        + '</tr>' for p in upg)
    addons = f"""<section class="section sand">
  <div class="wrap">
    <div class="head"><span class="eyebrow" data-reveal>Upgrades</span><h2 class="display-m" data-lines>{lines("Make it <em>yours.</em>")}</h2></div>
    <div class="addons" data-stagger>
      <article class="addon" data-reveal>
        <h3>Private room in Aziziya</h3>
        <p>Aziziya rooms are shared by five by default. Keep your family together.</p>
        <table><thead><tr><th>Room</th><th>Extra per person</th></tr></thead><tbody>{addon_rows(AZIZIYA_PRIVATE)}</tbody></table>
      </article>
      <article class="addon" data-reveal>
        <h3>Maysan Al Harithia, Madinah</h3>
        <p>Upgrade from Shaza Regency, on half board.</p>
        <div class="table-scroll"><table><thead><tr><th>Journey</th><th>Quad</th><th>Triple</th><th>Double</th></tr></thead><tbody>{upg_rows}</tbody></table></div>
      </article>
    </div>
  </div>
</section>"""

    inc = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in INCLUDED)
    terms = "".join(f'<li><b>{a}</b> {b}</li>' for a, b in TERMS)
    included = f"""<section class="section dark">
  <div class="wrap">
    <div class="head"><span class="eyebrow" data-reveal>Every journey</span><h2 class="display-m" data-lines>{lines("What's <em>included.</em>")}</h2></div>
    <ul class="inc-grid" data-reveal>{inc}</ul>
    <details class="all-table dark-details">
      <summary>Good to know: terms and exclusions <span class="plus" aria-hidden="true"></span></summary>
      <ul class="terms">{terms}</ul>
    </details>
  </div>
</section>"""

    umrah = f"""<section class="section" id="umrah">
  <div class="wrap split">
    <div class="split-copy">
      <span class="eyebrow" data-reveal>Umrah · all year</span>
      <h2 class="display-l" data-lines>{lines("Umrah, around", "<em>your dates.</em>")}</h2>
      <p data-reveal>Tell us when, which hotels and who's coming. We'll price it, usually within a day.</p>
      <div class="actions" data-reveal><a class="btn" href="contact.html">Ask for an Umrah quote {ARROW}</a></div>
    </div>
    <div class="media" data-parallax data-clip>{img("safa-marwa", "Pilgrims walking between Safa and Marwa", "(max-width: 860px) 100vw, 50vw")}</div>
  </div>
</section>"""

    low = min(p["gbp"][0] for p in PACKAGES)
    body = f"""
<section class="page-hero">
  <div class="bg">{img("holy-kaaba", "The Kaaba in Masjid al-Haram", "100vw", eager=True)}</div>
  <div class="wrap" data-enter>
    <span class="eyebrow" style="color:var(--gold-2)">Hajj 2027 · Category A</span>
    <h1 class="display-xl" style="margin-top:18px">Twelve ways to <em>answer the call.</em></h1>
    <p class="lead">Every journey: Maktab A in Zone 1, Aziziya on full board, the Haramain train.</p>
    <div class="hero-facts" style="margin-top:28px"><span class="chip">From {gbp(low)} pp</span><span class="chip">10 to 23 days</span><span class="chip">Excludes airfare</span></div>
  </div>
</section>

<div data-explorer>
<div class="tier-nav">
  <div class="wrap tier-nav-in">
    <nav class="tier-tabs" aria-label="Collections">{tabs}</nav>
    <div class="controls">{controls}</div>
  </div>
</div>
{"".join(secs)}
{compare}
{addons}
{included}
</div>
{umrah}
{cta_band("Not sure which <em>journey fits?</em>", "Tell us your dates and budget. We'll recommend one, and say why.", "maqam-ibrahim", ("Get a recommendation", "contact.html"), ("How to compare", "guide-choosing.html"))}
"""
    page("packages.html", "Hajj 2027 Packages from £5,935: Sakinah, Noor, Rahmah & Firdaus | Sada-e-Rehmat",
         "Compare twelve Hajj 2027 Category A journeys from 10 to 23 days, side by side. Maktab A Zone 1, Swissôtel Makkah, Maysan Al Harithia and Shaza Regency Madinah. Prices in GBP and USD.",
         body, dark_nav=True, crumb=("Hajj 2027 packages",), priority=0.95, extra_head=ld(trips_ld()),
         og=dict(image="holy-kaaba", eyebrow="Hajj 2027 packages", title="Twelve ways to answer the call.",
                 detail=f"From {gbp(low)} per person · compare side by side", chips=["Sakinah", "Noor", "Rahmah", "Firdaus"], theme="packages"))


def trips_ld():
    items = []
    for i, p in enumerate(PACKAGES):
        c = COLL[p["tier"]]
        items.append({"@type": "ListItem", "position": i + 1, "item": {
            "@type": "TouristTrip", "name": f"{pkg_name(p)} · {route_label(p)} · Hajj 2027",
            "description": f'{p["days"]}-day Hajj 2027 journey, {c["name"]} collection. Maktab A, Zone 1.',
            "url": f"{BASE}packages.html#{p['id']}", "touristType": "Hajj pilgrims",
            "offers": {"@type": "Offer", "price": p["gbp"][0], "priceCurrency": "GBP",
                       "availability": "https://schema.org/InStock", "url": f"{BASE}packages.html#{p['id']}"}}})
    return {"@context": "https://schema.org", "@type": "ItemList", "name": "Hajj 2027 packages", "itemListElement": items}


# --------------------------------------------------------------------------
# Sacred sites
# --------------------------------------------------------------------------
SITES_HAJJ = [
    ("kaaba-tawaf", "Makkah", "The Kaaba & Tawaf", "The heart of the journey, where every circle is a prayer. Hajj begins and ends here."),
    ("mina-tents", "Mina", "Mina, the city of tents", "On 8 Dhul Hijjah pilgrims move to Mina. Our Maktab A tents sit in Zone 1, closest to the Jamarat."),
    ("arafat", "Mount Arafat", "The plain of Arafat", "The 9th of Dhul Hijjah. A day of standing, prayer and forgiveness, and the essence of Hajj itself."),
    ("muzdalifah", "Between Arafat and Mina", "Muzdalifah", "A night beneath the open sky, gathering pebbles and strength for the days ahead."),
    ("jamarat", "Mina", "The Jamarat", "Over three days, pilgrims stone the pillars in remembrance of Ibrahim's resolve."),
]
SITES_UMRAH = [
    ("holy-kaaba", "Masjid al-Haram", "The Holy Kaaba", "The sacred centre of Makkah and the direction of every prayer on earth."),
    ("maqam-ibrahim", "Beside the Kaaba", "Maqam Ibrahim", "The station of Ibrahim, where pilgrims pray two rak'ahs after Tawaf."),
    ("zamzam", "Masjid al-Haram", "Zamzam", "The well that has given water since the time of Hajar and Isma'il."),
    ("safa-marwa", "Masjid al-Haram", "Safa & Marwa", "The walk of Hajar between two hills, retraced by every pilgrim in Sa'i."),
    ("madinah", "Madinah", "Masjid an-Nabawi", "The Prophet's Mosque ﷺ, and the peace of the city that welcomed him."),
]


def site_grid(items, start=1):
    out = []
    for i, (im, where, title, text) in enumerate(items):
        out.append(f"""<article class="site" data-reveal>
  <div class="media hover-zoom">{img(im, title, "(max-width: 760px) 100vw, 50vw")}</div>
  <div class="site-copy"><span class="num">{i + start:02d} · {where}</span><h3>{title}</h3><p>{text}</p></div>
</article>""")
    return '<div class="site-grid" data-stagger>' + "".join(out) + "</div>"


def build_gallery():
    body = f"""
<section class="page-hero">
  <div class="bg">{img("arafat", "Pilgrims on the plain of Arafat", "100vw", eager=True)}</div>
  <div class="wrap" data-enter>
    <span class="eyebrow" style="color:var(--gold-2)">Sacred sites</span>
    <h1 class="display-xl" style="margin-top:18px">The places that <em>call you.</em></h1>
    <p class="lead">Ten sites, from the Kaaba to the Prophet's Mosque ﷺ.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="head head-split"><div><span class="eyebrow" data-reveal>Hajj</span><h2 class="display-m" data-lines style="margin-top:14px">{lines("Five days, <em>five places.</em>")}</h2></div>
    <p class="lead" data-reveal>8 to 13 Dhul Hijjah. <a class="link" href="guide-hajj-step-by-step.html">Hajj day by day {ARROW}</a></p></div>
    {site_grid(SITES_HAJJ)}
  </div>
</section>
<section class="section sand">
  <div class="wrap">
    <div class="head head-split"><div><span class="eyebrow" data-reveal>Umrah & Madinah</span><h2 class="display-m" data-lines style="margin-top:14px">{lines("Any month, <em>any year.</em>")}</h2></div>
    <p class="lead" data-reveal>The Haram, then the city of the Prophet ﷺ. <a class="link" href="guide-first-umrah.html">Umrah step by step {ARROW}</a></p></div>
    {site_grid(SITES_UMRAH, 6)}
  </div>
</section>
{cta_band("Ready to stand <em>here yourself?</em>", "We'll plan the journey that brings you here.", "kaaba-tawaf")}
"""
    page("gallery.html", "Hajj & Umrah Sacred Sites | Sada-e-Rehmat",
         "Explore the sacred sites of Hajj and Umrah: the Kaaba, Mina, Arafat, Muzdalifah, the Jamarat, Maqam Ibrahim, Zamzam, Safa and Marwa and Masjid an-Nabawi.",
         body, dark_nav=True, crumb=("Sacred sites",), priority=0.7,
         og=dict(image="arafat", eyebrow="Sacred sites", title="The places that call you.",
                 detail="Ten sites, from the Kaaba to the Prophet's Mosque ﷺ", chips=["Mina", "Arafat", "Muzdalifah", "Jamarat", "Madinah"], theme="sites"))


# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------
def build_about():
    values = [("Care first", "Every pilgrim is treated as family, before, during and after the journey."),
              ("Nothing hidden", "Named hotels, written terms and prices that include what they say."),
              ("Done properly", "Category A service, seasoned guides and logistics checked twice."),
              ("Always reachable", "A bilingual team in the UK, Pakistan and on the ground in Saudi Arabia.")]
    vals = "".join(f'<div class="value" data-reveal><span class="n">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(values))
    steps = [("Tell us about you", "Dates, departure city, who is travelling and what matters most."),
             ("Choose your journey", "We recommend a collection and room type, and explain why."),
             ("Share your documents", "Securely, with a clear list of what is needed for your visa."),
             ("Confirm in writing", "Hotels, dates, rooms and terms, before any payment."),
             ("Prepare together", "Briefings on the rites, packing and health before you fly."),
             ("Travel with us", "Our team meets you and stays with your group throughout.")]
    st = "".join(f'<div class="step" data-reveal><b>0{i+1}</b><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    team = [("D", "Director", "Sets the direction and the standard of care for every pilgrimage."),
            ("C", "Co-founder", "Building a more human, transparent way to plan sacred travel."),
            ("S", "Sohail", "Co-founder, leading operations and the pilgrim experience."),
            ("R", "Rizwan", "Co-founder, leading logistics and journey coordination."),
            ("C", "CEO", "Leads the team with a focus on trust, service and long-term care.")]
    tm = "".join(f'<div class="member" data-reveal><span class="av">{a}</span><h3>{n}</h3><p>{d}</p></div>' for a, n, d in team)
    body = f"""
<section class="page-hero">
  <div class="bg">{img("maqam-ibrahim", "Masjid al-Haram at night", "100vw", eager=True)}</div>
  <div class="wrap" data-enter>
    <span class="eyebrow" style="color:var(--gold-2)">About Sada-e-Rehmat</span>
    <h1 class="display-xl" style="margin-top:18px">The voice of <em>mercy.</em></h1>
    <p class="lead">A Hajj and Umrah specialist with offices in Feltham and Rawalpindi, and twelve years of pilgrims behind us.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head head-split" style="margin-bottom:clamp(40px,5vw,64px)"><h2 class="display-m" data-lines>{lines("Care, clarity", "<em>and devotion.</em>")}</h2>
    <p class="lead" data-reveal>A small team of guides that grew into a full pilgrimage service, trusted by thousands of families.</p></div>
    <div class="stats" data-stagger>
      <div class="stat" data-reveal><strong data-count="15000" data-suffix="+">15,000+</strong><span>Pilgrims guided</span></div>
      <div class="stat" data-reveal><strong data-count="12">12</strong><span>Years of service</span></div>
      <div class="stat" data-reveal><strong data-count="98" data-suffix="%">98%</strong><span>Would recommend us</span></div>
      <div class="stat" data-reveal><strong>2</strong><span>Offices: UK & Pakistan</span></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap split">
    <div class="media" data-parallax data-clip>{img("madinah", "Masjid an-Nabawi in Madinah", "(max-width: 860px) 100vw, 50vw")}</div>
    <div class="split-copy">
      <span class="eyebrow" data-reveal>What we stand for</span>
      <h2 class="display-m" data-lines>{lines("Four promises,", "<em>kept on every journey.</em>")}</h2>
      <p data-reveal>We carry the logistics, so you can carry your intention.</p>
    </div>
  </div>
  <div class="wrap" style="margin-top:clamp(56px,7vw,96px)"><div class="values" data-stagger>{vals}</div></div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>How it works</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("From intention", "<em>to confirmation.</em>")}</h2></div>
      <p class="lead" data-reveal>Six steps, and a named person beside you at each one.</p>
    </div>
    <div class="steps" data-stagger>{st}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>The team</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("People behind", "<em>the journey.</em>")}</h2></div>
      <p class="lead" data-reveal>Travel coordination, customer care and a shared commitment to serving pilgrims with respect.</p>
    </div>
    <div class="team" data-stagger>{tm}</div>
  </div>
</section>

<section class="section sand">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Visit us</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("Our doors", "<em>are open.</em>")}</h2></div>
      <p class="lead" data-reveal>Sada-e-Rehmat Ltd is registered in England and Wales, company no. 16043621.</p>
    </div>
    {offices()}
  </div>
</section>

{cta_band("Begin your <em>blessed journey.</em>", "Join the thousands of families who trusted us with their most sacred trip.", "kaaba-tawaf")}
"""
    page("about-us.html", "About Sada-e-Rehmat | Hajj & Umrah Specialists, UK & Pakistan",
         "Sada-e-Rehmat is a Hajj and Umrah specialist with offices in Feltham, UK and Rawalpindi, Pakistan. Twelve years, 15,000+ pilgrims, and a team with you throughout.",
         body, dark_nav=True, crumb=("About us",), priority=0.8,
         og=dict(image="maqam-ibrahim", eyebrow="About Sada-e-Rehmat", title="The voice of mercy.",
                 detail="12 years · 15,000+ pilgrims · Feltham & Rawalpindi", chips=[], theme="about"))


# --------------------------------------------------------------------------
# Contact
# --------------------------------------------------------------------------
def build_contact():
    opts = ['<option value="">Not sure yet, please advise</option>']
    for c in COLLECTIONS:
        group = "".join(
            f'<option value="{p["id"]}">{pkg_name(p)} · {route_label(p)} · {p["days"]} days</option>'
            for p in PACKAGES if p["tier"] == c["id"])
        opts.append(f'<optgroup label="{c["name"]} — {c["meaning"]}">{group}</optgroup>')
    opts.append('<option value="umrah">Umrah, tailored</option>')
    body = f"""
<section class="page-hero page-hero-plain">
  <div class="wrap" data-enter>
    <span class="eyebrow">Contact</span>
    <h1 class="display-xl" style="margin-top:18px">Let's plan your <em>journey.</em></h1>
    <p class="lead">Send us a few details and a specialist will reply within one working day. Every conversation is free and without obligation.</p>
  </div>
</section>

<section class="section-tight" style="padding-top:0">
  <div class="wrap contact-grid">
    <aside class="contact-side" data-stagger>
      <div class="contact-item" data-reveal><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      <div class="contact-item" data-reveal><small>United Kingdom</small><a href="tel:{PHONE_UK[1]}">{PHONE_UK[0]}</a><span class="muted" style="font-size:16px">685 Staines Road, Feltham</span></div>
      <div class="contact-item" data-reveal><small>Pakistan</small><a href="tel:{PHONE_PK[1]}">{PHONE_PK[0]}</a><span class="muted" style="font-size:16px">Bahria Town Phase 7, Rawalpindi</span></div>
      <div class="contact-item" data-reveal><small>Office hours</small><span>Mon–Fri · 09:00–17:00</span><span class="muted" style="font-size:16px">On-ground support 24/7 while you travel</span></div>
    </aside>
    <form class="form" action="https://formsubmit.co/{EMAIL}" method="POST" data-reveal="scale">
      <input type="hidden" name="_subject" value="New Sada-e-Rehmat pilgrimage enquiry">
      <input type="hidden" name="_next" value="{BASE}thank-you.html">
      <input type="hidden" name="_captcha" value="true">
      <input type="hidden" name="_template" value="table">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <div class="field"><label for="name">Full name *</label><input id="name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="phone">Phone *</label><input id="phone" name="phone" type="tel" autocomplete="tel" required></div>
      <div class="field full"><label for="email">Email *</label><input id="email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="category">Journey</label><select id="category" name="category"><option>Hajj</option><option>Umrah</option><option>Ramadan Umrah</option></select></div>
      <div class="field"><label for="group">Travellers</label><select id="group" name="group_size"><option>1 · Solo</option><option>2 · Couple</option><option>3–5 · Small family</option><option>6–15 · Family or group</option><option>16+ · Large group</option></select></div>
      <div class="field full"><label for="package">Hajj 2027 journey of interest</label><select id="package" name="package">{"".join(opts)}</select></div>
      <div class="field"><label for="room">Room preference</label><select id="room" name="room"><option>Quad</option><option>Triple</option><option>Double</option><option>Not sure</option></select></div>
      <div class="field"><label for="from">Travelling from</label><select id="from" name="departing_from"><option>United Kingdom</option><option>Pakistan</option><option>Elsewhere</option></select></div>
      <div class="field full"><label for="message">Anything we should know?</label><textarea id="message" name="message" placeholder="Preferred dates, mobility needs, questions…"></textarea></div>
      <p class="note">We only use your details to plan your journey. See our <a class="link" href="privacy-policy.html">privacy notice</a>.</p>
      <button class="btn" type="submit">Send enquiry {ARROW}</button>
    </form>
  </div>
</section>

<section class="section sand">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>After you press send</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("What happens", "<em>next.</em>")}</h2></div>
      <p class="lead" data-reveal>No call centre, no pressure.</p>
    </div>
    <div class="steps steps-light" data-stagger>
      <div class="step" data-reveal><b>01</b><h3>We reply</h3><p>Within one working day, by phone or email, in English or Urdu.</p></div>
      <div class="step" data-reveal><b>02</b><h3>One recommendation</h3><p>A journey for your dates and budget, with hotels named and exclusions listed.</p></div>
      <div class="step" data-reveal><b>03</b><h3>Paperwork</h3><p>A checklist: passport, visa route, Nusuk, and the ACWY certificate.</p></div>
      <div class="step" data-reveal><b>04</b><h3>In writing</h3><p>Your itinerary and terms in writing, before any payment.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Visit us</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("Two offices,", "<em>close to you.</em>")}</h2></div>
      <p class="lead" data-reveal>Drop in to talk it through in person, in English or Urdu.</p>
    </div>
    {offices()}
  </div>
</section>
"""
    page("contact.html", "Contact Sada-e-Rehmat | Hajj & Umrah Offices in the UK and Pakistan",
         "Enquire about Hajj 2027 or Umrah. Offices in Feltham, UK and Rawalpindi, Pakistan. Call +44 20 3002 2999 or +92 333 9999200, or email info@sada-e-rehmat.com.",
         body, crumb=("Contact",), priority=0.8,
         og=dict(image="madinah", eyebrow="Contact", title="Let's plan your journey.",
                 detail="UK +44 20 3002 2999 · Pakistan +92 333 9999200", chips=[], theme="contact"))


# --------------------------------------------------------------------------
# Guides
# --------------------------------------------------------------------------
def build_guides():
    filt = '<div class="hub-filter" role="group" aria-label="Filter guides"><button aria-pressed="true" data-cat="all">All guides</button>' + \
        "".join(f'<button aria-pressed="false" data-cat="{k}">{v}</button>' for k, v in CATS.items()) + "</div>"
    plan_items = [
        ("6 months before", "Passports and route", 'Six months\' validity. Book via <a href="guide-hajj-uk.html">Nusuk Hajj (UK)</a> or <a href="guide-hajj-pakistan.html">Pakistan\'s scheme</a>.'),
        ("3 months before", "Package and visa", '<a href="guide-choosing.html">Compare packages</a>, then sort your <a href="guide-umrah-visa.html">visa and Nusuk</a>.'),
        ("6 weeks before", "Vaccines and walking", 'ACWY at least 10 days before arrival. <a href="guide-health.html">Health guide</a>.'),
        ("2 weeks before", "Rites and packing", '<a href="guide-first-umrah.html">Umrah</a>, <a href="guide-duas.html">duas</a>, <a href="guide-packing.html">packing list</a>.'),
        ("On the flight", "Ihram before the Miqat", '<a href="guide-miqat.html">When to put on Ihram</a>.'),
    ]
    plan = '<ol class="plan" data-stagger>' + "".join(f'<li data-reveal><span>{w}</span><h3>{t}</h3><p>{d}</p></li>' for w, t, d in plan_items) + '</ol>'
    hub_ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Hajj and Umrah guides", "url": BASE + "guides.html",
              "hasPart": [{"@type": "Article", "headline": GUIDE[g]["title"], "url": f"{BASE}{g}.html"} for g in GUIDE_ORDER]}
    body = f"""
<section class="page-hero page-hero-plain">
  <div class="wrap" data-enter>
    <span class="eyebrow">{len(ALL_GUIDES)} guides · updated November 2026</span>
    <h1 class="display-xl" style="margin-top:18px">Prepare with <em>a calm mind.</em></h1>
    <p class="lead">Practical Hajj and Umrah guides for pilgrims from the UK and Pakistan: the rites step by step, visas, Nusuk, health, packing and what to ask before you book.</p>
  </div>
</section>
<section class="section-tight" style="padding-top:0">
  <div class="wrap">{filt}{guide_cards(GUIDE_ORDER, filterable=True)}</div>
</section>
<section class="section sand">
  <div class="wrap">
    <div class="head head-split">
      <div><span class="eyebrow" data-reveal>Your plan</span><h2 class="display-l" data-lines style="margin-top:18px">{lines("From six months out", "<em>to the Miqat.</em>")}</h2></div>
      <p class="lead" data-reveal>What to do, and when, with the guide for each step.</p>
    </div>
    {plan}
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="split-copy">
      <span class="eyebrow" data-reveal>A helpful reminder</span>
      <h2 class="display-m" data-lines>{lines("Official guidance", "<em>comes first.</em>")}</h2>
      <p data-reveal>Rules change each season. Always confirm with the official sources for your passport and dates.</p>
      <div class="actions" data-reveal><a class="btn btn-ghost" href="https://www.nusuk.sa/" target="_blank" rel="noopener">Nusuk ↗</a><a class="btn btn-ghost" href="https://www.gov.uk/foreign-travel-advice/saudi-arabia/pilgrimage" target="_blank" rel="noopener">UK FCDO ↗</a><a class="btn btn-ghost" href="https://www.mora.gov.pk/" target="_blank" rel="noopener">Pakistan MoRA ↗</a></div>
    </div>
    <div class="media" data-parallax data-clip>{img("jamarat", "Pilgrims at the Jamarat", "(max-width: 860px) 100vw, 50vw")}</div>
  </div>
</section>
{cta_band("Still have <em>a question?</em>", "Ask us anything about Hajj or Umrah. There's no such thing as a small question.", "muzdalifah", ("Ask our team", "contact.html"))}
"""
    page("guides.html", "Hajj & Umrah Guides 2026–27 | Sada-e-Rehmat",
         "Free Hajj and Umrah guides for pilgrims from the UK and Pakistan: how to perform Umrah, Hajj day by day with 2027 dates, Ihram, Miqat, duas, visas, Nusuk, health and packing.",
         body, crumb=("Guides",), extra_head=ld(hub_ld), priority=0.85,
         og=dict(image="jamarat", eyebrow=f"{len(ALL_GUIDES)} free guides", title="Prepare with a calm mind.",
                 detail="Umrah · Hajj · Visas · Duas · Health · Packing", chips=[], theme="guides"))

    for g in ALL_GUIDES:
        build_guide(g)


def build_guide(g):
    slug = g["slug"]
    secs = list(g["sections"])
    toc = [("tldr", "In short")]
    steps_html = ""
    if g.get("scrolly"):
        if slug in ("guide-first-umrah", "guide-hajj-step-by-step"):
            inner = f'<div class="guide-scrolly">{scrolly(g["scrolly"], aria=strip(g["h1"]))}</div>'
        else:
            inner = '<ol class="steps-list">' + "".join(f'<li><h3>{st[2]}</h3><p>{st[3]}</p></li>' for st in g["scrolly"]) + '</ol>'
        steps_html = f'<section id="steps"><h2>Step by step</h2>{inner}</section>'
        toc.append(("steps", "Step by step"))
    toc += [(sid, h) for sid, h, _ in secs]
    if g["faqs"]:
        toc.append(("faq", "Questions"))
    tldr = '<div class="guide-tldr" id="tldr"><h2>In short</h2><ul>' + "".join(f"<li>{t}</li>" for t in g["tldr"]) + "</ul></div>"
    body_secs = "".join(f'<section id="{sid}"><h2>{h}</h2>{html}</section>' for sid, h, html in secs)
    faq_html = ""
    if g["faqs"]:
        faq_html = '<section id="faq"><h2>Questions</h2><div class="faq">' + "".join(
            f'<details><summary>{q}<span class="plus" aria-hidden="true"></span></summary><div class="ans"><p>{a}</p></div></details>'
            for q, a in g["faqs"]) + "</div></section>"
    src = ""
    if g["sources"]:
        src = '<section id="sources"><h2>Sources and official links</h2><ul class="sources">' + "".join(
            f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in g["sources"]) + \
            '</ul><p class="sources" style="color:var(--muted)">Last checked 19 November 2026. Rules and dates can change; always confirm with official sources.</p></section>'
    rail = "".join(f'<a href="#{i}">{t}</a>' for i, t in toc)
    related = [r for r in g["related"] if r in GUIDE][:3]
    url = f"{BASE}{slug}.html"
    og_img = f"{BASE}assets/og/{slug}.jpg"
    article = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"][:110], "description": g["desc"],
               "image": [og_img], "datePublished": UPDATED, "dateModified": UPDATED, "inLanguage": "en-GB",
               "mainEntityOfPage": url, "articleSection": CATS[g["cat"]],
               "author": {"@type": "Organization", "name": "Sada-e-Rehmat", "url": BASE},
               "publisher": {"@type": "Organization", "name": "Sada-e-Rehmat", "logo": {"@type": "ImageObject", "url": BASE + "assets/img/logo-ink.png"}}}
    lds = [article]
    if g["faqs"]:
        lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in g["faqs"]]})
    if g.get("scrolly") and slug in ("guide-first-umrah", "guide-hajj-step-by-step", "guide-hajj-uk"):
        lds.append({"@context": "https://schema.org", "@type": "HowTo", "name": strip(g["h1"]).rstrip("."), "description": g["desc"],
                    "image": og_img, "step": [{"@type": "HowToStep", "position": i + 1, "name": strip(st[2]), "text": strip(st[3]),
                                               "url": f"{url}#steps"} for i, st in enumerate(g["scrolly"])]})
    body = f"""
<div class="read-progress" aria-hidden="true"><span></span></div>
<section class="page-hero">
  <div class="bg">{img(g["image"], "", "100vw", eager=True)}</div>
  <div class="wrap" data-enter>
    <span class="eyebrow" style="color:var(--gold-2)"><a href="guides.html">Guides</a> · {g["eyebrow"]}</span>
    <h1 class="display-l" style="margin-top:18px;max-width:16ch">{g["h1"]}</h1>
    <p class="lead">{g["intro"]}</p>
    <div class="guide-meta"><span>{g["minutes"]} min read</span><span>Updated 19 November 2026</span><span>{CATS[g["cat"]]}</span></div>
  </div>
</section>
<section class="section-tight">
  <div class="wrap guide-layout">
    <aside class="guide-rail">
      <div><h4>On this page</h4><nav aria-label="On this page">{rail}</nav></div>
      <div class="rail-card"><strong>Planning Hajj 2027?</strong><p>Maktab A, Zone 1, from £5,935 per person.</p><a class="btn btn-sm btn-light" href="packages.html">See journeys {ARROW}</a></div>
    </aside>
    <article class="guide-body">
      {tldr}
      {steps_html}
      {body_secs}
      {faq_html}
      {src}
    </article>
  </div>
</section>
<section class="section-tight sand">
  <div class="wrap">
    <div class="head"><span class="eyebrow" data-reveal>Keep reading</span><h2 class="display-m" data-lines>{lines("Related guides")}</h2></div>
    {guide_cards(related)}
  </div>
</section>
{cta_band("Want help <em>planning?</em>", "Bring your dates, departure city, group size and questions. We will talk you through the right journey.", "kaaba-tawaf", ("Speak to an expert", "contact.html"), ("See Hajj 2027", "packages.html"))}
"""
    page(slug + ".html", g["title"] + " | Sada-e-Rehmat" if len(g["title"]) < 50 else g["title"], g["desc"], body,
         dark_nav=True, crumb=(short_title(g), ("Guides", "guides.html")), extra_head=ld(*lds), og_type="article", priority=0.75,
         og=dict(image=g["image"], eyebrow=f'Guide · {g["eyebrow"]}', title=short_title(g) + ".", detail=g["og"],
                 chips=[f'{g["minutes"]} min read', CATS[g["cat"]]], theme="guide"))


# --------------------------------------------------------------------------
# Policies, thank you, 404, services redirect
# --------------------------------------------------------------------------
def build_policies():
    meta = json.load(open(os.path.join(SRC, "content", "meta.json"), encoding="utf-8"))
    for slug in ("privacy-policy", "cookie-policy"):
        m = meta[slug]
        raw = open(os.path.join(SRC, "content", slug + ".html"), encoding="utf-8").read()
        content, _, updated = raw.partition("<!--updated-->")
        intro = {"privacy-policy": "How Sada-e-Rehmat Ltd handles personal information when you browse this website, contact us, or ask us to plan Hajj, Umrah, Ziyarat, travel, accommodation, transport or related services.",
                 "cookie-policy": "How Sada-e-Rehmat Ltd uses cookies, local storage and similar technologies on this website."}[slug]
        body = f"""
<section class="page-hero page-hero-plain">
  <div class="wrap" data-enter>
    <span class="eyebrow">{m['eyebrow']}</span>
    <h1 class="display-l" style="margin-top:18px">{m['h1']}</h1>
    <p class="lead">{intro}</p>
  </div>
</section>
<article class="article" style="padding-top:0">
  <div class="wrap-narrow">
    {content.replace('<section>', '<section data-reveal>')}
    <p class="note">{updated.strip()}</p>
  </div>
</article>
"""
        page(slug + ".html", m["title"], m["desc"], body, cta=False, crumb=(m["h1"],), priority=0.3,
             og=dict(image="madinah", eyebrow="Sada-e-Rehmat Ltd", title=m["h1"] + ".", detail="Company no. 16043621 · England and Wales", chips=[], theme="legal"))


def build_misc():
    check = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5L20 7"/></svg>'
    page("thank-you.html", "Thank You | Sada-e-Rehmat", "Your enquiry has been sent to the Sada-e-Rehmat pilgrimage team.", f"""
<section class="message">
  <div data-enter>
    <div class="badge">{check}</div>
    <h1 class="display-l">Thank you. <em>We've got it.</em></h1>
    <p class="lead">Your enquiry is with our pilgrimage team. A specialist will reply within one working day. If you don't hear from us, check your spam folder or email <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <div class="actions"><a class="btn" href="index.html">Back to home {ARROW}</a><a class="btn btn-ghost" href="packages.html">Browse Hajj 2027</a></div>
  </div>
</section>""", cta=False, index=False)
    with open(os.path.join(ROOT, "thank-you.html")) as f:
        s = f.read().replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    with open(os.path.join(ROOT, "thank-you.html"), "w") as f:
        f.write(s)

    page("404.html", "Page Not Found | Sada-e-Rehmat", "This page could not be found.", f"""
<section class="message">
  <div data-enter>
    <div class="big404">404</div>
    <h1 class="display-m" style="margin-top:24px">This page has <em>wandered off the path.</em></h1>
    <p class="lead">Let us guide you back.</p>
    <div class="actions"><a class="btn" href="index.html">Return home {ARROW}</a><a class="btn btn-ghost" href="contact.html">Contact our team</a></div>
  </div>
</section>""", cta=False, index=False)
    with open(os.path.join(ROOT, "404.html")) as f:
        s = f.read().replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
        # absolute asset paths so the 404 renders under any missing URL
        s = re.sub(r'(src|href|srcset)="(assets/|style\.css|script\.js|index\.html|contact\.html|packages\.html|gallery\.html|guides\.html|about-us\.html|privacy-policy\.html|cookie-policy\.html)',
                   r'\1="/sada-e-rehmat/\2', s)
        s = s.replace(', assets/img/', ', /sada-e-rehmat/assets/img/')
    with open(os.path.join(ROOT, "404.html"), "w") as f:
        f.write(s)

    with open(os.path.join(ROOT, "services.html"), "w") as f:
        f.write(f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><title>Packages & services | Sada-e-Rehmat</title>
<meta http-equiv="refresh" content="0; url=packages.html"><link rel="canonical" href="{BASE}packages.html"><meta name="robots" content="noindex">
</head><body><p><a href="packages.html">Continue to Hajj 2027 packages</a></p></body></html>
""")
    print("built services.html (redirect)")


if __name__ == "__main__":
    build_home()
    build_packages()
    build_gallery()
    build_about()
    build_contact()
    build_guides()
    build_policies()
    build_misc()
    lines_ = "".join(f"  <url><loc>{BASE}{'' if f == 'index.html' else f}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority></url>\n" for f, pr in PAGES_BUILT)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + lines_ + "</urlset>\n")
    with open(os.path.join(SRC, "og-manifest.json"), "w") as fh:
        json.dump(OG_MANIFEST, fh, ensure_ascii=False, indent=1)
    print(f"sitemap: {len(PAGES_BUILT)} urls · og manifest: {len(OG_MANIFEST)} images")
