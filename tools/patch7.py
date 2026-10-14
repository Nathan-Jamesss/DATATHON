import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def load(p): return open(p, encoding='utf-8').read()
def save(p, s): open(p, 'w', encoding='utf-8').write(s)
def must(s, a, b):
    assert a in s, a[:70]
    return s.replace(a, b)

# ---------- build.py (data) ----------
s = load('build.py')
s = must(s, ' ("IoT / sensor integration", "Useful sensor pipeline and impact on product decisions", 10),\n', '')
s = must(s, '("ML model from scratch", "Trained from scratch scores highest. API-key / pretrained-only scores lowest", 20)', '("ML model from scratch", "Trained from scratch scores highest. API-key / pretrained-only scores lowest", 25)')
s = must(s, '("Working product & workflow", "Functional end-to-end prototype, usability and reliability", 15)', '("Working product & workflow", "Functional end-to-end prototype, usability and reliability", 20)')
s = must(s, '("ML Approach & IoT", "From-scratch model (declare any API used), baseline, split, metric, IoT path", False)', '("ML Approach", "From-scratch model (declare any API used), baseline, split, metric", False)')
s = s.replace(", a meaningful sensor / IoT data path, and", " and")
s = re.sub(r"and not just for having IoT hardware or a complicated algorithm", "and not just for a complicated algorithm", s)
s = re.sub(r', "Optional IoT integration[^"]*"', '', s)
s = s.replace(' (IoT).', '.')
s = s.replace('The IoT table supports sensor-stream processing or anomaly detection. It is simulated and is <b>not</b> suitable for clinical diagnosis.', 'The device-vitals table is simulated and is <b>not</b> suitable for clinical diagnosis.')
save('build.py', s)

# ---------- build2.py ----------
s = load('build2.py')
s = re.sub(r'<details class="rule"><summary data-n="IoT">.*?</details>', '', s, flags=re.S)
s = must(s, 'Up to the full 20 marks.', 'Up to the full 25 marks.')
s = must(s, '{strip()}', '{tcards()}')
save('build2.py', s)

# ---------- pages_r2.py ----------
s = load('pages_r2.py')
s = '\n'.join(l for l in s.split('\n') if 'name="iot"' not in l and '"iotDetail"' not in l)
save('pages_r2.py', s)

# ---------- js ----------
s = load('../site/js/round2.js')
s = must(s, " iot: o.iot || '', iotDetail: o.iotDetail || '',", '')
save('../site/js/round2.js', s)
s = load('../site/js/judge.js')
s = must(s, "['model', 'ML model from scratch', 20], ['iot', 'IoT / sensor integration', 10], ['product', 'Working product & workflow', 15],", "['model', 'ML model from scratch', 25], ['product', 'Working product & workflow', 20],")
s = re.sub(r", \['IoT', \[s\.iot, s\.iotDetail\]\.filter\(Boolean\)\.join\(': '\)\]", '', s)
save('../site/js/judge.js', s)
s = load('../site/js/config.js')
s = must(s, 'TIER_CAPS: { scratch: 20, finetuned: 12, api: 5, none: 0 }', 'TIER_CAPS: { scratch: 25, finetuned: 15, api: 5, none: 0 }')
save('../site/js/config.js', s)

# ---------- ppt ----------
s = load('mkppt.py')
s = must(s, 'slide(5, "ML MODEL & IoT", [', 'slide(5, "ML MODEL", [')
s = must(s, '''    ("ML Approach", ["Model built from scratch, or using an API key?", "Features, target, baseline, split and metric"], False),
    ("IoT / Sensor Data", ["Sensor pipeline and how it affects decisions"], False)])''',
          '''    ("ML Approach", ["Model built from scratch, or using an API key?", "Features, target, baseline, split and metric", "How the model output is used in the product"], False)])''')
save('mkppt.py', s)

# ---------- css ----------
with open('../site/css/v5.css', 'a', encoding='utf-8') as f:
    f.write('\n.ptab b { font-size: 12.5px; text-wrap: balance; }\n.ptrack__title { font-size: clamp(28px, 3.6vw, 46px); }\n.ptab__no { font-size: 30px; }\n')
print('ok')
