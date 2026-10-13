# Jordan-inspired redesign and SEO review

Branch: `feature/jordan-inspired-redesign-seo`. Baseline: main `c4432648ecc6d52ef4ae46dc6f928002c4e91a0c`. No merge or deployment.

## Reference comparison (13 October 2026)
These are selected reference websites, not a verified ranking of the best companies. Research assessed published page structure and content; reference visuals and mobile behavior were not independently browser-tested.

| Reference URL | Useful feature | Existing Al Maher | Enhancement | Priority |
|---|---|---|---|---|
| https://www.bashservices.jo/en/cleaning-services | Detailed service catalogue, corporate/handover sections | Short service pages | Service-specific scope, quote factors and preparation | High |
| https://inserviceclean.com/en | Clear contact journey and sequential booking explanation | CTAs scattered across many sections | Focused hero, service selection shortcuts, three-step enquiry path | High |
| https://homihs.com/ | Service discovery, preparation FAQs, local coverage | Text-only catalogue | Image cards, preparation guide and coverage confirmation | High |
| https://www.wowservice.net/en | Commercial proposal journey | Existing corporate form | Clearer business section and internal links | Medium |

Strong references found in Amman; no equally suitable Russeifa/Zarqa website was verified in this search. Al Maher's existing content welcomes enquiries from all three areas; address coverage remains subject to team confirmation. No competitor prices, testimonials, certifications or guarantees were imported.

## Implemented
- Focused blue/gold home design, editorial hero, image-led service cards, service intent shortcuts, enquiry steps, residential and commercial paths, original offers, preparation guide, FAQs and review invitation.
- Eleven bilingual service pages explain scope to discuss, quote factors and preparation. These are planning guidance; exact service inclusions are agreed by the team.
- Existing logo, font files, image assets and palette preserved byte-for-byte. Existing local WebP assets reused for reliable primary photo delivery; no external assets imported. Existing stock-gallery references remain illustrative, not represented as completed jobs.
- Quote, booking and corporate requests keep their WhatsApp handoff and confirmation requirement. Photo upload control removed because there is no upload backend; photos can be attached manually in WhatsApp.
- Full public header, footer and page content generated as HTML using the same rendering functions as the application. Navigation works before JavaScript. Forms have a no-JavaScript contact alternative.
- Arabic RTL/English LTR, keyboard focus, native FAQ disclosure, touch targets, safe-area mobile contact bar and reduced-motion CSS.

## SEO
Existing static HTML/CSS/JS architecture retained. Build now emits full public-page content rather than a short fallback list replaced by JavaScript. Language variants, canonical URLs, hreflang, metadata, social metadata, LocalBusiness/Service/Breadcrumb schema, sitemap, robots and a 404 page are generated reproducibly. Homepage canonical uses the directory URL. Campaign/offer/service aliases are noindex and canonicalize to their relevant service. No invented ratings, hours, coordinates or business statistics. Font delivery stays local and images have dimensions; primary photos are local, non-hero photos lazy-loaded.

Core Web Vitals are not measured and rankings are not promised. GitHub Pages cannot implement arbitrary server redirects or response-header policies; alias canonicalization is used. Verify Search Console and the final production domain after approved deployment.

## Backend dependencies
Durable bookings, availability, automated confirmations, authentication, private uploads, content persistence, review moderation and notifications require backend services. Admin remains a session-only presentation workspace. None of these capabilities was claimed as live.

## Content gaps
Owner-supplied real paired job photos, approved reviews/client logos, final offer dates and eligibility, exact map pin, opening hours, approved policies, verified service inclusions and service-specific pricing are still needed. Unapproved client placeholders were removed from the home page; no substitute logos or fake results were added.

## Preview and verification
`docs/branch-preview.html` is a self-contained, offline interactive review file with embedded existing assets. Download and open it in a modern browser. It includes language switching, public navigation and request preparation; actual enquiries still require an explicit WhatsApp send. No website has been deployed.

Browser automation infrastructure is unavailable in this session. Visual appearance, viewport behavior and end-to-end browser interactions remain unverified. Source, rendering, metadata, links, schema and existing validation/routing checks are validated separately; see check results supplied at handoff.

Completed checks: 56 public/root language variants passed HTML content, heading, structured-data, image and internal-link checks; sitemap/404/upload checks passed; 4 existing validation tests and 2 route tests passed; modified JavaScript syntax and whitespace checks passed. Mobile/desktop visual QA remains outstanding.

## Latest content update
Primary image URLs now match main’s photos and service-image records; original gallery image pairs remain in use with existing local fallbacks. Added clearly labelled sample residential, upholstery and office enquiries plus three fictional sample reviews. Samples use data-nosnippet and are omitted from review/rating schema. Service-specific FAQs are rendered on the page and emitted in matching FAQPage structured data. Replace illustrative content with owner-approved material when available.
