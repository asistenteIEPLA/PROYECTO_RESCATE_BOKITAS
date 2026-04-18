# Bokitas Data Intelligence

[Read this in English](README.md)

[![Security: GRI 418](https://img.shields.io/badge/Security-GRI_418-blue.svg)](SECURITY.md)
[![License: Propitery](https://img.shields.io/badge/License-Proprietary-red.svg)]()
[![Status: Secured](https://img.shields.io/badge/Status-Secured-success.svg)]()

Plataforma inteligente para la gestión, análisis y visibilidad de salud nutricional infantil. Este proyecto representa la evolución tecnológica de un sistema legacy hacia una arquitectura moderna basada en la nube.

## 🌟 Resumen de Fases
1. **Fase 1: Arqueología de Datos:** Ingeniería inversa forense de FoxPro 2.6, recuperación de 25 tablas y extracción de lógica.
2. **Fase 2: Normalización:** Adaptación de campos a los estándares de la OMS (Z-Scores) y Graffar-Méndez Castellano.
3. **Fase 3: Seguridad:** Aplicación del protocolo GRI 418, anonimización de datos y limpieza de historial Git.
4. **Fase 4: Arquitectura:** Diseño de esquema SQL Maestro para Supabase, Vercel, Docker e integración con R.

## 🛠 Metodología y Estándares de Calidad
- **Cálculo Nutricional:** Implementación de la metodología **WHO Child Growth Standards** utilizando librerías validadas en **R (Anthro)**.
- **Clasificación Social:** Automatización del indicador **Graffar-Méndez Castellano**.
- **Ciberseguridad:** Cumplimiento estricto del estándar **GRI 418: Privacidad del Cliente**.

## 📦 Stack Tecnológico
- **Cloud Backend:** [Supabase](https://supabase.com/) (PostgreSQL + Realtime).
- **Frontend Dashboard:** Next.js / Streamlit.
- **Analítica:** Motor de R para Z-Scores avanzados.
- **Contenerización:** Docker para despliegues reproducibles.
- **Legacy Source:** Visual FoxPro 2.6.

## 🔐 Guía de Inicio Seguro
Para proteger la privacidad de los menores, este repositorio **no contiene datos reales**.

1.  **Configuración de Entorno:** Copia `.env.example` a `.env` y configura tus llaves.
2.  **Mock Data:** Utiliza los archivos en `output/raw_csv/` (versiones anonymizadas) para pruebas locales.
3.  **Herramientas:** Los scripts de auditoría se encuentran en `scratch/`.

## 🌍 Centro de Soporte Internacional y Descargas
Los informes oficiales de cumplimiento y sostenibilidad están disponibles en varios idiomas:

| Idioma | Reporte en Vivo (RMD) | Versión Digital (HTML) | Formato de Salida |
| :--- | :--- | :--- | :--- |
| 🇪🇸 **Español** | [Link](INFORME_COMPLIANCE_GRI.Rmd) | [Descargar](dist/reports/INFORME_COMPLIANCE_ES.html) | HTML/Imprimible |
| 🇺🇸 **Inglés** | [Link](docs/international/INFORME_COMPLIANCE_EN.Rmd) | [Descargar](dist/reports/INFORME_COMPLIANCE_EN.html) | HTML/Imprimible |
| 🇫🇷 **Francés** | [Link](docs/international/INFORME_COMPLIANCE_FR.Rmd) | [Descargar](dist/reports/INFORME_COMPLIANCE_FR.html) | HTML/Imprimible |
| 🇸🇦 **Árabe** | [Link](docs/international/INFORME_COMPLIANCE_AR.Rmd) | [Descargar](dist/reports/INFORME_COMPLIANCE_AR.html) | Soporte RTL |
| 🇮🇱 **Hebreo** | [Link](docs/international/INFORME_COMPLIANCE_HE.Rmd) | [Descargar](dist/reports/INFORME_COMPLIANCE_HE.html) | Soporte RTL |

---
*Mantenido por el equipo de Inteligencia de Datos - BOKITAS*
