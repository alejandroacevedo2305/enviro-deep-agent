---
title: Sin título
author: Adrián González
date: D:20221012130027-03'00'
language: es
type: report
pages: 30
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO: P6764-Análisis de Incertidumbre SOLICITANTE: F4F SpA
  - Fecha: Septiembre 2022 At: Sr. Claudio Huircán
-->

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 1 de 30

# PROYECTO: P6764-Análisis de Incertidumbre SOLICITANTE: F4F SpA

# Fecha: Septiembre 2022 At: Sr. Claudio Huircán

CONTROL DE CAMBIOS www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 2 de 30

Análisis de Incertidumbre
Nombre Ficha:
F4F SpA - Planta Talca

Reporte no: Borrador 0.1

Código de proyecto: P 6764

Meteorología, incertidumbre, dispersión, variables ambientales,
Palabras claves
rosas de viento, transporte de contaminantes

Preparado a petición de: F4F SpA

Contacto: Sr. Claudio Huircán - Jefe de planta

Preparado por:

Envirometrika

Europa 2066 - Providencia - Santiago - Chile  56 2 2668 1260
Arturo Prat 199 -Torre A of 1401 Concepción  56 41 383 3978
[e-mail: info@envirometrika.com](mailto:info@envirometrika.com)

[www.envirometrika.com](http://www.envirometrika.com/)

Tamara Araya
Autores:
Camila Reyes

Firmado y aprobado por: Envirometrika por Héctor Vergara

Fecha: Septiembre 2022

CONTROL DE CAMBIOS www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 3 de 30

**CONTROL DE CAMBIOS**

|DESARROLLADO POR:|FIRMA|ÁREA|
|---|---|---|
|Tamara Araya||Modelación y Simulación|
|Camila Reyes||Modelación y Simulación|

|REVISADO POR:|FIRMA|ÁREA|
|---|---|---|
|Ricardo Guerra||Modelación y Simulación|

|APROBADO POR:|FIRMA|ÁREA|
|---|---|---|
|Héctor Vergara||Gerencia|

**REVISIONES**

|REVISIÓN|TIPO DE CAMBIO|FECHA|
|---|---|---|
|V 0.1|1a revisión reporte borrador para<br>entrega al cliente|09 de septiembre de 2022|
|V 1.0|Envío reporte final|12 de octubre de 2022|

CONTROL DE CAMBIOS www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 4 de 30

**ÍNDICE**

CONTROL DE CAMBIOS ................................................................................................................................. 3
ÍNDICE ......................................................................................................................................................... 4
1 ANÁLISIS METEOROLÓGICO ................................................................................................................... 6

1.1 Rosas de viento anual - horaria ...................................................................................................... 7

1.2 Rosas de viento estacional - horaria ................................................................................................ 8
1.3 Caracterización geográfica ............................................................................................................ 12
1.4 Altura de mezcla........................................................................................................................... 13
2 ANÁLISIS DE INCERTIDUMBRE ............................................................................................................. 15
2.1 Etapa 1 - Diagnóstico de datos meteorológicos observados ............................................................ 15
Series de tiempo ....................................................................................................................... 17
Ciclos diarios ............................................................................................................................ 20
2.2 Etapa 2 - Comparación entre pronóstico y observaciones ............................................................... 23
Análisis cualitativo de serie de pronóstico y observada ................................................................ 23
Análisis cuantitativo de serie de pronóstico y observada .............................................................. 27
3 ANÁLISIS DE RESULTADOS ................................................................................................................... 29
4 BIBLIOGRAFÍA ..................................................................................................................................... 30

**ÍNDICE TABLAS**
Tabla 1 - Coordenadas representativas de Planta Talca ................................................................................... 6
Tabla 2 - Descripción de ciclos de análisis meteorológicos ............................................................................... 6
Tabla 3 - Rosas y campos de viento pronóstico anual ..................................................................................... 7
Tabla 4 - Rosas y campos de viento pronóstico estacional - Verano ................................................................ 8
Tabla 5 - Rosas y campos de viento pronóstico estacional - Otoño .................................................................. 9
Tabla 6 - Rosas y campos de viento pronóstico estacional - Invierno ............................................................. 10
Tabla 7 - Rosas y campos de viento pronóstico estacional - Primavera .......................................................... 11
Tabla 8 - Registro de ortofotografías - Isolíneas de altura de mezcla ............................................................. 14
Tabla 9 - Altura de mezcla - promedios por periodo estacional y horario [m] ................................................. 14
Tabla 10 - Coordenada de localización estación meteorológica La Florida ....................................................... 15
Tabla 11 - Porcentaje datos válidos ............................................................................................................. 16
Tabla 12 - Resumen de estadísticos de incertidumbre ................................................................................... 27

**ÍNDICE GRÁFICOS**
Gráfico 1 - Altura de mezcla y temperatura - Serie de tiempo ....................................................................... 14
Gráfico 2 - Serie pronóstico, temperatura [°C] .............................................................................................. 17
Gráfico 3 - Serie observada, temperatura [°C] .............................................................................................. 17
Gráfico 4 - Serie pronóstico, velocidad del viento [m/s] ................................................................................. 18
Gráfico 5 - Serie observada, velocidad del viento [m/s] ................................................................................. 18
Gráfico 6 - Serie pronóstico, humedad relativa [%]....................................................................................... 19
Gráfico 7 - Serie observada, humedad relativa [%] ....................................................................................... 19
Gráfico 8 - Ciclos diarios promedios de la temperatura - serie pronóstico ....................................................... 20
Gráfico 9 - Ciclos diarios promedios de la temperatura - serie observada ....................................................... 20
Gráfico 10 - Ciclos diarios promedios de velocidad del viento - serie pronóstico .............................................. 21
Gráfico 11 - Ciclos diarios promedios de velocidad del viento - serie observada .............................................. 21
Gráfico 12 - Ciclos diarios promedios de humedad relativa - serie pronóstico .................................................. 22
Gráfico 13 - Ciclos diarios promedios de humedad relativa - serie observada .................................................. 22
Gráfico 14 - Ciclos diarios promedios de temperatura, serie pronóstico y observado ....................................... 23
Gráfico 15 - Ciclos diarios promedios de velocidad del viento, serie pronóstico y observada ............................ 23
Gráfico 16 - Ciclos diarios promedios de humedad relativa, serie pronóstico y observada ................................ 24

ÍNDICE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 5 de 30

Gráfico 17 - Ciclos diarios de variación del viento, serie pronóstico ................................................................ 24
Gráfico 18 - Ciclos diarios de variación del viento, serie observada ................................................................ 24
Gráfico 19 - Distribución anual de frecuencia de velocidad del viento serie pronóstico y observada. ................. 25
Gráfico 20 - Rosas de viento anual por periodo horario, serie pronóstico y observada ..................................... 25
Gráfico 21 - Rosas de viento anual según periodo horario, serie pronóstico y observada ................................. 26
Gráfico 22 - Rosas de viento anual por periodo estacional, serie pronóstico y observada ................................. 26

**ÍNDICE FIGURAS**
Figura 1 - Comportamiento de campos de viento .......................................................................................... 12
Figura 2 - Distribución general de altura de mezcla (ortofotografías) ............................................................. 13
Figura 3 - Localización de estación meteorológica La Florida ......................................................................... 16

ÍNDICE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 6 de 30

**1** **ANÁLISIS METEOROLÓGICO**

La evaluación del comportamiento de los parámetros meteorológicos y su interacción a nivel local se realizó a
partir de series de datos horarios para el periodo de un año, extraídas desde la grilla meteorológica de
pronóstico WRF-MMIF’21. Cuya extracción fue en base a coordenadas representativas de la instalación, donde
se localizan las fuentes de emisión consideradas en el presente estudio.

Tabla 1 - Coordenadas representativas de Planta Talca

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|X: Este|Y: Sur|Huso|Datum|
|259.549|6.072.856|19 Sur|WGS-84|

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

La evaluación de campos de viento incluyó antecedentes bibliográficos topoclimáticos que describen la
dinámica y cinética de las masas de aire que interactúan en la zona de estudio. Esta información permite
evaluar la coherencia de las series de datos obtenidas de la meteorología de pronóstico e interpretar las
variables de influencia en las condiciones de dispersión.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 7 de 30

**1.1** **Rosas de viento anual - horaria**

Los campos de viento están determinados por la velocidad del viento y las componentes vectoriales de
dirección, producto del comportamiento dinámico de las masas de aire. La interacción de estas
componentes caracteriza el comportamiento del viento y cómo intervienen en la dispersión de
contaminantes en el área de interés.

Tabla 3 - Rosas y campos de viento pronóstico anual

|Col1|Rosa de viento|Col3|Distribución de velocidad del viento|Col5|Características|
|---|---|---|---|---|---|
|Anual Nocturno|||5,09<br>12,88<br>34,40<br>25,32<br>15,26<br>5,13<br>1,37<br>0,27<br>0,23<br>0,04<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**||El viento predominó desde la componente SSO,<br>con un 32% de la frecuencia.<br>La velocidad varió de brisa muy débil 1 a<br>moderada, observándose brisas frescas, en<br>menor frecuencia.<br>La distribución de frecuencia de velocidad de<br>viento presentó una asimetría positiva.<br> <br>Promedio velocidad del viento: 2,09 [m/s].<br> <br>Frecuencia de vientos calmos: 5,09%.|
|Anual AM|||<br>4,83<br>11,99<br>30,03<br>23,36<br>15,45<br>7,12<br>3,80<br>1,95<br>0,68<br>0,79<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>4,83<br>11,99<br>30,03<br>23,36<br>15,45<br>7,12<br>3,80<br>1,95<br>0,68<br>0,79<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>Las masas de viento provinieron en mayor<br>frecuencia desde el rango S-SSO (50%).<br>La intensidad del viento osciló de brisa muy<br>débil<br>2 a<br>moderada.<br>Adicionalmente,<br>se<br>registraron brisas frescas.<br>La curva de distribución tuvo una tendencia<br>asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,42 [m/s].<br> <br>Frecuencia de vientos calmos: 4,83%.|
|Anual PM|||<br>3,04<br>8,74<br>28,89<br>27,18<br>18,81<br>8,04<br>2,89<br>1,46<br>0,58<br>0,37<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>3,04<br>8,74<br>28,89<br>27,18<br>18,81<br>8,04<br>2,89<br>1,46<br>0,58<br>0,37<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de viento provinieron con mayor<br>frecuencia desde el SSO (31%). En general, la<br>velocidad fluctuó de brisa muy débil<br>3 a<br>moderada.<br>Respecto a la distribución de la velocidad, ésta<br>tuvo un sesgo positivo.<br> <br>Promedio velocidad del viento: 2,51 [m/s].<br> <br>Frecuencia de vientos calmos: 3,04%.|

Fuente: Envirometrika, 2022.

Del análisis meteorológico anual WRF-MMIF’21 se resume que:

Se observó una mayor frecuencia de dirección de viento desde la componente SSO. La distribución de
frecuencia de velocidad de viento tiene una tendencia asimétrica positiva, caracterizada por la fluctuación de
intensidad de rango de brisa muy débil a moderada. Respecto a los vientos calmos, arrojó que la mayor
probabilidad de ocurrencia se presentaría en horario nocturno.

1 Organización Meteorológica Mundial. (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A - Claves alfanuméricas - Escala

Beaufort de Viento. OMM-N°306. OMM. Suiza.
2 Ibíd.
3 Ibíd.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 8 de 30

**1.2** **Rosas de viento estacional - horaria**

Tabla 4 - Rosas y campos de viento pronóstico estacional - Verano

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Col6|Col7|Características|
|---|---|---|---|---|---|---|---|
|Verano Nocturno|||||7,78<br>17,14<br>34,92<br>22,38<br>11,43<br>5,56<br>0,79<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**||El viento predominó desde la componente SSO,<br>con una frecuencia del 34%.<br>En general, la intensidad del viento varió de brisa<br>muy débil a moderada y la curva de distribución<br>tuvo una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 1,87 [m/s].<br> <br>Frecuencia de vientos calmos: 7,78%.|
|Verano AM|||||||Las masas de aire provinieron con mayor<br>frecuencia desde el rango S-SO (53%). La<br>velocidad varió de brisa muy débil a moderada.<br>La curva de distribución marcó una tendencia<br>asimétrica positiva.<br> <br>Promedio velocidad del viento: 1,95 [m/s].<br> <br>Frecuencia de vientos calmos: 7,64%.|
|Verano AM|||||7,64<br>17,50<br>33,61<br>19,31<br>13,61<br>6,81<br>1,53<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|7,64<br>17,50<br>33,61<br>19,31<br>13,61<br>6,81<br>1,53<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|7,64<br>17,50<br>33,61<br>19,31<br>13,61<br>6,81<br>1,53<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|
|Verano PM|||||1,36<br>5,43<br>25,80<br>33,09<br>24,94<br>7,41<br>1,85<br>0,00<br>0,00<br>0,12<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**||Los campos de viento predominaron desde el<br>3ocuadrante, con un 82% de la frecuencia. La<br>intensidad fluctuó de brisa débil a moderada. La<br>curva de distribución arrogó un comportamiento<br>leptocúrtico agrupándose mayormente en el<br>rango 2-3[m/s]. <br> <br>Promedio velocidad del viento: 2,55 [m/s].<br> <br>Frecuencia de vientos calmos: 1,36%.|

Planta Talca.
Fuente: Envirometrika, 2022.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 9 de 30

Tabla 5 - Rosas y campos de viento pronóstico estacional - Otoño

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Col6|Col7|Características|
|---|---|---|---|---|---|---|---|
|Otoño Nocturno|||||5,28<br>14,75<br>33,85<br>24,07<br>17,08<br>4,19<br>0,78<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**||Los campos de viento provinieron con mayor<br>frecuencia desde la componente SSO (31%) y<br>en menor medida desde SO (16%). La<br>intensidad del viento osciló de brisa muy débil<br>a moderada. La curva de distribución presentó<br>una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,01 [m/s].<br> <br>Frecuencia de vientos calmos: 5,28%.|
|Otoño AM||||<br> <br>4,76<br>12,23<br>28,94<br>26,22<br>16,98<br>6,93<br>2,45<br>0,82<br>0,41<br>0,27<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br> <br>4,76<br>12,23<br>28,94<br>26,22<br>16,98<br>6,93<br>2,45<br>0,82<br>0,41<br>0,27<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br> <br>4,76<br>12,23<br>28,94<br>26,22<br>16,98<br>6,93<br>2,45<br>0,82<br>0,41<br>0,27<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|El viento predominó con mayor frecuencia<br>desde la componente SSO (32%), y en menor<br>medida, desde la componente S (18%). La<br>intensidad del viento fluctuó de brisa muy débil<br>a débil.<br>Respecto a la distribución, ésta tuvo una<br>tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 2,30 [m/s].<br> <br>Frecuencia de vientos calmos: 4,76%.|
|Otoño PM||||<br>4,95<br>11,11<br>35,63<br>29,23<br>13,77<br>4,35<br>0,72<br>0,24<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>4,95<br>11,11<br>35,63<br>29,23<br>13,77<br>4,35<br>0,72<br>0,24<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|<br>4,95<br>11,11<br>35,63<br>29,23<br>13,77<br>4,35<br>0,72<br>0,24<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provienen en mayor<br>frecuencia desde la componente SSO (30%) y<br>en menor medida desde las componentes S y<br>SO (14%). En general, la velocidad varió de<br>brisa muy débil a moderada.<br>La curva de distribución tiende a una asimétrica<br>positiva, agrupándose mayormente en el rango<br>de 1-2 [m/s]. <br> <br>Promedio velocidad del viento: 2,05 [m/s].<br> <br>Frecuencia de vientos calmos: 4,95%.|

Planta Talca
Fuente: Envirometrika, 2022.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 10 de 30

Tabla 6 - Rosas y campos de viento pronóstico estacional - Invierno

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Invierno Nocturno||||<br>3,73<br>12,27<br>34,63<br>23,29<br>15,53<br>5,90<br>2,80<br>0,78<br>0,93<br>0,16<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario nocturno los vientos<br>provinieron desde las componentes SSO (22%)<br>y NE (11%). En general, la intensidad osciló de<br>brisa muy débil a moderado, generando una<br>curva de distribución asimétrica positiva.<br> <br>Promedio velocidad del viento: 2,27 [m/s].<br> <br>Frecuencia de vientos calmos: 3,73%.|
|Invierno AM||||<br> <br>3,67<br>11,55<br>30,43<br>22,96<br>13,18<br>5,43<br>5,71<br>3,40<br>1,09<br>2,58<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron desde las<br>componentes SSO (25%), S (19%). La<br>velocidad fluctuó de brisa muy débil a<br>moderada, donde la distribución tuvo una curva<br>de<br>distribución<br>asimétrica<br>positiva,<br>agrupándose mayormente en el rango de 1-4<br>[m/s]. <br> <br>Promedio velocidad del viento: 2,66 [m/s].<br> <br>Frecuencia de vientos calmos: 3,67%.|
|Invierno PM||||<br>5,07<br>13,16<br>30,68<br>20,77<br>14,01<br>7,37<br>3,86<br>2,90<br>0,97<br>1,21<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de vientos provinieron con mayor<br>frecuencia desde SSO (23%), y en menor<br>medida desde s (9%). En general, la intensidad<br>varió de brisa muy débil a moderada y la<br>distribución se presentó con sesgo positivo.<br> <br>Promedio velocidad del viento: 2,47 [m/s].<br> <br>Frecuencia de vientos calmos: 5,07%.|

Planta Talca
Fuente: Envirometrika, 2022.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 11 de 30

Tabla 7 - Rosas y campos de viento pronóstico estacional - Primavera

|Col1|Rosa de viento|Col3|Campos de viento|Distribución de velocidad del viento|Características|
|---|---|---|---|---|---|
|Primavera Nocturno||||<br>3,61<br>7,38<br>34,22<br>31,55<br>16,95<br>4,87<br>1,10<br>0,31<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Los campos de viento predominaron desde la<br>componente SSO, con una frecuencia del 41%.<br>En general, los vientos fluctuaron de brisa muy<br>débil a moderada, donde la distribución tuvo<br>una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,21 [m/s].<br> <br>Frecuencia de vientos calmos: 3,61%.|
|Primavera AM||||<br>3,30<br>6,73<br>27,20<br>24,86<br>17,99<br>9,34<br>5,49<br>3,57<br>1,24<br>0,27<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Las masas de aire provinieron desde las<br>componentes: SSO (41%), S (20%).<br>La velocidad de los vientos osciló de brisa muy<br>débil a moderada; en la distribución, estas<br>exhibieron curva con tendencia asimétrica<br>positiva. <br> <br>Promedio velocidad del viento: 2,76 [m/s].<br> <br>Frecuencia de vientos calmos: 3,30%.|
|Primavera PM||<br>||<br>0,73<br>5,13<br>23,32<br>25,76<br>22,71<br>13,06<br>5,13<br>2,69<br>1,34<br>0,12<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]**|Durante el horario PM, los vientos provinieron<br>en mayor frecuencia desde la componente SSO<br>(42%) y en menor medida desde SO (14%).<br>La velocidad varió de brisa muy débil a<br>moderada.<br>Respecto a la distribución de intensidad de<br>vientos, esta presentó un comportamiento<br>mesocúrtico.<br> <br>Promedio velocidad del viento: 2,98 [m/s].<br> <br>Frecuencia de vientos calmos: 0,73%.|

Planta Talca
Fuente: Envirometrika, 2022.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 12 de 30

**1.3** **Caracterización geográfica**

Figura 1 - Comportamiento de campos de viento

Fuente: Envirometrika, 2022.

A nivel regional, el área de estudio se inserta en la unidad geomorfológica denominada como Llano Central
Fluvio-Galcio-Volcánico (depresión intermedia), presenta un relieve plano sólo interrumpido por los
numerosos ríos que lo atraviesan en sentido este-oeste. Sin embargo, hacia la parte central y sur de la
región aparece entre la depresión intermedia y la cordillera de los Andes un relieve precordillerano de alturas
de entre 400 y 1.000 [msnm], que le quita limpieza a la depresión intermedia y que se conoce con el
nombre de "La Montaña". A nivel más local, la comuna presenta algunos relieves conformados por cerros
islas y algunas estribaciones orientales de la cordillera de la Costa [4] .

La comuna forma parte de la cuenca hidrográfica del Río Maule, correspondiente a uno de los más
importantes del país, nace en la Cordillera de los Andes, recorre la llanura aluvial central hasta llegar a la
Cordillera de la Costa donde se une el Río Claro para finalmente desembocar el océano por el sector de
Constitución [5] .

En términos climáticos se caracteriza por un clima templado mediterráneo cálido, con estación seca
prolongada y calurosa, de seis o más meses y periodos rigurosos durante el invierno. Las precipitaciones
son liquidas y suceden principalmente en los meses de junio, julio y agosto. La temperatura media anual
alcanza los 19 [°C], los meses cálidos supera los 30 [°C], mientras que en epoca invernal las temperaturas
pueden bajar de los 0 [°C] [6] .

4 Centro de información de Recursos Naturales. (2021). Recursos Naturales Comuna de Maule. Sistema de Información Territorial. Chile.
5 Dirección General de Aguas. (2004). Cuenca del Río Maule - Diagnóstico y Clasificaciones de los cursos y cuerpos de agua según Objetivos

de Calidad. Ministerio de Obras Públicas. Chile.
6 Centro de información de Recursos Naturales. (2021). Recursos Naturales Comuna de Maule. Sistema de Información Territorial. Chile.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 13 de 30

**1.4** **Altura de mezcla**

La altura de mezcla depende fuertemente del calentamiento superficial, ya que éste determina el ascenso
de las masas de aire (boyancia) y, en consecuencia, la inestabilidad atmosférica que determina la altura
a la cual las emisiones se dispersan. Por esta razón, la variación de la altura de mezcla es de ciclo diario
y estacional.
A continuación, se presentan isolíneas de alturas de mezclas para cuatro períodos estacionales en tres
ciclos horarios, dentro del dominio de modelación.

Figura 2 - Distribución general de altura de mezcla (ortofotografías)

Fuente: Envirometrika, 2022.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 14 de 30

Los periodos de obtención de las isolíneas de altura de mezcla, desde el modelo de dispersión, se detallan
a continuación:

Tabla 8 - Registro de ortofotografías - Isolíneas de altura de mezcla

Gráfico 1 - Altura de mezcla y temperatura - Serie de tiempo

Fuente: Envirometrika, 2022.

Tabla 9 - Altura de mezcla - promedios por periodo estacional y horario [m]

Fuente: Envirometrika, 2022.

ANÁLISIS METEOROLÓGICO www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 15 de 30

**2** **ANÁLISIS DE INCERTIDUMBRE**

Los modelos meteorológicos corresponden a herramientas matemáticas que nos permiten representar de forma
aproximada la realidad de una condición meteorológica. Estas incorporan dentro de sus resultados,
incertidumbres, expresadas a través de las diferencias entre lo estimado por el modelo y las observaciones de
una estación meteorológica (o errores del modelo) [7] . Se evaluó la capacidad del modelo para representar la
situación atmosférica local [8] del periodo anual 2021 mediante el desarrollo de las siguientes etapas:

a) **Etapa 1 - Diagnóstico de datos meteorológicos observados:**

Distribución temporal de las variables meteorológicas de velocidad del viento [m/s], dirección del viento

[grados], temperatura [°C] y humedad relativa [%] mediante: series de tiempo y ciclos diarios.

b) **Etapa 2 - Comparación entre pronóstico y observaciones** :

 Análisis cualitativo: Comparaciones gráficas para datos meteorológicos observados y simulados a través

de los ciclos diarios.

 Análisis cuantitativo: Cálculo de las métricas de estadísticas del sesgo (BIAS), Error medio cuadrático

(RSME) y Coeficiente de correlación entre las variables meteorológicas pronosticadas y observadas.

**2.1** **Etapa 1 - Diagnóstico de datos meteorológicos observados**

Los datos meteorológicos observados corresponden a los registros obtenidos desde el Sistema de
Información Nacional de Calidad de Aire [9], en estación La Florida durante el periodo anual 2021.

Tabla 10 - Coordenada de localización estación meteorológica La Florida

|Coordenadas UTM [m]|Col2|Col3|Col4|
|---|---|---|---|
|Este|Sur|Huso|Datum|
|256.889|6.075.395|19 Sur|WGS 84|

7 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA. Santiago, Chile.
8 Ibíd.
9 Ministerio del Medio Ambiente. (2018). Sistema de Información Nacional de Calidad del Aire (SINCA). Adquirido 19 de agosto de 2022:

[https://sinca.mma.gob.cl/index.php/estacion/index/id/276](https://sinca.mma.gob.cl/index.php/estacion/index/id/276)

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 16 de 30

Figura 3 - Localización de estación meteorológica La Florida

Fuente: Envirometrika, 2022.

Los datos observados en una primera revisión fueron validados siguiendo los lineamientos definidos en la
guía “Meteorological Monitoring Guidance for Regulatory Modeling Applications” [10] . Los porcentajes de
datos meteorológicos observados válidos, calculados en función al total de horas teóricas (8.760 horas en
un año).

En una la segunda validación se consideró lo descrito en “Guía para el Uso de Modelos de Calidad del Aire
en el SEIA”, la cual señala que “Se recomienda que el porcentaje de datos válidos de las series de tiempo
sea siempre superior al 75%...” [11] . De acuerdo con lo anterior, datos provenientes de la estación
meteorológica cumplirían con lo recomendado, según se describe en la siguiente tabla:

Tabla 11 - Porcentaje datos válidos

|Variable meteorológica|% datos válidos|Cumple con recomendación SEA<br>(>75%)|
|---|---|---|
|Velocidad del viento [m/s]<br>Dirección del viento [°]<br>Temperatura [°C]<br>Humedad relativa [%]|90,81%<br>99,63%<br>99,62%<br>99,93%|<br><br><br>|

10 U.S. Environmental Protection Agency. (2000). Meteorological Monitoring Guidance for Regulatory Modeling Applications. Estados Unidos.
11 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA. Santiago, Chile.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 17 de 30

**Series de tiempo**

Temperatura, [°C]

Gráfico 2 - Serie pronóstico, temperatura [°C]

Fuente: Envirometrika, 2022.

Gráfico 3 - Serie observada, temperatura [°C]

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 18 de 30

Velocidad del viento, [m/s]

Gráfico 4 - Serie pronóstico, velocidad del viento [m/s]

Fuente: Envirometrika, 2022.

Gráfico 5 - Serie observada, velocidad del viento [m/s]

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 19 de 30

Humedad relativa, [%]

Gráfico 6 - Serie pronóstico, humedad relativa [%]

Fuente: Envirometrika, 2022.

Gráfico 7 - Serie observada, humedad relativa [%]

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 20 de 30

**Ciclos diarios**

Temperatura, [°C]

Gráfico 8 - Ciclos diarios promedios de la temperatura - serie pronóstico

Fuente: Envirometrika, 2022.

Gráfico 9 - Ciclos diarios promedios de la temperatura - serie observada

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 21 de 30

Velocidad del viento, [m/s]

Gráfico 10 - Ciclos diarios promedios de velocidad del viento - serie pronóstico

Fuente: Envirometrika, 2022.

Gráfico 11 - Ciclos diarios promedios de velocidad del viento - serie observada

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 22 de 30

Humedad relativa, [%]

Gráfico 12 - Ciclos diarios promedios de humedad relativa - serie pronóstico

Fuente: Envirometrika, 2022.

Gráfico 13 - Ciclos diarios promedios de humedad relativa - serie observada

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 23 de 30

**2.2** **Etapa 2 - Comparación entre pronóstico y observaciones**

La comparación de las observaciones (serie de datos obtenida de registros de la estación meteorológica
superficial) con las simulaciones del modelo de pronóstico (serie de datos obtenida del modelo numérico
WRF) en el punto de medición, permite evaluar la incertidumbre de los datos meteorológicos
tridimensionales generados y de los resultados del modelo de dispersión y así poder analizar una posible
sobre o subestimación [12] . Para poder determinar un grado de incertidumbre, se deben evaluar las
diferencias de lo observado versus lo modelado realizando un análisis cuantitativo y cualitativo, según se
recomienda en la guía de modelación [13] .

**Análisis cualitativo de serie de pronóstico y observada**

Temperatura, [°C]

Gráfico 14 - Ciclos diarios promedios de temperatura, serie pronóstico y observado

Fuente: Envirometrika, 2022.

Velocidad del viento, [m/s]

Gráfico 15 - Ciclos diarios promedios de velocidad del viento, serie pronóstico y observada

Fuente: Envirometrika, 2022.

12 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA. Santiago, Chile.
13 Ibíd.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 24 de 30

Humedad Relativa, [%]

Gráfico 16 - Ciclos diarios promedios de humedad relativa, serie pronóstico y observada

Fuente: Envirometrika, 2022.

Dirección del viento, [grados]

Gráfico 17 - Ciclos diarios de variación del viento, serie pronóstico

Fuente: Envirometrika, 2022.

Gráfico 18 - Ciclos diarios de variación del viento, serie observada

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 25 de 30

Gráfico 19 - Distribución anual de frecuencia de velocidad del viento serie pronóstico y observada.

WRF-MMIF, 2021 Estación La Florida, 2021

Gráfico 20 - Rosas de viento anual por periodo horario, serie pronóstico y observada

Meteorología pronóstico Meteorología observada

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 26 de 30

Gráfico 21 - Rosas de viento anual según periodo horario, serie pronóstico y observada

|Col1|Col2|Anual Nocturno|Anual AM|Anual PM|
|---|---|---|---|---|
|Pronóstico|||||
|Observado|||||

Fuente: Envirometrika, 2022.

Gráfico 22 - Rosas de viento anual por periodo estacional, serie pronóstico y observada

|Col1|Col2|Verano|Otoño|Invierno|Primavera|
|---|---|---|---|---|---|
|Pronóstico||||||
|Observado||||||

Fuente: Envirometrika, 2022.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 27 de 30

**Análisis cuantitativo de serie de pronóstico y observada**

El análisis cuantitativo se realizó en base a una metodología celda-punto, el cual comparó los
datos de la meteorología de pronóstico con los registrados por la estación superficial, de cada
dato horario. Se calcularon las métricas de estadísticas de error medio cuadrático (RSME), sesgo
(BIAS), coeficiente de correlación, índice de concordancia (IOA), entre las variables
meteorológicas pronosticadas y observadas.

Tabla 12 - Resumen de estadísticos de incertidumbre

|Estadístico|Descripción|Fórmula|Resultados|Col5|Col6|
|---|---|---|---|---|---|
|Estadístico|Descripción|Fórmula|Velocidad del<br>viento [m/s]|Temperatura<br>[°C]|Humedad<br>relativa [%]|
|RMSE|Error medio cuadrático (Root<br>mean square Error), nos indica la<br>medida de las diferencias en<br>promedio<br>entre<br>valores<br>pronosticados y observados.||0,90|3,35|22,44|
|NRMSD|Error<br>medio<br>cuadrático<br>normalizado<br>(Normalized<br>Root<br>mean square deviation) señala la<br>varianza residual entre los valores<br>pronosticados y observados.||0,13|0,09|0,27|
|NMAE|Error medio absoluto normalizado,<br>toma en cuenta el peso del error<br>respecto al valor de la variable<br>medida,<br>normaliza<br>el<br>error<br>absoluto.||0,10|0,07|0,21|
|BIAS|Sesgo, proporciona información<br>sobre la tendencia del modelo a<br>sobrestimar o subestimar una<br>variable.||0,24|-1,33|16,39|
|Coeficiente<br>de<br>correlación<br>de Pearson|Un índice que mide el grado de<br>relación de dos variables siempre<br>y <br>cuando<br>ambas<br>sean<br>cuantitativas.||0,62|0,93|0,71|
|IOA|El IOA (Index Of Agreement)<br>acuerdo es una medida de la<br>coincidencia entre la salida de<br>cada predicción de la media<br>observada y la salida de cada<br>observación<br>de<br>la<br>media<br>observada.||0,76|1,00|1,00|

Los índices RMSE, NRMSD y NMAE, arrojaron que las variables de velocidad del viento,
temperatura y humedad relativa pronosticadas presentaron una diferencia de 0,90 [m/s], 3,35

[°C] y 22,44 [%], respecto a lo observado para el periodo anual.

Del Sesgo (BIAS) se interpreta que la meteorología del modelo de pronóstico WRF-MMIF,
sobrestima en cierto grado las variables de velocidad y humedad relativa. Mientras que la
temperatura presenta una leve subestimación al evaluar el periodo anual.

La correlación arrojó asociación positiva para las variables analizadas, siendo la temperatura la de
mayor ajuste [14] [/] [15] .

14 Correlación positiva débil=+0,10, Correlación positiva media=+0,50, Correlación positiva considerable=+0,75.
15 Castejón Sandoval, O. (2011). Diseño y Análisis de Experimentos con Statistix. Universidad Rafael Urdaneta, Fondo editorial biblioteca.

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 28 de 30

El IOA exhibió un nivel de 0,76 categorizado como acuerdo para velocidad del viento. La variable
de temperatura y humedad relativa arrojó acuerdo perfecto con un valor de 1. Todas las variables
se encuentran dentro de los rangos aceptables según puntos de referencias Emery et al. (2001).

ANÁLISIS DE INCERTIDUMBRE www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 29 de 30

**3** **ANÁLISIS DE RESULTADOS**

Del análisis meteorológico, se desprende que:

 En base al análisis del comportamiento anual de los campos de vientos en el área de estudio, bajo las

condiciones meteorológicas locales se favorecería la dispersión de las emisiones hacia el NNE de la
instalación.

 Respecto a las condiciones más desfavorables de dispersión, estas se presentarían en horario nocturno,

debido a la mayor frecuencia de vientos de baja intensidad y condiciones de calma, junto al bajo desarrollo
de la capa de mezcla, lo cual limitaría la dispersión vertical de las emisiones.

Del análisis de incertidumbre, se concluye que:

 Del levantamiento meteorológico realizado, la estación meteorológica La Florida, cumplió con los requisitos,

requerido por el SEA [16], para la realización del análisis.

 Del análisis cuantitativo y cualitativo entre las series, se desprende que la serie de pronóstico presentaría

un comportamiento coherente a lo registrado por estación La Florida para las variables relevantes. Por lo
tanto, la base meteorológica proveniente del modelo WRF sería representativa de los campos de vientos a
nivel local.

 Los resultados indicarían que lo pronosticado reproduciría condiciones meteorológicas horarias y mensuales,

con una mayor frecuencia de vientos de mediana intensidad. Respecto al ciclo diario, si bien reproduce la
variabilidad observada, esta presentaría un cierto grado de subestimación en las condiciones ambientales
durante el periodo nocturno.

16 Servicio de Evaluación Ambiental. (2012). Guía para el Uso de Modelos de Calidad del Aire en el SEIA. Santiago, Chile.

ANÁLISIS DE RESULTADOS www.envirometrika.com

P6764 - Análisis de Incertidumbre Septiembre 2022
F4F SpA - Planta Talca Página 30 de 30

**4** **BIBLIOGRAFÍA**

 Castejón Sandoval, O. (2011). Diseño y Análisis de Experimentos con Statistix. Universidad Rafael Urdaneta,


Centro de información de Recursos Naturales. (2021). Recursos Naturales Comuna de Maule. Sistema de

Información Territorial. Chile.

 Dirección General de Aguas. (2004). Cuenca del Río Maule - Diagnostico y Clasificaciones de los cursos y

cuerpos de agua según Objetivos de Calidad. Ministerio de Obras Públicas. Chile.

 Ministerio del Medio Ambiente. (2018). Sistema de Información Nacional de Calidad del Aire (SINCA).

[Adquirido 19 de Agosto de 2022: https://sinca.mma.gob.cl/index.php/estacion/index/id/276](https://sinca.mma.gob.cl/index.php/estacion/index/id/276)

 Organización Meteorológica Mundial. (2010). Manual de claves, Claves internacional, Volumen I.1 Parte A

- Claves alfanuméricas - Escala Beaufort de Viento. OMM-N°306. OMM. Suiza.

 Servicio de Evaluación Ambiental. (2012). Guía para el uso de modelos de calidad del aire en el SEIA.

Santiago, Chile.

 U.S. Environmental Protection Agency. (2000). Meteorological Monitoring Guidance for Regulatory Modeling

Applications. Estados Unidos.

BIBLIOGRAFÍA www.envirometrika.com

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: - Coordenadas representativas de Planta Talca**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| X: Este | Y: Sur | Huso | Datum |
| 259.549 | 6.072.856 | 19 Sur | WGS-84 |

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

| Col1 | Rosa de viento | Col3 | Distribución de velocidad del viento | Col5 | Características |
| --- | --- | --- | --- | --- | --- |
| Anual Nocturno |  |  | 5,09<br>12,88<br>34,40<br>25,32<br>15,26<br>5,13<br>1,37<br>0,27<br>0,23<br>0,04<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** |  | El viento predominó desde la componente SSO,<br>con un 32% de la frecuencia.<br>La velocidad varió de brisa muy débil 1 a<br>moderada, observándose brisas frescas, en<br>menor frecuencia.<br>La distribución de frecuencia de velocidad de<br>viento presentó una asimetría positiva.<br> <br>Promedio velocidad del viento: 2,09 [m/s].<br> <br>Frecuencia de vientos calmos: 5,09%. |
| Anual AM |  |  | <br>4,83<br>11,99<br>30,03<br>23,36<br>15,45<br>7,12<br>3,80<br>1,95<br>0,68<br>0,79<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | <br>4,83<br>11,99<br>30,03<br>23,36<br>15,45<br>7,12<br>3,80<br>1,95<br>0,68<br>0,79<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | <br>Las masas de viento provinieron en mayor<br>frecuencia desde el rango S-SSO (50%).<br>La intensidad del viento osciló de brisa muy<br>débil<br>2 a<br>moderada.<br>Adicionalmente,<br>se<br>registraron brisas frescas.<br>La curva de distribución tuvo una tendencia<br>asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,42 [m/s].<br> <br>Frecuencia de vientos calmos: 4,83%. |
| Anual PM |  |  | <br>3,04<br>8,74<br>28,89<br>27,18<br>18,81<br>8,04<br>2,89<br>1,46<br>0,58<br>0,37<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | <br>3,04<br>8,74<br>28,89<br>27,18<br>18,81<br>8,04<br>2,89<br>1,46<br>0,58<br>0,37<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de viento provinieron con mayor<br>frecuencia desde el SSO (31%). En general, la<br>velocidad fluctuó de brisa muy débil<br>3 a<br>moderada.<br>Respecto a la distribución de la velocidad, ésta<br>tuvo un sesgo positivo.<br> <br>Promedio velocidad del viento: 2,51 [m/s].<br> <br>Frecuencia de vientos calmos: 3,04%. |

**Tabla 4: - Rosas y campos de viento pronóstico estacional - Verano**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Col6 | Col7 | Características |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Verano Nocturno |  |  |  |  | 7,78<br>17,14<br>34,92<br>22,38<br>11,43<br>5,56<br>0,79<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** |  | El viento predominó desde la componente SSO,<br>con una frecuencia del 34%.<br>En general, la intensidad del viento varió de brisa<br>muy débil a moderada y la curva de distribución<br>tuvo una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 1,87 [m/s].<br> <br>Frecuencia de vientos calmos: 7,78%. |
| Verano AM |  |  |  |  |  |  | Las masas de aire provinieron con mayor<br>frecuencia desde el rango S-SO (53%). La<br>velocidad varió de brisa muy débil a moderada.<br>La curva de distribución marcó una tendencia<br>asimétrica positiva.<br> <br>Promedio velocidad del viento: 1,95 [m/s].<br> <br>Frecuencia de vientos calmos: 7,64%. |
| Verano AM |  |  |  |  | 7,64<br>17,50<br>33,61<br>19,31<br>13,61<br>6,81<br>1,53<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | 7,64<br>17,50<br>33,61<br>19,31<br>13,61<br>6,81<br>1,53<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | 7,64<br>17,50<br>33,61<br>19,31<br>13,61<br>6,81<br>1,53<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** |
| Verano PM |  |  |  |  | 1,36<br>5,43<br>25,80<br>33,09<br>24,94<br>7,41<br>1,85<br>0,00<br>0,00<br>0,12<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** |  | Los campos de viento predominaron desde el<br>3ocuadrante, con un 82% de la frecuencia. La<br>intensidad fluctuó de brisa débil a moderada. La<br>curva de distribución arrogó un comportamiento<br>leptocúrtico agrupándose mayormente en el<br>rango 2-3[m/s]. <br> <br>Promedio velocidad del viento: 2,55 [m/s].<br> <br>Frecuencia de vientos calmos: 1,36%. |

**Tabla 5: - Rosas y campos de viento pronóstico estacional - Otoño**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Col6 | Col7 | Características |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Otoño Nocturno |  |  |  |  | 5,28<br>14,75<br>33,85<br>24,07<br>17,08<br>4,19<br>0,78<br>0,00<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** |  | Los campos de viento provinieron con mayor<br>frecuencia desde la componente SSO (31%) y<br>en menor medida desde SO (16%). La<br>intensidad del viento osciló de brisa muy débil<br>a moderada. La curva de distribución presentó<br>una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,01 [m/s].<br> <br>Frecuencia de vientos calmos: 5,28%. |
| Otoño AM |  |  |  | <br> <br>4,76<br>12,23<br>28,94<br>26,22<br>16,98<br>6,93<br>2,45<br>0,82<br>0,41<br>0,27<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | <br> <br>4,76<br>12,23<br>28,94<br>26,22<br>16,98<br>6,93<br>2,45<br>0,82<br>0,41<br>0,27<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | <br> <br>4,76<br>12,23<br>28,94<br>26,22<br>16,98<br>6,93<br>2,45<br>0,82<br>0,41<br>0,27<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | El viento predominó con mayor frecuencia<br>desde la componente SSO (32%), y en menor<br>medida, desde la componente S (18%). La<br>intensidad del viento fluctuó de brisa muy débil<br>a débil.<br>Respecto a la distribución, ésta tuvo una<br>tendencia asimétrica positiva.<br> <br>Promedio velocidad del viento: 2,30 [m/s].<br> <br>Frecuencia de vientos calmos: 4,76%. |
| Otoño PM |  |  |  | <br>4,95<br>11,11<br>35,63<br>29,23<br>13,77<br>4,35<br>0,72<br>0,24<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | <br>4,95<br>11,11<br>35,63<br>29,23<br>13,77<br>4,35<br>0,72<br>0,24<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | <br>4,95<br>11,11<br>35,63<br>29,23<br>13,77<br>4,35<br>0,72<br>0,24<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provienen en mayor<br>frecuencia desde la componente SSO (30%) y<br>en menor medida desde las componentes S y<br>SO (14%). En general, la velocidad varió de<br>brisa muy débil a moderada.<br>La curva de distribución tiende a una asimétrica<br>positiva, agrupándose mayormente en el rango<br>de 1-2 [m/s]. <br> <br>Promedio velocidad del viento: 2,05 [m/s].<br> <br>Frecuencia de vientos calmos: 4,95%. |

**Tabla 6: - Rosas y campos de viento pronóstico estacional - Invierno**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Invierno Nocturno |  |  |  | <br>3,73<br>12,27<br>34,63<br>23,29<br>15,53<br>5,90<br>2,80<br>0,78<br>0,93<br>0,16<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario nocturno los vientos<br>provinieron desde las componentes SSO (22%)<br>y NE (11%). En general, la intensidad osciló de<br>brisa muy débil a moderado, generando una<br>curva de distribución asimétrica positiva.<br> <br>Promedio velocidad del viento: 2,27 [m/s].<br> <br>Frecuencia de vientos calmos: 3,73%. |
| Invierno AM |  |  |  | <br> <br>3,67<br>11,55<br>30,43<br>22,96<br>13,18<br>5,43<br>5,71<br>3,40<br>1,09<br>2,58<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron desde las<br>componentes SSO (25%), S (19%). La<br>velocidad fluctuó de brisa muy débil a<br>moderada, donde la distribución tuvo una curva<br>de<br>distribución<br>asimétrica<br>positiva,<br>agrupándose mayormente en el rango de 1-4<br>[m/s]. <br> <br>Promedio velocidad del viento: 2,66 [m/s].<br> <br>Frecuencia de vientos calmos: 3,67%. |
| Invierno PM |  |  |  | <br>5,07<br>13,16<br>30,68<br>20,77<br>14,01<br>7,37<br>3,86<br>2,90<br>0,97<br>1,21<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de vientos provinieron con mayor<br>frecuencia desde SSO (23%), y en menor<br>medida desde s (9%). En general, la intensidad<br>varió de brisa muy débil a moderada y la<br>distribución se presentó con sesgo positivo.<br> <br>Promedio velocidad del viento: 2,47 [m/s].<br> <br>Frecuencia de vientos calmos: 5,07%. |

**Tabla 7: - Rosas y campos de viento pronóstico estacional - Primavera**

| Col1 | Rosa de viento | Col3 | Campos de viento | Distribución de velocidad del viento | Características |
| --- | --- | --- | --- | --- | --- |
| Primavera Nocturno |  |  |  | <br>3,61<br>7,38<br>34,22<br>31,55<br>16,95<br>4,87<br>1,10<br>0,31<br>0,00<br>0,00<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Los campos de viento predominaron desde la<br>componente SSO, con una frecuencia del 41%.<br>En general, los vientos fluctuaron de brisa muy<br>débil a moderada, donde la distribución tuvo<br>una tendencia asimétrica positiva. <br> <br>Promedio velocidad del viento: 2,21 [m/s].<br> <br>Frecuencia de vientos calmos: 3,61%. |
| Primavera AM |  |  |  | <br>3,30<br>6,73<br>27,20<br>24,86<br>17,99<br>9,34<br>5,49<br>3,57<br>1,24<br>0,27<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Las masas de aire provinieron desde las<br>componentes: SSO (41%), S (20%).<br>La velocidad de los vientos osciló de brisa muy<br>débil a moderada; en la distribución, estas<br>exhibieron curva con tendencia asimétrica<br>positiva. <br> <br>Promedio velocidad del viento: 2,76 [m/s].<br> <br>Frecuencia de vientos calmos: 3,30%. |
| Primavera PM |  | <br> |  | <br>0,73<br>5,13<br>23,32<br>25,76<br>22,71<br>13,06<br>5,13<br>2,69<br>1,34<br>0,12<br>0<br>5<br>10<br>15<br>20<br>25<br>30<br>35<br>40<br>Calmos<br>0,5 - 1<br>1 - 2<br>2 - 3<br>3 - 4<br>4 - 5<br>5 - 6<br>6 - 7<br>7 - 8<br>>= 8<br>**%**<br>**[m/s]** | Durante el horario PM, los vientos provinieron<br>en mayor frecuencia desde la componente SSO<br>(42%) y en menor medida desde SO (14%).<br>La velocidad varió de brisa muy débil a<br>moderada.<br>Respecto a la distribución de intensidad de<br>vientos, esta presentó un comportamiento<br>mesocúrtico.<br> <br>Promedio velocidad del viento: 2,98 [m/s].<br> <br>Frecuencia de vientos calmos: 0,73%. |

**Tabla 10: - Coordenada de localización estación meteorológica La Florida**

| Coordenadas UTM [m] | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Este | Sur | Huso | Datum |
| 256.889 | 6.075.395 | 19 Sur | WGS 84 |

**Tabla 11: - Porcentaje datos válidos**

| Variable meteorológica | % datos válidos | Cumple con recomendación SEA<br>(>75%) |
| --- | --- | --- |
| Velocidad del viento [m/s]<br>Dirección del viento [°]<br>Temperatura [°C]<br>Humedad relativa [%] | 90,81%<br>99,63%<br>99,62%<br>99,93% | <br><br><br> |

**Tabla 12: - Resumen de estadísticos de incertidumbre**

| Estadístico | Descripción | Fórmula | Resultados | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| Estadístico | Descripción | Fórmula | Velocidad del<br>viento [m/s] | Temperatura<br>[°C] | Humedad<br>relativa [%] |
| RMSE | Error medio cuadrático (Root<br>mean square Error), nos indica la<br>medida de las diferencias en<br>promedio<br>entre<br>valores<br>pronosticados y observados. |  | 0,90 | 3,35 | 22,44 |
| NRMSD | Error<br>medio<br>cuadrático<br>normalizado<br>(Normalized<br>Root<br>mean square deviation) señala la<br>varianza residual entre los valores<br>pronosticados y observados. |  | 0,13 | 0,09 | 0,27 |
| NMAE | Error medio absoluto normalizado,<br>toma en cuenta el peso del error<br>respecto al valor de la variable<br>medida,<br>normaliza<br>el<br>error<br>absoluto. |  | 0,10 | 0,07 | 0,21 |
| BIAS | Sesgo, proporciona información<br>sobre la tendencia del modelo a<br>sobrestimar o subestimar una<br>variable. |  | 0,24 | -1,33 | 16,39 |
| Coeficiente<br>de<br>correlación<br>de Pearson | Un índice que mide el grado de<br>relación de dos variables siempre<br>y <br>cuando<br>ambas<br>sean<br>cuantitativas. |  | 0,62 | 0,93 | 0,71 |
| IOA | El IOA (Index Of Agreement)<br>acuerdo es una medida de la<br>coincidencia entre la salida de<br>cada predicción de la media<br>observada y la salida de cada<br>observación<br>de<br>la<br>media<br>observada. |  | 0,76 | 1,00 | 1,00 |
