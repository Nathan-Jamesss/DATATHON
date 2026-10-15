"""v2 multi-page build. Usage: python tools/build2.py site   (imports data from build.py)"""
import os, sys, json
sys.argv = [sys.argv[0], sys.argv[1]] if len(sys.argv) > 1 else [sys.argv[0], "site"]
from build import *  # noqa: data + helpers (STOPS, TRACKS, RUBRIC, RULES, PPT_SLIDES, FIRST_STEPS, ic, human, pipeline, marquee, REG)

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = sys.argv[1]
stats = json.load(open(os.path.join(HERE, "stats.json")))

def head2(title, desc):
    h = head(title, desc)
    nl = chr(10)
    css = "".join('<link rel="stylesheet" href="css/' + n + '.css">' + nl for n in ("v2", "v3", "v4", "v5"))
    h = h.replace('<link rel="stylesheet" href="css/style.css">', '<link rel="stylesheet" href="css/style.css">' + nl + css + '<script>document.documentElement.className+=" js"</script>')
    return h

NAV = [("index.html", "Home", "home"), ("timeline.html", "Timeline", "timeline"), ("problem-statements.html", "Problem Statements", "problems"),
       ("ppt.html", "Round 1 PPT", "ppt"), ("round2.html", "Round 2", "round2"), ("judging.html", "Judging & Prizes", "judging"), ("rules.html", "Rules", "rules")]

def nav2(page):
    li = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == page else ""}>{t}</a>' for h, t, k in NAV)
    return f"""<header class="nav-shell"><div class="wrap"><nav class="nav" aria-label="Main">
<a class="nav__brand" href="index.html" aria-label="DATATHON home"><img src="assets/logo-dsc.png" alt="Data Science Club VIT-AP"><span class="wordmark">DATA<b>T</b>HON</span></a>
<div class="nav__links" id="navlinks">{li}</div>
<div class="nav__cta"><span class="nav__iiec"><img src="assets/logo-iiec.png" alt="IIEC"></span><a class="btn btn--fill" href="{REG}" target="_blank" rel="noopener">Register</a>
<button class="nav__plus" id="navplus" aria-expanded="false" aria-controls="navlinks" aria-label="Menu">{ic('plus')}</button></div>
</nav></div></header>"""

def footer2(extra=""):
    f = footer().replace('<div class="footer__meta">', '<div class="footer__meta"><a href="judge.html">Judges</a>')
    return f.replace('<script src="js/site.js"></script>', '<script src="js/site.js"></script>' + extra)

def page_head(eyebrow, title, lede="", extra=""):
    return f"""<section class="band band-dark page-head"><div class="wrap">
<div class="page-head__row"><div><span class="eyebrow">{eyebrow}</span><h1 class="display ph-title">{title}</h1></div>
<div class="page-head__logos"><img src="assets/logo-dsc.png" alt="Data Science Club VIT-AP"><img src="assets/logo-iiec.png" alt="IIEC"></div></div>
{f'<p class="lede">{lede}</p>' if lede else ''}{extra}</div></section>"""

def wrapp(page, title, desc, body, extra_js=""):
    return head2(title, desc) + marquee() + nav2(page) + "<main>" + body + "</main>" + footer2(extra_js)

# ---------------- timeline ----------------
SHORT = {
 "Opening Ceremony": "Registration, rules, evaluation criteria and team setup.",
 "Problem Statements Released": "4 tracks + datasets go live. Pick one track.",
 "Round 1 · PPT + Base Prototype": "Idea PPT (USP + MVP mandatory) plus a base prototype on the dataset.",
 "Evaluation + Elimination Round": "Judges review Round 1. Only shortlisted teams advance.",
 "Lunch Break": "Refuel before the final push.",
 "Round 2 · Complete Prototype": "Finish the complete prototype by 4:00 PM: model + working product.",
 "Round 2 Demos & Judging": "Live demo of the complete prototype, scored on the 100-mark rubric.",
 "Winner Declaration": "Results across all four tracks.",
 "Closing": "Prize distribution, photos and the closing note.",
}
def tcards():
    out = []
    n = len(STOPS)
    for i, s in enumerate(STOPS):
        row, k = i // 3, i % 3
        col = k + 1 if row % 2 == 0 else 3 - k
        if i == n - 1: arrow = ""
        elif k == 2: arrow = "d"
        else: arrow = "r" if row % 2 == 0 else "l"
        variant = {"stop--milestone": " tcard--milestone", "stop--break": " tcard--break", "stop--winner": " tcard--winner"}.get(s["cls"], "")
        tags = "".join(f'<span class="chip">{t}</span>' for t in s["tags"][:2])
        link = f'<a class="btn btn--sm btn--fill" style="align-self:flex-start;margin-top:4px" href="{s["link"][0]}">{s["link"][1].split(" &")[0]} {ic("arrow")}</a>' if s.get("link") else ""
        out.append(f"""<li class="tcard{variant}" style="grid-column:{col};grid-row:{row+1}" data-start="2026-10-16T{s['s']}:00+05:30" data-end="2026-10-16T{s['e']}:00+05:30">
<span class="stop__live">● LIVE NOW</span>
<div class="tcard__top"><div class="tcard__time">{s['time']}<small>{s['sub']}</small></div><span class="tcard__node">{ic(s['icon'])}</span></div>
<h3>{s['title']}</h3><p>{SHORT[s['title']]}</p><div class="stop__tags">{tags}</div>{link}
{f'<span class="tarrow tarrow--{arrow}"></span>' if arrow else ''}</li>""")
    return f'<ol class="tl" style="list-style:none;padding:0">{"".join(out)}</ol>'

def timeline_page():
    body = page_head("Fri 16 Oct 2026 · 9:00 AM – 6:00 PM", "The day <span class=\"t\">plan</span>", "Follow the arrows: opening → Round 1 (PPT + base prototype) → elimination → Round 2 (complete prototype by 4 PM) → winners.")
    body += f'<section class="band band-wash band--tight"><div class="wrap">{tcards()}</div></section>'
    return wrapp("timeline", "Timeline · DATATHON 2026", "DATATHON event itinerary for 16 October 2026.", body)

# ---------------- home ----------------
def strip():
    items = []
    n = len(STOPS)
    for i, s in enumerate(STOPS):
        row, k = i // 5, i % 5
        col = k + 1 if row == 0 else 5 - k
        if i == n - 1: arrow = ""
        elif k == 4: arrow = "d"
        else: arrow = "r" if row == 0 else "l"
        glyph = {"r": "→", "l": "←", "d": "↓"}.get(arrow, "")
        hl = " strip__box--hl" if s["cls"] in ("stop--milestone", "stop--winner") else ""
        label = s["title"].replace("Round 1 · ", "R1 · ").replace("Round 2 · ", "R2 · ").replace("Round 2 Demos", "R2 Demos").replace(" Round", "")
        items.append(f'<a class="strip__item" href="timeline.html" style="grid-column:{col};grid-row:{row+1}"><div class="strip__box{hl}" data-start="2026-10-16T{s["s"]}:00+05:30" data-end="2026-10-16T{s["e"]}:00+05:30"><b>{s["time"]}</b><span>{label}</span></div>{f"<span class=\"strip__arrow strip__arrow--{arrow}\" aria-hidden=\"true\">{glyph}</span>" if arrow else ""}</a>')
    return f'<div class="strip" role="list">{"".join(items)}</div>'

TILES = [
 ("01", "timeline.html", "clock", "Timeline", "Full itinerary with arrows, 9 AM to 6 PM.", "band-cyan"),
 ("02", "problem-statements.html", "db", "Problem Statements", "Unlocks Fri 16 Oct at 10:00 AM, with a live countdown.", "band-wash"),
 ("03", "ppt.html", "file", "Round 1 PPT", "Idea PPT + base prototype. USP + MVP are mandatory.", "band-dark"),
 ("04", "round2.html", "cube", "Round 2", "Submit your GitHub repo and model details by 4 PM.", "band-cyan"),
 ("05", "judging.html", "trophy", "Judging & Prizes", "100-mark rubric (from-scratch ML scores highest) and the ₹4,500 pool.", "band-wash"),
 ("06", "rules.html", "check", "Rules", "The 15 rules every team follows.", "band-dark"),
]
def home_page():
    chain = "".join(f'<span class="chip">{t}</span>' + ('<span class="chain__a" aria-hidden="true">→</span>' if k < 4 else "") for k, t in enumerate(["Data", "Analyze", "Model", "Build", "Deploy"]))
    hero = f"""<section class="band band-dark hero"><div class="wrap">
<p class="hero__kicker">A product-focused data science hackathon · VIT-AP</p>
<h1 class="display hero__title">DATA<span class="t">T</span>HON
<span class="sticker sticker--hide-sm" style="--rot:-8deg; top:4%; right:2%">USP + MVP</span>
<span class="sticker sticker--white sticker--hide-sm" style="--rot:7deg; bottom:-6%; right:24%">Real data</span>
</h1>
<div class="hero__sub"><span>From data to</span><span class="hl">Deployable</span><span>ideas</span></div>
<div class="chain">{chain}</div>
<div class="bento">
<div class="bcell b-date"><small>Friday</small><b>16 Oct 2026</b><span>9:00 AM – 6:00 PM · Venue: CB G20, VIT-AP University</span></div>
<div class="bcell b-prize"><small>Prize pool</small><b>₹4,500</b><span>1st ₹2,000 · 2nd ₹1,500 · 3rd ₹1,000</span></div>
<div class="bcell b-team"><small>Teams</small><b>Solo or Duo</b><span>1–2 members · OD provided</span></div>
<div class="bcell b-rounds"><a class="round" href="ppt.html"><small>Round 1 · 10 AM–12 PM</small><b>PPT + base prototype</b></a><span class="round__arrow" aria-hidden="true">→</span><a class="round" href="round2.html"><small>Round 2 · till 4 PM</small><b>Complete prototype</b></a></div>
<a class="bcell b-reg" href="{REG}" target="_blank" rel="noopener"><img src="assets/qr.png" alt="Registration QR code" width="96" height="96"><div><b>Register</b><span>Scan or tap {ic('arrow')}</span></div></a>
</div>
<div class="bigcount"><div class="bigcount__label"><small>Starts in</small><span>Fri 16 Oct 2026 · 9:00 AM · CB G20, VIT-AP University</span></div><div class="countdown" id="countdown" data-target="2026-10-16T09:00:00+05:30" aria-live="off"></div></div>
</div></section>"""
    tiles = "".join(f'<a class="card tile {b}" href="{h}" style="background:var(--bg);color:var(--fg);--line:{ "#fff" if b=="band-dark" else "#000"}"><div class="tile__top"><span class="tile__no">{n}</span><span class="tile__badge">{ic(i)}</span></div><h3>{t}</h3><p>{d}</p><span class="tile__go">Open {ic("arrow")}</span></a>' for n, h, i, t, d, b in TILES)
    body = hero + f"""
<section class="band band-wash band--tight" id="timeline"><div class="wrap">
<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap;margin-bottom:18px"><div><span class="eyebrow">Event day · Fri 16 Oct 2026</span><h2 class="display" style="font-size:clamp(40px,6vw,84px);margin-top:14px">The day <span class="t">plan</span></h2></div><a class="btn btn--fill" href="timeline.html">Open full timeline {ic('arrow')}</a></div>
{tcards()}
</div></section>
<section class="band band-dark band--tight"><div class="wrap">
<div class="tiles">{tiles}</div>
</div></section>"""
    return wrapp("home", "DATATHON 2026 · VIT-AP", "DATATHON — a product-focused Data Science hackathon by Data Science Club (DSC) with IIEC, VIT-AP University. 16 October 2026.", body)

# ---------------- ppt ----------------
def ppt_page():
    body = page_head("Round 1 · 10:00 AM – 12:00 PM", "Idea <span class=\"t\">PPT</span> round", "Round 1 = this PPT plus a base prototype. Round 2 (by 4:00 PM) is the complete prototype. Sections marked MUST are mandatory.")
    slides = "".join(f'<li><div><b>{t}{" <span class=must>MUST</span>" if m else ""}</b><span>{d}</span></div></li>' for t, d, m in PPT_SLIDES)
    body += f"""<section class="band band-wash band--tight"><div class="wrap"><div class="ppt-layout">
<div class="stack">
<div class="card" style="background:var(--carbon);color:var(--paper);border-radius:40px;padding:32px;--line:#000">
<span class="eyebrow">Template</span><h3 class="display" style="font-size:clamp(34px,4vw,54px);margin:18px 0">Datathon<br>Round 1 <span class="t" style="color:var(--cyan);-webkit-text-stroke:0">PPT</span></h3>
<p style="color:var(--mist)">8 slides max. Points and diagrams, not paragraphs. Team name on every slide.</p>
<div class="cta-row"><a class="btn btn--lg" style="background:var(--cyan);color:var(--carbon);border-color:var(--cyan)" href="downloads/DATATHON-Round1-Idea-PPT-Template.pptx" download>Download PPT {ic('download')}</a></div></div>
<div class="flow"><span class="chip chip--cyan">Problem</span>{ic('arrow')}<span class="chip">User</span>{ic('arrow')}<span class="chip">Data</span>{ic('arrow')}<span class="chip">Model</span>{ic('arrow')}<span class="chip">Product</span>{ic('arrow')}<span class="chip chip--cyan">Demo</span></div>
</div>
<ol class="slide-list sgrid">{slides}</ol>
</div></div></section>"""
    return wrapp("ppt", "Round 1 PPT · DATATHON 2026", "Download the DATATHON Round 1 idea PPT template.", body)

# ---------------- judging ----------------
def judging_page():
    cards = "".join(f'<div class="rcard"><div class="rcard__top"><b>{n}</b><span class="rcard__pts">{m}</span></div><small>{d}</small><div class="rubric__bar" role="img" aria-label="{m} of 100 marks"><i style="width:{m*5}%"></i></div></div>' for n, d, m in RUBRIC)
    body = page_head("One rubric · all four tracks", "How you’re <span class=\"t\">judged</span>", "100 marks. Judges score what is demonstrated. Models trained from scratch are weighted most; relying on an API key scores lowest.")
    body += f"""<section class="band band-wash band--tight"><div class="wrap">
<div class="tiers"><div class="tier tier--top"><small>ML model from scratch</small><b>Highest</b><span>Trained by your team on the provided data. Up to the full 25 marks.</span></div><div class="tier"><small>Fine-tuned model</small><b>Partial</b><span>Pretrained model you meaningfully fine-tune. Reduced marks.</span></div><div class="tier tier--low"><small>API key only</small><b>Lowest</b><span>Hosted / LLM API with no model of your own. Allowed as a supporting part, minimal marks.</span></div></div>
<div class="rgrid">{cards}<div class="rcard rcard--total" style="grid-column:1/-1;display:flex;justify-content:space-between;align-items:center"><b style="font-size:20px">Total marks</b><span class="rcard__pts">100</span></div></div>
</div></section>
<section class="band band-cyan band--tight"><div class="wrap">
<span class="eyebrow">Winners announced 5:30 PM</span><h2 class="display" style="font-size:clamp(40px,6vw,84px);margin:14px 0 22px">Prize <span class="t">pool</span></h2>
<div class="prizes4"><div class="prize prize--1"><small>1st prize</small><b>₹2,000</b></div><div class="prize"><small>2nd prize</small><b>₹1,500</b></div><div class="prize"><small>3rd prize</small><b>₹1,000</b></div><div class="prize" style="background:var(--carbon);color:var(--paper)"><small>Total pool</small><b style="color:var(--cyan)">₹4,500</b></div></div>
</div></section>"""
    return wrapp("judging", "Judging & Prizes · DATATHON 2026", "DATATHON judging rubric (100 marks) and prize pool.", body)

# ---------------- rules ----------------
def rules_page():
    body = page_head("The fine print", "Ground <span class=\"t\">rules</span>", "15 rules. Tap any rule to expand.")
    r = "".join(f'<details class="rule"><summary data-n="{i+1:02d}">{t}</summary><p>{d}</p></details>' for i, (t, d) in enumerate(RULES))
    body += f"""<section class="band band-dark band--tight"><div class="wrap">
<div class="rules">{r}</div>
</div></section>"""
    return wrapp("rules", "Rules · DATATHON 2026", "DATATHON rules.", body)

# ---------------- problem statements ----------------
def users_list(u):
    u = u.rstrip(".").replace(", and ", ", ").replace(" and ", ", ")
    return [x.strip().capitalize() for x in u.split(",") if x.strip()]

def ptrack(t):
    fs = stats[t["folder"]]
    tot = sum(v[0] for v in fs.values())
    rows = "".join(f"""<div class="file"><div><b>{name}</b><small>{desc}</small></div><a class="btn btn--sm btn--fill" href="datasets/{t['folder']}/{name}" download>{ic('download')} CSV</a>
<div class="file__meta"><span class="chip">{fs[name][0]:,} rows</span><span class="chip">{human(fs[name][1])}</span></div></div>""" for name, desc in t["files"])
    users = "".join(f'<span class="chip">{u}</span>' for u in users_list(t["users"]))
    outs = "".join(f"<li>{o}</li>" for o in t["outcomes"])
    return f"""<section class="ptrack" id="track-{t['n']}" role="tabpanel" aria-labelledby="tab-{t['n']}" data-track="{t['n']}">
<div class="ptrack__head"><div class="track__dom"><span class="chip chip--cyan">{ic(t['icon'])} Track {t['n']} · {t['dom']}</span><span class="chip">{len(t['files'])} files · {tot:,} rows</span></div>
<h2 class="ptrack__title">{t['title']}</h2><p class="ptrack__challenge">{t['challenge']}</p></div>
<div class="ptrack__body">
<div class="pcol">
<div class="pblock"><h4>Built for</h4><div class="chips">{users}</div></div>
<div class="pblock"><h4>What you could build</h4><ul class="ogrid">{outs}</ul></div>
<details class="more"><summary>Full problem brief</summary><p>{t['problem']}</p></details>
<details class="more"><summary>How the data helps</summary><p>{t['helps']}</p></details>
<details class="more"><summary>Possible ML / data-science work</summary><p>{t['ml']}</p></details>
<div class="question"><small>Useful product question</small><p>“{t['q']}”</p></div>
</div>
<aside class="pcol" aria-label="Track {t['n']} datasets">
<div class="files"><div class="files__head"><h4>Download datasets</h4><a class="btn btn--sm btn--fill" href="datasets/{t['folder']}.zip" download>{ic('download')} All (.zip)</a></div>
{rows}
<div class="file"><div><b>README.txt</b><small>Joins and caveats for this track.</small></div><a class="btn btn--sm" href="datasets/{t['folder']}/README.txt" download>{ic('download')} TXT</a></div>
<p class="files__note">Synthetic educational data, not real records.</p></div>
</aside></div></section>"""

def problems_page():
    zips = "".join(f'<a class="btn btn--sm" href="datasets/{t["folder"]}.zip" download>{ic("download")} 0{t["n"]} {t["dom"]}</a>' for t in TRACKS)
    dlbar = f'<div class="dlbar"><span class="label">Download</span><a class="btn btn--fill" href="datasets/DATATHON_All_Track_Datasets.zip" download>{ic("download")} All 4 tracks (.zip)</a>{zips}</div>'
    tabs = "".join(f'<button class="ptab" role="tab" id="tab-{t["n"]}" aria-controls="track-{t["n"]}" aria-selected="false" data-n="{t["n"]}"><span class="ptab__no">0{t["n"]}</span><b>{t["title"]}</b><small>{t["dom"]}</small></button>' for t in TRACKS)
    body = page_head("Released 10:00 AM · Round 1", "Problem <span class=\"t\">statements</span>", "Pick one track. Build a working data-powered product, not just a notebook.", dlbar)
    team_opts = "".join(f'<option value="0{t["n"]} {t["dom"]}">Track {t["n"]} · {t["dom"]} — {t["title"]}</option>' for t in TRACKS)
    TEAM_FORM = '<form id="teamform" class="r2form teamform" novalidate>\n<fieldset><legend><span>★</span> Register your team &amp; track</legend>\n<p class="muted" style="margin:0 0 14px">Fill this once. It tells the judges which problem your team picked. You can save again to correct anything.</p>\n<div class="fgrid tf3">\n<label class="fld"><span>Team name *</span><input type="text" name="team" required></label>\n<label class="fld"><span>Members (1–2) *</span><input type="text" name="members" required placeholder="Name, Name"></label>\n<label class="fld"><span>Contact email *</span><input type="email" name="email" required></label>\n<label class="fld"><span>Number of people *</span><select name="size" required><option value="">Choose</option><option value="1">1 (solo)</option><option value="2">2 (duo)</option></select></label>\n<label class="fld tf-wide"><span>Track chosen *</span><select name="track" required><option value="">Choose your track</option>{team_opts}</select></label>\n<div class="tf-btn"><button class="btn btn--fill btn--lg" type="submit">Save my team</button></div>\n</div>\n<div id="teamout" class="r2out" hidden></div>\n</fieldset></form>\n'.replace("{team_opts}", team_opts)
    body += f"""<div class="lock" id="lock" hidden><div><span class="eyebrow" style="justify-content:center">Locked until release</span><h2 class="display" style="margin-top:24px">Drops at <span class="t">10:00</span></h2><p>Friday 16 October 2026, 10:00 AM IST.</p><div class="countdown" id="lockcd" data-target="2026-10-16T10:00:00+05:30" style="justify-content:center"></div><p><a class="btn" href="index.html">Back to home</a></p></div></div>
<section class="band band-wash band--tight"><div class="wrap">
{TEAM_FORM}
<div class="ptabs" role="tablist" aria-label="Tracks">{tabs}</div>
{''.join(ptrack(t) for t in TRACKS)}
</div></section>"""
    return wrapp("problems", "Problem Statements & Datasets · DATATHON 2026", "All four DATATHON problem statements with downloadable datasets.", body, '\n<script src="js/config.js"></script>\n<script src="js/tabs.js"></script>\n<script src="js/lock.js"></script>\n<script src="js/teamreg.js"></script>')

from pages_r2 import make
round2_page, judge_page = make(wrapp, page_head, ic, TRACKS, REG)
for name, fn in [("round2.html", round2_page), ("judge.html", judge_page), ("index.html", home_page), ("timeline.html", timeline_page), ("ppt.html", ppt_page), ("judging.html", judging_page), ("rules.html", rules_page), ("problem-statements.html", problems_page)]:
    open(os.path.join(SITE, name), "w", encoding="utf-8").write(fn())
print("built", SITE)
