(function () {
  // mobile nav
  var plus = document.getElementById('navplus');
  var links = document.getElementById('navlinks');
  if (plus && links) {
    plus.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      plus.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { links.classList.remove('is-open'); plus.setAttribute('aria-expanded', 'false'); }
    });
  }

  // countdown(s)
  function pad(n) { return n < 10 ? '0' + n : '' + n; }
  document.querySelectorAll('.countdown[data-target]').forEach(function (el) {
    var target = new Date(el.dataset.target).getTime();
    function tick() {
      var d = target - Date.now();
      if (d <= 0) { el.innerHTML = '<span class="countdown__live">● Live now</span>'; return false; }
      var s = Math.floor(d / 1000);
      var cells = [[Math.floor(s / 86400), 'days'], [Math.floor(s % 86400 / 3600), 'hrs'], [Math.floor(s % 3600 / 60), 'min'], [s % 60, 'sec']];
      el.innerHTML = cells.map(function (c) { return '<div class="countdown__cell"><b>' + pad(c[0]) + '</b><small>' + c[1] + '</small></div>'; }).join('');
      return true;
    }
    if (tick()) { var t = setInterval(function () { if (!tick()) clearInterval(t); }, 1000); }
  });

  // highlight the itinerary stop that is happening right now (event day only)
  var stops = document.querySelectorAll('.stop[data-start], .tcard[data-start], .strip__box[data-start]');
  function mark() {
    var now = Date.now(), hit = null;
    stops.forEach(function (s) {
      s.classList.remove('is-now');
      var a = new Date(s.dataset.start).getTime(), b = new Date(s.dataset.end).getTime();
      if (now >= a && now < b) hit = s; // later stops win, so the release milestone yields to Round 1 only after 10:05
    });
    if (hit) hit.classList.add('is-now');
  }
  if (stops.length) { mark(); setInterval(mark, 30000); }
})();
