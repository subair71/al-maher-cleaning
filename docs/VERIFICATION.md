# Dev preview verification — 30 September 2026

## Completed

- [x] Existing vanilla stack and original logo retained; six existing services preserved.
- [x] Home, About, individual service pages, offers, comparison gallery, contact, FAQ and draft legal pages.
- [x] Arabic default/RTL and English/LTR; persistent language preference; translated forms, errors and admin labels.
- [x] Local optimized WebP photos and licensed WOFF2 fonts; lazy loading, reduced-motion support and visible keyboard focus.
- [x] Contact links use `tel:+962778842130` and `https://wa.me/962778842130`.
- [x] Quote/booking validation; future date/time validation; required consent; explicit simulated-success wording.
- [x] Multiple image preview/removal, MIME/size/count checks and decoded-image checks; simulated progress.
- [x] Open admin preview: content CRUD, search, status filters, record details, attachments, status changes and reset.
- [x] Sample records are separate from any production service; no backend or real customer dataset is connected.
- [x] Proposal states total price TBC and marks suggested milestones/timeline/terms as proposed.
- [x] Planned API/schema, security, backup/restore, handover and future-phase boundaries documented.

## Checks executed

`npm test`: 4 tests passed for validation, uploads, escaping and sample-repository reset.

`CHROME_EXECUTABLE=/tmp/chromium SCREENSHOT_DIR=<scratch>/qa node tests/browser.cjs`: 108 layout/page/language combinations passed (18 public/admin pages × Arabic/English × 390, 768 and 1440px widths). No horizontal overflow or browser JavaScript errors observed. Checks also exercised comparison keyboard adjustment, category filter, invalid and successful demo forms, image rejection/preview/removal, request-to-admin flow, attachment viewing, content editing/add/delete, search/status filters, reset, mobile navigation, contact URLs and reduced motion. Screenshots visually reviewed for desktop, mobile Arabic and admin. Official logo asset unchanged.

The self-contained HTML export was also opened with `file://` and checked for language switching, quote validation, navigation and admin overview. It requires a browser that executes JavaScript; some attachment viewers only show a static file preview. Opening the downloaded file in a browser allows interaction.

## Remaining production setup

- [ ] Hosting, domain, ownership/account access, usage limits and recurring fees agreed.
- [ ] Production database/API, server validation, spam controls, private upload storage and notification delivery.
- [ ] Real administrator login/MFA, protected API permissions, sessions and audit logging.
- [ ] Verified map pin/directions and opening hours; address re-confirmation.
- [ ] Genuine approved before/after photos and testimonials; verified offer dates/terms.
- [ ] Reviewed legal copy, retention policy and processor details.
- [ ] HTTPS/security headers, scheduled backups and a successful restore exercise.
- [ ] Approved production URL/SEO indexing and analytics ID/consent integration.
- [ ] Real-device Safari/Android acceptance, production accessibility audit and performance checks under actual hosting/network conditions.

No claim of production submissions, confirmed bookings, secure authentication, active backups or live analytics is made. `main` and the existing public deployment remain untouched. All implementation changes target `dev`.
