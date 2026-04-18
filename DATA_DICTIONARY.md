# Diccionario de Datos: Bokitas Data Intelligence

Este documento detalla la estructura, tipos de datos y orígenes clínicos de los campos maestros utilizados en la plataforma.

## 1. Tabla: `tb_menores.csv` (Maestro de Beneficiarios)
Almacena la información demográfica básica del menor.

| Campo | Tipo | Descripción Técnica | Observación Clínica |
| :--- | :--- | :--- | :--- |
| `CEDULA` | String (UUID/Mock) | Identificador único del menor. | Llave primaria para el seguimiento longitudinal. |
| `NOMBRE` | String | Nombre del beneficiario (Anominizado). | - |
| `APELLIDO` | String | Apellido del beneficiario (Anonimizado). | - |
| `SEXO` | Integer | Género (1: Masculino, 2: Femenino). | Requerido para baremos OMS. |
| `FECHA_NAC` | Date (YYYY-MM-DD) | Fecha de nacimiento. | Cálculo dinámico de edad en días/meses. |
| `PROYECTO` | String | Código del centro o proyecto de atención. | - |

## 2. Tabla: `tb_antropometrica.csv` (Seguimiento Nutricional)
Registra las medidas físicas y el diagnóstico resultante de cada consulta.

| Campo | Tipo | Descripción Técnica | Observación Clínica |
| :--- | :--- | :--- | :--- |
| `CEDULA` | String | Identificador del menor (FK). | Relación con `tb_menores`. |
| `FECHA_INI` | Date | Fecha de la toma de medidas. | - |
| `PESO` | Numeric (Decimal) | Masa corporal en Kilogramos. | Precisión de 100g. |
| `TALLA` | Numeric (Decimal) | Estatura en Centímetros. | Medido en posición supina o de pie. |
| `CBI` | Numeric (Decimal) | Circunferencia del Brazo Izquierdo (cm). | Indicador de reserva proteica. |
| `DIAGNOSTIC` | String | Diagnóstico nutricional primario. | Basado en Z-Scores (OMS 2006). |
| `DIAGNOSTI2` | String | Diagnóstico nutricional secundario. | Usualmente clasifica Desnutrición Aguda/Crónica. |

## 3. Tabla: `tb_socioeconomico.csv` (Vulnerabilidad Social)
Variables para el cálculo del estrato social.

| Campo | Tipo | Descripción Técnica | Observación Clínica |
| :--- | :--- | :--- | :--- |
| `CEDULA_REP` | String | Cédula del representante legal. | Vínculo con el grupo familiar. |
| `ESTRATO` | Integer | Nivel social (I al V). | **Graffar-Méndez Castellano**. |
| `PUNTAJE` | Integer | Total de puntos de la encuesta. | Determina el grado de pobreza. |

---
*Nota: Los campos marcados con sustento OMS provienen directamente de los estándares internacionales de crecimiento infantil.*
