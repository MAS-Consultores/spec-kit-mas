# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See
`.specify/templates/plan-template.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement, selected approach, and
delivery-sensitive context]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the concrete
  technical details for the feature. Unknowns must be marked as
  NEEDS CLARIFICATION and resolved in research.md before implementation.
-->

**Registered Project Stack**: [Read from `.specify/context/stack.md`; if absent, state that no stack is registered yet]<br>
**Selected Approved Stack**: [Normally matches the registered stack; if not, explain the exception clearly]<br>
**Stack Fit / Justification**: [Why this feature fits the registered stack and existing product context]<br>
**Poor-Fit / Strain Signals**: [Any aspects of the feature that pull against the registered stack, and whether they require an exception]<br>
**Deviation / Exception Needed**: [None or explicit exception with rationale, scope, and approver path]<br>
**Stack Profile Constraints**: [Relevant constraints pulled from `.specify/context/stack.md`]<br>
**Stack-Specific Risks**: [Relevant risks pulled from `.specify/context/stack.md`]<br>
**Stack Security Controls**: [Summarize applicable bullets from `## Security Controls` in `.specify/context/stack.md`; if no stack file, state N/A]<br>
**Stack Security Pitfalls to Mitigate**: [List relevant items from `## Security Pitfalls` in `stack.md` and how this work avoids them]<br>
**Stack Security Evidence**: [List evidence you will produce per `## Security Evidence` in `stack.md`]<br>
**Expected Stack Artifacts**: [Artifacts this feature should produce for the selected stack]<br>
**Language / Runtime**: [e.g., PHP 8.2, Node 20, MySQL 8 or NEEDS CLARIFICATION]  
**Primary Dependencies**: [frameworks, packages, platform modules or NEEDS CLARIFICATION]  
**Storage / Persistence**: [existing schema, new tables, files, N/A or NEEDS CLARIFICATION]  
**Testing / QA**: [unit/integration/manual/QA flow or NEEDS CLARIFICATION]  
**Target Environment**: [e.g., shared hosting, Docker/Nginx/MySQL, RDS-backed environment, Moodle instance, N/A]  
**Project Type**: [portal, plugin, internal admin tool, LMS extension, web app or NEEDS CLARIFICATION]  
**Performance Goals**: [domain-specific targets or N/A]  
**Operational Constraints**: [latency, batch windows, legacy compatibility, uptime, export size, N/A]  
**Scale / Scope**: [users, records, institutions, reports, courses, N/A]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Stack Alignment**: Selected approach uses an approved stack or records a
  justified exception.
- **Security and Privacy**: Plan identifies whether the work touches
  authentication, authorization, sensitive data, credentials, encryption, or
  secure transport requirements; it MUST reference `.specify/memory/security-
  standard.md` for applicable MUST items and MUST map the feature to **Security
  Controls**, **Security Pitfalls**, and **Security Evidence** in
  `.specify/context/stack.md` when a stack is registered (or document N/A and
  justify if `stack.md` is absent).
- **Data Modeling and Integrity**: Plan states whether the work changes core
  domain data, schema, migrations, seeders, imports, exports, or persistence
  rules, and whether data-model artifacts are required.
- **Traceability and Auditability**: Plan identifies required audit trails,
  operational logs, branch strategy, and release traceability expectations.
- **Administrative Usability**: Plan states whether the work affects
  admin-facing workflows, back-office operations, large listings, reports, or
  exports, including pagination or bulk-action implications where relevant.
- **Reliability and Operations**: Plan documents operational expectations,
  deployment-sensitive components, rollback-sensitive areas, and validation of
  post-release behavior.
- **Maintainability and Standardization**: Plan identifies reusable component,
  schema, structure, or environment conventions that must be preserved.

## Impact Assessment

**Touches Authentication / Authorization** (including new roles, policies,
public endpoints, or session changes): [Yes/No + impact summary]  
**Touches Cryptography or Secret Material** (keys, tokens, new encryption,
password flows): [Yes/No + summary]  
**Touches Sensitive Data / Privacy**: [Yes/No + data classes and handling summary]  
**Touches Core Domain Data**: [Yes/No + entities / records affected]  
**Touches Large Listings / Reports / Exports**: [Yes/No + pagination / batching implications]  
**Touches Admin-Facing Workflows**: [Yes/No + affected operational users / flows]  
**Touches Deployment-Sensitive Components**: [Yes/No + environments / dependencies affected]  
**Touches Rollback-Sensitive Areas**: [Yes/No + why rollback is delicate]

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
|-- plan.md              # This file (/speckit.plan command output)
|-- research.md          # Phase 0 output (/speckit.plan command)
|-- data-model.md        # Phase 1 output (/speckit.plan command)
|-- quickstart.md        # Phase 1 output (/speckit.plan command)
|-- contracts/           # Phase 1 output (/speckit.plan command)
`-- tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths. The delivered plan must not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Legacy/monolithic application
app/
|-- Controller/
|-- Model/
|-- View/
`-- Console/

tests/
|-- integration/
`-- unit/

# [REMOVE IF UNUSED] Option 2: Structured web application
backend/
|-- app/ or src/
|-- database/
|-- routes/ or config/
`-- tests/

frontend/
|-- src/
|   |-- components/
|   |-- pages/
|   `-- services/
`-- tests/

# [REMOVE IF UNUSED] Option 3: Moodle extension / portal structure
plugin_or_portal/
|-- classes/ or lib/
|-- db/
|-- lang/
|-- templates/ or pages/
`-- tests/
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Implementation Considerations

### Security and Access Control

[Summarize applicable authentication, authorization, password, encryption,
secure-channel, and privacy requirements. Use "N/A" only when clearly
inapplicable.]

Explicitly tie this section to:

- `.specify/memory/security-standard.md` — list which numbered sections (1–16)
  apply and which MUST items you satisfy.
- `.specify/context/stack.md` — quote or summarize the relevant bullets under
  **Security Controls**, how you mitigate **Security Pitfalls**, and what
  **Security Evidence** you will attach (tests, config, audit events).
- For work on non-approved stacks (for example legacy Moodle 3), reference
  `.specify/memory/legacy/moodle3-security-template.md` and record the approved
  exception in **Deviation / Exception Needed** above.

### Data Model and Persistence

[Summarize affected entities, schema changes, data dictionary / ER impact,
migration strategy, seeding needs, and disciplined schema handling. Use "N/A"
only when no persistence impact exists.]

### Administrative and Operational UX

[Summarize operator-facing flows, back-office actions, filters, pagination,
reporting, reusable forms, and error-recovery expectations.]

### Performance and Reliability

[Summarize operational load, large listings, export/report limits, job behavior,
timeouts, failure handling, monitoring, and recovery expectations.]

## Delivery Plan

**Branch Strategy**: [One branch per functionality, hotfix exception if needed]  
**Commit Strategy**: [Clear and frequent commits expectation for this work]  
**Promotion Path**: [feature branch -> testing -> master, or justified hotfix path]  
**QA Validation**: [Required QA checks before release]  
**Deployment Plan**: [Controlled deployment approach and environment sequence]  
**Rollback Plan**: [How this change is reversed, mitigated, or contained]  
**Production Validation**: [Operational checks after deployment]

## Risky Assumptions and Open Questions

- [Assumption or open question with potential delivery impact]
- [Assumption or open question with security / data / operational impact]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., Non-approved integration pattern] | [current need] | [why approved pattern is insufficient] |
| [e.g., Direct schema workaround] | [specific problem] | [why standard schema approach is insufficient] |
