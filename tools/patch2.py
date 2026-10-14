import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = open('build2.py', encoding='utf-8').read()

def r(a, b):
    global s
    assert a in s, a[:60]
    s = s.replace(a, b)

r(' "Round 1 · Ideation + Base Prototype": "PPT round: frame the user, define USP + MVP, show a base prototype.",',
  ' "Round 1 · PPT + Base Prototype": "Idea PPT (USP + MVP mandatory) plus a base prototype on the dataset.",')
r(' "Final Round": "Connect your model to a working product; finalise demo and slides.",',
  ' "Round 2 · Complete Prototype": "Finish the complete prototype by 4:00 PM: model + working product.",')
r(' "Final Demos & Judging": "Live demo, USP and data use, scored on the 100-mark rubric.",',
  ' "Round 2 Demos & Judging": "Live demo of the complete prototype, scored on the 100-mark rubric.",')
r('.replace("Round 1 · ", "R1 · ")', '.replace("Round 1 · ", "R1 · ").replace("Round 2 · ", "R2 · ").replace("Round 2 Demos", "R2 Demos")')
r("Follow the arrows: opening ceremony → Round 1 PPT round → elimination → final round → winners.",
  "Follow the arrows: opening → Round 1 (PPT + base prototype) → elimination → Round 2 (complete prototype by 4 PM) → winners.")
r('"The Datathon idea PPT template. USP + MVP are mandatory."', '"Round 1: idea PPT + base prototype. USP + MVP are mandatory."')
r('"100-mark rubric and the ₹4,500 prize pool."', '"100-mark rubric (from-scratch ML scores highest) and the ₹4,500 prize pool."')
r('Pretrained APIs / LLM calls alone don’t count.', 'An API key or pretrained model alone earns the lowest marks; training from scratch earns the most.')
r('"Submit your Round 1 idea in the official Datathon PPT template. Sections marked MUST are mandatory."',
  '"Round 1 = this PPT plus a base prototype. Round 2 (by 4:00 PM) is the complete prototype. Sections marked MUST are mandatory."')
r('<div class="rgrid">{cards}',
  '<div class="tiers"><div class="tier tier--top"><small>ML model from scratch</small><b>Highest</b><span>Trained by your team on the provided data. Up to the full 20 marks.</span></div><div class="tier"><small>Fine-tuned model</small><b>Partial</b><span>Pretrained model you meaningfully fine-tune. Reduced marks.</span></div><div class="tier tier--low"><small>API key only</small><b>Lowest</b><span>Hosted / LLM API with no model of your own. Allowed as a supporting part, minimal marks.</span></div></div>\n<div class="rgrid">{cards}')
r('"100 marks. Judges score what is demonstrated, not who processed the most rows."',
  '"100 marks. Judges score what is demonstrated. Models trained from scratch are weighted most; relying on an API key scores lowest."')
r('<link rel="stylesheet" href="css/v2.css">', '<link rel="stylesheet" href="css/v2.css">\\n<link rel="stylesheet" href="css/v3.css">')

i = s.index('def home_page():'); j = s.index('# ---------------- ppt')
new = '''def home_page():
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
<div class="bcell b-date"><small>Friday</small><b>16 Oct 2026</b><span>9:00 AM – 6:00 PM · VIT-AP University · venue updating soon</span></div>
<div class="bcell b-prize"><small>Prize pool</small><b>₹4,500</b><span>1st ₹2,000 · 2nd ₹1,500 · 3rd ₹1,000</span></div>
<div class="bcell b-team"><small>Teams</small><b>Solo or Duo</b><span>1–2 members · OD provided</span></div>
<div class="bcell b-rounds"><div class="round"><small>Round 1 · 10 AM–12 PM</small><b>PPT + base prototype</b></div><span class="round__arrow" aria-hidden="true">→</span><div class="round"><small>Round 2 · till 4 PM</small><b>Complete prototype</b></div></div>
<div class="bcell b-count"><small>Starts in</small><div class="countdown" id="countdown" data-target="2026-10-16T09:00:00+05:30" aria-live="off"></div></div>
<a class="bcell b-reg" href="{REG}" target="_blank" rel="noopener"><img src="assets/qr.png" alt="Registration QR code" width="96" height="96"><div><b>Register</b><span>Scan or tap {ic('arrow')}</span></div></a>
</div>
</div></section>"""
    tiles = "".join(f'<a class="card tile {b}" href="{h}" style="background:var(--bg);color:var(--fg);--line:{ "#fff" if b=="band-dark" else "#000"}"><div class="tile__top"><span class="tile__no">{n}</span><span class="tile__badge">{ic(i)}</span></div><h3>{t}</h3><p>{d}</p><span class="tile__go">Open {ic("arrow")}</span></a>' for n, h, i, t, d, b in TILES)
    body = hero + f"""
<section class="band band-wash band--tight" id="timeline"><div class="wrap">
<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap;margin-bottom:18px"><div><span class="eyebrow">Event day · Fri 16 Oct 2026</span><h2 class="display" style="font-size:clamp(40px,6vw,84px);margin-top:14px">The day <span class="t">plan</span></h2></div><a class="btn btn--fill" href="timeline.html">Open full timeline {ic('arrow')}</a></div>
{strip()}
</div></section>
<section class="band band-dark band--tight"><div class="wrap">
<div class="tiles">{tiles}</div>
</div></section>"""
    return wrapp("home", "DATATHON 2026 · VIT-AP", "DATATHON — a product-focused Data Science hackathon by Data Science Club (DSC) with IIEC, VIT-AP University. 16 October 2026.", body)

'''
s = s[:i] + new + s[j:]
open('build2.py', 'w', encoding='utf-8').write(s)
print("patched")
