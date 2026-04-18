# Bitácora de Proyecto: Rescate e Inteligencia de Datos BOKITAS

## Resumen Ejecutivo
Este documento registra el proceso técnico y normativo de transformación del sistema legacy **Bokitas Ver 2.6 (FoxPro)** hacia la plataforma moderna **Bokitas Data Intelligence**.

---

## Fase 1: Arqueología de Datos e Ingeniería Inversa
**Objetivo:** Extracción de datos y lógica de un sistema de base de datos relacional de finales de los 90.
- **Acciones:**
    - Identificación de 25 tablas maestros (`.DBF`) y archivos de soporte (`.DBC`, `.FPT`).
    - Descompilación de lógica de negocio incrustada en formularios (`.SCX`/`.SCT`) y programas (`.PRG`).
    - Mapeo de diccionarios de datos para campos clínicos: `PESO`, `TALLA`, `CBI`, `DIAGNOSTIC`.
- **Resultado:** Inventario técnico completo y recuperación de la lógica de diagnóstico basada en baremos OMS.

## Fase 2: Normalización y Estandarización Clínica
**Objetivo:** Garantizar que los datos sean compatibles con estándares internacionales modernos.
- **Acciones:**
    - Transformación de tipos de datos FoxPro (Numeric/Binary) a formatos universales (CSV/JSON/SQL).
    - Adaptación del campo `DIAGNOSTIC` al estándar de Z-Scores de la **OMS** (Desviaciones Estándar -3 a +3).
    - Integración de indicadores socio-económicos basados en el método **Graffar-Méndez Castellano**.
- **Resultado:** Master Data Maestro consolidado y limpio para ingesta analítica.

## Fase 3: Seguridad y Cumplimiento Normativo (GDPR / GRI 418)
**Objetivo:** Blindaje de información sensible y protección de la privacidad de los beneficiarios.
- **Acciones:**
    - Ejecución de Auditoría de Sensibilidad para detectar PII (Información Personal Identificable).
    - Migración de data real a almacenamiento externo seguro (BOKITAS_PRIVATE_DATA).
    - Generación de **Mock Data** sintética para desarrollo seguro.
    - Sanitización de historial Git y establecimiento de protocolos en `SECURITY.md`.
- **Resultado:** Repositorio blindado con cumplimiento normativo **GRI 418**.

## Fase 4: Arquitectura de Nueva Generación
**Objetivo:** Diseño del ecosistema para la escalabilidad y visibilidad gerencial.
- **Acciones:**
    - Definición del esquema **PostgreSQL** para **Supabase**.
    - Modelado del motor de cálculo en **R** para indicadores analíticos avanzados.
    - Integración de reportes dinámicos en **Vercel** y **Streamlit**.
- **Resultado:** Blueprint técnico listo para despliegue productivo.

---
*Fecha de Cierre de Fase: 18 de Abril de 2026*
*Responsable: Documentación Técnica Senior & AI Coding Assistant*
