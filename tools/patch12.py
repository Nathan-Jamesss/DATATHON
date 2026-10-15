import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def edit(path, pairs):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (path, a[:70])
        s = s.replace(a, b, 1)
    open(path, 'w', encoding='utf-8').write(s)

TEAM_FORM = '''<form id="teamform" class="r2form teamform" novalidate>
<fieldset><legend><span>★</span> Register your team &amp; track</legend>
<p class="muted" style="margin:0 0 14px">Fill this once. It tells the judges which problem your team picked. You can save again to correct anything.</p>
<div class="fgrid tf3">
<label class="fld"><span>Team name *</span><input type="text" name="team" required></label>
<label class="fld"><span>Members (1–2) *</span><input type="text" name="members" required placeholder="Name, Name"></label>
<label class="fld"><span>Contact email *</span><input type="email" name="email" required></label>
<label class="fld"><span>Number of people *</span><select name="size" required><option value="">Choose</option><option value="1">1 (solo)</option><option value="2">2 (duo)</option></select></label>
<label class="fld tf-wide"><span>Track chosen *</span><select name="track" required><option value="">Choose your track</option>{team_opts}</select></label>
<div class="tf-btn"><button class="btn btn--fill btn--lg" type="submit">Save my team</button></div>
</div>
<div id="teamout" class="r2out" hidden></div>
</fieldset></form>
'''

edit('build2.py', [
 ('<div class="ptabs" role="tablist" aria-label="Tracks">',
  '{TEAM_FORM}\n<div class="ptabs" role="tablist" aria-label="Tracks">'),
 ('    body += f"""<div class="lock" id="lock" hidden>',
  '    team_opts = "".join(f\'<option value="0{t["n"]} {t["dom"]}">Track {t["n"]} · {t["dom"]} — {t["title"]}</option>\' for t in TRACKS)\n    TEAM_FORM = ' + repr(TEAM_FORM) + '.replace("{team_opts}", team_opts)\n    body += f"""<div class="lock" id="lock" hidden>'),
 ("'\\n<script src=\"js/tabs.js\"></script>\\n<script src=\"js/lock.js\"></script>'",
  "'\\n<script src=\"js/config.js\"></script>\\n<script src=\"js/tabs.js\"></script>\\n<script src=\"js/lock.js\"></script>\\n<script src=\"js/teamreg.js\"></script>'"),
])

edit('../site/js/round2.js', [(
 "  var verifyBtn = document.getElementById('verify');",
 "  // prefill from the team registration on the Problem Statements page\n  try {\n    var tm = JSON.parse(localStorage.getItem('dt_team') || 'null');\n    if (tm) ['team', 'members', 'email', 'size', 'track'].forEach(function (k) { var el = form.elements[k]; if (el && !el.value && tm[k]) el.value = tm[k]; });\n  } catch (e) {}\n\n  var verifyBtn = document.getElementById('verify');")])

with open('../site/css/v5.css', 'a', encoding='utf-8') as f:
    f.write('\n.tf3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }\n.tf-wide { grid-column: span 2; }\n.tf-btn { display: flex; align-items: end; }\n.teamform { margin-bottom: 24px; }\n@media (max-width: 900px) { .tf3 { grid-template-columns: minmax(0, 1fr); } .tf-wide { grid-column: auto; } }\n')
print('ok')
