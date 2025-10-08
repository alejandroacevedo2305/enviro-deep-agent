---
title: CAPÍTULO 1
author: Jorge
date: D:20210803102300-04'00'
language: es
type: report
pages: 84
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA 1 INFORME MODELAMIENTO DE LA DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS
-->

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

# ADENDA 1 INFORME MODELAMIENTO DE LA DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS

## (Actualizado) PROYECTO: COMPLEJO INDUSTRIAL PHOENIX

**Preparada para:**

**AECI Mining and Chemical Services (Chile) Ltda.**
Comerc/Import/Export productos químicos y fabricante explosivos
Av. Nueva Tajamar 481, WTC, Torre Sur, Piso 8, Oficina 802, Las Condes,
**Santiago**

Preparada por:

**BORDOLI & Consultores Asociados EIRL**

Av. O’Higgins 1338, Oficina 1002, Antofagasta
Teléfono (56-55) 2255181

web: www.bordoli.cl

e-mail: jbordoli@bordoli.cl

Agosto 2021

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 1 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**INFORME MODELAMIENTO DE LA DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS**

**PROYECTO COMPLEJO INDUSTRIAL PHOENIX**

INDICE DE MATERIAS

**1.** **INTRODUCCIÓN** ................................................................................................................................ 6

**2.** **DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO ..........................................................................8**

**3.** **ESCENARIO METEOROLÓGICO .............................................................................................. 10**

3.1 Series de Tiempo. ........................................................................................................... 14

3.2 Campos de Viento ........................................................................................................... 16

**4.** **BASES DE DATOS Y ARCHIVOS DE MODELACIÓN .................................................................... 18**

4.1 Archivos de Entrada y Salida de la Modelación ........................................................................ 18
**5.** **CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN Y SU ENTORNO ....................................... 19**

5.1 Localización ............................................................................................................................... 19

5.2 Área de Modelamiento Meteorológica .................................................................................... 20

5.3 Grilla de Modelamiento Meteorológico ................................................................................... 21
5.4 Topografía del Área de Modelamiento Meteorológico ............................................................ 22

5.5 Dominio de Modelación de Emisiones Atmosféricas. .............................................................. 23

5.6 Receptores en el Área de Modelamiento ................................................................................. 24
5.7 Suelos del Área de Modelamiento............................................................................................ 26

**6.** **RESULTADOS DE LA MODELACIÓN ........................................................................................ 27**

6.1 RESULTADOS DEL MODELO ...................................................................................................... 27

6.1.1 Cumplimiento Normas de Calidad Ambiental Primaria ....................................................... 27

6.1.2 Cumplimiento Normas de Calidad Ambiental Secundaria .................................................. 31
**7.** **ANÁLISIS DE INCERTIDUMBRE ............................................................................................... 34**

7.1 Análisis Cualitativo de los Campos de Vientos ......................................................................... 34

7.2 Análisis Cuantitativo Para el Cálculo de Incertidumbre ............................................................ 34

**8.** **ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE ............................................................. 42**

8.1 Análisis de Cumplimiento Normativo Vigente Para MP10 ....................................................... 42

8.2 Análisis de Cumplimiento Normativo Vigente Para MP2,5 ...................................................... 42

8.3 Análisis de Cumplimiento Normativo Vigente Para MPS ......................................................... 43

8.4 Análisis de Cumplimiento Normativo Vigente Para Gases CO ................................................. 43

8.5 Análisis de Cumplimiento Normativo Vigente Para Gases NO2 ............................................... 43

8.6 Análisis de Cumplimiento Normativo Vigente Para Gases SO2 ................................................ 43

8.7 Puntos de Máximo Impacto ...................................................................................................... 43

**9.** **CONCLUSIONES .................................................................................................................... 45**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 2 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**10. MAPAS DE ISOCONCENTRACIONES ....................................................................................... 45**

INDICE DE TABLAS

Tabla 1: Normas de Calidad Ambiental Primarias y Secundarias ........................................................... 7

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- máximos permisibles establecidos en las normas primarias y secundarias de calidad del aire establecido en la legislación chilena, los cuales se presentan en la Tabla 1 siguiente: -->

**Tabla 1: Normas de Calidad Ambiental Primarias y Secundarias****

| Parámetro | Unidad Estadística | Límite Máximo<br>Permitido | Referencia Legal |
| --- | --- | --- | --- |
| MP 10 | Promedio Anual1 | 50 (μg/m3N) | NP DS 59/98 |
| MP 10 | Percentil 98 Promedio 24 horas2 | 150 (μg/m3N) | NP DS 59/98 |
| MP 2.5 | Promedio Trianual3 | 20 (μg/m3N) | NP DS 12/2011 |
| MP 2.5 | Percentil 98 Promedio Diario4 | 50 (μg/m3N) | NP DS 12/2011 |
| MPS | Promedio Mensual | 150 mg/m2dia | NS DE 4/1992 |
| MPS | Promedio Anual | 100 mg/m2dia | NS DE 4/1992 |
| SO2 | Promedio Anual5 | 80 (μg/m3N) | NP DS 113/2002 |
| SO2 | Promedio Diario, percentil 996 | 250 (μg/m3N) | NP DS 113/2002 |
| SO2 | Promedio Anual7 | 80 (μg/m3N) | NS DS 185/1991 |
| SO2 | Percentil 99.7 Concentración Diaria8 | 365 (μg/m3N) | NS DS 185/1991 |

<!-- Estadísticas: 10 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 1 Promedio Anual: se refiere a la concentración promedio anual. Se considera sobrepasada la norma cuando la concentración anual calculada como promedio aritmético de tres años calendario consecutivos, sea mayor o igual a lo indicado a la tabla. -->
<!-- FIN TABLA 1 -->


Tabla 2: Información de la Orden de los Datos WRF ............................................................................ 10

Tabla 3: Información General de la Estación Meteorológica de Superficie ......................................... 12

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DECLARACIÓN DE IMPACTO AMBIENTAL COMPLEJO INDUSTRIAL PHOENIX -->

**Tabla 3: Información General de la Estación Meteorológica de Superficie****

| Código Nacional | 200006 |
| --- | --- |
| Código OMM | 85418 |
| Código OACI | SCDA |
| Nombre de la Estación | Diego Aracena Iquique Ap. |
| Región | Tarapacá |
| Provincia | Iquique |
| Comuna | Iquique |
| Coordenadas UTM | 376.877,2 E - 7.727.300,6 N |
| Huso horario | 19S |

<!-- Estadísticas: 8 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- La estación “Diego Aracena Iquique Ap.” se encuentra dentro del área de modelación que se presenta en la figura 2. -->
<!-- FIN TABLA 3 -->


Tabla 4: Información para el modelamiento ........................................................................................ 18

Tabla 5: Archivos de entrada y salida de la modelación ....................................................................... 18

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los archivos de entrada y salida de la modelación, para cada etapa del proyecto y que se anexan en forma digital (DVD), son los siguientes: -->

**Tabla 5: Archivos de entrada y salida de la modelación****

| CALMET | GEO.DAT |
| --- | --- |
| CALMET | CALMET.DAT |
| CALMET | CALMET.LST |
| CALMET | CALMET.INP |
| CALPUF | CALPUFF.LST |
| CALPUF | CALPUFF.INP |
| CALPUF | CONS.INP |
| CALPOST | CALPOST.DAT |
| CALPOST | CALPOST.LST |
| CALPOST | CALPOST.INP |
| ARCHIVOS COMPLEMENTARIOS | Dry Flux Data File |
| ARCHIVOS COMPLEMENTARIOS | Wet Flux Data |

<!-- Estadísticas: 11 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 18 de 84 Agosto 2021 DECLARACIÓN DE IMPACTO AMBIENTAL -->
<!-- FIN TABLA 5 -->


Tabla 6: Coordenadas de Ubicación del Proyecto ................................................................................ 19

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.1 Localización** Las coordenadas geográficas de ubicación del proyecto en Datum WGS 84- Huso 19S son las siguientes: -->

**Tabla 6: Coordenadas de Ubicación del Proyecto****

| Vértice | Coordenada Norte<br>WGS 84, Huso 19 Sur | Coordenada Este<br>WGS 84, Huso 19 Sur |
| --- | --- | --- |
| V1 | 7.703.219 | 384.047 |
| V2 | 7.702.644 | 384.588 |
| V3 | 7.701.261 | 383.729 |
| V4 | 7.701.693 | 383.205 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Nota: Polígono de 120 hectáreas aproximadamente. **Figura 7 Localización del Proyecto a Nivel Regional** -->
<!-- FIN TABLA 6 -->


Tabla 7: Ubicación y descripción de puntos receptores sensibles ....................................................... 24

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- particulado y gases, generados por las actividades de las distintas fases del proyecto Complejo Industrial Phoenix. -->

**Tabla 7: Ubicación y descripción de puntos receptores sensibles****

| Punto Receptor | Coordenadas<br>Datum WGS 84 Huso 19S | Col3 | Uso de Suelo<br>Efectivo<br>Plano Regulador | Tipo de Zona | Distancia del<br>Proyecto al<br>Receptor (m) |
| --- | --- | --- | --- | --- | --- |
| **Punto Receptor** | **Este** | **Norte** | **Norte** | **Norte** | **Norte** |
| R1<br>Caleta Chanavayita | 376.710 | 7.710.180 | Rural | Rural | 10.820 |
| R2<br>Área industrial<br>deshidratación de<br>concentrado de<br>cobre | 378.383 | 7.700.715 | Rural | Industrial | 5.800 |
| R3<br>Caleta Cáñamo | 376.921 | 7.699.889 | Rural | Rural | 7.500 |
| R4<br>Área industrial<br>Quebrada Blanca | 376.960 | 7.701.702 | Rural | Industrial | 7.000 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 24 de 84 Agosto 2021 DECLARACIÓN DE IMPACTO AMBIENTAL -->
<!-- FIN TABLA 7 -->


Tabla 8: Aportes del Proyecto Etapa de Construcción ......................................................................... 28

Tabla 9: Aportes del Proyecto Etapa de Operación .............................................................................. 29

Tabla 10: Aportes del Proyecto Etapa de Cierre ................................................................................... 30

Tabla 11: Aportes del Proyecto Etapa de Construcción ........................................................................ 31

Tabla 12: Aportes del Proyecto Etapa de Operación ............................................................................ 32

Tabla 13: Aportes del Proyecto Etapa de Cierre ................................................................................... 33

Tabla 14: Velocidad promedio del Viento en m/s................................................................................. 35

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DECLARACIÓN DE IMPACTO AMBIENTAL COMPLEJO INDUSTRIAL PHOENIX -->

**Tabla 14: Velocidad promedio del Viento en m/s****

| Estación | Promedio Observado | Promedio Pronóstico<br>WRF | % de Error |
| --- | --- | --- | --- |
| Diego Aracena Iquique<br>Ap. | 3,90 | 4,16 | 6,7 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _% Error_ _V_ = % de error entre los valores modelado y observado de la velocidad del viento. (Valor modelado) = 4,16 m/s -->
<!-- FIN TABLA 14 -->


Tabla 15: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección ......... 36

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DECLARACIÓN DE IMPACTO AMBIENTAL COMPLEJO INDUSTRIAL PHOENIX -->

**Tabla 15: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita | %<br>Respecto<br>de la<br>Norma | Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial | %<br>Respecto<br>de la<br>Norma | Conc.<br>(μg/m3N)<br>Receptor<br>R3<br>Caleta<br>Cáñamo | %<br>Respecto<br>de la<br>Norma | Conc.<br>(μg/m3N)<br>Receptor<br>R4<br>Área<br>industrial | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98<br>Promedio 24<br>horas | 150 | 0,37 | 0,19 | 0,19 | 0,09 | 0,19 | 0,09 | 0,19 | 0,19 |
| MP10 | Promedio Anual | 50 | 0,09 | 0,19 | 0,09 | 0,09 | 0,00 | 0,09 | 0,00 | 0,09 |
| MP2,5 | Percentil 98<br>Promedio Diario | 50 | 0,19 | 0,37 | 0,09 | 0,19 | 0,09 | 0,19 | 0,19 | 0,28 |
| MP2,5 | Promedio Anual | 20 | 0,09 | 0,28 | 0,00 | 0,19 | 0,00 | 0,09 | 0,00 | 0,19 |
| CO | Percentil 99, máx.<br>1 hora | 30000 | 0,56 | 0,00 | 0,37 | 0,00 | 0,28 | 0,00 | 0,47 | 0,00 |
| CO | Percentil 99, máx.<br>8 hora | 10000 | 0,09 | 0,00 | 0,09 | 0,00 | 0,09 | 0,00 | 0,09 | 0,00 |
| NO2 | Percentil 99, máx.<br>1 hora | 400 | 2,15 | 0,56 | 1,59 | 0,37 | 1,21 | 0,28 | 1,77 | 0,47 |
| NO2 | Promedio, Anual | 100 | 0,09 | 0,09 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| SO2 | Promedio Diario,<br>percentil 99 | 250 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

<!-- Estadísticas: 9 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 36 de 84 Agosto 2021 DECLARACIÓN DE IMPACTO AMBIENTAL -->
<!-- FIN TABLA 15 -->


Tabla 16: Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección .............. 37

Tabla 17: Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección ..................... 38

Tabla 18: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección ......... 39

Tabla 19: Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección .............. 40

<!-- INICIO TABLA 19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DECLARACIÓN DE IMPACTO AMBIENTAL COMPLEJO INDUSTRIAL PHOENIX -->

**Tabla 19: Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita | %<br>Respecto<br>de la<br>Norma | Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial | %<br>Respecto<br>de la<br>Norma | Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo | %<br>Respecto<br>de la<br>Norma | Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SO2 | Promedio Anual | 80 | 0,09 | 0,09 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| SO2 | Percentil<br>99.7<br>Conc. Diaria | 365 | 0,28 | 0,09 | 0,28 | 0,09 | 0,19 | 0,09 | 0,28 | 0,09 |
| SO2 | Percentil<br>99.73<br>Conc. 1 hora | 1.000 | 2,43 | 0,28 | 2,99 | 0,28 | 1,59 | 0,19 | 2,24 | 0,19 |

<!-- Estadísticas: 3 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 40 de 84 Agosto 2021 DECLARACIÓN DE IMPACTO AMBIENTAL -->
<!-- FIN TABLA 19 -->


Tabla 20: Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección ..................... 41

<!-- INICIO TABLA 20 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DECLARACIÓN DE IMPACTO AMBIENTAL COMPLEJO INDUSTRIAL PHOENIX -->

**Tabla 20: Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita | %<br>Respecto<br>de la<br>Norma | Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial | %<br>Respecto<br>de la<br>Norma | Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo | %<br>Respecto<br>de la<br>Norma | Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SO2 | Promedio Anual | 80 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| SO2 | Percentil 99.7<br>Conc. Diaria | 365 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| SO2 | Percentil 99.73<br>Conc. 1 hora | 1.000 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

<!-- Estadísticas: 3 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: Tablas 18, 19 y 20 los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día Nota 2: Tablas 18, 19 y 20 los aportes de SO 2 en cada uno de los receptores, se expresan en μg/m [3] N INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 41 de 84 -->
<!-- FIN TABLA 20 -->


Tabla 21: Puntos de Máximo Impacto - Fase de Construcción ............................................................. 43

<!-- INICIO TABLA 21 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- proyecto, en cada una de sus fases, se presentan en las siguientes tablas, indicando ubicación en coordenadas UTM WGS-84 Huso 19S y concentración máxima: -->

**Tabla 21: Puntos de Máximo Impacto - Fase de Construcción****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Este** | **Norte** | **Norte** |
| MP10 | Percentil 98 Promedio 24 horas | 383.586 | 7.701.920 | 22,9 |
| MP10 | Promedio Anual | 383.586 | 7.701.920 | 12,1 |
| MP2,5 | Percentil 98 Promedio Diario | 383.586 | 7.701.920 | 15,7 |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 43 de 84 Agosto 2021 DECLARACIÓN DE IMPACTO AMBIENTAL -->
<!-- FIN TABLA 21 -->


Tabla 22: Puntos de Máximo Impacto - Fase de Operación ................................................................. 44

<!-- INICIO TABLA 22 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |NO2|Promedio, Anual|383.586|7.701.920|32,9| |SO2|Percentil 99,73 Concentración 1 hora|383.586|7.701.920|89,7| |SO2|Promedio Diario, percentil 99|383.586|7.701.920|7,3| |SO2|Promedio, Anual|383.586|7.701.920|2,2| -->

**Tabla 22: Puntos de Máximo Impacto - Fase de Operación****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Este** | **Norte** | **Norte** |
| MP10 | Percentil 98 Promedio 24 horas | 383.586 | 7.701.920 | 267,0 |
| MP10 | Promedio Anual | 383.586 | 7.701.920 | 74,7 |
| MP2,5 | Percentil 98 Promedio Diario | 383.586 | 7.701.920 | 257,0 |
| MP2,5 | Promedio Trianual | 383.586 | 7.701.920 | 64,2 |
| CO | Percentil 99, máx. 1 hora | 383.586 | 7.701.920 | 19019,0 |
| CO | Percentil 99, máx. 8 hora | 383.586 | 7.701.920 | 2482,0 |
| NO2 | Percentil 99, máx. 1 hora | 383.586 | 7.701.920 | 56918,0 |
| NO2 | Promedio, Anual | 383.586 | 7.701.920 | 866,0 |
| SO2 | Percentil 99,73 Concentración 1 hora | 383.586 | 7.701.920 | 3614,0 |
| SO2 | Promedio Diario, percentil 99 | 383.586 | 7.701.920 | 267,0 |
| SO2 | Promedio, Anual | 383.586 | 7.701.920 | 55,9 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 23: Puntos de Máximo Impacto - Fase de Cierre** |Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)| |---|---|---|---|---| -->
<!-- FIN TABLA 22 -->


Tabla 23: Puntos de Máximo Impacto - Fase de Cierre ........................................................................ 44

<!-- INICIO TABLA 23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |NO2|Promedio, Anual|383.586|7.701.920|866,0| |SO2|Percentil 99,73 Concentración 1 hora|383.586|7.701.920|3614,0| |SO2|Promedio Diario, percentil 99|383.586|7.701.920|267,0| |SO2|Promedio, Anual|383.586|7.701.920|55,9| -->

**Tabla 23: Puntos de Máximo Impacto - Fase de Cierre****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Este** | **Norte** | **Norte** |
| MP10 | Percentil 98 Promedio 24 horas | 383.586 | 7.701.920 | 4,3 |
| MP10 | Promedio Anual | 383.586 | 7.701.920 | 1,9 |
| MP2,5 | Percentil 98 Promedio Diario | 383.586 | 7.701.920 | 3,5 |
| MP2,5 | Promedio Trianual | 383.586 | 7.701.920 | 1,2 |
| CO | Percentil 99, máx. 1 hora | 383.586 | 7.701.920 | 217,1 |
| CO | Percentil 99, máx. 8 hora | 383.586 | 7.701.920 | 30,7 |
| NO2 | Percentil 99, máx. 1 hora | 383.586 | 7.701.920 | 980,2 |
| NO2 | Promedio, Anual | 383.586 | 7.701.920 | 16,4 |
| SO2 | Percentil 99,73 Concentración 1 hora | 383.586 | 7.701.920 | 44,9 |
| SO2 | Promedio Diario, percentil 99 | 383.586 | 7.701.920 | 3,6 |
| SO2 | Promedio, Anual | 383.586 | 7.701.920 | 1,1 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 44 de 84 Agosto 2021 DECLARACIÓN DE IMPACTO AMBIENTAL -->
<!-- FIN TABLA 23 -->


INDICE DE FIGURAS

Figura 1: Rosa de Vientos .................................................................................................................... 11

Figura 2 Ubicación Estación Meteorológica ....................................................................................... 12

Figura 3: Velocidad promedio del viento ............................................................................................ 13

Figura 4: Serie de tiempo registros horarios de velocidad del viento - Estación Diego Aracena

Iquique Ap., periodo 01.01.20 al 31-12-20........................................................................... 15

Figura 5: Serie de tiempo registros horarios de Dirección del viento - Estación Diego Aracena

Iquique Ap., periodo 01.01.20 al 31-12-20........................................................................... 16

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 3 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

Figura 6: Rosa de Viento Estación Diego Aracena Iquique Ap. v/s Rosa de Viento modelada con

WRF. ..................................................................................................................................... 17

Figura 7: Localización del Proyecto a Nivel Regional .......................................................................... 19
Figura 8: Área de Modelamiento ........................................................................................................ 20

Figura 9: Grilla Meteorológica de Modelamiento ............................................................................... 21
Figura 10: Topografía del Área de Modelación .................................................................................... 22

Figura 11: Emplazamiento de Puntos Receptores Sensibles ................................................................ 25

Figura 12: Uso de Suelo ........................................................................................................................ 26

Figura 13: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (24 h) .... 46

Figura 14: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (Anual) .. 47

Figura 15: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (24 h) ... 48

Figura 16: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción

(Anual) .................................................................................................................................. 49

Figura 17: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de

Construcción (24 horas) ....................................................................................................... 50

Figura 18: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de

Construcción (Anual) ............................................................................................................ 51

Figura 19: Mapa de Isoconcentración Gases CO - Etapa de Construcción (1h) ................................... 52

Figura 20: Mapa de Isoconcentración Gases CO - Etapa de Construcción (8h) ................................... 53

Figura 21: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (1 h) ................................ 54

Figura 22: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (Anual) ............................ 55

Figura 23: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (1h) .................................. 56

Figura 24: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (24h) ................................ 57

Figura 25: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (Anual) ............................ 58

Figura 26: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (24 h) ........ 59

Figura 27: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (Anual) ...... 60

Figura 28: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (24 h) ....... 61

Figura 29: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (Anual) ..... 62

Figura 30: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de

Operación (mensual). ........................................................................................................... 63

Figura 31: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de

Operación (Anual) ................................................................................................................ 64

Figura 32: Mapa de Isoconcentración Gases CO - Etapa de Operación (1h) ........................................ 65

Figura 33: Mapa de Isoconcentración Gases CO - Etapa de Operación (8h) ........................................ 66

Figura 34: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (1 h) .................................... 67

Figura 35: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (Anual) ................................ 68

Figura 36: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (1h) ...................................... 69

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 4 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

Figura 37: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (24h) .................................... 70

Figura 38: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (Anual) ................................. 71

Figura 39: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (24 h) ............... 72

Figura 40: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (Anual) ............. 73

Figura 41: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (24 h) .............. 74

Figura 42: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (Anual) ............ 75

Figura 43: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre

(mensual) .............................................................................................................................. 76

Figura 44: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre

(Anual) .................................................................................................................................. 77

Figura 45: Mapa de Isoconcentración Gases CO - Etapa de Cierre (1h) ............................................... 78

Figura 46: Mapa de Isoconcentración Gases CO - Etapa de Cierre (8h) ............................................... 79

Figura 47: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (1 h) ........................................... 80

Figura 48: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (Anual) ....................................... 81

Figura 49: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (1h) ............................................. 82

Figura 50: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (24h) ........................................... 83

Figura 51: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (Anual) ........................................ 84

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 5 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**INFORME MODELAMIENTO DE LA DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS**

**PROYECTO COMPLEJO INDUSTRIAL PHOENIX**

**1.** **INTRODUCCIÓN**

En este documento se presentan los resultados del modelamiento de la dispersión de contaminantes

generados durante las distintas fases del Proyecto “COMPLEJO INDUSTRIAL PHOENIX” de AECI

Mining and Chemical Services (Chile) Ltda. Estas emisiones corresponden específicamente a material

particulado respirable (MP 10 y MP 2.5 ), gases (CO, HC, NOx, SOx), y material particulado sedimentable

(MPS), las cuales son generadas por las distintas actividades consideradas en las fases de

construcción, operación y cierre del proyecto Complejo Industrial Phoenix y por el transporte,

tránsito de vehículos por caminos pavimentados, tránsito de vehículos livianos y vehículos pesados

por caminos no pavimentados, y utilización de maquinarias, equipos, vehículos y generadores

eléctricos.

El proyecto “COMPLEJO INDUSTRIAL PHOENIX”, en adelante el “Proyecto”, consiste en la

construcción y operación de una planta de ANFO más una planta de emulsión matriz de Nitrato de

Amonio, químico utilizado para la fabricación de explosivos, además del almacenamiento y

comercialización de explosivos y sistemas de iniciación. Como consecuencia del desarrollo de este

proyecto, se ampliará la oferta de estos importantes insumos en el mercado nacional.

El presente proyecto, objeto de evaluación ambiental, se ha concebido de forma tal que el producto

a generar en el nuevo complejo industrial sea entregado in situ, es decir, que será el comprador

quien se encargará del retiro de los productos terminados as emulsiones desde la nueva planta,

utilizando para ello empresas de transporte especializadas y autorizadas por parte de la autoridad

competente y por la legislación vigente. En consecuencia, el transporte de productos terminados

fuera del predio industrial, no forma parte de la presente Declaración de Impacto Ambiental (DIA):

De esta forma, el nuevo proyecto tendrá la capacidad de producción de 10.000 t de emulsión para

explosivos al mes y 2.700 toneladas de ANFO.

Adicionalmente a las obras señaladas anteriormente, el proyecto contempla la construcción de

instalaciones de apoyo que consisten en oficinas administrativas, instalaciones sanitarias, áreas de

almacenamiento transitorio de residuos, bodega y comedor para el personal, además de talleres

para la mantención de equipos, vehículos y maquinarias.

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 6 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

El proyecto “Complejo Industrial Phoenix” se ubica en la Región y Provincia de Iquique, Comuna de

Iquique.

Para realizar el modelamiento de dispersión de los contaminantes atmosféricos, se utilizó la Guía

para el Uso de Modelos de Calidad del Aire en el SEIA (2012).

Los resultados de la modelación atmosférica, se han analizado tomando en consideración los límites

máximos permisibles establecidos en las normas primarias y secundarias de calidad del aire

establecido en la legislación chilena, los cuales se presentan en la Tabla 1 siguiente:

**Tabla 1: Normas de Calidad Ambiental Primarias y Secundarias**

|Parámetro|Unidad Estadística|Límite Máximo<br>Permitido|Referencia Legal|
|---|---|---|---|
|MP 10|Promedio Anual1|50 (μg/m3N)|NP DS 59/98|
|MP 10|Percentil 98 Promedio 24 horas2|150 (μg/m3N)|NP DS 59/98|
|MP 2.5|Promedio Trianual3|20 (μg/m3N)|NP DS 12/2011|
|MP 2.5|Percentil 98 Promedio Diario4|50 (μg/m3N)|NP DS 12/2011|
|MPS|Promedio Mensual|150 mg/m2dia|NS DE 4/1992|
|MPS|Promedio Anual|100 mg/m2dia|NS DE 4/1992|
|SO2|Promedio Anual5|80 (μg/m3N)|NP DS 113/2002|
|SO2|Promedio Diario, percentil 996|250 (μg/m3N)|NP DS 113/2002|
|SO2|Promedio Anual7|80 (μg/m3N)|NS DS 185/1991|
|SO2|Percentil 99.7 Concentración Diaria8|365 (μg/m3N)|NS DS 185/1991|

1 Promedio Anual: se refiere a la concentración promedio anual. Se considera sobrepasada la norma cuando la

concentración anual calculada como promedio aritmético de tres años calendario consecutivos, sea mayor o
igual a lo indicado a la tabla.
2 Percentil 98, 24 horas: se refiere a la concentración promedio de 24 horas. Se considera sobrepasada la

norma cuando el Percentil 98 de las concentraciones de 24horas registradas durante un período anual sea
mayor o igual a ese valor de la tabla.
3 Promedio Trianual: se refiere al promedio tri-anual de las concentraciones anuales. Se considera sobrepasada

la norma cuando el valor sea mayor al indicado en la tabla.
4 Percentil 98, Promedio Diario: se refiere al percentil 98 de los promedios diarios registrados durante un año. Se
considera sobrepasada la norma cuando el valor sea mayor al indicado en la tabla

5 Promedio Anual: se refiere al promedio aritmético de los valores de concentración anual de tres años
calendarios sucesivos. Se considera sobrepasada la norma con un valor igual o superior indicado en la tabla.
6 Promedio Diario, Percentil 99: se refiere al promedio aritmético de tres años sucesivos, del percentil 99 de las
concentraciones de 24 horas registradas durante un año calendario. Se considera sobrepasada la norma con
un valor igual o superior indicado en la tabla.
7 Promedio Anual: se refiere al promedio aritmético de los valores de concentración anual de tres años

calendarios sucesivos. Se considera sobrepasada la norma con un valor mayor o igual al doble del nivel
indicado en la tabla.
8 Percentil 99.7: se refiere al promedio aritmético de tres años calendario sucesivo de los valores del percentil

99,7 de las concentraciones de 24 horas registradas cada año. Se considera sobrepasada la norma con un
valor mayor o igual al doble del nivel indicado en la tabla.

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 7 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

|Col1|Percentil 99.73 Concentración 1 hora9|1000 (μg/m3N)|NS DS 185/1991|
|---|---|---|---|
|NO2|Promedio Anual10|100 (μg/m3N)|NP DS 114/2002|
|NO2|Percentil 99, máx. 1 hora11|400 (μg/m3N)|NP DS 114/2002|
|CO|Percentil 99,máx.8 horas12|10.000<br>(μg/m3N)|NP DS 115/2002|
|CO|Percentil 99, máx. 1 hora13|30.000<br>(μg/m3N)|NP DS 115/2002|

**2.** **DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO**

Cualquier modelo que se ocupe para los fines que persigue el SEIA debe cumplir con las siguientes

características:

 - Disponer de documentación completa que describa sus fundamentos conceptuales, ecuaciones

matemáticas, y los tipos de datos de entrada y de salida junto con sus respectivos formatos;

 - Estar escrito en un lenguaje de programación común y con un código abierto;

 - Ser de uso libre;

 - Disponer de documentación sobre su evaluación, en forma de informes técnicos, publicaciones

científicas o equivalente; y

 - Contar con desarrollo y soporte técnico actualizado de parte de su comunidad de usuarios o

desarrolladores.

Los modelos recomendados en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”,

elaborada por el Servicio de Evaluación Ambiental (SEA), cumplen con los requisitos anteriores.

El modelo recomendado en la guía citada, para contaminantes primarios, en dominio de modelación

9 Percentil 99.73: se refiere al promedio aritmético de tres años calendario sucesivo de los valores del percentil

99,73 de las concentraciones de 1 hora registradas cada año. Se considera sobrepasada la norma con un valor
mayor o igual al doble del nivel indicado en la tabla.
10 Promedio Anual: se refiere al promedio aritmético de los valores de concentración anual de tres años

calendarios sucesivos. Se considera sobrepasada la norma con un valor igual o superior indicado en la tabla.
11 Percentil 99: se refiere al promedio aritmético de tres años sucesivos del percentil 99 de los máximos diarios de

concentración de 1 hora registrados durante un año calendario. Se considera sobrepasada la norma con un
valor igual o superior indicado en la tabla.
12 Percentil 99: se refiere al promedio aritmético de tres años sucesivos, del percentil 99 de los máximos diarios

de concentración de 8 horas registrados durante un año calendario. Se considera sobrepasada la norma con
un valor igual o superior indicado en la tabla.
13 Percentil 99: se refiere al promedio aritmético de tres años sucesivos, del percentil 99 de los máximos diarios

de concentración de 1 hora registrados durante un año calendario. Se considera sobrepasada la norma con un
valor igual o superior indicado en la tabla.

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 8 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

de menos de 5 km, es el AERMOD, ya que, a esta escala, se puede suponer una meteorología

homogénea. Por lo tanto, es aceptable utilizar un modelo Gaussiano para modelar contaminantes

primarios. Dado que la información meteorológica de entrada en este caso debe ser de carácter

observacional, los 5 km deben considerarse desde la estación meteorológica (no la fuente emisora).

En el caso de que alguno de los bordes del dominio espacial de modelación esté a más de 5 km de la

fuente de emisión, lo más adecuado es utilizar un modelo que permita simular meteorología

heterogénea. Los modelos capaces de esto son los de tipo “puff” o Eulerianos. El modelo tipo “puff”

recomendado es el modelo CALPUFF; en el caso de modelos Eulerianos, se recomiendan los modelos

WRF-Chem, CAMx y CMAQ

En todos los casos, también se debe analizar si existen factores que podrían perturbar el carácter

lineal de los campos de viento dentro del dominio, situación en que debe utilizarse un modelo como

el descrito en el párrafo anterior, incluso si se verifica la distancia máxima de 5 km desde la estación.

Debido a que no se cuenta con una estación de monitoreo meteorológico de superficie para obtener

datos observados a menos de 5 km de las fuentes emisoras, será necesario crear un dominio de

modelación mayor, por lo tanto, en el presente estudio, se utilizará el modelo de dispersión de

contaminantes CALPUFF. Este modelo creado por científicos del ASG (Grupo de Estudios

Atmosféricos de TRC Solutions), corresponde a un avanzado sistema de modelación meteorológica y

de calidad del aire.

Este modelo ha sido adoptado por la Agencia de Protección Medioambiental de los Estados Unidos

(EPA por sus siglas en inglés) en su Guía para Modelos de Calidad del Aire como el preferido para la

evaluación de transporte de contaminantes a gran escala y como una base caso a caso para

determinadas aplicaciones que involucran condiciones meteorológicas complejas.

Este modelo (CALPUFF) está formado principalmente por tres componentes y un set de programas

de pre- y post-procesamiento. Estos componentes son:

CALMET: modelo meteorológico que desarrolla campos horarios de viento y temperatura en un

dominio de modelación de grilla tridimensional. Contiene además parametrizaciones de flujos de

laderas, efectos cinemáticos y de bloqueo del terreno, un procedimiento de minimización de

divergencia y un modelo micrometeorológico para capas límites sobre tierra y agua. En el archivo

producido por CALMET están también incluidos campos bidimensionales asociados como altura de

mezcla, características de la superficie y propiedades de dispersión.

CALPUFF: modelo de transporte y dispersión lagrangiano, gaussiano, no estacionario, que contiene

módulos para efectos de terreno complejo, transporte sobre agua, deposiciones secas y húmedas y

transformaciones químicas simples. El modelo advecta "puffs" o bocanadas de material emitido

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 9 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

desde fuentes modeladas, simulando procesos de dispersión y transformación en el camino.

Típicamente usa los campos generados por CALMET, o como opción puede usar datos

meteorológicos más simples no grillados muy similares a modelos de plumas existentes. En la

distribución resultante de "puffs", a lo largo del período simulado, incorpora explícitamente

variaciones temporales y espaciales en los campos meteorológicos seleccionados. Los archivos de

salida primarios de CALPUFF contienen concentraciones o flujos de deposiciones horarias evaluadas

en lugares seleccionados de recepción.

CALPOST: procesador de los archivos de CALPUFF, produciendo tablas que resumen los resultados de

la simulación, identificando por ejemplo las concentraciones máximas promedios de tres horas y las

segundas más altas en cada receptor. Cuando se realizan modelaciones relacionadas a visibilidad,

CALPOST usa concentraciones de CALPUFF para calcular coeficientes de extinción y mediciones

relacionadas a visibilidad, reportándolas para los tiempos promediados y lugares seleccionados.

Cada uno de estos programas tiene una interfaz gráfica, existiendo además otros numerosos

procesadores que pueden ser utilizados para preparar datos geofísicos (como el terreno y uso de

suelo), meteorológicos (como precipitación o datos provenientes de boyas), o interfaces a otros

modelos como el MM5, WRF, modelos RUC o RAMS.

Para seleccionar el modelo adecuado, se consideraron los criterios establecidos en la Guía para el

Uso de Modelos de Calidad del Aire en el SEIA, (apartado 4.2, modelos recomendados, pág. 17).

CALPUFF, resulto ser el más adecuado, considerando que los datos disponibles para establecer el

dominio espacial de la modelación, se sitúan a más de 5 km de la fuente de emisión.

**3.** **ESCENARIO METEOROLÓGICO**

El escenario meteorológico utilizado para la modelación, fue obtenido a través del modelo

meteorológico de pronostico Weather Research and Forecasting Model (WRF), adquiridos a la

empresa Lakes Environmental, con un domino de 100 km por 100 km, una resolución de 4 km y el

periodo de data año 2020.

**Tabla 2: Información de la Orden de los Datos WRF**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 10 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

WRF es uno de los modelos meteorológicos de pronóstico más avanzados y completos y es

mantenido por NCAR9/ NOAA10 de Estados Unidos. Además, se ha ocupado en la mayoría de los

proyectos relacionados con modelación atmosférica encargados por organismos estatales, como la

ex-CONAMA y la Comisión Nacional de Energía (CNE) en los últimos años.

Rosas de Viento

Respecto a la dirección del viento, se puede apreciar que la dirección del viento predominante es

hacia el Noreste, con una velocidad que fluctúa principalmente entre 0,5 y 8,5 m/s, con un

porcentaje de calma de 4,38 %.

**Figura 1: Rosa de Vientos**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 11 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Tabla 3: Información General de la Estación Meteorológica de Superficie**

|Código Nacional|200006|
|---|---|
|Código OMM|85418|
|Código OACI|SCDA|
|Nombre de la Estación|Diego Aracena Iquique Ap.|
|Región|Tarapacá|
|Provincia|Iquique|
|Comuna|Iquique|
|Coordenadas UTM|376.877,2 E - 7.727.300,6 N|
|Huso horario|19S|

La estación “Diego Aracena Iquique Ap.” se encuentra dentro del área de modelación que se

presenta en la figura 2.

**Figura 2 Ubicación Estación Meteorológica**

Se ha considerado en el presente análisis la información disponible registrada en la Estación Diego

Aracena Iquique Ap., la que será comparada de manera referencial con la información utilizada para

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 12 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

el modelamiento y que corresponde al modelo meteorológicos de pronóstico WRF.

**3.1 Viento**

Esta sección trata sobre el vector de viento promedio por hora del área ancha (velocidad y dirección)

a 10 metros sobre el suelo. El viento de cierta ubicación depende en gran medida de la topografía

local y de otros factores; y la velocidad instantánea y dirección del viento varían más ampliamente

que los promedios por hora.

**3.1.1** **Velocidad del Viento**

La velocidad promedio del viento por hora en Aeropuerto Internacional Diego Aracena tiene

variaciones estacionales leves en el transcurso del año.

La parte más ventosa del año dura 7,4 meses, del 13 de septiembre al 25 de abril, con velocidades

promedio del viento de más de 11,8 kilómetros por hora. El día más ventoso del año en el 7 de

diciembre, con una velocidad promedio del viento de 13,1 kilómetros por hora.

El tiempo más calmado del año dura 4,6 meses, del 25 de abril al 13 de septiembre. El día más

calmado del año es el 11 de junio, con una velocidad promedio del viento de 10,5 kilómetros por

hora.

**Figura 3: Velocidad Promedio del viento**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 13 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

Durante el periodo comprendido entre el 01/01/2020 y 31/12/2020, la velocidad promedio del

viento, en la Estación Diego Aracena Iquique Ap., fue de 3,90 m/s. ( _fuente: Red Agrometeorológica de_

_INIA)._

**3.1.2** **Dirección del Viento.**

La dirección del viento promedio por hora predominante en el Aeropuerto Internacional Diego

Aracena es de sur durante el año. A continuación se presenta la rosa de viento correspondiente al

período comprendido entre el 01/01/2020 y el 31/12/2020

**3.2 Series de tiempo.**

Las estadísticas de datos válidos monitoreado, durante el periodo 01/01/2020 y el 31/12/2020 en la

Estación Diego Aracena Iquique Ap., es la siguiente:

 - Datos totales: 8.784

 - Datos disponibles: 8.784

 - % datos válidos: 100 %

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 14 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

Las series de tiempo presentadas a continuación para las variables de dirección y velocidad del

viento, permiten un análisis cualitativo de los datos en términos de completitud de la serie. En estas

se puede observar la variabilidad, amplitud de rango y frecuencia de los datos con que se cuenta.

**Figura 4: Serie de tiempo registros horarios de velocidad del viento - Estación Diego Aracena**

**Iquique Ap., periodo 01.01.20 al 31-12-20**

Elaboración: propia
Fuente: www.agrometeorologia.cl

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 15 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 5: Serie de tiempo registros horarios de Dirección del viento - Estación Diego Aracena**

**Iquique Ap., periodo 01.01.20 al 31-12-20**

Elaboración: propia
Fuente: www.agrometeorologia.cl

**3.3 Campos de viento**

La Figura 6, muestran la Rosa de Viento generada con los datos observados de la Estación Diego

Aracena Iquique Ap. durante el periodo (01.01.2020 al 31.12 2020) y la Rosa de Viento generada con

el modelo de pronóstico WRF durante el mismo período, en el mismo punto de localización de la

Estación Diego Aracena Iquique Ap.

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 16 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 6: Rosa de Viento Estación Diego Aracena Iquique Ap. v/s Rosa de Viento modelada con**

**WRF.**

ROSA DE VIENTO ESTACIÓN DIEGO ARACENA, IQUIQUE

Velocidad promedio: 3,90 m/s

ROSA DE VIENTO WRF, IQUIQUE

Velocidad promedio: 4,16 m/s

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 17 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

En la Rosa obtenida en base a las mediciones meteorológicas de la Estación de Diego Aracena

Iquique Ap., se observa que la dirección predominante de los vientos es Sur y Sur Oeste, con

intensidades de los vientos de moderados. Puede apreciarse que el modelo de pronóstico WRF indica

vientos predominantes del Oeste, y con velocidades, menos intentas.

**4.** **BASES DE DATOS Y ARCHIVOS DE MODELACIÓN**

La base de datos para la modelación CALMET-CALPUFF considero la siguiente información:

**Tabla 4: Información para el modelamiento**

**4.1 Archivos de entrada y salida de la modelación**

Los archivos de entrada y salida de la modelación, para cada etapa del proyecto y que se anexan en

forma digital (DVD), son los siguientes:

**Tabla 5: Archivos de entrada y salida de la modelación**

|CALMET|GEO.DAT|
|---|---|
|CALMET|CALMET.DAT|
|CALMET|CALMET.LST|
|CALMET|CALMET.INP|
|CALPUF|CALPUFF.LST|
|CALPUF|CALPUFF.INP|
|CALPUF|CONS.INP|
|CALPOST|CALPOST.DAT|
|CALPOST|CALPOST.LST|
|CALPOST|CALPOST.INP|
|ARCHIVOS COMPLEMENTARIOS|Dry Flux Data File|
|ARCHIVOS COMPLEMENTARIOS|Wet Flux Data|

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 18 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**5.** **CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN Y SU ENTORNO**

**5.1 Localización**

Las coordenadas geográficas de ubicación del proyecto en Datum WGS 84- Huso 19S son las
siguientes:

**Tabla 6: Coordenadas de Ubicación del Proyecto**

|Vértice|Coordenada Norte<br>WGS 84, Huso 19 Sur|Coordenada Este<br>WGS 84, Huso 19 Sur|
|---|---|---|
|V1|7.703.219|384.047|
|V2|7.702.644|384.588|
|V3|7.701.261|383.729|
|V4|7.701.693|383.205|

Nota: Polígono de 120 hectáreas aproximadamente.

**Figura 7 Localización del Proyecto a Nivel Regional**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 19 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**5.2 Área de modelamiento meteorológica**

El área o dominio de modelación considerado tiene su origen en las coordenadas UTM WGS84 19S
E: 406.084 y N: 7.717.424 A partir de este punto, el dominio considera un área de 50 kilómetros en la

dirección Este y 50 kilómetros en la dirección Norte, que incluye la totalidad de las fuentes emisoras

del proyecto, estación de superficie (para comparación referencial) y los receptores circundantes al

proyecto.

**Figura 8: Área de Modelamiento**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 20 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**5.3 Grilla de modelamiento meteorológico**

La grilla de modelamiento utilizada corresponde a un dominio de 100 x 100 km con espaciamiento de

1 km.

**Figura 9: Grilla Meteorológica de Modelamiento**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 21 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**5.4 Topografía del área de modelamiento meteorológico**

La topografía del área de modelamiento se ha obtenido satelitalmente mediante la aplicación de

archivos de terreno del software Calpuff View. La siguiente figura ilustra las curvas de nivel para el

área de modelamiento.

**Figura 10: Topografía del Área de Modelación**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 22 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**5.5 Dominio de modelación de emisiones atmosféricas.**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 23 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**5.6 Receptores en el área de modelamiento**

El área de influencia (AI) para el componente aire se determinó en función de los receptores

sensibles (asentamiento humano), que puedan verse afectados por las emisiones de material

particulado y gases, generados por las actividades de las distintas fases del proyecto Complejo

Industrial Phoenix.

**Tabla 7: Ubicación y descripción de puntos receptores sensibles**

|Punto Receptor|Coordenadas<br>Datum WGS 84 Huso 19S|Col3|Uso de Suelo<br>Efectivo<br>Plano Regulador|Tipo de Zona|Distancia del<br>Proyecto al<br>Receptor (m)|
|---|---|---|---|---|---|
|**Punto Receptor**|**Este**|**Norte**|**Norte**|**Norte**|**Norte**|
|R1<br>Caleta Chanavayita|376.710|7.710.180|Rural|Rural|10.820|
|R2<br>Área industrial<br>deshidratación de<br>concentrado de<br>cobre|378.383|7.700.715|Rural|Industrial|5.800|
|R3<br>Caleta Cáñamo|376.921|7.699.889|Rural|Rural|7.500|
|R4<br>Área industrial<br>Quebrada Blanca|376.960|7.701.702|Rural|Industrial|7.000|

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 24 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 11: Emplazamiento de Puntos Receptores Sensibles**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 25 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**5.7 Suelos del área de modelamiento**

La siguiente figura ilustra el tipo de suelo en el área de modelamiento.

**Figura 12: Uso de Suelo**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 26 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**6.** **RESULTADOS DE LA MODELACIÓN**

Mediante la aplicación del modelo CALPUFF fue posible obtener las concentraciones de material

particulado respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), material particulado

sedimentable (MPS), y concentraciones de gases (SO 2, NOx, CO), que aportará el Proyecto en cada

una de sus fases (construcción, operación y cierre). A continuación, se presentan los resultados del

modelo, análisis de los resultados y mapas de Isoconcentración.

**6.1** **Resultados del Modelo**

Las siguientes tablas resúmenes, presentan los resultados obtenidos de la modelación para cada fase

del proyecto.

**6.1.1 Cumplimiento Normas de Calidad Ambiental Primaria**

Las siguientes tablas presentan las concentraciones de cada contaminante en cada uno de los

receptores y su nivel respecto de la norma respectiva:

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 27 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### Tabla 8: Aportes del Proyecto Etapa de Construcción

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MP10<br>|~~Percentil 98~~<br>Promedio 24<br>horas<br>|150<br>|0,4 <br>|0,2<br>|0,2 <br>|0,1<br>|0,2 <br>|0,1<br>|0,2 <br>|0,2<br>|
|~~MP10~~|~~Promedio Anual~~<br>|~~50~~|~~0,1~~|~~0,2~~|~~0,1~~|~~0,1~~|~~0,0~~|~~0,1~~|~~0,0~~|~~0,1~~|
|MP2,5<br>|~~Percentil 98~~<br>Promedio Diario<br>|50<br>|0,2 <br>|0,4<br>|0,1 <br>|0,2<br>|0,1 <br>|0,2<br>|0,2 <br>|0,3<br>|
|~~MP2,5~~|~~Promedio Anual~~<br>|~~20~~|~~0,1~~|~~0,3~~|~~0,0~~|~~0,2~~|~~0,0~~|~~0,1~~|~~0,0~~|~~0,2~~|
|CO|~~Percentil 99, máx.~~<br>1 hora<br>|30000|0,6|0,0|0,4|0,0|0,3|0,0|0,5|0,0|
|CO|~~Percentil 99, máx.~~<br>8 hora<br>|10000|0,1|0,0|0,1|0,0|0,1|0,0|0,1|0,0|
|NO2<br>|~~Percentil 99, máx.~~<br>1 hora<br>|400<br>|2,3 <br>|0,6<br>|1,7 <br>|0,4<br>|1,3 <br>|0,3<br>|1,9 <br>|0,5<br>|
|~~NO2~~|~~Promedio, Anual~~<br>|~~100~~|~~0,1~~|~~0,1~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|
|SO2|~~Promedio Diario,~~<br>percentil 99|250|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 28 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### Tabla 9: Aportes del Proyecto Etapa de Operación

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R4<br>Área<br>Industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MP10<br>|~~Percentil 98~~<br>Promedio 24 hora<br>|150<br>|0,5 <br>|0,4<br>|0,4 <br>|0,3<br>|0,3 <br>|0,2<br>|0,4 <br>|0,3<br>|
|~~MP10~~|~~Promedio Anual~~<br>|~~50~~|~~0,1~~|~~0,3~~|~~0,1~~|~~0,1~~|~~0,0~~|~~0,1~~|~~0,1~~|~~0,1~~|
|MP2,5<br>|~~Percentil 98~~<br>Promedio Diario<br>|50<br>|0,4 <br>|0,8<br>|0,4 <br>|0,7<br>|0,3 <br>|0,5<br>|0,3 <br>|0,7<br>|
|~~MP2,5~~|~~Promedio Anual~~<br>|~~20~~|~~0,1~~|~~0,6~~|~~0,1~~|~~0,3~~|~~0,0~~|~~0,2~~|~~0,0~~|~~0,2~~|
|CO|~~Percentil 99, máx.~~<br>1 hora<br>|30000|18,9|0,1|33,7|0,1|10,3|0,0|16,6|0,1|
|CO|~~Percentil 99, máx.~~<br>8 hora<br>|10000|3,6|0,0|4,6|0,1|2,1|0,0|2,9|0,0|
|NO2<br>|~~Percentil 99, máx.~~<br>1 hora<br>|400<br>|57,0 <br>|14,2<br>|53,1 <br>|13,3<br>|31,4 <br>|7,9<br>|46,3 <br>|11,6<br>|
|~~NO2~~|~~Promedio, Anual~~<br>|~~100~~|~~1,4~~|~~1,4~~|~~0,5~~|~~0,5~~|~~0,4~~|~~0,4~~|~~0,5~~|~~0,5~~|
|SO2|~~Promedio Diario,~~<br>percentil 99|250|0,3|0,1|0,3|0,1|0,2|0,1|0,3|0,1|

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 29 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### Tabla 10: Aportes del Proyecto Etapa de Cierre

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MP10<br>|~~Percentil 98~~<br>Promedio 24 horas<br>|150<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|
|~~MP10~~|~~Promedio Anual~~<br>|~~50~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|
|MP2,5<br>|~~Percentil 98~~<br>Promedio Diario<br>|50<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|
|~~MP2,5~~|~~Promedio Anual~~<br>|~~20~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|
|CO|~~Percentil 99, máx.~~<br>1 hora<br>|30000|0,3|0,0|0,2|0,0|0,2|0,0|0,3|0,0|
|CO|~~Percentil 99, máx.~~<br>8 hora<br>|10000|0,1|0,0|0,0|0,0|0,0|0,0|0,1|0,0|
|NO2<br>|~~Percentil 99, máx.~~<br>1 hora<br>|400<br>|1,2<br>|0,3<br>|0,9<br>|0,2<br>|0,7<br>|0,2<br>|1,0<br>|0,3<br>|
|~~NO2~~|~~Promedio, Anual~~<br>|~~100~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|
|SO2|~~Promedio Diario,~~<br>percentil 99|250|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 30 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### 6.1.2 Cumplimiento Normas de Calidad Ambiental Secundaria Tabla 11: Aportes del Proyecto Etapa de Construcción

|Parámetro|Estadístico|Limite<br>Norma<br>(mg/m2día)|Conc.<br>(mg/m2día)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MPS|~~Promedio~~<br>Mensual<br>|150<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|
|MPS|~~Promedio Anual~~|~~100~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|SO2|~~Promedio Anual~~<br>|~~80~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|
|SO2|~~Percentil 99.7~~<br>Conc. Diaria<br>|365|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|
|SO2|~~Percentil 99.73~~<br>Conc. 1 hora|1.000|0,1|0,0|0,1|0,0|0,1|0,0|0,1|0,0|

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 31 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### Tabla 12: Aportes del Proyecto Etapa de Operación

|Parámetro|Estadístico|Limite<br>Norma<br>(mg/m2día)|Conc.<br>(mg/m2día)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor R3<br>Caleta<br>Cáñamo|%<br>Respect<br>o de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MPS|~~Promedio~~<br>Mensual<br>|150<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|0,00<br>|
|MPS|~~Promedio Anual~~|~~100~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|SO2|~~Promedio Anual~~<br><br>|~~80~~|~~0,1~~|~~0,1~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|
|SO2|~~Percentil~~<br>~~99.7~~<br>Conc. Diaria<br><br>|365|0,3|0,1|0,3|0,1|0,2|0,1|0,3|0,1|
|SO2|~~Percentil~~<br>~~99.73~~<br>Conc. 1 hora|1.000|2,6|0,3|3,2|0,3|1,7|0,2|2,4|0,2|

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 32 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### Tabla 13: Aportes del Proyecto Etapa de Cierre

|Parámetro|Estadístico|Limite<br>Norma<br>(mg/m2día)|Conc.<br>(mg/m2día)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MPS|~~Promedio~~<br>Mensual<br>|150<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|
|MPS|~~Promedio Anual~~|~~100~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|SO2|~~Promedio Anual~~<br>|~~80~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|
|SO2|~~Percentil 99.7~~<br>Conc. Diaria<br>|365|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|
|SO2|~~Percentil 99.73~~<br>Conc. 1 hora|1.000|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|

### Nota 1: Tablas 11, 12 y 13 los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día Nota 2: Tablas 11, 12 y 13 los aportes de SO 2 en cada uno de los receptores, se expresan en μg/m [3] N

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 33 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**7.** **ANÁLISIS DE INCERTIDUMBRE**

**7.1 Análisis cualitativo de los campos de vientos**

Respecto de la dirección de los vientos en la estación, no existen mayores diferencias entre lo

observado y lo modelado.

De acuerdo con la información presentada en el apartado 3.3 (Campos de Vientos), los campos de

vientos provienen principalmente de la dirección suroeste

Al comparar los datos anteriores con los campos de vientos generados por el modelo utilizando

meteorología WRF, se aprecia que existe bastante similitud con el modelo de pronóstico.

Conforme a lo anterior, se puede concluir que en gran parte del día coinciden las direcciones de los

vientos.

A partir de lo anterior se puede sostener que el modelo meteorológico predice de buena forma el

comportamiento espacial de los flujos de viento, ya que las diferencias entre las direcciones del

viento son mínimas.

**7.2 Análisis cuantitativo para el cálculo de incertidumbre**

El análisis cuantitativo consiste en determinar el % de variación que experimenta la velocidad

promedio del viento entre los valores utilizados en el modelo versus los valores observados de

velocidad del viento.

De acuerdo a los datos registrados en la Estación Diego Aracena Iquique Ap., la velocidad promedio

del viento registrada por dicha estación (considerando un universo de 8.874 datos, que representan

el 100% del total de datos del año 2020), es de 3,90 m/s

Al modelar con WRF en el punto de localización de la Estación Diego Aracena Iquique Ap., el modelo

arroja una velocidad media del viento para el mismo período de 4,16 m/s

Las velocidades promedias registradas en las estaciones de monitoreo (valor observado) versus las

representadas por el modelo (valor modelado) se tiene que:

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 34 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Tabla 14: Velocidad promedio del Viento en m/s**

|Estación|Promedio Observado|Promedio Pronóstico<br>WRF|% de Error|
|---|---|---|---|
|Diego Aracena Iquique<br>Ap.|3,90|4,16|6,7|

_% Error_
_V_ = % de error entre los valores modelado y observado de la velocidad del viento.

(Valor modelado) = 4,16 m/s

(Valor observado) = 3,90 m/s

4,16 (m/s) - 3,90 (m/s) I

% de Error = [x] 100

3,90 (m/s)

% de Error = 6,7 %

Conforme a lo anterior, se observa que el modelo sobrestima en 6,7% la velocidad del viento con

respecto a los datos observados de la Estación Diego Aracena Iquique Ap.

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 35 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Tabla 15: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98<br>Promedio 24<br>horas|150|0,37|0,19|0,19|0,09|0,19|0,09|0,19|0,19|
|MP10|Promedio Anual|50|0,09|0,19|0,09|0,09|0,00|0,09|0,00|0,09|
|MP2,5|Percentil 98<br>Promedio Diario|50|0,19|0,37|0,09|0,19|0,09|0,19|0,19|0,28|
|MP2,5|Promedio Anual|20|0,09|0,28|0,00|0,19|0,00|0,09|0,00|0,19|
|CO|Percentil 99, máx.<br>1 hora|30000|0,56|0,00|0,37|0,00|0,28|0,00|0,47|0,00|
|CO|Percentil 99, máx.<br>8 hora|10000|0,09|0,00|0,09|0,00|0,09|0,00|0,09|0,00|
|NO2|Percentil 99, máx.<br>1 hora|400|2,15|0,56|1,59|0,37|1,21|0,28|1,77|0,47|
|NO2|Promedio, Anual|100|0,09|0,09|0,00|0,00|0,00|0,00|0,00|0,00|
|SO2|Promedio Diario,<br>percentil 99|250|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 36 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### Tabla 16: Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MP10<br>|~~Percentil 98~~<br>Promedio 24 hora<br>|150<br>|0,47 <br>|0,37<br>|0,37 <br>|0,28<br>|0,28 <br>|0,19<br>|0,37 <br>|0,28<br>|
|~~MP10~~|~~Promedio Anual~~<br>|~~50~~|~~0,09~~|~~0,28~~|~~0,09~~|~~0,09~~|~~0,00~~|~~0,09~~|~~0,09~~|~~0,09~~|
|MP2,5<br>|~~Percentil 98~~<br>Promedio Diario<br>|50<br>|0,37 <br>|0,75<br>|0,37 <br>|0,65<br>|0,28 <br>|0,47<br>|0,28 <br>|0,65<br>|
|~~MP2,5~~|~~Promedio Anual~~<br>|~~20~~|~~0,09~~|~~0,56~~|~~0,09~~|~~0,28~~|~~0,00~~|~~0,19~~|~~0,00~~|~~0,19~~|
|CO|~~Percentil 99, máx.~~<br>1 hora<br>|30000|17,63|0,09|31,44|0,09|9,61|0,00|15,49|0,09|
|CO|~~Percentil 99, máx.~~<br>8 hora<br>|10000|3,36|0,00|4,29|0,09|1,96|0,00|2,71|0,00|
|NO2<br>|~~Percentil 99, máx.~~<br>1 hora<br>|400<br>|53,18 <br>|13,25<br>|49,54 <br>|12,41<br>|29,30 <br>|7,37<br>|43,20 <br>|10,82<br>|
|~~NO2~~|~~Promedio, Anual~~<br>|~~100~~|~~1,31~~|~~1,31~~|~~0,47~~|~~0,47~~|~~0,37~~|~~0,37~~|~~0,47~~|~~0,47~~|
|SO2|~~Promedio Diario,~~<br>percentil 99|250|0,28|0,09|0,28|0,09|0,19|0,09|0,28|0,09|

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 37 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### Tabla 17: Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MP10<br>|~~Percentil 98~~<br>Promedio 24 horas<br>|150<br>|0,00 <br>|0,00<br>|0,00 <br>|0,00<br>|0,00 <br>|0,00<br>|0,00 <br>|0,00<br>|
|~~MP10~~|~~Promedio Anual~~<br>|~~50~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|
|MP2,5<br>|~~Percentil 98~~<br>Promedio Diario<br>|50<br>|0,00 <br>|0,00<br>|0,00 <br>|0,00<br>|0,00 <br>|0,00<br>|0,00 <br>|0,00<br>|
|~~MP2,5~~|~~Promedio Anual~~<br>|~~20~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|
|CO|~~Percentil 99, máx.~~<br>1 hora<br>|30000|0,28|0,00|0,19|0,00|0,19|0,00|0,28|0,00|
|CO|~~Percentil 99, máx.~~<br>8 hora<br>|10000|0,09|0,00|0,00|0,00|0,00|0,00|0,09|0,00|
|NO2<br>|~~Percentil 99, máx.~~<br>1 hora<br>|400<br>|1,12 <br>|0,28<br>|0,84 <br>|0,19<br>|0,65 <br>|0,19<br>|0,93 <br>|0,28<br>|
|~~NO2~~|~~Promedio, Anual~~<br>|~~100~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|
|SO2|~~Promedio Diario,~~<br>percentil 99|250|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 38 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

### Tabla 18: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección

|Parámetro|Estadístico|Limite<br>Norma<br>(mg/m2día)|Conc.<br>(mg/m2día)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MPS|~~Promedio~~<br>Mensual<br>|150<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|0,0<br>|
|MPS|~~Promedio Anual~~|~~100~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|~~0,0~~|

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayit<br>a|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|SO2|~~Promedio Anual~~<br>|~~80~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|~~0,00~~|
|SO2|~~Percentil 99.7~~<br>Conc. Diaria<br>|365|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|SO2|~~Percentil 99.73~~<br>Conc. 1 hora|1.000|0,09|0,00|0,09|0,00|0,09|0,00|0,09|0,00|

#### INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 39 de 84 Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Tabla 19 Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(mg/m2día)|Conc.<br>(mg/m2día)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor R3<br>Caleta<br>Cáñamo|%<br>Respect<br>o de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MPS|Promedio<br>Mensual|150|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|
|MPS|Promedio Anual|100|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|SO2|Promedio Anual|80|0,09|0,09|0,00|0,00|0,00|0,00|0,00|0,00|
|SO2|Percentil<br>99.7<br>Conc. Diaria|365|0,28|0,09|0,28|0,09|0,19|0,09|0,28|0,09|
|SO2|Percentil<br>99.73<br>Conc. 1 hora|1.000|2,43|0,28|2,99|0,28|1,59|0,19|2,24|0,19|

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 40 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Tabla 20 Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(mg/m2día)|Conc.<br>(mg/m2día)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|MPS|Promedio<br>Mensual|150|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|
|MPS|Promedio Anual|100|0,0|0,0|0,0|0,0|0,0|0,0|0,0|0,0|

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Conc.<br>(μg/m3N)<br>Receptor<br>R1<br>Caleta<br>Chanavayita|%<br>Respecto<br>de la<br>Norma|Conc.<br>(μg/m3N)<br>Receptor<br>R2<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R3<br>Caleta<br>Cáñamo|%<br>Respecto<br>de la<br>Norma|Conc.<br>(mg/m2día)<br>Receptor<br>R4<br>Área<br>industrial|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|
|SO2|Promedio Anual|80|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|SO2|Percentil 99.7<br>Conc. Diaria|365|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|SO2|Percentil 99.73<br>Conc. 1 hora|1.000|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

Nota 1: Tablas 18, 19 y 20 los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día
Nota 2: Tablas 18, 19 y 20 los aportes de SO 2 en cada uno de los receptores, se expresan en μg/m [3] N

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 41 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**8.** **ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE**

El presente estudio de dispersión de emisiones atmosféricas ha considerado 4 receptores de interés,

localizados en el entorno al área del proyecto, los que se indican a continuación:

|Punto Receptor|Coordenadas<br>Datum WGS 84 Huso 19S|Col3|Uso de Suelo<br>Efectivo<br>Plano Regulador|Tipo de<br>Zona|Distancia del<br>Proyecto al<br>Receptor (m)|
|---|---|---|---|---|---|
|**Punto Receptor**|**Este**|**Norte**|**Norte**|**Norte**|**Norte**|
|R1<br>Caleta Chanavayita|376.710|7.710.180|Rural|Rural|10.820|
|R2<br>Área industrial<br>deshidratación de<br>concentrado de<br>cobre|378.383|7.700.715|Rural|Industrial|5.800|
|R3<br>Caleta Cáñamo|376.921|7.699.889|Rural|Rural|7.500|
|R4<br>Área industrial<br>Quebrada Blanca|376.960|7.701.702|Rural|Industrial|7.000|

Sobre estos receptores se ha determinado el nivel de impacto que generara el proyecto en cada una

de sus fases.

**8.1 Análisis de Cumplimiento Normativo Vigente Para MP10**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la

calidad del aire por MP10. El mayor impacto se genera durante la fase de operación sobre el receptor
número 1 con 0,47 μg/m [3] N como promedio de 24 horas, lo que representa un 0,37 % respecto del

valor de la norma.

**8.2 Análisis de Cumplimiento Normativo Vigente Para MP2,5**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la

calidad del aire por MP2,5. El mayor impacto se genera durante la fase de construcción sobre el
receptor número 1 con 0,37 μg/m [3] N como promedio de 24 horas, lo que representa un 0,75%

respecto del valor de la norma.

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 42 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**8.3 Análisis de Cumplimiento Normativo Vigente Para MPS**

No existen zonas biológicas de interés cercanas al área del proyecto por lo que se han defino como

receptores biológicos los mismos receptores humanos anteriormente analizados. Respecto de ello se

puede señalar que no existe impacto sobre alguno de ellos ya que todos los valores son

extremadamente bajos, representando un nulo aporte (0,0% respecto del valor de la norma).

**8.4 Análisis de Cumplimiento Normativo Vigente Para Gases CO**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la

calidad del aire por CO en los receptores analizados ya que todos los valores son extremadamente

bajos respecto a los límites máximos permitidos por norma.

**8.5 Análisis de Cumplimiento Normativo Vigente Para Gases NO** **2**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la

calidad del aire por NO 2 en los receptores analizados ya que todos los valores son extremadamente

bajos respecto a los límites máximos permitidos por norma.

**8.6 Análisis de Cumplimiento Normativo Vigente Para Gases SO** **2**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la

calidad del aire por SO 2 en los receptores analizados ya que todos los valores son extremadamente

bajos respecto a los límites máximos permitidos por norma.

**8.7 Puntos de Máximo Impacto**

De acuerdo con los resultados de la modelación, los puntos de máximo impacto generados por el

proyecto, en cada una de sus fases, se presentan en las siguientes tablas, indicando ubicación en

coordenadas UTM WGS-84 Huso 19S y concentración máxima:

**Tabla 21: Puntos de Máximo Impacto - Fase de Construcción**

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Este**|**Norte**|**Norte**|
|MP10|Percentil 98 Promedio 24 horas|383.586|7.701.920|22,9|
|MP10|Promedio Anual|383.586|7.701.920|12,1|
|MP2,5|Percentil 98 Promedio Diario|383.586|7.701.920|15,7|

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 43 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

|MP2,5|Promedio Trianual|383.586|7.701.920|8,8|
|---|---|---|---|---|
|CO|Percentil 99, máx. 1 hora|383.586|7.701.920|430,1|
|CO|Percentil 99, máx. 8 hora|383.586|7.701.920|60,7|
|NO2|Percentil 99, máx. 1 hora|383.586|7.701.920|1979,3|
|NO2|Promedio, Anual|383.586|7.701.920|32,9|
|SO2|Percentil 99,73 Concentración 1 hora|383.586|7.701.920|89,7|
|SO2|Promedio Diario, percentil 99|383.586|7.701.920|7,3|
|SO2|Promedio, Anual|383.586|7.701.920|2,2|

**Tabla 22: Puntos de Máximo Impacto - Fase de Operación**

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Este**|**Norte**|**Norte**|
|MP10|Percentil 98 Promedio 24 horas|383.586|7.701.920|267,0|
|MP10|Promedio Anual|383.586|7.701.920|74,7|
|MP2,5|Percentil 98 Promedio Diario|383.586|7.701.920|257,0|
|MP2,5|Promedio Trianual|383.586|7.701.920|64,2|
|CO|Percentil 99, máx. 1 hora|383.586|7.701.920|19019,0|
|CO|Percentil 99, máx. 8 hora|383.586|7.701.920|2482,0|
|NO2|Percentil 99, máx. 1 hora|383.586|7.701.920|56918,0|
|NO2|Promedio, Anual|383.586|7.701.920|866,0|
|SO2|Percentil 99,73 Concentración 1 hora|383.586|7.701.920|3614,0|
|SO2|Promedio Diario, percentil 99|383.586|7.701.920|267,0|
|SO2|Promedio, Anual|383.586|7.701.920|55,9|

**Tabla 23: Puntos de Máximo Impacto - Fase de Cierre**

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Este**|**Norte**|**Norte**|
|MP10|Percentil 98 Promedio 24 horas|383.586|7.701.920|4,3|
|MP10|Promedio Anual|383.586|7.701.920|1,9|
|MP2,5|Percentil 98 Promedio Diario|383.586|7.701.920|3,5|
|MP2,5|Promedio Trianual|383.586|7.701.920|1,2|
|CO|Percentil 99, máx. 1 hora|383.586|7.701.920|217,1|
|CO|Percentil 99, máx. 8 hora|383.586|7.701.920|30,7|
|NO2|Percentil 99, máx. 1 hora|383.586|7.701.920|980,2|
|NO2|Promedio, Anual|383.586|7.701.920|16,4|
|SO2|Percentil 99,73 Concentración 1 hora|383.586|7.701.920|44,9|
|SO2|Promedio Diario, percentil 99|383.586|7.701.920|3,6|
|SO2|Promedio, Anual|383.586|7.701.920|1,1|

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 44 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**9.** **CONCLUSIONES**

Los resultados obtenidos de la modelación realizada y el análisis efectuado en los apartados

anteriores, indican que el proyecto, en general, no presenta impactos en la calidad del aire en

ninguno de los receptores analizados, y por lo tanto, no compromete la salud de la población.

Con respecto a si generan efectos adversos significativos sobre los recursos naturales del sector, al

igual que en el caso anterior, no se presentan impactos en ninguna de las zonas analizadas, en

consecuencia, no se presentan efectos adversos significativos sobre los recursos naturales.

**10.MAPAS DE ISOCONCENTRACIONES**

En las siguientes figuras se presentan las curvas de Isoconcentración para las 3 etapas (Operación,

Construcción y Cierre), como puede apreciarse en las tablas de resultados y láminas de

Isoconcentración, el proyecto no genera ningún tipo impactos significativos en la calidad del aire en

zona poblada.

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 45 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 13: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (24 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 46 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 14: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 47 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 15: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (24 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 48 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 16: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 49 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 17: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Construcción (24 horas)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 50 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 18: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Construcción (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 51 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 19: Mapa de Isoconcentración Gases CO - Etapa de Construcción (1h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 52 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 20: Mapa de Isoconcentración Gases CO - Etapa de Construcción (8h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 53 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 21: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (1 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 54 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 22: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 55 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 23: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (1h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 56 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 24: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (24h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 57 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 25: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 58 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 26: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (24 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 59 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 27: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 60 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 28: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (24 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 61 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 29: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 62 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 30: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Operación (mensual).**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 63 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 31: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Operación (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 64 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 32: Mapa de Isoconcentración Gases CO - Etapa de Operación (1h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 65 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 33: Mapa de Isoconcentración Gases CO - Etapa de Operación (8h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 66 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 34: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (1 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 67 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 35: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 68 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 36: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (1h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 69 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 37: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (24h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 70 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 38: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 71 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 39: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (24 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 72 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 40: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 73 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 41: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (24 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 74 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 42: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 75 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 43: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre (mensual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 76 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 44: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 77 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 45: Mapa de Isoconcentración Gases CO - Etapa de Cierre (1h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 78 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 46: Mapa de Isoconcentración Gases CO - Etapa de Cierre (8h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 79 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 47: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (1 h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 80 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 48: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 81 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 49: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (1h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 82 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 50: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (24h)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 83 de 84
Agosto 2021

DECLARACIÓN DE IMPACTO AMBIENTAL

COMPLEJO INDUSTRIAL PHOENIX

**Figura 51: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (Anual)**

INFORME MODELAMIENTO DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS - Rev. B4 Página 84 de 84
Agosto 2021