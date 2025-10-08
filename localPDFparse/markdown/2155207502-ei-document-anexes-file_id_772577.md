---
title: Tipo de Informe o Capítulo
author: Kisi Cerda
date: D:20220215171636-03'00'
language: es
type: report
pages: 48
has_toc: False
has_tables: True
extraction_quality: high
---

ANEXO E

INFORME

MODELACIÓN DE CALIDAD DEL AIRE

DECLARACIÓN DE IMPACTO AMBIENTAL

“MAKROPLAZA”

COMUNA DE VIÑA DEL MAR, REGIÓN DE VALPARAÍSO

FEBRERO, 2022

ELABORADO PARA CBLS AMBIENTAL

POR KISI CERDA PALMA - INGENIERO CIVIL AMBIENTAL

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

ÍNDICE GENERAL

**1.** **ANTECEDENTES GENERALES DEL PROYECTO** **...................................................................... 5**

**2.** **LINEA DE BASE** **......................................................................................................................... 6**

2.1. METEOROLOGÍA ......................................................................................................................................................7

2.1.1 Validez de los registros meteorológicos ...................................................................................................7

2.1.2 Velocidad del viento .........................................................................................................................................7

2.1.3 Dirección del Viento .........................................................................................................................................8

2.2. CALIDAD DEL AIRE............................................................................................................................................... 10

**3.** **MODELACIÓN CALIDAD DEL AIRE** **......................................................................................... 10**

3.1. Información Geográfica ......................................................................................................................................... 10

3.2. Descripción del Modelo Meteorológico WRF................................................................................................. 13

3.3. Análisis de Incertidumbre del Modelo Meteorológico WRF ...................................................................... 13

3.3.1 Velocidad del Viento ..................................................................................................................................... 13

3.3.2 Dirección del Viento ...................................................................................................................................... 14

3.4. Grilla de receptores................................................................................................................................................. 16

3.5. Receptores sensibles............................................................................................................................................. 18

3.6. Fuentes de emisión................................................................................................................................................. 19

**4.** **MARCO LEGAL APLICABLE AL PROYECTO** **........................................................................... 22**

**5.** **RESULTADOS DE LA MODELACIÓN ....................................................................................... 23**

5.1. Puntos de máximo Impacto ................................................................................................................................. 23

5.1.1 Análisis Normativo ......................................................................................................................................... 25

5.2. Receptores Discretos............................................................................................................................................. 25

5.2.1 Análisis Normativo ......................................................................................................................................... 27

5.3. Curvas de Isoconcentración - Fase de Construcción ................................................................................ 28

5.4. Material Particulado Sedimentable.................................................................................................................... 38

**6.** **ÁREA DE INFLUENCIA ............................................................................................................ 39**

**7.** **CONCLUSIONES ...................................................................................................................... 45**

**8.** **BIBLIOGRAFÍA......................................................................................................................... 47**

**9.** **ANEXO A ARCHIVOS DE ENTRADA Y SALIDA DEL MODELO (DIGITAL)** **................................ 48**

Página | 2

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**INDICE DE TABLAS**

Tabla 2-1 Ubicación de la estación Junta de Vecinos ......................................................................................................6

Tabla 2-2 Validez de registros meteorológicos - Año 2020. ..........................................................................................7

Tabla 2-3 Distribución de frecuencias (%) - Estación Junta de Vecinos 2020 ........................................................9

Tabla 2-4 Línea de base de calidad del aire trienio 2017 - 2019 en la estación Junta de Vecinos .............. 10

Tabla 3-1 Parámetros de la proyección cónica del modelo WRF .............................................................................. 13

Tabla 3-2 Error Cuadrático Medio, Sesgo y Coeficiente de Correlación del ciclo diario de Velocidad del

Viento. Mediciones vs. Modelo WRF en Estación Junta de Vecinos........................................................................ 14

Tabla 3-3 Características del dominio de modelación ................................................................................................... 16

Tabla 3-4 Receptores discretos del modelo ...................................................................................................................... 18

Tabla 3-5 Emisiones totales de contaminantes atmosféricos - Año 1 Fase de construcción ......................... 19

Tabla 3-6 Superficie y emisiones agrupadas por fuente ............................................................................................... 20

Tabla 3-7 Emisiones ingresadas al modelo - Fase de construcción Año 1 ........................................................... 20

Tabla 4-1 Normativa primaria de calidad del aire aplicable al Proyecto.................................................................. 22

Tabla 4-2 Normativa secundaria de calidad del aire aplicable al Proyecto ............................................................ 22

Tabla 5-1 Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1........................ 23

Tabla 5-2 Coordenadas del Punto de Máximo Impacto - Fase de construcción Año 1 ..................................... 24

Tabla 5-3 Análisis normativo en Puntos de Máximo Impacto - Fase de construcción Año 1.......................... 25

Tabla 5-4 Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1 .................................. 26

Tabla 5-5 Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de construcción

Año 1 ............................................................................................................................................................................................... 26

Tabla 5-6 Análisis normativo en receptores discretos - Concentración diaria MP10 ......................................... 27

Tabla 5-7 Análisis normativo en receptores discretos - Concentración anual MP10 ......................................... 27

Tabla 5-8 Análisis normativo en receptores discretos - Concentración horaria SO 2 ......................................... 27

Tabla 5-9 Análisis normativo en receptores discretos - Concentración diaria SO 2 ............................................ 28

Tabla 5-10 Análisis normativo en receptores discretos - Concentración anual SO 2 .......................................... 28

Tabla 6-1 Concentración equivalente al 1% de la norma ............................................................................................. 39

**ÍNDICE DE FIGURAS**

Figura 1-1 Emplazamiento del Proyecto ................................................................................................................................5

Figura 2-1 Ubicación de la estación Junta de Vecinos .....................................................................................................6

Figura 2-2 Serie de tiempo de la velocidad del viento registrada durante el año 2020 - Estación Junta de

Vecinos ..............................................................................................................................................................................................7

Figura 2-3 Ciclo diario de la velocidad del viento registrada durante el año 2020 - Estación Junta de Vecinos

..............................................................................................................................................................................................................8

Figura 2-4 Serie de tiempo de la dirección del viento 2020 - Estación Junta de Vecinos....................................8

Figura 2-5 Rosa de vientos 2020 - Estación Junta de Vecinos .....................................................................................9

Figura 3-1 Representación de información topográfica utilizada por el modelo ................................................... 11

Figura 3-2 Representación de la información de uso de suelo utilizada por el modelo ..................................... 12

Página | 3

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

Figura 3-3 Comparación de ciclos diarios de la velocidad del viento en Estación Junta de Vecinos.

Mediciones vs. Modelo WRF .................................................................................................................................................. 14

Figura 3-4 Rosas de viento obtenidas del modelo WRF y los registros de la estación Junta de Vecinos .. 15

Figura 3-5 Comparación de series de tiempo de dirección del viento. Registros vs. Modelo WRF - Estación

Junta de Vecinos 2020.............................................................................................................................................................. 15

Figura 3-6 Dominio de modelación y grilla de receptores. ........................................................................................... 17

Figura 3-7 Distribución de receptores sensibles o discretos ....................................................................................... 18

Figura 3-8 Representación de las fuentes en el modelo. ............................................................................................. 21

Figura 5-1 Ubicación de los Puntos de Máximo Impacto - Fase de construcción Año 1. ................................ 24

Figura 5-2 Curvas de Isoconcentración - MP10 24 horas Percentil 98................................................................... 29

Figura 5-3 Curvas de Isoconcentración - MP10 concentración anual ..................................................................... 30

Figura 5-4 Curvas de Isoconcentración - MP2,5 24 horas Percentil 98 ................................................................. 31

Figura 5-5 Curvas de Isoconcentración - MP2,5 Anual ................................................................................................ 32

Figura 5-6 Curvas de Isoconcentración - NO 2 1 hora Percentil 99........................................................................... 33

Figura 5-7 Curvas de Isoconcentración - NO 2 Anual..................................................................................................... 34

Figura 5-8 Curvas de Isoconcentración - SO 2 1 hora Percentil 98,5 ....................................................................... 35

Figura 5-9 Curvas de Isoconcentración - SO 2 24 horas Percentil 99 ...................................................................... 36

Figura 5-10 Curvas de Isoconcentración - SO 2 concentración anual ...................................................................... 37

Figura 5-11 Curvas de isodeposición MPS anual - Fase de Construcción. .......................................................... 38
Figura 6-1 Área de influencia - Concentración MP10 24 horas Percentil 98. ....................................................... 40

Figura 6-2 Área de influencia - Concentración MP10 Anual....................................................................................... 40
Figura 6-3 Área de influencia - Concentración MP2,5 24 horas Percentil 98 ....................................................... 41

Figura 6-4 Área de influencia - Concentración MP2,5 Anual. .................................................................................... 41
Figura 6-5 Área de influencia - Concentración NO 2 1 hora Percentil 99. ............................................................... 42

Figura 6-6 Área de influencia - Concentración NO 2 Anual .......................................................................................... 42

Figura 6-7 Área de influencia - Concentración CO 1 hora Percentil 99 .................................................................. 43
Figura 6-8 Área de influencia - Concentración CO 8 horas Percentil 99 ................................................................ 43

Figura 6-9 Área de influencia del Proyecto para la componente aire ....................................................................... 44

Página | 4

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**1.** **ANTECEDENTES GENERALES DEL PROYECTO**

Makroplaza (en adelante, el Proyecto) es un proyecto inmobiliario que se desarrollará en el radio urbano

de la comuna de Viña del Mar, en la provincia y región de Valparaíso, en un predio ubicado en Av. Edmundo

Eluchans esquina Teresa Hamel Nieto, y que tiene una superficie de 8.038,66 m [2] . La ubicación del Proyecto

se presenta en la Figura 1-1.

El Proyecto, que se somete en forma voluntaria al Sistema de Evaluación de Impacto Ambiental (SEIA)

mediante la presente Declaración de Impacto Ambiental (DIA), cuyo titular es la empresa Makroplaza S.A.,

consistirá en la construcción de:

i) Un edificio con destino residencial de 35 pisos que alberga 308 departamentos y
equipamiento común en el último piso y cubierta;

ii) Un edificio de oficinas de 10 pisos que considera 108 unidades;

iii) 1 placa comercial con 10 locales para comercio menor, distribuidos en el primer piso de
ambos edificios

iv) 3 subterráneos con 562 estacionamientos para automóviles y 328 bodegas, siendo el primer
subterráneo destinado al uso de estacionamientos y bodegas para las oficinas y comercio, y
el segundo y tercer subterráneo a uso de estacionamientos y bodegas exclusivo del edificio
residencial. Además, se cuenta con 32 estacionamientos en superficie.

El presente informe describe la modelación de la dispersión de las emisiones atmosféricas estimadas para

el primer año de la construcción del Proyecto de acuerdo a las exigencias indicadas en la “Guía para el uso

de modelos de calidad del aire en el SEA”.

**Figura 1-1 Emplazamiento del Proyecto**

Fuente: Elaboración propia.

Página | 5

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**2.** **LINEA DE BASE**

Para determinar la línea de base meteorológica y de calidad del aire del área donde se emplazará el

Proyecto, se han utilizado los datos registrados en la estación Junta de Vecinos, ubicada en Concón, a un

costado de la Plaza Las Petras y que pertenece a la red de monitoreo de ENAP. La estación se encuentra a

2,6 km al NE del Proyecto, tal como se puede observar en la Figura 2-1.

**Tabla 2-1 Ubicación de la estación Junta de Vecinos**

|Coordenadas UTM|Col2|Distancia al Proyecto<br>(km)|Altura sobre el nivel del mar<br>(m)|
|---|---|---|---|
|**X (m)**|**Y (m)**|**Y (m)**|**Y (m)**|
|263.872|6.353.054|2,6|81|

Fuente: Elaboración propia. DATUM WGS84 Huso 19. Fuente: Elaboración propia.

**Figura 2-1 Ubicación de la estación Junta de Vecinos**

Proyección Cónica Conforme de Lambert, DATUM NWS-84. Fuente: Elaboración propia.

Página | 6

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

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

|Variable|N° Registros Válidos|% Registros Válidos|
|---|---|---|
|Velocidad del Viento|8.769|99,87%|
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
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

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
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 2-5 Rosa de vientos 2020 - Estación Junta de Vecinos**

Fuente: Elaboración propia.

**Tabla 2-3 Distribución de frecuencias (%) - Estación Junta de Vecinos 2020**

|Dirección del Viento|Rango de Velocidad (m/s)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Dirección del Viento**|**0,5 - 2,1**|**2,1 - 3,6**|**3,6 - 5,7**|**5,7 - 8,8**|**8,8 - 11,1**|**>= 11,10**|**Total (%)**|
|N|4,6|1,2|0,3|0,0|0,0|0,0|6,0|
|NNE|3,8|0,7|0,0|0,0|0,0|0,0|4,5|
|NE|1,7|0,0|0,0|0,0|0,0|0,0|1,7|
|ENE|1,1|0,0|0,0|0,0|0,0|0,0|1,1|
|E|3,8|0,1|0,0|0,0|0,0|0,0|3,9|
|ESE|5,0|0,4|0,0|0,0|0,0|0,0|5,4|
|SE|6,2|0,0|0,0|0,0|0,0|0,0|6,2|
|SSE|4,6|0,4|0,0|0,0|0,0|0,0|4,9|
|S|7,3|0,8|0,5|0,0|0,0|0,0|8,6|
|SSW|2,0|0,6|0,2|0,0|0,0|0,0|2,7|
|SW|2,1|3,4|0,8|0,0|0,0|0,0|6,3|
|WSW|2,7|2,6|0,0|0,0|0,0|0,0|5,4|
|W|3,4|2,8|0,0|0,0|0,0|0,0|6,2|
|WNW|3,2|2,4|0,0|0,0|0,0|0,0|5,6|
|NW|7,0|5,1|0,3|0,0|0,0|0,0|12,4|
|NNW|6,1|1,5|0,4|0,0|0,0|0,0|8,0|
|Sub-Total|64,6|21,8|2,6|0,0|0,0|0,0|89,0|
|Calmas (%)|Calmas (%)|Calmas (%)|Calmas (%)|Calmas (%)|Calmas (%)|Calmas (%)|10,8|
|Sin dato (%)|Sin dato (%)|Sin dato (%)|Sin dato (%)|Sin dato (%)|Sin dato (%)|Sin dato (%)|0,2|
|Total (%)|Total (%)|Total (%)|Total (%)|Total (%)|Total (%)|Total (%)|100|

Fuente: Elaboración propia.

Página | 9

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**2.2.** **CALIDAD DEL AIRE**

Para determinar la línea de base de calidad se han considerado las mediciones de MP10 y SO 2 efectuadas

en la estación Junta de Vecinos durante el trienio 2017-2019 y que constan en el Informe “Línea de Base

de la Calidad del Aire en la Región de Valparaíso. Período 2017-2019” elaborado en conjunto por la SEREMI

Medio Ambiente y la SEREMI Salud de la región de Valparaíso (2020).

**Tabla 2-4 Línea de base de calidad del aire trienio 2017 - 2019 en la estación Junta de Vecinos**

|Norma|Valor norma<br>(μg/Nmɜ)|Concentración<br>(μg/Nmɜ)|% Norma|
|---|---|---|---|
|MP10 24 horas Percentil 98|150|64|43|
|MP10 Anual|50|37|74|
|SO2 1 hora Percentil 98,5|350|33|9|
|SO2 24 horas Percentil 99|150|31|21|
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
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 3-1 Representación de información topográfica utilizada por el modelo**

Fuente: Elaboración propia.

Página | 11

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 3-2 Representación de la información de uso de suelo utilizada por el modelo**

Fuente: Elaboración propia.

Página | 12

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

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
| Proyección | LCC (Cónica Conforme de Lambert) |
| DATUM | NWS-84 6370KM Radius |
| Origen Proyección (latitud) | 32,960 |
| Origen Proyección (longitud) | 71,544 |
| Paralelo Estándar (Latitud 1) | 32,720 |
| Paralelo Estándar (Latitud 2) | 33,200 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: ENVIROMODELING. **3.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF** -->
<!-- FIN TABLA 3-1 -->


**Tabla 3-1 Parámetros de la proyección cónica del modelo WRF**

|Sistema coordenado del modelo WRF|Col2|
|---|---|
|Proyección|LCC (Cónica Conforme de Lambert)|
|DATUM|NWS-84 6370KM Radius|
|Origen Proyección (latitud)|32,960|
|Origen Proyección (longitud)|71,544|
|Paralelo Estándar (Latitud 1)|32,720|
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
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 3-3 Comparación de ciclos diarios de la velocidad del viento en Estación Junta de Vecinos. Mediciones vs.**

**Modelo WRF**

Fuente: Elaboración propia

**Tabla 3-2 Error Cuadrático Medio, Sesgo y Coeficiente de Correlación del ciclo diario de Velocidad del Viento.**

**Mediciones vs. Modelo WRF en Estación Junta de Vecinos**

|Estadístico|Valor|
|---|---|
|Error cuadrático Medio (m/s)|0,42|
|Sesgo (m/s)|0,40|
|Coeficiente de Correlación|0,99|

Fuente: Elaboración propia

**3.3.2** **Dirección del Viento**

En la Figura 3-4 se presentan las rosas de viento obtenidas a partir de los datos registrados y modelados

para el año 2018, mientras que en la Figura 3-5 se muestran los gráficos de ambas series de datos. Tal

como puede observarse, para este punto del dominio, el modelo WRF presenta las direcciones S y SSE

como predominantes, mientras que los registros muestran una dirección y que es la SSE.

Página | 14

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 3-4 Rosas de viento obtenidas del modelo WRF y los registros de la estación Junta de Vecinos**

|Mediciones|Modelo WRF|
|---|---|
|||

Fuente: Elaboración propia.

**Figura 3-5 Comparación de series de tiempo de dirección del viento. Registros vs. Modelo WRF - Estación Junta**

**de Vecinos 2020**

Fuente: Elaboración propia.

Página | 15

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

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

**Tabla 3-3 Características del dominio de modelación**

|Coordenadas del centro (m)<br>(DATUM WGS84 18H)|X = 262.211<br>Y = 6.350.275|
|---|---|
|**Tamaño**|50 km x 50 km|
|**Resolución**|1 km|
|**N° de receptores**|2.500|

Fuente: Elaboración propia.

Página | 16

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 3-6 Dominio de modelación y grilla de receptores.**

Fuente: Elaboración propia.

Página | 17

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**3.5.** **RECEPTORES SENSIBLES**

Los receptores sensibles, o de interés, definidos para la modelación se presentan en la Tabla 3-4 y

corresponden a los principales puntos sensibles que se encuentran dentro del dominio de modelación del

Proyecto, tales como viviendas y centros comerciales. La ubicación de los receptores se presenta en la

Figura 3-7.

**Tabla 3-4 Receptores discretos del modelo**

|ID|Descripción|Uso efectivo|X<br>(m)|Y<br>(m)|Distancia<br>al<br>Proyecto<br>(m)|Altura<br>(m.s.n.m)|
|---|---|---|---|---|---|---|
|R1|Edificio Cumbre de 24 pisos, ubicado<br>en Av. Edmundo Eluchans 1615.|Vivienda|262.157|6.350.314|17|70|
|R2|Edificio Reñacamar II de 25 pisos,<br>ubicado Av. Edmundo Eluchans 1737.|Vivienda|262.155|6.350.381|22|73|
|R3|Edificio Las Golondrinas de 26 pisos,<br>ubicado en calle Golondrinas 1731.|Vivienda|262.298|6.350.417|18|93|
|R4|Gasolinera Shell con strip center.|Comercial|262.209|6.350.423|51|84|

Fuente: Elaboración propia. DATUM WGS84.

**Figura 3-7 Distribución de receptores sensibles o discretos**

Fuente: Elaboración propia.

Página | 18

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**3.6.** **FUENTES DE EMISIÓN**

El escenario a modelar corresponde al primer año de la fase de construcción del Proyecto (Año 1) dado

que es la etapa en que se producirá el mayor volumen de emisiones atmosféricas. En la Tabla 3-5 se

muestran las emisiones atmosféricas estimadas para el Año 1 y cuyo detalle de cálculo se presenta en el

Anexo E Estimación de Emisiones Atmosféricas de la presente Declaración de Impacto Ambiental.

Como puede observarse, las mayores emisiones de contaminantes atmosféricos que se generarán durante

el primer año de la fase de construcción del Proyecto corresponden al NOx generado por la operación de

la maquinaria (8,6 toneladas/año). Le siguen en importancia las emisiones de MPS resuspendido por el

tránsito de camiones en caminos pavimentados (6,7 toneladas/año). En tercer lugar, se encuentran las

emisiones CO producto del funcionamiento de la maquinaria (2,1 toneladas/año).

En la Tabla 3-6 se presentan las emisiones agrupadas por fuente de emisión y la superficie que se ha

asignado a cada una de éstas en el modelo. Para estimar el área de los caminos se asignó a todos, un ancho

de 8 metros.

**Tabla 3-5 Emisiones totales de contaminantes atmosféricos - Año 1 Fase de construcción**

|Actividad|Emisiones - Fase de construcción Año 1 (kg/año)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MPS**|**MP10**|**MP2,5**|**CO**|**NOx**|**SOx**|**COV/HC**|
|Escarpe|16,4|16,4|16,4|-|-|-|-|
|Excavaciones|560,5|69,0|58,8|-|-|-|-|
|Transferencia de Material|75,4|35,7|5,4|-|-|-|-|
|Resuspensión en caminos<br>pavimentados|6.744,2|1.294,6|313,2|-|-|-|-|
|Resuspensión en caminos internos no<br>pavimentados|900,2|183,5|18,4|-|-|-|-|
|Resuspensión en caminos públicos no<br>pavimentados|1.937,7|724,3|72,4|-|-|-|-|
|Combustión de motores de vehículos<br>- Caminos pavimentados|40,2|40,2|40,2|468,0|2.018,8|51,2|85,1|
|Combustión de motores de vehículos<br>- Caminos no pavimentados públicos|0,2|0,2|0,2|2,5|8,8|0,2|0,6|
|Combustión de motores de vehículos<br>- Caminos no pavimentados internos|4,6|4,6|4,6|49,9|175,1|4,5|11,2|
|Combustión maquinaria fuera de ruta|709,6|709,6|709,6|2.050,9|8.598,1|10,4|928,7|
|Grupos electrógenos|2,5|2,5|2,5|7,6|33,8|2,3|-|
|**Total (kg/año)**|**10.991**|**3.081**|**1.242**|**2.579**|**10.834**|**69**|**1.026**|
|**Total (ton/año)**|**11,0**|**3,1**|**1,2**|**2,6**|**10,8**|**0,1**|**1,0**|

Fuente: Tabla 5.1 Anexo E Estimación de Emisiones Atmosféricas DIA Edificio Makroplaza.

Página | 19

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Tabla 3-6 Superficie y emisiones agrupadas por fuente**

|Fuente|Área fuente en el<br>modelo (m2)|Emisiones - Fase de construcción Año 1 (kg/año)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Fuente**|**Área fuente en el**<br>**modelo (m2)**|**MPS**|**MP10**|**MP2,5**|**CO**|**NOx**|**SOx**|
|Proyecto|6.564|3.753|1.389|1.140|2.704|10.307|461|
|Caminos pavimentados|164.696|5.633|1.108|293|389|1.676|42|
|Caminos no pavimentados públicos|400|5.131|1.841|188|45|171|4|
|**Total (kg/año)**|**Total (kg/año)**|**14.517**|**4.338**|**1.622**|**3.138**|**12.155**|**508**|

Fuente: Elaboración propia.

Al ingresar las emisiones al modelo se ha supuesto que todo el NOx y el SOx obtenido en la estimación de

emisiones corresponden a NO 2 y SO 2, respectivamente. Las tasas de emisión ingresadas al modelo se

presentan en la Tabla 3-7. La representación gráfica de las fuentes en el modelo CALPUFF, se presenta en

<!-- INICIO TABLA 3-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- presentan en la Tabla 3-7. La representación gráfica de las fuentes en el modelo CALPUFF, se presenta en la Figura 3-8. -->

**Tabla 3-7: Emisiones ingresadas al modelo - Fase de construcción Año 1****

| Fuente | Emisión (ton/m2·año) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **MPS** | **MP10** | **MP2,5** | **CO** | **NOx** | **SOx** |
| Proyecto | 5,7E-04 | 2,1E-04 | 1,7E-04 | 4,1E-04 | 1,6E-03 | 7,0E-05 |
| Caminos pavimentados | 3,4E-05 | 6,7E-06 | 1,8E-06 | 2,4E-06 | 1,0E-05 | 2,6E-07 |
| Caminos no pavimentados públicos | 6,1E-04 | 2,2E-04 | 2,2E-05 | 5,4E-06 | 2,0E-05 | 5,3E-07 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Página | 20 -->
<!-- FIN TABLA 3-7 -->


la Figura 3-8.

**Tabla 3-7 Emisiones ingresadas al modelo - Fase de construcción Año 1**

|Fuente|Emisión (ton/m2·año)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Fuente**|**MPS**|**MP10**|**MP2,5**|**CO**|**NOx**|**SOx**|
|Proyecto|5,7E-04|2,1E-04|1,7E-04|4,1E-04|1,6E-03|7,0E-05|
|Caminos pavimentados|3,4E-05|6,7E-06|1,8E-06|2,4E-06|1,0E-05|2,6E-07|
|Caminos no pavimentados públicos|6,1E-04|2,2E-04|2,2E-05|5,4E-06|2,0E-05|5,3E-07|

Fuente: Elaboración propia.

Página | 20

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 3-8 Representación de las fuentes en el modelo.**

Fuente: Elaboración propia.

Página | 21

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

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

| Contaminante | Decreto N° | Año Promulgación | Promedio | Límite<br>(μg/Nmɜ) |
| --- | --- | --- | --- | --- |
| MP10 | 59 | 1998 | 24 horas - Percentil 98 | 150 |
| MP10 | 59 | 1998 | Anual | 50 |
| MP2,5 | 12 | 2011 | 24 horas - Percentil 98 | 50 |
| MP2,5 | 12 | 2011 | Anual | 20 |
| CO | 115 | 2002 | 1 hora | 30.000 |
| CO | 115 | 2002 | 8 horas | 10.000 |
| NO2 | 114 | 2002 | 1 hora | 400 |
| NO2 | 114 | 2002 | Anual | 100 |
| SO2 | 104 | 2018 | 1 hora | 350 |
| SO2 | 104 | 2018 | 24 horas | 150 |
| SO2 | 104 | 2018 | Anual | 60 |

<!-- Estadísticas: 11 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Por otro lado, la norma secundaria de calidad ambiental es aquella que establece los valores de las -->
<!-- FIN TABLA 4-1 -->


**Tabla 4-1 Normativa primaria de calidad del aire aplicable al Proyecto**

|Contaminante|Decreto N°|Año Promulgación|Promedio|Límite<br>(μg/Nmɜ)|
|---|---|---|---|---|
|MP10|59|1998|24 horas - Percentil 98|150|
|MP10|59|1998|Anual|50|
|MP2,5|12|2011|24 horas - Percentil 98|50|
|MP2,5|12|2011|Anual|20|
|CO|115|2002|1 hora|30.000|
|CO|115|2002|8 horas|10.000|
|NO2|114|2002|1 hora|400|
|NO2|114|2002|Anual|100|
|SO2|104|2018|1 hora|350|
|SO2|104|2018|24 horas|150|
|SO2|104|2018|Anual|60|

Fuente: Elaboración propia.

Por otro lado, la norma secundaria de calidad ambiental es aquella que establece los valores de las

concentraciones y períodos, máximos o mínimos permisibles de sustancias, elementos, energía o

combinación de ellos, cuya presencia o carencia en el ambiente pueda constituir un riesgo para la

protección o la conservación del medio ambiente, o la preservación de la naturaleza. La normativa

secundaria de calidad del aire aplicable al Proyecto se presenta en la Tabla 4-2.

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- protección o la conservación del medio ambiente, o la preservación de la naturaleza. La normativa secundaria de calidad del aire aplicable al Proyecto se presenta en la Tabla 4-2. -->

**Tabla 4-2: Normativa secundaria de calidad del aire aplicable al Proyecto****

| Norma | Decreto N° | Año Promulgación | Ministerio | Promedio | Unidad | Límite norma |
| --- | --- | --- | --- | --- | --- | --- |
| MPS | 4 | 1992 | MINSEGPRES | Anual | mg/m2·d | 100 |
| SO2 | 22 | 2009 | Agricultura | 1 hora Percentil 99,73 | μg/Nmɜ | 1.000 |
| SO2 | 22 | 2009 | Agricultura | 24 horas Percentil 99,7 | 24 horas Percentil 99,7 | 365 |
| SO2 | 22 | 2009 | Agricultura | Anual | Anual | 80 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Página | 22 -->
<!-- FIN TABLA 4-2 -->


**Tabla 4-2 Normativa secundaria de calidad del aire aplicable al Proyecto**

|Norma|Decreto N°|Año Promulgación|Ministerio|Promedio|Unidad|Límite norma|
|---|---|---|---|---|---|---|
|MPS|4|1992|MINSEGPRES|Anual|mg/m2·d|100|
|SO2|22|2009|Agricultura|1 hora Percentil 99,73|μg/Nmɜ|1.000|
|SO2|22|2009|Agricultura|24 horas Percentil 99,7|24 horas Percentil 99,7|365|
|SO2|22|2009|Agricultura|Anual|Anual|80|

Fuente: Elaboración propia.

Página | 22

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

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

es el NO 2 que alcanza el 56,98% del límite horario con 227,93 μg/Nmɜ.

El punto de máximo impacto es el mismo para todos los contaminantes y corresponde al receptor sensible

R1 representativo del Edificio Cumbre, de 24 pisos, ubicado en Edmundo Eluchans 1615. Las coordenadas

del punto de máximo impacto se presentan en la Tabla 5-2. La ubicación de dicho punto, relativa al

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- INFORME DE MODELACIÓN DE CALIDAD DEL AIRE DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA _____________________________________________________________________________________________________________________ -->

**Tabla 5-2: Coordenadas del Punto de Máximo Impacto - Fase de construcción Año 1****

| Receptor | X (m) | Y (m) |
| --- | --- | --- |
| R2 | 262.157 | 6.350.314 |

<!-- Estadísticas: 1 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. DATUM WGS84 Huso 19S. **Figura 5-1 Ubicación de los Puntos de Máximo Impacto - Fase de construcción Año 1.** -->
<!-- FIN TABLA 5-2 -->


Proyecto, se presenta la Figura 5-1.

**Tabla 5-1 Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1**

|Norma de calidad del aire|Valor Norma<br>(μg/Nmɜ)|Concentración<br>(μg/Nmɜ)|Aporte respecto a<br>norma %|
|---|---|---|---|
|MP10 24 horas Per98|150|9,27|6,18%|
|MP10 Anual|50|3,97|7,95%|
|MP2,5 24 horas Per98|50|7,32|14,63%|
|MP2,5 Anual|20|3,14|15,71%|
|NO2 1 hora Per99|400|227,93|56,98%|
|NO2 Anual|100|33,10|33,10%|
|CO 1 hora Per99|30.000|54,67|0,18%|
|CO 8 horas Per99|10.000|35,85|0,36%|
|SO2 1 hora Per98,5|350|0,32|0,09%|
|SO2 24 horas Per99|150|0,13|0,09%|
|SO2 Anual|60|0,05|0,09%|
|SO2 1 hora Per99,7|1.000|0,44|0,04%|
|SO2 24 horas Per99,7|365|0,17|0,05%|
|SO2 Anual|80|0,05|0,06%|

Fuente: Elaboración propia.

Página | 23

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Tabla 5-2 Coordenadas del Punto de Máximo Impacto - Fase de construcción Año 1**

|Receptor|X (m)|Y (m)|
|---|---|---|
|R2|262.157|6.350.314|

Fuente: Elaboración propia. DATUM WGS84 Huso 19S.

**Figura 5-1 Ubicación de los Puntos de Máximo Impacto - Fase de construcción Año 1.**

Fuente: Elaboración propia.

Página | 24

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**5.1.1** **Análisis Normativo**

Tal como se describe en la sección 2.2, los contaminantes monitoreados en la estación Junta de Vecinos

corresponden a MP10 y SO 2 . En la Tabla 5-3 se presenta el análisis normativo para MP10 y SO 2 efectuado

en el punto de máximo impacto. Para realizar el análisis se ha considerado como representativa de todos

los receptores, la línea de base de calidad del aire registrada en dicha estación de monitoreo.

De acuerdo a las mediciones de MP10 registradas en la estación durante los años 2017, 2018 y 2019, la

concentración de 24 horas en el PMI alcanzaría un valor total de 73,27 μg/Nm3 correspondiente al 49% de

la norma diaria. En el caso de la concentración anual, ésta alcanzaría los 40,97 μg/Nm3 equivalentes al 82%

de la norma para dicho período.

En cuanto al de SO 2 registrado en la estación durante los años 2017, 2018 y 2019, la concentración horaria

total alcanzaría un valor de 33,32 μg/Nm3 equivalente al 10% del valor de dicha norma. Para la

concentración de 24 horas en el PMI alcanzaría un valor de 31,13 μg/Nm3 correspondiente al 21% de la

norma diaria. En el caso de la concentración anual, ésta alcanzaría los 9,05 μg/Nm3 equivalentes al 15% de

la norma para dicho período.

De esta forma, la construcción del Proyecto no representaría un riesgo para la salud de la población, pues

la concentración proyectada no sobrepasaría ninguna de estas normas de calidad de aire y también, dada

la magnitud de las emisiones de material particulado y dióxido de azufre.

**Tabla 5-3 Análisis normativo en Puntos de Máximo Impacto - Fase de construcción Año 1**

|Norma|Valor Norma<br>(μg/Nmɜ)|Aporte proyecto<br>en PMI (μg/Nmɜ)|Línea de Base<br>(μg/Nmɜ)|Total<br>(μg/Nmɜ)|% Respecto a<br>norma|
|---|---|---|---|---|---|
|MP10 24 horas Per98|150|9,27|64|73,27|49%|
|MP10 Anual|50|3,97|37|40,97|82%|
|SO2 1 hora Per98,5|350|0,32|33|33,32|10%|
|SO2 24 horas Per99|150|0,13|31|31,13|21%|
|SO2 Anual|60|0,05|9|9,05|15%|

Fuente: Elaboración propia.

**5.2.** **RECEPTORES DISCRETOS**

En la Tabla 5-4 se presentan las concentraciones obtenidas en los cuatro receptores discretos o de interés

que se han definido para el Proyecto (Tabla 3-4). En la Tabla 5-5 se comparan dichas concentraciones con

<!-- INICIO TABLA 3-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto, tales como viviendas y centros comerciales. La ubicación de los receptores se presenta en la Figura 3-7. -->

**Tabla 3-4: Receptores discretos del modelo****

| ID | Descripción | Uso efectivo | X<br>(m) | Y<br>(m) | Distancia<br>al<br>Proyecto<br>(m) | Altura<br>(m.s.n.m) |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | Edificio Cumbre de 24 pisos, ubicado<br>en Av. Edmundo Eluchans 1615. | Vivienda | 262.157 | 6.350.314 | 17 | 70 |
| R2 | Edificio Reñacamar II de 25 pisos,<br>ubicado Av. Edmundo Eluchans 1737. | Vivienda | 262.155 | 6.350.381 | 22 | 73 |
| R3 | Edificio Las Golondrinas de 26 pisos,<br>ubicado en calle Golondrinas 1731. | Vivienda | 262.298 | 6.350.417 | 18 | 93 |
| R4 | Gasolinera Shell con strip center. | Comercial | 262.209 | 6.350.423 | 51 | 84 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. DATUM WGS84. **Figura 3-7 Distribución de receptores sensibles o discretos** -->
<!-- FIN TABLA 3-4 -->


los límites establecidos en las normas de calidad de cada contaminante atmosférico. Tal como puede

observarse, el aporte del Proyecto es bajo en todos los receptores discretos alcanzando un máximo del

56,98% (227,93 μg/Nm3) de la norma primaria de NO 2 en concentración de 1 hora en el receptor R1

correspondiente al Edificio Cumbre, de 24 pisos, ubicado en Edmundo Eluchans 1615 al sur poniente del

Proyecto y que también corresponde al punto de máximo impacto descrito en la sección 5.1 del presente

documento.

Página | 25

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Tabla 5-4 Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1**

|Norma|Valor norma<br>(μg/Nmɜ)|Aporte del Proyecto en Receptores Discretos - Fase<br>de construcción Año 1 (μg/Nmɜ)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Norma**|**Valor norma**<br>**(μg/Nmɜ)**|**R1**|**R2**|**R3**|**R4**|
|MP10 24 horas Per98|150|9,27|7,33|2,83|5,52|
|MP10 Anual|50|3,97|3,39|1,02|1,89|
|MP2,5 24 horas Per98|50|7,32|5,83|2,21|4,39|
|MP2,5 Anual|20|3,14|2,69|0,78|1,48|
|NO2 1 hora Per99|400|227,93|153,01|104,63|129,08|
|NO2 Anual|100|33,10|28,37|8,14|15,61|
|CO 1 hora Per99|30.000|54,67|36,55|25,09|30,92|
|CO 8 horas Per99|10.000|35,85|24,59|11,10|18,03|
|SO2 1 horas Per98,5|350|0,32|0,22|0,13|0,17|
|SO2 24 horas Per99|150|0,13|0,10|0,05|0,08|
|SO2Anual|60|0,05|0,04|0,01|0,03|
|SO2 1 hora Per99,7|1.000|0,44|0,27|0,24|0,27|
|SO2 24 horas Per99,7|365|0,17|0,10|0,05|0,10|
|SO2 Anual|60|0,05|0,04|0,01|0,03|

Fuente: Elaboración propia.

**Tabla 5-5 Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de construcción Año 1**

|Norma|Aporte del Proyecto en Receptores Discretos con respecto a la norma<br>(%) - Fase de construcción Año 1|Col3|Col4|Col5|
|---|---|---|---|---|
|**Norma**|**R1**|**R2**|**R3**|**R4**|
|MP10 24 horas Per98|6,18%|4,89%|1,89%|3,68%|
|MP10 Anual|7,95%|6,79%|2,04%|3,79%|
|MP2,5 24 horas Per98|14,63%|11,67%|4,41%|8,78%|
|MP2,5 Anual|15,71%|13,43%|3,90%|7,40%|
|NO2 1 hora Per99|56,98%|38,25%|26,16%|32,27%|
|NO2 Anual|33,10%|28,37%|8,14%|15,61%|
|CO 1 hora Per99|0,18%|0,12%|0,08%|0,10%|
|CO 8 horas Per99|0,36%|0,25%|0,11%|0,18%|
|SO2 1 horas Per98,5|0,09%|0,06%|0,04%|0,05%|
|SO2 24 horas Per99|0,09%|0,06%|0,03%|0,05%|
|SO2Anual|0,09%|0,07%|0,02%|0,04%|
|SO2 1 hora Per99,7|0,04%|0,03%|0,02%|0,03%|
|SO2 24 horas Per99,7|0,05%|0,03%|0,01%|0,03%|
|SO2 Anual|0,06%|0,05%|0,02%|0,03%|

Fuente: Elaboración propia.

Página | 26

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**5.2.1** **Análisis Normativo**

En la Tabla 5-6 y Tabla 5-8 se presenta el análisis normativo efectuado en los receptores discretos para los

contaminantes MP10 y SO 2, en donde se suma el aporte del Proyecto con la línea de base registrada en la

estación Junta de Vecinos. Para realizar el análisis se ha considerado como representativa de todos los

receptores, la línea de base de calidad del aire registrada en dicha estación de monitoreo (Tabla 2-4).

<!-- INICIO TABLA 2-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de la Calidad del Aire en la Región de Valparaíso. Período 2017-2019” elaborado en conjunto por la SEREMI Medio Ambiente y la SEREMI Salud de la región de Valparaíso (2020). -->

**Tabla 2-4: Línea de base de calidad del aire trienio 2017 - 2019 en la estación Junta de Vecinos****

| Norma | Valor norma<br>(μg/Nmɜ) | Concentración<br>(μg/Nmɜ) | % Norma |
| --- | --- | --- | --- |
| MP10 24 horas Percentil 98 | 150 | 64 | 43 |
| MP10 Anual | 50 | 37 | 74 |
| SO2 1 hora Percentil 98,5 | 350 | 33 | 9 |
| SO2 24 horas Percentil 99 | 150 | 31 | 21 |
| SO2 Anual | 60 | 9 | 14 |

<!-- Estadísticas: 5 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Tabla 6.1 Concentraciones Trianuales Período 2017-2019, Informe “Línea de Base de la Calidad del Aire en la Región de Valparaíso. Período 2017-2019”. SEREMI Medio Ambiente y SEREMI Salud región de Valparaíso, 2020. -->
<!-- FIN TABLA 2-4 -->


Dado que las normas de calidad para estos contaminantes no se sobrepasan en ningún receptor discreto,

las emisiones producidas en el primer año de la fase de construcción del Proyecto no pondrán en riesgo la

salud de la población ni los recursos naturales asociada a dichos receptores. Cabe destacar que, dada la

magnitud del aporte del Proyecto, las concentraciones finales obtenidas en los receptores discretos no

representan cambios significativos con respecto a las concentraciones basales registradas en la estación

Junta de Vecinos.

**Tabla 5-6 Análisis normativo en receptores discretos - Concentración diaria MP10**

|Receptor|MP10 24 horas Percentil 98|Col3|Col4|Col5|
|---|---|---|---|---|
|**Receptor**|**Aporte Proyecto**<br>**(μg/Nmɜ)**|**Línea de Base**<br>**(μg/Nmɜ)**|**Concentración total**<br>**(μg/Nmɜ)**|**% Norma**|
|R1|9,3|64,0|73,3|49%|
|R2|7,3|7,3|71,3|48%|
|R3|2,8|2,8|66,8|45%|
|R4|5,5|5,5|69,5|46%|

Fuente: Elaboración propia.

**Tabla 5-7 Análisis normativo en receptores discretos - Concentración anual MP10**

|Receptor|MP10 anual|Col3|Col4|Col5|
|---|---|---|---|---|
|**Receptor**|**Aporte Proyecto**<br>**(μg/Nmɜ)**|**Línea de Base**<br>**(μg/Nmɜ)**|**Concentración total**<br>**(μg/Nmɜ)**|**% Norma**|
|R1|4,0|37,0|41,0|82%|
|R2|3,4|3,4|40,4|81%|
|R3|1,0|1,0|38,0|76%|
|R4|1,9|1,9|38,9|78%|

Fuente: Elaboración propia.

**Tabla 5-8 Análisis normativo en receptores discretos - Concentración horaria SO** **2**

|Receptor|SO2 1 hora Percentil 98,5|Col3|Col4|Col5|
|---|---|---|---|---|
|**Receptor**|**Aporte Proyecto**<br>**(μg/Nmɜ)**|**Línea de Base**<br>**(μg/Nmɜ)**|**Concentración total**<br>**(μg/Nmɜ)**|**% Norma**|
|R1|0,32|33,0|33,32|10%|
|R2|0,22|0,22|33,22|9%|
|R3|0,13|0,13|33,13|9%|
|R4|0,17|0,17|33,17|9%|

Fuente: Elaboración propia.

Página | 27

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Tabla 5-9 Análisis normativo en receptores discretos - Concentración diaria SO** **2**

|Receptor|SO2 24 horas Percentil 99|Col3|Col4|Col5|
|---|---|---|---|---|
|**Receptor**|**Aporte Proyecto**<br>**(μg/Nmɜ)**|**Línea de Base**<br>**(μg/Nmɜ)**|**Concentración total**<br>**(μg/Nmɜ)**|**% Norma**|
|R1|0,13|31,0|31,13|21%|
|R2|0,10|0,10|31,10|21%|
|R3|0,05|0,05|31,05|21%|
|R4|0,08|0,08|31,08|21%|

Fuente: Elaboración propia.

**Tabla 5-10 Análisis normativo en receptores discretos - Concentración anual SO** **2**

|Receptor|SO2 Anual|Col3|Col4|Col5|
|---|---|---|---|---|
|**Receptor**|**Aporte Proyecto**<br>**(μg/Nmɜ)**|**Línea de Base**<br>**(μg/Nmɜ)**|**Concentración total**<br>**(μg/Nmɜ)**|**% Norma**|
|R1|0,05|9|9,05|15%|
|R2|0,04|0,04|9,04|15%|
|R3|0,01|0,01|9,01|15%|
|R4|0,03|0,03|9,03|15%|

Fuente: Elaboración propia.

**5.3.** **Curvas de Isoconcentración - Fase de Construcción**

En las siguientes figuras se presentan las curvas de isoconcentración obtenidas para los contaminantes

atmosféricos modelados para la fase de construcción del Proyecto. En todas las figuras se puede observar

que el impacto sobre la calidad del aire se acota al área circundante al Proyecto debido, principalmente, a

la baja magnitud de las emisiones.

Página | 28

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-2 Curvas de Isoconcentración - MP10 24 horas Percentil 98**

Fuente: Elaboración propia.

Página | 29

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-3 Curvas de Isoconcentración - MP10 concentración anual**

Fuente: Elaboración propia.

Página | 30

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-4 Curvas de Isoconcentración - MP2,5 24 horas Percentil 98**

Fuente: Elaboración propia.

Página | 31

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-5 Curvas de Isoconcentración - MP2,5 Anual**

Fuente: Elaboración propia.

Página | 32

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-6 Curvas de Isoconcentración - NO** **2** **1 hora Percentil 99**

Fuente: Elaboración propia.

Página | 33

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-7 Curvas de Isoconcentración - NO** **2** **Anual**

Fuente: Elaboración propia.

Página | 34

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-8 Curvas de Isoconcentración - SO** **2** **1 hora Percentil 98,5**

Fuente: Elaboración propia.

Página | 35

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-9 Curvas de Isoconcentración - SO** **2** **24 horas Percentil 99**

Fuente: Elaboración propia.

Página | 36

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 5-10 Curvas de Isoconcentración - SO** **2** **concentración anual**

Fuente: Elaboración propia.

Página | 37

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**5.4.** **MATERIAL PARTICULADO SEDIMENTABLE**

En el caso del material particulado sedimentable generado en la fase de construcción, se obtiene que en

el punto de máximo impacto el promedio anual alcanza un valor de 0,0013 μg/m [2] - s, equivalente a 0,11

mg/m [2] - d.

Siendo la norma anual de 100 mg/m [2] - d según el Decreto Exento N° 4/1992 del Ministerio de Agricultura

que establece la Norma de calidad del aire para MPS en la cuenca del río Huasco, III Región, el aporte del

Proyecto es bajo (0,11% de la norma) por lo que no generaría un impacto significativo sobre los recursos

naturales que se encuentren dentro del área de influencia del Proyecto. Las curvas de isodeposición anual

de MPS se presentan en la Figura 5-11.

**Figura 5-11 Curvas de isodeposición MPS anual - Fase de Construcción.**

Fuente: Elaboración propia.

Página | 38

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**6.** **ÁREA DE INFLUENCIA**

De manera preliminar, y con el fin de mostrar el área en la que el Proyecto genera un mayor impacto, se

ha definido como área de influencia aquella superficie en que el aporte del Proyecto, para un

contaminante determinado, presenta concentraciones superiores al 1% de la norma. Las concentraciones

equivalentes al 1% de cada norma se presentan en la Tabla 6-1. En el caso del SO 2, el aporte es tan bajo

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Figura 6-9, correspondiente al área de influencia del NO 2 concentración 1 hora, dado que es la curva que involucra una mayor superficie (4,0 km [2] ) y permite establecer el escenario más conservador. -->

**Tabla 6-1: Concentración equivalente al 1% de la norma****

| Contaminante | Norma | Valor Norma<br>(μg/Nmɜ) | 1% de la norma (μg/Nmɜ) |
| --- | --- | --- | --- |
| MP10 | 24 horas Percentil 98 | 150 | 1,5 |
| MP10 | Anual | 50 | 0,5 |
| MP2,5 | 24 horas Percentil 98 | 50 | 0,5 |
| MP2,5 | Anual | 20 | 0,2 |
| NO2 | 1 hora Percentil 99 | 400 | 4,0 |
| NO2 | Anual | 100 | 1,0 |
| CO | 1 hora Percentil 99 | 30.000 | 300,0 |
| CO | 8 horas Percentil 99 | 10.000 | 100,0 |
| SO2 | 1 hora Percentil 98,5 | 350 | 3,5 |
| SO2 | 24 horas Percentil 99 | 150 | 1,5 |
| SO2 | Anual | 60 | 0,6 |
| SO2 | 1 hora Percentil 99,73 | 1.000 | 10 |
| SO2 | 24 horas Percentil 99,7 | 365 | 3,65 |
| SO2 | Anual | 80 | 0,8 |

<!-- Estadísticas: 14 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Página | 39 -->
<!-- FIN TABLA 6-1 -->


que en ningún punto del dominio de modelación la concentración alcanza el 1% de sus respectivas normas.

Las áreas de influencia obtenidas se presentan desde la Figura 6-1 a la Figura 6-8.

Finalmente, se define como área de influencia del Proyecto para la componente aire, la presentada en la

Figura 6-9, correspondiente al área de influencia del NO 2 concentración 1 hora, dado que es la curva que

involucra una mayor superficie (4,0 km [2] ) y permite establecer el escenario más conservador.

**Tabla 6-1 Concentración equivalente al 1% de la norma**

|Contaminante|Norma|Valor Norma<br>(μg/Nmɜ)|1% de la norma (μg/Nmɜ)|
|---|---|---|---|
|MP10|24 horas Percentil 98|150|1,5|
|MP10|Anual|50|0,5|
|MP2,5|24 horas Percentil 98|50|0,5|
|MP2,5|Anual|20|0,2|
|NO2|1 hora Percentil 99|400|4,0|
|NO2|Anual|100|1,0|
|CO|1 hora Percentil 99|30.000|300,0|
|CO|8 horas Percentil 99|10.000|100,0|
|SO2|1 hora Percentil 98,5|350|3,5|
|SO2|24 horas Percentil 99|150|1,5|
|SO2|Anual|60|0,6|
|SO2|1 hora Percentil 99,73|1.000|10|
|SO2|24 horas Percentil 99,7|365|3,65|
|SO2|Anual|80|0,8|

Fuente: Elaboración propia.

Página | 39

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 6-1 Área de influencia - Concentración MP10 24 horas Percentil 98.**

Fuente: Elaboración propia.

**Figura 6-2 Área de influencia - Concentración MP10 Anual.**

Fuente: Elaboración propia.

Página | 40

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 6-3 Área de influencia - Concentración MP2,5 24 horas Percentil 98**

Fuente: Elaboración propia.

**Figura 6-4 Área de influencia - Concentración MP2,5 Anual.**

Fuente: Elaboración propia.

Página | 41

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 6-5 Área de influencia - Concentración NO** **2** **1 hora Percentil 99.**

Fuente: Elaboración propia.

**Figura 6-6 Área de influencia - Concentración NO** **2** **Anual**

Fuente: Elaboración propia.

Página | 42

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 6-7 Área de influencia - Concentración CO 1 hora Percentil 99**

Fuente: Elaboración propia.

**Figura 6-8 Área de influencia - Concentración CO 8 horas Percentil 99**

Fuente: Elaboración propia.

Página | 43

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**Figura 6-9 Área de influencia del Proyecto para la componente aire**

Fuente: Elaboración propia.

Página | 44

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

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

El modelo de calidad del aire desarrollado para evaluar el impacto del proyecto DIA “Edificio Makroplaza”

considera las emisiones que se generarán durante el primer año de su construcción, dado que corresponde

a la etapa del Proyecto en donde se produce el escenario más desfavorable desde el punto de vista de la

calidad del aire. Las emisiones atmosféricas obtenidas para el Año 1 de la fase de construcción y cuya

dispersión se describe en el presente documento, se resumen a continuación:

 - 11,0 toneladas de MPS

 - 3,1 toneladas de MP10,

 - 1,2 toneladas de MP2,5,

 - 2,6 toneladas de CO,

 - 10,8 toneladas de NO 2, y

 - 0,1 toneladas de SO 2 .

El análisis de los resultados de la modelación, indica que las concentraciones proyectadas para el área

donde se emplazará el Proyecto cumplen con toda la normativa primaria y secundaria de calidad del aire

vigente en el territorio nacional (Decretos del MINSEGPRES: D.S. N°114/02 para NO 2, D.S. N° 20/13 para

MP10 y D.S. N°115/02 para CO, D.S. N° 12/11, D.S. N°104/2018 para SO 2 D.E. N°4/92 del Ministerio de

Página | 45

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

Agricultura para MPS), tanto en los receptores (discretos y adyacentes) como en los puntos de máximo

impacto, para los cinco contaminantes analizados.

Expuesto lo anterior, y tomando en cuenta que las actividades de construcción son transitorias, se puede

concluir que el desarrollo del proyecto DIA “Edificio Makroplaza” no afectará la salud de la población ni

los recursos naturales que se encuentran dentro del área de influencia definida para esta componente

ambiental, dado que no se sobrepasa ninguna de las normas vigentes de calidad del aire aplicables al

Proyecto.

Kisi Valeska Cerda Palma

Ingeniero Civil Ambiental

Página | 46

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**8.** **BIBLIOGRAFÍA**

_Guía para el uso de modelos de calidad del aire en el SEIA_ . Servicio de Evaluación Ambiental. Ministerio de

Medio Ambiente, 2012.

_Informe Línea de Base de Calidad del Aire en la Región de Valparaíso. Periodo 2017-2019_ . SEREMI de Medio

Ambiente de la Región de Valparaíso, 2020.

Página | 47

INFORME DE MODELACIÓN DE CALIDAD DEL AIRE
DECLARACIÓN DE IMPACTO AMBIENTAL MAKROPLAZA

_____________________________________________________________________________________________________________________

**9.** **ANEXO A ARCHIVOS DE ENTRADA Y SALIDA DEL MODELO (DIGITAL)**

Página | 48

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1: Ubicación de la estación Junta de Vecinos****

| Coordenadas UTM | Col2 | Distancia al Proyecto<br>(km) | Altura sobre el nivel del mar<br>(m) |
| --- | --- | --- | --- |
| **X (m)** | **Y (m)** | **Y (m)** | **Y (m)** |
| 263.872 | 6.353.054 | 2,6 | 81 |

**Tabla 2-2: Validez de registros meteorológicos - Año 2020.****

| Variable | N° Registros Válidos | % Registros Válidos |
| --- | --- | --- |
| Velocidad del Viento | 8.769 | 99,87% |
| Dirección del Viento | 8.769 | 99,87% |

**Tabla 2-3: Distribución de frecuencias (%) - Estación Junta de Vecinos 2020****

| Dirección del Viento | Rango de Velocidad (m/s) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección del Viento** | **0,5 - 2,1** | **2,1 - 3,6** | **3,6 - 5,7** | **5,7 - 8,8** | **8,8 - 11,1** | **>= 11,10** | **Total (%)** |
| N | 4,6 | 1,2 | 0,3 | 0,0 | 0,0 | 0,0 | 6,0 |
| NNE | 3,8 | 0,7 | 0,0 | 0,0 | 0,0 | 0,0 | 4,5 |
| NE | 1,7 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 1,7 |
| ENE | 1,1 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 1,1 |
| E | 3,8 | 0,1 | 0,0 | 0,0 | 0,0 | 0,0 | 3,9 |
| ESE | 5,0 | 0,4 | 0,0 | 0,0 | 0,0 | 0,0 | 5,4 |
| SE | 6,2 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 6,2 |
| SSE | 4,6 | 0,4 | 0,0 | 0,0 | 0,0 | 0,0 | 4,9 |
| S | 7,3 | 0,8 | 0,5 | 0,0 | 0,0 | 0,0 | 8,6 |
| SSW | 2,0 | 0,6 | 0,2 | 0,0 | 0,0 | 0,0 | 2,7 |
| SW | 2,1 | 3,4 | 0,8 | 0,0 | 0,0 | 0,0 | 6,3 |
| WSW | 2,7 | 2,6 | 0,0 | 0,0 | 0,0 | 0,0 | 5,4 |
| W | 3,4 | 2,8 | 0,0 | 0,0 | 0,0 | 0,0 | 6,2 |
| WNW | 3,2 | 2,4 | 0,0 | 0,0 | 0,0 | 0,0 | 5,6 |
| NW | 7,0 | 5,1 | 0,3 | 0,0 | 0,0 | 0,0 | 12,4 |
| NNW | 6,1 | 1,5 | 0,4 | 0,0 | 0,0 | 0,0 | 8,0 |
| Sub-Total | 64,6 | 21,8 | 2,6 | 0,0 | 0,0 | 0,0 | 89,0 |
| Calmas (%) | Calmas (%) | Calmas (%) | Calmas (%) | Calmas (%) | Calmas (%) | Calmas (%) | 10,8 |
| Sin dato (%) | Sin dato (%) | Sin dato (%) | Sin dato (%) | Sin dato (%) | Sin dato (%) | Sin dato (%) | 0,2 |
| Total (%) | Total (%) | Total (%) | Total (%) | Total (%) | Total (%) | Total (%) | 100 |

**Tabla 3-2: Error Cuadrático Medio, Sesgo y Coeficiente de Correlación del ciclo diario de Velocidad del Viento.****

| Estadístico | Valor |
| --- | --- |
| Error cuadrático Medio (m/s) | 0,42 |
| Sesgo (m/s) | 0,40 |
| Coeficiente de Correlación | 0,99 |

**Tabla 3-3: Características del dominio de modelación****

| Coordenadas del centro (m)<br>(DATUM WGS84 18H) | X = 262.211<br>Y = 6.350.275 |
| --- | --- |
| **Tamaño** | 50 km x 50 km |
| **Resolución** | 1 km |
| **N° de receptores** | 2.500 |

**Tabla 3-5: Emisiones totales de contaminantes atmosféricos - Año 1 Fase de construcción****

| Actividad | Emisiones - Fase de construcción Año 1 (kg/año) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MPS** | **MP10** | **MP2,5** | **CO** | **NOx** | **SOx** | **COV/HC** |
| Escarpe | 16,4 | 16,4 | 16,4 | - | - | - | - |
| Excavaciones | 560,5 | 69,0 | 58,8 | - | - | - | - |
| Transferencia de Material | 75,4 | 35,7 | 5,4 | - | - | - | - |
| Resuspensión en caminos<br>pavimentados | 6.744,2 | 1.294,6 | 313,2 | - | - | - | - |
| Resuspensión en caminos internos no<br>pavimentados | 900,2 | 183,5 | 18,4 | - | - | - | - |
| Resuspensión en caminos públicos no<br>pavimentados | 1.937,7 | 724,3 | 72,4 | - | - | - | - |
| Combustión de motores de vehículos<br>- Caminos pavimentados | 40,2 | 40,2 | 40,2 | 468,0 | 2.018,8 | 51,2 | 85,1 |
| Combustión de motores de vehículos<br>- Caminos no pavimentados públicos | 0,2 | 0,2 | 0,2 | 2,5 | 8,8 | 0,2 | 0,6 |
| Combustión de motores de vehículos<br>- Caminos no pavimentados internos | 4,6 | 4,6 | 4,6 | 49,9 | 175,1 | 4,5 | 11,2 |
| Combustión maquinaria fuera de ruta | 709,6 | 709,6 | 709,6 | 2.050,9 | 8.598,1 | 10,4 | 928,7 |
| Grupos electrógenos | 2,5 | 2,5 | 2,5 | 7,6 | 33,8 | 2,3 | - |
| **Total (kg/año)** | **10.991** | **3.081** | **1.242** | **2.579** | **10.834** | **69** | **1.026** |
| **Total (ton/año)** | **11,0** | **3,1** | **1,2** | **2,6** | **10,8** | **0,1** | **1,0** |

**Tabla 3-6: Superficie y emisiones agrupadas por fuente****

| Fuente | Área fuente en el<br>modelo (m2) | Emisiones - Fase de construcción Año 1 (kg/año) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **Área fuente en el**<br>**modelo (m2)** | **MPS** | **MP10** | **MP2,5** | **CO** | **NOx** | **SOx** |
| Proyecto | 6.564 | 3.753 | 1.389 | 1.140 | 2.704 | 10.307 | 461 |
| Caminos pavimentados | 164.696 | 5.633 | 1.108 | 293 | 389 | 1.676 | 42 |
| Caminos no pavimentados públicos | 400 | 5.131 | 1.841 | 188 | 45 | 171 | 4 |
| **Total (kg/año)** | **Total (kg/año)** | **14.517** | **4.338** | **1.622** | **3.138** | **12.155** | **508** |

**Tabla 5-1: Aporte del Proyecto en Puntos de Máximo Impacto - Fase de construcción Año 1****

| Norma de calidad del aire | Valor Norma<br>(μg/Nmɜ) | Concentración<br>(μg/Nmɜ) | Aporte respecto a<br>norma % |
| --- | --- | --- | --- |
| MP10 24 horas Per98 | 150 | 9,27 | 6,18% |
| MP10 Anual | 50 | 3,97 | 7,95% |
| MP2,5 24 horas Per98 | 50 | 7,32 | 14,63% |
| MP2,5 Anual | 20 | 3,14 | 15,71% |
| NO2 1 hora Per99 | 400 | 227,93 | 56,98% |
| NO2 Anual | 100 | 33,10 | 33,10% |
| CO 1 hora Per99 | 30.000 | 54,67 | 0,18% |
| CO 8 horas Per99 | 10.000 | 35,85 | 0,36% |
| SO2 1 hora Per98,5 | 350 | 0,32 | 0,09% |
| SO2 24 horas Per99 | 150 | 0,13 | 0,09% |
| SO2 Anual | 60 | 0,05 | 0,09% |
| SO2 1 hora Per99,7 | 1.000 | 0,44 | 0,04% |
| SO2 24 horas Per99,7 | 365 | 0,17 | 0,05% |
| SO2 Anual | 80 | 0,05 | 0,06% |

**Tabla 5-3: Análisis normativo en Puntos de Máximo Impacto - Fase de construcción Año 1****

| Norma | Valor Norma<br>(μg/Nmɜ) | Aporte proyecto<br>en PMI (μg/Nmɜ) | Línea de Base<br>(μg/Nmɜ) | Total<br>(μg/Nmɜ) | % Respecto a<br>norma |
| --- | --- | --- | --- | --- | --- |
| MP10 24 horas Per98 | 150 | 9,27 | 64 | 73,27 | 49% |
| MP10 Anual | 50 | 3,97 | 37 | 40,97 | 82% |
| SO2 1 hora Per98,5 | 350 | 0,32 | 33 | 33,32 | 10% |
| SO2 24 horas Per99 | 150 | 0,13 | 31 | 31,13 | 21% |
| SO2 Anual | 60 | 0,05 | 9 | 9,05 | 15% |

**Tabla 5-4: Aporte del Proyecto en Receptores Discretos - Fase de construcción Año 1****

| Norma | Valor norma<br>(μg/Nmɜ) | Aporte del Proyecto en Receptores Discretos - Fase<br>de construcción Año 1 (μg/Nmɜ) | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Norma** | **Valor norma**<br>**(μg/Nmɜ)** | **R1** | **R2** | **R3** | **R4** |
| MP10 24 horas Per98 | 150 | 9,27 | 7,33 | 2,83 | 5,52 |
| MP10 Anual | 50 | 3,97 | 3,39 | 1,02 | 1,89 |
| MP2,5 24 horas Per98 | 50 | 7,32 | 5,83 | 2,21 | 4,39 |
| MP2,5 Anual | 20 | 3,14 | 2,69 | 0,78 | 1,48 |
| NO2 1 hora Per99 | 400 | 227,93 | 153,01 | 104,63 | 129,08 |
| NO2 Anual | 100 | 33,10 | 28,37 | 8,14 | 15,61 |
| CO 1 hora Per99 | 30.000 | 54,67 | 36,55 | 25,09 | 30,92 |
| CO 8 horas Per99 | 10.000 | 35,85 | 24,59 | 11,10 | 18,03 |
| SO2 1 horas Per98,5 | 350 | 0,32 | 0,22 | 0,13 | 0,17 |
| SO2 24 horas Per99 | 150 | 0,13 | 0,10 | 0,05 | 0,08 |
| SO2Anual | 60 | 0,05 | 0,04 | 0,01 | 0,03 |
| SO2 1 hora Per99,7 | 1.000 | 0,44 | 0,27 | 0,24 | 0,27 |
| SO2 24 horas Per99,7 | 365 | 0,17 | 0,10 | 0,05 | 0,10 |
| SO2 Anual | 60 | 0,05 | 0,04 | 0,01 | 0,03 |

**Tabla 5-5: Aporte del Proyecto en Receptores Discretos con respecto a la norma (%) - Fase de construcción Año 1****

| Norma | Aporte del Proyecto en Receptores Discretos con respecto a la norma<br>(%) - Fase de construcción Año 1 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Norma** | **R1** | **R2** | **R3** | **R4** |
| MP10 24 horas Per98 | 6,18% | 4,89% | 1,89% | 3,68% |
| MP10 Anual | 7,95% | 6,79% | 2,04% | 3,79% |
| MP2,5 24 horas Per98 | 14,63% | 11,67% | 4,41% | 8,78% |
| MP2,5 Anual | 15,71% | 13,43% | 3,90% | 7,40% |
| NO2 1 hora Per99 | 56,98% | 38,25% | 26,16% | 32,27% |
| NO2 Anual | 33,10% | 28,37% | 8,14% | 15,61% |
| CO 1 hora Per99 | 0,18% | 0,12% | 0,08% | 0,10% |
| CO 8 horas Per99 | 0,36% | 0,25% | 0,11% | 0,18% |
| SO2 1 horas Per98,5 | 0,09% | 0,06% | 0,04% | 0,05% |
| SO2 24 horas Per99 | 0,09% | 0,06% | 0,03% | 0,05% |
| SO2Anual | 0,09% | 0,07% | 0,02% | 0,04% |
| SO2 1 hora Per99,7 | 0,04% | 0,03% | 0,02% | 0,03% |
| SO2 24 horas Per99,7 | 0,05% | 0,03% | 0,01% | 0,03% |
| SO2 Anual | 0,06% | 0,05% | 0,02% | 0,03% |

**Tabla 5-6: Análisis normativo en receptores discretos - Concentración diaria MP10****

| Receptor | MP10 24 horas Percentil 98 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **Aporte Proyecto**<br>**(μg/Nmɜ)** | **Línea de Base**<br>**(μg/Nmɜ)** | **Concentración total**<br>**(μg/Nmɜ)** | **% Norma** |
| R1 | 9,3 | 64,0 | 73,3 | 49% |
| R2 | 7,3 | 7,3 | 71,3 | 48% |
| R3 | 2,8 | 2,8 | 66,8 | 45% |
| R4 | 5,5 | 5,5 | 69,5 | 46% |

**Tabla 5-7: Análisis normativo en receptores discretos - Concentración anual MP10****

| Receptor | MP10 anual | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **Aporte Proyecto**<br>**(μg/Nmɜ)** | **Línea de Base**<br>**(μg/Nmɜ)** | **Concentración total**<br>**(μg/Nmɜ)** | **% Norma** |
| R1 | 4,0 | 37,0 | 41,0 | 82% |
| R2 | 3,4 | 3,4 | 40,4 | 81% |
| R3 | 1,0 | 1,0 | 38,0 | 76% |
| R4 | 1,9 | 1,9 | 38,9 | 78% |

**Tabla 5-8: Análisis normativo en receptores discretos - Concentración horaria SO** **2****

| Receptor | SO2 1 hora Percentil 98,5 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **Aporte Proyecto**<br>**(μg/Nmɜ)** | **Línea de Base**<br>**(μg/Nmɜ)** | **Concentración total**<br>**(μg/Nmɜ)** | **% Norma** |
| R1 | 0,32 | 33,0 | 33,32 | 10% |
| R2 | 0,22 | 0,22 | 33,22 | 9% |
| R3 | 0,13 | 0,13 | 33,13 | 9% |
| R4 | 0,17 | 0,17 | 33,17 | 9% |

**Tabla 5-9: Análisis normativo en receptores discretos - Concentración diaria SO** **2****

| Receptor | SO2 24 horas Percentil 99 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **Aporte Proyecto**<br>**(μg/Nmɜ)** | **Línea de Base**<br>**(μg/Nmɜ)** | **Concentración total**<br>**(μg/Nmɜ)** | **% Norma** |
| R1 | 0,13 | 31,0 | 31,13 | 21% |
| R2 | 0,10 | 0,10 | 31,10 | 21% |
| R3 | 0,05 | 0,05 | 31,05 | 21% |
| R4 | 0,08 | 0,08 | 31,08 | 21% |

**Tabla 5-10: Análisis normativo en receptores discretos - Concentración anual SO** **2****

| Receptor | SO2 Anual | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **Aporte Proyecto**<br>**(μg/Nmɜ)** | **Línea de Base**<br>**(μg/Nmɜ)** | **Concentración total**<br>**(μg/Nmɜ)** | **% Norma** |
| R1 | 0,05 | 9 | 9,05 | 15% |
| R2 | 0,04 | 0,04 | 9,04 | 15% |
| R3 | 0,01 | 0,01 | 9,01 | 15% |
| R4 | 0,03 | 0,03 | 9,03 | 15% |
