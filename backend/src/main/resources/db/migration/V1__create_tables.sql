CREATE TABLE enquiries (
 id UUID PRIMARY KEY,
 kind VARCHAR(20) NOT NULL CHECK (kind IN ('QUOTE','BOOKING','CORPORATE','CONTACT')),
 name VARCHAR(120) NOT NULL,
 phone VARCHAR(35) NOT NULL,
 email VARCHAR(254),
 service_slug VARCHAR(100),
 city VARCHAR(120),
 address VARCHAR(500),
 requested_date DATE,
 preferred_time VARCHAR(80),
 message TEXT,
 language VARCHAR(2) NOT NULL DEFAULT 'ar' CHECK (language IN ('ar','en')),
 consent BOOLEAN NOT NULL,
 status VARCHAR(20) NOT NULL DEFAULT 'NEW' CHECK (status IN ('NEW','CONTACTED','QUOTED','CONFIRMED','COMPLETED','CANCELLED')),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_enquiries_status_created ON enquiries(status, created_at DESC);
CREATE INDEX idx_enquiries_kind_created ON enquiries(kind, created_at DESC);
CREATE TABLE catalog_entries (
 id UUID PRIMARY KEY,
 category VARCHAR(30) NOT NULL CHECK (category IN ('SERVICE','OFFER','FAQ','REVIEW','CLIENT','GALLERY','BEFORE_AFTER','LANDING_PAGE','SITE_CONTENT')),
 slug VARCHAR(120) NOT NULL,
 title_ar VARCHAR(300) NOT NULL,
 title_en VARCHAR(300) NOT NULL,
 body_ar TEXT,
 body_en TEXT,
 image_url VARCHAR(1000),
 published BOOLEAN NOT NULL DEFAULT FALSE,
 display_order INTEGER NOT NULL DEFAULT 0,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE(category, slug)
);
CREATE INDEX idx_catalog_public ON catalog_entries(category,published,display_order);
