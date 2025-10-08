---
title: 1 INTRODUCCIÓN
author: Claudio Seguel
date: D:20171026112550-03'00'
language: es
type: report
pages: 86
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - _ANEXO I_
  - _ANEXO II_
-->

**INFORME DE RESULTADOS**

Titular:

Preparado por:

###### _INFORME DE RESULTADOS_

#### _INFORME DE RESULTADOS ATM 067-17_ _ATM 067-17_

###### _MODELACIÓN DE LA DISPERSIÓN DE LAS EMISIONES_ _MODELACIÓN DE LA DISPERSIÓN DE LAS EMISIONES ATMOSFÉRICAS PROVENIENTES DEL PROYECTO_ _ATMOSFÉRICAS PROVENIENTES DEL PROYECTO FORTUNA_ _FORTUNA_

Preparado para:

|Versión del Documento|Col2|Col3|Col4|Versión A-1|Col6|
|---|---|---|---|---|---|
|**_Responsable Elaboración_**|**_Responsable Elaboración_**|**_Responsable Revisión_**|**_Responsable Revisión_**|**_Responsable Aprobación_**|**_Responsable Aprobación_**|
|Nombre:|Nicolás Escárate R.|Nombre:|Evelyn Antiñir H.|Nombre:|Claudio Seguel O.|
|Cargo:|Ingeniero de Proyecto<br>Modelación Ambiental|Cargo|Jefe de Área<br>Modelación Ambiental|Cargo:|Gerente General|
|Fecha:||Fecha:||Fecha:||
|Firma:||Firma:||Firma:||

**Octubre, 2017**

**Arzobispo Larraín Gandarillas 90, Providencia, Santiago de Chile - Fono 56-2-23616600**

**www.algoritmospa.com**

**ÍNDICE DE CONTENIDOS**

1 Introducción ................................................................................ 1

2 Marco Legal ................................................................................. 4

3 Línea de Base .............................................................................. 5

4 Meteorología Imperante en la Zona de Estudio ................................. 7

4.1 Series de Tiempo .......................................................................... 8

4.2 Rosa de Vientos ........................................................................... 9

4.3 Ciclo Diario ................................................................................ 12

4.4 Ciclo estacional .......................................................................... 13

5 Estimación de Emisiones del Proyecto ........................................... 14

5.1 Actividades Emisoras .................................................................. 14

5.2 Método de Cálculo ...................................................................... 14

5.3 Factores de Emisión del Proyecto .................................................. 16

5.3.1 Peso promedio ........................................................................... 20

5.3.1.1 Peso promedio etapa de Operación. .............................................. 21

5.4 Nivel de actividad Etapa de Operación ........................................... 23

5.4.1 Tronaduras y Perforaciones .......................................................... 23

5.4.2 Carga y Descarga de Material....................................................... 23

5.4.3 Chancadores y Harneros ............................................................. 27

5.4.4 Tránsito de Vehículos por tipo de carpeta. ..................................... 27

5.4.5 Motor de Vehículos ..................................................................... 33

5.4.6 Motor de Maquinarias .................................................................. 30

5.4.7 Medidas de Abatimiento de Polvo ................................................. 31

5.5 Tasas de Emisión ........................................................................ 31

6 Descripción del Modelo Utilizado ................................................... 33

6.1 Modelo de Dispersión Atmosférica ................................................ 33

6.1.1 Base Teórica .............................................................................. 33

6.1.2 Sistema de Modelación WRF - CALPUFF ......................................... 33

6.2 Variables de Entrada al Sistema de Modelación .............................. 35

7 Modelación ................................................................................ 38

8 Resultados de la Modelación ........................................................ 38

8.1 Campos de Viento ...................................................................... 38

8.2 Aportes Obtenidos en la Modelación .............................................. 43

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

8.3 Análisis respecto de los valores establecidos en la Normativa

Ambiental ............................................................................ 44

8.4 Ubicación Puntos de Máximo Impacto ........................................... 46

8.5 Mapas de Isoconcentraciones ....................................................... 48

9 Análisis sinérgicos con otros proyectos respecto a los valores

establecidos en la Normativa Ambiental ................................... 62

10 Conclusiones .............................................................................. 64

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**ÍNDICE DE TABLAS**

Tabla N° 1 Coordenadas Vértices del Área de Modelación ................................. 1

Tabla N° 2 Normas de Calidad del Aire Consideradas en el Estudio .................... 4

Tabla N° 3 Coordenadas Estaciones de Monitoreo ........................................... 5

Tabla N° 4 Línea de Base de Calidad del Aire, Estación Chamonate (g/m3N) .... 5

Tabla N° 5 Línea de Base de Calidad del Aire, Estación Copiapó SIVICA ............. 6

Tabla N° 6 Estadísticas de Datos Meteorológicos Modelados ............................. 8

Tabla N° 7 Actividades Emisoras de Material Particulado y Gases .................... 14

Tabla N° 8 Factores de Emisión Considerados en el Cálculo Etapa de

Operación ................................................................................ 16

Tabla N° 9 Valores Considerados en los Factores de Emisión Etapa de

Operación ................................................................................ 18

Tabla N° 10 Peso Promedio Vehículos (ton) en Caminos no Pavimentados

“Etapa de Operación” ................................................................ 21

Tabla N° 11 Peso Promedio Vehículos (ton) en Caminos Pavimentados “Etapa

de Operación” .......................................................................... 22

Tabla N° 12 Nivel de Actividad para Tronaduras y Perforaciones Etapa de

Operación ................................................................................ 23

Tabla N° 13 Carga de Material (ton/año) Etapa de Operación ......................... 23

Tabla N° 14 Descarga de Material (ton/año) Etapa de Operación .................... 24

Tabla N° 15 Cantidad de Material a procesar en chancadores (ton/año) Etapa

de Operación ........................................................................... 27

Tabla N° 16 Cantidad de Material a procesar en harneros (ton/año) Etapa de

Operación ................................................................................ 27

Tabla N° 17 Cálculo del Nivel de Actividad para Tránsito de Vehículos por

Caminos no Pavimentados (veh-km/año) Etapa de Operación ........ 28

Tabla N° 18 Cálculo del Nivel de Actividad para Tránsito de Vehículos por

Caminos Pavimentados (veh-km/año) Etapa de Operación ............. 29

Tabla N° 19 Cálculo del Nivel de Actividad para Motor de Maquinarias

(hr/año) Etapa de Operación ...................................................... 30

Tabla N° 20 Medidas de Control que se aplicaran en los Caminos en la Etapa

de Operación. .......................................................................... 31

Tabla N° 22 Tasas de Emisión Etapa de Operación (ton/año) .......................... 32

Tabla N° 23 Características del Uso de Suelo ................................................ 35

Tabla N° 24 Localización Puntos Discretos .................................................... 37

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

Tabla N° 25 Aportes del Proyecto, Etapa de Operación. ................................. 43

Tabla N° 26 Análisis Normativo Estación Chamonate, Etapa de Operación. ....... 45

Tabla N° 27 Análisis Normativo Estación Copiapó SIVICA, Etapa de

Operación. ............................................................................... 45

Tabla N° 28 Valores y coordenadas de Localización de Puntos de Máximo

Impacto .................................................................................. 46

Tabla N° 29 Aportes en MP10 del Proyecto Bellavista .................................... 62

Tabla N° 30 Aportes Sinérgicos en MP10 con Proyecto Mina Bellavista, en

Estación Chamonate ................................................................. 63

Tabla N° 31 Aportes Sinérgicos en MP10 con Proyecto Mina Bellavista, en

Estación Copiapó SIVICA ........................................................... 63

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**ÍNDICE DE FIGURAS**

Figura N° 1 Área de Modelación del Proyecto .................................................. 3

Figura N° 2 Serie temporal horaria velocidad del viento - Estación WRF

Chamonate Periodo 01 Enero 2015 - 31 Diciembre 2015 ................. 8

Figura N° 3 Serie temporal horaria dirección del viento - Estación WRF

Chamonate Periodo 01 Enero 2015 - 31 Diciembre 2015 ................. 9

Figura N° 4 Rosas de Viento Ciclo Completo - WRF Estación Chamonate

Periodo 01 Enero 2015 - 31 Diciembre 2015 ................................ 10

Figura N° 5 Variabilidad temporal del viento - WRF Estación Chamonate ......... 11

Figura N° 6 Ciclo diario de la velocidad del viento -WRF Estación Chamonate ... 12

Figura N° 7 Ciclo estacional del viento - Estación Chamonate Periodo 01

Enero 2015 - 31 Diciembre 2015................................................ 13

Figura N° 8 Uso de Suelo ........................................................................... 36

Figura N° 9 Curvas de Nivel del Área de Modelación ...................................... 37

Figura N° 10 Campos de Viento a las 06:00 hrs. ........................................... 39

Figura N° 11 Campos de Viento a las 12:00 hrs. ........................................... 40

Figura N° 12 Campos de Viento a las 18:00 hrs. ........................................... 41

Figura N° 13 Campos de Viento a las 00:00 hrs. ........................................... 42

Figura N° 14 Ubicación Puntos de Máximo Impacto (PMI) .............................. 47

Figura N° 15 Promedio del periodo MP10, Etapa de Operación ........................ 48

Figura N° 16 Percentil 98 Diario de MP10, Etapa de Operación ....................... 49

Figura N° 17 Promedio del Periodo de MP2,5, Etapa de Operación .................. 50

Figura N° 18 Percentil 98 Diario de MP2,5, Etapa de Operación ...................... 51

Figura N° 19 Promedio del Periodo de MPS, Etapa de Operación ..................... 52

Figura N° 20 Promedio Mensual de MPS, Etapa de Operación ......................... 53

Figura N° 21 Promedio del Periodo de SO2, Etapa de Operación ..................... 54

Figura N° 22 Percentil 99 Diario de SO2, Etapa de Operación ......................... 55

Figura N° 23 Percentil 99,7 Diario de SO2, Etapa de Operación ...................... 56

Figura N° 24 Percentil 99,73 Horario de SO2, Etapa de Operación .................. 57

Figura N° 25 Promedio del Periodo de NO2, Etapa de Operación ..................... 58

Figura N° 26 Percentil 99 Horario NO2, Etapa de Operación ........................... 59

Figura N° 27 Percentil 99 8 Horas de CO, Etapa de Operación ........................ 60

Figura N° 28 Percentil 99 Horario de CO, Etapa de Operación ......................... 61

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 1 Introducción

El presente documento da cuenta de los resultados obtenidos al modelar la
dispersión atmosférica de las concentraciones de material particulado respirable
(MP 10 y MP 2,5 ), material particulado sedimentable (MPS), dióxido de azufre (SO 2 ),
óxidos de nitrógeno (NO X ) y monóxido de carbono (CO), provenientes de la etapa
de operación del proyecto minero “Fortuna” (en adelante, el Proyecto) el cual se
encuentra ubicado en la comuna de Copiapó, Provincia de Copiapó, Región de
Atacama.

El área de modelación corresponde a una grilla de 50 km x 37 km, con un
espaciamiento de 1 km., en cuyo interior se encuentra ubicado el sitio de
emplazamiento del Proyecto y puntos de interés. La Figura No 1 presenta el área
de modelación.

La Tabla N° 1 muestra las coordenadas de los vértices del área de modelación.

_**Tabla N° 1**_
_**Coordenadas Vértices del Área de Modelación**_ _**[a]**_

|Vértice|Este (m)|Norte (m)|
|---|---|---|
|Noreste|375.864|6.990.131|
|Noroeste|325.774|6.989.573|
|Suroeste|326.198|6.951.703|
|Sureste|376.288|6.952.267|

Fuente: Algoritmos 2017.

Los aportes de concentraciones de material particulado y gases asociados al
Proyecto, fueron obtenidos en base a los requerimientos de la “Guía para el Uso
de Modelos de Calidad del Aire en el SEIA, 2012” Servicio de Evaluación
Ambiental a través la aplicación del sistema de modelación atmosférica “WRFCALPUFF” y del “Informe Final servicio de recopilación de factores de emisión al
aire para el Servicio de Evaluación Ambiental”, ambos procedimientos definidos
por la agencia EPA como sistema de referencia para modelar la dispersión de
contaminantes provenientes de centros industriales ubicados en terreno
complejo.

La meteorología utilizada en la modelación, correspondió a la obtenida por medio
del modelo meteorológico de pronóstico Weather Research and Forecasting Model
(WRF), la cual será utilizada como entrada para el modelo de dispersión
CALPUFF. Dicha información es referente al entorno del proyecto y corresponde al
periodo comprendido entre el 1 de Enero 2015 hasta el 31 diciembre 2015.

a Coordenadas registradas según Datum WGS-84

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**1**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

Para la estimación de emisiones, se utilizaron los factores de emisión definidos en
el documento “AP 42, Fifth Edition, Compilation of Air Pollutant Emission Factors,
Volume 1: Stationary Point and Area Sources, United States - Environmental
Protection Agency”, en la “Guía para la Estimación de Emisiones Atmosféricas de
Proyectos Inmobiliarios para la Región Metropolitana, Enero 2012” y en el
“Informe Final Servicio de recopilación y sistematización de factores de emisión al
aire para el Servicio de Evaluación Ambiental del año 2015.”

Cabe señalar, que los factores de emisión establecidos en la Guía elaborada por
la SEREMI de Medio Ambiente, son los mismos factores definidos por la EPA, pero
se encuentran adaptados al sistema de unidades utilizado a nivel nacional.
Además, define valores por defecto para las situaciones en las cuales no se
cuentan con mediciones (contenido de finos, porcentajes de humedad, etc.).

En la Figura N° 1 se presenta el área de modelación, en la cual se encuentran los
principales puntos de interés evaluados en ella.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**2**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 1**_
_**Área de Modelación del Proyecto**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**3**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 2 Marco Legal

Para evaluar los impactos del proyecto respecto de la normativa ambiental, se
consideraron las normas primarias y secundarias de calidad del aire definidas en
la legislación chilena.

La Tabla N° 2 presenta los valores límites de referencia para el análisis del
presente documento.

_**Tabla N° 2**_

_**Normas de Calidad del Aire Consideradas en el Estudio**_

|Parámetro|Tipo de<br>Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|MPS(*)|Secundaria|Promedio del periodo|100 mg/ m2-día|D.S. N°04/92 MINAGRI|
|MPS(*)|Secundaria|Promedio mensual|150 mg/m2-día|D.S. N°04/92 MINAGRI|
|MP10|Primaria|Promedio del periodo|50g/m3N|D.S. N°45/02 MINSEGPRES|
|MP10|Primaria|Percentil 98 Diario|150g/m3N|D.S. N°59/98 MINSEGPRES|
|MP2,5|Primaria|Promedio del periodo|20g/m3N|D.S. N°12/11 MMA|
|MP2,5|Primaria|Percentil 98 Diario|50g/m3N|D.S. N°12/11 MMA|
|SO2|Primaria|Promedio del periodo|80g/m3N|D.S. N°113/02 MINSEGPRES|
|SO2|Primaria|Percentil 99 Diario|250g/m3N|D.S. N°113/02 MINSEGPRES|
|SO2|Secundaria|Promedio del periodo|80g/m3N|D.S. N°22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 Diario|365g/m3N|D.S. N°22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,73 Horario|1.000g/m3N|D.S. N°22/10 MINSEGPRES|
|NO2|Primaria|Promedio del periodo|100g/m3N|D.S. N°114/02 MINSEGPRES|
|NO2|Primaria|Percentil 99 Horario|400g/m3N|D.S. N°114/02 MINSEGPRES|
|CO|Primaria|Percentil 99 8 hrs.|10.000g/m3N|D.S. N°115/02 MINSEGPRES|
|CO|Primaria|Percentil 99 Horario|30.000g/m3N|D.S. N°115/02 MINSEGPRES|

(*)Norma de referencia de Huasco (D.S. 04/92 MINAGRI).
Fuente: Biblioteca del Congreso Nacional de Chile.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**4**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 3 Línea de Base

Para caracterizar la línea de base de calidad del aire imperante en el área de
influencia del Proyecto, se consideraron los datos monitoreados por dos
estaciones de calidad del aire, Chamonate y Copiapó SIVICA. Cabe destacar que
ambas estaciones monitorean MP 10 y MP 2,5 .

En la Tabla N° 3 se presentan las estaciones consideradas en el análisis de Línea
de Base.

_**Tabla N° 3**_

_**Coordenadas Estaciones de Monitoreo**_

|Estación de<br>Monitoreo|Parámetro|Coordenadas UTM|Col4|Periodo de Monitoreo|
|---|---|---|---|---|
|**_Estación de_**<br>**_Monitoreo_**|**_Parámetro_**|**_Este_**|**_Norte_**|**_Norte_**|
|Chamonate|MP10<br>MP2,5|360.196|6.980.081|1 de Agosto de 2016 a 31 de<br>Diciembre de 2016|
|Copiapó SIVICA|Copiapó SIVICA|369.133|6.971.887|1 de Enero de 2016 a 31 de<br>Diciembre de 2016|

Fuente: Algoritmos, 2017.

La Tabla N° 4 presenta los resultados de línea de base de calidad del aire
obtenidos a partir de la información medida en la estación de monitoreo
Chamonate.

_**Tabla N° 4**_
_**Línea de Base de Calidad del Aire, Estación Chamonate (**_  _**g/m**_ _**[3]**_ _**N)**_

|Contaminante|Tipo de Norma|Estadístico|Valor<br>(ug/m3N)|Norma|% Norma|
|---|---|---|---|---|---|
|MP10|Primaria|Promedio del periodo|37|50|74%|
|MP10|Primaria|Percentil 98 Diario|82|150|55%|
|MP2,5|Primaria|Promedio del periodo|9|20|45%|
|MP2,5|Primaria|Percentil 98 Diario|18|50|36%|

Fuente: Algoritmos, 2017.

De la tabla anterior, se desprende que las concentraciones de material
particulado registradas en estación Chamonate, no sobrepasan los valores límites
establecidos en la normativa ambiental vigente y tampoco alcanzan el estado de
latencia en ninguno de los contaminantes allí monitoreados.

La Tabla N° 5 presenta los resultados de línea de base de calidad del aire
obtenidos a partir de la información medida en la estación de monitoreo Copiapó
SIVICA de los periodos antes indicados en la Tabla N°4.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**5**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

Se reitera que esta estación solo monitorea MP 10 y MP 2,5, por lo que solo se puede
caracterizar la línea base en relación a estos contaminantes.

_**Tabla N° 5**_
_**Línea de Base de Calidad del Aire, Estación Copiapó SIVICA**_

|Contaminante|Tipo de<br>Norma|Estadístico|Valor<br>(ug/m3N)|Norma<br>(ug/m3N)|% de la<br>Norma<br>(*)|
|---|---|---|---|---|---|
|MP10|Primaria|Promedio del periodo|49|50|98%|
|MP10|Primaria|Percentil 98 Diario|107|150|71%|
|MP2,5|Primaria|Promedio del periodo|14|20|70%|
|MP2,5|Primaria|Percentil 98 Diario|30|50|60%|

Fuente: Algoritmos 2017.

De la Tabla anterior, se desprende que las concentraciones de material
particulado MP 10 promedio del período en la estación Copiapó SIVICA, alcanzan
un 98% de los valores límites establecidos en la normativa ambiental vigente. En
cuanto al percentil 98 promedio diario éste alcanza un máximo de 71% de los
valores normados. En el caso del MP 2,5 el promedio del periodo llega al 70% de la
norma y el percentil 98 diario alcanza un 60% del límite de la norma.

Se aprecia que todos los estadísticos se encuentran bajo el límite establecido por
la normativa primaria de calidad del aire y que solo el promedio del período para
MP 10 alcanza el estado de latencia

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**6**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 4 Meteorología Imperante en la Zona de Estudio

Las variables meteorológicas de mayor incidencia en la dispersión de las
emisiones atmosféricas generadas por el Proyecto, fueron obtenidas por medio
del modelo meteorológico de pronóstico Weather Research and Forecasting Model
(WRF).

Este modelo es recomendado por la “Guía para el uso de modelos de calidad del
aire en el SEIA”, para la generación de datos meteorológicos, ya que, según
indica, es uno de los modelos meteorológicos de pronóstico más avanzados y
completos, siendo empleado en la mayoría de los proyectos relacionados con
modelación atmosférica encargados por organismos estatales como el Ministerio
del Medio Ambiente (MMA) y la ex Comisión Nacional de Energía (CNE) (ahora
Ministerio de Energía).

El WRF es un sistema de predicción numérico de meso escala no hidrostático
(considera los movimientos verticales), usado con fines de pronóstico operacional
y en investigación de la atmósfera. Los principales componentes de este modelo
son las fuentes externas de datos, como son los datos de entrada y la
información geográfica, el sistema de pre-procesamiento, el modelo WRF-ARW y
los sistemas de post-procesamiento.

Las fuentes externas de datos contienen información necesaria para inicializar
WRF. Éstos corresponden a las observaciones convencionales o satélites de la
atmósfera. De estos datos se obtienen las condiciones iniciales y de borde para
las simulaciones del WRF. También es necesario entregarle datos sobre el terreno
que contengan información sobre la orografía, uso de suelo, relieve y vegetación,
entre otros.

Para generar la modelación meteorológica, se utilizan cuatro dominios anidados,
donde cada celda es de 27, 9, 3 y 1 kilómetros respectivamente, centrados en el
Proyecto para un año calendario (2015) y resolución horaria. La información del
dominio con mayor resolución (1 km) es utilizado como dato de entrada para el
modelo de dispersión CALPUFF.

A continuación se realiza un análisis de la data meteorológica pronosticada de
superficie (modelo WRF) en la coordenada de localización de la estación de
monitoreo Chamonate, con resolución horaria para los parámetros de velocidad y
dirección de viento.

La Tabla N° 6 muestra los porcentajes de calmas en el periodo diurno y nocturno.
Cabe mencionar que la velocidad del viento considerada como calma,
corresponde a los registros inferiores a 0,5 (m/s).

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**7**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Tabla N° 6**_
_**Estadísticas de Datos Meteorológicos Modelados**_

|Estación|Datos Totales|Porcentaje de Calma (%)|Col4|
|---|---|---|---|
|**_Estación_**|**_Datos Totales_**|**_Periodo Diurno_**|**_Periodo Nocturno_**|
|WRF Chamonate|8.760|0,7|3,8|

Fuente: Algoritmos, 2017.

En las siguientes secciones se realiza un análisis cualitativo y cuantitativo de la
velocidad y dirección del viento modelado, ya que estos parámetros influyen
directamente en el fenómeno de dispersión de contaminantes.

**4.1** _**Series de Tiempo**_

Al observar la serie de tiempo de velocidad de viento (Figura N° 2), en términos
de variabilidad se observa un ciclo estacional con mayores velocidades
concentradas entre Agosto y Abril con valores que varían entre 0,5 y 8 m/s. Los
meses restante la variabilidad se encuentra concentrada en un rango menor, esto
es entre 0,5 y 4 m/s.

_**Figura N° 2**_
_**Serie temporal horaria velocidad del viento - Estación WRF Chamonate**_

_**Periodo 01 Enero 2015 - 31 Diciembre 2015**_

Fuente: Algoritmos, 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**8**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

Con respecto a la dirección de viento (Figura N° 3) es posible identificar tres
patrones principales. El primero de ellos corresponde a vientos provenientes
desde el Suroeste (SO), el segundo corresponde a vientos desde el Noreste (NE)
concentrados los meses de Abril a Septiembre, finalmente se observan vientos
desde Sur Sureste (SSE) correspondiente a la línea centrada entre 150 y 180°.

_**Figura N° 3**_
_**Serie temporal horaria dirección del viento - Estación WRF Chamonate**_

_**Periodo 01 Enero 2015 - 31 Diciembre 2015**_

Fuente: Algoritmos, 2017.

**4.2** **Rosa de Vientos**

La Figura N° 4 muestra la rosa de vientos indicando el porcentaje de frecuencia
en que el viento sopla en diferentes direcciones. Observando el comportamiento
desde las 00:00 a 23:00 horas, los registros muestran que la dirección de
máxima frecuencia corresponde a vientos procedentes desde el Suroeste (SO)
explicando un 33% de la frecuencia total, con valores de velocidades entre 3,6 y
8,8 m/s.

La Figura N° 5 muestra el comportamiento espacial de los vientos modelados en
los diferentes periodos del día para la estación WRF Chamonate. Durante la
madrugada (00:00 - 05:00 horas) es posible observar vientos que provienen
preferentemente desde el Noreste (NE) y Este Sureste (ESE) explicando en
conjunto sobre un 58% de la frecuencia total. Luego entre las 06:00 y 17:00
horas el viento cambia su patrón, presentando vientos procedentes desde el
Suroeste (SO) explicando en horas de la tarde el 70% de la frecuencia total.
Finalmente en horas de la tarde-noche entre las 18:00 y 23:00 horas el patrón
del viento vuelve a cambiar, siendo este desde el Sur Sureste (SSE) y Sureste
(SE) explicando en conjunto un 39% de la frecuencia total. Se observa además
que las velocidades varían entre 2,1 y 8,8 m/s.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**9**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 4**_
_**Rosas de Viento Ciclo Completo - WRF Estación Chamonate**_

_**Periodo 01 Enero 2015 - 31 Diciembre 2015**_

Fuente: Algoritmos, 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**10**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 5**_
_**Variabilidad temporal del viento - WRF Estación Chamonate**_

Fuente: Algoritmos, 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**11**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**4.3** **Ciclo Diario**

En la Figura N° 6 la curva de viento promedio para la estación Chamonate
muestra un marcado ciclo diario, con un mínimo observado alrededor de las
09:00 horas y el máximo a las 15:00 horas alcanzando una velocidad promedio
de 6 m/s aproximadamente. Se presenta una condición homogénea durante el
periodo nocturno con escasa presencia de calmas (viento inferior a 0,5 m/s) sin
máximos relativos. A partir de las 09:00 horas comienza a aumentar rápidamente
la intensidad donde una vez alcanzado el máximo comienza a disminuir.

En cuanto al ciclo diario de la dirección, se observan dos patrones reconocibles. El
primero en la madrugada con vientos que varían alrededor de 60°, es decir,
vientos procedentes desde el Noreste (NE). Luego esta componente se suprime,
dominando vientos preferentemente desde el Suroeste (SO) desde la 08:00 hasta
19:00 horas.

_**Figura N° 6**_
_**Ciclo diario de la velocidad del viento -WRF Estación Chamonate**_

_**Periodo 01 Enero 2015 - 31 Diciembre 2015**_

Fuente: Algoritmos, 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**12**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**4.4** **Ciclo estacional**

Al apreciar la Figura N° 7, es posible identificar que los vientos durante el periodo
diurno tienden a ser intensos la mayor parte del año, con valores que sobrepasan
los 6 m/s, lo cual presume condiciones favorables para la ventilación en la zona
del Proyecto, de esta manera se generaría menores tiempos de residencia de los
contaminantes que son emitidos hacia la atmósfera. Los vientos más débiles se
observan durante la madrugada con valores que no superan 3 m/s. En cuanto a
la dirección se observa durante el día vientos procedentes desde el Suroeste
(SO), los cuales están presente durante todo el año. Por otra parte, en horas de
la madrugada se observan dos patrones estacionales, por una parte vientos
desde Sur (S) Sureste (SE) desde enero a abril, y vientos desde Noreste (NE)
desde mayo a diciembre.

_**Figura N° 7**_
_**Ciclo estacional del viento - Estación Chamonate**_

_**Periodo 01 Enero 2015 - 31 Diciembre 2015**_

Fuente: Algoritmos, 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**13**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 5 Estimación de Emisiones del Proyecto

**5.1** **Actividades Emisoras**

La Tabla N°7 presenta las principales actividades emisoras de material
particulado respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), material
particulado sedimentable (MPS), dióxido de azufre (SO 2 ), óxidos de nitrógeno
(NO X ) y monóxido de carbono (CO) del Proyecto:

_**Tabla N° 7**_
_**Actividades Emisoras de Material Particulado y Gases**_

|Etapa|Actividades|
|---|---|
|Operación|Perforaciones, tronaduras, chancado, operación de harneros, carga y<br>descarga de material, tránsito de vehículos por caminos pavimentados y<br>no pavimentados, motor de vehículos y maquinarias.|

Fuente: Algoritmos 2017.

**5.2** **Método de Cálculo**

La ecuación general para determinar las emisiones de cualquier actividad es
definida por la EPA como sigue a continuación.

###### E  Fe  Na   1 Ea  (I)  100 

Dónde:

E : Emisión

FE : Factor de emisión

Na : Nivel de actividad

Ea : Eficiencia de abatimiento

Las emisiones asociadas a cada una de las actividades antes descritas, fueron
calculadas utilizando los factores de emisión definidos en el documento “AP 42,
Fifth Edition, _Compilation of Air Pollutant Emission Factors, Volumen 1: Stationary_
_Point and Area Sources, United States - Environmental Protection Agency”_ y en la
_“Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios_
_para la Región Metropolitana (Enero 2012)”_, habiéndose considerado además lo
señalado en el documento del Servicio de Evaluación Ambiental “INFORME FINAL;
Servicio de recopilación y sistematización de factores de emisión al aire para el
Servicio de Evaluación Ambiental”, publicado en Julio del año 2015.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**14**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

Para el caso del dióxido de azufre, la ecuación general (II) utilizada para el
cálculo de emisiones provenientes desde el motor de vehículos y maquinarias es
la siguiente:

#### E SO 2  2  CC  S comb (II)

Dónde:

E SO2 : Emisión SO 2 (Kg/h)

CC : Consumo de combustible (Kg/h)

S comb : Contenido de azufre del combustible (en peso m/m)

El contenido de azufre considerado para el cálculo de emisiones corresponde al
combustible Petróleo Diésel equivalente a 50 ppm(50/1.000.000 peso m/m).

Para determinar el consumo de combustible del motor de vehículos, se considera
la velocidad de circulación de cada uno de ellos.

En el caso del motor de maquinarias, el consumo de combustible se determina a
través de la siguiente ecuación (III):

_P_ _E_
_Cmm_ 


 _Ef_ 
 
 100 

_Ef_ 

 _PC_

(III)

100

Dónde:

Cmm : Consumo combustible de la maquinaria (kg/h)

P E : Potencia equivalente del motor (kcal/h)

Ef : Eficiencia motor (%)
PC : Poder calórico combustible (kcal/kg)

Para los cálculos se consideró, como escenario conservador desde el punto de
vista de la calidad del aire, que la eficiencia de los motores es del 50% y un
poder calórico del combustible de 10.900 kcal/kg, correspondiente a Petróleo
Diésel.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**15**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**5.3** **Factores de Emisión del Proyecto**

Los factores de emisión para material particulado MP 10, MP 2,5, MPS y gases NO 2,
SO 2 y CO considerados en el cálculo, se presentan en la siguiente Tabla.

_**Tabla N° 8**_
_**Factores de Emisión Considerados en el Cálculo**_

_**Etapa de Operación**_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
|Perforaciones|MPS<br>MP10 <br>MP2,5|0,59|(1)|Kg/perf|--|
|Tronaduras|MPS<br>MP10 <br>MP2,5||(1)|Kg/tron|k:Factor<br>tamaño de<br>partícula|
|Tronaduras|MPS<br>MP10 <br>MP2,5||(1)|Kg/tron|A:Área<br>detonada|
|Excavaciones|MP10|<br>|(1)|Kg/hr|f:% de finos<br>del material|
|Excavaciones|MP2,5<br>MPS|<br>|<br>|<br>|H:%<br>humedad del<br>material<br>|
|Excavaciones|MP2,5<br>MPS|<br>|<br>|<br>|k: Factor<br>tamaño de<br>partícula|
|Carga, descarga<br>y transferencia<br>de material|MPS<br>MP10 <br>MP2,5|<br>( <br> ~~)~~<br> <br>( <br> )<br>|(2)|Kg/ton|k: Factor<br>tamaño de<br>partícula|
|Carga, descarga<br>y transferencia<br>de material|MPS<br>MP10 <br>MP2,5|<br>( <br> ~~)~~<br> <br>( <br> )<br>|(2)|Kg/ton|u:Velocidad<br>del viento<br>(m/s)|
|Carga, descarga<br>y transferencia<br>de material|MPS<br>MP10 <br>MP2,5|<br>( <br> ~~)~~<br> <br>( <br> )<br>|(2)|Kg/ton|H: Humedad<br>del material<br>(%)|
|Fugitivas<br>caminos no<br>pavimentados<br>(vehículos<br>pesados)|MP10<br>MP2,5|~~( ~~ <br> ~~)~~<br> <br> ( <br> )<br> <br>|(4)|g/veh-<br>km|f: % de finos<br>del material|
|Fugitivas<br>caminos no<br>pavimentados<br>(vehículos<br>pesados)|MPS|~~( ~~ <br> ~~)~~<br> <br> ( <br> ~~)~~<br> <br>|(4)|g/veh-<br>km|W: Peso<br>promedio del<br>camión|
|Fugitivas<br>caminos no<br>pavimentados<br>(vehículos<br>pesados)|MPS|~~( ~~ <br> ~~)~~<br> <br> ( <br> ~~)~~<br> <br>|(4)|g/veh-<br>km|k: Factor<br>tamaño de<br>partícula|
|Fugitivas<br>caminos<br>pavimentados|MPS<br>MP10 <br>MP2,5||(4)|g/veh-<br>km|sL: Carga de<br>fino de la<br>superficie<br>(g/m2).|
|Fugitivas<br>caminos<br>pavimentados|MPS<br>MP10 <br>MP2,5||(4)|g/veh-<br>km|W: Peso<br>promedio del<br>camión|
|Fugitivas<br>caminos<br>pavimentados|MPS<br>MP10 <br>MP2,5||(4)|g/veh-<br>km|k: Factor<br>tamaño de<br>partícula|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**16**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
|Chancador<br>Primario|MPS<br>MP10 <br>MP2,5|0,20<br>0,02<br>0,02|(5)|Kg/ton|--|
|Chancador<br>Secundario|MPS<br>MP10 <br>MP2,5|0,60<br>0,05<br>0,05|(6)|Kg/ton|--|
|Chancador<br>Terciario|MPS<br>MP10 <br>MP2,5|1,40<br>0,08<br>0,08|(6)|Kg/ton|--|
|Harnero<br>Secundario|MPS<br>MP10 <br>MP2,5|0,036<br>0,036<br>0,150|(7)|Kg/ton|--|
|Harnero<br>Terciario|MPS<br>MP10 <br>MP2,5|0,036<br>0,036<br>0,150|(7)|Kg/ton|--|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|MPS<br>MP10 <br>MP2,5|((0,10+(0,42*exp(((-1)*0,04)*V)))+(0,86*<br>exp(((-1)*0,16)*V)))|(8)|g/veh-<br>km|V:Velocidad<br>camión<br>(Km/h)|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|SO2 <br>(CC)|((199,10+(496,04*exp(((-1)*0,05)*V)))+<br>(3.798,31*exp(((-1)*0,57)*V)))|((199,10+(496,04*exp(((-1)*0,05)*V)))+<br>(3.798,31*exp(((-1)*0,57)*V)))|((199,10+(496,04*exp(((-1)*0,05)*V)))+<br>(3.798,31*exp(((-1)*0,57)*V)))|((199,10+(496,04*exp(((-1)*0,05)*V)))+<br>(3.798,31*exp(((-1)*0,57)*V)))|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|CO|(1,26+(103,70/(1+exp((((-1)*-1,39)+<br>(0,54*ln(V)))+(0,04*V)))))|(8)|g/veh-<br>km|V:Velocidad<br>camión<br>(Km/h)|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|NOx|((5,58+(14,57*exp(((-1)*0,05)*V)))<br>+(45,65*exp(((-1)*0,31)*V)))|((5,58+(14,57*exp(((-1)*0,05)*V)))<br>+(45,65*exp(((-1)*0,31)*V)))|((5,58+(14,57*exp(((-1)*0,05)*V)))<br>+(45,65*exp(((-1)*0,31)*V)))|((5,58+(14,57*exp(((-1)*0,05)*V)))<br>+(45,65*exp(((-1)*0,31)*V)))|
|Motor de<br>vehículos<br>comerciales<br>Diésel tipo 2<br>(EURO III)|MPS<br>MP10 <br>MP2,5|0,67*(0.00005*V2- <br>0,005*V+0,19)<br>|(8)|g/veh-<br>km|V:Velocidad<br>vehículo<br>(Km/h)|
|Motor de<br>vehículos<br>comerciales<br>Diésel tipo 2<br>(EURO III)|SO2 <br>(CC)|0,02*V~~2~~- <br>2,51*V+137,42|0,02*V~~2~~- <br>2,51*V+137,42|0,02*V~~2~~- <br>2,51*V+137,42|0,02*V~~2~~- <br>2,51*V+137,42|
|Motor de<br>vehículos<br>comerciales<br>Diésel tipo 2<br>(EURO III)|CO|0,82*(0,0002*V2- <br>0,03*V+1,08)|(8)|g/veh-<br>km|V:Velocidad<br>vehículo<br>(Km/h)|
|Motor de<br>vehículos<br>comerciales<br>Diésel tipo 2<br>(EURO III)|NOx|0,84*(0.0002*V2- <br>0,03*V+2,02)|0,84*(0.0002*V2- <br>0,03*V+2,02)|0,84*(0.0002*V2- <br>0,03*V+2,02)|0,84*(0.0002*V2- <br>0,03*V+2,02)|
|Motor de buses<br>interurbanos<br>Diésel tipo 3<br>(EURO III)|MPS<br>MP10 <br>MP2,5|(0.08+(1.06/(1+EXP((((-1)*2.35)+<br>(1.08*LN(v)))+(0.01*v)))))|(8)|g/veh-<br>km|V: Velocidad<br>vehículo<br>(Km/h)|
|Motor de buses<br>interurbanos<br>Diésel tipo 3<br>(EURO III)|NOx|((5.31+(21.88*EXP(((-1)*0.05)*v)))+<br>(90.06*EXP(((-1)*0.25)*v)))|((5.31+(21.88*EXP(((-1)*0.05)*v)))+<br>(90.06*EXP(((-1)*0.25)*v)))|((5.31+(21.88*EXP(((-1)*0.05)*v)))+<br>(90.06*EXP(((-1)*0.25)*v)))|((5.31+(21.88*EXP(((-1)*0.05)*v)))+<br>(90.06*EXP(((-1)*0.25)*v)))|
|Motor de buses<br>interurbanos<br>Diésel tipo 3<br>(EURO III)|CC|((191.11+(700.03*EXP(((-1)*0.05)*v)))+<br>(3813.80*EXP(((-1)*0.45)*v)))|((191.11+(700.03*EXP(((-1)*0.05)*v)))+<br>(3813.80*EXP(((-1)*0.45)*v)))|((191.11+(700.03*EXP(((-1)*0.05)*v)))+<br>(3813.80*EXP(((-1)*0.45)*v)))|((191.11+(700.03*EXP(((-1)*0.05)*v)))+<br>(3813.80*EXP(((-1)*0.45)*v)))|
|Motor de buses<br>interurbanos<br>Diésel tipo 3<br>(EURO III)|CO|((1.09+(6.47*EXP(((-1)*0.05)*v)))+<br>(15.001*EXP(((-1)*0.22)*v)))|((1.09+(6.47*EXP(((-1)*0.05)*v)))+<br>(15.001*EXP(((-1)*0.22)*v)))|((1.09+(6.47*EXP(((-1)*0.05)*v)))+<br>(15.001*EXP(((-1)*0.22)*v)))|((1.09+(6.47*EXP(((-1)*0.05)*v)))+<br>(15.001*EXP(((-1)*0.22)*v)))|
|Motor de buses<br>interurbanos<br>Diésel tipo 3<br>(EURO III)|HC|(0.23+(15.66/(1+EXP((((-1)*-<br>0.53)+(0.65*LN(v)))+(0.03*v)))))|(8)|g/veh-<br>km|V: Velocidad<br>vehículo<br>(Km/h)|
|Motor de<br>maquinarias|MPS<br>MP10 <br>MP2,5<br>CO<br>NOx||(8)|g/hr|FP: Factor<br>potencia<br>maquina|
|Motor de<br>maquinarias|MPS<br>MP10 <br>MP2,5<br>CO<br>NOx||(8)|g/hr|C: Carga de<br>la maquina|
|Motor de<br>maquinarias|MPS<br>MP10 <br>MP2,5<br>CO<br>NOx||(8)|g/hr|P: Potencia<br>de la<br>maquina|

(1) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.9 “Western Surface Coal Mining”.
(2) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.4 “AggregateHandling and Storage
Piles”.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**17**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

(3) Factor obtenido desde Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para
la Región Metropolitana (Enero 2012), basado en “Industria del Árido en Chile, Tomo I, Sistemización de
Antecedentes Técnicos y Ambientales, 2001”.
(4) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.2 “Unpaved Road”.
(5) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.24 “MetallicMineralsProcessing”.
(6) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.24 “MetallicMineralsProcessing”.
Extrapolado linealmente desde factores de emisión para chancador primario y terciario.
(7) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.19 “Mineral Products Industry”.
(8) Factor obtenido desde Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para
la Región Metropolitana (Enero 2012).

_**Tabla N° 9**_
_**Valores Considerados en los Factores de Emisión**_

_**Etapa de Operación**_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
|Tronaduras|k: Factor tamaño de partícula MPS|1,00|(9)|
|Tronaduras|k: Factor tamaño de partícula MP10|0,52|(9)|
|Tronaduras|k: Factor tamaño de partícula MP2.5|0,03|(9)|
|Tronaduras|A: Área detonada (m2)|400|(10)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MPS|0,74|(12)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MP10|0,35|(12)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MP2.5|0,053|(12)|
|Carga y descarga de<br>material|H: Humedad del material (%)|2,2/5,4|(17)|
|Carga y descarga de<br>material|u: Velocidad del viento (m/s)|3,00|(13)|
|Fugitivas caminos no<br>pavimentados (vehículos<br>pesados)|k: Factor tamaño de partícula MPS|4,90|(14)|
|Fugitivas caminos no<br>pavimentados (vehículos<br>pesados)|k: Factor tamaño de partícula MP10|1,50|(14)|
|Fugitivas caminos no<br>pavimentados (vehículos<br>pesados)|k: Factor tamaño de partícula MP2.5|0,15|(14)|
|Fugitivas caminos no<br>pavimentados (vehículos<br>pesados)|W: Peso promedio flota camiones|--|(15)|
|Fugitivas caminos no<br>pavimentados (vehículos<br>pesados)|f: % de finos del suelo|9,7|(11)|
|Fugitivas caminos<br>pavimentados.|k: Factor tamaño de partícula MPS|3,230|(16)|
|Fugitivas caminos<br>pavimentados.|k: Factor tamaño de partícula MP10|0,620|(16)|
|Fugitivas caminos<br>pavimentados.|k: Factor tamaño de partícula MP2.5|0,150|(16)|
|Fugitivas caminos<br>pavimentados.|sL: Carga de fino de la superficie (g/m2)|0,02/0,6|(17)|
|Fugitivas caminos<br>pavimentados.|W: Peso promedio flota camiones|--|(15)|
|Motor de camiones<br>pesados diésel tipo 3<br>(EURO III)|v: Velocidad vehículos pesados en caminos internos<br>planta Mina (Km/h)|30|(10)|
|Motor de camiones<br>pesados diésel tipo 3<br>(EURO III)|v: Velocidad vehículos en caminos pavimentados (Km/h)|90|(10)|
|Motor de vehículos<br>comerciales Diésel tipo 2<br>(EURO III)|v: Velocidad vehículos en caminos externos(Km/h)|30|(10)|
|Motor de vehículos<br>comerciales Diésel tipo 2<br>(EURO III)|v: Velocidad vehículos en caminos pavimentados (Km/h)|90|(10)|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**18**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
|Motor de buses<br>interurbanos Diésel tipo 3<br>(EURO III)|v: Velocidad vehículos en caminos externos(Km/h)|30|(10)|
|Motor de buses<br>interurbanos Diésel tipo 3<br>(EURO III)|v: Velocidad vehículos en caminos pavimentados (Km/h)|90|(10)|
|Motor de Maquinarias|FP: Factor potencia Perforadora ROC 608 MP10 - MP2,5<br>- MPS|1,10|(18)|
|Motor de Maquinarias|FP: Factor potencia Excavadora MP10 - MP2,5 - MPS|1,10|(18)|
|Motor de Maquinarias|FP: Factor potencia Cargador Frontal MP10 - MP2,5 -<br>MPS|1,10|(18)|
|Motor de Maquinarias|FP: Factor potencia Bulldozer CAT D-08 MP10 - MP2,5 -<br>MPS|1,10|(18)|
|Motor de Maquinarias|FP: Factor potencia Motoniveladora CAT 120-M MP10 -<br>MP2,5 - MPS|1,23|(18)|
|Motor de Maquinarias|FP: Factor potencia Picarrocas MP10 - MP2,5 - MPS|1,10|(18)|
|Motor de Maquinarias|FP: Factor potencia Wheeldozer MP10 - MP2,5 - MPS|1,10|(18)|
|Motor de Maquinarias|FP: Factor potencia Perforadora ROC 608 CO|3,00|(18)|
|Motor de Maquinarias|FP: Factor potencia Excavadora CO|3,00|(18)|
|Motor de Maquinarias|FP: Factor potencia Cargador frontal CO|3,00|(18)|
|Motor de Maquinarias|FP: Factor potencia Bulldozer CAT D-08 CO|3,00|(18)|
|Motor de Maquinarias|FP: Factor potencia Motoniveladora CAT 120-M CO|3,76|(18)|
|Motor de Maquinarias|FP: Factor potencia Picarrocas CO|3,00|(18)|
|Motor de Maquinarias|FP: Factor potencia Wheeldozer CO|3,00|(18)|
|Motor de Maquinarias|FP: Factor potencia Perforadora ROC 608 NO2|14,36|(18)|
|Motor de Maquinarias|FP: Factor potencia Excavadora NO2|14,36|(18)|
|Motor de Maquinarias|FP: Factor potencia Cargador Frontal NO2|14,36|(18)|
|Motor de Maquinarias|FP: Factor potencia Bulldozer CAT D-08 NO2|14,36|(18)|
|Motor de Maquinarias|FP: Factor potencia Motoniveladora CAT 120-M NO2|14,36|(18)|
|Motor de Maquinarias|FP: Factor potencia Picarrocas NO2|14,36|(18)|
|Motor de Maquinarias|FP: Factor potencia Wheeldozer NO2|14,36|(18)|
|Motor de Maquinarias|C: Carga de la máquina Perforadora ROC 608|0,43|(18)|
|Motor de Maquinarias|C: Carga de la máquina Excavadora|0,59|(18)|
|Motor de Maquinarias|C: Carga de la máquina Cargador Frontal|0,59|(18)|
|Motor de Maquinarias|C: Carga de la máquina Bulldozer CAT D-08|0,59|(18)|
|Motor de Maquinarias|C: Carga de la máquina Motoniveladora CAT 120-M|0,59|(18)|
|Motor de Maquinarias|C: Carga de la máquina Picarrocas|0,59|(18)|
|Motor de Maquinarias|C: Carga de la máquina Wheeldozer|0,59|(18)|
|Motor de Maquinarias|P: Potencia nominal (kW) Perforadora ROC 608|402|(19)|
|Motor de Maquinarias|P: Potencia nominal (kW) Excavadora|485|(19)|
|Motor de Maquinarias|P: Potencia nominal (kW) Cargador Frontal|672|(19)|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**19**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
|Motor de Maquinarias|P: Potencia nominal (kW) Bulldozer CAT D-08|259|(19)|
|Motor de Maquinarias|P: Potencia nominal (kW) Motoniveladora CAT 120-M|103|(19)|
|Motor de Maquinarias|P: Potencia nominal (kW) Picarrocas|402|(19)|
|Motor de Maquinarias|P: Potencia nominal (kW) Wheeldozer|175|(19)|

(9) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.9 “Western Surface Coal Mining”.
(10) Valor proporcionado por el cliente
(11) Información obtenida muestreo de suelos
(12) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.4 “AggregateHandling and Storage

Piles”.
(13) Valor obtenido de modelación meteorológica en WRF.
(14) Factor obtenido desde Ap42, 5th edition: Capítulo 13, sección 13.2.2 “Unpaved Road”
(15) Ver sección 5.3.1.
(16) Factor obtenido desde Ap42, 5th edition: Capítulo 13, sección 13.2.1 “Paved Road”
(17) Factor obtenido desde el Informe Final Servicio de recopilación y sistematización de factores de emisión al

aire para el Servicio de Evaluación Ambiental Julio 2015
(18) EPA-420-R-10-016, NR-005d, julio 2010, “Median Life, Annual Activity, and Load Factor Values for Nonroad

Engine Emissions Modeling”.
(19) Valor extraído de la ficha técnica de cada maquinaria

**5.3.1** **Peso promedio**

Se determinó el peso promedio de la flota, considerando proporciones de acuerdo
al número de viajes que realiza cada vehículo que circulará por una misma vía:

(IV)

∑ (V)
Dónde _:_

_PPP_ : Proporción por tipo de vehículo del total de la flota

_PPR_ : Peso medio (ton)

_PPC_ : Peso medio asignado a cada tipo de vehículo (ton)

_PV_ : (Viajes totales por tipo de vehículo)/(total de viajes de la flota)

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**20**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**5.3.1.1** **Peso promedio etapa de Operación.**

**a)** **Caminos no Pavimentados:**

Los pesos promedio para la flota de vehículos que circularán por las vías no
pavimentadas, en la etapa de operación, son los siguientes:

_**Tabla N° 10**_
_**Peso Promedio Vehículos (ton) en Caminos no Pavimentados**_

_**“Etapa de Operación”**_

|Vehículo|Camino|Peso<br>Medio<br>(PPC)|No de<br>viajes al<br>año|Proporción<br>de viajes<br>(PV)b|Proporción<br>por peso<br>(PPP)c|Peso medio<br>de la Flota<br>“ton” (PPR)d|
|---|---|---|---|---|---|---|
|Camión de<br>Transporte|Rajo-Planta|50|91.250|0,962|47,88|49,5|
|Camión Aljibe Rajo-<br>Planta|Camión Aljibe Rajo-<br>Planta|44|3.650|0,038|1,653|1,653|
|Camión de<br>Transporte (100<br>ton)|Rajo - Botadero<br>de estéril|119|127.142|0,972|115,92|117,1|
|Camión Aljibe|Camión Aljibe|44|3.650|0,028|1,218|1,218|
|Camión de<br>Transporte|Planta- Botadero<br>de estéril|50|54.750|1,00|50|50|
|Camión de<br>Transporte (Mina -<br>Puerto)|Ruta C-357<br>(Tramo de<br>Bischofita)|56|28.389|0,478|26,77|47,8|
|Camión de<br>Transporte (Mina -<br>Planta Magnetita)|Camión de<br>Transporte (Mina -<br>Planta Magnetita)|56|20.278|0,341|19,12|19,12|
|Camión aljibe agua<br>industrial|Camión aljibe agua<br>industrial|44|730|0,012|0,535|0,535|
|Camión aljibe agua<br>potable|Camión aljibe agua<br>potable|44|183|0,003|0,134|0,134|
|Camión combustible|Camión combustible|14|104|0,002|0,025|0,025|
|Camión limpia fosas|Camión limpia fosas|14|52|0,001|0,012|0,012|
|Bus de personal|Bus de personal|26|1.460|0,025|0,646|0,646|
|Camión retiro<br>residuos|Camión retiro<br>residuos|28|156|0,003|0,073|0,073|
|Camionetas|Camionetas|3|7.300|0,123|0,398|0,398|
|Otros|Otros|3|730|0,012|0,040|0,040|

Fuente: Algoritmos 2017, en base a información proporcionada por el cliente.

b Proporción entre viajes totales de cada tipo de vehículo respecto del total de viajes en el camino
c Resultado al multiplicar la proporción de viajes de cada tipo de vehículo por el respectivo peso medio
d Peso promedio de la flota que circula por caminos no pavimentados.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**21**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**b)** **Caminos Pavimentados:**

Los pesos promedio para la flota de vehículos que circularán por las vías
pavimentadas, en la etapa de operación, son los siguientes:

_**Tabla N° 11**_
_**Peso Promedio Vehículos (ton) en Caminos Pavimentados**_

_**“Etapa de Operación”**_

|Vehículo|Camino|Peso Medio<br>(PPC)|No viajes<br>al año|Proporción<br>de viajes<br>(PV)e|Proporción<br>por peso<br>(PPP)f|Peso medio<br>de la Flota<br>“ton” (PPR)g|
|---|---|---|---|---|---|---|
|Camión de<br>Transporte<br>(Mina - Puerto)|Ruta C-357<br>/ Ruta C-<br>327|56|28.389|0,478|26,77|47,7|
|Camión de<br>Transporte<br>(Mina - Planta<br>Magnetita)|Camión de<br>Transporte<br>(Mina - Planta<br>Magnetita)|56|20.278|0,341|19,10|19,10|
|Camión aljibe<br>agua industrial|Camión aljibe<br>agua industrial|44|730|0,012|0,522|0,522|
|Camión aljibe<br>agua potable|Camión aljibe<br>agua potable|44|183|0,003|0,131|0,131|
|Camión<br>combustible|Camión<br>combustible|14|104|0,002|0,028|0,028|
|Camión limpia<br>fosas|Camión limpia<br>fosas|14|52|0,001|0,014|0,014|
|Bus de personal|Bus de personal|26|1.460|0,025|0,657|0,657|
|Camión retiro<br>residuos|Camión retiro<br>residuos|28|156|0,003|0,083|0,083|
|Camionetas|Camionetas|3|7.300|0,123|0,398|0,398|
|Otros|Otros|3|730|0,012|0,039|0,039|
|Camión de<br>Transporte Mina<br>- Puerto|Ruta 5 a<br>Puerto|56|48.667|1|56|56|
|Camión de<br>Transporte<br>(Mina - Planta<br>Magnetita)|Ruta 5 a<br>Planta<br>Magnetita|56|20.278|1|56|56|
|Camión aljibe<br>agua industrial|Ruta 5 a<br>Copiapó|44|730|0,068|2,958|10,3|
|Camión aljibe<br>agua potable|Camión aljibe<br>agua potable|44|183|0,017|0,740|0,740|
|Camión<br>combustible|Camión<br>combustible|14|104|0,010|0,141|0,141|
|Camión limpia<br>fosas|Camión limpia<br>fosas|14|52|0,005|0,071|0,071|
|Bus de personal|Bus de personal|26|1.460|0,136|3,574|3,574|

e Proporción entre viajes totales de cada tipo de vehículo respecto del total de viajes en el camino
f Resultado al multiplicar la proporción de viajes de cada tipo de vehículo por el respectivo peso medio
g Peso promedio de la flota que circula por caminos no pavimentados.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**22**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Vehículo|Camino|Peso Medio<br>(PPC)|No viajes<br>al año|Proporción<br>de viajes<br>(PV)e|Proporción<br>por peso<br>(PPP)f|Peso medio<br>de la Flota<br>“ton” (PPR)g|
|---|---|---|---|---|---|---|
|Camión retiro<br>residuos|Ruta 5 a<br>Copiapó|28|156|0,015|0,416|10,3|
|Camionetas|Camionetas|3|7.300|0,681|2,203|2,203|
|Otros|Otros|3|730|0,068|0,220|0,220|

Fuente: Algoritmos 2017, en base a información proporcionada por el cliente.

**5.4** **Nivel de actividad Etapa de Operación**

Para efecto del cálculo de emisiones se consideró un periodo anual de operación
de 365 días, en jornada completa de 24 horas diarias.

**5.4.1** **Tronaduras y Perforaciones**

Su nivel de actividad se determina de acuerdo al número de tronaduras y de
perforaciones que se realizarán anualmente.

_**Tabla N° 12**_
_**Nivel de Actividad para Tronaduras y Perforaciones**_

_**Etapa de Operación**_

|Sector|No de tronaduras<br>(tronaduras/año)|No de perforaciones<br>(perforaciones/año)|
|---|---|---|
|Mina Planta|156|12.960|

Fuente: Algoritmos 2017

**5.4.2** **Carga y Descarga de Material**

Para determinar el nivel de actividad asociado a la carga y descarga de material,
se requiere conocer el total de material involucrado en este proceso, en toneladas
al año. Para esto se utilizó el plan minero del Proyecto.

Las siguientes Tablas presenta la cantidad de material a cargar y descargar
(ton/año) en la etapa de operación.

_**Tabla N° 13**_
_**Carga de Material (ton/año)**_

_**Etapa de Operación**_

|Detalle|Carga (ton)|
|---|---|
|Material desde Stock Pile primario (A) a correa transportadora (C2-A)|1.800.000|
|Material desde Stock Pile primario (B) a correa transportadora (C4-B)|1.800.000|
|Material desde Stock Pile secundario (A) a correa transportadora (C7-A)|900.000|
|Material desde Stock Pile secundario (A) a correa transportadora (C6-A)|900.000|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**23**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Detalle|Carga (ton)|
|---|---|
|Material desde Stock Pile secundario (B) a correa transportadora (C6-B)|900.000|
|Material desde Stock Pile secundario (B) a correa transportadora (C7-B)|900.000|
|Material desde Stock Pile terciario (A) a correa transportadora (C13-A)|1.800.000|
|Material desde Stock Pile terciario (B) a correa transportadora (C13-B)|1.800.000|
|Material desde el Rajo al botadero (lastre generado en el rajo)|12.540.000|
|Rechazo de la planta a Botadero<br>|2.160.000|

Fuente: Algoritmos 2017.

_**Tabla N° 14**_
_**Descarga de Material (ton/año)**_

_**Etapa de Operación**_

|Detalle|Carga (ton)|
|---|---|
|Material desde el Rajo a alimentador Grizzly (A)|1.800.000|
|Material desde el Rajo a alimentador Grizzly (B)|1.800.000|
|Material desde alimentador Grizzly (A) a chancador primario (CH1-A)|1.350.000|
|Material desde alimentador Grizzly (B) a chancador primario (CH1-B)|1.350.000|
|Material desde alimentador Grizzly (A) a correa transportadora (C1-A)|450.000|
|Material desde alimentador Grizzly (B) a correa transportadora (C1-B)|450.000|
|Material desde chancador primario (A) a correa transportadora (C1-A)|1.350.000|
|Material desde chancador primario (B) a correa transportadora (C1-B)|1.350.000|
|Material desde correa transportadora (C1-A) a Stock Pile primario (A)|1.800.000|
|Material desde correa transportadora (C1-A) a Stock Pile primario (B)|1.800.000|
|Material desde Stock Pile primario (A) a correa transportadora (C2-A)|1.800.000|
|Material desde Stock Pile primario (B) a correa transportadora (C2-B)|1.800.000|
|Material desde correa transportadora (C2-A) a harnero (H1-A)|1.800.000|
|Material desde correa transportadora (C2-B) a harnero (H1-B)|1.800.000|
|Material desde harnero (H1-A) a chancador secundario (CH2-A)|1.350.000|
|Material desde harnero (H1-B) a chancador secundario (CH2-B)|1.350.000|
|Material desde chancador secundario (CH2-A) a correa transportadora (C3-A)|1.350.000|
|Material desde chancador secundario (CH2-B) a correa transportadora (C3-B)|1.350.000|
|Material desde correa transportadora (C3-A) a harnero (H1-A)|1.350.000|
|Material desde correa transportadora (C3-B) a harnero (H1-B)|1.350.000|
|Material desde harnero (H1-A) a correa transportadora (C4-A)|1.800.000|
|Material desde harnero (H1-B) a correa transportadora (C4-B)|1.800.000|
|Material correa transportadora (C4-A) a Stock Pile Secundario (A)|1.800.000|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**24**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Detalle|Carga (ton)|
|---|---|
|Material correa transportadora (C4-B) a Stock Pile Secundario (B)|1.800.000|
|Material desde Stock Pile secundario (A) a correa transportadora (C7-A)|900.000|
|Material desde Stock Pile secundario (B) a correa transportadora (C6-B)|900.000|
|Material desde Stock Pile secundario (A) a correa transportadora (C6-A)|900.000|
|Material desde Stock Pile secundario (B) a correa transportadora (C7-B)|900.000|
|Material desde correa transportadora (C7-A) a harnero (H2-A)|900.000|
|Material desde harnero (H2-A) a correa transportadora (C12-A)|675.000|
|Material desde correa transportadora (C12-A) a chancador terciario (CH3-A)|675.000|
|Material desde chancador terciario (CH3-A) a correa transportadora (C8-A)|675.000|
|Material desde correa transportadora (C8-A) a harnero (H2-A)|675.000|
|Material desde harnero (H2-A) a correa transportadora (C11-A)|900.000|
|Material desde correa transportadora (C11-A) a Stock Pile terciario (A)|900.000|
|Material desde correa transportadora (C6-A) a harnero (H3-A)|900.000|
|Material desde harnero (H3-A) a correa transportadora (C9-A)|675.000|
|Material desde correa transportadora (C9-A) a chancador terciario (CH4-A)|675.000|
|Material desde chancador terciario (CH4-A) a correa transportadora (C5-A)|675.000|
|Material desde correa transportadora (C5-A) a harnero (H3-A)|675.000|
|Material desde harnero (H3-A) a correa transportadora (C10-A)|900.000|
|Material desde correa transportadora (C10-A) a Stock Pile terciario (A)|900.000|
|Material desde correa transportadora (C6-B) a harnero (H2-B)|900.000|
|Material desde harnero (H2-B) a correa transportadora (C9-B)|675.000|
|Material desde correa transportadora (C9-B) a chancador terciario (CH3-B)|675.000|
|Material desde chancador terciario (CH3-B) a correa transportadora (C5-B)|675.000|
|Material desde correa transportadora (C5-B) a harnero (H2-B)|675.000|
|Material desde harnero (H2-B) a correa transportadora (C10-B)|900.000|
|Material desde correa transportadora (C10-B) a Stock Pile terciario (B)|900.000|
|Material desde correa transportadora (C7-B) a harnero (H3-B)|900.000|
|Material desde harnero (H3-B) a correa transportadora (C12-B)|675.000|
|Material desde correa transportadora (C12-B) a chancador terciario (CH4-B)|675.000|
|Material desde chancador terciario (CH4-B) a correa transportadora (C8-B)|675.000|
|Material desde correa transportadora (C8-B) a harnero (H3-B)|675.000|
|Material desde harnero (H3-B) a correa transportadora (C11-B)|900.000|
|Material desde correa transportadora (C11-B) a Stock Pile terciario (B)|900.000|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**25**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Detalle|Carga (ton)|
|---|---|
|Material desde Stock Pile terciario (A) a correa transportadora (C13-A)|1.800.000|
|Material desde Stock Pile terciario (B) a correa transportadora (C13-B)|1.800.000|
|Material desde correa transportadora (C13-A) a Torre 1|1.800.000|
|Material desde correa transportadora (C13-B) a Torre 1|1.800.000|
|Material desde Torre 1 a correa transportadora (C-14)|1.285.680|
|Material desde correa transportadora (C-14) a Producto concentrado (62%)|1.285.680|
|Material desde Torre 1 a correa transportadora (C-15)|2.314.320|
|Material desde correa transportadora (C-15) a Torre 2|2.314.320|
|Material desde Torre 2 a correa transportadora (C-16)|154.320|
|Material desde correa transportadora (C-16) a Producto concentrado (57%)|154.320|
|Material desde Torre 2 a correa transportadora (C-17)|2.160.000|
|Material desde correa transportadora (C-17) a rechazo planta|2.160.000|
|Rechazo de la planta a Botadero|2.160.000|
|Material desde el Rajo al botadero (lastre generado en el rajo)<br>|12.540.000|

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**26**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**5.4.3** **Chancadores y Harneros**

Para determinar el nivel de actividad asociado a la operación de chancadores y
harneros, se requiere conocer el total de material en toneladas al año que serán
procesados. Cabe señalar que durante el proceso existen 2 líneas de producción
que se consideraron en la estimación de emisiones.

La cantidad de material a chancar en Planta, se presenta en la siguiente Tabla.

_**Tabla N° 15**_
_**Cantidad de Material a procesar en chancadores (ton/año)**_

_**Etapa de Operación**_

|Línea de producción|Material a procesar en chancadores (ton/año)|Col3|Col4|
|---|---|---|---|
|**_Línea de producción_**|**_Primario_**|**_Secundario_**|**_Terciario_**|
|A|1.350.000|1.350.000|1.350.000|
|B|1.350.000|1.350.000|1.350.000|

Fuente: Algoritmos 2017.

_**Tabla N° 16**_
_**Cantidad de Material a procesar en harneros (ton/año)**_

_**Etapa de Operación**_

|Línea de producción|Material a procesar en harneros (ton/año)|Col3|
|---|---|---|
|**_Línea de producción_**|**_Secundario_**|**_Terciario_**|
|A|1.350.000|1.350.000|
|B|1.350.000|1.350.000|

Fuente: Algoritmos 2017.

**5.4.4** **Tránsito de Vehículos por tipo de carpeta.**

Para determinar el nivel de actividad asociado al tránsito de vehículos por
caminos no pavimentados, se requiere obtener los kilómetros totales recorridos
por cada tipo de vehículo. Para ello se ha considerado la siguiente ecuación (VII):

_KTR_  _VT_  _DR_ (VII)
Dónde:

KTR : Kilómetros totales recorridos al año (veh-Km/año)
VT : Viajes totales (ida + vuelta) al año por tipo de vehículo (veh/año)

DR : Distancia recorrida en cada viaje de ida (Km.)
Para estimar los viajes totales (ida + vuelta) al año que realizarán los camiones
tolvas (relleno y suministros), se consideró la siguiente ecuación (VIII):

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**27**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_VT_   _M_   2 (VIII)

 _CP_ 

Dónde:

VT : Viajes totales (ida + vuelta) al año por tipo de vehículo (veh/año)

M : Cantidad de material a transportar (ton)
CP : Capacidad de carga del camión (ton)

La siguiente Tabla presenta la cantidad de viajes totales (ida + vuelta) al año por
tipo de vehículos, la distancia recorrida en cada viajes de ida y el nivel de
actividad obtenidos al aplicar la ecuación (VII) y ecuación (VIII) en caminos no
pavimentados.

_**Tabla N° 17**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_

_**por Caminos no Pavimentados (veh-km/año)**_

_**Etapa de Operación**_

|Sector|Viajes Totales<br>(veh/año)<br>[VT]|Distancia<br>(km)<br>[DR]|Kilómetros Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|**Rajo-Planta**|**Rajo-Planta**|**Rajo-Planta**|**Rajo-Planta**|
|Camión de Transporte|182.500|0,7|127.750|
|Camión Aljibe Rajo-Planta|7.300|0,7|5.110|
|**Rajo - Botadero de estéril**|**Rajo - Botadero de estéril**|**Rajo - Botadero de estéril**|**Rajo - Botadero de estéril**|
|Camión de Transporte (100 ton)|254.283|1,0|254.283|
|Camión Aljibe|7.300|1,0|7.300|
|**Planta- Botadero de estéril**|**Planta- Botadero de estéril**|**Planta- Botadero de estéril**|**Planta- Botadero de estéril**|
|Camión de Transporte|109.500|0,25|27.375|
|**Ruta C-357 y ruta de acceso a faena (Tramo de Bischofita)**|**Ruta C-357 y ruta de acceso a faena (Tramo de Bischofita)**|**Ruta C-357 y ruta de acceso a faena (Tramo de Bischofita)**|**Ruta C-357 y ruta de acceso a faena (Tramo de Bischofita)**|
|Camión de Transporte (Mina - Puerto)|97.333|3,0|292.973|
|Camión de Transp Mina - Planta Magnetita|60.833|3,0|183.108|
|Camión aljibe agua industrial|1.460|3,0|4.395|
|Camión aljibe agua potable|365|3,0|1.099|
|Camión combustible|209|3,0|628|
|Camión limpia fosas|104|3,0|314|
|Bus de personal|2.920|3,0|8.789|
|Camión retiro residuos|313|3,0|942|
|Camionetas|14.600|3,0|43.946|
|Otros<br>|1.460<br>|3,0|4.395|

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**28**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

La siguiente Tabla presenta la cantidad de viajes totales (ida + vuelta) al año por
tipo de vehículos, la distancia recorrida en cada viaje de ida y el nivel de
actividad obtenidos al aplicar la ecuación (VII) y ecuación (VIII) en caminos
pavimentados.

_**Tabla N° 18**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_

_**por Caminos Pavimentados (veh-km/año)**_

_**Etapa de Operación**_

|Sector|Viajes Totales<br>(veh/año)<br>[VT]|Distancia<br>(km)<br>[DR]|Kilómetros Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|**Ruta C-357 / Ruta C-327**|**Ruta C-357 / Ruta C-327**|**Ruta C-357 / Ruta C-327**|**Ruta C-357 / Ruta C-327**|
|Camión de Transporte (Mina - Puerto)|97.333|3,5|336.773|
|Camión aljibe agua industrial|1.460|3,5|5.052|
|Camión aljibe agua potable|365|3,5|1.263|
|Camión combustible|209|3,5|722|
|Camión limpia fosas|104|3,5|361|
|Bus de personal|2.920|3,5|10.103|
|Camión retiro residuos|313|3,5|1.082|
|Camionetas|14.600|3,5|50.516|
|Otros|1.460|3,5|5.052|
|**Ruta 5 a Puerto**|**Ruta 5 a Puerto**|**Ruta 5 a Puerto**|**Ruta 5 a Puerto**|
|Camión de Transporte Mina - Puerto|97.333|39|3.796.000|
|**Ruta 5 a Planta Magnetita**|**Ruta 5 a Planta Magnetita**|**Ruta 5 a Planta Magnetita**|**Ruta 5 a Planta Magnetita**|
|Camión de Transp Mina - Planta Magnetita|40.556|38|1.541.111|
|**Ruta 5 a Copiapó**|**Ruta 5 a Copiapó**|**Ruta 5 a Copiapó**|**Ruta 5 a Copiapó**|
|Camión aljibe agua industrial|1.460|9,0|13.067|
|Camión aljibe agua potable|365|9,0|3.267|
|Camión combustible|209|9,0|1.867|
|Camión limpia fosas|104|9,0|933|
|Bus de personal|2.920|9,0|26.134|
|Camión retiro residuos|313|9,0|2.800|
|Camionetas|14.600|9,0|130.670|
|Otros|1.460|9,0|13.067|

Fuente: Algoritmos 2017.

En la estimación del número total de viajes que realizará cada vehículo se
consideraron tanto los viajes de ida como los de vuelta.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**29**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**5.4.5** **Motor de Maquinarias**

Para determinar el nivel de actividad asociado a la operación de cada motor de
maquinarias, se requiere obtener las horas de funcionamiento al año. Para ello se
ha considerado la siguiente ecuación (IX):

_HF_  _C_  _HD_  _DA_ (IX)
Dónde:

HF : Horas de funcionamiento al año (hr/año)

C : Cantidad de maquinarias
HD : Horas de funcionamiento al día por cada maquinaria (hr/día)
DA : Días de funcionamiento al año por cada maquinaria (días/año)

La siguiente Tabla presenta el tipo de maquinaria a utilizar, la potencia (kW), la
cantidad (C), periodos de funcionamiento y el nivel de actividad (hr/año)
obtenido al aplicar la ecuación (IX).

_**Tabla N° 19**_
_**Cálculo del Nivel de Actividad para Motor de Maquinarias (hr/año)**_

_**Etapa de Operación**_

|Tipo Maquinaria|Cantidad<br>[C]|Hr/día<br>[HD]|Día/año<br>[DA]|Hr/año<br>[HF]|Potencia<br>[kW]|
|---|---|---|---|---|---|
|Perforadora Roc 608|1|24|365|8.760|402|
|Perforadora Roc 608|1|8|365|2.920|402|
|Excavadora (Balde 4.5 m3)|1|24|365|8.760|485|
|Excavadora (Balde 2.5 m3)|1|8|365|2.920|370|
|Cargador Frontal (Balde 11 m3)|1|24|365|8.760|672|
|Cargador Frontal (Balde 6 m3)|1|24|365|8.760|396|
|Cargador Frontal Volvo W200|1|24|365|8.760|266|
|Bulldozer tipo Cat D-08|1|24|365|8.760|259|
|Bulldozer tipo Cat D-08|1|8|365|2.920|259|
|Motoniveladora tipo Cat 120 M|1|8|365|2.920|103|
|Pica rocas (Martillo Hidraulico)|1|8|365|2.920|402|
|Wheeldozer Modelo CAT.814|1|8|365|2.920|175|

Fuente: Algoritmos 2017, en base a información proporcionado por el cliente.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**30**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**5.4.6** **Medidas de Abatimiento de Polvo**

Con el objeto de reducir y controlar las emisiones de material particulado, se
implementará las siguientes acciones en los caminos:

_**Tabla N° 20**_
_**Medidas de Control que se aplicaran en los Caminos en la**_

_**Etapa de Operación.**_

|Sector|Medidas de Control de Emisiones de Material<br>Particulado|Eficiencia|
|---|---|---|
|Caminos de Acceso|Bischofita|90%|
|Caminos Secundarios|Aplicación de polímero orgánico|85%|
|Caminos Mineros|Aplicación de polímero orgánico|85%|

Fuente: Algoritmos 2017.

El respaldo técnico de los porcentajes atribuidos a cada supresor de polvo se
indica en el Anexo II, además se adjuntan los documentos originales en formato
PDF.

**5.5** **Tasas de Emisión**

Al multiplicar los factores de emisión presentados en la sección 5.3 con los
niveles de actividad definidos en las secciones 5.4 considerando la aplicación de
las medidas mitigatorias descritas, se obtienen las tasas de emisión anuales de
MPS, MP 10, MP 2,5 y gases SO 2, NO x y CO del Proyecto.

Las siguientes tablas presentan un resumen de las tasas de emisión resultantes
para la etapa de operación. En el Anexo I se presenta el detalle de las tasas de
emisiones según actividad y sector. Se reitera que estas emisiones consideran la
aplicación de las medidas de control de emisiones antes descritas en cada etapa
del proyecto.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**31**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Tabla N° 21**_
_**Tasas de Emisión Etapa de Operación (ton/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|Unidad|
|---|---|---|---|---|---|---|---|
|Perforaciones|0,0000|0,0000|0,0000|7,6464|7,6464|7,6464|ton/año|
|Tronaduras|0,0000|0,0000|0,0000|0,0083|0,1432|0,2753|ton/año|
|Carga|0,0000|0,0000|0,0000|2,2312|14,7346|31,1532|ton/año|
|Descarga|0,0000|0,0000|0,0000|5,8551|38,6658|81,7506|ton/año|
|Chancadores|0,0000|0,0000|0,0000|84,2400|84,2400|2.376,0000|ton/año|
|Harneros|0,0000|0,0000|0,0000|77,7600|77,7600|324,0000|ton/año|
|Tránsito camino no pavimentado|0,0000|0,0000|0,0000|17,6089|176,0891|600,1083|ton/año|
|Tránsito camino pavimentado|0,0000|0,0000|0,0000|5,3125|21,9585|114,3969|ton/año|
|Motor vehículos Caminos no pavimentados|0,0298|8,0497|2,2999|0,2129|0,2129|0,2129|ton/año|
|Motor de Vehículos camino Pavimentado|0,1229|33,8776|7,8040|0,6675|0,6675|0,6675|ton/año|
|Motor maquinaria|0,4219|215,6023|45,1771|16,5386|16,5386|16,5386|ton/año|
|**Total**|**0,5746**|**257,5296**|**55,2811**|**218,0814**|**438,6566**|**3.552,7497**|**ton/año**|

Fuente: Algoritmos 2017

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**32**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 6 Descripción del Modelo Utilizado

**6.1** **Modelo de Dispersión Atmosférica**

**6.1.1** **Base Teórica**

La aplicación de modelos de dispersión atmosférica permite determinar el aporte
de las emisiones provenientes de fuentes emisoras, en localidades y sectores
aledaños a las instalaciones de un determinado proyecto, permitiendo de este
modo asignar las cuotas de responsabilidad en los niveles de calidad del aire
medidos en su entorno.

Los modelos lagrangianos, se caracterizan por hacer uso de un sistema de
referencia que se ajusta al movimiento atmosférico. Es decir, las emisiones,
reacciones, deposición y mezclado de los contaminantes se analizan para un
volumen de aire que va cambiando su posición de acuerdo con la velocidad y
dirección del viento. Bajo este esquema general, los modelos lagrangianos se
pueden clasificar como modelos de trayectoria y modelos gaussianos, de acuerdo
con la geometría del sistema de modelación. Los modelos de trayectoria pueden
simular los procesos para una columna hipotética de aire, en cambio cuando la
simulación se hace para una pluma de emisión, continua o discreta (como
paquetes comúnmente llamados “puffs”), se trata de modelos gaussianos.

Los modelos gaussianos describen el transporte y mezcla de los contaminantes
asumiendo que las emisiones presentan, en las direcciones horizontal y vertical,
una distribución normal o de curva gaussiana con una concentración máxima en
el centro de la pluma. Generalmente estos modelos se aplican para evaluar la
dispersión de contaminantes provenientes de fuentes puntuales, aunque también
se aplican para simular emisiones de fuentes de área y de línea. Otra
característica de este tipo de modelos es que normalmente son aplicados para
evaluar la dispersión de contaminantes primarios no reactivos, aunque existen
versiones que incluyen en su formulación consideraciones especiales para poder
simular procesos de deposición y transformación química.

**6.1.2** **Motor de Vehículos**

Para determinar el nivel de actividad asociado a la operación de motores de
vehículos debido al tránsito por caminos se requiere obtener los kilómetros
totales recorridos por cada tipo de vehículo. Para ello, se han considerado los
valores presentados en la sección anterior, (Tabla N° 17 y Tabla N° 18).

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**33**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**6.1.3** **Sistema de Modelación WRF - CALPUFF**

El modelo utilizado para determinar el efecto que tendrán las emisiones de
material particulado y gases provenientes de la operación del Proyecto,
corresponde al sistema de modelación “WRF-CALPUFF” desarrollado por Earth
Tech.

En este modelo las emisiones se tratan como “puffs”, que se van desplazando a
través de un campo meteorológico tridimensional.

El sistema de modelación CALPUFF incluye tres componentes principales: WRF,
CALPUFF y CALPOST, además de una larga selección de preprocesadores
diseñados para incluir en el modelo datos meteorológicos y geofísicos.

En términos simples, WRF es un modelo de pronóstico meteorológico que simula
campos de viento y temperatura en un dominio de modelación engrillado y
tridimensional, WRF también produce campos en dos-dimensiones como altura de
mezcla, características de superficie y propiedades de dispersión.

CALPUFF modela el transporte y dispersión de contaminantes emitidos por las
fuentes emisoras en forma de paquetes o “PUFF” de material procesándolos a
través del dominio de modelación. La salida primaria de este modelo contiene
cada hora de concentración o flujo de deposición evaluados en receptores
determinados.

Finalmente CALPOST procesa las salidas de CALPUFF creando los archivos con las
tabulaciones necesarias para la evaluación de los resultados.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**34**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**6.2** **Variables de Entrada al Sistema de Modelación**

El sistema de modelación WRF-CALPUFF requiere de la siguiente data de entrada:

Archivos FNL, datos de entrada para el modelo de dispersión WRF.

Uso de Suelo, a partir de estos datos de definen los coeficientes de rugosidad

superficial, razón de Bowen y albedo. En la siguiente Tabla se presentan las
características de suelo.

_**Tabla N° 22**_
_**Características del Uso de Suelo**_

|Uso de Suelo|Albedoh|Col3|Razón de Boweni|Col5|Rugosidad Superficial|Col7|
|---|---|---|---|---|---|---|
|**_Uso de Suelo_**|**_Verano_**|**_Invierno_**|**_Verano_**|**_Invierno_**|**_Verano_**|**_Invierno_**|
|Urbano|0,18|0,18|1,50|1,50|0,50|0,50|
|Prados|0,19|0,23|1|1|0,12|0,1|
|Matorrales|0,22|0,25|1|1|0,1|0,1|
|Sabana|0,20|0,20|1,00|1,00|0,15|0,15|
|Humedales de<br>Madera|0,14|0,14|0,5|0,5|0,4|0,4|
|Terrenos de escasa<br>vegetación tipo<br>Barren|0,25|0,25|1|1|0,1|0,1|

Fuente: Algoritmos 2017.

h Albedo: reflectividad a la luz solar del suelo (expresada como fracción respecto a la unidad)
i Razón de Bowen: definida como la razón entre flujos sensibles y latentes, a nivel de superficie.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**35**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 8**_
_**Uso de Suelo**_

Fuente: Algoritmos 2017.

- Data de emisiones, Correspondiente al valor máximo mensual por fuente

emisora y contaminante, calculado en el capítulo anterior.

Ubicación de puntos de interés, Para evaluar los resultados en comparación
con la normativa aplicable, fueron considerados 2 puntos de interés, cuyas
coordenadas UTM - WGS84, se presenta en la. Tabla N° 23.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**36**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Tabla N° 23**_
_**Localización Puntos Discretos**_ _**[j]**_

|Punto de Interés|Este (m)|Norte (m)|Elevación (m)|
|---|---|---|---|
|Est Chamonate|360.196|6.980.081|300,2|
|Est Copiapó SIVICA|369.133|6.971.887|385,9|
|Tierra Amarilla|374.998|6.961.175|541,2|

Fuente: Algoritmos 2017.

_**Figura N° 9**_
_**Curvas de Nivel del Área de Modelación**_

Fuente: Algoritmos 2017.

j Datum WGS84, coordenadas UTM.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**37**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 7 Modelación

La modelación atmosférica permitirá evaluar el aporte de material particulado
sedimentable (MPS), material particulado (MP 10 ), material particulado respirable
fino (MP 2,5 ), dióxido de azufre (SO 2 ), óxidos de nitrógeno (NO X ) y monóxido de
carbono (CO).

Corresponde a las actividades asociadas a las fases de Operación, donde las
emisiones consideradas se presentan en el Capítulo 5 de este documento.

##### 8 Resultados de la Modelación

**8.1** **Campos de Viento**

Mediante la aplicación del modelo WRF fue posible simular el comportamiento de
los campos de vientos sobre el área de influencia del Proyecto, para cada una de
las horas consideradas en la modelación. Dichos campos de vientos permitirán
determinar posteriormente la dispersión de los contaminantes, a través de la
aplicación del modelo CALPUFF.

A modo de ejemplo, se seleccionó el día 20 de Agosto del año 2015, para
representar el comportamiento de los vientos superficiales en horas
representativas del día, en la madrugada (06:00 hrs.), a medio día (12:00 hrs.),
durante la tarde (18:00 hrs.) y en la noche (00:00 hrs.).

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**38**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 10**_
_**Campos de Viento a las 00:00 hrs.**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**39**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 11**_
_**Campos de Viento a las 06:00 hrs.**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**40**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 12**_
_**Campos de Viento a las 12:00 hrs.**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**41**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 13**_
_**Campos de Viento a las 18:00 hrs.**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**42**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**8.2** **Aportes Obtenidos en la Modelación**

Mediante la aplicación del modelo CALPUFF fue posible obtener las
concentraciones de material particulado y gases, que aportará el Proyecto.

Las siguientes Tabla presentan el resumen de las concentraciones resultantes de
la modelación en las estaciones de monitoreo definidas.

_**Tabla N° 24**_
_**Aportes del Proyecto, Etapa de Operación.**_

|Parámetro|Tipo de Norma|Estadístico|Receptores de interés|Col5|Col6|Unidad|
|---|---|---|---|---|---|---|
|**_Parámetro_**|**_Tipo de Norma_**|**_Estadístico_**|**_Est._**<br>**_Chamonate_**|**_Est._**<br>**_Copiapó_**|**_Tierra_**<br>**_Amarilla_**|**_Tierra_**<br>**_Amarilla_**|
|MPS|Secundaria|Media Anual|0,1828|0,0175|0,0056|mg/m2-día|
|MPS|Secundaria|Media Mensual|0,3291|0,0205|0,0069|0,0069|
|MP10|Primaria|Media Anual|6,2460|0,4221|0,1272|μg/m3N|
|MP10|Primaria|P98 Diario|16,5840|0,9564|0,2892|0,2892|
|MP2,5|Primaria|Media Anual|2,9524|0,1982|0,0623|0,0623|
|MP2,5|Primaria|P98 Diario|9,6674|0,4511|0,1580|0,1580|
|SO2|Primaria|Media Anual|0,0039|0,0007|0,0002|0,0002|
|SO2|Primaria|P99 Diario|0,0112|0,0015|0,0003|0,0003|
|SO2|Secundaria|Media Anual|0,0039|0,0007|0,0002|0,0002|
|SO2|Secundaria|P99,7 Diario|0,0130|0,0015|0,0003|0,0003|
|SO2|Secundaria|P99,73 Horario|0,0457|0,0053|0,0008|0,0008|
|NO2|Primaria|Media Anual|2,1414|0,2945|0,0705|0,0705|
|NO2|Primaria|P99 Horario|43,2970|2,6695|0,5307|0,5307|
|CO|Primaria|P99 8 hrs.|3,2016|0,2705|0,0690|0,0690|
|CO|Primaria|P99 Horario|8,7472|0,5813|0,1343|0,1343|

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**43**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**8.3** **Análisis respecto de los valores establecidos en la Normativa**

**Ambiental**

Para establecer el análisis respecto de la normativa ambiental vigente de calidad
del aire, se suman los aportes modelados en las estaciones de monitoreo con los
valores de línea de base registrados en ellas y que son presentados en la sección
3.

Cabe mencionar que en las estaciones Chamonante y Copiapó SIVICA solo se
realizó análisis comparativo de MP 10 y MP 2,5 ya que son los únicos contaminantes
monitoreados en estas estaciones.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**44**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

La siguiente Tabla presenta el análisis respecto de la normativa de calidad de aire correspondiente a la estación de
monitoreo Chamonate, donde (LB) corresponde a la línea de base y (AP) al aporte del Proyecto en etapa de
operación.

_**Tabla N° 25**_
_**Análisis Normativo Estación Chamonate, Etapa de Operación.**_

|Parámetro|Tipo de Norma|Estadístico|(LB)<br>(μg/m3N)|(AP)<br>(μg/m3N)|(LB+ AP)<br>(μg/m3N)|Norma<br>(μg/m3N)|% Norma|
|---|---|---|---|---|---|---|---|
|MP10|Primaria|Media Anual|37|6,25|43,25|50|86%|
|MP10|Primaria|P98 Diario|82|16,58|98,58|150|66%|
|MP2,5 <br>|Primaria<br>|Media Anual|9|2,95|11,95|20|60%|
|MP2,5 <br>|Primaria<br>|P98 Diario|18|9,67|27,67|50|55%|

Fuente: Algoritmos 2017

La Tabla N° 26 presenta el análisis respecto de la normativa de calidad de aire correspondiente a la estación de
monitoreo Copiapó SIVICA, donde (LB) corresponde a la línea de base y (AP) al aporte del Proyecto en etapa de
operación.

_**Tabla N° 26**_
_**Análisis Normativo Estación Copiapó SIVICA, Etapa de Operación.**_

|Parámetro|Tipo de Norma|Estadístico|(LB)<br>(μg/m3N)|(AP)<br>(μg/m3N)|(LB+ AP)<br>(μg/m3N)|Norma<br>(μg/m3N)|% Norma|
|---|---|---|---|---|---|---|---|
|MP10|Primaria|Media Anual|49|0,42|49,42|50|99%|
|MP10|Primaria|P98 Diario|107|0,96|107,96|150|72%|
|MP2,5 <br>|Primaria<br>|Media Anual|14|0,20|14,20|20|71%|
|MP2,5 <br>|Primaria<br>|P98 Diario|30|0,45|30,45|50|61%|

Fuente: Algoritmos 2017

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**45**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**8.4** **Ubicación Puntos de Máximo Impacto**

La Tabla N° 27 presenta los valores y la ubicación de los Puntos de Máximo
Impacto (PMI) para la etapa de Operación del Proyecto, para material particulado
sedimentable MPS, MP 10, MP 2,5, y gases SO 2, NO 2 y CO, en todos sus estadísticos
normados.

_**Tabla N° 27**_
_**Valores y coordenadas de Localización de Puntos de Máximo Impacto**_

|Parámetro|Estadístico|PMI|Norma|% Norma|Coordenadas UTM -<br>WGS84|Col7|
|---|---|---|---|---|---|---|
|**_Parámetro_**|**_Estadístico_**|**_PMI_**|**_Norma_**|**_% Norma_**|**_Este (m)_**|**_Norte (m)_**|
|MPS<br>(mg/m2 día)|Promedio del<br>Periodo|16,0980|100|16%|361.905|6.983.997|
|MPS<br>(mg/m2 día)|Promedio<br>mensual|19,0987|150|13%|361.905|6.983.997|
|MP10 <br>(ug/m3)|Promedio del<br>Periodo|351,5900|50|703%|361.905|6.983.997|
|MP10 <br>(ug/m3)|Percentil 98<br>Diario|653,9700|150|436%|361.905|6.983.997|
|MP2,5 <br>(ug/m3)|Promedio del<br>Periodo|507,0800|20|2535%|361.905|6.983.997|
|MP2,5 <br>(ug/m3)|Percentil 98<br>Diario|263,8100|50|528%|361.905|6.983.997|
|SO2 (ug/m3)|Promedio del<br>Periodo|0,1330|80|0.2%|361.905|6.983.997|
|SO2 (ug/m3)|Percentil 99<br>Diario|0,2793|250|0.1%|361.905|6.983.997|
|SO2 (ug/m3)|Percentil<br>99,7 Diario|0,3392|260|0.1%|361.905|6.983.997|
|SO2 (ug/m3)|Percentil<br>99,73<br>Horario|2,4945|700|0.4%|361.905|6.983.997|
|NO2 (ug/m3)|Promedio del<br>Periodo|39,4650|100|39.5%|361.905|6.983.997|
|NO2 (ug/m3)|Percentil 99<br>Horario|642,8400|400|160.7%|361.905|6.983.997|
|CO (ug/m3)|Percentil 99<br>8 Horas,|77,8410|10.000|0.8%|361.905|6.983.997|
|CO (ug/m3)|Percentil 99<br>Horario|199,7300|30.000|1%|361.905|6.983.997|

Fuente: Algoritmos 2017.

En la siguiente figura se observa la distribución espacial de los puntos de Máximo
Impacto (PMI) en el área de modelación. Cabe destacar que la totalidad de los
PMI, se ubican en un sector despoblado aledaño al Proyecto.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**46**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 14**_
_**Ubicación Puntos de Máximo Impacto (PMI)**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**47**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**8.5** **Mapas de Isoconcentraciones**
A continuación se presentan las isolíneas de concentración para el MP 10 para la etapa de Operación.

_**Figura N° 15**_
_**Promedio del periodo MP**_ _**10**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**48**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 16**_
_**Percentil 98 Diario de MP**_ _**10**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**49**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 17**_
_**Promedio del Periodo de MP**_ _**2,5**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**50**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 18**_
_**Percentil 98 Diario de MP**_ _**2,5**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**51**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 19**_
_**Promedio del Periodo de MPS, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**52**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 20**_
_**Promedio Mensual de MPS, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**53**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 21**_
_**Promedio del Periodo de SO**_ _**2**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**54**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 22**_
_**Percentil 99 Diario de SO**_ _**2**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**55**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 23**_
_**Percentil 99,7 Diario de SO**_ _**2**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**56**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 24**_
_**Percentil 99,73 Horario de SO**_ _**2**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**57**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 25**_
_**Promedio del Periodo de NO**_ _**2**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**58**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 26**_
_**Percentil 99 Horario NO**_ _**2**_ _**, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**59**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 27**_
_**Percentil 99 8 Horas de CO, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**60**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Figura N° 28**_
_**Percentil 99 Horario de CO, Etapa de Operación**_

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**61**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 9 Análisis sinérgicos con otros proyectos respecto a los valores establecidos en la Normativa Ambiental

Para establecer el análisis sinérgico con otros proyectos, respecto de la normativa
ambiental vigente de calidad del aire, se consideró el proyecto Mina Bellavista el
cual fue aprobado con RCA N°261, con fecha 20 de Agosto del año 2008.

Cabe mencionar que el Proyecto Mina Bellavista no se encuentra en operación,
por lo cual los registros monitoreados en las Estaciones Chamonate y Copiapó
SIVICA no consideran su aporte. Pese a esto, y ante una posible puesta en
marcha del proyecto se realizó el presente análisis.

El proyecto Mina Bellavista presentó una tasa de emisión de 179,5 (ton/año) de
MP 10, con lo cual se obtuvieron los siguientes aportes en las estaciones antes
mencionadas.

_**Tabla N° 28**_
_**Aportes en MP**_ _**10**_ _**del Proyecto Bellavista**_

|Estadístico|Aporte Proyecto<br>Bellavista<br>en EMRP|Aporte Proyecto<br>Bellavista<br>en Est. Copiapó SIVICA|Unidad|Norma|
|---|---|---|---|---|
|Valor promedio del período|1,33|0,11|ug/m3|50|
|Percentil 98 Promedio<br>Diario|4,74|0,33|ug/m3|150|

Fuente: Algoritmos 2017, en base a RCA N°261.

Cabe destacar que la EMRP sólo monitorea MP 10 y que se ubica en el mismo punto
geográfico de la Estación Chamonate, establecida en la modelación del presente
informe.

Con los aportes del Proyecto Mina Bellavista presentados en la Tabla N° 28 y los
correspondientes al Proyecto Fortuna, se realizó la suma de ambos más la Línea
de Base presentada. Los resultados se informan en las Tabla N° 29 y Tabla N°
30.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**62**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Tabla N° 29**_
_**Aportes Sinérgicos en MP**_ _**10**_ _**con Proyecto Mina Bellavista, en Estación**_

_**Chamonate**_

|Estadístico|Línea de<br>Base|Aporte<br>Proyecto<br>Bellavista<br>(AP1)|Aporte<br>Proyecto<br>Fortuna<br>(AP2)|LB+AP1+AP2|Norma|% de la<br>norma|
|---|---|---|---|---|---|---|
|Valor promedio<br>del período|37|1,33|6,25|44,58|50|89%|
|Percentil 98<br>Promedio Diario|82|4,74|16,58|103,32|150|69%|

Fuente: Algoritmos 2017.

_**Tabla N° 30**_
_**Aportes Sinérgicos en MP**_ _**10**_ _**con Proyecto Mina Bellavista, en Estación**_

_**Copiapó SIVICA**_

|Estadístico|Línea de<br>Base|Aporte<br>Proyecto<br>Bellavista<br>(AP1)|Aporte<br>Proyecto<br>Fortuna<br>(AP2)|LB+AP1+AP2|Norma|% de la<br>norma|
|---|---|---|---|---|---|---|
|Valor promedio<br>del período|49|0,11|0,42|49,53|50|99%|
|Percentil 98<br>Promedio Diario|107|0,33|0,96<br>|108,29|150|72%|

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**63**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

##### 10 Conclusiones

La modelación atmosférica realizada para el escenario de Operación permitió
evaluar los aportes generados por el Proyecto.

Según lo expuesto en las secciones anteriores, se concluye:

**Respecto de la Línea de Base:**

 - La Estación Copiapó SIVICA presenta el mayor porcentaje de
concentraciones de MP 10 monitoreado respecto de la normativa vigente. El
estadístico Promedio del Periodo para éste contaminante equivale al 98%
del valor que establece la norma, mientras el percentil 98 diario alcanza el
71%.

 - En relación al monitoreo de MP 2.5, la Estación Copiapó SIVICA nuevamente
presenta el mayor porcentaje de concentraciones respecto de la normativa.
El estadístico Promedio del Periodo para éste contaminante equivale al
70% del valor que establece la norma, mientras el percentil 98 diario
alcanza el 60%.

**Respecto del inventario de emisiones atmosféricas del proyecto, fase de**
**operación.**

 Los principal aportes en términos de emisiones de MP 2,5 y MPS están
definidos por el proceso de chancado con el 39% y 67% del total de
emisiones, respectivamente.

 Con respecto al MP 10, el principal aporte se debe al tránsito vehicular por
los caminos no pavimentados con el 40% del total de las emisiones de este
contaminante.

 - Los aportes principales para los contaminantes SO 2, NO 2 y CO, provienen
de la operación de maquinaria fuera de ruta con un 73%,84 % y 82% del
total de estas emisiones, respectivamente.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**64**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**Respecto del análisis de cumplimiento de la normativa**

A continuación se presentan los resultados obtenidos al sumar a la línea de base
los aportes del proyecto en la etapa de Operación, para ambas estaciones.

Estación Chamonate:

 - En el caso del material particulado MP 10 en el promedio del periodo se
alcanza un 86% del límite de la norma de 50 ug/m [3] N, alcanzando un
estado de latencia. Sin embargo, se destaca que los aportes del proyecto,
son pocos significativos con respecto a la norma, 6,25 μg/m [3] N (12,5% de
la Norma), y que el porcentaje de latencia se ve mayormente influenciado
por la línea de base registrada en esta estación, 37 μg/m [3] (74% de la
Norma). Para el estadístico percentil 98 diario de MP 10 se alcanza el 66%
del límite normado de 150 ug/m [3] N.

 En el material particulado fino MP 2,5 se alcanza para el promedio del
periodo un 60% del límite de 20 ug/m [3] N y en el estadístico percentil 98
diario un 55% de la norma límite de 50 ug/m [3] N.

Estación Copiapó SIVICA:

 - Para el caso del material particulado MP 10 en el promedio del periodo se
alcanza un 99% del límite de la norma de 50 ug/m [3] N, alcanzando un
estado de latencia. Sin embargo, al igual que en la Estación Chamonate, se
destaca que los aportes del proyecto, son pocos significativos con respecto
a la norma, 0,42 μg/m [3] N (0,84% de la Norma), y que el porcentaje de
latencia se ve mayormente influenciado por la línea de base registrada en
esta estación, 49 μg/m [3] (98% de la Norma). Para el estadístico percentil
98 diario de MP 10 se alcanza el 72% del límite de 150 ug/m [3] N, con un
aporte del proyecto que representa el 0,64% de la normativa.

 En el material particulado fino MP 2,5 se alcanza para el promedio del
periodo un 71% del límite de 20 ug/m [3] N, valor fuertemente influenciado
por la línea de base que aporta con el 99% del total. Para el estadístico
percentil 98 diario se alcanza un 61% de la norma límite de 50 ug/m [3] N,
con un aporte del proyecto que representa el 1,68% de la normativa.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**65**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

**Respecto del análisis sinérgicos con otro proyectos.**

Del análisis realizado en la Estación Chamonate se obtuvo que la suma de los
aporte de los Proyectos Fortuna y Bellavista a la línea de base actual no supera la
normativa vigente para MP 10 en ninguno de los dos estadísticos. Para el caso del
promedio del período se alcanza un 89% de la norma y para el percentil 98
diario, un 69%. Cabe destacar que en ambos estadísticos el aporte principal es
debido a los registros presentados en la Línea de Base.

Así también, se obtuvo que en la Estación Copiapó SIVICA la suma de los aporte
de los Proyectos Fortuna y Bellavista a la línea de base actual tampoco superan la
normativa vigente para MP 10 en ninguno de los dos estadísticos analizados. Para
el caso del promedio del período se alcanza un 99% de la norma y para el
percentil 98 diario, un 72%. Los valores de ambos estadísticos presentan gran
influencia del aporte de la Línea de Base.

De lo anterior se concluye que la operación del proyecto “Explotación Mina
Fortuna” genera bajos aportes en los contaminantes normados y monitoreados en
las zonas de interés analizadas.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**66**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

# _ANEXO I_

## _EMISIONES DESAGREGADAS_

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**67**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente|Descripción|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|
|---|---|---|---|---|---|---|---|
|Perforaciones|perf/año promedio|0,0000|0,0000|0,0000|7,6464|7,6464|7,6464|
|Tronaduras|tronadura/año promedio|0,0000|0,0000|0,0000|0,0083|0,1432|0,2753|
|Carga|Material desde Stock Pile primario (A) a correa transportadora (C2-A)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Carga|Material desde Stock Pile primario (B) a correa transportadora (C2-B)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Carga|Material desde Stock Pile secundario (A) a correa transportadora (C7-A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Carga|Material desde Stock Pile secundario (A) a correa transportadora (C6-A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Carga|Material desde Stock Pile secundario (B) a correa transportadora (C6-B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Carga|Material desde Stock Pile secundario (B) a correa transportadora (C7-B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Carga|Material desde Stock Pile terciario (A) a correa transportadora (C13-A)|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|
|Carga|Material desde Stock Pile terciario (B) a correa transportadora (C13-B)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Carga|Material desde el Rajo al botadero (lastre generado en el rajo)|0,0000|0,0000|0,0000|1,3927|9,1970|19,4450|
|Carga|Rechazo de la planta a Botadero|0,0000|0,0000|0,0000|0,0682|0,4507|0,9528|
|Descarga|Material desde el Rajo a alimentador Grizzly (A)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Descarga|Material desde el Rajo a alimentador Grizzly (B)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Descarga|Material desde alimentador Grizzly (A) a chancador primario (CH1-A)|0,0000|0,0000|0,0000|0,1499|0,9901|2,0934|
|Descarga|Material desde alimentador Grizzly (B) a chancador primario (CH1-B)|0,0000|0,0000|0,0000|0,1499|0,9901|2,0934|
|Descarga|Material desde alimentador Grizzly (A) a correa transportadora (C1-A)|0,0000|0,0000|0,0000|0,0500|0,3300|0,6978|
|Descarga|Material desde alimentador Grizzly (B) a correa transportadora (C1-B)|0,0000|0,0000|0,0000|0,0500|0,3300|0,6978|
|Descarga|Material desde chancador primario (A) a correa transportadora (C1-A)|0,0000|0,0000|0,0000|0,1499|0,9901|2,0934|
|Descarga|Material desde chancador primario (B) a correa transportadora (C1-B)|0,0000|0,0000|0,0000|0,1499|0,9901|2,0934|
|Descarga|Material desde correa transportadora (C1-A) a Stock Pile primario (A)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Descarga|Material desde correa transportadora (C1-A) a Stock Pile primario (B)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Descarga|Material desde Stock Pile primario (A) a correa transportadora (C2-A)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**68**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente|Descripción|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|
|---|---|---|---|---|---|---|---|
|Descarga|Material desde Stock Pile primario (B) a correa transportadora (C2-B)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Descarga|Material desde correa transportadora (C2-A) a harnero (H1-A)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Descarga|Material desde correa transportadora (C2-B) a harnero (H1-B)|0,0000|0,0000|0,0000|0,1999|1,3201|2,7911|
|Descarga|Material desde harnero (H1-A) a chancador secundario (CH2-A)|0,0000|0,0000|0,0000|0,1499|0,9901|2,0934|
|Descarga|Material desde harnero (H1-B) a chancador secundario (CH2-B)|0,0000|0,0000|0,0000|0,1499|0,9901|2,0934|
|Descarga|Material desde chancador secundario (CH2-A) a correa transportadora (C3-A)|0,0000|0,0000|0,0000|0,0427|0,2817|0,5955|
|Descarga|Material desde chancador secundario (CH2-B) a correa transportadora (C3-B)|0,0000|0,0000|0,0000|0,0427|0,2817|0,5955|
|Descarga|Material desde correa transportadora (C3-A) a harnero (H1-A)|0,0000|0,0000|0,0000|0,0427|0,2817|0,5955|
|Descarga|Material desde correa transportadora (C3-B) a harnero (H1-B)|0,0000|0,0000|0,0000|0,0427|0,2817|0,5955|
|Descarga|Material desde harnero (H1-A) a correa transportadora (C4-A)|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|
|Descarga|Material desde harnero (H1-B) a correa transportadora (C4-B)|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|
|Descarga|Material correa transportadora (C4-A) a Stock Pile Secundario (A)|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|
|Descarga|Material correa transportadora (C4-B) a Stock Pile Secundario (B)|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|
|Descarga|Material desde Stock Pile secundario (A) a correa transportadora (C7-A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde Stock Pile secundario (B) a correa transportadora (C6-B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde Stock Pile secundario (A) a correa transportadora (C6-A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde Stock Pile secundario (B) a correa transportadora (C7-B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde correa transportadora (C7-A) a harnero (H2-A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde harnero (H2-A) a correa transportadora (C12-A)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde correa transportadora (C12-A) a chancador terciario (CH3-A)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde chancador terciario (CH3-A) a correa transportadora (C8-A)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde correa transportadora (C8-A) a harnero (H2-A)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde harnero (H2-A) a correa transportadora (C11-A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**69**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente|Descripción|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|
|---|---|---|---|---|---|---|---|
|Descarga|Material desde correa transportadora (C11-A) a Stock Pile terciario (A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde correa transportadora (C6-A) a harnero (H3-A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde harnero (H3-A) a correa transportadora (C9-A)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde correa transportadora (C9-A) a chancador terciario (CH4-A)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde chancador terciario (CH4-A) a correa transportadora (C5-A)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde correa transportadora (C5-A) a harnero (H3-A)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde harnero (H3-A) a correa transportadora (C10-A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde correa transportadora (C10-A) a Stock Pile terciario (A)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde correa transportadora (C6-B) a harnero (H2-B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde harnero (H2-B) a correa transportadora (C9-B)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde correa transportadora (C9-B) a chancador terciario (CH3-B)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde chancador terciario (CH3-B) a correa transportadora (C5-B)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde correa transportadora (C5-B) a harnero (H2-B)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde harnero (H2-B) a correa transportadora (C10-B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde correa transportadora (C10-B) a Stock Pile terciario (B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde correa transportadora (C7-B) a harnero (H3-B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde harnero (H3-B) a correa transportadora (C12-B)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde correa transportadora (C12-B) a chancador terciario (CH4-B)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde chancador terciario (CH4-B) a correa transportadora (C8-B)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde correa transportadora (C8-B) a harnero (H3-B)|0,0000|0,0000|0,0000|0,0213|0,1408|0,2978|
|Descarga|Material desde harnero (H3-B) a correa transportadora (C11-B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde correa transportadora (C11-B) a Stock Pile terciario (B)|0,0000|0,0000|0,0000|0,0284|0,1878|0,3970|
|Descarga|Material desde Stock Pile terciario (A) a correa transportadora (C13-A)|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**70**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente|Descripción|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|
|---|---|---|---|---|---|---|---|
|Descarga|Material desde Stock Pile terciario (B) a correa transportadora (C13-B)|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|
|Descarga|Material desde correa transportadora (C13-A) a Torre 1|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|
|Descarga|Material desde correa transportadora (C13-B) a Torre 1|0,0000|0,0000|0,0000|0,0569|0,3755|0,7940|
|Descarga|Material desde Torre 1 a correa transportadora (C-14)|0,0000|0,0000|0,0000|0,0406|0,2682|0,5671|
|Descarga|Material desde correa transportadora (C-14) a Producto concentrado (62%)|0,0000|0,0000|0,0000|0,0406|0,2682|0,5671|
|Descarga|Material desde Torre 1 a correa transportadora (C-15)|0,0000|0,0000|0,0000|0,0731|0,4828|1,0209|
|Descarga|Material desde correa transportadora (C-15) a Torre 2|0,0000|0,0000|0,0000|0,0731|0,4828|1,0209|
|Descarga|Material desde Torre 2 a correa transportadora (C-16)|0,0000|0,0000|0,0000|0,0049|0,0322|0,0681|
|Descarga|Material desde correa transportadora (C-16) a Producto concentrado (57%)|0,0000|0,0000|0,0000|0,0049|0,0322|0,0681|
|Descarga|Material desde Torre 2 a correa transportadora (C-17)|0,0000|0,0000|0,0000|0,0682|0,4507|0,9528|
|Descarga|Material desde correa transportadora (C-17) a rechazo planta|0,0000|0,0000|0,0000|0,0682|0,4507|0,9528|
|Descarga|Rechazo de la planta a Botadero|0,0000|0,0000|0,0000|0,0682|0,4507|0,9528|
|Descarga|Material desde el Rajo al botadero (lastre generado en el rajo)|0,0000|0,0000|0,0000|1,3927|9,1970|19,4450|
|Chancador|Chancador primario Planta (CH1-A)|0,0000|0,0000|0,0000|10,8000|10,8000|108,0000|
|Chancador|Chancador primario Planta (CH1-B)|0,0000|0,0000|0,0000|10,8000|10,8000|108,0000|
|Chancador|Chancador secundario (CH2-A)|0,0000|0,0000|0,0000|27,0000|27,0000|324,0000|
|Chancador|Chancador secundario (CH2-B)|0,0000|0,0000|0,0000|27,0000|27,0000|324,0000|
|Chancador|Chancador terciario (CH3-A)|0,0000|0,0000|0,0000|2,1600|2,1600|378,0000|
|Chancador|Chancador terciario (CH4-A)|0,0000|0,0000|0,0000|2,1600|2,1600|378,0000|
|Chancador|Chancador terciario (CH3-B)|0,0000|0,0000|0,0000|2,1600|2,1600|378,0000|
|Chancador|Chancador terciario (CH4-B)|0,0000|0,0000|0,0000|2,1600|2,1600|378,0000|
|Harneros|Harnero secundario vibrador (H1-A)|0,0000|0,0000|0,0000|19,4400|19,4400|81,0000|
|Harneros|Harnero secundario vibrador (H1-B)|0,0000|0,0000|0,0000|19,4400|19,4400|81,0000|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**71**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente|Descripción|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|
|---|---|---|---|---|---|---|---|
|Harneros|Harnero terciario vibrador (H1-A)|0,0000|0,0000|0,0000|9,7200|9,7200|40,5000|
|Harneros|Harnero terciario vibrador (H2-A)|0,0000|0,0000|0,0000|9,7200|9,7200|40,5000|
|Harneros|Harnero terciario vibrador (H1-B)|0,0000|0,0000|0,0000|9,7200|9,7200|40,5000|
|Harneros|Harnero terciario vibrador (H2-B)|0,0000|0,0000|0,0000|9,7200|9,7200|40,5000|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Rajo-Planta|0,0000|0,0000|0,0000|2,4800|24,8003|84,5189|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión Aljibe Rajo-Planta|0,0000|0,0000|0,0000|0,0992|0,9920|3,3808|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Rajo - Botadero de estéril (100 ton)|0,0000|0,0000|0,0000|7,2715|72,7146|247,8099|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión Aljibe Rajo- Botadero de estéril|0,0000|0,0000|0,0000|0,2088|2,0875|7,1142|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Planta - Botadero de estéril (40 ton)|0,0000|0,0000|0,0000|0,5326|5,3258|18,1503|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Mina - Puerto|0,0000|0,0000|0,0000|3,8028|38,0282|129,5995|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Mina - Planta Magnetita|0,0000|0,0000|0,0000|2,3768|23,7676|80,9997|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión aljibe agua industrial|0,0000|0,0000|0,0000|0,0570|0,5704|1,9440|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión aljibe agua potable|0,0000|0,0000|0,0000|0,0143|0,1426|0,4860|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión combustible|0,0000|0,0000|0,0000|0,0081|0,0815|0,2777|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión limpiafosas|0,0000|0,0000|0,0000|0,0041|0,0407|0,1389|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Bus de personal|0,0000|0,0000|0,0000|0,1141|1,1408|3,8880|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camión retiro residuos|0,0000|0,0000|0,0000|0,0122|0,1222|0,4166|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Camionetas|0,0000|0,0000|0,0000|0,5704|5,7042|19,4399|
|Tránsito<br>vehículos<br>camino no<br>pavimentado|Otros|0,0000|0,0000|0,0000|0,0570|0,5704|1,9440|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Rajo-Planta|0,0041|1,1164|0,3184|0,0293|0,0293|0,0293|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión Aljibe Rajo-Planta|0,0002|0,0447|0,0127|0,0012|0,0012|0,0012|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Rajo - Botadero de estéril (100 ton)|0,0082|2,2222|0,6337|0,0584|0,0584|0,0584|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión Aljibe Rajo- Botadero de estéril|0,0002|0,0638|0,0182|0,0017|0,0017|0,0017|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**72**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente|Descripción|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|
|---|---|---|---|---|---|---|---|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Planta - Botadero de estéril (40 ton)|0,0009|0,2392|0,0682|0,0063|0,0063|0,0063|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Mina - Puerto|0,0094|2,5603|0,7302|0,0673|0,0673|0,0673|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión de Transp Mina - Planta Magnetita|0,0059|1,6002|0,4563|0,0420|0,0420|0,0420|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión aljibe agua industrial|0,0001|0,0384|0,0110|0,0010|0,0010|0,0010|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión aljibe agua potable|0,0000|0,0096|0,0027|0,0003|0,0003|0,0003|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión combustible|0,0000|0,0055|0,0016|0,0001|0,0001|0,0001|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión limpiafosas|0,0000|0,0027|0,0008|0,0001|0,0001|0,0001|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Bus de personal|0,0003|0,0863|0,0241|0,0022|0,0022|0,0022|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camión retiro residuos|0,0000|0,0082|0,0023|0,0002|0,0002|0,0002|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Camionetas|0,0004|0,0475|0,0179|0,0026|0,0026|0,0026|
|Motor tránsito<br>vehículos<br>camino no<br>pavimentado|Otros|0,0000|0,0048|0,0018|0,0003|0,0003|0,0003|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión de Transp Mina - Puerto|0,0000|0,0000|0,0000|0,6954|2,8741|14,9733|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión de Transp Mina - Planta Magnetita|0,0000|0,0000|0,0000|0,2897|1,1976|6,2389|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión aljibe agua industrial|0,0000|0,0000|0,0000|0,0104|0,0431|0,2246|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión aljibe agua potable|0,0000|0,0000|0,0000|0,0026|0,0108|0,0562|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión combustible|0,0000|0,0000|0,0000|0,0015|0,0062|0,0321|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión limpiafosas|0,0000|0,0000|0,0000|0,0007|0,0031|0,0160|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Bus de personal|0,0000|0,0000|0,0000|0,0209|0,0862|0,4492|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión retiro residuos|0,0000|0,0000|0,0000|0,0022|0,0092|0,0481|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camionetas|0,0000|0,0000|0,0000|0,1043|0,4311|2,2460|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Otros|0,0000|0,0000|0,0000|0,0104|0,0431|0,2246|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión de Transp Mina - Puerto|0,0000|0,0000|0,0000|2,9501|12,1938|63,5256|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión de Transp Mina - Planta Magnetita|0,0000|0,0000|0,0000|1,1977|4,9505|25,7903|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**73**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente|Descripción|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|
|---|---|---|---|---|---|---|---|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión aljibe agua industrial|0,0000|0,0000|0,0000|0,0018|0,0075|0,0390|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión aljibe agua potable|0,0000|0,0000|0,0000|0,0005|0,0019|0,0097|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión combustible|0,0000|0,0000|0,0000|0,0003|0,0011|0,0056|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión limpiafosas|0,0000|0,0000|0,0000|0,0001|0,0005|0,0028|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Bus de personal|0,0000|0,0000|0,0000|0,0036|0,0150|0,0779|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camión retiro residuos|0,0000|0,0000|0,0000|0,0004|0,0016|0,0084|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Camionetas|0,0000|0,0000|0,0000|0,0181|0,0748|0,3897|
|Tránsito<br>vehículos<br>camino<br>pavimentado|Otros|0,0000|0,0000|0,0000|0,0018|0,0075|0,0390|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión de Transp Mina - Puerto|0,0070|1,9299|0,4421|0,0373|0,0373|0,0373|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión de Transp Mina - Planta Magnetita|0,0029|0,8041|0,1842|0,0156|0,0156|0,0156|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión aljibe agua industrial|0,0001|0,0289|0,0066|0,0006|0,0006|0,0006|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión aljibe agua potable|0,0000|0,0072|0,0017|0,0001|0,0001|0,0001|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión combustible|0,0000|0,0041|0,0009|0,0001|0,0001|0,0001|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión limpiafosas|0,0000|0,0021|0,0005|0,0000|0,0000|0,0000|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Bus de personal|0,0002|0,0555|0,0120|0,0011|0,0011|0,0011|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión retiro residuos|0,0000|0,0062|0,0014|0,0001|0,0001|0,0001|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camionetas|0,0004|0,0473|0,0225|0,0040|0,0040|0,0040|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Otros|0,0000|0,0047|0,0022|0,0004|0,0004|0,0004|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión de Transp Mina - Puerto|0,0784|21,7527|4,9830|0,4207|0,4207|0,4207|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión de Transp Mina - Planta Magnetita|0,0318|8,8312|2,0230|0,1708|0,1708|0,1708|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión aljibe agua industrial|0,0003|0,0749|0,0172|0,0014|0,0014|0,0014|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión aljibe agua potable|0,0001|0,0187|0,0043|0,0004|0,0004|0,0004|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión combustible|0,0000|0,0107|0,0025|0,0002|0,0002|0,0002|

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**74**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

|Fuente|Descripción|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|
|---|---|---|---|---|---|---|---|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión limpiafosas|0,0000|0,0053|0,0012|0,0001|0,0001|0,0001|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Bus de personal|0,0005|0,1435|0,0311|0,0029|0,0029|0,0029|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camión retiro residuos|0,0001|0,0160|0,0037|0,0003|0,0003|0,0003|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Camionetas|0,0009|0,1223|0,0581|0,0103|0,0103|0,0103|
|Motor tránsito<br>vehículos<br>camino<br>pavimentado|Otros|0,0001|0,0122|0,0058|0,0010|0,0010|0,0010|
|Maquinaria<br>Fuera de Ruta<br><br>|Perforadora Roc 608|0,0556|21,7447|4,5428|1,6657|1,6657|1,6657|
|Maquinaria<br>Fuera de Ruta<br><br>|Perforadora Roc 608|0,0185|7,2482|1,5143|0,5552|0,5552|0,5552|
|Maquinaria<br>Fuera de Ruta<br><br>|Excavadora (Balde 4,5 m3)|0,0671|35,9958|7,5200|2,7573|2,7573|2,7573|
|Maquinaria<br>Fuera de Ruta<br><br>|Excavadora (Balde 2,5 m3)|0,0171|9,1536|1,9123|0,7012|0,7012|0,7012|
|Maquinaria<br>Fuera de Ruta<br><br>|Cargador Frontal (Balde 11 m3)|0,0930|49,8746|10,4195|3,8205|3,8205|3,8205|
|Maquinaria<br>Fuera de Ruta<br><br>|Cargador Frontal (Balde 6 m3)|0,0548|29,3904|6,1401|2,2514|2,2514|2,2514|
|Maquinaria<br>Fuera de Ruta<br><br>|Cargador Frontal Volvo W200|0,0368|19,7420|4,1244|1,5123|1,5123|1,5123|
|Maquinaria<br>Fuera de Ruta<br><br>|Bulldozer tipo Cat D-08|0,0358|19,2225|4,0158|1,4725|1,4725|1,4725|
|Maquinaria<br>Fuera de Ruta<br><br>|Bulldozer tipo Cat D-08|0,0119|6,4075|1,3386|0,4908|0,4908|0,4908|
|Maquinaria<br>Fuera de Ruta<br><br>|Motoniveladora tipo Cat 120 M|0,0047|2,5482|0,6672|0,2183|0,2183|0,2183|
|Maquinaria<br>Fuera de Ruta<br><br>|Pica rocas (Martillo Hidraulico)|0,0185|9,9452|2,0777|0,7618|0,7618|0,7618|
|Maquinaria<br>Fuera de Ruta<br><br>|Wheeldozer Modelo CAT,814<br>|0,0081|4,3294|0,9045|0,3316|0,3316|0,3316|

Fuente: Algoritmos 2017.

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**75**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

# _ANEXO II_
## _FICHAS TÉCNICAS SUPRESORES DE POLVO_

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**76**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Ficha técnica de supresión de polvo por aplicación de polímero orgánico**_

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**77**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_

_**Ficha técnica de supresión de polvo por aplicación de Bischofita**_

_**Modelación de la Dispersión de las Emisiones Atmosféricas Provenientes del Proyecto**_ _**78**_
_**Fortuna**_
_**Versión A-1**_

_**Octubre, 2017**_