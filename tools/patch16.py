"""Add registration numbers to both team forms, the payloads and the Google Sheet tabs."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def edit(path, pairs):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (path, a[:60])
        s = s.replace(a, b, 1)
    open(path, 'w', encoding='utf-8').write(s)

REG_PH = "e.g. 23BCE1234, 23BCE5678"
edit('pages_r2.py', [(
    '{f("Members (1–2)", "members", req=True, ph="Name, Name")}',
    '{f("Members (1–2)", "members", req=True, ph="Name, Name")}{f("Registration number(s) *", "regNos", req=True, ph="' + REG_PH + '")}'.replace(' *", "regNos"', '", "regNos"'))])
edit('build2.py', [(
    '<label class="fld"><span>Members (1–2) *</span><input type="text" name="members" required placeholder="Name, Name"></label>',
    '<label class="fld"><span>Members (1–2) *</span><input type="text" name="members" required placeholder="Name, Name"></label>\\n<label class="fld"><span>Registration number(s) *</span><input type="text" name="regNos" required placeholder="' + REG_PH + '"></label>')])
edit('../site/js/round2.js', [
    ("members: o.members || '',", "members: o.members || '', regNos: o.regNos || '',"),
    ("['team', 'members', 'email', 'size', 'track']", "['team', 'members', 'regNos', 'email', 'size', 'track']")])
edit('../site/js/teamreg.js', [
    ("['team', 'members', 'email', 'size', 'track']", "['team', 'members', 'regNos', 'email', 'size', 'track']"),
    ("members: form.elements.members.value.trim(),", "members: form.elements.members.value.trim(), regNos: form.elements.regNos.value.trim(),")])
edit('apps-script-receiver.gs', [
    ("'email', 'json'];", "'email', 'json', 'regNos'];"),
    ("var TEAM_HEAD = ['Team name', 'Track', 'Members', 'People'];", "var TEAM_HEAD = ['Team name', 'Track', 'Members', 'People', 'Reg numbers'];"),
    ("    sh.setFrozenRows(1);\n  }\n  return sh;",
     "    sh.setFrozenRows(1);\n  } else if (sh.getRange(1, head.length).getValue() !== head[head.length - 1]) {\n    sh.getRange(1, 1, 1, head.length).setValues([head]);   // add new column titles to an existing tab\n  }\n  return sh;"),
    ("  var vals = [d.team, d.track, d.members, Number(d.size) || ''];", "  var vals = [d.team, d.track, d.members, Number(d.size) || '', d.regNos || ''];"),
    ("sh.getRange(i + 1, 1, 1, 4).setValues([vals])", "sh.getRange(i + 1, 1, 1, vals.length).setValues([vals])"),
    ("d.email, JSON.stringify(d)\n", "d.email, JSON.stringify(d), d.regNos || ''\n"),
])
print('ok')
