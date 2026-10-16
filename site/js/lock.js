// OPTIONAL release lock for the problem-statements page.
// Set LOCK_UNTIL_RELEASE to true to cover the page with a countdown until 9:30 AM IST on event day.
// NOTE: this is cosmetic only — the files are still reachable by URL. For a hard embargo, upload the
// /datasets folder at 9:30 AM instead of before.
(function () {
  var CONFIG = { LOCK_UNTIL_RELEASE: false, RELEASE_AT: '2026-10-16T09:30:00+05:30' };
  var lock = document.getElementById('lock');
  if (!lock || !CONFIG.LOCK_UNTIL_RELEASE) return;
  function check() {
    var locked = Date.now() < new Date(CONFIG.RELEASE_AT).getTime();
    lock.hidden = !locked;
    document.body.style.overflow = locked ? 'hidden' : '';
    return locked;
  }
  if (check()) { var t = setInterval(function () { if (!check()) clearInterval(t); }, 1000); }
})();
