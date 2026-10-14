import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
L = open('pages_r2.py', encoding='utf-8').read().split('\n')
def find(sub):
    return [i for i, l in enumerate(L) if sub in l][0]

# project: pitch optional
i = find('{f("Product name", "product"')
L[i] = '{f("Product name", "product", req=True)}{f("One-line pitch (optional)", "pitch")}'
# model block
i = find('{f("Algorithm / base model"')
L[i] = '{f("What does your model predict?", "task", req=True, ph="e.g. waiting time at a hospital")}{f("Algorithm used", "algo", req=True, ph="e.g. Random Forest, LSTM")}'
j = find('{f("Path to training code in repo"')
L[i + 1:j + 1] = ['{f("Training code file in your repo", "trainPath", req=True, ph="e.g. notebooks/train.ipynb")}{f("Result, if you measured one (optional)", "metric", ph="e.g. error 6 min")}']
# apis & data block
i = find('{f("Other API / pretrained model (name)"')
j = find('{f("How to run your project"')
L[i:j + 1] = ['{f("Any extra data you used? (optional)", "extraData", span=True)}']
s = '\n'.join(L)
s = re.sub(r'decls = \[.*?\]\n', 'decls = ["Our GitHub repo is public.",\n             "We listed every API / pretrained model we used and committed no API keys."]\n', s, count=1, flags=re.S)
open('pages_r2.py', 'w', encoding='utf-8').write(s)

# rules wording
b = open('build.py', encoding='utf-8').read()
a = '("Disclose additional data.", "Include source, licence/permission, collection method, and what it contributes."),'
assert a in b
b = b.replace(a, '("Tell us about extra data.", "If you used data beyond the provided pack, say where it came from."),')
open('build.py', 'w', encoding='utf-8').write(b)

# apps script: lock to avoid concurrent-write clashes
g = open('apps-script-receiver.gs', encoding='utf-8').read()
g = g.replace("  var d = JSON.parse(e.postData.contents);\n  getSheet_().appendRow(", "  var d = JSON.parse(e.postData.contents);\n  var lock = LockService.getScriptLock();\n  lock.waitLock(20000);\n  getSheet_().appendRow(")
g = g.replace("JSON.stringify(d)]);\n  return ContentService.createTextOutput('ok');", "JSON.stringify(d)]);\n  lock.releaseLock();\n  return ContentService.createTextOutput('ok');")
open('apps-script-receiver.gs', 'w', encoding='utf-8').write(g)
print('ok')
