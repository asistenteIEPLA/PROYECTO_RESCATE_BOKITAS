# 📓 Bitácora de Desarrollo: Recuperación de Data Bokitas

Esta bitácora narra el proceso de ingeniería de datos para la recuperación de la infraestructura histórica de Bokitas.

### 🗓️ Día 1: Diagnóstico y Acceso
* **Situación:** El sistema original basado en Visual FoxPro se encontraba inaccesible, con riesgo inminente de pérdida de datos por obsolescencia del software.
* **Acción:** Localización de los archivos core: `tb_beneficiario.dbf`, `tb_antropometrica.dbf` y `tb_pesotallamenores5x.dbf`.
* **Resultado:** Identificación del entorno de trabajo y verificación de la integridad física de los archivos.

### 🗓️ Día 2: Extracción Binaria y Orfebrería de Encoding
* **Reto:** Archivos memo `.FPT` faltantes provocaban el colapso de los lectores estándar.
* **Solución:** Implementación de extracción forzada ignorando archivos memo faltantes (`ignore_missing_memofile=True`).
* **Calidad:** Resolución del encoding `CP850`. Se logró rescatar tildes y eñes (ej. *MUÑOZ*, *BRICEÑO*) que estaban transformándose en ruido visual en extracciones previas.
* **Resultado:** Primeros CSVs crudos con 100% de registros rescatados.

### 🗓️ Día 3: Resolución de IDs Huérfanos
* **Descubrimiento:** La tabla de mediciones contenía IDs de 10-11 dígitos que no existían en la tabla de beneficiarios (8 dígitos).
* **Solución Forense:** Localización de `tb_menores.dbf`. Se descubrió que esta tabla de enlace contenía la relación entre el ID del niño y el ID del representante.
* **Acción:** Creación de un motor de unión (Merge) que vinculó exitosamente las mediciones con la identidad real de los niños.

### 🗓️ Día 4: Consolidación y Certificación OMS
* **Acción:** Generación del `MASTER_DATA_ANTROPOMETRICA.csv`. 
* **Hito:** Recálculo de la `edad_meses_al_pesaje`. Dado que la tabla original tenía inconsistencias en las edades manuales, se implementó una lógica diferencial basada en `FECHA_PESAJE - FECHA_NAC`.
* **Certificación:** Auditoría final confirma 528 mediciones normalizadas y listas para el motor estadístico de la OMS en R.

---
**Estado Final del Hito 1:** Completado con éxito.
