# Bokitas Data Intelligence

[![Security: GRI 418](https://img.shields.io/badge/Security-GRI_418-blue.svg)](SECURITY.md)
[![License: Private](https://img.shields.io/badge/License-Proprietary-red.svg)]()

Plataforma inteligente para la gestión, análisis y visibilidad de salud nutricional infantil. Este proyecto representa la evolución tecnológica de un sistema legacy hacia una arquitectura moderna basada en la nube.

## 🚀 Misión del Proyecto
Transformar el rescate forense de datos clínicos en inteligencia operativa, facilitando la toma de decisiones gerenciales para la reducción de la desnutrición infantil.

## 🛠 Metodología y Estándares de Calidad
- **Cálculo Nutricional:** Implementación de la metodología **WHO Child Growth Standards** utilizando librerías validadas en **R (Anthro)**.
- **Clasificación Social:** Automatización del indicador **Graffar-Méndez Castellano**.
- **Ciberseguridad:** Cumplimiento estricto del estándar **GRI 418: Privacidad del Cliente**. El repositorio implementa blindaje de datos PII y anonimización de entornos de desarrollo.

## 📦 Stack Tecnológico
- **Cloud Backend:** [Supabase](https://supabase.com/) (PostgreSQL + Realtime).
- **Frontend Dashboard:** Next.js / Streamlit.
- **Analítica:** Motor de R para Z-Scores avanzados.
- **Contenerización:** Docker para despliegues reproducibles.
- **Legacy Source:** Visual FoxPro 2.6 (Fase de Rescate Finalizada).

## 🔐 Guía de Inicio Seguro
Para proteger la privacidad de los menores, este repositorio **no contiene datos reales**.

1.  **Configuración de Entorno:** Copia `.env.example` a `.env` y configura tus llaves de Supabase.
2.  **Mock Data:** Utiliza los archivos en `mock_data/` para poblar tu base de datos local o de pruebas.
    ```bash
    python tools/ingest_mock_data.py # Ejemplo conceptual
    ```
3.  **Scripts de Extracción:** Las herramientas de ingeniería inversa se encuentran en `tools/` (anteriormente `scratch/`).

## 📊 Reporte de Sostenibilidad e Impacto
Toda la gestión analítica se rige por indicadores de impacto social que pueden consultarse en la [Plantilla de Informe GRI](INFORME_GRI_BOKITAS.md).

---
*Mantenido por el equipo de Inteligencia de Datos - BOKITAS*
