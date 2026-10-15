// Release gates (run on Vercel's servers, so they can't be bypassed from the browser).
// Until each release time the gated pages show a countdown (datasets return 403).
// To change a time, edit the date below and push. Nothing else to touch.
const PROBLEMS_AT = Date.parse('2026-10-16T10:00:00+05:30'); // Fri 16 Oct 2026, 10:00 AM IST
const ROUND2_AT = Date.parse('2026-10-16T13:00:00+05:30');   // Fri 16 Oct 2026,  1:00 PM IST

export const config = {
  matcher: ['/problem-statements', '/problem-statements.html', '/datasets/:path*', '/round2', '/round2.html'],
};

const PASS = () => new Response(null, { headers: { 'x-middleware-next': '1' } });

function lockedPage({ title, at, text, release }) {
  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title} · DATATHON 2026</title><meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@500;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;background:#000;color:#fff;font-family:Inter,system-ui,sans-serif;padding:24px;text-align:center}
.eyebrow{font-weight:800;letter-spacing:.32em;text-transform:uppercase;font-size:12px;color:#19e3f5}
h1{font-family:'Archivo Black',Impact,sans-serif;font-weight:400;text-transform:uppercase;line-height:.9;font-size:clamp(28px,6.2vw,84px);margin:18px 0 8px}
.at{font-family:'Archivo Black',Impact,sans-serif;text-transform:uppercase;color:#19e3f5;font-size:clamp(22px,4.2vw,54px);line-height:1;white-space:nowrap;margin:0 0 22px}
.logos{display:flex;gap:clamp(20px,5vw,56px);justify-content:center;align-items:center;margin-bottom:34px}.logos img{height:clamp(46px,7vw,76px);width:auto}
p{color:#a9b4b6;max-width:46ch;margin:0 auto 24px;font-size:16px}
.cd{display:flex;gap:clamp(6px,2vw,12px);justify-content:center;flex-wrap:nowrap;margin:0 auto 32px;max-width:520px}
.c{flex:1;min-width:0;border:1px solid rgba(255,255,255,.35);border-radius:20px;padding:14px 4px}
.c b{display:block;font:400 clamp(28px,5.5vw,56px)/.9 'Archivo Black',Impact,sans-serif;color:#19e3f5}
.c small{display:block;margin-top:8px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#a9b4b6}
a{display:inline-block;color:#fff;border:1px solid #fff;border-radius:999px;padding:14px 26px;text-decoration:none;font-weight:800;font-size:13px;letter-spacing:.04em;text-transform:uppercase}
a:hover{background:#fff;color:#000}
</style></head><body><main>
<div class="logos"><img src="/assets/logo-dsc.png" alt="Data Science Club VIT-AP"><img src="/assets/logo-iiec.png" alt="IIEC"></div>
<div class="eyebrow">Locked until release</div>
<h1>${title}</h1>
<div class="at">${at}</div>
<p>${text}</p>
<div class="cd" id="cd"></div>
<a href="/">Back to home</a>
</main>
<script>
var T=${release};
function pad(n){return n<10?'0'+n:''+n}
function tick(){var s=Math.floor((T-Date.now())/1000);
if(s<=0){document.getElementById('cd').innerHTML='<div class="c"><b>Live</b><small>reloading</small></div>';setTimeout(function(){location.reload()},1500);return}
var c=[[Math.floor(s/86400),'days'],[Math.floor(s%86400/3600),'hrs'],[Math.floor(s%3600/60),'min'],[s%60,'sec']];
document.getElementById('cd').innerHTML=c.map(function(x){return '<div class="c"><b>'+pad(x[0])+'</b><small>'+x[1]+'</small></div>'}).join('')}
tick();setInterval(tick,1000);
</script></body></html>`;
  return new Response(html, {
    status: 200,
    headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' },
  });
}

// Organiser preview: open any locked page once with ?preview=<PREVIEW_KEY> and a cookie keeps it open for 12 hours
// in that browser only. The key lives in Vercel's environment variables (not in this repo).
const KEY = (typeof process !== 'undefined' && process.env && process.env.PREVIEW_KEY) || '';

export default function middleware(request) {
  const url = new URL(request.url);
  const { pathname } = url;
  const now = Date.now();

  if (KEY) {
    if (url.searchParams.get('preview') === KEY) {
      url.searchParams.delete('preview');
      return new Response(null, {
        status: 302,
        headers: { location: url.toString(), 'set-cookie': `dt_preview=${KEY}; Path=/; Max-Age=43200; HttpOnly; Secure; SameSite=Lax`, 'cache-control': 'no-store' },
      });
    }
    if ((request.headers.get('cookie') || '').split(/;\s*/).includes(`dt_preview=${KEY}`)) return PASS();
  }

  if (pathname.startsWith('/round2')) {
    if (now >= ROUND2_AT) return PASS();
    return lockedPage({
      title: 'Round 2', at: 'Opens at 1:00 PM', release: ROUND2_AT,
      text: 'Friday 16 October 2026, 1:00 PM IST. The Round 2 submission page opens for everyone at the same moment.',
    });
  }

  // problem statements page + datasets
  if (now >= PROBLEMS_AT) return PASS();
  if (pathname.startsWith('/datasets')) {
    return new Response('Locked until 16 Oct 2026, 10:00 AM IST.', {
      status: 403,
      headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store' },
    });
  }
  return lockedPage({
    title: 'Problem statements', at: 'Drops at 10:00 AM', release: PROBLEMS_AT,
    text: 'Friday 16 October 2026, 10:00 AM IST. Problem statements and datasets unlock for everyone at the same moment.',
  });
}
