-- Migration: SignFlow lookup seed data
-- Created at: 2026-08-22
-- Run after: 20260822000001_schema.sql

-- ---------------------------------------------------------------------------
-- Status / reference lookups
-- ---------------------------------------------------------------------------

INSERT INTO event_type_lk (code, label, description) VALUES
    ('envelope.sent',      'Envelope Sent',      'Envelope was sent to recipients'),
    ('envelope.viewed',    'Envelope Viewed',    'Envelope was opened by a recipient'),
    ('envelope.signed',    'Envelope Signed',    'A recipient completed signing'),
    ('envelope.completed', 'Envelope Completed', 'All required signatures collected'),
    ('envelope.declined',  'Envelope Declined',  'Envelope was declined by a recipient'),
    ('envelope.voided',    'Envelope Voided',    'Envelope was voided by the sender')
ON CONFLICT (code) DO NOTHING;

INSERT INTO mime_type_lk (code, label, description) VALUES
    ('application/pdf', 'PDF Document', 'Portable Document Format'),
    ('text/csv',        'CSV Document', 'Comma-separated values')
ON CONFLICT (code) DO NOTHING;

INSERT INTO envelope_status_lk (code, label, description) VALUES
    ('draft',     'Draft',     'Envelope is being prepared'),
    ('sent',      'Sent',      'Envelope has been sent to recipients'),
    ('viewed',    'Viewed',    'Envelope has been opened by a recipient'),
    ('completed', 'Completed', 'All required signatures are collected'),
    ('declined',  'Declined',  'Envelope was declined by a recipient'),
    ('voided',    'Voided',    'Envelope was voided by the sender')
ON CONFLICT (code) DO NOTHING;

INSERT INTO recipient_status_lk (code, label, description) VALUES
    ('waiting',  'Waiting',  'Recipient is waiting for their turn'),
    ('sent',     'Sent',     'Signing invitation sent to recipient'),
    ('viewed',   'Viewed',   'Recipient opened the signing session'),
    ('signed',   'Signed',   'Recipient completed signing'),
    ('declined', 'Declined', 'Recipient declined to sign')
ON CONFLICT (code) DO NOTHING;

INSERT INTO team_member_status_lk (code, label, description) VALUES
    ('active',  'Active',  'Team member has joined the workspace'),
    ('invited', 'Invited', 'Team member has been invited but not yet joined')
ON CONFLICT (code) DO NOTHING;

INSERT INTO invite_status_lk (code, label, description) VALUES
    ('pending',   'Pending',   'Invite created but not yet sent'),
    ('sent',      'Sent',      'Invite has been sent to the invitee'),
    ('accepted',  'Accepted',  'Invitee accepted the invite'),
    ('declined',  'Declined',  'Invitee declined the invite'),
    ('expired',   'Expired',   'Invite expired without a response'),
    ('revoked',   'Revoked',   'Invite was revoked by the sender')
ON CONFLICT (code) DO NOTHING;

INSERT INTO invite_type_lk (code, label, description) VALUES
    ('candidate',  'Candidate',  'Invite sent to a candidate'),
    ('contractor', 'Contractor', 'Invite sent to a contractor'),
    ('contact',    'Contact',    'Invite sent to an address-book contact')
ON CONFLICT (code) DO NOTHING;

INSERT INTO contract_status_lk (code, label, description) VALUES
    ('draft',      'Draft',      'Contract is being prepared'),
    ('pending',    'Pending',    'Contract awaiting acceptance or signature'),
    ('active',     'Active',     'Contract is in effect'),
    ('completed',  'Completed',  'Contract term completed'),
    ('terminated', 'Terminated', 'Contract was terminated early'),
    ('voided',     'Voided',     'Contract was voided')
ON CONFLICT (code) DO NOTHING;


INSERT INTO webhook_delivery_status_lk (code, label, description) VALUES
    ('delivered', 'Delivered', 'Webhook was delivered successfully'),
    ('failed',    'Failed',    'Webhook delivery failed')
ON CONFLICT (code) DO NOTHING;

-- ---------------------------------------------------------------------------
-- Identity lookups
-- ---------------------------------------------------------------------------

INSERT INTO user_type_lk (code, description) VALUES
    ('OWNER',  'Workspace owner with full control'),
    ('ADMIN',  'Administrator who can manage team and settings'),
    ('SENDER', 'Can create and send signing envelopes'),
    ('VIEWER', 'Read-only access to envelopes and audit')
ON CONFLICT (code) DO NOTHING;

INSERT INTO auth_type_lk (code, description) VALUES
    ('PASSWORD',       'Standard password authentication'),
    ('OAUTH_GOOGLE',   'Google OAuth 2.0 single sign-on'),
    ('OAUTH_GITHUB',   'GitHub OAuth 2.0 single sign-on'),
    ('OAUTH_LINKEDIN', 'LinkedIn OAuth 2.0 single sign-on'),
    ('SAML_SSO',       'SAML 2.0 enterprise single sign-on')
ON CONFLICT (code) DO NOTHING;

INSERT INTO mfa_type_lk (code, description) VALUES
    ('TOTP',  'Time-based one-time password authenticator app'),
    ('SMS',   'SMS one-time passcode'),
    ('EMAIL', 'Email one-time passcode')
ON CONFLICT (code) DO NOTHING;

INSERT INTO otp_type_lk (code, description) VALUES
    ('LOGIN',            'Multi-factor login passcode'),
    ('PASSWORD_RESET',   'Account password reset verification passcode'),
    ('MFA_VERIFICATION', 'Security MFA challenge passcode')
ON CONFLICT (code) DO NOTHING;
