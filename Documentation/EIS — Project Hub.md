# EIS — Project Hub

> Source: Notion — EIS (https://app.notion.com/p/41ad71c0838d81b4bbccdf37435ec5c6) · Exported 2026-11-19

## Project overview

Plan a multi-tenant SaaS platform for electronic invoicing and related workflows in the Philippines, with integration to the Bureau of Internal Revenue (BIR) Electronic Invoicing System (EIS).

**Current working principle:** planning first. No code or implementation work is requested yet.

## Confirmed product direction

- **Product model:** SaaS.
- **Market and regulatory context:** Philippines; BIR EIS.
- **Customer segments:** both direct business customers and accounting firms managing multiple client companies.
- **Backend preference:** .NET / ASP.NET Core.
- **Scope:** full platform, not only a BIR connector.
- **Current phase:** product and technical planning.

## Proposed technology and architecture (not yet approved)

| Area | Current proposal | Status |
| --- | --- | --- |
| Backend | .NET / ASP.NET Core | User preference |
| Frontend | React | User preference |
| Database | SQLite initially; SQL Server as a possible later target | Suggested; validate before production |
| Architecture | Modular monolith initially | Suggested |
| Background processing | Background workers and a message queue | Suggested |
| Cache | Redis | Suggested |
| Deployment | Docker and a cloud environment | Suggested |
| Observability | Centralized logging, metrics, and telemetry | Suggested |

The modular-monolith approach is intended to keep the first version manageable while maintaining clear module boundaries. Services can be separated later if scale or operational needs justify it.

## Customer and account model

The platform must support two customer journeys:

1. **Direct business customer:** a company signs up and manages its own users, customers, products, invoices, and BIR-related submissions.
2. **Accounting firm:** a firm has its own staff and manages multiple client companies, with access controlled per client.

The design should distinguish the accounting-firm organization from each client business. Each business should retain its own company profile, authorized users, tax and BIR configuration, documents, and submission history. Firm staff should only access client companies for which they have permission.

### Capabilities to plan for

| Capability | Direct business | Accounting firm |
| --- | --- | --- |
| Company management | Own company | Multiple client companies |
| Invoice creation | Own company | For authorized clients |
| BIR submissions | Own company | Per client company |
| User management | Company users | Firm staff and client users |
| Reporting | Per company | Per client and consolidated views |
| Billing | Usage attributable to company | Usage attributable to managed client companies |

## Core platform scope to investigate

The intended scope is the full platform. Candidate modules include:

- Tenant, firm, and company management
- User accounts, roles, permissions, and client access delegation
- Company profiles and tax/BIR configuration
- Customers and suppliers
- Products and services
- Invoice and other supported document lifecycle
- Document numbering and validation
- BIR EIS integration and submission tracking
- Submission responses, errors, retries, and reconciliation
- Credit notes, debit notes, cancellations, and voiding where supported by applicable rules
- Transaction usage, billing, wallet/credits, and payment records
- Reports, audit history, and exports
- Notifications and operational monitoring
- Platform administration and customer support tools

This is a planning inventory, not a finalized feature specification. Exact document types and workflows must be checked against current official requirements.

## BIR integration and compliance considerations

Regulatory correctness is a critical dependency.

- Obtain and verify the current official BIR EIS technical documentation, schemas, API contract, security requirements, cryptographic requirements, certification or testing materials, result codes, and production onboarding process before finalizing the connector.
- Treat any previously discussed legacy API paths or cryptographic details as provisional, not as the current official contract.
- Keep the BIR connector versioned and replaceable so changes to the official interface do not require redesigning the entire product.
- Separate the business document lifecycle (draft, issued, voided, etc.) from the BIR transmission lifecycle (queued, submitted, accepted, rejected, retry pending, etc.). The exact state model must be validated against official rules.
- Maintain traceable submission attempts, responses, timestamps, and audit events.
- Do not claim BIR accreditation, certification, or production connectivity until those statuses have been verified and obtained.

## Transaction-based pricing discussion

The founder is considering charging per transaction rather than deciding on a subscription model now. Pricing is **not decided** and should be revisited later.

A possible direction discussed was usage-based billing, potentially with prepaid credits and/or postpaid billing. A hybrid arrangement was suggested as an option, but no billing approach was selected.

### Important billing design questions

- What exactly counts as a billable transaction?
- Should the charge apply when an invoice is successfully issued, when it is successfully submitted to BIR, or at another clearly defined event?
- How should retries, failed submissions, cancellations, voids, credit notes, debit notes, and corrections be treated?
- Should usage be charged to the individual business, the accounting firm, or either depending on the customer arrangement?
- Will customers use prepaid credits, postpaid invoicing, or both?
- What volume tiers, minimums, refunds, and credit-expiry rules (if any) are appropriate?

An illustrative pricing table was discussed, but the example rates were not researched or approved and must not be treated as actual pricing.

### Billing-system design considerations

Regardless of the eventual commercial model, plan for an auditable usage ledger that records charges, refunds, adjustments, transaction references, and balances. Avoid charging twice for repeated technical attempts relating to the same billable business event unless the eventual pricing policy explicitly says otherwise. Billing rules should be configurable and consistently applied.

## Planning sequence

1. Define product requirements and customer workflows for both customer segments.
2. Verify current BIR requirements and the official EIS integration contract.
3. Define the system architecture and module boundaries.
4. Design the tenant, firm, company, user, document, submission, and audit data model.
5. Map invoice and BIR submission workflows, including failures and reconciliation.
6. Decide the transaction definition and commercial billing model later.
7. Prepare a phased development roadmap and implementation plan.
8. Only begin coding when the planning phase and requirements are sufficiently clear.

## Open decisions and questions

- [ ] Decide the React application setup (framework/build tooling and rendering needs).
- [ ] Confirm database and infrastructure choices.
- [ ] Verify current BIR EIS documentation and onboarding requirements.
- [ ] Finalize supported invoice and document types.
- [ ] Define roles and permission boundaries for accounting firms and client companies.
- [ ] Decide how a firm and its clients are represented in the tenant/account model.
- [ ] Decide later whether transaction billing is prepaid, postpaid, or both.
- [ ] Define the billable transaction event and treatment of retries, failures, voids, and corrections.
- [ ] Establish pricing after usage assumptions and operating costs are better understood.

## Explicit working constraints

- Do not write code during the current planning phase.
- Treat suggested technologies, architecture choices, pricing examples, and workflows as proposals unless explicitly confirmed.
- Preserve regulatory uncertainty until current official BIR materials have been checked.

## Documentation map

This page is the EIS project hub. Detailed planning is split into focused child pages:

1. [01 — MVP Product Scope & Workflow](01%20—%20MVP%20Product%20Scope%20%26%20Workflow.pdf) — first-release scope, customer journeys, upload and validation workflow, screens, acceptance criteria and deferred features.
2. [02 — BIR Regulatory & Provider Readiness](02%20—%20BIR%20Regulatory%20%26%20Provider%20Readiness.pdf) — provider/accreditation questions, official BIR materials, compliance gates, privacy/security considerations and integration dependencies.
3. [03 — Technical Architecture & Conceptual Data Model](03%20—%20Technical%20Architecture%20%26%20Conceptual%20Data%20Model.pdf) — proposed architecture, tenant model, modules, conceptual entities, data integrity, audit and security.
4. [04 — Development Roadmap & Implementation Plan](04%20—%20Development%20Roadmap%20%26%20Implementation%20Plan.pdf) — phases, deliverables, exit criteria, indicative effort, work breakdown and launch gates.
5. [05 — BIR Requirements Gate & Development Workflow](05%20—%20BIR%20Requirements%20Gate%20%26%20Development%20Workflow.pdf) — regulatory-first workflow diagram and gate checklist covering potential ESP status, eligibility, BIR accreditation stages, taxpayer PTI/EIS Certification/PTT requirements, technical documentation, and the go/no-go decision before development.
6. [On-premise Installation](On-premise%20Installation.pdf) — preferred deployment direction: locally installed software operated on the taxpayer's own PC or server, dedicated to one taxpayer and its registered branches, with direct outbound BIR connectivity.
7. [EIS Product Editions & Pricing Strategy](EIS%20Product%20Editions%20%26%20Pricing%20Strategy.pdf) — proposed commercial model for the locally installed EIS product, with two editions sharing one invoice and transmission engine.

### Latest regulatory/product clarification — November 18, 2026

The intended first service is an accountant-side invoice import and BIR transmission platform. The preliminary assessment is that it may still fall under the third-party ESP framework if our SaaS validates, prepares, integrates or transmits invoice data for multiple independent taxpayer businesses. The invoice source format and direct-versus-partner transmission model remain undecided. See the product-specific section in [05 — BIR Requirements Gate & Development Workflow](05%20—%20BIR%20Requirements%20Gate%20%26%20Development%20Workflow.pdf). This classification is preliminary and must be confirmed with BIR / Philippine tax counsel before development.

## Recommended reading order

1. MVP Product Scope & Workflow
2. BIR Regulatory & Provider Readiness
3. Technical Architecture & Conceptual Data Model
4. Development Roadmap & Implementation Plan

## Organization principles

- Keep this page as the project hub and overview.
- Keep detailed requirements in the page with the matching subject; avoid unnecessary duplication.
- Distinguish confirmed decisions from proposals and unresolved questions.
- Keep regulatory assumptions marked as unverified until supported by current official BIR materials.
- Pricing remains deferred; no pricing model or transaction rate has been approved.
- The project remains in planning mode. Do not write code until explicitly requested.
