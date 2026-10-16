"""Round 2: 'Before you submit' checklist, optional branch field; evaluator: branch checkout, no demo video expected."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def edit(path, pairs):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (path, a[:60])
        s = s.replace(a, b, 1)
    open(path, 'w', encoding='utf-8').write(s)

CHECK = '''<div class="r2check">
<h3>Before you submit — your repo is judged automatically</h3>
<p>There is no live demo. Judges (and an AI evaluator) read only your GitHub repo, so make sure:</p>
<ul>
<li><b>Public repo.</b> Press <b>Check repo</b> below; it must find your repo. Private repos cannot be judged.</li>
<li><b>Code is on the main branch</b> (or type your branch name below).</li>
<li><b>README</b> explains the problem, the target user, and <b>how to run</b> the project.</li>
<li><b>README has screenshots</b> of your product (and sample outputs). No video needed.</li>
<li><b>Training code and data loading are in the repo</b>, using this track's dataset files — not only on your laptop.</li>
<li>Your <b>last commit before 4:00 PM</b> is what gets judged. Later pushes are ignored.</li>
</ul>
</div>
'''
edit('pages_r2.py', [
    ('<div class="r2info">{info}</div>\n', '<div class="r2info">{info}</div>\n' + CHECK),
    ('<div id="evidence" class="fld--wide"></div>',
     '{f("Branch (only if your code is not on main)", "branch", ph="main")}\n<div id="evidence" class="fld--wide"></div>'),
])
edit('../site/js/round2.js', [("repo: (o.repo || '').trim(),", "repo: (o.repo || '').trim(), branch: (o.branch || '').trim(),")])
with open('../site/css/v5.css', 'a', encoding='utf-8') as f:
    f.write('\n.r2check { background: var(--carbon); color: var(--paper); border-radius: var(--r-card-lg); padding: 22px 26px; margin-bottom: 22px; }\n'
            '.r2check h3 { font: 400 clamp(20px, 2.4vw, 28px)/1 var(--font-display); text-transform: uppercase; color: var(--cyan); margin-bottom: 10px; }\n'
            '.r2check p { color: var(--mist); margin-bottom: 10px; }\n.r2check ul { display: grid; gap: 6px; padding-left: 20px; list-style: disc; }\n.r2check li { line-height: 1.4; }\n')

# evaluator
edit('../evaluator/config.py', [('"Demo material exists in the repo or README (screenshots, demo video link, sample outputs)."',
                                 '"Screenshots of the product or sample outputs are in the README or repo (no demo video is expected)."')])
edit('../evaluator/judges.py', [('"demo" = README/screenshots/video/sample outputs.',
                                 '"demo" = there is NO live demo or video; judge the README, screenshots and sample outputs only.')])
edit('../evaluator/prepare.py', [(
    '        late = git(repo, "rev-list", "-1", "--before=2026-10-16T16:00:00+05:30", "HEAD").strip()\n',
    '        br = (d.get("branch") or "").strip()\n'
    '        if br and br.lower() not in ("main", "master"):   # team asked to judge another branch\n'
    '            subprocess.run(["git", "-C", repo, "checkout", "--quiet", f"origin/{br}"], capture_output=True)\n'
    '        late = git(repo, "rev-list", "-1", "--before=2026-10-16T16:00:00+05:30", "HEAD").strip()\n')])
print('ok')
