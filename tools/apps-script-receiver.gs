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

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET) || ss.insertSheet(SHEET);
  if (sh.getLastRow() === 0) {
    sh.appendRow(['submittedAt', 'team', 'track', 'repo', 'modelType', 'apis', 'email', 'json']);
  }
  return sh;
}

function doPost(e) {
  if (e.postData.contents.length > 200000) return ContentService.createTextOutput('too large');
  var d = JSON.parse(e.postData.contents);
  getSheet_().appendRow([d.submittedAt, d.team, d.track, d.repo, d.modelType, (d.apis || []).join(', '), d.email, JSON.stringify(d)]);
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
