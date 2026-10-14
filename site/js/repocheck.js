// Heuristic GitHub repo inspector (public repos, browser-side). It gives judges evidence, not a verdict.
(function () {
  var MODEL_EXT = /\.(pkl|pickle|joblib|h5|keras|pt|pth|onnx|pb|safetensors|ckpt|tflite)$/i;
  var CODE_EXT = /\.(py|ipynb|js|ts|jsx|tsx)$/i;
  var DEP_FILES = /(^|\/)(requirements[^/]*\.txt|pyproject\.toml|environment\.ya?ml|package\.json|Pipfile)$/i;
  var ML_LIBS = /(scikit-learn|sklearn|xgboost|lightgbm|catboost|torch|tensorflow|keras|statsmodels|prophet|pytorch)/i;
  var API_LIBS = /(openai|anthropic|google-generativeai|google-genai|groq|cohere|mistralai|langchain|together|replicate|huggingface[_-]hub|ollama)/i;
  var TRAIN_CODE = /(\.fit\(|\.train\(|trainer\.train|loss\.backward|optimizer\.step|RandomForest|GradientBoosting|XGB(Classifier|Regressor)|LGBM|nn\.Module|keras\.Sequential|train_test_split|cross_val)/;
  var API_CODE = /(openai|anthropic|genai|GenerativeModel|chat\.completions|ChatOpenAI|Groq\(|cohere|api[_-]?key|messages\.create)/i;
  var KEY_LEAK = /(sk-[A-Za-z0-9_\-]{20,}|AIza[0-9A-Za-z_\-]{30,}|gsk_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{25,})/;

  function parse(url) {
    var m = /github\.com\/([^\/\s]+)\/([^\/\s#?]+)/i.exec(url || '');
    if (!m) return null;
    return { owner: m[1], repo: m[2].replace(/\.git$/i, '') };
  }
  function token() { try { return localStorage.getItem('dt_gh_token') || ''; } catch (e) { return ''; } }
  function getJSON(u) { var h = { Accept: 'application/vnd.github+json' }; if (token()) h.Authorization = 'Bearer ' + token(); return fetch(u, { headers: h }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }); }
  function getText(u) { return fetch(u).then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); }); }

  function check(url) {
    var p = parse(url);
    if (!p) return Promise.resolve({ ok: false, error: 'Not a GitHub repository URL.' });
    var out = { ok: true, owner: p.owner, repo: p.repo, modelFiles: [], trainFiles: [], notebooks: 0, readme: false, mlLibs: [], apiLibs: [], trainHits: [], apiHits: [], keyLeak: [], notes: [], checkedAt: new Date().toISOString() };
    out.branch = 'HEAD';
    // one API call only (60/hour per IP without a token); file contents come from raw.githubusercontent.com
    return getJSON('https://api.github.com/repos/' + p.owner + '/' + p.repo + '/git/trees/HEAD?recursive=1').then(function (tree) {
      var paths = (tree.tree || []).filter(function (t) { return t.type === 'blob'; });
      out.fileCount = paths.length; out.truncated = !!tree.truncated;
      var code = [], deps = [];
      paths.forEach(function (t) {
        var path = t.path;
        if (/(^|\/)readme(\.md|\.txt)?$/i.test(path)) out.readme = true;
        if (MODEL_EXT.test(path)) out.modelFiles.push(path);
        if (/\.ipynb$/i.test(path)) out.notebooks++;
        if (CODE_EXT.test(path) && /(train|fit|model)/i.test(path)) out.trainFiles.push(path);
        if (DEP_FILES.test(path)) deps.push(path);
        if (CODE_EXT.test(path) && t.size < 400000) code.push(t);
      });
      code.sort(function (a, b) {
        var sa = /(train|model|app|main|predict|api)/i.test(a.path) ? 0 : 1, sb = /(train|model|app|main|predict|api)/i.test(b.path) ? 0 : 1;
        return sa - sb || a.size - b.size;
      });
      var base = 'https://raw.githubusercontent.com/' + out.owner + '/' + out.repo + '/' + out.branch + '/';
      var jobs = deps.slice(0, 4).map(function (d) { return getText(base + d).then(function (txt) { return { dep: true, txt: txt }; }).catch(function () { return null; }); })
        .concat(code.slice(0, 14).map(function (c) { return getText(base + c.path).then(function (txt) { return { path: c.path, txt: txt }; }).catch(function () { return null; }); }));
      return Promise.all(jobs);
    }).then(function (files) {
      files.forEach(function (f) {
        if (!f) return;
        var t = f.txt;
        if (f.dep) {
          var ml = t.match(new RegExp(ML_LIBS.source, 'gi')) || [], ap = t.match(new RegExp(API_LIBS.source, 'gi')) || [];
          ml.forEach(function (x) { x = x.toLowerCase(); if (out.mlLibs.indexOf(x) < 0) out.mlLibs.push(x); });
          ap.forEach(function (x) { x = x.toLowerCase(); if (out.apiLibs.indexOf(x) < 0) out.apiLibs.push(x); });
        } else {
          if (TRAIN_CODE.test(t)) out.trainHits.push(f.path);
          if (API_CODE.test(t)) out.apiHits.push(f.path);
          if (KEY_LEAK.test(t)) out.keyLeak.push(f.path);
        }
      });
      var scratch = (out.trainHits.length > 0 || out.trainFiles.length > 0) && (out.modelFiles.length > 0 || out.mlLibs.length > 0);
      var api = out.apiLibs.length > 0 || out.apiHits.length > 0;
      out.suggested = scratch && !api ? 'scratch' : scratch && api ? 'mixed' : api ? 'api' : 'unclear';
      if (!out.readme) out.notes.push('No README found.');
      if (out.keyLeak.length) out.notes.push('Possible API key committed in: ' + out.keyLeak.join(', '));
      if (out.truncated) out.notes.push('Repo is large; only part of it was scanned.');
      out.notes.push('Heuristic only: only the most relevant ~14 code files were scanned. Judge by reading the code.');
      return out;
    }).catch(function (e) {
      return { ok: false, error: /^(403|429)$/.test(String(e.message)) ? 'GitHub rate limit hit (shared Wi-Fi uses one quota). Judges can add a GitHub token on the judges page; teams can skip this check.' : 'Repo not found or private (make it public).' };
    });
  }

  var LABEL = { scratch: 'Looks trained from scratch', mixed: 'Own model + API calls', api: 'API / pretrained only', unclear: 'Unclear — read the code' };
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function list(a) { return a.length ? a.slice(0, 6).map(esc).join(', ') + (a.length > 6 ? ' +' + (a.length - 6) + ' more' : '') : '<em>none</em>'; }

  function render(el, r) {
    if (!r.ok) { el.innerHTML = '<div class="ev ev--bad"><b>Could not check repo</b><span>' + esc(r.error) + '</span></div>'; return; }
    el.innerHTML = '<div class="ev"><div class="ev__top"><span class="chip chip--cyan">' + esc(LABEL[r.suggested]) + '</span><a href="https://github.com/' + esc(r.owner + '/' + r.repo) + '" target="_blank" rel="noopener">' + esc(r.owner + '/' + r.repo) + '</a></div>' +
      '<dl><dt>Model files</dt><dd>' + list(r.modelFiles) + '</dd><dt>Training code</dt><dd>' + list(r.trainHits.length ? r.trainHits : r.trainFiles) + '</dd><dt>ML libraries</dt><dd>' + list(r.mlLibs) + '</dd>' +
      '<dt>API libraries / calls</dt><dd>' + list(r.apiLibs.concat(r.apiHits)) + '</dd><dt>Notebooks</dt><dd>' + r.notebooks + '</dd><dt>README</dt><dd>' + (r.readme ? 'yes' : '<b>missing</b>') + '</dd></dl>' +
      (r.notes.length ? '<ul class="ev__notes">' + r.notes.map(function (n) { return '<li>' + esc(n) + '</li>'; }).join('') + '</ul>' : '') + '</div>';
  }

  window.RepoCheck = { check: check, render: render, parse: parse, LABEL: LABEL, esc: esc };
})();
