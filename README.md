# 🦴 PROYECTO RESCATE BOKITAS
## Sistema de Recuperación Forense y Normalización de Datos Antropométricos (1990-2026)

Este proyecto representa un esfuerzo técnico y humanitario para salvaguardar la memoria nutricional de cientos de niños. Ante el colapso del sistema heredado en **Visual FoxPro**, se implementó un motor de extracción binaria para rescatar y normalizar registros históricos críticos.

### 🛡️ Misión del Proyecto
Rescatar, limpiar y consolidar datos de salud que se encontraban en archivos `.DBF` corruptos o incompletos, transformándolos en un dataset maestro listo para análisis estadístico avanzado según los estándares de la **Organización Mundial de la Salud (OMS)**.

### 🚀 Valor Humanitario
Se han rescatado **528 mediciones históricas** de niños en condiciones vulnerables. Gracias a este proceso, estos datos ahora pueden ser utilizados para calcular Z-Scores y diseñar políticas de intervención nutricional efectivas.

### 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.12
- **Librerías Core:** 
  - `pandas`: Procesamiento y normalización de datos.
  - `dbfread`: Extracción de archivos binarios de FoxPro.
- **Entorno de Ejecución:** Antigravity (Advanced Agentic Coding Environment)

### 📈 Características Técnicas
- **Ingeniería Forense:** Recuperación de datos incluso ante la ausencia de archivos memo (`.FPT`) o índices (`.CDX`).
- **Normalización Multidimensional:** Resolución de problemas de codificación `CP850` para preservar la integridad de nombres y ubicaciones.
- **Vinculación Maestra:** Algoritmo de resolución de "IDs Huérfanos" mediante la triangulación de tablas de beneficiarios, menores y mediciones.
- **Cálculo de Precisión:** Recalculado de la edad en meses al momento del pesaje mediante lógica diferencial de fechas.

### 📂 Estructura del Repositorio
- `/src`: Scripts de ingeniería y consolidación.
- `/output`: Dataset maestro `MASTER_DATA_ANTROPOMETRICA.csv` y archivos procesados.
- `/docs`: Documentación técnica y bitácora de desarrollo.

---
*Desarrollado con precisión técnica por Antigravity para el equipo de Bokitas.*
