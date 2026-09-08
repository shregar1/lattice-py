"""OpenAPI tag constants — resource tags and action-verb tags used across the platform."""

from typing import Final
from .abstraction import IAPIConstant


class APITag(IAPIConstant):

    """OpenAPI and documentation tags."""

    # Health tags
    HEALTH: Final[str] = "HEALTH"
    HEALTH_CHECK: Final[str] = "HEALTH_CHECK"
    DB_HEALTH: Final[str] = "HEALTH_DB"
    LIVELINESS_HEALTH: Final[str] = "HEALTH_LIVELINESS"
    READINESS_HEALTH: Final[str] = "HEALTH_READINESS"

    # Resource tags
    APPLICATIONS: Final[str] = "APPLICATIONS"
    CANDIDATES: Final[str] = "CANDIDATES"
    JOBS: Final[str] = "JOBS"
    INTERVIEWS: Final[str] = "INTERVIEWS"
    OFFERS: Final[str] = "OFFERS"
    REQUISITIONS: Final[str] = "REQUISITIONS"
    SCORECARDS: Final[str] = "SCORECARDS"
    TENANTS: Final[str] = "TENANTS"
    USERS: Final[str] = "USERS"
    CAMPAIGNS: Final[str] = "CAMPAIGNS"
    AUTOMATION: Final[str] = "AUTOMATION"
    SOURCING: Final[str] = "SOURCING"
    AI_SCREENING: Final[str] = "AI_SCREENING"
    ANALYTICS: Final[str] = "ANALYTICS"
    SCHEDULING: Final[str] = "SCHEDULING"

    # CRUD tags
    CREATE: Final[str] = "CREATE"
    READ: Final[str] = "READ"
    UPDATE: Final[str] = "UPDATE"
    DELETE: Final[str] = "DELETE"
    LIST: Final[str] = "LIST"
    FETCH: Final[str] = "FETCH"
    FETCH_ALL: Final[str] = "FETCH_ALL"
    FETCH_ONE: Final[str] = "FETCH_ONE"
    GET: Final[str] = "GET"
    POST: Final[str] = "POST"
    PUT: Final[str] = "PUT"
    PATCH: Final[str] = "PATCH"
    FILTER: Final[str] = "FILTER"
    SEARCH: Final[str] = "SEARCH"
    QUERY: Final[str] = "QUERY"
    FIND: Final[str] = "FIND"
    LOOKUP: Final[str] = "LOOKUP"

    # Bulk/batch CRUD tags
    BULK_CREATE: Final[str] = "BULK_CREATE"
    BULK_UPDATE: Final[str] = "BULK_UPDATE"
    BULK_DELETE: Final[str] = "BULK_DELETE"
    BULK_IMPORT: Final[str] = "BULK_IMPORT"
    BULK_EXPORT: Final[str] = "BULK_EXPORT"
    IMPORT_: Final[str] = "IMPORT"
    EXPORT: Final[str] = "EXPORT"
    UPLOAD: Final[str] = "UPLOAD"
    DOWNLOAD: Final[str] = "DOWNLOAD"

    # Lifecycle / state transitions
    ARCHIVE: Final[str] = "ARCHIVE"
    RESTORE: Final[str] = "RESTORE"
    ACTIVATE: Final[str] = "ACTIVATE"
    DEACTIVATE: Final[str] = "DEACTIVATE"
    ENABLE: Final[str] = "ENABLE"
    DISABLE: Final[str] = "DISABLE"
    LOCK: Final[str] = "LOCK"
    UNLOCK: Final[str] = "UNLOCK"
    PUBLISH: Final[str] = "PUBLISH"
    UNPUBLISH: Final[str] = "UNPUBLISH"
    DRAFT: Final[str] = "DRAFT"
    SUBMIT: Final[str] = "SUBMIT"
    WITHDRAW: Final[str] = "WITHDRAW"
    CANCEL: Final[str] = "CANCEL"
    RESCHEDULE: Final[str] = "RESCHEDULE"
    CLOSE: Final[str] = "CLOSE"
    REOPEN: Final[str] = "REOPEN"
    COMPLETE: Final[str] = "COMPLETE"
    REJECT: Final[str] = "REJECT"
    APPROVE: Final[str] = "APPROVE"
    DECLINE: Final[str] = "DECLINE"
    ACCEPT: Final[str] = "ACCEPT"
    ACK: Final[str] = "ACK"
    ACKNOWLEDGE: Final[str] = "ACKNOWLEDGE"
    ESCALATE: Final[str] = "ESCALATE"
    ASSIGN: Final[str] = "ASSIGN"
    UNASSIGN: Final[str] = "UNASSIGN"
    REASSIGN: Final[str] = "REASSIGN"
    TRANSFER: Final[str] = "TRANSFER"
    PROMOTE: Final[str] = "PROMOTE"
    DEMOTE: Final[str] = "DEMOTE"
    MERGE: Final[str] = "MERGE"
    SPLIT: Final[str] = "SPLIT"
    CLONE: Final[str] = "CLONE"
    DUPLICATE: Final[str] = "DUPLICATE"
    MOVE: Final[str] = "MOVE"
    COPY: Final[str] = "COPY"
    RENAME: Final[str] = "RENAME"
    ARCHIVE_BULK: Final[str] = "ARCHIVE_BULK"
    RESTORE_BULK: Final[str] = "RESTORE_BULK"

    # Workflow / domain actions
    RATE: Final[str] = "RATE"
    SCORE: Final[str] = "SCORE"
    EVALUATE: Final[str] = "EVALUATE"
    ASSESS: Final[str] = "ASSESS"
    SCREEN: Final[str] = "SCREEN"
    RUN: Final[str] = "RUN"
    EXECUTE: Final[str] = "EXECUTE"
    TRIGGER: Final[str] = "TRIGGER"
    PROCESS: Final[str] = "PROCESS"
    RESOLVE: Final[str] = "RESOLVE"
    APPLY: Final[str] = "APPLY"
    MATCH: Final[str] = "MATCH"
    DEDUPLICATE: Final[str] = "DEDUPLICATE"
    REDISCOVER: Final[str] = "REDISCOVER"
    ADVANCE: Final[str] = "ADVANCE"
    ENROLL: Final[str] = "ENROLL"
    BOOK: Final[str] = "BOOK"
    INVITE: Final[str] = "INVITE"
    SCHEDULE: Final[str] = "SCHEDULE"
    CALENDAR_SYNC: Final[str] = "CALENDAR_SYNC"
    SOLVE: Final[str] = "SOLVE"
    AUTO_SCHEDULE: Final[str] = "AUTO_SCHEDULE"
    VERIFY: Final[str] = "VERIFY"
    VALIDATE: Final[str] = "VALIDATE"
    AUTHENTICATE: Final[str] = "AUTHENTICATE"
    AUTHORIZE: Final[str] = "AUTHORIZE"
    LOGIN: Final[str] = "LOGIN"
    LOGOUT: Final[str] = "LOGOUT"
    REFRESH: Final[str] = "REFRESH"
    ROTATE: Final[str] = "ROTATE"
    RESEND: Final[str] = "RESEND"
    REQUEST: Final[str] = "REQUEST"
    RESET: Final[str] = "RESET"
    CHANGE: Final[str] = "CHANGE"
    UPDATE_STATUS: Final[str] = "UPDATE_STATUS"
    UPDATE_RATING: Final[str] = "UPDATE_RATING"
    UPDATE_STAGE: Final[str] = "UPDATE_STAGE"
    UPDATE_DECISION: Final[str] = "UPDATE_DECISION"
    MOVE_STAGE: Final[str] = "MOVE_STAGE"
    RATE_APPLICATION: Final[str] = "RATE_APPLICATION"

    # Notifications / communication
    NOTIFY: Final[str] = "NOTIFY"
    SEND: Final[str] = "SEND"
    BROADCAST: Final[str] = "BROADCAST"
    MESSAGE: Final[str] = "MESSAGE"

    # File / media
    UPLOAD_FILE: Final[str] = "UPLOAD_FILE"
    DOWNLOAD_FILE: Final[str] = "DOWNLOAD_FILE"
    ATTACH: Final[str] = "ATTACH"
    DETACH: Final[str] = "DETACH"
    SIGN: Final[str] = "SIGN"

    # Async / background
    ENQUEUE: Final[str] = "ENQUEUE"
    DEQUEUE: Final[str] = "DEQUEUE"
    SCHEDULE_JOB: Final[str] = "SCHEDULE_JOB"
    CANCEL_JOB: Final[str] = "CANCEL_JOB"
    POLL: Final[str] = "POLL"
    SUBSCRIBE: Final[str] = "SUBSCRIBE"
    UNSUBSCRIBE: Final[str] = "UNSUBSCRIBE"

    # Read-only / introspection
    READINESS: Final[str] = "READINESS"
    LIVENESS: Final[str] = "LIVENESS"
    STATUS: Final[str] = "STATUS"
    METRICS: Final[str] = "METRICS"
    PING: Final[str] = "PING"

    # Aggregations / analytics
    AGGREGATE: Final[str] = "AGGREGATE"
    SUMMARIZE: Final[str] = "SUMMARIZE"
    ANALYZE: Final[str] = "ANALYZE"
    REPORT: Final[str] = "REPORT"
    EXPORT_REPORT: Final[str] = "EXPORT_REPORT"
    DASHBOARD: Final[str] = "DASHBOARD"

    # Permissions / RBAC
    GRANT: Final[str] = "GRANT"
    REVOKE: Final[str] = "REVOKE"
    CHECK_PERMISSION: Final[str] = "CHECK_PERMISSION"

    # Migrations / sync
    MIGRATE: Final[str] = "MIGRATE"
    SYNC: Final[str] = "SYNC"
    REINDEX: Final[str] = "REINDEX"
    RECONCILE: Final[str] = "RECONCILE"

    # Soft operations
    PREVIEW: Final[str] = "PREVIEW"
    SIMULATE: Final[str] = "SIMULATE"
    DRY_RUN: Final[str] = "DRY_RUN"

    # Bulk read variants
    EXPORT_ALL: Final[str] = "EXPORT_ALL"
    LIST_ALL: Final[str] = "LIST_ALL"

    # Search variants
    FULL_TEXT_SEARCH: Final[str] = "FULL_TEXT_SEARCH"
    ADVANCED_SEARCH: Final[str] = "ADVANCED_SEARCH"
    FACETED_SEARCH: Final[str] = "FACETED_SEARCH"

    # Validation / preview
    VALIDATE_BODY: Final[str] = "VALIDATE_BODY"
    PREVIEW_CREATE: Final[str] = "PREVIEW_CREATE"
    PREVIEW_UPDATE: Final[str] = "PREVIEW_UPDATE"

    # Duplicate detection
    FIND_DUPLICATES: Final[str] = "FIND_DUPLICATES"

    # Versioning
    LIST_VERSIONS: Final[str] = "LIST_VERSIONS"
    REVERT: Final[str] = "REVERT"

    # Tags / categorization
    ADD_TAG: Final[str] = "ADD_TAG"
    REMOVE_TAG: Final[str] = "REMOVE_TAG"
    SET_TAGS: Final[str] = "SET_TAGS"

    # Notes / comments
    ADD_NOTE: Final[str] = "ADD_NOTE"
    REMOVE_NOTE: Final[str] = "REMOVE_NOTE"
    LIST_NOTES: Final[str] = "LIST_NOTES"

    # Attachments / files
    LIST_ATTACHMENTS: Final[str] = "LIST_ATTACHMENTS"
    UPLOAD_ATTACHMENT: Final[str] = "UPLOAD_ATTACHMENT"
    DELETE_ATTACHMENT: Final[str] = "DELETE_ATTACHMENT"

    # Relations
    LINK: Final[str] = "LINK"
    UNLINK: Final[str] = "UNLINK"
    ADD_RELATION: Final[str] = "ADD_RELATION"
    REMOVE_RELATION: Final[str] = "REMOVE_RELATION"

    # History / audit
    LIST_HISTORY: Final[str] = "LIST_HISTORY"
    LIST_AUDIT: Final[str] = "LIST_AUDIT"
    LIST_CHANGES: Final[str] = "LIST_CHANGES"

    # Bulk operations beyond CRUD
    RESTORE_BULK_DELETED: Final[str] = "RESTORE_BULK_DELETED"
    PERMANENT_DELETE: Final[str] = "PERMANENT_DELETE"
    PURGE: Final[str] = "PURGE"

    # Scheduling
    AVAILABILITY: Final[str] = "AVAILABILITY"
    BOOK_AVAILABILITY: Final[str] = "BOOK_AVAILABILITY"
    SOLVE_AVAILABILITY: Final[str] = "SOLVE_AVAILABILITY"

    # Voting / polls
    VOTE: Final[str] = "VOTE"
    POLL_CREATE: Final[str] = "POLL_CREATE"
    POLL_CLOSE: Final[str] = "POLL_CLOSE"

    # Sharing / collaboration
    SHARE: Final[str] = "SHARE"
    UNSHARE: Final[str] = "UNSHARE"
    COLLABORATE: Final[str] = "COLLABORATE"

    # Impersonation / delegation
    IMPERSONATE: Final[str] = "IMPERSONATE"
    DELEGATE: Final[str] = "DELEGATE"

    # Audit
    LIST_LOGS: Final[str] = "LIST_LOGS"
    LIST_EVENTS: Final[str] = "LIST_EVENTS"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "APITag"
