# 03 — Technical Architecture & Conceptual Data Model

> Source: Notion — EIS (https://app.notion.com/p/41cd71c0838d8102ba1ae1a65a6f77d6) · Exported 2026-11-19

Define a practical technical foundation for the first release while preserving a path to the broader EIS SaaS product.

All technology choices below are proposals unless explicitly marked as a user preference.

## Guiding architecture

Start with a modular monolith and a separate background worker process where useful. Keep clear module boundaries and avoid introducing microservices before scale or team structure justifies them.

### Proposed stack

| Layer | Proposal | Status |
| --- | --- | --- |
| Backend | .NET / ASP.NET Core | User preference |
| Frontend | React | User preference |
| Database | SQLite initially (prototype/development); SQL Server as a possible later production target | Proposed; validate before production |
| File storage | S3-compatible object storage | Proposed |
| Background work | .NET Worker Service and durable job/queue mechanism | Proposed |
| Authentication | ASP.NET Core Identity or equivalent | Proposed |
| Deployment | Containers and cloud hosting | Proposed |
| Observability | Structured logs, metrics, tracing and alerting | Required capability; vendor TBD |

**Database portability plan:** Treat SQLite as the initial prototype/development database and SQL Server as a possible later target, not a drop-in upgrade. If using EF Core, keep provider-specific migrations separate; avoid SQLite-only SQL/features and assumptions about locking or concurrent writes. Test critical queries, constraints, data types (especially monetary values), and data migrations against SQL Server before switching. Before production SaaS deployment, validate concurrency, multi-instance hosting, backups and restore, and operational requirements; SQLite may not be suitable for that workload.

Avoid making Redis, a message broker, or multiple deployable services mandatory for the first prototype unless a concrete requirement calls for them.

## Logical modules

1. **Identity and access** — users, authentication, roles, invitations and sessions.
2. **Organizations and companies** — SaaS customer organizations, registered businesses, branches and company settings.
3. **Import management** — file upload, template versions, parsing, import batches and row-level results.
4. **Invoice domain** — invoice headers, lines, taxes, parties and document references.
5. **Validation** — structural, business and regulatory rule sets, versioned independently.
6. **Submission orchestration** — submission grouping, queueing, idempotency, attempts and reconciliation.
7. **BIR adapter** — replaceable, versioned integration boundary.
8. **Audit and evidence** — user actions, state transitions, source files, payloads and responses.
9. **Administration and support** — tenant support, operational views and controlled troubleshooting.
10. **Usage/billing (later)** — auditable usage events and ledger; pricing remains undecided.

## High-level component flow

Business portal → ASP.NET Core API → domain modules and validation → SQLite initially/object storage → background processing → BIR adapter (only through an approved and verified integration route).

The browser must never call the BIR integration directly or hold provider credentials.

## Multi-tenant design

The system should distinguish:

- SaaS organization/account: the customer relationship and billing boundary.
- Company: the legal business entity whose invoices are being managed.
- Branch: a location or registered branch of a company.
- User: an individual login identity.
- Membership/permission: the user's access to an organization, company or branch.
- Accounting firm: an organization that may be delegated access to multiple client companies.

A direct business may have one organization and one company initially. An accounting firm may have one organization and many client companies. Model these relationships explicitly rather than treating the accounting firm itself as the taxpayer.

Tenant isolation must be enforced server-side on every relevant query and operation. Do not rely on the frontend to hide other tenants' data. Add automated cross-tenant access tests.

## Conceptual data model

| Entity | Purpose / key relationships |
| --- | --- |
| Organizations | SaaS customer/account; owns memberships |
| Companies | Legal taxpayer/business; belongs to an organization or is managed through a firm relationship |
| Branches | Belong to a company |
| Users | Login identities |
| OrganizationMemberships | User-to-organization roles |
| CompanyAccessGrants | Explicit delegated access to companies |
| ImportTemplates | Versioned file format and mapping definitions |
| ImportBatches | One uploaded source file and reporting period |
| ImportRows | Parsed source rows and row-level errors |
| Invoices | Normalized invoice header records |
| InvoiceItems | Invoice line items |
| InvoiceTaxes | Tax breakdowns |
| BusinessPartners | Buyer/customer details appearing on invoices |
| SubmissionBatches | Grouping of invoices for an external submission |
| SubmissionItems | Invoice-to-submission relationship |
| SubmissionAttempts | Each transmission attempt and its outcome |
| SubmissionResponses | External acknowledgement, response and error details |
| AuditEvents | Append-oriented record of important user/system events |
| UsageEvents | Future auditable billable usage events |

### Important separations

**ImportBatch vs Invoice:** one file can contain many invoice records; invoices should not be trapped inside a file-level record.

**ImportBatch vs SubmissionBatch:** the uploaded file is the source intake event; the external submission grouping may differ. Preserve the relationship without assuming one upload always equals one transmission.

**Invoice lifecycle vs submission lifecycle:** a document's business/legal state is distinct from its transmission state. Define exact states only after checking official rules.

**SubmissionAttempt vs SubmissionResponse:** retries and responses must be individually traceable.

**Source file vs normalized data vs outbound payload:** preserve lineage between original input, parsed values, normalized invoice, and any payload generated for a specific integration version.

## Data integrity and audit requirements

- Use stable internal identifiers; do not use invoice number alone as a primary key.
- Define uniqueness rules scoped to the relevant company/branch and document type.
- Store monetary values using appropriate fixed-precision decimal types.
- Store timestamps consistently and preserve the relevant business timezone for reporting periods.
- Version import templates and validation rules.
- Preserve source-file metadata and cryptographic hash where appropriate.
- Record who uploaded, reviewed, confirmed, changed or retried a batch.
- Make state transitions explicit and auditable.
- Use idempotency keys for processing and external submission where supported.
- Avoid destructive edits to issued documents; follow the legally required correction-document process.
- Define retention and deletion policies with regulatory and privacy advice.

## Security baseline

- Strong authentication and secure session handling.
- Role-based and resource-level authorization.
- Tenant isolation enforced in backend and database access patterns.
- TLS in transit and encryption at rest.
- Secret and key management outside source code.
- Malware scanning and strict validation for uploaded files.
- Rate limits and abuse protection.
- Audit trails for privileged access.
- Backups with restore tests.
- Centralized error handling without exposing taxpayer data in logs.
- Data minimization and controlled support access.

## Architecture decisions still open

- React application setup (framework/build tooling and rendering needs).
- Database provider and hosting.
- File storage provider.
- Durable queue/background job technology.
- Authentication approach and optional MFA.
- Tenant isolation strategy at database level.
- Hosting region and privacy implications.
- Availability, performance and retention targets.
- Exact BIR adapter contract after official documentation is obtained.

## Related EIS documentation

See the EIS hub for product scope, regulatory readiness and the development roadmap.
