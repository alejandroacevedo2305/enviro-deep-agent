---
title: Sin título
author: jurbistondo
date: D:20141008125331-03'00'
language: es
type: report
pages: 76
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - DIA: “MEJORAMIENTO CONDICIONES DE ALMACENAMIENTO DE CONCENTRADO DE COBRE, 46.000 TON” MODELACIÓN DE DISPERSION DE CONTAMINANTES
-->

# DIA: “MEJORAMIENTO CONDICIONES DE ALMACENAMIENTO DE CONCENTRADO DE COBRE, 46.000 TON” MODELACIÓN DE DISPERSION DE CONTAMINANTES

|Versión|Elaboró|Revisó|Aprobó|Fecha|
|---|---|---|---|---|
|<br>REV 00|<br>JS|<br>SOI|<br>MSC|<br>01/10/2014|

**Elaborado por:**

**Preparado por:**

**José Salim**
**Ingeniero Civil Mecánico, Universidad de Chile**
**Máster en Gestión Integrada de Prevención, Medio Ambiente y Calidad, Universidad**

**Politécnica de Cataluña.**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**2/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**2/ 73**|

**INDICE**

**1.0** **INTRODUCCIÓN .......................................................................................................... 6**

**2.0** **OBJETIVOS ................................................................................................................. 7**

2.1 Objetivo general ................................................................................................ 7

2.2 Objetivos específicos ......................................................................................... 7

**3.0** **NORMATIVA DE CALIDAD DE APLICABLE .............................................................. 8**

**4.0** **CARACTERIZACIÓN DEL ÁREA DE ESTUDIO ......................................................... 8**

4.1 Localización ....................................................................................................... 8

**5.0** **PRESENTACIÓN DE DATOS UTILIZADOS ................................................................ 9**

5.1 Descripción y justificación del modelo................................................................ 9

5.2 Receptores considerados ................................................................................ 10

5.3 Dominio de modelación ................................................................................... 10

5.4 Topografía ....................................................................................................... 12

5.5 Fuentes de emisión y parámetros utilizados en modelación ............................ 12

5.5.1 Fuentes de emisión ......................................................................................... 12

**6.0** **LÍNEA BASE DE CLIMA Y METEOROLÓGICA ........................................................ 16**

6.1 Caracterización climática regional ................................................................... 16

6.1.1 Clima templado cálido con estación seca prolongada y gran nubosidad .......... 18

6.2 Presentación de datos meteorológicos observados ......................................... 18

6.2.1 Series de tiempo .............................................................................................. 18

6.2.2 Ciclos diarios ................................................................................................... 23

6.2.3 Rosa del viento ................................................................................................ 29

6.2.4 Ciclos estacionales .......................................................................................... 31

**7.0** **LÍNEA BASE DE CALIDA DEL AIRE ........................................................................ 35**

7.1 Línea base de calidad del aire ......................................................................... 35

7.2 Presentación de datos de calidad del aire observados .................................... 36

7.2.1 Series de tiempo .............................................................................................. 36

7.2.2 Ciclos diarios ................................................................................................... 38

7.2.3 Ciclos estacionales .......................................................................................... 41

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**3/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**3/ 73**|

**8.0** **MODELACIÓN DE CALIDAD DEL AIRE Y RESULTADOS ...................................... 43**

8.1 Aportes del Proyecto ....................................................................................... 43

8.1.1 Etapa de Construcción .................................................................................... 43

8.1.2 Etapa de Operación ......................................................................................... 54

8.2 Análisis de incertidumbre y concentraciones modeladas con Calpuff. ............. 61

8.2.1 Análisis de datos meteorológicos modelados con WRF v/s datos

observacionales. ........................................................................................... 61

8.2.2 Análisis de incertidumbre y determinación de factores de corrección de

concentraciones modeladas ......................................................................... 68

8.3 Evaluación de cumplimiento de normativa ....................................................... 70

8.3.1 Etapa de Construcción .................................................................................... 70

8.3.2 Etapa de Operación ......................................................................................... 72

**9.0** **CONCLUSIONES ....................................................................................................... 75**

**LISTADO DE TABLAS**

Tabla 1: Normativa de calidad aplicable al Proyecto. ........................................................... 8

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---| |<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**8/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**8/ 73**| **3.0** **NORMATIVA DE CALIDAD DE APLICABLE** -->

**Tabla 1: se muestran las normas de calidad del aire vigentes aplicables al Proyecto y**

| Tipo | Normativa | Estadígrafo | Límite |
| --- | --- | --- | --- |
| **Tipo**<br> | **Normativa** | **Estadígrafo** | **(ug/m3N)** |
| **Norma Primaria de**<br>**Calidad del Aire** | MP10 (D.S N°20/13 MIN. DEL MEDIO<br>AMBIENTE) | Promedio diario, percentil 98 | 150 |
| **Norma Primaria de**<br>**Calidad del Aire** | MP10 (D.S N°20/13 MIN. DEL MEDIO<br>AMBIENTE) | Media aritmética anual | 50 |
| **Norma Primaria de**<br>**Calidad del Aire** | MP2.5 (D.S N°12/11 MINSEGPRES) | Promedio diario, percentil 98 | 50 |
| **Norma Primaria de**<br>**Calidad del Aire** | MP2.5 (D.S N°12/11 MINSEGPRES) | Media aritmética anual | 20 |
| **Norma Primaria de**<br>**Calidad del Aire** | SO2 (D.S N°113/02 MINSEGPRES) | Promedio diario, percentil 99 | 250 |
| **Norma Primaria de**<br>**Calidad del Aire** | SO2 (D.S N°113/02 MINSEGPRES) | Media aritmética anual | 80 |
| **Norma**<br>**Secundaria** | SO2 (D.S N°22/09 MINSEGPRES, Zona Norte) | Promedio anual | 80 |
| **Norma**<br>**Secundaria** | SO2 (D.S N°22/09 MINSEGPRES, Zona Norte) | Promedio diario, percentil 99,7 | 365 |
| **Norma**<br>**Secundaria** | SO2 (D.S N°22/09 MINSEGPRES, Zona Norte) | Promedio de 1 hora, percentil 99,73 | 1.000 |

<!-- Estadísticas: 10 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **4.0** **CARACTERIZACIÓN DEL ÁREA DE ESTUDIO** -->
<!-- FIN TABLA 1 -->


Tabla 2: Receptores puntuales considerados. ................................................................... 10

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la evaluación de las concentraciones aportadas por el Proyecto en su área de influencia, se han considerado los receptores puntuales que se muestran en la Tabla 2, correspondientes a las estaciones de calidad del aire más cercanas al Proyecto. -->

**Tabla 2: Receptores Puntuales** **considerados.****

| Estación | Coordenadas UTM Datum<br>WGS84 | Col3 | Uso | Distancia a<br>Proyecto |
| --- | --- | --- | --- | --- |
| **Estación** | **Este (m)** | **Sur (m)** | **Sur (m)** | **km** |
| La Greda | 268.185 | 6.373.910 | 19 Sur | 0,95 |
| Los Maitenes | 270.073 | 6.372.171 | 19 Sur | 2,9 |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 5.3 DOMINIO DE MODELACIÓN -->
<!-- FIN TABLA 2 -->


Tabla 3: Características del dominio de modelación. ......................................................... 11

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---| |<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**11/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**11/ 73**| **Figura 2. Dominio de Modelación y Receptores Puntuales considerados** -->

**Tabla 3: Características del Dominio de Modelación.****

| Descripción | Detalle |
| --- | --- |
| Tamaño de la grilla | 1 km x 1 km |
| Resolución horizontal y vertical del<br>dominio | 20 km (Este - Oeste) x 20 km (Norte - Sur) |
| Número capas | 11 entre 0 y 4.000 m de altura |
| Coordenadas central de origen (UTM) | 267.003 m E y 6.370.378 m S, Datum WGS 84 |
| Área del dominio en km2 | 400 km2 |
| Topografía | Extraída de SRTM3 con resolución de 90 m |
| Usos de suelo | Extraídos de Global Land Cover Characterization<br>(GLCC) del US Geological Survey (UGS), EEUU. |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| -->
<!-- FIN TABLA 3 -->


Tabla 4: Fuentes modeladas en Calpuff y actividades emisoras asociadas - Etapa de

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _**Etapa de Construcción**_ En la Tabla 4 se muestran las fuentes emisoras modeladas en Calpuff y las actividades emisoras consideradas. -->

**Tabla 4: Fuentes Modeladas en Calpuff y Actividades Emisoras Asociadas - Etapa de****

| Source<br>ID | Actividades | Tipo de Fuente | Área | Período | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Source**<br>**ID** | **Actividades** | **Tipo de Fuente** | **m2 ** | **meses** | **días/mes** | **horas/día** |
| SRC_1 | Movimiento de<br>tierra | Área | 4.166 | 10 | 24 | 15 |
| SRC_1 | Maquinarias | Maquinarias | Maquinarias | Maquinarias | Maquinarias | Maquinarias |
| SRC_2 | Circulación de<br>vehículos por<br>caminos<br>pavimentados<br>(Fuentes móviles) | Línea - Área | 130.764 | 10 | 24 | 15 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. En la Tabla 5 y Tabla 6 se muestra la emisión de las fuentes y la tasa de emisión calculada en gramos por segundo, para material particulado y gases respectivamente. La tasa de -->
<!-- FIN TABLA 4 -->


Construcción. ....................................................................................................... 13

Tabla 5: Tasa de emisión de material particulado y fuente modelada asociada

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- en gramos por segundo, para material particulado y gases respectivamente. La tasa de emisión se ha estimado considerado un funcionamiento de 10 meses, 6 días a la semana (lunes a sábado), dos turnos (día y noche), lo que corresponde a un total de 15 horas al día, considerando el límite de horas laborales (45 horas semanales por turno). -->

**Tabla 5: Tasa de Emisión de Material Particulado y Fuente Modelada Asociada - Etapa****

| Source<br>ID | Actividades | MP10 | Col4 | Col5 | MP2.5 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Source**<br>**ID** | **Actividades** | **ton/período** | **g/s** | **g/(m2*s)** | **ton/período** | **g/s** | **g/(m2*s)** |
| SRC_1 | Movimiento de tierra | 2,281 | 1,76E-01 | 4,22E-05 | 2,281 | 1,76E-01 | 4,22E-05 |
| SRC_1 | Maquinarias | Maquinarias | Maquinarias | Maquinarias | Maquinarias | Maquinarias | Maquinarias |
| SRC_2 | Circulación de<br>vehículos por<br>caminos<br>pavimentados<br>(Fuentes móviles) | 0,513 | 3,96E-02 | 3,03E-07 | 0,076 | 5,86E-03 | 4,48E-08 |
| **Total Emisión:** | **Total Emisión:** | **2,794** | **2,16E-01** |  | **2,357** | **1,82E-01** |  |

<!-- Estadísticas: 5 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| -->
<!-- FIN TABLA 5 -->

Construcción. ....................................................................................................... 13

Tabla 6: Tasa de emisión de gases y fuente modelada asociada - Construcción. .............. 14

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| |<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**14/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**14/ 73**| -->

**Tabla 6: Tasa de Emisión de Gases y Fuente Modelada Asociada - Etapa****

| Source<br>ID | Actividades | SO<br>2 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Source**<br>**ID** | **Actividades** | **ton/período** | **g/s** | **g/(m2*s)** |
| SRC_1 | Movimiento<br>de tierra | 0,000 | 0,00E+00 | 0,00E+00 |
| SRC_1 | Maquinarias | Maquinarias | Maquinarias | Maquinarias |
| SRC_2 | Circulación<br>de vehículos<br>por caminos<br>pavimentados<br>(Fuentes<br>móviles) | 0,003 | 2,31E-04 | 1,77E-09 |
| **Total Emisión:** | **Total Emisión:** | **0,003** | **2,31E-04** |  |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. _**Etapa de Operación**_ -->
<!-- FIN TABLA 6 -->


Tabla 7: Fuentes modeladas en Calpuff y actividades emisoras asociadas - Etapa de

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _**Etapa de Operación**_ En la Tabla 7 se muestran las fuentes emisoras modeladas en Calpuff y las actividades emisoras consideradas. -->

**Tabla 7: Fuentes Modeladas en Calpuff y Actividades Emisoras Asociadas - Etapa de****

| Source<br>ID | Actividades | Tipo de Fuente | Área | Período | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Source**<br>**ID** | **Actividades** | **Tipo de Fuente** | **m2 ** | **meses** | **días/mes** | **horas/día** |
| SRC_1 | Maquinaria (2<br>cargadores<br>frontales) | Área | 4.166 | 12 | 1 | 24 |
| SRC_1 | Transporte y<br>transferencia de<br>material | Transporte y<br>transferencia de<br>material | Transporte y<br>transferencia de<br>material | Transporte y<br>transferencia de<br>material | 30 | 24 |

<!-- Estadísticas: 3 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| -->
<!-- FIN TABLA 7 -->


Operación. ........................................................................................................... 14

Tabla 8: Tasa de emisión de material particulado y fuente modelada asociada

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la Tabla 8 y Tabla 9 se muestra la emisión de las fuentes y la tasa de emisión calculada en gramos por segundo, para material particulado y gases. La tasa de emisión se ha estimado considerando el tiempo de funcionamiento indicado en la tabla anterior. -->

**Tabla 8: Tasa de Emisión de Material Particulado y Fuente Modelada Asociada -****

| Source<br>ID | Actividades | MP10 | Col4 | MP2.5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Source**<br>**ID** | **Actividades** | **g/s** | **g/(m2*s)** | **ton/período** | **g/s** | **g/(m2*s)** |
| SRC_1 | Maquinaria (2<br>cargadores frontales) | 1,91E-02 | 4,58E-06 | 0,396 | 1,91E-02 | 4,58E-06 |
| SRC_1 | Transporte y<br>transferencia de<br>material | Transporte y<br>transferencia de<br>material | Transporte y<br>transferencia de<br>material | Transporte y<br>transferencia de<br>material | Transporte y<br>transferencia de<br>material | Transporte y<br>transferencia de<br>material |
| **Total Emisión:** | **Total Emisión:** | **1,91E-02** |  | **0,396** | **1,91E-02** |  |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 9: Tasa de Emisión de Gases y Fuente Modelada Asociada - Etapa Operación.** -->
<!-- FIN TABLA 8 -->

Operación. ........................................................................................................... 15

Tabla 9: Tasa de emisión de gases y fuente modelada asociada - Operación. .................. 15

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |SRC_1|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material| |**Total Emisión:**|**Total Emisión:**|**1,91E-02**||**0,396**|**1,91E-02**|| Fuente: Elaboración propia. -->

**Tabla 9: Tasa de Emisión de Gases y Fuente Modelada Asociada - Etapa Operación.****

| Source<br>ID | Actividades | SO<br>2 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Source**<br>**ID** | **Actividades** | **ton/período** | **g/s** | **g/(m2*s)** |
| SRC_1 | Maquinaria<br>(2<br>cargadores<br>frontales) | 0,000 | 0,00E+00 | 0,00E+00 |
| SRC_1 | Transporte y<br>transferencia<br>de material | Transporte y<br>transferencia<br>de material | Transporte y<br>transferencia<br>de material | Transporte y<br>transferencia<br>de material |
| **Total Emisión:** | **Total Emisión:** | **0,000** | **0,00E+00** |  |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| -->
<!-- FIN TABLA 9 -->


Tabla 10: Estaciones meteorológicas disponibles en la zona ............................................. 16

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 2013, en el área de modelación. Para el análisis se han utilizado los datos de la Estación Meteorológica Principal de la red Ventanas, por estar cerca del Proyecto (1,4 km) y presentar mayor número de parámetros monitoreados. Los parámetros monitoreados se muestran en la Tabla 10. -->

**Tabla 10: Estaciones Meteorológicas disponibles en la zona****

| Estación | Coordenadas UTM<br>Datum WGS84 | Col3 | Información registrada |
| --- | --- | --- | --- |
| **Estación** | **Este (m)** | **Sur (m)** | **Sur (m)** |
| Est. Meteorológica<br>Principal | 267.310 | 6371.939 | V V, DV, Temperatura, HR, Presión, Radiación<br>y Precipitaciones. |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 6.1 CARACTERIZACIÓN CLIMÁTICA REGIONAL -->
<!-- FIN TABLA 10 -->


Tabla 11: Línea base de Calidad del Aire Período (2010-2012). ........................................ 35

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- efecto del Proyecto, la cual ha sido elaborada a partir de los antecedentes contenidos en el “Informe de Calidad del Aire de la Región de Valparaíso período 2010 - 2012”, elaborado por la SEREMI de Salud de la Región de Valparaíso, por ser la información oficial más actualizada disponible. -->

**Tabla 11: Línea Base de Calidad del Aire Período (2010-2012).****

| Tipo | Contaminante | Estadígrafo | Límite | La Greda | Col6 | Los Maitenes | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **Contaminante** | **Estadígrafo** | **Límite** | **Línea Base** | **Línea Base** | **Línea Base** | **Línea Base** |
| **Tipo** | **Contaminante** | **Estadígrafo** | **(ug/m3)** | **ug/m3 ** | **% de la norma** | **ug/m3** | **% de la norma** |
| **Norma Primaria de Calidad**<br>**del Aire (1)** | MP10 | 24 horas, P98 | 150 | 77 | 51,3% | 56 | 37,3% |
| **Norma Primaria de Calidad**<br>**del Aire (1)** | MP10 | Anual | 50 | 44 | 88,0% | 32 | 64,0% |
| **Norma Primaria de Calidad**<br>**del Aire (1)** | MP2.5 | 24 horas, P98 | 50 | 36 | 72,0% | 32 | 64,0% |
| **Norma Primaria de Calidad**<br>**del Aire (1)** | MP2.5 | Anual | 20 | 17 | 85,0% | 14 | 70,0% |
| **Norma Primaria de Calidad**<br>**del Aire (1)** | SO2 | 24 horas, P99 | 250 | 64 | 25,6% | 132 | 52,8% |
| **Norma Primaria de Calidad**<br>**del Aire (1)** | SO2 | Anual | 80 | 11 | 13,8% | 35 | 43,8% |
| **Norma Secundaria (2)** | SO2 | Anual | 80 | 14 | 17,5% | 33 | 41,3% |
| **Norma Secundaria (2)** | SO2 | 24 horas, P99,7 | 365 | 110 | 30,0% | 158 | 43,3% |
| **Norma Secundaria (2)** | SO2 | 1 hora, P99,73 | 1.000 | 286 | 28,6% | 542 | 54,2% |

<!-- Estadísticas: 11 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- (1) Línea base corresponde a período 2010-2012. (2) Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012. -->
<!-- FIN TABLA 11 -->


Tabla 12: Aporte del Proyecto en los receptores puntuales y Punto de Máximo

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| |<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br> <br> <br>**44/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**44/ 73**| -->

**Tabla 12: Aporte del Proyecto en los Receptores Puntuales y Punto de Máximo Impacto (PMI) - Construcción****

| Tipo | Contaminante | Estadígrafo | Límite | La Greda | Col6 | Los Maitenes | Col8 | Punto de Máximo Impacto (PMI) (1) | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **Contaminante** | **Estadígrafo** | **Límite** | ~~**Aporte Proyecto**~~<br> | ~~**Aporte Proyecto**~~<br> | ~~**Aporte Proyecto**~~<br> | ~~**Aporte Proyecto**~~<br> | ~~**Aporte Proyecto**~~<br> | ~~**Aporte Proyecto**~~<br> | **UTM**<br>**Este (m)** | **UTM Sur**<br>**(m)** |
| **Tipo** | **Contaminante** | **Estadígrafo** | **(ug/m3)** | **ug/m3** | ~~**% de la**~~<br>**norma** | **ug/m3** | ~~**% de la**~~<br>**norma** | **ug/m3** | ~~**% de la**~~<br>**norma** | ~~**% de la**~~<br>**norma** | ~~**% de la**~~<br>**norma** |
| **Norma**<br>**Primaria de**<br>**Calidad del**<br><br> | MP10 | 24 horas, P98 | 150 | 4,43 | 3,0% | 0,36 | 0,2% | 35,50 | 23,7% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br>**Calidad del**<br><br> | MP10 | Anual | 50 | 0,57 | 1,1% | 0,04 | 0,1% | 5,92 | 11,8% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br>**Calidad del**<br><br> | **Aire**<br>MP2.5 | 24 horas, P98 | 50 | 4,22 | 8,4% | 0,34 | 0,7% | 35,44 | 70,9% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br>**Calidad del**<br><br> | **Aire**<br>MP2.5 | Anual | 20 | 0,53 | 2,7% | 0,03 | 0,2% | 5,90 | 29,5% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br>**Calidad del**<br><br> | SO2 | 24 horas, P99 | 250 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 272.503 | 6.375.224 |
| **Norma**<br>**Primaria de**<br>**Calidad del**<br><br> | SO2 | Anual | 80 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 269.503 | 6.375.239 |
| **Norma**<br>**Secundaria** | SO2 | Anual | 80 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 269.503 | 6.375.239 |
| **Norma**<br>**Secundaria** | SO2 | 24 horas, P99,7 | 365 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 269.503 | 6.375.239 |
| **Norma**<br>**Secundaria** | SO2 | 1 hora, P99,73 | 1.000 | 0,01 | 0,0% | 0,00 | 0,0% | 0,03 | 0,0% | 269.503 | 6.373.238 |

<!-- Estadísticas: 11 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: Punto de máximo impacto ocurre dentro de las instalaciones del Proyecto. Fuente Elaboración propia a partir de resultados de la modelación |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| -->
<!-- FIN TABLA 12 -->


Impacto (PMI) - Construcción ............................................................................... 44

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**4/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**4/ 73**|

Tabla 13: Aporte del Proyecto en los receptores puntuales y Punto de Máximo

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| |<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**55/73**<br>|<br>**N° DE PÁGINA**<br>**55/73**<br>| -->

**Tabla 13: Aporte del Proyecto en los Receptores Puntuales y Punto de Máximo Impacto (PMI) - Operación****

| Tipo | Contaminante | Estadígrafo | Límite | La Greda | Col6 | Los Maitenes | Col8 | Punto de Máximo Impacto (PMI) | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **Contaminante** | **Estadígrafo** | **Límite** | ~~**Aporte Proyecto**~~ | ~~**Aporte Proyecto**~~ | ~~**Aporte Proyecto**~~ | ~~**Aporte Proyecto**~~ | ~~**Aporte Proyecto**~~ | ~~**Aporte Proyecto**~~ | ~~**UTM**~~<br>**Este**<br>**(m)** | **UTM Sur**<br>**(m)** |
| **Tipo** | **Contaminante** | **Estadígrafo** | **(ug/m3)** | **ug/m3** | **% de la norma** | **ug/m3** | **% de la norma** | **ug/m3** | **% de la norma** | **% de la norma** | **% de la norma** |
| **Norma**<br>**Primaria de**<br> | **d l**<br>MP10 | 24 horas, P98 | 150 | 0,46 | 0,3% | 0,04 | 0,0% | 3,85 | 2,6% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br> | **d l**<br>MP10 | Anual | 50 | 0,06 | 0,1% | 0,00 | 0,0% | 0,64 | 1,3% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br> | **id d **<br>MP2.5 | 24 horas, P98 | 50 | 0,46 | 0,9% | 0,04 | 0,1% | 3,85 | 7,7% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br> | **id d **<br>MP2.5 | Anual | 20 | 0,06 | 0,3% | 0,00 | 0,0% | 0,64 | 3,2% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br> | **C l**<br>SO2 | 24 horas, P99 | 250 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 267.502 | 6.373.238 |
| **Norma**<br>**Primaria de**<br> | **C l**<br>SO2 | Anual | 80 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 267.502 | 6.373.238 |
| **Norma**<br>**Secundaria** | SO2 | Anual | 80 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 267.502 | 6.373.238 |
| **Norma**<br>**Secundaria** | SO2 | 24 horas, P99,7 | 365 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 267.502 | 6.373.238 |
| **Norma**<br>**Secundaria** | SO2 | 1 hora, P99,73 | 1.000 | 0,00 | 0,0% | 0,00 | 0,0% | 0,00 | 0,0% | 267.502 | 6.373.238 |

<!-- Estadísticas: 11 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: Punto de máximo impacto ocurre dentro de las instalaciones del Proyecto. Fuente: Elaboración propia a partir de resultados de la modelación. |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| -->
<!-- FIN TABLA 13 -->


Impacto (PMI) - Operación .................................................................................. 55

Tabla 14: Diferencia entre intensidad del viento observada y modelada en Estación

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| |<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**69/73**<br>|<br>**N° DE PÁGINA**<br>**69/73**<br>| -->

**Tabla 14: Diferencia entre Intensidad del Viento Observada y Modelada en Estación INIA****

| Estación | Observado<br>(m/s) | Modelado (WRF)<br>(m/s) | Diferencia<br>Mod-Obs<br>(m/s) | Variación<br>Porcentual<br>% |
| --- | --- | --- | --- | --- |
| Principal | 2,30 | 2,87 | 0,57 | 24,78 |
| Principal diurno | 3,43 | 3,61 | 0,18 | 5,25 |
| Principal nocturno | 1,62 | 2,13 | 0,51 | 31,48 |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia A continuación se analiza la diferencia del viento modelado respecto al observado, en función de su dirección, para lo cual se ha dividido la rosa de los vientos en cuadrantes, -->
<!-- FIN TABLA 14 -->


INIA ...................................................................................................................... 69

Tabla 15: Diferencia entre intensidad del viento observada y modelada en Estación

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- del viento en las direcciones con componente oeste, con una diferencia en la velocidad menor a 1 m/s. Como es habitual la mayor diferencia se presenta en horario nocturno, debido a que las bajas intensidades del viento, hacen más difícil predecir su intensidad por el modelo. -->

**Tabla 15: Diferencia entre Intensidad del Viento Observada y Modelada en Estación INIA****

| Dirección<br>viento<br>(grados) | Diurno | Col3 | Col4 | Col5 | Nocturno | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección**<br>**viento**<br>**(grados)** | Obs<br>(m/s) | WRF<br>(m/s) | Dif<br>(m/s) | Variación<br>% | Obs<br>(m/s) | WRF<br>(m/s) | Dif<br>(m/s) | Variación<br>% |
| 0-90 | 2,33 | 2,76 | 0,43 | 18,45 | 2,03 | 2,05 | 0,02 | 0,98 |
| 90-180 | 1,37 | 2,26 | 0,89 | 64,69 | 1,52 | 2,09 | 0,57 | 37,50 |
| **180-270** | **3,31** | **4,05** | **0,74** | **22,36** | **1,33** | **2,28** | **0,95** | **71,43** |
| **270-360** | **3,04** | **2,94** | **-0,10** | **-3,29** | **1,90** | **2,00** | **0,10** | **5,27** |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| |<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**70/73**<br>|<br>**N° DE PÁGINA**<br>**70/73**<br>| -->
<!-- FIN TABLA 15 -->


INIA (Diurno y Nocturno) ...................................................................................... 69

Tabla 16: Cumplimiento de normativa en Estación La Greda - Construcción ..................... 71

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto a SO 2, también se observa cumplimiento de todas las normas de calidad del aire, pudiéndose considerar el aporte del Proyecto en las estaciones La Greda y Los Maitenes, como nulo. Lo que es de esperar dado el bajo contenido de azufre del combustible diesel disponible en Chile (menos de 50 ppm). -->

**Tabla 16: Cumplimiento de Normativa en Estación La Greda - Construcción****

| Tipo | Contaminante | Estadígrafo | Límite | La Greda | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo**<br> | **Contaminante** | **Estadígrafo** | **Límite** | **Línea Base** | **Línea Base** | ~~**Aporte**~~<br>**Proyecto** | ~~**Aporte**~~<br>**Proyecto** | **Línea Base+ Aporte** | **Línea Base+ Aporte** | **Línea Base+ Aporte** |
| **Tipo**<br> | **Contaminante** | **Estadígrafo** | **ug/m3 ** | **ug/m3 ** | **% de**<br>**la**<br>**norma** | **ug/m3 ** | **% de**<br>**la**<br>**norma** | **ug/m3 ** | **% de**<br>**la**<br>**norma** | **Cumplimiento** |
| **Norma Primaria de**<br>**Calidad del Aire ** | MP10 | 24 horas, P98 | 150 | 77 | 51,3% | 4,43 | 3,0% | 81 | 54,3% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire ** | MP10 | Anual | 50 | 44 | 88,0% | 0,57 | 1,1% | 45 | 89,1% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire ** | MP2.5 | 24 horas, P98 | 50 | 36 | 72,0% | 4,22 | 8,4% | 40 | 80,4% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire ** | MP2.5 | Anual | 20 | 17 | 85,0% | 0,53 | 2,7% | 18 | 87,7% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire ** | SO2 | 24 horas, P99 | 250 | 64 | 25,6% | 0,00 | 0,0% | 64 | 25,6% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire ** | SO2 | Anual | 80 | 11 | 13,8% | 0,00 | 0,0% | 11 | 13,8% | Cumple |
| **Norma**<br>**Secundaria** | SO2 | Anual | 80 | 14 | 17,5% | 0,00 | 0,0% | 14 | 17,5% | Cumple |
| **Norma**<br>**Secundaria** | SO2 | 24 horas, P99,7 | 365 | 110 | 30,0% | 0,00 | 0,0% | 110 | 30,0% | Cumple |
| **Norma**<br>**Secundaria** | SO2 | 1 hora, P99,73 | 1.000 | 286 | 28,6% | 0,01 | 0,0% | 286 | 28,6% | Cumple |

<!-- Estadísticas: 11 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- (1): Línea base corresponde a período 2010-2012. (2): Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012 n/a: No aplica debido a que no hay monitoreo de línea base para esta variable Fuente: Elaboración propia en base de resultados de modelación e “Informe de Calidad del Aire de la Región de Valparaíso, período -->
<!-- FIN TABLA 16 -->


Tabla 17: Cumplimiento de normativa en Estación Los Maitenes - Construcción ............... 72

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| |<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**72/73**<br>|<br>**N° DE PÁGINA**<br>**72/73**<br>| -->

**Tabla 17: Cumplimiento de Normativa en Estación Los Maitenes - Construcción****

| Tip<br>o | Contaminante | Estadígrafo | Límite | Los Maitenes | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tip**<br>**o **<br> | **Contaminante** | **Estadígrafo** | **Límite** | **Línea Base**<br> | **Línea Base**<br> | ~~**Aporte**~~<br>**Proyecto** | ~~**Aporte**~~<br>**Proyecto** | **Línea base+ Aporte** | **Línea base+ Aporte** | **Línea base+ Aporte** |
| **Tip**<br>**o **<br> | **Contaminante** | **Estadígrafo** | **ug/m3 ** | **ug/m3 ** | ~~**% de**~~<br>**la**<br>**norma** | **ug/m3 ** | **% de la**<br>**norma** | **ug/m3 ** | **% de la**<br>**norma** | **Cumplimient**<br>**o ** |
| **Norma Primaria de**<br>**Calidad del Aire **<br> | MP10 | 24 horas, P98 | 150 | 56 | 37,3% | 0,36 | 0,2% | 56,36 | 37,6% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire **<br> | MP10 | Anual | 50 | 32 | 64,0% | 0,04 | 0,1% | 32,04 | 64,1% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire **<br> | MP2.5 | 24 horas, P98 | 50 | 32 | 64,0% | 0,34 | 0,7% | 32,34 | 64,7% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire **<br> | MP2.5 | Anual | 20 | 14 | 70,0% | 0,03 | 0,2% | 14,03 | 70,2% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire **<br> | SO2 | 24 horas, P99 | 250 | 132 | 52,8% | 0,00 | 0,0% | 132 | 52,8% | Cumple |
| **Norma Primaria de**<br>**Calidad del Aire **<br> | SO2 | Anual | 80 | 35 | 43,8% | 0,00 | 0,0% | 35 | 43,8% | Cumple |
| **Norma**<br>**Secundaria (2) ** | SO2 | Anual | 80 | 33 | 41,3% | 0,00 | 0,0% | 33 | 41,3% | Cumple |
| **Norma**<br>**Secundaria (2) ** | SO2 | 24 horas,<br>P99,7 | 365 | 158 | 43,3% | 0,00 | 0,0% | 158 | 43,3% | Cumple |
| **Norma**<br>**Secundaria (2) ** | SO2 | 1 hora,<br>P99,73 | 1.000 | 542 | 54,2% | 0,00 | 0,0% | 541,5 | 54,2% | Cumple |

<!-- Estadísticas: 11 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- (1): Línea base corresponde a período 2010-2012. (2): Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012 n/a: No aplica debido a que no hay monitoreo de línea base para esta variable Fuente: Elaboración propia en base de resultados de modelación e “Informe de Calidad del Aire de la Región de Valparaíso, -->
<!-- FIN TABLA 17 -->


Tabla 18: Cumplimiento de normativa en Estación La Greda - Operación ........................ 73

<!-- INICIO TABLA 18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto a SO 2, también se observa cumplimiento de todas las normas de calidad del aire, pudiéndose considerar el aporte del Proyecto en las estaciones La Greda y Los Maitenes, como nulo. Lo que es de esperar dado el bajo contenido de azufre del combustible diesel disponible en Chile (menos de 50 ppm). -->

**Tabla 18: Cumplimiento de Normativa en Estación La Greda - Operación****

| Tipo | Contaminant<br>e | Estadígrafo | Límite | La Greda | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **Contaminant**<br>**e ** | **Estadígrafo** | **Límite** | **Línea Base** | **Línea Base** | ~~**Aporte**~~<br>**Proyecto** | ~~**Aporte**~~<br>**Proyecto** | **Línea base+ Aporte**<br> | **Línea base+ Aporte**<br> | **Línea base+ Aporte**<br> |
| **Tipo** | **Contaminant**<br>**e ** | **Estadígrafo** | **ug/m3 ** | **ug/m3 ** | **% de la**<br>**norma** | **ug/m3 ** | **% de la**<br>**norma** | **ug/m3 ** | ~~**% de**~~<br>**la**<br>**norma** | **Cumplimiento** |
| **Norma Primaria de Calidad**<br>**del Aire (1)**<br> | MP10 | 24 horas,<br>P98 | 150 | 77 | 51,3% | 0,46 | 0,3% | 77 | 51,6% | Cumple |
| **Norma Primaria de Calidad**<br>**del Aire (1)**<br> | MP10 | Anual | 50 | 44 | 88,0% | 0,06 | 0,1% | 44 | 88,1% | Cumple |
| **Norma Primaria de Calidad**<br>**del Aire (1)**<br> | MP2.5 | 24 horas,<br>P98 | 50 | 36 | 72,0% | 0,46 | 0,9% | 36 | 72,9% | Cumple |
| **Norma Primaria de Calidad**<br>**del Aire (1)**<br> | MP2.5 | Anual | 20 | 17 | 85,0% | 0,06 | 0,3% | 17 | 85,3% | Cumple |
| **Norma Primaria de Calidad**<br>**del Aire (1)**<br> | SO2 | 24 horas,<br>P99 | 250 | 64 | 25,6% | 0,00 | 0,0% | 64 | 25,6% | Cumple |
| **Norma Primaria de Calidad**<br>**del Aire (1)**<br> | SO2 | Anual | 80 | 11 | 13,8% | 0,00 | 0,0% | 11 | 13,8% | Cumple |
| **Norma**<br>**Secundaria (2)** | SO2 | Anual | 80 | 14 | 17,5% | 0,00 | 0,0% | 14 | 17,5% | Cumple |
| **Norma**<br>**Secundaria (2)** | SO2 | 24 horas,<br>P99,7 | 365 | 110 | 30,0% | 0,00 | 0,0% | 110 | 30,0% | Cumple |
| **Norma**<br>**Secundaria (2)** | SO2 | 1 hora,<br>P99,73 | 1.000 | 286 | 28,6% | 0,00 | 0,0% | 286 | 28,6% | Cumple |

<!-- Estadísticas: 11 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- (1): Línea base corresponde a período 2010-2012. (2): Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012 n/a: No aplica debido a que no hay monitoreo de línea base para esta variable Fuente: Elaboración propia en base de resultados de modelación e “Informe de Calidad del Aire de la Región de Valparaíso, -->
<!-- FIN TABLA 18 -->


Tabla 19: Cumplimiento de normativa en Estación Los Maitenes - Operación ................... 74

<!-- INICIO TABLA 19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:| |---|---|---| |<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**74/73**<br>|<br>**N° DE PÁGINA**<br>**74/73**<br>| -->

**Tabla 19: Cumplimiento de Normativa en Estación Los Maitenes - Operación****

| Ti<br>po | Contaminante | Estadígrafo | Límite | Los Maitenes | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ti**<br>**po** | **Contaminante** | **Estadígrafo** | **Límite** | **Línea Base** | **Línea Base** | ~~**Aporte**~~<br>**Proyecto** | ~~**Aporte**~~<br>**Proyecto** | **Línea base+ Aporte** | **Línea base+ Aporte** | **Línea base+ Aporte** |
| **Ti**<br>**po** | **Contaminante** | **Estadígrafo** | **ug/m3 ** | **ug/m3 ** | **% de la**<br>**norma** | **ug/**<br>**m3 ** | **% de la**<br>**norma** | **ug/m3 ** | **% de la**<br>**norma** | **Cumplimiento** |
| **Norma Primaria de Calidad**<br>**delAire (1)** | MP10 | 24 horas,<br>P98 | 150 | 56 | 37,3% | 0,04 | 0,0% | 56,04 | 37,4% | Cumple |
| **Norma Primaria de Calidad**<br>**delAire (1)** | MP10 | Anual | 50 | 32 | 64,0% | 0,00 | 0,0% | 32 | 64,0% | Cumple |
| **Norma Primaria de Calidad**<br>**delAire (1)** | MP2.5 | 24 horas,<br>P98 | 50 | 32 | 64,0% | 0,04 | 0,1% | 32,04 | 64,1% | Cumple |
| **Norma Primaria de Calidad**<br>**delAire (1)** | MP2.5 | Anual | 20 | 14 | 70,0% | 0,00 | 0,0% | 14 | 70,0% | Cumple |
| **Norma Primaria de Calidad**<br>**delAire (1)** | SO2 | 24 horas,<br>P99 | 250 | 132 | 52,8% | 0,00 | 0,0% | 132 | 52,8% | Cumple |
| **Norma Primaria de Calidad**<br>**delAire (1)** | SO2 | Anual | 80 | 35 | 43,8% | 0,00 | 0,0% | 35 | 43,8% | Cumple |
| **Norma**<br>**Secundaria (2)** | SO2 | Anual | 80 | 33 | 41,3% | 0,00 | 0,0% | 33 | 41,3% | Cumple |
| **Norma**<br>**Secundaria (2)** | SO2 | 24 horas,<br>P99,7 | 365 | 158 | 43,3% | 0,00 | 0,0% | 158 | 43,3% | Cumple |
| **Norma**<br>**Secundaria (2)** | SO2 | 1 hora,<br>P99,73 | 1.000 | 542 | 54,2% | 0,00 | 0,0% | 541,5 | 54,2% | Cumple |

<!-- Estadísticas: 11 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- (1): Línea base corresponde a período 2010-2012. (2): Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012 n/a: No aplica debido a que no hay monitoreo de línea base para esta variable Fuente: Elaboración propia en base de resultados de modelación e “Informe de Calidad del Aire de la Región de Valparaíso, -->
<!-- FIN TABLA 19 -->


**LISTADO DE FIGURAS**

Figura 1 Localización del Proyecto ...................................................................................... 9

Figura 2 Dominio de modelación y receptores puntuales considerados ............................. 11

Figura 3 Topografía del dominio de modelación ................................................................ 12

Figura 4. Clasificación del clima según Köppen, fuente: Dirección Meteorológica de

Chile. .................................................................................................................... 17

Figura 5. Curva de Iso-concentración, MP10, 24 horas, P98 (Construcción). .................... 46

Figura 6. Curva de Iso-concentración, MP10, anual (Construcción). .................................. 47

Figura 7. Curva de Iso-concentración, MP2.5, 24 horas, P98 (Construcción). ................... 48

Figura 8. Curva de Iso-concentración, MP2.5, anual (Construcción). ................................. 49

Figura 9. Curva de Iso-concentración, SO2, 24 horas, P99 (Construcción)........................ 50

Figura 10. Curva de Iso-concentración, SO2, anual (Construcción). .................................. 51

Figura 11. Curva de Iso-concentración, SO2, 24 horas P99,7 - Norma secundaria

(Construcción). ..................................................................................................... 52

Figura 12. Curva de Iso-concentración, SO2, 1 hora P99,73 - Norma secundaria

(Construcción). ..................................................................................................... 53

Figura 13. Curva de Iso-concentración, MP10, 24 horas, P98 (Operación). ....................... 57

Figura 14. Curva de Iso-concentración, MP10, anual (Operación). .................................... 58

Figura 15. Curva de Iso-concentración, MP2.5, 24 horas, P98 (Operación). ...................... 59

Figura 16. Curva de Iso-concentración, MP2.5, anual (Operación). ................................... 60

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**5/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**5/ 73**|

Figura 17. Ciclo diario de magnitud del viento Est. Principal, año 2013 (observado). ......... 61

Figura 18. Ciclo diario de magnitud del viento Est. Principal, año 2013 (simulado). ........... 62

Figura 19. Ciclo diario de dirección del viento, porcentaje de ocurrencia (%), Est.

Principal, año 2013 (observado). .......................................................................... 63

Figura 20. Ciclo diario de dirección del viento, porcentaje de ocurrencia (%), Est.

Principal, año 2013 (simulado). ............................................................................ 64

Figura 21. Rosas de viento año 2013, Est. Principal (observado). ..................................... 65

Figura 22. Rosas de viento año 2013, Est. Principal (simulado)......................................... 66

Figura 23. Ciclo estacional del viento, Est. Principal, año 2013 (observado). ..................... 67

Figura 24. Ciclo estacional del viento, Est. Principal, año 2013 (simulado). ....................... 67

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**6/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**6/ 73**|

**1.0** **INTRODUCCIÓN**

El presente estudio contiene los resultados de la simulación de dispersión de contaminantes,
que permite estimar las concentración de MP10, MP2.5 y gases, asociadas al Proyecto DIA
“”MEJORAMIENTO CONDICIONES DE ALMACENAMIENTO DE CONCENTRADO DE
COBRE, 46.000 TON”, en adelante el Proyecto.

La estimación de las emisiones atmosféricas se presentan en el Apéndice 1 “Estimación de
Emisiones Atmosféricas”, las que corresponden principalmente a material particulado (MP10
y MP2.5) producido durante las actividades de construcción y operación del Proyecto.

Según lo recomendado por la autoridad competente a otros Proyectos evaluados en la
región, los niveles de emisión generados por estas actividades se estimaron utilizando las
ecuaciones y factores de emisión contenidos en la “Guía Metodológica Inventario de
Emisiones Atmosféricas: M11 Metodología SINCA 2011” (http://www.sinia.cl/1292/w3article-52667.html), complementado de ser necesario con metodología e información del
Reporte AP-42 de la U.S. EPA (AP-42, Compilation of Air Pollutant Emision Factors, versión
digital).

El objetivo de la modelación es evaluar el efecto que tendrá el Proyecto en los receptores
de su área de influencia en su fase más emisora, y en particular en las estaciones de calidad
del aire cercanas al Proyecto es decir Estación La Greda y Las Maitenes.

Según se ha determinado en el Apéndice 1 “Estimación de Emisiones Atmosféricas” la fase
más emisora correspondería a la etapa de construcción. Sin embargo, dada la permanencia
que tendrá la fase de operación en el tiempo, se ha realizado una modelación de ambas
fases, construcción y operación.

La herramienta más comúnmente utilizada para caracterizar cuantitativamente los efectos
de las emisiones de contaminantes atmosféricos sobre la calidad del aire, es la aplicación
de modelos matemáticos. Estos modelos permiten estimar la distribución espacial de las
concentraciones del compuesto modelado, basándose en las características de las
emisiones (ubicación de la fuente de emisión, tasa de emisión, velocidad de salida, altura de
la emisión, temperatura, entre otros), características del terreno (topografía) y datos
meteorológicos.

La simulación de dispersión fue realizada mediante la aplicación del modelo de dispersión
Calpuff, el cual corresponde a uno de los modelos más avanzado recomendado por la
_Environmental Protection Agency_ (EPA) y por la “Guía para el uso de modelos de calidad
del aire en el SEIA, año 2012 [1] ”, para Proyectos que cumplen con las siguientes condiciones:

 Emisión permanente durante la etapa de operación.

1 Guía Para el Uso de Modelos de Calidad del Aire en el SEIA, año 2012, Ministerio del Medio Ambiente

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**7/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**7/ 73**|

 Emisiones inyectadas a través de una chimenea con un empuje térmico importante.

 Receptores ubicados a más de 5 km de área de emisión.

 - Terreno complejo.

Si bien el Proyecto se ubica cercano al borde costero, al no incluir éste grandes chimeneas
con empuje térmico importante, los efectos de fumigación costera son poco significativos, no
obstante dado que se encuentra en una zona declarada como saturada por MP10 y SO 2, se
ha considerado el uso del modelo Calpuff para la evaluación de la dispersión de sus
emisiones.

La estructura del estudio considera los siguientes puntos:

 - Normativa de calidad del aire aplicable.

 - Caracterización del área de estudio.

 - Presentación de datos utilizados.

 Línea base meteorológica.

 - Línea base de calidad del aire.

 - Modelación de calidad del aire.

 - Conclusiones.

**2.0** **OBJETIVOS**

2.1 OBJETIVO GENERAL

Evaluar el aporte de las emisiones del Proyecto en su etapa de construcción y operación, en
su área de influencia y en particular en las estaciones más cercanas al Proyecto, Estación
La Greda y Estación Maitenes.

2.2 OBJETIVOS ESPECÍFICOS

Los objetivos específicos corresponden a:

 - Establecer la línea base de calidad del aire.

 Establecer la línea base de meteorología.

 - Establecer las concentraciones a esperar en la calidad del aire en general y en los
receptores cercanos en particular, por medio de la utilización del modelo Calpuff.

 Análisis de nivel de cumplimento de la normativa de calidad del aire, en base a los
aportes modelados del Proyecto y los registros de Línea Base.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**8/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**8/ 73**|

**3.0** **NORMATIVA DE CALIDAD DE APLICABLE**

Tabla 1 se muestran las normas de calidad del aire vigentes aplicables al Proyecto y
utilizadas en la evaluación del efecto que tendrá en la calidad del aire.

**Tabla 1: Normativa de Calidad aplicable al Proyecto.**

|Tipo|Normativa|Estadígrafo|Límite|
|---|---|---|---|
|**Tipo**<br>|**Normativa**|**Estadígrafo**|**(ug/m3N)**|
|**Norma Primaria de**<br>**Calidad del Aire**|MP10 (D.S N°20/13 MIN. DEL MEDIO<br>AMBIENTE)|Promedio diario, percentil 98|150|
|**Norma Primaria de**<br>**Calidad del Aire**|MP10 (D.S N°20/13 MIN. DEL MEDIO<br>AMBIENTE)|Media aritmética anual|50|
|**Norma Primaria de**<br>**Calidad del Aire**|MP2.5 (D.S N°12/11 MINSEGPRES)|Promedio diario, percentil 98|50|
|**Norma Primaria de**<br>**Calidad del Aire**|MP2.5 (D.S N°12/11 MINSEGPRES)|Media aritmética anual|20|
|**Norma Primaria de**<br>**Calidad del Aire**|SO2 (D.S N°113/02 MINSEGPRES)|Promedio diario, percentil 99|250|
|**Norma Primaria de**<br>**Calidad del Aire**|SO2 (D.S N°113/02 MINSEGPRES)|Media aritmética anual|80|
|**Norma**<br>**Secundaria**|SO2 (D.S N°22/09 MINSEGPRES, Zona Norte)|Promedio anual|80|
|**Norma**<br>**Secundaria**|SO2 (D.S N°22/09 MINSEGPRES, Zona Norte)|Promedio diario, percentil 99,7|365|
|**Norma**<br>**Secundaria**|SO2 (D.S N°22/09 MINSEGPRES, Zona Norte)|Promedio de 1 hora, percentil 99,73|1.000|

Fuente: Elaboración propia.

**4.0** **CARACTERIZACIÓN DEL ÁREA DE ESTUDIO**

4.1 LOCALIZACIÓN

En la Figura 1 se muestra una vista general de la zona donde se emplazará el Proyecto la
cual corresponde a la Región de Valparaíso, en el complejo industrial de Ventanas, en la
costa de la V región, y a una altura promedio de 20,0 m.s.n.m.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**9/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**9/ 73**|

**Figura 1. Localización del Proyecto**

**5.0** **PRESENTACIÓN DE DATOS UTILIZADOS**

5.1 DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO

El Proyecto considera la modelación de la dispersión utilizando el modelo Calpuff,
alimentado con campos de viento obtenidos del modelo WRF. Calpuff corresponde a un
modelo de dispersión de tercera generación que cual se ajusta a la complejidad de la
simulación de emisiones de gases y partículas a altas temperaturas por chimenea, así como
la evaluación de receptores a larga distancia (más de 5km).

A su vez, el modelo WRF, es uno de los modelos meteorológicos de pronóstico más
avanzados y completos, por lo que su utilización en la generación de los campos de viento
utilizados en Calpuff permite dar robustez a la simulación en condiciones de terreno
complejo, y de evaluaciones de dispersión a larga distancia como las presentadas por el
Proyecto, si bien la zona donde se desarrollará el Proyecto no corresponde a una topografía
compleja, debido a que presenta poco relieve y no existen grandes masas de agua.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**10/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**10/ 73**|

5.2 RECEPTORES CONSIDERADOS

En la evaluación de las concentraciones aportadas por el Proyecto en su área de
influencia, se han considerado los receptores puntuales que se muestran en la Tabla 2,
correspondientes a las estaciones de calidad del aire más cercanas al Proyecto.

**Tabla 2: Receptores Puntuales** **considerados.**

|Estación|Coordenadas UTM Datum<br>WGS84|Col3|Uso|Distancia a<br>Proyecto|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Sur (m)**|**Sur (m)**|**km**|
|La Greda|268.185|6.373.910|19 Sur|0,95|
|Los Maitenes|270.073|6.372.171|19 Sur|2,9|

Fuente: Elaboración propia.

5.3 DOMINIO DE MODELACIÓN

En la Figura 2, se muestra el dominio de modelación, asimismo se observa la ubicación
relativa de los receptores respecto a las fuentes de emisión evaluadas. La extensión del
dominio se ha seleccionado considerando las estaciones de calidad del aire y sitios poblados
más cercanos. En la Tabla 3, se indican los parámetros considerados en el dominio de
modelación.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**11/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**11/ 73**|

**Figura 2. Dominio de Modelación y Receptores Puntuales considerados**

**Tabla 3: Características del Dominio de Modelación.**

|Descripción|Detalle|
|---|---|
|Tamaño de la grilla|1 km x 1 km|
|Resolución horizontal y vertical del<br>dominio|20 km (Este - Oeste) x 20 km (Norte - Sur)|
|Número capas|11 entre 0 y 4.000 m de altura|
|Coordenadas central de origen (UTM)|267.003 m E y 6.370.378 m S, Datum WGS 84|
|Área del dominio en km2|400 km2|
|Topografía|Extraída de SRTM3 con resolución de 90 m|
|Usos de suelo|Extraídos de Global Land Cover Characterization<br>(GLCC) del US Geological Survey (UGS), EEUU.|

Fuente: Elaboración propia.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**12/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**12/ 73**|

5.4 TOPOGRAFÍA

La información topográfica utilizada en la modelación del Proyecto corresponde a cartas
topográficas digitales SRTM3, con resolución de 90 metros, la cual se muestran en la Figura
3.

**Figura 3. Topografía del Dominio de Modelación**

5.5 FUENTES DE EMISIÓN Y PARÁMETROS UTILIZADOS EN MODELACIÓN

**5.5.1** **Fuentes de emisión**

Considerando el tipo de Proyecto, se ha realizado una modelación de la etapa de
construcción y operación.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**13/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**13/ 73**|

_**Etapa de Construcción**_

En la Tabla 4 se muestran las fuentes emisoras modeladas en Calpuff y las actividades
emisoras consideradas.

**Tabla 4: Fuentes Modeladas en Calpuff y Actividades Emisoras Asociadas - Etapa de**

**Construcción.**

|Source<br>ID|Actividades|Tipo de Fuente|Área|Período|Col6|Col7|
|---|---|---|---|---|---|---|
|**Source**<br>**ID**|**Actividades**|**Tipo de Fuente**|**m2 **|**meses**|**días/mes**|**horas/día**|
|SRC_1|Movimiento de<br>tierra|Área|4.166|10|24|15|
|SRC_1|Maquinarias|Maquinarias|Maquinarias|Maquinarias|Maquinarias|Maquinarias|
|SRC_2|Circulación de<br>vehículos por<br>caminos<br>pavimentados<br>(Fuentes móviles)|Línea - Área|130.764|10|24|15|

Fuente: Elaboración propia.

En la Tabla 5 y Tabla 6 se muestra la emisión de las fuentes y la tasa de emisión calculada
en gramos por segundo, para material particulado y gases respectivamente. La tasa de
emisión se ha estimado considerado un funcionamiento de 10 meses, 6 días a la semana
(lunes a sábado), dos turnos (día y noche), lo que corresponde a un total de 15 horas al día,
considerando el límite de horas laborales (45 horas semanales por turno).

**Tabla 5: Tasa de Emisión de Material Particulado y Fuente Modelada Asociada - Etapa**
**Construcción.**

|Source<br>ID|Actividades|MP10|Col4|Col5|MP2.5|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Source**<br>**ID**|**Actividades**|**ton/período**|**g/s**|**g/(m2*s)**|**ton/período**|**g/s**|**g/(m2*s)**|
|SRC_1|Movimiento de tierra|2,281|1,76E-01|4,22E-05|2,281|1,76E-01|4,22E-05|
|SRC_1|Maquinarias|Maquinarias|Maquinarias|Maquinarias|Maquinarias|Maquinarias|Maquinarias|
|SRC_2|Circulación de<br>vehículos por<br>caminos<br>pavimentados<br>(Fuentes móviles)|0,513|3,96E-02|3,03E-07|0,076|5,86E-03|4,48E-08|
|**Total Emisión:**|**Total Emisión:**|**2,794**|**2,16E-01**||**2,357**|**1,82E-01**||

Fuente: Elaboración propia.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**14/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**14/ 73**|

**Tabla 6: Tasa de Emisión de Gases y Fuente Modelada Asociada - Etapa**

**Construcción.**

|Source<br>ID|Actividades|SO<br>2|Col4|Col5|
|---|---|---|---|---|
|**Source**<br>**ID**|**Actividades**|**ton/período**|**g/s**|**g/(m2*s)**|
|SRC_1|Movimiento<br>de tierra|0,000|0,00E+00|0,00E+00|
|SRC_1|Maquinarias|Maquinarias|Maquinarias|Maquinarias|
|SRC_2|Circulación<br>de vehículos<br>por caminos<br>pavimentados<br>(Fuentes<br>móviles)|0,003|2,31E-04|1,77E-09|
|**Total Emisión:**|**Total Emisión:**|**0,003**|**2,31E-04**||

Fuente: Elaboración propia.

_**Etapa de Operación**_

En la Tabla 7 se muestran las fuentes emisoras modeladas en Calpuff y las actividades
emisoras consideradas.

**Tabla 7: Fuentes Modeladas en Calpuff y Actividades Emisoras Asociadas - Etapa de**

**Operación.**

|Source<br>ID|Actividades|Tipo de Fuente|Área|Período|Col6|Col7|
|---|---|---|---|---|---|---|
|**Source**<br>**ID**|**Actividades**|**Tipo de Fuente**|**m2 **|**meses**|**días/mes**|**horas/día**|
|SRC_1|Maquinaria (2<br>cargadores<br>frontales)|Área|4.166|12|1|24|
|SRC_1|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|30|24|

Fuente: Elaboración propia.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**15/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**15/ 73**|

En la Tabla 8 y Tabla 9 se muestra la emisión de las fuentes y la tasa de emisión calculada
en gramos por segundo, para material particulado y gases. La tasa de emisión se ha
estimado considerando el tiempo de funcionamiento indicado en la tabla anterior.

**Tabla 8: Tasa de Emisión de Material Particulado y Fuente Modelada Asociada -**

**Etapa Operación.**

|Source<br>ID|Actividades|MP10|Col4|MP2.5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Source**<br>**ID**|**Actividades**|**g/s**|**g/(m2*s)**|**ton/período**|**g/s**|**g/(m2*s)**|
|SRC_1|Maquinaria (2<br>cargadores frontales)|1,91E-02|4,58E-06|0,396|1,91E-02|4,58E-06|
|SRC_1|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|Transporte y<br>transferencia de<br>material|
|**Total Emisión:**|**Total Emisión:**|**1,91E-02**||**0,396**|**1,91E-02**||

Fuente: Elaboración propia.

**Tabla 9: Tasa de Emisión de Gases y Fuente Modelada Asociada - Etapa Operación.**

|Source<br>ID|Actividades|SO<br>2|Col4|Col5|
|---|---|---|---|---|
|**Source**<br>**ID**|**Actividades**|**ton/período**|**g/s**|**g/(m2*s)**|
|SRC_1|Maquinaria<br>(2<br>cargadores<br>frontales)|0,000|0,00E+00|0,00E+00|
|SRC_1|Transporte y<br>transferencia<br>de material|Transporte y<br>transferencia<br>de material|Transporte y<br>transferencia<br>de material|Transporte y<br>transferencia<br>de material|
|**Total Emisión:**|**Total Emisión:**|**0,000**|**0,00E+00**||

Fuente: Elaboración propia.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**16/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**16/ 73**|

**6.0** **LÍNEA BASE DE CLIMA Y METEOROLÓGICA**

A continuación se presenta el análisis de los datos meteorológicos observacionales, año
2013, en el área de modelación. Para el análisis se han utilizado los datos de la Estación
Meteorológica Principal de la red Ventanas, por estar cerca del Proyecto (1,4 km) y presentar
mayor número de parámetros monitoreados. Los parámetros monitoreados se muestran en
la Tabla 10.

**Tabla 10: Estaciones Meteorológicas disponibles en la zona**

|Estación|Coordenadas UTM<br>Datum WGS84|Col3|Información registrada|
|---|---|---|---|
|**Estación**|**Este (m)**|**Sur (m)**|**Sur (m)**|
|Est. Meteorológica<br>Principal|267.310|6371.939|V V, DV, Temperatura, HR, Presión, Radiación<br>y Precipitaciones.|

Fuente: Elaboración propia.

6.1 CARACTERIZACIÓN CLIMÁTICA REGIONAL

El clima es un fenómeno natural que se da a nivel atmosférico, caracterizado por una serie
de parámetros meteorológicos como temperatura, humedad relativa, presión,
precipitaciones, viento, entre otros, los cuales dependen de la geografía de una región en
particular.

El área de estudio se ubica en la V región de Valparaíso, la cual presenta tres tipos de clima
principalmente:

 Clima templado cálido con estación seca prolongada y gran nubosidad.

 Clima templado cálido con estación seca prolongada.

 Clima templado cálido con estación seca.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**17/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**17/ 73**|

**Figura 4. Clasificación del Clima según Köppen. Fuente: Dirección Meteorológica de**
**Chile.**

La zona de estudio presenta un clima principalmente. Corresponde al tipo Templado Cálido
con Estación Seca Prolongada de 8 a 7 meses y Gran Nubosidad.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**18/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**18/ 73**|

**6.1.1** **Clima Templado Cálido con estación seca prolongada y gran nubosidad**

Este clima se presenta en la zona litoral desde los 32°S por el norte, hasta la desembocadura
del río Mataquito. Se caracteriza por abundante nubosidad, no obstante, no persistente (a
diferencia de lo que ocurre en la IV región). La nubosidad y la cercanía con la costa definen
una amplitud térmica de 10°C aproximadamente. El régimen pluviométrico es básicamente
de origen frontal, manifestándose mayormente en los meses de mayo a agosto, cuando
precipita el 80% del total anual, que alcanza un valor climatológico entre 300 y 600
milímetros.

La circulación de los vientos predominante es del suroeste, registrándose vientos en las
tardes, y vientos calmos durante la noche y la mañana con una intensidad aproximada de
18 Km/h (5 m/s).

6.2 PRESENTACIÓN DE DATOS METEOROLÓGICOS OBSERVADOS

**6.2.1** **Series de Tiempo**

Para el presente análisis se consideraron las mediciones de dirección e intensidad de los
vientos a una altura de 10 m del suelo. Para el análisis del comportamiento del viento se han
considerado datos del año 2013 debido a que es el año más reciente disponible.

Los gráficos de la serie temporal presentados a continuación, permiten un análisis cualitativo
de los datos en términos de completitud de la serie y periodos con datos faltantes, valores
fuera de rango y problemas de equipos (datos constantes, tendencias, entre otras).

**Gráfico 1: Serie de Tiempo para Registros Horarios de Velocidad del Viento,**

**Estación Principal año 2013.**

La serie de tiempo de la velocidad del viento, muestra un comportamiento similar en todas
las épocas del año. En la época invernal se observan valores altos de velocidad del viento,
debido al paso de sistemas de bajas presiones por la zona, no obstante en general las
velocidades son menores a las observadas en la época estival. Los valores fluctúan entre 0
y 9,5 m/s con un promedio de velocidad de 2,3 m/s. No se observan valores fuera de rango
con sobre el 99% de los datos.

**Gráfico 2: Serie de Tiempo para Registros Horarios de Dirección del Viento,**

**Estación Principal, año 2013**

La serie de tiempo de la dirección del viento, muestra dos direcciones predominantes oeste
(270°) y este (90°), lo que sugiere la ocurrencia de ciclos diurnos de rotación del viento. No
se observan datos fuera de rango, con el 99% de los datos.

**Gráfico 3: Serie de Tiempo para Registros Horarios de Temperatura, Estación**

**Principal, año 2013**

La serie de tiempo de la temperatura, muestra que durante el periodo estival las
temperaturas son superiores a lo observado en el periodo invernal. En invierno, las
temperaturas inclusive descienden de los 0°C en algunas ocasiones. El valor medio de la
temperatura alcanza los 12,2°C. La máxima se registra en verano, 23,9°C y la mínima en
invierno, -1,1°C. Este comportamiento es típico de estaciones de latitudes medias cercanas
a la costa: veranos cálidos e inviernos fríos con escasa amplitud térmica. No se observan
datos fuera de rango, con un 98% de los datos registrados.

**Gráfico 4: Serie de Tiempo para Registros Horarios de Humedad Relativa, Estación**

**Principal, año 2013.**

La serie de tiempo de la humedad relativa, muestra escasa diferencia entre lo observado en
invierno con lo observado en verano. Al ser una estación cercana a la costa, se observan
valores cercanos al 100% durante todo el año. El valor medio es 83%. No se observan
valores fuera de rango, con un 99% de los valores registrados.

**Gráfico 5: Serie de Tiempo para Registros Horarios de Presión Atmosférica,**

**Estación Principal, año 2013.**

La serie de tiempo de la presión atmosférica, muestra escasa amplitud durante el año. Las
mayores presiones se presentan finalizando el invierno y en primavera. Los valores oscilan
entre 1002 y 1024 mb. No se observan valores fuera de rango, con un 99% de los valores
registrados.

**Gráfico 6: Serie de Tiempo para Registros Horarios de Radiación Solar, Estación**

**Principal, año 2013.**

La serie de tiempo de la radiación solar, muestra que la mayor radiación se recibe en época
estival y la menor en época invernal. Este es un comportamiento típico de estaciones de
latitudes medias. No se observan valores fuera de rango, con un 99% de los valores
registrados.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**23/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**23/ 73**|

**Gráfico 7: Serie de Tiempo para Registros Diarios de Precipitación**

**Estación Principal año 2013**

Los valores acumulados diarios de precipitación, muestran escasos eventos de
precipitaciones durante el año 2013, concentrados en los meses invernales. El evento con
mayor precipitación se registró en mayo con 42,7 mm.

**6.2.2** **Ciclos Diarios**

A continuación se muestra un análisis de los ciclos diarios de las variables medidas en la
Estación Principal.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**24/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**24/ 73**|

**Gráfico 8: Serie de Tiempo para Registros Diarios de Precipitación.**

**Estación Principal año 2013.**

En el Gráfico 8 se observa el perfil diurno de la velocidad del viento. En promedio, se
presenta de 2,3 m/s. Durante la tarde se registran las mayores velocidades, sobrepasando
los 3 m/s entre las 11:00 y 17:00 horas, con una intensidad máxima de 3,8 m/s a las 14:00
horas. El mínimo de velocidad se produce entre las 23:00 y 02:00 horas, con un valor mínimo
de 1,5 m/s.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**25/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**25/ 73**|

**Gráfico 9: Ciclo Diurno de la Dirección del Viento, Porcentaje de Ocurrencia,**

**Estación Principal, año 2013.**

El Gráfico 9, muestra el porcentaje de ocurrencia para la dirección del viento. Se puede
observar un ciclo diurno típico del ciclo tierra-mar mar-tierra. Durante la noche y madrugada
el viento predominante es de dirección este (tierra a mar) mientras que durante la mañana y
tarde/noche el viento es predominante del oeste (mar a tierra).

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**26/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**26/ 73**|

**Gráfico 10: Ciclo Diurno de los Promedios Horarios de la Temperatura,**

**Estación Principal, año 2013**

El ciclo diario de la temperatura muestra un comportamiento con una mínima matutina, en
torno a las 05:00-07:00 horas cercana a los 8,3 °C, y una máxima por la tarde cerca de las
14:00 horas cercana a los 14 °C. Se observa una amplitud térmica en los valores medios
horarios, reflejado en los percentiles, las mínimas podrían llegar a los 2 °C y las máximas
cercanas a 18 °C.

**Gráfico 11: Ciclo Diurno de los Promedios Horarios de la Humedad Relativa,**

**Estación Principal, año 2013.**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**27/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**27/ 73**|

Se observa el ciclo diurno de la humedad relativa. Se presentan los mayores valores durante
la noche y la madrugada, coincidiendo con el momento de menor temperatura e intensidad
del viento. Durante la tarde la humedad disminuye a valores medios, alrededor de un 75%.
En general, la estación presenta valores altos de humedad relativa, esto debido
principalmente a su cercanía con la costa.

**Gráfico 12: Ciclo Diurno de los Promedios Horarios de la Presión Atmosférica,**

**Estación Principal, año 2013.**

En el Gráfico 12 se observa el ciclo diurno de la presión atmosférica. Se observa un ciclo
diurno poco pronunciado, con un máximo relativo de presión en horas de la mañana y dos
mínimos, uno en la madrugada y otro en la tarde.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**28/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**28/ 73**|

**Gráfico 13: Ciclo Diurno de los Promedios Horarios de la Radiación Solar, Estación**

**Principal, año 2013.**

En el Gráfico 13 se observa el ciclo diurno de la radiación solar. Se puede apreciar que el
máximo se presenta entre las 10:00 y 15:00 horas con un peak a las 14:00 horas. Entre las
20:00 y 05:00 horas la radiación promedio es cero.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**29/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**29/ 73**|

**6.2.3** **Rosa del Viento**

|Rosa de Viento Período 01:00 AM a 06:00 AM Entre el 01/01/2013<br>y el 31/12/2013|Rosa de Viento Período 07:00 AM a 12:00 AM Entre el 01/01/2013<br>y el 31/12/2013|
|---|---|
|<br>Rosa de Viento Período 13:00 PM a 18:00 PM Entre el 01/01/2013 y<br>el 31/12/2013|<br>Rosa de Viento Período 19:00 PM a 24:00 AM Entre el 01/01/2013 y<br>el 31/12/2013|

**Gráfico 14: Rosa del Viento, Ciclo Diario, Estación Principal, año 2013.**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**30/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**30/ 73**|

La dirección de viento durante el día presenta dos direcciones predominantes: este y oeste.
Durante la madrugada, entre las 01:00 y 06:00 horas, el viento predominante proviene de la
dirección este, con intensidades débiles, entre 0,5 y 3,6 m/s. Entre las 07:00 y las 12:00
horas, la predominancia de los vientos se comparte entre este y oeste, es el momento del
día en que la circulación tierra-mar comienza a cambiar a mar-tierra. La intensidad mayor se
presenta en los vientos de dirección oeste, mayormente entre 2,1 y 5,6 m/s. Entre las 13:00
y las 18:00 horas el viento de es predominante del oeste y con las mayores intensidades del
día, que alcanzan los 8.8 m/s. Hacia la noche, entre las 19:00 y las 24:00 horas, continúa la
predominancia de vientos del oeste, no obstante comienza la rotación al este.

Durante toda la jornada, son los vientos de dirección oeste los que presentan las mayores
intensidades.

**Gráfico 15: Rosa del viento, estación INIA, año 2013.**

La dirección del viento, muestra que la dirección predominante, en porcentaje e intensidad,
es la dirección oeste.

En cuanto al gráfico de frecuencias por clase de intensidad, se observa una distribución de
Wiebull con mayores frecuencias en intensidades ligeramente bajo la media, entre 0,5 y 2,1
m/s.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**31/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**31/ 73**|

**6.2.4** **Ciclos Estacionales**

**Gráfico 16: Ciclo Estacional del Viento, Estación Principal año 2013**

El ciclo estacional del viento, muestra que en el general las mayores velocidades del viento
se producen durante el día, dejando las menores velocidades en la noche y madrugada. En
los meses invernales el máximo de viento se produce entre las 12:00 y 18:00 horas, mientras
que en los meses estivales entre las 10:00 y 20:00 horas aproximadamente. El máximo
_maximorum_ del viento se produce en noviembre, entre las 14:00 y 17:00 horas con valores
cercanos a los 5 m/s (color rojo), este máximo se repite levemente inferior, en febrero en el
mismo horario. La dirección predominante al momento de los máximos vientos es oeste, y
durante los vientos débiles (color azul) es este.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**32/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**32/ 73**|

**Gráfico 17: Ciclo Estacional de la Temperatura, Estación Principal año 2013,**

El ciclo estacional de la temperatura muestra que en los meses estivales presentan las
mayores temperaturas observándose un máximo _maximorum_ entorno a las 16:00 horas
entre enero y febrero. El mínimo _minimorum_ se presenta entre julio y septiembre alrededor
de las 07:00 horas. Las temperaturas mínimas en los meses estivales, diciembre a marzo,
iguala o supera a la temperatura máxima registrada durante el invierno.

**Gráfico 18: Ciclo Estacional de la Humedad Relativa, Estación Principal año 2013.**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**33/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**33/ 73**|

El ciclo estacional de la humedad relativa, muestra que las mayores humedades (colores
rojos), durante todo el año se presentan entre las 22:00 y 09:00 horas aproximadamente. En
general, entre las 12:00 y 19:00 horas, en todos los meses, se observan valores menores de
humedad.

**Gráfico 19: Ciclo Estacional de la Presión Atmosférica, Estación Principal año 2013.**

La presión atmosférica, muestra un ciclo estacional que va de máximos de presión entre
agosto y septiembre a mínimos entre enero y febrero.

**Gráfico 20: Ciclo Estacional de la Radiación Solar, Estación Principal año 2013**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**34/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**34/ 73**|

El ciclo estacional de la radiación solar muestra que las una mayor cantidad de horas con
radiación en los meses estivales y menor en los invernales. Mientras en verano desde las
06:00 hasta las 21:00 horas comienzan a registrarse valores de radiación, en invierno sucede
entre las 07:00 y 19:00 horas. El máximo maximorum ocurren entre diciembre y febrero entre
las 14:00 y 16:00 horas.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**35/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**35/ 73**|

**7.0** **LÍNEA BASE DE CALIDAD DEL AIRE**

7.1 LÍNEA BASE DE CALIDAD DEL AIRE

En la Tabla 11, se presenta la línea base de calidad de aire a utilizar en la evaluación del
efecto del Proyecto, la cual ha sido elaborada a partir de los antecedentes contenidos en el
“Informe de Calidad del Aire de la Región de Valparaíso período 2010 - 2012”, elaborado
por la SEREMI de Salud de la Región de Valparaíso, por ser la información oficial más
actualizada disponible.

**Tabla 11: Línea Base de Calidad del Aire Período (2010-2012).**

|Tipo|Contaminante|Estadígrafo|Límite|La Greda|Col6|Los Maitenes|Col8|
|---|---|---|---|---|---|---|---|
|**Tipo**|**Contaminante**|**Estadígrafo**|**Límite**|**Línea Base**|**Línea Base**|**Línea Base**|**Línea Base**|
|**Tipo**|**Contaminante**|**Estadígrafo**|**(ug/m3)**|**ug/m3 **|**% de la norma**|**ug/m3**|**% de la norma**|
|**Norma Primaria de Calidad**<br>**del Aire (1)**|MP10|24 horas, P98|150|77|51,3%|56|37,3%|
|**Norma Primaria de Calidad**<br>**del Aire (1)**|MP10|Anual|50|44|88,0%|32|64,0%|
|**Norma Primaria de Calidad**<br>**del Aire (1)**|MP2.5|24 horas, P98|50|36|72,0%|32|64,0%|
|**Norma Primaria de Calidad**<br>**del Aire (1)**|MP2.5|Anual|20|17|85,0%|14|70,0%|
|**Norma Primaria de Calidad**<br>**del Aire (1)**|SO2|24 horas, P99|250|64|25,6%|132|52,8%|
|**Norma Primaria de Calidad**<br>**del Aire (1)**|SO2|Anual|80|11|13,8%|35|43,8%|
|**Norma Secundaria (2)**|SO2|Anual|80|14|17,5%|33|41,3%|
|**Norma Secundaria (2)**|SO2|24 horas, P99,7|365|110|30,0%|158|43,3%|
|**Norma Secundaria (2)**|SO2|1 hora, P99,73|1.000|286|28,6%|542|54,2%|

(1) Línea base corresponde a período 2010-2012.
(2) Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año
2011 y 2012.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**36/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**36/ 73**|

7.2 PRESENTACIÓN DE DATOS DE CALIDAD DEL AIRE OBSERVADOS

A partir de los datos horarios de calidad del aire registrados estación La Greda y Los Maitenes durante
el año 2013 se ha realizado un análisis del comportamiento temporal de las concentraciones. El año
de análisis se escogió a modo que coincidiera con el año de la modelación de calidad del aire, y
corresponde al año más reciente con datos disponibles. Sin embargo, es importante aclarar que para
efectos de línea base, se consideraron los datos contenidos en el “Informe de Calidad del Aire de la
Región de Valparaíso, Período 2010 -2012”, de la SEREMI de Salud, Región de Valparaíso, debido
a que representan la información oficial más actualizada de evaluación de la calidad del aire en la
región.

**7.2.1** **Series de Tiempo**

Los gráficos de la serie temporal presentados a continuación, permiten un análisis cualitativo
de los datos en términos de completitud de la serie y periodos con datos faltantes, valores
fuera de rango y problemas de equipos (datos constantes, tendencias, entre otras).

_**Serie de Tiempo de MP10**_

**Gráfico 21: Concentración Diaria de MP10, Estación La Greda, año 2013.**

**Gráfico 22: Concentración Diaria de MP10, Estación Los Maitenes, año 2013.**

_**Serie de Tiempo de MP 2.5**_

**Gráfico 23: Concentración Diaria de MP2.5, Estación La Greda, año 2013.**

**Gráfico 24: Concentración Diaria de MP2.5, Estación Los Maitenes, año 2013.**

**7.2.2** **Ciclos Diarios**

**Gráfico 25: Ciclo Diario del MP10, Estación La Greda, año 2013**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**39/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**39/ 73**|

**Gráfico 26: Ciclo diario del MP10, Estación Los Maitenes, año 2013**

En el Gráfico 25 y Gráfico 26, se observa que en La Greda las mayores concentraciones de
MP10 ocurren desde las 10:00 hasta las 23:00 momento en que empiezan a decrecer,
mientras que en Los Maitenes, las concentraciones tienen un período de máximos más
acotado y también de menor intensidad el cual ocurren entre las 10:00 y 18:00 horas.

**Gráfico 27: Ciclo diario del MP2.5, Estación La Greda, año 2013**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**40/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**40/ 73**|

**Gráfico 28: Ciclo Diario del MP2.5, Estación Los Maitenes, año 2013**

Según se observa en el Gráfico 27 en La Greda, ocurren dos máximos de concentraciones
MP2.5 uno a medio día y otro en la noche, mientras que en el Gráfico 28, se observa que en
la Estación Los Maitenes presenta solo un máximo al medio día

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**41/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**41/ 73**|

**7.2.3** **Ciclos Estacionales**

A continuación se muestra el ciclo estacional de las concentraciones de calidad del aire.

**Gráfico 29: Ciclo Estacional de MP10, Estación La Greda, año 2013**

**Gráfico 30: Ciclo Estacional de MP10, Estación Los Maitenes, año 2013**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**42/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**42/ 73**|

En el Gráfico 29 y Gráfico 30, se observa que las mayores concentraciones de MP10 en
estación La Greda ocurren entre las 12:00 y 22:00, principalmente en época invernal, entre
los meses de julio y agosto, mientras en la estación Los Maitenes las mayores
concentraciones ocurren entre las 11:00 y 15:00 horas desde enero a septiembre, también
se observa otros máximos a las 19:00, en el mes de marzo.

**Gráfico 31: Ciclo Estacional de MP2.5, Estación La Greda, año 2013**

**Gráfico 32: Ciclo Estacional de MP2.5, Estación Los Maitenes, año 2013**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br> <br> <br>**43/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**43/ 73**|

En el Gráfico 31 y Gráfico 32, se observa que las mayores concentraciones de MP2.5 en
estación La Greda ocurren en horario nocturno entre las 20:00 y las 06:00 am, y en época
invernal entre mayo y agosto, mientras que en la estación Los Maitenes las máximas
concentraciones ocurren entre las 12:00 y las 14:00 desde marzo a septiembre.

**8.0** **MODELACIÓN DE CALIDAD DEL AIRE Y RESULTADOS**

Se ha realizado una modelación de las emisiones de Proyecto en su etapa de construcción
y operación, utilizando modelo Calpuff.

8.1 APORTES DEL PROYECTO

**8.1.1** **Etapa de Construcción**

En la Tabla 12 y las figuras siguientes de iso-líneas de concentración se muestran los aportes
modelados del Proyecto, en la etapa de construcción, en los receptores puntuales
considerados y en el punto de máximo impacto (PMI). Es importante señalar que el período
de construcción será acotado, no superando los 10 meses.

En la Tabla 12 se observa, que los aportes del Proyecto en los receptores puntuales son de
baja magnitud.

Respecto a MP10 y MP2.5 los aportes en la Estación La Greda no superan el 8,4% del valor
de la norma, mientras que en la Estación Los Maitenes, no supera el 0,7%. En aquellos
estadígrafos que evalúan concentraciones de largo plazo (anuales), el aporte no supera el
2,7% del nivel de las normas.

El punto de máximo impacto (PMI) se presenta dentro de las instalaciones del PVSA, a
excepción del SO 2 cuyas mayores emisiones ocurren en el camino de acceso. Sin embargo,
las concentraciones de emisiones de SO 2, aportadas por el Proyecto son prácticamente
nulas.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br> <br> <br>**44/ 73**|<br>**N° DE PÁGINA**<br> <br> <br>**44/ 73**|

**Tabla 12: Aporte del Proyecto en los Receptores Puntuales y Punto de Máximo Impacto (PMI) - Construcción**

|Tipo|Contaminante|Estadígrafo|Límite|La Greda|Col6|Los Maitenes|Col8|Punto de Máximo Impacto (PMI) (1)|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo**|**Contaminante**|**Estadígrafo**|**Límite**|~~**Aporte Proyecto**~~<br>|~~**Aporte Proyecto**~~<br>|~~**Aporte Proyecto**~~<br>|~~**Aporte Proyecto**~~<br>|~~**Aporte Proyecto**~~<br>|~~**Aporte Proyecto**~~<br>|**UTM**<br>**Este (m)**|**UTM Sur**<br>**(m)**|
|**Tipo**|**Contaminante**|**Estadígrafo**|**(ug/m3)**|**ug/m3**|~~**% de la**~~<br>**norma**|**ug/m3**|~~**% de la**~~<br>**norma**|**ug/m3**|~~**% de la**~~<br>**norma**|~~**% de la**~~<br>**norma**|~~**% de la**~~<br>**norma**|
|**Norma**<br>**Primaria de**<br>**Calidad del**<br><br>|MP10|24 horas, P98|150|4,43|3,0%|0,36|0,2%|35,50|23,7%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>**Calidad del**<br><br>|MP10|Anual|50|0,57|1,1%|0,04|0,1%|5,92|11,8%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>**Calidad del**<br><br>|**Aire**<br>MP2.5|24 horas, P98|50|4,22|8,4%|0,34|0,7%|35,44|70,9%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>**Calidad del**<br><br>|**Aire**<br>MP2.5|Anual|20|0,53|2,7%|0,03|0,2%|5,90|29,5%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>**Calidad del**<br><br>|SO2|24 horas, P99|250|0,00|0,0%|0,00|0,0%|0,00|0,0%|272.503|6.375.224|
|**Norma**<br>**Primaria de**<br>**Calidad del**<br><br>|SO2|Anual|80|0,00|0,0%|0,00|0,0%|0,00|0,0%|269.503|6.375.239|
|**Norma**<br>**Secundaria**|SO2|Anual|80|0,00|0,0%|0,00|0,0%|0,00|0,0%|269.503|6.375.239|
|**Norma**<br>**Secundaria**|SO2|24 horas, P99,7|365|0,00|0,0%|0,00|0,0%|0,00|0,0%|269.503|6.375.239|
|**Norma**<br>**Secundaria**|SO2|1 hora, P99,73|1.000|0,01|0,0%|0,00|0,0%|0,03|0,0%|269.503|6.373.238|

Nota 1: Punto de máximo impacto ocurre dentro de las instalaciones del Proyecto.
Fuente Elaboración propia a partir de resultados de la modelación

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**45/73**<br>|<br>**N° DE PÁGINA**<br>**45/73**<br>|

A continuación se muestran las figuras con isolíneas de concentración.

Respecto a MP10 y MP2.5, según se observa en las Figura 5 a Figura 8, la concentración se
reduce rápidamente a medida que las emisiones se alejan del centro del Proyecto, alcanzando
en todos los receptores considerados concentraciones relativamente bajas, en especial en la
Estación Maitenes donde la concentración es prácticamente nula en todos los contaminantes
analizados. El punto de mayor concentración en todos los casos se ubica dentro de las
instalaciones de PVSA.

Según se observa en las Figuras 9 a Figura 12, también las concentraciones de SO 2 se reducen
rápidamente a medida que las emisiones se alejan del centro del Proyecto, alcanzándose en
todos los receptores considerados concentraciones relativamente bajas. Las mayores emisones
de SO 2 ocurren en el camino de acceso, sin embargo, las concentraciones de emisiones de SO 2
son prácticamente nulas.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**46/73**<br>|<br>**N° DE PÁGINA**<br>**46/73**<br>|

**Figura 5. Curva de Iso-concentración, MP10, 24 horas, P98 (Construcción).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**47/73**<br>|<br>**N° DE PÁGINA**<br>**47/73**<br>|

**Figura 6. Curva de Iso-concentración, MP10, anual (Construcción).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**48/73**<br>|<br>**N° DE PÁGINA**<br>**48/73**<br>|

**Figura 7. Curva de Iso-concentración, MP2.5, 24 horas, P98 (Construcción).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**49/73**<br>|<br>**N° DE PÁGINA**<br>**49/73**<br>|

**Figura 8. Curva de Iso-concentración, MP2.5, anual (Construcción).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**50/73**<br>|<br>**N° DE PÁGINA**<br>**50/73**<br>|

**Figura 9. Curva de Iso-concentración, SO2, 24 horas, P99 (Construcción).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**51/73**<br>|<br>**N° DE PÁGINA**<br>**51/73**<br>|

**Figura 10. Curva de Iso-concentración, SO2, anual (Construcción).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**52/73**<br>|<br>**N° DE PÁGINA**<br>**52/73**<br>|

**Figura 11. Curva de Iso-concentración, SO2, 24 horas P99,7 - Norma Secundaria**

**(Construcción).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**53/73**<br>|<br>**N° DE PÁGINA**<br>**53/73**<br>|

**Figura 12. Curva de Iso-concentración, SO2, 1 hora P99,73 - Norma Secundaria (Construcción).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**54/73**<br>|<br>**N° DE PÁGINA**<br>**54/73**<br>|

**8.1.2** **Etapa de Operación**

En la Tabla 13 y las figuras siguientes de iso-líneas de concentración se muestran los aportes
modelados del Proyecto, en la etapa de operación, en los receptores puntuales considerados y
en el punto de máximo impacto (PMI).

En la Tabla 13 se observa, que los aportes del Proyecto en los receptores puntuales son de muy
baja magnitud, pudiéndose considerar la mayoría prácticamente como aportes nulos.

Respecto a MP10 y MP2.5 los aportes en la Estación La Greda no superan el 0,9% del valor de
la norma, mientras que en la Estación Los Maitenes, no supera el 0,1%. En aquellos estadígrafos
que evalúan concentraciones de largo plazo (anuales), el aporte no supera el 0,3 % del nivel de
las normas. Considerando, la baja magnitud de los aportes, el efecto del Proyecto en la calidad
del aire puede ser considerado prácticamente nulo.

El punto de máximo impacto (PMI) se presenta dentro de las instalaciones del PVSA, a excepción
del SO2 cuyas mayores emisiones ocurren en el camino de acceso. Sin embargo, las
concentraciones de emisiones de SO2, son prácticamente nulas.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br>|<br>**N° DE PÁGINA**<br>**55/73**<br>|<br>**N° DE PÁGINA**<br>**55/73**<br>|

**Tabla 13: Aporte del Proyecto en los Receptores Puntuales y Punto de Máximo Impacto (PMI) - Operación**

|Tipo|Contaminante|Estadígrafo|Límite|La Greda|Col6|Los Maitenes|Col8|Punto de Máximo Impacto (PMI)|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo**|**Contaminante**|**Estadígrafo**|**Límite**|~~**Aporte Proyecto**~~|~~**Aporte Proyecto**~~|~~**Aporte Proyecto**~~|~~**Aporte Proyecto**~~|~~**Aporte Proyecto**~~|~~**Aporte Proyecto**~~|~~**UTM**~~<br>**Este**<br>**(m)**|**UTM Sur**<br>**(m)**|
|**Tipo**|**Contaminante**|**Estadígrafo**|**(ug/m3)**|**ug/m3**|**% de la norma**|**ug/m3**|**% de la norma**|**ug/m3**|**% de la norma**|**% de la norma**|**% de la norma**|
|**Norma**<br>**Primaria de**<br>|**d l**<br>MP10|24 horas, P98|150|0,46|0,3%|0,04|0,0%|3,85|2,6%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>|**d l**<br>MP10|Anual|50|0,06|0,1%|0,00|0,0%|0,64|1,3%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>|**id d **<br>MP2.5|24 horas, P98|50|0,46|0,9%|0,04|0,1%|3,85|7,7%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>|**id d **<br>MP2.5|Anual|20|0,06|0,3%|0,00|0,0%|0,64|3,2%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>|**C l**<br>SO2|24 horas, P99|250|0,00|0,0%|0,00|0,0%|0,00|0,0%|267.502|6.373.238|
|**Norma**<br>**Primaria de**<br>|**C l**<br>SO2|Anual|80|0,00|0,0%|0,00|0,0%|0,00|0,0%|267.502|6.373.238|
|**Norma**<br>**Secundaria**|SO2|Anual|80|0,00|0,0%|0,00|0,0%|0,00|0,0%|267.502|6.373.238|
|**Norma**<br>**Secundaria**|SO2|24 horas, P99,7|365|0,00|0,0%|0,00|0,0%|0,00|0,0%|267.502|6.373.238|
|**Norma**<br>**Secundaria**|SO2|1 hora, P99,73|1.000|0,00|0,0%|0,00|0,0%|0,00|0,0%|267.502|6.373.238|

Nota 1: Punto de máximo impacto ocurre dentro de las instalaciones del Proyecto.
Fuente: Elaboración propia a partir de resultados de la modelación.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**56/73**<br>|<br>**N° DE PÁGINA**<br>**56/73**<br>|

A continuación se muestran las figuras con isolíneas de concentración.

Respecto a MP10 y MP2.5, según se observa en las Figura 13 a Figura 16, la concentración
se reduce rápidamente a medida que las emisiones se alejan del centro del Proyecto,
alcanzando en todos los receptores considerados concentraciones relativamente bajas, en
especial en la Estación Maitenes donde la concentración es prácticamente nula en todos los
contaminantes analizados. El punto de mayor concentración en todos los casos se ubica
dentro de las instalaciones de PVSA.

Debido a que el efecto en las concentraciones de SO 2 es nulo, no se muestran isolíneas
para dicho contaminante.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**57/73**<br>|<br>**N° DE PÁGINA**<br>**57/73**<br>|

**Figura 13. Curva de Iso-concentración, MP10, 24 horas, P98 (Operación).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**58/73**<br>|<br>**N° DE PÁGINA**<br>**58/73**<br>|

**Figura 14. Curva de Iso-concentración, MP10, anual (Operación).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**59/73**<br>|<br>**N° DE PÁGINA**<br>**59/73**<br>|

**Figura 15. Curva de Iso-concentración, MP2.5, 24 horas, P98 (Operación).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**60/73**<br>|<br>**N° DE PÁGINA**<br>**60/73**<br>|

**Figura 16. Curva de Iso-concentración, MP2.5, anual (Operación).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**61/73**<br>|<br>**N° DE PÁGINA**<br>**61/73**<br>|

8.2 ANÁLISIS DE INCERTIDUMBRE Y CONCENTRACIONES MODELADAS CON
CALPUFF.

**8.2.1** **Análisis de datos meteorológicos modelados con WRF v/s datos**
**observacionales.**

A continuación se presenta un análisis comparativo de la representatividad del campo de
viento modelado con WRF, respecto de los datos observacionales de la Estación Principal.

En la Figura 17 y Figura 18 de intensidades del viento observada y modelada, se aprecia
que existe un muy buen ajuste entre las velocidades modeladas y las observadas. El viento
medio en ambos casos presenta las mayores intensidades al medio día, entre las 14:00 y
15:00, y menores intensidades en el período nocturno y en la madrugada, entre las 21:00 y
8:00.

Respecto a la intensidad media del viento, el modelo se ajusta muy bien a lo observado,
presentando solo una ligera sobrestimación, que no supera los 0,8 m/s, cuando lo observado
se presenta en torno a 3,8 m/s, el modelo estima 4,6 m/s. El modelo también presenta un
poco más de variabilidad en las intensidades.

**Figura 17. Ciclo Diario de Magnitud del Viento, Est. Principal, año 2013 (observado).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**62/73**<br>|<br>**N° DE PÁGINA**<br>**62/73**<br>|

**Figura 9. Ciclo Diario de Magnitud del Viento Est. Principal, año 2013 (simulado).**

La Figura 19 y Figura 20 muestran el porcentaje de ocurrencia de la dirección del viento,
observándose que el modelo logra representar de buena manera el viento suroeste
predominante durante la tarde, no obstante le resta predominancia al viento este,
predominante durante la noche y madrugada. Mientras el observado, durante la madrugada
y noche, muestra principalmente dirección este, el modelo estima dirección suroeste.

No obstante, considerando que el Proyecto se encuentra al suroeste de la estación La
Greda, que es el receptor puntual más cercano, el hecho de que el viento modelado
considere mayor frecuencia de vientos suroeste, tiene como efecto sobreestimar el aporte
de las emisiones, durante la modelación con Calpuff, en dicho receptor.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**63/73**<br>|<br>**N° DE PÁGINA**<br>**63/73**<br>|

**Figura 19. Ciclo Diario de Dirección del Viento, Porcentaje de Ocurrencia (%), Est.**

**Principal, año 2013 (observado).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**64/73**<br>|<br>**N° DE PÁGINA**<br>**64/73**<br>|

**Figura 20. Ciclo Diario de Dirección del Viento, Porcentaje de Ocurrencia (%), Est.**

**Principal, año 2013 (simulado).**

En la Figura 21 y Figura 22 se observa el ciclo diurno del viento representado en rosas del
viento. Se puede observar que en los datos observados, las direcciones predominantes son
este, durante la madrugada principalmente, y oeste durante gran parte del día.

El modelo estima que la dirección predominante durante la jornada es suroeste y en segunda
medida noreste.

Este hecho tiene como efecto que durante la modelación con Calpuff se considere un
período más largo en que el viento moviliza emisiones desde el Proyecto a la Estación La
Greda, sobreestimándose por lo tanto los aportes del Proyecto en la Estación la Greda.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**65/73**<br>|<br>**N° DE PÁGINA**<br>**65/73**<br>|

**Figura 21. Rosas de Viento año 2013, Est. Principal (observado).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**66/73**<br>|<br>**N° DE PÁGINA**<br>**66/73**<br>|

**Figura 22. Rosas de Viento año 2013, Est. Principal (simulado).**

En la Figura 23 y Figura 24 se muestra el ciclo estacional del viento observado y simulado
respectivamente para el año 2013. Se observa que el modelo logra representar de buena
forme el ciclo estacional. Los centros de mayor intensidad son representados de buena
manera, ocurriendo entre las 12:00 y 18:00.

El modelo tiende a sobreestimar en alguna medida los vientos máximos, en época invernal
y principalmente en horario nocturno y de madrugada. Sin embargo en dicho comento el
viento preferente es del este, por lo que las emisiones son transportadas en dirección
opuesta al receptor más cercano, representado por la Estación La Greda, por lo que el efecto
de esta imprecisión no se traduce en un efecto relevante durante la modelación con Calpuff.

Asimismo, como ya se ha indicado, se observa que el viento modelado tiene una mayor
componente suroeste, lo que tendería a sobreestimar el impacto del Proyecto en la Estación
La Greda.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**67/73**<br>|<br>**N° DE PÁGINA**<br>**67/73**<br>|

**Figura 23. Ciclo Estacional del Viento, Est. Principal, año 2013 (observado).**

**Figura 24. Ciclo Estacional del Viento, Est. Principal, año 2013 (simulado).**

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**68/73**<br>|<br>**N° DE PÁGINA**<br>**68/73**<br>|

**8.2.2** **Análisis de Incertidumbre y Determinación de Factores de Corrección de**
**Concentraciones Modeladas**

Para determinar el grado de incertidumbre asociado a la modelación meteorológica, se
realizará un análisis comparativo de los datos simulados y los observados de magnitud del
viento en la estación Principal. Esto debido a que la magnitud del viento es la variable de
mayor efecto en los procesos de dispersión.

La variación entre la meteorología observada y simulada se obtendrá restando el promedio
de la intensidad del viento simulada con el promedio de la intensidad del viento observada
en la estación.

Finalmente se determinará, según juicio experto, si es necesario estimar un factor de
corrección de las concentraciones modeladas con CALPUFF, a partir de la diferencia en la
intensidad del viento, en la dirección asociada al transporte de los contaminantes desde la
fuente a los receptores puntuales evaluados.

En la Tabla 14 se expone el análisis comparativo de intensidad del viento observada y
modelada. Considerando las diferencias observadas en el comportamiento diurno y
nocturno, se ha realizado el análisis para estos dos períodos, estando el periodo diurno
comprendido entre las 10:00 y 21:00 horas y el nocturno, entre las 22:00 y 09:00 horas

Las variaciones porcentuales negativas indican intensidad del viento simulada por el modelo
WRF menor a la observada (subestimación), mientras que las positivas indican
sobrestimación.

En la Tabla 14 se puede apreciar que las diferencias se mantienen dentro de los rangos
aceptables, el modelo tiende a sobreestimar, solo ligeramente, la intensidad del viento,
principalmente durante la noche, que es el periodo en el que la intensidad del viento
disminuye. Sin embargo, en dicho momento la dirección del viento es este, siendo las
emisiones del Proyecto movilizadas en dirección contraria a los receptores.

Durante el día, el modelo también tiende a sobrestimar la intensidad del viento, aunque en
menor medida.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**69/73**<br>|<br>**N° DE PÁGINA**<br>**69/73**<br>|

**Tabla 14: Diferencia entre Intensidad del Viento Observada y Modelada en Estación INIA**

|Estación|Observado<br>(m/s)|Modelado (WRF)<br>(m/s)|Diferencia<br>Mod-Obs<br>(m/s)|Variación<br>Porcentual<br>%|
|---|---|---|---|---|
|Principal|2,30|2,87|0,57|24,78|
|Principal diurno|3,43|3,61|0,18|5,25|
|Principal nocturno|1,62|2,13|0,51|31,48|

Fuente: Elaboración propia

A continuación se analiza la diferencia del viento modelado respecto al observado, en
función de su dirección, para lo cual se ha dividido la rosa de los vientos en cuadrantes,
analizándose tanto el periodo diurno como el nocturno.

En la Tabla 15 que observan los resultados obtenidos para la estación Principal. Es
importante señalar que las direcciones más relevantes para el caso en análisis son las
direcciones con componente oeste (180°-270° y 270° - 360°) debido a que es la dirección
en que el viento moviliza los contaminantes desde el Proyecto hacia el continente, y en
particular hacia la Estación La Greda, mientras que las otras direcciones movilizan los
contaminantes en dirección contraria a los receptores.

Se observa que el modelo presenta, en general, una buena predicción de las intensidades
del viento en las direcciones con componente oeste, con una diferencia en la velocidad
menor a 1 m/s. Como es habitual la mayor diferencia se presenta en horario nocturno, debido
a que las bajas intensidades del viento, hacen más difícil predecir su intensidad por el
modelo.

**Tabla 15: Diferencia entre Intensidad del Viento Observada y Modelada en Estación INIA**

|Dirección<br>viento<br>(grados)|Diurno|Col3|Col4|Col5|Nocturno|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**<br>**viento**<br>**(grados)**|Obs<br>(m/s)|WRF<br>(m/s)|Dif<br>(m/s)|Variación<br>%|Obs<br>(m/s)|WRF<br>(m/s)|Dif<br>(m/s)|Variación<br>%|
|0-90|2,33|2,76|0,43|18,45|2,03|2,05|0,02|0,98|
|90-180|1,37|2,26|0,89|64,69|1,52|2,09|0,57|37,50|
|**180-270**|**3,31**|**4,05**|**0,74**|**22,36**|**1,33**|**2,28**|**0,95**|**71,43**|
|**270-360**|**3,04**|**2,94**|**-0,10**|**-3,29**|**1,90**|**2,00**|**0,10**|**5,27**|

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**70/73**<br>|<br>**N° DE PÁGINA**<br>**70/73**<br>|

Nota 1: En negrilla, direcciones del viento en que se produce movilización de contaminantes del Proyecto

hacia los receptores.
Fuente: Elaboración propia a partir de datos de modelo WRF.

Considerando lo antes expuesto, y que el modelo WRF predice una mayor frecuencia de
vientos de componente oeste, lo que sobrestima el impacto predicho por el modelo Calpuff.
No se ha considerado necesario corregir las concentraciones modeladas.

8.3 EVALUACIÓN DE CUMPLIMIENTO DE NORMATIVA

A continuación se realiza una evaluación de cumplimiento de normativa de calidad del aire,
para lo cual se ha considerado la línea base monitoreada y los aportes modelados del
Proyecto.

Es importante aclarar, que la modelación se realizó con la información meteorológica más
actualizada, correspondiente al año 2013. Sin embargo, para efectos de línea base, se
consideraron los datos contenidos en el “Informe de Calidad del Aire de la Región de
Valparaíso, Período 2010 -2012”, de la SEREMI de Salud, Región de Valparaíso, debido a
que representan la información oficial más actualizada de evaluación de la calidad del aire
en la región.

**8.3.1** **Etapa de Construcción**

En la Tabla 16 y Tabla 17 se muestra la línea base monitoreada, las concentraciones
modeladas por Calpuff y la concentración final alcanzada en el área de influencia del
Proyecto en la etapa de construcción, se observa cumplimiento de todas las normas
evaluadas. Es importante señalar que la etapa de construcción será acotada en el tiempo,
durando 10 meses.

Respecto a MP10 y MP2.5, se observa cumplimiento de todas las normas de calidad del
aire, con bajos aportes del Proyecto en las Estaciones La Greda y Los Maitenes, con niveles
que no superan el 8,4% de los límites establecidos en la norma de calidad del aire.

Respecto a MP10, el aporte del Proyecto en la concentración anual, no supera los 0,57
ug/m3 en las estaciones La Greda y los 0,04 ug/m3 en Los Maitenes, mientras que en la
concentración de 24 horas, no supera los 4,43 ug/m3 y 0,36 ug/m3, respectivamente, siendo
estos aportes relativamente bajos, dado que se predice que la calidad del aire seguirá
estando bajo el nivel establecido en las normas de calidad del aire.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**71/73**<br>|<br>**N° DE PÁGINA**<br>**71/73**<br>|

Respecto a MP2.5, el aporte del Proyecto en la concentración anual, no supera los 0,53
ug/m3 en las estaciones La Greda y los 0,03 ug/m3 en Los Maitenes, mientras que en la
concentración de 24 horas, no supera los 4,22 ug/m3 y 0,34 ug/m3, respectivamente, siendo
estos aportes relativamente bajos, dado que se predice que la calidad del aire seguirá
estando bajo el nivel establecido en las normas de calidad del aire.

Respecto a SO 2, también se observa cumplimiento de todas las normas de calidad del aire,
pudiéndose considerar el aporte del Proyecto en las estaciones La Greda y Los Maitenes,
como nulo. Lo que es de esperar dado el bajo contenido de azufre del combustible diesel
disponible en Chile (menos de 50 ppm).

**Tabla 16: Cumplimiento de Normativa en Estación La Greda - Construcción**

|Tipo|Contaminante|Estadígrafo|Límite|La Greda|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo**<br>|**Contaminante**|**Estadígrafo**|**Límite**|**Línea Base**|**Línea Base**|~~**Aporte**~~<br>**Proyecto**|~~**Aporte**~~<br>**Proyecto**|**Línea Base+ Aporte**|**Línea Base+ Aporte**|**Línea Base+ Aporte**|
|**Tipo**<br>|**Contaminante**|**Estadígrafo**|**ug/m3 **|**ug/m3 **|**% de**<br>**la**<br>**norma**|**ug/m3 **|**% de**<br>**la**<br>**norma**|**ug/m3 **|**% de**<br>**la**<br>**norma**|**Cumplimiento**|
|**Norma Primaria de**<br>**Calidad del Aire **|MP10|24 horas, P98|150|77|51,3%|4,43|3,0%|81|54,3%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **|MP10|Anual|50|44|88,0%|0,57|1,1%|45|89,1%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **|MP2.5|24 horas, P98|50|36|72,0%|4,22|8,4%|40|80,4%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **|MP2.5|Anual|20|17|85,0%|0,53|2,7%|18|87,7%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **|SO2|24 horas, P99|250|64|25,6%|0,00|0,0%|64|25,6%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **|SO2|Anual|80|11|13,8%|0,00|0,0%|11|13,8%|Cumple|
|**Norma**<br>**Secundaria**|SO2|Anual|80|14|17,5%|0,00|0,0%|14|17,5%|Cumple|
|**Norma**<br>**Secundaria**|SO2|24 horas, P99,7|365|110|30,0%|0,00|0,0%|110|30,0%|Cumple|
|**Norma**<br>**Secundaria**|SO2|1 hora, P99,73|1.000|286|28,6%|0,01|0,0%|286|28,6%|Cumple|

(1): Línea base corresponde a período 2010-2012.
(2): Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012
n/a: No aplica debido a que no hay monitoreo de línea base para esta variable
Fuente: Elaboración propia en base de resultados de modelación e “Informe de Calidad del Aire de la Región de Valparaíso, período
2010-2012”, Seremi de Salud Región de Valparaíso.

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**72/73**<br>|<br>**N° DE PÁGINA**<br>**72/73**<br>|

**Tabla 17: Cumplimiento de Normativa en Estación Los Maitenes - Construcción**

|Tip<br>o|Contaminante|Estadígrafo|Límite|Los Maitenes|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Tip**<br>**o **<br>|**Contaminante**|**Estadígrafo**|**Límite**|**Línea Base**<br>|**Línea Base**<br>|~~**Aporte**~~<br>**Proyecto**|~~**Aporte**~~<br>**Proyecto**|**Línea base+ Aporte**|**Línea base+ Aporte**|**Línea base+ Aporte**|
|**Tip**<br>**o **<br>|**Contaminante**|**Estadígrafo**|**ug/m3 **|**ug/m3 **|~~**% de**~~<br>**la**<br>**norma**|**ug/m3 **|**% de la**<br>**norma**|**ug/m3 **|**% de la**<br>**norma**|**Cumplimient**<br>**o **|
|**Norma Primaria de**<br>**Calidad del Aire **<br>|MP10|24 horas, P98|150|56|37,3%|0,36|0,2%|56,36|37,6%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **<br>|MP10|Anual|50|32|64,0%|0,04|0,1%|32,04|64,1%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **<br>|MP2.5|24 horas, P98|50|32|64,0%|0,34|0,7%|32,34|64,7%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **<br>|MP2.5|Anual|20|14|70,0%|0,03|0,2%|14,03|70,2%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **<br>|SO2|24 horas, P99|250|132|52,8%|0,00|0,0%|132|52,8%|Cumple|
|**Norma Primaria de**<br>**Calidad del Aire **<br>|SO2|Anual|80|35|43,8%|0,00|0,0%|35|43,8%|Cumple|
|**Norma**<br>**Secundaria (2) **|SO2|Anual|80|33|41,3%|0,00|0,0%|33|41,3%|Cumple|
|**Norma**<br>**Secundaria (2) **|SO2|24 horas,<br>P99,7|365|158|43,3%|0,00|0,0%|158|43,3%|Cumple|
|**Norma**<br>**Secundaria (2) **|SO2|1 hora,<br>P99,73|1.000|542|54,2%|0,00|0,0%|541,5|54,2%|Cumple|

(1): Línea base corresponde a período 2010-2012.
(2): Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012
n/a: No aplica debido a que no hay monitoreo de línea base para esta variable
Fuente: Elaboración propia en base de resultados de modelación e “Informe de Calidad del Aire de la Región de Valparaíso,
período 2010-2012”, Seremi de Salud Región de Valparaíso.

**8.3.2** **Etapa de Operación**

En la Tabla 18 y Tabla 19 se muestra la línea base monitoreada, las concentraciones
modeladas por Calpuff y la concentración final alcanzada en el área de influencia del
Proyecto en la etapa de operación, se observa cumplimiento de todas las normas evaluadas.

Respecto a MP10 y MP2.5, se observa cumplimiento de todas las normas de calidad del
aire, con muy bajos aportes del Proyecto en las Estaciones La Greda y Los Maitenes, donde
se observan niveles que no superan el 0,9% de los límites establecidos en la norma de
calidad del aire.

Respecto a MP10, el aporte del Proyecto en la concentración anual, no supera los 0,06
ug/m3 en las estaciones La Greda, siendo nulo (0,00 ug/m3) en Los Maitenes, mientras que
en la concentración de 24 horas, no supera los 0,46 ug/m3 y 0,04 ug/m3, respectivamente,
siendo por lo tanto los aportes del Proyecto en la etpa de operación, prácticamente nulos.

Respecto a MP2.5, el aporte en las estaciones La Greda y Los Maitenes es el mismo que el
de MP10

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**73/73**<br>|<br>**N° DE PÁGINA**<br>**73/73**<br>|

Respecto a SO 2, también se observa cumplimiento de todas las normas de calidad del aire,
pudiéndose considerar el aporte del Proyecto en las estaciones La Greda y Los Maitenes,
como nulo. Lo que es de esperar dado el bajo contenido de azufre del combustible diesel
disponible en Chile (menos de 50 ppm).

**Tabla 18: Cumplimiento de Normativa en Estación La Greda - Operación**

|Tipo|Contaminant<br>e|Estadígrafo|Límite|La Greda|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo**|**Contaminant**<br>**e **|**Estadígrafo**|**Límite**|**Línea Base**|**Línea Base**|~~**Aporte**~~<br>**Proyecto**|~~**Aporte**~~<br>**Proyecto**|**Línea base+ Aporte**<br>|**Línea base+ Aporte**<br>|**Línea base+ Aporte**<br>|
|**Tipo**|**Contaminant**<br>**e **|**Estadígrafo**|**ug/m3 **|**ug/m3 **|**% de la**<br>**norma**|**ug/m3 **|**% de la**<br>**norma**|**ug/m3 **|~~**% de**~~<br>**la**<br>**norma**|**Cumplimiento**|
|**Norma Primaria de Calidad**<br>**del Aire (1)**<br>|MP10|24 horas,<br>P98|150|77|51,3%|0,46|0,3%|77|51,6%|Cumple|
|**Norma Primaria de Calidad**<br>**del Aire (1)**<br>|MP10|Anual|50|44|88,0%|0,06|0,1%|44|88,1%|Cumple|
|**Norma Primaria de Calidad**<br>**del Aire (1)**<br>|MP2.5|24 horas,<br>P98|50|36|72,0%|0,46|0,9%|36|72,9%|Cumple|
|**Norma Primaria de Calidad**<br>**del Aire (1)**<br>|MP2.5|Anual|20|17|85,0%|0,06|0,3%|17|85,3%|Cumple|
|**Norma Primaria de Calidad**<br>**del Aire (1)**<br>|SO2|24 horas,<br>P99|250|64|25,6%|0,00|0,0%|64|25,6%|Cumple|
|**Norma Primaria de Calidad**<br>**del Aire (1)**<br>|SO2|Anual|80|11|13,8%|0,00|0,0%|11|13,8%|Cumple|
|**Norma**<br>**Secundaria (2)**|SO2|Anual|80|14|17,5%|0,00|0,0%|14|17,5%|Cumple|
|**Norma**<br>**Secundaria (2)**|SO2|24 horas,<br>P99,7|365|110|30,0%|0,00|0,0%|110|30,0%|Cumple|
|**Norma**<br>**Secundaria (2)**|SO2|1 hora,<br>P99,73|1.000|286|28,6%|0,00|0,0%|286|28,6%|Cumple|

(1): Línea base corresponde a período 2010-2012.
(2): Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012
n/a: No aplica debido a que no hay monitoreo de línea base para esta variable
Fuente: Elaboración propia en base de resultados de modelación e “Informe de Calidad del Aire de la Región de Valparaíso,
período 2010-2012”, Seremi de Salud Región de Valparaíso

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**74/73**<br>|<br>**N° DE PÁGINA**<br>**74/73**<br>|

**Tabla 19: Cumplimiento de Normativa en Estación Los Maitenes - Operación**

|Ti<br>po|Contaminante|Estadígrafo|Límite|Los Maitenes|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Ti**<br>**po**|**Contaminante**|**Estadígrafo**|**Límite**|**Línea Base**|**Línea Base**|~~**Aporte**~~<br>**Proyecto**|~~**Aporte**~~<br>**Proyecto**|**Línea base+ Aporte**|**Línea base+ Aporte**|**Línea base+ Aporte**|
|**Ti**<br>**po**|**Contaminante**|**Estadígrafo**|**ug/m3 **|**ug/m3 **|**% de la**<br>**norma**|**ug/**<br>**m3 **|**% de la**<br>**norma**|**ug/m3 **|**% de la**<br>**norma**|**Cumplimiento**|
|**Norma Primaria de Calidad**<br>**delAire (1)**|MP10|24 horas,<br>P98|150|56|37,3%|0,04|0,0%|56,04|37,4%|Cumple|
|**Norma Primaria de Calidad**<br>**delAire (1)**|MP10|Anual|50|32|64,0%|0,00|0,0%|32|64,0%|Cumple|
|**Norma Primaria de Calidad**<br>**delAire (1)**|MP2.5|24 horas,<br>P98|50|32|64,0%|0,04|0,1%|32,04|64,1%|Cumple|
|**Norma Primaria de Calidad**<br>**delAire (1)**|MP2.5|Anual|20|14|70,0%|0,00|0,0%|14|70,0%|Cumple|
|**Norma Primaria de Calidad**<br>**delAire (1)**|SO2|24 horas,<br>P99|250|132|52,8%|0,00|0,0%|132|52,8%|Cumple|
|**Norma Primaria de Calidad**<br>**delAire (1)**|SO2|Anual|80|35|43,8%|0,00|0,0%|35|43,8%|Cumple|
|**Norma**<br>**Secundaria (2)**|SO2|Anual|80|33|41,3%|0,00|0,0%|33|41,3%|Cumple|
|**Norma**<br>**Secundaria (2)**|SO2|24 horas,<br>P99,7|365|158|43,3%|0,00|0,0%|158|43,3%|Cumple|
|**Norma**<br>**Secundaria (2)**|SO2|1 hora,<br>P99,73|1.000|542|54,2%|0,00|0,0%|541,5|54,2%|Cumple|

(1): Línea base corresponde a período 2010-2012.
(2): Por falta de antecedentes la línea base de la norma secundaria corresponde a promedio año 2011 y 2012
n/a: No aplica debido a que no hay monitoreo de línea base para esta variable
Fuente: Elaboración propia en base de resultados de modelación e “Informe de Calidad del Aire de la Región de Valparaíso,
período 2010-2012”, Seremi de Salud Región de Valparaíso

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**75/73**<br>|<br>**N° DE PÁGINA**<br>**75/73**<br>|

**9.0** **CONCLUSIONES**

- Se realizó una modelación de los aportes de las emisiones del Proyecto, en su etapa de
construcción y operación utilizando el modelo Calpuff.

- La modelación arroja que el efecto del Proyecto sobre la calidad del aire será muy localizado,
estando el punto de máximo impacto dentro de las instalaciones de PVSA, lo que es de
esperar considerando que las mayores emisiones están asociadas a las tareas de excavación
o movimiento de concentrado dentro de la bodega.

- La evaluación del cumplimiento de normativa concluye que se cumplirá con las normas de
calidad del aire.

- Los resultados de la modelación arrojan que los aportes del Proyecto respecto a MP10 y
MP2.5, en los receptores evaluados Estación La Greda y Estación Los Maitenes, se pueden
considerar relativamente bajos en la etapa de construcción y prácticamente nulos en la etapa
de operación.

- El efecto del Proyecto en la etapa de construcción será mayor que en la etapa de operación.
Sin embargo, en la etapa de construcción las emisiones se generarán en un tiempo acotado,
de tan solo 10 meses.

- Respecto a MP10 en la etapa de construcción, el aporte del Proyecto en la concentración
anual, no supera los 0,57 ug/m3 en las estaciones La Greda y los 0,04 ug/m3 en Los
Maitenes, mientras que en la concentración de 24 horas, no supera los 4,43 ug/m3 y 0,36
ug/m3, respectivamente, siendo estos aportes relativamente bajos, dado que se predice que
la calidad del aire seguirá estando bajo el nivel establecido en las normas de calidad del aire.

- Respecto a MP2.5 en la etapa de construcción, el aporte del Proyecto en la concentración
anual, no supera los 0,53 ug/m3 en las estaciones La Greda y los 0,03 ug/m3 en Los
Maitenes, mientras que en la concentración de 24 horas, no supera los 4,22 ug/m3 y 0,34
ug/m3, respectivamente, siendo estos aportes relativamente bajos, dado que se predice que
también que la calidad del aire seguirá estando bajo el nivel establecido en las normas de
calidad del aire.

- Respecto a SO 2, en la etapa de construcción también se observa cumplimiento de todas las
normas de calidad del aire, pudiéndose considerar el aporte del Proyecto en las estaciones

|Elaborado por:|MODELACIÓN DE DISPERSIÓN DE<br>CONTAMINANTES|Preparado para:|
|---|---|---|
|<br>**Elaborado por:**<br> <br>|<br>**N° DE PÁGINA**<br>**76/73**<br>|<br>**N° DE PÁGINA**<br>**76/73**<br>|

La Greda y Los Maitenes, como nulo. Lo que es de esperar dado el bajo contenido de
azufre del combustible diesel disponible en Chile (menos de 50 ppm).

- Respecto a MP10 y MP2.5 en la etapa de operación, se observa cumplimiento de todas las
normas de calidad del aire, con muy bajos aportes del Proyecto en las Estaciones La Greda
y Los Maitenes, donde se observan niveles que no superan el 0,9% de los límites establecidos
en la norma de calidad del aire.

- Respecto a MP10, el aporte del Proyecto en la concentración anual, no supera los 0,06 ug/m3
en las estaciones La Greda, siendo nulo (0,00 ug/m3) en Los Maitenes, mientras que en la
concentración de 24 horas, no supera los 0,46 ug/m3 y 0,04 ug/m3, respectivamente, siendo
por lo tanto los aportes del Proyecto en la etapa de operación, prácticamente nulos. Respecto
a MP2.5, el aportes en las estaciones La Greda y Los Maitenes es el mismo que el de MP10.

- Respecto a SO 2, en la etapa de operación también se observa cumplimiento de todas las
normas de calidad del aire, pudiéndose considerar el aporte del Proyecto en las estaciones
La Greda y Los Maitenes, como nulo. Lo que es de esperar dado el bajo contenido de azufre
del combustible diesel disponible en Chile (menos de 50 ppm).

- Por lo antes indicado, es posible concluir a partir de los bajos aportes del Proyecto a la calidad
del aire en su área de influencia, que éste no producirá un efecto significativo en la calidad
del aire.