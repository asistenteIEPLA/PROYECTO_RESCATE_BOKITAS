# Inteligencia de Recuperación de Data Bokitas

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

## 🧪 Calidad y Validación Clínica
Para garantizar la confianza absoluta de donantes y aliados, cada cálculo clínico es auditado automáticamente:
- **Pruebas Clínicas:** Tests unitarios en `/tests` verifican que el motor de Z-Scores coincida con los valores de control del **Gold Standard de la OMS**.
- **Integridad de Datos:** Chequeos rutinarios aseguran que ninguna medida viole límites biológicos (protección contra desbordamientos).
- **Auditoría:** Ejecutar pruebas con `python tests/test_z_scores.py`.

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

## 📊 Informes de Cumplimiento Internacional

Los informes científicos de cumplimiento están disponibles en varios idiomas. Para garantizar la máxima calidad e integridad de los datos, estos informes se suministran en formato **RMarkdown (.Rmd)** para su procesamiento nativo.

### 🛠️ Procesamiento en RStudio
El usuario puede generar versiones digitales de alta calidad directamente:
1.  Abrir [RStudio](https://rstudio.com/).
2.  Navegar a la carpeta `docs/international/`.
3.  Abrir el archivo `.Rmd` deseado.
4.  Ejecutar `Knit to PDF` o `Knit to HTML` para distribución local.

| Idioma | Archivo Fuente (RMD) | Estándar de Política |
| :--- | :--- | :--- |
| 🇪🇸 **Español** | [INFORME_COMPLIANCE_GRI.Rmd](INFORME_COMPLIANCE_GRI.Rmd) | GRI 203 / 418 |
| 🇺🇸 **Inglés** | [INFORME_COMPLIANCE_EN.Rmd](docs/international/INFORME_COMPLIANCE_EN.Rmd) | GRI 203 / 418 |
| 🇫🇷 **Francés** | [INFORME_COMPLIANCE_FR.Rmd](docs/international/INFORME_COMPLIANCE_FR.Rmd) | GRI 203 / 418 |
| 🇸🇦 **Árabe** | [INFORME_COMPLIANCE_AR.Rmd](docs/international/INFORME_COMPLIANCE_AR.Rmd) | Soporte RTL |
| 🇮🇱 **Hebreo** | [INFORME_COMPLIANCE_HE.Rmd](docs/international/INFORME_COMPLIANCE_HE.Rmd) | Soporte RTL |

---
*Mantenido por el equipo de Inteligencia de Datos - BOKITAS*

---
*Mantenido por el equipo de Inteligencia de Datos - BOKITAS*
