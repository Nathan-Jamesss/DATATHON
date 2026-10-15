import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
p = '../middleware.js'
s = open(p, encoding='utf-8').read()

def r(a, b):
    global s
    assert a in s, a[:60]
    s = s.replace(a, b)

# smaller heading, "10:00 AM" on its own single line, logos on top
r("h1{font-family:'Archivo Black',Impact,sans-serif;font-weight:400;text-transform:uppercase;line-height:.85;font-size:clamp(44px,11vw,150px);margin:22px 0}\nh1 span{color:#19e3f5}",
  "h1{font-family:'Archivo Black',Impact,sans-serif;font-weight:400;text-transform:uppercase;line-height:.9;font-size:clamp(28px,6.2vw,84px);margin:18px 0 8px}\n"
  ".at{font-family:'Archivo Black',Impact,sans-serif;text-transform:uppercase;color:#19e3f5;font-size:clamp(22px,4.2vw,54px);line-height:1;white-space:nowrap;margin:0 0 22px}\n"
  ".logos{display:flex;gap:clamp(20px,5vw,56px);justify-content:center;align-items:center;margin-bottom:34px}.logos img{height:clamp(46px,7vw,76px);width:auto}")
r("p{color:#a9b4b6;max-width:46ch;margin:0 auto 28px;font-size:18px}", "p{color:#a9b4b6;max-width:46ch;margin:0 auto 24px;font-size:16px}")
r(".c b{display:block;font:400 clamp(34px,7vw,72px)/.9 'Archivo Black',Impact,sans-serif;color:#19e3f5}", ".c b{display:block;font:400 clamp(28px,5.5vw,56px)/.9 'Archivo Black',Impact,sans-serif;color:#19e3f5}")
r(".c{border:1px solid rgba(255,255,255,.35);border-radius:24px;padding:18px 10px;min-width:92px}", ".c{border:1px solid rgba(255,255,255,.35);border-radius:20px;padding:14px 8px;min-width:80px}")
r('<main>\n<div class="eyebrow">Locked until release</div>\n<h1>Problem<br>statements<br>drop at <span>10:00 AM</span></h1>',
  '<main>\n<div class="logos"><img src="/assets/logo-dsc.png" alt="Data Science Club VIT-AP"><img src="/assets/logo-iiec.png" alt="IIEC"></div>\n<div class="eyebrow">Locked until release</div>\n<h1>Problem statements</h1>\n<div class="at">Drops at 10:00 AM</div>')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
