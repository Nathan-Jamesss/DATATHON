/**
 * DATATHON Round 2 submission receiver (Google Apps Script).
 *
 * Setup (5 minutes):
 *  1. Create a Google Sheet. Extensions > Apps Script. Paste this file.
 *  2. Deploy > New deployment > type "Web app".
 *       Execute as: Me.   Who has access: Anyone.
 *  3. Copy the web-app URL into site/js/config.js as SUBMIT_ENDPOINT.
 *
 * Every Round 2 submission adds a row to TWO tabs:
 *   "Teams"        team name + track + members + number of people   (the list you hand to judges)
 *   "Submissions"  the full Round 2 details (repo, model type, APIs, ...)
 * If you ever change the columns, delete both tabs; they are recreated on the next submission.
 *
 * Optional: Project Settings > Script properties > JUDGE_KEY lets the judges console's "Load from endpoint"
 * button read submissions (without a key nobody can read anything through the URL).
 */
var SUBMISSIONS = 'Submissions';
var TEAMS = 'Teams';
var SUB_HEAD = ['submittedAt', 'team', 'track', 'product', 'repo', 'demo', 'modelType', 'task', 'algorithm', 'trainFile', 'apis', 'apiUse', 'extraData', 'email', 'json'];
var TEAM_HEAD = ['Team name', 'Track', 'Members', 'People'];

function getTab_(name, head) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    sh.appendRow(head);
    sh.getRange(1, 1, 1, head.length).setFontWeight('bold').setBackground('#000000').setFontColor('#ffffff');
    sh.setFrozenRows(1);
  }
  return sh;
}

// One row per team in "Teams": a team that registers on the Problem Statements page and later submits Round 2 is updated, not duplicated.
function upsertTeam_(d) {
  var sh = getTab_(TEAMS, TEAM_HEAD);
  var rows = sh.getDataRange().getValues();
  var name = String(d.team || '').trim().toLowerCase();
  var vals = [d.team, d.track, d.members, Number(d.size) || ''];
  for (var i = 1; i < rows.length; i++) {
    if (String(rows[i][0]).trim().toLowerCase() === name) { sh.getRange(i + 1, 1, 1, 4).setValues([vals]); return; }
  }
  sh.appendRow(vals);
}

function doPost(e) {
  if (e.postData.contents.length > 200000) return ContentService.createTextOutput('too large');
  var d = JSON.parse(e.postData.contents);
  var m = d.modelDetails || {};
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  upsertTeam_(d);
  if (d.type === 'team') { lock.releaseLock(); return ContentService.createTextOutput('ok'); }
  getTab_(SUBMISSIONS, SUB_HEAD).appendRow([
    d.submittedAt, d.team, d.track, d.product, d.repo, d.demo, d.modelType,
    m.task || '', m.algo || '', m.trainPath || '',
    (d.apis || []).join(', '), d.apiUse || '', d.extraData || '', d.email, JSON.stringify(d)
  ]);
  lock.releaseLock();
  return ContentService.createTextOutput('ok');
}

function doGet(e) {
  var key = PropertiesService.getScriptProperties().getProperty('JUDGE_KEY');
  if (!key || !e || !e.parameter || e.parameter.key !== key) {
    return ContentService.createTextOutput('[]').setMimeType(ContentService.MimeType.JSON);
  }
  var rows = getTab_(SUBMISSIONS, SUB_HEAD).getDataRange().getValues();
  var jsonCol = rows[0].indexOf('json');
  var out = [];
  for (var i = 1; i < rows.length; i++) {
    try { out.push(JSON.parse(rows[i][jsonCol])); } catch (err) {}
  }
  return ContentService.createTextOutput(JSON.stringify(out)).setMimeType(ContentService.MimeType.JSON);
}
