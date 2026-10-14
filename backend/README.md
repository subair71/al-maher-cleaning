# Al Maher Cleaning Services — Spring Boot API

Separate Java 21 / Spring Boot 3 REST backend for the existing bilingual static website. No frontend is replaced or wired to this API yet.

## Development
1. Install Java 21, Maven 3.9+, and Docker Compose.
2. Copy `.env.example` to `.env` and set unique secrets (minimum 16 characters for `ADMIN_PASSWORD`).
3. From `backend/`, start PostgreSQL using `docker compose --env-file .env up -d`.
4. Export environment variables from `.env` (e.g. `set -a; source .env; set +a`) and start with `mvn spring-boot:run`.
5. API listens on `http://localhost:8081`; `GET /actuator/health` confirms readiness.

## Endpoints
| Method | Path | Authentication |
| --- | --- | --- |
| POST | /api/v1/enquiries | Public |
| GET | /api/v1/catalog/{category} | Public; published only |
| GET | /api/v1/catalog/{category}/{slug} | Public; published only |
| GET | /api/v1/admin/enquiries | HTTP Basic admin |
| GET | /api/v1/admin/enquiries/{id} | HTTP Basic admin |
| PATCH | /api/v1/admin/enquiries/{id}/status | HTTP Basic admin |
| GET | /api/v1/admin/catalog | HTTP Basic admin |
| POST | /api/v1/admin/catalog | HTTP Basic admin |
| PUT | /api/v1/admin/catalog/{id} | HTTP Basic admin |
| DELETE | /api/v1/admin/catalog/{id} | HTTP Basic admin |

Categories: SERVICE, OFFER, FAQ, REVIEW, CLIENT, GALLERY, BEFORE_AFTER, LANDING_PAGE, SITE_CONTENT.
Enquiry kinds: QUOTE, BOOKING, CORPORATE, CONTACT.
Statuses: NEW, CONTACTED, QUOTED, CONFIRMED, COMPLETED, CANCELLED.

Example public quote request:
```sh
curl -i http://localhost:8081/api/v1/enquiries -H 'Content-Type: application/json' -d '{"kind":"QUOTE","name":"Demo Customer","phone":"+962778842130","serviceSlug":"sofa","city":"Russeifa","message":"Please contact me","language":"en","consent":true}'
```
Create private admin content only over HTTPS with credentials stored securely, not in frontend JavaScript.

## Important security & production work
- HTTP Basic is a starter mechanism for a server-managed admin client; **never place admin credentials in the static GitHub Pages site**. Replace with OIDC/short-lived token auth and role controls before integrating the browser admin UI.
- Restrict public enquiry requests with edge/WAF rate limiting, anti-spam controls and input abuse monitoring before live traffic. Add consent/privacy policy and data retention, backups, and an audit log.
- Image uploads, notifications, customer accounts, campaign analytics and frontend persistence are **not implemented**.
- Use TLS, private database networking, and a controlled production secret manager. Set strict origin list via CORS_ORIGINS; CORS is not authentication.
- Flyway owns schema migrations; JPA is set to validate, never mutate schema.
- Review and approve content, client logos and testimonials before marking published.

## Frontend integration
The current public website still prepares WhatsApp messages and the admin page still uses session-only data. Integration should adapt `js/repository.js` and public forms to call this API and must create a genuinely authenticated admin session before showing real customer data.
