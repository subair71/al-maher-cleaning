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

## Published stylesheet repair

The Sites checkout contained the previous design's `style.css` alongside the new page markup. Replaced it with the matching responsive stylesheet and gave all entry pages a new stylesheet filename (`responsive-v3.css`) to avoid stale asset reuse. Added SVG width/height attributes so icons remain 23px even if styles fail, narrow-phone wrapping, tablet grids and 16px mobile form controls.

`tests/responsive.cjs` validates the actual Sites `dist` directory: 50 combinations of five screens × Arabic/English × 320/390/768/1024/1440px passed. No horizontal overflow, all icons at most 42px, correct theme loaded, and 23px fallback with the stylesheet blocked. Mobile Arabic and desktop English screenshots inspected.

## Expanded design branch — 5 October 2026

- 476 route/language/viewport combinations passed: 34 routes × Arabic/English × 320/375/390/430/768/1024/1440 pixels; no horizontal overflow.
- All rendered internal links resolved; nested campaign routes and service-to-quote prefilling passed.
- Request validation, rejected SVG, image selection, review/edit dialog and WhatsApp handoff passed.
- Request status change, all admin navigation tabs and client editing passed.
- Mobile menu stacking issue discovered and fixed; RTL mobile navigation passed.
- Review message preparation passed; no automatic publication or backend submission.
- No browser JavaScript errors in the interaction suite.
- Desktop home/campaign/admin and Arabic mobile home/booking screenshots visually inspected.
- External image requests blocked during deterministic browser checks to exercise local fallbacks. Live external image availability is not guaranteed; existing local cleaning photographs handle failed sources.
- Existing form-validation unit suite passed (4 tests).

The old browser suite describes previous interfaces; use tests/expanded.cjs for this branch. Actual backend, security enforcement and integrations are explicitly outside this design-only update.
