-- Migration: SignFlow schema (all models)
-- Created at: 2026-08-22

-- ---------------------------------------------------------------------------
-- Status / reference lookups (ILookupModel)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS event_type_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(64)  NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS mime_type_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(128) NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS envelope_status_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS recipient_status_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS team_member_status_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS invite_status_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS contract_status_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS invite_type_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS webhook_delivery_status_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    label       VARCHAR(255) NOT NULL,
    description TEXT         NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- Identity lookups (ICoreLookupModel)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS user_type_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS auth_type_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS mfa_type_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS otp_type_lk (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code        VARCHAR(50)  NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE
);

-- ---------------------------------------------------------------------------
-- Identity & tenancy (IModel)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS "user" (
    id             BIGSERIAL    PRIMARY KEY,
    urn            UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    email          VARCHAR(255) NOT NULL UNIQUE,
    password       VARCHAR(255) NOT NULL,
    is_mfa_enabled BOOLEAN      NOT NULL DEFAULT FALSE,
    mfa_secret     VARCHAR(255) NULL,
    last_login     TIMESTAMPTZ  NULL,
    mfa_type_id    BIGINT       NULL REFERENCES mfa_type_lk (id),
    auth_type_id   BIGINT       NOT NULL REFERENCES auth_type_lk (id),
    created_at     TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at     TIMESTAMPTZ  NULL,
    created_by     BIGINT       NULL REFERENCES "user" (id),
    updated_by     BIGINT       NULL REFERENCES "user" (id),
    is_deleted     BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active      BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS tenant (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    subdomain   VARCHAR(100) NOT NULL UNIQUE,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    created_by  BIGINT       NULL REFERENCES "user" (id),
    updated_by  BIGINT       NULL REFERENCES "user" (id),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS tenant_profile (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    tenant_id   BIGINT       NOT NULL REFERENCES tenant (id),
    name        VARCHAR(255) NOT NULL,
    logo_url    VARCHAR(2048) NULL,
    website     VARCHAR(2048) NOT NULL,
    industry    VARCHAR(100) NULL,
    description TEXT         NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    created_by  BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by  BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS user_recovery_code (
    id         BIGSERIAL    PRIMARY KEY,
    urn        UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    code_hash  VARCHAR(255) NOT NULL,
    is_used    BOOLEAN      NOT NULL DEFAULT FALSE,
    user_id    BIGINT       NOT NULL REFERENCES "user" (id),
    created_at TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ  NULL,
    created_by BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active  BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS user_otp (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    otp_hash    VARCHAR(255) NOT NULL,
    expires_at  TIMESTAMPTZ  NOT NULL,
    attempts    SMALLINT     NOT NULL DEFAULT 0,
    verified_at TIMESTAMPTZ  NULL,
    user_id     BIGINT       NOT NULL REFERENCES "user" (id),
    otp_type_id BIGINT       NOT NULL REFERENCES otp_type_lk (id),
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    created_by  BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by  BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS company (
    id           BIGSERIAL    PRIMARY KEY,
    urn          UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    name         VARCHAR(255) NOT NULL,
    title        VARCHAR(255) NOT NULL,
    user_type_id BIGINT       NOT NULL REFERENCES user_type_lk (id),
    tenant_id    BIGINT       NOT NULL REFERENCES tenant (id),
    user_id      BIGINT       NOT NULL REFERENCES "user" (id),
    created_at   TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at   TIMESTAMPTZ  NULL,
    created_by   BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by   BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted   BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active    BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS company_profile (
    id                      BIGSERIAL     PRIMARY KEY,
    urn                     UUID          NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    tenant_id               BIGINT        NOT NULL UNIQUE REFERENCES tenant (id),
    legal_name              VARCHAR(255)  NOT NULL,
    display_name            VARCHAR(255)  NOT NULL,
    industry                VARCHAR(100)  NULL,
    company_size            VARCHAR(32)   NULL,
    business_type           VARCHAR(64)   NULL,
    description             TEXT          NULL,
    tax_id                  VARCHAR(64)   NULL,
    website                 VARCHAR(2048) NULL,
    phone                   VARCHAR(32)   NULL,
    support_email           VARCHAR(255)  NULL,
    billing_email           VARCHAR(255)  NULL,
    address_line_1          VARCHAR(255)  NULL,
    address_line_2          VARCHAR(255)  NULL,
    city                    VARCHAR(100)  NULL,
    state                   VARCHAR(100)  NULL,
    zip_code                VARCHAR(20)   NULL,
    country_code            CHAR(2)       NULL,
    logo_url                VARCHAR(2048) NULL,
    logo_text               VARCHAR(12)   NULL,
    accent_color            VARCHAR(7)    NULL,
    email_footer            VARCHAR(500)  NULL,
    timezone                VARCHAR(100)  NULL,
    onboarding_step         SMALLINT      NOT NULL DEFAULT 0,
    onboarding_completed_at TIMESTAMPTZ   NULL,
    created_at              TIMESTAMPTZ   NOT NULL DEFAULT now(),
    updated_at              TIMESTAMPTZ   NULL,
    created_by              BIGINT        NOT NULL REFERENCES "user" (id),
    updated_by              BIGINT        NOT NULL REFERENCES "user" (id),
    is_deleted              BOOLEAN       NOT NULL DEFAULT FALSE,
    is_active               BOOLEAN       NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- Templates (ISignFlowModel)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS template (
    id             BIGSERIAL    PRIMARY KEY,
    urn            UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id    VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id      BIGINT       NOT NULL REFERENCES tenant (id),
    template_name  VARCHAR(255) NOT NULL,
    description    TEXT         NOT NULL,
    document_name  VARCHAR(255) NOT NULL,
    document_data  TEXT         NOT NULL,
    pages          SMALLINT     NOT NULL,
    shared         BOOLEAN      NOT NULL DEFAULT FALSE,
    use_count      INTEGER      NOT NULL DEFAULT 0,
    config         JSONB        NOT NULL DEFAULT '{}'::jsonb,
    created_at     TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at     TIMESTAMPTZ  NULL,
    created_by     BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by     BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted     BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active      BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS template_role (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id VARCHAR(64)  NOT NULL UNIQUE,
    template_id BIGINT       NOT NULL REFERENCES template (id),
    role_name   VARCHAR(255) NOT NULL,
    kind        VARCHAR(16)  NOT NULL,
    sort_order  SMALLINT     NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    created_by  BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by  BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS project (
    id           BIGSERIAL    PRIMARY KEY,
    urn          UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id  VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id    BIGINT       NOT NULL REFERENCES tenant (id),
    project_name VARCHAR(255) NOT NULL,
    description  TEXT         NULL,
    config       JSONB        NOT NULL DEFAULT '{}'::jsonb,
    created_at   TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at   TIMESTAMPTZ  NULL,
    created_by   BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by   BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted   BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active    BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS project_template (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id VARCHAR(64)  NOT NULL UNIQUE,
    project_id  BIGINT       NOT NULL REFERENCES project (id),
    template_id BIGINT       NOT NULL REFERENCES template (id),
    config      JSONB        NOT NULL DEFAULT '{}'::jsonb,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    created_by  BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by  BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE,
    UNIQUE (project_id, template_id)
);

-- ---------------------------------------------------------------------------
-- Envelopes, recipients, fields (ISignFlowModel)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS envelope (
    id                      BIGSERIAL    PRIMARY KEY,
    urn                     UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id             VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id               BIGINT       NOT NULL REFERENCES tenant (id),
    subject                 VARCHAR(500) NOT NULL,
    message                 TEXT         NOT NULL,
    status_id               BIGINT       NOT NULL REFERENCES envelope_status_lk (id),
    document_name           VARCHAR(255) NOT NULL,
    document_data           TEXT         NOT NULL,
    pages                   SMALLINT     NOT NULL,
    signing_order           VARCHAR(16)  NOT NULL,
    reminder_delay_days     SMALLINT     NULL,
    reminder_frequency_days SMALLINT     NULL,
    expires_in_days         SMALLINT     NULL,
    expires_at              TIMESTAMPTZ  NULL,
    template_id             BIGINT       NULL REFERENCES template (id),
    decline_reason          TEXT         NULL,
    void_reason             TEXT         NULL,
    sent_at                 TIMESTAMPTZ  NULL,
    completed_at            TIMESTAMPTZ  NULL,
    created_at              TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at              TIMESTAMPTZ  NULL,
    created_by              BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by              BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted              BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active               BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS recipient (
    id              BIGSERIAL    PRIMARY KEY,
    urn             UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id     VARCHAR(64)  NOT NULL UNIQUE,
    envelope_id     BIGINT       NOT NULL REFERENCES envelope (id),
    token           VARCHAR(64)  NOT NULL UNIQUE,
    recipient_name  VARCHAR(255) NOT NULL,
    email           VARCHAR(255) NOT NULL,
    role            VARCHAR(100) NULL,
    kind            VARCHAR(16)  NOT NULL,
    sort_order      SMALLINT     NOT NULL,
    access_code     VARCHAR(64)  NULL,
    status_id       BIGINT       NOT NULL REFERENCES recipient_status_lk (id),
    viewed_at       TIMESTAMPTZ  NULL,
    signed_at       TIMESTAMPTZ  NULL,
    declined_at     TIMESTAMPTZ  NULL,
    signature_mode  VARCHAR(16)  NULL,
    signature_data  TEXT         NULL,
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ  NULL,
    created_by      BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by      BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted      BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active       BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS field (
    id            BIGSERIAL     PRIMARY KEY,
    urn           UUID          NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id   VARCHAR(64)   NOT NULL UNIQUE,
    envelope_id   BIGINT        NULL REFERENCES envelope (id),
    template_id   BIGINT        NULL REFERENCES template (id),
    recipient_ref VARCHAR(64)   NOT NULL,
    field_type    VARCHAR(16)   NOT NULL,
    page          SMALLINT      NOT NULL,
    x             NUMERIC(6, 3) NOT NULL,
    y             NUMERIC(6, 3) NOT NULL,
    w             NUMERIC(6, 3) NOT NULL,
    h             NUMERIC(6, 3) NOT NULL,
    required      BOOLEAN       NOT NULL DEFAULT TRUE,
    label         VARCHAR(255)  NULL,
    reason        TEXT          NULL,
    value         TEXT          NULL,
    created_at    TIMESTAMPTZ   NOT NULL DEFAULT now(),
    updated_at    TIMESTAMPTZ   NULL,
    created_by    BIGINT        NOT NULL REFERENCES "user" (id),
    updated_by    BIGINT        NOT NULL REFERENCES "user" (id),
    is_deleted    BOOLEAN       NOT NULL DEFAULT FALSE,
    is_active     BOOLEAN       NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- Audit, contacts, team (ISignFlowModel)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS audit_event (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id   BIGINT       NOT NULL REFERENCES tenant (id),
    envelope_id BIGINT       NULL REFERENCES envelope (id),
    event_at    TIMESTAMPTZ  NOT NULL,
    event_type  VARCHAR(64)  NOT NULL,
    actor       VARCHAR(255) NOT NULL,
    ip          INET         NOT NULL,
    detail      TEXT         NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    created_by  BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by  BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS contact (
    id           BIGSERIAL    PRIMARY KEY,
    urn          UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id  VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id    BIGINT       NOT NULL REFERENCES tenant (id),
    contact_name VARCHAR(255) NOT NULL,
    email        VARCHAR(255) NOT NULL,
    company_name VARCHAR(255) NULL,
    title        VARCHAR(255) NULL,
    created_at   TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at   TIMESTAMPTZ  NULL,
    created_by   BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by   BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted   BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active    BOOLEAN      NOT NULL DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS invite (
    id            BIGSERIAL    PRIMARY KEY,
    urn           UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id   VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id     BIGINT       NOT NULL REFERENCES tenant (id),
    contact_id    BIGINT       NULL REFERENCES contact (id),
    envelope_id   BIGINT       NULL REFERENCES envelope (id),
    invite_type_id BIGINT      NOT NULL REFERENCES invite_type_lk (id),
    status_id     BIGINT       NOT NULL REFERENCES invite_status_lk (id),
    invitee_name  VARCHAR(255) NOT NULL,
    email         VARCHAR(255) NOT NULL,
    token         VARCHAR(64)  NOT NULL UNIQUE,
    message       TEXT         NULL,
    sent_at       TIMESTAMPTZ  NOT NULL,
    expires_at    TIMESTAMPTZ  NULL,
    accepted_at   TIMESTAMPTZ  NULL,
    created_at    TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at    TIMESTAMPTZ  NULL,
    created_by    BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by    BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted    BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active     BOOLEAN      NOT NULL DEFAULT TRUE
);


CREATE TABLE IF NOT EXISTS contract (
    id             BIGSERIAL    PRIMARY KEY,
    urn            UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id    VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id      BIGINT       NOT NULL REFERENCES tenant (id),
    employer_id    BIGINT       NOT NULL REFERENCES "user" (id),
    contractor_id  BIGINT       NULL REFERENCES contact (id),
    candidate_id   BIGINT       NULL REFERENCES contact (id),
    invite_id      BIGINT       NOT NULL REFERENCES invite (id),
    envelope_id    BIGINT       NULL REFERENCES envelope (id),
    status_id      BIGINT       NOT NULL REFERENCES contract_status_lk (id),
    title          VARCHAR(255) NOT NULL,
    started_at     TIMESTAMPTZ  NULL,
    ended_at       TIMESTAMPTZ  NULL,
    created_at     TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at     TIMESTAMPTZ  NULL,
    created_by     BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by     BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted     BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active      BOOLEAN      NOT NULL DEFAULT TRUE,
    CONSTRAINT contract_party_chk CHECK (
        contractor_id IS NOT NULL OR candidate_id IS NOT NULL
    )
);

CREATE TABLE IF NOT EXISTS team_member (
    id          BIGSERIAL    PRIMARY KEY,
    urn         UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id   BIGINT       NOT NULL REFERENCES tenant (id),
    member_name VARCHAR(255) NOT NULL,
    email       VARCHAR(255) NOT NULL,
    role        VARCHAR(16)  NOT NULL,
    status_id   BIGINT       NOT NULL REFERENCES team_member_status_lk (id),
    joined_at   TIMESTAMPTZ  NOT NULL,
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ  NULL,
    created_by  BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by  BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted  BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- Webhooks & exports (ISignFlowModel)
-- ---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS webhook_endpoint (
    id          BIGSERIAL     PRIMARY KEY,
    urn         UUID          NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id VARCHAR(64)   NOT NULL UNIQUE,
    tenant_id   BIGINT        NOT NULL REFERENCES tenant (id),
    url         VARCHAR(2048) NOT NULL,
    events      TEXT          NOT NULL,
    active      BOOLEAN       NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMPTZ   NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ   NULL,
    created_by  BIGINT        NOT NULL REFERENCES "user" (id),
    updated_by  BIGINT        NOT NULL REFERENCES "user" (id),
    is_deleted  BOOLEAN       NOT NULL DEFAULT FALSE,
    is_active   BOOLEAN       NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS webhook_delivery (
    id                 BIGSERIAL     PRIMARY KEY,
    urn                UUID          NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id        VARCHAR(64)   NOT NULL UNIQUE,
    tenant_id          BIGINT        NOT NULL REFERENCES tenant (id),
    endpoint_id        BIGINT        NOT NULL REFERENCES webhook_endpoint (id),
    endpoint_url       VARCHAR(2048) NOT NULL,
    event_type_id      BIGINT        NOT NULL REFERENCES event_type_lk (id),
    envelope_id        BIGINT        NULL REFERENCES envelope (id),
    payload_json       TEXT          NOT NULL,
    delivery_status_id BIGINT        NOT NULL REFERENCES webhook_delivery_status_lk (id),
    http_status        SMALLINT      NOT NULL,
    latency_ms         INTEGER       NOT NULL,
    delivered_at       TIMESTAMPTZ   NOT NULL,
    created_at         TIMESTAMPTZ   NOT NULL DEFAULT now(),
    updated_at         TIMESTAMPTZ   NULL,
    created_by         BIGINT        NOT NULL REFERENCES "user" (id),
    updated_by         BIGINT        NOT NULL REFERENCES "user" (id),
    is_deleted         BOOLEAN       NOT NULL DEFAULT FALSE,
    is_active          BOOLEAN       NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS export (
    id           BIGSERIAL    PRIMARY KEY,
    urn          UUID         NOT NULL UNIQUE DEFAULT gen_random_uuid(),
    external_id  VARCHAR(64)  NOT NULL UNIQUE,
    tenant_id    BIGINT       NOT NULL REFERENCES tenant (id),
    kind         VARCHAR(32)  NOT NULL,
    label        VARCHAR(255) NOT NULL,
    envelope_id  BIGINT       NULL REFERENCES envelope (id),
    mime_type_id BIGINT       NOT NULL REFERENCES mime_type_lk (id),
    bytes_data   TEXT         NOT NULL,
    created_at   TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at   TIMESTAMPTZ  NULL,
    created_by   BIGINT       NOT NULL REFERENCES "user" (id),
    updated_by   BIGINT       NOT NULL REFERENCES "user" (id),
    is_deleted   BOOLEAN      NOT NULL DEFAULT FALSE,
    is_active    BOOLEAN      NOT NULL DEFAULT TRUE
);

-- ---------------------------------------------------------------------------
-- Indexes
-- ---------------------------------------------------------------------------

CREATE INDEX IF NOT EXISTS event_type_lk_code_idx ON event_type_lk (code);
CREATE INDEX IF NOT EXISTS mime_type_lk_code_idx ON mime_type_lk (code);
CREATE INDEX IF NOT EXISTS envelope_status_lk_code_idx ON envelope_status_lk (code);
CREATE INDEX IF NOT EXISTS recipient_status_lk_code_idx ON recipient_status_lk (code);
CREATE INDEX IF NOT EXISTS team_member_status_lk_code_idx ON team_member_status_lk (code);
CREATE INDEX IF NOT EXISTS webhook_delivery_status_lk_code_idx ON webhook_delivery_status_lk (code);
CREATE INDEX IF NOT EXISTS user_type_lk_code_idx ON user_type_lk (code);
CREATE INDEX IF NOT EXISTS auth_type_lk_code_idx ON auth_type_lk (code);
CREATE INDEX IF NOT EXISTS mfa_type_lk_code_idx ON mfa_type_lk (code);
CREATE INDEX IF NOT EXISTS otp_type_lk_code_idx ON otp_type_lk (code);

CREATE INDEX IF NOT EXISTS user_email_idx ON "user" (email);
CREATE INDEX IF NOT EXISTS user_auth_type_idx ON "user" (auth_type_id);
CREATE INDEX IF NOT EXISTS user_mfa_type_idx ON "user" (mfa_type_id);
CREATE INDEX IF NOT EXISTS tenant_subdomain_idx ON tenant (subdomain);
CREATE INDEX IF NOT EXISTS tenant_profile_tenant_idx ON tenant_profile (tenant_id);
CREATE INDEX IF NOT EXISTS user_recovery_code_user_idx ON user_recovery_code (user_id);
CREATE INDEX IF NOT EXISTS user_otp_user_idx ON user_otp (user_id);
CREATE INDEX IF NOT EXISTS company_tenant_idx ON company (tenant_id);
CREATE INDEX IF NOT EXISTS company_user_idx ON company (user_id);
CREATE INDEX IF NOT EXISTS company_user_type_idx ON company (user_type_id);
CREATE INDEX IF NOT EXISTS company_profile_tenant_idx ON company_profile (tenant_id);
CREATE INDEX IF NOT EXISTS company_profile_display_name_idx ON company_profile (display_name);

CREATE INDEX IF NOT EXISTS template_tenant_idx ON template (tenant_id);
CREATE INDEX IF NOT EXISTS template_role_template_idx ON template_role (template_id);
CREATE INDEX IF NOT EXISTS project_tenant_idx ON project (tenant_id);
CREATE INDEX IF NOT EXISTS project_template_project_idx ON project_template (project_id);
CREATE INDEX IF NOT EXISTS project_template_template_idx ON project_template (template_id);
CREATE INDEX IF NOT EXISTS envelope_tenant_idx ON envelope (tenant_id);
CREATE INDEX IF NOT EXISTS envelope_template_idx ON envelope (template_id);
CREATE INDEX IF NOT EXISTS envelope_status_idx ON envelope (status_id);
CREATE INDEX IF NOT EXISTS recipient_envelope_idx ON recipient (envelope_id);
CREATE INDEX IF NOT EXISTS recipient_token_idx ON recipient (token);
CREATE INDEX IF NOT EXISTS recipient_status_idx ON recipient (status_id);
CREATE INDEX IF NOT EXISTS field_envelope_idx ON field (envelope_id);
CREATE INDEX IF NOT EXISTS field_template_idx ON field (template_id);

CREATE INDEX IF NOT EXISTS audit_event_tenant_idx ON audit_event (tenant_id);
CREATE INDEX IF NOT EXISTS audit_event_envelope_idx ON audit_event (envelope_id);
CREATE INDEX IF NOT EXISTS contact_tenant_idx ON contact (tenant_id);
CREATE INDEX IF NOT EXISTS contact_tenant_email_idx ON contact (tenant_id, email);
CREATE INDEX IF NOT EXISTS invite_status_lk_code_idx ON invite_status_lk (code);
CREATE INDEX IF NOT EXISTS invite_type_lk_code_idx ON invite_type_lk (code);
CREATE INDEX IF NOT EXISTS invite_tenant_idx ON invite (tenant_id);
CREATE INDEX IF NOT EXISTS invite_contact_idx ON invite (contact_id);
CREATE INDEX IF NOT EXISTS invite_envelope_idx ON invite (envelope_id);
CREATE INDEX IF NOT EXISTS invite_status_idx ON invite (status_id);
CREATE INDEX IF NOT EXISTS invite_type_idx ON invite (invite_type_id);
CREATE INDEX IF NOT EXISTS invite_email_idx ON invite (tenant_id, email);
CREATE INDEX IF NOT EXISTS invite_token_idx ON invite (token);
CREATE INDEX IF NOT EXISTS contract_status_lk_code_idx ON contract_status_lk (code);
CREATE INDEX IF NOT EXISTS contract_tenant_idx ON contract (tenant_id);
CREATE INDEX IF NOT EXISTS contract_employer_idx ON contract (employer_id);
CREATE INDEX IF NOT EXISTS contract_contractor_idx ON contract (contractor_id);
CREATE INDEX IF NOT EXISTS contract_candidate_idx ON contract (candidate_id);
CREATE INDEX IF NOT EXISTS contract_invite_idx ON contract (invite_id);
CREATE INDEX IF NOT EXISTS contract_envelope_idx ON contract (envelope_id);
CREATE INDEX IF NOT EXISTS contract_status_idx ON contract (status_id);
CREATE INDEX IF NOT EXISTS team_member_tenant_idx ON team_member (tenant_id);
CREATE INDEX IF NOT EXISTS team_member_status_idx ON team_member (status_id);

CREATE INDEX IF NOT EXISTS webhook_endpoint_tenant_idx ON webhook_endpoint (tenant_id);
CREATE INDEX IF NOT EXISTS webhook_delivery_tenant_idx ON webhook_delivery (tenant_id);
CREATE INDEX IF NOT EXISTS webhook_delivery_endpoint_idx ON webhook_delivery (endpoint_id);
CREATE INDEX IF NOT EXISTS webhook_delivery_event_type_idx ON webhook_delivery (event_type_id);
CREATE INDEX IF NOT EXISTS webhook_delivery_status_idx ON webhook_delivery (delivery_status_id);
CREATE INDEX IF NOT EXISTS export_mime_type_idx ON export (mime_type_id);
CREATE INDEX IF NOT EXISTS export_tenant_idx ON export (tenant_id);
