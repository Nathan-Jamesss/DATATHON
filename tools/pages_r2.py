"""Round 2 submission page + judges console. Loaded by build2.py."""

def make(wrapp, page_head, ic, TRACKS, REG):
    def f(label, name, kind="text", req=False, ph="", hint="", span=False, rows=3):
        r = " required" if req else ""
        star = " *" if req else ""
        cls = "fld fld--wide" if span else "fld"
        h = f"<small>{hint}</small>" if hint else ""
        if kind == "textarea":
            inp = f'<textarea name="{name}" rows="{rows}" placeholder="{ph}"{r}></textarea>'
        else:
            inp = f'<input type="{kind}" name="{name}" placeholder="{ph}"{r}>'
        return f'<label class="{cls}"><span>{label}{star}</span>{inp}{h}</label>'

    track_opts = "".join(f'<option value="0{t["n"]} {t["dom"]}">Track {t["n"]} · {t["dom"]}</option>' for t in TRACKS)
    opts = [
        ("scratch", "Trained from scratch", "We built and trained our own model on the provided data. Scores highest."),
        ("finetuned", "Fine-tuned a pretrained model", "We meaningfully fine-tuned an existing model. Partial marks."),
        ("api", "API key / hosted model only", "We call an API (LLM etc.) with no model of our own. Lowest marks."),
        ("none", "No ML model", "Rules / analytics / optimisation only."),
    ]
    radios = "".join(f'<label class="opt"><input type="radio" name="modelType" value="{v}" required><span><b>{t}</b><small>{d}</small></span></label>' for v, t, d in opts)
    apis = ["OpenAI", "Anthropic Claude", "Google Gemini", "Groq", "Hugging Face Inference", "Cohere", "Other", "None"]
    api_boxes = "".join(f'<label class="chk"><input type="checkbox" name="api" value="{a}"><span>{a}</span></label>' for a in apis)
    decls = ["Our GitHub repo is public.",
             "We listed every API / pretrained model we used and committed no API keys."]
    decl_boxes = "".join(f'<label class="chk chk--block"><input type="checkbox" name="decl" value="{d}" required><span>{d}</span></label>' for d in decls)

    def round2_page():
        body = page_head("Round 2 · complete prototype · due 4:30 PM", "Submit your <span class=\"t\">repo</span>",
                         "Round 2 is the complete prototype. Share your public GitHub repository and tell us exactly how your model was built. Judges check the code.")
        steps = [("1", "Public GitHub repo", "Code, README and run steps."), ("2", "Your model", "Trained from scratch scores highest. API-key-only scores lowest."),
                 ("3", "Declare APIs & data", "Every API, pretrained model and extra dataset."), ("4", "Submit by 4:30 PM", "Friday 16 October 2026.")]
        info = "".join(f'<div class="r2step"><span>{n}</span><div><b>{t}</b><small>{d}</small></div></div>' for n, t, d in steps)
        body += f"""<section class="band band-wash band--tight"><div class="wrap">
<div class="r2info">{info}</div>
<div class="r2check">
<h3>Before you submit — your repo is judged automatically</h3>
<p>There is no live demo. Judges (and an AI evaluator) read only your GitHub repo, so make sure:</p>
<ul>
<li><b>Public repo.</b> Press <b>Check repo</b> below; it must find your repo. Private repos cannot be judged.</li>
<li><b>Code is on the main branch</b> (or type your branch name below).</li>
<li><b>README</b> explains the problem, the target user, and <b>how to run</b> the project.</li>
<li><b>README has screenshots</b> of your product (and sample outputs). No video needed.</li>
<li><b>Training code and data loading are in the repo</b>, using this track's dataset files — not only on your laptop.</li>
<li>Your <b>last commit before 4:30 PM</b> is what gets judged. Later pushes are ignored.</li>
</ul>
</div>
<form id="r2form" class="r2form" novalidate>
<fieldset><legend><span>01</span> Team</legend><div class="fgrid">
{f("Team name", "team", req=True)}
<label class="fld"><span>Number of people *</span><select name="size" required><option value="">Choose</option><option value="1">1 (solo)</option><option value="2">2 (duo)</option></select></label>
<div class="fld fld--wide memblock"><div class="fgrid"><label class="fld"><span>Member 1 name *</span><input type="text" name="m1name" required></label><label class="fld"><span>Member 1 registration no. *</span><input type="text" name="m1reg" required placeholder="e.g. 23BCE1234"></label><label class="fld"><span>Member 1 phone (optional)</span><input type="tel" name="m1phone" inputmode="tel" placeholder="10-digit mobile, e.g. 7012345678"></label><label class="fld" data-m2 hidden><span>Member 2 name *</span><input type="text" name="m2name" disabled></label><label class="fld" data-m2 hidden><span>Member 2 registration no. *</span><input type="text" name="m2reg" disabled placeholder="e.g. 23BCE5678"></label><label class="fld" data-m2 hidden><span>Member 2 phone (optional)</span><input type="tel" name="m2phone" disabled inputmode="tel" placeholder="10-digit mobile, e.g. 7012345678"></label></div><input type="hidden" name="members"><input type="hidden" name="regNos"><input type="hidden" name="phones"></div>
{f("Contact email", "email", "email", True)}
<label class="fld"><span>Track *</span><select name="track" required><option value="">Choose your track</option>{track_opts}</select></label>
</div></fieldset>
<fieldset><legend><span>02</span> Project &amp; GitHub</legend><div class="fgrid">
{f("Product name", "product", req=True)}{f("One-line pitch (optional)", "pitch")}
<label class="fld fld--wide"><span>GitHub repository URL *</span><div class="inline"><input type="url" name="repo" placeholder="https://github.com/team/project" required><button type="button" class="btn btn--fill" id="verify">Check repo</button></div><small>Must be public. “Check repo” is optional: it scans for model files, training code and API usage to help judges.</small></label>
{f("Branch (only if your code is not on main)", "branch", ph="main")}
<div id="evidence" class="fld--wide"></div>
</div></fieldset>
<fieldset><legend><span>03</span> Your ML model</legend>
<div class="opts" role="radiogroup" aria-label="Model type">{radios}</div>
<div class="fgrid" style="margin-top:14px">
<div class="fgrid fld--wide" data-when="scratch finetuned" hidden>
{f("What does your model predict?", "task", req=True, ph="e.g. waiting time at a hospital")}{f("Algorithm used", "algo", req=True, ph="e.g. Random Forest, LSTM")}
{f("Training code file in your repo", "trainPath", req=True, ph="e.g. notebooks/train.ipynb")}{f("Result, if you measured one (optional)", "metric", ph="e.g. error 6 min")}
</div>
<div class="fld--wide" data-when="api" hidden>{f("What does the API do in your product?", "apiUse", "textarea", True, span=True, rows=2)}</div>
</div></fieldset>
<fieldset><legend><span>04</span> APIs, keys &amp; data</legend>
<div class="chks">{api_boxes}</div>
<div class="fgrid" style="margin-top:14px">
{f("Any extra data you used? (optional)", "extraData", span=True)}
{f("Which dataset files does your code use? (optional)", "datasetsUsed", span=True, ph="e.g. encounters.csv, patients.csv")}
{f("How to run your project, one line (optional)", "howToRun", span=True, ph="e.g. pip install -r requirements.txt && streamlit run app.py")}
</div>
<div class="notice">{ic('info')}<span>Never commit API keys. Keep them in a <b>.env</b> file listed in <b>.gitignore</b>. Keys found in a public repo are flagged to judges.</span></div>
</fieldset>
<fieldset><legend><span>05</span> Declaration</legend>{decl_boxes}</fieldset>
<div class="r2actions"><button class="btn btn--fill btn--lg" type="submit">Submit Round 2 {ic('arrow')}</button><span class="muted">Your answers autosave in this browser until you submit.</span></div>
<div id="r2out" class="r2out" hidden></div>
</form>
</div></section>"""
        return wrapp("round2", "Round 2 Submission · DATATHON 2026", "Submit your GitHub repository and model details for DATATHON Round 2.", body,
                     '\n<script src="js/config.js"></script>\n<script src="js/repocheck.js"></script>\n<script src="js/round2.js"></script>\n<script src="js/members.js"></script>')

    def judge_page():
        body = page_head("Organisers only", "Judges <span class=\"t\">console</span>",
                         "Review Round 2 submissions, check whether each team really trained a model, and score on the 100-mark rubric.")
        body += f"""<section class="band band-wash band--tight"><div class="wrap">
<div class="notice" style="margin:0 0 16px;border-color:#000;color:#000">{ic('info')}<span>This page has no password. Scores live only in <b>this browser</b> — export the CSV often. Don't share the link with teams.</span></div>
<div class="jtools">
<div class="card"><span class="eyebrow">Load submissions</span>
<div class="jrow"><label class="btn btn--fill btn--sm" style="cursor:pointer">Import .json files<input id="file" type="file" accept=".json,application/json" multiple hidden></label><button class="btn btn--sm" id="load" type="button">Load from endpoint</button></div>
<input id="gh-token" type="password" placeholder="GitHub token (optional: lifts the 60 checks/hour limit)" autocomplete="off">
<details class="more" style="margin-top:12px"><summary>Paste JSON</summary><div style="padding:0 16px 14px"><textarea id="paste" rows="4" style="width:100%"></textarea><button class="btn btn--sm" id="paste-go" type="button" style="margin-top:8px">Add</button></div></details></div>
<div class="card"><span class="eyebrow">Add a repo manually</span>
<div class="jrow"><input id="add-team" placeholder="Team name"><input id="add-repo" placeholder="https://github.com/…">
<select id="add-track"><option value="">Track</option>{"".join(f'<option>0{t["n"]} {t["dom"]}</option>' for t in TRACKS)}</select>
<select id="add-model"><option value="">Claimed model</option><option value="scratch">From scratch</option><option value="finetuned">Fine-tuned</option><option value="api">API only</option><option value="none">No ML</option></select>
<button class="btn btn--fill btn--sm" id="add-go" type="button">Add</button></div></div>
</div>
<div class="jhead"><h2 class="sub-h" style="margin:24px 0 8px">Leaderboard · <span id="count">0</span> teams</h2><div class="jrow"><button class="btn btn--fill btn--sm" id="export" type="button">Export CSV</button><button class="btn btn--sm" id="clear" type="button">Clear all</button></div></div>
<div id="board" class="jboard"></div>
<h2 class="sub-h" style="margin:32px 0 12px">Submissions</h2>
<div id="cards" class="jcards"></div>
</div></section>"""
        return wrapp("judge", "Judges Console · DATATHON 2026", "Organiser scoring console.", body,
                     '\n<script src="js/config.js"></script>\n<script src="js/repocheck.js"></script>\n<script src="js/judge.js"></script>')

    return round2_page, judge_page
