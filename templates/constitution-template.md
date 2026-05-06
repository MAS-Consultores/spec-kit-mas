# [PROJECT_NAME] Constitution

## Core Principles

### I. Security and Access Control
- Every feature MUST identify its actors, permissions, sensitive data, privacy
  obligations, and abuse or failure paths before implementation begins.
- Access to data and privileged actions MUST be denied by default and granted
  explicitly according to business role and operational responsibility.
- Authentication, access control, credential handling, password policy,
  encryption, and secure transport requirements MUST be defined whenever
  applicable to the feature.
- Secrets, credentials, and personal data MUST be protected in transit, at rest,
  and in logs; production data exposure in non-production environments is
  prohibited unless explicitly approved and sanitized.
- Authorization MUST be enforced on the server for every entrypoint (including
  APIs, background jobs, and CLI); client-side or UI-only checks are never
  sufficient.
- Multi-factor authentication SHOULD be required for administrative or
  high-privilege roles where technically feasible; password storage MUST use
  adaptive hashing and MUST NOT use deprecated algorithms such as md5 or sha1
  for credentials.
- Sessions and cookies MUST use TLS, `Secure`, `HttpOnly`, and appropriate
  `SameSite`; sessions MUST be invalidated or rotated when privilege level
  changes.
- Untrusted input MUST be validated on the server; output MUST be encoded in
  context; data access MUST use parameterized queries or ORM bindings; state-
  changing browser requests MUST be protected against CSRF where applicable.
- Production environments MUST apply baseline HTTP hardening (for example CSP,
  HSTS, `X-Content-Type-Options`, and a coherent `Referrer-Policy`) unless a
  formal exception is recorded with compensating controls.
- Cryptography MUST use maintained libraries and current algorithms; custom
  cryptography is prohibited; key material MUST stay out of source control and
  MUST be rotatable after exposure.
- Dependencies and third-party components MUST be tracked and scanned for known
  vulnerabilities; high-severity findings MUST be remediated or formally risk-
  accepted before production promotion.
- Security-relevant events and permission-sensitive mutations MUST be logged and
  auditable without recording credentials or unnecessary personal data in logs.
- Secure delivery practices MUST include lightweight threat review for high-risk
  changes, peer review of security-sensitive paths, and evidence of validation
  before release when security, integrity, or recovery readiness is in scope.
- Stack-agnostic security expectations live in `.specify/memory/security-
  standard.md` (initialized from the bundled template). When a stack is
  registered, `.specify/context/stack.md` MUST include **Security Controls**,
  **Security Pitfalls**, and **Security Evidence** sections populated from the
  approved stack profile; plans and reviews MUST align with both documents.

### II. Traceability and Auditability
- Requirements, decisions, code changes, data migrations, and releases MUST be
  traceable from specification through deployment.
- Business-critical, permission-sensitive, and data-changing operations MUST emit
  audit evidence sufficient to reconstruct who acted, on what, and when.
- Hotfixes, manual interventions, and emergency changes MUST leave the same
  reviewable record as standard delivery work.

### III. Explicit Data Models and Integrity
- Core entities, relationships, lifecycle states, validation rules, and ownership
  boundaries MUST be modeled explicitly before implementation.
- Persistent changes MUST be backed by an explicit data model, including an ER
  view and data dictionary or equivalent artifact suitable for the chosen stack.
- Data changes MUST preserve referential integrity, deterministic business rules,
  and safe retry behavior where failures or duplicate execution are plausible.
- Irreversible or high-impact data changes MUST include migration, recovery, and
  stakeholder communication planning before release.

### IV. Operational Performance and Reliability
- Every feature MUST declare measurable operational expectations such as response
  time, throughput, latency sensitivity, or batch-processing limits.
- Systems MUST provide actionable logging, diagnostics, and failure visibility so
  support and engineering teams can isolate incidents without ad hoc code changes.
- Integrations, jobs, and high-volume read or write paths MUST be designed for
  bounded resource usage, graceful degradation, and predictable recovery.

### V. Administrative Usability
- Administrative and back-office workflows are first-class product surfaces and
  MUST be designed for clarity, efficiency, and safe error recovery.
- Operational users MUST be able to understand record state, recent changes, and
  next available actions without requiring direct database or source-code access.
- Data-heavy screens and operational listings MUST support navigable, bounded
  result sets and predictable filtering or pagination behavior.
- Bulk actions, status transitions, and approval flows MUST include safeguards
  proportionate to their business impact.

### VI. Standardization and Stack-Constrained Design
- Solutions MUST fit an approved company stack unless an explicit exception is
  approved before implementation.
- Approved stacks are limited to: CakePHP 2.x + MySQL, Moodle 5 Plugin, Moodle 5
  Portal, and Laravel + Inertia + React.
- Architecture, naming, project structure, and delivery patterns MUST align with
  the chosen stack's approved conventions and shared company standards.
- Stack-specific implementation rules belong in templates, plans, and supporting
  standards; this constitution remains principle-driven and stack-agnostic.

### VII. Maintainability and Standardization
- Codebases MUST favor shared patterns, reusable components, disciplined schema
  handling, and clear module boundaries over ad hoc feature-by-feature design.
- Repeated form, validation, and administrative interaction patterns MUST be
  standardized through reusable project-level components or equivalents.
- Infrastructure, runtime dependencies, and environment assumptions MUST be
  explicit, reproducible, and appropriate for the selected approved stack.

### VIII. Controlled Delivery and Rollback Readiness
- Each release MUST be deployable in controlled increments with validated rollback,
  mitigation, or containment paths proportional to its operational risk.
- Database changes, configuration changes, and third-party dependency changes MUST
  be reversible or explicitly risk-accepted before release.
- Delivery flow MUST preserve traceability: one branch per functionality, clear
  incremental commits, QA validation before release, and promotion through
  testing before master except for justified hotfixes.
- Production deployment MUST include controlled execution, rollback readiness, and
  post-release validation of critical operational behavior.
- Production promotion MUST be blocked when security, data integrity,
  observability, or recovery readiness cannot be demonstrated.

## Delivery Requirements

- Specifications MUST cover user journeys, administrative workflows,
  permissions, key entities, integration points, and non-functional expectations
  relevant to the requested change.
- Implementation plans MUST document the selected approved stack, affected data
  structures, audit events, performance constraints, validation strategy, and
  deployment and rollback approach.
- Implementation plans MUST also capture security controls, privacy handling,
  data-model artifacts, branch and release strategy, and operational validation
  expectations for the change.
- Task plans MUST include work for verification, observability or auditability,
  administrative experience, and release readiness whenever those concerns are
  materially affected.
- Deviations from approved patterns MUST be recorded as explicit exceptions with
  rationale, impact, and approver.

## Governance

- This constitution overrides local preferences and lower-level guidance whenever
  they conflict.
- Constitution compliance MUST be checked during specification, planning, review,
  and release approval; unresolved violations block progression.
- Amendments require documented rationale, review of impacted templates and
  workflow artifacts, and approval by the maintainers of this internal
  distribution.
- Versioning follows semantic intent: MAJOR for incompatible governance changes,
  MINOR for new principles or materially expanded obligations, and PATCH for
  clarifications that do not alter enforcement.

**Version**: [CONSTITUTION_VERSION] | **Ratified**: [RATIFICATION_DATE] | **Last Amended**: [LAST_AMENDED_DATE]
