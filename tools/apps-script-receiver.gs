/**
 * DATATHON Round 2 submission receiver (Google Apps Script).
 *
 * Setup (5 minutes):
 *  1. Create a Google Sheet. Extensions > Apps Script. Paste this file.
 *  2. Deploy > New deployment > type "Web app".
 *       Execute as: Me.   Who has access: Anyone.
 *  3. Copy the web-app URL into site/js/config.js as SUBMIT_ENDPOINT.
 *
 * Teams' submissions are appended to the "Submissions" sheet (one row each, full JSON in the last column).
 * The judges console's "Load from endpoint" button calls doGet, which returns every submission as JSON,
 * but ONLY when the request carries the judge key. Set it: Project Settings > Script properties > JUDGE_KEY = <a long random string>.
 * (The endpoint URL is public inside config.js, so without this key anyone could read all submissions.)
 */
var SHEET = 'Submissions';
var TEAMS = 'Teams';
var SUMMARY = 'Summary';
var TRACKS = ['01 Health', '02 Education', '03 Smart City', '04 Business'];

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET) || ss.insertSheet(SHEET);
  if (sh.getLastRow() === 0) {
    sh.appendRow(['submittedAt', 'team', 'track', 'repo', 'modelType', 'apis', 'email', 'json']);
  }
  return sh;
}

function getTeams_() {
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

function doPost(e) {
  if (e.postData.contents.length > 200000) return ContentService.createTextOutput('too large');
  var d = JSON.parse(e.postData.contents);
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  getSheet_().appendRow([d.submittedAt, d.team, d.track, d.repo, d.modelType, (d.apis || []).join(', '), d.email, JSON.stringify(d)]);
  getTeams_().appendRow([d.submittedAt, d.team, d.members, Number(d.size) || '', d.track, d.email, d.product, d.repo, d.modelType]);
  ensureSummary_();
  lock.releaseLock();
  return ContentService.createTextOutput('ok');
}

function doGet(e) {
  var key = PropertiesService.getScriptProperties().getProperty('JUDGE_KEY');
  if (!key || !e || !e.parameter || e.parameter.key !== key) {
    return ContentService.createTextOutput('[]').setMimeType(ContentService.MimeType.JSON);
  }
  var rows = getSheet_().getDataRange().getValues();
  var out = [];
  for (var i = 1; i < rows.length; i++) {
    try { out.push(JSON.parse(rows[i][7])); } catch (err) {}
  }
  return ContentService.createTextOutput(JSON.stringify(out)).setMimeType(ContentService.MimeType.JSON);
}
