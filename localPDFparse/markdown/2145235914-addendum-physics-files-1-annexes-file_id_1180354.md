---
title: Sin título
author: LEN
date: D:20200320133344-03'00'
language: es
type: report
pages: 47
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA Modelación Calidad del Aire Proyecto “Extracción de Áridos y Planta de Asfaltos Sector Pozo D8” Región de Antofagasta
  - Desglose de emisiones ingresadas al modelo Calpuff
-->

# ADENDA Modelación Calidad del Aire Proyecto “Extracción de Áridos y Planta de Asfaltos Sector Pozo D8” Región de Antofagasta

**Marzo 2020**

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|B||CMZ|||
|A|13-03-2020|CMZ|JOA|RTQ|
|**REV**|**FECHA**|**POR**|**REV.**|**APR.**|
|**REV**|**FECHA**|LEN & Asociados Ingenieros Consultores Ltda.|LEN & Asociados Ingenieros Consultores Ltda.||
|||18-006-DIA-D8-DP-A-01-B|18-006-DIA-D8-DP-A-01-B|Rev. B|

**TABLA DE CONTENIDOS**

**1.** **INTRODUCCIÓN ...................................................................................................................... 6**

**2.** **OBJETIVO ................................................................................................................................ 6**

**3.** **METODOLOGÍA ....................................................................................................................... 6**

**4.** **NORMATIVA AMBIENTAL APLICABLE ................................................................................ 7**

**5.** **CARACTERIZACIÓN CALIDAD DEL AIRE ............................................................................ 7**

**6.** **CARACTERIZACIÓN METEOROLÓGICA .............................................................................. 8**

**6.1.** **Velocidad del viento ............................................................................................................... 9**

**6.2.** **Dirección del viento .............................................................................................................. 11**

**6.3.** **Temperatura .......................................................................................................................... 14**

**7.** **MODELO METEOROLÓGICO ............................................................................................... 16**

**7.1.** **Justificación y descripción del modelo meteorológico .................................................... 16**

**7.2.** **Dominio de modelación ....................................................................................................... 17**

**7.3.** **Evaluación del modelo meteorológico ............................................................................... 18**

7.3.1. Velocidad del viento ................................................................................................................ 20

7.3.2. Dirección del viento ................................................................................................................. 23

7.3.3. Conclusiones análisis de incertidumbre ................................................................................. 28

**8.** **MODELO DE DISPERSIÓN DE EMISIONES ATMOSFÉRICAS .......................................... 28**

**8.1.** **Justificación y descripción del modelo de calidad del aire ............................................. 28**

**8.2.** **Dominio de modelación ....................................................................................................... 29**

**8.3.** **Receptores sensibles ........................................................................................................... 31**

**9.** **FUENTES EMISIORAS CONSIDERADAS EN LA MODELACIÓN ...................................... 33**

**10.** **RESULTADOS ....................................................................................................................... 36**

**10.1.** **Aportes en receptores sensibles para MP10 y MP2.5 ....................................................... 36**

**10.2.** **Aportes en punto de máximo impacto ............................................................................... 37**

**10.3.** **Aportes de proyectos con RCA ........................................................................................... 38**

**10.4.** **Curvas de concentración ..................................................................................................... 39**

**12.** **EVALUACIÓN NORMATIVA AMBIENTAL APLICABLE ..................................................... 44**

**13.** **CONCLUSIONES ................................................................................................................... 45**

Adenda - Modelación Calidad del Aire
Proyecto Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020

**ÍNDICE DE TABLAS**

Tabla 4-1: Normativa Primaria de Calidad del Aire ....................................................................................... 7

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La normativa ambiental aplicable al proyecto corresponde a la normativa primaria de calidad del aire para aquellos contaminantes que el Proyecto emita en cantidades suficientes como para aumentar significativamente los niveles existentes. -->

**Tabla 4-1: Normativa Primaria de Calidad del Aire****

| Contaminante | Estadístico | Concentración<br>(μg/m3N) | Referencia |
| --- | --- | --- | --- |
| MP10 | Promedio<br>trianual<br>de<br>las<br>concentraciones anuales | 50 | D.S. No 59/1998 del<br>Ministerio Secretaría<br>General de la<br>República |
| MP10 | Percentil 98 de las concentraciones<br>de 24 horas de un año | 150 | 150 |
| MP2.5 | Promedio<br>trianual<br>de<br>las<br>concentraciones anuales | 20 | D.S. No 12/2011 del<br>Ministerio de Medio<br>Ambiente |
| MP2.5 | Percentil 98 de las concentraciones<br>de 24 horas de un año | 50 | 50 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **5.** **CARACTERIZACIÓN CALIDAD DEL AIRE** -->
<!-- FIN TABLA 4-1 -->


Tabla 6-1: Resumen estadístico monitoreo meteorológico estación Sierra Gorda, Año 2019 ..................... 9

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Marzo de 2020 Pág. 8 En la siguiente tabla se presenta un resumen de los resultados obtenidos de las variables meteorológicas monitoreadas. -->

**Tabla 6-1: Resumen estadístico monitoreo meteorológico estación Sierra Gorda, Año 2019****

| Estadístico | Variables meteorológicas | Col3 | Col4 |
| --- | --- | --- | --- |
| **Estadístico** | **Velocidad del**<br>**Viento** | **Dirección del**<br>**Viento** | **Temperatura** |
| Número de registros de la estación (datos período) | 8.760 | 8.760 | 8.760 |
| Número de datos medidos y validados | 8.747 | 8.747 | 8.747 |
| Porcentaje de datos válidos | 99,9% | 99,9% | 99,9% |
| Mínimo | 0,21 (m/s) | 0,03 (grados) | -1,13 (°C) |
| Promedio | 3,4 (m/s) | 163,44 (grados) | 18,88 (°C) |
| Máximo | 13,2 (m/s) | 359,95 (grados) | 33,5 (°C) |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. A continuación, se presenta el análisis por cada variable meteorológica monitoreada en la -->
<!-- FIN TABLA 6-1 -->


Tabla 7-1: Características dominio de modelación WRF ............................................................................ 17

<!-- INICIO TABLA 7-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **7.2. Dominio de modelación** En la Tabla 7-1 se presenta las características del dominio de modelación del modelo WRF. Posteriormente, en la Figura 7-1se presenta el dominio antes mencionado. -->

**Tabla 7-1: Características dominio de modelación WRF****

| Período Modelado | 01 enero 2019 - 31 diciembre 2019 |
| --- | --- |
| Latitud del origen del dominio | 22.854S |
| Longitud del origen del dominio | 69.230W |
| Proyección | LCC |
| Datum | NWS-84 |
| Resolución | 1 km |
| Tamaño del dominio | 101 x 101 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Enviro Modeling. Adenda - Modelación Calidad del Aire Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8 -->
<!-- FIN TABLA 7-1 -->


Tabla 7-2: Evaluación estadística velocidad del viento ............................................................................... 23

<!-- INICIO TABLA 7-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Adenda - Modelación Calidad del Aire Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8 Marzo de 2020 Pág. 22 -->

**Tabla 7-2: Evaluación estadística velocidad del viento****

| Medida de Error | Serie de tiempo | Ciclo Diario |
| --- | --- | --- |
| Sesgo (S) | -1,6 | -1,6 |
| Error cuadrático medio (ECM) | 2,2 | 1,7 |
| Coeficiente de correlación (r) | 0,7 | 0,6 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. De la tabla anterior se observa que el valor del sesgo presenta valores negativos, por lo tanto y tal como se señaló anteriormente el modelo meteorológico subestima los valores de velocidad -->
<!-- FIN TABLA 7-2 -->


Tabla 7-3: Factor de corrección .................................................................................................................. 28

Tabla 8-1: Coordenadas receptores sensibles para MP10 y MP2.5 .......................................................... 32

<!-- INICIO TABLA 8-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Adenda - Modelación Calidad del Aire Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8 Marzo de 2020 Pág. 31 -->

**Tabla 8-1: Coordenadas receptores sensibles para MP10 y MP2.5****

| Receptor | Coordenadas UTM (WGS84) | Col3 | Descripción |
| --- | --- | --- | --- |
| **Receptor** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| Receptor sensible | 479.836 | 7.488.356 | Vivienda |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Figura 8-3: Distribución espacial receptores sensibles MP10 y MP2.5** -->
<!-- FIN TABLA 8-1 -->


Tabla 9-1: Resumen de emisiones por fase del proyecto ........................................................................... 33

<!-- INICIO TABLA 9-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de Emisiones Atmosféricas que serán generadas durante las fases de construcción, operación y cierre del proyecto. En la siguiente tabla se presenta un resumen de las emisiones obtenidas. -->

**Tabla 9-1: Resumen de emisiones por fase del proyecto****

| Fase | Año | Emisión (toneladas) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Año** | **MPS** | **MP10** | **MP2.5** | **HC** | **CO** | **NOx** | **SO2 ** |
| Construcción | Construcción | 0,5713 | 0,2045 | 0,1121 | 0,0554 | 0,1353 | 0,5884 | 0,0179 |
| Operación | Año 1 | 54,8662 | 17,9746 | 9,3612 | 5,9237 | 17,3224 | 73,3563 | 1,8551 |
| Operación | Año 2 | 59,7361 | 19,5811 | 10,2064 | 6,4597 | 18,8861 | 79,9810 | 2,0237 |
| Operación | Año 3 | 59,7361 | 19,5811 | 10,2064 | 6,4597 | 18,8861 | 79,9810 | 2,0237 |
| Operación | Año 4 | 16,9813 | 6,8623 | 4,3438 | 3,7907 | 12,2781 | 54,3128 | 2,0172 |
| Cierre | Cierre | 0,0283 | 0,0132 | 0,0096 | 0,0112 | 0,0264 | 0,1243 | 0,0000 |

<!-- Estadísticas: 7 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Tal como se observa en la tabla anterior, en el año 2 y 3 de la fase de operación, se generan las máximas emisiones del proyecto, por lo tanto y como condición más desfavorable será el año 2 -->
<!-- FIN TABLA 9-1 -->


Tabla 9-2: Desglose de emisiones año 2, fase de operación. .................................................................... 34

<!-- INICIO TABLA 9-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Adenda - Modelación Calidad del Aire Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8 Marzo de 2020 Pág. 33 -->

**Tabla 9-2: Desglose de emisiones año 2, fase de operación.****

| Fuente Emisora | Emisión (toneladas/año) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente Emisora** | **MPS** | **MP10** | **MP2.5** | **HC** | **CO** | **NOx** | **SO2 ** |
| Excavaciones | 28,3821 | 5,3486 | 2,9801 | --- | --- | --- | --- |
| Carga de material | 0,6351 | 0,3004 | 0,0455 | --- | --- | --- | --- |
| Descarga de material | 0,4827 | 0,2283 | 0,0346 | --- | --- | --- | --- |
| Erosión eólica | 6,9640 | 3,4820 | 0,5131 | --- | --- | --- | --- |
| Planta de Áridos | 0,9969 | 0,3588 | 0,0370 | --- | --- | --- | --- |
| Planta de Asfalto | 1,8568 | 1,1937 | 1,1937 | --- | --- | --- | --- |
| Tránsito camino pavimentado | 8,0471 | 1,5446 | 0,3737 | --- | --- | --- | --- |
| Tránsito camino no pavimentado | 7,3454 | 2,0987 | 0,2099 | --- | --- | --- | --- |
| Motor - Tránsito camino pavimentado | 0,1701 | 0,1701 | 0,1701 | 0,3910 | 1,8802 | 7,7658 | 0,0086 |
| Motor - Tránsito camino no pavimentado | 0,0022 | 0,0022 | 0,0022 | 0,0053 | 0,0236 | 0,0828 | 0,0001 |
| Motor de maquinarias y grupos electrógenos | 4,8537 | 4,8537 | 4,6465 | 6,0634 | 16,9823 | 72,1324 | 2,0150 |
| Total | **59,7361** | **19,5811** | **10,2064** | **6,4597** | **18,8861** | **79,9810** | **2,0237** |

<!-- Estadísticas: 13 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Las emisiones atmosféricas, se caracterizan por ser principalmente fugitivas, y de baja altura de descarga, es por ello, que serán simuladas como fuentes de “Áreas”. Por otra parte, y como -->
<!-- FIN TABLA 9-2 -->


Tabla 10-1: Concentración MP10, año 2 fase de operación (μg/m [3] ) .......................................................... 36

<!-- INICIO TABLA 10-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La siguiente tabla presenta las concentraciones de MP10 obtenidas directamente del modelo de dispersión y las concentraciones corregidas obtenidas a partir del factor de corrección presentado en la sección 7.3.3. -->

**Tabla 10-1: Concentración MP10, año 2 fase de operación (μg/m** **[3]** **)****

| Receptor | Aporte MP10 Modelo<br>CALPUFF | Col3 | Factor de<br>Corrección | Aporte MP10 Modelo<br>CALPUFF Corregido | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Receptor** | **P98 promedio**<br>**24 horas** | **Promedio**<br>**anual** | **Promedio**<br>**anual** | **P98 promedio**<br>**24 horas** | **Promedio**<br>**anual** |
| Receptor sensible | 0,29 | 0,09 | 0,5 | 0,15 | 0,05 |
| **Valor de la Norma (μg/m3) ** | **Valor de la Norma (μg/m3) ** | **Valor de la Norma (μg/m3) ** | **Valor de la Norma (μg/m3) ** | **150** | **50** |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. De la tabla anterior se observa que el aporte corregido de concentración tanto diaria como anual de material particulado MP10 del proyecto en el receptor sensible cercano al proyecto se -->
<!-- FIN TABLA 10-1 -->


Tabla 10-2: Concentración MP2.5, año 2 fase de operación (μg/m [3] ) ......................................................... 36

<!-- INICIO TABLA 10-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la siguiente tabla se presenta las concentraciones de MP2.5 obtenidas directamente del modelo de dispersión y las concentraciones corregidas obtenidas a partir del factor de corrección presentado en la sección 7.3.3. -->

**Tabla 10-2: Concentración MP2.5, año 2 fase de operación (μg/m** **[3]** **)****

| Receptor | Aporte MP2.5 Modelo<br>CALPUFF | Col3 | Factor de<br>Corrección | Aporte MP2.5 Modelo<br>CALPUFF Corregido | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Receptor** | **P98 promedio**<br>**24 horas** | **Promedio**<br>**anual** | **Promedio**<br>**anual** | **P98 promedio**<br>**24 horas** | **Promedio**<br>**anual** |
| Receptor sensible | 0,07 | 0,02 | 0,5 | 0,04 | 0,01 |
| **Valor de la norma (μg/m3) ** | **Valor de la norma (μg/m3) ** | **Valor de la norma (μg/m3) ** | **Valor de la norma (μg/m3) ** | **50** | **20** |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Adenda - Modelación Calidad del Aire Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8 -->
<!-- FIN TABLA 10-2 -->


Tabla 10-3: Aporte MP10 y MP2.5 en punto de máximo impacto (PMI), año 2 fase de operación (μg/m [3] ) 37

<!-- INICIO TABLA 10-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **10.2. Aportes en punto de máximo impacto** En la siguiente tabla se presenta los aportes del proyecto en el punto de máximo impacto para MP10 y MP2.5. -->

**Tabla 10-3: Aporte MP10 y MP2.5 en punto de máximo impacto (PMI),****

| Contaminante | Estadístico | Aporte<br>(μg/m3) | Factor de<br>corrección | Aporte<br>corregido<br>(μg/m3) | Norma<br>(μg/m3) | % Norma | Coordenadas UTM (WGS-84) | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadístico** | **Aporte**<br>**(μg/m3) ** | **Factor de**<br>**corrección** | **Aporte**<br>**corregido**<br>**(μg/m3) ** | **Norma**<br>**(μg/m3) ** | **% Norma** | **Este (m)** | **Norte (m)** |
| MP10 | P98 promedio 24<br>horas | 24,30 | 0,5 | 12,15 | 150 | 8 | 481.000 | 7.490.582 |
| MP10 | Promedio anual | 4,34 | 0,5 | 2,17 | 50 | 4 | 479.999 | 7.490.581 |
| MP2.5 | P98 promedio 24<br>horas | 6,38 | 0,5 | 3,19 | 50 | 6 | 479.999 | 7.490.581 |
| MP2.5 | Promedio anual | 1,97 | 0,5 | 0,99 | 20 | 5 | 479.999 | 7.490.581 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Tal como se observa en la tabla anterior, los aportes en concentración tanto de MP10 como de MP2.5 producto de las emisiones generadas durante el año 2 de la fase de operación del proyecto -->
<!-- FIN TABLA 10-3 -->


Tabla 12-1: Evaluación cumplimiento normativa en receptor sensible cercano al proyecto ...................... 44

<!-- INICIO TABLA 12-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **12.** **EVALUACIÓN NORMATIVA AMBIENTAL APLICABLE** En la siguiente tabla se presenta la evaluación del cumplimiento de la normativa para cada contaminante en el receptor sensible cercano al proyecto. -->

**Tabla 12-1: Evaluación cumplimiento normativa en receptor sensible cercano al proyecto****

| Contaminante | Estadístico | Línea de<br>Base<br>(μm3/N)<br>LB | Aporte<br>Proyectos con<br>RCA (μm3/N)<br>AP<br>RCA | Aporte<br>Proyecto<br>(μm3/N)<br>AP | LB+AP+AP<br>RCA<br>(μm3/N) | Norma<br>(μm3/N | % de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Promedio anual | S/I | N/A | 0,2 | 0 | 50 | 0 |
| MP10 | Percentil 98 promedio 24 horas | S/I | N/A | 0,1 | 0 | 150 | 0 |
| MP2.5 | Promedio anual | S/I | N/A | 0,0 | 0 | 20 | 0 |
| MP2.5 | Percentil 98 promedio 24 horas | S/I | N/A | 0,0 | 0 | 50 | 0 |

<!-- Estadísticas: 4 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- S/I: Sin información N/A: No aplica Fuente: Elaboración propia. -->
<!-- FIN TABLA 12-1 -->


Adenda - Modelación Calidad del Aire
Proyecto Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020

**ÍNDICE DE FIGURAS**

Figura 6-1: Localización del proyecto respecto de Calama y Sierra Gorda .................................................. 8

Figura 6-1: Serie de tiempo velocidad del viento estación Sierra Gorda, Año 2019 .................................. 10

Figura 6-2: Ciclo diario velocidad del viento estación Sierra Gorda, Año 2019 .......................................... 11

Figura 6-3: Serie de tiempo dirección del viento estación Sierra Gorda, Año 2019 ................................... 12

Figura 6-4: Rosa de vientos por período del día estación Sierra Gorda, Año 2019 ................................... 12

Figura 6-5: Rosa de vientos estación Sierra Gorda, Año 2019................................................................... 14

Figura 6-6: Serie de tiempo temperatura estación Sierra Gorda, Año 2019 ............................................... 15

Figura 6-7: Ciclo diario temperatura estación Sierra Gorda, Año 2019 ...................................................... 16

Figura 7-1: Dominio de modelación WRF ................................................................................................... 18

Figura 7-2: Serie de tiempo velocidad del viento, Estación Sierra Gorda modelado y observado 2019 .... 20

Figura 7-3: Ciclo diario velocidad del viento, Estación Sierra Gorda modelado y observado 2019 ........... 22

Figura 7-4: Serie de tiempo dirección del viento, Estación Sierra Gorda modelado y observado 2019 .... 24

Figura 7-5: Rosa de vientos, Estación Sierra Gorda modelado y observado 2019 .................................... 25

Figura 8-1: Dominio de modelación Calpuff ................................................................................................ 30

Figura 8-2: Topografía del dominio de modelación Calpuff ........................................................................ 31

Figura 8-3: Distribución espacial receptores sensibles MP10 y MP2.5 ...................................................... 32

Figura 9-1: Fuentes modeladas, año 2 fase de construcción ..................................................................... 35

Figura 10-1: Ubicación puntos de máximo impacto .................................................................................... 38

Figura 10-3: Curvas de concentración percentil 98 24 horas MP10 ........................................................... 40

Figura 10-4: Curvas de concentración promedio anual MP10 .................................................................... 41

Figura 10-5: Curvas de concentración percentil 98 24 horas MP2.5 .......................................................... 42

Figura 10-6: Curvas de concentración promedio anual MP2.5 ................................................................... 43

**ÍNDICE DE APÉNDICES**

Apéndice A Desglose de emisiones ingresadas al modelo Calpuff ............................................................ 47

Adenda - Modelación Calidad del Aire
Proyecto Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020

**1.** **INTRODUCCIÓN**

El presente informe contiene los resultados de la modelación de la dispersión de las emisiones
atmosféricas para material particulado respirable y fino respirable (MP10 y MP2.5), asociadas a
la fase de operación del Proyecto “Extracción de Áridos y Planta de Asfaltos Sector Pozo D8” en
adelante “el Proyecto”.

El objetivo general del Proyecto es explotar áridos para producir material de distintas calidades,
además de la producción de asfalto.

La modelación de la dispersión de emisiones atmosféricas de material particulado MP10 y MP2.5
se realizó en base a la utilización del modelo CALPUFF, aprobado por la Agencia de Protección
Ambiental US-EPA y recomendado por la “Guía para el Uso de Modelos de Calidad del Aire en
el SEIA” (Servicio de Evaluación Ambiental, 2012).

**2.** **OBJETIVO**

Estimar el impacto de las concentraciones de material particulado MP10 y MP2.5 producto de las
emisiones atmosféricas generadas durante la fase de operación del Proyecto “Extracción de
Áridos y Planta de Asfaltos Sector Pozo D8”.

**3.** **METODOLOGÍA**

Para estimar las concentraciones de material particulado MP10 y MP2.5 que serán percibidas en
los receptores sensibles más cercanos al Proyecto, se consideró la siguiente metodología:

➢ Analizar la normativa ambiental aplicable para los contaminantes en evaluación.

➢ Caracterización calidad del aire.

➢ Caracterización meteorológica.

➢ Describir y justificar el modelo meteorológico utilizado por el modelo de dispersión de

emisiones atmosféricas.

➢ Describir y justificar el modelo de dispersión de emisiones atmosféricas.

➢ Describir y caracterizar las emisiones atmosféricas que serán utilizadas en el modelo de
dispersión de emisiones atmosféricas.

➢ Analizar los resultados obtenidos del modelo de dispersión de emisiones atmosféricas,
tomando en consideración la normativa ambiental aplicable.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 6

**4.** **NORMATIVA AMBIENTAL APLICABLE**

La normativa ambiental aplicable al proyecto corresponde a la normativa primaria de calidad del
aire para aquellos contaminantes que el Proyecto emita en cantidades suficientes como para
aumentar significativamente los niveles existentes.

**Tabla 4-1: Normativa Primaria de Calidad del Aire**

|Contaminante|Estadístico|Concentración<br>(μg/m3N)|Referencia|
|---|---|---|---|
|MP10|Promedio<br>trianual<br>de<br>las<br>concentraciones anuales|50|D.S. No 59/1998 del<br>Ministerio Secretaría<br>General de la<br>República|
|MP10|Percentil 98 de las concentraciones<br>de 24 horas de un año|150|150|
|MP2.5|Promedio<br>trianual<br>de<br>las<br>concentraciones anuales|20|D.S. No 12/2011 del<br>Ministerio de Medio<br>Ambiente|
|MP2.5|Percentil 98 de las concentraciones<br>de 24 horas de un año|50|50|

Fuente: Elaboración propia.

**5.** **CARACTERIZACIÓN CALIDAD DEL AIRE**

En base a la localización del proyecto, y a la disponibilidad de estaciones de calidad del aire en
el Sistema de Información de Calidad del Aire (SINCA), se identificaron estaciones de monitoreo
en el sector de Sierra Gorda y en Calama. La estación de calidad del aire ubicada en la localidad
de Sierra Gorda se encuentra a unos 25 km en línea recta del proyecto, y las estaciones de

calidad del aire ubicadas en la ciudad de Calama se encuentran a unos 38 km en línea recta del

proyecto, tal como se muestra en la siguiente figura.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 7

**Figura 5-1: Localización del proyecto respecto de Calama y Sierra Gorda**

Fuente: Elaboración propia.

Dado la distancia a las estaciones de calidad del aire, encontrándose éstas fuera del área de

influencia del proyecto, definida por un área de 14x14 km como condición conservadora, las
estaciones de calidad del aire identificadas no son representativas del área de influencia del
proyecto, puesto que se encuentran ubicadas en entornos urbanos y cercanas a proyectos
actualmente en ejecución.

**6.** **CARACTERIZACIÓN METEOROLÓGICA**

Para la caracterización meteorológica en el área de emplazamiento del Proyecto, se analizaron
los registros de las variables meteorológicas, velocidad y dirección del viento y temperatura,

monitoreadas durante el año 2019 en la estación Sierra Gorda. Si bien como se mencionó

anteriormente la estación Sierra Gorda se encuentra a unos 25 km en línea recta del proyecto, la
información meteorológica resulta válida, toda vez que no existen mayores diferencias
topográficas que puedan alterar por una parte la dirección y velocidad del viento ni variar
significativamente las temperaturas entre el área del proyecto y lo registrado en la estación Sierra

Gorda.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 8

En la siguiente tabla se presenta un resumen de los resultados obtenidos de las variables
meteorológicas monitoreadas.

**Tabla 6-1: Resumen estadístico monitoreo meteorológico estación Sierra Gorda, Año 2019**

|Estadístico|Variables meteorológicas|Col3|Col4|
|---|---|---|---|
|**Estadístico**|**Velocidad del**<br>**Viento**|**Dirección del**<br>**Viento**|**Temperatura**|
|Número de registros de la estación (datos período)|8.760|8.760|8.760|
|Número de datos medidos y validados|8.747|8.747|8.747|
|Porcentaje de datos válidos|99,9%|99,9%|99,9%|
|Mínimo|0,21 (m/s)|0,03 (grados)|-1,13 (°C)|
|Promedio|3,4 (m/s)|163,44 (grados)|18,88 (°C)|
|Máximo|13,2 (m/s)|359,95 (grados)|33,5 (°C)|

Fuente: Elaboración propia.

A continuación, se presenta el análisis por cada variable meteorológica monitoreada en la

estación Sierra Gorda durante el año 2019.

**6.1. Velocidad del viento**

En la Figura 6-1 se presenta la serie de tiempo de la velocidad del viento registrada en la estación
Sierra Gorda para el año 2019.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 9

**Figura 6-1: Serie de tiempo velocidad del viento estación Sierra Gorda, Año 2019**

Fuente: Elaboración propia.

Tal como se observa en la figura anterior, la velocidad del viento alcanza intensidades sobre los
9 (m/s) durante los meses de primavera y verano, mientras que en los meses de otoño e invierno
se observa una disminución en la velocidad del viento respecto de los meses de verano y
primavera, cuyos valores se encuentran en general bajo los (7 m/s), presentándose algunas
máximas sobre los 12 (m/s).

En la Figura 6-2 se presenta el ciclo diario de la velocidad del viento registrada en la estación
Sierra Gorda para el año 2019.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 10

**Figura 6-2: Ciclo diario velocidad del viento estación Sierra Gorda, Año 2019**

Fuente: Elaboración propia.

Tal como se observa en la figura anterior, el ciclo diario de la velocidad del viento presenta las
menores intensidades durante las primeras horas del día, siendo éstas en promedio inferior a 2,6
(m/s), posteriormente dichas intensidades aumentan hasta alcanzar su valor máximo promedio
de 6,6 (m/s) entre las 17:00 y 19:00 horas, para luego disminuir nuevamente durante la noche.

**6.2. Dirección del viento**

En la Figura 6-3 se presenta la serie de tiempo correspondiente a la dirección del viento

monitoreada durante el año 2019 en la estación Sierra Gorda.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 11

**Figura 6-3: Serie de tiempo dirección del viento estación Sierra Gorda, Año 2019**

Fuente: Elaboración propia.

La serie de tiempo de la dirección del viento presenta una predominancia de vientos de
componente principalmente Noreste y Suroeste.

En las siguientes figuras se presentan las rosas de viento para distintos períodos del día.

**Figura 6-4: Rosa de vientos por período del día estación Sierra Gorda, Año 2019**

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 12

Fuente: Elaboración propia.

De las figuras anteriores se observa que durante las primeras horas del día se presentan vientos
predominantes desde el noreste con intensidades principalmente entre 1,5 y 4,5 m/s.

Para el periodo entre las 06:00 y 11:00 horas, se mantiene la predominancia del viento noreste y
además se observa la presencia de vientos Nor Noreste con predominancia similar. La intensidad
del viento predominante se mantiene.

A partir de las 12:00 y hasta las 17:00 horas se observa predominancia de vientos provenientes
desde el Nor Noroeste y desde el Suroeste, con un aumento en la intensidad del viento respecto
del periodo anterior, superando los 6,5 m/s.

Finalmente, en el periodo entre las 18:00 y 23:00 horas, se observa predominancia de vientos
desde el Suroeste, con intensidades mayormente entre 2,5 y 6,5 m/s.

En la siguiente figura se presenta la rosa de vientos para el año 2019 en la estación Sierra Gorda.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 13

**Figura 6-5: Rosa de vientos estación Sierra Gorda, Año 2019**

Fuente: Elaboración propia.

Tal como muestra la rosa de vientos, durante el año monitoreado se observa predominancia de
vientos Noreste con intensidades entre1,5 y 4,5 m/s mayoritariamente y vientos predominantes
con dirección Suroeste con intensidades que superan los 6,5 m/s.

**6.3. Temperatura**

En la siguiente figura se presenta la serie de tiempo para los valores monitoreados de temperatura
en la estación Sierra Gorda en el período 2019.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 14

**Figura 6-6: Serie de tiempo temperatura estación Sierra Gorda, Año 2019**

Fuente: Elaboración propia.

En la Figura 6-6 se muestra el comportamiento de la temperatura ambiental durante el año 2019,
donde se observa una mayor oscilación entre las temperaturas mínimas y máximas en el período
de otoño e invierno. Respecto de las máximas temperaturas no se presentan grandes variaciones
a lo largo del año. La temperatura máxima supera los 33°C mientras que la mínima es inferior a

0°C.

A continuación, se presenta el ciclo diario de la temperatura.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 15

**Figura 6-7: Ciclo diario temperatura estación Sierra Gorda, Año 2019**

Fuente: Elaboración propia.

En base a la figura anterior, las mínimas temperaturas se presentan en las primeras horas del
día, mientras que las máximas se presentan entre las 14:00 y 17:00 horas en promedio.

**7.** **MODELO METEOROLÓGICO**

**7.1. Justificación y descripción del modelo meteorológico**

El modelo meteorológico utilizado como input para realizar la modelación de calidad del aire del
Proyecto, corresponde al Modelo WRF.

El modelo llamado Weather Research and Forecasting (WRF) es un modelo numérico de área
limitada de última generación diseñado para la investigación y la predicción numérica del tiempo
meteorológico. Este modelo permite simulaciones tanto de condiciones atmosféricas reales (a
través de análisis y observaciones) como idealizadas, a diferentes escalas. Dada su flexibilidad y
constantes mejoras, el modelo WRF actualmente es uno de los modelos de mayor uso en
diversos centros meteorológicos y de investigación alrededor del mundo.

Se recomienda el uso del modelo WRF en la “Guía para el uso de modelos de calidad del aire en
el SEIA”. La información meteorológica obtenida del modelo WRF y que será utilizada en el
modelo de dispersión de emisiones atmosféricas se adquirió de la empresa Enviro Modeling.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 16

**7.2. Dominio de modelación**

En la Tabla 7-1 se presenta las características del dominio de modelación del modelo WRF.
Posteriormente, en la Figura 7-1se presenta el dominio antes mencionado.

**Tabla 7-1: Características dominio de modelación WRF**

|Período Modelado|01 enero 2019 - 31 diciembre 2019|
|---|---|
|Latitud del origen del dominio|22.854S|
|Longitud del origen del dominio|69.230W|
|Proyección|LCC|
|Datum|NWS-84|
|Resolución|1 km|
|Tamaño del dominio|101 x 101|

Fuente: Enviro Modeling.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 17

**Figura 7-1: Dominio de modelación WRF**

Fuente: Elaboración propia.

**7.3. Evaluación del modelo meteorológico**

Para evaluar el desempeño de la modelación meteorológica realizada mediante el modelo WRF,
se analizan los datos medidos en la estación Sierra Gorda durante el año 2019 y se comparan
con los datos modelados para la coordenada (x,y) dentro de la grilla de modelación en la cual se
emplaza la estación Sierra Gorda. Las variables meteorológicas evaluadas corresponden a
velocidad del viento y dirección del viento.

Para la evaluación cualitativa se presentan gráficos con la serie de tiempo y ciclos diarios,
mientras que para la evaluación cuantitativa se evalúan las métricas estadísticas tales como el
sesgo (S), error cuadrático medio (ECM) y el coeficiente de correlación (r), los cuales se describen

a continuación:

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 18

Sesgo (S): Representa la tendencia del modelo a sobrestimar o subestimar las condiciones
reales. Para valores negativos el modelo tiende a subestimar el valor de las variables modeladas,
mientras que, para valores positivos, el modelo tiende a sobreestimar.

Error cuadrático medio (ECM): Entrega la diferencia promedio entre los valores modelados y

observados.

Coeficiente de Correlación (r): Entrega una medida de la relación lineal entre la variable modelada
y la observada. El valor del coeficiente se encuentra entre -1 y 1. Para el caso de la modelación,
entre más cercano a 1, mejor es la capacidad del modelo de representar las condiciones

atmosféricas.

Donde:

Mi: Variable modelada.

Oi: Variable observada.

: Promedio variables modeladas.

: Promedio variables observadas.

N: Total de datos evaluados.

A continuación, se presentan los resultados obtenidos para las variables analizadas.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 19

**7.3.1. Velocidad del viento**

En la Figura 7-2 se presenta la serie de tiempo para la velocidad del viento, contrastando los
valores observados en la estación Sierra Gorda (puntos de color celeste) con los valores
modelados para el año 2019 en WRF (puntos de color naranjo).

**Figura 7-2: Serie de tiempo velocidad del viento, Estación Sierra Gorda**

**modelado y observado 2019**

Fuente: Elaboración propia.

Tal como se observa en la figura anterior los valores de velocidad del viento modelados (puntos
de color naranjo) son menores a los observados (puntos de color azul), se tiene que la diferencia
en magnitud entre los valores modelados con los observados se encuentra principalmente entre
1 m/s y -4 m/s. Las diferencias con valores positivos indican que el modelo WRF sobreestimó las

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 20

magnitudes de la velocidad del viento respecto a los valores observados, y los valores negativos
indican que el modelo WRF subestimó los valores observados.

En cuanto al comportamiento anual de la velocidad del viento, se observa que tanto los valores
observados como modelados presentan la misma tendencia, es decir, las mayores intensidades
se presentan en el período primavera - verano, mientras que se observa un leve descenso de

las intensidades del viento en los meses de otoño e invierno.

En la Figura 7-3 se presenta el ciclo diario de la velocidad del viento tanto para los valores
observados (color azul) como para los valores modelados (color naranjo), durante el año 2019,
en el cual se observa que el modelo subestima la velocidad del viento respecto de los valores
observados durante todas las horas del día, con diferencias en magnitudes que van entre 1 m/s
y 3,5 m/s, donde las menores diferencias se presentan durante la madruga hasta medio día y
durante la noche (cercanas a 1 m/s) y las mayores diferencias se obtienen entre las 17:00 y 21:00
horas (cercanas a 3,5 m/s).

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 21

**Figura 7-3: Ciclo diario velocidad del viento, Estación Sierra Gorda**

**modelado y observado 2019**

Fuente: Elaboración propia.

En cuanto a las medidas estadísticas evaluadas, en la Tabla 7-2 se presentan los valores

obtenidos.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 22

**Tabla 7-2: Evaluación estadística velocidad del viento**

|Medida de Error|Serie de tiempo|Ciclo Diario|
|---|---|---|
|Sesgo (S)|-1,6|-1,6|
|Error cuadrático medio (ECM)|2,2|1,7|
|Coeficiente de correlación (r)|0,7|0,6|

Fuente: Elaboración propia.

De la tabla anterior se observa que el valor del sesgo presenta valores negativos, por lo tanto y
tal como se señaló anteriormente el modelo meteorológico subestima los valores de velocidad
del viento en el punto en el cual se ubica la estación Sierra Gorda.

Al observar el error cuadrático medio (ECM), se infiere que la serie de tiempo presenta un mayor
valor respecto del ciclo diario, dado que este último promedia los valores horarios y por lo tanto
suaviza los valores mínimos y máximos.

Finalmente, el coeficiente de correlación (r), se encuentra cercano a 1, mostrando un buen ajuste
lineal tanto para la serie de tiempo como para el ciclo diario.

**7.3.2. Dirección del viento**

En la Figura 7-4 se presenta la serie de tiempo para la dirección del viento, contrastando los
valores observados (puntos de color celeste) en la estación Sierra Gorda con los valores
modelados para el año 2018 en WRF (puntos de color naranjo).

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 23

**Figura 7-4: Serie de tiempo dirección del viento, Estación Sierra Gorda**

**modelado y observado 2019**

Fuente: Elaboración propia.

Tal como se observa en la figura anterior, la dirección predominante de los vientos para los
valores observados y los obtenidos del modelo WRF corresponden a Suroeste, Noreste y Nor
Noreste, principalmente.

En la siguiente figura se presentan las rosas de viento observada y modelada en la estación
Sierra Gorda para el período 2019 y para diferentes períodos del día.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 24

**Figura 7-5: Rosa de vientos, Estación Sierra Gorda**

**modelado y observado 2019**

|Rosa de vientos observada|Rosa de vientos modelada|
|---|---|
|<br>Año 2019|<br>Año 2019|
|<br>Período 00:00 - 05:00|<br>Período 00:00 - 05:00|

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 25

|Rosa de vientos observada|Rosa de vientos modelada|
|---|---|
|<br>Período 06:00 - 11:00|<br>Período 06:00 - 11:00|
|<br>Período 12:00 - 17:00|<br>Período 12:00 - 17:00|

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 26

|Rosa de vientos observada|Rosa de vientos modelada|
|---|---|
|<br>Período 18:00 - 23:00|<br>Período 18:00 - 23:00|

Fuente: Elaboración propia.

Tal como se observa en la figura anterior, la rosa de vientos para el año 2019 correspondiente a
los datos modelados, presenta un buen ajuste respecto de los datos observados, presentándose
una sobrestimación de vientos Nor Noroeste y subestimación de vientos Noreste. Por otra parte,

el modelo tiende a subestimar la intensidad de los vientos.

En cuanto a los diferentes períodos del día, se observa que en el período de 00:00 a 05:00 horas
el viento predominante observado proviene desde el Noreste con intensidades entre 1,5 a 4,5 m/s
principalmente, mientras que el viento predominante modelado proviene desde el Este, con
intensidades entre 1,0 y 2,5 m/s principalmente.

En el período comprendido entre las 06:00 y 11:00 horas el viento observado presenta dirección
predominante desde el Noreste y Nor Noreste, mientras que el viento modelado presenta
direcciones predominantes desde el Nor Noreste, Norte y Este.

Posteriormente, para el período comprendido entre las 12:00 y 17:00 horas el viento modelado
presenta un mejor ajuste con la dirección del viento observado. Sin embargo, la intensidad de los
vientos modelados sigue siendo inferior a los valores observados.

Finalmente, para el período entre las 18:00 y 23:00 horas tanto el viento observado como
modelado proviene principalmente desde el Suroeste, siendo de mayor intensidad el viento

observado.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 27

**7.3.3. Conclusiones análisis de incertidumbre**

En base al análisis de incertidumbre realizado para el modelo WRF en la estación Sierra Gorda,
para las variables meteorológicas velocidad y dirección del viento, se concluye lo siguiente:

El modelo WRF subestima la velocidad del viento respecto de los valores observados durante
todas las horas del día, con diferencias en magnitudes que van entre 1 m/s y 3,5 m/s, donde las
menores diferencias se presentan durante la madruga hasta medio día y durante la noche
(cercanas a 1 m/s) y las mayores diferencias se obtienen entre las 17:00 y 21:00 horas (cercanas
a 3,5 m/s).

En cuanto a la evaluación estadística, los valores negativos obtenidos para el sesgo señalan la
subestimación de los valores de velocidad del viento obtenidos por el modelo para la estación
Sierra Gorda respecto de los valores observados. Por otra parte, se observa un buen ajuste lineal,
representando por el coeficiente de correlación, donde se obtienen valores cercanos a 1.

Respecto a la dirección del viento, presenta un buen ajuste respecto de los datos observados,
presentándose una sobrestimación de vientos Nor Noroeste y subestimación de vientos Noreste.

En base a lo anterior, es que se estimó un factor de corrección el cual se aplicará sobre los
resultados de concentración, de manera de corregir esta subestimación por parte del modelo
meteorológico sobre la velocidad del viento, dado que a menor velocidad del viento menor será
la dispersión de los contaminantes y por tanto más altas las concentraciones modeladas. Dicho
factor se construyó en base a los valores promedio de velocidad del viento, tal como se muestra
en la siguiente tabla.

|Col1|Tabla 7-3: Factor de corrección|Col3|Col4|
|---|---|---|---|
|**Estación**|**Velocidad del viento promedio**|**Velocidad del viento promedio**|**Factor de corrección**|
|**Estación**|**Observado (m/s)**|**Modelado (m/s)**|**Modelado (m/s)**|
|Centro|3,4|1,8|0,5|

Fuente: Elaboración propia.

**8.** **MODELO DE DISPERSIÓN DE EMISIONES ATMOSFÉRICAS**

**8.1. Justificación y descripción del modelo de calidad del aire**

La selección del modelo de calidad del aire se basa fundamentalmente en lo recomendado en la

“Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, en la cual se recomienda el modelo
tipo “puff” CALPUFF para proyectos, cuya área de influencia es mayor a 5 km y cuyos

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 28

contaminantes sean del tipo primario, es decir, cuyas emisiones se liberan directamente al

ambiente.

El sistema de modelación CALPUFF incluye tres componentes principales: WRF, CALPUFF y
CALPOST, además de una larga selección de preprocesadores que incorporan en el modelo
datos meteorológicos y geofísicos.

El modelo WRF es un modelo de pronóstico meteorológico que simula campos de viento y
temperatura en un dominio de modelación engrillado y tridimensional, WRF también produce
campos en dos-dimensiones como altura de mezcla, características de superficie y propiedades
de dispersión.

CALPUFF es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario capaz de modelar el
transporte y dispersión de contaminantes en base a los campos de vientos simulados con WRF.
Los modelos tipo “puff” representan una pluma de contaminantes continuo como un número
discreto de paquetes de material contaminante. El modelo evalúa la contribución de un “puff” en
la concentración atmosférica de un receptor en un instante determinado, para luego permitir que
el puff se mueva, evolucione en tamaño, fuerza, etc., hasta la próxima iteración. Luego, la
concentración total en un receptor resultará de la sumatoria de las contribuciones de todos los
“puff”.

Finalmente, a través de CALPOST se procesan las salidas de CALPUFF creando los archivos
con las tabulaciones necesarias para la evaluación de los resultados, según los parámetros

establecidos en las normas de calidad del aire.

**8.2. Dominio de modelación**

Para el modelo de dispersión se acotó el área de modelación meteorológica WRF, a una grilla
con un dominio de modelación de 14 x 14 km con un espaciamiento de celdas de 1 km, dentro
de la cual se ubica el proyecto y los receptores sensibles más cercanos.

En la Figura 8-1, se observa el área de modelación para CALPUFF. Posteriormente en la Figura
8-2 se presenta la topografía del área modelada.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 29

**Figura 8-1: Dominio de modelación Calpuff**

Fuente: Elaboración propia.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 30

**Figura 8-2: Topografía del dominio de modelación Calpuff**

Fuente: Elaboración propia.

**8.3. Receptores sensibles**

Dentro del área de influencia del proyecto, se identificó una edificación del tipo habitacional
ubicada a menos de 2 km al sur del proyecto. Las coordenadas de dicho receptor se presentan
en la Tabla 8-1 y su distribución espacial en la Figura 8-3.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 31

**Tabla 8-1: Coordenadas receptores sensibles para MP10 y MP2.5**

|Receptor|Coordenadas UTM (WGS84)|Col3|Descripción|
|---|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Receptor sensible|479.836|7.488.356|Vivienda|

Fuente: Elaboración propia.

**Figura 8-3: Distribución espacial receptores sensibles MP10 y MP2.5**

Fuente: Elaboración propia.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 32

**9.** **FUENTES EMISIORAS CONSIDERADAS EN LA MODELACIÓN**

En el Anexo 6.1 de la presente Adenda, se presenta el detalle de la actualización de la Estimación
de Emisiones Atmosféricas que serán generadas durante las fases de construcción, operación y
cierre del proyecto.

En la siguiente tabla se presenta un resumen de las emisiones obtenidas.

**Tabla 9-1: Resumen de emisiones por fase del proyecto**

|Fase|Año|Emisión (toneladas)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Fase**|**Año**|**MPS**|**MP10**|**MP2.5**|**HC**|**CO**|**NOx**|**SO2 **|
|Construcción|Construcción|0,5713|0,2045|0,1121|0,0554|0,1353|0,5884|0,0179|
|Operación|Año 1|54,8662|17,9746|9,3612|5,9237|17,3224|73,3563|1,8551|
|Operación|Año 2|59,7361|19,5811|10,2064|6,4597|18,8861|79,9810|2,0237|
|Operación|Año 3|59,7361|19,5811|10,2064|6,4597|18,8861|79,9810|2,0237|
|Operación|Año 4|16,9813|6,8623|4,3438|3,7907|12,2781|54,3128|2,0172|
|Cierre|Cierre|0,0283|0,0132|0,0096|0,0112|0,0264|0,1243|0,0000|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, en el año 2 y 3 de la fase de operación, se generan las
máximas emisiones del proyecto, por lo tanto y como condición más desfavorable será el año 2
de la fase de operación la fase modelada (siendo el año 3 idéntico en emisiones), entendiéndose
que durante el año 1 y 4 de la fase de operación, la fase de construcción y cierre el aporte en

concentraciones de contaminantes será menor.

En la siguiente tabla se presenta el desglose de emisiones generadas durante el año 2 de la fase

de construcción.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 33

**Tabla 9-2: Desglose de emisiones año 2, fase de operación.**

|Fuente Emisora|Emisión (toneladas/año)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Fuente Emisora**|**MPS**|**MP10**|**MP2.5**|**HC**|**CO**|**NOx**|**SO2 **|
|Excavaciones|28,3821|5,3486|2,9801|---|---|---|---|
|Carga de material|0,6351|0,3004|0,0455|---|---|---|---|
|Descarga de material|0,4827|0,2283|0,0346|---|---|---|---|
|Erosión eólica|6,9640|3,4820|0,5131|---|---|---|---|
|Planta de Áridos|0,9969|0,3588|0,0370|---|---|---|---|
|Planta de Asfalto|1,8568|1,1937|1,1937|---|---|---|---|
|Tránsito camino pavimentado|8,0471|1,5446|0,3737|---|---|---|---|
|Tránsito camino no pavimentado|7,3454|2,0987|0,2099|---|---|---|---|
|Motor - Tránsito camino pavimentado|0,1701|0,1701|0,1701|0,3910|1,8802|7,7658|0,0086|
|Motor - Tránsito camino no pavimentado|0,0022|0,0022|0,0022|0,0053|0,0236|0,0828|0,0001|
|Motor de maquinarias y grupos electrógenos|4,8537|4,8537|4,6465|6,0634|16,9823|72,1324|2,0150|
|Total|**59,7361**|**19,5811**|**10,2064**|**6,4597**|**18,8861**|**79,9810**|**2,0237**|

Fuente: Elaboración propia.

Las emisiones atmosféricas, se caracterizan por ser principalmente fugitivas, y de baja altura de
descarga, es por ello, que serán simuladas como fuentes de “Áreas”. Por otra parte, y como
condición conservadora, se considera que las emisiones de todas las fuentes serán generadas
en forma simultánea. Finalmente, se considera toda el área del proyecto en explotación durante

el año 2 como condición más desfavorable.

En Apéndice A se detallan las emisiones de material particulado MP10 y MP2.5 de cada fuente
ingresadas al modelo.

La siguiente figura presenta las fuentes emisoras modeladas, correspondientes a las generadas
en el área del proyecto y en las rutas utilizadas para el transporte de personal, insumos, terraplén
y asfalto.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 34

**Figura 9-1: Fuentes modeladas, año 2 fase de construcción**

Fuente: Elaboración propia.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 35

**10.** **RESULTADOS**

A continuación, se presentan los resultados de concentración de material particulado MP10 y
MP2.5 en los receptores sensibles evaluados. Posteriormente, se presenta la dispersión de

dichos contaminantes a través de curvas de concentración.

**10.1. Aportes en receptores sensibles para MP10 y MP2.5**

La siguiente tabla presenta las concentraciones de MP10 obtenidas directamente del modelo de
dispersión y las concentraciones corregidas obtenidas a partir del factor de corrección presentado

en la sección 7.3.3.

**Tabla 10-1: Concentración MP10, año 2 fase de operación (μg/m** **[3]** **)**

|Receptor|Aporte MP10 Modelo<br>CALPUFF|Col3|Factor de<br>Corrección|Aporte MP10 Modelo<br>CALPUFF Corregido|Col6|
|---|---|---|---|---|---|
|**Receptor**|**P98 promedio**<br>**24 horas**|**Promedio**<br>**anual**|**Promedio**<br>**anual**|**P98 promedio**<br>**24 horas**|**Promedio**<br>**anual**|
|Receptor sensible|0,29|0,09|0,5|0,15|0,05|
|**Valor de la Norma (μg/m3) **|**Valor de la Norma (μg/m3) **|**Valor de la Norma (μg/m3) **|**Valor de la Norma (μg/m3) **|**150**|**50**|

Fuente: Elaboración propia.

De la tabla anterior se observa que el aporte corregido de concentración tanto diaria como anual
de material particulado MP10 del proyecto en el receptor sensible cercano al proyecto se
encuentra muy por debajo del valor de la norma respectiva.

En la siguiente tabla se presenta las concentraciones de MP2.5 obtenidas directamente del
modelo de dispersión y las concentraciones corregidas obtenidas a partir del factor de corrección
presentado en la sección 7.3.3.

**Tabla 10-2: Concentración MP2.5, año 2 fase de operación (μg/m** **[3]** **)**

|Receptor|Aporte MP2.5 Modelo<br>CALPUFF|Col3|Factor de<br>Corrección|Aporte MP2.5 Modelo<br>CALPUFF Corregido|Col6|
|---|---|---|---|---|---|
|**Receptor**|**P98 promedio**<br>**24 horas**|**Promedio**<br>**anual**|**Promedio**<br>**anual**|**P98 promedio**<br>**24 horas**|**Promedio**<br>**anual**|
|Receptor sensible|0,07|0,02|0,5|0,04|0,01|
|**Valor de la norma (μg/m3) **|**Valor de la norma (μg/m3) **|**Valor de la norma (μg/m3) **|**Valor de la norma (μg/m3) **|**50**|**20**|

Fuente: Elaboración propia.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 36

De la tabla anterior se observa que el aporte corregido de concentración tanto diaria como anual
de material particulado MP2.5 del proyecto en el receptor sensible cercano al proyecto se
encuentra muy por debajo del valor de la norma respectiva.

**10.2. Aportes en punto de máximo impacto**

En la siguiente tabla se presenta los aportes del proyecto en el punto de máximo impacto para
MP10 y MP2.5.

**Tabla 10-3: Aporte MP10 y MP2.5 en punto de máximo impacto (PMI),**

**año 2 fase de operación (μg/m** **[3]** **)**

|Contaminante|Estadístico|Aporte<br>(μg/m3)|Factor de<br>corrección|Aporte<br>corregido<br>(μg/m3)|Norma<br>(μg/m3)|% Norma|Coordenadas UTM (WGS-84)|Col9|
|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadístico**|**Aporte**<br>**(μg/m3) **|**Factor de**<br>**corrección**|**Aporte**<br>**corregido**<br>**(μg/m3) **|**Norma**<br>**(μg/m3) **|**% Norma**|**Este (m)**|**Norte (m)**|
|MP10|P98 promedio 24<br>horas|24,30|0,5|12,15|150|8|481.000|7.490.582|
|MP10|Promedio anual|4,34|0,5|2,17|50|4|479.999|7.490.581|
|MP2.5|P98 promedio 24<br>horas|6,38|0,5|3,19|50|6|479.999|7.490.581|
|MP2.5|Promedio anual|1,97|0,5|0,99|20|5|479.999|7.490.581|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes en concentración tanto de MP10 como de
MP2.5 producto de las emisiones generadas durante el año 2 de la fase de operación del proyecto
no superan el valor de la norma en el punto de máximo impacto, siendo dichos aportes inferiores
al 10% de la norma respectiva.

En la Figura 10-1 se presenta la ubicación de los puntos de máximo impacto antes mencionados.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 37

**Figura 10-1: Ubicación puntos de máximo impacto**

Fuente: Elaboración propia.

Tal como se observa en la figura anterior, el PMI para MP10 concentración anual y MP2.5
concentración diaria y anual se ubican dentro del área de explotación del proyecto. El PMI para
MP10 concentración diaria se ubica a un costado del área de explotación, cercano al proyecto.

**10.3. Aportes de proyectos con RCA**

Para determinar el aporte de proyectos que cuentan con resolución de calificación ambiental
(RCA) favorable en el área de influencia del proyecto, se considera lo siguiente:

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 38

➢ Se realizará una revisión en el Sistema de Evaluación de Impacto Ambiental (SEIA). De
dicha revisión se consideró aquellos proyectos que se encuentran dentro del área de
influencia del proyecto y que se encuentren aprobados desde el periodo enero 2015 a la
fecha, considerando la fecha de caducidad de una RCA de 5 años.

➢ Luego se realizará una revisión de la fase actual en la que se encuentra el proyecto,
construcción, operación o cierre, a través de la información publicada en el Sistema
Nacional de Información de Fiscalización Ambiental (SNIFA).

➢ Finalmente, se excluirán los proyectos que hayan iniciado su operación previo a enero 2017,
dado que, de ser así su aporte a la calidad del aire se encuentra medido en la línea de base
para el periodo 2017-2019.

Del análisis anterior no se encontraron proyectos con RCA favorable en el área de influencia del

proyecto.

**10.4. Curvas de concentración**

Las figuras siguientes presentan las curvas de concentraciones obtenidos por el modelo de
dispersión de emisiones atmosféricas para material particulado MP10 y MP2.5, según los
estadísticos establecidos en la normativa correspondiente.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 39

**Figura 10-2: Curvas de concentración percentil 98 24 horas MP10**

Fuente: Elaboración propia.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 40

**Figura 10-3: Curvas de concentración promedio anual MP10**

Fuente: Elaboración propia.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 41

**Figura 10-4: Curvas de concentración percentil 98 24 horas MP2.5**

Fuente: Elaboración propia.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 42

**Figura 10-5: Curvas de concentración promedio anual MP2.5**

Fuente: Elaboración propia.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 43

**12.** **EVALUACIÓN NORMATIVA AMBIENTAL APLICABLE**

En la siguiente tabla se presenta la evaluación del cumplimiento de la normativa para cada
contaminante en el receptor sensible cercano al proyecto.

**Tabla 12-1: Evaluación cumplimiento normativa en receptor sensible cercano al proyecto**

|Contaminante|Estadístico|Línea de<br>Base<br>(μm3/N)<br>LB|Aporte<br>Proyectos con<br>RCA (μm3/N)<br>AP<br>RCA|Aporte<br>Proyecto<br>(μm3/N)<br>AP|LB+AP+AP<br>RCA<br>(μm3/N)|Norma<br>(μm3/N|% de la<br>Norma|
|---|---|---|---|---|---|---|---|
|MP10|Promedio anual|S/I|N/A|0,2|0|50|0|
|MP10|Percentil 98 promedio 24 horas|S/I|N/A|0,1|0|150|0|
|MP2.5|Promedio anual|S/I|N/A|0,0|0|20|0|
|MP2.5|Percentil 98 promedio 24 horas|S/I|N/A|0,0|0|50|0|

S/I: Sin información
N/A: No aplica

Fuente: Elaboración propia.

Cabe señalar que, si bien no se cuenta con línea de base medida en el receptor y que no se
identificaron proyectos con RCA favorable dentro del área de influencia, el aporte en
concentración del proyecto en el receptor sensible es nulo (inferior a 0,5 μm [3] /N) tanto para MP10
como para MP2.5.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 44

**13.** **CONCLUSIONES**

De acuerdo con los antecedentes expuestos en el presente anexo, se obtiene lo siguiente:

De la caracterización de la calidad del aire, no se cuenta con información de monitoreo de

contaminantes en el área de influencia del proyecto, definida por un área de 14x14 km.

De la caracterización meteorológica, utilizando como referencia la información monitoreada en la
estación Sierra Gorda, se obtiene que, las velocidades del viento durante el período de
madrugada y noche alcanzan promedios diarios de 2,6 m/s, mientras que durante el mediodía y
tarde alcanzan promedios diarios máximos de 6,6 m/s, con vientos predominantes de
componente este Noreste y Suroeste.

Del modelo meteorológico, se obtiene que el modelo WRF (recomendado por la “Guía para el uso
de modelos de calidad del aire en el SEIA”), subestima las velocidades del viento horarios y
promedio diarios medidos en la estación Sierra Gorda, alcanzando velocidades máximas
promedio horarias no superan los 4,2 m/s, mientras que las velocidades máximas promedio
horarias medidas en superficie alcanzan los 6,6 m/s, por lo cual se utilizó un factor de corrección
que ajustara las concentraciones obtenidas por el modelo de dispersión. Respecto a la dirección
del viento, presenta un buen ajuste respecto de los datos observados, presentándose una
sobrestimación de vientos Nor Noroeste y subestimación de vientos Noreste. Por otra parte, el

modelo tiende a subestimar la intensidad de los vientos.

Del modelo de dispersión de emisiones atmosféricas, se obtiene que se ha seleccionado el
modelo CALPUFF, dado que es recomendado en la Guía para el Uso de Modelos de Calidad del
Aire en el SEIA, en la cual se recomienda el modelo tipo “puff” CALPUFF para proyectos, cuya
área de influencia es mayor a 5 km y cuyos contaminantes sean del tipo primario, es decir, cuyas

emisiones se emiten directamente al ambiente.

De las emisiones atmosféricas estimadas para el proyecto durante las fases de construcción,
operación y cierre, se ha modelado el año 2 de la fase de operación como peor escenario (misma
emisión obtenida para el año 3), puesto que durante dicha fase se generarán las máximas
emisiones de material particulado MP10 y MP2.5 del proyecto, infiriéndose así que los aportes en
concentración de contaminantes en los años 1 y 4 de la fase de operación y en la fase de
construcción y cierre serán menores a los obtenidos para el año 2 de la fase de operación.

De los resultados del modelo de dispersión, se observa que las concentraciones de material
particulado MP10 y MP2.5 obtenidas en el receptor sensible cercano al proyecto, se encuentran
muy por debajo de la norma. Tanto el valor obtenido directamente del modelo como el valor
corregido es inferior a 0,5 μm [3] /N, tanto para MP10 como para MP2.5 .

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 45

Cabe señalar que las emisiones generadas durante la fase de operación serán acotadas en el
tiempo y se generarán principalmente en el sector de las obras del proyecto, en el cual se ubica
el punto de máximo impacto (PMI), para MP10 como concentración anual y para MP2.5 como
concentración diaria y anual. Respecto del PMI para MP10 como concentración diaria, éste se
ubica a un costado del proyecto.

Al evaluar el cumplimiento de la normativa, se obtiene que las concentraciones obtenidas son
nulas (inferior a 0,5 μm [3] /N) en el receptor sensible cercano al proyecto tanto para MP10 como
para MP2.5, por tanto, pese a que no se cuenta con mediciones de calidad del aire en dicho
receptor, el aporte del proyecto no altera las condiciones de calidad del aire.

En base a lo anterior el proyecto no genera efectos adversos significativos sobre la salud de la
población cercana.

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 46

**Apéndice A**

# Desglose de emisiones ingresadas al modelo Calpuff

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 47

|Type|ID|Descripción|Área (m2)|Emisión (g/s-m2)|Col6|
|---|---|---|---|---|---|
|**Type**|**ID**|**Descripción**|**Área (m2) **|**MP10**|**MP2.5**|
|AREA_POLY|SRC_1|Área de extracción|443.960,70|2,24849E-06|1,52551E-06|
|AREA_POLY|SRC_2|Área de acopio|6.208,60|7,83460E-05|1,15710E-05|
|AREA_POLY|SRC_3|Planta de áridos|1.695,40|6,56024E-05|3,52009E-05|
|AREA|SRC_4|Camino de acceso|255,60|2,18348E-04|2,20393E-05|
|AREA|SRC_5|Camino de acceso|159,66|2,18348E-04|2,20393E-05|
|AREA|SRC_6|Camino de acceso|334,98|2,18348E-04|2,20393E-05|
|AREA|SRC_7|Camino de acceso|487,14|2,18348E-04|2,20393E-05|
|AREA_POLY|SRC_8|Planta de asfalto|905,00|4,76873E-04|4,49231E-04|
|AREA|SRC_9|Ruta Norte|12.978,66|6,29163E-07|2,00865E-07|
|AREA|SRC_10|Ruta Norte|8.996,64|6,29163E-07|2,00865E-07|
|AREA|SRC_11|Ruta Norte|781,38|6,29163E-07|2,00865E-07|
|AREA|SRC_12|Ruta Norte|7.026,24|6,29163E-07|2,00865E-07|
|AREA|SRC_13|Ruta Norte|1.150,80|6,29163E-07|2,00865E-07|
|AREA|SRC_14|Ruta Norte|5.985,90|6,29163E-07|2,00865E-07|
|AREA|SRC_15|Ruta Norte|2.083,38|6,29163E-07|2,00865E-07|
|AREA|SRC_16|Ruta Norte|975,18|6,29163E-07|2,00865E-07|
|AREA|SRC_17|Ruta Norte|13.099,38|6,29163E-07|2,00865E-07|
|AREA|SRC_18|Ruta Norte|923,28|6,29163E-07|2,00865E-07|
|AREA|SRC_19|Ruta Norte|7.584,42|6,29163E-07|2,00865E-07|
|AREA|SRC_20|Ruta Norte|3.330,78|6,29163E-07|2,00865E-07|
|AREA|SRC_21|Ruta Norte|793,56|6,29163E-07|2,00865E-07|
|AREA|SRC_22|Ruta Norte|1.067,34|6,29163E-07|2,00865E-07|
|AREA|SRC_23|Ruta Sur|11.914,50|7,07708E-07|2,23114E-07|
|AREA|SRC_24|Ruta Sur|6.773,04|7,07708E-07|2,23114E-07|
|AREA|SRC_25|Ruta Sur|6.027,66|7,07708E-07|2,23114E-07|
|AREA|SRC_26|Ruta Sur|15.574,26|7,07708E-07|2,23114E-07|
|AREA|SRC_27|Ruta Sur|1.685,88|7,07708E-07|2,23114E-07|

Adenda - Modelación Calidad del Aire
Proyecto Ampliación Extracción de Áridos y Planta de Asfaltos Sector Pozo D8
Marzo de 2020 Pág. 48