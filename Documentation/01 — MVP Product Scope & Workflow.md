# 01 — MVP Product Scope & Workflow

> Source: Notion — EIS (https://app.notion.com/p/41cd71c0838d814eada4cc51cc5ddf25) · Exported 2026-11-19

Define the first useful release of the EIS SaaS. The initial product is intentionally narrow: help businesses prepare, upload, validate, review, and track invoice data. It is not initially a full accounting, POS, inventory, or invoice-creation system.

## Product vision for the first release

Provide a secure business portal where an authorized user can submit invoice data for a reporting period, correct validation issues, confirm a batch, and track the resulting processing/submission status.

**Important distinction:** A monthly upload to this SaaS is a proposed customer workflow. It must not be represented as the BIR-prescribed reporting or electronic-invoice process until current BIR rules and the applicable provider requirements have been verified.

## Target customer journeys

### Direct business

1. Business registers an organization.
2. Business creates or verifies its registered company profile.
3. Business invites authorized users.
4. User selects the reporting period.
5. User downloads the agreed import template.
6. User uploads invoice data from an existing system or spreadsheet.
7. System previews records and runs validation.
8. User corrects errors and re-uploads or edits permitted fields.
9. User reviews the batch totals and confirms it.
10. System processes the batch and displays status, errors, references, and history.

### Accounting firm

Accounting firms are part of the longer-term product direction. The data model should support a firm managing multiple client companies with explicit per-client permissions. The initial release may prioritize direct businesses if that materially reduces delivery complexity, but the architecture should not make the firm model impossible.

## MVP functional scope

| Capability | MVP expectation |
| --- | --- |
| Registration and sign-in | Secure account creation and authentication |
| Organization/company setup | Capture legal name, TIN, registered address, tax profile and relevant identifiers |
| Branch setup | Support branch records where required |
| User access | Owner/admin and authorized submitter roles at minimum |
| Import template | Download a documented CSV/Excel template |
| Upload | Accept supported file formats with size/type controls |
| Preview | Show parsed invoice records before committing |
| Validation | Identify missing, malformed, inconsistent and duplicate data |
| Correction | Explain errors and allow correction/re-upload |
| Batch review | Show counts and monetary/tax totals before confirmation |
| Processing | Track each batch through defined internal states |
| Submission tracking | Store external references and responses when an authorized integration is available |
| History | Search and view prior batches and records |
| Admin support | Inspect organizations, batches, errors and operational status |
| Audit | Record important user and system actions |

## Out of scope for MVP

- General ledger and bookkeeping
- Full accounting package
- Inventory and purchasing
- POS and cashiering
- Payroll
- Payment gateway
- Automated tax return preparation
- Product catalogue management beyond what is required for invoice import
- Deep integrations with accounting platforms
- Advanced accounting-firm consolidated dashboards
- Final transaction pricing, wallet, prepaid credits or postpaid billing

## Invoice import design principles

- Publish a versioned template with clear field definitions and examples.
- Preserve the original uploaded file for traceability, subject to retention and privacy requirements.
- Store parsed invoice data separately from the uploaded file.
- Identify each import batch by organization, company, reporting period, upload time and uploader.
- Detect duplicate records using a defined business key; do not rely only on filename.
- Do not silently discard invalid rows.
- Provide downloadable error results that identify the row, field and reason.
- Make import retries safe and idempotent.
- Keep source data, normalized data and any transformed submission payload distinguishable.

## Conceptual batch lifecycle

Draft → Uploaded → Parsing → Validation failed / Ready for review → Confirmed → Processing → Completed / Partially completed / Failed.

These are proposed internal workflow states, not official BIR status codes. The final state model must reflect the approved BIR process and distinguish internal processing from external acceptance.

## Core screens

1. Sign in / account creation
2. Organization and company profile
3. Branch management
4. User and access management
5. Submission dashboard
6. New monthly batch
7. Template download and upload
8. Import preview
9. Validation results
10. Batch review and confirmation
11. Batch details and processing timeline
12. Submission history
13. Platform administration

## MVP acceptance criteria

- A business can register and maintain its company profile.
- An authorized user can upload a valid supported file.
- The system can preview and validate records before confirmation.
- Invalid records have actionable row/field-level explanations.
- Re-uploading or retrying does not create unintended duplicate invoices or duplicate external submissions.
- A user can see batch totals and confirm the batch.
- The system preserves the upload, normalized records, processing events and available external responses.
- Users cannot access another organization's records.
- Admins can investigate failures without altering source records invisibly.

## Decisions still required

- Confirm whether the first supported source is CSV, Excel, manual entry, or a combination.
- Confirm the exact BIR-required invoice fields and data format.
- Confirm whether the first customer cohort is direct businesses only or includes accounting firms.
- Confirm the reporting period rules and whether the assumed monthly process is valid.
- Confirm supported document types and correction workflows.
- Confirm file size, invoice volume and retention limits.

## Related EIS documentation

See the EIS hub for the regulatory, architecture and development planning documents.
