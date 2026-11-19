# EIS Documentation

## Requirements

1. Confirm you are outside ESP accreditation
   - Who: Vendor
   - When: Before selling
   - Needed for on-prem: Yes
   - Source: Written legal opinion from tax counsel; BIR clarification or ruling letter

2. ESP Accreditation Certificate (deferred)
   - Who: Vendor (if SaaS)
   - When: Before commercial SaaS
   - Needed for on-prem: No (deferred route)
   - Source: Electronic Invoicing Solutions Accreditation Certificate, valid 5 years

3. Current official API guide and JSON format
   - Who: Vendor
   - When: Before building the BIR connector
   - Needed for on-prem: Yes
   - Source: API Development Guide, JSON File Format workbook, Certification User Guide, BIR public key (portal login)

4. Taxpayer account on the EIS Certification Portal
   4a. Sign‑up for portal user ID and password
       - Who: Taxpayer
       - Source: Portal user ID and password
   4b. Create an application on the portal
       - Who: Taxpayer
       - Source: Accreditation ID (8 chars) and Application ID
   4c. Settings page on the portal
       - Who: Taxpayer
       - Source: Application Secret Key, EIS private key and key ID (shown once)
   4d. Each API login (automatic)
       - Who: Taxpayer's EIS install
       - Source: authToken (6 h) and Session Secret Key (generated at runtime)

5. Software registration (Acknowledgement Certificate)
   - Who: Taxpayer
   - When: Before PTI
   - Needed for on-prem: Yes
   - Source: RMO 9‑2021, RMC 5‑2021

6. PTI Electronic Invoice
   - Who: Taxpayer
   - When: Before first e‑invoice
   - Needed for on-prem: Yes
   - Source: RMC 98‑2026; PTI number in invoice JSON

7. EIS Certification
   - Who: Taxpayer
   - When: Within 6 months of PTI
   - Needed for on-prem: Yes
   - Source: RMC 98‑2026; EIS Certificate number

8. Static IP whitelisting (unconfirmed)
   - Who: Taxpayer
   - When: Before live transmission
   - Needed for on-prem: Yes
   - Source: Confirmation that public IP(s) are registered for production (no ID)

9. Permit to Transmit (PTT)
   - Who: Taxpayer
   - When: When BIR activates sales reporting
   - Needed for on-prem: Later
   - Source: RMC 98‑2026

10. Manual invoice fallback
   - Who: Taxpayer
   - When: Ongoing
   - Needed for on-prem: Yes
   - Source: RMC 98‑2026; pre‑printed Authority to Print invoices

11. Product rules the software must enforce
    - Who: Vendor
    - When: During build
    - Needed for on-prem: Yes
    - Source: Not specified (internal product rules)