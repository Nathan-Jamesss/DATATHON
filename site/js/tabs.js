(function () {
  var tabs = [].slice.call(document.querySelectorAll('.ptab'));
  var panels = [].slice.call(document.querySelectorAll('.ptrack'));
  if (!tabs.length) return;
  function show(n, push) {
    tabs.forEach(function (t) { t.setAttribute('aria-selected', t.dataset.n === String(n) ? 'true' : 'false'); });
    panels.forEach(function (p) { p.hidden = p.dataset.track !== String(n); });
    if (push) { try { history.replaceState(null, '', '#track-' + n); } catch (e) {} }
  }
  tabs.forEach(function (t) { t.addEventListener('click', function () { show(t.dataset.n, true); }); });
  var m = /track-(\d)/.exec(location.hash);
  show(m ? m[1] : 1, false);
  window.addEventListener('hashchange', function () { var h = /track-(\d)/.exec(location.hash); if (h) show(h[1], false); });
})();
