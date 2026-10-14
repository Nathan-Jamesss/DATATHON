import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = open('build2.py', encoding='utf-8').read()

# ---- strip: 2-row snake, no horizontal scroll
i = s.index('def strip():'); j = s.index('TILES = [')
new_strip = '''def strip():
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
        items.append(f'<a class="strip__item" href="timeline.html" style="grid-column:{col};grid-row:{row+1}"><div class="strip__box{hl}" data-start="2026-10-16T{s["s"]}:00+05:30" data-end="2026-10-16T{s["e"]}:00+05:30"><b>{s["time"]}</b><span>{label}</span></div>{f"<span class=\\"strip__arrow strip__arrow--{arrow}\\" aria-hidden=\\"true\\">{glyph}</span>" if arrow else ""}</a>')
    return f'<div class="strip" role="list">{"".join(items)}</div>'

'''
s = s[:i] + new_strip + s[j:]

# ---- countdown: remove from bento, add big panel after it
a = '<div class="bcell b-count"><small>Starts in</small><div class="countdown" id="countdown" data-target="2026-10-16T09:00:00+05:30" aria-live="off"></div></div>\n'
assert a in s
s = s.replace(a, '')
b = '</a>\n</div>\n</div></section>"""\n    tiles ='
assert b in s
s = s.replace(b, '''</a>
</div>
<div class="bigcount"><div class="bigcount__label"><small>Starts in</small><span>Fri 16 Oct 2026 · 9:00 AM · VIT-AP University</span></div><div class="countdown" id="countdown" data-target="2026-10-16T09:00:00+05:30" aria-live="off"></div></div>
</div></section>"""
    tiles =''')
open('build2.py', 'w', encoding='utf-8').write(s)
print('ok')
