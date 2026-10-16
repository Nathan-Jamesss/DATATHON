"""Copy site/ to docs/ so GitHub Pages can serve a backup mirror (github.io) when vercel.app is unreachable on some networks.
The mirror has no server-side locks, so Round 2 gets a client-side lock (cosmetic) until 1:00 PM IST on 16 Oct 2026."""
import os, shutil
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
src, dst = os.path.join(root, 'site'), os.path.join(root, 'docs')
if os.path.exists(dst): shutil.rmtree(dst)
shutil.copytree(src, dst)
open(os.path.join(dst, '.nojekyll'), 'w').close()
p = os.path.join(dst, 'round2.html')
s = open(p, encoding='utf-8').read()
lock = ("<script>if(Date.now()<Date.parse('2026-10-16T13:00:00+05:30')){document.body.innerHTML="
        "'<main style=\"min-height:100vh;display:grid;place-items:center;background:#000;color:#fff;text-align:center;font-family:Inter,sans-serif;padding:24px\">"
        "<div><p style=\"letter-spacing:.3em;color:#19e3f5;font-weight:800;font-size:12px\">LOCKED UNTIL RELEASE</p>"
        "<h1 style=\"font-size:clamp(34px,8vw,84px);margin:16px 0\">ROUND 2 OPENS AT 1:00 PM</h1>"
        "<p style=\"color:#a9b4b6\">Friday 16 October 2026, 1:00 PM IST.</p>"
        "<p><a href=\"index.html\" style=\"color:#fff\">Back to home</a></p></div></main>';}</script>")
s = s.replace('</body>', lock + '</body>')
open(p, 'w', encoding='utf-8').write(s)
print('mirror ready:', dst)
