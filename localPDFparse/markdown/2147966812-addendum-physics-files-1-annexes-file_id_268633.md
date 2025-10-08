---
title: Sin título
author: Adrián González
date: D:20210112164820-03'00'
language: es
type: report
pages: 41
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO: P6260B Anexos Meteorológicos - Estudio de Impacto Odorante SOLICITANTE: Agrícola Sun Ltda.
  - Fecha: Enero 2021 At: Sr. Henry Gálvez
-->

# PROYECTO: P6260B Anexos Meteorológicos - Estudio de Impacto Odorante SOLICITANTE: Agrícola Sun Ltda.

# Fecha: Enero 2021 At: Sr. Henry Gálvez

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 2 de 41

Anexos Meteorológicos de Estudio de Impacto Odorante
Nombre Reporte:
AGRÍCOLA SUN LTDA - Planta Sunsweet

Reporte no: Final 1.0

Código de proyecto: P 6260B

Modelo de dispersión, WRF, series de pronóstico, meteorología
Palabras clave:
observada, meteorología de pronóstico, campos de viento

Preparado a petición de: WSP Ambiental S.A.

Contacto: Sr. Henry Gálvez - Jefe de proyectos

Preparado por:

Envirometrika
Europa 2066 - Providencia - Santiago - Chile  56 2 2668 1260
Arturo Prat 199 -Torre A of 1401 Concepción  56 41 383 3978
[e-mail: info@envirometrika.com](mailto:info@envirometrika.com)
[www.envirometrika.com](http://www.envirometrika.com/)

Autores: Ricardo Guerra

Firmado y aprobado por: Envirometrika por Vania Zorich

Fecha: Enero 2020

www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 3 de 41

**ÍNDICE**

ÍNDICE ......................................................................................................................................................... 3
1 ANEXO 1 - ANÁLISIS METEOROLÓGICO .................................................................................................. 5
1.1 Rosas y campos de viento ............................................................................................................... 6
1.2 Altura de mezcla........................................................................................................................... 12
2 ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE ............................................................................................ 14
2.1 Levantamiento y selección de información meteorológica observada................................................ 15
2.2 Diagnóstico de datos meteorológicos ............................................................................................. 16
2.2.1 Datos meteorológicos ................................................................................................................ 16
2.2.2 Ciclos diarios ............................................................................................................................ 20
2.3 Comparación entre pronóstico y observaciones .............................................................................. 28
2.3.1 Análisis cualitativo de serie de pronóstico y observada ................................................................ 28
2.3.2 Análisis cuantitativo de serie de pronóstico y observada .............................................................. 33
3 ANÁLISIS DE RESULTADOS ................................................................................................................... 34
4 BIBLIOGRAFÍA ..................................................................................................................................... 35
5 ANEXO 3 - PARAMETRIZACIÓN METEOROLOGÍA DE PRONÓSTICO ........................................................ 36

5.1 Namelist WPS ............................................................................................................................... 36
5.2 Namelist Input ............................................................................................................................. 37
6 ANEXO 4 - JUSTIFICACIÓN BASE METEOROLÓGICA DE PRONÓSTICO .................................................... 40
6.1 Aplicabilidad del modelo................................................................................................................ 40
6.2 Aplicabilidad de meteorología de pronóstico ................................................................................... 41

**ÍNDICE TABLAS**
Tabla 1 - Coordenadas representativas de Sunsweet Santa Cruz ..................................................................... 5
Tabla 2 - Descripción de ciclos de análisis meteorológicos ............................................................................... 5
Tabla 3 - Rosas y campos de viento pronóstico anual ..................................................................................... 6
Tabla 4 - Rosas y campos de viento pronóstico estacional - Verano ................................................................ 7
Tabla 5 - Rosas y campos de viento pronóstico estacional - Otoño .................................................................. 8
Tabla 6 - Rosas y campos de viento pronóstico estacional - Invierno ............................................................... 9
Tabla 7 - Rosas y campos de viento pronóstico estacional - Primavera .......................................................... 10
Tabla 8 - Registro de ortofotografías - Isolíneas de altura de mezcla ............................................................. 13
Tabla 9 - Altura de mezcla - promedios por periodo estacional y horario [m] ................................................. 13
Tabla 10 - Estaciones meteorológicas superficiales en el dominio de modelación WRF .................................... 15
Tabla 11 - Coordenada de localización, serie de pronóstico WRF ................................................................... 16
Tabla 12 - Coordenada de localización estación meteorológica ...................................................................... 16
Tabla 13 - Porcentaje datos válidos en parámetros evaluados ....................................................................... 17
Tabla 14 - Ciclos diarios de la temperatura - serie pronóstico ........................................................................ 20
Tabla 15 - Ciclos diarios de la temperatura - serie observada ........................................................................ 21
Tabla 16 - Ciclos diarios promedios serie pronóstico ..................................................................................... 22
Tabla 17 - Ciclos diarios promedios serie observada...................................................................................... 23
Tabla 18 - Ciclos diarios de dirección del viento serie pronóstico .................................................................... 24
Tabla 19 - Ciclos diarios de dirección del viento serie observada .................................................................... 25
Tabla 20 - Frecuencia mensual de vientos calmos - serie pronóstico .............................................................. 26
Tabla 21 - Frecuencia horaria de vientos calmos - serie pronóstico ................................................................ 26
Tabla 22 - Frecuencia mensual de vientos calmos - serie observada .............................................................. 27

Tabla 23 - Frecuencia horaria de vientos calmos - serie observada ................................................................ 27
Tabla 24 - Error medio cuadrático, sesgo, coeficiente de correlación, IOA, velocidad del viento y temperatura . 33

ÍNDICE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 4 de 41

**ÍNDICE GRÁFICOS**
Gráfico 1 - Altura de mezcla y temperatura - Serie de tiempo ....................................................................... 13
Gráfico 2 - Serie pronóstico, temperatura [°C] .............................................................................................. 18
Gráfico 3 - Serie observada, temperatura [°C] .............................................................................................. 18
Gráfico 4 - Serie pronóstico, velocidad del viento [m/s] ................................................................................. 19
Gráfico 5 - Serie observada, velocidad del viento [m/s] ................................................................................. 19
Gráfico 6 - Ciclos diarios promedios de la temperatura - serie pronóstico ....................................................... 20
Gráfico 7 - Ciclos diarios promedios de la temperatura - serie observada ....................................................... 21
Gráfico 8 - Ciclos diarios promedios de velocidad del viento - serie pronóstico ................................................ 22
Gráfico 9 - Ciclos diarios promedios de velocidad del viento - serie observada ................................................ 23
Gráfico 10 - Ciclos diarios de dirección del viento - serie pronóstico ............................................................... 24
Gráfico 11 - Ciclos diarios de dirección del viento - serie observada ............................................................... 25
Gráfico 12 - Ciclos diarios promedios de temperatura, serie pronóstico y observado. ...................................... 28
Gráfico 13 - Ciclos diarios promedios de velocidad del viento, serie pronóstico y observada ............................ 29
Gráfico 14 - Distribución anual de frecuencia de velocidad del viento serie pronóstico y observada. ................. 29
Gráfico 15 - Ciclos diarios de variación del viento, serie pronóstico ................................................................ 30
Gráfico 16 - Ciclos diarios de variación del viento, serie observada ................................................................ 30
Gráfico 17 - Rosas de viento anual por periodo horario, serie pronóstico y observada ..................................... 31
Gráfico 18 - Rosas de viento anual por periodo estacional, serie pronóstico y observada. ................................ 32

**ÍNDICE FIGURAS**
Figura 1 - Comportamiento de campos de viento .......................................................................................... 11
Figura 2 - Distribución general de altura de mezcla (ortofotografías) ............................................................. 12
Figura 3 - Localización de estación meteorológica ......................................................................................... 17
Figura 4 - Visualización de dominios anidados WRF ...................................................................................... 39

ÍNDICE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 5 de 41

**1** **ANEXO 1 - ANÁLISIS METEOROLÓGICO**

La evaluación del comportamiento de los parámetros meteorológicos y su interacción a nivel local, se realizó a
partir de series de datos horarios para el periodo de un año, extraídas desde la grilla meteorológica de pronóstico
WRF-MMIF’19. Cuya extracción fue en base a coordenadas representativas de la instalación, donde se localizan
las fuentes de emisión consideradas en el presente estudio.

Tabla 1 - Coordenadas representativas de Sunsweet Santa Cruz

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|X: Este|Y: Sur|Huso|Datum|
|288.373|6.164.479|19 Sur|WGS-84|

Los parámetros meteorológicos considerados fueron:

 - Velocidad del viento [m/s].

 Dirección del viento [grados].

 - Altura de capa de mezcla [m].

 - Temperatura [°C].

El análisis se realizó bajo el formato de:

 Rosas de viento y gráficos de distribución de velocidad del viento.

 - Campos de viento.

 - Altura de capa de mezcla.

Los resultados se analizaron de acuerdo al comportamiento anual, estacional y horario. La descripción de cada
ciclo se indica en la siguiente tabla:

Tabla 2 - Descripción de ciclos de análisis meteorológicos

|Ciclo|Descripción|Col3|
|---|---|---|
|Anual|12 meses|Enero a diciembre|
|Estacional|Verano|22 de diciembre a 21 de marzo|
|Estacional|Otoño|22 de marzo a 21 de junio|
|Estacional|Invierno|22 de junio a 21 de septiembre|
|Estacional|Primavera|22 de septiembre a 21 de diciembre|
|Horario|Nocturno|00:00 a 06:59|
|Horario|AM|07:00 a 14:59|
|Horario|PM|15:00 a 23:59|

La evaluación de campos de viento incluyó antecedentes bibliográficos topoclimáticos que describen la dinámica
y cinética de las masas de aire que interactúan en la zona de estudio. Esta información permite evaluar la
coherencia de las series de datos obtenidas de la meteorología de pronóstico e interpretar las variables de
influencia en las condiciones de dispersión.

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 6 de 41

**1.1** **Rosas y campos de viento**

Los campos de viento están determinados por la velocidad del viento y las componentes vectoriales de
dirección, producto del comportamiento dinámico de las masas de aire. La interacción de estas componentes
caracteriza el comportamiento del viento y cómo intervienen en la dispersión de contaminantes en el área de
interés.

Tabla 3 - Rosas y campos de viento pronóstico anual

|Col1|Rosa de vientos|Col3|Distribución de velocidad del viento|Características|
|---|---|---|---|---|
|Anual Nocturno|||<br>12,84<br>23,33<br>33,78<br>22,27<br>5,60<br>1,41<br>0,39<br>0,12<br>0,20<br>0,08<br>0<br>10<br>20<br>30<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de vientos predominaron desde la<br>dirección ESE con un 30% de la frecuencia.<br>La velocidad varió de ventolina1 a brisa débil. La<br>distribución del viento tuvo una tendencia<br>asimétrica positiva. <br> <br>Velocidad promedio de viento: 1,51 [m/s].<br> <br>Frecuencia de vientos calmos: 12,84%.|
|Anual AM|||<br>12,98<br>14,90<br>23,87<br>19,18<br>15,21<br>10,07<br>2,77<br>0,51<br>0,31<br>0,21<br>0<br>10<br>20<br>30<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron en mayor<br>frecuencia desde el rango ESE-SE, con un 49%<br>de la frecuencia.<br>La velocidad varió de calma a brisa moderada2.<br>Respecto a la distribución de los vientos, éstos<br>tuvieron una tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,14 [m/s].<br> <br>Frecuencia de vientos calmos: 12,98%.|
|Anual PM|||<br>10,41<br>17,23<br>28,80<br>21,19<br>11,72<br>6,48<br>2,74<br>0,88<br>0,33<br>0,21<br>0<br>10<br>20<br>30<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario PM, se observó una<br>predominancia de los vientos desde los rangos E-<br>ESE y OSO-O, con un 27% y 25% de la frecuencia<br>respectivamente. La velocidad de los vientos<br>varió de ventolina a brisa débil3.<br>La distribución de los vientos se observó con una<br>tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,02 [m/s]<br> <br>Frecuencia de vientos calmos: 10,41%|

Fuente: Envirometrika, 2020.

Del análisis meteorológico anual WRF-MMIF’19 se resume que:
Las masas de aire describieron un comportamiento homogéneo en cuando a la variable direccional del viento,
siendo predominante la dirección ESE, principalmente en horarios Nocturno y AM. En cuanto a la velocidad
del viento, está osciló principalmente de brisa muy débil a débil, con intensidades promedio cercanas a 2

[m/s]. Respecto a los vientos calmos, la mayor frecuencia se presentaría en horario nocturno y AM.

1 Organización Meteorológica Mundial (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A - Claves alfanuméricas - Escala

Beaufort de Viento. OMM-N°306, Suiza: OMM.
2 Ibíd.
3 Ibíd.

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 7 de 41

Tabla 4 - Rosas y campos de viento pronóstico estacional - Verano

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Verano Nocturno||||13,02<br>28,89<br>41,43<br>14,29<br>2,38<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|El viento predominó desde la componente ESE,<br>con una frecuencia del 23%.<br>En general, la intensidad del viento se<br>caracterizó por variar de ventolina a brisa muy<br>débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 1,23 [m/s].<br> <br>Frecuencia de vientos calmos: 13,02%.|
|Verano AM||||14,31<br>17,64<br>24,17<br>23,47<br>12,22<br>6,81<br>1,39<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron con mayor<br>frecuencia desde la componente ESE, con un<br>28% de la frecuencia, y en menor medida,<br>desde dirección SE (15%). La velocidad del<br>viento varió de brisa muy débil a moderada. La<br>distribución marcó una tendencia asimétrica<br>positiva.<br> <br>Promedio velocidad del viento: 1,86 [m/s].<br> <br>Frecuencia de vientos calmos: 14,31%.|
|Verano PM||||11,11<br>18,27<br>28,89<br>18,89<br>13,21<br>6,30<br>1,85<br>1,48<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de viento predominaron desde el<br>rango OSO-O, con un 40% de la frecuencia. La<br>intensidad del viento fluctuó de brisa muy débil<br>a moderada. La curva de distribución tuvo una<br>tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 1,96 [m/s].<br> <br>Frecuencia de vientos calmos: 11,11%.|

Sunsweet Santa Cruz
Fuente: Envirometrika, 2020.

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 8 de 41

Tabla 5 - Rosas y campos de viento pronóstico estacional - Otoño

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Otoño Nocturno||||16,30<br>28,42<br>32,14<br>18,17<br>4,04<br>0,93<br>0,00<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de viento provinieron con mayor<br>frecuencia desde la componente ESE (25%) y<br>en menor medida desde la componente ONO<br>(11%). La intensidad del viento se caracterizó<br>como brisa muy débil a débil.<br>La distribución de frecuencia de velocidad del<br>viento muestra una tendencia asimétrica<br>positiva. <br> <br>Promedio velocidad del viento: 1,29 [m/s].<br> <br>Frecuencia de vientos calmos: 16,30%.|
|Otoño AM||||15,76<br>17,53<br>27,04<br>16,58<br>12,77<br>7,74<br>1,22<br>0,41<br>0,54<br>0,41<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|El viento provino con mayor frecuencia desde la<br>componente ESE (31%), y en menor medida,<br>desde SE (12%). La intensidad del viento<br>fluctuó de brisa muy débil a moderada.<br>Respecto a la distribución, ésta tuvo una<br>tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 1,89 [m/s].<br> <br>Frecuencia de vientos calmos: 15,76%.|
|Otoño PM||||13,65<br>18,96<br>32,00<br>21,62<br>7,00<br>3,38<br>1,57<br>0,48<br>0,48<br>0,85<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron en mayor<br>frecuencia desde el rango ESE-SE (32%) y en<br>menor medida desde el rango O-NO (28%). En<br>general, la velocidad del viento se caracterizó<br>como brisa muy débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo un comportamiento asimétrico<br>positivo. <br> <br>Promedio velocidad del viento: 1,76 [m/s].<br> <br>Frecuencia de vientos calmos: 13,65%.|

Sunsweet Santa Cruz
Fuente: Envirometrika, 2020.

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 9 de 41

Tabla 6 - Rosas y campos de viento pronóstico estacional - Invierno

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Invierno Nocturno||||11,65<br>19,41<br>25,16<br>26,24<br>10,87<br>3,88<br>1,40<br>0,31<br>0,78<br>0,31<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario nocturno los vientos<br>provinieron desde la componente ESE (43%).<br>En general, la intensidad del viento osciló de<br>brisa muy débil a moderada.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 1,89 [m/s].<br> <br>Frecuencia de vientos calmos: 11,65%.|
|Invierno AM||||9,65<br>12,09<br>25,00<br>14,27<br>15,08<br>14,81<br>6,66<br>1,36<br>0,68<br>0,41<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron desde las<br>componentes ESE (38%) y SE (20%). La<br>velocidad fluctuó de brisa muy débil a<br>moderada.<br>La<br>intensidad<br>del<br>viento<br>presentó<br>una<br>distribución heterogénea, con una mayor<br>frecuencia entorno al rango de 1-2 [ms]. <br> <br>Promedio velocidad del viento: 2,53 [m/s].<br> <br>Frecuencia de vientos calmos: 9,65%.|
|Invierno PM||||8,82<br>14,73<br>25,60<br>24,15<br>14,01<br>8,70<br>3,50<br>0,36<br>0,12<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de vientos provinieron con mayor<br>frecuencia desde ESE (28%), y en menor<br>medida desde E (17%). En general, la<br>intensidad del viento varió de brisa muy débil a<br>moderada y la distribución se presentó como<br>asimétrico positivo.<br> <br>Promedio velocidad del viento: 2,18 [m/s].<br> <br>Frecuencia de vientos calmos: 8,82%.|

Sunsweet Santa Cruz
Fuente: Envirometrika, 2020.

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 10 de 41

Tabla 7 - Rosas y campos de viento pronóstico estacional - Primavera

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Primavera Nocturno||||10,36<br>16,64<br>36,58<br>30,30<br>5,02<br>0,78<br>0,16<br>0,16<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Predominio de los vientos desde la componente<br>ESE, con una frecuencia del 30%.<br>En general, la velocidad del viento fluctuó de<br>brisa muy débil a moderada.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 1,63 [m/s].<br> <br>Frecuencia de vientos calmos: 10,36%.|
|Primavera AM||||12,23<br>12,36<br>19,23<br>22,53<br>20,74<br>10,85<br>1,79<br>0,27<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron desde la<br>componente ESE, con una frecuencia del 40%.<br>La velocidad del viento osciló de brisa muy débil<br>a moderada.<br>La distribución de frecuencia de velocidad del<br>viento exhibió una curva con tendencia<br>asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,26 [m/s].<br> <br>Frecuencia de vientos calmos: 12,23%.|
|Primavera PM||<br>||8,06<br>16,97<br>28,69<br>20,02<br>12,70<br>7,57<br>4,03<br>1,22<br>0,73<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario PM, los vientos provinieron<br>desde el rango OSO-NO, con una frecuencia del<br>43%.<br>La velocidad del viento varió de brisa muy débil<br>a moderada.<br>Respecto a la distribución de intensidad de<br>vientos, esta presentó un comportamiento<br>asimétrico positivo tendiente a la normalidad.<br> <br>Promedio velocidad del viento: 2,17 [m/s].<br> <br>Frecuencia de vientos calmos: 8,06%.|

Sunsweet Santa Cruz
Fuente: Envirometrika, 2020.

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 11 de 41

Figura 1 - Comportamiento de campos de viento

Fuente: Envirometrika, 2020.

A nivel regional, el área de estudio se localiza en la cuenca hidrográfica del Río Rapel, compuesta
principalmente por las subcuencas de los ríos Cachapoal y Tinguiririca, inserta en la unidad geomorfologica
Llanos de sedimentación fluvial o aluvional. En la región es posible identificar tres unidades de relieve, la
Cordillera de Los Andes, Depresión Intermedia y la Cordillera de la Costa [4] .

En terminos locales, la Comuna de Santa Cruz se ubica en el valle del río Tinguiririca, específicamente en un
sector caracterizado por un relieve que combina, por el norte la Cordillera de la Costa (Angostura de Pelequén)
y la apertura de la Depresión Intermedia [5], conformando un valle originado a partir de material de arrastre
depositado en las riberas de los ríos, esteros y otros cursos de agua, que presenta suelos de riego, planos,
profundos.

El área donde se inserta el proyecto, se inscribe en el tipo climático Templado Mediterráneo, el cual presenta
variaciones por efectos de la topografía local. En la costa se existe mayor nubosidad, mientras que hacia en
interior se experimentan fuertes contrastes térmicos debido a la sequedad de la zona. Las precipitaciones
son mayores en la costa y en la Cordillera de Los Andes, debido al relieve, las temperaturas máximas en
verano superan los 28 [°C] y en invierno las mínimas llegan bajo los 0 [°C] [6] .

La zona además se caracteriza por presentar una estación seca y calurosa de 7 a 8 meses de duración y una
estación fría y lluviosa que se prolonga por 4 a 5 meses. La temperatura media anual oscila entre los 12,5

[°C] y 15 [°C] y el registro de precipitaciones en un año normal oscila entre los 700 y 900 [mm] [7] .

4 Dirección General de Aguas. (2004). Diagnóstico y Clasificación de los Cursos y Cuerpos de Agua según Objetivo de Calidad: Cuenca del Río

Rapel. Ministerio de Obras Públicas. Chile.
5 Ilustre Municipalidad de Santa Cruz (1997). Memoria explicativa Plan Regulador Comunal de Santa Cruz. Chile.
6 Dirección General de Aguas. (2004). Diagnóstico y Clasificación de los Cursos y Cuerpos de Agua según Objetivo de Calidad: Cuenca del Río

Rapel. Ministerio de Obras Públicas. Chile.
7 Centro de Información de Recursos Naturales. (2016). Región del Libertador General Bernardo O’Higgins, Provincia de Colchagua, Comuna

de Santa Cruz: Recursos Naturales y Proyectos. Sistema de Información Territorial Rural. Chile.

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 12 de 41

**1.2** **Altura de mezcla**

La altura de mezcla depende fuertemente del calentamiento superficial, ya que éste determina el ascenso de
las masas de aire (boyancia) y, en consecuencia, la inestabilidad atmosférica que determina la altura a la
cual las emisiones se dispersan. Por esta razón, la variación de la altura de mezcla es de ciclo diario y
estacional.
A continuación, se presentan isolíneas de alturas de mezclas para cuatro períodos estacionales en tres ciclos
horarios, dentro del dominio de modelación.

Figura 2 - Distribución general de altura de mezcla (ortofotografías)

Fuente: Envirometrika, 2020.

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 13 de 41

Los periodos de obtención de las isolíneas de altura de mezcla, desde el modelo de dispersión, se detallan a
continuación:

Tabla 8 - Registro de ortofotografías - Isolíneas de altura de mezcla

Gráfico 1 - Altura de mezcla y temperatura - Serie de tiempo

Fuente: Envirometrika, 2020.

Tabla 9 - Altura de mezcla - promedios por periodo estacional y horario [m]

ANEXO 1 - ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 14 de 41

**2** **ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE**

Los modelos meteorológicos o de calidad del aire utilizados para representar una aproximación a la realidad,
incorporan dentro de sus resultados, incertidumbres. Estas incertidumbres se expresan a través de las diferencias
entre lo estimado y las observaciones (o errores del modelo) [8] .

El objetivo de realizar un análisis de incertidumbre es evaluar la capacidad de un modelo de representar una cierta
situación atmosférica [9] .

Considerando que la meteorología es el componente principal que determina la variabilidad espacial y temporal
de las concentraciones de contaminantes dentro de un dominio específico, es necesario realizar un análisis de
incertidumbre a las variables meteorológicas más relevantes en términos de dispersión como son la velocidad del
viento, la dirección del viento, la temperatura y la humedad relativa [10] . Aunque se debe tener en cuenta que no
siempre es posible contar con registros de las variables más relevantes.
El análisis debiera incorporar incertidumbre de las variables meteorológicas de superficie y de altura, sin embargo,
en Chile, los datos meteorológicos de altura provienen principalmente de los radiosondeos que realiza la Dirección
Meteorológica de Chile (DCM) en Antofagasta, Santo Domingo, Puerto Montt y a Arenas, lugares que se
encuentran fuera del área de modelación en donde se emplaza la zona de estudio y, por lo tanto, no son
representativos de la zona evaluada. Cabe destacar, que, en tales casos, la información de altura medida
representa la estructura vertical de la costa y esta difiere de la continental [11] . Debido a lo anterior, el análisis de
incertidumbre solo aborda las diferencias entre los parámetros meteorológicos superficiales (observado) y lo
modelado (estimado).

El análisis consiste en realizar:

a) **Diagnóstico de datos meteorológicos:** Este diagnóstico tiene por objeto determinar la variabilidad

temporal de cada uno de los parámetros meteorológicos. Debe incluir series de tiempo y ciclos diarios.

b) **Comparación entre pronóstico y observaciones** : La finalidad de esta comparación es determinar

Error e Incertidumbre en forma cualitativa y cuantitativa.

 Análisis cualitativo: Comparaciones gráficas para datos meteorológicos pronosticados y observados,
principalmente, a través de los ciclos diarios.

 Análisis cuantitativo: Cálculo de las métricas de estadísticas del sesgo (BIAS), Error medio cuadrático
(RSME) y Coeficiente de correlación entre las variables meteorológicas pronosticadas y observadas.

8 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.
9 Ibíd.
10 Ibíd.
11 Ibíd.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 15 de 41

**2.1** **Levantamiento y selección de información meteorológica observada**

Con el objeto de evaluar los datos meteorológicos tridimensionales generados del modelo de pronóstico WRF,
la comparación de las observaciones con las simulaciones del modelo en el punto de medición de los datos
observados permite evaluar la incertidumbre asociada [12] . Para lograr este objetivo se hace necesario levantar
la información meteorológica en el área de estudio. Por lo anterior se realizó una búsqueda en las fuentes
públicas de información, tales como SINCA, Meteochile, Agromet, aeropuertos, entre otros. En caso de la
fuente de información disponga de registros para el mismo año modelado, se aplican criterios de validación
meteorológica [13], tales como: revisión de estándares de instalación WMO [14], registro variables meteorológicas
mínimas, porcentaje de datos válidos, entre otras.

La información se resume en la siguiente tabla:

Tabla 10 - Estaciones meteorológicas superficiales en el dominio de modelación WRF

|ID|Nombre estación|Coordenadas geográficas UTM Huso 19|Col4|Col5|Datos válidos [%]|Col7|Col8|
|---|---|---|---|---|---|---|---|
|ID|Nombre estación|Este [m]|Sur [m]|Distancia<br>a Planta<br>[km]|Dirección<br>viento|Velocidad<br>viento|Temperatura|
|**1 **|**Palmilla**(a)|**280.207**|**6.174.620**|**12,7**|**75,06**|**79,63**|**95,25**|
|2|Liceo Jean Buchanan(a)|301.015|6.191.667|15,6|98,55|87,45|98,06|
|3|Placilla Chacarilla(a)|304.252|6.164.625|29,7|98,55|87,45|98,01|

(a) Referencia: Red Agroclimática Nacional (AGROMET).

Basado en el criterio de porcentaje de datos válidos y similitud de las características geográficas, se seleccionó
la estación Palmilla (AGROMET) para efectuar el análisis. Si bien las estaciones Liceo Jean Buchanan y Placilla
Chacarilla presentan mayor porcentaje de datos válidos, ambas estaciones presentan periodos extensos con
datos faltantes (lagunas).

Por otra parte, si bien se dispone de información meteorológica observada dentro del dominio de modelación,
estas se estarían fuera del radio de representatividad meteorológica de 5 [km], recomendada por la Guía
para el Uso de Modelos de Calidad de Aire en el SEIA [15] para nuestro territorio nacional según lo indicado.
Siendo aplicable su uso sólo para el análisis de incertidumbre de la base meteorológica de pronóstico del
modelo de dispersión. En este mismo contexto, las estaciones observadas disponibles estarían fuera del radio
de representatividad de 10 [km] sugerido por la normativa de referencia Lombardía, no siendo recomendado
su incorporación a la base meteorológica del modelo de dispersión.

12 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.
13 Ibíd.
14 World Meteorological Organization (2010). Guide to Meteorological Instruments and Methods of Observation-WMO-No. 8, Geneva,

Switzerland.
15 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 16 de 41

**2.2** **Diagnóstico de datos meteorológicos**

Los datos meteorológicos corresponden a datos de pronóstico y observados. Los datos de pronóstico
son aquellos generados por el modelo numérico de pronóstico WRF [16] y los datos observados son los
registrados por la estación meteorológica superficial. Los parámetros meteorológicos considerados para
el análisis, en función del total de horas del periodo anual (8.670), corresponden a:

 - Velocidad del viento [m/s].

 - Dirección del viento [grados].

 - Temperatura [°C].

De pronóstico, WRF

La serie de pronóstico representa los datos de la meteorología de pronóstico del año 2019. La
coordenada utilizada para la extracción de datos pronosticados corresponde a la misma coordenada
de localización de la estación meteorológica superficial seleccionada, con el fin de comparar los datos
del mismo periodo y lugar [17] .

Tabla 11 - Coordenada de localización, serie de pronóstico WRF

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|Este|Sur|Huso|Datum|
|280.207|6.174.620|19 Sur|WGS 84|

Observados, estación meteorológica superficial

La serie observada corresponde a datos meteorológicos registrados por la Estación Palmilla, año 2019,
perteneciente a la Red Agroclimática Nacional (AGROMET), la cual se localiza en las siguientes
coordenadas:

Tabla 12 - Coordenada de localización estación meteorológica

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|Este|Sur|Huso|Datum|
|280.207|6.174.620|19 Sur|WGS 84|

16 Weather Research and Forecasting Model.
17 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 17 de 41

Figura 3 - Localización de estación meteorológica

Fuente: Envirometrika, 2020.

Los datos de la serie fueron validados siguiendo los lineamientos definidos en la guía “Meteorological
Monitoring Guidance for Regulatory Modeling Applications” [18], donde se definen distintos niveles de
validación. Para los parámetros meteorológicos considerados se realizó la validación Nivel 3 que implica
un análisis más detallado, debido a que los errores de las mediciones podrían causar inconsistencias
en el análisis y modelación de los resultados [19] . Los porcentajes de datos meteorológicos observados
válidos, calculados en función al total de horas teóricas (8.760 horas en un año).

Luego de la validación de la serie de datos, se debe tener en consideración que la “Guía para el Uso
de Modelos de Calidad del Aire en el SEIA” señala lo siguiente: “Se recomienda que el porcentaje de
datos válidos de las series de tiempo sea siempre superior al 75%...” [20] . De acuerdo a lo anterior, la
serie de datos de la estación meteorológica cumplió con lo recomendado, según se describe en la
siguiente tabla:

Tabla 13 - Porcentaje datos válidos en parámetros evaluados

|Parámetro meteorológico<br>evaluado|% datos válidos|Cumple con<br>recomendación SEA<br>(>75%)|
|---|---|---|
|Velocidad del viento [m/s]<br>Dirección del viento [°]<br>Temperatura [°C]|75,06%<br>79,63%<br>95,25%|<br><br> <br><br> <br>|

18 Environmental Protection Agency.(2000). Meteorological Monitoring Guidance for Regulatory Modeling Applications. Office of Air and

Radiation. Office of Air Quality Planning and Standards Research Triangle Park, NC 27711.
19 Ibíd.
20 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 18 de 41

**Series de tiempo**

Con la finalidad de analizar la calidad de la información, se graficaron las series de tiempo completas
de los datos de pronóstico y observados [21] para las variables meteorológicas de temperatura [°C] y
velocidad del viento [m/s].

Temperatura, [°C]

Gráfico 2 - Serie pronóstico, temperatura [°C]

Fuente: Envirometrika, 2020.

Gráfico 3 - Serie observada, temperatura [°C]

Fuente: Envirometrika, 2020.

21 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 19 de 41

Velocidad del viento, [m/s]

Gráfico 4 - Serie pronóstico, velocidad del viento [m/s]

Fuente: Envirometrika, 2020.

Gráfico 5 - Serie observada, velocidad del viento [m/s]

Fuente: Envirometrika, 2020.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 20 de 41

Para visualizar fluctuaciones típicas de las variables meteorológicas, se obtuvieron los ciclos horarios
promedios de cada parámetro, junto con su variabilidad en términos de los percentiles 5 y 95 [22] .

Temperatura, [°C]
Se graficaron los ciclos diarios promedios de temperaturas [°C], para las series pronóstico y observada.

Tabla 14 - Ciclos diarios de la temperatura - serie pronóstico

|Hora|Promedio de<br>Temperatura [°C]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|11,85<br>11,41<br>11,06<br>10,81<br>10,54<br>10,33<br>10,08<br>10,26<br>10,94<br>12,19<br>13,75<br>15,36<br>16,85<br>18,12<br>19,04<br>19,52<br>19,48<br>18,86<br>17,48<br>15,81<br>14,43<br>13,60<br>12,95<br>12,39|6,47<br>5,98<br>5,84<br>5,52<br>5,40<br>5,19<br>4,99<br>4,69<br>4,60<br>5,49<br>6,60<br>7,65<br>9,04<br>10,29<br>11,00<br>11,46<br>11,24<br>10,35<br>9,19<br>8,38<br>7,93<br>7,52<br>7,04<br>6,69|16,97<br>16,61<br>16,14<br>15,63<br>15,18<br>15,07<br>14,72<br>15,19<br>16,87<br>19,06<br>21,15<br>22,97<br>24,67<br>26,02<br>27,02<br>27,67<br>27,75<br>27,42<br>26,27<br>24,00<br>21,72<br>19,82<br>18,91<br>18,10|

Gráfico 6 - Ciclos diarios promedios de la temperatura - serie pronóstico

Fuente: Envirometrika, 2020.

22 Servicio de Evaluación Ambiental. (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 21 de 41

Tabla 15 - Ciclos diarios de la temperatura - serie observada

|Hora|Promedio de<br>temperatura [°C]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|12,55<br>11,89<br>11,42<br>11,01<br>10,71<br>10,39<br>10,06<br>9,95<br>10,73<br>12,59<br>14,59<br>16,66<br>18,61<br>20,36<br>21,66<br>22,29<br>22,57<br>22,17<br>20,96<br>19,31<br>17,17<br>15,56<br>14,35<br>13,71|5,88<br>5,66<br>4,90<br>4,98<br>4,55<br>4,40<br>4,00<br>3,60<br>3,94<br>5,30<br>7,50<br>8,88<br>9,76<br>11,10<br>12,00<br>12,20<br>12,10<br>11,46<br>10,30<br>8,80<br>7,71<br>7,70<br>7,10<br>6,47|19,73<br>19,22<br>19,00<br>18,34<br>17,85<br>17,28<br>16,63<br>16,63<br>18,30<br>20,59<br>23,23<br>26,13<br>28,30<br>30,75<br>32,30<br>32,30<br>33,05<br>32,80<br>32,20<br>30,80<br>28,00<br>24,20<br>22,06<br>21,60|

Gráfico 7 - Ciclos diarios promedios de la temperatura - serie observada

Fuente: Envirometrika, 2020.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 22 de 41

Velocidad del viento, [m/s]

Se graficaron los ciclos diarios promedios de la velocidad del viento [m/s] para cada serie, junto a los
percentiles 5 y 95, para cada horario analizado.

Tabla 16 - Ciclos diarios promedios serie pronóstico

|Hora|Promedio velocidad<br>del viento [m/s]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|2,42<br>2,42<br>2,48<br>2,60<br>2,69<br>2,69<br>2,74<br>2,88<br>3,03<br>3,14<br>3,11<br>3,01<br>2,91<br>2,89<br>2,93<br>3,07<br>3,10<br>3,00<br>2,70<br>2,43<br>2,45<br>2,51<br>2,51<br>2,48|0,38<br>0,44<br>0,29<br>0,29<br>0,42<br>0,35<br>0,26<br>0,35<br>0,39<br>0,54<br>0,50<br>0,32<br>0,51<br>0,62<br>0,49<br>0,66<br>0,55<br>0,62<br>0,39<br>0,40<br>0,57<br>0,48<br>0,41<br>0,42|5,36<br>5,51<br>5,60<br>5,65<br>5,66<br>5,64<br>5,80<br>6,10<br>6,34<br>6,39<br>6,51<br>6,50<br>6,48<br>6,44<br>6,45<br>6,22<br>6,03<br>5,72<br>5,66<br>5,32<br>5,17<br>5,35<br>5,36<br>5,40|

Gráfico 8 - Ciclos diarios promedios de velocidad del viento - serie pronóstico

Fuente: Envirometrika, 2020.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 23 de 41

Tabla 17 - Ciclos diarios promedios serie observada

|Hora|Promedio velocidad<br>del viento [m/s]|Percentil 5|Percentil 95|
|---|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|1,22<br>1,32<br>1,47<br>1,48<br>1,42<br>1,56<br>1,49<br>1,54<br>1,83<br>2,02<br>2,03<br>2,16<br>2,02<br>2,11<br>2,04<br>2,03<br>2,13<br>1,86<br>1,72<br>1,63<br>1,35<br>1,23<br>1,24<br>0,92|0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,03<br>0,34<br>0,40<br>0,50<br>0,60<br>0,70<br>0,60<br>0,60<br>0,50<br>0,20<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00|2,80<br>2,90<br>3,60<br>3,12<br>3,20<br>3,10<br>3,10<br>3,30<br>3,78<br>3,80<br>3,80<br>4,00<br>3,60<br>3,77<br>4,00<br>3,80<br>4,40<br>4,10<br>4,00<br>3,60<br>2,90<br>2,80<br>2,90<br>2,60|

Gráfico 9 - Ciclos diarios promedios de velocidad del viento - serie observada

Fuente: Envirometrika, 2020.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 24 de 41

Dirección del viento, [grados]

Se graficó la frecuencia de la dirección del viento en grados, para un año, durante periodos horarios
de 1 hora para las series de pronóstico y observada.

Tabla 18 - Ciclos diarios de dirección del viento serie pronóstico

|Col1|Dirección del viento [grados]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Hora<br>del día|0-20|20-40|40-60|60-80|80-100|100-120|120-140|140-160|160-180|180-200|200-220|220-240|240-260|260-280|280-300|300-320|320-340|340-360|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|40<br>26<br>16<br>5 <br>0 <br>4 <br>5 <br>17<br>67<br>106<br>24<br>0 <br>0 <br>0 <br>0 <br>5 <br>13<br>37<br>46<br>29<br>10<br>3 <br>3 <br>2 <br>2 <br>12<br>68<br>113<br>24<br>0 <br>1 <br>1 <br>0 <br>5 <br>12<br>34<br>44<br>20<br>9 <br>7 <br>4 <br>2 <br>6 <br>7 <br>62<br>122<br>23<br>2 <br>1 <br>2 <br>2 <br>5 <br>11<br>36<br>40<br>21<br>8 <br>3 <br>1 <br>0 <br>2 <br>8 <br>48<br>150<br>25<br>3 <br>1 <br>1 <br>3 <br>9 <br>8 <br>34<br>29<br>24<br>8 <br>1 <br>2 <br>1 <br>3 <br>6 <br>48<br>147<br>31<br>3 <br>1 <br>1 <br>6 <br>10<br>11<br>33<br>35<br>12<br>7 <br>3 <br>2 <br>0 <br>3 <br>6 <br>49<br>129<br>51<br>2 <br>3 <br>1 <br>2 <br>5 <br>13<br>41<br>37<br>15<br>5 <br>1 <br>1 <br>3 <br>3 <br>5 <br>50<br>128<br>48<br>2 <br>0 <br>6 <br>3 <br>6 <br>16<br>36|
|07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|33<br>13<br>10<br>2 <br>3 <br>2 <br>1 <br>5 <br>35<br>144<br>50<br>1 <br>1 <br>2 <br>0 <br>6 <br>17<br>40<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>32<br>9 <br>3 <br>0 <br>1 <br>4 <br>0 <br>3 <br>62<br>136<br>28<br>0 <br>2 <br>0 <br>1 <br>9 <br>10<br>65<br>28<br>8 <br>2 <br>2 <br>0 <br>1 <br>1 <br>5 <br>90<br>110<br>21<br>2 <br>2 <br>1 <br>3 <br>9 <br>17<br>63<br>22<br>7 <br>5 <br>2 <br>1 <br>0 <br>0 <br>12<br>107<br>80<br>12<br>3 <br>4 <br>2 <br>5 <br>6 <br>31<br>66<br>18<br>1 <br>0 <br>3 <br>2 <br>0 <br>1 <br>37<br>98<br>66<br>6 <br>1 <br>3 <br>3 <br>0 <br>12<br>46<br>68<br>17<br>7 <br>2 <br>1 <br>0 <br>1 <br>2 <br>40<br>105<br>43<br>9 <br>5 <br>0 <br>2 <br>1 <br>9 <br>44<br>77<br>20<br>5 <br>4 <br>2 <br>0 <br>0 <br>3 <br>53<br>85<br>48<br>7 <br>5 <br>4 <br>0 <br>3 <br>20<br>39<br>67|
|15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|20<br>3 <br>2 <br>1 <br>1 <br>2 <br>1 <br>43<br>91<br>46<br>15<br>11<br>7 <br>3 <br>6 <br>12<br>33<br>68<br>22<br>3 <br>2 <br>1 <br>0 <br>2 <br>1 <br>41<br>82<br>44<br>20<br>31<br>13<br>1 <br>6 <br>12<br>34<br>50<br>12<br>12<br>6 <br>1 <br>1 <br>2 <br>0 <br>25<br>76<br>54<br>35<br>36<br>14<br>3 <br>4 <br>12<br>39<br>33<br>11<br>10<br>8 <br>3 <br>0 <br>8 <br>0 <br>13<br>77<br>64<br>37<br>50<br>14<br>3 <br>2 <br>14<br>30<br>21<br>11<br>7 <br>7 <br>5 <br>5 <br>8 <br>6 <br>21<br>75<br>75<br>42<br>34<br>15<br>0 <br>1 <br>11<br>22<br>20<br>21<br>13<br>10<br>12<br>6 <br>12<br>7 <br>44<br>71<br>90<br>25<br>6 <br>5 <br>1 <br>1 <br>6 <br>16<br>19<br>21<br>30<br>19<br>10<br>6 <br>1 <br>11<br>45<br>79<br>78<br>16<br>3 <br>1 <br>4 <br>2 <br>4 <br>16<br>19<br>29<br>33<br>20<br>11<br>2 <br>2 <br>4 <br>29<br>84<br>90<br>14<br>2 <br>3 <br>1 <br>2 <br>7 <br>12<br>20<br>40<br>25<br>15<br>6 <br>2 <br>1 <br>5 <br>22<br>88<br>81<br>19<br>2 <br>3 <br>2 <br>2 <br>8 <br>12<br>32|

|0-20|0.11 0.13 0.12 0.11 0.08 0.10 0.10 0.09 0.08 0.09 0.08 0.06 0.05 0.05 0.05 0.05 0.06 0.03 0.03 0.03 0.06 0.06 0.08 0.11<br>0.07 0.08 0.05 0.06 0.07 0.03 0.04 0.04 0.04 0.02 0.02 0.02 0.00 0.02 0.01 0.01 0.01 0.03 0.03 0.02 0.04 0.08 0.09 0.07<br>0.04 0.03 0.02 0.02 0.02 0.02 0.01 0.03 0.02 0.01 0.01 0.01 0.00 0.01 0.01 0.01 0.01 0.02 0.02 0.02 0.03 0.05 0.05 0.04<br>0.01 0.01 0.02 0.01 0.00 0.01 0.00 0.01 0.00 0.00 0.01 0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.01 0.01 0.03 0.03 0.03 0.02<br>0.00 0.01 0.01 0.00 0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.00 0.01 0.00 0.00 0.00 0.00 0.00 0.00 0.01 0.02 0.02 0.01 0.01<br>0.01 0.01 0.01 0.00 0.00 0.00 0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.00 0.00 0.01 0.01 0.01 0.02 0.02 0.03 0.00 0.01 0.00<br>0.01 0.01 0.02 0.01 0.01 0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.00 0.01 0.01 0.00 0.00 0.00 0.00 0.02 0.02 0.03 0.01 0.01<br>0.05 0.03 0.02 0.02 0.02 0.02 0.01 0.01 0.02 0.01 0.01 0.03 0.10 0.11 0.15 0.12 0.11 0.07 0.04 0.06 0.12 0.12 0.08 0.06<br>0.18 0.19 0.17 0.13 0.13 0.13 0.14 0.10 0.13 0.17 0.25 0.29 0.27 0.29 0.23 0.25 0.22 0.21 0.21 0.21 0.19 0.22 0.23 0.24<br>0.29 0.31 0.33 0.41 0.40 0.35 0.35 0.39 0.38 0.37 0.30 0.22 0.18 0.12 0.13 0.13 0.12 0.15 0.18 0.21 0.25 0.21 0.25 0.22<br>0.07 0.07 0.06 0.07 0.08 0.14 0.13 0.14 0.11 0.08 0.06 0.03 0.02 0.02 0.02 0.04 0.05 0.10 0.10 0.12 0.07 0.04 0.04 0.05<br>0.00 0.00 0.01 0.01 0.01 0.01 0.01 0.00 0.00 0.00 0.01 0.01 0.00 0.01 0.01 0.03 0.08 0.10 0.14 0.09 0.02 0.01 0.01 0.01<br>0.00 0.00 0.00 0.00 0.00 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.01 0.00 0.01 0.02 0.04 0.04 0.04 0.04 0.01 0.00 0.01 0.01<br>0.00 0.00 0.01 0.00 0.00 0.00 0.02 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.00 0.01 0.00 0.01 0.01 0.00 0.00 0.01 0.00 0.01<br>0.00 0.00 0.01 0.01 0.02 0.01 0.01 0.00 0.00 0.00 0.01 0.01 0.00 0.00 0.01 0.02 0.02 0.01 0.01 0.00 0.00 0.01 0.01 0.01<br>0.01 0.01 0.01 0.02 0.03 0.01 0.02 0.02 0.01 0.02 0.02 0.02 0.03 0.02 0.05 0.03 0.03 0.03 0.04 0.03 0.02 0.01 0.02 0.02<br>0.04 0.03 0.03 0.02 0.03 0.04 0.04 0.05 0.05 0.03 0.05 0.08 0.13 0.12 0.11 0.09 0.09 0.11 0.08 0.06 0.04 0.04 0.03 0.03<br>0.10 0.09 0.10 0.09 0.09 0.11 0.10 0.11 0.13 0.18 0.17 0.18 0.19 0.21 0.18 0.19 0.14 0.09 0.06 0.05 0.05 0.05 0.05 0.09|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|
|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|
|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|
|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|
|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|
|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|
|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|
|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|
|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|
|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|
|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|
|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|
|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|
|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|
|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|
|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|
|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|
||0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 25 de 41

Tabla 19 - Ciclos diarios de dirección del viento serie observada

|Col1|Dirección del viento [grados]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Hora<br>Del día|0-20|20-40|40-60|60-80|80-100|100-120|120-140|140-160|160-180|180-200|200-220|220-240|240-260|260-280|280-300|300-320|320-340|340-360|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6|
|07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29|
|15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12|

Gráfico 11 - Ciclos diarios de dirección del viento - serie observada

|0-20|0.08 0.08 0.07 0.04 0.02 0.04 0.04 0.04 0.05 0.03 0.01 0.01 0.01 0.00 0.01 0.01 0.02 0.01 0.02 0.01 0.02 0.01 0.03 0.08<br>0.05 0.05 0.03 0.02 0.01 0.03 0.02 0.00 0.02 0.03 0.02 0.02 0.00 0.00 0.00 0.01 0.01 0.01 0.01 0.02 0.03 0.02 0.02 0.06<br>0.04 0.02 0.01 0.01 0.01 0.01 0.01 0.01 0.02 0.01 0.02 0.01 0.01 0.01 0.01 0.02 0.01 0.01 0.00 0.01 0.02 0.01 0.02 0.03<br>0.02 0.02 0.00 0.01 0.01 0.03 0.02 0.01 0.01 0.01 0.00 0.00 0.00 0.01 0.00 0.01 0.01 0.01 0.00 0.00 0.00 0.00 0.03 0.04<br>0.02 0.01 0.00 0.00 0.01 0.01 0.00 0.00 0.02 0.00 0.00 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.01<br>0.00 0.00 0.00 0.01 0.00 0.00 0.00 0.00 0.00 0.01 0.02 0.01 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.01 0.00 0.01 0.00 0.00<br>0.02 0.00 0.00 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.00 0.01 0.01 0.02 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.01 0.01 0.01<br>0.01 0.00 0.01 0.00 0.01 0.00 0.00 0.00 0.02 0.00 0.01 0.00 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.01 0.01 0.02 0.01 0.03<br>0.12 0.08 0.12 0.14 0.16 0.14 0.12 0.11 0.08 0.06 0.09 0.09 0.05 0.07 0.10 0.08 0.11 0.10 0.12 0.11 0.22 0.33 0.30 0.22<br>0.29 0.30 0.29 0.28 0.34 0.26 0.29 0.37 0.30 0.36 0.43 0.34 0.38 0.36 0.33 0.33 0.29 0.31 0.26 0.22 0.31 0.28 0.30 0.26<br>0.20 0.23 0.26 0.30 0.29 0.36 0.34 0.28 0.34 0.28 0.20 0.22 0.15 0.15 0.12 0.12 0.11 0.11 0.14 0.23 0.21 0.17 0.13 0.15<br>0.07 0.07 0.11 0.07 0.06 0.07 0.05 0.06 0.05 0.03 0.01 0.05 0.06 0.04 0.03 0.03 0.04 0.06 0.11 0.10 0.05 0.05 0.08 0.04<br>0.00 0.00 0.00 0.01 0.00 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.03 0.02 0.01 0.05 0.03 0.03 0.02 0.02 0.00 0.00 0.00 0.00<br>0.00 0.00 0.01 0.01 0.00 0.00 0.00 0.00 0.00 0.01 0.01 0.01 0.02 0.02 0.02 0.04 0.01 0.03 0.02 0.01 0.01 0.00 0.00 0.00<br>0.00 0.00 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.01 0.02 0.01 0.03 0.03 0.04 0.03 0.02 0.03 0.02 0.01 0.00 0.01 0.01 0.00<br>0.00 0.01 0.01 0.02 0.01 0.00 0.00 0.00 0.00 0.01 0.03 0.00 0.03 0.06 0.08 0.05 0.04 0.06 0.04 0.02 0.01 0.00 0.00 0.00<br>0.02 0.03 0.02 0.02 0.03 0.02 0.03 0.03 0.03 0.06 0.04 0.08 0.10 0.12 0.14 0.13 0.14 0.12 0.13 0.07 0.04 0.02 0.00 0.02<br>0.06 0.06 0.07 0.06 0.05 0.04 0.03 0.05 0.06 0.10 0.09 0.13 0.10 0.10 0.09 0.06 0.11 0.08 0.10 0.15 0.05 0.03 0.06 0.05|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|
|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|
|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|
|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|
|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|
|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|
|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|
|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|
|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|
|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|
|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|
|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|
|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|
|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|
|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|
|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|
|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|
||0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 26 de 41

Vientos calmos, < 0,5 [m/s]

La condición de calma o cuasi-calma (velocidades de viento menores a 0,5 [m/s] [23] ), es de especial
interés en calidad del aire, pues son las condiciones en que el movimiento del aire es casi nulo
(estancamiento). Lo anterior puede ser crítico para fuentes emisoras a nivel de superficie, ya que
puede: Condicionar la acumulación de contaminantes en su lugar de origen, incrementar en la
concentración en el tiempo o que las masas de aire no se renueven en forma efectiva y recirculen [24] .
La información a continuación indica el período del día y del año en que se presenta el mayor porcentaje
de vientos calmos, según la serie de pronóstico y observada.

Tabla 20 - Frecuencia mensual de vientos calmos - serie pronóstico

Nota: Sumatoria de horas/mes de vientos calmos.

|Mes|Frecuencia de<br>vientos calmos|N°<br>días|%|
|---|---|---|---|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|45<br>71<br>79<br>51<br>51<br>45<br>45<br>22<br>31<br>42<br>26<br>41|744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744|6%<br>11%<br>11%<br>7%<br>7%<br>6%<br>6%<br>3%<br>4%<br>6%<br>4%<br>6%|

Fuente: Envirometrika, 2020.

Tabla 21 - Frecuencia horaria de vientos calmos - serie pronóstico

Nota: Sumatoria de horas/año de vientos calmos.

|Hora|Frecuencia de<br>vientos calmos|%|
|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00<br>|27<br>22<br>33<br>29<br>28<br>32<br>31<br>32<br>25<br>17<br>19<br>26<br>18<br>16<br>19<br>14<br>14<br>17<br>23<br>26<br>13<br>20<br>23<br>25<br>|7%<br>6%<br>9%<br>8%<br>8%<br>9%<br>8%<br>9%<br>7%<br>5%<br>5%<br>7%<br>5%<br>4%<br>5%<br>4%<br>4%<br>5%<br>6%<br>7%<br>4%<br>5%<br>6%<br>7%|

Fuente: Envirometrika, 2020.

23 Barclay, J. Scire, J. (2011). Generic Guidance and Optimum Model Settings for the CALPUFF Modeling System for Inclusion into the Approved

Methods for the Modeling and Assessments of Air Pollutants in NSW, Australia. TRC Environmental Corporation.
24 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 27 de 41

Tabla 22 - Frecuencia mensual de vientos calmos - serie observada

|Mes|Frecuencia de<br>vientos calmos|N°<br>días|%|
|---|---|---|---|
|Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre|69<br>67<br>73<br>72<br>65<br>56<br>43<br>52<br>33<br>53<br>42<br>36|744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744|9%<br>10%<br>10%<br>10%<br>9%<br>8%<br>6%<br>7%<br>5%<br>7%<br>6%<br>5%|

Fuente: Envirometrika, 2020.

Nota: Sumatoria de horas/mes de vientos calmos.

Tabla 23 - Frecuencia horaria de vientos calmos - serie observada

Nota: Sumatoria de horas/año de vientos calmos.

|Hora|Frecuencia de<br>vientos calmos|%|
|---|---|---|
|00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00|52<br>34<br>20<br>22<br>19<br>17<br>27<br>25<br>20<br>15<br>12<br>6 <br>7 <br>5 <br>10<br>9 <br>13<br>26<br>42<br>33<br>48<br>61<br>60<br>78|14%<br>9%<br>5%<br>6%<br>5%<br>5%<br>7%<br>7%<br>5%<br>4%<br>3%<br>2%<br>2%<br>1%<br>3%<br>2%<br>4%<br>7%<br>12%<br>9%<br>13%<br>17%<br>16%<br>21%|

Fuente: Envirometrika, 2020.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 28 de 41

**2.3** **Comparación entre pronóstico y observaciones**

La comparación de las observaciones (serie de datos obtenida de registros de la estación meteorológica
superficial) con las simulaciones del modelo de pronóstico (serie de datos obtenida del modelo numérico
WRF) en el punto de medición, permite evaluar la incertidumbre de los datos meteorológicos tridimensionales
generados y de los resultados del modelo de dispersión y así poder analizar una posible sobre o
subestimación [25] . Para poder determinar un grado de incertidumbre, se deben evaluar las diferencias de lo
observado versus lo modelado realizando un análisis cuantitativo y cualitativo, según se recomienda en la
guía de modelación [26] .

El análisis cualitativo se determinó en base a la comparación de la serie de pronóstico versus la
observada, mediante gráficos de ciclos diarios promedios para las variables de temperatura, velocidad
y dirección del viento.

Temperatura, [°C]

Gráfico 12 - Ciclos diarios promedios de temperatura, serie pronóstico y observado.

Fuente: Envirometrika, 2020.

Del gráfico comparativo, se tiene que la serie pronóstico reprodujo la curva de los promedios de la
serie observada subestimando en promedio a lo observado en 1,4 [°C], principalmente en horario AM
y PM.

25 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.
26 Ibíd.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 29 de 41

Velocidad del viento, [m/s]

Gráfico 13 - Ciclos diarios promedios de velocidad del viento, serie pronóstico y observada

Fuente: Envirometrika, 2020.

Se observó que la serie pronóstico sobrestima la curva promedio de lo observado durante todo el
período, cuya diferencia promedio de 1,1 [m/s].

Gráfico 14 - Distribución anual de frecuencia de velocidad del viento serie pronóstico y observada.

WRF-MMIF, 2019 Estación Palmilla, 2019

En términos generales, la serie pronóstico reproduce la frecuencia de los vientos menores a 4 [m/s]
correspondientes al rango de ventolina a brisa débil [27] . Sin embargo, la serie de pronóstico presenta
una mayor frecuencia en los rangos de mayor intensidad. Esta condición resultaría en un mayor alcance
de las emisiones proyectadas en distintos escenarios sujetos a modelación. En cuanto a los vientos en
calma, el modelo de pronóstico reproduce la frecuencia observado con una variación cercana al 1,28%.

27 Organización Meteorológica Mundial (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A - Claves alfanuméricas - Escala

Beaufort de Viento. OMM-N°306. OMM. Suiza.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 30 de 41

Dirección del viento, [grados]

Gráfico 15 - Ciclos diarios de variación del viento, serie pronóstico

Gráfico 16 - Ciclos diarios de variación del viento, serie observada

|0-20|0.08 0.08 0.07 0.04 0.02 0.04 0.04 0.04 0.05 0.03 0.01 0.01 0.01 0.00 0.01 0.01 0.02 0.01 0.02 0.01 0.02 0.01 0.03 0.08<br>0.05 0.05 0.03 0.02 0.01 0.03 0.02 0.00 0.02 0.03 0.02 0.02 0.00 0.00 0.00 0.01 0.01 0.01 0.01 0.02 0.03 0.02 0.02 0.06<br>0.04 0.02 0.01 0.01 0.01 0.01 0.01 0.01 0.02 0.01 0.02 0.01 0.01 0.01 0.01 0.02 0.01 0.01 0.00 0.01 0.02 0.01 0.02 0.03<br>0.02 0.02 0.00 0.01 0.01 0.03 0.02 0.01 0.01 0.01 0.00 0.00 0.00 0.01 0.00 0.01 0.01 0.01 0.00 0.00 0.00 0.00 0.03 0.04<br>0.02 0.01 0.00 0.00 0.01 0.01 0.00 0.00 0.02 0.00 0.00 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.01<br>0.00 0.00 0.00 0.01 0.00 0.00 0.00 0.00 0.00 0.01 0.02 0.01 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.01 0.00 0.01 0.00 0.00<br>0.02 0.00 0.00 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.00 0.01 0.01 0.02 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.01 0.01 0.01<br>0.01 0.00 0.01 0.00 0.01 0.00 0.00 0.00 0.02 0.00 0.01 0.00 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.01 0.01 0.02 0.01 0.03<br>0.12 0.08 0.12 0.14 0.16 0.14 0.12 0.11 0.08 0.06 0.09 0.09 0.05 0.07 0.10 0.08 0.11 0.10 0.12 0.11 0.22 0.33 0.30 0.22<br>0.29 0.30 0.29 0.28 0.34 0.26 0.29 0.37 0.30 0.36 0.43 0.34 0.38 0.36 0.33 0.33 0.29 0.31 0.26 0.22 0.31 0.28 0.30 0.26<br>0.20 0.23 0.26 0.30 0.29 0.36 0.34 0.28 0.34 0.28 0.20 0.22 0.15 0.15 0.12 0.12 0.11 0.11 0.14 0.23 0.21 0.17 0.13 0.15<br>0.07 0.07 0.11 0.07 0.06 0.07 0.05 0.06 0.05 0.03 0.01 0.05 0.06 0.04 0.03 0.03 0.04 0.06 0.11 0.10 0.05 0.05 0.08 0.04<br>0.00 0.00 0.00 0.01 0.00 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.03 0.02 0.01 0.05 0.03 0.03 0.02 0.02 0.00 0.00 0.00 0.00<br>0.00 0.00 0.01 0.01 0.00 0.00 0.00 0.00 0.00 0.01 0.01 0.01 0.02 0.02 0.02 0.04 0.01 0.03 0.02 0.01 0.01 0.00 0.00 0.00<br>0.00 0.00 0.01 0.01 0.01 0.01 0.01 0.01 0.00 0.01 0.02 0.01 0.03 0.03 0.04 0.03 0.02 0.03 0.02 0.01 0.00 0.01 0.01 0.00<br>0.00 0.01 0.01 0.02 0.01 0.00 0.00 0.00 0.00 0.01 0.03 0.00 0.03 0.06 0.08 0.05 0.04 0.06 0.04 0.02 0.01 0.00 0.00 0.00<br>0.02 0.03 0.02 0.02 0.03 0.02 0.03 0.03 0.03 0.06 0.04 0.08 0.10 0.12 0.14 0.13 0.14 0.12 0.13 0.07 0.04 0.02 0.00 0.02<br>0.06 0.06 0.07 0.06 0.05 0.04 0.03 0.05 0.06 0.10 0.09 0.13 0.10 0.10 0.09 0.06 0.11 0.08 0.10 0.15 0.05 0.03 0.06 0.05|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|53 - 100<br>50 - 53<br>48 - 50<br>45 - 48<br>43 - 45<br>40 - 43<br>38 - 40<br>35 - 38<br>33 - 35<br>30 - 33<br>28 - 30<br>25 - 28<br>23 - 25<br>20 - 23<br>18 - 20<br>15 - 18<br>13 - 15<br>10 - 13<br>8 - 10<br>5 - 8<br>3 - 5<br>0 - 3|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|20-40|
|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|40-60|
|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|60-80|
|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|80-100|
|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|100-120|
|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|120-140|
|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|140-160|
|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|160-180|
|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|180-200|
|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|200-220|
|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|220-240|
|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|240-260|
|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|260-280|
|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|280-300|
|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|300-320|
|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|320-340|
|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|340-360|
|0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|23|

Fuente: Envirometrika, 2020.

Al comparar ambas gráficas, se puede apreciar que la serie pronóstico reproduce la distribución de
vientos, tanto en el rango de dirección como en su comportamiento horario, donde logra representar
las mayores frecuencias descritas por la serie observada.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 31 de 41

Gráfico 17 - Rosas de viento anual por periodo horario, serie pronóstico y observada

Meteorología pronóstico Meteorología observada

|Col1|Col2|Anual Nocturno|Anual AM|Anual PM|
|---|---|---|---|---|
|Pronóstico|||||
|Observado|||||

Fuente: Envirometrika, 2020.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 32 de 41

Gráfico 18 - Rosas de viento anual por periodo estacional, serie pronóstico y observada.

|Col1|Verano|Otoño|Invierno|Primavera|
|---|---|---|---|---|
|Pronóstico||<br>|<br>|<br>|
|Observado||<br>|<br>|<br>|

Fuente: Envirometrika, 2020.

Del análisis anual de las rosas de viento, arrojó lo siguiente:

 - El modelo pronóstico presentó una sobrestimación respecto al modelo observado en cuanto a la
frecuencia e intensidad del viento proveniente desde las componentes NNO-N y SSE-S.

En cuanto al análisis horario y estacional, se tiene que la serie de pronóstico:

 - Sugiere una mayor frecuencia e intensidad de los vientos provenientes desde el rango NNO-NNE
y S-SSO, mayormente en los horarios nocturnos y PM.

 - Reproduce en gran medida la distribución estacional de vientos, con variaciones en frecuencia e
intensidad, los que se evidencian mayormente en la estación invernal.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 33 de 41

El análisis cuantitativo se realizó en base a una metodología celda-punto, el cual comparó los datos de
la meteorología de pronóstico con los registrados por la estación superficial, de cada dato horario. Se
calcularon las métricas de estadísticas de error medio cuadrático (RSME), sesgo (BIAS), coeficiente de
correlación, índice de concordancia (IOA), entre las variables meteorológicas pronosticadas y
observadas.

Tabla 24 - Error medio cuadrático, sesgo, coeficiente de correlación, IOA, velocidad del viento y temperatura

|Estadístico|Descripción|Fórmula|Resultado|Col5|
|---|---|---|---|---|
|Estadístico|Descripción|Fórmula|Velocidad del<br>viento [m/s]|Temperatura<br>[°C]|
|RMSE|Error medio cuadrático (Root<br>mean square Error), nos indica la<br>medida de las diferencias en<br>promedio<br>entre<br>valores<br>pronosticados y observados||1,86|3,21|
|NRMSD|Error<br>medio<br>cuadrático<br>normalizado<br>(Normalized<br>Root<br>mean square deviation) señala la<br>varianza residual entre los valores<br>pronosticados y observados||0,28|0,09|
|NMAE|Error medio absoluto normalizado,<br>toma en cuenta el peso del error<br>respecto al valor de la variable<br>medida,<br>normaliza<br>el<br>error<br>absoluto||0,23|0,07|
|BIAS|Sesgo, proporciona información<br>sobre la tendencia del modelo a<br>sobrestimar o subestimar una<br>variable||1,25|-1,49|
|Coeficiente de<br>correlación de<br>Pearson|Un índice que mide el grado de<br>relación de dos variables siempre<br>y <br>cuando<br>ambas<br>sean<br>cuantitativas.||0,60|0,93|
|IOA|El IOA (Index Of Agreement)<br>acuerdo es una medida de la<br>coincidencia entre la salida de<br>cada predicción de la media<br>observada y la salida de cada<br>observación<br>de<br>la<br>media||0,69|1,00|

 - Al evaluar el RMSE, se tiene que las variables de velocidad del viento y la temperatura
pronosticadas presentaron una diferencia de 1,86 [m/s] y 3,21 [°C], respecto a lo observado para
el periodo anual.

 Del Sesgo (BIAS) se interpreta que la meteorología del modelo de pronóstico WRF-MMIF,
sobrestima la velocidad del viento en 1,25 [m/s] y la temperatura subestima en 1,49 [°C], respecto
de lo observado.

 La correlación arrojó asociación positiva media para la variable de velocidad del viento y positiva
considerable para la variable de temperatura [28] [/] [29] .

 El IOA exhibió un nivel de 0,69 categorizado como acuerdo para velocidad del viento y para la
variable de temperatura arrojó acuerdo perfecto con un valor de 1. Por lo tanto, las variables se
encontrarían dentro del límite de 0,6 cuyo valor es aceptado para su aplicación en el modelo
(Emery et al., 2001).

28 Correlación positiva débil=+0,10, Correlación positiva media=+0,50, Correlación positiva considerable=+0,75.
29 Castejón Sandoval, O. (2011). Diseño y Análisis de Experimentos con Statistix. Universidad Rafael Urdaneta, Fondo editorial biblioteca.

ANEXO 2 - ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 34 de 41

**3** **ANÁLISIS DE RESULTADOS**

En base al análisis del comportamiento anual de los campos de vientos en el área de estudio, se tiene que el
transporte de las emisiones podría darse mayormente hacia la orientación ONO.

Respecto a las condiciones más desfavorables de dispersión, estas se presentarían en horario nocturno, debido a
la mayor frecuencia de vientos de baja intensidad y condiciones de calma, junto con el bajo desarrollo de la capa
de mezcla, que en su conjunto limitan la dispersión vertical y horizontal de las emisiones.

Del análisis de incertidumbre, se concluye que:

 Del levantamiento meteorológico realizado, la estación meteorológica Palmilla, cumplió con los requisitos,

requerido por el SEA [30], para la realización del análisis.

 Del análisis cuantitativo entre las series, se desprende que la serie de pronóstico reproduce coherentemente

la serie observada correspondiente a la estación Palmilla.

 En cuanto al análisis cualitativo, los resultados indicarían que lo pronosticado reproduciría las condiciones

meteorológicas más desfavorables. Respecto al ciclo mensual y diario, se observa una sobreestimación de la
frecuencia e intensidad.

30 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANÁLISIS DE RESULTADOS www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 35 de 41

**4** **BIBLIOGRAFÍA**

 Barclay, J. Scire, J. (2011) Generic Guidance and Optimum Model Settings for the CALPUFF Modeling System

for Inclusion into the Approved Methods for the Modeling and Assessments of Air Pollutants in NSW, Australia.
TRC Environmental Corporation.

 Castejón Sandoval, O. (2011). Diseño y Análisis de Experimentos con Statistix. Universidad Rafael Urdaneta,

Fondo editorial biblioteca. Venezuela.

 Centro de Información de Recursos Naturales. (2016). Región del Libertador General Bernardo O’Higgins,

Provincia de Colchagua, Comuna de Santa Cruz: Recursos Naturales y Proyectos. Sistema de Información
Territorial Rural. Chile.

 Dirección General de Aguas. (2004). Diagnóstico y Clasificación de los Cursos y Cuerpos de Agua según Objetivo

de Calidad: Cuenca del Río Rapel. Ministerio de Obras Públicas. Chile.

 Environmental Protection Agency. (2000). Meteorological Monitoring Guidance for Regulatory Modeling

Applications. Office of Air and Radiation. Office of Air Quality Planning and Standards Research Triangle Park,
NC 27711.

 - Ilustre Municipalidad de Santa Cruz (1997). Memoria explicativa Plan Regulador Comunal de Santa Cruz. Chile.

 Organización Meteorológica Mundial (2010). Manual de claves, Claves internacional, Volumen I.1 Parte AClaves alfanuméricas - Escala Beaufort de Viento. OMM-N°306. OMM. Suiza.

 Servicio de Evaluación Ambiental (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago,

Chile.

 World Meteorological Organization (2010). Guide to Meteorological Instruments and Methods of Observation
WMO-No. 8, Geneva, Switzerland.

BIBLIOGRAFÍA www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 36 de 41

**5** **ANEXO 3 - PARAMETRIZACIÓN METEOROLOGÍA DE PRONÓSTICO**

**5.1** **Namelist WPS**

&share
wrf_core = 'ARW',
max_dom = 2,
start_date = '2018-12-31_00:00:00', '2018-12-31_00:00:00',
end_date = '2020-01-02_18:00:00', '2020-01-02_18:00:00',
interval_seconds = 21600,
io_form_geogrid = 2,
/

&geogrid
parent_id = 1, 1,
parent_grid_ratio = 1, 3,
i_parent_start = 1, 30,
j_parent_start = 1, 30,
e_we = 88, 88,
e_sn = 88, 88,
geog_data_res = 'modis_15s+gmted2010_30s','modis_15s+gmted2010_30s',
dx = 3000,
dy = 3000,
map_proj = 'lambert',
ref_lat = -34.670008,
ref_lon = -71.350500,
truelat1 = -34.400,
truelat2 = -34.940,
stand_lon = -71.350500,
geog_data_path = '/wrfmain/static/geo'
/

&ungrib
out_format = 'WPS',
prefix = 'FILE',
pmin = 5000,
/

&metgrid
fg_name = '/wrfmain/static/met/ungribbed/fnl.2019/FILE'
io_form_metgrid = 2,
/

ANEXO 3 - PARAMETRIZACIÓN METEOROLOGÍA DE PRONÓSTICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 37 de 41

**5.2** **Namelist Input**

&time_control
run_days = 0,
run_hours = 0,
run_minutes = 0,
run_seconds = 0,
start_year = 2018, 2018,
start_month = 12, 12,
start_day = 31, 31,
start_hour = 18, 18,
start_minute = 0, 0,
start_second = 0, 0,
end_year = 2020, 2020,
end_month = 1, 1,
end_day = 2, 2,
end_hour = 18, 18,
end_minute = 0, 0,
end_second = 0, 0,
interval_seconds = 21600,
input_from_file = .true., .true.,
history_interval = 100000, 60,
frames_per_outfile = 100000, 100000,
restart = .false.,
restart_interval = 500000,
io_form_history = 2
io_form_restart = 2
io_form_input = 2
io_form_boundary = 2
debug_level = 0
/

&domains

time_step = 15,
time_step_fract_num = 0,
time_step_fract_den = 1,
max_dom = 2,
e_we = 88, 88,
e_sn = 88, 88,
e_vert = 35, 35,
p_top_requested = 5000,
num_metgrid_levels = 24,
num_metgrid_soil_levels = 4,
dx = 3000, 1000,
dy = 3000, 1000,
grid_id = 1, 2,
parent_id = 0, 1,
i_parent_start = 1, 30,
j_parent_start = 1, 30,
parent_grid_ratio = 1, 3,
parent_time_step_ratio = 1, 3,

ANEXO 3 - PARAMETRIZACIÓN METEOROLOGÍA DE PRONÓSTICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 38 de 41

feedback = 1,
smooth_option = 0,
/

&physics
mp_physics = 3, 3,
ra_lw_physics = 1, 1,
ra_sw_physics = 1, 1,
radt =12, 12,
sf_sfclay_physics = 4, 4,
sf_surface_physics = 1, 1,
bl_pbl_physics = 4, 4,
bldt = 0, 0,
cu_physics = 2, 2,
cudt = 0, 1,
isfflx = 1,
ifsnow = 0,
icloud = 1,
iz0tlnd = 1,
surface_input_source = 1,
slope_rad = 1,
num_land_cat = 21,
num_soil_cat = 16,
num_soil_layers = 4,
sf_urban_physics = 0, 0,

/

&fdda
/

&dynamics
w_damping = 1,
diff_opt = 1,
km_opt = 4,
diff_6th_opt = 0, 0,
diff_6th_factor = 0.12, 0.12,
base_temp = 290.
damp_opt = 0,
zdamp = 5000., 5000.,
dampcoef = 0.2, 0.2,
khdif = 0, 0,
kvdif = 0, 0,
non_hydrostatic = .true., .true.,
moist_adv_opt = 1, 1,
scalar_adv_opt = 1, 1,
/

&bdy_control
spec_bdy_width = 5,

ANEXO 3 - PARAMETRIZACIÓN METEOROLOGÍA DE PRONÓSTICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 39 de 41

spec_zone = 1,
relax_zone = 4,
specified = .true., .false.,
nested = .false., .true.,
/

&grib2
/

&namelist_quilt
nio_tasks_per_group = 0,
nio_groups = 1,
/

Figura 4 - Visualización de dominios anidados WRF

ANEXO 3 - PARAMETRIZACIÓN METEOROLOGÍA DE PRONÓSTICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 40 de 41

**6** **ANEXO 4 - JUSTIFICACIÓN BASE METEOROLÓGICA DE PRONÓSTICO**

**6.1** **Aplicabilidad del modelo**

Al momento de definir la aplicabilidad de un modelo de dispersión en particular (capacidad de representación
de la heterogeneidad y complejidad del terreno [31] ), se debe tener en consideración cuáles son los
requerimientos mínimos de los datos de entrada, de modo que se asegure la calidad de la información que
se pretende obtener del modelo. Además, tener claro que los modelos de dispersión son potentes
herramientas matemáticas de predicción, que describen la influencia de la turbulencia atmosférica sobre una
emisión en particular y su efecto sobre la dilución y dispersión en el entorno cercano [32] . La información
obtenida permitirá predecir y evaluar el potencial impacto de las fuentes representadas sobre una zona o
punto de interés [33] .

Debido a las características en donde se encontraría emplazada planta (Llanos de sedimentación entre la
Cordillera de la Costa y Depresión Intermedia), es de importancia la representación del comportamiento del
viento sobre las distintas elevaciones de terreno que se describen en el entorno local. La interacción de la
interface valle/cordillera [34], podría incrementar el potencial de impacto en los receptores situados próximos a
la instalación.
Estas condiciones de dispersión pueden ser abordadas de forma adecuada con un modelo de tipo “puff” como
CALPUFF. Dado que este modelo no presenta limitaciones respecto a bajas velocidades permitiendo al “puff”
crecer y difundirse sin un efecto de advección. Esta característica permite representar eventos de
estancamiento durante periodos con condición de calma donde los “puff” se acumularían en función del
tiempo.

Es importante tener en consideración, que el modelo CALPUFF permite una representación más realista de la
dinámica de vientos en la zona interés, al utilizar campos de vientos tridimensionales, característica ausente
en un modelo de tipo Gaussiano.
Los modelos Gaussianos no presentan efecto de memoria de los contaminantes emitidos en las horas previas.
Esta característica podría ser de importancia en dominios donde se presenten condiciones de vientos de baja
velocidad o de calma.

Por otra parte, con respecto a datos observados que representan información meteorológica objetiva del
lugar, no es usual disponer de registros que cumplan con los criterios, definidos por el SEA, para ser
incorporados al modelo. Según lo señalado en la Guía para el uso de modelos de calidad del aire en el SEIA,
en el caso del modelo de tipo “puff”, como CALPUFF, estos pueden incorporar meteorología proveniente de
un modelo meteorológico de pronóstico.

Las simulaciones deben abarcar todas las variaciones climáticas de la zona de estudio y así asegurar la
inclusión de las condiciones meteorológicas más desfavorables. Sin embargo, y como lo señala la Guía para
el uso de modelos de calidad del aire en el SEIA, “...por razones prácticas se recomienda una simulación de
al menos un año completo...”. Con relación a lo anterior, se entiende que la meteorología de un lugar es un
evento que responde a patrones climatológicos de gran escala y, por lo tanto, entre un año y otro no existen
mayores diferencias.

31 Servicio de Evaluación Ambiental. (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Chile.
32 Environment Agency. (2012). Horizontal Guidance: Technical Guidance Note - H4 Odour Management. Environment Agency.
33 Environment Agency. (2011). Horizontal Guidance: Environmental Permitting - H4 Odour Management. Environment Agency.
34 Barclay, J. Scire, J. (2011). Generic Guidance and Optimum Model Settings for the CALPUFF Modeling System for Inclusion into the Approved

Methods for the Modeling and Assessments of Air Pollutants in NSW. TRC Environmental Corporation. Australia.

ANEXO 4 - JUSTIFICACIÓN BASE METEOROLÓGICA DE PRONÓSTICO www.envirometrika.com

P6260B - Anexos meteorológicos del Estudio de Impacto Odorante Enero 2021
WSP Ambiental S.A. - Sunsweet Santa Cruz Página 41 de 41

**6.2** **Aplicabilidad de meteorología de pronóstico**

La proyección de dispersión odorante considera la aplicación del software de modelación atmosférica
“CALPUFF VIEW” versión 8.6.0, modelo alternativo indicado por EPA [35] (USA). El software contempla 3
módulos de análisis numérico: CALMET, CALPUFF (v7.2.1) y CALPOST.

CALMET es un modelo que simula campos de viento, temperaturas y otras variables meteorológicas, en un
dominio de modelación tridimensional. Sin embargo, en la Guía para el uso de modelos de calidad del aire
en el SEIA se menciona que “...En el caso de CALPUFF, se recomienda usar la información del modelo de
pronóstico directamente, sin usar el preprocesador CALMET” [36] .
De acuerdo con lo anterior, se utilizó como preprocesador meteorológico el modelo MMIF [37] recomendado por
EPA (USA), siendo una alternativa a CALMET en la generación de los campos tridimensionales para la
evaluación en el análisis de impacto en la calidad del aire [38] .

Tal como señala la Guía para el Uso de Modelos de Calidad del Aire en el SEIA, en el caso de los modelos
tipo “puff”, si bien son capaces de representar meteorología heterogénea en el dominio de modelación, no
tienen un desempeño muy superior a los modelos Gaussianos si se utilizan con información meteorológica de
sólo una estación y un radiosondeo como información de entrada. Es por ello que estos modelos debieran
usarse únicamente con datos provenientes de un modelo meteorológico de pronóstico.
En el caso de CALPUFF, se recomienda usar la información del modelo de pronóstico directamente, sin usar
el preprocesador CALMET.
Basado en estos criterios y dado que no se dispone de un conjunto de estaciones dentro del radio de
representatividad de 5 [km] y que cumplan con el porcentaje mínimo de 75% de datos válidos para el periodo
anual, se aplicó una base meteorológica WRF-MMIF en formato Calpuff-Ready, para su uso directo en el
modelo de dispersión Calpuff, dando cumplimiento a lo señalado por la Guía de Modelación. El uso de este
preprocesador permite convertir la información meteorológica de pronóstico a parámetros y formatos
requeridos para el ingreso directo al modelo de dispersión, siendo una alternativa a CALMET en la generación
de los campos tridimensionales para la evaluación en el análisis de impacto en la calidad del aire.

MMIF es un modelo que procesa específicamente los campos de salida geofísicos y meteorológicos de los
modelos de pronósticos como WRF, manteniendo la misma proyección y resolución del modelo meteorológico.
El procesamiento directo de la meteorología de pronóstico (WRF) en CALPUFF a partir de MMIF proporciona
un nivel mayor de consistencia de la base meteorológica sin modificaciones adicionales.

CALPUFF es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario, capaz de modelar el transporte y
dispersión de contaminantes sobre un campo de viento construido con MMIF.

Este tipo de modelo permite la representación de una pluma de emisión continua como un número discreto
de paquetes de material correspondiente a la especie de interés.
El modelo evalúa la contribución de un “puff” en la concentración atmosférica de un receptor en un instante
determinado. Luego, la concentración total en un receptor resultará de la sumatoria de las contribuciones de
todos los “puff”.

Finalmente, el modelo CALPOST procesa las salidas de CALPUFF creando así, los archivos con las tabulaciones
necesarias para la evaluación de los resultados según los percentiles definidos en el modelo.

35 Environmental Protection Agency, U.S.
36 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA. Chile. Servicio de Evaluación Ambiental,

Chile.
37 Mesoscale Model Interface Program, MMIF.
38 Brashers, B., Emery, C. (2014). Draft User’s Manual: The Mesoscale Model Interface Program (MMIF), Version 3.1. U.S. Environmental

Protection Agency.

ANEXO 4 - JUSTIFICACIÓN BASE METEOROLÓGICA DE PRONÓSTICO www.envirometrika.com

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: - Coordenadas representativas de Sunsweet Santa Cruz**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| X: Este | Y: Sur | Huso | Datum |
| 288.373 | 6.164.479 | 19 Sur | WGS-84 |

**Tabla 2: - Descripción de ciclos de análisis meteorológicos**

| Ciclo | Descripción | Col3 |
| --- | --- | --- |
| Anual | 12 meses | Enero a diciembre |
| Estacional | Verano | 22 de diciembre a 21 de marzo |
| Estacional | Otoño | 22 de marzo a 21 de junio |
| Estacional | Invierno | 22 de junio a 21 de septiembre |
| Estacional | Primavera | 22 de septiembre a 21 de diciembre |
| Horario | Nocturno | 00:00 a 06:59 |
| Horario | AM | 07:00 a 14:59 |
| Horario | PM | 15:00 a 23:59 |

**Tabla 3: - Rosas y campos de viento pronóstico anual**

| Col1 | Rosa de vientos | Col3 | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- |
| Anual Nocturno |  |  | <br>12,84<br>23,33<br>33,78<br>22,27<br>5,60<br>1,41<br>0,39<br>0,12<br>0,20<br>0,08<br>0<br>10<br>20<br>30<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de vientos predominaron desde la<br>dirección ESE con un 30% de la frecuencia.<br>La velocidad varió de ventolina1 a brisa débil. La<br>distribución del viento tuvo una tendencia<br>asimétrica positiva. <br> <br>Velocidad promedio de viento: 1,51 [m/s].<br> <br>Frecuencia de vientos calmos: 12,84%. |
| Anual AM |  |  | <br>12,98<br>14,90<br>23,87<br>19,18<br>15,21<br>10,07<br>2,77<br>0,51<br>0,31<br>0,21<br>0<br>10<br>20<br>30<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron en mayor<br>frecuencia desde el rango ESE-SE, con un 49%<br>de la frecuencia.<br>La velocidad varió de calma a brisa moderada2.<br>Respecto a la distribución de los vientos, éstos<br>tuvieron una tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,14 [m/s].<br> <br>Frecuencia de vientos calmos: 12,98%. |
| Anual PM |  |  | <br>10,41<br>17,23<br>28,80<br>21,19<br>11,72<br>6,48<br>2,74<br>0,88<br>0,33<br>0,21<br>0<br>10<br>20<br>30<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario PM, se observó una<br>predominancia de los vientos desde los rangos E-<br>ESE y OSO-O, con un 27% y 25% de la frecuencia<br>respectivamente. La velocidad de los vientos<br>varió de ventolina a brisa débil3.<br>La distribución de los vientos se observó con una<br>tendencia asimétrica positiva.<br> <br>Velocidad promedio de viento: 2,02 [m/s]<br> <br>Frecuencia de vientos calmos: 10,41% |

**Tabla 4: - Rosas y campos de viento pronóstico estacional - Verano**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Verano Nocturno |  |  |  | 13,02<br>28,89<br>41,43<br>14,29<br>2,38<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | El viento predominó desde la componente ESE,<br>con una frecuencia del 23%.<br>En general, la intensidad del viento se<br>caracterizó por variar de ventolina a brisa muy<br>débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 1,23 [m/s].<br> <br>Frecuencia de vientos calmos: 13,02%. |
| Verano AM |  |  |  | 14,31<br>17,64<br>24,17<br>23,47<br>12,22<br>6,81<br>1,39<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron con mayor<br>frecuencia desde la componente ESE, con un<br>28% de la frecuencia, y en menor medida,<br>desde dirección SE (15%). La velocidad del<br>viento varió de brisa muy débil a moderada. La<br>distribución marcó una tendencia asimétrica<br>positiva.<br> <br>Promedio velocidad del viento: 1,86 [m/s].<br> <br>Frecuencia de vientos calmos: 14,31%. |
| Verano PM |  |  |  | 11,11<br>18,27<br>28,89<br>18,89<br>13,21<br>6,30<br>1,85<br>1,48<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de viento predominaron desde el<br>rango OSO-O, con un 40% de la frecuencia. La<br>intensidad del viento fluctuó de brisa muy débil<br>a moderada. La curva de distribución tuvo una<br>tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 1,96 [m/s].<br> <br>Frecuencia de vientos calmos: 11,11%. |

**Tabla 5: - Rosas y campos de viento pronóstico estacional - Otoño**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Otoño Nocturno |  |  |  | 16,30<br>28,42<br>32,14<br>18,17<br>4,04<br>0,93<br>0,00<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de viento provinieron con mayor<br>frecuencia desde la componente ESE (25%) y<br>en menor medida desde la componente ONO<br>(11%). La intensidad del viento se caracterizó<br>como brisa muy débil a débil.<br>La distribución de frecuencia de velocidad del<br>viento muestra una tendencia asimétrica<br>positiva. <br> <br>Promedio velocidad del viento: 1,29 [m/s].<br> <br>Frecuencia de vientos calmos: 16,30%. |
| Otoño AM |  |  |  | 15,76<br>17,53<br>27,04<br>16,58<br>12,77<br>7,74<br>1,22<br>0,41<br>0,54<br>0,41<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | El viento provino con mayor frecuencia desde la<br>componente ESE (31%), y en menor medida,<br>desde SE (12%). La intensidad del viento<br>fluctuó de brisa muy débil a moderada.<br>Respecto a la distribución, ésta tuvo una<br>tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 1,89 [m/s].<br> <br>Frecuencia de vientos calmos: 15,76%. |
| Otoño PM |  |  |  | 13,65<br>18,96<br>32,00<br>21,62<br>7,00<br>3,38<br>1,57<br>0,48<br>0,48<br>0,85<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron en mayor<br>frecuencia desde el rango ESE-SE (32%) y en<br>menor medida desde el rango O-NO (28%). En<br>general, la velocidad del viento se caracterizó<br>como brisa muy débil.<br>La distribución de frecuencia de velocidad del<br>viento tuvo un comportamiento asimétrico<br>positivo. <br> <br>Promedio velocidad del viento: 1,76 [m/s].<br> <br>Frecuencia de vientos calmos: 13,65%. |

**Tabla 6: - Rosas y campos de viento pronóstico estacional - Invierno**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Invierno Nocturno |  |  |  | 11,65<br>19,41<br>25,16<br>26,24<br>10,87<br>3,88<br>1,40<br>0,31<br>0,78<br>0,31<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario nocturno los vientos<br>provinieron desde la componente ESE (43%).<br>En general, la intensidad del viento osciló de<br>brisa muy débil a moderada.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 1,89 [m/s].<br> <br>Frecuencia de vientos calmos: 11,65%. |
| Invierno AM |  |  |  | 9,65<br>12,09<br>25,00<br>14,27<br>15,08<br>14,81<br>6,66<br>1,36<br>0,68<br>0,41<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron desde las<br>componentes ESE (38%) y SE (20%). La<br>velocidad fluctuó de brisa muy débil a<br>moderada.<br>La<br>intensidad<br>del<br>viento<br>presentó<br>una<br>distribución heterogénea, con una mayor<br>frecuencia entorno al rango de 1-2 [ms]. <br> <br>Promedio velocidad del viento: 2,53 [m/s].<br> <br>Frecuencia de vientos calmos: 9,65%. |
| Invierno PM |  |  |  | 8,82<br>14,73<br>25,60<br>24,15<br>14,01<br>8,70<br>3,50<br>0,36<br>0,12<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de vientos provinieron con mayor<br>frecuencia desde ESE (28%), y en menor<br>medida desde E (17%). En general, la<br>intensidad del viento varió de brisa muy débil a<br>moderada y la distribución se presentó como<br>asimétrico positivo.<br> <br>Promedio velocidad del viento: 2,18 [m/s].<br> <br>Frecuencia de vientos calmos: 8,82%. |

**Tabla 7: - Rosas y campos de viento pronóstico estacional - Primavera**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Primavera Nocturno |  |  |  | 10,36<br>16,64<br>36,58<br>30,30<br>5,02<br>0,78<br>0,16<br>0,16<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Predominio de los vientos desde la componente<br>ESE, con una frecuencia del 30%.<br>En general, la velocidad del viento fluctuó de<br>brisa muy débil a moderada.<br>La distribución de frecuencia de velocidad del<br>viento tuvo una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 1,63 [m/s].<br> <br>Frecuencia de vientos calmos: 10,36%. |
| Primavera AM |  |  |  | 12,23<br>12,36<br>19,23<br>22,53<br>20,74<br>10,85<br>1,79<br>0,27<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron desde la<br>componente ESE, con una frecuencia del 40%.<br>La velocidad del viento osciló de brisa muy débil<br>a moderada.<br>La distribución de frecuencia de velocidad del<br>viento exhibió una curva con tendencia<br>asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,26 [m/s].<br> <br>Frecuencia de vientos calmos: 12,23%. |
| Primavera PM |  | <br> |  | 8,06<br>16,97<br>28,69<br>20,02<br>12,70<br>7,57<br>4,03<br>1,22<br>0,73<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>45<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario PM, los vientos provinieron<br>desde el rango OSO-NO, con una frecuencia del<br>43%.<br>La velocidad del viento varió de brisa muy débil<br>a moderada.<br>Respecto a la distribución de intensidad de<br>vientos, esta presentó un comportamiento<br>asimétrico positivo tendiente a la normalidad.<br> <br>Promedio velocidad del viento: 2,17 [m/s].<br> <br>Frecuencia de vientos calmos: 8,06%. |

**Tabla 10: - Estaciones meteorológicas superficiales en el dominio de modelación WRF**

| ID | Nombre estación | Coordenadas geográficas UTM Huso 19 | Col4 | Col5 | Datos válidos [%] | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ID | Nombre estación | Este [m] | Sur [m] | Distancia<br>a Planta<br>[km] | Dirección<br>viento | Velocidad<br>viento | Temperatura |
| **1 ** | **Palmilla**(a) | **280.207** | **6.174.620** | **12,7** | **75,06** | **79,63** | **95,25** |
| 2 | Liceo Jean Buchanan(a) | 301.015 | 6.191.667 | 15,6 | 98,55 | 87,45 | 98,06 |
| 3 | Placilla Chacarilla(a) | 304.252 | 6.164.625 | 29,7 | 98,55 | 87,45 | 98,01 |

**Tabla 11: - Coordenada de localización, serie de pronóstico WRF**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Este | Sur | Huso | Datum |
| 280.207 | 6.174.620 | 19 Sur | WGS 84 |

**Tabla 12: - Coordenada de localización estación meteorológica**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Este | Sur | Huso | Datum |
| 280.207 | 6.174.620 | 19 Sur | WGS 84 |

**Tabla 13: - Porcentaje datos válidos en parámetros evaluados**

| Parámetro meteorológico<br>evaluado | % datos válidos | Cumple con<br>recomendación SEA<br>(>75%) |
| --- | --- | --- |
| Velocidad del viento [m/s]<br>Dirección del viento [°]<br>Temperatura [°C] | 75,06%<br>79,63%<br>95,25% | <br><br> <br><br> <br> |

**Tabla 14: - Ciclos diarios de la temperatura - serie pronóstico**

| Hora | Promedio de<br>Temperatura [°C] | Percentil 5 | Percentil 95 |
| --- | --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 11,85<br>11,41<br>11,06<br>10,81<br>10,54<br>10,33<br>10,08<br>10,26<br>10,94<br>12,19<br>13,75<br>15,36<br>16,85<br>18,12<br>19,04<br>19,52<br>19,48<br>18,86<br>17,48<br>15,81<br>14,43<br>13,60<br>12,95<br>12,39 | 6,47<br>5,98<br>5,84<br>5,52<br>5,40<br>5,19<br>4,99<br>4,69<br>4,60<br>5,49<br>6,60<br>7,65<br>9,04<br>10,29<br>11,00<br>11,46<br>11,24<br>10,35<br>9,19<br>8,38<br>7,93<br>7,52<br>7,04<br>6,69 | 16,97<br>16,61<br>16,14<br>15,63<br>15,18<br>15,07<br>14,72<br>15,19<br>16,87<br>19,06<br>21,15<br>22,97<br>24,67<br>26,02<br>27,02<br>27,67<br>27,75<br>27,42<br>26,27<br>24,00<br>21,72<br>19,82<br>18,91<br>18,10 |

**Tabla 15: - Ciclos diarios de la temperatura - serie observada**

| Hora | Promedio de<br>temperatura [°C] | Percentil 5 | Percentil 95 |
| --- | --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 12,55<br>11,89<br>11,42<br>11,01<br>10,71<br>10,39<br>10,06<br>9,95<br>10,73<br>12,59<br>14,59<br>16,66<br>18,61<br>20,36<br>21,66<br>22,29<br>22,57<br>22,17<br>20,96<br>19,31<br>17,17<br>15,56<br>14,35<br>13,71 | 5,88<br>5,66<br>4,90<br>4,98<br>4,55<br>4,40<br>4,00<br>3,60<br>3,94<br>5,30<br>7,50<br>8,88<br>9,76<br>11,10<br>12,00<br>12,20<br>12,10<br>11,46<br>10,30<br>8,80<br>7,71<br>7,70<br>7,10<br>6,47 | 19,73<br>19,22<br>19,00<br>18,34<br>17,85<br>17,28<br>16,63<br>16,63<br>18,30<br>20,59<br>23,23<br>26,13<br>28,30<br>30,75<br>32,30<br>32,30<br>33,05<br>32,80<br>32,20<br>30,80<br>28,00<br>24,20<br>22,06<br>21,60 |

**Tabla 16: - Ciclos diarios promedios serie pronóstico**

| Hora | Promedio velocidad<br>del viento [m/s] | Percentil 5 | Percentil 95 |
| --- | --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 2,42<br>2,42<br>2,48<br>2,60<br>2,69<br>2,69<br>2,74<br>2,88<br>3,03<br>3,14<br>3,11<br>3,01<br>2,91<br>2,89<br>2,93<br>3,07<br>3,10<br>3,00<br>2,70<br>2,43<br>2,45<br>2,51<br>2,51<br>2,48 | 0,38<br>0,44<br>0,29<br>0,29<br>0,42<br>0,35<br>0,26<br>0,35<br>0,39<br>0,54<br>0,50<br>0,32<br>0,51<br>0,62<br>0,49<br>0,66<br>0,55<br>0,62<br>0,39<br>0,40<br>0,57<br>0,48<br>0,41<br>0,42 | 5,36<br>5,51<br>5,60<br>5,65<br>5,66<br>5,64<br>5,80<br>6,10<br>6,34<br>6,39<br>6,51<br>6,50<br>6,48<br>6,44<br>6,45<br>6,22<br>6,03<br>5,72<br>5,66<br>5,32<br>5,17<br>5,35<br>5,36<br>5,40 |

**Tabla 17: - Ciclos diarios promedios serie observada**

| Hora | Promedio velocidad<br>del viento [m/s] | Percentil 5 | Percentil 95 |
| --- | --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 1,22<br>1,32<br>1,47<br>1,48<br>1,42<br>1,56<br>1,49<br>1,54<br>1,83<br>2,02<br>2,03<br>2,16<br>2,02<br>2,11<br>2,04<br>2,03<br>2,13<br>1,86<br>1,72<br>1,63<br>1,35<br>1,23<br>1,24<br>0,92 | 0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,03<br>0,34<br>0,40<br>0,50<br>0,60<br>0,70<br>0,60<br>0,60<br>0,50<br>0,20<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00<br>0,00 | 2,80<br>2,90<br>3,60<br>3,12<br>3,20<br>3,10<br>3,10<br>3,30<br>3,78<br>3,80<br>3,80<br>4,00<br>3,60<br>3,77<br>4,00<br>3,80<br>4,40<br>4,10<br>4,00<br>3,60<br>2,90<br>2,80<br>2,90<br>2,60 |

**Tabla 18: - Ciclos diarios de dirección del viento serie pronóstico**

| 0-20 | 0.11 0.13 0.12 0.11 0.08 0.10 0.10 0.09 0.08 0.09 0.08 0.06 0.05 0.05 0.05 0.05 0.06 0.03 0.03 0.03 0.06 0.06 0.08 0.11<br>0.07 0.08 0.05 0.06 0.07 0.03 0.04 0.04 0.04 0.02 0.02 0.02 0.00 0.02 0.01 0.01 0.01 0.03 0.03 0.02 0.04 0.08 0.09 0.07<br>0.04 0.03 0.02 0.02 0.02 0.02 0.01 0.03 0.02 0.01 0.01 0.01 0.00 0.01 0.01 0.01 0.01 0.02 0.02 0.02 0.03 0.05 0.05 0.04<br>0.01 0.01 0.02 0.01 0.00 0.01 0.00 0.01 0.00 0.00 0.01 0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.01 0.01 0.03 0.03 0.03 0.02<br>0.00 0.01 0.01 0.00 0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.00 0.01 0.00 0.00 0.00 0.00 0.00 0.00 0.01 0.02 0.02 0.01 0.01<br>0.01 0.01 0.01 0.00 0.00 0.00 0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.00 0.00 0.01 0.01 0.01 0.02 0.02 0.03 0.00 0.01 0.00<br>0.01 0.01 0.02 0.01 0.01 0.01 0.01 0.00 0.01 0.00 0.00 0.00 0.00 0.01 0.01 0.00 0.00 0.00 0.00 0.02 0.02 0.03 0.01 0.01<br>0.05 0.03 0.02 0.02 0.02 0.02 0.01 0.01 0.02 0.01 0.01 0.03 0.10 0.11 0.15 0.12 0.11 0.07 0.04 0.06 0.12 0.12 0.08 0.06<br>0.18 0.19 0.17 0.13 0.13 0.13 0.14 0.10 0.13 0.17 0.25 0.29 0.27 0.29 0.23 0.25 0.22 0.21 0.21 0.21 0.19 0.22 0.23 0.24<br>0.29 0.31 0.33 0.41 0.40 0.35 0.35 0.39 0.38 0.37 0.30 0.22 0.18 0.12 0.13 0.13 0.12 0.15 0.18 0.21 0.25 0.21 0.25 0.22<br>0.07 0.07 0.06 0.07 0.08 0.14 0.13 0.14 0.11 0.08 0.06 0.03 0.02 0.02 0.02 0.04 0.05 0.10 0.10 0.12 0.07 0.04 0.04 0.05<br>0.00 0.00 0.01 0.01 0.01 0.01 0.01 0.00 0.00 0.00 0.01 0.01 0.00 0.01 0.01 0.03 0.08 0.10 0.14 0.09 0.02 0.01 0.01 0.01<br>0.00 0.00 0.00 0.00 0.00 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.01 0.00 0.01 0.02 0.04 0.04 0.04 0.04 0.01 0.00 0.01 0.01<br>0.00 0.00 0.01 0.00 0.00 0.00 0.02 0.01 0.00 0.00 0.00 0.01 0.01 0.01 0.00 0.01 0.00 0.01 0.01 0.00 0.00 0.01 0.00 0.01<br>0.00 0.00 0.01 0.01 0.02 0.01 0.01 0.00 0.00 0.00 0.01 0.01 0.00 0.00 0.01 0.02 0.02 0.01 0.01 0.00 0.00 0.01 0.01 0.01<br>0.01 0.01 0.01 0.02 0.03 0.01 0.02 0.02 0.01 0.02 0.02 0.02 0.03 0.02 0.05 0.03 0.03 0.03 0.04 0.03 0.02 0.01 0.02 0.02<br>0.04 0.03 0.03 0.02 0.03 0.04 0.04 0.05 0.05 0.03 0.05 0.08 0.13 0.12 0.11 0.09 0.09 0.11 0.08 0.06 0.04 0.04 0.03 0.03<br>0.10 0.09 0.10 0.09 0.09 0.11 0.10 0.11 0.13 0.18 0.17 0.18 0.19 0.21 0.18 0.19 0.14 0.09 0.06 0.05 0.05 0.05 0.05 0.09 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 | 20-40 |
| 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 | 40-60 |
| 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 | 60-80 |
| 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 | 80-100 |
| 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 | 100-120 |
| 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 | 120-140 |
| 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 | 140-160 |
| 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 | 160-180 |
| 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 | 180-200 |
| 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 | 200-220 |
| 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 | 220-240 |
| 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 | 240-260 |
| 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 | 260-280 |
| 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 | 280-300 |
| 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 | 300-320 |
| 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 | 320-340 |
| 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 | 340-360 |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |

**Tabla 19: - Ciclos diarios de dirección del viento serie observada**

| Col1 | Dirección del viento [grados] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hora<br>Del día | 0-20 | 20-40 | 40-60 | 60-80 | 80-100 | 100-120 | 120-140 | 140-160 | 160-180 | 180-200 | 200-220 | 220-240 | 240-260 | 260-280 | 280-300 | 300-320 | 320-340 | 340-360 |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 | 17<br>12<br>8 <br>5 <br>4 <br>0 <br>4 <br>2 <br>27<br>64<br>44<br>15<br>0 <br>0 <br>1 <br>1 <br>4 <br>14<br>17<br>11<br>5 <br>4 <br>2 <br>0 <br>1 <br>1 <br>16<br>61<br>46<br>14<br>1 <br>1 <br>0 <br>3 <br>6 <br>13<br>13<br>5 <br>1 <br>0 <br>0 <br>0 <br>0 <br>1 <br>21<br>52<br>47<br>20<br>0 <br>2 <br>1 <br>1 <br>4 <br>12<br>7 <br>3 <br>1 <br>1 <br>0 <br>2 <br>2 <br>0 <br>27<br>54<br>58<br>14<br>1 <br>1 <br>1 <br>3 <br>4 <br>12<br>3 <br>2 <br>1 <br>2 <br>1 <br>0 <br>1 <br>2 <br>30<br>65<br>56<br>12<br>0 <br>0 <br>1 <br>1 <br>5 <br>10<br>7 <br>5 <br>1 <br>5 <br>2 <br>0 <br>1 <br>0 <br>27<br>50<br>70<br>14<br>1 <br>0 <br>1 <br>0 <br>3 <br>7 <br>9 <br>5 <br>2 <br>5 <br>0 <br>0 <br>3 <br>1 <br>25<br>60<br>70<br>10<br>0 <br>0 <br>2 <br>0 <br>7 <br>6 |
| 07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 | 9 <br>1 <br>3 <br>2 <br>0 <br>0 <br>2 <br>1 <br>23<br>79<br>61<br>14<br>1 <br>1 <br>2 <br>0 <br>7 <br>10<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>8 <br>8 <br>2 <br>3 <br>1 <br>2 <br>0 <br>0 <br>17<br>102<br>80<br>8 <br>2 <br>2 <br>3 <br>2 <br>17<br>28<br>3 <br>7 <br>5 <br>1 <br>1 <br>6 <br>1 <br>2 <br>28<br>137<br>64<br>4 <br>2 <br>3 <br>5 <br>9 <br>14<br>28<br>2 <br>5 <br>4 <br>1 <br>2 <br>3 <br>2 <br>1 <br>29<br>111<br>72<br>15<br>4 <br>2 <br>4 <br>1 <br>25<br>44<br>3 <br>1 <br>4 <br>0 <br>2 <br>4 <br>2 <br>3 <br>17<br>129<br>49<br>20<br>9 <br>6 <br>9 <br>10<br>33<br>35<br>0 <br>1 <br>2 <br>2 <br>3 <br>0 <br>7 <br>3 <br>22<br>120<br>49<br>12<br>8 <br>6 <br>9 <br>19<br>40<br>34<br>2 <br>0 <br>4 <br>1 <br>2 <br>1 <br>3 <br>4 <br>33<br>111<br>41<br>10<br>4 <br>6 <br>12<br>28<br>49<br>29 |
| 15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 | 2 <br>3 <br>6 <br>3 <br>3 <br>1 <br>4 <br>5 <br>28<br>111<br>39<br>10<br>17<br>14<br>11<br>16<br>44<br>22<br>6 <br>3 <br>5 <br>5 <br>3 <br>4 <br>3 <br>4 <br>36<br>100<br>38<br>14<br>10<br>4 <br>8 <br>15<br>46<br>36<br>3 <br>3 <br>2 <br>2 <br>4 <br>2 <br>2 <br>4 <br>35<br>103<br>36<br>20<br>11<br>10<br>10<br>21<br>41<br>28<br>6 <br>2 <br>1 <br>0 <br>2 <br>2 <br>2 <br>0 <br>40<br>85<br>46<br>35<br>6 <br>5 <br>8 <br>12<br>42<br>34<br>2 <br>6 <br>3 <br>1 <br>2 <br>2 <br>2 <br>4 <br>35<br>68<br>74<br>31<br>6 <br>4 <br>3 <br>5 <br>21<br>46<br>6 <br>8 <br>6 <br>1 <br>2 <br>1 <br>1 <br>3 <br>67<br>92<br>63<br>16<br>0 <br>3 <br>0 <br>4 <br>12<br>16<br>3 <br>6 <br>4 <br>1 <br>3 <br>2 <br>3 <br>5 <br>94<br>80<br>48<br>15<br>1 <br>1 <br>2 <br>0 <br>6 <br>8 <br>7 <br>6 <br>5 <br>9 <br>1 <br>0 <br>3 <br>3 <br>79<br>79<br>35<br>21<br>0 <br>0 <br>2 <br>0 <br>1 <br>15<br>18<br>14<br>7 <br>9 <br>2 <br>1 <br>3 <br>6 <br>52<br>63<br>35<br>10<br>0 <br>0 <br>1 <br>1 <br>4 <br>12 |

**Tabla 20: - Frecuencia mensual de vientos calmos - serie pronóstico**

| Mes | Frecuencia de<br>vientos calmos | N°<br>días | % |
| --- | --- | --- | --- |
| Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre | 45<br>71<br>79<br>51<br>51<br>45<br>45<br>22<br>31<br>42<br>26<br>41 | 744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744 | 6%<br>11%<br>11%<br>7%<br>7%<br>6%<br>6%<br>3%<br>4%<br>6%<br>4%<br>6% |

**Tabla 21: - Frecuencia horaria de vientos calmos - serie pronóstico**

| Hora | Frecuencia de<br>vientos calmos | % |
| --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00<br> | 27<br>22<br>33<br>29<br>28<br>32<br>31<br>32<br>25<br>17<br>19<br>26<br>18<br>16<br>19<br>14<br>14<br>17<br>23<br>26<br>13<br>20<br>23<br>25<br> | 7%<br>6%<br>9%<br>8%<br>8%<br>9%<br>8%<br>9%<br>7%<br>5%<br>5%<br>7%<br>5%<br>4%<br>5%<br>4%<br>4%<br>5%<br>6%<br>7%<br>4%<br>5%<br>6%<br>7% |

**Tabla 22: - Frecuencia mensual de vientos calmos - serie observada**

| Mes | Frecuencia de<br>vientos calmos | N°<br>días | % |
| --- | --- | --- | --- |
| Enero<br>Febrero<br>Marzo<br>Abril<br>Mayo<br>Junio<br>Julio<br>Agosto<br>Septiembre<br>Octubre<br>Noviembre<br>Diciembre | 69<br>67<br>73<br>72<br>65<br>56<br>43<br>52<br>33<br>53<br>42<br>36 | 744<br>672<br>744<br>720<br>744<br>720<br>744<br>744<br>720<br>744<br>720<br>744 | 9%<br>10%<br>10%<br>10%<br>9%<br>8%<br>6%<br>7%<br>5%<br>7%<br>6%<br>5% |

**Tabla 23: - Frecuencia horaria de vientos calmos - serie observada**

| Hora | Frecuencia de<br>vientos calmos | % |
| --- | --- | --- |
| 00:00<br>01:00<br>02:00<br>03:00<br>04:00<br>05:00<br>06:00<br>07:00<br>08:00<br>09:00<br>10:00<br>11:00<br>12:00<br>13:00<br>14:00<br>15:00<br>16:00<br>17:00<br>18:00<br>19:00<br>20:00<br>21:00<br>22:00<br>23:00 | 52<br>34<br>20<br>22<br>19<br>17<br>27<br>25<br>20<br>15<br>12<br>6 <br>7 <br>5 <br>10<br>9 <br>13<br>26<br>42<br>33<br>48<br>61<br>60<br>78 | 14%<br>9%<br>5%<br>6%<br>5%<br>5%<br>7%<br>7%<br>5%<br>4%<br>3%<br>2%<br>2%<br>1%<br>3%<br>2%<br>4%<br>7%<br>12%<br>9%<br>13%<br>17%<br>16%<br>21% |

**Tabla 24: - Error medio cuadrático, sesgo, coeficiente de correlación, IOA, velocidad del viento y temperatura**

| Estadístico | Descripción | Fórmula | Resultado | Col5 |
| --- | --- | --- | --- | --- |
| Estadístico | Descripción | Fórmula | Velocidad del<br>viento [m/s] | Temperatura<br>[°C] |
| RMSE | Error medio cuadrático (Root<br>mean square Error), nos indica la<br>medida de las diferencias en<br>promedio<br>entre<br>valores<br>pronosticados y observados |  | 1,86 | 3,21 |
| NRMSD | Error<br>medio<br>cuadrático<br>normalizado<br>(Normalized<br>Root<br>mean square deviation) señala la<br>varianza residual entre los valores<br>pronosticados y observados |  | 0,28 | 0,09 |
| NMAE | Error medio absoluto normalizado,<br>toma en cuenta el peso del error<br>respecto al valor de la variable<br>medida,<br>normaliza<br>el<br>error<br>absoluto |  | 0,23 | 0,07 |
| BIAS | Sesgo, proporciona información<br>sobre la tendencia del modelo a<br>sobrestimar o subestimar una<br>variable |  | 1,25 | -1,49 |
| Coeficiente de<br>correlación de<br>Pearson | Un índice que mide el grado de<br>relación de dos variables siempre<br>y <br>cuando<br>ambas<br>sean<br>cuantitativas. |  | 0,60 | 0,93 |
| IOA | El IOA (Index Of Agreement)<br>acuerdo es una medida de la<br>coincidencia entre la salida de<br>cada predicción de la media<br>observada y la salida de cada<br>observación<br>de<br>la<br>media |  | 0,69 | 1,00 |
