# Bokitas Data Intelligence

[Leer esto en Español](README.es.md)

[![Security: GRI 418](https://img.shields.io/badge/Security-GRI_418-blue.svg)](SECURITY.md)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)]()
[![Status: Secured](https://img.shields.io/badge/Status-Secured-success.svg)]()

Intelligent platform for the management, analysis, and visibility of child nutritional health. This project represents the technological evolution of a legacy system into a modern cloud-based architecture.

## 🌟 Phase Summary
1. **Phase 1: Database Archaeology:** Forensic reverse engineering of FoxPro 2.6, recovery of 25 tables, and business logic extraction.
2. **Phase 2: Data Normalization:** Adaptation of fields to WHO (Z-Scores) and Graffar-Méndez Castellano standards.
3. **Phase 3: Security & Anonymization:** Implementation of GRI 418 protocol, PII isolation, and Git history sanitization.
4. **Phase 4: Architecture Design:** SQL Master schema for Supabase, Vercel, Docker, and R integration.

## 🛠 Methodology and Quality Standards
- **Nutritional Calculation:** Implementation of the **WHO Child Growth Standards** methodology using validated libraries in **R (Anthro)**.
- **Social Classification:** Automation of the **Graffar-Méndez Castellano** indicator.
- **Cybersecurity:** Strict compliance with the **GRI 418: Customer Privacy** standard.

## 📦 Tech Stack
- **Cloud Backend:** [Supabase](https://supabase.com/) (PostgreSQL + Realtime).
- **Frontend Dashboard:** Next.js / Streamlit.
- **Analytics:** R Engine for advanced Z-Scores.
- **Containerization:** Docker for reproducible deployments.
- **Legacy Source:** Visual FoxPro 2.6.

## 🔐 Secure Quick Start
To protect the privacy of minors, this repository **does not contain real data**.

1.  **Environment Setup:** Copy `.env.example` to `.env` and configure your API keys.
2.  **Mock Data:** Use the files in `output/raw_csv/` (anonymized versions) for local testing and development.
3.  **Audit Tools:** Reverse engineering and security scripts are located in `scratch/`.

## 🌍 International Support & Download Center
Official compliance and sustainability reports are available in multiple languages:

| Language | Live Report (RMD) | Digital Version (HTML) | Output Format |
| :--- | :--- | :--- | :--- |
| 🇪🇸 **Spanish** | [Link](INFORME_COMPLIANCE_GRI.Rmd) | [Download](dist/reports/INFORME_COMPLIANCE_ES.html) | HTML/Printable |
| 🇺🇸 **English** | [Link](docs/international/INFORME_COMPLIANCE_EN.Rmd) | [Download](dist/reports/INFORME_COMPLIANCE_EN.html) | HTML/Printable |
| 🇫🇷 **French** | [Link](docs/international/INFORME_COMPLIANCE_FR.Rmd) | [Download](dist/reports/INFORME_COMPLIANCE_FR.html) | HTML/Printable |
| 🇸🇦 **Arabic** | [Link](docs/international/INFORME_COMPLIANCE_AR.Rmd) | [Download](dist/reports/INFORME_COMPLIANCE_AR.html) | RTL Support |
| 🇮🇱 **Hebrew** | [Link](docs/international/INFORME_COMPLIANCE_HE.Rmd) | [Download](dist/reports/INFORME_COMPLIANCE_HE.html) | RTL Support |

---
*Maintained by the Data Intelligence Team - BOKITAS*
