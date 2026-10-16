"""Phone number per member (member 2 only for duo teams), carried to both Sheet tabs."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def edit(path, pairs, count=1):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (path, a[:70])
        s = s.replace(a, b, count)
    open(path, 'w', encoding='utf-8').write(s)

PH1 = '<label class="fld"><span>Member 1 phone *</span><input type="tel" name="m1phone" required inputmode="tel" pattern="[+]?[0-9 -]{10,15}" placeholder="10-digit mobile"></label>'
PH2 = '<label class="fld" data-m2 hidden><span>Member 2 phone *</span><input type="tel" name="m2phone" disabled inputmode="tel" pattern="[+]?[0-9 -]{10,15}" placeholder="10-digit mobile"></label>'
R1 = 'placeholder="e.g. 23BCE1234"></label>'
R2 = 'placeholder="e.g. 23BCE5678"></label>'
HID = '<input type="hidden" name="regNos"></div>'
for p in ('pages_r2.py', 'build2.py'):
    edit(p, [(R1, R1 + PH1), (R2, R2 + PH2), (HID, '<input type="hidden" name="regNos"><input type="hidden" name="phones"></div>')])

edit('../site/js/members.js', [
    ("      f('regNos').value = [f('m1reg').value, duo ? f('m2reg').value : ''].map(function (s) { return s.trim().toUpperCase(); }).filter(Boolean).join(', ');\n",
     "      f('regNos').value = [f('m1reg').value, duo ? f('m2reg').value : ''].map(function (s) { return s.trim().toUpperCase(); }).filter(Boolean).join(', ');\n"
     "      f('phones').value = [f('m1phone').value, duo ? f('m2phone').value : ''].map(function (s) { return s.trim(); }).filter(Boolean).join(', ');\n"),
    ("      var n = (f('members').value || '').split(','), r = (f('regNos').value || '').split(',');\n",
     "      var n = (f('members').value || '').split(','), r = (f('regNos').value || '').split(','), ph = (f('phones').value || '').split(',');\n"
     "      if (!f('m1phone').value && ph[0]) f('m1phone').value = ph[0].trim();\n"
     "      if (!f('m2phone').value && ph[1]) f('m2phone').value = ph[1].trim();\n"),
])
edit('../site/js/round2.js', [
    ("regNos: o.regNos || '',", "regNos: o.regNos || '', phones: o.phones || '',"),
    ("['team', 'members', 'regNos', 'email', 'size', 'track']", "['team', 'members', 'regNos', 'phones', 'email', 'size', 'track']")])
edit('../site/js/teamreg.js', [
    ("['team', 'members', 'regNos', 'email', 'size', 'track']", "['team', 'members', 'regNos', 'phones', 'email', 'size', 'track']"),
    ("regNos: form.elements.regNos.value.trim(),", "regNos: form.elements.regNos.value.trim(), phones: form.elements.phones.value.trim(),")])
edit('apps-script-receiver.gs', [
    ("'json', 'regNos'];", "'json', 'regNos', 'phones'];"),
    ("'People', 'Reg numbers'];", "'People', 'Reg numbers', 'Phones'];"),
    ("Number(d.size) || '', d.regNos || ''];", "Number(d.size) || '', d.regNos || '', d.phones || ''];"),
    ("JSON.stringify(d), d.regNos || ''\n", "JSON.stringify(d), d.regNos || '', d.phones || ''\n")])
with open('../site/css/v5.css', 'a', encoding='utf-8') as fh:
    fh.write('\n.memblock .fgrid { grid-template-columns: repeat(3, minmax(0, 1fr)); }\n@media (max-width: 700px) { .memblock .fgrid { grid-template-columns: minmax(0, 1fr); } }\n')
print('ok')
