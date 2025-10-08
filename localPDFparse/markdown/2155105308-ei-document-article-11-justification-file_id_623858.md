---
title: Sin título
author: p_reszczynski@jaimeillanes.cl
date: D:20220214113139-03'00'
language: es
type: manual
pages: 25
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO CA-1
-->

# ANEXO CA-1

## MODELACIÓN CALIDAD DEL AIRE

### _Cliente:_

**ÍNDICE**

1. INTRODUCCIÓN ....................................................................................................................................... 1

2. OBJETIVO .................................................................................................................................................... 1

3. MARCO LEGAL .......................................................................................................................................... 2

4. METODOLOGIA ........................................................................................................................................ 4

4.1. BASE TEÓRICA DEL MODELO UTILIZADO ................................................................................ 4

4.2. CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN ....................................................... 5

4.3. ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF Y FACTOR DE

CORRECIÓN ...................................................................................................................................... 7

5. PARÁMETROS DE ENTRADA DEL MODELO ................................................................................... 8

5.1. CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO ....................................................... 8

5.2. PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN ................ 8

5.3. ANALISIS DE INCERTIDUMBRE Y DETERMINACIÓN DEL FACTOR DE CORRECCIÓN

............................................................................................................................................................. 12

6. RESULTADOS ........................................................................................................................................... 13

6.1.1. PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC) ........................................................... 13

6.2. RESULTADOS DE LA MODELACIÓN ......................................................................................... 14

6.2.1. FASE DE CONSTRUCCIÓN ....................................................................................................... 14

7. CUMPLIMIENTO DE NORMATIVA ................................................................................................... 18

8. CONCLUSIONES ..................................................................................................................................... 22

**APÉNDICES**

Apéndice 1 Archivos de Modelación

Apéndice 2 Isoconcentraciones Fase de Construcción

ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**TABLAS**

TABLA 1: Norma Primaria de Calidad del Aire ................................................................... 2

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- a), b) y d) del artículo 11 de la Ley 19.300 en el área de influencia del Proyecto en su fase de construcción en el “peor escenario”, se ha considerado la normativa ambiental primaria y secundaria de calidad de aire vigente para MP 10, MP 2,5, MPS, NO 2, SO 2 y CO, presentadas en las tablas a continuación: -->

**Tabla 1: Norma Primaria de Calidad del Aire**

| Parámetro | Cuerpo Legal | Estadístico | Valor |
| --- | --- | --- | --- |
| MP10 | D.S. N°59/98<br>MINSEGPRES,<br>modificada por<br>D.S. N°45/01 | Promedio aritmético de tres años calendario<br>consecutivos | 50 μg/m3N |
| MP10 | D.S. N°59/98<br>MINSEGPRES,<br>modificada por<br>D.S. N°45/01 | Percentil 98 de las concentraciones de 24 horas<br>registradas durante un período anual | 150 μg/ m3N |
| MP2,5 | D.S. N°12/11<br>del MMA | Promedio trianual de las concentraciones anuales | 20 μg/m3 |
| MP2,5 | D.S. N°12/11<br>del MMA | Percentil 98 de los promedios diarios registrados<br>durante un año | 50 μg/m3 |
| NO2 | D.S. N°<br>114/2002 del<br>MINSEGPRES | Promedio<br>aritmético<br>de<br>los<br>valores<br>de<br>concentración anual de tres años calendarios<br>sucesivos | 100 μg/m3N |
| NO2 | D.S. N°<br>114/2002 del<br>MINSEGPRES | Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario | 400 μg/m3N |
| SO2 | D.S.<br>N°<br>104/2019<br>del<br>MINSEGPRES | Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 99 de las<br>concentraciones de 24 horas registradas cada año | 150 μg/m3N |
| SO2 | D.S.<br>N°<br>104/2019<br>del<br>MINSEGPRES | Promedio aritmético de tres años calendario<br>sucesivos de los valores de concentración anual | 60 μg/m3N |
| SO2 | D.S.<br>N°<br>104/2019<br>del<br>MINSEGPRES | Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 98,5 de las<br>concentraciones de 1 hora registradas cada año | 350 μg/m3N |
| CO | D.S. N°<br>115/2002 del<br>MINSEGPRES | Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario | 30 mg/m3N |
| CO | D.S. N°<br>115/2002 del<br>MINSEGPRES | Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 8 horas (promedio móvil)<br>registrados durante un año calendario | 10 mg/m3N |

<!-- Estadísticas: 11 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: SINCA, 2022. 2 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE -->
<!-- FIN TABLA 1 -->


TABLA 2: Norma Secundaria de Calidad del Aire .............................................................. 3

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE Para el caso de la normativa de calidad secundaria, se ha considerado la norma suiza como referencia para el análisis de MPS. -->

**Tabla 2: Norma Secundaria de Calidad del Aire**

| Parámetro | Cuerpo Legal | Estadístico | Valor |
| --- | --- | --- | --- |
| SO2 | D.S. N°22/09 del<br>MINSEGPRES | Promedio<br>aritmético<br>de<br>tres<br>años<br>calendario sucesivos de los valores del<br>percentil 99,73 de las concentraciones de 1<br>hora registradas cada año | 1.000 μg/m3N |
| SO2 | D.S. N°22/09 del<br>MINSEGPRES | Promedio<br>aritmético<br>de<br>tres<br>años<br>calendario sucesivos de los valores del<br>percentil 99,7 de las concentraciones de 24<br>horas registradas cada año | 365 μg/m3N |
| SO2 | D.S. N°22/09 del<br>MINSEGPRES | Promedio<br>aritmético<br>de<br>tres<br>años<br>calendario sucesivos de los valores de<br>concentración anual | 80 μg/m3N |
| MPS | Ordinance on Air<br>Pollution Control<br>(OAPC) -<br>Confederación Suiza | Promedio anual (media aritmética). | 200<br>mg/m2/día |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: SINCA, 2022. 3 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE -->
<!-- FIN TABLA 2 -->


TABLA 3: Ubicación Receptores primarios y secundarios .............................................. 5

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- corresponde a receptores cada 1,10 km a lo largo de la localidad. Por otro lado, se incorporaron receptores secundarios, aguas arriba de la Quebrada de Vítor (o también conocida como Quebrada de Chaca), cuya ubicación se presenta a continuación, en la siguiente tabla. -->

**Tabla 3: Ubicación Receptores primarios y secundarios**

| ID | Nombre | Tipo de receptor | Coordenadas UTM WGS84 Huso 19S | Col5 |
| --- | --- | --- | --- | --- |
| **ID** | **Nombre** | **Tipo de receptor** | **Este [m]** | **Norte [m]** |
| R_1 | R1 | Primario/Secundario | 381.629 | 7.917.047 |
| R_2 | R2 | Primario/Secundario | 380.763 | 7.917.805 |
| R_3 | R3 | Primario/Secundario | 379.936 | 7.918.538 |
| R_4 | R4 | Primario/Secundario | 379.129 | 7.919.233 |
| R_5 | R5 | Primario/Secundario | 378.363 | 7.919.974 |
| R_6 | R6 | Primario/Secundario | 377.217 | 7.920.529 |
| R_7 | R7 | Secundario | 387.833 | 7.913.381 |
| R_8 | R8 | Secundario | 385.394 | 7.914.735 |
| R_9 | R9 | Secundario | 383.092 | 7.916.652 |

<!-- Estadísticas: 10 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: JIA, 2022. Para una mejor comprensión, en la siguiente figura se presenta la ubicación geográfica del dominio de modelación y los receptores discretos. -->
<!-- FIN TABLA 3 -->


TABLA 4: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- acuerdo con la configuración definida por el SEA en su Guía de modelación: cuenta con una resolución horizontal de 1 [km] y una resolución vertical de 10 niveles a 20, 40, 80, 160, 320, 640, 1.200, 2.000, 3.000 y 4.000 metros. En la tabla a continuación se señalan las coordenadas de los vértices del dominio de modelación WRF/CALPUFF. -->

**Tabla 4: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF**

| Vértices | Coordenadas UTM [m] Datum: WGS-84, Huso: 19S | Col3 |
| --- | --- | --- |
| **Vértices** | **Este** | **Norte** |
| **SW** | 357.166,85 | 7.886.678,31 |
| **NE** | 406.859,13 | 7.936.632,36 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 6 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE |Vértices|Coordenadas UTM [m] Datum: WGS-84, Huso: 19S|Col3| -->
<!-- FIN TABLA 4 -->


........................................................................................................................................... 6

TABLA 5: Tasas de emisión, fuentes de área ....................................................................... 9

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- incrementan las tasas de emisión). 8 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE -->

**Tabla 5: Tasas de emisión, fuentes de área**

| Fuente | Tasa de emisión [kg/m2-h] | Col3 | Col4 | Col5 | Col6 | Col7 | Área<br>[m2] | Tiempo<br>[h] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **MP30 ** | **MP10 ** | **MP2,5 ** | **CO** | **NOX (*)** | **SO2 ** | **SO2 ** | **SO2 ** |
| Línea de<br>transmisión | 3,22 E-<br>06 | 1,94 E-<br>06 | 1,74 E-<br>06 | 1,16 E-<br>05 | 1,87 E-<br>05 | 3,65 E-<br>07 | 130.132,0 | 4.380 |
| Obras Fase I | 3,43 E-<br>07 | 1,92 E-<br>07 | 1,69 E-<br>07 | 1,25 E-<br>06 | 1,69 E-<br>06 | 1,00 E-<br>08 | 3.321.103<br>,2 | 4.380 |

<!-- Estadísticas: 3 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Nota (*): Se ha considerado una proporción de NO/NO 2 respecto de los niveles de emisión de NO X, asumiendo que el 90% generado es NO y el restante 10% -->
<!-- FIN TABLA 5 -->


TABLA 6: Tasas de emisión, fuentes de camino ................................................................. 9

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- corresponde a NO 2 ; Fuente: JIA, 2022. -->

**Tabla 6: Tasas de emisión, fuentes de camino**

| Fuente | Tasa de emisión [kg/m-h] | Col3 | Col4 | Col5 | Col6 | Col7 | Largo<br>[m] | Tiempo<br>[h] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **MP30 ** | **MP10 ** | **MP2,5 ** | **CO** | **NOX (*)** | **SO2 ** | **SO2 ** | **SO2 ** |
| Ruta Pavimentada 1 | 1,51 E-<br>05 | 2,97 E-<br>06 | 7,87 E-<br>07 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 41.555,7 | 4.380 |
| Ruta NO<br>Pavimentada 1 | 2,00 E-<br>03 | 5,73 E-<br>04 | 5,74 E-<br>05 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 10.957,9 | 4.380 |
| Ruta NO<br>Pavimentada 2 | 1,82 E-<br>03 | 5,20 E-<br>04 | 5,20 E-<br>05 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 762,9 | 4.380 |
| Ruta NO<br>Pavimentada 3 | 1,51 E-<br>03 | 4,32 E-<br>04 | 4,32 E-<br>05 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 968,3 | 4.380 |
| Ruta NO<br>Pavimentada 4 | 1,51 E-<br>03 | 4,30 E-<br>04 | 4,31 E-<br>05 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 1.008,5 | 4.380 |
| Ruta NO<br>Pavimentada 5 | 1,26 E-<br>03 | 3,59 E-<br>04 | 3,60 E-<br>05 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 3.526,6 | 4.380 |
| Ruta NO<br>Pavimentada 6 | 5,97 E-<br>05 | 1,71 E-<br>05 | 1,79 E-<br>06 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 1.329,5 | 4.380 |
| Ruta NO<br>Pavimentada 7 | 5,94 E-<br>05 | 1,70 E-<br>05 | 1,79 E-<br>06 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 4.328,5 | 4.380 |
| Ruta NO<br>Pavimentada 8 | 6,01 E-<br>05 | 1,72 E-<br>05 | 1,81 E-<br>06 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 496,4 | 4.380 |
| Ruta NO<br>Pavimentada 9 | 5,89 E-<br>05 | 1,69 E-<br>05 | 1,77 E-<br>06 | 4,07 E-<br>07 | 8,22 E-<br>06 | 2,35 E-<br>08 | 334,2 | 4.380 |
| Ruta NO<br>Pavimentada 10 | 0,00<br>E+00 | 0,00<br>E+00 | 0,00<br>E+00 | 0,00<br>E+00 | 0,00<br>E+00 | 0,00<br>E+00 | 2.628,5 | 4.380 |

<!-- Estadísticas: 12 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Nota (*): Se ha considerado una proporción de NO/NO 2 respecto de los niveles de emisión de NO X, asumiendo que el 90% generado es NO y el restante 10% -->
<!-- FIN TABLA 6 -->


TABLA 7: Tasas de emisión, fuentes puntuales ................................................................ 10

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente: JIA, 2022. 9 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE -->

**Tabla 7: Tasas de emisión, fuentes puntuales**

| Fuente | Tasa de emisión [kg/h] | Col3 | Col4 | Col5 | Col6 | Col7 | Altura<br>de<br>Chime<br>nea<br>[m] | Temper<br>atura de<br>salida<br>[K] | Diám<br>etro<br>intern<br>o [m] | Veloci<br>dad<br>de<br>salida<br>de<br>gases<br>[m/s] | Tiemp<br>o [h] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **MP30 ** | **MP10** | **MP2,5 ** | **CO** | **NOX **<br>**(*)** | **SO2 ** | **SO2 ** | **SO2 ** | **SO2 ** | **SO2 ** | **SO2 ** |
| Grupo<br>Electrógeno<br>Fijo | 9,34<br>E-02 | 9,34<br>E-02 | 9,34<br>E-02 | 2,86<br>E-01 | 1,33<br>E+00 | 8,74<br>E-02 | 1,76 | 770,00 | 0,10 | 26,21 | 4.380 |

<!-- Estadísticas: 2 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- Nota (*): Se ha considerado una proporción de NO/NO 2 respecto de los niveles de emisión de NO X, asumiendo que el 90% generado es NO y el restante 10% -->
<!-- FIN TABLA 7 -->


TABLA 8: Estadígrafos de ajuste de la modelación meteorológica, Estación Altos

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de Agrometeorología del INIA, específico, para la estación Chaca para el año 2020, que corresponde al período de valores obtenidos mediante el modelo WRF. A partir de ambos conjuntos de datos, se realizó un breve análisis estadístico, según lo descrito en el inciso 4.3. Los resultados obtenidos son presentados en la tabla a continuación: -->

**Tabla 8: Estadígrafos de ajuste de la modelación meteorológica, Estación Altos La Portada**

| Estación | Variable | RMSE | BIAS | Bondad<br>BIAS | IOA | Bondad<br>IOA |
| --- | --- | --- | --- | --- | --- | --- |
| Chaca | Dirección del<br>viento (°) | 133,72 | 55,98 | <+-/10 | 0,65 | -- |
| Chaca | Velocidad del<br>viento (m/s) | 4,53 | -2,39 | <+-/0,5 | 0,70 | >0,60 |

<!-- Estadísticas: 2 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: JIA, 2022. De las tablas anterior, es posible desprender que los estadígrafos se encuentran sobre el rango de bondad de ajuste para la dirección y velocidad del viento, por lo cual se considera -->
<!-- FIN TABLA 8 -->

La Portada ................................................................................................................... 12

TABLA 9: Puntos de máxima concentración y depositación (PMI) - Fase de

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **6.1.1.** **PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC)** En la Tabla a continuación se presentan las coordenadas y aportes de los puntos de máxima concentración modelada, para cada parámetro y estadístico de la Fase de Construcción. -->

**Tabla 9: Puntos de máxima concentración y depositación (PMI) - Fase de Construcción**

| Parámetro | Tipo de<br>Norma | ID | Estadístico | PMC<br>[μg/m3] | Coordenadas UTM<br>WGS84 Huso 19S | Col7 | Coordenadas<br>LCC<br>NWS-84<br>(NWS 6.370<br>km) | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Tipo de**<br>**Norma** | **ID** | **Estadístico** | **PMC**<br>**[μg/m3]** | **Este**<br>**[m]** | **Norte**<br>**[m]** | **X **<br>**[km]** | **Y **<br>**[km]** |
| MP10 | Primaria | PMI 1 | 24h P98 | 11,90 | 381.540 | 7.911.239 | -0,50 | -0,50 |
| MP10 | Primaria | PMI 1 | Anual | 2,79 | 381.540 | 7.911.239 | -0,50 | -0,50 |
| MP2,5 | Primaria | PMI 1 | 24h P98 | 1,66 | 381.540 | 7.911.239 | -0,50 | -0,50 |
| MP2,5 | Primaria | PMI 1 | Anual | 0,45 | 381.540 | 7.911.239 | -0,50 | -0,50 |
| MPS (*) | Secundaria | PMI 1 | Anual | 13,37 | 381.540 | 7.911.239 | -0,50 | -0,50 |
| SO2 | Primaria | PMI 1 | 1h P98,5 | 0,35 | 381.540 | 7.911.239 | -0,50 | -0,50 |
| SO2 | Primaria | PMI 2 | 24h P99 | 0,09 | 380.536 | 7.911.246 | -1,50 | -0,50 |
| SO2 | Secundaria | PMI 3 | 1h P99,73 | 0,92 | 378.515 | 7.912.211 | -3,50 | 0,50 |
| SO2 | Secundaria | PMI 3 | 24h P99,7 | 0,10 | 378.515 | 7.912.211 | -3,50 | 0,50 |
| SO2 | Primaria/<br>Secundaria | PMI 1 | Anual | 0,05 | 381.540 | 7.911.239 | -0,50 | -0,50 |
| NO2 | Primaria | PMI 4 | 1h P99 | 14,30 | 381.527 | 7.912.237 | -0,50 | 0,50 |
| NO2 | Primaria | PMI 4 | Anual | 0,28 | 381.527 | 7.912.237 | -0,50 | 0,50 |
| CO (**) | Primaria | PMI 4 | 1h P99 | 0,11 | 381.527 | 7.912.237 | -0,50 | 0,50 |
| CO (**) | Primaria | PMI 4 | 8h P99 | 0,01 | 381.527 | 7.912.237 | -0,50 | 0,50 |

<!-- Estadísticas: 15 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Nota (*): Punto de máxima depositación de MPS en mg/m [2] -día; Nota (**): Puntos de máxima concentración de CO en μg/m [3] ; -->
<!-- FIN TABLA 9 -->

Construcción .............................................................................................................. 13

TABLA 10: Aportes del Proyecto .............................................................................................. 14

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **6.2.1.** **FASE DE CONSTRUCCIÓN** A continuación, se presentan los resultados modelados en los receptores de interés descritos anteriormente. -->

**Tabla 10: Aportes del Proyecto**

| Parámetro | Receptor | Tipo de<br>Norma | Estadístico | Línea de<br>Base<br>Proyectada<br>[μg/m3] | Aporte sin<br>FC<br>[μg/m3] | Aporte<br>con FC<br>[μg/m3] |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | R1 | Primaria | 24h P98 | - | 0,06 | 0,07 |
| MP10 | R1 | Primaria | Anual | - | 0,02 | 0,02 |
| MP10 | R2 | R2 | 24h P98 | - | 0,06 | 0,06 |
| MP10 | R2 | R2 | Anual | - | 0,01 | 0,02 |
| MP10 | R3 | R3 | 24h P98 | - | 0,05 | 0,05 |
| MP10 | R3 | R3 | Anual | - | 0,01 | 0,01 |
| MP10 | R4 | R4 | 24h P98 | - | 0,05 | 0,05 |
| MP10 | R4 | R4 | Anual | - | 0,01 | 0,01 |
| MP10 | R5 | R5 | 24h P98 | - | 0,04 | 0,04 |
| MP10 | R5 | R5 | Anual | - | 0,01 | 0,01 |
| MP10 | R6 | R6 | 24h P98 | - | 0,04 | 0,04 |
| MP10 | R6 | R6 | Anual | - | 0,01 | 0,01 |
| MP2,5 | R1 | Primaria | 24h P98 | - | 0,01 | 0,01 |
| MP2,5 | R1 | Primaria | Anual | - | 0,00 | 0,00 |
| MP2,5 | R2 | R2 | 24h P98 | - | 0,01 | 0,01 |
| MP2,5 | R2 | R2 | Anual | - | 0,00 | 0,00 |
| MP2,5 | R3 | R3 | 24h P98 | - | 0,01 | 0,01 |
| MP2,5 | R3 | R3 | Anual | - | 0,00 | 0,00 |
| MP2,5 | R4 | R4 | 24h P98 | - | 0,01 | 0,01 |
| MP2,5 | R4 | R4 | Anual | - | 0,00 | 0,00 |
| MP2,5 | R5 | R5 | 24h P98 | - | 0,01 | 0,01 |
| MP2,5 | R5 | R5 | Anual | - | 0,00 | 0,00 |

<!-- Estadísticas: 22 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- 14 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE |Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Línea de<br>Base<br>Proyectada<br>[μg/m3]|Aporte sin<br>FC<br>[μg/m3]|Aporte<br>con FC<br>[μg/m3]| -->
<!-- FIN TABLA 10 -->


TABLA 11: Calidad del aire futura para MP - Fase de Construcción .......................... 19

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- observa a continuación, en las siguientes tablas. 18 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE -->

**Tabla 11: Calidad del aire futura para MP - Fase de Construcción**

| Parámetro | Receptor | Tipo de<br>Norma | Estadístico | Aporte (AP)<br>[μg/m3] | Norma<br>[μg/m3] | % AP c/r<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | R1 | Primaria | 24h P98 | 0 | 150 | 0 |
| MP10 | R1 | Primaria | Anual | 0 | 50 | 0 |
| MP10 | R2 | R2 | 24h P98 | 0 | 150 | 0 |
| MP10 | R2 | R2 | Anual | 0 | 50 | 0 |
| MP10 | R3 | R3 | 24h P98 | 0 | 150 | 0 |
| MP10 | R3 | R3 | Anual | 0 | 50 | 0 |
| MP10 | R4 | R4 | 24h P98 | 0 | 150 | 0 |
| MP10 | R4 | R4 | Anual | 0 | 50 | 0 |
| MP10 | R5 | R5 | 24h P98 | 0 | 150 | 0 |
| MP10 | R5 | R5 | Anual | 0 | 50 | 0 |
| MP10 | R6 | R6 | 24h P98 | 0 | 150 | 0 |
| MP10 | R6 | R6 | Anual | 0 | 50 | 0 |
| MP2,5 | R1 | Primaria | 24h P98 | 0 | 50 | 0 |
| MP2,5 | R1 | Primaria | Anual | 0 | 20 | 0 |
| MP2,5 | R2 | R2 | 24h P98 | 0 | 50 | 0 |
| MP2,5 | R2 | R2 | Anual | 0 | 20 | 0 |
| MP2,5 | R3 | R3 | 24h P98 | 0 | 50 | 0 |
| MP2,5 | R3 | R3 | Anual | 0 | 20 | 0 |
| MP2,5 | R4 | R4 | 24h P98 | 0 | 50 | 0 |
| MP2,5 | R4 | R4 | Anual | 0 | 20 | 0 |
| MP2,5 | R5 | R5 | 24h P98 | 0 | 50 | 0 |
| MP2,5 | R5 | R5 | Anual | 0 | 20 | 0 |
| MP2,5 | R6 | R6 | 24h P98 | 0 | 50 | 0 |
| MP2,5 | R6 | R6 | Anual | 0 | 20 | 0 |
| MPS (*) | R1 | Secundaria | Anual | 0 | 200 | 0 |
| MPS (*) | R2 | R2 | Anual | 0 | 200 | 0 |
| MPS (*) | R3 | R3 | Anual | 0 | 200 | 0 |
| MPS (*) | R4 | R4 | Anual | 0 | 200 | 0 |
| MPS (*) | R5 | R5 | Anual | 0 | 200 | 0 |
| MPS (*) | R6 | R6 | Anual | 0 | 200 | 0 |
| MPS (*) | R7 | R7 | Anual | 0 | 200 | 0 |
| MPS (*) | R8 | R8 | Anual | 0 | 200 | 0 |
| MPS (*) | R9 | R9 | Anual | 0 | 200 | 0 |

<!-- Estadísticas: 33 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Nota (*): Unidades en mg/m [2] -día. Fuente: JIA, 2022. -->
<!-- FIN TABLA 11 -->


TABLA 12: Calidad del aire futura para Gases - Fase de Construcción ..................... 20

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente: JIA, 2022. 19 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE -->

**Tabla 12: Calidad del aire futura para Gases - Fase de Construcción**

| Parámetro | Receptor | Tipo de<br>Norma | Estadístico | Aporte (AP)<br>[μg/m3] | Norma<br>[μg/m3] | % AP c/r<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | R1 | Primaria | 1h P98,5 | 0 | 350 | 0 |
| SO2 | R1 | Primaria | 24h P99 | 0 | 150 | 0 |
| SO2 | R1 | Primaria | Anual | 0 | 60 | 0 |
| SO2 | R2 | R2 | 1h P98,5 | 0 | 350 | 0 |
| SO2 | R2 | R2 | 24h P99 | 0 | 150 | 0 |
| SO2 | R2 | R2 | Anual | 0 | 60 | 0 |
| SO2 | R3 | R3 | 1h P98,5 | 0 | 350 | 0 |
| SO2 | R3 | R3 | 24h P99 | 0 | 150 | 0 |
| SO2 | R3 | R3 | Anual | 0 | 60 | 0 |
| SO2 | R4 | R4 | 1h P98,5 | 0 | 350 | 0 |
| SO2 | R4 | R4 | 24h P99 | 0 | 150 | 0 |
| SO2 | R4 | R4 | Anual | 0 | 60 | 0 |
| SO2 | R5 | R5 | 1h P98,5 | 0 | 350 | 0 |
| SO2 | R5 | R5 | 24h P99 | 0 | 150 | 0 |
| SO2 | R5 | R5 | Anual | 0 | 60 | 0 |
| SO2 | R6 | R6 | 1h P98,5 | 0 | 350 | 0 |
| SO2 | R6 | R6 | 24h P99 | 0 | 150 | 0 |
| SO2 | R6 | R6 | Anual | 0 | 60 | 0 |
| SO2 | R1 | Secundaria | 1h P99,73 | 0 | 1.000 | 0 |
| SO2 | R1 | Secundaria | 24h P99,7 | 0 | 365 | 0 |
| SO2 | R1 | Secundaria | Anual | 0 | 80 | 0 |
| SO2 | R2 | R2 | 1h P99,73 | 0 | 1.000 | 0 |
| SO2 | R2 | R2 | 24h P99,7 | 0 | 365 | 0 |
| SO2 | R2 | R2 | Anual | 0 | 80 | 0 |
| SO2 | R3 | R3 | 1h P99,73 | 0 | 1.000 | 0 |
| SO2 | R3 | R3 | 24h P99,7 | 0 | 365 | 0 |
| SO2 | R3 | R3 | Anual | 0 | 80 | 0 |
| SO2 | R4 | R4 | 1h P99,73 | 0 | 1.000 | 0 |
| SO2 | R4 | R4 | 24h P99,7 | 0 | 365 | 0 |
| SO2 | R4 | R4 | Anual | 0 | 80 | 0 |
| SO2 | R5 | R5 | 1h P99,73 | 0 | 1.000 | 0 |
| SO2 | R5 | R5 | 24h P99,7 | 0 | 365 | 0 |
| SO2 | R5 | R5 | Anual | 0 | 80 | 0 |
| SO2 | R6 | R6 | 1h P99,73 | 0 | 1.000 | 0 |
| SO2 | R6 | R6 | 24h P99,7 | 0 | 365 | 0 |
| SO2 | R6 | R6 | Anual | 0 | 80 | 0 |
| SO2 | R7 | R7 | 1h P99,73 | 0 | 1.000 | 0 |
| SO2 | R7 | R7 | 24h P99,7 | 0 | 365 | 0 |

<!-- Estadísticas: 38 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- 20 ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE |Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Aporte (AP)<br>[μg/m3]|Norma<br>[μg/m3]|% AP c/r<br>Norma| -->
<!-- FIN TABLA 12 -->


**FIGURAS**

FIGURA-1: Ubicación de dominios de modelación y receptores discretos ................ 6

FIGURA-2: Dominio de Modelación (Computacional Grid), fuentes emisoras y
receptores discretos. Fase de Construcción ................................................... 11

FIGURA-3: Frecuencia relativa de la dirección del viento observada y modelada
(WRF). Estación Chaca ............................................................................................ 12

ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**1.** **INTRODUCCIÓN**

En la presente sección se entrega la caracterización de las condiciones meteorológicas en el
área de estudio asociada al sector donde se emplazarán las obras del Proyecto
**“Modificación Planta Solar Fotovoltaica Pampa Camarones”** (en adelante, el Proyecto),
ubicado entre las comunas de Arica y Camarones, específicamente a unos 50 kilómetros al
sureste de la ciudad de Arica, fuera del límite urbano de la misma.

La simulación de los aportes del Proyecto a las concentraciones ambientales se realiza
mediante la aplicación del sistema de modelación WRF/CALPUFF; sistema que considera la
utilización de la modelación meteorológica para el año 2020 (WRF), un dominio
computacional de modelación de CALPUFF de 50x50 [km], con una resolución de 1x1 [km].

A continuación, se presenta el análisis de la dispersión y transporte de las emisiones
correspondientes a la fase de construcción del Proyecto, que considera principalmente las
actividades de movimiento de tierra, tránsito de vehículos por caminos pavimentados y no
pavimentados, combustión de grupos electrógenos, entre otros, descritos en el Anexo C1-5
de la DIA, para el peor escenario de emisiones (Construcción de la Fase 1 del Proyecto).

En concordancia a lo señalado en la Guía para el uso de modelos de calidad del aire en el
SEIA (emitida por el Servicio de Evaluación Ambiental el año 2012), los resultados de la
modelación se entregan en tablas adecuadas, a modo de comparar los aportes del Proyecto
con y sin factor de corrección. Además, se comparan los resultados de la modelación
respecto de la línea de base proyectada (que corresponde a los valores medidos más la suma
de aportes de otros proyectos señalados en evaluaciones ambientales) y, a su vez, respecto
de las normas de calidad del aire nacionales (artículo 11 del D.S. N° 40/12 que aprueba el
Reglamento del Sistema de Evaluación de Impacto Ambiental -RSEIA-), de manera de
evaluar el grado de cumplimiento normativo.

Finalmente, es relevante indicar que los archivos digitales de la modelación con el modelo
CALPUFF (entradas y salidas) se presentan de manera digital en el Apéndice 1 de este
documento.

**2.** **OBJETIVO**

Determinar el aporte incremental a las concentraciones ambientales de material particulado
que generará el Proyecto en los receptores sensibles identificados, y comparar dichos
aportes con respecto a las normas de calidad primaria.

1
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**3.** **MARCO LEGAL**

Para determinar la existencia de los efectos, características o circunstancias de los literales
a), b) y d) del artículo 11 de la Ley 19.300 en el área de influencia del Proyecto en su fase de
construcción en el “peor escenario”, se ha considerado la normativa ambiental primaria y
secundaria de calidad de aire vigente para MP 10, MP 2,5, MPS, NO 2, SO 2 y CO, presentadas en
las tablas a continuación:

TABLA 1: Norma Primaria de Calidad del Aire

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|MP10|D.S. N°59/98<br>MINSEGPRES,<br>modificada por<br>D.S. N°45/01|Promedio aritmético de tres años calendario<br>consecutivos|50 μg/m3N|
|MP10|D.S. N°59/98<br>MINSEGPRES,<br>modificada por<br>D.S. N°45/01|Percentil 98 de las concentraciones de 24 horas<br>registradas durante un período anual|150 μg/ m3N|
|MP2,5|D.S. N°12/11<br>del MMA|Promedio trianual de las concentraciones anuales|20 μg/m3|
|MP2,5|D.S. N°12/11<br>del MMA|Percentil 98 de los promedios diarios registrados<br>durante un año|50 μg/m3|
|NO2|D.S. N°<br>114/2002 del<br>MINSEGPRES|Promedio<br>aritmético<br>de<br>los<br>valores<br>de<br>concentración anual de tres años calendarios<br>sucesivos|100 μg/m3N|
|NO2|D.S. N°<br>114/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario|400 μg/m3N|
|SO2|D.S.<br>N°<br>104/2019<br>del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 99 de las<br>concentraciones de 24 horas registradas cada año|150 μg/m3N|
|SO2|D.S.<br>N°<br>104/2019<br>del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores de concentración anual|60 μg/m3N|
|SO2|D.S.<br>N°<br>104/2019<br>del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 98,5 de las<br>concentraciones de 1 hora registradas cada año|350 μg/m3N|
|CO|D.S. N°<br>115/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario|30 mg/m3N|
|CO|D.S. N°<br>115/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 8 horas (promedio móvil)<br>registrados durante un año calendario|10 mg/m3N|

Fuente: SINCA, 2022.

2
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

Para el caso de la normativa de calidad secundaria, se ha considerado la norma suiza como
referencia para el análisis de MPS.

TABLA 2: Norma Secundaria de Calidad del Aire

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|SO2|D.S. N°22/09 del<br>MINSEGPRES|Promedio<br>aritmético<br>de<br>tres<br>años<br>calendario sucesivos de los valores del<br>percentil 99,73 de las concentraciones de 1<br>hora registradas cada año|1.000 μg/m3N|
|SO2|D.S. N°22/09 del<br>MINSEGPRES|Promedio<br>aritmético<br>de<br>tres<br>años<br>calendario sucesivos de los valores del<br>percentil 99,7 de las concentraciones de 24<br>horas registradas cada año|365 μg/m3N|
|SO2|D.S. N°22/09 del<br>MINSEGPRES|Promedio<br>aritmético<br>de<br>tres<br>años<br>calendario sucesivos de los valores de<br>concentración anual|80 μg/m3N|
|MPS|Ordinance on Air<br>Pollution Control<br>(OAPC) -<br>Confederación Suiza|Promedio anual (media aritmética).|200<br>mg/m2/día|

Fuente: SINCA, 2022.

3
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**4.** **METODOLOGIA**

La modelación se realizó acorde con la metodología descrita en la Guía para el uso de
modelos de calidad del aire en el SEIA (2012), en adelante la “Guía de modelación”. Se utilizó
el modelo numérico Weather Research and Forecasting (WRF) en la generación de datos
meteorológicos para el año 2020, y el modelo CALPUFF para la modelación de la dispersión
y transporte de las emisiones, en el escenario considerado.

**4.1.** **BASE TEÓRICA DEL MODELO UTILIZADO**

WRF es el modelo meteorológico recomendado en la Guía de modelación para la generación
de la grilla meteorológica. Este modelo genera una grilla tridimensional de campos de
viento, además de múltiples variables atmosféricas, a través de dominios anidados con una
resolución horizontal recomendada por la Guía de modelación para el dominio de menor
tamaño, de 1 kilómetro.

Por su parte, CALPUFF es un modelo de dispersión, transporte y deposición de
contaminantes atmosféricos de tipo puff lagrangiano-gaussiano, no estacionario,
recomendado por la Guía de modelación y también por la Agencia de Protección Ambiental
de Estados Unidos (US EPA su sigla en inglés) [1], el cual es aplicable a terrenos complejos y a
múltiples tipos de fuentes emisoras (puntuales, areales y volumétricas). CALPUFF realiza sus
cálculos tomando los datos meteorológicos superficiales y de la capa superior atmosférica,
incluyendo la posibilidad de modelar la dispersión de contaminantes primarios y
secundarios, obteniendo resultados confiables para distancias de hasta 100 [km].

El sistema de modelación incluye tres componentes principales: CALMET, CALPUFF y
CALPOST, además de una serie de programas de preprocesamiento diseñados para la
preparación de la información meteorológica y geofísica, En este caso, no se utilizaron los
preprocesadores ni el módulo CALMET, ya que se emplearon directamente los resultados de
la modelación meteorológica realizada con WRF, en base a los lineamientos de la
mencionada Guía.

CALPOST es un programa postprocesador que permite compilar los resultados de CALPUFF
creando los archivos según los estadísticos establecidos en las normas de calidad del aire
para la evaluación de los resultados.

1 40 CFR Part 51, Revision to the Guideline on Air Quality Models: Adoption of a Preferred General Purpose (Flat
and Complex Terrain) Dispersion Model and Other Revisions; Final Rule.
[http://www.epa.gov/ttn/scram/guidance/guide/appw_05.pdf](http://www.epa.gov/ttn/scram/guidance/guide/appw_05.pdf)

4
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**4.2.** **CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN**

Para que los procesos meteorológicos de mesoescala sean representados de una forma
adecuada, tanto por el modelo meteorológico como por el modelo de dispersión, se generó
un dominio de modelación de WRF/CALPUFF, en donde se consideraron las características
topográficas de la zona.

Se ha considerado la construcción de un escenario de modelación, donde se incorporaron
receptores sensibles a lo largo de la localidad de Chaca, cuyo criterio de ubicación
corresponde a receptores cada 1,10 km a lo largo de la localidad. Por otro lado, se
incorporaron receptores secundarios, aguas arriba de la Quebrada de Vítor (o también
conocida como Quebrada de Chaca), cuya ubicación se presenta a continuación, en la
siguiente tabla.

TABLA 3: Ubicación Receptores primarios y secundarios

|ID|Nombre|Tipo de receptor|Coordenadas UTM WGS84 Huso 19S|Col5|
|---|---|---|---|---|
|**ID**|**Nombre**|**Tipo de receptor**|**Este [m]**|**Norte [m]**|
|R_1|R1|Primario/Secundario|381.629|7.917.047|
|R_2|R2|Primario/Secundario|380.763|7.917.805|
|R_3|R3|Primario/Secundario|379.936|7.918.538|
|R_4|R4|Primario/Secundario|379.129|7.919.233|
|R_5|R5|Primario/Secundario|378.363|7.919.974|
|R_6|R6|Primario/Secundario|377.217|7.920.529|
|R_7|R7|Secundario|387.833|7.913.381|
|R_8|R8|Secundario|385.394|7.914.735|
|R_9|R9|Secundario|383.092|7.916.652|

Fuente: JIA, 2022.

Para una mejor comprensión, en la siguiente figura se presenta la ubicación geográfica del
dominio de modelación y los receptores discretos.

5
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

FIGURA-1: Ubicación de dominios de modelación y receptores discretos

Fuente: JIA, 2021.

Cabe señalar que la modelación meteorológica WRF fue realizada para el año 2020, de
acuerdo con la configuración definida por el SEA en su Guía de modelación: cuenta con una
resolución horizontal de 1 [km] y una resolución vertical de 10 niveles a 20, 40, 80, 160, 320,
640, 1.200, 2.000, 3.000 y 4.000 metros. En la tabla a continuación se señalan las coordenadas
de los vértices del dominio de modelación WRF/CALPUFF.

TABLA 4: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF

|Vértices|Coordenadas UTM [m] Datum: WGS-84, Huso: 19S|Col3|
|---|---|---|
|**Vértices**|**Este**|**Norte**|
|**SW**|357.166,85|7.886.678,31|
|**NE**|406.859,13|7.936.632,36|

6
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

|Vértices|Coordenadas UTM [m] Datum: WGS-84, Huso: 19S|Col3|
|---|---|---|
|**Vértices**|**Este**|**Norte**|
|**NW**|356.809,78|7.936.388,77|
|**SE**|407.187,64|7.886.897,13|

Fuente: JIA, 2022.

**4.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF Y**
**FACTOR DE CORRECIÓN**

La modelación atmosférica está basada en uno de los modelos de pronóstico meteorológico
más avanzados y completos disponibles [2], el cual cuenta con un gran número de
parametrizaciones que permiten, si son adecuadamente seleccionadas e implementadas,
simular gran parte de los procesos meteorológicos de mesoescala. Este modelo
corresponde, como ya se ha mencionado, al Weather Research and Forecasting (WRF). En el
caso del presente estudio, el modelo WRF utilizado ha sido parametrizado de acuerdo con
lo establecido por el SEA y corresponde al año 2020.

Sin embargo, e independiente de las bondades del sistema utilizado, todo modelo
atmosférico requiere ser validado para cada condición meteorológica y de terreno. En este
punto es donde se tienen las mayores dificultades, dado que la incorrecta implementación
de alguna parametrización puede llevar a errores significativos en la estimación de los
vientos en superficie y, consecuentemente, de las trayectorias de los contaminantes.

Por ello, para realizar el análisis de incertidumbre se han considerado las recomendaciones
establecidas en la Guía de modelación descritas en el acápite 7, donde menciona que
cualquier modelo representa una aproximación a la realidad y sus resultados tienen
incertidumbres asociadas, las cuales se expresan a través de diferencias entre lo estimado y
lo observado.

Cabe señalar que, a partir de las estaciones meteorológicas analizadas en el capítulo se
evaluaron los estadígrafos meteorológicos recomendados por la USEPA, que corresponden
al BIAS (sesgo) y al IOA (índice de ajustes), además de error cuadrático medio (RMSE) para
la velocidad [m/s] y la dirección del viento [°] entre los valores de la estación modelada a
partir del modelo meteorológico WRF utilizado y las observaciones de terreno disponibles
para el área a modelar.

Luego del ajuste en las direcciones de viento, se calcula la frecuencia relativa del viento para
cada una de las direcciones seleccionadas respecto de la frecuencia total de las estas, tanto
para los datos observados como para los datos modelados. Por lo tanto, si se denomina _Xi_
a las frecuencias observadas de cada una de las direcciones de viento (i) y _Wi_ a las frecuencias

2 Numeral 5.3.2 Fuentes de Datos Meteorológicas. Guía para el uso de modelos de calidad del aire. SEA 2012.

7
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

modeladas, entonces las frecuencias relativas observadas ( F obs ) corresponderán a las
calculadas de acuerdo con la ecuación 1:

F obs =

∑ 3i=1 X i X i Ecuación 1

Asimismo, las frecuencias relativas modeladas ( F WRF ), corresponderán a las calculadas de
acuerdo con la ecuación 2:

F WRF =

∑ 3i=1 W i W i Ecuación 2

De esta manera, al restar ambas frecuencias relativas obtenemos información respecto al
grado de subestimación o sobrestimación de las direcciones de viento que pueden favorecer
el transporte de los parámetros atmosféricos a modelar. En el caso de que la diferencia entre
lo observado y lo modelado sea mayor que cero, significaría que el modelo subestimó la
dirección que favorece el transporte de contaminantes. En dicho caso, se aplicó un factor de
corrección dado por la ecuación 3:

FC= 1 + [F obs −F WRF ] Ecuación 3

**5.** **PARÁMETROS DE ENTRADA DEL MODELO**

A continuación, se detallan los principales parámetros de entrada del modelo de calidad del
aire, los que corresponden a: características topográficas, uso del suelo, fuentes emisoras
externas (aportes de terceros) y escenario de modelación (emisiones asociadas a las
instalaciones donde se emplaza el Proyecto).

**5.1.** **CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO**

Las características topográficas y de uso de suelo, son parámetros asociados a la elevación
de terreno, los coeficientes de rugosidad, razón de bowen, entre otros, que son parte
integrante de los datos que incluye el archivo de modelación WRF, por lo cual no se requiere
su caracterización.

**5.2.** **PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN**

En los siguientes acápites se presentan las tasas de emisión ingresadas a la modelación de
calidad del aire. Como escenario de evaluación, se consideró el peor escenario,
correspondiente a la Fase 1, debido a que las emisiones son mayores que las descritas en la
Fase 2. Por otro lado, si bien, el cronograma habla de 14 meses para la Fase 1, y la
modelación se realiza en base anual, se ha considerado una peor condición, incorporando
la totalidad de emisiones a generarse, en un año calendario (peor escenario, dado que
incrementan las tasas de emisión).

8
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA 5: Tasas de emisión, fuentes de área

|Fuente|Tasa de emisión [kg/m2-h]|Col3|Col4|Col5|Col6|Col7|Área<br>[m2]|Tiempo<br>[h]|
|---|---|---|---|---|---|---|---|---|
|**Fuente**|**MP30 **|**MP10 **|**MP2,5 **|**CO**|**NOX (*)**|**SO2 **|**SO2 **|**SO2 **|
|Línea de<br>transmisión|3,22 E-<br>06|1,94 E-<br>06|1,74 E-<br>06|1,16 E-<br>05|1,87 E-<br>05|3,65 E-<br>07|130.132,0|4.380|
|Obras Fase I|3,43 E-<br>07|1,92 E-<br>07|1,69 E-<br>07|1,25 E-<br>06|1,69 E-<br>06|1,00 E-<br>08|3.321.103<br>,2|4.380|

Nota (*): Se ha considerado una proporción de NO/NO 2 respecto de los niveles de

emisión de NO X, asumiendo que el 90% generado es NO y el restante 10%

corresponde a NO 2 ;

Fuente: JIA, 2022.

TABLA 6: Tasas de emisión, fuentes de camino

|Fuente|Tasa de emisión [kg/m-h]|Col3|Col4|Col5|Col6|Col7|Largo<br>[m]|Tiempo<br>[h]|
|---|---|---|---|---|---|---|---|---|
|**Fuente**|**MP30 **|**MP10 **|**MP2,5 **|**CO**|**NOX (*)**|**SO2 **|**SO2 **|**SO2 **|
|Ruta Pavimentada 1|1,51 E-<br>05|2,97 E-<br>06|7,87 E-<br>07|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|41.555,7|4.380|
|Ruta NO<br>Pavimentada 1|2,00 E-<br>03|5,73 E-<br>04|5,74 E-<br>05|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|10.957,9|4.380|
|Ruta NO<br>Pavimentada 2|1,82 E-<br>03|5,20 E-<br>04|5,20 E-<br>05|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|762,9|4.380|
|Ruta NO<br>Pavimentada 3|1,51 E-<br>03|4,32 E-<br>04|4,32 E-<br>05|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|968,3|4.380|
|Ruta NO<br>Pavimentada 4|1,51 E-<br>03|4,30 E-<br>04|4,31 E-<br>05|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|1.008,5|4.380|
|Ruta NO<br>Pavimentada 5|1,26 E-<br>03|3,59 E-<br>04|3,60 E-<br>05|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|3.526,6|4.380|
|Ruta NO<br>Pavimentada 6|5,97 E-<br>05|1,71 E-<br>05|1,79 E-<br>06|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|1.329,5|4.380|
|Ruta NO<br>Pavimentada 7|5,94 E-<br>05|1,70 E-<br>05|1,79 E-<br>06|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|4.328,5|4.380|
|Ruta NO<br>Pavimentada 8|6,01 E-<br>05|1,72 E-<br>05|1,81 E-<br>06|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|496,4|4.380|
|Ruta NO<br>Pavimentada 9|5,89 E-<br>05|1,69 E-<br>05|1,77 E-<br>06|4,07 E-<br>07|8,22 E-<br>06|2,35 E-<br>08|334,2|4.380|
|Ruta NO<br>Pavimentada 10|0,00<br>E+00|0,00<br>E+00|0,00<br>E+00|0,00<br>E+00|0,00<br>E+00|0,00<br>E+00|2.628,5|4.380|

Nota (*): Se ha considerado una proporción de NO/NO 2 respecto de los niveles de

emisión de NO X, asumiendo que el 90% generado es NO y el restante 10%

corresponde a NO 2 ;

Fuente: JIA, 2022.

9
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA 7: Tasas de emisión, fuentes puntuales

|Fuente|Tasa de emisión [kg/h]|Col3|Col4|Col5|Col6|Col7|Altura<br>de<br>Chime<br>nea<br>[m]|Temper<br>atura de<br>salida<br>[K]|Diám<br>etro<br>intern<br>o [m]|Veloci<br>dad<br>de<br>salida<br>de<br>gases<br>[m/s]|Tiemp<br>o [h]|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**MP30 **|**MP10**|**MP2,5 **|**CO**|**NOX **<br>**(*)**|**SO2 **|**SO2 **|**SO2 **|**SO2 **|**SO2 **|**SO2 **|
|Grupo<br>Electrógeno<br>Fijo|9,34<br>E-02|9,34<br>E-02|9,34<br>E-02|2,86<br>E-01|1,33<br>E+00|8,74<br>E-02|1,76|770,00|0,10|26,21|4.380|

Nota (*): Se ha considerado una proporción de NO/NO 2 respecto de los niveles de

emisión de NO X, asumiendo que el 90% generado es NO y el restante 10%

corresponde a NO 2 ;

Fuente: JIA, 2022.

10
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

A continuación, en la siguiente Figura se presenta la ubicación del dominio de modelación,
fuentes emisoras y receptores para la fase de construcción:

FIGURA-2: Dominio de Modelación (Computacional Grid), fuentes emisoras y receptores

discretos. Fase de Construcción

Fuente: elaboración propia.

11
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**5.3.** **ANALISIS DE INCERTIDUMBRE Y DETERMINACIÓN DEL FACTOR DE**
**CORRECCIÓN**

Para realizar el análisis de incertidumbre, se consideró la información disponible en el portal
de Agrometeorología del INIA, específico, para la estación Chaca para el año 2020, que
corresponde al período de valores obtenidos mediante el modelo WRF. A partir de ambos
conjuntos de datos, se realizó un breve análisis estadístico, según lo descrito en el inciso 4.3.
Los resultados obtenidos son presentados en la tabla a continuación:

TABLA 8: Estadígrafos de ajuste de la modelación meteorológica, Estación Altos La Portada

|Estación|Variable|RMSE|BIAS|Bondad<br>BIAS|IOA|Bondad<br>IOA|
|---|---|---|---|---|---|---|
|Chaca|Dirección del<br>viento (°)|133,72|55,98|<+-/10|0,65|--|
|Chaca|Velocidad del<br>viento (m/s)|4,53|-2,39|<+-/0,5|0,70|>0,60|

Fuente: JIA, 2022.

De las tablas anterior, es posible desprender que los estadígrafos se encuentran sobre el
rango de bondad de ajuste para la dirección y velocidad del viento, por lo cual se considera
la aplicación de un factor de corrección.

De acuerdo con la metodología descrita en el numeral 4.3, se graficaron las frecuencias
relativas de las direcciones del viento que favorecen el transporte de los parámetros
atmosféricos a modelar, a modo de determinar los parámetros F WRF y F obs . El gráfico de las
frecuencias relativas señaladas se realizó tanto de los datos registrados en la estación de
monitoreo, como los datos modelados con WRF, lo cual se muestra a continuación:

FIGURA-3: Frecuencia relativa de la dirección del viento observada y modelada (WRF).

Estación Chaca

|Col1|N|NN<br>E|NE|ENE|E|ESE|SE|SSE|S|SS<br>W|SW|WS<br>W|W|WN<br>W|NW|NN<br>W|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|OBS|0%|0%|1%|1%|2%|3%|7%|3%|2%|2%|3%|4%|2%|1%|59%|8%|
|MOD|2%|1%|1%|0%|0%|0%|0%|0%|0%|1%|3%|3%|4%|19%|61%|4%|

Fuente: JIA, 2022.

12
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

Como es posible observar en la figura anterior, el modelo meteorológico replica de manera
correcta las direcciones de viento, con algunas desviaciones, por lo que se considera un
factor de corrección de 1,07.

**6.** **RESULTADOS**

A continuación, se presentan los valores de máxima concentración obtenidos mediante el
modelo, para cada contaminante y período analizado. Finalmente, se presentan los aportes
estimados de la Fase de Construcción para cada uno de los parámetros modelados.

**6.1.1.** **PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC)**

En la Tabla a continuación se presentan las coordenadas y aportes de los puntos de máxima
concentración modelada, para cada parámetro y estadístico de la Fase de Construcción.

TABLA 9: Puntos de máxima concentración y depositación (PMI) - Fase de Construcción

|Parámetro|Tipo de<br>Norma|ID|Estadístico|PMC<br>[μg/m3]|Coordenadas UTM<br>WGS84 Huso 19S|Col7|Coordenadas<br>LCC<br>NWS-84<br>(NWS 6.370<br>km)|Col9|
|---|---|---|---|---|---|---|---|---|
|**Parámetro**|**Tipo de**<br>**Norma**|**ID**|**Estadístico**|**PMC**<br>**[μg/m3]**|**Este**<br>**[m]**|**Norte**<br>**[m]**|**X **<br>**[km]**|**Y **<br>**[km]**|
|MP10|Primaria|PMI 1|24h P98|11,90|381.540|7.911.239|-0,50|-0,50|
|MP10|Primaria|PMI 1|Anual|2,79|381.540|7.911.239|-0,50|-0,50|
|MP2,5|Primaria|PMI 1|24h P98|1,66|381.540|7.911.239|-0,50|-0,50|
|MP2,5|Primaria|PMI 1|Anual|0,45|381.540|7.911.239|-0,50|-0,50|
|MPS (*)|Secundaria|PMI 1|Anual|13,37|381.540|7.911.239|-0,50|-0,50|
|SO2|Primaria|PMI 1|1h P98,5|0,35|381.540|7.911.239|-0,50|-0,50|
|SO2|Primaria|PMI 2|24h P99|0,09|380.536|7.911.246|-1,50|-0,50|
|SO2|Secundaria|PMI 3|1h P99,73|0,92|378.515|7.912.211|-3,50|0,50|
|SO2|Secundaria|PMI 3|24h P99,7|0,10|378.515|7.912.211|-3,50|0,50|
|SO2|Primaria/<br>Secundaria|PMI 1|Anual|0,05|381.540|7.911.239|-0,50|-0,50|
|NO2|Primaria|PMI 4|1h P99|14,30|381.527|7.912.237|-0,50|0,50|
|NO2|Primaria|PMI 4|Anual|0,28|381.527|7.912.237|-0,50|0,50|
|CO (**)|Primaria|PMI 4|1h P99|0,11|381.527|7.912.237|-0,50|0,50|
|CO (**)|Primaria|PMI 4|8h P99|0,01|381.527|7.912.237|-0,50|0,50|

Nota (*): Punto de máxima depositación de MPS en mg/m [2] -día;

Nota (**): Puntos de máxima concentración de CO en μg/m [3] ;

Fuente: JIA, 2021.

En el Apéndice 2 se presenta la representación gráfica de cada uno de los puntos de máxima
concentración.

13
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**6.2.** **RESULTADOS DE LA MODELACIÓN**

Los resultados de la modelación para cada uno de los parámetros modelados de acuerdo
con los estadísticos definidos en las normas primarias y secundarias calidad del aire
evaluadas para la Fase de Construcción se presentan a continuación. Los resultados son
presentados con y sin factor de corrección (FC en las tablas siguientes), de acuerdo con lo
detallado en el numeral 4.3 (Análisis de incertidumbre) y lo recomendado en la Guía de
modelación.

**6.2.1.** **FASE DE CONSTRUCCIÓN**

A continuación, se presentan los resultados modelados en los receptores de interés descritos
anteriormente.

TABLA 10: Aportes del Proyecto

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Línea de<br>Base<br>Proyectada<br>[μg/m3]|Aporte sin<br>FC<br>[μg/m3]|Aporte<br>con FC<br>[μg/m3]|
|---|---|---|---|---|---|---|
|MP10|R1|Primaria|24h P98|-|0,06|0,07|
|MP10|R1|Primaria|Anual|-|0,02|0,02|
|MP10|R2|R2|24h P98|-|0,06|0,06|
|MP10|R2|R2|Anual|-|0,01|0,02|
|MP10|R3|R3|24h P98|-|0,05|0,05|
|MP10|R3|R3|Anual|-|0,01|0,01|
|MP10|R4|R4|24h P98|-|0,05|0,05|
|MP10|R4|R4|Anual|-|0,01|0,01|
|MP10|R5|R5|24h P98|-|0,04|0,04|
|MP10|R5|R5|Anual|-|0,01|0,01|
|MP10|R6|R6|24h P98|-|0,04|0,04|
|MP10|R6|R6|Anual|-|0,01|0,01|
|MP2,5|R1|Primaria|24h P98|-|0,01|0,01|
|MP2,5|R1|Primaria|Anual|-|0,00|0,00|
|MP2,5|R2|R2|24h P98|-|0,01|0,01|
|MP2,5|R2|R2|Anual|-|0,00|0,00|
|MP2,5|R3|R3|24h P98|-|0,01|0,01|
|MP2,5|R3|R3|Anual|-|0,00|0,00|
|MP2,5|R4|R4|24h P98|-|0,01|0,01|
|MP2,5|R4|R4|Anual|-|0,00|0,00|
|MP2,5|R5|R5|24h P98|-|0,01|0,01|
|MP2,5|R5|R5|Anual|-|0,00|0,00|

14
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Línea de<br>Base<br>Proyectada<br>[μg/m3]|Aporte sin<br>FC<br>[μg/m3]|Aporte<br>con FC<br>[μg/m3]|
|---|---|---|---|---|---|---|
||R6||24h P98|-|0,01|0,01|
||R6||Anual|-|0,00|0,00|
|MPS (**)|R1|Secundaria|Anual|-|0,03|0,03|
|MPS (**)|R2|R2|Anual|-|0,02|0,02|
|MPS (**)|R3|R3|Anual|-|0,02|0,02|
|MPS (**)|R4|R4|Anual|-|0,02|0,02|
|MPS (**)|R5|R5|Anual|-|0,02|0,02|
|MPS (**)|R6|R6|Anual|-|0,02|0,02|
|MPS (**)|R7|R7|Anual|-|0,06|0,07|
|MPS (**)|R8|R8|Anual|-|0,05|0,05|
|MPS (**)|R9|R9|Anual|-|0,03|0,03|
|SO2|R1|Primaria|1h P98,5|-|0,00|0,00|
|SO2|R1|Primaria|24h P99|-|0,00|0,00|
|SO2|R1|Primaria|Anual|-|0,00|0,00|
|SO2|R2|R2|1h P98,5|-|0,00|0,00|
|SO2|R2|R2|24h P99|-|0,00|0,00|
|SO2|R2|R2|Anual|-|0,00|0,00|
|SO2|R3|R3|1h P98,5|-|0,00|0,00|
|SO2|R3|R3|24h P99|-|0,00|0,00|
|SO2|R3|R3|Anual|-|0,00|0,00|
|SO2|R4|R4|1h P98,5|-|0,00|0,00|
|SO2|R4|R4|24h P99|-|0,00|0,00|
|SO2|R4|R4|Anual|-|0,00|0,00|
|SO2|R5|R5|1h P98,5|-|0,00|0,00|
|SO2|R5|R5|24h P99|-|0,00|0,00|
|SO2|R5|R5|Anual|-|0,00|0,00|
|SO2|R6|R6|1h P98,5|-|0,00|0,00|
|SO2|R6|R6|24h P99|-|0,00|0,00|
|SO2|R6|R6|Anual|-|0,00|0,00|
|SO2|R1|Secundaria|1h P99,73|-|0,01|0,01|
|SO2|R1|Secundaria|24h P99,7|-|0,00|0,00|
|SO2|R1|Secundaria|Anual|-|0,00|0,00|
|SO2|R2|R2|1h P99,73|-|0,00|0,01|
|SO2|R2|R2|24h P99,7|-|0,00|0,00|
|SO2|R2|R2|Anual|-|0,00|0,00|
|SO2|R3|R3|1h P99,73|-|0,00|0,00|

15
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Línea de<br>Base<br>Proyectada<br>[μg/m3]|Aporte sin<br>FC<br>[μg/m3]|Aporte<br>con FC<br>[μg/m3]|
|---|---|---|---|---|---|---|
||||24h P99,7|-|0,00|0,00|
||||Anual|-|0,00|0,00|
||R4|R4|1h P99,73|-|0,00|0,00|
||R4|R4|24h P99,7|-|0,00|0,00|
||R4|R4|Anual|-|0,00|0,00|
||R5|R5|1h P99,73|-|0,00|0,00|
||R5|R5|24h P99,7|-|0,00|0,00|
||R5|R5|Anual|-|0,00|0,00|
||R6|R6|1h P99,73|-|0,00|0,00|
||R6|R6|24h P99,7|-|0,00|0,00|
||R6|R6|Anual|-|0,00|0,00|
||R7|R7|1h P99,73|-|0,00|0,00|
||R7|R7|24h P99,7|-|0,00|0,00|
||R7|R7|Anual|-|0,00|0,00|
||R8|R8|1h P99,73|-|0,01|0,01|
||R8|R8|24h P99,7|-|0,00|0,00|
||R8|R8|Anual|-|0,00|0,00|
||R9|R9|1h P99,73|-|0,01|0,01|
||R9|R9|24h P99,7|-|0,00|0,00|
||R9|R9|Anual|-|0,00|0,00|
|NO2|R1|Primaria|1h P99|-|0,06|0,07|
|NO2|R1|Primaria|Anual|-|0,00|0,00|
|NO2|R2|R2|1h P99|-|0,04|0,05|
|NO2|R2|R2|Anual|-|0,00|0,00|
|NO2|R3|R3|1h P99|-|0,04|0,04|
|NO2|R3|R3|Anual|-|0,00|0,00|
|NO2|R4|R4|1h P99|-|0,05|0,05|
|NO2|R4|R4|Anual|-|0,00|0,00|
|NO2|R5|R5|1h P99|-|0,04|0,04|
|NO2|R5|R5|Anual|-|0,00|0,00|
|NO2|R6|R6|1h P99|-|0,03|0,04|
|NO2|R6|R6|Anual|-|0,00|0,00|
|CO (*)|R1|Primaria|1h P99|-|0,00|0,00|
|CO (*)|R1|Primaria|8h P99|-|0,00|0,00|
|CO (*)|R2|R2|1h P99|-|0,00|0,00|
|CO (*)|R2|R2|8h P99|-|0,00|0,00|

16
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Línea de<br>Base<br>Proyectada<br>[μg/m3]|Aporte sin<br>FC<br>[μg/m3]|Aporte<br>con FC<br>[μg/m3]|
|---|---|---|---|---|---|---|
||R3||1h P99|-|0,00|0,00|
||R3||8h P99|-|0,00|0,00|
||R4|R4|1h P99|-|0,00|0,00|
||R4|R4|8h P99|-|0,00|0,00|
||R5|R5|1h P99|-|0,00|0,00|
||R5|R5|8h P99|-|0,00|0,00|
||R6|R6|1h P99|-|0,00|0,00|
||R6|R6|8h P99|-|0,00|0,00|

Nota (**): Unidades en mg/m [2] -día.

Nota (*): Unidades en mg/m [3] .

Fuente: JIA, 2022.

17
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**7.** **CUMPLIMIENTO DE NORMATIVA**

A continuación, se presentan las tablas de evaluación de cumplimiento normativo para cada
parámetro modelado, en las cuales se comparan los aportes del Proyecto en los receptores
discretos considerados.

Es importante mencionar que se modelaron las peores condiciones de emisiones,
considerando todas las actividades del Proyecto. De acuerdo con los resultados obtenidos,
no se esperan aportes en ninguno de los receptores, para ninguno de los parámetros
modelados, tanto para las normas de calidad primaria, como secundarias, tal como se
observa a continuación, en las siguientes tablas.

18
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA 11: Calidad del aire futura para MP - Fase de Construcción

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Aporte (AP)<br>[μg/m3]|Norma<br>[μg/m3]|% AP c/r<br>Norma|
|---|---|---|---|---|---|---|
|MP10|R1|Primaria|24h P98|0|150|0|
|MP10|R1|Primaria|Anual|0|50|0|
|MP10|R2|R2|24h P98|0|150|0|
|MP10|R2|R2|Anual|0|50|0|
|MP10|R3|R3|24h P98|0|150|0|
|MP10|R3|R3|Anual|0|50|0|
|MP10|R4|R4|24h P98|0|150|0|
|MP10|R4|R4|Anual|0|50|0|
|MP10|R5|R5|24h P98|0|150|0|
|MP10|R5|R5|Anual|0|50|0|
|MP10|R6|R6|24h P98|0|150|0|
|MP10|R6|R6|Anual|0|50|0|
|MP2,5|R1|Primaria|24h P98|0|50|0|
|MP2,5|R1|Primaria|Anual|0|20|0|
|MP2,5|R2|R2|24h P98|0|50|0|
|MP2,5|R2|R2|Anual|0|20|0|
|MP2,5|R3|R3|24h P98|0|50|0|
|MP2,5|R3|R3|Anual|0|20|0|
|MP2,5|R4|R4|24h P98|0|50|0|
|MP2,5|R4|R4|Anual|0|20|0|
|MP2,5|R5|R5|24h P98|0|50|0|
|MP2,5|R5|R5|Anual|0|20|0|
|MP2,5|R6|R6|24h P98|0|50|0|
|MP2,5|R6|R6|Anual|0|20|0|
|MPS (*)|R1|Secundaria|Anual|0|200|0|
|MPS (*)|R2|R2|Anual|0|200|0|
|MPS (*)|R3|R3|Anual|0|200|0|
|MPS (*)|R4|R4|Anual|0|200|0|
|MPS (*)|R5|R5|Anual|0|200|0|
|MPS (*)|R6|R6|Anual|0|200|0|
|MPS (*)|R7|R7|Anual|0|200|0|
|MPS (*)|R8|R8|Anual|0|200|0|
|MPS (*)|R9|R9|Anual|0|200|0|

Nota (*): Unidades en mg/m [2] -día.

Fuente: JIA, 2022.

19
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA 12: Calidad del aire futura para Gases - Fase de Construcción

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Aporte (AP)<br>[μg/m3]|Norma<br>[μg/m3]|% AP c/r<br>Norma|
|---|---|---|---|---|---|---|
|SO2|R1|Primaria|1h P98,5|0|350|0|
|SO2|R1|Primaria|24h P99|0|150|0|
|SO2|R1|Primaria|Anual|0|60|0|
|SO2|R2|R2|1h P98,5|0|350|0|
|SO2|R2|R2|24h P99|0|150|0|
|SO2|R2|R2|Anual|0|60|0|
|SO2|R3|R3|1h P98,5|0|350|0|
|SO2|R3|R3|24h P99|0|150|0|
|SO2|R3|R3|Anual|0|60|0|
|SO2|R4|R4|1h P98,5|0|350|0|
|SO2|R4|R4|24h P99|0|150|0|
|SO2|R4|R4|Anual|0|60|0|
|SO2|R5|R5|1h P98,5|0|350|0|
|SO2|R5|R5|24h P99|0|150|0|
|SO2|R5|R5|Anual|0|60|0|
|SO2|R6|R6|1h P98,5|0|350|0|
|SO2|R6|R6|24h P99|0|150|0|
|SO2|R6|R6|Anual|0|60|0|
|SO2|R1|Secundaria|1h P99,73|0|1.000|0|
|SO2|R1|Secundaria|24h P99,7|0|365|0|
|SO2|R1|Secundaria|Anual|0|80|0|
|SO2|R2|R2|1h P99,73|0|1.000|0|
|SO2|R2|R2|24h P99,7|0|365|0|
|SO2|R2|R2|Anual|0|80|0|
|SO2|R3|R3|1h P99,73|0|1.000|0|
|SO2|R3|R3|24h P99,7|0|365|0|
|SO2|R3|R3|Anual|0|80|0|
|SO2|R4|R4|1h P99,73|0|1.000|0|
|SO2|R4|R4|24h P99,7|0|365|0|
|SO2|R4|R4|Anual|0|80|0|
|SO2|R5|R5|1h P99,73|0|1.000|0|
|SO2|R5|R5|24h P99,7|0|365|0|
|SO2|R5|R5|Anual|0|80|0|
|SO2|R6|R6|1h P99,73|0|1.000|0|
|SO2|R6|R6|24h P99,7|0|365|0|
|SO2|R6|R6|Anual|0|80|0|
|SO2|R7|R7|1h P99,73|0|1.000|0|
|SO2|R7|R7|24h P99,7|0|365|0|

20
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Aporte (AP)<br>[μg/m3]|Norma<br>[μg/m3]|% AP c/r<br>Norma|
|---|---|---|---|---|---|---|
||||Anual|0|80|0|
||R8|R8|1h P99,73|0|1.000|0|
||R8|R8|24h P99,7|0|365|0|
||R8|R8|Anual|0|80|0|
||R9|R9|1h P99,73|0|1.000|0|
||R9|R9|24h P99,7|0|365|0|
||R9|R9|Anual|0|80|0|
|NO2|R1|Primaria|1h P99|0|400|0|
|NO2|R1|Primaria|Anual|0|100|0|
|NO2|R2|R2|1h P99|0|400|0|
|NO2|R2|R2|Anual|0|100|0|
|NO2|R3|R3|1h P99|0|400|0|
|NO2|R3|R3|Anual|0|100|0|
|NO2|R4|R4|1h P99|0|400|0|
|NO2|R4|R4|Anual|0|100|0|
|NO2|R5|R5|1h P99|0|400|0|
|NO2|R5|R5|Anual|0|100|0|
|NO2|R6|R6|1h P99|0|400|0|
|NO2|R6|R6|Anual|0|100|0|
|CO (*)|R1|Primaria|1h P99|0|30|0|
|CO (*)|R1|Primaria|8h P99|0|10|0|
|CO (*)|R2|R2|1h P99|0|30|0|
|CO (*)|R2|R2|8h P99|0|10|0|
|CO (*)|R3|R3|1h P99|0|30|0|
|CO (*)|R3|R3|8h P99|0|10|0|
|CO (*)|R4|R4|1h P99|0|30|0|
|CO (*)|R4|R4|8h P99|0|10|0|
|CO (*)|R5|R5|1h P99|0|30|0|
|CO (*)|R5|R5|8h P99|0|10|0|
|CO (*)|R6|R6|1h P99|0|30|0|
|CO (*)|R6|R6|8h P99|0|10|0|

Nota (*): Unidades en mg/m [3] ;

Fuente: JIA, 2022.

21
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE

**8.** **CONCLUSIONES**

De los resultados obtenidos en la modelación atmosférica de emisiones, correspondientes
a la Fase de Construcción, se concluye que el Proyecto “ **Modificación Planta Solar**
**Fotovoltaica Pampa Camarones** ” no generará un aporte incremental significativo en las
concentraciones ambientales de material particulado en los receptores evaluados con
respecto las normas de calidad primaria y secundaria vigentes.

Respecto a la ubicación de los puntos de máxima concentración de la grilla de receptores,
se observa que se localizan en sectores aledaños los caminos de acceso hacia los frentes de
trabajo y/o cercanas a las obras del Proyecto, donde no existen receptores discretos de
interés, por lo que no han sido considerados dentro del análisis normativo.

Dado lo anterior, se concluye que el Proyecto no produce impactos significativos sobre la
calidad del aire, dado que los aportes del Proyecto no modifican significativamente la
condición de calidad del aire de su entorno. Por ende, no se produce alguno de los efectos,
características o circunstancias de aquellos señalados en el artículo 11 de la Ley N° 19.300.

22
ANEXO CA-1 - MODELACIÓN CALIDAD DEL AIRE