# 04 — Development Roadmap & Implementation Plan

> Source: Notion — EIS (https://app.notion.com/p/41cd71c0838d8182a473d1a9989ba26c) · Exported 2026-11-19

Provide an actionable sequence for taking the EIS SaaS from planning into development and a controlled pilot.

**Working constraint:** planning and documentation only at this stage. Do not generate application code or begin implementation until explicitly requested.

## Recommended delivery strategy

Build one narrow, end-to-end workflow first: business account → company profile → invoice data upload → validation → review/confirmation → processing/submission tracking → history.

Do not build the full accounting platform before proving this workflow and confirming the applicable BIR route.

## Phase 0 — Regulatory and commercial feasibility

**Goal:** establish that the proposed product and provider model can legally and operationally work.

Tasks:

- Determine whether the intended provider role requires ESP accreditation or another approval.
- Verify startup eligibility, financial/operational requirements and the current application process.
- Confirm whether a monthly upload workflow is permitted and appropriate for the intended taxpayers.
- Obtain the current official BIR technical documentation, schemas, test access and production onboarding requirements.
- Consult a Philippine tax/regulatory professional.
- Identify the first customer segment and likely pilot users.

Deliverables:

- Regulatory requirements matrix.
- Provider eligibility assessment.
- Confirmed or revised product workflow.
- List of regulatory dependencies and risks.

Exit criteria: the team understands the permitted product role and has a credible route to lawful testing and production.

## Phase 1 — Product requirements and UX

**Goal:** turn the MVP into a testable product specification.

Tasks:

- Write user stories for business registration, company setup and monthly upload.
- Define user roles and permissions.
- Define the supported import source and template.
- Define each invoice field and validation rule from authoritative requirements.
- Design the review, correction and confirmation process.
- Design batch status and error screens.
- Create wireframes for the business portal and internal admin portal.
- Define accessibility, usability and support expectations.

Deliverables:

- Product requirements document.
- User journey diagrams.
- Screen inventory and wireframes.
- Import template specification.
- MVP acceptance criteria.

Exit criteria: a business user can be walked through the entire proposed workflow using mockups and sample data.

## Phase 2 — Architecture and data design

**Goal:** make the core technical decisions needed to start safely.

Tasks:

- Confirm backend, frontend, database and hosting choices.
- Define modular-monolith boundaries.
- Define organization/company/branch/user relationships.
- Define tenant isolation and authorization rules.
- Define import, invoice, submission, attempt, response and audit entities.
- Define file storage, retention and backup approach.
- Define state machines and idempotency requirements.
- Define the versioned BIR adapter boundary.
- Define security and privacy requirements.

Deliverables:

- Architecture decision records.
- Component/context diagram.
- Conceptual and logical database schema.
- API/module responsibility outline.
- Security and privacy design.
- Deployment/environment design.

Exit criteria: the design supports the MVP without locking the system to an unverified BIR API contract.

## Phase 3 — Development foundation

**Goal:** create a deployable application skeleton before building business features.

Planned tasks (not to be executed until coding is authorized):

- Create source repository and branching strategy.
- Establish solution/project structure.
- Configure local development environment.
- Set up database migrations and test data strategy.
- Configure authentication and authorization.
- Implement organization/company context and tenant checks.
- Configure structured logging and error handling.
- Establish automated unit/integration testing.
- Establish development, test/staging and production environments.
- Configure CI/CD, secrets, backups and monitoring.

Deliverable: deployable application foundation with secure sign-in and organization/company access.

## Phase 4 — MVP workflow implementation

**Goal:** complete the first usable customer journey.

Recommended implementation order:

1. Registration and authentication.
2. Organization and company profile.
3. Branch setup where required.
4. User invitations and permissions.
5. Versioned template download.
6. Secure file upload and storage.
7. Import parsing and preview.
8. Row-level validation and error export.
9. Correction and re-upload workflow.
10. Batch review and totals.
11. User confirmation and audit event.
12. Internal processing state and queue.
13. Submission adapter interface and test/sandbox integration when available.
14. Submission status, errors and history.
15. Internal administration and support views.

Deliverable: complete workflow using test data and a simulated or authorized test integration.

## Phase 5 — Quality, security and regulatory testing

Test at minimum:

- Valid and invalid import files.
- Empty, malformed, oversized and malicious files.
- Duplicate invoices and repeated uploads.
- Partial batches and row-level failures.
- Concurrent users and large batches.
- Retry after timeouts and uncertain external outcomes.
- External service downtime and recovery.
- Unauthorized cross-tenant access.
- Role and permission boundaries.
- Backup restoration and disaster recovery.
- Audit completeness and data export.
- Reconciliation between local state and external acknowledgements.

Deliverables:

- Test plan and test evidence.
- Security assessment and remediation list.
- Performance results.
- Reconciliation evidence.
- Required BIR test/certification evidence.

## Phase 6 — Pilot and controlled launch

Tasks:

- Select a small pilot cohort.
- Onboard businesses and verify their company details.
- Provide import templates and onboarding instructions.
- Run controlled tests with representative data.
- Monitor import failures, support requests and processing time.
- Reconcile all test submissions.
- Gather feedback and prioritize fixes.
- Confirm regulatory approval and production access before live operation.
- Prepare support, incident response and customer communications.

Deliverable: pilot review and go/no-go decision for commercial launch.

## Indicative planning estimates

These are rough effort estimates for a small team, not commitments. Regulatory access, approval and integration readiness may dominate the schedule.

| Workstream | Indicative effort |
| --- | --- |
| Regulatory and product discovery | 1–2 weeks |
| Product and UX design | 1–2 weeks |
| Architecture and data design | 1–2 weeks |
| Development foundation | 1–2 weeks |
| Core upload and validation workflow | 3–5 weeks |
| Integration and compliance testing | Dependent on BIR documentation, test access and approval |
| Pilot and refinement | 2–3 weeks |

Do not use these estimates as a launch promise until the regulatory path and scope are confirmed.

## Suggested project work breakdown

### Discovery

- [ ] Confirm provider classification and accreditation route.
- [ ] Confirm the monthly workflow against official requirements.
- [ ] Obtain official schemas and integration documentation.
- [ ] Identify pilot customer profile.

### Product

- [ ] Finalize MVP scope.
- [ ] Define roles and permissions.
- [ ] Define import template and data dictionary.
- [ ] Define validation and error handling.
- [ ] Produce screen wireframes.
- [ ] Write acceptance criteria.

### Architecture

- [ ] Confirm technology stack.
- [ ] Approve module boundaries.
- [ ] Approve tenant model.
- [ ] Approve conceptual/logical schema.
- [ ] Define state machines and idempotency.
- [ ] Define security, privacy, backup and retention.

### Build readiness

- [ ] Create repository and development workflow.
- [ ] Define environments and deployment approach.
- [ ] Define testing strategy.
- [ ] Define observability and support operations.

### MVP delivery

- [ ] Build registration and company setup.
- [ ] Build import/upload and preview.
- [ ] Build validation and correction.
- [ ] Build batch confirmation and history.
- [ ] Build processing/submission tracking.
- [ ] Build admin support views.

### Launch readiness

- [ ] Complete security and privacy review.
- [ ] Complete regulatory tests and approvals.
- [ ] Run pilot and reconciliation.
- [ ] Approve production go-live.

## What to defer

Keep accounting, inventory, POS, payroll, payment gateway, tax-return preparation, deep third-party integrations, advanced accounting-firm dashboards and pricing mechanics out of the initial MVP.

The data model may anticipate future usage billing, but the pricing model and billable event remain undecided.

## Immediate next step

Do not start coding yet. Complete Phase 0 and Phase 1 first. The next concrete planning artifact should be a detailed end-to-end workflow and screen-by-screen specification based on the confirmed invoice source and BIR-compliant process.

## Related EIS documentation

See the EIS hub for the product scope, regulatory readiness and architecture documents.
