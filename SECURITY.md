# Security Policy and Data Privacy (GRI 418)

## Overview
This repository is dedicated to the **Bokitas Data Intelligence** platform development. Under the **GRI 418: Customer Privacy** standard, we are committed to protecting all individual data. This repository contains only application code and anonymized/mock data structures. **Zero real patient or beneficiary data (PII) is permitted in this public-facing codebase.**

## Data Protection Compliance
- **GDPR Compliance:** All data processing logic implemented in this software follows the principles of data minimization, purpose limitation, and storage limitation.
- **Anonymization:** Any demonstration datasets provided are synthesized "Mock" data.
- **Access Control:** Production credentials and sensitive migration assets are strictly managed via environment variables and excluded from version control.

## Reporting a Vulnerability
We strongly encourage security researchers and developers to report any potential security issues or accidental data exposures.

### Reporting Process
1.  **Do not create a public issue** for security vulnerabilities.
2.  Send a detailed report to the security team at: **security-bokitas@iepla.org** (Example)
3.  Include a description of the vulnerability, steps to reproduce, and potential impact.

## Security Audit History
- **Initial Audit (2026-04-18):** Full repository scan for PII and secrets before public synchronization. Implementation of strict `.gitignore` and `.env.example`.

---
*Maintained by the Cybersecurity & Compliance Team*
