"""Approved project stack profiles for stack-aware initialization."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


STACK_CONTEXT_FILE = Path(".specify/context/stack.md")
STACK_CONTEXT_REQUIRED_SECTIONS = (
    "## Selected Stack",
    "## Purpose / Typical Use",
    "## When This Stack Fits",
    "## When This Stack Is a Poor Fit",
    "## Core Constraints",
    "## Typical Risks",
    "## Expected Artifacts",
    "## Preferred Practices",
    "## Things To Avoid",
    "## Security Controls",
    "## Security Pitfalls",
    "## Security Evidence",
)


@dataclass(frozen=True)
class StackProfile:
    """Company-approved stack metadata and planning guidance."""

    key: str
    name: str
    purpose: str
    when_it_fits: tuple[str, ...]
    poor_fit: tuple[str, ...]
    core_constraints: tuple[str, ...]
    typical_risks: tuple[str, ...]
    expected_artifacts: tuple[str, ...]
    preferred_practices: tuple[str, ...]
    avoid: tuple[str, ...]
    security_controls: tuple[str, ...]
    security_pitfalls: tuple[str, ...]
    security_evidence: tuple[str, ...]


APPROVED_STACKS: dict[str, StackProfile] = {
    "cakephp2-mysql": StackProfile(
        key="cakephp2-mysql",
        name="CakePHP 2.x + MySQL",
        purpose="Legacy internal and admin-heavy web applications that must stay compatible with the existing CakePHP 2.x estate and MySQL-backed operational data.",
        when_it_fits=(
            "The feature extends an existing CakePHP 2.x codebase, module, or back-office workflow instead of creating a new platform.",
            "The work is centered on server-rendered CRUD, reporting, operational listings, approvals, exports, or compatibility-sensitive maintenance.",
            "The business value depends on preserving the current authentication, deployment, hosting, and schema model instead of introducing a new application shell.",
        ),
        poor_fit=(
            "Greenfield product surfaces that need a modern component-driven frontend or a new application platform.",
            "Work that would require a de facto framework migration, SPA architecture, or a separate runtime to stay maintainable.",
            "Heavy asynchronous integration or event-driven designs that would fight the legacy request lifecycle and operational environment.",
        ),
        core_constraints=(
            "Preserve CakePHP 2.x conventions, controller/model/view boundaries, legacy bootstrap behavior, and established auth or ACL patterns.",
            "Favor conservative MySQL migrations, explicit rollback planning, and schema changes that are safe for live operational data.",
            "Assume legacy compatibility and hosting constraints are real unless the plan records an approved exception.",
        ),
        typical_risks=(
            "Tight coupling in reused models, helpers, or components causing regressions far from the feature entry point.",
            "Slow queries, pagination regressions, or export/report timeouts on large operational datasets.",
            "Hidden manual SQL, ad hoc production data fixes, or fragile migrations that bypass traceable delivery controls.",
        ),
        expected_artifacts=(
            "Controller, model, view, component, helper, shell, or config changes that stay aligned with the CakePHP 2.x structure already in use.",
            "Documented MySQL schema or migration impact, validation rules, indexes, seed or backfill needs, and rollback notes.",
            "QA coverage for permissions, admin flows, listings, filters, exports, and other operational paths touched by the feature.",
        ),
        preferred_practices=(
            "Reuse established CakePHP components, helpers, and query patterns before introducing new abstractions.",
            "Keep data-model, pagination, indexing, and report/export impacts explicit in the plan and tasks.",
            "Make risky legacy touchpoints visible early so QA, deployment, and rollback planning are not afterthoughts.",
        ),
        avoid=(
            "Do not smuggle in a parallel frontend architecture or framework migration under a normal feature request.",
            "Do not bypass migrations, data-model documentation, or delivery traceability with direct database changes.",
            "Do not ship large-listing or admin workflow changes without validating performance, pagination, and rollback behavior.",
        ),
        security_controls=(
            "Enable `SecurityComponent` with form tampering and CSRF protection on every controller that accepts mutations.",
            "Authorize privileged actions with `AuthComponent` server-side; never rely on view-only checks.",
            "Hash credentials with `Security::hash($pwd, 'blowfish')` or migrate to `password_hash` / `password_verify` in a dedicated layer; never use md5/sha1 for passwords.",
            "Keep `Security.salt` and `Security.cipherSeed` out of version-controlled `app/Config/core.php`; rotate them after credential incidents.",
            "Use ORM bindings or `$Model->find` parameter arrays; ban string-concatenated `$this->Model->query(...)` for user-controlled input.",
            "Validate and sanitize `$this->request->data` server-side; never echo request data without contextual escaping helpers.",
            "Use the `h()` helper every time user-influenced or stored dynamic text is output in views, elements, layouts, and emails (including inside HTML attributes and JSON-in-script); treat omission of `h()` as a defect unless the value is provably constant and non-HTML.",
            "For every file upload, validate the real MIME type and magic bytes (for example `finfo_file` / `mime_content_type` on a temp path) against an allow-list; never trust the browser `Content-Type` or the original filename alone. Reject `.php`, `.phtml`, `.phar`, `.htaccess`, path traversal in names, and double extensions that smuggle executables.",
            "Store uploads outside the webroot or behind non-executable delivery (no direct PHP execution from the upload directory); normalize stored filenames.",
            "Apply security headers (CSP, HSTS, X-Content-Type-Options, Referrer-Policy) at the web server or reverse proxy; CakePHP 2 has no robust native equivalent.",
            "Maintain a manual CVE and patch inventory because CakePHP 2.x is out of official maintenance; track third-party plugin compatibility per release.",
        ),
        security_pitfalls=(
            "Disabling `SecurityComponent` because forms break instead of fixing FormHelper usage.",
            "Calling `$this->Model->query('SELECT ... WHERE id = ' . $id)` with user-controlled input.",
            "Storing `Security.salt` / `cipherSeed` in committed configuration files.",
            "Authorizing only in views or hidden fields instead of `AuthComponent` / `isAuthorized`.",
            "Printing dynamic values with `echo` / short tags without `h()`, or embedding them unescaped in attributes, `<script>`, or JavaScript literals (XSS).",
            "Accepting uploads based only on client `Content-Type` or file extension without server-side MIME and content checks, or allowing `.php` / scriptable types into a web-served folder.",
            "Logging request bodies, sessions, or stack traces that contain credentials or PII.",
            "Letting legacy plugins or vendor trees drift from a known-good patched baseline.",
        ),
        security_evidence=(
            "Plan documents controllers where `SecurityComponent` or `AuthComponent` configuration changes.",
            "Plan lists views or elements that render user-influenced text and confirms `h()` (or equivalent) is applied at every output site.",
            "Plan describes upload handling: MIME and extension allow-list, denial of `.php` and related types, storage path, and how files are served without execution risk.",
            "Plan lists models and queries touched and confirms parameterized access (no raw SQL with user input).",
            "Plan attaches the CVE/patch inventory delta when third-party or core code changes.",
            "QA covers authentication, authorization, CSRF, and pagination for affected operational paths.",
            "Deployment notes include web-server header configuration when applicable.",
        ),
    ),
    "moodle5-plugin": StackProfile(
        key="moodle5-plugin",
        name="Moodle 5 Plugin",
        purpose="Bounded Moodle 5 extensions delivered as plugins that fit Moodle's plugin APIs, lifecycle, permissions, privacy model, and Bootstrap 5-based UI reality.",
        when_it_fits=(
            "The feature is a discrete Moodle capability that can live inside a standard plugin boundary with clear ownership.",
            "The work fits Moodle plugin APIs, capabilities, forms, events, privacy APIs, scheduled tasks, and upgrade steps.",
            "UI work can stay inside Moodle's rendering model, Mustache or renderer patterns, and the Bootstrap 5 conventions already present in Moodle 5.",
        ),
        poor_fit=(
            "Requests that really require a broader portal or cross-area institutional workflow rather than a bounded plugin.",
            "Features that only work by patching Moodle core, replacing shared portal navigation, or ignoring Moodle's upgrade lifecycle.",
            "Frontend-heavy experiences that assume a custom standalone application shell instead of Moodle's plugin and Bootstrap 5 environment.",
        ),
        core_constraints=(
            "Stay inside Moodle 5 plugin APIs, capability checks, events, privacy handling, versioning, and upgrade-step conventions.",
            "Assume Moodle ecosystem compatibility matters: plugin changes must coexist with the host instance, theme, and upgrade path.",
            "Treat Bootstrap 5, Moodle form APIs, language strings, and renderer or template conventions as the frontend baseline rather than inventing a separate UI system.",
        ),
        typical_risks=(
            "Capability, privacy, or data-exposure regressions that leak course, user, grading, or institutional information.",
            "Broken installs or upgrades due to missing `version.php`, `db/install.xml`, `db/upgrade.php`, or incomplete capability and privacy changes.",
            "Maintenance drag from bypassing Moodle APIs or building frontend behavior that fights Moodle's rendering and theming model.",
        ),
        expected_artifacts=(
            "Plugin files such as `version.php`, `db/install.xml`, `db/upgrade.php`, language strings, capabilities, privacy metadata, classes, forms, templates, or renderers as applicable.",
            "Explicit install, upgrade, rollback, and permissions notes for the plugin and any stored or derived data it introduces.",
            "QA coverage for teacher, student, admin, and manager workflows touched by the plugin, including Bootstrap 5 UI states where relevant.",
        ),
        preferred_practices=(
            "Use Moodle forms, capability checks, string management, privacy APIs, and plugin upgrade paths consistently.",
            "Keep plugin data bounded and document any new tables, scheduled tasks, events, or privacy exports explicitly.",
            "Design UI additions to feel native to Moodle 5, including Bootstrap 5-based layout and predictable admin workflows.",
        ),
        avoid=(
            "Do not patch Moodle core when a plugin extension point is the correct solution.",
            "Do not skip capability, privacy, versioning, install, or upgrade analysis for seemingly small features.",
            "Do not introduce a separate frontend stack that ignores Moodle's Bootstrap 5 and plugin rendering constraints unless an exception is approved.",
        ),
        security_controls=(
            "Call `require_login()` and `require_capability()` with the correct context on every plugin entrypoint (pages, AJAX, web services, scheduled tasks).",
            "Protect state-changing flows with `sesskey()` / `confirm_sesskey()` or Moodle Forms (`moodleform`), which handle sesskey automatically.",
            "Use the `$DB` API with named placeholders only; never concatenate user-controlled input into SQL strings.",
            "Render output with `format_string` / `format_text` using the proper context and filters; never echo raw user input.",
            "Serve uploads via the Files API and `pluginfile.php` with capability checks; never expose raw filesystem paths.",
            "For every upload surface (draft areas, file managers, custom forms), enforce allowed extensions and MIME type groups server-side (`file_extension`, `file_mimetype_in_typegroup`, or equivalent); reject `.php`, `.phtml`, `.phar`, `.htaccess`, path tricks, and double extensions. Never persist user binaries to a web-served directory outside Moodle's file storage model.",
            "Implement the Privacy API (provider, metadata, export, delete) for any plugin that stores or derives personal data.",
            "Use language strings (`get_string`) for user-visible text; keep credentials and identifiers out of debug output.",
            "Track Moodle compatibility via `version.php` and ship `db/upgrade.php` paths that preserve capabilities and privacy metadata across upgrades.",
        ),
        security_pitfalls=(
            "Skipping `require_login` on AJAX endpoints because they are internal.",
            "Calling `$DB->execute` or `$DB->get_records_sql` with concatenated user input.",
            "Using `optional_param` / `required_param` with the wrong type (e.g. PARAM_RAW) where PARAM_INT, PARAM_ALPHANUM, or PARAM_TEXT is required.",
            "Bypassing the Files API by writing directly to `$CFG->dataroot` or returning filesystem paths in URLs.",
            "Accepting uploads without server-side MIME and extension checks, or allowing scriptable types (for example `.php`) to be stored or served in a way that could execute under the web server.",
            "Omitting privacy metadata for new tables, leaving the plugin non-compliant with the Privacy API.",
            "Sharing state with globals across requests instead of session and context APIs.",
        ),
        security_evidence=(
            "Plan lists each entrypoint, the capability checked, and the context level used.",
            "Plan records `version.php`, `db/install.xml` / `db/upgrade.php`, and privacy metadata changes.",
            "Plan lists new or changed language strings.",
            "QA covers teacher, student, admin, and guest flows, including capability denial paths.",
            "Plan documents how uploads are stored and served through the Files API, including MIME or typegroup rules, extension deny-list, and capability checks on `pluginfile`.",
        ),
    ),
    "moodle5-portal": StackProfile(
        key="moodle5-portal",
        name="Moodle 5 Portal",
        purpose="Institution-facing Moodle 5 portal work that spans multiple workflows, operational teams, reports, and user roles while still living inside Moodle's ecosystem and Bootstrap 5 UI constraints.",
        when_it_fits=(
            "The feature crosses portal navigation, reporting, enrollment, certification, institution-facing operations, or multiple Moodle touchpoints.",
            "Operational users need coordinated workflows, dashboards, filters, reports, exports, or support tooling that go beyond a small isolated plugin.",
            "The solution can remain aligned with Moodle 5 services, Bootstrap 5 UI conventions, shared permissions, and portal-wide governance.",
        ),
        poor_fit=(
            "Small self-contained functionality that should remain a bounded Moodle plugin instead of portal work.",
            "Greenfield product requests that would be better served by the Laravel + Inertia + React stack rather than portal customizations.",
            "Features that need to ignore shared portal permissions, reporting standards, or Moodle ecosystem constraints to be viable.",
        ),
        core_constraints=(
            "Portal behavior must fit existing Moodle 5 capabilities, service boundaries, navigation patterns, and Bootstrap 5-based operational UI expectations.",
            "Treat reporting, pagination, exports, cohort or enrollment flows, and institutional data sensitivity as first-class design constraints.",
            "Assume multi-role operational ownership: supportability, traceability, and rollout safety matter as much as the feature itself.",
        ),
        typical_risks=(
            "Cross-area permission leakage, role confusion, or inconsistent workflow behavior between portal surfaces.",
            "Performance and operability failures in large listings, reports, exports, enrollments, or synchronization-heavy flows.",
            "Portal drift caused by ad hoc solutions that bypass shared portal conventions, observability needs, or institutional support requirements.",
        ),
        expected_artifacts=(
            "Portal page, renderer, template, integration, permission, and reporting changes mapped clearly to the affected operational flows.",
            "Documented pagination, filtering, export, audit, rollout, and rollback expectations for institution-facing screens and jobs.",
            "QA and production validation steps that cover real administrative users, support teams, and shared portal operations.",
        ),
        preferred_practices=(
            "Use Moodle-native capabilities and services while keeping portal workflows explicit, observable, and supportable.",
            "Design for backend pagination, predictable filters, reusable Bootstrap 5 admin patterns, and safe exports or batch actions.",
            "Document which roles, institutions, reports, and support teams are affected so delivery planning reflects operational reality.",
        ),
        avoid=(
            "Do not treat institution-wide portal changes as if they were isolated plugin tweaks.",
            "Do not bypass shared portal auth, navigation, reporting, or observability standards for local convenience.",
            "Do not ship operationally sensitive portal changes without controlled deployment and rollback planning.",
        ),
        security_controls=(
            "Apply institution-aware capability checks on every cross-area page; never assume a global admin context.",
            "Paginate large listings, reports, and exports server-side with explicit per-context permission checks before each batch.",
            "Emit audit events for cohort or enrollment changes, role assignments, and bulk actions through Moodle's event API.",
            "Enforce cohort or tenant isolation: reports, exports, and notifications must scope to the active institution context.",
            "Protect report and export downloads through `pluginfile.php` with capability-aware callbacks.",
            "Coordinate LDAP, SAML, or SSO with central identity ownership; do not bypass Moodle auth plugins for shortcuts.",
            "For portal file intake (imports, attachments, archives, generated exports that re-ingest user files), validate real MIME types and enforce extension allow-lists server-side; reject `.php`, `.phtml`, `.phar`, nested archives with executables, and path-traversal names. Keep persisted user files in Moodle file storage with `pluginfile` delivery, not ad-hoc web directories.",
        ),
        security_pitfalls=(
            "Querying institutional data without filtering by the active context (course, cohort, category).",
            "Building dashboards that mix institutions without explicit tenant scoping.",
            "Shipping bulk actions without confirmation, audit events, or partial-failure handling.",
            "Returning unbounded result sets in admin reports, enabling slow rendering or timeout-based abuse.",
            "Hardcoding institution-specific roles instead of capabilities and contexts.",
            "Bulk-importing or re-hosting user-supplied files without MIME and extension validation, allowing executable content into institutional workflows or web-served paths.",
        ),
        security_evidence=(
            "Plan lists operational roles touched and the capability and context combination each requires.",
            "Plan documents pagination, filtering, and export limits for every large listing or report.",
            "Plan registers audit events for sensitive operations (cohort, enrollment, role assignment, bulk).",
            "QA validates institution isolation: users in institution A must not see institution B data.",
            "Plan describes any portal upload or import path: MIME and extension policy, explicit rejection of `.php` and related types, and how files are stored and delivered without execution risk.",
        ),
    ),
    "laravel-inertia-react": StackProfile(
        key="laravel-inertia-react",
        name="Laravel + Inertia + React",
        purpose="The company's standard modern web application stack for business systems that use Laravel on the backend and Inertia with React on the frontend.",
        when_it_fits=(
            "The feature belongs in a modern Laravel application with server-owned routing, validation, authorization, and data access.",
            "The UI benefits from React components and Inertia pages while still fitting a server-driven application model instead of a disconnected SPA.",
            "The work can follow the company conventions around React + TypeScript starterkit usage, Tailwind, shadcn/ui, backend pagination, reusable form components, and traceable Laravel delivery practices.",
        ),
        poor_fit=(
            "Moodle plugin or portal requests that need to live inside Moodle's ecosystem and Bootstrap 5 reality.",
            "Legacy CakePHP 2.x enhancements where compatibility matters more than adopting the modern stack.",
            "Features that only make sense as a standalone public API platform or a custom client-only application outside the current Laravel + Inertia operating model.",
        ),
        core_constraints=(
            "Laravel remains the source of truth for routing, validation, authorization, persistence, jobs, notifications, and business rules.",
            "Use the React + TypeScript starterkit direction, Tailwind styling, and shadcn/ui-based reusable components rather than ad hoc UI patterns.",
            "Follow company defaults such as REST-style routes and controllers, `spatie/laravel-permission` for roles or permissions, Socialite where external auth or SSO is in scope, backend-driven pagination, and disciplined migrations or seeders.",
        ),
        typical_risks=(
            "Boundary drift between controllers, requests, policies, Inertia responses, and React pages leading to duplicated or contradictory logic.",
            "Authorization, validation, pagination, or form-state problems caused by pushing too much behavior into the client layer.",
            "Inconsistent UI, brittle deployments, or broken environments when migrations, seeders, assets, permissions, or auth integrations are handled informally.",
        ),
        expected_artifacts=(
            "Laravel routes, controllers, form requests, policies, actions or services, models, migrations, seeders, and tests as required by the feature.",
            "Inertia pages, React + TypeScript components, Tailwind or shadcn/ui composition, and reusable form or table components where the UI changes.",
            "Explicit handling of permissions, Socialite integrations when relevant, backend pagination, QA, deployment, and rollback-sensitive migrations or config changes.",
        ),
        preferred_practices=(
            "Keep business rules, permissions, and validation centered in Laravel while using Inertia page props intentionally.",
            "Prefer reusable Tailwind or shadcn/ui components, typed React props, backend pagination, and shared form patterns over feature-by-feature improvisation.",
            "Treat migrations, seeders, permission changes, QA, and controlled deployment as part of the feature's standard artifact set rather than optional cleanup.",
        ),
        avoid=(
            "Do not create parallel client-side data flows that bypass Laravel, Inertia, or the established permission model without an approved exception.",
            "Do not duplicate authorization or validation rules across backend and frontend when Laravel should own the canonical behavior.",
            "Do not skip migrations, seeders, permission setup, reusable form components, or backend pagination where the feature clearly needs them.",
        ),
        security_controls=(
            "Authorize every controller action with Policies and Gates (`$this->authorize(...)` or `can:` middleware); never rely on React or Inertia alone.",
            "For mutating actions (`store`, `update`, and any other write that accepts a request body), type-hint a dedicated `FormRequest` subclass with explicit rules and authorization; do not use `Illuminate\\Http\\Request` in those methods. Read-only endpoints may use `Request` only when no validated body is consumed.",
            "Reject unvalidated array hydration from any request object into models or commands.",
            "Enforce mass-assignment rules with explicit `$fillable` (or guarded models with deliberate fillable lists) on every Eloquent model that accepts user input.",
            "Hash credentials with bcrypt or argon2id via `Hash::make`; encrypt PII with `encrypted` or `encrypted:array` casts and rotate `APP_KEY` per policy.",
            "Apply `RateLimiter` or `throttle:` middleware to authentication, password reset, and sensitive write endpoints; log throttling events.",
            "Keep CSRF middleware enabled on all state-changing routes; forward the XSRF cookie or token for Inertia as documented.",
            "Emit security headers (CSP with nonce or hashes, HSTS, X-Content-Type-Options, Referrer-Policy, Permissions-Policy) via middleware or reverse proxy; align Vite and Inertia HTML with the CSP nonce when used.",
            "Run `composer audit` and `npm audit --omit=dev` in CI; resolve high-severity advisories before release.",
            "Strip sensitive values from Inertia shared data in `HandleInertiaRequests`; expose only minimal session or user fields.",
            "For uploads, validate in Form Requests using `file`, `mimes`, `mimetypes`, and size limits; verify the real MIME type from the stored file (for example `File::mimeType()` or `finfo`) against an allow-list. Reject `.php`, `.phtml`, `.phar`, `.htaccess`, path traversal in original names, and double extensions. Store outside `public/` or serve only through authenticated download routes; never execute uploaded binaries.",
            "Disable debug surfaces in production (`APP_DEBUG=false`); protect Telescope, Horizon, and Pulse behind authorization.",
        ),
        security_pitfalls=(
            "Authorizing only in React or Inertia without a backend Policy or Gate.",
            "Using `Request $request` (or untyped request) in `store`, `update`, or other write actions instead of a dedicated `FormRequest`, which bypasses centralized validation and `authorize()` on the request class.",
            "Using `Model::create($request->all())` or `Model::fill($request->all())` without Form Request validation and `$fillable` enforcement.",
            "Rendering user HTML with `dangerouslySetInnerHTML` without server-side sanitization.",
            "Storing API tokens, signed URLs, or PII in Inertia shared props or client state that leaks in the page payload.",
            "Disabling CSRF middleware instead of wiring the token correctly.",
            "Returning raw Eloquent models in Inertia responses, exposing hidden attributes or internal flags.",
            "Running `php artisan tinker`, `migrate:fresh`, or ad hoc `DB::statement` in production without an audit trail.",
            "Trusting the browser filename or `Content-Type` alone, storing uploads under `public/` with predictable URLs, or skipping MIME checks so `.php` or disguised executables can be uploaded or executed.",
        ),
        security_evidence=(
            "Plan lists Policies, Gates, and Form Requests added or reused, with the routes they cover.",
            "Plan or PR lists each `store` / `update` (and other write) action and names the concrete `FormRequest` class used; no generic `Request` type-hint on those methods.",
            "Plan states which Eloquent models change and the fillable or guarded posture for each.",
            "Migrations and seeders document PII handling (encrypted casts, hashing, factory redaction).",
            "Pull requests include `composer audit` and `npm audit` results with remediation for high-severity issues.",
            "QA notes cover authentication boundaries, rate limiting, CSRF on Inertia forms, and CSP or headers in the target environment.",
            "Plan documents each upload endpoint: validation rules, MIME verification, extension deny-list, storage disk and path, and how downloads are authorized.",
        ),
    ),
}


def approved_stack_ids() -> tuple[str, ...]:
    """Return approved stack identifiers in stable order."""

    return tuple(APPROVED_STACKS.keys())


def approved_stack_help() -> str:
    """Return a human-readable approved stack list."""

    return ", ".join(approved_stack_ids())


def get_stack_profile(stack_id: str | None) -> StackProfile | None:
    """Resolve an approved stack profile by identifier."""

    if not stack_id:
        return None
    return APPROVED_STACKS.get(stack_id)


def _split_frontmatter(content: str) -> tuple[dict[str, str], str] | tuple[None, str]:
    """Extract simple YAML-like frontmatter from the stack context."""

    if not content.startswith("---\n"):
        return None, content

    end_index = content.find("\n---\n", 4)
    if end_index == -1:
        return None, content

    raw_frontmatter = content[4:end_index].splitlines()
    data: dict[str, str] = {}
    for line in raw_frontmatter:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()

    body = content[end_index + len("\n---\n") :]
    return data, body


def _section_body(body: str, heading: str) -> str:
    """Return the markdown body for a given section heading."""

    start = body.find(heading)
    if start == -1:
        return ""

    start += len(heading)
    next_heading = body.find("\n## ", start)
    if next_heading == -1:
        next_heading = len(body)
    return body[start:next_heading].strip()


def validate_stack_context_content(content: str) -> list[str]:
    """Validate stack context structure and metadata."""

    errors: list[str] = []
    frontmatter, body = _split_frontmatter(content)

    if frontmatter is None:
        return ["Missing or malformed frontmatter block."]

    stack_id = frontmatter.get("stack_id")
    stack_name = frontmatter.get("stack_name")
    profile = get_stack_profile(stack_id)

    if not stack_id:
        errors.append("Missing frontmatter key: stack_id.")
    elif profile is None:
        errors.append(f"Unknown approved stack id in context: {stack_id}.")

    if not stack_name:
        errors.append("Missing frontmatter key: stack_name.")
    elif profile and stack_name != profile.name:
        errors.append(
            f"stack_name '{stack_name}' does not match approved name '{profile.name}'."
        )

    for heading in STACK_CONTEXT_REQUIRED_SECTIONS:
        if heading not in body:
            errors.append(f"Missing required section: {heading}.")
            continue

        section_body = _section_body(body, heading)
        if "- " not in section_body:
            errors.append(f"Section {heading} must contain at least one bullet.")

    return errors


def load_stack_profile_from_context(project_root: Path) -> tuple[StackProfile | None, list[str]]:
    """Load and validate the registered stack from ``stack.md`` when available."""

    context_path = project_root / STACK_CONTEXT_FILE
    if not context_path.exists():
        return None, []

    try:
        content = context_path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, [f"Could not read {STACK_CONTEXT_FILE.as_posix()}: {exc}"]

    errors = validate_stack_context_content(content)
    if errors:
        return None, errors

    frontmatter, _body = _split_frontmatter(content)
    if frontmatter is None:
        return None, ["Missing or malformed frontmatter block."]

    profile = get_stack_profile(frontmatter.get("stack_id"))
    if profile is None:
        return None, [
            f"Unknown approved stack id in {STACK_CONTEXT_FILE.as_posix()}."
        ]

    return profile, []


def render_stack_context(profile: StackProfile) -> str:
    """Render the durable project stack context file."""

    def bullets(items: tuple[str, ...]) -> str:
        return "\n".join(f"- {item}" for item in items)

    return (
        f"---\n"
        f"stack_id: {profile.key}\n"
        f"stack_name: {profile.name}\n"
        f"---\n\n"
        f"# Project Stack Profile\n\n"
        f"## Selected Stack\n\n"
        f"- **ID**: {profile.key}\n"
        f"- **Name**: {profile.name}\n\n"
        f"## Purpose / Typical Use\n\n"
        f"- {profile.purpose}\n\n"
        f"## When This Stack Fits\n\n"
        f"{bullets(profile.when_it_fits)}\n\n"
        f"## When This Stack Is a Poor Fit\n\n"
        f"{bullets(profile.poor_fit)}\n\n"
        f"## Core Constraints\n\n"
        f"{bullets(profile.core_constraints)}\n\n"
        f"## Typical Risks\n\n"
        f"{bullets(profile.typical_risks)}\n\n"
        f"## Expected Artifacts\n\n"
        f"{bullets(profile.expected_artifacts)}\n\n"
        f"## Preferred Practices\n\n"
        f"{bullets(profile.preferred_practices)}\n\n"
        f"## Things To Avoid\n\n"
        f"{bullets(profile.avoid)}\n\n"
        f"## Security Controls\n\n"
        f"{bullets(profile.security_controls)}\n\n"
        f"## Security Pitfalls\n\n"
        f"{bullets(profile.security_pitfalls)}\n\n"
        f"## Security Evidence\n\n"
        f"{bullets(profile.security_evidence)}\n"
    )


def write_stack_context(project_root: Path, profile: StackProfile) -> Path:
    """Write the durable stack context file into the project."""

    destination = project_root / STACK_CONTEXT_FILE
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_stack_context(profile), encoding="utf-8")
    return destination
