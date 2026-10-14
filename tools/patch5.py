import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---- build.py: Round 2 stop gets a link
b = open('build.py', encoding='utf-8').read()
a = 'tags=["Complete prototype", "Submission freeze 4:00 PM"]),'
assert a in b
b = b.replace(a, 'tags=["Complete prototype", "Submission freeze 4:00 PM"], link=("round2.html", "Submit your repo")),')
open('build.py', 'w', encoding='utf-8').write(b)

s = open('build2.py', encoding='utf-8').read()
def r(a, c):
    global s
    assert a in s, a[:70]
    s = s.replace(a, c)

# nav: add Round 2
r('("ppt.html", "Round 1 PPT", "ppt"), ("judging.html"', '("ppt.html", "Round 1 PPT", "ppt"), ("round2.html", "Round 2", "round2"), ("judging.html"')
# css list
r('("v2", "v3", "v4")', '("v2", "v3", "v4", "v5")')
# footer: judges link
r('def footer2(extra=""):\n    f = footer()', 'def footer2(extra=""):\n    f = footer().replace(\'<div class="footer__meta">\', \'<div class="footer__meta"><a href="judge.html">Judges</a>\')')
# hero rounds -> links
r('<div class="round"><small>Round 1 · 10 AM–12 PM</small><b>PPT + base prototype</b></div>', '<a class="round" href="ppt.html"><small>Round 1 · 10 AM–12 PM</small><b>PPT + base prototype</b></a>')
r('<div class="round"><small>Round 2 · till 4 PM</small><b>Complete prototype</b></div>', '<a class="round" href="round2.html"><small>Round 2 · till 4 PM</small><b>Complete prototype</b></a>')
# tiles
i = s.index('TILES = ['); j = s.index(']\n', i) + 2
s = s[:i] + '''TILES = [
 ("01", "timeline.html", "clock", "Timeline", "Full itinerary with arrows, 9 AM to 6 PM.", "band-cyan"),
 ("02", "problem-statements.html", "db", "Problem Statements", "4 tracks and every downloadable dataset.", "band-wash"),
 ("03", "ppt.html", "file", "Round 1 PPT", "Idea PPT + base prototype. USP + MVP are mandatory.", "band-dark"),
 ("04", "round2.html", "cube", "Round 2", "Submit your GitHub repo and model details by 4 PM.", "band-cyan"),
 ("05", "judging.html", "trophy", "Judging & Prizes", "100-mark rubric (from-scratch ML scores highest) and the ₹4,500 pool.", "band-wash"),
 ("06", "rules.html", "check", "Rules", "15 rules plus first steps for every team.", "band-dark"),
]
''' + s[j:]
# pages
r('for name, fn in [("index.html", home_page)', 'from pages_r2 import make\nround2_page, judge_page = make(wrapp, page_head, ic, TRACKS, REG)\nfor name, fn in [("round2.html", round2_page), ("judge.html", judge_page), ("index.html", home_page)')
open('build2.py', 'w', encoding='utf-8').write(s)
print('ok')
