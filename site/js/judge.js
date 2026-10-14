(function () {
  var CFG = window.DATATHON || {};
  var CAPS = CFG.TIER_CAPS || { scratch: 20, finetuned: 12, api: 5, none: 0 };
  var CRIT = [
    ['problem', 'Problem understanding & user need', 10], ['data', 'Provided dataset usage', 10], ['dsml', 'Data Science / ML quality', 15],
    ['model', 'ML model from scratch', 25], ['product', 'Working product & workflow', 20],
    ['usp', 'USP & innovation', 10], ['impact', 'Impact, feasibility & responsible use', 5], ['demo', 'Demo & presentation', 5]
  ];
  var TIERS = [['', 'Not verified yet'], ['scratch', 'Trained from scratch'], ['finetuned', 'Fine-tuned pretrained'], ['api', 'API key only'], ['none', 'No ML model']];
  var CLAIM = { scratch: 'Claims: from scratch', finetuned: 'Claims: fine-tuned', api: 'Claims: API only', none: 'Claims: no ML' };
  var esc = RepoCheck.esc, KEY = 'dt_judge_v1';
  var state = { subs: [], scores: {} };
  try { state = JSON.parse(localStorage.getItem(KEY)) || state; } catch (e) {}
  function save() { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} }
  var $ = function (id) { return document.getElementById(id); };

  function sc(id) { return state.scores[id] || (state.scores[id] = { v: {}, tier: '', note: '' }); }
  function cap(id, key, max) { return key === 'model' ? (CAPS[sc(id).tier] !== undefined && sc(id).tier ? CAPS[sc(id).tier] : max) : max; }
  function total(id) {
    var s = sc(id), t = 0;
    CRIT.forEach(function (c) { var v = Math.min(+s.v[c[0]] || 0, cap(id, c[0], c[2])); t += v; });
    return t;
  }

  function addSub(s) {
    if (!s || !s.repo) return;
    s.id = s.id || 'j-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 5);
    var i = state.subs.findIndex(function (x) { return x.id === s.id || (x.repo === s.repo && x.team === s.team); });
    if (i >= 0) state.subs[i] = s; else state.subs.push(s);
  }

  function board() {
    var rows = state.subs.map(function (s) { return { s: s, t: total(s.id) }; }).sort(function (a, b) { return b.t - a.t; });
    $('board').innerHTML = rows.length ? '<table><thead><tr><th>#</th><th>Team</th><th>Track</th><th>Model tier</th><th>Total</th></tr></thead><tbody>' +
      rows.map(function (r, i) { var t = sc(r.s.id).tier; return '<tr><td>' + (i + 1) + '</td><td>' + esc(r.s.team || r.s.repo) + '</td><td>' + esc(r.s.track || '') + '</td><td>' + esc((TIERS.filter(function (x) { return x[0] === t; })[0] || ['', ''])[1] || '—') + '</td><td><b>' + r.t + '</b>/100</td></tr>'; }).join('') + '</tbody></table>' : '<p class="muted">No submissions yet. Import, add a repo, or load from the endpoint.</p>';
  }

  function card(s) {
    var m = s.modelDetails || {}, S = sc(s.id);
    var det = [['Product', s.product], ['Pitch', s.pitch], ['Members', s.members], ['Demo', s.demo], ['Model task', m.task], ['Algorithm', m.algo], ['Target', m.target], ['Features', m.features], ['Split', m.split], ['Baseline', m.baseline], ['Final metric', m.metric], ['Training code', m.trainPath], ['Model file', m.modelPath],
      ['APIs used', (s.apis || []).concat(s.apiOther ? [s.apiOther] : []).join(', ')], ['API purpose', s.apiUse], ['Extra data', s.extraData], ['How to run', s.howToRun]]
      .filter(function (r) { return r[1]; }).map(function (r) { return '<dt>' + esc(r[0]) + '</dt><dd>' + esc(r[1]) + '</dd>'; }).join('');
    return '<article class="jcard" data-id="' + esc(s.id) + '"><header><div><h3>' + esc(s.team || s.repo) + '</h3><div class="chips"><span class="chip">' + esc(s.track || 'track ?') + '</span><span class="chip chip--cyan">' + esc(CLAIM[s.modelType] || 'Claim: not stated') + '</span></div></div>' +
      '<div class="jtotal"><b data-total>0</b><small>/100</small></div></header>' +
      '<p><a class="btn btn--sm" href="' + esc(s.repo) + '" target="_blank" rel="noopener">Open repo</a> <button class="btn btn--sm" data-act="analyze">Analyze repo</button> <button class="btn btn--sm" data-act="remove">Remove</button></p>' +
      '<div class="ev-slot" data-ev></div>' + (det ? '<details class="more"><summary>Team answers</summary><dl class="kv">' + det + '</dl></details>' : '') +
      '<div class="jscore"><label class="jtier"><span>Verified model tier</span><select data-tier>' + TIERS.map(function (t) { return '<option value="' + t[0] + '"' + (S.tier === t[0] ? ' selected' : '') + '>' + t[1] + '</option>'; }).join('') + '</select></label>' +
      CRIT.map(function (c) { return '<label><span>' + esc(c[1]) + ' <em data-max="' + c[0] + '">/' + cap(s.id, c[0], c[2]) + '</em></span><input type="number" min="0" step="0.5" data-k="' + c[0] + '" value="' + (S.v[c[0]] === undefined ? '' : S.v[c[0]]) + '"></label>'; }).join('') +
      '</div><label class="jnote"><span>Judge notes</span><textarea rows="2" data-note>' + esc(S.note || '') + '</textarea></label></article>';
  }

  function refreshCard(el) {
    var id = el.dataset.id, s = state.subs.filter(function (x) { return x.id === id; })[0];
    if (!s) return;
    el.querySelector('[data-total]').textContent = total(id);
    CRIT.forEach(function (c) { var e = el.querySelector('[data-max=' + c[0] + ']'); if (e) e.textContent = '/' + cap(id, c[0], c[2]); });
  }

  function render() {
    $('cards').innerHTML = state.subs.map(card).join('');
    state.subs.forEach(function (s) {
      var el = document.querySelector('.jcard[data-id="' + s.id + '"]');
      if (s.evidence) RepoCheck.render(el.querySelector('[data-ev]'), s.evidence);
      refreshCard(el);
    });
    $('count').textContent = state.subs.length;
    board(); save();
  }

  $('cards').addEventListener('input', function (e) {
    var el = e.target.closest('.jcard'); if (!el) return; var id = el.dataset.id, S = sc(id);
    if (e.target.dataset.k) S.v[e.target.dataset.k] = e.target.value;
    if (e.target.hasAttribute('data-tier')) S.tier = e.target.value;
    if (e.target.hasAttribute('data-note')) S.note = e.target.value;
    refreshCard(el); board(); save();
  });
  $('cards').addEventListener('click', function (e) {
    var b = e.target.closest('[data-act]'); if (!b) return;
    var el = b.closest('.jcard'), id = el.dataset.id, s = state.subs.filter(function (x) { return x.id === id; })[0];
    if (b.dataset.act === 'remove') { if (confirm('Remove this submission and its scores?')) { state.subs = state.subs.filter(function (x) { return x.id !== id; }); delete state.scores[id]; render(); } return; }
    b.disabled = true; el.querySelector('[data-ev]').innerHTML = '<div class="ev"><span>Checking repository…</span></div>';
    RepoCheck.check(s.repo).then(function (r) { s.evidence = r.ok ? r : null; RepoCheck.render(el.querySelector('[data-ev]'), r); b.disabled = false; save(); });
  });

  function ingest(text) {
    var d; try { d = JSON.parse(text); } catch (e) { alert('Not valid JSON.'); return; }
    [].concat(d).forEach(addSub); render();
  }
  $('file').addEventListener('change', function (e) {
    [].forEach.call(e.target.files, function (f) { var r = new FileReader(); r.onload = function () { ingest(r.result); }; r.readAsText(f); });
    e.target.value = '';
  });
  $('paste-go').addEventListener('click', function () { ingest($('paste').value); $('paste').value = ''; });
  $('add-go').addEventListener('click', function () {
    var repo = $('add-repo').value.trim();
    if (!RepoCheck.parse(repo)) { alert('Enter a GitHub repo URL'); return; }
    addSub({ team: $('add-team').value.trim() || RepoCheck.parse(repo).repo, repo: repo, track: $('add-track').value, modelType: $('add-model').value });
    $('add-repo').value = ''; $('add-team').value = ''; render();
  });
  $('load').addEventListener('click', function () {
    if (!CFG.SUBMIT_ENDPOINT) { alert('Set SUBMIT_ENDPOINT in js/config.js first.'); return; }
    var k = prompt('Judge key (JUDGE_KEY from Apps Script):'); if (!k) return;
    fetch(CFG.SUBMIT_ENDPOINT + (CFG.SUBMIT_ENDPOINT.indexOf('?') < 0 ? '?' : '&') + 'key=' + encodeURIComponent(k)).then(function (r) { return r.json(); }).then(function (d) { [].concat(d).forEach(addSub); render(); }).catch(function () { alert('Could not load from the endpoint.'); });
  });
  $('export').addEventListener('click', function () {
    var head = ['rank', 'team', 'track', 'repo', 'claimed_model', 'verified_tier'].concat(CRIT.map(function (c) { return c[1]; }), ['total', 'notes']);
    var rows = state.subs.map(function (s) { return { s: s, t: total(s.id) }; }).sort(function (a, b) { return b.t - a.t; }).map(function (r, i) {
      var S = sc(r.s.id); return [i + 1, r.s.team, r.s.track, r.s.repo, r.s.modelType || '', S.tier || ''].concat(CRIT.map(function (c) { return Math.min(+S.v[c[0]] || 0, cap(r.s.id, c[0], c[2])); }), [r.t, S.note || '']);
    });
    var csv = [head].concat(rows).map(function (r) { return r.map(function (x) { return '"' + String(x == null ? '' : x).replace(/"/g, '""') + '"'; }).join(','); }).join('\n');
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv' })); a.download = 'datathon-scores.csv'; document.body.appendChild(a); a.click(); a.remove();
  });
  $('clear').addEventListener('click', function () { if (confirm('Delete ALL submissions and scores from this browser?')) { state = { subs: [], scores: {} }; render(); } });
  var tk = $('gh-token');
  try { tk.value = localStorage.getItem('dt_gh_token') || ''; } catch (e) {}
  tk.addEventListener('input', function () { try { localStorage.setItem('dt_gh_token', tk.value.trim()); } catch (e) {} });
  render();
})();
