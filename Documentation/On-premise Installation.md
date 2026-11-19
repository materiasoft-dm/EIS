# On-premise Installation

> Source: Notion — EIS (https://app.notion.com/p/41cd71c0838d81639c14e1ef893d1042) · Exported 2026-11-19

## Executive summary

The preferred deployment direction for the EIS project is **Model A: locally installed software operated on the taxpayer's own computer or server**. The business owner and authorized staff operate the system directly. The installation is dedicated to one taxpayer and its registered branches; it does not serve unrelated legal entities from a shared installation.

This model is attractive because RMC 110-2026 describes an exclusion from its ESP accreditation framework for an internally developed system, or software licensed to a taxpayer and operated on that taxpayer's own infrastructure, when used exclusively by one taxpayer and its registered branches. The exclusion is conditional and must be implemented carefully.

**Regulatory status:** promising interpretation, not yet confirmed by BIR or Philippine tax counsel. Do not market the product as BIR-approved, accredited, certified, or exempt until the applicable requirements and written BIR position are confirmed.

## 1. Proposed product model

- **Deployment:** installed on the business's own PC or server.
- **Operator:** business owner and authorized employees; accountant access is optional and delegated by the taxpayer.
- **Customer boundary:** one taxpayer/legal entity and its registered branches per installation and configuration.
- **Transmission:** the local installation communicates directly with BIR endpoints, subject to the official technical contract, taxpayer authorization, testing, and applicable permits/certification.
- **Commercial model:** software license plus support/maintenance is a possible model. Pricing remains undecided.
- **Cloud role:** no shared cloud service should perform core invoice validation, storage, middleware, or BIR transmission in a way that changes the substance of the arrangement into a third-party ESP service. Optional remote licensing/update services need separate review.

## 2. Regulatory implications

### 2.1 RMC 110-2026 — potential ESP exclusion

RMC 110-2026 states that an internally developed system, or software licensed to a taxpayer and operated on the taxpayer's own infrastructure, used exclusively by one taxpayer and its registered branches, is not covered by that circular and remains governed by existing CAS, POS, or other applicable registration rules.

It also states that a system or service offered to an affiliate, subsidiary, related party, franchisee, customer, or any other separate juridical entity is treated as an ESP service unless exempted by the BIR. A provider may request an exemption in writing from the concerned RDO or Large Taxpayers Service office.

**Practical interpretation for our product:**

- License a separate installation to each taxpayer.
- The taxpayer controls the computer/server, data, operation, and BIR configuration.
- Avoid a shared multi-tenant transmission service operated by our company.
- Do not allow one customer's installation or account to process invoices for other independent legal entities.
- A group of companies, franchisees, affiliates, or subsidiaries should be treated as separate taxpayers for this analysis unless BIR confirms otherwise.
- If our company remotely operates, hosts, stores, validates, transforms, or transmits data for customers, the arrangement may be viewed differently despite the software being installed locally.

The exact scope of "taxpayer's own infrastructure" and whether direct transmission by the installed software falls within the exclusion should be confirmed in writing with BIR/tax counsel.

### 2.2 RMC 98-2026 — taxpayer obligations still apply

The potential ESP exclusion does **not** exempt the customer from electronic invoicing requirements.

RMC 98-2026 provides that covered taxpayers must:

- Use an eligible registered/approved/accredited invoicing system that generates structured electronic invoice data.
- Electronically generate and deliver the invoice to the buyer through an accepted digital means.
- Ensure invoice data can be electronically extracted, processed, and transmitted to BIR.
- Obtain a PTI Electronic Invoice before generating or issuing electronic invoices, where required.
- Obtain EIS Certification within six months from PTI issuance.
- Observe the applicable branch coverage and system identification requirements.

The PTI identifies the approved software/system and its coverage. Changes to the software identity, name, platform, or core system details may require a new or amended PTI. Each head office and branch must be correctly covered.

The taxpayer remains responsible for invoice correctness and compliance even when it buys commercial software.

### 2.3 Excel import limitation

Excel can be an import mechanism for structured data exported from an existing invoicing or accounting system. However, RMC 98-2026 says invoices manually created using Excel, Word, Google Sheets, or similar office productivity applications are not valid electronic invoices for tax compliance purposes.

Therefore:

- Accept Excel as a migration/import format where the underlying invoice was generated by a compliant source system, subject to BIR confirmation of the workflow.
- Do not treat a manually prepared Excel spreadsheet as a valid electronic invoice merely because our software later converts and transmits its data.
- The product should ultimately generate and issue compliant electronic invoices itself, or integrate with the taxpayer's approved source invoicing system.

### 2.4 Electronic invoicing vs electronic sales reporting

RMC 98-2026 distinguishes electronic invoice issuance under Section 237 from electronic sales reporting under Section 237-A. The sales-reporting obligation applies upon issuance of BIR implementing policies/guidelines/procedures and the relevant CIR direction.

The product must support the requirements confirmed by the current BIR EIS technical pack. Do not assume every invoice must be transmitted in real time as Section 237-A sales-reporting data until the BIR confirms the applicable process.

The circular also states that a Permit to Transmit (PTT) applies upon notification or directive from the CIR for Section 237-A reporting. PTI Electronic Invoice and EIS Certification are separate taxpayer requirements.

## 3. Recommended architecture

### 3.1 Local application

A Windows-first desktop application or locally hosted web application is recommended for the initial target market. The software runs on the taxpayer's own PC or server.

Proposed components:

- **User interface:** desktop UI or browser UI served only on the local network/device.
- **Local application service:** invoice lifecycle, business rules, validation, document numbering, and BIR integration orchestration.
- **Local database:** stores company configuration, customers, products/services, invoices, submission attempts, responses, and audit history.
- **Local document storage:** generated invoice files and supporting artifacts.
- **BIR connector:** versioned adapter for official BIR schemas, authentication, endpoints, response codes, and certification test cases.
- **Background worker:** handles queued transmissions, retry scheduling, status checks, and reconciliation.
- **Update and licensing client:** verifies license and downloads signed updates; should not require our cloud to process or relay invoice data.

### 3.2 High-level data flow

1. Taxpayer configures company identity, branches, tax details, BIR credentials, and approved software details.
2. Authorized user creates an invoice in the local application or imports eligible structured data from a source system.
3. Application validates required fields, tax calculations, customer details, numbering, and document rules.
4. Application generates the compliant electronic invoice and delivers it to the buyer through an approved digital channel.
5. The invoice and its immutable issued representation are saved locally.
6. The local transmission worker prepares the required BIR payload and sends it directly to BIR over a secure outbound connection, when the applicable BIR process requires transmission.
7. The application records the request, response, timestamps, identifiers, and status.
8. Users review accepted/rejected results, correct errors using compliant adjustment documents, and reconcile local records against BIR responses.

### 3.3 Reliability and security principles

- Outbound-only network communication where possible; no public inbound ports required.
- TLS and current BIR-required authentication/signature mechanisms.
- Protect secrets and taxpayer credentials using OS-protected secret storage; never store credentials in plain text.
- Encrypt sensitive local data and backups.
- Use transactional local queues and idempotency controls to avoid duplicate submissions after crashes or timeouts.
- Preserve immutable issued invoice records. Corrections should use separate documents referencing the original invoice, not editing or deleting issued invoices.
- Maintain tamper-evident audit logs for invoice creation, issuance, delivery, transmission, response, correction, user access, and configuration changes.
- Provide backup, restore, retention, and disaster-recovery procedures.
- Handle offline operation and downtime according to BIR rules, including authorized manual invoice contingency and subsequent replacement where required.
- Digitally sign software updates and maintain release/version history.
- Keep BIR integration schemas and endpoints versioned and replaceable.
- Provide diagnostics and exportable support logs while minimizing exposure of taxpayer data.

## 4. What our company should and should not operate

| Function | Recommended responsibility |
| --- | --- |
| Invoice creation, validation and local storage | Taxpayer's local installation |
| BIR payload preparation and transmission | Taxpayer's local installation |
| BIR credentials and taxpayer configuration | Controlled by taxpayer |
| Invoice and submission audit history | Stored locally and controlled by taxpayer |
| Software licensing | Our company, with minimal metadata |
| Signed software updates | Our company distributes; customer installation applies them |
| Optional remote support | Customer-authorized, logged, and privacy-controlled |
| Centralized invoice storage or shared transmission relay | Avoid unless separately assessed and authorized |
| Multi-company processing for separate legal entities | Not part of this on-premise model without BIR approval/accreditation |

## 5. Product boundaries and risks

The deployment model must be real in substance, not just a locally installed user interface connected to a backend that performs the regulated service centrally.

Potential risk factors:

- Our servers receive and store invoice content or structured sales data.
- Our cloud validates, transforms, queues, or transmits invoices for multiple taxpayers.
- One installation is used by an accounting firm to process invoices for multiple separate client entities.
- A license is shared across separate legal entities.
- We remotely operate the system or control taxpayer transmission credentials.
- Our support team routinely accesses customer invoice data without a clear authorization and data governance process.

Any of these could change the regulatory analysis. Obtain advice before adding cloud features that process taxpayer data.

## 6. Decisions and questions to confirm with BIR

Before finalizing the design, seek written clarification on:

1. Does the RMC 110-2026 exclusion apply to a commercially licensed, locally installed invoicing application that prepares and transmits the taxpayer's own invoice data directly to BIR?
2. What exactly qualifies as the taxpayer's "own infrastructure" (single PC, on-premise server, private cloud, or customer-controlled virtual machine)?
3. Can the vendor provide signed updates, license validation, and remote technical support without being treated as providing ESP services?
4. What CAS/CBA/POS registration, PTI, EIS Certification, and other approvals are required for the commercial software and for each taxpayer?
5. What is the current production transmission workflow under Section 237, and what is the separate process for Section 237-A sales reporting?
6. What official API specifications, authentication, encryption, certificates, callbacks, acknowledgements, retry rules, and test cases must be implemented?
7. Can a taxpayer's registered branches use the same installation and system, and how must branch coverage be reflected in the PTI?
8. If the vendor supplies the same licensed product to many unrelated taxpayers through separate local installations, does any part of the vendor's activity still trigger ESP obligations?

## 7. Recommended go/no-go gates

- [ ] Obtain the signed full text and Annex A of RMC 110-2026 and have counsel interpret the on-premise exclusion.
- [ ] Request written BIR clarification on our exact deployment, support, licensing, and direct-transmission model.
- [ ] Obtain the current official EIS Certification technical pack and production integration documentation.
- [ ] Confirm the applicable CAS/CBA/POS registration route for our software.
- [ ] Define taxpayer PTI and EIS Certification responsibilities and branch coverage.
- [ ] Confirm whether the product itself must be tested/certified and how the BIR identifies each version.
- [ ] Validate invoice delivery, immutable records, corrections, downtime, and audit requirements.
- [ ] Only then approve the final architecture and begin implementation.

## 8. Current recommendation

Proceed with Model A as the **preferred architecture for planning**, but keep regulatory status as an unresolved gate. Design the software as a taxpayer-controlled, single-entity local installation with direct outbound BIR connectivity. Keep cloud functions limited to licensing, signed updates, and optional customer-authorized support unless BIR confirms a broader role is permitted.

Do not build a shared cloud transmission backend as a hidden dependency of the on-premise application. That could undermine the regulatory rationale for choosing this model.

## Sources

- [RMC 110-2026 — BIR official circular listing](https://www.bir.gov.ph/2026-Revenue-Memorandum-Circulars) (open the Full Text and Annex A entry for RMC 110-2026).
- [RMC 110-2026 — reproduced text including the on-premise exclusion](https://batasnatin.com/laws/rmc-no-110-2026-prescribing-the-accreditation-technical-operational-securi).
- [RMC 98-2026 — BIR official digest](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2098-2026%20Digest.pdf).
- [BIR EIS Certification Portal](https://eis-cert.bir.gov.ph/).

This page is a product and architecture planning document, not legal advice or confirmation of BIR approval. No code is being written at this stage.
