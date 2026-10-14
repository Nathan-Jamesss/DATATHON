# DATATHON 2026 — VIT-AP

Website for DATATHON (Data Science Club x IIEC, VIT-AP University, 16 Oct 2026): static site, no build step needed to view.

- `site/` — the website. Open `site/index.html`. Pages: home, timeline, problem statements + datasets, Round 1 PPT, Round 2 submission, judging, rules, judges console.
- `tools/` — generators. `python tools/build2.py site` rebuilds the HTML; `python tools/mkppt.py site/assets <out.pptx>` rebuilds the PPT template. `apps-script-receiver.gs` collects Round 2 submissions into a Google Sheet (see comments in the file).
- `DESIGN.md`, `theme.css`, `tokens.json`, `variables.css` — design reference the site follows (recoloured to the poster: black, cyan, white).
- Problem statement briefs, dataset pack and the poster are kept at the top level.

Organiser settings (submission endpoint, model-tier mark caps): `site/js/config.js`.
