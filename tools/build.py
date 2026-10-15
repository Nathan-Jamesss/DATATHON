import os, sys, html
OUT = sys.argv[1]
REG = "https://forms.gle/7uUpkc1J9UCxxKup7"

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-db" viewBox="0 0 24 24"><ellipse cx="12" cy="5.5" rx="7" ry="3"/><path d="M5 5.5v13c0 1.7 3.1 3 7 3s7-1.3 7-3v-13M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/></symbol>
<symbol id="i-bars" viewBox="0 0 24 24"><path class="f" d="M4 20h3.2V13H4zM10.4 20h3.2V8h-3.2zM16.8 20H20V4h-3.2z" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-cube" viewBox="0 0 24 24"><path d="M12 2.5l8 4.5v10l-8 4.5-8-4.5V7zM4 7l8 4.5L20 7M12 11.5v10"/></symbol>
<symbol id="i-bulb" viewBox="0 0 24 24"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></symbol>
<symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M3.5 10h17M8 3v4M16 3v4"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
<symbol id="i-users" viewBox="0 0 24 24"><circle cx="8.5" cy="8" r="3"/><circle cx="16.5" cy="9" r="2.5"/><path d="M3 19c0-3 2.5-5 5.5-5s5.5 2 5.5 5M15 14.2c2.6-.3 6 .8 6 4.8"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6"/></symbol>
<symbol id="i-download" viewBox="0 0 24 24"><path d="M12 3v12M6.5 10.5L12 16l5.5-5.5M4 20h16"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-health" viewBox="0 0 24 24"><path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/></symbol>
<symbol id="i-cap" viewBox="0 0 24 24"><path d="M2 9l10-5 10 5-10 5zM6 11.5V16c0 1.5 2.7 3 6 3s6-1.5 6-3v-4.5M22 9v6"/></symbol>
<symbol id="i-coin" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M14.5 8.5c-.5-.8-1.5-1.2-2.5-1.2-1.4 0-2.5.8-2.5 2s1 1.6 2.5 2 2.5.8 2.5 2-1.1 2-2.5 2c-1 0-2-.4-2.5-1.2M12 5.5v1.8M12 16.7v1.8"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></symbol>
<symbol id="i-file" viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6zM14 3v4h4M9 13h6M9 17h6"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></symbol>
<symbol id="i-trophy" viewBox="0 0 24 24"><path d="M8 4h8v6a4 4 0 0 1-8 0zM8 6H4v2a4 4 0 0 0 4 4M16 6h4v2a4 4 0 0 1-4 4M12 14v4M8 21h8M10 18h4"/></symbol>
<symbol id="i-flag" viewBox="0 0 24 24"><path d="M5 21V4M5 4h11l-2 4 2 4H5"/></symbol>
<symbol id="i-info" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/></symbol>
</defs></svg>"""

def ic(n, cls=""):
    return f'<svg class="icon {cls}" aria-hidden="true"><use href="#i-{n}"/></svg>'

FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%23000'/%3E%3Ctext x='32' y='46' font-family='Arial Black,Arial' font-weight='900' font-size='40' text-anchor='middle' fill='%2319e3f5'%3ET%3C/text%3E%3C/svg%3E"

def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#000000">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{SPRITE}
"""

MARQ_ITEMS = ["DATATHON 2026", "Fri 16 Oct 2026 · 9:00 AM – 6:00 PM", "From Data to Deployable Ideas", "Solo or Duo · OD provided", "Prize pool ₹4,500", "Venue CB G20, VIT-AP University", "Organised by Data Science Club × IIEC"]
def marquee():
    one = "".join(f"<span>{m}</span>" for m in MARQ_ITEMS)
    return f'<div class="marquee" aria-label="Datathon announcements"><div class="marquee__track">{one}{one}{one}{one}</div></div>'

def nav(page):
    if page == "home":
        links = [("#timeline", "Timeline"), ("problem-statements.html", "Problem Statements"), ("#ppt", "Round 1 PPT"), ("#judging", "Judging"), ("#rules", "Rules"), ("#prizes", "Prizes")]
    else:
        links = [("index.html", "Home"), ("#download", "Download all"), ("#track-1", "01 Health"), ("#track-2", "02 Education"), ("#track-3", "03 Smart City"), ("#track-4", "04 Business")]
    li = "".join(f'<a href="{h}"{" aria-current=\"page\"" if (page=="problems" and h=="problem-statements.html") else ""}>{t}</a>' for h, t in links)
    if page == "home":
        li = li.replace('href="problem-statements.html"', 'href="problem-statements.html"')
    return f"""<header class="nav-shell"><div class="wrap"><nav class="nav" aria-label="Main">
<a class="nav__brand" href="index.html" aria-label="DATATHON home"><img src="assets/logo-dsc.png" alt="Data Science Club VIT-AP"><span class="wordmark">DATA<b>T</b>HON</span></a>
<div class="nav__links" id="navlinks">{li}</div>
<div class="nav__cta"><a class="btn btn--fill" href="{REG}" target="_blank" rel="noopener">Register</a>
<button class="nav__plus" id="navplus" aria-expanded="false" aria-controls="navlinks" aria-label="Menu">{ic('plus')}</button></div>
</nav></div></header>"""

def footer():
    return f"""<footer class="band band-dark footer"><div class="wrap">
<div class="footer__logos">
<img src="assets/logo-dsc.png" alt="Data Science Club, VIT-AP">
<img src="assets/logo-vitap.png" alt="VIT-AP University">
<img src="assets/logo-iiec.png" alt="IIEC">
</div>
<div class="display footer__big" aria-hidden="true">DATA<span class="t">T</span>HON</div>
<div class="footer__meta"><span>Organised by Data Science Club (DSC)</span><span>In collaboration with IIEC</span><span>Fri 16 Oct 2026 · CB G20, VIT-AP University</span></div>
</div></footer>
<script src="js/site.js"></script>
</body>
</html>
"""

# =============================== HOME ===============================
STOPS = [
 dict(cls="", icon="users", time="9:00", sub="AM – 10:00 AM", s="09:00", e="10:00", title="Opening Ceremony", text="Registration, welcome, rules, evaluation criteria and team setup. Get seated, get connected, get ready.", tags=["Registration", "Rules briefing", "Team setup"]),
 dict(cls="stop--milestone", icon="file", time="10:00", sub="AM · Release", s="10:00", e="10:05", title="Problem Statements Released", text="Four tracks and their starter datasets go live. Pick one track and start exploring.", tags=["4 tracks", "Datasets unlock"], link=("problem-statements.html", "Open problem statements & datasets")),
 dict(cls="", icon="bulb", time="10:00", sub="AM – 12:00 PM", s="10:00", e="12:00", title="Round 1 · PPT + Base Prototype", text="Submit your idea PPT (USP + MVP mandatory) and show a base prototype built on the provided dataset.", tags=["PPT", "USP + MVP", "Base prototype"], link=("#ppt", "Get the PPT template")),
 dict(cls="", icon="bars", time="12:00", sub="PM – 1:00 PM", s="12:00", e="13:00", title="Evaluation + Elimination Round", text="Judges review every Round 1 submission. Only shortlisted teams move on to the Final Round.", tags=["Judges review", "Elimination"]),
 dict(cls="stop--break", icon="clock", time="1:00", sub="PM – 1:30 PM", s="13:00", e="13:30", title="Lunch Break", text="Refuel. Shortlisted teams get ready for the final push.", tags=["30 min"]),
 dict(cls="", icon="cube", time="1:30", sub="PM – 4:00 PM", s="13:30", e="16:00", title="Round 2 · Complete Prototype", text="Finish the complete prototype: trained model wired into a working product, ready to demo.", tags=["Complete prototype", "Submission freeze 4:00 PM"], link=("round2.html", "Submit your repo")),
 dict(cls="", icon="users", time="4:00", sub="PM – 5:30 PM", s="16:00", e="17:30", title="Round 2 Demos & Judging", text="Shortlisted teams demo the complete prototype; judges score on the 100-mark rubric.", tags=["Live demo", "100-mark rubric"]),
 dict(cls="stop--winner", icon="trophy", time="5:30", sub="PM – 6:00 PM", s="17:30", e="18:00", title="Winner Declaration", text="Results announced across all four tracks — one overall competition, one leaderboard.", tags=["₹4,500 prize pool"]),
 dict(cls="", icon="flag", time="6:00", sub="PM · Closing", s="18:00", e="18:15", title="Closing", text="Prize distribution, photos and the closing note.", tags=["Closing"]),
]

def stop_html(s):
    cls = ("stop " + s["cls"]).strip()
    tags = "".join(f'<span class="chip">{t}</span>' for t in s["tags"])
    link = ""
    if s.get("link"):
        link = f'<div class="stop__tags"><a class="btn btn--sm btn--fill" href="{s["link"][0]}">{s["link"][1]} {ic("arrow")}</a></div>'
    return f"""<li class="{cls}" data-start="2026-10-16T{s['s']}:00+05:30" data-end="2026-10-16T{s['e']}:00+05:30">
<div class="stop__time"><b>{s['time']}</b><small>{s['sub']}</small></div>
<div class="stop__rail"><span class="stop__node">{ic(s['icon'])}</span><span class="stop__line"></span></div>
<div class="stop__card"><span class="stop__live">● LIVE NOW</span><h3>{s['title']}</h3><p>{s['text']}</p><div class="stop__tags">{tags}</div>{link}</div>
</li>"""

PIPE = [("db", "Data"), ("bars", "Analyze"), ("cube", "Model"), ("bulb", "Build"), ("bars", "Deploy")]
def pipeline():
    out = []
    for i, (n, t) in enumerate(PIPE):
        last = " pipe-step--last" if i == len(PIPE) - 1 else ""
        out.append(f'<div class="pipe-step{last}"><span class="pipe-step__ring">{ic(n, "icon--fill" if n=="bars" else "")}</span>{t}</div>')
        if i < len(PIPE) - 1:
            out.append('<span class="pipe-arrow" aria-hidden="true"></span>')
    return '<div class="pipeline" role="list" aria-label="Data, Analyze, Model, Build, Deploy">' + "".join(out) + "</div>"

TRACKS_TEASER = [
 ("01", "Health", "health", "The Forgotten Patient", "Hospital-flow product: find where patients wait and what to investigate first.", 5, "01_health_forgotten_patient"),
 ("02", "Education", "cap", "The Campus Has Space. Students Don’t.", "Match room requests to the best feasible room — with evidence.", 5, "02_education_campus_space"),
 ("03", "Smart City", "pin", "Where Should We Fix First?", "A transparent, evidence-backed priority list for city fixes.", 5, "03_smart_city_where_fix_first"),
 ("04", "Business", "coin", "The Money Leak", "Find what’s going wrong with revenue and what the manager should do next.", 6, "04_business_money_leak"),
]

RUBRIC = [
 ("Problem understanding & user need", "Clear user, pain point, and scope", 10),
 ("Provided dataset usage", "Meaningful joins, analysis, features and data-driven decisions", 10),
 ("Data Science / ML quality", "Appropriate method, baseline, evaluation and reasoning", 15),
 ("ML model from scratch", "Trained from scratch scores highest. API-key / pretrained-only scores lowest", 25),
 ("Working product & workflow", "Functional end-to-end prototype, usability and reliability", 20),
 ("USP & innovation", "Differentiation and quality of the solution", 10),
 ("Impact, feasibility & responsible use", "Plausible benefit, limitations and responsible claims", 5),
 ("Demo & presentation", "Clear demonstration and communication", 5),
]

RULES = [
 ("Choose one track.", "Build against the corresponding problem statement and starter dataset."),
 ("The provided dataset is foundational.", "You may add relevant public data, APIs or self-collected data if permitted, but you must still use the supplied dataset meaningfully."),
 ("Tell us about extra data.", "If you used data beyond the provided pack, say where it came from."),
 ("No replacing the core dataset.", "A product that ignores the provided data and relies entirely on an external API will lose data-use marks."),
 ("Build a product, not only a model.", "A notebook, static chart or model file alone is not a complete submission."),
 ("Model claims must be supported.", "Report the evaluation method and appropriate metrics. Do not claim “high accuracy” without evidence."),
 ("Prevent leakage.", "Use time-based or group-based splits where appropriate; never use future information to predict the past."),
 ("Explain the result.", "A user should understand why a prediction, alert or recommendation appeared."),
 ("Acknowledge synthetic-data limits.", "You cannot claim the generated data proves real-world performance."),
 ("Responsible use.", "No real personal/medical records, unauthorised access, unsafe live deployment or misleading public-safety claims."),
 ("Use permitted tools.", "Disclose every API key, pretrained model and external service. They are allowed as supporting parts, but a model trained from scratch earns far more marks than an API-key solution."),
 ("Demonstrate the workflow.", "Judges should see a real input and a useful product output."),
 ("One overall competition.", "All tracks use the same judging rubric and compete for the same prizes."),
 ("Submission freeze.", "Submit your source/demo and presentation by the deadline announced by the organisers."),
 ("Team integrity.", "Identify borrowed code, datasets, models and templates. Plagiarism or fabricated evaluation results may lead to disqualification."),
]

PPT_SLIDES = [
 ("Title & Team", "Product name, track, team name and members", False),
 ("Problem & Target User", "Who hurts, why now, and the one workflow you’ll fix", False),
 ("Proposed Solution & USP", "What you’re building and why it beats the obvious answer", True),
 ("Dataset Usage & Insights", "Tables joined, cleaning done, patterns found", False),
 ("ML Approach", "From-scratch model (declare any API used), baseline, split, metric", False),
 ("Base Prototype & MVP", "Screens of your Round 1 base prototype + what Round 2 will complete", True),
 ("Architecture & Workflow", "Tech stack and the input → analysis → output → action flow", False),
 ("Feasibility, Impact & Next Steps", "Limitations, responsible use, impact, references", False),
]

def home():
    h = head("DATATHON 2026 · VIT-AP", "DATATHON — a product-focused Data Science hackathon by Data Science Club (DSC) with IIEC, VIT-AP University. 16 October 2026. From data to deployable ideas.")
    h += marquee() + nav("home")
    h += f"""<main id="top">
<section class="band band-dark hero"><div class="wrap">
<div class="logo-strip"><img src="assets/logo-dsc.png" alt="Data Science Club VIT-AP"><span class="logo-strip__div"></span><img src="assets/logo-vitap.png" alt="VIT-AP University"><span class="logo-strip__div"></span><img src="assets/logo-iiec.png" alt="IIEC"></div>
<p class="hero__kicker">A product-focused data science hackathon</p>
<h1 class="display hero__title">DATA<span class="t">T</span>HON
<span class="sticker sticker--hide-sm" style="--rot:-8deg; top:2%; right:3%">USP + MVP</span>
<span class="sticker sticker--white sticker--hide-sm" style="--rot:7deg; bottom:-4%; right:26%">Real data</span>
<span class="sticker sticker--ring sticker--hide-sm" style="--rot:0deg; top:-14%; left:58%" aria-hidden="true">{ic('cube')}</span>
</h1>
<p class="hero__sub"><span>From data to</span><span class="hl">Deployable</span><span>ideas</span></p>
{pipeline()}
<div class="hero__grid">
<div class="hero__copy">
<div class="quote-bar"><p class="lede">Explore data. Solve real-world problems. Build a working product.</p><p class="muted">Think like a product team: users, solution, USP, ML.</p></div>
<div class="info-list">
<div class="info"><span class="info__ico">{ic('calendar')}</span><div class="info__body"><strong>Friday, 16 October 2026</strong><span>9:00 AM – 6:00 PM</span></div></div>
<div class="info"><span class="info__ico">{ic('pin')}</span><div class="info__body"><strong>Venue: CB G20</strong><span>VIT-AP University</span></div></div>
<div class="info"><span class="info__ico">{ic('users')}</span><div class="info__body"><strong>Solo or Duo</strong><span>Teams of 1–2 members</span><span><span class="hl" style="font-size:13px;font-weight:800;letter-spacing:.03em">OD WILL BE PROVIDED</span></span></div></div>
</div>
<div class="hero__actions">
<a class="btn btn--fill btn--lg" href="{REG}" target="_blank" rel="noopener">Register now {ic('arrow')}</a>
<a class="btn btn--lg" href="#timeline">See the timeline</a>
<a class="btn btn--lg" href="problem-statements.html">Problem statements</a>
</div>
<div class="countdown" id="countdown" data-target="2026-10-16T09:00:00+05:30" aria-live="off"></div>
</div>
<div class="hero__art-wrap">
<div class="hero__art"><img src="assets/hero-art.png" alt="Glowing path climbing a mountain through data, analytics, model and idea blocks" width="1339" height="1717"></div>
<span class="sticker" style="--rot:-7deg; top:6%; left:-4%">Prize pool ₹4,500</span>
<span class="sticker sticker--white" style="--rot:6deg; bottom:8%; right:-3%">4 tracks · 1 winner</span>
</div>
</div>
</div></section>

<section class="band band-wash" id="timeline"><div class="wrap">
<div class="section-head"><span class="eyebrow">Event itinerary · Fri 16 Oct 2026</span>
<h2 class="display h-section">The <span class="t">day</span><br>plan</h2>
<p class="lede">Nine stops from opening ceremony to winner declaration. Round 1 is the PPT round: problem statements drop at 10 AM, ideation plus base prototype run until noon, and only shortlisted teams reach the Final Round.</p></div>
<ol class="itinerary">
{''.join(stop_html(s) for s in STOPS)}
</ol>
</div></section>

<section class="band band-cyan" id="tracks"><div class="wrap">
<div class="section-head"><span class="eyebrow">4 tracks · pick one</span>
<h2 class="display h-section">Problem<br><span class="t">state</span>ments</h2>
<p class="lede">Each team gets one problem statement and its starter dataset. Open the problem statements page for the full briefs and every downloadable dataset file.</p></div>
<div class="grid-4">
{''.join(f'''<a class="card track-card" href="problem-statements.html#track-{n[1]}" aria-label="Track {n} {dom}: {t}">
<div style="display:flex;justify-content:space-between;align-items:flex-start"><span class="track-card__no">{n}</span><span class="track-card__badge">{ic(icn)}</span></div>
<span class="chip">{dom}</span><h3>{t}</h3><p>{d}</p>
<div class="track-card__foot"><span>{files} CSV files</span><span style="display:inline-flex;gap:6px;align-items:center">Open {ic('arrow')}</span></div></a>''' for (n, dom, icn, t, d, files, _) in TRACKS_TEASER)}
</div>
<div class="cta-row"><a class="btn btn--fill btn--lg" href="problem-statements.html">Open problem statements & datasets {ic('download')}</a><span class="chip">Synthetic data · same starter pack for every team</span></div>
</div></section>

<section class="band band-dark" id="ppt"><div class="wrap">
<div class="section-head"><span class="eyebrow">Round 1 · 10:00 AM – 12:00 PM</span>
<h2 class="display h-section">Idea <span class="t">PPT</span><br>round</h2>
<p class="lede">Submit your Round 1 idea in the official Datathon PPT template. It’s built to make you think like a product team — the two sections marked <span class="must">MUST</span> are mandatory.</p></div>
<div class="two-col">
<div>
<ol class="slide-list">
{''.join(f'<li><div><b>{t}{" <span class=must>MUST</span>" if m else ""}</b><span>{d}</span></div></li>' for t, d, m in PPT_SLIDES)}
</ol>
</div>
<div class="stack">
<div class="card" style="border-radius:40px;padding:32px">
<span class="eyebrow">Template</span>
<h3 class="display" style="font-size:clamp(34px,4.5vw,60px);margin:18px 0">Datathon<br>Round 1 <span class="t">PPT</span></h3>
<p class="muted">8 slides max, points and diagrams over paragraphs. Every slide carries your team name; fill it in and submit before 12:00 PM.</p>
<div class="cta-row"><a class="btn btn--fill btn--lg" href="downloads/DATATHON-Round1-Idea-PPT-Template.pptx" download>Download PPT template {ic('download')}</a></div>
</div>
<div class="card"><span class="eyebrow">What judges want to see</span>
<div class="flow" style="margin-top:18px">
<span class="chip chip--cyan">Problem</span>{ic('arrow')}<span class="chip">User need</span>{ic('arrow')}<span class="chip">Data exploration</span>{ic('arrow')}<span class="chip">Model / logic</span>{ic('arrow')}<span class="chip">Recommendation</span>{ic('arrow')}<span class="chip">Product interface</span>{ic('arrow')}<span class="chip chip--cyan">Demo</span>
</div>
<p class="muted" style="margin-top:18px">The ML model is one component of the product, not the whole product. Show an original trained model and an explained output a real user can act on.</p></div>
</div>
</div>
</div></section>

<section class="band band-wash" id="judging"><div class="wrap">
<div class="section-head"><span class="eyebrow">One rubric · all four tracks</span>
<h2 class="display h-section">How you’re<br><span class="t">judged</span></h2>
<p class="lede">100 marks. Same rubric for every track. Judges score what is actually demonstrated — not who processed the most rows, and not just for a complicated algorithm.</p></div>
<div class="rubric">
{''.join(f'<div class="rubric__row"><div><b>{n}</b><small>{d}</small></div><div class="rubric__bar" role="img" aria-label="{m} of 100 marks"><i style="width:{m*5}%"></i></div><div class="rubric__pts">{m}</div></div>' for n, d, m in RUBRIC)}
<div class="rubric__total"><span>Total</span><span>100</span></div>
</div>
</div></section>

<section class="band band-dark" id="rules"><div class="wrap">
<div class="section-head"><span class="eyebrow">The fine print</span>
<h2 class="display h-section">Ground <span class="t">rules</span></h2></div>
<div class="rules">
{''.join(f'<details class="rule"><summary data-n="{i+1:02d}">{t}</summary><p>{d}</p></details>' for i, (t, d) in enumerate(RULES))}
</div>
<div class="cta-row"><a class="btn btn--fill" href="problem-statements.html#before-you-start">Recommended first steps {ic('arrow')}</a></div>
</div></section>

<section class="band band-cyan" id="prizes"><div class="wrap">
<div class="section-head"><span class="eyebrow">Winners announced 5:30 PM</span>
<h2 class="display h-section">Prize<br><span class="t">pool</span></h2></div>
<div class="prizes">
<div class="prize prize--1"><small>1st prize</small><b>₹2,000</b></div>
<div class="prize"><small>2nd prize</small><b>₹1,500</b></div>
<div class="prize"><small>3rd prize</small><b>₹1,000</b></div>
</div>
<div class="pool"><span>Total prize pool</span><b>₹4,500</b></div>
<div class="reg" id="register">
<div class="reg__qr"><img src="assets/qr.png" alt="QR code linking to the DATATHON registration form" width="515" height="515"></div>
<div><h3>Register <b>now</b></h3><p>Scan the QR or use the button. Teams of 1–2 members. OD will be provided.</p>
<a class="btn btn--fill btn--lg" href="{REG}" target="_blank" rel="noopener">Open registration form {ic('arrow')}</a></div>
</div>
</div></section>
</main>
"""
    h += footer()
    return h

# =============================== PROBLEMS ===============================
TRACKS = [
 dict(n=1, dom="Health", icon="health", band="band-wash", folder="01_health_forgotten_patient",
  title="The Forgotten Patient",
  problem="A patient’s experience in a hospital is a connected journey: arrival, triage, consultation, diagnostic tests, treatment, and discharge. When these stages are managed separately, delays and capacity issues can be difficult to spot early. Hospital teams need a clearer view of where patients are waiting, which services are under pressure, and where intervention may help.",
  challenge="Build a hospital-flow product that helps staff understand patient journeys, identify likely bottlenecks, and make better-informed operational decisions.",
  users="Hospital operations managers, department coordinators, and service administrators.",
  outcomes=["A patient-flow dashboard with department-level queues and wait times.", "A forecast of demand or likely delays by department/time period.", "Alerts for unusual waiting patterns or potentially overloaded services.", "A diagnostic-test turnaround monitor.", "A “what should we investigate first?” queue ranked by impact and confidence.", "An explanation panel showing which data signals led to each alert."],
  helps="Teams can link visits to patients and departments, calculate wait and service patterns, compare departments, estimate test turnaround, study time-of-day demand, and build an operational view from several tables. This data is simulated and is <b>not</b> suitable for clinical diagnosis.",
  ml="Waiting-time regression, demand forecasting, clustering of visit patterns, anomaly detection, prioritization/ranking, or queue/resource optimization. Use a time-aware split when evaluating predictions involving future time.",
  q="What is likely to get delayed next, why, and what should the operations team examine?",
  files=[("patients.csv", "2,000 patient profiles."), ("encounters.csv", "8,000 visits with arrival, service, and discharge times."), ("departments.csv", "12 departments with staffing/capacity attributes."), ("diagnostic_tests.csv", "5,000 diagnostic-test records.")]),
 dict(n=2, dom="Education", icon="cap", band="band-dark", folder="02_education_campus_space",
  title="The Campus Has Space. Students Don’t.",
  problem="Universities may have classrooms, laboratories, seminar rooms, and study spaces while students and clubs still struggle to find a suitable place at the right time. Some rooms may be underused, while others are in high demand. Fixed schedules and fragmented booking information make it hard to match actual demand to available capacity and facilities.",
  challenge="Build a campus-space product that helps students find suitable rooms and helps administrators use existing campus space more effectively.",
  users="Students, club coordinators, faculty, and campus facilities administrators.",
  outcomes=["A room finder that matches time, capacity, accessibility, and facilities.", "A room-availability estimate using the class schedule and room requests.", "A utilization dashboard showing where space is consistently underused.", "A recommendation engine for room allocation or event relocation.", "A demand forecast for busy days/time periods.", "An explanation for each match (“capacity fit, projector available, no clash at that time”)."],
  helps="Room metadata defines capacity and facilities; schedules describe planned use; requests represent demand; event records add non-classroom demand. Together, these allow teams to estimate utilization, rank room matches, and suggest better allocations.",
  ml="Availability classification, demand forecasting, room recommendation/ranking, clustering of utilization patterns, or constrained room allocation. A valid solution should account for capacity, facilities, timing, and conflicting bookings — not merely predict availability.",
  q="Given a room request, what is the best feasible room and what evidence supports that recommendation?",
  files=[("rooms.csv", "120 room profiles."), ("class_schedule.csv", "5,000 class-schedule records."), ("room_requests.csv", "5,000 room requests."), ("events.csv", "1,800 event records.")]),
 dict(n=3, dom="Smart City", icon="pin", band="band-cyan", folder="03_smart_city_where_fix_first",
  title="Where Should We Fix First?",
  problem="Cities receive reports about road damage, traffic, flooding, streetlights, drainage, and pedestrian safety. Budgets and field teams are limited, so not every issue can be handled at once. Authorities need a transparent way to combine incident history, public complaints, traffic conditions, and local context to decide which locations deserve attention first.",
  challenge="Build a city-prioritization product that helps officials identify problem locations, understand the evidence behind their ranking, and compare possible interventions.",
  users="Municipal operations teams, road/traffic departments, and civic-service coordinators.",
  outcomes=["A map and ranked list of locations requiring attention.", "A complaint/incident trend monitor.", "A severity-and-frequency-based priority score.", "A resolution-time dashboard for public complaints.", "A recommendation queue with reasons and confidence, not an unexplained “risk score.”"],
  helps="The common <b>location_id</b> allows incidents, complaints, road conditions and context to be brought together. Teams can aggregate repeated issues, estimate patterns over time, compare zones, and create a transparent intervention-priority list.",
  ml="Incident-volume forecasting, complaint-category classification, resolution-time estimation, anomaly detection, location ranking, or resource-allocation optimization. Explain limitations and avoid claiming the synthetic coordinates represent real locations.",
  q="Which locations should be reviewed first, based on what evidence, and what information is still missing?",
  files=[("locations.csv", "1,000 simulated locations and context attributes."), ("incidents.csv", "10,000 incident records."), ("public_complaints.csv", "8,000 complaint records.")]),
 dict(n=4, dom="Business", icon="coin", band="band-dark", folder="04_business_money_leak",
  title="The Money Leak",
  problem="A business can record thousands of transactions and still struggle to understand why revenue or margin is underperforming. Cancellations, returns, discounts, stockouts, customer changes, and marketing spend can tell different parts of the story. These signals are often spread across separate systems, making it difficult to turn raw records into a clear action.",
  challenge="Build a business decision-support product that helps a manager identify potential revenue or operational problems, investigate their likely drivers, and decide what to do next.",
  users="Business owners, retail managers, product/category managers, and operations teams.",
  outcomes=["A revenue, cancellation, and return investigation dashboard.", "A customer/product/region breakdown of performance.", "A stockout and inventory-risk monitor.", "A campaign-efficiency view connecting spend, clicks, and conversions.", "A forecast or alert for unusual performance changes.", "A “why this is flagged” panel with supporting metrics."],
  helps="Transaction records can be joined with customer and product information to study sales and status patterns. Inventory records add stock availability; campaigns add marketing context. Build a product around investigation and action rather than a generic sales chart.",
  ml="Cancellation/return classification, demand forecasting, customer segmentation, anomaly detection, stockout-risk estimation, campaign conversion analysis, or inventory optimization. Document assumptions about costs, prices, returns, and profit calculations.",
  q="What appears to be going wrong, what evidence supports that finding, and what action should the manager consider?",
  files=[("customers.csv", "3,000 customer profiles."), ("products.csv", "250 product records."), ("transactions.csv", "18,000 transaction records."), ("inventory.csv", "5,000 inventory observations."), ("campaigns.csv", "1,200 campaign records.")]),
]

FIRST_STEPS = ["Read the track README and inspect all tables.", "Check row counts, missing values, duplicate keys, ranges, and timestamp coverage.", "Draw a small data-relationship diagram and decide which tables need to be joined.", "Define the product user and one high-value workflow.", "Choose a measurable data-science objective that supports that workflow.", "Create a simple baseline before trying a more complex model.", "Validate the model/logic, then connect it to the product interface.", "Show a complete example from input → analysis/model → output → user action."]

def human(n):
    return f"{n} B" if n < 1000 else (f"{n/1024:.0f} KB" if n < 1000 * 1024 else f"{n/1024/1024:.1f} MB")

def track_html(t, stats):
    fs = stats[t["folder"]]
    rows = "".join(
        f"""<div class="file"><div><b>{name}</b><small>{desc}</small></div>
<a class="btn btn--sm btn--fill" href="datasets/{t['folder']}/{name}" download>{ic('download')} CSV</a>
<div class="file__meta"><span class="chip">{fs[name][0]:,} rows</span><span class="chip">{human(fs[name][1])}</span></div></div>"""
        for name, desc in t["files"])
    tot = sum(v[0] for v in fs.values())
    outs = "".join(f"<li><span>{o}</span></li>" for o in t["outcomes"])
    return f"""<section class="band {t['band']}" id="track-{t['n']}"><div class="wrap">
<div class="track__top"><span class="display track__no">0{t['n']}</span>
<div><div class="track__dom"><span class="chip chip--cyan">{ic(t['icon'])} Track {t['n']} · {t['dom']}</span><span class="chip">{len(t['files'])} CSV files · {tot:,} rows</span></div>
<h2 class="display track__title">{t['title']}</h2></div></div>
<div class="track__body">
<div class="stack">
<div class="block"><h4>Problem statement</h4><p>{t['problem']}</p></div>
<div class="block"><h4>Challenge</h4><p><b>{t['challenge']}</b></p></div>
<div class="block"><h4>Primary users</h4><p>{t['users']}</p></div>
<div class="block"><h4>Product outcomes could include</h4><ul class="bul">{outs}</ul></div>
<div class="block"><h4>How the data helps</h4><p>{t['helps']}</p></div>
<div class="block"><h4>Possible ML / data-science work</h4><p>{t['ml']}</p></div>
<div class="question"><small>Useful product question</small><p>“{t['q']}”</p></div>
</div>
<aside class="stack" aria-label="Track {t['n']} datasets">
<div class="files"><div class="files__head"><h4>Datasets · Track 0{t['n']}</h4>
<a class="btn btn--sm btn--fill" href="datasets/{t['folder']}.zip" download>{ic('download')} All files (.zip)</a></div>
{rows}
<div class="file"><div><b>README.txt</b><small>Joins, caveats and notes for this track.</small></div><a class="btn btn--sm" href="datasets/{t['folder']}/README.txt" download>{ic('download')} TXT</a></div>
<p class="files__note">Folder: <b>{t['folder']}/</b> · Synthetic educational data — not real records.</p></div>
</aside>
</div></div></section>"""

def problems(stats):
    h = head("Problem Statements & Datasets · DATATHON 2026", "All four DATATHON problem statements with downloadable starter datasets: Health, Education, Smart City and Business.")
    h += marquee() + nav("problems")
    total_all = sum(sum(v[0] for v in s.values()) for s in stats.values())
    zips = "".join(f'<a class="btn btn--sm" href="datasets/{t["folder"]}.zip" download>{ic("download")} 0{t["n"]} {t["dom"]}</a>' for t in TRACKS)
    jump = "".join(f'<a class="btn" href="#track-{t["n"]}">0{t["n"]} · {t["dom"]}</a>' for t in TRACKS)
    h += f"""<div class="lock" id="lock" hidden><div><span class="eyebrow" style="justify-content:center">Locked until release</span><h2 class="display" style="margin-top:24px">Problem<br>statements<br>drop at <span class="t">10:00</span></h2><p>Friday 16 October 2026, 10:00 AM IST. Check back then.</p><div class="countdown" id="lockcd" data-target="2026-10-16T10:00:00+05:30" style="justify-content:center"></div><p><a class="btn" href="index.html">Back to home</a></p></div></div>
<main>
<section class="band band-dark subhero"><div class="wrap">
<span class="eyebrow">Released 10:00 AM · Round 1</span>
<h1 class="display">Problem<br><span class="t">state</span>ments</h1>
<p class="lede">Four tracks. One starter dataset each. Pick one track, build a working data-powered product — not just a notebook, chart, or isolated ML model.</p>
<div class="jump">{jump}</div>
<div class="dl-hub" id="download">
<div class="card"><span class="eyebrow">Download everything</span><h3>All 4 track<br>dataset packs</h3>
<p class="muted">{sum(len(t['files']) for t in TRACKS)} CSV files · {total_all:,} rows across four tracks, plus a README per track.</p>
<div><a class="btn btn--fill btn--lg" href="datasets/DATATHON_All_Track_Datasets.zip" download>{ic('download')} DATATHON_All_Track_Datasets.zip</a></div></div>
<div class="card"><span class="eyebrow">Or one track at a time</span><h3>Track<br>zips</h3><div class="dl-zips">{zips}</div>
<div class="notice">{ic('info')}<span>Synthetic educational data created for this event. Not real patient, campus, city, or company data. Do not use it for real clinical, civic-safety, or business decisions.</span></div></div>
</div>
</div></section>
{''.join(track_html(t, stats) for t in TRACKS)}
<section class="band band-wash" id="before-you-start"><div class="wrap">
<div class="section-head"><span class="eyebrow">Every team · every track</span>
<h2 class="display h-section">Before you<br><span class="t">start</span></h2>
<p class="lede">What a strong submission connects: Problem → User need → Data exploration → Model/logic → Recommendation/action → Product interface → Demonstration.</p></div>
<ol class="steps">{''.join(f'<li><span>{s}</span></li>' for s in FIRST_STEPS)}</ol>
<div class="two-col" style="margin-top:40px">
<div class="card"><span class="eyebrow">Original ML model counts when…</span>
<ul class="block bul" style="margin-top:16px;display:grid;gap:8px">
<li>You define a prediction, classification, ranking, forecasting or anomaly-detection task.</li>
<li>You train or meaningfully fine-tune a model on the provided (or permitted extra) data.</li>
<li>You document features, label, split strategy, baseline, metric and limitations.</li>
<li>The model is wired into the product and changes a real workflow, alert or decision.</li></ul>
<p class="muted" style="margin-top:12px;font-size:14px">Pretrained APIs / LLM calls are fine as supporting parts but don’t count as a team-trained model.</p></div>
<div class="card"><span class="eyebrow">Meaningful IoT work counts when…</span>
<ul class="block bul" style="margin-top:16px;display:grid;gap:8px">
<li>You ingest sensor data (live, replayed or simulated) in a clearly explained pipeline.</li>
<li>You handle timestamps, missing/noisy readings, device status or streaming updates.</li>
<li>Sensor signals feed a model or a product decision.</li>
<li>You demonstrate the sensor → model → interface path.</li></ul>
<p class="muted" style="margin-top:12px;font-size:14px">Hardware is optional. A replay/simulator is fine if clearly labelled. A decorative sensor graphic doesn’t count.</p></div>
</div>
<div class="cta-row"><a class="btn btn--fill btn--lg" href="index.html#ppt">Round 1 PPT template {ic('arrow')}</a><a class="btn btn--lg" href="index.html#rules">Read all rules</a></div>
</div></section>
</main>
"""
    h += footer().replace('<script src="js/site.js"></script>', '<script src="js/site.js"></script>\n<script src="js/lock.js"></script>')
    return h

if __name__ == "__main__":
    import json
    stats = json.load(open(os.path.join(os.path.dirname(__file__), "stats.json")))
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(home())
    open(os.path.join(OUT, "problem-statements.html"), "w", encoding="utf-8").write(problems(stats))
    print("ok")
