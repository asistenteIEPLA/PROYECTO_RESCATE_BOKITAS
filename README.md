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

## 📊 International Compliance Reports

Scientific compliance reports are available in multiple languages. To ensure the highest quality and data integrity, these reports are provided in **RMarkdown (.Rmd)** format for native processing.

### 🛠️ Processing in RStudio
High-quality digital versions can be generated directly by the user:
1.  Open [RStudio](https://rstudio.com/).
2.  Navigate to `docs/international/`.
3.  Open the desired `.Rmd` file.
4.  Execute `Knit to PDF` or `Knit to HTML` for local distribution.

| Language | Source File (RMD) | Policy Standard |
| :--- | :--- | :--- |
| 🇪🇸 **Spanish** | [INFORME_COMPLIANCE_GRI.Rmd](INFORME_COMPLIANCE_GRI.Rmd) | GRI 203 / 418 |
| 🇺🇸 **English** | [INFORME_COMPLIANCE_EN.Rmd](docs/international/INFORME_COMPLIANCE_EN.Rmd) | GRI 203 / 418 |
| 🇫🇷 **French** | [INFORME_COMPLIANCE_FR.Rmd](docs/international/INFORME_COMPLIANCE_FR.Rmd) | GRI 203 / 418 |
| 🇸🇦 **Arabic** | [INFORME_COMPLIANCE_AR.Rmd](docs/international/INFORME_COMPLIANCE_AR.Rmd) | RTL |
| 🇮🇱 **Hebrew** | [INFORME_COMPLIANCE_HE.Rmd](docs/international/INFORME_COMPLIANCE_HE.Rmd) | RTL |

---
*Maintained by the Data Intelligence Team - BOKITAS*

---
*Maintained by the Data Intelligence Team - BOKITAS*
