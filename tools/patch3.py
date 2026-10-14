import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
s = open('mkppt.py', encoding='utf-8').read()
def r(a, b):
    global s
    assert a in s, a[:50]
    s = s.replace(a, b)
r('"MVP Scope for the Final Round"', '"MVP Scope for Round 2 (complete prototype)"')
r('("Base Prototype (built in Round 1)"', '("Base Prototype (Round 1)"') if '("Base Prototype (built in Round 1)"' in s else None
r('("Task", "prediction / classification / ranking / forecasting / anomaly"),',
  '("Built from scratch, or via API key?", "state it clearly — from-scratch models score highest"),\n    ("Task", "prediction / classification / ranking / forecasting / anomaly"),')
r('"Keep to a maximum of eight (8) slides, including the title slide.",',
  '"Keep to a maximum of eight (8) slides, including the title slide. Round 1 = this PPT + a base prototype.",')
r('"Disclose all additional data, third-party APIs, pretrained models and borrowed code. Don’t claim accuracy without evidence.",',
  '"Disclose every API key, pretrained model, extra dataset and borrowed code. An ML model trained from scratch earns the most marks; API-key-only earns the least.",')
open('mkppt.py', 'w', encoding='utf-8').write(s)
