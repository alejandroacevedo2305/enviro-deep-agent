---
title: Microsoft Word - MOD Portal La Foresta Adenda
author: Rodrigo
date: D:20211227222911-03'00'
language: es
type: report
pages: 50
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ÍNDICE GENERAL
-->

ANEXO C

INFORME

MODELACIÓN DE CALIDAD DEL AIRE

DECLARACIÓN DE IMPACTO AMBIENTAL

“PORTAL LA FORESTA”

COMUNA DE VIÑA DEL MAR, REGIÓN DE VALPARAÍSO

SEPTIEMBRE, 2021

ELABORADO PARA CBLS AMBIENTAL

POR KISI CERDA PALMA - INGENIERO CIVIL AMBIENTAL

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

# ÍNDICE GENERAL

**1.** **ANTECEDENTES GENERALES DEL PROYECTO ................................................................................ 5**

**2.** **LINEA DE BASE ......................................................................................................................................... 6**

2.1. METEOROLOGÍA ...................................................................................................................................... 7

2.1.1 Validez de los registros meteorológicos ........................................................................................ 7

2.1.2 Velocidad del viento .......................................................................................................................... 7

2.1.3 Dirección del Viento .......................................................................................................................... 8

2.2. CALIDAD DEL AIRE................................................................................................................................ 10

**3.** **MODELACIÓN CALIDAD DEL AIRE....................................................................................................... 10**

3.1. Información Geográfica ........................................................................................................................... 10

3.2. Descripción del Modelo Meteorológico WRF ...................................................................................... 13

3.3. Análisis de Incertidumbre del Modelo Meteorológico WRF ............................................................... 13

3.3.1 Velocidad del Viento ....................................................................................................................... 13

3.3.2 Dirección del Viento ........................................................................................................................ 14

3.4. Grilla de receptores ................................................................................................................................. 16

3.5. Receptores Discretos .............................................................................................................................. 18

3.6. Fuentes de emisión ................................................................................................................................. 19

**4.** **MARCO LEGAL APLICABLE AL PROYECTO ...................................................................................... 23**

**5.** **RESULTADOS DE LA MODELACIÓN .................................................................................................... 24**

5.1. Puntos de máximo Impacto .................................................................................................................... 24

5.1.1 Análisis Normativo .......................................................................................................................... 26

5.2. Receptores Discretos .............................................................................................................................. 26

5.2.1 Análisis Normativo .......................................................................................................................... 28

5.3. Curvas de Isoconcentración - Fase de Construcción ........................................................................ 30

5.4. Material Particulado Sedimentable ....................................................................................................... 40

**6.** **ÁREA DE INFLUENCIA ............................................................................................................................ 41**

**7.** **CONCLUSIONES ....................................................................................................................................... 47**

**8.** **BIBLIOGRAFÍA .......................................................................................................................................... 49**

**9.** **ANEXO C ARCHIVOS DE ENTRADA Y SALIDA DEL MODELO (DIGITAL) ..................................... 50**

Página | 2

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**INDICE DE TABLAS**

Tabla 2-1 Ubicación de la estación Junta de Vecinos ........................................................................................... 6

Tabla 2-2 Validez de registros meteorológicos - Año 2020. ................................................................................ 7

Tabla 2-3 Distribución de frecuencias (%) - Estación Junta de Vecinos 2020 ................................................. 9

Tabla 2-4 Línea de base de calidad del aire trienio 2017 - 2019 en la estación Junta de Vecinos ............. 10

Tabla 3-1 Parámetros de la proyección cónica del modelo WRF ...................................................................... 13

Tabla 3-2 Error Cuadrático Medio, Sesgo y Coeficiente de Correlación del ciclo diario de Velocidad del

Viento. Mediciones vs. Modelo WRF en Estación Junta de Vecinos ................................................................ 14

Tabla 3-3 Características del dominio de modelación ......................................................................................... 16

Tabla 3-4 Receptores discretos del modelo .......................................................................................................... 18

Tabla 3-5 Emisiones totales de contaminantes atmosféricos - Año 1 Fase de construcción ....................... 20

Tabla 3-6 Superficie y emisiones agrupadas por fuente ..................................................................................... 21

Tabla 3-7 Emisiones ingresadas al modelo - Fase de construcción Año 1 ..................................................... 21

Tabla 4-1 Normativa primaria de calidad del aire aplicable al Proyecto ........................................................... 23

Tabla 4-2 Normativa secundaria de calidad del aire aplicable al Proyecto ...................................................... 23

Tabla 5-1 Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1 ..................... 24

Tabla 5-2 Coordenadas de los Puntos de Máximo Impacto - Fase de construcción Año 1 .......................... 25

Tabla 5-3 Análisis normativo en Puntos de Máximo Impacto - Fase de construcción Año 1 ....................... 26

Tabla 5-4 Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1............................... 27

Tabla 5-5 Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de construcción

Año 1 ........................................................................................................................................................................... 27

Tabla 5-6 Análisis normativo en receptores discretos - Concentración diaria MP10 ..................................... 28

Tabla 5-7 Análisis normativo en receptores discretos - Concentración anual MP10 ..................................... 29

Tabla 5-8 Análisis normativo en receptores discretos - Concentración horaria SO 2 ..................................... 29

Tabla 5-9 Análisis normativo en receptores discretos - Concentración diaria SO 2 ........................................ 30

Tabla 5-10 Análisis normativo en receptores discretos - Concentración anual SO 2 ...................................... 30

Tabla 6-1 Concentración equivalente al 1% de la norma ................................................................................... 41

**ÍNDICE DE FIGURAS**

Figura 1-1 Emplazamiento del Proyecto .................................................................................................................. 5

Figura 2-1 Ubicación de la estación Junta de Vecinos .......................................................................................... 6

Figura 2-2 Serie de tiempo de la velocidad del viento registrada durante el año 2020 - Estación Junta de

Vecinos ......................................................................................................................................................................... 7

Figura 2-3 Ciclo diario de la velocidad del viento registrada durante el año 2020 - Estación Junta de Vecinos

....................................................................................................................................................................................... 8

Figura 2-4 Serie de tiempo de la dirección del viento 2020 - Estación Junta de Vecinos ............................... 8

Figura 2-5 Rosa de vientos 2020 - Estación Junta de Vecinos............................................................................ 9

Figura 3-1 Representación de información topográfica utilizada por el modelo .............................................. 11

Figura 3-2 Representación de la información de uso de suelo utilizada por el modelo ................................. 12

Página | 3

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

Figura 3-3 Comparación de ciclos diarios de la velocidad del viento en Estación Junta de Vecinos.

Mediciones vs. Modelo WRF ................................................................................................................................... 14

Figura 3-4 Rosas de viento obtenidas del modelo WRF y los registros de la estación Junta de Vecinos .. 15

Figura 3-5 Comparación de series de tiempo de dirección del viento. Registros vs. Modelo WRF - Estación

Junta de Vecinos 2020 ............................................................................................................................................. 15

Figura 3-6 Dominio de modelación y grilla de receptores. .................................................................................. 17

Figura 3-7 Distribución de receptores sensibles o discretos .............................................................................. 19

Figura 3-8 Representación de las fuentes en el modelo. .................................................................................... 22

Figura 5-1 Ubicación de los Puntos de Máximo Impacto - Fase de construcción Año 1. ............................. 25

Figura 5-2 Curvas de Isoconcentración - MP10 24 horas Percentil 98 ............................................................ 31

Figura 5-3 Curvas de Isoconcentración - MP10 concentración anual .............................................................. 32

Figura 5-4 Curvas de Isoconcentración - MP2,5 24 horas Percentil 98........................................................... 33

Figura 5-5 Curvas de Isoconcentración - MP2,5 Anual ...................................................................................... 34

Figura 5-6 Curvas de Isoconcentración - NO 2 1 hora Percentil 99 ................................................................... 35

Figura 5-7 Curvas de Isoconcentración - NO 2 Anual .......................................................................................... 36

Figura 5-8 Curvas de Isoconcentración - SO 2 1 hora Percentil 98,5 ................................................................ 37

Figura 5-9 Curvas de Isoconcentración - SO 2 24 horas Percentil 99 ............................................................... 38

Figura 5-10 Curvas de Isoconcentración - SO 2 concentración anual ............................................................... 39

Figura 5-11 Curvas de isodeposición MPS anual - Fase de Construcción. .................................................... 40
Figura 6-1 Área de influencia - Concentración MP10 24 horas Percentil 98. ................................................. 42
Figura 6-2 Área de influencia - Concentración MP10 Anual. ............................................................................. 42
Figura 6-3 Área de influencia - Concentración MP2,5 24 horas Percentil 98 ................................................. 43
Figura 6-4 Área de influencia - Concentración MP2,5 Anual............................................................................. 43
Figura 6-5 Área de influencia - Concentración NO 2 1 hora Percentil 99. ........................................................ 44
Figura 6-6 Área de influencia - Concentración NO 2 Anual ................................................................................. 44
Figura 6-7 Área de influencia - Concentración SO 2 1 hora Percentil 98,5 ...................................................... 45
Figura 6-8 Área de influencia - Concentración SO 2 24 horas Percentil 99...................................................... 45
Figura 6-9 Área de influencia - Concentración SO 2 Anual ................................................................................. 46
Figura 6-10 Área de influencia del Proyecto para la componente aire ............................................................. 46

Página | 4

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**1.** **ANTECEDENTES GENERALES DEL PROYECTO**

El proyecto “Portal La Foresta” (en adelante, el Proyecto) consiste en la construcción de dos edificios de

carácter habitacional para albergar departamentos pensados en familias modernas que valoren tener

seguridad, muy buena conectividad mediante vías estructurantes, movilización pública a la puerta y el

recién inaugurado Parque La Foresta, ubicado a escasos metros de distancia.

La localización permite insertar en un medio urbano plenamente consolidado una oferta de viviendas que

utilizarán servicios públicos previamente diseñados para estos efectos, como son la vialidad estructurante,

de servicios y el parque urbano más grande de la comuna en este sector. El Proyecto ofrece, también,

equipamientos deportivos exclusivos que vienen a complementar los accesos inmediatos al parque y algo

más lejanamente al borde costero.

La identidad del Proyecto está construida a partir de conceptos bien definidos: los diseños interiores de

los departamentos y exteriores de los edificios, las formas de sus terrazas y fachadas, los equipamientos

deportivos como una piscina semi olímpica de 25 metros de largo y una cancha de paddle tenis, la

disposición de estacionamientos y el fomento del uso de bicicletas. Este desarrollo inmobiliario se

emplazará en un predio ubicado en Av. Edmundo Eluchans N° 2460 y 2490, esquina calle Los Médanos,

Reñaca Bajo, Viña del Mar. La ubicación del Proyecto se presenta en la Figura 1-1.

El presente informe describe la modelación de la dispersión de las emisiones atmosféricas estimadas para

el primer año de la construcción del Proyecto de acuerdo a las exigencias indicadas en la “Guía para el uso

de modelos de calidad del aire en el SEA”.

**Figura 1-1 Emplazamiento del Proyecto**

Fuente: Elaboración propia.

Página | 5

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**2.** **LINEA DE BASE**

Para determinar la línea de base meteorológica y de calidad del aire del área donde se emplazará el

Proyecto, se han utilizado los datos registrados en la estación Junta de Vecinos, ubicada en Concón, a un

costado de la Plaza Las Petras y que pertenece a la red de monitoreo de ENAP. La estación se encuentra a

2,6 km al NE del Proyecto, tal como se puede observar en la Figura 2-1.

**Tabla 2-1 Ubicación de la estación Junta de Vecinos**

Fuente: Elaboración propia. DATUM WGS84 Huso 19. Fuente: Elaboración propia.

**Figura 2-1 Ubicación de la estación Junta de Vecinos**

Proyección Cónica Conforme de Lambert, DATUM NWS-84. Fuente: Elaboración propia.

Página | 6

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**2.1.** **METEOROLOGÍA**

Para caracterizar la meteorología se utilizarán los registros efectuados en la estación durante el año 2020.

**2.1.1** **Validez de los registros meteorológicos**

En la Tabla 2-2 se presentan las variables meteorológicas medidas en la estación y el porcentaje de

registros válidos. Dado que los parámetros medidos presentan validez de datos superiores al 99%, se da

cumplimiento a lo indicado en la “Guía para el uso de modelos de calidad del aire en el SEIA” que

recomienda que el porcentaje de datos válidos en un año sea superior al 75% (valor asociado a la validez

de la información de monitoreo establecido en las normas primarias de calidad del aire).

**Tabla 2-2 Validez de registros meteorológicos - Año 2020.**

|Variable N° Registros Válidos % Registros Válidos|Col2|Col3|
|---|---|---|
|Velocidad del Viento<br>8.769<br>99,87%|Velocidad del Viento<br>8.769<br>99,87%|Velocidad del Viento<br>8.769<br>99,87%|
|Dirección del Viento|8.769|99,87%|

Fuente: Elaboración propia.

**2.1.2** **Velocidad del viento**

La serie de tiempo de la velocidad del viento registrada en la estación Junta de Vecinos durante el año

2020 se presenta en la Figura 2-2. La velocidad del viento promedio registrada en la estación es de 1,5

m/s. Las velocidades del viento más bajas se presentan durante el período nocturno y comienzan a

aumentar desde las 7 de la mañana. En promedio, las velocidades más altas se registran entre las 14 y las

16 horas (2,5 m/s), tal como puede observarse en la Figura 2-3.

**Figura 2-2 Serie de tiempo de la velocidad del viento registrada durante el año 2020 - Estación Junta de Vecinos**

Fuente: Elaboración propia

Página | 7

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 2-3 Ciclo diario de la velocidad del viento registrada durante el año 2020 - Estación Junta de Vecinos**

Fuente: Elaboración propia

**2.1.3** **Dirección del Viento**

En la Figura 2-4 se muestran los registros horarios de la dirección del viento, obtenidos en la estación Junta

de Vecinos, mientras que en la Figura 2-5 se presenta la rosa de viento elaborada con dichos registros. En

la Tabla 2-3 se presenta de la distribución de frecuencias de la dirección del viento en función de la

magnitud de la velocidad. La dirección del viento predominante corresponde a la noroeste con una

ocurrencia del 12,4%, seguida por la dirección sur con un 8,6%.

**Figura 2-4 Serie de tiempo de la dirección del viento 2020 - Estación Junta de Vecinos**

Fuente: Elaboración propia.

Página | 8

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 2-5 Rosa de vientos 2020 - Estación Junta de Vecinos**

Fuente: Elaboración propia.

**Tabla 2-3 Distribución de frecuencias (%) - Estación Junta de Vecinos 2020**

|Rango de Velocidad (m/s)<br>Dirección del Viento<br>0,5 - 2,1 2,1 - 3,6 3,6 - 5,7 5,7 - 8,8 8,8 - 11,1 >= 11,10 Total (%)|Col2|
|---|---|
|N <br>4,6<br>1,2<br>0,3<br>0,0<br>0,0<br>0,0<br>6,0|N <br>4,6<br>1,2<br>0,3<br>0,0<br>0,0<br>0,0<br>6,0|
|NNE<br>3,8<br>0,7<br>0,0<br>0,0<br>0,0<br>0,0<br>4,5|NNE<br>3,8<br>0,7<br>0,0<br>0,0<br>0,0<br>0,0<br>4,5|
|NE<br>1,7<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>1,7|NE<br>1,7<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>1,7|
|ENE<br>1,1<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>1,1|ENE<br>1,1<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>1,1|
|E <br>3,8<br>0,1<br>0,0<br>0,0<br>0,0<br>0,0<br>3,9|E <br>3,8<br>0,1<br>0,0<br>0,0<br>0,0<br>0,0<br>3,9|
|ESE<br>5,0<br>0,4<br>0,0<br>0,0<br>0,0<br>0,0<br>5,4|ESE<br>5,0<br>0,4<br>0,0<br>0,0<br>0,0<br>0,0<br>5,4|
|SE<br>6,2<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>6,2|SE<br>6,2<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>6,2|
|SSE<br>4,6<br>0,4<br>0,0<br>0,0<br>0,0<br>0,0<br>4,9|SSE<br>4,6<br>0,4<br>0,0<br>0,0<br>0,0<br>0,0<br>4,9|
|S <br>7,3<br>0,8<br>0,5<br>0,0<br>0,0<br>0,0<br>8,6|S <br>7,3<br>0,8<br>0,5<br>0,0<br>0,0<br>0,0<br>8,6|
|SSW<br>2,0<br>0,6<br>0,2<br>0,0<br>0,0<br>0,0<br>2,7|SSW<br>2,0<br>0,6<br>0,2<br>0,0<br>0,0<br>0,0<br>2,7|
|SW<br>2,1<br>3,4<br>0,8<br>0,0<br>0,0<br>0,0<br>6,3|SW<br>2,1<br>3,4<br>0,8<br>0,0<br>0,0<br>0,0<br>6,3|
|WSW<br>2,7<br>2,6<br>0,0<br>0,0<br>0,0<br>0,0<br>5,4|WSW<br>2,7<br>2,6<br>0,0<br>0,0<br>0,0<br>0,0<br>5,4|
|W <br>3,4<br>2,8<br>0,0<br>0,0<br>0,0<br>0,0<br>6,2|W <br>3,4<br>2,8<br>0,0<br>0,0<br>0,0<br>0,0<br>6,2|
|WNW<br>3,2<br>2,4<br>0,0<br>0,0<br>0,0<br>0,0<br>5,6|WNW<br>3,2<br>2,4<br>0,0<br>0,0<br>0,0<br>0,0<br>5,6|
|NW<br>7,0<br>5,1<br>0,3<br>0,0<br>0,0<br>0,0<br>12,4|NW<br>7,0<br>5,1<br>0,3<br>0,0<br>0,0<br>0,0<br>12,4|
|NNW<br>6,1<br>1,5<br>0,4<br>0,0<br>0,0<br>0,0<br>8,0|NNW<br>6,1<br>1,5<br>0,4<br>0,0<br>0,0<br>0,0<br>8,0|
|Sub-Total<br>64,6<br>21,8<br>2,6<br>0,0<br>0,0<br>0,0<br>89,0|Sub-Total<br>64,6<br>21,8<br>2,6<br>0,0<br>0,0<br>0,0<br>89,0|
|Calmas (%)<br>10,8|Calmas (%)<br>10,8|
|Sin dato (%)<br>0,2|Sin dato (%)<br>0,2|
|Total (%)|100|

Fuente: Elaboración propia.

Página | 9

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**2.2.** **CALIDAD DEL AIRE**

Para determinar la línea de base de calidad se han considerado las mediciones de MP10 y SO 2 efectuadas

en la estación Junta de Vecinos durante el trienio 2017-2019 y que constan en el Informe “Línea de Base

de la Calidad del Aire en la Región de Valparaíso. Período 2017-2019” elaborado en conjunto por la SEREMI

Medio Ambiente y SEREMI Salud de la región de Valparaíso (2020).

**Tabla 2-4 Línea de base de calidad del aire trienio 2017 - 2019 en la estación Junta de Vecinos**

|Valor norma Concentración<br>Norma % Norma<br>(μg/Nmɜ) (μg/Nmɜ)|Col2|Col3|Col4|
|---|---|---|---|
|MP10 24 horas Percentil 98<br>150<br>64<br>43|MP10 24 horas Percentil 98<br>150<br>64<br>43|MP10 24 horas Percentil 98<br>150<br>64<br>43|MP10 24 horas Percentil 98<br>150<br>64<br>43|
|MP10 Anual<br>50<br>37<br>74|MP10 Anual<br>50<br>37<br>74|MP10 Anual<br>50<br>37<br>74|MP10 Anual<br>50<br>37<br>74|
|SO2 1 hora Percentil 98,5<br>350<br>33<br>9|SO2 1 hora Percentil 98,5<br>350<br>33<br>9|SO2 1 hora Percentil 98,5<br>350<br>33<br>9|SO2 1 hora Percentil 98,5<br>350<br>33<br>9|
|SO2 24 horas Percentil 99<br>150<br>31<br>21|SO2 24 horas Percentil 99<br>150<br>31<br>21|SO2 24 horas Percentil 99<br>150<br>31<br>21|SO2 24 horas Percentil 99<br>150<br>31<br>21|
|SO2 Anual|60|9|14|

Fuente: Tabla 6.1 Concentraciones Trianuales Período 2017-2019, Informe “Línea de Base de la Calidad del Aire en la Región de

Valparaíso. Período 2017-2019”. SEREMI Medio Ambiente y SEREMI Salud región de Valparaíso, 2020.

**3.** **MODELACIÓN CALIDAD DEL AIRE**

**3.1.** **INFORMACIÓN GEOGRÁFICA**

La información de las elevaciones de terreno, utilizada por el modelo, corresponde a cartas topográficas

digitales SRTM3 (Shuttle Radar Topography Mission Global Coverage), con resolución de 90 metros. En la

Figura 3-1 se presentan las curvas de nivel utilizadas por el modelo.

La información de uso de suelo de la zona fue obtenida a través de los archivos Global Land Cover

Characterization (GLCC) desarrollados por el U.S. Geological Survey (USGS). El mapa de uso de suelos se

presenta en la Figura 3-2.

Página | 10

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 3-1 Representación de información topográfica utilizada por el modelo**

Fuente: Elaboración propia.

Página | 11

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 3-2 Representación de la información de uso de suelo utilizada por el modelo**

Fuente: Elaboración propia.

Página | 12

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**3.2.** **DESCRIPCIÓN DEL MODELO METEOROLÓGICO WRF**

El modelo WRF (Weather Research and Forecasting - WRF) es un sistema de predicción numérico de

mesoscala de última generación, diseñado para desarrollar pronósticos y estudios de la atmósfera. Este

modelo de última generación es el resultado de un trabajo mancomunado entre varias instituciones

norteamericanas como: la National Center for Atmospheric Research (NCAR), the National Oceanic and

Atmospheric Administration (NOAA), el National Centers for Environmental Prediction (NCEP), el Forecast

Systems Laboratory (FSL), la Air Force Weather Agency (AFWA), el Naval Research Laboratory, la

Universidad de Oklahoma, y la Federal Aviation Administration (FAA).

La elaboración del archivo meteorológico WRF utilizado en la presente modelación se encargó a la

empresa nacional ENVIROMODELING, y posee una resolución espacial de 1 km, abarcando un área de 50

× 50 km y cuyo centro corresponde al punto de referencia del Proyecto. Los parámetros de la proyección

cónica utilizada por el modelo WRF se presentan en la Tabla 3-1.

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- × 50 km y cuyo centro corresponde al punto de referencia del Proyecto. Los parámetros de la proyección cónica utilizada por el modelo WRF se presentan en la Tabla 3-1. -->

**Tabla 3-1: Parámetros de la proyección cónica del modelo WRF****

| Sistema coordenado del modelo WRF | Col2 |
| --- | --- |
| Proyección<br>LCC (Cónica Conforme de Lambert) | Proyección<br>LCC (Cónica Conforme de Lambert) |
| DATUM<br>NWS-84 6370KM Radius | DATUM<br>NWS-84 6370KM Radius |
| Origen Proyección (latitud)<br>32,960 | Origen Proyección (latitud)<br>32,960 |
| Origen Proyección (longitud)<br>71,544 | Origen Proyección (longitud)<br>71,544 |
| Paralelo Estándar (Latitud 1)<br>32,720 | Paralelo Estándar (Latitud 1)<br>32,720 |
| Paralelo Estándar (Latitud 2) | 33,200 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: ENVIROMODELING. **3.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF** -->
<!-- FIN TABLA 3-1 -->


**Tabla 3-1 Parámetros de la proyección cónica del modelo WRF**

|Sistema coordenado del modelo WRF|Col2|
|---|---|
|Proyección<br>LCC (Cónica Conforme de Lambert)|Proyección<br>LCC (Cónica Conforme de Lambert)|
|DATUM<br>NWS-84 6370KM Radius|DATUM<br>NWS-84 6370KM Radius|
|Origen Proyección (latitud)<br>32,960|Origen Proyección (latitud)<br>32,960|
|Origen Proyección (longitud)<br>71,544|Origen Proyección (longitud)<br>71,544|
|Paralelo Estándar (Latitud 1)<br>32,720|Paralelo Estándar (Latitud 1)<br>32,720|
|Paralelo Estándar (Latitud 2)|33,200|

Fuente: ENVIROMODELING.

**3.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF**

A continuación, se presentan los resultados obtenidos al cuantificar el grado de ajuste del modelo

meteorológico WRF con respecto a las mediciones efectuadas en la estación Junta de Vecinos durante el

año 2020.

**3.3.1** **Velocidad del Viento**

En la Figura 3-3 se presentan los ciclos diarios de la velocidad del viento (medida y modelada) obtenidos

en la estación Junta de Vecinos. En la Tabla 3-2 se presentan el error cuadrático medio, el sesgo y el

coeficiente de correlación, parámetros que determinan cuantitativamente el grado de ajuste entre ambas

series de datos. Tal como puede observarse, ambas curvas presentan una forma similar, sin embargo, las

velocidades del viento modeladas son, en promedio, superiores a las registradas en la estación. Las

mayores diferencias se presentan durante el peak de ambos ciclos (modelado y medido) entre las 14 y las

15 horas. El mejor ajuste de ambos ciclos se logra entre las 9 y las 11 de la mañana.

Página | 13

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 3-3 Comparación de ciclos diarios de la velocidad del viento en Estación Junta de Vecinos. Mediciones vs.**

**Modelo WRF**

Fuente: Elaboración propia

**Tabla 3-2 Error Cuadrático Medio, Sesgo y Coeficiente de Correlación del ciclo diario de Velocidad del Viento.**

**Mediciones vs. Modelo WRF en Estación Junta de Vecinos**

|Estadístico Valor|Col2|
|---|---|
|Error cuadrático Medio (m/s)<br>0,42|Error cuadrático Medio (m/s)<br>0,42|
|Sesgo (m/s)<br>0,40|Sesgo (m/s)<br>0,40|
|Coeficiente de Correlación|0,99|

Fuente: Elaboración propia

**3.3.2** **Dirección del Viento**

En la Figura 3-4 se presentan las rosas de viento obtenidas a partir de los datos registrados y modelados

para el año 2018, mientras que en la Figura 3-5 se muestran los gráficos de ambas series de datos. Tal

como puede observarse, para este punto del dominio, el modelo WRF presenta las direcciones S y SSE

como predominantes, mientras que los registros muestran una dirección y que es la SSE.

Página | 14

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 3-4 Rosas de viento obtenidas del modelo WRF y los registros de la estación Junta de Vecinos**

|Mediciones Modelo WRF|Col2|
|---|---|
|||

Fuente: Elaboración propia.

**Figura 3-5 Comparación de series de tiempo de dirección del viento. Registros vs. Modelo WRF - Estación Junta**

**de Vecinos 2020**

Fuente: Elaboración propia.

Página | 15

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

Como es de esperar, al comparar la magnitud y la dirección de la velocidad del viento en la estación Junta

de Vecinos se obtiene una diferencia entre el modelo y las mediciones. Sin embargo, cabe destacar que el

modelo meteorológico WRF utilizado en la modelación de calidad del aire del presente proyecto fue

elaborado tomando en cuenta todas las indicaciones presentadas por la Autoridad Ambiental en la “Guía

para el uso de modelos de calidad del aire en el SEA”, constituyendo la mejor herramienta disponible para

incorporar información meteorológica al sistema de modelación de calidad del aire.

**3.4.** **GRILLA DE RECEPTORES**

Las características del dominio utilizado para la evaluar el impacto del Proyecto sobre la calidad del aire se

presentan en la Tabla 3-3 y Figura 3-6. Las modelaciones se han realizado sobre una grilla de 2.500

receptores, separados por una distancia de 1 km, tal como lo indica la “Guía para el uso de modelos de

calidad del aire en el SEIA”, con el fin de determinar el aporte del Proyecto en cada uno de estos puntos e

identificar la ubicación y magnitud de las concentraciones en los puntos de máximo impacto para cada

contaminante modelado.

|Tabla 3-3 Características del dominio de modelación|Col2|
|---|---|
|**Coordenadas del centro (m)**<br>**(DATUM WGS84 18H)**<br>X = 262.211<br>Y = 6.350.275|**Coordenadas del centro (m)**<br>**(DATUM WGS84 18H)**<br>X = 262.211<br>Y = 6.350.275|
|**Tamaño**<br>50 km x 50 km|**Tamaño**<br>50 km x 50 km|
|**Resolución**<br>1 km|**Resolución**<br>1 km|
|**N° de receptores**|2.500|

Fuente: Elaboración propia.

Página | 16

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 3-6 Dominio de modelación y grilla de receptores.**

Fuente: Elaboración propia.

Página | 17

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**3.5.** **RECEPTORES DISCRETOS**

Los receptores discretos o de interés definidos para la modelación se presentan en la Tabla 3-4 y

corresponden a los principales puntos sensibles que se encuentran dentro del dominio de modelación del

Proyecto, tales como viviendas, colegios, centros de salud y áreas verdes. La ubicación de los receptores

se presenta en la Figura 3-7.

**Tabla 3-4 Receptores discretos del modelo**

|Uso X Y Altura<br>ID Descripción<br>efectivo (m) (m) (m.s.n.m)|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82|R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82|R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82|R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82|R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82|R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82|
|R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82|R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82|R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82|R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82|R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82|R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82|
|R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82|R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82|R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82|R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82|R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82|R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82|
|R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79|R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79|R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79|R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79|R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79|R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79|
|R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112|R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112|R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112|R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112|R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112|R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112|
|R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104|R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104|R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104|R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104|R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104|R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104|
|R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106|R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106|R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106|R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106|R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106|R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106|
|R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103|R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103|R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103|R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103|R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103|R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103|
|R9|Colegio Sagrada Familia ubicado en Parcela<br>4, Los Pinos|Educación|262.803|6.351.045|124|

Fuente: Elaboración propia. DATUM WGS84.

Página | 18

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 3-7 Distribución de receptores sensibles o discretos**

Fuente: Elaboración propia.

**3.6.** **FUENTES DE EMISIÓN**

El escenario a modelar corresponde al primer año de la fase de construcción del Proyecto (Año 1)dado que

es la etapa en que se producirá el mayor volumen de emisiones atmosféricas. En la Tabla 3-5 se muestran

las emisiones atmosféricas estimadas para el Año 1 y cuyo detalle de cálculo se presenta en el Anexo 8

Estimación de Emisiones Atmosféricas de la presente Declaración de Impacto Ambiental. Como puede

observarse, las mayores emisiones de contaminantes atmosféricos que se generarán durante el primer

año de la fase de construcción del Proyecto corresponden al NOx generado por la operación de los grupos

electrógenos (6,5 toneladas/año). Le siguen en importancia las emisiones de MPS resuspendido por el

tránsito de camiones en caminos pavimentados (5,6 toneladas/año). En tercer lugar, se encuentran las

emisiones NOx producto del funcionamiento de la maquinaria fuera de ruta (3,8 toneladas/año).

Página | 19

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

En la Tabla 3-6 se presentan las emisiones agrupadas por fuente de emisión y la superficie que se ha

asignado a cada una de éstas en el modelo. Para estimar el área de los caminos se asignó a todos, un ancho

de 8 metros.

**Tabla 3-5 Emisiones totales de contaminantes atmosféricos - Año 1 Fase de construcción**

|Emisiones - Fase de construcción (kg)<br>Actividad<br>MPS MP10 MP2,5 CO NOx SOx COV/HC|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br>|Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br>|Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br>|Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br>|Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br>|Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br>|Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br>|Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br>|
|Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br>|Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br>|Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br>|Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br>|Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br>|Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br>|Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br>|Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br>|
|Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br>|Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br>|Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br>|Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br>|Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br>|Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br>|Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br>|Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br>|
|Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br>|Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br>|Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br>|Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br>|Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br>|Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br>|Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br>|Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br>|
|Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br>|Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br>|Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br>|Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br>|Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br>|Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br>|Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br>|Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br>|
|Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br>|Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br>|Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br>|Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br>|Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br>|Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br>|Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br>|Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br>|
|Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6|Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6|Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6|Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6|Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6|Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6|Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6|Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6|
|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0|
|Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5|Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5|Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5|Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5|Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5|Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5|Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5|Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5|
|Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0|Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0|Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0|Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0|Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0|Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0|Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0|Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0|
|Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br>|Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br>|Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br>|Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br>|Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br>|Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br>|Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br>|Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br>|
|**Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651**|**Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651**|**Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651**|**Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651**|**Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651**|**Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651**|**Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651**|**Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651**|
|**Total (ton/año)**|**14,5**|**4,3**|**1,6**|**3,1**|**12,2**|**0,5**|**0,7**|

Fuente: Tabla 5.1 Anexo 8 Estimación de Emisiones Atmosféricas DIA Portal La Foresta.

Página | 20

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Tabla 3-6 Superficie y emisiones agrupadas por fuente**

|Área fuente en el Emisiones - Fase de construcción Año 1 (kg/año)<br>Fuente<br>modelo (m2) MPS MP10 MP2,5 CO NOx SOx|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461|Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461|Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461|Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461|Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461|Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461|Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461|
|Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42|Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42|Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42|Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42|Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42|Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42|Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42|
|Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4|Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4|Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4|Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4|Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4|Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4|Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4|
|**Total (kg/año)**|**14.517**|**4.338**|**1.622**|**3.138**|**12.155**|**508**|

Fuente: Elaboración propia.

Al ingresar las emisiones al modelo se ha supuesto que todo el NOx y el SOx obtenido en la estimación de

emisiones corresponden a NO 2 y SO 2, respectivamente. Las tasas de emisión ingresadas al modelo se

presentan en la Tabla 3-7. La representación gráfica de las fuentes en el modelo CALPUFF, se presenta en

<!-- INICIO TABLA 3-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- presentan en la Tabla 3-7. La representación gráfica de las fuentes en el modelo CALPUFF, se presenta en la Figura 3-8. -->

**Tabla 3-7: Emisiones ingresadas al modelo - Fase de construcción Año 1****

| Emisión (ton/m2·año)<br>Fuente<br>MPS MP10 MP2,5 CO NOx SOx | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05 | Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05 | Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05 | Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05 | Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05 | Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05 | Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05 |
| Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07 | Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07 | Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07 | Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07 | Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07 | Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07 | Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07 |
| Caminos no pavimentados públicos | 6,1E-04 | 2,2E-04 | 2,2E-05 | 5,4E-06 | 2,0E-05 | 5,3E-07 |

<!-- Estadísticas: 3 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Página | 21 -->
<!-- FIN TABLA 3-7 -->


la Figura 3-8.

**Tabla 3-7 Emisiones ingresadas al modelo - Fase de construcción Año 1**

|Emisión (ton/m2·año)<br>Fuente<br>MPS MP10 MP2,5 CO NOx SOx|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05|Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05|Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05|Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05|Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05|Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05|Proyecto<br>5,7E-04<br>2,1E-04<br>1,7E-04<br>4,1E-04<br>1,6E-03<br>7,0E-05|
|Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07|Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07|Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07|Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07|Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07|Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07|Caminos pavimentados<br>3,4E-05<br>6,7E-06<br>1,8E-06<br>2,4E-06<br>1,0E-05<br>2,6E-07|
|Caminos no pavimentados públicos|6,1E-04|2,2E-04|2,2E-05|5,4E-06|2,0E-05|5,3E-07|

Fuente: Elaboración propia.

Página | 21

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 3-8 Representación de las fuentes en el modelo.**

Fuente: Elaboración propia.

Página | 22

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**4.** **MARCO LEGAL APLICABLE AL PROYECTO**

La Ley sobre Bases Generales del Medio Ambiente (Ley N° 19.300, modificada por la Ley N° 20.417/2010,

ambas del Ministerio Secretaría Regional de la Presidencia), establece en su artículo N° 32, la existencia

de dos tipos de normas de calidad ambiental. Las normas de calidad primarias, son aquellas que tienen

como objetivo proteger la salud de la población humana dentro del territorio nacional. Una definición más

precisa de norma primaria es la que se establece en artículo 2° de la Ley: _“Norma Primaria de Calidad_

_Ambiental: aquella que establece los valores de las concentraciones y períodos, máximos o mínimos_

_permisibles de elementos, compuestos, sustancias, derivados químicos o biológicos, energías, radiaciones,_

_vibraciones, ruidos o combinación de ellos, cuya presencia o carencia en el ambiente pueda constituir un_

_riesgo para la vida o la salud de la población.”_ La normativa primaria de calidad del aire aplicable al

Proyecto se presenta en la Tabla 4-1.

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _riesgo para la vida o la salud de la población.”_ La normativa primaria de calidad del aire aplicable al Proyecto se presenta en la Tabla 4-1. -->

**Tabla 4-1: Normativa primaria de calidad del aire aplicable al Proyecto****

| Límite<br>Contaminante Decreto N° Año Promulgación Promedio<br>(μg/Nmɜ) | Col2 | Col3 |
| --- | --- | --- |
| MP10<br>59<br>1998<br>24 horas - Percentil 98<br>150<br>Anual<br>50 | MP10<br>59<br>1998<br>24 horas - Percentil 98<br>150<br>Anual<br>50 | MP10<br>59<br>1998<br>24 horas - Percentil 98<br>150<br>Anual<br>50 |
| MP2,5<br>12<br>2011<br>24 horas - Percentil 98<br>50<br>Anual<br>20 | MP2,5<br>12<br>2011<br>24 horas - Percentil 98<br>50<br>Anual<br>20 | MP2,5<br>12<br>2011<br>24 horas - Percentil 98<br>50<br>Anual<br>20 |
| CO<br>115<br>2002<br>1 hora<br>30.000<br>8 horas<br>10.000 | CO<br>115<br>2002<br>1 hora<br>30.000<br>8 horas<br>10.000 | CO<br>115<br>2002<br>1 hora<br>30.000<br>8 horas<br>10.000 |
| NO2 <br>114<br>2002<br>1 hora<br>400<br>Anual<br>100 | NO2 <br>114<br>2002<br>1 hora<br>400<br>Anual<br>100 | NO2 <br>114<br>2002<br>1 hora<br>400<br>Anual<br>100 |
| SO2 <br>104<br>2018<br>1 hora<br>350<br>24 horas<br>150<br>Anual<br>60 | SO2 <br>104<br>2018<br>1 hora<br>350<br>24 horas<br>150<br>Anual<br>60 | SO2 <br>104<br>2018<br>1 hora<br>350<br>24 horas<br>150<br>Anual<br>60 |
| SO2 <br>104<br>2018<br>1 hora<br>350<br>24 horas<br>150<br>Anual<br>60 | Anual | 60 |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Por otro lado, la norma secundaria de calidad ambiental es aquella que establece los valores de las -->
<!-- FIN TABLA 4-1 -->


**Tabla 4-1 Normativa primaria de calidad del aire aplicable al Proyecto**

|Límite<br>Contaminante Decreto N° Año Promulgación Promedio<br>(μg/Nmɜ)|Col2|Col3|
|---|---|---|
|MP10<br>59<br>1998<br>24 horas - Percentil 98<br>150<br>Anual<br>50|MP10<br>59<br>1998<br>24 horas - Percentil 98<br>150<br>Anual<br>50|MP10<br>59<br>1998<br>24 horas - Percentil 98<br>150<br>Anual<br>50|
|MP2,5<br>12<br>2011<br>24 horas - Percentil 98<br>50<br>Anual<br>20|MP2,5<br>12<br>2011<br>24 horas - Percentil 98<br>50<br>Anual<br>20|MP2,5<br>12<br>2011<br>24 horas - Percentil 98<br>50<br>Anual<br>20|
|CO<br>115<br>2002<br>1 hora<br>30.000<br>8 horas<br>10.000|CO<br>115<br>2002<br>1 hora<br>30.000<br>8 horas<br>10.000|CO<br>115<br>2002<br>1 hora<br>30.000<br>8 horas<br>10.000|
|NO2 <br>114<br>2002<br>1 hora<br>400<br>Anual<br>100|NO2 <br>114<br>2002<br>1 hora<br>400<br>Anual<br>100|NO2 <br>114<br>2002<br>1 hora<br>400<br>Anual<br>100|
|SO2 <br>104<br>2018<br>1 hora<br>350<br>24 horas<br>150<br>Anual<br>60|SO2 <br>104<br>2018<br>1 hora<br>350<br>24 horas<br>150<br>Anual<br>60|SO2 <br>104<br>2018<br>1 hora<br>350<br>24 horas<br>150<br>Anual<br>60|
|SO2 <br>104<br>2018<br>1 hora<br>350<br>24 horas<br>150<br>Anual<br>60|Anual|60|

Fuente: Elaboración propia.

Por otro lado, la norma secundaria de calidad ambiental es aquella que establece los valores de las

concentraciones y períodos, máximos o mínimos permisibles de sustancias, elementos, energía o

combinación de ellos, cuya presencia o carencia en el ambiente pueda constituir un riesgo para la

protección o la conservación del medio ambiente, o la preservación de la naturaleza. La normativa

secundaria de calidad del aire aplicable al Proyecto se presenta en la Tabla 4-2.

**Tabla 4-2 Normativa secundaria de calidad del aire aplicable al Proyecto**

Fuente: Elaboración propia.

Página | 23

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**5.** **RESULTADOS DE LA MODELACIÓN**

A continuación, se presentan los resultados obtenidos al incorporar al modelo de dispersión las emisiones

generadas durante el primer año de la construcción del Proyecto.

**5.1.** **PUNTOS DE MÁXIMO IMPACTO**

Los puntos de máximo impacto (PMI) corresponden a aquellos receptores de la grilla del modelo en donde

las emisiones generadas durante la construcción del Proyecto, generan las máximas concentraciones de

los distintos contaminantes atmosféricos. Estas concentraciones pueden corresponder a promedios de

una hora, 8 horas, 24 horas o un año, de acuerdo a las diferentes normas de calidad existentes.

En la Tabla 5-1 se presentan los PMI del Proyecto para cada contaminante atmosférico de acuerdo a la

normativa de calidad del aire vigente. Como puede comprobarse, en ningún punto este aporte máximo

excede la norma. El contaminante para el que se obtiene la mayor concentración con respecto a la norma

es el NO 2 que alcanza el 42,7% del límite horario con 170,8 μg/Nmɜ.

En la Tabla 5-2 se muestran las coordenadas del punto de máximo impacto para cada norma. Los puntos

corresponden a los receptores sensibles R1 y R2, correspondiente a los edificios más cercanos al Proyecto.

Las ubicaciones de dichos puntos, relativa al Proyecto, se presenta la Figura 5-1.

**Tabla 5-1 Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1**

|Valor Norma Concentración Aporte respecto a<br>Norma de calidad del aire<br>(μg/Nmɜ) (μg/Nmɜ) norma %|Col2|Col3|Col4|
|---|---|---|---|
|MP10 24 horas Per98<br>150<br>8,3<br>5,5%|MP10 24 horas Per98<br>150<br>8,3<br>5,5%|MP10 24 horas Per98<br>150<br>8,3<br>5,5%|MP10 24 horas Per98<br>150<br>8,3<br>5,5%|
|MP10 Anual<br>50<br>2,7<br>5,4%|MP10 Anual<br>50<br>2,7<br>5,4%|MP10 Anual<br>50<br>2,7<br>5,4%|MP10 Anual<br>50<br>2,7<br>5,4%|
|MP2,5 24 horas Per98<br>50<br>6,9<br>13,8%|MP2,5 24 horas Per98<br>50<br>6,9<br>13,8%|MP2,5 24 horas Per98<br>50<br>6,9<br>13,8%|MP2,5 24 horas Per98<br>50<br>6,9<br>13,8%|
|MP2,5 Anual<br>20<br>2,2<br>11,0%|MP2,5 Anual<br>20<br>2,2<br>11,0%|MP2,5 Anual<br>20<br>2,2<br>11,0%|MP2,5 Anual<br>20<br>2,2<br>11,0%|
|NO2 1 hora Per99<br>400<br>170,8<br>42,7%|NO2 1 hora Per99<br>400<br>170,8<br>42,7%|NO2 1 hora Per99<br>400<br>170,8<br>42,7%|NO2 1 hora Per99<br>400<br>170,8<br>42,7%|
|NO2 Anual<br>100<br>19,0<br>19,0%|NO2 Anual<br>100<br>19,0<br>19,0%|NO2 Anual<br>100<br>19,0<br>19,0%|NO2 Anual<br>100<br>19,0<br>19,0%|
|CO 1 hora Per99<br>30.000<br>45,9<br>0,2%|CO 1 hora Per99<br>30.000<br>45,9<br>0,2%|CO 1 hora Per99<br>30.000<br>45,9<br>0,2%|CO 1 hora Per99<br>30.000<br>45,9<br>0,2%|
|CO 8 horas Per99<br>10.000<br>28,8<br>0,3%|CO 8 horas Per99<br>10.000<br>28,8<br>0,3%|CO 8 horas Per99<br>10.000<br>28,8<br>0,3%|CO 8 horas Per99<br>10.000<br>28,8<br>0,3%|
|SO2 1 hora Per98,5<br>350<br>7,0<br>2,0%|SO2 1 hora Per98,5<br>350<br>7,0<br>2,0%|SO2 1 hora Per98,5<br>350<br>7,0<br>2,0%|SO2 1 hora Per98,5<br>350<br>7,0<br>2,0%|
|SO2 24 horas Per99<br>150<br>3,0<br>2,0%|SO2 24 horas Per99<br>150<br>3,0<br>2,0%|SO2 24 horas Per99<br>150<br>3,0<br>2,0%|SO2 24 horas Per99<br>150<br>3,0<br>2,0%|
|SO2 Anual<br>60<br>0,8<br>1,4%|SO2 Anual<br>60<br>0,8<br>1,4%|SO2 Anual<br>60<br>0,8<br>1,4%|SO2 Anual<br>60<br>0,8<br>1,4%|
|SO2 1 hora Per99,7<br>1.000<br>9,8<br>1,0%|SO2 1 hora Per99,7<br>1.000<br>9,8<br>1,0%|SO2 1 hora Per99,7<br>1.000<br>9,8<br>1,0%|SO2 1 hora Per99,7<br>1.000<br>9,8<br>1,0%|
|SO2 24 horas Per99,7<br>365<br>3,1<br>0,9%|SO2 24 horas Per99,7<br>365<br>3,1<br>0,9%|SO2 24 horas Per99,7<br>365<br>3,1<br>0,9%|SO2 24 horas Per99,7<br>365<br>3,1<br>0,9%|
|SO2 Anual|80|0,8|1,1%|

Fuente: Elaboración propia.

Página | 24

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Tabla 5-2 Coordenadas de los Puntos de Máximo Impacto - Fase de construcción Año 1**

|Norma Receptor X (m) Y (m)|Col2|Col3|Col4|
|---|---|---|---|
|MP10 24 horas Per98<br>R2<br>262.146<br>6.351.100|MP10 24 horas Per98<br>R2<br>262.146<br>6.351.100|MP10 24 horas Per98<br>R2<br>262.146<br>6.351.100|MP10 24 horas Per98<br>R2<br>262.146<br>6.351.100|
|MP10 Anual<br>R2<br>262.146<br>6.351.100|MP10 Anual<br>R2<br>262.146<br>6.351.100|MP10 Anual<br>R2<br>262.146<br>6.351.100|MP10 Anual<br>R2<br>262.146<br>6.351.100|
|MP2,5 24 horas Per98<br>R2<br>262.146<br>6.351.100|MP2,5 24 horas Per98<br>R2<br>262.146<br>6.351.100|MP2,5 24 horas Per98<br>R2<br>262.146<br>6.351.100|MP2,5 24 horas Per98<br>R2<br>262.146<br>6.351.100|
|MP2,5 Anual<br>R2<br>262.146<br>6.351.100|MP2,5 Anual<br>R2<br>262.146<br>6.351.100|MP2,5 Anual<br>R2<br>262.146<br>6.351.100|MP2,5 Anual<br>R2<br>262.146<br>6.351.100|
|NO2 1 hora Per99<br>R2<br>262.146<br>6.351.100|NO2 1 hora Per99<br>R2<br>262.146<br>6.351.100|NO2 1 hora Per99<br>R2<br>262.146<br>6.351.100|NO2 1 hora Per99<br>R2<br>262.146<br>6.351.100|
|NO2 Anual<br>R2<br>262.146<br>6.351.100|NO2 Anual<br>R2<br>262.146<br>6.351.100|NO2 Anual<br>R2<br>262.146<br>6.351.100|NO2 Anual<br>R2<br>262.146<br>6.351.100|
|CO 1 hora Per99<br>R2<br>262.146<br>6.351.100|CO 1 hora Per99<br>R2<br>262.146<br>6.351.100|CO 1 hora Per99<br>R2<br>262.146<br>6.351.100|CO 1 hora Per99<br>R2<br>262.146<br>6.351.100|
|CO 8 horas Per99<br>R2<br>262.146<br>6.351.100|CO 8 horas Per99<br>R2<br>262.146<br>6.351.100|CO 8 horas Per99<br>R2<br>262.146<br>6.351.100|CO 8 horas Per99<br>R2<br>262.146<br>6.351.100|
|SO2 1 hora Per98,5<br>R2<br>262.146<br>6.351.100|SO2 1 hora Per98,5<br>R2<br>262.146<br>6.351.100|SO2 1 hora Per98,5<br>R2<br>262.146<br>6.351.100|SO2 1 hora Per98,5<br>R2<br>262.146<br>6.351.100|
|SO2 24 horas Per99<br>R2<br>262.146<br>6.351.100|SO2 24 horas Per99<br>R2<br>262.146<br>6.351.100|SO2 24 horas Per99<br>R2<br>262.146<br>6.351.100|SO2 24 horas Per99<br>R2<br>262.146<br>6.351.100|
|SO2 Anual<br>R2<br>262.146<br>6.351.100|SO2 Anual<br>R2<br>262.146<br>6.351.100|SO2 Anual<br>R2<br>262.146<br>6.351.100|SO2 Anual<br>R2<br>262.146<br>6.351.100|
|SO2 1 hora Per99,7<br>R1<br>262.128<br>6.351.174|SO2 1 hora Per99,7<br>R1<br>262.128<br>6.351.174|SO2 1 hora Per99,7<br>R1<br>262.128<br>6.351.174|SO2 1 hora Per99,7<br>R1<br>262.128<br>6.351.174|
|SO2 24 horas Per99,7<br>R2<br>262.146<br>6.351.100|SO2 24 horas Per99,7<br>R2<br>262.146<br>6.351.100|SO2 24 horas Per99,7<br>R2<br>262.146<br>6.351.100|SO2 24 horas Per99,7<br>R2<br>262.146<br>6.351.100|
|SO2 Anual|R2|262.146|6.351.100|

Fuente: Elaboración propia. DATUM 19 WGS84.

**Figura 5-1 Ubicación de los Puntos de Máximo Impacto - Fase de construcción Año 1.**

Fuente: Elaboración propia.

Página | 25

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**5.1.1** **Análisis Normativo**

Tal como se describe en la sección 2.2, los contaminantes monitoreados en la estación Junta de Vecinos

corresponden a MP10 y SO 2 . En la Tabla 5-3 se presenta el análisis normativo para MP10 y SO 2 efectuado

en los puntos de máximo impacto. Para realizar el análisis se ha considerado como representativa de todos

los receptores, la línea de base de calidad del aire registrada en dicha estación.

De acuerdo a las mediciones de MP10 registradas en la estación durante los años 2017, 2018 y 2019, la

concentración de 24 horas en el PMI alcanzaría un valor total de 72,3 μg/Nm3 correspondiente al 48% de

la norma diaria. En el caso de la concentración anual, ésta alcanzaría los 39,7 μg/Nm3 equivalentes al 79%

de la norma para dicho período.

En cuanto al de SO 2 registrado en la estación durante los años 2017, 2018 y 2019, la concentración horaria

total alcanzaría un valor de 40,0 μg/Nm3 equivalente al 11% del valor de dicha norma. Para la

concentración de 24 horas en el PMI alcanzaría un valor de 34,0 μg/Nm3 correspondiente al 23% de la

norma diaria. En el caso de la concentración anual, ésta alcanzaría los 9,8 μg/Nm3 equivalentes al 16% de

la norma para dicho período.

De esta forma, la construcción del Proyecto no representaría un riesgo para la salud de la población, dada

la magnitud de las emisiones de material particulado y dióxido de azufre.

**Tabla 5-3 Análisis normativo en Puntos de Máximo Impacto - Fase de construcción Año 1**

|Valor Norma Aporte proyecto Línea de Base Total % Respecto a<br>Norma<br>(μg/Nmɜ) en PMI (μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ) norma|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48%|MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48%|MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48%|MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48%|MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48%|MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48%|
|MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79%|MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79%|MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79%|MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79%|MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79%|MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79%|
|SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11%|SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11%|SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11%|SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11%|SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11%|SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11%|
|SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23%|SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23%|SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23%|SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23%|SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23%|SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23%|
|SO2 Anual|60|0,8|9|9,8|16%|

Fuente: Elaboración propia.

**5.2.** **RECEPTORES DISCRETOS**

En la Tabla 5-4 se presentan las concentraciones obtenidas en los 9 receptores discretos o de interés que

se han definido para el Proyecto (Tabla 3-4). En la Tabla 5-5 se comparan dichas concentraciones con los

<!-- INICIO TABLA 3-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto, tales como viviendas, colegios, centros de salud y áreas verdes. La ubicación de los receptores se presenta en la Figura 3-7. -->

**Tabla 3-4: Receptores discretos del modelo****

| Uso X Y Altura<br>ID Descripción<br>efectivo (m) (m) (m.s.n.m) | Col2 | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82 | R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82 | R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82 | R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82 | R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82 | R1<br>Edificio de 24 pisos ubicado en Avenida<br>Edmundo Eluchans 2475<br>Vivienda<br>262.128<br>6.351.174<br>82 |
| R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82 | R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82 | R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82 | R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82 | R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82 | R2<br>Edificio Grecomar de 18 pisos ubicado en<br>Avenida Edmundo Eluchans 2485<br>Vivienda<br>262.146<br>6.351.100<br>82 |
| R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82 | R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82 | R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82 | R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82 | R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82 | R3<br>Edificio Altomar de 14 pisos ubicado en<br>Avenida Edmundo Eluchans 2355<br>Vivienda<br>262.170<br>6.350.966<br>82 |
| R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79 | R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79 | R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79 | R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79 | R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79 | R4<br>Edificio Eluchans Plaza de 20 pisos ubicado<br>en Avenida Edmundo Eluchans 2066<br>Vivienda<br>262.199<br>6.350.697<br>79 |
| R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112 | R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112 | R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112 | R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112 | R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112 | R5<br>Edificio de 13 pisos ubicado en J. M. Escriba<br>de Balanguer 725<br>Vivienda<br>262.454<br>6.351.369<br>112 |
| R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104 | R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104 | R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104 | R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104 | R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104 | R6<br>Edificio Sports Medicina Deportiva ubicado<br>en Bosques de Montemar 65<br>Salud<br>262.321<br>6.351.374<br>104 |
| R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106 | R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106 | R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106 | R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106 | R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106 | R7<br>Colegio Alianza Francesa ubicado en Av.<br>Las Perdices 450<br>Educación<br>262.516<br>6.350.509<br>106 |
| R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103 | R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103 | R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103 | R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103 | R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103 | R8<br>Parque La Foresta<br>Recreación<br>263.378<br>6.351.017<br>103 |
| R9 | Colegio Sagrada Familia ubicado en Parcela<br>4, Los Pinos | Educación | 262.803 | 6.351.045 | 124 |

<!-- Estadísticas: 9 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. DATUM WGS84. Página | 18 -->
<!-- FIN TABLA 3-4 -->


límites establecidos en las normas de calidad de cada contaminante atmosférico. Tal como puede

observarse, el aporte del Proyecto es bajo en todos los receptores discretos alcanzando un máximo del

42,7% (170,8 μg/Nm3) de la norma primaria de NO 2 en concentración de 1 hora en el receptor R2

correspondiente al Edificio Grecomar ubicado al costado poniente del Proyecto.

Página | 26

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Tabla 5-4 Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1**

|Valor Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1<br>Norma norma (μg/Nmɜ)<br>(μg/Nmɜ) R1 R2 R3 R4 R5 R6 R7 R8 R9|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7|
|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2|
|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6|
|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1|
|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8|
|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|
|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2|
|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3|
|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5|
|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2|
|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0|
|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6|
|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2|
|SO2 Anual|60|0,7|0,8|0,7|0,2|0,1|0,1|0,03|0,3|0,05|

Fuente: Elaboración propia.

**Tabla 5-5 Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de construcción Año 1**

|Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de<br>Norma construcción Año 1<br>R1 R2 R3 R4 R5 R6 R7 R8 R9|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5|
|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3|
|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1|
|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7|
|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7|
|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0|
|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|
|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0|
|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1|
|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1|
|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1|
|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2|
|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1|
|SO2 Anual|0,9|1,1|0,9|0,3|0,1|0,1|0,0|0,4|0,1|

Página | 27

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

Fuente: Elaboración propia.

**5.2.1** **Análisis Normativo**

En la Tabla 5-6 y Tabla 5-8 se presenta el análisis normativo efectuado en los receptores discretos para los

contaminantes MP10 y SO 2, en donde se suma el aporte del Proyecto con la línea de base registrada en la

estación Junta de Vecinos. Para realizar el análisis se ha considerado como representativa de todos los

receptores, la línea de base de calidad del aire registrada en dicha estación de monitoreo (Tabla 2-4).

<!-- INICIO TABLA 2-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de la Calidad del Aire en la Región de Valparaíso. Período 2017-2019” elaborado en conjunto por la SEREMI Medio Ambiente y SEREMI Salud de la región de Valparaíso (2020). -->

**Tabla 2-4: Línea de base de calidad del aire trienio 2017 - 2019 en la estación Junta de Vecinos****

| Valor norma Concentración<br>Norma % Norma<br>(μg/Nmɜ) (μg/Nmɜ) | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| MP10 24 horas Percentil 98<br>150<br>64<br>43 | MP10 24 horas Percentil 98<br>150<br>64<br>43 | MP10 24 horas Percentil 98<br>150<br>64<br>43 | MP10 24 horas Percentil 98<br>150<br>64<br>43 |
| MP10 Anual<br>50<br>37<br>74 | MP10 Anual<br>50<br>37<br>74 | MP10 Anual<br>50<br>37<br>74 | MP10 Anual<br>50<br>37<br>74 |
| SO2 1 hora Percentil 98,5<br>350<br>33<br>9 | SO2 1 hora Percentil 98,5<br>350<br>33<br>9 | SO2 1 hora Percentil 98,5<br>350<br>33<br>9 | SO2 1 hora Percentil 98,5<br>350<br>33<br>9 |
| SO2 24 horas Percentil 99<br>150<br>31<br>21 | SO2 24 horas Percentil 99<br>150<br>31<br>21 | SO2 24 horas Percentil 99<br>150<br>31<br>21 | SO2 24 horas Percentil 99<br>150<br>31<br>21 |
| SO2 Anual | 60 | 9 | 14 |

<!-- Estadísticas: 5 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Tabla 6.1 Concentraciones Trianuales Período 2017-2019, Informe “Línea de Base de la Calidad del Aire en la Región de Valparaíso. Período 2017-2019”. SEREMI Medio Ambiente y SEREMI Salud región de Valparaíso, 2020. -->
<!-- FIN TABLA 2-4 -->


Dado que las normas de calidad para estos contaminantes no se sobrepasan en ningún receptor discreto,

las emisiones producidas en el primer año de la fase de construcción del Proyecto no pondrán en riesgo la

salud de la población ni los recursos naturales asociada a dichos receptores.

Cabe destacar que, dada la magnitud del aporte del Proyecto, las concentraciones finales obtenidas en los

receptores discretos no representan cambios significativos con respecto a las concentraciones basales

medidas en la estación Junta de Vecinos.

**Tabla 5-6 Análisis normativo en receptores discretos - Concentración diaria MP10**

|MP10 24 horas Percentil 98<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ)|Col2|Col3|Col4|
|---|---|---|---|
|R1<br>8,1<br>64,0<br>72,1<br>48%<br>R2<br>8,3<br>72,3<br>48%<br>R3<br>7,2<br>71,2<br>47%<br>R4<br>3,0<br>67,0<br>45%<br>R5<br>1,0<br>65,0<br>43%<br>R6<br>1,2<br>65,2<br>43%<br>R7<br>0,6<br>64,6<br>43%<br>R8<br>3,4<br>67,4<br>45%<br>R9<br>0,7<br>64,7<br>43%|R1<br>8,1<br>64,0<br>72,1<br>48%<br>R2<br>8,3<br>72,3<br>48%<br>R3<br>7,2<br>71,2<br>47%<br>R4<br>3,0<br>67,0<br>45%<br>R5<br>1,0<br>65,0<br>43%<br>R6<br>1,2<br>65,2<br>43%<br>R7<br>0,6<br>64,6<br>43%<br>R8<br>3,4<br>67,4<br>45%<br>R9<br>0,7<br>64,7<br>43%|R1<br>8,1<br>64,0<br>72,1<br>48%<br>R2<br>8,3<br>72,3<br>48%<br>R3<br>7,2<br>71,2<br>47%<br>R4<br>3,0<br>67,0<br>45%<br>R5<br>1,0<br>65,0<br>43%<br>R6<br>1,2<br>65,2<br>43%<br>R7<br>0,6<br>64,6<br>43%<br>R8<br>3,4<br>67,4<br>45%<br>R9<br>0,7<br>64,7<br>43%|R1<br>8,1<br>64,0<br>72,1<br>48%<br>R2<br>8,3<br>72,3<br>48%<br>R3<br>7,2<br>71,2<br>47%<br>R4<br>3,0<br>67,0<br>45%<br>R5<br>1,0<br>65,0<br>43%<br>R6<br>1,2<br>65,2<br>43%<br>R7<br>0,6<br>64,6<br>43%<br>R8<br>3,4<br>67,4<br>45%<br>R9<br>0,7<br>64,7<br>43%|
|R9|0,7|64,7|43%|

Fuente: Elaboración propia.

Página | 28

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Tabla 5-7 Análisis normativo en receptores discretos - Concentración anual MP10**

|MP10 anual<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ)|Col2|Col3|Col4|
|---|---|---|---|
|R1<br>2,3<br>37,0<br>39,3<br>79%<br>R2<br>2,7<br>39,7<br>79%<br>R3<br>2,4<br>39,4<br>79%<br>R4<br>0,8<br>37,8<br>76%<br>R5<br>0,3<br>37,3<br>75%<br>R6<br>0,3<br>37,3<br>75%<br>R7<br>0,1<br>37,1<br>74%<br>R8<br>0,9<br>37,9<br>76%<br>R9<br>0,2<br>37,2<br>74%|R1<br>2,3<br>37,0<br>39,3<br>79%<br>R2<br>2,7<br>39,7<br>79%<br>R3<br>2,4<br>39,4<br>79%<br>R4<br>0,8<br>37,8<br>76%<br>R5<br>0,3<br>37,3<br>75%<br>R6<br>0,3<br>37,3<br>75%<br>R7<br>0,1<br>37,1<br>74%<br>R8<br>0,9<br>37,9<br>76%<br>R9<br>0,2<br>37,2<br>74%|R1<br>2,3<br>37,0<br>39,3<br>79%<br>R2<br>2,7<br>39,7<br>79%<br>R3<br>2,4<br>39,4<br>79%<br>R4<br>0,8<br>37,8<br>76%<br>R5<br>0,3<br>37,3<br>75%<br>R6<br>0,3<br>37,3<br>75%<br>R7<br>0,1<br>37,1<br>74%<br>R8<br>0,9<br>37,9<br>76%<br>R9<br>0,2<br>37,2<br>74%|R1<br>2,3<br>37,0<br>39,3<br>79%<br>R2<br>2,7<br>39,7<br>79%<br>R3<br>2,4<br>39,4<br>79%<br>R4<br>0,8<br>37,8<br>76%<br>R5<br>0,3<br>37,3<br>75%<br>R6<br>0,3<br>37,3<br>75%<br>R7<br>0,1<br>37,1<br>74%<br>R8<br>0,9<br>37,9<br>76%<br>R9<br>0,2<br>37,2<br>74%|
|R9|0,2|37,2|74%|

Fuente: Elaboración propia.

**Tabla 5-8 Análisis normativo en receptores discretos - Concentración horaria SO** **2**

|SO 1 hora Percentil 98,5<br>2<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ)|Col2|Col3|Col4|
|---|---|---|---|
|R1<br>6,0<br>33,0<br>39,0<br>11%<br>R2<br>7,0<br>40,0<br>11%<br>R3<br>6,6<br>39,6<br>11%<br>R4<br>3,2<br>36,2<br>10%<br>R5<br>1,0<br>34,0<br>10%<br>R6<br>1,2<br>34,2<br>10%<br>R7<br>0,4<br>33,4<br>10%<br>R8<br>3,6<br>36,6<br>10%<br>R9<br>0,5<br>33,5<br>10%|R1<br>6,0<br>33,0<br>39,0<br>11%<br>R2<br>7,0<br>40,0<br>11%<br>R3<br>6,6<br>39,6<br>11%<br>R4<br>3,2<br>36,2<br>10%<br>R5<br>1,0<br>34,0<br>10%<br>R6<br>1,2<br>34,2<br>10%<br>R7<br>0,4<br>33,4<br>10%<br>R8<br>3,6<br>36,6<br>10%<br>R9<br>0,5<br>33,5<br>10%|R1<br>6,0<br>33,0<br>39,0<br>11%<br>R2<br>7,0<br>40,0<br>11%<br>R3<br>6,6<br>39,6<br>11%<br>R4<br>3,2<br>36,2<br>10%<br>R5<br>1,0<br>34,0<br>10%<br>R6<br>1,2<br>34,2<br>10%<br>R7<br>0,4<br>33,4<br>10%<br>R8<br>3,6<br>36,6<br>10%<br>R9<br>0,5<br>33,5<br>10%|R1<br>6,0<br>33,0<br>39,0<br>11%<br>R2<br>7,0<br>40,0<br>11%<br>R3<br>6,6<br>39,6<br>11%<br>R4<br>3,2<br>36,2<br>10%<br>R5<br>1,0<br>34,0<br>10%<br>R6<br>1,2<br>34,2<br>10%<br>R7<br>0,4<br>33,4<br>10%<br>R8<br>3,6<br>36,6<br>10%<br>R9<br>0,5<br>33,5<br>10%|
|R9|0,5|33,5|10%|

Fuente: Elaboración propia.

Página | 29

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Tabla 5-9 Análisis normativo en receptores discretos - Concentración diaria SO** **2**

|SO 24 horas Percentil 99<br>2<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ)|Col2|Col3|Col4|
|---|---|---|---|
|<br>2,8<br>31,0<br>33,8<br>23%<br> <br>3,0<br>34,0<br>23%<br> <br>2,5<br>33,5<br>22%<br> <br>0,9<br>31,9<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,2<br>31,2<br>21%<br> <br>1,1<br>32,1<br>21%<br> <br>0,2<br>31,2<br>21%|<br>2,8<br>31,0<br>33,8<br>23%<br> <br>3,0<br>34,0<br>23%<br> <br>2,5<br>33,5<br>22%<br> <br>0,9<br>31,9<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,2<br>31,2<br>21%<br> <br>1,1<br>32,1<br>21%<br> <br>0,2<br>31,2<br>21%|<br>2,8<br>31,0<br>33,8<br>23%<br> <br>3,0<br>34,0<br>23%<br> <br>2,5<br>33,5<br>22%<br> <br>0,9<br>31,9<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,2<br>31,2<br>21%<br> <br>1,1<br>32,1<br>21%<br> <br>0,2<br>31,2<br>21%|<br>2,8<br>31,0<br>33,8<br>23%<br> <br>3,0<br>34,0<br>23%<br> <br>2,5<br>33,5<br>22%<br> <br>0,9<br>31,9<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,2<br>31,2<br>21%<br> <br>1,1<br>32,1<br>21%<br> <br>0,2<br>31,2<br>21%|
||0,2|31,2|21%|

Fuente: Elaboración propia.

**Tabla 5-10 Análisis normativo en receptores discretos - Concentración anual SO** **2**

|SO Anual<br>2<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ)|Col2|Col3|Col4|
|---|---|---|---|
|R1<br>0,7<br>9,0<br>9,7<br>2%<br>R2<br>0,8<br>9,8<br>2%<br>R3<br>0,7<br>9,7<br>2%<br>R4<br>0,2<br>9,2<br>2%<br>R5<br>0,1<br>9,1<br>2%<br>R6<br>0,1<br>9,1<br>2%<br>R7<br>0,03<br>9,0<br>2%<br>R8<br>0,3<br>9,3<br>2%<br>R9<br>0,05<br>9,0<br>2%|R1<br>0,7<br>9,0<br>9,7<br>2%<br>R2<br>0,8<br>9,8<br>2%<br>R3<br>0,7<br>9,7<br>2%<br>R4<br>0,2<br>9,2<br>2%<br>R5<br>0,1<br>9,1<br>2%<br>R6<br>0,1<br>9,1<br>2%<br>R7<br>0,03<br>9,0<br>2%<br>R8<br>0,3<br>9,3<br>2%<br>R9<br>0,05<br>9,0<br>2%|R1<br>0,7<br>9,0<br>9,7<br>2%<br>R2<br>0,8<br>9,8<br>2%<br>R3<br>0,7<br>9,7<br>2%<br>R4<br>0,2<br>9,2<br>2%<br>R5<br>0,1<br>9,1<br>2%<br>R6<br>0,1<br>9,1<br>2%<br>R7<br>0,03<br>9,0<br>2%<br>R8<br>0,3<br>9,3<br>2%<br>R9<br>0,05<br>9,0<br>2%|R1<br>0,7<br>9,0<br>9,7<br>2%<br>R2<br>0,8<br>9,8<br>2%<br>R3<br>0,7<br>9,7<br>2%<br>R4<br>0,2<br>9,2<br>2%<br>R5<br>0,1<br>9,1<br>2%<br>R6<br>0,1<br>9,1<br>2%<br>R7<br>0,03<br>9,0<br>2%<br>R8<br>0,3<br>9,3<br>2%<br>R9<br>0,05<br>9,0<br>2%|
|R9|0,05|9,0|2%|

Fuente: Elaboración propia.

**5.3.** **Curvas de Isoconcentración - Fase de Construcción**

En las siguientes figuras se presentan las curvas de isoconcentración obtenidas para los contaminantes

atmosféricos modelados para la fase de construcción del Proyecto. En todas las figuras se puede observar

que el impacto sobre la calidad del aire se acota al área circundante al Proyecto debido, principalmente, a

la baja magnitud de las emisiones.

Página | 30

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-2 Curvas de Isoconcentración - MP10 24 horas Percentil 98**

Fuente: Elaboración propia.

Página | 31

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-3 Curvas de Isoconcentración - MP10 concentración anual**

Fuente: Elaboración propia.

Página | 32

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-4 Curvas de Isoconcentración - MP2,5 24 horas Percentil 98**

Fuente: Elaboración propia.

Página | 33

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-5 Curvas de Isoconcentración - MP2,5 Anual**

Fuente: Elaboración propia.

Página | 34

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-6 Curvas de Isoconcentración - NO** **2** **1 hora Percentil 99**

Fuente: Elaboración propia.

Página | 35

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-7 Curvas de Isoconcentración - NO** **2** **Anual**

Fuente: Elaboración propia.

Página | 36

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-8 Curvas de Isoconcentración - SO** **2** **1 hora Percentil 98,5**

Fuente: Elaboración propia.

Página | 37

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-9 Curvas de Isoconcentración - SO** **2** **24 horas Percentil 99**

Fuente: Elaboración propia.

Página | 38

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 5-10 Curvas de Isoconcentración - SO** **2** **concentración anual**

Fuente: Elaboración propia.

Página | 39

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**5.4.** **MATERIAL PARTICULADO SEDIMENTABLE**

En el caso del material particulado sedimentable generado en la fase de construcción, se obtiene que en

el punto de máximo impacto el promedio anual alcanza un valor de 0,0026 μg/m [2] - s, equivalente a 0,23

mg/m [2] - d.

Siendo la norma anual de 100 mg/m [2] - d según el Decreto Exento N° 4/1992 del Ministerio de Agricultura

que establece la Norma de calidad del aire para MPS en la cuenca del río Huasco, III Región, el aporte del

Proyecto es bajo (0,2% de la norma) por lo que no generaría un impacto significativo sobre los recursos

naturales que se encuentren dentro del área de influencia del Proyecto. Las curvas de isodeposición anual

de MPS se presentan en la Figura 5-11.

**Figura 5-11 Curvas de isodeposición MPS anual - Fase de Construcción.**

Fuente: Elaboración propia.

Página | 40

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**6.** **ÁREA DE INFLUENCIA**

De manera preliminar, y con el fin de mostrar el área en la que el Proyecto genera un mayor impacto, se

ha definido como área de influencia aquella superficie en que el aporte del Proyecto, para un

contaminante determinado, presenta concentraciones superiores al 1% de la norma. Las concentraciones

equivalentes al 1% de cada norma se presentan en la Tabla 6-1. En el caso del CO y el SO 2 secundario, el

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Figura 6-10, correspondiente al área de influencia del NO 2 concentración 1 hora, dado que es la curva que involucra una mayor superficie (5,9 km [2] ) y permite establecer el escenario más conservador. -->

**Tabla 6-1: Concentración equivalente al 1% de la norma****

| Valor Norma<br>Contaminante Norma 1% de la norma (μg/Nmɜ)<br>(μg/Nmɜ) | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| MP10<br>24 horas Percentil 98<br>150<br>1,5<br>Anual<br>50<br>0,5 | MP10<br>24 horas Percentil 98<br>150<br>1,5<br>Anual<br>50<br>0,5 | MP10<br>24 horas Percentil 98<br>150<br>1,5<br>Anual<br>50<br>0,5 | MP10<br>24 horas Percentil 98<br>150<br>1,5<br>Anual<br>50<br>0,5 |
| MP2,5<br>24 horas Percentil 98<br>50<br>0,5<br>Anual<br>20<br>0,2 | MP2,5<br>24 horas Percentil 98<br>50<br>0,5<br>Anual<br>20<br>0,2 | MP2,5<br>24 horas Percentil 98<br>50<br>0,5<br>Anual<br>20<br>0,2 | MP2,5<br>24 horas Percentil 98<br>50<br>0,5<br>Anual<br>20<br>0,2 |
| NO2 <br>1 hora Percentil 99<br>400<br>4,0<br>Anual<br>100<br>1,0 | NO2 <br>1 hora Percentil 99<br>400<br>4,0<br>Anual<br>100<br>1,0 | NO2 <br>1 hora Percentil 99<br>400<br>4,0<br>Anual<br>100<br>1,0 | NO2 <br>1 hora Percentil 99<br>400<br>4,0<br>Anual<br>100<br>1,0 |
| CO<br>1 hora Percentil 99<br>30.000<br>300,0<br>8 horas Percentil 99<br>10.000<br>100,0 | CO<br>1 hora Percentil 99<br>30.000<br>300,0<br>8 horas Percentil 99<br>10.000<br>100,0 | CO<br>1 hora Percentil 99<br>30.000<br>300,0<br>8 horas Percentil 99<br>10.000<br>100,0 | CO<br>1 hora Percentil 99<br>30.000<br>300,0<br>8 horas Percentil 99<br>10.000<br>100,0 |
| SO2 <br>1 hora Percentil 98,5<br>350<br>3,5<br>24 horas Percentil 99<br>150<br>1,5<br>Anual<br>60<br>0,6 | SO2 <br>1 hora Percentil 98,5<br>350<br>3,5<br>24 horas Percentil 99<br>150<br>1,5<br>Anual<br>60<br>0,6 | SO2 <br>1 hora Percentil 98,5<br>350<br>3,5<br>24 horas Percentil 99<br>150<br>1,5<br>Anual<br>60<br>0,6 | SO2 <br>1 hora Percentil 98,5<br>350<br>3,5<br>24 horas Percentil 99<br>150<br>1,5<br>Anual<br>60<br>0,6 |
| SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8 | SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8 | SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8 | SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8 |
| SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8 | Anual | 80 | 0,8 |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Página | 41 -->
<!-- FIN TABLA 6-1 -->


aporte es tan bajo que en ningún punto del dominio de modelación la concentración alcanza el 1% de las

respectivas normas. Las áreas de influencia obtenidas se presentan desde la Figura 6-1 a la Figura 6-9.

Finalmente, se define como área de influencia del Proyecto para la componente aire, la presentada en la

Figura 6-10, correspondiente al área de influencia del NO 2 concentración 1 hora, dado que es la curva que

involucra una mayor superficie (5,9 km [2] ) y permite establecer el escenario más conservador.

**Tabla 6-1 Concentración equivalente al 1% de la norma**

|Valor Norma<br>Contaminante Norma 1% de la norma (μg/Nmɜ)<br>(μg/Nmɜ)|Col2|Col3|Col4|
|---|---|---|---|
|MP10<br>24 horas Percentil 98<br>150<br>1,5<br>Anual<br>50<br>0,5|MP10<br>24 horas Percentil 98<br>150<br>1,5<br>Anual<br>50<br>0,5|MP10<br>24 horas Percentil 98<br>150<br>1,5<br>Anual<br>50<br>0,5|MP10<br>24 horas Percentil 98<br>150<br>1,5<br>Anual<br>50<br>0,5|
|MP2,5<br>24 horas Percentil 98<br>50<br>0,5<br>Anual<br>20<br>0,2|MP2,5<br>24 horas Percentil 98<br>50<br>0,5<br>Anual<br>20<br>0,2|MP2,5<br>24 horas Percentil 98<br>50<br>0,5<br>Anual<br>20<br>0,2|MP2,5<br>24 horas Percentil 98<br>50<br>0,5<br>Anual<br>20<br>0,2|
|NO2 <br>1 hora Percentil 99<br>400<br>4,0<br>Anual<br>100<br>1,0|NO2 <br>1 hora Percentil 99<br>400<br>4,0<br>Anual<br>100<br>1,0|NO2 <br>1 hora Percentil 99<br>400<br>4,0<br>Anual<br>100<br>1,0|NO2 <br>1 hora Percentil 99<br>400<br>4,0<br>Anual<br>100<br>1,0|
|CO<br>1 hora Percentil 99<br>30.000<br>300,0<br>8 horas Percentil 99<br>10.000<br>100,0|CO<br>1 hora Percentil 99<br>30.000<br>300,0<br>8 horas Percentil 99<br>10.000<br>100,0|CO<br>1 hora Percentil 99<br>30.000<br>300,0<br>8 horas Percentil 99<br>10.000<br>100,0|CO<br>1 hora Percentil 99<br>30.000<br>300,0<br>8 horas Percentil 99<br>10.000<br>100,0|
|SO2 <br>1 hora Percentil 98,5<br>350<br>3,5<br>24 horas Percentil 99<br>150<br>1,5<br>Anual<br>60<br>0,6|SO2 <br>1 hora Percentil 98,5<br>350<br>3,5<br>24 horas Percentil 99<br>150<br>1,5<br>Anual<br>60<br>0,6|SO2 <br>1 hora Percentil 98,5<br>350<br>3,5<br>24 horas Percentil 99<br>150<br>1,5<br>Anual<br>60<br>0,6|SO2 <br>1 hora Percentil 98,5<br>350<br>3,5<br>24 horas Percentil 99<br>150<br>1,5<br>Anual<br>60<br>0,6|
|SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8|SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8|SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8|SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8|
|SO2 <br>1 hora Percentil 99,73<br>1.000<br>10<br>24 horas Percentil 99,7<br>365<br>3,65<br>Anual<br>80<br>0,8|Anual|80|0,8|

Fuente: Elaboración propia.

Página | 41

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 6-1 Área de influencia - Concentración MP10 24 horas Percentil 98.**

Fuente: Elaboración propia.

**Figura 6-2 Área de influencia - Concentración MP10 Anual.**

Fuente: Elaboración propia.

Página | 42

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 6-3 Área de influencia - Concentración MP2,5 24 horas Percentil 98**

Fuente: Elaboración propia.

**Figura 6-4 Área de influencia - Concentración MP2,5 Anual.**

Fuente: Elaboración propia.

Página | 43

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 6-5 Área de influencia - Concentración NO** **2** **1 hora Percentil 99.**

Fuente: Elaboración propia.

**Figura 6-6 Área de influencia - Concentración NO** **2** **Anual**

Fuente: Elaboración propia.

Página | 44

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 6-7 Área de influencia - Concentración SO** **2** **1 hora Percentil 98,5**

Fuente: Elaboración propia.

**Figura 6-8 Área de influencia - Concentración SO** **2** **24 horas Percentil 99**

Fuente: Elaboración propia.

Página | 45

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**Figura 6-9 Área de influencia - Concentración SO** **2** **Anual**

Fuente: Elaboración propia.

**Figura 6-10 Área de influencia del Proyecto para la componente aire**

Fuente: Elaboración propia.

Página | 46

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**7.** **CONCLUSIONES**

La caracterización meteorológica del área en donde se emplazará del Proyecto, elaborada mediante los

registros efectuados en la estación Junta de Vecinos, permite determinar que la velocidad del viento

presenta un promedio de 1,5 m/s, con mínimos de 0,9 m/s durante la noche y máximos de 2,5 m/s durante

la tarde. La dirección predominante del viento durante el día es noroeste y durante el período nocturno

es sur.

La modelación de la dispersión de contaminantes atmosféricos utilizó la información meteorológica

contenida en el modelo WRF (WeatherResearch and Forecasting Model) descrito en la Sección 4.2. En el

análisis de incertidumbre del modelo, efectuado para un punto del dominio (correspondiente a la estación

Junta de Vecinos), se obtiene una diferencia entre la intensidad del viento modelada y la medida. Es

preciso subrayar que esta diferencia se obtiene sólo a nivel de superficie, dado que tanto en Reñaca como

en gran parte del territorio nacional, no existen mediciones de meteorología de altura, por lo que no es

posible establecer una comparación completa y adecuada para esta variable. No obstante, el modelo

meteorológico WRF utilizado en la modelación de calidad del aire del presente Proyecto fue elaborado

tomando en cuenta todas las indicaciones presentadas por la Autoridad Ambiental en la “Guía para el uso

de modelos de calidad del aire en el SEA”, constituyendo la mejor herramienta disponible para incorporar

información meteorológica al sistema de modelación de dispersión de contaminantes atmosféricos.

Además, la estimación de emisiones y el modelo de calidad del aire se construyeron, ambos, de manera

de representar, simular y evaluar el peor escenario posible de emisiones atmosféricas con el fin de obtener

resultados conservadores.

El modelo de calidad del aire desarrollado para evaluar el impacto del proyecto DIA “Portal La Foresta”

considera las emisiones que se generarán durante el primer año de su construcción, dado que corresponde

a la etapa del Proyecto en donde se produce el escenario más desfavorable desde el punto de vista de la

calidad del aire. Las emisiones atmosféricas obtenidas para el Año 1 de la fase de construcción y cuya

dispersión se describe en el presente documento, se resumen a continuación:

 - 14,5 toneladas de MPS

 - 4,3 toneladas de MP10,

 - 1,6 toneladas de MP2,5,

 - 3,1 toneladas de CO,

 - 12,2 toneladas de NO 2, y

 - 0,5 toneladas de SO 2 .

El análisis de los resultados de la modelación, indica que las concentraciones proyectadas para el área

donde se emplazará el Proyecto cumplen con toda la normativa primaria y secundaria de calidad del aire

vigente en el territorio nacional (Decretos del MINSEGPRES: D.S. N°114/02 para NO 2, D.S. N° 20/13 para

MP10 y D.S. N°115/02 para CO, D.S. N° 12/11, D.S. N°104/2018 para SO 2 D.E. N°4/92 del Ministerio de

Página | 47

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

Agricultura para MPS), tanto en los receptores (discretos y adyacentes) como en los puntos de máximo

impacto, para los cinco contaminantes analizados.

Expuesto lo anterior, y tomando en cuenta que las actividades de construcción son transitorias, se puede

concluir que el desarrollo del proyecto DIA “Portal La Foresta” no afectará la salud de la población ni los

recursos naturales que se encuentran dentro del área de influencia definida para esta componente

ambiental, dado que no se sobrepasa ninguna de las normas vigentes de calidad del aire aplicables al

Proyecto.

Kisi Valeska Cerda Palma

Ingeniero Civil Ambiental

Página | 48

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**8.** **BIBLIOGRAFÍA**

_Guía para el uso de modelos de calidad del aire en el SEIA_ . Servicio de Evaluación Ambiental. Ministerio de

Medio Ambiente, 2012.

_Informe Línea de Base de Calidad del Aire en la Región de Valparaíso. Periodo 2017-2019_ . SEREMI de Medio

Ambiente de la Región de Valparaíso, 2020.

Página | 49

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL PORTAL LA FORESTA

_____________________________________________________________________________________________________________________

**9.** **ANEXO C ARCHIVOS DE ENTRADA Y SALIDA DEL MODELO (DIGITAL)**

Página | 50

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-2: Validez de registros meteorológicos - Año 2020.****

| Variable N° Registros Válidos % Registros Válidos | Col2 | Col3 |
| --- | --- | --- |
| Velocidad del Viento<br>8.769<br>99,87% | Velocidad del Viento<br>8.769<br>99,87% | Velocidad del Viento<br>8.769<br>99,87% |
| Dirección del Viento | 8.769 | 99,87% |

**Tabla 2-3: Distribución de frecuencias (%) - Estación Junta de Vecinos 2020****

| Rango de Velocidad (m/s)<br>Dirección del Viento<br>0,5 - 2,1 2,1 - 3,6 3,6 - 5,7 5,7 - 8,8 8,8 - 11,1 >= 11,10 Total (%) | Col2 |
| --- | --- |
| N <br>4,6<br>1,2<br>0,3<br>0,0<br>0,0<br>0,0<br>6,0 | N <br>4,6<br>1,2<br>0,3<br>0,0<br>0,0<br>0,0<br>6,0 |
| NNE<br>3,8<br>0,7<br>0,0<br>0,0<br>0,0<br>0,0<br>4,5 | NNE<br>3,8<br>0,7<br>0,0<br>0,0<br>0,0<br>0,0<br>4,5 |
| NE<br>1,7<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>1,7 | NE<br>1,7<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>1,7 |
| ENE<br>1,1<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>1,1 | ENE<br>1,1<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>1,1 |
| E <br>3,8<br>0,1<br>0,0<br>0,0<br>0,0<br>0,0<br>3,9 | E <br>3,8<br>0,1<br>0,0<br>0,0<br>0,0<br>0,0<br>3,9 |
| ESE<br>5,0<br>0,4<br>0,0<br>0,0<br>0,0<br>0,0<br>5,4 | ESE<br>5,0<br>0,4<br>0,0<br>0,0<br>0,0<br>0,0<br>5,4 |
| SE<br>6,2<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>6,2 | SE<br>6,2<br>0,0<br>0,0<br>0,0<br>0,0<br>0,0<br>6,2 |
| SSE<br>4,6<br>0,4<br>0,0<br>0,0<br>0,0<br>0,0<br>4,9 | SSE<br>4,6<br>0,4<br>0,0<br>0,0<br>0,0<br>0,0<br>4,9 |
| S <br>7,3<br>0,8<br>0,5<br>0,0<br>0,0<br>0,0<br>8,6 | S <br>7,3<br>0,8<br>0,5<br>0,0<br>0,0<br>0,0<br>8,6 |
| SSW<br>2,0<br>0,6<br>0,2<br>0,0<br>0,0<br>0,0<br>2,7 | SSW<br>2,0<br>0,6<br>0,2<br>0,0<br>0,0<br>0,0<br>2,7 |
| SW<br>2,1<br>3,4<br>0,8<br>0,0<br>0,0<br>0,0<br>6,3 | SW<br>2,1<br>3,4<br>0,8<br>0,0<br>0,0<br>0,0<br>6,3 |
| WSW<br>2,7<br>2,6<br>0,0<br>0,0<br>0,0<br>0,0<br>5,4 | WSW<br>2,7<br>2,6<br>0,0<br>0,0<br>0,0<br>0,0<br>5,4 |
| W <br>3,4<br>2,8<br>0,0<br>0,0<br>0,0<br>0,0<br>6,2 | W <br>3,4<br>2,8<br>0,0<br>0,0<br>0,0<br>0,0<br>6,2 |
| WNW<br>3,2<br>2,4<br>0,0<br>0,0<br>0,0<br>0,0<br>5,6 | WNW<br>3,2<br>2,4<br>0,0<br>0,0<br>0,0<br>0,0<br>5,6 |
| NW<br>7,0<br>5,1<br>0,3<br>0,0<br>0,0<br>0,0<br>12,4 | NW<br>7,0<br>5,1<br>0,3<br>0,0<br>0,0<br>0,0<br>12,4 |
| NNW<br>6,1<br>1,5<br>0,4<br>0,0<br>0,0<br>0,0<br>8,0 | NNW<br>6,1<br>1,5<br>0,4<br>0,0<br>0,0<br>0,0<br>8,0 |
| Sub-Total<br>64,6<br>21,8<br>2,6<br>0,0<br>0,0<br>0,0<br>89,0 | Sub-Total<br>64,6<br>21,8<br>2,6<br>0,0<br>0,0<br>0,0<br>89,0 |
| Calmas (%)<br>10,8 | Calmas (%)<br>10,8 |
| Sin dato (%)<br>0,2 | Sin dato (%)<br>0,2 |
| Total (%) | 100 |

**Tabla 3-2: Error Cuadrático Medio, Sesgo y Coeficiente de Correlación del ciclo diario de Velocidad del Viento.****

| Estadístico Valor | Col2 |
| --- | --- |
| Error cuadrático Medio (m/s)<br>0,42 | Error cuadrático Medio (m/s)<br>0,42 |
| Sesgo (m/s)<br>0,40 | Sesgo (m/s)<br>0,40 |
| Coeficiente de Correlación | 0,99 |

**Tabla 3-5: Emisiones totales de contaminantes atmosféricos - Año 1 Fase de construcción****

| Emisiones - Fase de construcción (kg)<br>Actividad<br>MPS MP10 MP2,5 CO NOx SOx COV/HC | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br> | Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br> | Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br> | Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br> | Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br> | Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br> | Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br> | Escarpe<br>13,4<br>13,4<br>13,4<br> <br> <br> <br> |
| Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br> | Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br> | Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br> | Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br> | Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br> | Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br> | Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br> | Excavaciones<br>2.381,8<br>378,8<br>250,1<br> <br> <br> <br> |
| Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br> | Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br> | Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br> | Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br> | Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br> | Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br> | Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br> | Transferencia de Material<br>78,7<br>37,2<br>5,6<br> <br> <br> <br> |
| Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br> | Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br> | Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br> | Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br> | Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br> | Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br> | Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br> | Resuspensión en caminos<br>pavimentados<br>5.599,5<br>1.074,8<br>260,0<br> <br> <br> <br> |
| Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br> | Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br> | Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br> | Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br> | Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br> | Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br> | Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br> | Resuspensión en caminos internos no<br>pavimentados<br>418,1<br>98,3<br>9,8<br> <br> <br> <br> |
| Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br> | Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br> | Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br> | Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br> | Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br> | Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br> | Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br> | Resuspensión en caminos públicos no<br>pavimentados<br>5.126,9<br>1.836,9<br>183,7<br> <br> <br> <br> |
| Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6 | Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6 | Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6 | Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6 | Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6 | Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6 | Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6 | Combustión de motores de vehículos<br>- Caminos pavimentados<br>33,4<br>33,4<br>33,4<br>388,5<br>1.676,2<br>42,5<br>70,6 |
| Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0 | Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0 | Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0 | Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0 | Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0 | Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0 | Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0 | Combustión de motores de vehículos<br>- Caminos no pavimentados públicos<br>4,2<br>4,2<br>4,2<br>45,2<br>171,4<br>4,4<br>10,0 |
| Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5 | Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5 | Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5 | Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5 | Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5 | Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5 | Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5 | Combustión de motores de vehículos<br>- Caminos no pavimentados internos<br>0,2<br>0,2<br>0,2<br>2,2<br>8,5<br>0,2<br>0,5 |
| Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0 | Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0 | Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0 | Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0 | Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0 | Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0 | Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0 | Combustión maquinaria fuera de ruta<br>378,8<br>378,8<br>378,8<br>1.240,3<br>3.818,6<br>11,1<br>570,0 |
| Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br> | Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br> | Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br> | Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br> | Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br> | Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br> | Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br> | Grupos electrógenos<br>482,4<br>482,4<br>482,4<br>1.461,6<br>6.480,0<br>450,0<br> |
| **Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651** | **Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651** | **Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651** | **Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651** | **Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651** | **Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651** | **Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651** | **Total (kg/año)**<br>**14.517**<br>**4.338**<br>**1.622**<br>**3.138**<br>**12.155**<br>**508**<br>**651** |
| **Total (ton/año)** | **14,5** | **4,3** | **1,6** | **3,1** | **12,2** | **0,5** | **0,7** |

**Tabla 3-6: Superficie y emisiones agrupadas por fuente****

| Área fuente en el Emisiones - Fase de construcción Año 1 (kg/año)<br>Fuente<br>modelo (m2) MPS MP10 MP2,5 CO NOx SOx | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461 | Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461 | Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461 | Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461 | Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461 | Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461 | Proyecto<br>6.564<br>3.753<br>1.389<br>1.140<br>2.704<br>10.307<br>461 |
| Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42 | Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42 | Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42 | Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42 | Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42 | Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42 | Caminos pavimentados<br>164.696<br>5.633<br>1.108<br>293<br>389<br>1.676<br>42 |
| Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4 | Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4 | Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4 | Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4 | Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4 | Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4 | Caminos no pavimentados públicos<br>400<br>5.131<br>1.841<br>188<br>45<br>171<br>4 |
| **Total (kg/año)** | **14.517** | **4.338** | **1.622** | **3.138** | **12.155** | **508** |

**Tabla 5-1: Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1****

| Valor Norma Concentración Aporte respecto a<br>Norma de calidad del aire<br>(μg/Nmɜ) (μg/Nmɜ) norma % | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| MP10 24 horas Per98<br>150<br>8,3<br>5,5% | MP10 24 horas Per98<br>150<br>8,3<br>5,5% | MP10 24 horas Per98<br>150<br>8,3<br>5,5% | MP10 24 horas Per98<br>150<br>8,3<br>5,5% |
| MP10 Anual<br>50<br>2,7<br>5,4% | MP10 Anual<br>50<br>2,7<br>5,4% | MP10 Anual<br>50<br>2,7<br>5,4% | MP10 Anual<br>50<br>2,7<br>5,4% |
| MP2,5 24 horas Per98<br>50<br>6,9<br>13,8% | MP2,5 24 horas Per98<br>50<br>6,9<br>13,8% | MP2,5 24 horas Per98<br>50<br>6,9<br>13,8% | MP2,5 24 horas Per98<br>50<br>6,9<br>13,8% |
| MP2,5 Anual<br>20<br>2,2<br>11,0% | MP2,5 Anual<br>20<br>2,2<br>11,0% | MP2,5 Anual<br>20<br>2,2<br>11,0% | MP2,5 Anual<br>20<br>2,2<br>11,0% |
| NO2 1 hora Per99<br>400<br>170,8<br>42,7% | NO2 1 hora Per99<br>400<br>170,8<br>42,7% | NO2 1 hora Per99<br>400<br>170,8<br>42,7% | NO2 1 hora Per99<br>400<br>170,8<br>42,7% |
| NO2 Anual<br>100<br>19,0<br>19,0% | NO2 Anual<br>100<br>19,0<br>19,0% | NO2 Anual<br>100<br>19,0<br>19,0% | NO2 Anual<br>100<br>19,0<br>19,0% |
| CO 1 hora Per99<br>30.000<br>45,9<br>0,2% | CO 1 hora Per99<br>30.000<br>45,9<br>0,2% | CO 1 hora Per99<br>30.000<br>45,9<br>0,2% | CO 1 hora Per99<br>30.000<br>45,9<br>0,2% |
| CO 8 horas Per99<br>10.000<br>28,8<br>0,3% | CO 8 horas Per99<br>10.000<br>28,8<br>0,3% | CO 8 horas Per99<br>10.000<br>28,8<br>0,3% | CO 8 horas Per99<br>10.000<br>28,8<br>0,3% |
| SO2 1 hora Per98,5<br>350<br>7,0<br>2,0% | SO2 1 hora Per98,5<br>350<br>7,0<br>2,0% | SO2 1 hora Per98,5<br>350<br>7,0<br>2,0% | SO2 1 hora Per98,5<br>350<br>7,0<br>2,0% |
| SO2 24 horas Per99<br>150<br>3,0<br>2,0% | SO2 24 horas Per99<br>150<br>3,0<br>2,0% | SO2 24 horas Per99<br>150<br>3,0<br>2,0% | SO2 24 horas Per99<br>150<br>3,0<br>2,0% |
| SO2 Anual<br>60<br>0,8<br>1,4% | SO2 Anual<br>60<br>0,8<br>1,4% | SO2 Anual<br>60<br>0,8<br>1,4% | SO2 Anual<br>60<br>0,8<br>1,4% |
| SO2 1 hora Per99,7<br>1.000<br>9,8<br>1,0% | SO2 1 hora Per99,7<br>1.000<br>9,8<br>1,0% | SO2 1 hora Per99,7<br>1.000<br>9,8<br>1,0% | SO2 1 hora Per99,7<br>1.000<br>9,8<br>1,0% |
| SO2 24 horas Per99,7<br>365<br>3,1<br>0,9% | SO2 24 horas Per99,7<br>365<br>3,1<br>0,9% | SO2 24 horas Per99,7<br>365<br>3,1<br>0,9% | SO2 24 horas Per99,7<br>365<br>3,1<br>0,9% |
| SO2 Anual | 80 | 0,8 | 1,1% |

**Tabla 5-2: Coordenadas de los Puntos de Máximo Impacto - Fase de construcción Año 1****

| Norma Receptor X (m) Y (m) | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| MP10 24 horas Per98<br>R2<br>262.146<br>6.351.100 | MP10 24 horas Per98<br>R2<br>262.146<br>6.351.100 | MP10 24 horas Per98<br>R2<br>262.146<br>6.351.100 | MP10 24 horas Per98<br>R2<br>262.146<br>6.351.100 |
| MP10 Anual<br>R2<br>262.146<br>6.351.100 | MP10 Anual<br>R2<br>262.146<br>6.351.100 | MP10 Anual<br>R2<br>262.146<br>6.351.100 | MP10 Anual<br>R2<br>262.146<br>6.351.100 |
| MP2,5 24 horas Per98<br>R2<br>262.146<br>6.351.100 | MP2,5 24 horas Per98<br>R2<br>262.146<br>6.351.100 | MP2,5 24 horas Per98<br>R2<br>262.146<br>6.351.100 | MP2,5 24 horas Per98<br>R2<br>262.146<br>6.351.100 |
| MP2,5 Anual<br>R2<br>262.146<br>6.351.100 | MP2,5 Anual<br>R2<br>262.146<br>6.351.100 | MP2,5 Anual<br>R2<br>262.146<br>6.351.100 | MP2,5 Anual<br>R2<br>262.146<br>6.351.100 |
| NO2 1 hora Per99<br>R2<br>262.146<br>6.351.100 | NO2 1 hora Per99<br>R2<br>262.146<br>6.351.100 | NO2 1 hora Per99<br>R2<br>262.146<br>6.351.100 | NO2 1 hora Per99<br>R2<br>262.146<br>6.351.100 |
| NO2 Anual<br>R2<br>262.146<br>6.351.100 | NO2 Anual<br>R2<br>262.146<br>6.351.100 | NO2 Anual<br>R2<br>262.146<br>6.351.100 | NO2 Anual<br>R2<br>262.146<br>6.351.100 |
| CO 1 hora Per99<br>R2<br>262.146<br>6.351.100 | CO 1 hora Per99<br>R2<br>262.146<br>6.351.100 | CO 1 hora Per99<br>R2<br>262.146<br>6.351.100 | CO 1 hora Per99<br>R2<br>262.146<br>6.351.100 |
| CO 8 horas Per99<br>R2<br>262.146<br>6.351.100 | CO 8 horas Per99<br>R2<br>262.146<br>6.351.100 | CO 8 horas Per99<br>R2<br>262.146<br>6.351.100 | CO 8 horas Per99<br>R2<br>262.146<br>6.351.100 |
| SO2 1 hora Per98,5<br>R2<br>262.146<br>6.351.100 | SO2 1 hora Per98,5<br>R2<br>262.146<br>6.351.100 | SO2 1 hora Per98,5<br>R2<br>262.146<br>6.351.100 | SO2 1 hora Per98,5<br>R2<br>262.146<br>6.351.100 |
| SO2 24 horas Per99<br>R2<br>262.146<br>6.351.100 | SO2 24 horas Per99<br>R2<br>262.146<br>6.351.100 | SO2 24 horas Per99<br>R2<br>262.146<br>6.351.100 | SO2 24 horas Per99<br>R2<br>262.146<br>6.351.100 |
| SO2 Anual<br>R2<br>262.146<br>6.351.100 | SO2 Anual<br>R2<br>262.146<br>6.351.100 | SO2 Anual<br>R2<br>262.146<br>6.351.100 | SO2 Anual<br>R2<br>262.146<br>6.351.100 |
| SO2 1 hora Per99,7<br>R1<br>262.128<br>6.351.174 | SO2 1 hora Per99,7<br>R1<br>262.128<br>6.351.174 | SO2 1 hora Per99,7<br>R1<br>262.128<br>6.351.174 | SO2 1 hora Per99,7<br>R1<br>262.128<br>6.351.174 |
| SO2 24 horas Per99,7<br>R2<br>262.146<br>6.351.100 | SO2 24 horas Per99,7<br>R2<br>262.146<br>6.351.100 | SO2 24 horas Per99,7<br>R2<br>262.146<br>6.351.100 | SO2 24 horas Per99,7<br>R2<br>262.146<br>6.351.100 |
| SO2 Anual | R2 | 262.146 | 6.351.100 |

**Tabla 5-3: Análisis normativo en Puntos de Máximo Impacto - Fase de construcción Año 1****

| Valor Norma Aporte proyecto Línea de Base Total % Respecto a<br>Norma<br>(μg/Nmɜ) en PMI (μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ) norma | Col2 | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48% | MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48% | MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48% | MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48% | MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48% | MP10 24 horas Per98<br>150<br>8,3<br>64<br>72,3<br>48% |
| MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79% | MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79% | MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79% | MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79% | MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79% | MP10 Anual<br>50<br>2,7<br>37<br>39,7<br>79% |
| SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11% | SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11% | SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11% | SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11% | SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11% | SO2 1 hora Per98,5<br>350<br>7,0<br>33<br>40,0<br>11% |
| SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23% | SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23% | SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23% | SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23% | SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23% | SO2 24 horas Per99<br>150<br>3,0<br>31<br>34,0<br>23% |
| SO2 Anual | 60 | 0,8 | 9 | 9,8 | 16% |

**Tabla 5-4: Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1****

| Valor Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1<br>Norma norma (μg/Nmɜ)<br>(μg/Nmɜ) R1 R2 R3 R4 R5 R6 R7 R8 R9 | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 | MP10 24 horas Per98<br>150<br>8,1<br>8,3<br>7,2<br>3,0<br>1,0<br>1,2<br>0,6<br>3,4<br>0,7 |
| MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 | MP10 Anual<br>50<br>2,3<br>2,7<br>2,4<br>0,8<br>0,3<br>0,3<br>0,1<br>0,9<br>0,2 |
| MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 | MP2,5 24 horas Per98<br>50<br>6,5<br>6,9<br>6,0<br>2,7<br>0,8<br>1,0<br>0,5<br>2,7<br>0,6 |
| MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 | MP2,5 Anual<br>20<br>1,8<br>2,2<br>1,9<br>0,7<br>0,2<br>0,2<br>0,1<br>0,7<br>0,1 |
| NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 | NO2 1 hora Per99<br>400<br>155,0<br>170,8<br>161,2<br>81,8<br>35,0<br>40,0<br>11,9 <br>98,3<br>14,8 |
| NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>100<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 |
| CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 | CO 1 hora Per99<br>30.000<br>42,0<br>45,9<br>43,6<br>25,5<br>9,7<br>11,3<br>3,5<br>26,2<br>4,2 |
| CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 | CO 8 horas Per99<br>10.000<br>25,9<br>28,8<br>26,3<br>12,0<br>4,1<br>4,7<br>2,3<br>11,6<br>2,3 |
| SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 | SO2 1 horas Per98,5<br>350<br>6,0<br>7,0<br>6,6<br>3,2<br>1,0<br>1,2<br>0,4<br>3,6<br>0,5 |
| SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 | SO2 24 horas Per99<br>150<br>2,8<br>3,0<br>2,5<br>0,9<br>0,4<br>0,4<br>0,2<br>1,1<br>0,2 |
| SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 | SO2Anual<br>60<br>0,7<br>0,8<br>0,7<br>0,2<br>0,1<br>0,1<br>0,0<br>0,3<br>0,0 |
| SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 | SO2 1 hora Per99,7<br>1.000<br>9,8<br>9,6<br>9,4<br>5,3<br>2,9<br>4,0<br>1,5<br>6,2<br>1,6 |
| SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 | SO2 24 horas Per99,7<br>365<br>3,1<br>3,1<br>2,7<br>1,1<br>0,4<br>0,5<br>0,2<br>1,3<br>0,2 |
| SO2 Anual | 60 | 0,7 | 0,8 | 0,7 | 0,2 | 0,1 | 0,1 | 0,03 | 0,3 | 0,05 |

**Tabla 5-5: Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de construcción Año 1****

| Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de<br>Norma construcción Año 1<br>R1 R2 R3 R4 R5 R6 R7 R8 R9 | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 | MP10 24 horas Per98<br>5,4<br>5,5<br>4,8<br>2,0<br>0,7<br>0,8<br>0,4<br>2,3<br>0,5 |
| MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 | MP10 Anual<br>4,5<br>5,4<br>4,8<br>1,6<br>0,5<br>0,6<br>0,3<br>1,9<br>0,3 |
| MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 | MP2,5 24 horas Per98<br>13,0<br>13,8<br>11,9<br>5,3<br>1,6<br>1,9<br>1,0<br>5,5<br>1,1 |
| MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 | MP2,5 Anual<br>9,2<br>11,0<br>9,7<br>3,3<br>1,0<br>1,1<br>0,5<br>3,7<br>0,7 |
| NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 | NO2 1 hora Per99<br>38,7<br>42,7<br>40,3<br>20,4<br>8,8<br>10,0<br>3,0 <br>24,6<br>3,7 |
| NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 | NO2 Anual<br>15,6<br>19,0<br>16,6<br>4,8<br>1,6<br>1,8<br>0,7<br>6,5<br>1,0 |
| CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 1 hora Per99<br>0,1<br>0,2<br>0,1<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 |
| CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 | CO 8 horas Per99<br>0,3<br>0,3<br>0,3<br>0,1<br>0,0<br>0,0<br>0,0<br>0,1<br>0,0 |
| SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 | SO2 1 horas Per98,5<br>1,7<br>2,0<br>1,9<br>0,9<br>0,3<br>0,3<br>0,1<br>1,0<br>0,1 |
| SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 | SO2 24 horas Per99<br>1,9<br>2,0<br>1,6<br>0,6<br>0,2<br>0,3<br>0,1<br>0,8<br>0,1 |
| SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 | SO2Anual<br>1,2<br>1,4<br>1,2<br>0,4<br>0,1<br>0,1<br>0,1<br>0,5<br>0,1 |
| SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 | SO2 1 hora Per99,7<br>1,0<br>1,0<br>0,9<br>0,5<br>0,3<br>0,4<br>0,1<br>0,6<br>0,2 |
| SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 | SO2 24 horas Per99,7<br>0,8<br>0,9<br>0,7<br>0,3<br>0,1<br>0,1<br>0,1<br>0,4<br>0,1 |
| SO2 Anual | 0,9 | 1,1 | 0,9 | 0,3 | 0,1 | 0,1 | 0,0 | 0,4 | 0,1 |

**Tabla 5-6: Análisis normativo en receptores discretos - Concentración diaria MP10****

| MP10 24 horas Percentil 98<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ) | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| R1<br>8,1<br>64,0<br>72,1<br>48%<br>R2<br>8,3<br>72,3<br>48%<br>R3<br>7,2<br>71,2<br>47%<br>R4<br>3,0<br>67,0<br>45%<br>R5<br>1,0<br>65,0<br>43%<br>R6<br>1,2<br>65,2<br>43%<br>R7<br>0,6<br>64,6<br>43%<br>R8<br>3,4<br>67,4<br>45%<br>R9<br>0,7<br>64,7<br>43% | R1<br>8,1<br>64,0<br>72,1<br>48%<br>R2<br>8,3<br>72,3<br>48%<br>R3<br>7,2<br>71,2<br>47%<br>R4<br>3,0<br>67,0<br>45%<br>R5<br>1,0<br>65,0<br>43%<br>R6<br>1,2<br>65,2<br>43%<br>R7<br>0,6<br>64,6<br>43%<br>R8<br>3,4<br>67,4<br>45%<br>R9<br>0,7<br>64,7<br>43% | R1<br>8,1<br>64,0<br>72,1<br>48%<br>R2<br>8,3<br>72,3<br>48%<br>R3<br>7,2<br>71,2<br>47%<br>R4<br>3,0<br>67,0<br>45%<br>R5<br>1,0<br>65,0<br>43%<br>R6<br>1,2<br>65,2<br>43%<br>R7<br>0,6<br>64,6<br>43%<br>R8<br>3,4<br>67,4<br>45%<br>R9<br>0,7<br>64,7<br>43% | R1<br>8,1<br>64,0<br>72,1<br>48%<br>R2<br>8,3<br>72,3<br>48%<br>R3<br>7,2<br>71,2<br>47%<br>R4<br>3,0<br>67,0<br>45%<br>R5<br>1,0<br>65,0<br>43%<br>R6<br>1,2<br>65,2<br>43%<br>R7<br>0,6<br>64,6<br>43%<br>R8<br>3,4<br>67,4<br>45%<br>R9<br>0,7<br>64,7<br>43% |
| R9 | 0,7 | 64,7 | 43% |

**Tabla 5-7: Análisis normativo en receptores discretos - Concentración anual MP10****

| MP10 anual<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ) | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| R1<br>2,3<br>37,0<br>39,3<br>79%<br>R2<br>2,7<br>39,7<br>79%<br>R3<br>2,4<br>39,4<br>79%<br>R4<br>0,8<br>37,8<br>76%<br>R5<br>0,3<br>37,3<br>75%<br>R6<br>0,3<br>37,3<br>75%<br>R7<br>0,1<br>37,1<br>74%<br>R8<br>0,9<br>37,9<br>76%<br>R9<br>0,2<br>37,2<br>74% | R1<br>2,3<br>37,0<br>39,3<br>79%<br>R2<br>2,7<br>39,7<br>79%<br>R3<br>2,4<br>39,4<br>79%<br>R4<br>0,8<br>37,8<br>76%<br>R5<br>0,3<br>37,3<br>75%<br>R6<br>0,3<br>37,3<br>75%<br>R7<br>0,1<br>37,1<br>74%<br>R8<br>0,9<br>37,9<br>76%<br>R9<br>0,2<br>37,2<br>74% | R1<br>2,3<br>37,0<br>39,3<br>79%<br>R2<br>2,7<br>39,7<br>79%<br>R3<br>2,4<br>39,4<br>79%<br>R4<br>0,8<br>37,8<br>76%<br>R5<br>0,3<br>37,3<br>75%<br>R6<br>0,3<br>37,3<br>75%<br>R7<br>0,1<br>37,1<br>74%<br>R8<br>0,9<br>37,9<br>76%<br>R9<br>0,2<br>37,2<br>74% | R1<br>2,3<br>37,0<br>39,3<br>79%<br>R2<br>2,7<br>39,7<br>79%<br>R3<br>2,4<br>39,4<br>79%<br>R4<br>0,8<br>37,8<br>76%<br>R5<br>0,3<br>37,3<br>75%<br>R6<br>0,3<br>37,3<br>75%<br>R7<br>0,1<br>37,1<br>74%<br>R8<br>0,9<br>37,9<br>76%<br>R9<br>0,2<br>37,2<br>74% |
| R9 | 0,2 | 37,2 | 74% |

**Tabla 5-8: Análisis normativo en receptores discretos - Concentración horaria SO** **2****

| SO 1 hora Percentil 98,5<br>2<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ) | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| R1<br>6,0<br>33,0<br>39,0<br>11%<br>R2<br>7,0<br>40,0<br>11%<br>R3<br>6,6<br>39,6<br>11%<br>R4<br>3,2<br>36,2<br>10%<br>R5<br>1,0<br>34,0<br>10%<br>R6<br>1,2<br>34,2<br>10%<br>R7<br>0,4<br>33,4<br>10%<br>R8<br>3,6<br>36,6<br>10%<br>R9<br>0,5<br>33,5<br>10% | R1<br>6,0<br>33,0<br>39,0<br>11%<br>R2<br>7,0<br>40,0<br>11%<br>R3<br>6,6<br>39,6<br>11%<br>R4<br>3,2<br>36,2<br>10%<br>R5<br>1,0<br>34,0<br>10%<br>R6<br>1,2<br>34,2<br>10%<br>R7<br>0,4<br>33,4<br>10%<br>R8<br>3,6<br>36,6<br>10%<br>R9<br>0,5<br>33,5<br>10% | R1<br>6,0<br>33,0<br>39,0<br>11%<br>R2<br>7,0<br>40,0<br>11%<br>R3<br>6,6<br>39,6<br>11%<br>R4<br>3,2<br>36,2<br>10%<br>R5<br>1,0<br>34,0<br>10%<br>R6<br>1,2<br>34,2<br>10%<br>R7<br>0,4<br>33,4<br>10%<br>R8<br>3,6<br>36,6<br>10%<br>R9<br>0,5<br>33,5<br>10% | R1<br>6,0<br>33,0<br>39,0<br>11%<br>R2<br>7,0<br>40,0<br>11%<br>R3<br>6,6<br>39,6<br>11%<br>R4<br>3,2<br>36,2<br>10%<br>R5<br>1,0<br>34,0<br>10%<br>R6<br>1,2<br>34,2<br>10%<br>R7<br>0,4<br>33,4<br>10%<br>R8<br>3,6<br>36,6<br>10%<br>R9<br>0,5<br>33,5<br>10% |
| R9 | 0,5 | 33,5 | 10% |

**Tabla 5-9: Análisis normativo en receptores discretos - Concentración diaria SO** **2****

| SO 24 horas Percentil 99<br>2<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ) | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| <br>2,8<br>31,0<br>33,8<br>23%<br> <br>3,0<br>34,0<br>23%<br> <br>2,5<br>33,5<br>22%<br> <br>0,9<br>31,9<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,2<br>31,2<br>21%<br> <br>1,1<br>32,1<br>21%<br> <br>0,2<br>31,2<br>21% | <br>2,8<br>31,0<br>33,8<br>23%<br> <br>3,0<br>34,0<br>23%<br> <br>2,5<br>33,5<br>22%<br> <br>0,9<br>31,9<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,2<br>31,2<br>21%<br> <br>1,1<br>32,1<br>21%<br> <br>0,2<br>31,2<br>21% | <br>2,8<br>31,0<br>33,8<br>23%<br> <br>3,0<br>34,0<br>23%<br> <br>2,5<br>33,5<br>22%<br> <br>0,9<br>31,9<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,2<br>31,2<br>21%<br> <br>1,1<br>32,1<br>21%<br> <br>0,2<br>31,2<br>21% | <br>2,8<br>31,0<br>33,8<br>23%<br> <br>3,0<br>34,0<br>23%<br> <br>2,5<br>33,5<br>22%<br> <br>0,9<br>31,9<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,4<br>31,4<br>21%<br> <br>0,2<br>31,2<br>21%<br> <br>1,1<br>32,1<br>21%<br> <br>0,2<br>31,2<br>21% |
|  | 0,2 | 31,2 | 21% |

**Tabla 5-10: Análisis normativo en receptores discretos - Concentración anual SO** **2****

| SO Anual<br>2<br>Receptor Aporte Proyecto Línea de Base Concentración total<br>% Norma<br>(μg/Nmɜ) (μg/Nmɜ) (μg/Nmɜ) | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| R1<br>0,7<br>9,0<br>9,7<br>2%<br>R2<br>0,8<br>9,8<br>2%<br>R3<br>0,7<br>9,7<br>2%<br>R4<br>0,2<br>9,2<br>2%<br>R5<br>0,1<br>9,1<br>2%<br>R6<br>0,1<br>9,1<br>2%<br>R7<br>0,03<br>9,0<br>2%<br>R8<br>0,3<br>9,3<br>2%<br>R9<br>0,05<br>9,0<br>2% | R1<br>0,7<br>9,0<br>9,7<br>2%<br>R2<br>0,8<br>9,8<br>2%<br>R3<br>0,7<br>9,7<br>2%<br>R4<br>0,2<br>9,2<br>2%<br>R5<br>0,1<br>9,1<br>2%<br>R6<br>0,1<br>9,1<br>2%<br>R7<br>0,03<br>9,0<br>2%<br>R8<br>0,3<br>9,3<br>2%<br>R9<br>0,05<br>9,0<br>2% | R1<br>0,7<br>9,0<br>9,7<br>2%<br>R2<br>0,8<br>9,8<br>2%<br>R3<br>0,7<br>9,7<br>2%<br>R4<br>0,2<br>9,2<br>2%<br>R5<br>0,1<br>9,1<br>2%<br>R6<br>0,1<br>9,1<br>2%<br>R7<br>0,03<br>9,0<br>2%<br>R8<br>0,3<br>9,3<br>2%<br>R9<br>0,05<br>9,0<br>2% | R1<br>0,7<br>9,0<br>9,7<br>2%<br>R2<br>0,8<br>9,8<br>2%<br>R3<br>0,7<br>9,7<br>2%<br>R4<br>0,2<br>9,2<br>2%<br>R5<br>0,1<br>9,1<br>2%<br>R6<br>0,1<br>9,1<br>2%<br>R7<br>0,03<br>9,0<br>2%<br>R8<br>0,3<br>9,3<br>2%<br>R9<br>0,05<br>9,0<br>2% |
| R9 | 0,05 | 9,0 | 2% |
