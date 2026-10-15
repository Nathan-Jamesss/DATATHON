import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def edit(path, pairs):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, (path, a[:60])
        s = s.replace(a, b, 1)
    open(path, 'w', encoding='utf-8').write(s)

# form: number of people
edit('pages_r2.py', [(
    '{f("Contact email", "email", "email", True)}',
    '{f("Contact email", "email", "email", True)}\n<label class="fld"><span>Number of people *</span><select name="size" required><option value="">Choose</option><option value="1">1 (solo)</option><option value="2">2 (duo)</option></select></label>')])
edit('../site/js/round2.js', [("members: o.members || '',", "members: o.members || '', size: o.size || '',")])
edit('../site/js/judge.js', [("['Members', s.members],", "['Members', s.members], ['Team size', s.size],")])

# Apps Script: second tab "Teams" + "Summary" tab with live counts per track
edit('apps-script-receiver.gs', [
 ("var SHEET = 'Submissions';",
  "var SHEET = 'Submissions';\nvar TEAMS = 'Teams';\nvar SUMMARY = 'Summary';\nvar TRACKS = ['01 Health', '02 Education', '03 Smart City', '04 Business'];"),
 ("function doPost(e) {",
  """function getTeams_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(TEAMS);
  if (!sh) {
    sh = ss.insertSheet(TEAMS);
    sh.appendRow(['submittedAt', 'team', 'members', 'people', 'track', 'email', 'product', 'repo', 'modelType']);
    sh.setFrozenRows(1);
  }
  return sh;
}

function ensureSummary_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (ss.getSheetByName(SUMMARY)) return;
  var sh = ss.insertSheet(SUMMARY);
  sh.appendRow(['Track', 'Teams', 'People']);
  for (var i = 0; i < TRACKS.length; i++) {
    var r = i + 2;
    sh.appendRow([TRACKS[i], '=COUNTIF(Teams!E:E,A' + r + ')', '=SUMIF(Teams!E:E,A' + r + ',Teams!D:D)']);
  }
  var t = TRACKS.length + 2;
  sh.appendRow(['Total', '=SUM(B2:B' + (t - 1) + ')', '=SUM(C2:C' + (t - 1) + ')']);
  sh.setFrozenRows(1);
}

function doPost(e) {"""),
 ("  lock.releaseLock();\n  return ContentService.createTextOutput('ok');",
  "  getTeams_().appendRow([d.submittedAt, d.team, d.members, Number(d.size) || '', d.track, d.email, d.product, d.repo, d.modelType]);\n  ensureSummary_();\n  lock.releaseLock();\n  return ContentService.createTextOutput('ok');"),
])
print('ok')
