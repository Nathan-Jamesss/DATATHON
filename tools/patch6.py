import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def edit(path, pairs):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (path, a[:60])
        s = s.replace(a, b)
    open(path, 'w', encoding='utf-8').write(s)

edit('../site/js/repocheck.js', [
 ("  function getJSON(u) { return fetch(u, { headers: { Accept: 'application/vnd.github+json' } })",
  "  function token() { try { return localStorage.getItem('dt_gh_token') || ''; } catch (e) { return ''; } }\n  function getJSON(u) { var h = { Accept: 'application/vnd.github+json' }; if (token()) h.Authorization = 'Bearer ' + token(); return fetch(u, { headers: h })"),
 ("    return getJSON('https://api.github.com/repos/' + p.owner + '/' + p.repo).then(function (meta) {\n      out.branch = meta.default_branch; out.pushedAt = meta.pushed_at; out.isPrivate = !!meta.private;\n      return getJSON('https://api.github.com/repos/' + p.owner + '/' + p.repo + '/git/trees/' + meta.default_branch + '?recursive=1');\n    }).then(function (tree) {",
  "    out.branch = 'HEAD';\n    // one API call only (60/hour per IP without a token); file contents come from raw.githubusercontent.com\n    return getJSON('https://api.github.com/repos/' + p.owner + '/' + p.repo + '/git/trees/HEAD?recursive=1').then(function (tree) {"),
 ("<dt>Last push</dt><dd>' + esc((r.pushedAt || '').replace('T', ' ').slice(0, 16)) + ' UTC</dd></dl>'", "</dl>'"),
 ("'GitHub rate limit hit. Try again in a few minutes.'", "'GitHub rate limit hit (shared Wi-Fi uses one quota). Judges can add a GitHub token on the judges page; teams can skip this check.'"),
])
edit('../site/js/round2.js', [
 ("    // auto-verify the repo before submitting so judges get evidence\n    if (!evidence || !evidence.ok || evidence.repo + evidence.owner !== (RepoCheck.parse(form.elements.repo.value) || {}).repo + (RepoCheck.parse(form.elements.repo.value) || {}).owner) {\n      RepoCheck.check(form.elements.repo.value).then(function (r) { evidence = r; RepoCheck.render(evEl, r); go(); });\n    } else go();",
  "    go();"),
 ("<small>Must be public. We scan it for model files, training code and API usage to help judges.</small>", "<small>Must be public.</small>") if False else ("    go();", "    go();"),
])
edit('../site/js/judge.js', [
 ("  render();\n})();", "  var tk = $('gh-token');\n  try { tk.value = localStorage.getItem('dt_gh_token') || ''; } catch (e) {}\n  tk.addEventListener('input', function () { try { localStorage.setItem('dt_gh_token', tk.value.trim()); } catch (e) {} });\n  render();\n})();"),
])
edit('pages_r2.py', [
 ("<details class=\"more\" style=\"margin-top:12px\"><summary>Paste JSON</summary>",
  "<input id=\"gh-token\" type=\"password\" placeholder=\"GitHub token (optional: lifts the 60 checks/hour limit)\" autocomplete=\"off\">\n<details class=\"more\" style=\"margin-top:12px\"><summary>Paste JSON</summary>"),
 ("We scan it for model files, training code and API usage to help judges.", "“Check repo” is optional: it scans for model files, training code and API usage to help judges."),
])
print('ok')
