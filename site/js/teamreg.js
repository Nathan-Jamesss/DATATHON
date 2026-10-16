(function () {
  var form = document.getElementById('teamform');
  if (!form) return;
  var CFG = window.DATATHON || {};
  var out = document.getElementById('teamout');
  var KEY = 'dt_team';

  try {
    var saved = JSON.parse(localStorage.getItem(KEY) || 'null');
    if (saved) ['team', 'members', 'regNos', 'phones', 'email', 'size', 'track'].forEach(function (k) { if (form.elements[k] && saved[k]) form.elements[k].value = saved[k]; });
  } catch (e) {}

  function show(msg, ok) {
    out.hidden = false; out.className = 'r2out ' + (ok ? 'r2out--ok' : '');
    out.textContent = msg;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;
    var d = {
      type: 'team', submittedAt: new Date().toISOString(),
      team: form.elements.team.value.trim(), members: form.elements.members.value.trim(), regNos: form.elements.regNos.value.trim(), phones: form.elements.phones.value.trim(), email: form.elements.email.value.trim(),
      size: form.elements.size.value, track: form.elements.track.value
    };
    try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e2) {}
    var json = JSON.stringify(d);
    if (CFG.SUBMIT_ENDPOINT) {
      fetch(CFG.SUBMIT_ENDPOINT, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: json })
        .then(function () { show('Saved. Team "' + d.team + '" · ' + d.track + '. You can submit Round 2 from the Round 2 page; these details will be filled in for you.', true); })
        .catch(function () { show('Could not reach the server. Check your internet and press Save again.', false); });
    } else {
      show('Saved on this device only (no server connected).', false);
    }
  });
})();
