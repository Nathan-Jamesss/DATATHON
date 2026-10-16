(function () {
  var CFG = window.DATATHON || {};
  var form = document.getElementById('r2form');
  if (!form) return;
  var evEl = document.getElementById('evidence');
  var out = document.getElementById('r2out');
  var evidence = null;

  // show/hide fields depending on the chosen model type
  function sync() {
    var t = (form.querySelector('input[name=modelType]:checked') || {}).value || '';
    form.querySelectorAll('[data-when]').forEach(function (el) {
      var on = el.dataset.when.split(' ').indexOf(t) >= 0;
      el.hidden = !on;
      el.querySelectorAll('input,select,textarea').forEach(function (i) { i.disabled = !on; });
    });
  }
  form.addEventListener('change', sync); sync();

  // draft autosave (per browser)
  var KEY = 'dt_r2_draft';
  try {
    var d = JSON.parse(localStorage.getItem(KEY) || 'null');
    if (d) Object.keys(d).forEach(function (k) {
      var els = form.elements[k]; if (!els) return;
      if (els.length && els[0] && els[0].type === 'radio') { [].forEach.call(els, function (r) { r.checked = r.value === d[k]; }); }
      else if (els.length && els[0] && els[0].type === 'checkbox') { [].forEach.call(els, function (c) { c.checked = [].concat(d[k]).indexOf(c.value) >= 0; }); }
      else if (els.type === 'checkbox') els.checked = !!d[k]; else if (els.value !== undefined) els.value = d[k];
    });
    sync();
  } catch (e) {}
  form.addEventListener('input', function () {
    try { localStorage.setItem(KEY, JSON.stringify(collect(true))); } catch (e) {}
  });

  function collect(draft) {
    var fd = new FormData(form), o = {};
    fd.forEach(function (v, k) { if (o[k] === undefined) o[k] = v; else o[k] = [].concat(o[k], v); });
    if (draft) return o;
    var apis = [].concat(o.api || []);
    var arr = function (x) { return x === undefined ? [] : [].concat(x); };
    return {
      id: 'r2-' + Date.now().toString(36),
      submittedAt: new Date().toISOString(),
      round: 2,
      team: o.team || '', members: o.members || '', regNos: o.regNos || '', phones: o.phones || '', size: o.size || '', email: o.email || '', track: o.track || '',
      product: o.product || '', pitch: o.pitch || '', repo: (o.repo || '').trim(), branch: (o.branch || '').trim(), demo: o.demo || '',
      modelType: o.modelType || '',
      modelDetails: { algo: o.algo || '', task: o.task || '', target: o.target || '', features: o.features || '', split: o.split || '', baseline: o.baseline || '', metric: o.metric || '', trainPath: o.trainPath || '', modelPath: o.modelPath || '' },
      apis: apis, apiOther: o.apiOther || '', apiUse: o.apiUse || '',
      extraData: o.extraData || '', howToRun: o.howToRun || '', datasetsUsed: o.datasetsUsed || '',
      declarations: arr(o.decl),
      evidence: evidence && evidence.ok ? evidence : null
    };
  }

  // prefill from the team registration on the Problem Statements page
  try {
    var tm = JSON.parse(localStorage.getItem('dt_team') || 'null');
    if (tm) ['team', 'members', 'regNos', 'phones', 'email', 'size', 'track'].forEach(function (k) { var el = form.elements[k]; if (el && !el.value && tm[k]) el.value = tm[k]; });
  } catch (e) {}

  var verifyBtn = document.getElementById('verify');
  verifyBtn.addEventListener('click', function () {
    var url = form.elements.repo.value.trim();
    evEl.innerHTML = '<div class="ev"><span>Checking repository…</span></div>';
    verifyBtn.disabled = true;
    RepoCheck.check(url).then(function (r) { evidence = r; RepoCheck.render(evEl, r); }).then(function () { verifyBtn.disabled = false; });
  });

  function download(name, text) {
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
    a.download = name; document.body.appendChild(a); a.click(); a.remove();
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!RepoCheck.parse(form.elements.repo.value)) { form.elements.repo.setCustomValidity('Enter a GitHub repository URL'); form.reportValidity(); return; }
    form.elements.repo.setCustomValidity('');
    var go = function () {
      var data = collect(false);
      var json = JSON.stringify(data, null, 2);
      var show = function (msg, ok) {
        out.hidden = false;
        out.className = 'r2out ' + (ok ? 'r2out--ok' : '');
        out.innerHTML = '<b>' + msg + '</b><textarea readonly rows="6">' + RepoCheck.esc(json) + '</textarea>';
      };
      var file = 'datathon-round2-' + (data.team || 'team').replace(/[^a-z0-9]+/gi, '-').toLowerCase() + '.json';
      if (CFG.SUBMIT_ENDPOINT) {
        fetch(CFG.SUBMIT_ENDPOINT, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: json })
          .then(function () { show('Submitted. Keep this copy for your records.', true); })
          .catch(function () { download(file, json); show('Could not reach the server. Your submission file was downloaded: send it to the organisers.', false); });
      } else {
        download(file, json);
        show('Submission file downloaded (' + file + '). Hand it to the organisers.', true);
      }
      out.scrollIntoView({ behavior: 'smooth', block: 'center' });
    };
    go();
  });
})();
