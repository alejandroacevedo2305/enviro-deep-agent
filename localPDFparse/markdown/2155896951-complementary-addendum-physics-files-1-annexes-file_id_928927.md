---
title: Tipo de Informe o Capítulo
author: Kisi Cerda
date: D:20230327113743-03'00'
language: es
type: report
pages: 35
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 3.2.1. MODELACIÓN DE CALIDAD DEL AIRE DECLARACIÓN DE IMPACTO AMBIENTAL DEL PROYECTO “PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II” ADENDA COMPLEMENTARIA
-->

# ANEXO 3.2.1. MODELACIÓN DE CALIDAD DEL AIRE DECLARACIÓN DE IMPACTO AMBIENTAL DEL PROYECTO “PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II” ADENDA COMPLEMENTARIA

**Marzo 2023**

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

## ÍNDICE

**1.** **ANTECEDENTES GENERALES DEL PROYECTO ............................................................................ 4**

**2.** **LÍNEA DE BASE METEOROLÓGICA ................................................................................................. 5**

2.1. Validez de los registros Meteorológicos ........................................................................................ 5

2.2. Velocidad del viento ...................................................................................................................... 5

2.3. Dirección del Viento ....................................................................................................................... 6

**3.** **MODELACIÓN CALIDAD DEL AIRE ................................................................................................... 8**

3.1. Información Geográfica ................................................................................................................. 8

3.2. Descripción del Modelo Meteorológico WRF .............................................................................. 11

3.3. Análisis de Incertidumbre del Modelo Meteorológico WRF ........................................................ 12

3.4. Grilla de receptores ..................................................................................................................... 12

3.5. Receptores Discretos .................................................................................................................. 14

3.6. Fuentes de emisión ..................................................................................................................... 15

**4.** **MARCO LEGAL APLICABLE AL PROYECTO ................................................................................. 18**

**5.** **RESULTADOS DE LA MODELACIÓN .............................................................................................. 18**

5.1. Puntos de máximo Impacto ......................................................................................................... 18

5.2. Receptores Discretos .................................................................................................................. 20

5.3. Curvas de Isoconcentración - Fase de Construcción Año 1 ...................................................... 22

**6.** **ÁREA DE INFLUENCIA ...................................................................................................................... 31**

**7.** **CONCLUSIONES ................................................................................................................................ 34**

**8.** **BIBLIOGRAFÍA ................................................................................................................................... 35**

**9.** **APENDICE ARCHIVOS DE ENTRADA Y SALIDA DEL MODELO .................................................. 35**

**INDICE DE TABLAS**

Tabla 2-1 Coordenadas del punto de extracción de los datos meteorológicos. ........................................... 5

Tabla 2-2 Validez de los datos meteorológicos - Año 2021 ......................................................................... 5

Tabla 2-3 Distribución de frecuencias d la dirección del viento. ................................................................... 7

Tabla 3-1 Parámetros de la proyección cónica del modelo WRF ............................................................... 12

Tabla 3-2 Características del dominio de modelación ................................................................................ 12

Tabla 3-3 Receptores discretos del modelo. ............................................................................................... 14

Tabla 3-4 Emisiones contaminantes atmosféricos - Año 1 Fase de Construcción. ................................... 16

Tabla 3-5 Superficie y emisiones por fuente. .............................................................................................. 16

Tabla 3-6 Emisiones ingresadas al modelo - Año 1 Fase de construcción. .............................................. 16

Tabla 4-1 Normativa primaria de Calidad del Aire aplicable al Proyecto. ................................................... 18

Tabla 5-1 Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1. .................. 19

Tabla 5-2 Coordenadas de los Puntos de Máximo Impacto - Fase de construcción Año 1. ...................... 19

Página | 2

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

Tabla 5-3 Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1 ........................... 21

Tabla 5-4 Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de

construcción Año 1 ....................................................................................................................... 21

Tabla 6-1 Concentración equivalente al 1% de la norma ........................................................................... 31

**ÍNDICE DE FIGURAS**

Figura 1-1 Emplazamiento del Proyecto. ...................................................................................................... 4

Figura 2-1 Serie de tiempo de la velocidad del viento obtenida para el año 2021 ....................................... 6

Figura 2-2 Ciclo diario de la velocidad del viento obtenida para el año 2021 ............................................... 6

Figura 2-3 Serie de tiempo de la dirección del viento obtenida para el año 2021. ....................................... 7

Figura 2-4 Rosa de vientos - Año 2021. ....................................................................................................... 7

Figura 3-1 Representación de información topográfica utilizada por el modelo. .......................................... 9

Figura 3-2 Representación de la información de uso de suelo utilizada por el modelo. ............................ 11

Figura 3-3 Dominio de modelación y grilla de receptores. .......................................................................... 13

Figura 3-4 Distribución de receptores discretos .......................................................................................... 15

Figura 3-5 Representación de las fuentes en el modelo. ............................................................................ 17

Figura 5-1 Ubicación de los Puntos de Máximo Impacto - Fase de construcción. .................................... 20

Figura 5-2 Curvas de Isoconcentración - MP10 24 horas Percentil 98. ..................................................... 23

Figura 5-3 Curvas de Isoconcentración - MP10 Anual. .............................................................................. 24

Figura 5-4 Curvas de Isoconcentración - MP2,5 24 horas Percentil 98. .................................................... 25

Figura 5-5 Curvas de Isoconcentración - MP2,5 Anual. ............................................................................. 26

Figura 5-6 Curvas de Isoconcentración - NO 2 1 hora Percentil 99. ........................................................... 27

Figura 5-7 Curvas de Isoconcentración - NO 2 Anual. ................................................................................ 28

Figura 5-8 Curvas de Isoconcentración - CO 1 hora Percentil 99 ............................................................. 29

Figura 5-9 Curvas de Isoconcentración - CO 8 horas Percentil 99 ............................................................ 30

Figura 6-1 Área de influencia - Concentración MP10 24 horas Percentil 98. ............................................ 31

Figura 6-2 Área de influencia - Concentración MP10 Anual. ..................................................................... 32

Figura 6-3 Área de influencia - Concentración MP2,5 Anual. .................................................................... 32

Figura 6-4 Área de influencia del Proyecto ................................................................................................. 33

Página | 3

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**1.** **ANTECEDENTES GENERALES DEL PROYECTO**

El Proyecto “Parque Fotovoltaico Andino Occidente II” (en adelante el Proyecto), pretende captar
y transformar la energía solar en energía eléctrica, para ser inyectada al Sistema Eléctrico
Nacional. Para ello, se llevará a cabo la construcción y operación de una planta fotovoltaica de
150,31 MWp de potencia instalada conformada por más de 200.000 paneles de 665 Wp de
potencia. El Proyecto considera la construcción y operación de una subestación elevadora y una
línea de transmisión eléctrica de 1x220 kV, de aproximadamente 6,38 km de longitud que
conectará el Proyecto a la ampliación de 220kV que tendrá la subestación eléctrica Portezuelo.

El Proyecto se emplazará en un terreno rural ubicado en la comuna de Marchihue, Región de
O’Higgins, Rol N° 64-121 tal como se muestra en la Figura 1-1.
El presente informe describe la modelación de la dispersión de las emisiones atmosféricas
estimadas para el primer año de la construcción del Proyecto de acuerdo a las exigencias
indicadas en la “Guía para el uso de modelos de calidad del aire en el SEA”.

**Figura 1-1 Emplazamiento del Proyecto.**

Fuente: DIA del Proyecto.

Página | 4

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**2.** **LÍNEA DE BASE METEOROLÓGICA**

Según la información recopilada, y dada la ausencia de registros válidos y que sean
representativos del área en que se emplazará el Proyecto, no es posible establecer una línea de
base meteorológica a partir de mediciones efectuadas en una estación de monitoreo
meteorológico.

Dado estos antecedentes se ha caracterizado la velocidad y la dirección del viento del lugar a
partir de los datos contenidos en el modelo WRF elaborado para el presente estudio. El punto de
extracción de los datos corresponde al centro del parque fotovoltaico del Proyecto y cuyas
coordenadas se presentan en la Tabla 2-1.

<!-- INICIO TABLA 2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Dado estos antecedentes se ha caracterizado la velocidad y la dirección del viento del lugar a partir de los datos contenidos en el modelo WRF elaborado para el presente estudio. El punto de extracción de los datos corresponde al centro del parque fotovoltaico del Proyecto y cuyas coordenadas se presentan en la Tabla 2-1. -->

**Tabla 2-1: Coordenadas del punto de extracción de los datos meteorológicos.****

| Coordenadas UTM | Col2 | Altura sobre el nivel del mar<br>(m) |
| --- | --- | --- |
| **X (m)** | **Y (m)** | **Y (m)** |
| 262.263 | 6.191.042 | 146 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. DATUM WGS84 Huso 19. **2.1.** **VALIDEZ DE LOS REGISTROS METEOROLÓGICOS** -->
<!-- FIN TABLA 2-1 -->


**Tabla 2-1 Coordenadas del punto de extracción de los datos meteorológicos.**

|Coordenadas UTM|Col2|Altura sobre el nivel del mar<br>(m)|
|---|---|---|
|**X (m)**|**Y (m)**|**Y (m)**|
|262.263|6.191.042|146|

Fuente: Elaboración propia. DATUM WGS84 Huso 19.

**2.1.** **VALIDEZ DE LOS REGISTROS METEOROLÓGICOS**

En la Tabla 2-2 se presentan las variables meteorológicas extraídas del modelo y el porcentaje
de valores válidos obtenidos para cada una. Dado que los datos presentan validez del 100%, se
da cumplimiento a lo indicado en la “Guía para el uso de modelos de calidad del aire en el SDIA”
que recomienda que el porcentaje de datos válidos en un año sea superior al 75% (valor asociado
a la validez de la información de monitoreo establecido en las normas primarias de calidad del
aire).

**Tabla 2-2 Validez de los datos meteorológicos - Año 2021**

|Variable|N° Registros Válidos|% Registros Válidos|
|---|---|---|
|Velocidad del Viento|8.760|100%|
|Dirección del Viento|8.760|100%|

Fuente: Elaboración propia.

**2.2.** **VELOCIDAD DEL VIENTO**

La serie de tiempo de la velocidad del viento obtenida en el punto de extracción se presenta en
la Figura 2-1. La velocidad del viento promedio obtenida es de 1,6 m/s. Las velocidades del viento
más bajas se presentan durante el período nocturno (0,8 m/s entre las horas 8 y 9) y comienzan
a aumentar a contar de las 10 de la mañana. En promedio, las velocidades más altas se registran
a las 16 horas (3,7 m/s), tal como puede observarse en la Figura 2-2.

Página | 5

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 2-1 Serie de tiempo de la velocidad del viento obtenida para el año 2021**

Fuente: Elaboración propia

**Figura 2-2 Ciclo diario de la velocidad del viento obtenida para el año 2021**

Fuente: Elaboración propia

**2.3.** **DIRECCIÓN DEL VIENTO**

En la Figura 2-3 se presenta la serie de tiempo de la dirección del viento obtenida en el punto de
extracción, mientras que en la Figura 2-4 se presenta la rosa de viento elaborada con dichos
datos. En la Tabla 2-3 se presenta de la distribución de frecuencias de la dirección del viento en
función de la magnitud de la velocidad. La dirección del viento predominante corresponde a la
ONO con una ocurrencia del 14,70%, seguida por la dirección NO con un 13,14%.

Página | 6

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 2-3 Serie de tiempo de la dirección del viento obtenida para el año 2021.**

Fuente: Elaboración propia.

**Figura 2-4 Rosa de vientos - Año 2021.**

Fuente: Elaboración propia.

**Tabla 2-3 Distribución de frecuencias d la dirección del viento.**

|Dirección del Viento|Rango de Velocidad (m/s)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Dirección del Viento**|**0,5 - 2,1**|**2,1 - 3,6**|**3,6 - 5,7**|**5,7 - 8,8**|**8,8 - 11,1**|**>= 11,10**|**Total (%)**|
|N|1,20%|0,50%|0,55%|0,25%|0,09%|0,01%|2,60%|
|NNE|0,74%|0,22%|0,13%|0,07%|0,02%|0,00%|1,18%|
|NE|0,61%|0,03%|0,00%|0,00%|0,00%|0,00%|0,64%|
|ENE|1,05%|0,00%|0,00%|0,00%|0,00%|0,00%|1,05%|
|E|2,75%|0,05%|0,00%|0,00%|0,00%|0,00%|2,80%|
|ESE|2,53%|0,10%|0,07%|0,00%|0,00%|0,00%|2,71%|

Página | 7

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

|Dirección del Viento|Rango de Velocidad (m/s)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Dirección del Viento**|**0,5 - 2,1**|**2,1 - 3,6**|**3,6 - 5,7**|**5,7 - 8,8**|**8,8 - 11,1**|**>= 11,10**|**Total (%)**|
|SE|2,22%|0,13%|0,01%|0,00%|0,00%|0,00%|2,35%|
|SSE|1,32%|0,05%|0,01%|0,00%|0,00%|0,00%|1,38%|
|S|1,42%|0,32%|0,16%|0,02%|0,00%|0,00%|1,92%|
|SSO|1,91%|1,70%|2,03%|0,31%|0,00%|0,00%|5,95%|
|SO|2,96%|2,66%|2,37%|0,14%|0,00%|0,00%|8,13%|
|OSO|4,16%|1,50%|2,99%|0,18%|0,00%|0,00%|8,82%|
|O|7,96%|0,95%|0,57%|0,00%|0,00%|0,00%|9,48%|
|ONO|13,35%|0,63%|0,73%|0,00%|0,00%|0,00%|14,70%|
|NO|10,77%|1,27%|1,05%|0,05%|0,01%|0,00%|13,14%|
|NNO|2,39%|0,53%|0,61%|0,43%|0,06%|0,00%|4,01%|
|Sub-Total|57,31%|10,62%|11,28%|1,45%|0,18%|0,01%|80,85%|
|Calmas (%)|Calmas (%)|Calmas (%)|Calmas (%)|Calmas (%)|Calmas (%)|Calmas (%)|19,16%|
|Sin dato (%)|Sin dato (%)|Sin dato (%)|Sin dato (%)|Sin dato (%)|Sin dato (%)|Sin dato (%)|0,00%|
|Total (%)|Total (%)|Total (%)|Total (%)|Total (%)|Total (%)|Total (%)|100,00%|

Fuente: Elaboración propia.

**3.** **MODELACIÓN CALIDAD DEL AIRE**

**3.1.** **INFORMACIÓN GEOGRÁFICA**

La información de las elevaciones de terreno, utilizada por el modelo, corresponde a cartas
topográficas digitales SRTM3 (Shuttle Radar Topography Mission Global Coverage), con
resolución de 90 metros. En la Figura 3-1 se presentan las curvas de nivel utilizadas por el
modelo.

La información de uso de suelo de la zona fue obtenida a través de los archivos Global Land
Cover Characterization (GLCC) desarrollados por el U.S. Geological Survey (USGS). El mapa de
uso de suelos se presenta en la Figura 3-2.

Página | 8

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 3-1 Representación de información topográfica utilizada por el modelo.**

Página | 9

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

Fuente: Elaboración propia.

Página | 10

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 3-2 Representación de la información de uso de suelo utilizada por el modelo.**

Fuente: Elaboración propia.

**3.2.** **DESCRIPCIÓN DEL MODELO METEOROLÓGICO WRF**

El modelo WRF (Weather Research and Forecasting - WRF) es un sistema de predicción
numérico de mesoscala de última generación, diseñado para desarrollar pronósticos y estudios
de la atmósfera. Este modelo de última generación es el resultado de un trabajo mancomunado
entre varias instituciones norteamericanas como: la National Center for Atmospheric Research
(NCAR), the National Oceanic and Atmospheric Administration (NOAA), el National Centers for
Environmental Prediction (NCEP), el Forecast Systems Laboratory (FSL), la Air Force Weather
Agency (AFWA), el Naval Research Laboratory, la Universidad de Oklahoma, y la Federal
Aviation Administration (FAA).

La elaboración del archivo meteorológico WRF utilizado en la presente modelación se encargó a
la empresa nacional ENVIROMODELIG, y posee una resolución espacial de 1 km, abarcando un
área de 50 × 50 km y cuyo centro corresponde al punto de referencia del Proyecto. Los
parámetros de la proyección cónica utilizada por el modelo WRF se presenta en la Tabla 3-1.

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Página | 11 **ANEXO MODELACIÓN DE CALIDAD DEL AIRE** **“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”** -->

**Tabla 3-1: Parámetros de la proyección cónica del modelo WRF****

| Sistema coordenado del modelo WRF | Col2 |
| --- | --- |
| Proyección | LCC (Cónica Conforme de Lambert) |
| DATUM | NWS-84 6370KM Radius |
| Origen Proyección (latitud) | 34,394° |
| Origen Proyección (longitud) | 71,584° |
| Paralelo Estándar (Latitud 1) | 34,634° |
| Paralelo Estándar (Latitud 2) | 34,154° |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Información proporcionada por Lakes Environmental. **3.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF** -->
<!-- FIN TABLA 3-1 -->


Página | 11

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Tabla 3-1 Parámetros de la proyección cónica del modelo WRF**

|Sistema coordenado del modelo WRF|Col2|
|---|---|
|Proyección|LCC (Cónica Conforme de Lambert)|
|DATUM|NWS-84 6370KM Radius|
|Origen Proyección (latitud)|34,394°|
|Origen Proyección (longitud)|71,584°|
|Paralelo Estándar (Latitud 1)|34,634°|
|Paralelo Estándar (Latitud 2)|34,154°|

Fuente: Información proporcionada por Lakes Environmental.

**3.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF**

Dado que no existen registros meteorológicos válidos en el área de influencia del Proyecto no es
posible elaborar un análisis de incertidumbre del modelo WRF utilizado en el presente estudio, y
que fue elaborado tomando en cuenta todas las indicaciones presentadas por la Autoridad
Ambiental en la “Guía para el uso de modelos de calidad del aire en el SEA”, constituyendo la
mejor herramienta disponible para incorporar información meteorológica al sistema de
modelación de dispersión de contaminantes atmosféricos

**3.4.** **GRILLA DE RECEPTORES**

Las características del dominio utilizado para la evaluar el impacto del Proyecto sobre la calidad
del aire se presentan en la Tabla 3-2 y Figura 3-3. Las modelaciones se han realizado sobre una
grilla de 2.500 receptores, separados por una distancia de 1 km, tal como lo indica la “Guía para
el uso de modelos de calidad del aire en el SDIA”, con el fin de determinar el aporte del Proyecto
en cada uno de estos puntos e identificar la ubicación y magnitud de las concentraciones en los
puntos de máximo impacto para cada contaminante modelado.

**Tabla 3-2 Características del dominio de modelación**

|Coordenadas del centro (m)<br>(DATUM WGS84 18H)|X = 262.280<br>Y = 6.191.173|
|---|---|
|**Tamaño**|50 km x 50 km|
|**Resolución**|1 km|
|**N° de receptores**|2.500|

Fuente: Elaboración propia.

Página | 12

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 3-3 Dominio de modelación y grilla de receptores.**

Fuente: Elaboración propia.

Página | 13

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**3.5.** **RECEPTORES DISCRETOS**

Los receptores discretos o de interés definidos para la modelación se presentan en la Tabla 3-3
y corresponden a los aquellos puntos sensibles identificados en la elaboración del “Estudio de
Ruidos y Vibraciones” (ANEXO N°3.3 de la presente Declaración de Impacto Ambiental) tales
como viviendas e instalaciones agroindustriales. Además, se incluye un receptor representativo
de la ciudad de Marchigue por ser el centro poblado más cercano al Proyecto.

Cabe señalar que el receptor R5, descrito en la modelación anterior, fue eliminado del análisis
debido a que en el lugar que representaba (caseta de riego) no existe riesgo para la salud de la
población ni los recursos naturales que pueda ser evaluado.

**Tabla 3-3 Receptores discretos del modelo.**

|ID|Descripción|X (m)|Y (m)|Distancia al<br>Proyecto<br>(m)|
|---|---|---|---|---|
|R1|Vivienda de dos pisos de altura material Mixto,<br>ubicado al este del área del Proyecto|261.124|6.190.944|163|
|R2|Fundo Santa Rita Marchigue, sector de viviendas de<br>un piso de altura, sector entrada al fundo. Estructura<br>de un piso de altura|263.537|6.189.423|1.093|
|R3|Fundo Santa Rita Marchigue, instalaciones<br>agroindustriales de hasta dos pisos de altura|263.633|6.190.619|725|
|R4|Sector de viviendas de un piso de altura, localizadas<br>al oriente del área del Proyecto|263.644|6.191.730|386|
|R5|Sector de viviendas de un piso de altura, ubicadas<br>al norte del área del Proyecto|263.773|6.192.451|Colindante|
|R6|Fundo “Silvestres”, estructura de uso agrícola de un<br>piso de altura ubicado al norte del área del Proyecto|262.270|6.193.267|1.146|
|R7|Vivienda de un piso de altura, ubicada al sur<br>occidente del área del Proyecto|260.047|6.192.228|463|
|R8|Vivienda de un piso de altura, localizada al<br>noroccidente del área del Proyecto|260.479|6.192.809|255|
|R9|Sitio de uso agrícola, estructura sólida de un piso de<br>altura ubicada al sur del área del Proyecto|258.730|6.194.167|154|
|R10|Sitio de uso agrícola, estructura sólida de un piso de<br>altura ubicada al norte del área del Proyecto|259.508|6.194.442|608|
|R11|Vivienda de un piso de altura, localizada al<br>noroccidente del área del Proyecto|259.074|6.195.066|55|
|R12|Sector de viviendas de entre uno y dos pisos de<br>altura, ubicada al norte del área del proyecto|259.641|6.196.069|Colindante|
|R13|Marchigue|258.955|6.190.541|2.337|

Fuente: Elaboración propia. DATUM WGS84, Huso 19 Sur.

Página | 14

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 3-4 Distribución de receptores discretos**

Fuente: Elaboración propia.

**3.6.** **FUENTES DE EMISIÓN**

En la Tabla 3-4 se muestran las emisiones estimadas para el Año 1 de la fase de construcción
del Proyecto y cuyo detalle de cálculo se presenta en el Anexo 3.2 “Estimación de Emisiones
Atmosféricas” de la Adenda Complementaria. Como puede observarse, las mayores emisiones
de contaminantes atmosféricos que se generarán durante la fase de construcción del Proyecto
corresponden a las emisiones de NOx generadas por la combustión de la maquinaria (2,99
ton/año). Le siguen en importancia las emisiones de monóxido de carbono (CO), generado,
también por la combustión de la maquinaria (1,58 ton/año). En tercer lugar, se encuentran las
emisiones de MP10 generado por las excavaciones (1,45 ton/año). No se modelan emisiones de
SO 2 puesto que son inferiores a 0,01 t/año, por lo cual no hay efectos en este contaminante.

Página | 15

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Tabla 3-4 Emisiones contaminantes atmosféricos - Año 1 Fase de Construcción.**

|Actividad|Emisión (ton/año)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Actividad**|**MP10**|**MP2,5**|**CO**|**NOx**|
|Escarpe|0,22|0,03|0,00|0,00|
|Excavación|1,45|0,75|0,00|0,00|
|Carguío y volteo de material|0,17|0,02|0,00|0,00|
|Nivelación|0,05|0,01|0,00|0,00|
|Perforación|0,85|0,13|0,00|0,00|
|Compactación|0,01|0,00|0,00|0,00|
|Camino no pavimentado|1,07|0,11|0,00|0,00|
|Caminos pavimentados|0,97|0,23|0,00|0,00|
|Combustión de vehículos|0,01|0,01|0,03|0,45|
|Combustión maquinaria fuera de ruta|0,17|0,17|1,58|2,99|
|Grupos electrógenos|0,00|0,00|0,01|0,05|
|**Total (ton/año)**|**4,97**|**1,46**|**1,62**|**3,48**|

Fuente: Anexo 3.2 Estimación de Emisiones Atmosféricas.

En la Tabla 3-5 se presentan las emisiones agrupadas por fuente de emisión y la superficie que
se ha asignado a cada una de éstas en el modelo. Para estimar el área de los caminos se asignó
a cada uno ancho común de 7 metros.

**Tabla 3-5 Superficie y emisiones por fuente.**

|Fuente|Área<br>fuente en<br>el modelo<br>(m2)|Emisiones Año 1 - Fase de Construcción (ton/año)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Fuente**|**Área**<br>**fuente en**<br>**el modelo**<br>**(m2)**|**MP10**|**MP2,5**|**CO**|**NOX**|
|Proyecto y Línea de Alta Tensión|2.138.367|2,91|1,11|1,59|3,04|
|Caminos no pavimentados|15.722|1,07|0,11|0,02|0,23|
|Caminos pavimentados|689.752|0,97|0,23|0,02|0,23|
|**Total (ton/año)**|**Total (ton/año)**|**4,97**|**1,46**|**1,62**|**3,48**|

Fuente: Elaboración propia.

Al ingresar las emisiones al modelo se ha supuesto que todo el NOx obtenido en la estimación
de emisiones corresponden a NO 2 . Las tasas de emisión ingresadas al modelo se presentan en
la Tabla 3-6. La representación gráfica de las fuentes en el modelo CALPUFF, se presenta en la

<!-- INICIO TABLA 3-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Al ingresar las emisiones al modelo se ha supuesto que todo el NOx obtenido en la estimación de emisiones corresponden a NO 2 . Las tasas de emisión ingresadas al modelo se presentan en la Tabla 3-6. La representación gráfica de las fuentes en el modelo CALPUFF, se presenta en la Figura 3-5. -->

**Tabla 3-6: Emisiones ingresadas al modelo - Año 1 Fase de construcción.****

| Fuente | Emisión (ton/m2·año) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Fuente** | **MP10** | **MP2,5** | **CO** | **NOx** |
| Proyecto y Línea de Alta Tensión | 1,4E-06 | 5,2E-07 | 7,4E-07 | 1,4E-06 |
| Caminos no pavimentados | 6,8E-05 | 7,0E-06 | 9,5E-07 | 1,4E-05 |
| Caminos pavimentados | 1,4E-06 | 3,4E-07 | 2,2E-08 | 3,3E-07 |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Página | 16 -->
<!-- FIN TABLA 3-6 -->

Figura 3-5.

**Tabla 3-6 Emisiones ingresadas al modelo - Año 1 Fase de construcción.**

|Fuente|Emisión (ton/m2·año)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Fuente**|**MP10**|**MP2,5**|**CO**|**NOx**|
|Proyecto y Línea de Alta Tensión|1,4E-06|5,2E-07|7,4E-07|1,4E-06|
|Caminos no pavimentados|6,8E-05|7,0E-06|9,5E-07|1,4E-05|
|Caminos pavimentados|1,4E-06|3,4E-07|2,2E-08|3,3E-07|

Fuente: Elaboración propia.

Página | 16

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 3-5 Representación de las fuentes en el modelo.**

Fuente: Elaboración propia.

Página | 17

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**4.** **MARCO LEGAL APLICABLE AL PROYECTO**

La Ley sobre Bases Generales del Medio Ambiente (Ley N° 19.300, modificada por la Ley N°
20.417/2010, ambas del Ministerio Secretaría Regional de la Presidencia), establece en su
artículo N° 32, la existencia de dos tipos de normas de calidad ambiental. Las normas de calidad
primarias, son aquellas que tienen como objetivo proteger la salud de la población humana dentro
del territorio nacional.
Una definición más precisa de norma primaria es la que se establece en artículo 2° de la Ley:
_“Norma Primaria de Calidad Ambiental: aquella que establece los valores de las concentraciones_
_y períodos, máximos o mínimos permisibles de elementos, compuestos, sustancias, derivados_
_químicos o biológicos, energías, radiaciones, vibraciones, ruidos o combinación de ellos, cuya_
_presencia o carencia en el ambiente pueda constituir un riesgo para la vida o la salud de la_
_población”._ La normativa primaria de calidad del aire aplicable al Proyecto se presenta en la Tabla
4-1.

**Tabla 4-1 Normativa primaria de Calidad del Aire aplicable al Proyecto.**

|Contaminante|Decreto N°|Año Promulgación|Promedio|Límite (μg/Nmɜ)|
|---|---|---|---|---|
|MP10|12|2022|24 horas - Percentil 98|130|
|MP10|12|2022|Anual|50|
|MP2,5|12|2011|24 horas - Percentil 98|50|
|MP2,5|12|2011|Anual|20|
|CO|115|2002|1 hora|30.000|
|CO|115|2002|8 horas|10.000|
|NO2|114|2002|1 hora|400|
|NO2|114|2002|Anual|100|

Fuente: Elaboración propia.

**5.** **RESULTADOS DE LA MODELACIÓN**

A continuación, se presentan los resultados obtenidos al incorporar al modelo de dispersión las
emisiones generadas durante el Año 1 de la fase de construcción del Proyecto.

**5.1.** **PUNTOS DE MÁXIMO IMPACTO**

Los puntos de máximo impacto (PMI) corresponden a aquellos receptores de la grilla del modelo
en donde las emisiones generadas durante la fase de construcción del Proyecto generan las
máximas concentraciones de los distintos contaminantes atmosféricos. Estas concentraciones
pueden corresponder a promedios de una hora, 8 horas, 24 horas o un año, de acuerdo con las
diferentes normas de calidad del aire analizadas.

En la Tabla 5-1 se presentan los PMI del Proyecto para cada contaminante atmosférico de
acuerdo con la normativa de calidad del aire vigente. Como puede comprobarse, en ningún punto
este aporte máximo excede la norma ni alcanza niveles de latencia. El contaminante para el que

Página | 18

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

se obtiene la mayor concentración con respecto a la norma es el MP10 que alcanza el 1,7% del
límite anual con 0,87 μg/mɜ, lo que corresponde a un aporte poco significativo, que no alterará la
condición basal de calidad del aire del área de influencia del Proyecto.

En la Tabla 5-2 se muestran las coordenadas del punto de máximo impacto para cada norma de
calidad del aire evaluada. Los puntos son dos, y corresponden al receptor discreto PMI1 que
coincide con R5 (vivienda ubicada a un costado del camino no pavimentado) y al receptor PMI2
(receptor de la grilla de modelación correspondiente a superficie de cultivos). La ubicación de
ambos puntos, relativa al Proyecto, se presenta la Figura 5-1.

**Tabla 5-1 Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1.**

|Norma de calidad del aire|Valor Norma<br>(μg/Nmɜ)|Concentración<br>(μg/mɜ)|Aporte respecto a<br>norma %|
|---|---|---|---|
|MP10 24 horas Per98|130|2,12|1,6%|
|MP10 Anual|50|0,87|1,7%|
|MP2,5 24 horas Per98|50|0,48|1,0%|
|MP2,5 Anual|20|0,25|1,3%|
|NO2 1 hora Per99|400|3,15|0,8%|
|NO2 Anual|100|0,62|0,6%|
|CO 1 hora Per99|30.000|1,78|0,01%|
|CO 8 horas Per99|10.000|1,24|0,01%|

Fuente: Elaboración propia.

**Tabla 5-2 Coordenadas de los Puntos de Máximo Impacto - Fase de construcción Año 1.**

|Norma|ID|X (m)|Y (m)|
|---|---|---|---|
|MP10 24 horas Per98|PMI1|263.799|6.192.439|
|MP10 Anual|PMI1|263.799|6.192.439|
|MP2,5 24 horas Per98|PMI2|262.965|6.190.633|
|MP2,5 Anual|PMI2|262.965|6.190.633|
|NO2 1 hora Per99|PMI2|262.965|6.190.633|
|NO2 Anual|PMI2|262.965|6.190.633|
|CO 1 hora Per99|PMI2|262.965|6.190.633|
|CO 8 horas Per99|PMI2|262.965|6.190.633|

Fuente: Elaboración propia. DATUM 19 WGS84.

Página | 19

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-1 Ubicación de los Puntos de Máximo Impacto - Fase de construcción.**

Fuente: Elaboración propia.

**5.2.** **RECEPTORES DISCRETOS**

En la Tabla 5-3 se presentan las concentraciones obtenidas en los 13 receptores discretos o
sensibles que se han definido para el Proyecto (Tabla 3-3). En la Tabla 5-4 se comparan dichas

<!-- INICIO TABLA 3-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Cabe señalar que el receptor R5, descrito en la modelación anterior, fue eliminado del análisis debido a que en el lugar que representaba (caseta de riego) no existe riesgo para la salud de la población ni los recursos naturales que pueda ser evaluado. -->

**Tabla 3-3: Receptores discretos del modelo.****

| ID | Descripción | X (m) | Y (m) | Distancia al<br>Proyecto<br>(m) |
| --- | --- | --- | --- | --- |
| R1 | Vivienda de dos pisos de altura material Mixto,<br>ubicado al este del área del Proyecto | 261.124 | 6.190.944 | 163 |
| R2 | Fundo Santa Rita Marchigue, sector de viviendas de<br>un piso de altura, sector entrada al fundo. Estructura<br>de un piso de altura | 263.537 | 6.189.423 | 1.093 |
| R3 | Fundo Santa Rita Marchigue, instalaciones<br>agroindustriales de hasta dos pisos de altura | 263.633 | 6.190.619 | 725 |
| R4 | Sector de viviendas de un piso de altura, localizadas<br>al oriente del área del Proyecto | 263.644 | 6.191.730 | 386 |
| R5 | Sector de viviendas de un piso de altura, ubicadas<br>al norte del área del Proyecto | 263.773 | 6.192.451 | Colindante |
| R6 | Fundo “Silvestres”, estructura de uso agrícola de un<br>piso de altura ubicado al norte del área del Proyecto | 262.270 | 6.193.267 | 1.146 |
| R7 | Vivienda de un piso de altura, ubicada al sur<br>occidente del área del Proyecto | 260.047 | 6.192.228 | 463 |
| R8 | Vivienda de un piso de altura, localizada al<br>noroccidente del área del Proyecto | 260.479 | 6.192.809 | 255 |
| R9 | Sitio de uso agrícola, estructura sólida de un piso de<br>altura ubicada al sur del área del Proyecto | 258.730 | 6.194.167 | 154 |
| R10 | Sitio de uso agrícola, estructura sólida de un piso de<br>altura ubicada al norte del área del Proyecto | 259.508 | 6.194.442 | 608 |
| R11 | Vivienda de un piso de altura, localizada al<br>noroccidente del área del Proyecto | 259.074 | 6.195.066 | 55 |
| R12 | Sector de viviendas de entre uno y dos pisos de<br>altura, ubicada al norte del área del proyecto | 259.641 | 6.196.069 | Colindante |
| R13 | Marchigue | 258.955 | 6.190.541 | 2.337 |

<!-- Estadísticas: 13 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. DATUM WGS84, Huso 19 Sur. Página | 14 -->
<!-- FIN TABLA 3-3 -->

concentraciones con los límites establecidos en las normas de calidad del aire de cada
contaminante atmosférico. Tal como puede observarse, el aporte del Proyecto es poco
significativo en todos los receptores discretos alcanzando un máximo del 1,7% (0,87 μg/Nm3) de
la norma primaria de MP10 en concentración anual en el receptor discreto R5.

Página | 20

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Tabla 5-3 Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1**

|Receptor|MP10 (μg/Nm3)|Col3|MP2,5 (μg/Nm3)|Col5|NO2 (μg/Nm3)|Col7|CO (μg/Nm3)|Col9|
|---|---|---|---|---|---|---|---|---|
|**Receptor**|**24 horas**|**Anual**|**24 horas**|**Anual**|**1 Hora**|**Anual**|**1 hora**|**8 horas**|
|R1|1,02|0,27|0,38|0,10|2,6|0,23|1,45|0,94|
|R2|0,49|0,16|0,19|0,06|1,3|0,13|0,74|0,54|
|R3|0,87|0,40|0,33|0,15|2,0|0,34|1,16|0,80|
|R4|0,87|0,43|0,24|0,12|1,6|0,27|0,90|0,55|
|R5|2,12|0,87|0,26|0,12|1,4|0,24|0,60|0,36|
|R6|0,40|0,11|0,11|0,03|0,7|0,05|0,41|0,27|
|R7|0,50|0,11|0,17|0,04|1,2|0,08|0,69|0,46|
|R8|0,56|0,11|0,14|0,03|1,0|0,07|0,58|0,40|
|R9|0,20|0,03|0,04|0,01|0,2|0,02|0,10|0,08|
|R10|0,14|0,04|0,04|0,01|0,2|0,02|0,11|0,09|
|R11|0,10|0,03|0,03|0,01|0,1|0,01|0,08|0,06|
|R12|0,07|0,02|0,02|0,01|0,1|0,01|0,07|0,04|
|Marchigue|0,24|0,05|0,09|0,02|0,6|0,03|0,33|0,22|

Fuente: Elaboración propia.

**Tabla 5-4 Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de**

**construcción Año 1**

|Receptor|MP10|Col3|MP2,5|Col5|NO2|Col7|CO|Col9|
|---|---|---|---|---|---|---|---|---|
|**Receptor**|**24 horas**|**Anual**|**24 horas**|**Anual**|**1 Hora**|**Anual**|**1 hora**|**8 horas**|
|R1|0,8%|0,5%|0,8%|0,5%|0,7%|0,2%|0,0%|0,0%|
|R2|0,4%|0,3%|0,4%|0,3%|0,3%|0,1%|0,0%|0,0%|
|R3|0,7%|0,8%|0,7%|0,8%|0,5%|0,3%|0,0%|0,0%|
|R4|0,7%|0,9%|0,5%|0,6%|0,4%|0,3%|0,0%|0,0%|
|R5|1,6%|1,7%|0,5%|0,6%|0,4%|0,2%|0,0%|0,0%|
|R6|0,3%|0,2%|0,2%|0,2%|0,2%|0,1%|0,0%|0,0%|
|R7|0,4%|0,2%|0,3%|0,2%|0,3%|0,1%|0,0%|0,0%|
|R8|0,4%|0,2%|0,3%|0,2%|0,3%|0,1%|0,0%|0,0%|
|R9|0,2%|0,1%|0,1%|0,1%|0,1%|0,0%|0,0%|0,0%|
|R10|0,1%|0,1%|0,1%|0,1%|0,1%|0,0%|0,0%|0,0%|
|R11|0,1%|0,1%|0,1%|0,1%|0,0%|0,0%|0,0%|0,0%|
|R12|0,1%|0,0%|0,0%|0,1%|0,0%|0,0%|0,0%|0,0%|
|Marchigue|0,2%|0,1%|0,2%|0,1%|0,2%|0,0%|0,0%|0,0%|

Fuente: Elaboración propia.

Página | 21

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**5.3.** **Curvas de Isoconcentración - Fase de Construcción Año 1**

En las siguientes figuras se presentan las curvas de isoconcentración obtenidas para los
contaminantes atmosféricos modelados para la fase de construcción del Proyecto. En todas las
figuras se puede observar que el impacto sobre la calidad del aire se acota al área circundante al
Proyecto debido, principalmente, a la baja magnitud de las emisiones.

Página | 22

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-2 Curvas de Isoconcentración - MP10 24 horas Percentil 98.**

Fuente: Elaboración propia.

Página | 23

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-3 Curvas de Isoconcentración - MP10 Anual.**

Fuente: Elaboración propia.

Página | 24

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-4 Curvas de Isoconcentración - MP2,5 24 horas Percentil 98.**

Fuente: Elaboración propia.

Página | 25

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-5 Curvas de Isoconcentración - MP2,5 Anual.**

Fuente: Elaboración propia.

Página | 26

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-6 Curvas de Isoconcentración - NO** **2** **1 hora Percentil 99.**

Fuente: Elaboración propia.

Página | 27

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-7 Curvas de Isoconcentración - NO** **2** **Anual.**

Fuente: Elaboración propia.

Página | 28

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-8 Curvas de Isoconcentración - CO 1 hora Percentil 99**

Fuente: Elaboración propia.

Página | 29

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 5-9 Curvas de Isoconcentración - CO 8 horas Percentil 99**

Fuente: Elaboración propia.

Página | 30

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**6.** **ÁREA DE INFLUENCIA**

Se ha definido como área de influencia aquella superficie en que el aporte del Proyecto para un
contaminante determinado presenta concentraciones superiores al 1% de la norma. Las
concentraciones equivalentes al 1% de cada norma se presentan en la Tabla 6-1. En el caso del

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- limitada por las curvas obtenidas para el MP10, que son las que abarcan un área mayor con el fin de establecer el escenario más conservador posible. La isolínea azul corresponde al 1% de norma anual de MP10, mientras que la isolínea verde corresponde al 1% de norma diaria de MP10. -->

**Tabla 6-1: Concentración equivalente al 1% de la norma****

| Contaminante | Norma | Valor Norma (μg/Nmɜ) | 1% de la norma (μg/Nmɜ) |
| --- | --- | --- | --- |
| MP10 | 24 horas Percentil 98 | 130 | 1,30 |
| MP10 | Anual | 50 | 0,50 |
| MP2,5 | 24 horas Percentil 98 | 50 | 0,50 |
| MP2,5 | Anual | 20 | 0,20 |
| NO2 | 1 hora Percentil 99 | 400 | 4,0 |
| NO2 | Anual | 100 | 1,0 |
| CO | 1 hora Percentil 99 | 30.000 | 300,0 |
| CO | 8 horas Percentil 99 | 10.000 | 100,0 |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Figura 6-1 Área de influencia - Concentración MP10 24 horas Percentil 98.** -->
<!-- FIN TABLA 6-1 -->

CO (1 y 8 horas) y el NO 2 (1 hora y anual) y el MP2,5 24 horas, el aporte es tan bajo que en
ningún punto del modelo la concentración alcanza el 1% de las respectivas normas. Las áreas
de influencia obtenidas se presentan desde la Figura 6-1 a la Figura 6-3. Finalmente, en la Figura
6-4 se presenta el área influencia definida para el Proyecto que corresponde a la superficie
limitada por las curvas obtenidas para el MP10, que son las que abarcan un área mayor con el
fin de establecer el escenario más conservador posible. La isolínea azul corresponde al 1% de
norma anual de MP10, mientras que la isolínea verde corresponde al 1% de norma diaria de
MP10.

**Tabla 6-1 Concentración equivalente al 1% de la norma**

|Contaminante|Norma|Valor Norma (μg/Nmɜ)|1% de la norma (μg/Nmɜ)|
|---|---|---|---|
|MP10|24 horas Percentil 98|130|1,30|
|MP10|Anual|50|0,50|
|MP2,5|24 horas Percentil 98|50|0,50|
|MP2,5|Anual|20|0,20|
|NO2|1 hora Percentil 99|400|4,0|
|NO2|Anual|100|1,0|
|CO|1 hora Percentil 99|30.000|300,0|
|CO|8 horas Percentil 99|10.000|100,0|

Fuente: Elaboración propia.

**Figura 6-1 Área de influencia - Concentración MP10 24 horas Percentil 98.**

Página | 31

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

Fuente: Elaboración propia.

**Figura 6-2 Área de influencia - Concentración MP10 Anual.**

Fuente: Elaboración propia.

**Figura 6-3 Área de influencia - Concentración MP2,5 Anual.**

Fuente: Elaboración propia.

Página | 32

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**Figura 6-4 Área de influencia del Proyecto**

Fuente: Elaboración propia.

Página | 33

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**7.** **CONCLUSIONES**

La caracterización meteorológica del área en donde se emplazará del Proyecto, elaborada mediante los
datos contenidos en el modelo WRF para el año 2021 en el punto de extracción, permite determinar que la
velocidad del viento presenta un promedio de 1,6 m/s, con mínimos de 0,8 m/s durante la noche y máximos
de 3,7 m/s en la tarde. La dirección predominante del viento durante el día es OSO y durante el período
nocturno es NO.

La modelación de la dispersión de contaminantes atmosféricos utilizó la información meteorológica
contenida en el modelo WRF (WeatherResearch and Forecasting Model) descrito en la Sección 3.2.
Aunque no fue posible elaborar un análisis de incertidumbre del modelo, es importante destacar que el
modelo meteorológico WRF utilizado en la modelación de calidad del aire del presente Proyecto fue
elaborado tomando en cuenta todas las indicaciones presentadas por la Autoridad Ambiental en la “Guía
para el uso de modelos de calidad del aire en el SEA”, constituyendo la mejor herramienta disponible para
incorporar información meteorológica al sistema de modelación de dispersión de contaminantes
atmosféricos. Además, la estimación de emisiones y el modelo de calidad del aire se construyeron, ambos,
de manera de representar, simular y evaluar el peor escenario posible de emisiones atmosféricas con el fin
de obtener resultados conservadores.

El modelo de calidad del aire desarrollado para evaluar el impacto del proyecto “PARQUE FOTOVOLTAICO
ANDINO OCCIDENTE II” considera las emisiones que se generarán durante el primer año de la fase de
construcción y que se resumen a continuación:

 - 4,97 toneladas de MP10

 - 1,46 toneladas de MP2,5

 - 1,62 toneladas de CO

 - 3,48 toneladas de NO 2

El análisis de los resultados de la modelación, indica que las concentraciones proyectadas para el área
donde se emplazará el Proyecto cumplen con toda la normativa primaria de calidad del aire vigente en el
territorio nacional, tanto sus criterios diarios, horarios como anuales, teniendo en cuenta que los límites
establecidos en las normas de calidad primaria apuntan a proteger la salud de la población, las que
establecen límites más estrictos que las normas de calidad secundaria, las cuales están orientadas a
preservar el medio ambiente (decretos del MINSEGPRES: D.S. N°114/02 para NO 2 y D.S. N°115/02 para
CO; Decretos MMA: D.S. N° 12/22 para MP10 y D.S. N° 12/11 MP2,5), tanto en los receptores sensibles
como en los puntos de máximo impacto, para los cuatro contaminantes analizados. Expuesto lo anterior, y
tomando en cuenta que las actividades de construcción son transitorias, se puede concluir que el desarrollo
del proyecto “PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II” no afectará significativamente la salud
de la población dado que no se sobrepasa ninguna de las normas vigentes de calidad del aire aplicables
al Proyecto, y su máximo aporte, corresponde a menos del 2% de la normativa ambiental vigente (MP10
promedio anual).

Por otro lado, tampoco hay efectos en los recursos naturales, ya que la norma secundaria de SO 2 no se
afecta, al no necesitar modelar ya que las emisiones son inferiores a 0,01 t/año.

Kisi Cerda Palma
Ingeniero Civil Ambiental

Página | 34

**ANEXO MODELACIÓN DE CALIDAD DEL AIRE**
**“PARQUE FOTOVOLTAICO ANDINO OCCIDENTE II”**

**8.** **BIBLIOGRAFÍA**

_Guía para el uso de modelos de calidad del aire en el SEIA_ . Servicio de Evaluación Ambiental.
Ministerio de Medio Ambiente, 2012.

**9.** **APENDICE ARCHIVOS DE ENTRADA Y SALIDA DEL MODELO**

Página | 35

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-2: Validez de los datos meteorológicos - Año 2021****

| Variable | N° Registros Válidos | % Registros Válidos |
| --- | --- | --- |
| Velocidad del Viento | 8.760 | 100% |
| Dirección del Viento | 8.760 | 100% |

**Tabla 2-3: Distribución de frecuencias d la dirección del viento.****

| Dirección del Viento | Rango de Velocidad (m/s) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección del Viento** | **0,5 - 2,1** | **2,1 - 3,6** | **3,6 - 5,7** | **5,7 - 8,8** | **8,8 - 11,1** | **>= 11,10** | **Total (%)** |
| N | 1,20% | 0,50% | 0,55% | 0,25% | 0,09% | 0,01% | 2,60% |
| NNE | 0,74% | 0,22% | 0,13% | 0,07% | 0,02% | 0,00% | 1,18% |
| NE | 0,61% | 0,03% | 0,00% | 0,00% | 0,00% | 0,00% | 0,64% |
| ENE | 1,05% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 1,05% |
| E | 2,75% | 0,05% | 0,00% | 0,00% | 0,00% | 0,00% | 2,80% |
| ESE | 2,53% | 0,10% | 0,07% | 0,00% | 0,00% | 0,00% | 2,71% |

**Tabla 3-2: Características del dominio de modelación****

| Coordenadas del centro (m)<br>(DATUM WGS84 18H) | X = 262.280<br>Y = 6.191.173 |
| --- | --- |
| **Tamaño** | 50 km x 50 km |
| **Resolución** | 1 km |
| **N° de receptores** | 2.500 |

**Tabla 3-4: Emisiones contaminantes atmosféricos - Año 1 Fase de Construcción.****

| Actividad | Emisión (ton/año) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Actividad** | **MP10** | **MP2,5** | **CO** | **NOx** |
| Escarpe | 0,22 | 0,03 | 0,00 | 0,00 |
| Excavación | 1,45 | 0,75 | 0,00 | 0,00 |
| Carguío y volteo de material | 0,17 | 0,02 | 0,00 | 0,00 |
| Nivelación | 0,05 | 0,01 | 0,00 | 0,00 |
| Perforación | 0,85 | 0,13 | 0,00 | 0,00 |
| Compactación | 0,01 | 0,00 | 0,00 | 0,00 |
| Camino no pavimentado | 1,07 | 0,11 | 0,00 | 0,00 |
| Caminos pavimentados | 0,97 | 0,23 | 0,00 | 0,00 |
| Combustión de vehículos | 0,01 | 0,01 | 0,03 | 0,45 |
| Combustión maquinaria fuera de ruta | 0,17 | 0,17 | 1,58 | 2,99 |
| Grupos electrógenos | 0,00 | 0,00 | 0,01 | 0,05 |
| **Total (ton/año)** | **4,97** | **1,46** | **1,62** | **3,48** |

**Tabla 3-5: Superficie y emisiones por fuente.****

| Fuente | Área<br>fuente en<br>el modelo<br>(m2) | Emisiones Año 1 - Fase de Construcción (ton/año) | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Fuente** | **Área**<br>**fuente en**<br>**el modelo**<br>**(m2)** | **MP10** | **MP2,5** | **CO** | **NOX** |
| Proyecto y Línea de Alta Tensión | 2.138.367 | 2,91 | 1,11 | 1,59 | 3,04 |
| Caminos no pavimentados | 15.722 | 1,07 | 0,11 | 0,02 | 0,23 |
| Caminos pavimentados | 689.752 | 0,97 | 0,23 | 0,02 | 0,23 |
| **Total (ton/año)** | **Total (ton/año)** | **4,97** | **1,46** | **1,62** | **3,48** |

**Tabla 4-1: Normativa primaria de Calidad del Aire aplicable al Proyecto.****

| Contaminante | Decreto N° | Año Promulgación | Promedio | Límite (μg/Nmɜ) |
| --- | --- | --- | --- | --- |
| MP10 | 12 | 2022 | 24 horas - Percentil 98 | 130 |
| MP10 | 12 | 2022 | Anual | 50 |
| MP2,5 | 12 | 2011 | 24 horas - Percentil 98 | 50 |
| MP2,5 | 12 | 2011 | Anual | 20 |
| CO | 115 | 2002 | 1 hora | 30.000 |
| CO | 115 | 2002 | 8 horas | 10.000 |
| NO2 | 114 | 2002 | 1 hora | 400 |
| NO2 | 114 | 2002 | Anual | 100 |

**Tabla 5-1: Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1.****

| Norma de calidad del aire | Valor Norma<br>(μg/Nmɜ) | Concentración<br>(μg/mɜ) | Aporte respecto a<br>norma % |
| --- | --- | --- | --- |
| MP10 24 horas Per98 | 130 | 2,12 | 1,6% |
| MP10 Anual | 50 | 0,87 | 1,7% |
| MP2,5 24 horas Per98 | 50 | 0,48 | 1,0% |
| MP2,5 Anual | 20 | 0,25 | 1,3% |
| NO2 1 hora Per99 | 400 | 3,15 | 0,8% |
| NO2 Anual | 100 | 0,62 | 0,6% |
| CO 1 hora Per99 | 30.000 | 1,78 | 0,01% |
| CO 8 horas Per99 | 10.000 | 1,24 | 0,01% |

**Tabla 5-2: Coordenadas de los Puntos de Máximo Impacto - Fase de construcción Año 1.****

| Norma | ID | X (m) | Y (m) |
| --- | --- | --- | --- |
| MP10 24 horas Per98 | PMI1 | 263.799 | 6.192.439 |
| MP10 Anual | PMI1 | 263.799 | 6.192.439 |
| MP2,5 24 horas Per98 | PMI2 | 262.965 | 6.190.633 |
| MP2,5 Anual | PMI2 | 262.965 | 6.190.633 |
| NO2 1 hora Per99 | PMI2 | 262.965 | 6.190.633 |
| NO2 Anual | PMI2 | 262.965 | 6.190.633 |
| CO 1 hora Per99 | PMI2 | 262.965 | 6.190.633 |
| CO 8 horas Per99 | PMI2 | 262.965 | 6.190.633 |

**Tabla 5-3: Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1****

| Receptor | MP10 (μg/Nm3) | Col3 | MP2,5 (μg/Nm3) | Col5 | NO2 (μg/Nm3) | Col7 | CO (μg/Nm3) | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **24 horas** | **Anual** | **24 horas** | **Anual** | **1 Hora** | **Anual** | **1 hora** | **8 horas** |
| R1 | 1,02 | 0,27 | 0,38 | 0,10 | 2,6 | 0,23 | 1,45 | 0,94 |
| R2 | 0,49 | 0,16 | 0,19 | 0,06 | 1,3 | 0,13 | 0,74 | 0,54 |
| R3 | 0,87 | 0,40 | 0,33 | 0,15 | 2,0 | 0,34 | 1,16 | 0,80 |
| R4 | 0,87 | 0,43 | 0,24 | 0,12 | 1,6 | 0,27 | 0,90 | 0,55 |
| R5 | 2,12 | 0,87 | 0,26 | 0,12 | 1,4 | 0,24 | 0,60 | 0,36 |
| R6 | 0,40 | 0,11 | 0,11 | 0,03 | 0,7 | 0,05 | 0,41 | 0,27 |
| R7 | 0,50 | 0,11 | 0,17 | 0,04 | 1,2 | 0,08 | 0,69 | 0,46 |
| R8 | 0,56 | 0,11 | 0,14 | 0,03 | 1,0 | 0,07 | 0,58 | 0,40 |
| R9 | 0,20 | 0,03 | 0,04 | 0,01 | 0,2 | 0,02 | 0,10 | 0,08 |
| R10 | 0,14 | 0,04 | 0,04 | 0,01 | 0,2 | 0,02 | 0,11 | 0,09 |
| R11 | 0,10 | 0,03 | 0,03 | 0,01 | 0,1 | 0,01 | 0,08 | 0,06 |
| R12 | 0,07 | 0,02 | 0,02 | 0,01 | 0,1 | 0,01 | 0,07 | 0,04 |
| Marchigue | 0,24 | 0,05 | 0,09 | 0,02 | 0,6 | 0,03 | 0,33 | 0,22 |

**Tabla 5-4: Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de****

| Receptor | MP10 | Col3 | MP2,5 | Col5 | NO2 | Col7 | CO | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **24 horas** | **Anual** | **24 horas** | **Anual** | **1 Hora** | **Anual** | **1 hora** | **8 horas** |
| R1 | 0,8% | 0,5% | 0,8% | 0,5% | 0,7% | 0,2% | 0,0% | 0,0% |
| R2 | 0,4% | 0,3% | 0,4% | 0,3% | 0,3% | 0,1% | 0,0% | 0,0% |
| R3 | 0,7% | 0,8% | 0,7% | 0,8% | 0,5% | 0,3% | 0,0% | 0,0% |
| R4 | 0,7% | 0,9% | 0,5% | 0,6% | 0,4% | 0,3% | 0,0% | 0,0% |
| R5 | 1,6% | 1,7% | 0,5% | 0,6% | 0,4% | 0,2% | 0,0% | 0,0% |
| R6 | 0,3% | 0,2% | 0,2% | 0,2% | 0,2% | 0,1% | 0,0% | 0,0% |
| R7 | 0,4% | 0,2% | 0,3% | 0,2% | 0,3% | 0,1% | 0,0% | 0,0% |
| R8 | 0,4% | 0,2% | 0,3% | 0,2% | 0,3% | 0,1% | 0,0% | 0,0% |
| R9 | 0,2% | 0,1% | 0,1% | 0,1% | 0,1% | 0,0% | 0,0% | 0,0% |
| R10 | 0,1% | 0,1% | 0,1% | 0,1% | 0,1% | 0,0% | 0,0% | 0,0% |
| R11 | 0,1% | 0,1% | 0,1% | 0,1% | 0,0% | 0,0% | 0,0% | 0,0% |
| R12 | 0,1% | 0,0% | 0,0% | 0,1% | 0,0% | 0,0% | 0,0% | 0,0% |
| Marchigue | 0,2% | 0,1% | 0,2% | 0,1% | 0,2% | 0,0% | 0,0% | 0,0% |
