// Organiser settings for the Round 2 submission + judge pages.
window.DATATHON = {
  // Paste your Google Apps Script web-app URL here (see tools/apps-script-receiver.gs).
  // Leave empty to let teams download their submission as a JSON file instead.
  SUBMIT_ENDPOINT: '',

  // Maximum marks the "ML model from scratch" criterion can receive, by verified model tier.
  TIER_CAPS: { scratch: 25, finetuned: 15, api: 5, none: 0 }
};
