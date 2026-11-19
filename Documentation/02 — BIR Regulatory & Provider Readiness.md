# 02 — BIR Regulatory & Provider Readiness

> Source: Notion — EIS (https://app.notion.com/p/41cd71c0838d81d59b76dae45af3274c) · Exported 2026-11-19

Track the regulatory questions that must be answered before the product's submission workflow and BIR integration are finalized.

This document is a planning checklist, not legal advice and not confirmation that the product or its operator is accredited, certified, or authorized by the BIR.

## Critical product distinction

Do not assume that these are interchangeable:

- Electronic invoice creation and issuance
- Electronic transmission of invoice data
- Periodic or monthly sales/invoice reporting
- Use of an accredited Electronic Invoicing Service Provider (ESP)
- Use of BIR-provided systems or another permitted reporting channel

The proposed SaaS workflow—business uploads invoice data monthly—must be checked against the actual obligation and approved technical route applicable to each target taxpayer.

## Regulatory workstream

### 1. Determine the provider role

- [ ] Establish whether the planned business model makes the company an ESP or another category of service provider.
- [ ] Identify whether ESP accreditation, certification, registration, or other approval is required.
- [ ] Confirm whether a startup can meet the eligibility requirements.
- [ ] Review financial, operational, security, staffing, service continuity and transaction-volume requirements.
- [ ] Determine whether requirements differ for software vendors, intermediaries, and taxpayers using their own systems.
- [ ] Obtain advice from a Philippine tax/regulatory professional.

### 2. Obtain authoritative BIR materials

- [ ] Current circulars, revenue regulations and implementing guidance.
- [ ] Current EIS/ESP technical specifications and API documentation.
- [ ] Official schemas, field definitions and validation rules.
- [ ] Authentication and authorization requirements.
- [ ] Cryptographic/signature requirements, if applicable.
- [ ] Test environment access and test cases.
- [ ] Error/result codes and rejection handling.
- [ ] Certification/accreditation process and required evidence.
- [ ] Production onboarding, credentials and operational requirements.
- [ ] Retention, audit and taxpayer access requirements.

Record each source's title, issuing office, publication/effective date, URL, version and date checked. Prefer official BIR sources over summaries.

### 3. Confirm the taxpayer workflow

- [ ] Which taxpayers are covered and under what conditions?
- [ ] What documents and transactions are covered?
- [ ] Is invoice issuance required at transaction time?
- [ ] Is a separate periodic reporting requirement applicable?
- [ ] Is monthly batch upload an accepted channel, and under what conditions?
- [ ] What are the reporting periods and deadlines?
- [ ] How are corrections, replacements, cancellations, credit notes and debit notes handled?
- [ ] What evidence or acknowledgement must be returned to the taxpayer?
- [ ] What happens when the BIR service is unavailable?

### 4. Security, privacy and operational requirements

- [ ] Map personal and business data processed by the platform.
- [ ] Establish applicable Data Privacy Act obligations and controller/processor roles.
- [ ] Define data processing agreements and customer terms.
- [ ] Define access controls, encryption, key management and audit logging.
- [ ] Define retention, deletion, export and legal-hold policies.
- [ ] Define incident response and breach notification procedures.
- [ ] Define backup, disaster recovery and business continuity.
- [ ] Assess hosting and cross-border data transfer implications.
- [ ] Define support access controls and privileged-access auditing.

## Regulatory gates before production

**Gate A — Business model:** provider classification and eligibility are understood.

**Gate B — Technical contract:** current official schemas, interface, security controls and response semantics are obtained and versioned.

**Gate C — Test access:** the team has a legitimate test route and documented test scenarios.

**Gate D — Approval:** all required accreditation, certification, registration and production onboarding steps are completed.

**Gate E — Operational readiness:** security, privacy, support, monitoring, incident response and continuity controls are in place.

Do not advertise BIR approval, accreditation, certification or production connectivity before the relevant status has been formally obtained and verified.

## Integration design implications

- Keep the BIR integration behind a versioned adapter.
- Do not hardcode unverified endpoints, schemas, cryptographic algorithms or response codes.
- Preserve the original invoice data and the exact outbound payload/version used for each attempt.
- Store request timestamps, response timestamps, external references and full normalized error details.
- Distinguish invoice/document status from transmission status.
- Use idempotency and duplicate-prevention controls.
- Support retries only when the applicable protocol makes retry safe.
- Reconcile local records against external acknowledgements.

## Research log template

For each regulatory finding, record:

| Field | Description |
| --- | --- |
| Topic | Requirement or question |
| Official source | Circular, regulation, technical guide or BIR page |
| Issuing authority | BIR office or other regulator |
| Publication/effective date | As stated by source |
| Version checked | Document/API/schema version |
| Finding | Concise requirement |
| Product impact | Workflow, data, security or operations affected |
| Confidence | Confirmed / needs interpretation / unresolved |
| Follow-up | Owner and next action |

## Immediate next actions

1. Obtain the latest official ESP accreditation circular and annexes.
2. Ask a qualified Philippine tax/regulatory adviser to assess provider eligibility and the proposed monthly-upload model.
3. Request or locate the current official technical pack and production onboarding instructions.
4. Build a compliance requirements matrix before finalizing invoice fields or submission states.
5. Decide whether to pursue provider accreditation, partner with an accredited provider, or build a taxpayer-side tool using an officially permitted route.

## Related EIS documentation

See the EIS hub for the MVP, architecture and development roadmap.
