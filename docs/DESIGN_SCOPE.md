# Expanded scope — design presentation

This branch intentionally contains presentation work only, as requested on 5 October 2026. It retains the existing static HTML/CSS/JavaScript site, logo, photographs, blue/gold styling and Arabic-first navigation.

## Designed screens and interactions
- Existing public pages and six service pages, plus villa, apartment, car, tank and corporate service pages.
- Seven reusable campaign landing pages; nested route examples for campaigns, services and offers.
- Homepage corporate section, client logo placements, coverage areas, FAQs and contact block.
- Quote, booking and corporate enquiry layouts with bilingual validation, photo selection, review dialog and WhatsApp handoff.
- Review composition screen with WhatsApp handoff; no automatic public publication.
- Admin overview and navigation for requests, bookings, corporate, customers, notifications, services/prices, offers/promotions, gallery/before-after, reviews, clients/logos, landing pages, advertising campaigns, site content, FAQs and settings.
- Session-only add/edit/delete interactions and request status changes. Administration is not authenticated and MUST NOT be connected to private production data.
- Visible empty analytics states. No invented visitor statistics, testimonials or customer logos.

## Intentionally not implemented
No database, API, authentication, role enforcement, email/SMS notifications, live analytics, payment gateway, loyalty, workforce scheduling or mobile app. No secrets or production tracking IDs. Repository and configuration modules are presentation boundaries, not a deployed backend.

Form data and photos stay in tab memory and clear on reload. Forms prepare a request, then explicitly invite the visitor to send it through WhatsApp; they never claim it has reached the business. Photos must be attached manually in WhatsApp. The public review flow similarly prepares a message for the team. Content changes in administration are session-only.

## Future implementation
Replace the in-memory repository with authenticated backend services after scope approval. Specify server validation, private upload storage, rate limits, access rules, backups, retention, consent and notifications then. A shared customer/request domain can later support accounts, jobs, payment references and Flutter applications. Future role/payment/team field contracts are outlined in js/platform/catalog.js only; no security or scalability guarantee is implied by these models.

## Content and indexing
The branch keeps noindex/robots blocking until approved for production. Labels such as “demo” and “preview” are not used in the client-facing interface. Unverified client logos are represented by reserved placements, and illustrative gallery photographs are disclosed. Exact business map pin, actual testimonials, client logos and final policies still require owner content. Existing imagery is retained; confirm usage permissions before commercial launch.

## Commands
npm run build
npm test
npm run serve
node tests/expanded.cjs

Hosting remains the existing static setup. This change introduces no paid application subscription or recurring service.
