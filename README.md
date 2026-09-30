# Al Maher Cleaning & Dry Cleaning — dev preview

Premium Arabic-first / English website demo. Existing vanilla HTML/CSS/JavaScript stack and official logo retained.

```sh
npm run build
npm run serve
# open http://localhost:8080
npm test
```

Open `admin.html` and select **Enter demo workspace** for the openly accessible admin preview. No secure production login is installed. Requests, photo previews and admin changes remain in tab memory; reload restores the sample dataset. Only language preference is stored locally. Do not enter real personal information. No request is sent and no booking is confirmed.

## Deliverables

- Separate service pages, About, gallery, offers, contact, FAQs and draft legal pages.
- Arabic RTL / English LTR including forms, messages and dashboard.
- Quote and booking validation; multiple image previews, removal and simulated progress.
- Admin content CRUD, request search/filter/details and status changes.
- [Client proposal](docs/proposal.html) — price and unagreed commercial terms clearly marked.
- [Production architecture, API, security and backups](docs/PRODUCTION.md).
- [Verification checklist](docs/VERIFICATION.md).

`dev` only. No changes to production deployment or `main` are part of this update. Demo indexing is disabled. See production notes before enabling real submissions, authentication, analytics or search indexing.

To run the optional browser suite, install Playwright in the development environment and run `node tests/browser.cjs` (set `CHROME_EXECUTABLE` if using an existing Chromium). Export a self-contained shareable demo with `python3 scripts/export-demo.py /absolute/output/Al-Maher-Demo.html`.
