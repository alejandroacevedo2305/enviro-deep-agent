---
title: Sin título
author: jurbistondo
date: D:20190412120043-04'00'
language: es
type: report
pages: 77
has_toc: True
has_tables: True
extraction_quality: high
---

Declaración de Impacto Ambiental

“ Plan de Manejo de Sedimentos Central

Hidroeléctrica La Higuera ”

Adenda N°1

Anexo V-C. Modelación Dispersión de Contaminantes

Preparado por

Mayo 2019

Anexo V-C Modelación de Dispersión de Contaminantes

**INDICE**

**1.0** **INTRODUCCION ........................................................................................................................................................ 1**

**2.0** **OBJETIVOS ............................................................................................................................................................... 2**

2.1 Objetivo General ........................................................................................................................................... 2

2.2 Objetivos Específicos .................................................................................................................................... 2

**3.0** **NORMATIVA DE CALIDAD DE APLICABLE ............................................................................................................ 3**

**4.0** **CARACTERIZACION DEL AREA DE ESTUDIO ....................................................................................................... 4**

4.1 Localización ................................................................................................................................................... 4

**5.0** **PRESENTACIÓN DE DATOS UTILIZADOS ............................................................................................................. 5**

5.1 Descripción y Justificación del Modelo .......................................................................................................... 5

5.2 Receptores Considerados ............................................................................................................................. 5

5.3 Dominio de Modelación ................................................................................................................................. 6

5.4 Topografía ..................................................................................................................................................... 7

5.5 Uso de Suelo ................................................................................................................................................. 8

5.6 Fuentes de Emisión y Parámetros Utilizados en Modelación ........................................................................ 8

5.6.1 Fuentes de emisión ....................................................................................................................................... 8

**6.0** **LÍNEA BASE DE CLIMA Y METEOROLOGÍA ........................................................................................................ 12**

6.1 Caracterización climática regional ............................................................................................................... 12

6.1.1 Clima Templado cálido con estación seca prolongada de 8 a 7 meses ...................................................... 13

6.1.2 Clima Templado cálido con estación seca de 4 a 5 meses ......................................................................... 13

6.2 Presentación de datos meteorológicos observados .................................................................................... 13

6.2.1 Series de tiempo en la estación San Fernando ........................................................................................... 15

6.2.2 Ciclos diarios en la estación San Fernando ................................................................................................ 19

6.2.3 Rosa de los vientos estación San Fernando ............................................................................................... 23

6.2.4 Ciclos estacionales estación San Fernando ................................................................................................ 25

**7.0** **LÍNEA BASE DE CALIDAD DEL AIRE ................................................................................................................... 29**

7.1 Introducción ................................................................................................................................................. 29

7.2 Objetivos ..................................................................................................................................................... 29

7.3 Área de Influencia y área de Estudio ........................................................................................................... 29

7.4 Monitoreos disponibles. ............................................................................................................................... 30

7.5 Series de Tiempo ........................................................................................................................................ 32

7.5.1 Series de tiempo de concentraciones diarias de MP2.5 .............................................................................. 32

7.5.2 Series de tiempo de concentraciones diarias de MP10 ............................................................................... 33

7.5.3 Series de tiempo de concentraciones de 8 horas de O3 ............................................................................. 33

**i**

Anexo V-C Modelación de Dispersión de Contaminantes

7.6 Ciclos diarios ............................................................................................................................................... 34

7.7 Ciclos Estacionales ..................................................................................................................................... 36

7.8 Evaluación de normas de calidad de Aire ................................................................................................... 38

7.8.1 Evaluación de Normas de MP 10 .................................................................................................................. 38

7.8.2 Evaluación de Normas de MP 2.5 .................................................................................................................. 39

7.8.3 Evaluación de Normas de O3 ...................................................................................................................... 40

**8.0** **MODELACION DE CALIDAD DEL AIRE Y RESULTADOS .................................................................................... 42**

8.1 Aportes del Proyecto ................................................................................................................................... 42

8.2 Análisis de incertidumbre y determinación de factores de corrección de concentraciones

modeladas. .................................................................................................................................................. 54

8.2.1 Análisis de datos meteorológicos modelados con WRF v/s datos observacionales

disponibles para año 2018 ....................................................................................................................... 54

8.2.2 Análisis de incertidumbre. ........................................................................................................................... 60

8.2.3 Factores de corrección. ............................................................................................................................... 62

8.3 Aportes Corregidos del Proyecto ................................................................................................................. 63

8.4 Evaluación de Cumplimiento de Normativa ................................................................................................. 66

**9.0** **CONCLUSIONES ..................................................................................................................................................... 67**

**LISTADO DE TABLAS**

Tabla 3-1: Normativa de calidad aplicable al proyecto. ........................................................................................................ 3

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **3.0** **NORMATIVA DE CALIDAD DE APLICABLE** En la Tabla 3-1 se muestra la normativa de calidad del aire aplicable al proyecto. -->

**Tabla 3-1: Normativa de calidad aplicable al proyecto.****

| Tipo | Contaminante | Normativa | Estadígrafo | Límite |
| --- | --- | --- | --- | --- |
| **Tipo** | **Contaminante** | **Normativa** | **Estadígrafo** | **μg/m3N ** |
| **Norma Primaria** | **MP10** | MP10 (D.S. N°59/98 MINSEGPRES)(2) | Promedio diario, percentil 98 | 150 |
| **Norma Primaria** | **MP10** | MP10 (D.S. N°59/98 MINSEGPRES)(2) | Media aritmética anual | 50 |
| **Norma Primaria** | **MP2.5** | MP2.5 (D.S. N°12/11 MINSEGPRES) | Promedio diario, percentil 98 | 50 |
| **Norma Primaria** | **MP2.5** | MP2.5 (D.S. N°12/11 MINSEGPRES) | Media aritmética anual | 20 |
| **Norma Primaria** | **NO2 ** | NO2 (D.S. N°114/02 MINSEGPRES) | Máximo diario de 1 hora, percentil 99 | 400 |
| **Norma Primaria** | **NO2 ** | NO2 (D.S. N°114/02 MINSEGPRES) | Media aritmética anual | 100 |
| **Norma Primaria** | **SO2 ** | S.O2 (D.S. N°113/02 MINSEGPRES) | Promedio diario, percentil 99 | 250 |
| **Norma Primaria** | **SO2 ** | S.O2 (D.S. N°113/02 MINSEGPRES) | Media aritmética anual | 80 |
| **Norma Primaria** | **CO** | CO (D.S. N°115/02 MINSEGPRES) | Máximo diario de 1 hora, percentil 99 | 30.000 |
| **Norma Primaria** | **CO** | CO (D.S. N°115/02 MINSEGPRES) | Máximo diario de 8 hora, percentil 99 | 10.000 |

<!-- Estadísticas: 11 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia . **3** -->
<!-- FIN TABLA 3-1 -->


Tabla 5-1: Receptores puntuales considerados. .................................................................................................................. 6

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 5-1: Receptores puntuales considerados.****

| N° | Recepto | Coordenadas UTM Datum WGS84 (1) | Col4 |
| --- | --- | --- | --- |
| **N°** | **Recepto** | **Este (m)** | **Norte (m)** |
| 1 | Est. San Fernando | 317.503 | 6.171.746 |
| 2 | Puente Negro | 328.731 | 6.159.897 |
| 3 | La Rufina | 339.632 | 6.153.882 |
| 4 | Termas El Flaco | 368.824 | 6.130.717 |

<!-- Estadísticas: 5 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: Uso 19 Sur Fuente: Elaboración propia -->
<!-- FIN TABLA 5-1 -->


Tabla 5-2: Características del dominio de modelación. ....................................................................................................... 7

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **6** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 5-2: Características del dominio de modelación.****

| Descripción | Detalle |
| --- | --- |
| Tamaño de la grilla | 1 km x 1 km |
| Resolución horizontal y vertical del dominio | 64 km (Este - Oeste) x 49 km (Norte - Sur) |
| Número capas | 11 entre 0 y 4.000 m de altura |
| Coordenadas central de origen (UTM) | 345.196 m E y 6.151.543 m S, Datum WGS 84 |
| Área del dominio en km2 | 3.136 km2 |
| Topografía | Extraída de SRTM3 con resolución de 90 m |
| Usos de suelo | Extraídos de Global Land Cover Characterization (GLCC) del<br>US Geological Survey (UGS), EEUU, con resolución de 1 km. |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **5.4** **Topografía** -->
<!-- FIN TABLA 5-2 -->


Tabla 5-3: Emisiones Etapa de Operación. ......................................................................................................................... 9

<!-- INICIO TABLA 5-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **8** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 5-3: Emisiones Etapa de Operación.****

| Actividades | MP10 | MP2,5 | NOx | SO2 | CO | COV |
| --- | --- | --- | --- | --- | --- | --- |
| **Actividades** | **(ton/año)** | **(ton/año)** | **(ton/año)** | **(ton/año)** | **(ton/año)** | **(ton/año)** |
| **1. Circulación de vehículos por caminos**<br>**no pavimentados** | **10,892** | **1,089** | **0,000** | **0,000** | **0,000** | **0,000** |
| 1.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado) | 9,443 | 0,944 |  |  |  |  |
| 1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado) | 1,449 | 0,145 |  |  |  |  |
| **2. Circulación de vehículos por caminos**<br>**pavimentados** | **0,031** | **0,008** | **0,000** | **0,000** | **0,000** | **0,000** |
| 2.1 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado) | 0,011 | 0,003 |  |  |  |  |
| 2.2 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado) | 0,020 | 0,005 |  |  |  |  |
| **3. Combustión interna de motores de**<br>**vehículos** | **0,0015** | **0,0015** | **0,0479** | **0,0000** | **0,0140** | **0,0032** |
| 3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado) | 0,0006 | 0,0006 | 0,0123 | 0,0000 | 0,0041 | 0,0010 |
| 3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado) | 0,0006 | 0,0006 | 0,0241 | 0,0000 | 0,0069 | 0,0015 |
| 3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado) | 0,0001 | 0,0001 | 0,0020 | 0,0000 | 0,0007 | 0,0002 |
| 3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado) | 0,0002 | 0,0002 | 0,0094 | 0,0000 | 0,0023 | 0,0005 |
| **4. Combustión interna de motores de**<br>**maquinaria** | **0,380** | **0,380** | **4,963** | **0,000** | **1,037** | **0,467** |
| 4.1 Draga de succión Dragatec 300-350 | 0,243 | 0,243 | 3,171 | 0,000 | 0,662 | 0,298 |
| 4.2 Embarcación menor | 0,137 | 0,137 | 1,792 | 0,000 | 0,374 | 0,168 |
| **5. Combustión interna de motores de**<br>**generadores** | **0,013** | **0,013** | **0,180** | **0,012** | **0,039** | **0,000** |
| 5.1 Generador 25 KVA | 0,013 | 0,013 | 0,180 | 0,012 | 0,039 | 0,00 |
| **TOTAL** | **11,318** | **1,491** | **5,191** | **0,012** | **1,090** | **0,470** |

<!-- Estadísticas: 18 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. En la Tabla 5-4 se muestran las fuentes emisoras modeladas en Calpuff y las actividades emisoras consideradas. -->
<!-- FIN TABLA 5-3 -->


Tabla 5-4: Fuentes modeladas en Calpuff y actividades emisoras asociadas. .................................................................... 9

Tabla 5-5: Tasa de emisión de material particulado y fuente modelada asociada. ............................................................ 10

<!-- INICIO TABLA 5-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 5-5 a Tabla 5-6 se muestra la emisión mensual de las fuentes y la tasa de emisión calculada en gramos por segundo. La tasa de emisión se ha estimado considerado una jornada de 30 días al mes, 8 horas al día. Es importante señalar que la operación tendrá una duración de 5 meses al año, entre los meses de abril a agosto. -->

**Tabla 5-5: Tasa de emisión de material particulado y fuente modelada asociada.****

| Source<br>ID | Fuente | Actividades | MP10 | Col5 | Col6 | MP2.5 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Source**<br>**ID** | **Fuente** | **Actividades** | **ton/año** | **g/s** | **g/s/m2** | **ton/año** | **g/s** | **g/s/m2** |
| **SRC_1** | **Tramo 1 Puente**<br>**Negro - Pondaje**<br>**Tricahue PAV (No**<br>**Pavimentado)** | 1.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado) | 9,443 | 2,2E+00 |  | 0,944 | 2,2E-01 |  |
| **SRC_1** | **Tramo 1 Puente**<br>**Negro - Pondaje**<br>**Tricahue PAV (No**<br>**Pavimentado)** | 3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado) | 0,001 | 1,4E-04 |  | 0,001 | 1,4E-04 |  |
| **SRC_1** | **Tramo**<br>**2 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(No**<br>**Pavimentado)** | 1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado) | 1,449 | 3,4E-01 |  | 0,145 | 3,4E-02 |  |
| **SRC_1** | **Tramo**<br>**2 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(No**<br>**Pavimentado)** | 3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado) | 0,001 | 1,5E-04 |  | 0,001 | 1,5E-04 |  |
| **SRC_1** | **Tramo**<br>**2 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(No**<br>**Pavimentado)** | **Sub Total:** | **10,893** | **2,52E+00** | **6,0E-06** | **1,090** | **2,52E-01** | **6,0E-07** |
| **SRC_2** | **Tramo 3 Puente**<br>**Negro - Pondaje**<br>**Tricahue**<br>**PAV**<br>**(Pavimentado)** | 2.1 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado) | 0,011 | 2,6E-03 |  | 0,003 | 6,2E-04 |  |
| **SRC_2** | **Tramo 3 Puente**<br>**Negro - Pondaje**<br>**Tricahue**<br>**PAV**<br>**(Pavimentado)** | 3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado) | 0,000 | 2,3E-05 |  | 0,000 | 2,3E-05 |  |
| **SRC_2** | **Tramo 3 Puente**<br>**Negro - Pondaje**<br>**Tricahue**<br>**PAV**<br>**(Pavimentado)** | **Sub Total:** | **0,011** | **2,59E-03** | **8,1E-08** | **0,003** | **6,44E-04** | **2,0E-08** |
| **SRC_3** | **Tramo**<br>**4 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(Pavimentado)** | 2.2 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado) | 0,020 | 4,7E-03 |  | 0,005 | 1,1E-03 |  |
| **SRC_3** | **Tramo**<br>**4 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(Pavimentado)** | 3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado) | 0,000 | 4,8E-05 |  | 0,000 | 4,8E-05 |  |
| **SRC_3** | **Tramo**<br>**4 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(Pavimentado)** | **Sub Total:** | **0,020** | **4,72E-03** | **2,1E-08** | **0,005** | **1,18E-03** | **5,2E-09** |
| **SRC_4** | **Pondaje Tricahue** | 4.1 Draga de succión Dragatec 300-<br>350 | 0,243 | 5,6E-02 |  | 0,243 | 5,6E-02 |  |
| **SRC_4** | **Pondaje Tricahue** | 4.2 Embarcación menor | 0,137 | 3,2E-02 |  | 0,137 | 3,2E-02 |  |
| **SRC_4** | **Pondaje Tricahue** | 5.1 Generador 25 KVA | 0,013 | 3,0E-03 |  | 0,013 | 3,0E-03 |  |
| **SRC_4** | **Pondaje Tricahue** | **Sub Total:** | **0,393** | **9,10E-02** | **2,7E-06** | **0,393** | **9,10E-02** | **2,7E-06** |
|  |  |  | **11,318** |  | **8,8E-06** | **1,491** |  | **3,3E-06** |

<!-- Estadísticas: 17 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **10** -->
<!-- FIN TABLA 5-5 -->


Tabla 5-6: Tasa de emisión de gases y fuente modelada asociada. ................................................................................. 11

Tabla 6-1: Coordenadas y variables medidas en estaciones meteorológicas ................................................................... 14

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **13** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 6-1: Coordenadas y variables medidas en estaciones meteorológicas****

| N° | Receptor | Coordenadas UTM Datum<br>WGS84 (1) | Col4 | Uso | Distancia a<br>Proyecto | Información<br>meteorológica (2) |
| --- | --- | --- | --- | --- | --- | --- |
| **N°** | **Receptor** | **Norte (m)** | **Este (m)** | **Este (m)** | **Km** | **Km** |
| 1 | Estación San Fernando | 6.171.746 | 317.503 | 19H | 31,8 | VV, DV, Temp.,<br>HR, RS, PA |
| 2 | Estación El Tambo | 6.183.828 | 317.515 | 19H | 40,,1 | PP |

<!-- Estadísticas: 3 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 2: Velocidad del Viento (VV), Dirección del Viento (DV), Temperatura (Temp.), Humedad Relativa (HR), Radiación Solar (RS), Presión Atmosférica (PA), PP: Precipitación diaria Fuente: Elaboración propia. -->
<!-- FIN TABLA 6-1 -->


Tabla 6-2 Resumen de datos horarios válidos disponibles, estación San Fernando-2018 ................................................ 15

Tabla 7-1: Estación de Monitoreo y Variables Medida para período 2007 - 2018 ............................................................. 30

<!-- INICIO TABLA 7-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 7-1. Área de estudio y Estación de monitoreo** Fuente: Elaboración propia -->

**Tabla 7-1: Estación de Monitoreo y Variables Medida para período 2007 - 2018****

| N° | Receptor | Coordenadas* | Col4 | Distancia<br>al Proyecto<br>(km) | Monitoreos Disponibles** | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **N°** | **Receptor** | **Norte (m)** | **Este (m)** | **Este (m)** | **Variables** | **Período con datos** |
| 1 | San Fernando | 6.171.746 | 317.503 | 31.8 | MP10 | 01/04/2007 - 11/01/2019 |
| 1 | San Fernando | 6.171.746 | 317.503 | 31.8 | MP2.5 | 23/03/2016 - 11/01/2019 |
| 1 | San Fernando | 6.171.746 | 317.503 | 31.8 | O3 | 01/04/2007 - 11/01/2019 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- - UTM, Datum WGS 84, Huso 19 H. ** La estación está conectada en línea con datos actualizados hasta la fecha del informe, la fecha final de datos disponibles -->
<!-- FIN TABLA 7-1 -->


Tabla 7-2: Estación San Fernando - resumen registros válidos de MP2,5 ....................................................................... 31

<!-- INICIO TABLA 7-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- monitores los cuales si están considerados al calcular los registros válidos anuales. Por otra parte, para el análisis de los datos se consideraron las normas de calidad de aire vigentes en Chile cuyos valores límites se presentan en la Tabla 7-5. -->

**Tabla 7-2: Estación San Fernando - resumen registros válidos de MP2,5****

| Estación | Año | N° de<br>Registros | N°<br>Registros<br>Válidos | %<br>Registros<br>Válidos | % de<br>Registros<br>Válidos<br>Anuales | Concentraciones de 24<br>horas de MP2,5 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <br> <br>**Estación** | **Año** | **N° de**<br>**Registros** | **N°**<br>**Registros**<br>**Válidos** | **% **<br>**Registros**<br>**Válidos** | **% de**<br>**Registros**<br>**Válidos**<br>**Anuales** | **Min**<br>**μg/m3** | **Max**<br>**μg/m3** | **Prom**<br>**μg/m3** |
| San Fernando | 2015 | -- | -- | -- | -- | -- | -- | -- |
| San Fernando | 2016 | 279 | 255 | 91,4% | 69,7% | 6 | 117 | 30 |
| San Fernando | 2017 | 363 | 354 | 97,5% | 97,0% | 3 | 82 | 21 |
| San Fernando | 2018 | 358 | 346 | 96,6% | 94,8% | 3 | 89 | 18 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 7-3: Estación San Fernando - resumen registros válidos de MP10** |Estación|Año|N° de<br>Registros|N°<br>Registros<br>Válidos|%<br>Registros<br>Válidos|% de<br>Registros<br>Válidos<br>Anuales|Concentraciones de 24<br>horas de MP10|Col8|Col9| |---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 7-2 -->


Tabla 7-3: Estación San Fernando - resumen registros válidos de MP10 ........................................................................ 31

<!-- INICIO TABLA 7-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |San Fernando|2015|--|--|--|--|--|--|--| |San Fernando|2016|279|255|91,4%|69,7%|6|117|30| |San Fernando|2017|363|354|97,5%|97,0%|3|82|21| |San Fernando|2018|358|346|96,6%|94,8%|3|89|18| -->

**Tabla 7-3: Estación San Fernando - resumen registros válidos de MP10****

| Estación | Año | N° de<br>Registros | N°<br>Registros<br>Válidos | %<br>Registros<br>Válidos | % de<br>Registros<br>Válidos<br>Anuales | Concentraciones de 24<br>horas de MP10 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <br> <br>**Estación** | **Año** | **N° de**<br>**Registros** | **N°**<br>**Registros**<br>**Válidos** | **% **<br>**Registros**<br>**Válidos** | **% de**<br>**Registros**<br>**Válidos**<br>**Anuales** | **Min**<br>**μg/m3** | **Max**<br>**μg/m3** | **Prom**<br>**μg/m3** |
| San Fernando | 2015 | 363 | 357 | 98,3% | 97,8% | 10 | 183 | 47 |
| San Fernando | 2016 | 366 | 364 | 99,5% | 99,5% | 10 | 156 | 45 |
| San Fernando | 2017 | 364 | 355 | 97,5% | 97,3% | 10 | 107 | 39 |
| San Fernando | 2018 | 359 | 348 | 96,9% | 95,3% | 9 | 132 | 40 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 7-4: Estación San Fernando - resumen registros válidos de O3** |Estación|Año|N° de<br>Registros|N°<br>Registros<br>Válidos|%<br>Registros<br>Válidos|% de<br>Registros<br>Válidos<br>Anuales|Concentraciones de 8h<br>Máximas diarias de O3|Col8|Col9| |---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 7-3 -->


Tabla 7-4: Estación San Fernando - resumen registros válidos de O3 ............................................................................. 31

<!-- INICIO TABLA 7-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |San Fernando|2015|363|357|98,3%|97,8%|10|183|47| |San Fernando|2016|366|364|99,5%|99,5%|10|156|45| |San Fernando|2017|364|355|97,5%|97,3%|10|107|39| |San Fernando|2018|359|348|96,9%|95,3%|9|132|40| -->

**Tabla 7-4: Estación San Fernando - resumen registros válidos de O3****

| Estación | Año | N° de<br>Registros | N°<br>Registros<br>Válidos | %<br>Registros<br>Válidos | % de<br>Registros<br>Válidos<br>Anuales | Concentraciones de 8h<br>Máximas diarias de O3 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <br> <br>**Estación** | **Año** | **N° de**<br>**Registros** | **N°**<br>**Registros**<br>**Válidos** | **% **<br>**Registros**<br>**Válidos** | **% de**<br>**Registros**<br>**Válidos**<br>**Anuales** | **Min**<br>**μg/m3** | **Max**<br>**μg/m3** | **Prom**<br>**μg/m3** |
| San Fernando | 2015 | 365 | 365 | 100,0% | 100,0% | 2,0 | 117,9 | 28,00 |
| San Fernando | 2016 | 366 | 365 | 99,7% | 99,7% | 2,0 | 84,7 | 20,91 |
| San Fernando | 2017 | 365 | 363 | 99,5% | 99,5% | 2,0 | 116,5 | 27,69 |
| San Fernando | 2018 | 360 | 339 | 94,2% | 92,9% | 1,7 | 92,4 | 28,08 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **31** Anexo V-C Modelación de Dispersión de Contaminantes -->
<!-- FIN TABLA 7-4 -->


Tabla 7-5: Normativa de referencia para la Línea de Base ................................................................................................ 32

<!-- INICIO TABLA 7-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **31** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 7-5: Normativa de referencia para la Línea de Base****

| Contaminante | Normativa | Estadígrafo | Valor límite |
| --- | --- | --- | --- |
| MP10 | MP10 (D.S. N° 59/1998, MINSEGPRES.) | Promedio diario, percentil 98 | 150 μg/m3N |
| MP10 | MP10 (D.S. N° 59/1998, MINSEGPRES.) | Media aritmética anual | 50 μg/m3N |
| MP2.5 | MP2.5 (D.S. N° 12/2011, MINSEGPRES.) | Promedio diario, percentil 98 | 50 μg/m3 |
| MP2.5 | MP2.5 (D.S. N° 12/2011, MINSEGPRES.) | Media aritmética anual | 20 μg/m3 |
| O3 | O3 (D.S. N°112/2002, MINSEGPRES.) | Máx diario de 8 horas, percentil 99 | 120 μg/m3 |

<!-- Estadísticas: 5 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **7.5** **Series de Tiempo** -->
<!-- FIN TABLA 7-5 -->


Tabla 7-6: Monitoreo Aire MP10, Estación San Fernando, Periodo 2015 - 2018 .............................................................. 39

<!-- INICIO TABLA 7-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **38** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 7-6: Monitoreo Aire MP10, Estación San Fernando, Periodo 2015 - 2018****

| Estación | Año | % de<br>Registros<br>Válidos<br>Anuales | Norma Primaria MP10 (μg/m3N) | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Año** | **% de**<br>**Registros**<br>**Válidos**<br>**Anuales** | **Norma Diaria** | **Norma Diaria** | **Norma Diaria** | **Norma Diaria** | **Norma Anual** | **Norma Anual** | **Norma Anual** |
| **Estación** | **Año** | **% de**<br>**Registros**<br>**Válidos**<br>**Anuales** | **Concent**<br>**24h**<br>**Mínimo** | **Concent**<br>**24h**<br>**Máximo** | **Concent**<br>**24h,**<br>**P98** | **% Norma** | **Promedio**<br>**Anual** | **Promedio**<br>**Trianual** | **% **<br>**Norma** |
| **San Fernando** | 2015 | 97,8% | 10 | 183 | 112 | 75% | 47 |  |  |
| **San Fernando** | 2016 | 99,5% | 10 | 156 | 115 | 77% | 44 |  |  |
| **San Fernando** | 2017 | 97,3% | 10 | 107 | 92 | 61% | 39 | 43 | 87% |
| **San Fernando** | 2018 | 95,3% | 9 | 132 | 100 | 67% | 40 | 41 | 82% |
| Límite Máximo Permisible<br>**150μg/m3N Percentil 98** | Límite Máximo Permisible<br>**150μg/m3N Percentil 98** | Límite Máximo Permisible<br>**150μg/m3N Percentil 98** | Límite Máximo Permisible<br>**150μg/m3N Percentil 98** | Límite Máximo Permisible<br>**150μg/m3N Percentil 98** | Límite Máximo Permisible<br>**150μg/m3N Percentil 98** | Límite Máximo Permisible<br>**150μg/m3N Percentil 98** | **50μg/m3N Promedio 3 años** | **50μg/m3N Promedio 3 años** | **50μg/m3N Promedio 3 años** |
| 80% de Norma<br>**120μg/m3N** | 80% de Norma<br>**120μg/m3N** | 80% de Norma<br>**120μg/m3N** | 80% de Norma<br>**120μg/m3N** | 80% de Norma<br>**120μg/m3N** | 80% de Norma<br>**120μg/m3N** | 80% de Norma<br>**120μg/m3N** | **40μg/m3N** | **40μg/m3N** | **40μg/m3N** |

<!-- Estadísticas: 8 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia con datos de SINCA y SMA. La Figura 7-11 resume el cumplimiento de la norma diaria y de la norma anual de MP10. -->
<!-- FIN TABLA 7-6 -->


Tabla 7-7: Monitoreo Aire MP2.5 Estación San Fernando, Periodo 2016 - 2018 .............................................................. 40

<!-- INICIO TABLA 7-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **39** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 7-7: Monitoreo Aire MP2.5 Estación San Fernando, Periodo 2016 - 2018****

| Estación | Año | % de<br>Registros<br>Válidos<br>Anuales | Norma Primaria MP2.5 (μg/m3) | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Año** | **% de**<br>**Registros**<br>**Válidos**<br>**Anuales** | **Norma Diaria** | **Norma Diaria** | **Norma Diaria** | **Norma Diaria** | **Norma Anual** | **Norma Anual** | **Norma Anual** |
| **Estación** | **Año** | **% de**<br>**Registros**<br>**Válidos**<br>**Anuales** | **Concent**<br>**24h**<br>**Mínimo** | **Concent**<br>**24h**<br>**Máximo** | **Concent**<br>**24h,**<br>**P98** | **% Norma** | **Promedio**<br>**Anual** | **Promedio**<br>**Trianual** | <br>**% **<br>**Norma** |
| **San**<br>**Fernando** | 2016 | 69,7% | 6 | 117 | 101 | 202% | 301 |  |  |
| **San**<br>**Fernando** | 2017 | 97,0% | 3 | 82 | 70 | 140% | 21 |  |  |
| **San**<br>**Fernando** | 2018 | 94,8% | 3 | 89 | 63 | 126% | 18 | 19,52 | 98% |
| Límite Máximo Permisible<br>**50μg/m3 Percentil 98** | Límite Máximo Permisible<br>**50μg/m3 Percentil 98** | Límite Máximo Permisible<br>**50μg/m3 Percentil 98** | Límite Máximo Permisible<br>**50μg/m3 Percentil 98** | Límite Máximo Permisible<br>**50μg/m3 Percentil 98** | Límite Máximo Permisible<br>**50μg/m3 Percentil 98** | Límite Máximo Permisible<br>**50μg/m3 Percentil 98** | **20μg/m3N Promedio 3 años** | **20μg/m3N Promedio 3 años** | **20μg/m3N Promedio 3 años** |
| 80% de Norma<br>**40** **μg/m3N** | 80% de Norma<br>**40** **μg/m3N** | 80% de Norma<br>**40** **μg/m3N** | 80% de Norma<br>**40** **μg/m3N** | 80% de Norma<br>**40** **μg/m3N** | 80% de Norma<br>**40** **μg/m3N** | 80% de Norma<br>**40** **μg/m3N** | **16** **μg/m3** | **16** **μg/m3** | **16** **μg/m3** |

<!-- Estadísticas: 7 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- 1 Promedio anual inválido por tener menos de 9 meses válidos, solo hay 8 (abril a diciembre) 2 Promedio trianual solo de carácter referencial con promedios de años 2017 y 2018 -->
<!-- FIN TABLA 7-7 -->


Tabla 7-8: Monitoreo Aire O3, Est. San Fernando, Periodo 2015 - 2018 .......................................................................... 41

<!-- INICIO TABLA 7-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **40** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 7-8: Monitoreo Aire O3, Est. San Fernando, Periodo 2015 - 2018****

| Estación | Año | % de<br>Registros<br>Válidos<br>Anuales | Norma Primaria O3 (μg/m3N) | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Estación | Año | % de<br>Registros<br>Válidos<br>Anuales | Norma 8 horas | Norma 8 horas | Norma 8 horas | Norma 8 horas | Norma 8 horas |
| Estación | Año | % de<br>Registros<br>Válidos<br>Anuales | Concent<br>8horas<br>Mínimo | Concent<br>8horas<br>Máximo | Concent<br>8horas,<br>P99 | Promedio<br>Trianual | % <br>Norma |
| **San**<br>**Fernando** | 2015 | 100,0% | 2,0 | 117,9 | 105,4 | -- | -- |
| **San**<br>**Fernando** | 2016 | 99,7% | 2,0 | 84,7 | 81,5 | -- | -- |
| **San**<br>**Fernando** | 2017 | 99,5% | 2,0 | 116,5 | 101,5 | 96,13 | 80% |
| **San**<br>**Fernando** | 2018 | 92,9% | 1,7 | 92,4 | 89,2 | 90,71 | 76% |
| Límite Máximo Permisible<br>**120 μg/m3N Percentil 99** | Límite Máximo Permisible<br>**120 μg/m3N Percentil 99** | Límite Máximo Permisible<br>**120 μg/m3N Percentil 99** | Límite Máximo Permisible<br>**120 μg/m3N Percentil 99** | Límite Máximo Permisible<br>**120 μg/m3N Percentil 99** | Límite Máximo Permisible<br>**120 μg/m3N Percentil 99** | Límite Máximo Permisible<br>**120 μg/m3N Percentil 99** | Límite Máximo Permisible<br>**120 μg/m3N Percentil 99** |
| 80% de Norma<br>**96 μg/m3N** | 80% de Norma<br>**96 μg/m3N** | 80% de Norma<br>**96 μg/m3N** | 80% de Norma<br>**96 μg/m3N** | 80% de Norma<br>**96 μg/m3N** | 80% de Norma<br>**96 μg/m3N** | 80% de Norma<br>**96 μg/m3N** | 80% de Norma<br>**96 μg/m3N** |

<!-- Estadísticas: 8 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia con datos de SINCA. La Figura 7-13 resume el cumplimiento de la norma de 8 horas de O3 para la estación San Fernando. -->
<!-- FIN TABLA 7-8 -->


**ii**

Anexo V-C Modelación de Dispersión de Contaminantes

Tabla 8-1: Aporte del Proyecto en los receptores puntuales y punto de máximo aporte (PMA) ........................................ 43

<!-- INICIO TABLA 8-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **42** Anexo V-C Modelación de Dispersión de Contaminantes -->

**Tabla 8-1: Aporte del Proyecto en los receptores puntuales y punto de máximo aporte (PMA)****

| Tipo | Cont. | Estadígrafo | Límite | Est. San<br>Fernando | Col6 | Puente Negro | Col8 | La Rufina | Col10 | Termas El<br>Flaco | Col12 | Punto de<br>Máximo<br>Aporte (PMA) | Col14 | Nota |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **Cont.** | **Estadígrafo** | **μg/m3 ** | **μg/m3 ** | **% **<br>**norma** | **μg/m3 ** | **% **<br>**norma** | **μg/m3 ** | **% **<br>**norma** | **μg/m3 ** | **% **<br>**norma** | **μg/m3 ** | **% **<br>**norma** | **% **<br>**norma** |
| **Norma Primaria de Calidad del**<br>**Aire** | MP10 | 24 horas, P98 | 150 | 0,0 | 0% | 0,2 | 0% | 0,6 | 0% | 0,0 | 0% | 5,4 | 4% | 1 |
| **Norma Primaria de Calidad del**<br>**Aire** | MP10 | Anual | 50 | 0,0 | 0% | 0,0 | 0% | 0,1 | 0% | 0,0 | 0% | 0,8 | 2% | 2 |
| **Norma Primaria de Calidad del**<br>**Aire** | MP2.5 | 24 horas, P98 | 50 | 0,0 | 0% | 0,0 | 0% | 0,1 | 0% | 0,0 | 0% | 0,5 | 1% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | MP2.5 | Anual | 20 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,1 | 0% | 1 |
| **Norma Primaria de Calidad del**<br>**Aire** | NO2 | 1 hora, P99 | 400 | 0,0 | 0% | 0,0 | 0% | 0,1 | 0% | 0,1 | 0% | 25,7 | 6% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | NO2 | Anual | 100 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,8 | 1% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | SO2 | 24 horas, P99 | 250 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | SO2 | Anual | 80 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | CO | 1 hora, P99 | 30.000 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 5,4 | 0% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | CO | 8 horas, P99 | 10.000 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 3,5 | 0% | 3 |

<!-- Estadísticas: 11 filas, 15 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: El punto de máximo aporte (PMA) se ubica en el camino no pavimentado a 2,5 km al Sur Este de La Rufina, en UTM: 341.798 m Este, 6.152.539 m Sur. Nota 2: El punto de máximo aporte (PMA) se ubica cerca del camino no pavimentado a 1,7 km al Sur Este de Puente Negro, en UTM: 329.789 m Este, 6.158.539 m Sur. -->
<!-- FIN TABLA 8-1 -->


Tabla 8-2: Diferencia entre intensidad del viento observada y modelada en Estación San Fernando, año

<!-- INICIO TABLA 8-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- están dentro de los rangos esperados para este tipo de modelaciones. Considerando el promedio del año 2018, el modelo sobre estima la intensidad del viento, tanto en el período diurno como nocturno, siendo más alta la sobrestimación durante la noche que corresponde al período del día cuando la intensidad del viento disminuye. -->

**Tabla 8-2: Diferencia entre intensidad del viento observada y modelada en Estación San****

| Estación | Observado<br>(m/s) | Modelado (WRF)<br>(m/s) | Diferencia Mod-Obs<br>(m/s) | Variación Porcentual<br>% |
| --- | --- | --- | --- | --- |
| San Fernando | 1,70 | 2,52 | 0,82 | 48,0% |
| San Fernando diurno | 2,00 | 2,83 | 0,82 | 41,0% |
| San Fernando nocturno | 1,40 | 2,21 | 0,81 | 58,0% |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia En la Tabla 8-3, se analiza la diferencia del viento modelado con WRF respecto al observado para la Estación San Fernando, en función de su dirección, para lo cual se ha dividido la rosa de los vientos -->
<!-- FIN TABLA 8-2 -->


2018 .................................................................................................................................................................. 61

Tabla 8-3: Diferencia de intensidad del viento observada y modelada en Estación San Fernando por

<!-- INICIO TABLA 8-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **61** Anexo V-C - Modelación de Dispersión de Contaminantes -->

**Tabla 8-3: Diferencia de intensidad del viento observada y modelada en Estación San****

| Dirección<br>viento<br>(grados) | Diurno | Col3 | Col4 | Col5 | Nocturno | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección**<br>**viento**<br>**(grados)** | Observado<br>(m/s) | WRF<br>(m/s) | Diferencia<br>(m/s) | Variación<br>Porcentual<br>% | Observado<br>(m/s) | WRF<br>(m/s) | Diferencia<br>(m/s) | Variación<br>Porcentual<br>% |
| 0-90 | 1,06 | 3,48 | 2,42 | 227,1% | 0,83 | 2,21 | 1,38 | 165,2% |
| 90-180 | 2,07 | 1,34 | -0,73 | -35,4% | 1,56 | 1,16 | -0,40 | -25,5% |
| 180-270 | 2,08 | 2,80 | 0,73 | 35,0% | 1,43 | 2,50 | 1,07 | 74,9% |
| 270-360 | 2,28 | 3,47 | 1,19 | 52,0% | 0,94 | 2,34 | 1,40 | 148,5% |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia **8.2.3** **Factores de corrección.** -->
<!-- FIN TABLA 8-3 -->


dirección, año 2018 ........................................................................................................................................... 62

Tabla 8-4: Factor de corrección (FC) calculado de la diferencia de intensidad del viento en Estación San

<!-- INICIO TABLA 8-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Aplicando la Ecuación 2, a los datos de la Tabla 8-3 de la Estación San Fernando, se obtienen los factores de corrección de intensidad del viento y concentración de la Tabla 8-4, en cual corresponde a un factor de 1,80. Es decir un aumento en 180% del impacto modelado. -->

**Tabla 8-4: Factor de corrección (FC) calculado de la diferencia de intensidad del viento en****

| Dirección<br>viento<br>(grados) | Diurno | Col3 | Col4 | Nocturno | Col6 | Col7 | Factor Correción |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección**<br>**viento**<br>**(grados)** | **Observado**<br>**(Vobs) ** | **WRF**<br>**(VWRF) ** | **Factor de**<br>**Corrección**<br>**(VWRF/Vobs) ** | **Observado** | **WRF** | **Factor de**<br>**Corrección**<br>**(VWRF/Vobs) ** | **Promedio**<br>**(nocturno y**<br>**diurno)** |
| **Dirección**<br>**viento**<br>**(grados)** | **(m/s)** | **(m/s)** | **(m/s)** | **(m/s)** | **(m/s)** | **(m/s)** | **m/s** |
| 0-90 | 1,06 | 3,48 | 3,27 | 0,83 | 2,21 | 2,65 | 2,96 |
| 90-180 | 2,07 | 1,34 | 0,65 | 1,56 | 1,16 | 0,75 | 0,70 |
| 180-270 | 2,08 | 2,80 | 1,35 | 1,43 | 2,50 | 1,75 | 1,55 |
| 270-360 | 2,28 | 3,47 | 1,52 | 0,94 | 2,34 | 2,49 | 2,00 |
| **Promedio (Factor Corrección Calpuff) :** | **Promedio (Factor Corrección Calpuff) :** | **Promedio (Factor Corrección Calpuff) :** | **Promedio (Factor Corrección Calpuff) :** | **Promedio (Factor Corrección Calpuff) :** | **Promedio (Factor Corrección Calpuff) :** | **Promedio (Factor Corrección Calpuff) :** | **1,80** |

<!-- Estadísticas: 7 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia **8.3** **Aportes Corregidos del Proyecto** -->
<!-- FIN TABLA 8-4 -->


Fernando, año 2018 .......................................................................................................................................... 63

Tabla 8-5: Aporte corregido del Proyecto en los receptores puntuales y punto de máximo aporte (PMA) ........................ 65

<!-- INICIO TABLA 8-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **64** Anexo V-C - Modelación de Dispersión de Contaminantes -->

**Tabla 8-5: Aporte corregido del Proyecto en los receptores puntuales y punto de máximo aporte (PMA)****

| Tipo | Contaminante | Estadígrafo | Límite | Est. San<br>Fernando | Col6 | Puente Negro | Col8 | La Rufina | Col10 | Termas El<br>Flaco | Col12 | Punto de<br>Máximo<br>Aporte (PMA) | Col14 | Nota |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **Contaminante** | **Estadígrafo** | **μg/m3 ** | **μg/m3 ** | **% **<br>**norma** | **μg/m3 ** | **% **<br>**norma** | **μg/m3 ** | **% **<br>**norma** | **μg/m3 ** | **% **<br>**norma** | **μg/m3 ** | **% **<br>**norma** | **% **<br>**norma** |
| **Norma Primaria de Calidad del**<br>**Aire** | MP10 | 24 horas, P98 | 150 | 0,0 | 0% | 0,4 | 0% | 1,1 | 1% | 0,0 | 0% | 9,8 | 7% | 1 |
| **Norma Primaria de Calidad del**<br>**Aire** | MP10 | Anual | 50 | 0,0 | 0% | 0,0 | 0% | 0,2 | 0% | 0,0 | 0% | 1,4 | 3% | 2 |
| **Norma Primaria de Calidad del**<br>**Aire** | MP2.5 | 24 horas, P98 | 50 | 0,0 | 0% | 0,0 | 0% | 0,1 | 0% | 0,0 | 0% | 1,0 | 2% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | MP2.5 | Anual | 20 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,1 | 1% | 1 |
| **Norma Primaria de Calidad del**<br>**Aire** | NO2 | 1 hora, P99 | 400 | 0,0 | 0% | 0,0 | 0% | 0,1 | 0% | 0,1 | 0% | 46,3 | 12% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | NO2 | Anual | 100 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 1,5 | 1% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | SO2 | 24 horas, P99 | 250 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | SO2 | Anual | 80 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | CO | 1 hora, P99 | 30.000 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 9,8 | 0% | 3 |
| **Norma Primaria de Calidad del**<br>**Aire** | CO | 8 horas, P99 | 10.000 | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 0,0 | 0% | 6,4 | 0% | 3 |

<!-- Estadísticas: 11 filas, 15 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: El punto de máximo aporte (PMA) se ubica en el camino no pavimentado a 2,5 km al Sur Este de La Rufina, en UTM: 341.798 m Este, 6.152.539 m Sur. Nota 2: El punto de máximo aporte (PMA) se ubica cerca del camino no pavimentado a 1,7 km al Sur Este de Puente Negro, en UTM: 329.789 m Este, 6.158.539 m Sur. -->
<!-- FIN TABLA 8-5 -->


Tabla 8-6: Cumplimiento de normativa en estación San Fernando ................................................................................... 66

**LISTADO DE FIGURAS**

Figura 4-1 Localización del Proyecto ................................................................................................................................... 4

Figura 5-1 Dominio de modelación y receptores puntuales considerados ........................................................................... 6

Figura 5-2 Topografía del dominio de modelación ............................................................................................................... 7

Figura 5-3 Uso de Suelo ...................................................................................................................................................... 8

Figura 6-1 Clasificación del clima según Köppen .............................................................................................................. 12

Figura 6-2 Ubicación de estaciones meteorológicas San Fernando y El Tambo ............................................................... 14

Figura 6-3 Serie de registros horarios de velocidad del viento, Est. San Fernando, año 2018 .......................................... 15

Figura 6-4 Serie de registros horarios de dirección del viento, Est. San Fernando - 2018 ................................................ 16

Figura 6-5 Serie de tiempo para registros horarios de temperatura, Est. San Fernando - 2018 ........................................ 16

Figura 6-6 Serie de tiempo para registros horarios de humedad relativa, Est. San Fernando-2018.................................. 17

Figura 6-7 Serie de tiempo para registros horarios de Radiación Solar, Est. San Fernando-2018 .................................... 18

Figura 6-8 Serie de tiempo para registros horarios de Presión Atmosférica, Est. San Fernando-2016 ............................. 18

Figura 6-9 Serie de tiempo para registros diarios de precipitación, El Tambo - año 2018 ................................................. 19

Figura 6-10 Ciclo diario de los promedios horarios de la velocidad del viento, Est. San Fernando, año

2018 .................................................................................................................................................................. 20

Figura 6-11 Ciclo diurno de la dirección del viento, porcentaje de ocurrencia, Est. San Fernando, año

2018. ................................................................................................................................................................. 20

Figura 6-12 Ciclo diario de los promedios horarios de la temperatura, Est. San Fernando - 2018 ................................... 21

Figura 6-13 Ciclo diario de los promedios horarios de la hum. relativa, Est. San Fernando - 2018 .................................. 22

Figura 6-14 Ciclo diario de los promedios horarios de Radiación Solar, Est. San Fernando - 2018 ................................. 22

Figura 6-15 Ciclo diario de los promedios horarios de Presión Atmosférica, Est. San Fernando - 2016 .......................... 23

Figura 6-16 Rosa del viento, ciclo diario, Est. San Fernando, año 2018. .......................................................................... 24

Figura 6-17 Rosa del viento, Est. San Fernando, año 2018. ............................................................................................. 25

Figura 6-18 Ciclo estacional del Viento, Estación San Fernando - 2018 ........................................................................... 26

Figura 6-19 Ciclo estacional de Temperatura, Estación San Fernando - 2018 .................................................................. 26

Figura 6-20 Ciclo estacional de Humedad Relativa, Estación San Fernando - 2018 ........................................................ 27

**iii**

Anexo V-C Modelación de Dispersión de Contaminantes

Figura 6-21 Ciclo estacional de Radiación Solar, Estación San Fernando - 2018 ............................................................ 28

Figura 6-22 Ciclo estacional de Presión Atmosférica, Estación San Fernando - 2016 ..................................................... 28

Figura 7-1. Área de estudio y Estación de monitoreo ........................................................................................................ 30

Figura 7-2. Serie de concentraciones diarias de MP2.5, San Fernando 2015 - 2018 ....................................................... 33

Figura 7-3. Serie de concentraciones diarias de MP10, San Fernando 2015 - 2018 ........................................................ 33

Figura 7-4. Serie de concentraciones de 8 horas máximas de O3, San Fernando - 2015 a 2018 .................................... 34

Figura 7-5 Ciclo diario de MP2.5, Estación San Fernando - 2018 .................................................................................... 35

Figura 7-6 Ciclo diario de MP10, Estación San Fernando - 2018 ..................................................................................... 35

Figura 7-7 Ciclo diario de O3, Estación San Fernando - 2018 .......................................................................................... 36

Figura 7-8. Ciclo estacional de MP2.5, San Fernando - 2018 ........................................................................................... 37

Figura 7-9. Ciclo estacional de MP10, Estación San Fernando - 2018 ............................................................................. 37

Figura 7-10. Ciclo estacional de O3, Estación San Fernando - 2018 ................................................................................ 38

Figura 7-11: Cumplimiento de norma primaria diaria (Percentil 98) y anual (promedio trianual) de MP 10

(% de la norma) ................................................................................................................................................ 39

Figura 7-12: Cumplimiento de norma primaria diaria (Percentil 98) y anual (promedio trianual) de MP 2.5

(% de la norma) ................................................................................................................................................ 40

Figura 7-13: Cumplimiento de norma primaria de 8 horas de O3 (Percentil 99) (% de la norma) ..................................... 41

Figura 8-1: Curva de Iso-concentración, MP10, 24 horas, P98. ........................................................................................ 44

Figura 8-2: Curva de Iso-concentración, MP10, anual. ...................................................................................................... 45

Figura 8-3: Curva de Iso-concentración, MP2.5, 24 horas, P98. ....................................................................................... 46

Figura 8-4: Curva de Iso-concentración, MP2.5, Anual. .................................................................................................... 47

Figura 8-5: Curva de Iso-concentración, NO2, 1 hora P99. ............................................................................................... 48

Figura 8-6: Curva de Iso-concentración, NO2, Anual. ....................................................................................................... 49

Figura 8-7: Curva de Iso-concentración, SO2, 24 horas, P99. .......................................................................................... 50

Figura 8-8: Curva de Iso-concentración, SO2, anual. ........................................................................................................ 51

Figura 8-9: Curva de Iso-concentración, CO, 1 hora P99. ................................................................................................. 52

Figura 8-10: Curva de Iso-concentración, CO, 8 horas, P99. ............................................................................................ 53

Figura 8-11: Ciclo diario de magnitud del viento San Fernando, 2018 (observado). ......................................................... 54

Figura 8-12: Ciclo diario de magnitud del viento San Fernando, 2018 (simulado). ............................................................ 55

Figura 8-13. Ciclo diario de dirección del viento, porcentaje de ocurrencia (%), Estación San Fernando2018 (observado). ............................................................................................................................................. 56

Figura 8-14. Ciclo diario de dirección del viento, porcentaje de ocurrencia (%), Estación San Fernando2018 (simulado). ............................................................................................................................................... 56

Figura 8-15 Rosa del viento, ciclo diario, Estación San Fernando, 2018 (Observado) ...................................................... 57

Figura 8-16 Rosas de viento año 2018, Estación San Fernando, 2018 (simulado) ........................................................... 58

Figura 8-17 Ciclo estacional del viento, Estación San Fernando, Año 2018 (observado) .................................................. 60

**iv**

Anexo V-C Modelación de Dispersión de Contaminantes

Figura 8-18 Ciclo estacional del viento, Estación San Fernando, año 2018 (simulado) .................................................... 60

**v**

Anexo V-C Modelación de Dispersión de Contaminantes

**1.0** **INTRODUCCION**

El presente estudio contiene los resultados de la simulación de dispersión de material particulado
del proyecto DIA “Plan de Manejo de Sedimentos Central Hidroeléctrica La Higuera”, en adelante el
Proyecto.

El Proyecto se localiza en la Región del Libertador General Bernardo O’Higgins, provincia de
Colchagua, comuna de San Fernando. Específicamente, 55 km al oriente de la ciudad de San
Fernando y 30 km al suroriente del poblado de Puente Negro, en la subcuenca del río Tinguiririca
Alto.

La comuna de San Fernando fue incluida en la declaración de Zona Saturada por norma diaria y
anual de MP10 para las comunas del Valle Central de la Región de acuerdo al D.S. N°7/2009 de
MINSEGPRES. Posteriormente, en el año 2013 el D.S N°15 del Ministerio del Medio Ambiente
(MMA) estableció un Plan de descontaminación (PDA), el cual está en proceso de actualización de
acuerdo a la Res. Ex. N°669 de 2018 del MMA.

En el año 2017, la comuna de San Fernando fue incluida en la declaración de Zona Saturada por
norma diaria y anual de MP2,5 para las comunas del Valle Central de la Región de acuerdo al
Decreto N°42 del MMA. En junio de 2018 se dio inicio al proceso de un PDA de acuerdo a lo
establecido en la Res. Ex. N°503 del MMA.

La evaluación se realiza para un año de operación del Proyecto.

La estimación de las emisiones es presentada en el Anexo I-G de la Adenda, las que corresponden
principalmente a material particulado (MP10 y MP2.5) y en menor medida a gases, asociada a la
operación de los camiones y a maquinarias.

La línea base de calidad del aire, se ha actualizado considerando la información pública disponible
en el portal SINCA, hasta el 2018, por ser la más actualizada al cierre del informe.

La información disponible en el portal SINCA corresponde a la estación San Fernando.

La modelación fue realizada utilizando el modelo de dispersión Calpuff, el cual corresponde a uno

de los modelos más avanzado recomendado por la _Environmental Protection Agency_ (EPA),
utilizando el procedimiento indicado en la “Guía para el uso de modelos de calidad del aire en el
SEIA, año 2012 [1] ”.

La estructura del estudio considera los siguientes puntos:

 - Normativa de calidad del aire aplicable.

 - Caracterización del área de estudio.

 - Presentación de datos utilizados.

 - Línea base de clima y meteorología.

 - Línea base de calidad del aire.

 - Modelación de calidad del aire y resultados.

 - Conclusiones.

1 Guía Para el Uso de Modelos de Calidad del Aire en el SEIA, año 2012, Ministerio del Medio Ambiente.

**1**

Anexo V-C Modelación de Dispersión de Contaminantes

**2.0** **OBJETIVOS**

**2.1** **Objetivo General**

Evaluar el aporte de las emisiones de material particulado (MP10 y MP2.5) y gases (NO2, SO2 y
CO) del Proyecto en su etapa de mayor emisión, la cual corresponderá a la etapa de operación.

**2.2** **Objetivos Específicos**

Los objetivos específicos corresponden a:

 - Establecer la línea base de calidad del aire.

 - Establecer la línea base de meteorología.

 - Establecer las concentraciones a esperar en la calidad del aire en general y en los
receptores cercanos en particular, por medio de la utilización del modelo Calpuff.

 - Análisis de nivel de cumplimento de la normativa de calidad del aire, en base a los aportes
modelados del Proyecto y los registros de Línea Base.

**2**

Anexo V-C Modelación de Dispersión de Contaminantes

**3.0** **NORMATIVA DE CALIDAD DE APLICABLE**

En la Tabla 3-1 se muestra la normativa de calidad del aire aplicable al proyecto.

**Tabla 3-1: Normativa de calidad aplicable al proyecto.**

|Tipo|Contaminante|Normativa|Estadígrafo|Límite|
|---|---|---|---|---|
|**Tipo**|**Contaminante**|**Normativa**|**Estadígrafo**|**μg/m3N **|
|**Norma Primaria**|**MP10**|MP10 (D.S. N°59/98 MINSEGPRES)(2)|Promedio diario, percentil 98|150|
|**Norma Primaria**|**MP10**|MP10 (D.S. N°59/98 MINSEGPRES)(2)|Media aritmética anual|50|
|**Norma Primaria**|**MP2.5**|MP2.5 (D.S. N°12/11 MINSEGPRES)|Promedio diario, percentil 98|50|
|**Norma Primaria**|**MP2.5**|MP2.5 (D.S. N°12/11 MINSEGPRES)|Media aritmética anual|20|
|**Norma Primaria**|**NO2 **|NO2 (D.S. N°114/02 MINSEGPRES)|Máximo diario de 1 hora, percentil 99|400|
|**Norma Primaria**|**NO2 **|NO2 (D.S. N°114/02 MINSEGPRES)|Media aritmética anual|100|
|**Norma Primaria**|**SO2 **|S.O2 (D.S. N°113/02 MINSEGPRES)|Promedio diario, percentil 99|250|
|**Norma Primaria**|**SO2 **|S.O2 (D.S. N°113/02 MINSEGPRES)|Media aritmética anual|80|
|**Norma Primaria**|**CO**|CO (D.S. N°115/02 MINSEGPRES)|Máximo diario de 1 hora, percentil 99|30.000|
|**Norma Primaria**|**CO**|CO (D.S. N°115/02 MINSEGPRES)|Máximo diario de 8 hora, percentil 99|10.000|

Fuente: Elaboración propia .

**3**

Anexo V-C Modelación de Dispersión de Contaminantes

**4.0** **CARACTERIZACION DEL AREA DE ESTUDIO**

**4.1** **Localización**

En la Figura 4-1 se muestra una vista general de la zona donde se emplazará el Proyecto, el cual se
ubica en la Región del Libertador Bernardo O ́Higgins.

**Figura 4-1 Localización del Proyecto**

**4**

Anexo V-C Modelación de Dispersión de Contaminantes

**5.0** **PRESENTACIÓN DE DATOS UTILIZADOS**

**5.1** **Descripción y Justificación del Modelo**

El Proyecto considera la modelación de la dispersión utilizando el modelo Calpuff, alimentado con
campos de viento obtenidos del modelo WRF. Calpuff corresponde a un modelo de dispersión de
tercera generación el cual se ajusta a la complejidad de la modelación de dispersión en terreno
complejo, así como la evaluación de receptores, cercanos y a larga distancia (más de 5 km).

A su vez, el modelo WRF, es uno de los modelos meteorológicos de pronóstico más avanzados y
completos, por lo que su uso en la generación de los campos de viento utilizados en Calpuff permite
dar robustez a la simulación en condiciones de terreno complejo, y de evaluaciones de dispersión a
larga distancia.

Proyecto considera la modelación de la dispersión en los receptores sensibles identificados,
producto de las emisiones asociadas al escenario de mayor emisión en la fase de operación. Para
ello, se utilizó el software de modelación atmosférica CALPUFF View V. 8.5, recomendado por la
Agencia de Protección Ambiental de los Estados Unidos (US-EPA) y la Guía para el Uso de
Modelos de Calidad del Aire en el SEIA; en conjunto con la meteorología de pronóstico obtenida
mediante modelación numérica “Weather Research and Forecasting Model (WRF)”.

El sistema de modelación CALPUFF incluye tres componentes principales: WRF, CALPUFF y
CALPOST, además de una amplia selección de preprocesadores diseñados para incluir en el
modelo datos meteorológicos y geofísicos. Cada uno de estos componentes se describe
brevemente a continuación:

 - CALPUFF es un modelo no estacionario, de dispersión de puffs, que es capaz de simular la
distribución espacial de varios contaminantes en forma simultánea, a medida que son
transportados, modificados por reacciones químicas y depositadas en la superficie. Las
salidas de CALPUFF consisten en concentraciones en cada punto receptor o en formato de
grilla, para cada hora de modelación.

 - WRF corresponde al modelo meteorológico de pronóstico más avanzado y completo
mantenido por NCAR9/NOAA10 de Estados Unidos, capaz de simular campos de viento y
temperatura en un dominio de modelación engrillado y tridimensional. Dichos campos de
vientos permiten determinar posteriormente la dispersión de los contaminantes, a través de
la aplicación del modelo CALPUFF.

 - El modelo WRF, integra las variables relativas a uso de suelo, topografía, albedo, rugosidad,
entre otras, con fuente de información provista por el Land Cover Institute del U.S.
Geological Survey (USGS) en EE.UU.

 - CALPOST es una herramienta que permite obtener promedios móviles, máximos impactos,
percentiles, tabla de máximos impactos, estimaciones de visibilidad, etc., a partir de las
series de tiempos de concentraciones generadas por CALPUFF.

**5.2** **Receptores Considerados**

En la evaluación de las concentraciones aportadas por el Proyecto en su área de estudio, se han
considerado los receptores puntuales que se muestran en la Tabla 5-1, los cuales corresponde a los
receptores más cercanos.

**5**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 5-1: Receptores puntuales considerados.**

|N°|Recepto|Coordenadas UTM Datum WGS84 (1)|Col4|
|---|---|---|---|
|**N°**|**Recepto**|**Este (m)**|**Norte (m)**|
|1|Est. San Fernando|317.503|6.171.746|
|2|Puente Negro|328.731|6.159.897|
|3|La Rufina|339.632|6.153.882|
|4|Termas El Flaco|368.824|6.130.717|

Nota 1: Uso 19 Sur

Fuente: Elaboración propia

**5.3** **Dominio de Modelación**

En la Figura 5-1, se muestra el dominio de modelación. Asimismo, se observa la ubicación relativa
de los receptores respecto a las fuentes de emisión evaluadas. La extensión del dominio se ha
seleccionado considerando las estaciones de calidad del aire y receptores considerados.

En la Tabla 5-2, se indican los parámetros considerados en el dominio de modelación.

**Figura 5-1 Dominio de modelación y receptores puntuales considerados**

**6**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 5-2: Características del dominio de modelación.**

|Descripción|Detalle|
|---|---|
|Tamaño de la grilla|1 km x 1 km|
|Resolución horizontal y vertical del dominio|64 km (Este - Oeste) x 49 km (Norte - Sur)|
|Número capas|11 entre 0 y 4.000 m de altura|
|Coordenadas central de origen (UTM)|345.196 m E y 6.151.543 m S, Datum WGS 84|
|Área del dominio en km2|3.136 km2|
|Topografía|Extraída de SRTM3 con resolución de 90 m|
|Usos de suelo|Extraídos de Global Land Cover Characterization (GLCC) del<br>US Geological Survey (UGS), EEUU, con resolución de 1 km.|

Fuente: Elaboración propia.

**5.4** **Topografía**

La información topográfica utilizada en la modelación del Proyecto corresponde a cartas
topográficas digitales SRTM3, con resolución de 90 metros, la cual se muestran en Figura 5-2 .

**Figura 5-2 Topografía del dominio de modelación**

**7**

Anexo V-C Modelación de Dispersión de Contaminantes

**5.5** **Uso de Suelo**

La información de uso de suelo utilizada en la modelación del Proyecto corresponde a la
suministrada por el Global Land Cover Characterization (GLCC) del US Geological Survey (UGS) de
EEUU, con resolución de 1 km, la cual se muestran en Figura 5-3 .

**Figura 5-3 Uso de Suelo**

**5.6** **Fuentes de Emisión y Parámetros Utilizados en Modelación**

**5.6.1** **Fuentes de emisión**

Como se ha visto en el Apéndice A de estimación de emisiones, no habrá etapa de construcción,
por lo que la mayor emisión corresponde la etapa de operación, siendo ésta la etapa a modelar.

En la Tabla 5-3 se muestran las emisiones a generarse en la etapa de operación y las actividades
asociadas.

**8**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 5-3: Emisiones Etapa de Operación.**

|Actividades|MP10|MP2,5|NOx|SO2|CO|COV|
|---|---|---|---|---|---|---|
|**Actividades**|**(ton/año)**|**(ton/año)**|**(ton/año)**|**(ton/año)**|**(ton/año)**|**(ton/año)**|
|**1. Circulación de vehículos por caminos**<br>**no pavimentados**|**10,892**|**1,089**|**0,000**|**0,000**|**0,000**|**0,000**|
|1.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|9,443|0,944|||||
|1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|1,449|0,145|||||
|**2. Circulación de vehículos por caminos**<br>**pavimentados**|**0,031**|**0,008**|**0,000**|**0,000**|**0,000**|**0,000**|
|2.1 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|0,011|0,003|||||
|2.2 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|0,020|0,005|||||
|**3. Combustión interna de motores de**<br>**vehículos**|**0,0015**|**0,0015**|**0,0479**|**0,0000**|**0,0140**|**0,0032**|
|3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|0,0006|0,0006|0,0123|0,0000|0,0041|0,0010|
|3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|0,0006|0,0006|0,0241|0,0000|0,0069|0,0015|
|3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|0,0001|0,0001|0,0020|0,0000|0,0007|0,0002|
|3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|0,0002|0,0002|0,0094|0,0000|0,0023|0,0005|
|**4. Combustión interna de motores de**<br>**maquinaria**|**0,380**|**0,380**|**4,963**|**0,000**|**1,037**|**0,467**|
|4.1 Draga de succión Dragatec 300-350|0,243|0,243|3,171|0,000|0,662|0,298|
|4.2 Embarcación menor|0,137|0,137|1,792|0,000|0,374|0,168|
|**5. Combustión interna de motores de**<br>**generadores**|**0,013**|**0,013**|**0,180**|**0,012**|**0,039**|**0,000**|
|5.1 Generador 25 KVA|0,013|0,013|0,180|0,012|0,039|0,00|
|**TOTAL**|**11,318**|**1,491**|**5,191**|**0,012**|**1,090**|**0,470**|

Fuente: Elaboración propia.

En la Tabla 5-4 se muestran las fuentes emisoras modeladas en Calpuff y las actividades emisoras
consideradas.

Tanto los caminos de acceso al Proyecto han sido modelados como fuentes de línea, mientras que
el área del Proyecto ha sido modelado como fuente de área. Es importante señalar que dado que el
Tramo 1 Puente Negro - Pondaje Tricahue, como el Tramo 2 San Fernando - Pondaje Tricahue, de
transito sobre caminos no pavimentados, son los mismos. La emisión conjunta de estos tramos de
camino se ha modelado como una sola fuente (SRC_1).

**Tabla** **5-4: Fuentes modeladas** **en Calpuff y** **actividades** **emisoras** **asociadas.**

|Source<br>ID|Fuente|Actividades|Tipo<br>de<br>Fuente|Ancho|Largo|Área|
|---|---|---|---|---|---|---|
|**Source**<br>**ID**|**Fuente**|**Actividades**|**Tipo**<br>**de**<br>**Fuente**|**m **|**m **|**m2**|
|**SRC_1**|**Tramo 1 Puente**<br>**Negro - Pondaje**<br>**Tricahue PAV (No**<br>**Pavimentado)**|1.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|Línea|12|35.220|422.640|
|**SRC_1**|**Tramo 1 Puente**<br>**Negro - Pondaje**<br>**Tricahue PAV (No**<br>**Pavimentado)**|3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|
|**SRC_1**|** Tramo 2 San**<br>**Fernando - Pondaje**<br>**Tricahue PAV (No**<br>**Pavimentado)**|1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|
|**SRC_1**|** Tramo 2 San**<br>**Fernando - Pondaje**<br>**Tricahue PAV (No**<br>**Pavimentado)**|3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|
|**SRC_2**|**Tramo 3 Puente**|2.1 Tramo 3 Puente Negro - Pondaje|Línea|12|2.670|32.040|

**9**

Anexo V-C Modelación de Dispersión de Contaminantes

|Source<br>ID|Fuente<br>Negro - Pondaje<br>Tricahue PAV<br>(Pavimentado)|Actividades<br>Tricahue PAV (Pavimentado)|Tipo<br>de<br>Fuente|Ancho|Largo|Área|
|---|---|---|---|---|---|---|
|**Source**<br>**ID**|**Fuente**<br>**Negro - Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|**Actividades**<br>Tricahue PAV (Pavimentado)|**Tipo**<br>**de**<br>**Fuente**|**m **|**m **|**m2**|
|**Source**<br>**ID**|**Fuente**<br>**Negro - Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|
|**SRC_3**|**Tramo 4 San**<br>**Fernando - Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|2.2 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|Línea|12|19.000|228.000|
|**SRC_3**|**Tramo 4 San**<br>**Fernando - Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|
|**SRC_4**|**Pondaje Tricahue**|4.1 Draga de succión Dragatec 300-350|Área|||33.539|
|**SRC_4**|**Pondaje Tricahue**|4.2 Embarcación menor|4.2 Embarcación menor|4.2 Embarcación menor|4.2 Embarcación menor|4.2 Embarcación menor|
|**SRC_4**|**Pondaje Tricahue**|5.1 Generador 25 KVA|5.1 Generador 25 KVA|5.1 Generador 25 KVA|5.1 Generador 25 KVA|5.1 Generador 25 KVA|

Fuente: Elaboración propia.

En la Tabla 5-5 a Tabla 5-6 se muestra la emisión mensual de las fuentes y la tasa de emisión
calculada en gramos por segundo. La tasa de emisión se ha estimado considerado una jornada de
30 días al mes, 8 horas al día. Es importante señalar que la operación tendrá una duración de 5
meses al año, entre los meses de abril a agosto.

**Tabla 5-5: Tasa de emisión de material particulado y fuente modelada asociada.**

|Source<br>ID|Fuente|Actividades|MP10|Col5|Col6|MP2.5|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Source**<br>**ID**|**Fuente**|**Actividades**|**ton/año**|**g/s**|**g/s/m2**|**ton/año**|**g/s**|**g/s/m2**|
|**SRC_1**|**Tramo 1 Puente**<br>**Negro - Pondaje**<br>**Tricahue PAV (No**<br>**Pavimentado)**|1.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|9,443|2,2E+00||0,944|2,2E-01||
|**SRC_1**|**Tramo 1 Puente**<br>**Negro - Pondaje**<br>**Tricahue PAV (No**<br>**Pavimentado)**|3.1 Tramo 1 Puente Negro - Pondaje<br>Tricahue PAV (No Pavimentado)|0,001|1,4E-04||0,001|1,4E-04||
|**SRC_1**|**Tramo**<br>**2 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(No**<br>**Pavimentado)**|1.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|1,449|3,4E-01||0,145|3,4E-02||
|**SRC_1**|**Tramo**<br>**2 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(No**<br>**Pavimentado)**|3.2 Tramo 2 San Fernando - Pondaje<br>Tricahue PAV (No Pavimentado)|0,001|1,5E-04||0,001|1,5E-04||
|**SRC_1**|**Tramo**<br>**2 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(No**<br>**Pavimentado)**|**Sub Total:**|**10,893**|**2,52E+00**|**6,0E-06**|**1,090**|**2,52E-01**|**6,0E-07**|
|**SRC_2**|**Tramo 3 Puente**<br>**Negro - Pondaje**<br>**Tricahue**<br>**PAV**<br>**(Pavimentado)**|2.1 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|0,011|2,6E-03||0,003|6,2E-04||
|**SRC_2**|**Tramo 3 Puente**<br>**Negro - Pondaje**<br>**Tricahue**<br>**PAV**<br>**(Pavimentado)**|3.3 Tramo 3 Puente Negro - Pondaje<br>Tricahue PAV (Pavimentado)|0,000|2,3E-05||0,000|2,3E-05||
|**SRC_2**|**Tramo 3 Puente**<br>**Negro - Pondaje**<br>**Tricahue**<br>**PAV**<br>**(Pavimentado)**|**Sub Total:**|**0,011**|**2,59E-03**|**8,1E-08**|**0,003**|**6,44E-04**|**2,0E-08**|
|**SRC_3**|**Tramo**<br>**4 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(Pavimentado)**|2.2 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|0,020|4,7E-03||0,005|1,1E-03||
|**SRC_3**|**Tramo**<br>**4 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(Pavimentado)**|3.4 Tramo 4 San Fernando - Pondaje<br>Tricahue PAV (Pavimentado)|0,000|4,8E-05||0,000|4,8E-05||
|**SRC_3**|**Tramo**<br>**4 **<br>**San**<br>**Fernando**<br>**- **<br>**Pondaje Tricahue**<br>**PAV**<br>**(Pavimentado)**|**Sub Total:**|**0,020**|**4,72E-03**|**2,1E-08**|**0,005**|**1,18E-03**|**5,2E-09**|
|**SRC_4**|**Pondaje Tricahue**|4.1 Draga de succión Dragatec 300-<br>350|0,243|5,6E-02||0,243|5,6E-02||
|**SRC_4**|**Pondaje Tricahue**|4.2 Embarcación menor|0,137|3,2E-02||0,137|3,2E-02||
|**SRC_4**|**Pondaje Tricahue**|5.1 Generador 25 KVA|0,013|3,0E-03||0,013|3,0E-03||
|**SRC_4**|**Pondaje Tricahue**|**Sub Total:**|**0,393**|**9,10E-02**|**2,7E-06**|**0,393**|**9,10E-02**|**2,7E-06**|
||||**11,318**||**8,8E-06**|**1,491**||**3,3E-06**|

Fuente: Elaboración propia.

**10**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla** **5-6: Tasa** **de** **emisión de** **gases** **y fuente modelada** **asociada.**

|Source<br>ID|Fuente|Actividades|NOx|Col5|Col6|SO2|Col8|Col9|CO|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Source**<br>**ID**|**Fuente**|**Actividades**|**ton/año**|**g/s**|**g/s/m2**|**ton/año**|**g/s**|**g/s/m2**|**ton/año**|**g/s**|**g/s/m2**|
|**SRC_1**|**Tramo**<br>**1 **<br>**Puente Negro**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(No**<br>**Pavimentado)**|1.1<br>Tramo<br>1 <br>Puente<br>Negro<br>- <br>Pondaje<br>Tricahue<br>PAV<br>(No<br>Pavimentado)|0,000|0,0E+00||0,000|0,0E+00||0,000|0,0E+00||
|**SRC_1**|**Tramo**<br>**1 **<br>**Puente Negro**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(No**<br>**Pavimentado)**|3.1<br>Tramo<br>1 <br>Puente<br>Negro<br>- <br>Pondaje<br>Tricahue<br>PAV<br>(No<br>Pavimentado)|0,012|2,8E-03||0,000|0,0E+00||0,004|9,6E-04||
|**SRC_1**|** Tramo 2 San**<br>**Fernando**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(No**<br>**Pavimentado)**|1.2 Tramo 2 San<br>Fernando<br>- <br>Pondaje<br>Tricahue<br>PAV<br>(No<br>Pavimentado)|0,000|0,0E+00||0,000|0,0E+00||0,000|0,0E+00||
|**SRC_1**|** Tramo 2 San**<br>**Fernando**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(No**<br>**Pavimentado)**|3.2 Tramo 2 San<br>Fernando<br>- <br>Pondaje<br>Tricahue<br>PAV<br>(No<br>Pavimentado)|0,024|5,6E-03||0,000|0,0E+00||0,007|1,6E-03||
|**SRC_1**|** Tramo 2 San**<br>**Fernando**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(No**<br>**Pavimentado)**|**Sub Total:**|**0,036**|**8,44E-03**|**2,0E-08**|**0,000**|**0,00E+00**|**0,0E+00**|**0,011**|**2,55E-03**|**6,0E-09**|
|**SRC_2**|**Tramo**<br>**3 **<br>**Puente Negro**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|2.1<br>Tramo<br>3 <br>Puente<br>Negro<br>- <br>Pondaje<br>Tricahue<br>PAV<br>(Pavimentado)|0,000|0,0E+00||0,000|0,0E+00||0,000|0,0E+00||
|**SRC_2**|**Tramo**<br>**3 **<br>**Puente Negro**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|3.3<br>Tramo<br>3 <br>Puente<br>Negro<br>- <br>Pondaje<br>Tricahue<br>PAV<br>(Pavimentado)|0,002|4,6E-04||0,000|0,0E+00||0,001|1,6E-04||
|**SRC_2**|**Tramo**<br>**3 **<br>**Puente Negro**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|**Sub Total:**|**0,002**|**4,61E-04**|**1,4E-08**|**0,000**|**0,00E+00**|**0,0E+00**|**0,001**|**1,55E-04**|**4,8E-09**|
|**SRC_3**|**Tramo 4 San**<br>**Fernando**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|2.2 Tramo 4 San<br>Fernando<br>- <br>Pondaje<br>Tricahue<br>PAV<br>(Pavimentado)|0,000|0,0E+00||0,000|0,0E+00||0,000|0,0E+00||
|**SRC_3**|**Tramo 4 San**<br>**Fernando**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|3.4 Tramo 4 San<br>Fernando<br>- <br>Pondaje<br>Tricahue<br>PAV<br>(Pavimentado)|0,009|2,2E-03||0,000|0,0E+00||0,002|5,3E-04||
|**SRC_3**|**Tramo 4 San**<br>**Fernando**<br>**- **<br>**Pondaje**<br>**Tricahue PAV**<br>**(Pavimentado)**|**Sub Total:**|**0,009**|**2,19E-03**|**9,6E-09**|**0,000**|**0,00E+00**|**0,0E+00**|**0,002**|**5,31E-04**|**2,3E-09**|
|**SRC_4**|**Pondaje**<br>**Tricahue**|4.1<br>Draga<br>de<br>succión<br>Dragatec<br>300-350|3,171|7,3E-01||0,000|0,0E+00||0,662|1,5E-01||
|**SRC_4**|**Pondaje**<br>**Tricahue**|4.2<br>Embarcación<br>menor|1,792|4,1E-01||0,000|0,0E+00||0,374|8,7E-02||
|**SRC_4**|**Pondaje**<br>**Tricahue**|5.1 Generador 25<br>KVA|0,180|4,2E-02||0,012|2,8E-03||0,039|9,0E-03||
|**SRC_4**|**Pondaje**<br>**Tricahue**|**Sub Total:**|**5,143**|**1,19E+00**|**3,5E-05**|**0,012**|**2,78E-03**|**8,3E-08**|**1,076**|**2,49E-01**|**7,4E-06**|
|<br> <br>|<br> <br>|<br> <br>|**5,191**||**3,6E-05**|**0,012**||**8,3E-08**|**1,090**||**7,4E-06**|

Fuente: Elaboración propia.

**11**

Anexo V-C Modelación de Dispersión de Contaminantes

**6.0** **LÍNEA BASE DE CLIMA Y METEOROLOGÍA**

A continuación, se presenta la línea de base de clima y meteorología para el área de estudio del
Proyecto el cual se ubica en la Región del Libertador General Bernardo O’Higgins, en la comuna de
San Fernando. La descripción climática se efectuó en un contexto regional y local, mientras que la
meteorología se efectuó a escala local.

**6.1** **Caracterización climática regional**

El área de estudio se ubica en la comuna de San Fernando, Provincia del Colchagua en la Región
del Libertador General Bernardo O'Higgins, la cual está en la transición de dos zonas climáticas, la
primera corresponde al valle central bajo un predominio del Clima Templado cálido con estación
seca prolongada de 8 a 7 meses y la segunda hacia la zona precordillerana con un Clima Templado
Cálido con estación Seca de 5 a 4 meses cuya distribución se muestra en la Figura 6-1.

**Figura 6-1 Clasificación del clima según Köppen**

Fuente: Guía Climática Práctica de la Dirección Meteorológica de Chile.

**12**

Anexo V-C Modelación de Dispersión de Contaminantes

**6.1.1** **Clima Templado cálido con estación seca prolongada de 8 a 7 meses**

Según la clasificación presentada en la Figura 6-1, en el área del Valle Central, donde se ubica la
Comuna de San Fernando, predomina el clima templado cálido con estación seca prolongada de 8 a
7 meses. La principal característica de este clima son las precipitaciones que caen preferentemente
en invierno, entre mayo y agosto, cuando precipita alrededor del 80% de lo que cae en todo el año.
La época seca está constituida por 7 u 8 meses con precipitaciones inferiores a 40 milímetros. En
verano se observa un predominio de días despejados (22 por mes) y con altas temperaturas (28
días cálidos por mes), además no son frecuentes las lluvias en esta época. Durante los meses
invernales predominan los días nublados (13 en promedio) y se registran 5 días con precipitaciones
(2 débiles, 2 intensas y 1 muy intensa). En esta época son esperables 3 días con helada al mes.

**6.1.2** **Clima Templado cálido con estación seca de 4 a 5 meses**

Hacia la zona precordillerana donde se ubica el Proyecto, el clima corresponde a Templado Cálido
con estación Seca de 5 a 4 meses que comprende la pre cordillera de las regiones Metropolitana y
Sexta, además de la región del Maule y la parte norte de la región del Bío Bío. El ascenso del
relieve provoca grandes variaciones en el clima, ya que las temperaturas mínimas en el invierno se
aproximan a 0 grado y las precipitaciones invernales se pueden hacer sólidas, al mismo tiempo que
aumentan a cerca de 1000 milímetros anuales, acortándose así la duración de la estación seca, a
sólo 4 a 5 meses con precipitación inferior a 40 milímetros. Las temperaturas medias son del orden
de 4o C más bajas que en la zona climática contigua y la diferencia entre el mes más cálido y el más
frío también desciende a unos 11o C.

**6.2** **Presentación de datos meteorológicos observados**

La estación meteorológica más cercana al Proyecto, en el área de estudio y con datos validos
disponibles, corresponde a la estación San Fernando de la Red del Ministerio del Medio Ambiente.
La estación San Fernando fue instalada en el año 2007 y sus datos meteorológicos (validados y
preliminares sin validación) están quedando disponibles en línea en el sitio web del Sistema de
Información Nacional de Calidad del Aire (SINCA) [2] . Por otro lado, para complementar la información
de precipitación, se utilizaron los datos de la estación El Tambo de la Red Agro Climática Nacional
del Ministerio de Agricultura, los cuales están disponibles en línea en su sitio [3] web. En la Figura 6-2
se muestra la ubicación de ambas estaciones meteorológicas respecto al Proyecto.

La Tabla 6-1 resume la ubicación, la distancia al proyecto y las variables medidas en las estaciones
meteorológicas.

La Tabla 6-2 presenta un resumen de datos disponibles en la estación San Fernando para el año
2018.
De acuerdo a lo presentado en la Tabla 6-2, las variables meteorológicas tienen sobre 99% de datos
válidos, lo cual se puede verificar al observar los gráficos de series de tiempo presentados a
continuación.

2 Sistema Nacional de Calidad del Aire (SINCA), disponible en: http://sinca.mma.gob.cl
3 http://agromet.inia.cl

**13**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 6-1: Coordenadas y variables medidas en estaciones meteorológicas**

|N°|Receptor|Coordenadas UTM Datum<br>WGS84 (1)|Col4|Uso|Distancia a<br>Proyecto|Información<br>meteorológica (2)|
|---|---|---|---|---|---|---|
|**N°**|**Receptor**|**Norte (m)**|**Este (m)**|**Este (m)**|**Km**|**Km**|
|1|Estación San Fernando|6.171.746|317.503|19H|31,8|VV, DV, Temp.,<br>HR, RS, PA|
|2|Estación El Tambo|6.183.828|317.515|19H|40,,1|PP|

Nota 2: Velocidad del Viento (VV), Dirección del Viento (DV), Temperatura (Temp.), Humedad Relativa (HR), Radiación Solar (RS), Presión
Atmosférica (PA), PP: Precipitación diaria

Fuente: Elaboración propia.

**Figura 6-2 Ubicación de estaciones meteorológicas San Fernando y El Tambo**

**14**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 6-2 Resumen de datos horarios válidos disponibles, estación San Fernando-2018**

Nota1: datos de Presión atmosférica corresponden al año 2016

**6.2.1** **Series de tiempo en la estación San Fernando**

De acuerdo a la información disponible en SINCA, se utilizaron los datos horarios obtenidos de la
Estación San Fernando para el año 2018 de velocidad de viento, dirección de viento, temperatura,
humedad relativa y radiación solar. Los datos de presión atmosférica corresponden al año 2016 ya
que desde octubre del 2017 los valores no corresponden a los valores esperados para el
comportamiento de la presión atmosférica, es muy probable una falla en el sensor.

Los gráficos de la serie temporal presentados a continuación permiten un análisis cualitativo de los
datos en términos de completitud de la serie y periodos con datos faltantes, valores fuera de rango y
problemas de equipos (datos constantes, tendencias, entre otras).

Serie de Velocidad y Dirección del Viento

La serie de tiempo de la velocidad del viento de la Figura 6-3 muestra para el año 2018 que durante
la época invernal, producto del ingreso de sistemas frontales a la zona de estudio, hay días con
velocidades máximas más altas a las observadas en verano. Además, se observa que las
velocidades mínimas entre abril y septiembre son menores a las registradas de octubre a marzo.
Los valores fluctúan entre 0,0 y 5,5 m/s, con un promedio de velocidad para el año 2018 de 1,7 m/s.

**Figura 6-3 Serie de registros horarios de velocidad del viento, Est. San Fernando, año 2018**

Fuente: Elaboración propia con datos de SINCA.

La serie de tiempo de la dirección del viento presentada en la Figura 6-4, muestra para el año 2018
una marcada ocurrencia de vientos de componentes entre SurEste y SurOeste (entre 135° y 250°),

**15**

Anexo V-C Modelación de Dispersión de Contaminantes

siendo mayor la ocurrencia de componente cercana a SO en temporada estival y en la temporada
invernal hay mayor predominio de las componentes entre S y SE. Durante meses de otoño-invierno,
especialmente aquellos días que tienen las velocidades más altas que corresponden al paso de
sistemas frontales tienen componente principal de vientos desde el Norte.

**Figura 6-4 Serie de registros horarios de dirección del viento, Est. San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA.

Serie de Temperatura

La serie de tiempo de la temperatura de la Figura 6-5 muestra para el año 2018 un marcado ciclo
estacional, con mayores temperaturas en el periodo estival (diciembre a febrero) que superan 30°C
durante la mayoría de los días, en cambio las mínimas son cercanas a 15°C. Durante los meses de
invierno la mayoría de los días tiene máximas inferiores a 20°C y mínimas cercanas a 5°C, incluso
algunos días registran temperaturas inferiores a 0°C. El valor medio de la temperatura durante el
año 2018 alcanza los 14,2°C, con máximo de 32,6°C y una mínima de -2,5°C.

**Figura 6-5 Serie de tiempo para registros horarios de temperatura, Est. San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA.

**16**

Anexo V-C Modelación de Dispersión de Contaminantes

Serie de Humedad

La serie de tiempo de la humedad relativa presentada en la Figura 6-6, muestra un ciclo estacional
con mayores valores en Invierno, donde la mayoría de los días supera 85%, en cambio en meses de
verano las máximas son cercanas a 60%, pero las mínimas pueden descender hasta 20%. Para el
año 2018 el promedio de humedad fue 61,9%, con un máximo de 95% y un mínimo de 10%.

**Figura 6-6 Serie de tiempo para registros horarios de humedad relativa, Est. San Fernando-**

**2018**

Fuente: Elaboración propia con datos de SINCA.

Serie de Radiación Solar

La serie de tiempo de radiación presentada en la Figura 6-7 muestra un ciclo anual para el año 2018
con mayores valores de radiación en la época estival y menores en la época invernal. Algunos días
tienen bajos valores de radiación producto de la nubosidad, especialmente entre mayo y agosto con
valores inferiores a 150 W/m2. En verano, se registran los máximos horarios de radiación solar con
valores que superan 900 W/m [2] y en meses de invierno los máximos diarios de la mayoría de los
días son cercanos a 600 W/m2. Entre julio y agosto se registran algunos días con las máximas
diarias de radiación solar superiores a 800 W/m2 que no siguen la tendencia anual, las cuales
podrían estar asociadas a un mal funcionamiento del sensor de radiación.

**17**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 6-7 Serie de tiempo para registros horarios de Radiación Solar, Est. San Fernando-**

**2018**

Fuente: Elaboración propia con datos de SINCA.

Serie de Presión Atmosférica

La Figura 6-8 muestra para la presión atmosférica escasa variabilidad a lo largo del año 2016 ya
que no hay valores representativos disponibles desde octubre de 2017. El valor promedio para el
año 2016 es 978 hPa, con un mínimo de 963 hPa y un máximo de 990 hPa. Durante la época
invernal se observa una mayor variabilidad en los valores de presión durante el día, producto del
ingreso de altas presiones frías y bajas frontales, especialmente entre los meses de junio y agosto.

**Figura 6-8 Serie de tiempo para registros horarios de Presión Atmosférica, Est. San**

**Fernando-2016**

Fuente: Elaboración propia con datos de SINCA.

**18**

Anexo V-C Modelación de Dispersión de Contaminantes

Serie de Precipitación diaria

La Figura 6-9 presenta la serie de precipitaciones diarias para el año 2018 en la estación El Tambo
de la red Agroclimática de INIA, la cual corresponde al dato de precipitación más cercano a la
estación San Fernando. La precipitación en la estación El Tambo y alrededores es de carácter
frontal principalmente, los principales episodios de días con lluvias se registraron entre mayo y
agosto alcanzando un total anual de 302,3 mm. Durante el año 2018 el mayor evento de
precipitación diaria fue de 31,7 mm en junio, con 22 días por sobre 1mm y 11 días sobre 10 mm.

**Figura 6-9 Serie de tiempo para registros diarios de precipitación, El Tambo - año 2018**

Fuente: Elaboración propia con datos de http://agromet.inia.cl/.

**6.2.2** **Ciclos diarios en la estación San Fernando**

A continuación, se muestra un análisis de los ciclos diarios de las variables meteorológicas medidas
en la Estación San Fernando durante el año 2018, excepto para presión atmosférica que
corresponde al año 2016, es decir representar el comportamiento de las variables en un día
promedio. Cada ciclo considera tres curvas: Media para el comportamiento de los valores promedio,
Percentil 5% y Percentil 95%.

En la Figura 6-10 se observa el ciclo diario de la velocidad del viento. En promedio, se observa un
ciclo con poca variabilidad presentando las mayores velocidades durante las tardes con un valor
máximo de 2,4 m/s alrededor de las 17:00. Desde las 20:00 hasta las 06:00 de la mañana siguiente
los valores se mantienen cercanos a 1,4 m/s. Para la curva del percentil 95%, los máximos en las
tardes son cercanos a 3,6 m/s y los mínimos cercanos a 2,4 m/s en la madrugada. Además, se
aprecia que durante las tardes los valores máximos del percentil 5% son cercanos a 0,9 m/s entre
16:00 y 18:00 y los mínimos cercanos a 0,2 m/s desde las 20:00 hasta las 10:00 de la mañana del
día siguiente.

**19**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 6-10 Ciclo diario de los promedios horarios de la velocidad del viento, Est. San**

**Fernando, año 2018**

Fuente: Elaboración propia con datos de SINCA.

La Figura 6-11, muestra el ciclo diario de la dirección de viento expresado como porcentaje de
ocurrencia o frecuencias durante las horas del día para 16 sectores principales. Se puede observar
que la dirección predominante o principal desde donde viene el viento tiene una marcada
componente SSE (entre SurEste y Sur) durante la madrugada alcanzando un máximo de 26% entre
04:00 y 06:00. Desde mediodía hasta las 16:00 la componente principal es SO con un porcentaje de
32% rotando a frecuencias de 30% desde SSE entre 16:00 y 19:00. Durante la noche, entre las
20:00 y las 23:00 las frecuencias principales son nuevamente desde SO alcanzando un valor
cercano a 34%

**Figura 6-11 Ciclo diurno de la dirección del viento, porcentaje de ocurrencia, Est. San**

**Fernando, año 2018.**

Fuente: Elaboración propia con datos de SINCA.

**20**

Anexo V-C Modelación de Dispersión de Contaminantes

El ciclo diario de la temperatura para el año 2018 presentado en la Figura 6-12 muestra un
comportamiento con una amplitud térmica con diferencias cercanas a 15°C entre las curvas del
percentil 5% y 95% durante las horas de menor temperatura y cercana a 23°C durante la tarde a las
horas de mayor temperatura. Para la curva de los valores promedios, entre las 06:00 y 07:00 horas
se presenta una mínima matutina cercana a los 9,1 °C (temperatura media), y una máxima por la
tarde cerca de las 16:00 horas de 22,2 °C. Los valores máximos para la curva del percentil 95% son
cercanos a 30,4°C y los valores mínimos de la curva del percentil 5% son cercanos a 1°C.

**Figura 6-12 Ciclo diario de los promedios horarios de la temperatura, Est. San Fernando -**

**2018**

Fuente: Elaboración propia con datos de SINCA.

El ciclo diario de la humedad relativa para el año 2018 presentado en la Figura 6-13 muestra un
ciclo contrario al ciclo de la temperatura con una amplitud entre la curva de percentil 5% y 95%
cercana a 44% durante la las primeras horas del día, la cual disminuye hasta 28% a las horas de
temperaturas mínimas (07:00) y vuelve aumentar hasta 59% durante la tarde a las horas de mayor
temperatura y menor humedad. La curva del ciclo promedio muestra los mayores valores de
humedad durante la mañana cercanos a 80% y menores durante la tarde llegando hasta un 41%
entre 15:00 y 17:00. En cambio, el ciclo del percentil 95% tiene valores de humedad cercanos a
92% durante la noche y madrugada disminuyendo hasta 75% en la tarde a las horas de mayor
temperatura. El ciclo del percentil 5% registra los mayores valores de humedad alrededor de las
07:00 con 64% y menores valores cercanos a 17% durante la tarde, en el mismo horario de los
menores valores medios y del percentil 95%.

**21**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 6-13 Ciclo diario de los promedios horarios de la hum. relativa, Est. San Fernando -**

**2018**

Fuente: Elaboración propia con datos de SINCA.

El ciclo diario de la radiación solar para el año 2018 presentado en la Figura 6-14 muestra que entre
las 06:00 y 21:00 horas se presentan valores mayores a cero de radiación solar, en promedio. El
máximo de radiación se presenta a las 14:00 horas del orden de 923 W/m [2] para la curva del ciclo
del percentil 95% y con valores cercanos a 607 W/m [2] para la curva media. Durante las tardes, los
valores de radiación de la curva del percentil 5% alcanzan máximos de 97 W/m [2] .

**Figura 6-14 Ciclo diario de los promedios horarios de Radiación Solar, Est. San Fernando -**

**2018**

Fuente: Elaboración propia con datos de SINCA.

El ciclo diario de la presión atmosférica para el año 2016 presentado en la Figura 6-15, muestra un
ciclo prácticamente plano para las tres curvas. Para los valores medios se observa con un leve
aumento alrededor de mediodía y alrededor de las 22:00 horas con valores cercanos a 1010 hPa,

**22**

Anexo V-C Modelación de Dispersión de Contaminantes

durante el resto del día los valores son cercanos a 976 hPa, entre la curva del percentil 95% y la
curva del 5% se observa una diferencia de 12 hPa. Para la curva del percentil 95% los valores más
altos de presión son cercanos a 985 hPa y para la curva del 5% los valores más bajos son cercanos
a 971 hPa.

**Figura 6-15 Ciclo diario de los promedios horarios de Presión Atmosférica, Est. San**

**Fernando - 2016**

Fuente: Elaboración propia con datos de SINCA.

**6.2.3** **Rosa de los vientos estación San Fernando**

La Figura 6-16 muestra las rosas de distribución de frecuencia de dirección de vientos, para
distintas clases de velocidades de viento y cuatro períodos del día, para ilustrar los cambios entre
períodos diurnos y nocturnos.

**23**

Anexo V-C Modelación de Dispersión de Contaminantes

Viento (m/s):

**Figura 6-16 Rosa del viento, ciclo diario, Est. San Fernando, año 2018.**

Fuente: Elaboración propia con datos de SINCA.

De acuerdo a la Figura 6-16, durante la madrugada, entre las 00:00 y 05:00 horas, las direcciones
de viento provienen en mayor medida desde sectores de SurESte (SE) a SurOeste (SO) con un
predominio de la componente SSE con un 24% de los casos, seguido de SE con un 17% y en tercer
lugar SO con un 14%. Hay un 11,8% de calmas y un 69% de vientos en la clase 0,5 a 2,1 m/s.

Para el período 06:00 a 11:00 hay disminución del porcentaje de frecuencias de componente SSE
hasta 17%, aumentando SE hasta 20% y se mantienen en tercer lugar SO con 15%. Durante este
período hay un 7,7 de calmas y un 0,7% alcanzan velocidades más en la clase de 3,6 a 5,7 m/s.
Además, un 67% de las velocidades en la clase 0,5 a 2,1 m/s y un 25% en la clase 2,1 a 3,6 m/s.

Entre las 12:00 y las 17:00 horas la componente principal corresponde a SO con un 25%, en
segundo lugar SSE con un 19% y la componente S alcanza el tercer lugar con 13%. Durante este
período hay un 2,2 de calmas y un 0,1% alcanzan velocidades más en la clase de 5,7 a 8,8 m/s.
Además, un 35% de las velocidades están en la clase 0,5 a 2,1 m/s, un 57% en la clase 2,1 a 3,6
m/s y un 5% en la clase 3,6 a 5,7 m/s.

Hacia la noche, entre las 18:00 y las 23:00 horas comienza la transición al régimen nocturno,
disminuyendo la frecuencia de la componente SO a 24% y aumenta la componente SOS hasta 18%,
en tercer lugar se ubica SSE con 14%. Durante este período hay un 6,2 de calmas y un 1,4%
alcanzan velocidades más en la clase de 3,6 a 5,7 m/s. Además, un 59% de las velocidades están
en la clase 0,5 a 2,1 m/s y un 33% en la clase 2,1 a 3,6 m/s.

Al considerar toda la jornada y todo el año 2018, de acuerdo a lo presentado en la Figura 6-17, las
direcciones de viento provienen desde sectores de SE a OSO, con una mayor frecuencia de la
componente SO (con un 19,6% de los casos) y velocidades máximas en la clase 3,6 a 5,7m/s que
corresponden principalmente a las tardes y noches, en segundo lugar está la componente SSE con
un 18,3% y velocidades máximas que alcanzan la clase 3,6 a 5,7 m/s que corresponde
principalmente a las primeras horas del día.

**24**

Anexo V-C Modelación de Dispersión de Contaminantes

En cuanto al gráfico de frecuencias por clase de intensidad de la Figura 6-17, se observa una
distribución con 7% de calmas (menor a 0,5 m/s) y con mayores frecuencias (en intensidades de
viento en la clase entre los 0,5 a 2,1 m/s con 57,5% y en segundo lugar la clase 2,1 a 3,6 m/s con
33,3% y un 1,9% en la clase 3,6 a 5,7 m/s (velocidad máxima del año 2018 es 5,5 m/s).

**Figura 6-17 Rosa del viento, Est. San Fernando, año 2018.**

Fuente: Elaboración propia con datos de SINCA.

**6.2.4** **Ciclos estacionales estación San Fernando**

Desde la Figura 6-18 a la Figura 6-22 se resume el comportamiento estacional o durante un año
calendario de las variables meteorológicas, donde en el eje vertical se ubican los meses, desde
enero (1) hasta diciembre (12) y en el eje horizontal se ubican las horas del día, desde la hora 1
hasta la hora 24. Luego para cada mes cada intersección con la columna de las horas corresponde
al valor promedio de la variable en cada hora. Además, para el ciclo estacional del viento a cada
hora se incluye una flecha que ilustra la dirección de viento predominante, desde donde viene el
viento y la punta de la flecha hacia donde se dirige.

El ciclo estacional del viento presentado en la Figura 6-18 muestra que en el general las mayores
velocidades del viento del año 2018 se producen durante la tarde con direcciones provenientes
desde el SurOeste (SO) en Verano y desde Sur en otoño-invierno. Las máximas intensidades del
viento se producen en los meses estivales, desde septiembre a febrero, entre las 16:00 y 18:00
horas, siendo más altas en los meses de noviembre a febrero con máximas cercanas a 3,0 m/s en
promedio. En meses de invierno las velocidades máximas no superan 2,0 m/s en promedio con
direcciones desde Sur. Las menores velocidades promedios de viento se registran en noche y
durante la madrugada con valores menores a 1,5 m/s siendo más bajos entre los meses de abril a
agosto. Durante noche y madrugada las direcciones de viento provienen mayoritariamente desde el
Sur en meses de primavera-verano (septiembre a marzo) y desde SE y SSE entre abril y agosto.

**25**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 6-18 Ciclo estacional del Viento, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA.

De acuerdo a la Figura 6-19, se aprecia un marcado ciclo estacional de la temperatura para el año
2018 en el cual los meses estivales presentan las mayores temperaturas durante las tardes
observándose un máximo centrado en torno a las 17:00 horas del mes de Enero cercano a 29°C en
promedio para ese mes. Durante los meses de mayo a agosto las temperaturas máximas se
registran alrededor de las 16:00 con valores cercanos a 14°C en junio y 17°C en agosto. Las
temperaturas promedios menores se presentan durante las primeras horas de la mañana, entre
06:00 y 09:00, siendo menores entre los meses Julio con un valor cercano a 4°C a las 07:00 horas.

**Figura 6-19 Ciclo estacional de Temperatura, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA.

**26**

Anexo V-C Modelación de Dispersión de Contaminantes

De acuerdo a la Figura 6-20, el ciclo estacional de la humedad relativa para el año 2018 muestra un
comportamiento inverso al ciclo de la temperatura con máximos durante la madrugada y mañana,
entre 00:00 y 09:00, siendo más altos en los meses de abril a septiembre con valores cercanos a
85% en promedio. Las humedades más bajas del día ocurren siempre en las tardes, a las horas de
mayor temperatura siendo en meses de verano los valores más bajos del año llegando a 26% de
humedad entre Diciembre y Enero y a valores de 60% en meses de invierno.

**Figura 6-20 Ciclo estacional de Humedad Relativa, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA.

De acuerdo a la Figura 6-21, el ciclo estacional de la radiación solar para el año 2018 muestra
mayores valores en horas de la tarde entre 12:00 y 16:00, específicamente en los meses estivales
(septiembre a marzo). Durante los meses de invierno el número de horas con radiación se reduce,
así como también la magnitud de la radiación recibida en la estación. En verano la radiación
promedio alcanza su valor máximo en enero con 900 W/m [2] . En cambio en meses de invierno los
máximos promedios alcanza su valor de radiación más bajo en junio con 300 W/m2. Durante meses
de otoño y primavera los máximos diarios son cercanos a 500 W/m2.

**27**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 6-21 Ciclo estacional de Radiación Solar, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA.

De acuerdo a la Figura 6-22, el ciclo estacional de la presión atmosférica está bien definido, pero
con una baja variabilidad. Los mayores valores de presión se registran en los meses de mayo a
julio, es decir meses de invierno, con valores promedios cercanos a 982 hPa. Los valores más bajos
de presión se registran en los meses de verano, es decir de diciembre a marzo, con valores
cercanos a 973 hPa. Los meses tienen un comportamiento de la presión atmosférica similar durante
el día promedio de cada mes, donde los valores más altos de presión ocurren durante dos períodos
del día, el primero alrededor de mediodía (entre 10:00 y 14:00) y el segundo en la noche (entre
21:00 y 01:00) alcanzando los valores menores durante las tardes, alrededor de las 18:00.

**Figura 6-22 Ciclo estacional de Presión Atmosférica, Estación San Fernando - 2016**

Fuente: Elaboración propia con datos de SINCA.

**28**

Anexo V-C Modelación de Dispersión de Contaminantes

**7.0** **LÍNEA BASE DE CALIDAD DEL AIRE**

A continuación, se presenta la línea de base correspondiente a calidad del aire para el área de
estudio del Proyecto en la Región del Libertador Bernardo O’Higgins, Provincia de Colchagua,
comuna de San Fernando.

**7.1** **Introducción**

En esta Sección se realiza la caracterización de la calidad del aire del Área de Influencia del
Proyecto, lo que permitirá establecer la base de referencia para la identificación y evaluación de
potenciales efectos ambientales generados por el desarrollo del Proyecto en su fase de operación.

La línea base de calidad del aire se realizó a partir de información oficial disponible para los
contaminantes MP10, MP2.5 y O3, las cuales corresponden a los contaminantes que cuentan con
normas primarias de calidad de aire.

La comuna de San Fernando fue incluida en la declaración de Zona Saturada por norma diaria y
anual de MP10 para las comunas del Valle Central de la Región de acuerdo al D.S. N°7/2009 de
MINSEGPRES. Posteriormente, en el año 2013 el D.S N°15 del Ministerio del Medio Ambiente
(MMA) estableció un Plan de descontaminación (PDA), el cual está en proceso de actualización de
acuerdo a la Res. Ex. N°669 de 2018 del MMA.

En el año 2017, la comuna de San Fernando fue incluida en la declaración de Zona Saturada por
norma diaria y anual de MP2,5 para las comunas del Valle Central de la Región de acuerdo al
Decreto N°42 del MMA. En junio de 2018 se dio inicio al proceso de un PDA de acuerdo a lo
establecido en la Res. Ex. N°503 del MMA.

**7.2** **Objetivos**

El objetivo general de la presente Línea de Base es caracterizar la calidad del aire en el Área de
Influencia definida para este componente ambiental, determinando las concentraciones actuales de
los principales contaminantes atmosféricos asociados al Proyecto, para lo cual se definieron los
siguientes objetivos específicos:

 - Analizar los registros de monitoreo disponibles de MP10, MP2,5; NO2, SO2, CO y O3.

 - Determinar la calidad del aire en relación a las concentraciones de contaminantes

analizados.

**7.3** **Área de Influencia y área de Estudio**

El Área de influencia para este componente, queda determinada por la existencia de receptores
humanos en las cercanías del Proyecto, potencialmente afectados por las posibles emisiones del
Proyecto.

Por este motivo, se consideran en el análisis la estación más cercana que corresponden a San
Fernando.

**29**

Anexo V-C Modelación de Dispersión de Contaminantes

**7.4** **Monitoreos disponibles.**

Respecto a la información de calidad de aire disponible para el área de estudio, se cuenta con
monitoreo continuo de MP10, MP2,5 y O3 en la estación San Fernando de la red del MMA, la cual
está conectada en línea con el sitio web del Sistema Nacional de Calidad del Aire (SINCA) [4] .

La ubicación de la estación de calidad de aire se ilustra en la Figura 7-1. La estación, su ubicación,
las variables monitoreadas y el período con datos disponibles se muestran en la Tabla 7-1.

**Figura 7-1. Área de estudio y Estación de monitoreo**

Fuente: Elaboración propia

**Tabla 7-1: Estación de Monitoreo y Variables Medida para período 2007 - 2018**

|N°|Receptor|Coordenadas*|Col4|Distancia<br>al Proyecto<br>(km)|Monitoreos Disponibles**|Col7|
|---|---|---|---|---|---|---|
|**N°**|**Receptor**|**Norte (m)**|**Este (m)**|**Este (m)**|**Variables**|**Período con datos**|
|1|San Fernando|6.171.746|317.503|31.8|MP10|01/04/2007 - 11/01/2019|
|1|San Fernando|6.171.746|317.503|31.8|MP2.5|23/03/2016 - 11/01/2019|
|1|San Fernando|6.171.746|317.503|31.8|O3|01/04/2007 - 11/01/2019|

 - UTM, Datum WGS 84, Huso 19 H.

** La estación está conectada en línea con datos actualizados hasta la fecha del informe, la fecha final de datos disponibles

indica hasta la fecha de consulta en SINCA.

Fuente: Elaboración propia.

4 Sistema Nacional de Calidad del Aire (SINCA), disponible en: http://sinca.mma.gob.cl

**30**

Anexo V-C Modelación de Dispersión de Contaminantes

Además de los datos disponibles en SINCA. Se cuenta con la información validada de MP2,5 para
el año 2016 de la estación San Fernando realizada por la Superintendencia del Medio Ambiente
disponible en los informes de auditoría a los datos y sus anexos en el sitio web
http://snifa.sma.gob.cl/.

Desde la Tabla 7-2 hasta la Tabla 7-4 se presentan resúmenes de los registros válidos de las
concentraciones de 24h de MP10 y MP2.5 y de las máximas diarias de concentraciones de 8horas
de O3 los cuales incluyen las concentraciones mínimas, máximas y promedio para cada año de
2015 a 2018, indicadores usados para evaluar las normas de calidad de aire. La columna N° de
registros considera todos los días con al menos una concentración válida y N° de registros válidos
son aquellos días con al menos 75% de concentraciones válidas. Todas las variables tienen
registros válidos cercanos al 100% ya que no consideran períodos de falla o ausencia de los
monitores los cuales si están considerados al calcular los registros válidos anuales.

Por otra parte, para el análisis de los datos se consideraron las normas de calidad de aire vigentes
en Chile cuyos valores límites se presentan en la Tabla 7-5.

**Tabla 7-2: Estación San Fernando - resumen registros válidos de MP2,5**

|Estación|Año|N° de<br>Registros|N°<br>Registros<br>Válidos|%<br>Registros<br>Válidos|% de<br>Registros<br>Válidos<br>Anuales|Concentraciones de 24<br>horas de MP2,5|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|<br> <br>**Estación**|**Año**|**N° de**<br>**Registros**|**N°**<br>**Registros**<br>**Válidos**|**% **<br>**Registros**<br>**Válidos**|**% de**<br>**Registros**<br>**Válidos**<br>**Anuales**|**Min**<br>**μg/m3**|**Max**<br>**μg/m3**|**Prom**<br>**μg/m3**|
|San Fernando|2015|--|--|--|--|--|--|--|
|San Fernando|2016|279|255|91,4%|69,7%|6|117|30|
|San Fernando|2017|363|354|97,5%|97,0%|3|82|21|
|San Fernando|2018|358|346|96,6%|94,8%|3|89|18|

**Tabla 7-3: Estación San Fernando - resumen registros válidos de MP10**

|Estación|Año|N° de<br>Registros|N°<br>Registros<br>Válidos|%<br>Registros<br>Válidos|% de<br>Registros<br>Válidos<br>Anuales|Concentraciones de 24<br>horas de MP10|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|<br> <br>**Estación**|**Año**|**N° de**<br>**Registros**|**N°**<br>**Registros**<br>**Válidos**|**% **<br>**Registros**<br>**Válidos**|**% de**<br>**Registros**<br>**Válidos**<br>**Anuales**|**Min**<br>**μg/m3**|**Max**<br>**μg/m3**|**Prom**<br>**μg/m3**|
|San Fernando|2015|363|357|98,3%|97,8%|10|183|47|
|San Fernando|2016|366|364|99,5%|99,5%|10|156|45|
|San Fernando|2017|364|355|97,5%|97,3%|10|107|39|
|San Fernando|2018|359|348|96,9%|95,3%|9|132|40|

**Tabla 7-4: Estación San Fernando - resumen registros válidos de O3**

|Estación|Año|N° de<br>Registros|N°<br>Registros<br>Válidos|%<br>Registros<br>Válidos|% de<br>Registros<br>Válidos<br>Anuales|Concentraciones de 8h<br>Máximas diarias de O3|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|<br> <br>**Estación**|**Año**|**N° de**<br>**Registros**|**N°**<br>**Registros**<br>**Válidos**|**% **<br>**Registros**<br>**Válidos**|**% de**<br>**Registros**<br>**Válidos**<br>**Anuales**|**Min**<br>**μg/m3**|**Max**<br>**μg/m3**|**Prom**<br>**μg/m3**|
|San Fernando|2015|365|365|100,0%|100,0%|2,0|117,9|28,00|
|San Fernando|2016|366|365|99,7%|99,7%|2,0|84,7|20,91|
|San Fernando|2017|365|363|99,5%|99,5%|2,0|116,5|27,69|
|San Fernando|2018|360|339|94,2%|92,9%|1,7|92,4|28,08|

**31**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 7-5: Normativa de referencia para la Línea de Base**

|Contaminante|Normativa|Estadígrafo|Valor límite|
|---|---|---|---|
|MP10|MP10 (D.S. N° 59/1998, MINSEGPRES.)|Promedio diario, percentil 98|150 μg/m3N|
|MP10|MP10 (D.S. N° 59/1998, MINSEGPRES.)|Media aritmética anual|50 μg/m3N|
|MP2.5|MP2.5 (D.S. N° 12/2011, MINSEGPRES.)|Promedio diario, percentil 98|50 μg/m3|
|MP2.5|MP2.5 (D.S. N° 12/2011, MINSEGPRES.)|Media aritmética anual|20 μg/m3|
|O3|O3 (D.S. N°112/2002, MINSEGPRES.)|Máx diario de 8 horas, percentil 99|120 μg/m3|

Fuente: Elaboración propia.

**7.5** **Series de Tiempo**

Desde la Figura 7-2 a la Figura 7-4 se incluyen las series de tiempo de concentraciones diarias de
MP10, MP2,5 y O3 con información disponible en la estación San Fernando. Los criterios para
validar la información son:

 - Las concentraciones diarias fueron construidas usando las concentraciones horarias,
considerando válido un día con al menos 18 concentraciones horarias válidas.

 - Las concentraciones de 8 horas se consideran válidas con al menos 6 horas válidas.

 - En el caso de las concentraciones máximas horarias de cada día se requieren al menos 18
horas válidas para validar el cálculo del valor horario máximo de ese día.

Para visualizar las concentraciones respecto a los valores establecidos en las normas en los
gráficos de MP2,5 y MP10 se han incluido los niveles límites de las normas diarias y en los gráficos
de O3 el valor límite de la norma de 8 horas. Para comparar las series se consideró el periodo 20152018.

**7.5.1** **Series de tiempo de concentraciones diarias de MP2.5**

De acuerdo a la Figura 7-2, hay un evidente comportamiento estacional de las concentraciones de
MP2,5 en San Fernando, las cuales aumentan desde Abril hasta Septiembre, alcanzando valores
máximos en Junio o Julio. Las mediciones de MP2,5 en la estación San Fernando comenzaron en
marzo del año 2016.

De acuerdo a la Figura 7-2, en la estación San Fernando durante meses de primavera-verano la
mayoría de las concentraciones diarias de MP2,5 son inferiores a 25 μg/m3, en cambio durante
meses de otoño-invierno la mayoría está en el rango 50 a 100 μg/m3, llegando a un máximo de 117
μg/m3 en junio y julio de 2016. La serie permite identificar que se supera la norma diaria al
registrarse más de 7 días al año con concentraciones mayores al límite de la norma establecido en
50 μg/m3.

**32**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 7-2. Serie de concentraciones diarias de MP2.5, San Fernando 2015 - 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

**7.5.2** **Series de tiempo de concentraciones diarias de MP10**

De acuerdo a la Figura 7-3, al igual que las concentraciones diarias de MP2,5, hay un evidente
comportamiento estacional de las concentraciones de MP10, con aumento entre Abril y Septiembre,
alcanzando valores máximos entre Junio y Julio. En meses de primavera-verano la mayoría de las
concentraciones diarias de MP10 en la estación San Fernando son inferiores a 50 μg/m3N y en
meses de otoño-invierno la mayoría de las concentraciones está en el rango de 75 a 150 μg/m3N.
La concentración más alta de MP10 se registró en mayo de 2015 con 183 μg/m3N. Desde agosto de
2016 no hay concentraciones diarias mayores al valor de la norma establecido en 150 μg/m3N.

**Figura 7-3. Serie de concentraciones diarias de MP10, San Fernando 2015 - 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

**7.5.3** **Series de tiempo de concentraciones de 8 horas de O3**

La Figura 7-4 muestra las concentraciones de 8 horas máximas de cada día para la estación San
Fernando entre los años 2015 y 2017. Se aprecia un ciclo estacional, inverso a MP10 o MP2,5; es
decir hay aumento de las concentraciones en meses de primavera-verano período durante el cual la
mayoría de los días tiene concentraciones superiores a 60 μg/m3N, alcanzando un máximo de 117,8

**33**

Anexo V-C Modelación de Dispersión de Contaminantes

μg/m3N en marzo de 2015, es decir no hay días que superen el valor de la norma de 8 horas.
Durante los meses de otoño-invierno las concentraciones de 8 horas de O3 disminuyen registrando
la mayoría de los días concentraciones inferiores a 40 μg/m3N.

**Figura 7-4. Serie de concentraciones de 8 horas máximas de O3, San Fernando - 2015 a 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

**7.6** **Ciclos diarios**

Desde la Figura 7-5 hasta la Figura 7-7 se incluyen los ciclos diarios de MP10, MP2,5 y O3 para
estudiar el comportamiento durante un día promedio del año 2018. Cada una de las figuras
considera ciclos para valores promedios y para los percentiles 5% y 95% que son indicadores
estadísticamente más estables para ilustrar el comportamiento de los valores mínimos y máximos.

La Figura 7-5 presenta el ciclo diario promedio de MP2,5 para la estación San Fernando durante el
año 2018. Se observa un ciclo diario de MP2,5 con poca variabilidad, con valores menores en la
madrugada y tarde cercanos a 14 μg/m3, en cambio los valores máximos de MP2.5 se registran en
la noche alrededor de las 21:00 cercanos a 25 μg/m3 y máximos secundarios en la mañana de 14
μg/m3 alrededor de las 09:00. Para la curva del percentil 95% los valores máximos se alcanzan
alrededor de las 23:00 con 86 μg/m3 y los menores alrededor de las 06:00 con 36 μg/m3 y de las
14:00 con 32 μg/m3. La curva del percentil 5% tiene valores mínimos en madrugada y tarde con
valores cercanos a 3 μg/m3, los máximos alcanzan 6 μg/m3 a las 07:00.

**34**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 7-5 Ciclo diario de MP2.5, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

La Figura 7-6 presenta el ciclo diario promedio de MP10 para la estación San Fernando durante el
año 2018. Se aprecia un ciclo diario de MP10 con menores valores durante la madrugada con
mínimos cercanos a 54 μg/m3N entre 03:00 y 06:00, luego un aumento hasta un máximo principal
de 88 μg/m3N alrededor de las 08:00. Durante las tardes los valores son cercanos a 55 μg/m3N
aumentando en la noche hasta 82 μg/m3N alrededor de las 22:00. El ciclo del percentil 95%
reproduce el ciclo promedio, pero con máximos principales en la noche de 233 μg/m3N a las 22:00 y
máximo secundario de 202 μg/m3N a las 08:00, los mínimos son en la tarde cercanos a 105
μg/m3N. La curva del percentil 5% presenta valores en el rango 11 a 25 μg/m3N, con mínimos en la
madrugada y máximos en la noche.

**Figura 7-6 Ciclo diario de MP10, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

**35**

Anexo V-C Modelación de Dispersión de Contaminantes

La Figura 7-7 presenta el ciclo diario de O3 para el año 2018 en la estación San Fernando. Se
aprecia un ciclo con valores más altos durante la tarde a las horas de mayor radiación solar, entre
15:00 y 17:00 y menores alrededor de las 07:00. Para el ciclo promedio de O3 los valores más altos
son cercanos a 53 μg/m3N y los menores cercanos a 11 μg/m3N. La curva del percentil 95% tiene
concentraciones máximas de 90 μg/m3N a las 15:00 y mínimas de 29 μg/m3N a las 07:00. La curva
del percentil 5% tiene concentraciones en el rango de 2 μg/m3N a 12 μg/m3N.

**Figura 7-7 Ciclo diario de O3, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

**7.7** **Ciclos Estacionales**

Desde la Figura 7-8 hasta la Figura 7-10 se presentan ciclos estacionales que corresponden a un
gráfico XY que resume el comportamiento de las concentraciones horarias durante el día promedio
para cada uno de los meses del año, donde en el eje X están las horas y en el eje Y se ubican los

meses.

La Figura 7-8 presenta el ciclo estacional para las concentraciones horarias de MP2,5 en la estación
San Fernando durante el año 2018. Se aprecia un comportamiento estacional con un aumento de
las concentraciones en los meses de mayo a agosto durante los cuales se alcanzan
concentraciones de MP2,5 más altas en las noches hasta máximos cercanos a 75 μg/m3 entre 23:00
y 24:00 del mes de junio, por otro en las mañanas se alcanzan valores cercanos a 40 μg/m3,
durante el resto del día las concentraciones son cercanas a 25 μg/m3. En meses de primavera y
verano (septiembre a abril) las concentraciones de MP2,5 se mantienen bajas en el rango de 5 a 15
μg/m3, pero no tienen un ciclo definido durante el día.

**36**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 7-8. Ciclo estacional de MP2.5, San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

De acuerdo a la Figura 7-9, el ciclo estacional para MP10 en la estación San Fernando muestra un
ciclo similar a MP2,5 con un aumento de las concentraciones en los meses de abril a septiembre
período durante el cual los mayores valores ocurren durante las noches (entre 19:00 y 02:00) y en
menor medida en las mañanas (de 08:00 a 11:00), durante las madrugadas y tardes las
concentraciones son menores en el rango de 25 a 45 μg/m3N. Las concentraciones más altas se
alcanzan en el mes de julio con 110 μg/m3N a las 22:00 y 70 μg/m3N en la mañana a las 10:00.
Entre octubre y marzo las concentraciones están en el rango de 15 a 40 μg/m3N, con poca
variabilidad durante el día, pero menores concentraciones en madrugadas y tardes.

**Figura 7-9. Ciclo estacional de MP10, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

**37**

Anexo V-C Modelación de Dispersión de Contaminantes

De acuerdo a la Figura 7-10, el ciclo estacional para O3 en la estación de San Fernando durante el
año 2018 muestra un marcado ciclo anual con similitud con el ciclo de la temperatura con mayores
concentraciones durante el período diurno, entre 09:00 y 20:00 alcanzando máximos entre 12:00 y
16:00. Entre los meses de octubre a marzo los valores más altos están en el rango de 50 a 75
μg/m3N con máximos en los meses de enero y febrero. En los meses de mayo a septiembre los
valores más altos están en el rango de 25 a 45 μg/m3N, con máximos en el mes de julio. Durante la
noche y madrugada las concentraciones de O3 entre octubre y marzo son menores a 30 μg/m3N y
entre abril y septiembre son aún más bajas con concentraciones inferiores a 10 μg/m3N.

**Figura 7-10. Ciclo estacional de O3, Estación San Fernando - 2018**

Fuente: Elaboración propia con datos de SINCA y SMA.

**7.8** **Evaluación de normas de calidad de Aire**

Las tablas y gráficos que se presentan a continuación resumen los valores o indicadores de
cumplimiento de las normas primarias de calidad de aire para MP10, MP2,5 y O3 durante el año
2018 en la estación San Fernando.

**7.8.1** **Evaluación de Normas de MP** **10**

De acuerdo a la Tabla 7-6 y a la Figura 7-11 la estación San Fernando registra en el año 2018 un
percentil 98 de las concentraciones diarias de MP10 de 100 μg/m3N, lo cual equivale a un 67% de la
norma diaria establecida en 150 μg/m3N. La concentración diaria más alta durante los últimos 3
años fue 183 μg/m3N en el año 2015.

De acuerdo a la Tabla 7-6 y a la Figura 7-11 la estación San Fernando registra concentraciones
anuales de 44 μg/m3N, 39 μg/m3N y 40 μg/m3N entre 2016 y 2018, equivalente a un promedio
trianual de 41 μg/m3N es decir un 82% de la norma anual de MP10 establecida en 50 μg/m3N.

**38**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 7-6: Monitoreo Aire MP10, Estación San Fernando, Periodo 2015 - 2018**

|Estación|Año|% de<br>Registros<br>Válidos<br>Anuales|Norma Primaria MP10 (μg/m3N)|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Estación**|**Año**|**% de**<br>**Registros**<br>**Válidos**<br>**Anuales**|**Norma Diaria**|**Norma Diaria**|**Norma Diaria**|**Norma Diaria**|**Norma Anual**|**Norma Anual**|**Norma Anual**|
|**Estación**|**Año**|**% de**<br>**Registros**<br>**Válidos**<br>**Anuales**|**Concent**<br>**24h**<br>**Mínimo**|**Concent**<br>**24h**<br>**Máximo**|**Concent**<br>**24h,**<br>**P98**|**% Norma**|**Promedio**<br>**Anual**|**Promedio**<br>**Trianual**|**% **<br>**Norma**|
|**San Fernando**|2015|97,8%|10|183|112|75%|47|||
|**San Fernando**|2016|99,5%|10|156|115|77%|44|||
|**San Fernando**|2017|97,3%|10|107|92|61%|39|43|87%|
|**San Fernando**|2018|95,3%|9|132|100|67%|40|41|82%|
|Límite Máximo Permisible<br>**150μg/m3N Percentil 98**|Límite Máximo Permisible<br>**150μg/m3N Percentil 98**|Límite Máximo Permisible<br>**150μg/m3N Percentil 98**|Límite Máximo Permisible<br>**150μg/m3N Percentil 98**|Límite Máximo Permisible<br>**150μg/m3N Percentil 98**|Límite Máximo Permisible<br>**150μg/m3N Percentil 98**|Límite Máximo Permisible<br>**150μg/m3N Percentil 98**|**50μg/m3N Promedio 3 años**|**50μg/m3N Promedio 3 años**|**50μg/m3N Promedio 3 años**|
|80% de Norma<br>**120μg/m3N**|80% de Norma<br>**120μg/m3N**|80% de Norma<br>**120μg/m3N**|80% de Norma<br>**120μg/m3N**|80% de Norma<br>**120μg/m3N**|80% de Norma<br>**120μg/m3N**|80% de Norma<br>**120μg/m3N**|**40μg/m3N**|**40μg/m3N**|**40μg/m3N**|

Fuente: Elaboración propia con datos de SINCA y SMA.

La Figura 7-11 resume el cumplimiento de la norma diaria y de la norma anual de MP10.

**Figura 7-11: Cumplimiento de norma primaria diaria (Percentil 98) y anual (promedio trianual)**
**de MP** **10** **(% de la norma)**

Fuente: Elaboración propia con datos de SINCA y SMA.

**7.8.2** **Evaluación de Normas de MP** **2.5**

De acuerdo a la Tabla 7-7 y a la Figura 7-12 el percentil 98 de las concentraciones diarias de MP2,5
de 2018 en la estación San Fernando es 63 μg/m3, lo cual equivale a un 126% de la norma diaria
establecida en 50 μg/m3. La concentración diaria más alta durante los últimos 3 años fue 117 μg/m3
en el año 2016.

De acuerdo a la Tabla 7-7 y a la Figura 7-12 en el año 2016 la estación San Fernando tiene un
69,7% de datos anuales válidos ya que tiene solo 8 meses de mediciones válidas lo cual invalida el
promedio anual de 2016 y el cálculo del promedio trianual 2016-2018. Por este motivo, se calcula un
promedio de carácter referencial con los años 2017 y 2018 de 19,5 μg/m3, el cual equivale a un 98%
de la norma anual de MP2,5 establecida en 20 μg/m3.

**39**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 7-7: Monitoreo Aire MP2.5 Estación San Fernando, Periodo 2016 - 2018**

|Estación|Año|% de<br>Registros<br>Válidos<br>Anuales|Norma Primaria MP2.5 (μg/m3)|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Estación**|**Año**|**% de**<br>**Registros**<br>**Válidos**<br>**Anuales**|**Norma Diaria**|**Norma Diaria**|**Norma Diaria**|**Norma Diaria**|**Norma Anual**|**Norma Anual**|**Norma Anual**|
|**Estación**|**Año**|**% de**<br>**Registros**<br>**Válidos**<br>**Anuales**|**Concent**<br>**24h**<br>**Mínimo**|**Concent**<br>**24h**<br>**Máximo**|**Concent**<br>**24h,**<br>**P98**|**% Norma**|**Promedio**<br>**Anual**|**Promedio**<br>**Trianual**|<br>**% **<br>**Norma**|
|**San**<br>**Fernando**|2016|69,7%|6|117|101|202%|301|||
|**San**<br>**Fernando**|2017|97,0%|3|82|70|140%|21|||
|**San**<br>**Fernando**|2018|94,8%|3|89|63|126%|18|19,52|98%|
|Límite Máximo Permisible<br>**50μg/m3 Percentil 98**|Límite Máximo Permisible<br>**50μg/m3 Percentil 98**|Límite Máximo Permisible<br>**50μg/m3 Percentil 98**|Límite Máximo Permisible<br>**50μg/m3 Percentil 98**|Límite Máximo Permisible<br>**50μg/m3 Percentil 98**|Límite Máximo Permisible<br>**50μg/m3 Percentil 98**|Límite Máximo Permisible<br>**50μg/m3 Percentil 98**|**20μg/m3N Promedio 3 años**|**20μg/m3N Promedio 3 años**|**20μg/m3N Promedio 3 años**|
|80% de Norma<br>**40** **μg/m3N**|80% de Norma<br>**40** **μg/m3N**|80% de Norma<br>**40** **μg/m3N**|80% de Norma<br>**40** **μg/m3N**|80% de Norma<br>**40** **μg/m3N**|80% de Norma<br>**40** **μg/m3N**|80% de Norma<br>**40** **μg/m3N**|**16** **μg/m3**|**16** **μg/m3**|**16** **μg/m3**|

1 Promedio anual inválido por tener menos de 9 meses válidos, solo hay 8 (abril a diciembre)

2 Promedio trianual solo de carácter referencial con promedios de años 2017 y 2018

Fuente: Elaboración propia con datos de SINCA y SMA.

La Figura 7-12 resume el cumplimiento de la norma diaria y de la norma anual de MP2,5.

**Figura 7-12: Cumplimiento de norma primaria diaria (Percentil 98) y anual (promedio trianual)**
**de MP** **2.5** **(% de la norma)**

Fuente: Elaboración propia con datos de SINCA y SMA.

**7.8.3** **Evaluación de Normas de O3**

De acuerdo a la Tabla 7-8 y a la Figura 7-13 en el año 2018 la estación San Fernando tiene un
promedio trianual (2016-2018) de las concentraciones de 8 horas máximas de cada día de O3 de
90,71 μg/m3N equivalente a un 76% de la norma de 8 horas establecida en 120 μg/m3N, valor
inferior al registrado para el período 2015-2017 de 96,13 μg/m3N.

**40**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 7-8: Monitoreo Aire O3, Est. San Fernando, Periodo 2015 - 2018**

|Estación|Año|% de<br>Registros<br>Válidos<br>Anuales|Norma Primaria O3 (μg/m3N)|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Estación|Año|% de<br>Registros<br>Válidos<br>Anuales|Norma 8 horas|Norma 8 horas|Norma 8 horas|Norma 8 horas|Norma 8 horas|
|Estación|Año|% de<br>Registros<br>Válidos<br>Anuales|Concent<br>8horas<br>Mínimo|Concent<br>8horas<br>Máximo|Concent<br>8horas,<br>P99|Promedio<br>Trianual|% <br>Norma|
|**San**<br>**Fernando**|2015|100,0%|2,0|117,9|105,4|--|--|
|**San**<br>**Fernando**|2016|99,7%|2,0|84,7|81,5|--|--|
|**San**<br>**Fernando**|2017|99,5%|2,0|116,5|101,5|96,13|80%|
|**San**<br>**Fernando**|2018|92,9%|1,7|92,4|89,2|90,71|76%|
|Límite Máximo Permisible<br>**120 μg/m3N Percentil 99**|Límite Máximo Permisible<br>**120 μg/m3N Percentil 99**|Límite Máximo Permisible<br>**120 μg/m3N Percentil 99**|Límite Máximo Permisible<br>**120 μg/m3N Percentil 99**|Límite Máximo Permisible<br>**120 μg/m3N Percentil 99**|Límite Máximo Permisible<br>**120 μg/m3N Percentil 99**|Límite Máximo Permisible<br>**120 μg/m3N Percentil 99**|Límite Máximo Permisible<br>**120 μg/m3N Percentil 99**|
|80% de Norma<br>**96 μg/m3N**|80% de Norma<br>**96 μg/m3N**|80% de Norma<br>**96 μg/m3N**|80% de Norma<br>**96 μg/m3N**|80% de Norma<br>**96 μg/m3N**|80% de Norma<br>**96 μg/m3N**|80% de Norma<br>**96 μg/m3N**|80% de Norma<br>**96 μg/m3N**|

Fuente: Elaboración propia con datos de SINCA.

La Figura 7-13 resume el cumplimiento de la norma de 8 horas de O3 para la estación San
Fernando.

**Figura 7-13: Cumplimiento de norma primaria de 8 horas de O3 (Percentil 99) (% de la norma)**

Fuente: Elaboración propia con datos de SINCA.

**41**

Anexo V-C Modelación de Dispersión de Contaminantes

**8.0** **MODELACION DE CALIDAD DEL AIRE Y RESULTADOS**

**8.1** **Aportes del Proyecto**

En la Tabla 8-1 y las figuras siguientes de iso-líneas de concentración se muestran los aportes
modelados del Proyecto, en la etapa de operación en los receptores puntuales considerados y en el
Punto de Máximo Aporte (PMA).

El PMA se ubica cerca del Proyecto o en vías no pavimentadas de acceso al Proyecto, alejadas de
los receptores puntuales. Sin embargo, los aportes son de muy baja magnitud no superando
respecto a material particulado MP10 el 4% del nivel de la norma, y respecto a MP2.5 el 1% del
nivel de la norma. Respecto a gases el aporte también es muy reducido no superando el 6% del
nivel de la norma.

Acerca de los aportes del Proyecto en los receptores, se observa lo siguiente:

 - El máximo aporte del Proyecto en términos de concentración de MP10 promedio de 24
horas, percentil 98, se producirá en el receptor La Rufina. Sin embargo, este no supera el
0,6 μg/m [3] equivalente a 0% de la norma. Lo que se puede considerar un aporte
prácticamente nulo.

 - El máximo aporte del Proyecto en términos de concentración de MP10 promedio anual, se
producirá en el receptor La Rufina. Sin embargo, este no supera el 0,1 μg/m [3] equivalente a
0% de la norma. Lo que se puede considerar un aporte prácticamente nulo.

 - El máximo aporte del Proyecto en términos de concentración de MP2.5 promedio de 24
horas, percentil 98, se producirá en el receptor La Rufina. Sin embargo, este no supera el
0,1 μg/m [3] equivalente a 0% de la norma. Lo que se puede considerar un aporte
prácticamente nulo.

 - El aporte del Proyecto en términos de concentración de MP2.5 promedio anual, en todos los
receptores, será menor al 0,0 μg/m [3] y 0% de la norma. Lo que se puede considerar un
aporte nulo.

 - El máximo aporte del Proyecto en términos de concentración de NO 2 promedio de 1 hora,
percentil 99, se producirá en el receptor La Rufina. Sin embargo, este no supera el 0,1
μg/m [3] equivalente a 0% de la norma. Lo que se puede considerar un aporte prácticamente
nulo.

 - El aporte del Proyecto en términos de concentración de NO 2 promedio anual, en todos los
receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser considerado un aporte nulo.

 - El aporte del Proyecto en términos de concentración de SO 2 promedio de 24 horas, percentil
99, en todos los receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser
considerado un aporte nulo.

 - El aporte del Proyecto en términos de concentración de SO 2 promedio anual, en todos los
receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser considerado un aporte nulo.

 - El aporte del Proyecto en términos de concentración de CO 1 hora, percentil 99, en todos
los receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser considerado un aporte
nulo.

 - El máximo aporte del Proyecto en términos de concentración de CO promedio de 8 horas,
percentil 99, en todos los receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser
considerado un aporte nulo.

**42**

Anexo V-C Modelación de Dispersión de Contaminantes

**Tabla 8-1: Aporte del Proyecto en los receptores puntuales y punto de máximo aporte (PMA)**

|Tipo|Cont.|Estadígrafo|Límite|Est. San<br>Fernando|Col6|Puente Negro|Col8|La Rufina|Col10|Termas El<br>Flaco|Col12|Punto de<br>Máximo<br>Aporte (PMA)|Col14|Nota|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo**|**Cont.**|**Estadígrafo**|**μg/m3 **|**μg/m3 **|**% **<br>**norma**|**μg/m3 **|**% **<br>**norma**|**μg/m3 **|**% **<br>**norma**|**μg/m3 **|**% **<br>**norma**|**μg/m3 **|**% **<br>**norma**|**% **<br>**norma**|
|**Norma Primaria de Calidad del**<br>**Aire**|MP10|24 horas, P98|150|0,0|0%|0,2|0%|0,6|0%|0,0|0%|5,4|4%|1|
|**Norma Primaria de Calidad del**<br>**Aire**|MP10|Anual|50|0,0|0%|0,0|0%|0,1|0%|0,0|0%|0,8|2%|2|
|**Norma Primaria de Calidad del**<br>**Aire**|MP2.5|24 horas, P98|50|0,0|0%|0,0|0%|0,1|0%|0,0|0%|0,5|1%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|MP2.5|Anual|20|0,0|0%|0,0|0%|0,0|0%|0,0|0%|0,1|0%|1|
|**Norma Primaria de Calidad del**<br>**Aire**|NO2|1 hora, P99|400|0,0|0%|0,0|0%|0,1|0%|0,1|0%|25,7|6%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|NO2|Anual|100|0,0|0%|0,0|0%|0,0|0%|0,0|0%|0,8|1%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|SO2|24 horas, P99|250|0,0|0%|0,0|0%|0,0|0%|0,0|0%|0,0|0%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|SO2|Anual|80|0,0|0%|0,0|0%|0,0|0%|0,0|0%|0,0|0%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|CO|1 hora, P99|30.000|0,0|0%|0,0|0%|0,0|0%|0,0|0%|5,4|0%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|CO|8 horas, P99|10.000|0,0|0%|0,0|0%|0,0|0%|0,0|0%|3,5|0%|3|

Nota 1: El punto de máximo aporte (PMA) se ubica en el camino no pavimentado a 2,5 km al Sur Este de La Rufina, en UTM: 341.798 m Este, 6.152.539 m Sur.

Nota 2: El punto de máximo aporte (PMA) se ubica cerca del camino no pavimentado a 1,7 km al Sur Este de Puente Negro, en UTM: 329.789 m Este, 6.158.539 m Sur.

Nota 3: El punto de máximo aporte (PMA) se ubica a 0,5 km al sur del Proyecto, en UTM: 357.789 m Este, 6.143.539 m Sur.

Fuente: Elaboración propia

**43**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-1: Curva de Iso-concentración, MP10, 24 horas, P98.**

**44**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-2: Curva de Iso-concentración, MP10, anual.**

**45**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-3: Curva de Iso-concentración, MP2.5, 24 horas, P98.**

**46**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-4: Curva de Iso-concentración, MP2.5, Anual.**

**47**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-5: Curva de Iso-concentración, NO2, 1 hora P99.**

**48**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-6: Curva de Iso-concentración, NO2, Anual.**

**49**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-7: Curva de Iso-concentración, SO2, 24 horas, P99.**

**50**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-8: Curva de Iso-concentración, SO2, anual.**

**51**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-9: Curva de Iso-concentración, CO, 1 hora P99.**

**52**

Anexo V-C Modelación de Dispersión de Contaminantes

**Figura 8-10: Curva de Iso-concentración, CO, 8 horas, P99.**

**53**

Anexo V-C - Modelación de Dispersión de Contaminantes

**8.2** **Análisis de incertidumbre y determinación de factores de**
**corrección de concentraciones modeladas.**

**8.2.1** **Análisis de datos meteorológicos modelados con WRF v/s datos**
**observacionales disponibles para año 2018**

Considerando la información disponible, a continuación, se presenta un análisis comparativo de la
representatividad del campo de viento modelado con WRF durante el año 2018, respecto de los
datos observados en la Estación San Fernando, los cuales corresponden a los datos observados
más cercanos al proyecto dentro del dominio de modelación. La comparación se realizó para el año
2018.

En la Figura 8-11 y Figura 8-12 se presenta el ciclo diario de intensidades del viento Observado y
Simulado respectivamente, incluyendo en los gráficos los ciclos diarios para valor promedio o
media, percentil 5% y percentil 95%.

Se puede apreciar que el ciclo diario en el modelo WRF (simulado) tiene un comportamiento similar
durante madrugada, mañana y tarde. Durante todo el ciclo las intensidades modeladas son mayores
a las intensidades de viento observadas. En promedio la intensidad de viento observada tiene un
valor de 1,70 m/s, en cambio el promedio de la intensidad del viento simulado es 2.52 m/s.

**Figura 8-11: Ciclo diario de magnitud del viento San Fernando, 2018 (observado).**

Fuente: Elaboración propia

El ciclo promedio simulado presentado en la Figura 8-12 tiene valores menores en la madrugada
alcanzando un mínimo de 1,7 m/s alrededor de las 09:00. Durante la tarde se alcanzan máximos de
3,5 m/s alrededor de las 18:00, luego en la noche las velocidades descienden hasta 2,5 m/s
alrededor de las 00:00. En cambio, el ciclo promedio observado tiene valores bajos en noche y
madrugada cercanos a 1,3 m/s y máximos en la tarde de 2,4 m/s a las 17:00.

El ciclo del percentil 95% Simulado, al igual que el observado tiene un período de mayores
velocidades de viento en la tarde, cercanos a 5,4 m/s a las 18:00, más alto que el máximo
observado de 3,6 m/s a las 17:00, durante la mañana y noche se alcanzan mínimos modelados de
3,8 m/s y 4,2 m/s respectivamente superiores a los valores mínimos observados de 2,4 m/s en la

**54**

Anexo V-C - Modelación de Dispersión de Contaminantes

madrugada. El ciclo del percentil 5% simulado tiene máximos en la tarde de 1,5 m/s a las 18:00 y
cercanos a 0,2 en madrugada, en cambio el ciclo del percentil 5% observado tiene valores en el
rango de 0,1 a 0,9 m/s en las tardes y 0,2 en el resto del día.

**Figura 8-12: Ciclo diario de magnitud del viento San Fernando, 2018 (simulado).**

Fuente: Elaboración propia

La Figura 8-13 y la Figura 8-14 muestran el porcentaje de ocurrencia de la dirección del viento para
el viento Observado y Simulado respectivamente. Se aprecia que el modelo logra representar de
manera parcial el ciclo observado durante las primeras horas del día (hasta las 10:00) cuando la
dirección predominante observada es desde SurSurEste(SSE) y SurOeste (SO) con una frecuencia
máxima de 26% entre 04:00 y 06:00 desde SSE modelando entre 00:00 y 04:00 una componente
principal desde OesteSurOeste (OSO) con frecuencia máxima de 24%, entre 04:00 y 08:00 la
componente principal es Sur (S) con frecuencia máxima de 24%, entre 08:00 y 10:00 hay transición
hacia régimen diurno. Desde las 10:00 hasta las 18:00 hay una marcada dirección predominante SO
que alcanza un máximo de 56% a las 14:00, subestimando la componente SSE observada la cual
tiene una frecuencia cercana a 0%. Desde las 19:00 hasta las 23:00 la componente observada SO
con frecuencia máxima de 34% es modelada rotada hacia el Oeste, es decir componente OSO con
una frecuencia máxima de 44%, en este horario la componente secundaria observada SE es
modelada como componente S con un máximo de 20%.

**55**

Anexo V-C - Modelación de Dispersión de Contaminantes

**Figura 8-13. Ciclo diario de dirección del viento, porcentaje de ocurrencia (%), Estación San**

**Fernando - 2018 (observado).**

Fuente: Elaboración propia

**Figura 8-14. Ciclo diario de dirección del viento, porcentaje de ocurrencia (%), Estación San**

**Fernando - 2018 (simulado).**

Fuente: Elaboración propia

En la Figura 8-15 y Figura 8-16 se presenta el ciclo diario de la dirección del viento representado en
rosas de direcciones para el viento Observado y Simulado. Además, se incluye una cuantificación
de las velocidades de viento en diferentes clases de viento (calma o menor a 0,5 m/s; 0,5 a 2,1 m/s;
2,1 a 3,6 m/s; 3,6 a 5,7 m/s; 5,7 a 8,8 m/s; 8,8 a 11 m/s y mayores a 11 m/s) para cada uno de los
16 sectores considerados en las rosas de viento.

**56**

Anexo V-C - Modelación de Dispersión de Contaminantes

|Calmas:11,8%<br>Rosa de Viento Período 00:00 a 05:00 horas|Calmas:7,7%<br>Rosa de Viento Período 06:00 a 11:00 horas|
|---|---|
|<br>Rosa de Viento Período 12:00 a 17:00 horas <br>Calmas:2,2%|<br>Rosa de Viento Período 18:00 a 23:00 horas<br>Calmas:6,2%|

Viento (m/s):

**Figura 8-15 Rosa del viento, ciclo diario, Estación San Fernando, 2018 (Observado)**

Fuente: Elaboración propia

**57**

Anexo V-C - Modelación de Dispersión de Contaminantes

|Calmas:4,9%<br>Rosa de Viento Período 00:00 a 05:00 horas|Calmas:10,0%<br>Rosa de Viento Período 06:00 a 11:00 horas|
|---|---|
|<br>Rosa de Viento Período 12:00 a 17:00 horas <br>Calmas:1,1%|<br>Rosa de Viento Período 18:00 a 23:00 horas<br>Calmas:0,8%|

Viento (m/s):

**Figura 8-16 Rosas de viento año 2018, Estación San Fernando, 2018 (simulado)**

Fuente: Elaboración propia

De acuerdo a las rosas de viento presentadas en la Figura 8-15 y en la Figura 8-16. Entre las 00:00
y 05:00 horas, las direcciones de viento provienen principalmente desde sectores de SurESte (SE) a
SurOeste (SO) con un predominio de la componente SSE con un 24% de los casos, seguido de SE
con un 17% y en tercer lugar SO con un 14% son modelados rotados hacia el Oeste con una
sobrestimación de la componente S que alcanza la mayor frecuencia con 23%, en segundo lugar el
sector OSO con un 19% y SO con 15%. El modelo estima un 4,9% de calma respecto al 11,8%
observado. Las velocidades de viento son modeladas con intensidades mayores a las observadas,

**58**

Anexo V-C - Modelación de Dispersión de Contaminantes

con un 46,8% en la clase 0,5 a 2,1 m/s, un 33,7% en la clase 2,1 a 3,6 m/s, un 13,5% en la clase 3,6
a 5,7 m/s, un 1,1% en la clase de 5,7 a 8,8 m/s y un 0.1% >11 m/s. En el viento observado un 69%
está en la clase 0,5 a 2,1 m/s.

Entre las 06:00 y 11:00 horas, los vientos observados se mantienen principalmente desde sectores
de SurESte (SE) a SurOeste (SO), pero con una disminución del porcentaje de frecuencias de
componente SSE hasta 17%, aumentando SE hasta 20% y se mantienen en tercer lugar SO con
15%. Las direcciones son modeladas principalmente entre S y OSO sobrestimando la componente
SO que alcanza la mayor frecuencia con 36,6%, seguido de SSO con 18,1% y S con 10,9%. El
modelo estima un 10,0% de calma similar al 7,7% observado. Las velocidades de viento son
modeladas con intensidades mayores a las observadas, con un 49,5% en la clase 0,5 a 2,1 m/s, un
32,1% en la clase 2,1 a 3,6 m/s, un 6,7% en la clase 3,6 a 5,7 m/s, un 1,2% en la clase de 5,7 a 8,8
m/s y un 0,5 en la clase 8,8 a 11,0 m/s. En el viento observado hay un 67% de las velocidades en la
clase 0,5 a 2,1 m/s, un 25% en la clase 2,1 a 3,6 m/s y un 0,7% alcanzan velocidades más en la
clase de 3,6 a 5,7 m/s

Entre las 12:00 y 17:00 horas el modelo representa en forma aceptable las direcciones
predominantes observadas desde sectores SO con 25%, pero subestima las direcciones desde S a
SE que en conjunto suman un 38% observado las cuales son modeladas con un 48% para SO, 21%
para OSO, 9% para SSO y menos de un 4% para las direcciones de S a SE. El modelo estima un
1,1% de calma similar al 2,2% observado. Las velocidades de viento son modeladas con
intensidades mayores a las observadas, con un 19,5% en la clase 0,5 a 2,1 m/s, un 47,7% en la
clase 2,1 a 3,6 m/s, un 28,2% en la clase 3,6 a 5,7 m/s, un 3,0% en la clase de 5,7 a 8,8 m/s y un
0,3 en la clase 8,8 a 11 m/s. En el viento observado hay un 35% de las velocidades en la clase 0,5 a
2,1 m/s, un 57% en la clase 2,1 a 3,6 m/s y un 5% alcanzan velocidades más en la clase de 3,6 a
5,7 m/s

Entre las 18:00 y 23:00 horas, el modelo representa en forma parcial las direcciones predominantes
desde SO a S, con un máximo observado de SO con 24%, pero subestima las direcciones desde S
a SE que en conjunto suman un 40% observado las cuales son modeladas con un 37% para OSO,
18% para SO, 14% para SSO, 11% para S y menos de un 3% para las direcciones de SSE a SE. El
modelo estima un 0,8% de calma inferior al 6,2% observado Las velocidades de viento son
modeladas con intensidades mayores a las observadas, con un 24,9% en la clase 0,5 a 2,1 m/s, un
40,6% en la clase 2,1 a 3,6 m/s, un 32,1% en la clase 3,6 a 5,7 m/s, un 1,3% en la clase de 5,7 a
8,8 m/s, un 0,2 en la clase 8,8 a 11 m/s y un 0,05% mayor a 11 m/s. En el viento observado hay un
59% de las velocidades en la clase 0,5 a 2,1 m/s y un 33% en la clase 2,1 a 3,6 m/s.

En la Figura 8-17 y Figura 8-18 se muestra ciclos estacionales Observado y Simulado para el año
2018. Las componentes predominantes desde el SurOeste durante las tardes, a las horas de mayor
velocidad (entre 13:00 y 19:00) durante los meses de Primavera-Verano y desde Sur en meses de
Abril a Agosto son modeladas como componentes SO durante todo el año, sobrestimando las
velocidad de viento con máximos de 4,6 m/s respecto a 3,0 m/s observado. Desde las 19:00 hasta
medianoche, las velocidades en meses de verano con cercanas a 2 m/s y cercanas a 1,3 m/s en
meses de otoño-invierno, además la dirección desde S en la mayoría de los casos es modelada
rotada como SO en meses de primavera-verano y SSO en meses de otoño-invierno. Durante las
primeras horas del día, entre 01:00 y 10:00 la dirección predominante observada es S entre
septiembre y marzo y desde SE entre abril y agosto con velocidades del viento observada menor a
1,5 m/s con menores valores entre abril y agosto. En cambio, la dirección de viento modelada es S
en la mayoría de los meses con velocidad de viento menor a 2,5 m/s desde octubre a marzo y a
diferencia de lo observado hay un aumento de la intensidad entre abril y agosto a valores cercanos
a 3,0 m/s.

**59**

Anexo V-C - Modelación de Dispersión de Contaminantes

**Figura 8-17 Ciclo estacional del viento, Estación San Fernando, Año 2018 (observado)**

Fuente: Elaboración propia

**Figura 8-18 Ciclo estacional del viento, Estación San Fernando, año 2018 (simulado)**

Fuente: Elaboración propia

**8.2.2** **Análisis de incertidumbre.**

Para determinar el grado de incertidumbre asociado a la modelación meteorológica, se realizó un
análisis comparativo de los datos simulados y los observados de magnitud del viento en la Estación

**60**

Anexo V-C - Modelación de Dispersión de Contaminantes

San Fernando para el año 2018, esto debido a que la magnitud del viento es la variable de mayor
efecto en los procesos de dispersión.

La variación entre la meteorología observada y simulada se obtiene restando el promedio de la
intensidad del viento simulada con el promedio de la intensidad del viento observada en la estación.

Finalmente, se determina el ponderador de corrección de las concentraciones modeladas con
CALPUFF, a partir de la diferencia en la intensidad del viento, en la dirección asociada al transporte
de los contaminantes desde la fuente a los receptores puntuales evaluados.

En la Tabla 8-2 se expone el análisis comparativo de intensidad del viento observada y modelada.
Considerando las diferencias observadas en el comportamiento diurno y nocturno, se ha realizado el
análisis para estos dos períodos, estando el periodo diurno comprendido entre las 10:00 y 21:00
horas y el nocturno, entre las 22:00 y 09:00 horas

Las variaciones porcentuales negativas indican intensidad del viento simulada por el modelo WRF
menor a la observada (subestimación), mientras que las positivas indican sobrestimación.

En la Tabla 8-2 se puede apreciar que las diferencias entre lo observado y lo modelado con WRF
están dentro de los rangos esperados para este tipo de modelaciones. Considerando el promedio
del año 2018, el modelo sobre estima la intensidad del viento, tanto en el período diurno como
nocturno, siendo más alta la sobrestimación durante la noche que corresponde al período del día
cuando la intensidad del viento disminuye.

**Tabla 8-2: Diferencia entre intensidad del viento observada y modelada en Estación San**

**Fernando, año 2018**

|Estación|Observado<br>(m/s)|Modelado (WRF)<br>(m/s)|Diferencia Mod-Obs<br>(m/s)|Variación Porcentual<br>%|
|---|---|---|---|---|
|San Fernando|1,70|2,52|0,82|48,0%|
|San Fernando diurno|2,00|2,83|0,82|41,0%|
|San Fernando nocturno|1,40|2,21|0,81|58,0%|

Fuente: Elaboración propia

En la Tabla 8-3, se analiza la diferencia del viento modelado con WRF respecto al observado para la
Estación San Fernando, en función de su dirección, para lo cual se ha dividido la rosa de los vientos
en cuadrantes, analizándose tanto el periodo diurno como el nocturno. Se aprecia que, tanto para el
período diurno como nocturno, el modelo sobre estima las velocidades, excepto para el cuadrante
90-180°. Sin embargo, los valores pueden considerarse un buen acierto para el nivel de acierto que
puede tener el modelo WRF.

Conforme a lo anterior, se puede concluir respecto a la Estación San Fernando que las predicciones
del modelo WRF necesitan ligeras correcciones, teniendo en general un buen acierto en la
predicción de las magnitudes del viento.

Considerando que, a menor velocidad del viento, la dispersión es también es menor, si el modelo
WRF tiende en general a sobrevalorar la intensidad del viento, la modelación con Calpuff tenderá
por lo tanto a subestimar las concentraciones y vice versa.

**61**

Anexo V-C - Modelación de Dispersión de Contaminantes

**Tabla 8-3: Diferencia de intensidad del viento observada y modelada en Estación San**

**Fernando por dirección, año 2018**

|Dirección<br>viento<br>(grados)|Diurno|Col3|Col4|Col5|Nocturno|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**<br>**viento**<br>**(grados)**|Observado<br>(m/s)|WRF<br>(m/s)|Diferencia<br>(m/s)|Variación<br>Porcentual<br>%|Observado<br>(m/s)|WRF<br>(m/s)|Diferencia<br>(m/s)|Variación<br>Porcentual<br>%|
|0-90|1,06|3,48|2,42|227,1%|0,83|2,21|1,38|165,2%|
|90-180|2,07|1,34|-0,73|-35,4%|1,56|1,16|-0,40|-25,5%|
|180-270|2,08|2,80|0,73|35,0%|1,43|2,50|1,07|74,9%|
|270-360|2,28|3,47|1,19|52,0%|0,94|2,34|1,40|148,5%|

Fuente: Elaboración propia

**8.2.3** **Factores de corrección.**

A continuación, se determinan los factores de corrección de las concentraciones modeladas con
CALPUFF, en los distintos receptores considerados, a partir del análisis de la variación de
intensidad del viento ya analizado.

El factor de corrección se obtiene considerando que existe una relación lineal entre el viento
estimado por WRF y el observado que responde a la siguiente ecuación.

V WRF = FC × V Obsev (Ecuación 1)

Es decir,

FC = V WRF / V Obsev (Ecuación 2)

Dónde:

V WRF : Magnitud del viento modelada por WRF.

V Observ : Magnitud del viento observada.

FC : Factor de corrección de intensidad del viento observada.

Por otra parte, existe una relación directa entre la magnitud del viento y la capacidad de dispersión
de la atmosfera, es decir, a medida que aumenta la magnitud del viento, aumenta también la
capacidad de dispersión de contaminantes de la atmósfera. Asimismo, la relación entre la magnitud
del viento y la concentración a esperar en los receptores es inversa, es decir, a mayor magnitud del
viento es de esperar menores concentraciones en los receptores.

Lo anterior implicaría, que si durante la modelación de las emisiones se utiliza una magnitud del
viento (V WRF ), mayor a la que realmente ocurre en la zona de modelación (V obs ), el modelo tenderá a
predecir concentraciones menores a las que realmente ocurrirán, debiéndose por lo tanto aumentar
por un factor las concentraciones predichas para aproximarse mejor a las concentraciones que
ocurrirán realmente. Este factor coincide con el que tendríamos que utilizar para corregir la menor
magnitud real del viento (V obs ), de modo que coincida con la magnitud utilizada en el modelo (V WRF ).

Por lo tanto, la corrección de las concentraciones modeladas quedaría expresada a partir de la
siguiente ecuación, donde el factor FC, puede ser obtenido de la comparación del viento real
observado, con el utilizado en el modelo, a partir de la Ecuación 2.

**62**

Anexo V-C - Modelación de Dispersión de Contaminantes

C Corr = FC × C Calpuff (Ecuación 3)

Dónde:

C Corr : Concentración corregida.

C CALPUFF : Concentración estimada por CALPUFF.

FC : Factor de corrección de concentración de CALPUFF que es igual al factor de corrección
de intensidad del viento observada.

Aplicando la Ecuación 2, a los datos de la Tabla 8-3 de la Estación San Fernando, se obtienen los
factores de corrección de intensidad del viento y concentración de la Tabla 8-4, en cual corresponde
a un factor de 1,80. Es decir un aumento en 180% del impacto modelado.

**Tabla 8-4: Factor de corrección (FC) calculado de la diferencia de intensidad del viento en**

**Estación San Fernando, año 2018**

|Dirección<br>viento<br>(grados)|Diurno|Col3|Col4|Nocturno|Col6|Col7|Factor Correción|
|---|---|---|---|---|---|---|---|
|**Dirección**<br>**viento**<br>**(grados)**|**Observado**<br>**(Vobs) **|**WRF**<br>**(VWRF) **|**Factor de**<br>**Corrección**<br>**(VWRF/Vobs) **|**Observado**|**WRF**|**Factor de**<br>**Corrección**<br>**(VWRF/Vobs) **|**Promedio**<br>**(nocturno y**<br>**diurno)**|
|**Dirección**<br>**viento**<br>**(grados)**|**(m/s)**|**(m/s)**|**(m/s)**|**(m/s)**|**(m/s)**|**(m/s)**|**m/s**|
|0-90|1,06|3,48|3,27|0,83|2,21|2,65|2,96|
|90-180|2,07|1,34|0,65|1,56|1,16|0,75|0,70|
|180-270|2,08|2,80|1,35|1,43|2,50|1,75|1,55|
|270-360|2,28|3,47|1,52|0,94|2,34|2,49|2,00|
|**Promedio (Factor Corrección Calpuff) :**|**Promedio (Factor Corrección Calpuff) :**|**Promedio (Factor Corrección Calpuff) :**|**Promedio (Factor Corrección Calpuff) :**|**Promedio (Factor Corrección Calpuff) :**|**Promedio (Factor Corrección Calpuff) :**|**Promedio (Factor Corrección Calpuff) :**|**1,80**|

Fuente: Elaboración propia

**8.3** **Aportes Corregidos del Proyecto**

En la Tabla 8-5 se muestran los aportes modelados corregidos del Proyecto, en la etapa de
operación en los receptores puntuales considerados y en el Punto de Máximo Aporte (PMA). El
aporte corregido se ha obtenido multiplicando los aportes modelados presentados en el capítulo 8.1,
corregidos por el factor 1,8 calculado en el capítulo 8.2.

El PMA se ubica cerca del Proyecto o en vías no pavimentadas de acceso al Proyecto, alejadas de
los receptores puntuales. Sin embargo, los aportes son de muy baja magnitud no superando
respecto a material particulado MP10 el 7% del nivel de la norma, y respecto a MP2.5 el 2% del
nivel de la norma. Respecto a gases el aporte también es muy reducido no superando el 12% del
nivel de la norma.

Acerca de los aportes del Proyecto en los receptores, se observa lo siguiente:

 - El máximo aporte del Proyecto en términos de concentración de MP10 promedio de 24
horas, percentil 98, se producirá en el receptor La Rufina. Sin embargo, este no supera el
1,1 μg/m [3] equivalente a 1% de la norma. Lo que se puede considerar un aporte
prácticamente nulo.

 - El máximo aporte del Proyecto en términos de concentración de MP10 promedio anual, se
producirá en el receptor La Rufina. Sin embargo, este no supera el 0,2 μg/m [3] equivalente a
0% de la norma. Lo que se puede considerar un aporte prácticamente nulo.

**63**

Anexo V-C - Modelación de Dispersión de Contaminantes

- El máximo aporte del Proyecto en términos de concentración de MP2.5 promedio de 24
horas, percentil 98, se producirá en el receptor La Rufina. Sin embargo, este no supera el
0,1 μg/m [3] equivalente a 0% de la norma. Lo que se puede considerar un aporte
prácticamente nulo.

- El aporte del Proyecto en términos de concentración de MP2.5 promedio anual, en todos los
receptores, será menor al 0,0 μg/m [3] y 0% de la norma. Lo que se puede considerar un
aporte nulo.

- El máximo aporte del Proyecto en términos de concentración de NO 2 promedio de 1 hora,
percentil 99, se producirá en el receptor La Rufina. Sin embargo, este no supera el 0,1
μg/m [3] equivalente a 0% de la norma. Lo que se puede considerar un aporte prácticamente
nulo.

- El aporte del Proyecto en términos de concentración de NO 2 promedio anual, en todos los
receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser considerado un aporte nulo.

- El aporte del Proyecto en términos de concentración de SO 2 promedio de 24 horas, percentil
99, en todos los receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser
considerado un aporte nulo.

- El aporte del Proyecto en términos de concentración de SO 2 promedio anual, en todos los
receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser considerado un aporte nulo.

- El aporte del Proyecto en términos de concentración de CO 1 hora, percentil 99, en todos
los receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser considerado un aporte
nulo.

- El máximo aporte del Proyecto en términos de concentración de CO promedio de 8 horas,
percentil 99, en todos los receptores será a menos del 0,0 μg/m [3] y 0%. Lo que puede ser
considerado un aporte nulo.

**64**

Anexo V-C - Modelación de Dispersión de Contaminantes

**Tabla 8-5: Aporte corregido del Proyecto en los receptores puntuales y punto de máximo aporte (PMA)**

|Tipo|Contaminante|Estadígrafo|Límite|Est. San<br>Fernando|Col6|Puente Negro|Col8|La Rufina|Col10|Termas El<br>Flaco|Col12|Punto de<br>Máximo<br>Aporte (PMA)|Col14|Nota|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo**|**Contaminante**|**Estadígrafo**|**μg/m3 **|**μg/m3 **|**% **<br>**norma**|**μg/m3 **|**% **<br>**norma**|**μg/m3 **|**% **<br>**norma**|**μg/m3 **|**% **<br>**norma**|**μg/m3 **|**% **<br>**norma**|**% **<br>**norma**|
|**Norma Primaria de Calidad del**<br>**Aire**|MP10|24 horas, P98|150|0,0|0%|0,4|0%|1,1|1%|0,0|0%|9,8|7%|1|
|**Norma Primaria de Calidad del**<br>**Aire**|MP10|Anual|50|0,0|0%|0,0|0%|0,2|0%|0,0|0%|1,4|3%|2|
|**Norma Primaria de Calidad del**<br>**Aire**|MP2.5|24 horas, P98|50|0,0|0%|0,0|0%|0,1|0%|0,0|0%|1,0|2%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|MP2.5|Anual|20|0,0|0%|0,0|0%|0,0|0%|0,0|0%|0,1|1%|1|
|**Norma Primaria de Calidad del**<br>**Aire**|NO2|1 hora, P99|400|0,0|0%|0,0|0%|0,1|0%|0,1|0%|46,3|12%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|NO2|Anual|100|0,0|0%|0,0|0%|0,0|0%|0,0|0%|1,5|1%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|SO2|24 horas, P99|250|0,0|0%|0,0|0%|0,0|0%|0,0|0%|0,0|0%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|SO2|Anual|80|0,0|0%|0,0|0%|0,0|0%|0,0|0%|0,0|0%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|CO|1 hora, P99|30.000|0,0|0%|0,0|0%|0,0|0%|0,0|0%|9,8|0%|3|
|**Norma Primaria de Calidad del**<br>**Aire**|CO|8 horas, P99|10.000|0,0|0%|0,0|0%|0,0|0%|0,0|0%|6,4|0%|3|

Nota 1: El punto de máximo aporte (PMA) se ubica en el camino no pavimentado a 2,5 km al Sur Este de La Rufina, en UTM: 341.798 m Este, 6.152.539 m Sur.

Nota 2: El punto de máximo aporte (PMA) se ubica cerca del camino no pavimentado a 1,7 km al Sur Este de Puente Negro, en UTM: 329.789 m Este, 6.158.539 m Sur.

Nota 3: El punto de máximo aporte (PMA) se ubica a 0,5 km al sur del Proyecto, en UTM: 357.789 m Este, 6.143.539 m Sur.

Fuente: Elaboración propia

**65**

Anexo V-C - Modelación de Dispersión de Contaminantes

**8.4** **Evaluación de Cumplimiento de Normativa**

A continuación, se realiza una evaluación de cumplimiento de normativa de calidad del aire,
considerando la línea base monitoreada en la estación San Fernando y los aportes modelados
corregidos del Proyecto.

En la Tabla 8-6, se muestra la línea base monitoreada, las concentraciones corregidas modeladas
por Calpuff y la concentración final alcanzada en el área de estudio del Proyecto en la etapa de
mayor emisión, que corresponde a la etapa de operación.

La comuna de San Fernando fue incluida en la declaración de Zona Saturada por norma diaria y
anual de MP10 para las comunas del Valle Central de la Región de acuerdo al D.S. N°7/2009 de
MINSEGPRES. Posteriormente, en el año 2013 el D.S N°15 del Ministerio del Medio Ambiente
(MMA) estableció un Plan de descontaminación (PDA), el cual está en proceso de actualización de
acuerdo a la Res. Ex. N°669 de 2018 del MMA.

En el año 2017, la comuna de San Fernando fue incluida en la declaración de Zona Saturada por
norma diaria y anual de MP2,5 para las comunas del Valle Central de la Región de acuerdo al
Decreto N°42 del MMA. En junio de 2018 se dio inicio al proceso de un PDA de acuerdo a lo
establecido en la Res. Ex. N°503 del MMA.

Dado que la línea base de calidad del aire, confeccionada a partir de los datos del portal SINCA
2016 - 2018, registra aún niveles por sobre el límite establecido en la norma de calidad del aire de
MP2.5 como promedio de 24 horas, no es posible verificar el cumplimiento de dicha norma. Sin
embargo, la presente evaluación entrega antecedentes que permite afirmar que el aporte del
Proyecto en los receptores, se puede considerar nulo, dado que corresponden a 0,0 μg/m3 (0% el
nivel de la norma) y por lo tanto no aumentan las concentraciones de la línea base, ni el riesgo pre
existente.

**Tabla** **8-6: Cumplimiento** **de normativa** **en estación San Fernando**

|Tipo|Cont.|Estadígrafo|Límite|Est. San Fernando|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Tipo**<br>|**Cont.**|**Estadígrafo**|**Límite**|**Línea Base**|**Línea Base**|**Aporte Proyecto**|**Aporte Proyecto**|**Línea base + Aporte Proyecto**|**Línea base + Aporte Proyecto**|
|**Tipo**<br>|**Cont.**|**Estadígrafo**|**(μg/m3)**|**(μg/m3)**|**% Norma**|**(μg/m3)**|**% Norma**|**(μg/m3)**|**% Norma**|
|**Norma Primaria de**<br>**Calidad del Aire**|MP10|24 horas, P98|150|100,0|67%|0,0|0%|100,0|67%|
|**Norma Primaria de**<br>**Calidad del Aire**|MP10|Anual|50|41,0|82%|0,0|0%|41,0|82%|
|**Norma Primaria de**<br>**Calidad del Aire**|MP2.5|24 horas, P98|50|63,0|126%|0,0|0%|63,0|126%|
|**Norma Primaria de**<br>**Calidad del Aire**|MP2.5|Anual(1)|20|19,5|98%|0,0|0%|19,5|98%|

Nota 1: Promedio solo de carácter referencial calculado con mediciones año 2017 a 2018, dado que año 2016 es invalido por tener solo 9
meses de medición .

Fuente: Elaboración propia a partir de mediciones SINCA año 2016 a 2018.

**66**

Anexo V-C - Modelación de Dispersión de Contaminantes

**9.0** **CONCLUSIONES**

Se realizó una modelación con Calpuff, del DIA “Plan de Manejo de Sedimentos Central
Hidroeléctrica La Higuera”, en su etapa de mayor emisión, correspondiente a la etapa de operación
concluyéndose lo siguiente:

**Respecto a Clima y Meteorología**

- El área de estudio se ubica en la comuna de San Fernando, Provincia de Colchagua Región del
Libertador General Bernardo O'Higgins, la cual está en la transición de dos zonas climáticas, la
primera corresponde al valle central bajo un predominio del Clima Templado cálido con estación
seca prolongada de 8 a 7 meses y la segunda hacia la zona precordillerana con un Clima Templado
Cálido con estación Seca de 5 a 4 meses.

- La principal característica del Clima Templado cálido con estación seca prolongada de 8 a 7 meses
son las precipitaciones que caen preferentemente en invierno, entre mayo y agosto, cuando
precipita alrededor del 80% de lo que cae en todo el año. La época seca está constituida por 7 u 8
meses con precipitaciones inferiores a 40 milímetros. En verano se observa un predominio de días
despejados (22 por mes) y con altas temperaturas (28 días cálidos por mes), además no son
frecuentes las lluvias en esta época.

- En cambio, el Clima Templado Cálido con estación Seca de 5 a 4 meses comprende la pre
cordillera de las regiones Metropolitana y Sexta, además de la región del Maule y la parte norte de
la región del Bío Bío donde el ascenso del relieve provoca grandes variaciones en el clima, ya que
las temperaturas mínimas en el invierno se aproximan a 0 grado y las precipitaciones invernales se
pueden hacer sólidas, al mismo tiempo que aumentan a cerca de 1000 milímetros anuales,
acortándose así la duración de la estación seca, a sólo 4 a 5 meses con precipitación inferior a 40
milímetros.

- La estación meteorológica más cercana al Proyecto, en el área de estudio y con datos validos
disponibles corresponde a la estación San Fernando de la Red del Ministerio del Medio Ambiente.
La estación San Fernando fue instalada en el año 2007 y sus datos meteorológicos (validados y
preliminares sin validación) están quedando disponibles en línea en el sitio web del Sistema de
Información Nacional de Calidad del Aire (SINCA).

- La velocidad de viento durante la época invernal, producto del ingreso de sistemas frontales a la
zona de estudio, presenta días con velocidades máximas más altas a las observadas en verano.
Además, las velocidades de viento mínimas entre abril y septiembre son menores a las registradas
de octubre a marzo. Los valores fluctúan entre 0,0 y 5,5 m/s, con un promedio de velocidad para el
año 2018 de 1,7 m/s.

- La dirección del viento en la estación San Fernando para el año 2018 tiene una marcada ocurrencia
de vientos de componentes entre SurEste y SurOeste (entre 135° y 250°), siendo mayor la
ocurrencia de componente cercana a SO en temporada estival y en la temporada invernal hay
mayor predominio de las componentes entre S y SE. Durante meses de otoño-invierno,
especialmente aquellos días que tienen las velocidades más altas que corresponden al paso de
sistemas frontales tienen componente principal de vientos desde el Norte.

- La temperatura tiene para el año 2018 un marcado ciclo estacional, con mayores temperaturas en el
periodo estival (diciembre a febrero) que superan 30°C durante la mayoría de los días, en cambio
las mínimas son cercanas a 15°C. Durante los meses de invierno la mayoría de los días tiene
máximas inferiores a 20°C y mínimas cercanas a 5°C, incluso algunos días registran temperaturas
inferiores a 0°C. El valor medio de la temperatura durante el año 2018 alcanza los 14,2°C, con
máximo de 32,6°C y una mínima de -2,5°C.

- La humedad relativa tiene durante el año 2018 un ciclo estacional con mayores valores en invierno,
donde la mayoría de los días supera 85%, en cambio en meses de verano las máximas son

**67**

Anexo V-C - Modelación de Dispersión de Contaminantes

cercanas a 60%, pero las mínimas pueden descender hasta 20%. Para el año 2018 el promedio de
humedad fue 61,9%, con un máximo de 95% y un mínimo de 10%.

- La radiación solar tiene un ciclo anual para el año 2018 con mayores valores de radiación en la
época estival y menores en la época invernal. Algunos días tienen bajos valores de radiación
producto de la nubosidad, especialmente entre mayo y agosto con valores inferiores a 150 W/m2. En
verano, se registran los máximos horarios de radiación solar con valores que superan 900 W/m2 y
en meses de invierno los máximos diarios de la mayoría de los días son cercanos a 600 W/m2. Entre
julio y agosto se registran algunos días con las máximas diarias de radiación solar superiores a 800
W/m2 que no siguen la tendencia anual, podría ser un mal funcionamiento del sensor de radiación.

- No hay mediciones confiables de Presión Atmosférica desde octubre de 2017 por lo cual se analizó
el año 2016. Sin embargo, la Presión es una variable que no presenta grandes variaciones entre los
distintos años, por lo cual no afecta el análisis. El valor promedio para el año 2016 es 978 hPa, con
un mínimo de 963 hPa y un máximo de 990 hPa. Durante la época invernal se observa una mayor
variabilidad en los valores de presión durante el día, producto del ingreso de altas presiones frías y
bajas frontales, especialmente entre los meses de junio y agosto.

**Calidad de Aire:**

- Respecto a la información de calidad de aire disponible para el área de influencia, se cuenta
solamente con monitoreo continuo de MP10, MP2,5 y O3 desde el año 2007 en la estación San
Fernando, la cual está conectada en línea con el sitio web del Sistema Nacional de Calidad del Aire
(SINCA). Además, se cuenta con la información validada de calidad de aire del año 2015 para MP10
y O3, del año 2016 para MP2.5 en la estación San Fernando realizada por la Superintendencia del
Medio Ambiente disponible en los informes de auditoría a los datos y sus anexos en el sitio web
[http://snifa.sma.gob.cl/. Conforme a los estadígrafos indicados en las normas de calidad del aire, la](http://snifa.sma.gob.cl/)
línea base se confeccionó con los últimos tres años de monitoreo, período 2016 a 2018.

- Para MP10 durante el año 2018 se registra un percentil 98 de las concentraciones diarias inferior al
rango de Latencia por norma diaria alcanzando un valor de 100 μg/m3N, lo cual equivale a un 67%
de la norma diaria. Durante el período 2016-2018 se registra una concentración trianual de MP10 de
41 μg/m3N equivalente al 82% del valor de la norma, es decir en Rango de Latencia por norma
anual.

- Para MP2,5 durante el año 2018 se registra un percentil 98 de las concentraciones diarias superior
a la norma diaria de MP25 establecida en 50 μg/m3 con un valor de 63 μg/m3 equivalente a un 126%
de la norma. Por otro lado, el promedio del año 2016 es inválido por tener menos de 9 meses de
mediciones válidas, lo cual invalida el promedio trianual de MP2.5 que al ser calculado con los años
2017 y 2018 tiene un valor a modo de referencia de 19,5 μg/m3 en rango de latencia, pero muy
cercano a superar la norma anual establecida en 20 μg/m3.

- Para O3, el promedio trianual 2016-2018 de las concentraciones de 8 horas máximas de cada día
de O3 es inferior al rango de Latencia por norma de 8 horas establecida en 120 μg/m3N con un valor
de 90,71 μg/m3N equivalente a un 76% de la norma de 8 horas.

- En conclusión, conforme a la evaluación realizada, considerando los resultados de monitoreo de los
últimos tres años en la estación San Fernando, la evaluación de la norma arroja concentraciones
que se encuentran bajo el nivel de latencia para MP10 promedio 24 horas y O3 promedio de 8
horas, nivel de latencia para MP10 y MP2,5 promedio anual, y superación para MP2,5 promedio 24
horas.

**Aportes del Proyecto:**

- Se realizó una modelación de las emisiones del proyecto en su etapa de operación, por ser la etapa
de mayor emisión, ya que no habrá etapa de construcción, obteniéndose los aportes del proyecto en
la calidad del aire en los receptores puntuales considerados y en el Punto de Máximo Aporte (PMA).
Conforme a lo establecido en la Guía de Modelación del SEIA, los aportes modelados, han sido

**68**

Anexo V-C - Modelación de Dispersión de Contaminantes

multiplicados por el factor de corrección obtenidos en el capítulo 8.2 obteniéndose los aportes
corregidos, cuyos resultados se analizan a continuación.

- El PMA se ubica cerca del Proyecto o en vías no pavimentadas de acceso al Proyecto, alejadas de
los receptores puntuales. Sin embargo, los aportes son de muy baja magnitud no superando
respecto a material particulado MP10 el 7% del nivel de la norma, y respecto a MP2.5 el 2% del
nivel de la norma. Respecto a gases el aporte también es muy reducido no superando el 12% del
nivel de la norma.

- El máximo aporte del Proyecto en términos de concentración de MP10 promedio de 24 horas,
percentil 98, se producirá en el receptor La Rufina. Sin embargo, este no supera el 1,1 μg/m3
equivalente a 1% de la norma. Lo que se puede considerar un aporte prácticamente nulo.

- El máximo aporte del Proyecto en términos de concentración de MP10 promedio anual, se producirá
en el receptor La Rufina. Sin embargo, este no supera el 0,2 μg/m3 equivalente a 0% de la norma.
Lo que se puede considerar un aporte prácticamente nulo.

- El máximo aporte del Proyecto en términos de concentración de MP2.5 promedio de 24 horas,
percentil 98, se producirá en el receptor La Rufina. Sin embargo, este no supera el 0,1 μg/m3
equivalente a 0% de la norma. Lo que se puede considerar un aporte prácticamente nulo.

- El aporte del Proyecto en términos de concentración de MP2.5 promedio anual, en todos los
receptores, será menor al 0,0 μg/m3 y 0% de la norma. Lo que se puede considerar un aporte nulo.

- El máximo aporte del Proyecto en términos de concentración de NO2 promedio de 1 hora, percentil
99, se producirá en el receptor La Rufina. Sin embargo, este no supera el 0,1 μg/m3 equivalente a
0% de la norma. Lo que se puede considerar un aporte prácticamente nulo.

- El aporte del Proyecto en términos de concentración de NO2 promedio anual, en todos los
receptores será a menos del 0,0 μg/m3 y 0%. Lo que puede ser considerado un aporte nulo.

- El aporte del Proyecto en términos de concentración de SO2 promedio de 24 horas, percentil 99, en
todos los receptores será a menos del 0,0 μg/m3 y 0%. Lo que puede ser considerado un aporte
nulo.

- El aporte del Proyecto en términos de concentración de SO2 promedio anual, en todos los
receptores será a menos del 0,0 μg/m3 y 0%. Lo que puede ser considerado un aporte nulo.

- El aporte del Proyecto en términos de concentración de CO 1 hora, percentil 99, en todos los
receptores será a menos del 0,0 μg/m3 y 0%. Lo que puede ser considerado un aporte nulo.

- El máximo aporte del Proyecto en términos de concentración de CO promedio de 8 horas, percentil
99, en todos los receptores será a menos del 0,0 μg/m3 y 0%. Lo que puede ser considerado un
aporte nulo.

- Se realizó una evaluación de cumplimiento de normativa de calidad del aire, considerando la línea
base monitoreada en la estación San Fernando y los aportes modelados corregidos del Proyecto.

- Dado que la línea base de calidad del aire, confeccionada a partir de los datos del portal SINCA
2016 - 2018, registra aún niveles por sobre el límite establecido en la norma de calidad del aire de
MP2.5 como promedio de 24 horas, no es posible verificar el cumplimiento de dicha norma. Sin
embargo, la presente evaluación entrega antecedentes que permite afirmar que el aporte del
Proyecto en los receptores, se puede considerar nulo, dado que corresponden a 0,0 μg/m3 (0% el
nivel de la norma) y por lo tanto no aumentan las concentraciones de la línea base, ni el riesgo pre
existente.

Por lo antes indicado, es posible afirmar que el Proyecto, tendrá un aporte muy poco significativo en la
calidad del aire de su área de influencia, por lo que no generará un impacto significativo, ni aumentará el
riesgo pre existente.

**69**