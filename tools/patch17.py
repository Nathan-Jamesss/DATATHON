"""Per-member name + registration number (member 2 shown for duo teams). Hidden 'members'/'regNos' keep the sheet format."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def edit(path, pairs):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (path, a[:70])
        s = s.replace(a, b, 1)
    open(path, 'w', encoding='utf-8').write(s)

BLOCK = ('<div class="fld fld--wide memblock"><div class="fgrid">'
         '<label class="fld"><span>Member 1 name *</span><input type="text" name="m1name" required></label>'
         '<label class="fld"><span>Member 1 registration no. *</span><input type="text" name="m1reg" required placeholder="e.g. 23BCE1234"></label>'
         '<label class="fld" data-m2 hidden><span>Member 2 name *</span><input type="text" name="m2name" disabled></label>'
         '<label class="fld" data-m2 hidden><span>Member 2 registration no. *</span><input type="text" name="m2reg" disabled placeholder="e.g. 23BCE5678"></label>'
         '</div><input type="hidden" name="members"><input type="hidden" name="regNos"></div>')
SIZE = ('<label class="fld"><span>Number of people *</span><select name="size" required><option value="">Choose</option>'
        '<option value="1">1 (solo)</option><option value="2">2 (duo)</option></select></label>')

# Round 2 form: team name + size first, then members, then email + track
edit('pages_r2.py', [(
    '{f("Team name", "team", req=True)}{f("Members (1–2)", "members", req=True, ph="Name, Name")}{f("Registration number(s) *", "regNos", req=True, ph="e.g. 23BCE1234, 23BCE5678")}\n'
    '{f("Contact email", "email", "email", True)}\n'
    '<label class="fld"><span>Number of people *</span><select name="size" required><option value="">Choose</option><option value="1">1 (solo)</option><option value="2">2 (duo)</option></select></label>\n',
    '{f("Team name", "team", req=True)}\n' + SIZE + '\n' + BLOCK + '\n{f("Contact email", "email", "email", True)}\n')])

# team registration form on the Problem Statements page (inside a Python string literal -> no raw newlines)
edit('build2.py', [
    ('<label class="fld"><span>Members (1–2) *</span><input type="text" name="members" required placeholder="Name, Name"></label>\\n<label class="fld"><span>Registration number(s) *</span><input type="text" name="regNos" required placeholder="e.g. 23BCE1234, 23BCE5678"></label>\\n',
     ''),
    ('<label class="fld"><span>Number of people *</span><select name="size" required><option value="">Choose</option><option value="1">1 (solo)</option><option value="2">2 (duo)</option></select></label>\\n',
     SIZE + '\\n' + BLOCK.replace('"fld fld--wide memblock"', '"fld tf-wide memblock"') + '\\n'),
])
edit('build2.py', [("'\\n<script src=\"js/config.js\"></script>\\n<script src=\"js/tabs.js\"></script>\\n<script src=\"js/lock.js\"></script>\\n<script src=\"js/teamreg.js\"></script>'",
                    "'\\n<script src=\"js/config.js\"></script>\\n<script src=\"js/tabs.js\"></script>\\n<script src=\"js/lock.js\"></script>\\n<script src=\"js/teamreg.js\"></script>\\n<script src=\"js/members.js\"></script>'")])
edit('pages_r2.py', [("'\\n<script src=\"js/config.js\"></script>\\n<script src=\"js/repocheck.js\"></script>\\n<script src=\"js/round2.js\"></script>'",
                      "'\\n<script src=\"js/config.js\"></script>\\n<script src=\"js/repocheck.js\"></script>\\n<script src=\"js/round2.js\"></script>\\n<script src=\"js/members.js\"></script>'")])
print('ok')
