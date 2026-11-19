# EIS Product Editions & Pricing Strategy

> Source: Notion — EIS (https://app.notion.com/p/41cd71c0838d815990a5c56962f31849) · Exported 2026-11-19

## Purpose

This page records the proposed commercial model for the EIS product. The figures below are **working pricing hypotheses for customer validation**, not approved final prices or commitments.

## Product scope

EIS will support two usage modes within one locally installed product:

1. **Standalone invoicing:** the business creates and manages invoices in EIS.
2. **Integration and transmission:** the business continues using an existing POS, accounting, ERP or invoicing system. EIS imports invoice data, validates and prepares it, then handles the BIR connection and submission tracking, subject to the applicable BIR requirements and authorization.

The preferred architecture is a shared invoicing and transmission engine. Standalone users create invoices within EIS; integration users feed invoice data into the same engine through Excel/CSV initially and supported system integrations over time.

## Recommended pricing model

Use an annual software license per taxpayer installation, plus a one-time implementation fee. Offer separate editions because the two customer groups receive different levels of functionality and value.

### Proposed editions

| Edition | Proposed annual license | Target customer |
| --- | --- | --- |
| EIS Standalone | ₱24,000–₱45,000 | Businesses that need a complete invoicing system or want to replace their existing invoicing workflow |
| EIS Integration | ₱15,000–₱30,000 | Businesses that already have a POS, accounting, ERP or invoicing system and need import, validation, BIR transmission and reconciliation |

These ranges are initial hypotheses. Validate willingness to pay, support costs and implementation effort before finalizing.

### Proposed launch tiers

| Package | Standalone / year | Integration / year |
| --- | --- | --- |
| Basic | ₱18,000 | ₱12,000 |
| Business | ₱30,000 | ₱22,000 |
| Professional | ₱48,000 | ₱36,000 |

Tier differentiation should be based on business complexity and service requirements, not invoice count alone.

- **Basic:** one installation, small operation, standard templates, limited users and standard support.
- **Business:** more users, permitted branch support, additional reports, higher processing capacity and priority support.
- **Professional:** complex operations, advanced permissions, higher processing capacity, multiple integrations and priority technical support.

Branch and multi-entity entitlements must be checked against taxpayer registration and the regulatory scope of the deployment. Do not assume one installation can serve unrelated legal entities under the on-premise treatment.

## One-time implementation and service fees

| Service | Proposed fee |
| --- | --- |
| Standard installation | ₱3,000–₱5,000 |
| Initial configuration and training | ₱5,000–₱8,000 |
| Standard Excel template mapping | Included or ₱2,000 |
| Custom Excel/CSV mapping | ₱5,000–₱10,000 |
| Standard third-party integration | ₱10,000–₱20,000 |
| Custom API/ERP integration | ₱20,000–₱60,000+ |
| Onsite installation | Quoted separately |

These are planning estimates. The final quote should reflect actual delivery effort, travel, complexity and ongoing maintenance obligations. Consider discounted implementation for a limited pilot cohort in exchange for structured feedback and permission to use the experience as a case study.

## Annual renewal inclusions

The annual renewal should cover:

- Software license renewal.
- Supported BIR specification and software compatibility updates.
- Security fixes and bug fixes.
- Standard technical support.
- Access to the latest supported software version.

Avoid lifetime licenses because regulatory, security and operating-system changes create ongoing maintenance costs.

Keep software maintenance distinct from taxpayer applications, permits, certification and regulatory consulting. A software license does not itself grant a taxpayer's PTI Electronic Invoice or EIS Certification, and sales materials must not imply otherwise.

## Pricing strategy: annual license versus per-invoice fees

The recommended primary model is annual licensing, not a pure per-invoice charge.

| Method | Assessment |
| --- | --- |
| Per invoice only | Can make bills unpredictable and discourage usage |
| Monthly subscription only | Predictable but less natural for locally installed software |
| Annual license | Recommended base model |
| Lifetime license | Not recommended due to continuing maintenance and compliance updates |
| Annual license plus capacity tiers | Recommended; use invoice volume as one capacity factor, not the sole pricing basis |

If transmission creates measurable variable costs, consider a fair-use allowance or additional capacity tier later. Do not introduce a per-invoice surcharge until actual costs and customer response are understood.

## How to determine sustainable prices

Measure the real cost of serving each installation:

- Installation, onboarding and training hours.
- Configuration and data-mapping effort.
- Average monthly support time.
- Software update and maintenance costs allocated per client.
- BIR specification changes and regression testing.
- Backup, restore, security and incident-response responsibilities.
- Payment processing, sales commissions and administration.
- Third-party services or infrastructure, where applicable.

Use this calculation as a starting point:

Annual license price = annual cost per client ÷ (1 − target gross margin)

Example: if annual support and maintenance cost is ₱10,000 and the target gross margin is 60%, the indicative annual price is ₱25,000. This is an illustrative calculation, not a forecast.

## Initial launch offers to test

| Offer | Annual license | Initial setup |
| --- | --- | --- |
| EIS Standalone — Business | ₱30,000 | ₱5,000 |
| EIS Integration — Business | ₱22,000 | ₱5,000 |

Treat these as introductory pilot offers only. Confirm product readiness, regulatory position, support capacity and actual delivery costs before public launch.

## Market positioning

The product's potential differentiators:

- Installed and operated on the taxpayer's own PC or server.
- Standalone invoicing option for businesses without a suitable system.
- Integration option for businesses that want to retain their existing system.
- Local control of invoice records, subject to the customer's own security and backup practices.
- Business-owner-operated workflow without requiring an accountant to perform routine transmission.

Competitor subscription prices may be useful as reference points, but comparisons must account for differences in hosting, features, support, transaction allowances, certifications and deployment model. Do not treat competitor list prices as directly comparable.

Do not claim that EIS is "BIR-approved" or "BIR-certified" unless the specific approval or certification has actually been obtained and the claim accurately describes its scope.

## Pilot validation plan

Before finalizing prices:

1. Interview 10–15 potential business customers across both usage modes.
2. Record their current invoicing/accounting software, invoice volume, users, branches and current software costs.
3. Test willingness to pay for Standalone versus Integration.
4. Pilot with approximately 5–10 businesses when regulatory and technical prerequisites permit.
5. Measure installation time, mapping effort, support requests, maintenance effort and actual usage.
6. Compare actual costs with the proposed tiers and adjust the annual license and setup fees.
7. Test annual payment as the default and quarterly payment as an optional alternative if customers request it.

## Product and architecture principle

Build one common invoice and transmission engine:

- Standalone customers create invoices inside EIS.
- Integration customers import invoices from existing systems.
- Both paths use shared validation, data preparation, transmission, response handling, reconciliation and audit logging.

This avoids maintaining two independent transmission implementations and makes future integrations easier to support.

## Regulatory and commercial assumptions to validate

This pricing proposal assumes the local installation model is genuinely eligible for the relevant on-premise treatment under RMC 110-2026. The precise exception, its conditions and the treatment of direct BIR transmission must be confirmed with the BIR or Philippine tax counsel before commercial deployment.

The taxpayer's own PTI Electronic Invoice and EIS Certification obligations under applicable BIR rules remain separate from our software license. Do not advertise guaranteed compliance or certification as an automatic consequence of purchasing EIS.

## Open decisions

- What invoice-volume or processing-capacity limits should each tier include?
- How should branch support be priced while respecting taxpayer registration and permitted deployment scope?
- Which POS/accounting/ERP integrations should be supported first?
- What support response times are included in each tier?
- Should quarterly payment be offered, and at what premium?
- What is the actual annual support and maintenance cost per installation?
- What pilot discount, if any, should be offered?

## Status

**Status: Proposed pricing strategy — not final.** No code or commercial commitment is implied. Pricing should be finalized after regulatory clarification, product scoping, customer interviews and pilot cost measurement.
