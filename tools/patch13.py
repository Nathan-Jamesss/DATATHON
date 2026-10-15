import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = open('build2.py', encoding='utf-8').read()
q = '<div class="question"><small>Useful product question</small><p>“{t[\'q\']}”</p></div>\n'
assert q in s
s = s.replace(q, '', 1)
a = "<details class=\"more\"><summary>Possible ML / data-science work</summary><p>{t['ml']}</p></details>\n"
assert a in s
s = s.replace(a, a + q, 1)
open('build2.py', 'w', encoding='utf-8').write(s)
print('ok')
