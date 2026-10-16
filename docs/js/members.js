// Per-member name + registration number. Member 2 appears for duo teams.
// The hidden "members" / "regNos" fields are filled as "Name1, Name2" / "Reg1, Reg2" so the Google Sheet format stays the same.
(function () {
  document.querySelectorAll('.memblock').forEach(function (block) {
    var form = block.closest('form');
    var size = form.elements.size;
    var f = function (n) { return form.elements[n]; };

    function sync() {
      var duo = size.value === '2';
      block.querySelectorAll('[data-m2]').forEach(function (l) {
        l.hidden = !duo;
        var i = l.querySelector('input'); i.disabled = !duo; i.required = duo;
      });
    }
    function fill() {
      var duo = size.value === '2';
      f('members').value = [f('m1name').value, duo ? f('m2name').value : ''].map(function (s) { return s.trim(); }).filter(Boolean).join(', ');
      f('regNos').value = [f('m1reg').value, duo ? f('m2reg').value : ''].map(function (s) { return s.trim().toUpperCase(); }).filter(Boolean).join(', ');
      f('phones').value = [f('m1phone').value, duo ? f('m2phone').value : ''].map(function (s) { return s.trim(); }).filter(Boolean).join(', ');
    }
    // values pre-filled by other scripts (saved team / draft) arrive in the hidden fields: split them back out
    function split() {
      var n = (f('members').value || '').split(','), r = (f('regNos').value || '').split(','), ph = (f('phones').value || '').split(',');
      if (!f('m1phone').value && ph[0]) f('m1phone').value = ph[0].trim();
      if (!f('m2phone').value && ph[1]) f('m2phone').value = ph[1].trim();
      if (!f('m1name').value && n[0]) f('m1name').value = n[0].trim();
      if (!f('m1reg').value && r[0]) f('m1reg').value = r[0].trim();
      if (!f('m2name').value && n[1]) f('m2name').value = n[1].trim();
      if (!f('m2reg').value && r[1]) f('m2reg').value = r[1].trim();
      if (!size.value && n[1] && n[1].trim()) size.value = '2';
    }

    split(); sync();
    size.addEventListener('change', sync);
    form.addEventListener('input', fill);
    // runs before the page's own submit handler: fill hidden fields and block incomplete forms
    document.addEventListener('submit', function (e) {
      if (e.target !== form) return;
      fill();
      if (!form.reportValidity()) { e.preventDefault(); e.stopImmediatePropagation(); }
    }, true);
  });
})();
