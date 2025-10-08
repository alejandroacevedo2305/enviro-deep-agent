---
title: DIA Servicomunal
author: SGA
date: D:20160817102332-03'00'
language: es
type: report
pages: 48
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 2-13 MODELACIÓN ATMOSFÉRICA
-->

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

# ANEXO 2-13 MODELACIÓN ATMOSFÉRICA

**Rosario Norte 100 Piso 14, Las Condes, Santiago, Chile. Fono: 562-2580 6500;**

**[e-mail: contacto@sgasa.cl;](mailto:contacto@sgasa.cl)** **[www.sgasa.cl](http://www.sgasa.cl/)**

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**ÍNDICE**

**1** **INTRODUCCIÓN ....................................................................................................................................... 3**

**2** **RESUMEN DE ESTIMACIÓN DE EMISIONES ............................................................................................... 6**

**3** **MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES ............................................................................... 7**

3.1 M ARCO L EGAL ................................................................................................................................................ 7

3.2 B ASE T EÓRICA DEL M ODELO U TILIZADO .............................................................................................................. 8

3.3 A NÁLISIS M ETEOROLÓGICO ............................................................................................................................... 9

3.4 C ONSTRUCCIÓN DE E SCENARIOS ....................................................................................................................... 15

_3.4.1_ _Escenario de Emisiones ................................................................................................................... 15_

_3.4.2_ _Escenario de Receptores ................................................................................................................. 17_
_3.4.3_ _Escenario Meteorológico ................................................................................................................ 19_
_3.4.4_ _Escenario Geofísico ......................................................................................................................... 20_

3.5 R ESULTADOS DE LA I MPLEMENTACIÓN DEL M ODELO ............................................................................................ 21

_3.5.1_ _Implementación del Modelo de Dispersión CALPUFF ..................................................................... 21_

3.6 A NÁLISIS DE C UMPLIMIENTO N ORMATIVO VIGENTE DE C ALIDAD DEL A IRE ................................................................ 24

_3.6.1_ _Material Particulado Respirable (MP10) y Fino (MP2,5) Escenario de Construcción ..................... 24_
_3.6.2_ _Gases, Dióxido de Nitrógeno (NO2), Dióxido de Azufre (SO2) y Monóxido de Carbono (CO)_

_Escenario de Construcción ............................................................................................................................ 24_

_3.6.3_ _Material Particulado Respirable (MP10) y Fino (MP2,5) Escenario de Operación.......................... 25_
_3.6.4_ _Gases, Dióxido de Nitrógeno (NO2), Dióxido de Azufre (SO2) y Monóxido de Carbono (CO)_
_Escenario de Operación................................................................................................................................. 25_

3.7 R ESUMEN DE R ESULTADOS Y C ONCLUSIONES ...................................................................................................... 26

**ÍNDICE DE TABLAS**

T ABLA 1. R ESUMEN E STIMACIÓN DE E MISIONES, E TAPA DE C ONSTRUCCIÓN Y O PERACIÓN .......................................................... 6

T ABLA 2 N ORMAS DE C ALIDAD DEL A IRE C ONSIDERADAS EN EL E STUDIO . ................................................................................. 7

T ABLA 3 V ALORES DE T EMPERATURA WRF. ..................................................................................................................... 10

T ABLA 4: T ASA DE E MISIÓN C ONSIDERADAS - F ASE DE C ONSTRUCCIÓN . ................................................................................ 16

T ABLA 5: T ASA DE E MISIÓN C ONSIDERADAS - F ASE DE O PERACIÓN . ..................................................................................... 16

T ABLA 6: C OORDENADAS DE LOS RECEPTORES ................................................................................................................... 17

T ABLA 7 D ETALLE A RCHIVO WRF ................................................................................................................................... 19

T ABLA 8: A PORTES DE M ATERIAL P ARTICULADO DE LA F ASE DE C ONSTRUCCIÓN DEL P ROYECTO ( μG /N M 3) .................................. 22
T ABLA 9: A PORTES DE G ASES DE LA F ASE DE C ONSTRUCCIÓN DEL P ROYECTO ( μG /N M 3) .......................................................... 22
T ABLA 10: A PORTES DE MATERIAL PARTICULADO DE LA F ASE DE O PERACIÓN DEL P ROYECTO ( μG /N M 3) ...................................... 23
T ABLA 11: A PORTES DE GASES DE LA F ASE DE O PERACIÓN DEL P ROYECTO ( μG /N M 3) .............................................................. 23

Anexo 2-13 - Modelación de emisiones atmosféricas i

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**ÍNDICE DE FIGURAS**

F IGURA 1.U BICACIÓN DEL P ROYECTO A NIVEL REGIONAL ....................................................................................................... 4

F IGURA 2. U BICACIÓN L OCAL DEL P ROYECTO . ..................................................................................................................... 5

F IGURA 3 R EPRESENTACIÓN G RÁFICA DEL M ODELO T IPO P UFF Y DE P LUMA . ............................................................................ 9

F IGURA 4 C ICLO D IARIO T EMPERATURA, WRF. ................................................................................................................. 10

F IGURA 5 C ICLO E STACIONAL T EMPERATURA, WRF. .......................................................................................................... 11

F IGURA 6 R OSAS DE V IENTO P ROMEDIO P ERIODO, WRF. ................................................................................................... 12

F IGURA 7 R OSAS DE V IENTO SEGÚN P ERIODO DEL DÍA, WRF. .............................................................................................. 13

F IGURA 8 C ICLO D IARIO V ELOCIDAD DEL V IENTO, WRF. ..................................................................................................... 14

F IGURA 9 C ICLO E STACIONAL V ELOCIDAD DEL V IENTO, WRF. .............................................................................................. 14

F IGURA 10 U BICACIÓN DE R ECEPTORES . .......................................................................................................................... 18

F IGURA 11. D OMINIO DE M ODELACIÓN . ......................................................................................................................... 19

F IGURA 12 T OPOGRAFÍAS DE LA Z ONA . ........................................................................................................................... 20

F IGURA 13.I SOCONCENTRACIONES P ROMEDIO A NUAL MP10 ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN ................................... 28
F IGURA 14.I SOCONCENTRACIONES P ERCENTIL 98 24 H ORAS MP10 ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN .......................... 29
F IGURA 15.I SOCONCENTRACIONES P ROMEDIO A NUAL MP2,5 ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN .................................. 30
F IGURA 16.I SOCONCENTRACIONES P ERCENTIL 98 24 H ORAS MP2,5 ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN ......................... 31
F IGURA 17. I SOCONCENTRACIONES P ERCENTIL 99 1 H ORA NO2 ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN ............................... 32
F IGURA 18. I SOCONCENTRACIONES A NUAL NO2 ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN ..................................................... 33
F IGURA 19. I SOCONCENTRACIONES P ERCENTIL 99 1 H ORA CO ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN .................................. 34
F IGURA 20. I SOCONCENTRACIONES P ERCENTIL 99 8 H ORAS CO ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN ................................ 35
F IGURA 21. I SOCONCENTRACIONES A NUAL SO2 ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN ..................................................... 36
F IGURA 22. I SOCONCENTRACIONES P99 24 HORAS SO2 ( μG / M 3N) E SCENARIO DE C ONSTRUCCIÓN .......................................... 37
F IGURA 23.I SOCONCENTRACIONES P ROMEDIO A NUAL MP10 ( μG / M 3N) E SCENARIO DE O PERACIÓN ......................................... 38
F IGURA 24.I SOCONCENTRACIONES P ERCENTIL 98 24 H ORAS MP10 ( μG / M 3N) E SCENARIO DE O PERACIÓN ................................ 39
F IGURA 25.I SOCONCENTRACIONES P ROMEDIO A NUAL MP2,5 ( μG / M 3N) E SCENARIO DE O PERACIÓN ........................................ 40
F IGURA 26.I SOCONCENTRACIONES P ERCENTIL 98 24 H ORAS MP2,5 ( μG / M 3N) E SCENARIO DE O PERACIÓN ............................... 41
F IGURA 27. I SOCONCENTRACIONES P ERCENTIL 99 1 H ORA NO2 ( μG / M 3N) E SCENARIO DE O PERACIÓN ..................................... 42
F IGURA 28. I SOCONCENTRACIONES A NUAL NO2 ( μG / M 3N) E SCENARIO DE O PERACIÓN .......................................................... 43
F IGURA 29. I SOCONCENTRACIONES P ERCENTIL 99 1 H ORA CO ( μG / M 3N) E SCENARIO DE O PERACIÓN ....................................... 44
F IGURA 30. I SOCONCENTRACIONES P ERCENTIL 99 8 H ORAS CO ( μG / M 3N) E SCENARIO DE O PERACIÓN ...................................... 45
F IGURA 31. I SOCONCENTRACIONES A NUAL SO2 ( μG / M 3N) E SCENARIO DE O PERACIÓN ........................................................... 46
F IGURA 32. I SOCONCENTRACIONES P99 24 HORAS SO2 ( μG / M 3N) E SCENARIO DE O PERACIÓN ................................................ 47

Anexo 2-13 - Modelación de emisiones atmosféricas ii

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**1** **INTRODUCCIÓN**

En este anexo se presenta la modelación de emisiones atmosféricas de los contaminantes: material
particulado respirable (MP10) y fino (MP2,5), y gases de combustión (CO, NOx, SO2) para las Etapas de
Construcción y Operación del Proyecto “PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO
CAMANCHACA”, en adelante “el Proyecto”.

A partir del análisis de la descripción del Proyecto, se ha podido identificar que las actividades que
generan emisiones de MP10, MP2,5 y gases de combustión a la atmósfera que se presentan durante la
Fase de Construcción, producto de los trabajos asociados a la construcción de las obras las que
consideran actividades como excavaciones, compactación, transferencia de material, tránsito de
vehículos por caminos pavimentados, combustión generada por la operación de la maquinaria,
combustión de la operación de vehículos y el uso de grupo electrógeno. Por su parte durante la Fase de
Operación del Proyecto se considera que la generación de emisiones viene dada por el tránsito de
vehículos por caminos pavimentados, la combustión los motores de los vehículos, el uso de grupos
generadores y la operación de calderas. Finalmente no se contempla fase de cierre del Proyecto, una vez
cumplida la vida útil del Proyecto, dado los mejoramientos tecnológicos que pueden surgir en la vida útil
del Proyecto.

La estimación de emisiones del Proyecto se realizó aplicando los factores de emisión y fórmulas
propuestas por la Agencia de Protección Ambiental de los EE.UU. en el documento “AP-42 5th Edición”,
complementando esta información con el Informe Final “Servicio de Recopilación y Sistematización de
Factores de Emisión al Aire para el Servicio de Evaluación Ambiental” (BS Consultores, Mayo 2015),
además con el documento indicado por SEREMI de Medio Ambiente Región Metropolitana en el
documento “Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios” (Enero,
2012) y del mismo documento generado por CONAMA (2008), los cuales han sido utilizados como
referencia técnica para el cálculo de las emisiones.

La Figura 1 muestra la ubicación del Proyecto a nivel regional, mientras la Figura 2 muestra la
localización del proyecto a escala local.

Anexo 2-13- Modelación de emisiones atmosféricas 3

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**Figura 1.Ubicación del Proyecto a nivel regional**

Anexo 2-13- Modelación de emisiones atmosféricas 4

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**Figura 2. Ubicación Local del Proyecto.**

Anexo 2-13- Modelación de emisiones atmosféricas 5

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**2** **RESUMEN DE ESTIMACIÓN DE EMISIONES**

La estimación de emisiones del Proyecto se realizó aplicando los factores de emisión y fórmulas
propuestas por la Agencia de Protección Ambiental de los EE.UU. en el documento “AP-42 5th Edición”,
complementando esta información con la indicada por SEREMI de Medio Ambiente Región
Metropolitana en el documento “Guía para la Estimación de Emisiones Atmosféricas de Proyectos
Inmobiliarios” (Enero 2012) y en el Informe Final del “Servicio de recopilación y sistematización de
factores de emisión al aire para el Servicio de Evaluación Ambiental” (BS Consultores, Mayo 2015), los
que han sido utilizados como una referencia técnica para el cálculo de las emisiones. En el Anexo 2-1 se
presenta la estimación de emisiones correspondiente a la Fase de Construcción y Operación del

Proyecto.

A continuación en la Tabla 1 muestra el resumen de las emisiones de material particulado de tamaño
respirable (MP10), fino (MP2,5), óxidos de nitrógeno (NOx), monóxido de carbono (CO), óxidos de azufre
(SOx) e hidrocarburos/compuestos orgánicos volátiles (HC/COV). Las emisiones se presentan de acuerdo
al cronograma para los dos años que demora la Etapa de Construcción y un año de Operación estándar.

**Tabla 1. Resumen Estimación de Emisiones, Etapa de Construcción y Operación**

|Fase del Proyecto|Parámetros|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Fase del Proyecto**|**MP10**|**MP2,5**|**NOx**|**CO**|**SO2**|**HC/COV**|
|Fase de Construcción Año 1|2,0893|1,1591|10,5595|2,6352|0,8817|0,1838|
|Fase de Construcción Año 2|0,9656|0,3939|3,4218|0,7693|0,0440|0,1827|
|Fase de Operación|11,7448|8,3197|95,4463|15,2579|166,6972|0,268|

En virtud de los resultados, se puede indicar que el Proyecto generará emisiones atmosféricas que
tendrán un carácter temporal para la etapa de construcción de las obras las que consideran actividades
como excavaciones, compactación, transferencia de material, tránsito de vehículos por caminos
pavimentados, combustión generada por la operación de la maquinaria, combustión de la operación de
vehículos y el uso de grupos electrógenos. Por su parte durante la Fase de Operación, tendrá un carácter
permanente cuyas emisiones generadas están dadas por el tránsito de vehículos por caminos
pavimentados, la combustión los motores de los vehículos, el uso de grupos generadores y la operación
de calderas. El detalle de estos cálculos se puede observar en el Anexo 2-1 Memoria de Cálculo de

emisiones atmosféricas.

En cuanto a la Etapa de Cierre esta no considera emisiones ya que el Proyecto tiene características de
operación indefinida en el tiempo.

En el punto 3.4.1 se presentan las condiciones para la distribución de las emisiones son las siguientes:

Anexo 2-13- Modelación de emisiones atmosféricas 6

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**3** **MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES**

**3.1** **M** **ARCO** **L** **EGAL**

La siguiente modelación determinará el efecto en los receptores sensibles del Proyecto, producto de las
emisiones de Material Particulado Respirable (MP10), Fino (MP2,5) y gases generadas por las
actividades asociadas a la fase de construcción y operación del Proyecto.

En el contexto legal, existen normas primarias asociadas a los contaminantes de las emisiones
atmosféricas generadas en el Proyecto. Los estadísticos a evaluar se presentan en la Tabla 2 :

**Tabla 2 Normas de Calidad del Aire Consideradas en el Estudio.**

|Parámetro|Tipo de<br>Norma|Indicador|Límite Máximo<br>Permitido (μg/m3N)|Referencia|
|---|---|---|---|---|
|**MP10**|Primaria|Promedio Anual|50 (μg/m3N)|Decreto Supremo N°<br>59/1998 del<br>MINSEGPRES|
|**MP10**|Primaria|Percentil 98 24 Horas|150 (μg/m3N)|150 (μg/m3N)|
|**MP2,5**|Primaria|Promedio Anual|20 (μg/m3N)|Decreto Supremo N°<br>12/2011 del<br>MINSEGPRES|
|**MP2,5**|Primaria|Percentil 98 24 Horas|50 (μg/m3N)|50 (μg/m3N)|
|**NO2**|Primaria|Promedio Anual|100 (μg/m3N)|Decreto Supremo N°<br>114/2002 del<br>MINSEGPRES|
|**NO2**|Primaria|Percentil 99 Máximos diarios concentración<br>de 1 Hora|400 (μg/m3N)|400 (μg/m3N)|
|**SO2**|Primaria|Promedio Anual|80 (μg/m3N)|Decreto Supremo N°<br>113/2002 del<br>MINSEGPRES|
|**SO2**|Primaria|Percentil 99 24 Horas|250 (μg/m3N)|250 (μg/m3N)|
|**CO**|Primaria|Percentil 99 Máximos diarios concentración<br>de 1 Hora|30000 (μg/m3N)|Decreto Supremo N°<br>115/2002 del<br>MINSEGPRES|
|**CO**|Primaria|Percentil 99 Máximos diarios concentración<br>de 8 Horas|10000 (μg/m3N)|10000 (μg/m3N)|

Anexo 2-13- Modelación de emisiones atmosféricas 7

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**3.2** **B** **ASE** **T** **EÓRICA DEL** **M** **ODELO** **U** **TILIZADO**

El modelo utilizado para determinar el efecto que tendrán las emisiones de Material Particulado
Respirable (MP-10), Fino (MP-2,5) y los gases (NO 2, SO 2 y CO) generadas durante la Fase de Construcción
y Operación, corresponde al sistema de modelación “WRF-CALPUFF”.

El sistema de modelación incluye tres componentes principales: WRF, CALPUFF y CALPOST, además de
una larga selección de preprocesadores diseñados para incluir en el modelo datos meteorológicos y
geofísicos.

WRF es un sistema de predicción numérico de mesoescala no hidrostático (considera los movimientos
verticales), usado con fines de pronóstico operacional y en investigación de la atmósfera. Los principales
componentes de este modelo son las fuentes externas de datos, como son los datos de entrada y la
información geográfica, el sistema de pre-procesamiento, el modelo WRF-ARW y los sistemas de postprocesamiento.
CALPUFF es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario capaz de modelar el
transporte y dispersión de contaminantes sobre la base entregada por el Servicio Evaluación Ambiental
(SEA). Los modelos tipo “puff” representan una pluma de contaminantes continuo como un número
discreto de paquetes de material contaminante. El modelo evalúa la contribución de un “puff” en la
concentración atmosférica de un receptor en un instante determinado, para luego permitir que el puff
se mueva, evolucione en tamaño, fuerza, etc., hasta la próxima itineración. Luego, la concentración total
en un receptor resultará de la sumatoria de las contribuciones de todos los “puff”. La ecuación básica
del modelo se muestra a continuación:

Donde:

C: Concentración (g/m [3] )
Q: Masa del contaminante en el “puff” (g)
σx: Coeficiente de dispersión en dirección del viento (m)
σy: Coeficiente de dispersión en dirección perpendicular al viento (m)
σz: Coeficiente de dispersión vertical (m)
da: Distancia desde el centro del “puff” hacia el receptor en el eje de la dirección del viento (m)
dc: Distancia desde el centro del “puff” hacia el receptor en el eje perpendicular a la dirección
del viento (m)
g: Altura de la ecuación gaussiana (m)
H: Altura efectiva del “puff” (m)
h: Altura de la capa de mezcla (m)

A diferencia de un modelo de pluma, los modelos de tipo “puff” consideran las emisiones (de los puff)
independientes de su fuente de emisión permitiendo que los “puff” respondan a la meteorología en la

Anexo 2-13- Modelación de emisiones atmosféricas 8

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

que se encuentra inmerso en cada instante. Lo anterior se representa esquemáticamente en la siguiente
Figura 3.

**Figura 3 Representación Gráfica del Modelo Tipo Puff y de Pluma.**

_Fuente: Lakes Environmental._

Finalmente CALPOST procesa las salidas de CALPUFF creando los archivos con las tabulaciones
necesarias para la evaluación de los resultados según los estadísticos establecidos en las normas de

calidad del aire.

**3.3** **A** **NÁLISIS** **M** **ETEOROLÓGICO**

A continuación se presenta la caracterización meteorológica del área de estudio, la cual consideró la
descripción de vientos y temperatura. De esta forma, se representan los ciclos diarios y estacionales de

las variables anteriormente mencionadas.

Cabe mencionar que los datos considerados corresponden a los extraídos del Modelo de Pronóstico
Meteorológico WRF para el año 2014 de un punto central en las obras del Proyecto de coordenadas
381.224 E y 7.766.491 N.

Anexo 2-13- Modelación de emisiones atmosféricas 9

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**a)** **Temperatura**

En la siguiente sección se presentan de manera gráfica los ciclos diarios y estacionales de la variable

temperatura.

Se observa el ciclo de la temperatura típico de la zona norte y específicamente respecto a sectores
costeros, observando baja variabilidad interanual y diaria. La temperatura promedio anual alcanza los
17°C, además la mínima mensual no baja de los 10°C, mientras que la máxima no sobrepasa los 25°C.

**Tabla 3 Valores de Temperatura WRF.**

|Mes|2014|Col3|Col4|
|---|---|---|---|
|**Mes**|**T° Min**|**T° Max**|**T° Promedio**|
|Enero|18,1|24,6|21,0|
|Febrero|17,3|22,8|19,9|
|Marzo|16,4|23,1|19,5|
|Abril|14,9|22,7|17,9|
|Mayo|14,7|24,7|16,9|
|Junio|13,1|20,5|15,5|
|Julio|11,8|22,1|14,4|
|Agosto|11,5|19,4|14,5|
|Septiembre|12,3|19,9|14,5|
|Octubre|12,9|20,8|15,7|
|Noviembre|14,3|20,1|16,6|
|Diciembre|15,2|20,7|17,3|

La Figura 4 muestra el ciclo diario de la temperatura donde se observa la baja variabilidad diaria,
mientras la Figura 5 muestra el ciclo estacional de ésta con una leve disminución de las temperaturas
donde los mínimos se registran en los meses de julio y agosto.

**Figura 4 Ciclo Diario Temperatura, WRF** .

Anexo 2-13- Modelación de emisiones atmosféricas 10

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**Figura 5 Ciclo Estacional Temperatura, WRF** .

**a)** **Régimen de Viento**

A continuación se presentan las rosas de viento promedio y según periodo del día. Como promedio
anual, los vientos presentan una componente predominante del sur-suroeste (SSO) con velocidades que
alcanzan el rango de los 5,7 -8,8 m/s. Otra componente predominante pero con menor frecuencia es
suroeste (SO) donde el rango de velocidad predominante es 2,1-4,5 m/s.

Se observa que los vientos predominantes durante todo el día corresponden a vientos del noroeste
(SSO) con intensidades que disminuyen a partir de las 18:00 horas donde el rango predominante es 2,14,5 m/s condición que se presenta hasta alrededor de las 05:00 horas. Por otra parte, en las primeras
horas del día la intensidad de los vientos comienza su ascenso alcanzando velocidades de 8,8 m/s.

La Figura 8 muestra el ciclo diario de la velocidad del viento, donde se observa el aumento de las
intensidades a partir de las 06:00 horas, condición que se mantiene hasta las 13:00 horas.

En cuanto al ciclo estacional de la velocidad de los vientos, presenta una leve variabilidad, donde en los
meses de julio y agosto se observan los mínimos valores de velocidad promedio.

Anexo 2-13- Modelación de emisiones atmosféricas 11

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**Figura 6 Rosas de Viento Promedio Periodo, WRF** .

Anexo 2-13- Modelación de emisiones atmosféricas 12

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**Figura 7 Rosas de Viento según Periodo del día, WRF** .

|Periodo 00-05 hrs - Año 2014|Periodo 06-11 hrs - Año 2014|
|---|---|
|||
|**Periodo 12-17 hrs - Año 2014**|**Periodo 18-23 hrs - Año 2014**|
|||

Anexo 2-13- Modelación de emisiones atmosféricas 13

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**Figura 8 Ciclo Diario Velocidad del Viento, WRF** .

**Figura 9 Ciclo Estacional Velocidad del Viento, WRF** .

Anexo 2-13- Modelación de emisiones atmosféricas 14

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**3.4** **C** **ONSTRUCCIÓN DE** **E** **SCENARIOS**

El desarrollo del modelo involucra la construcción de un escenario meteorológico, geofísico, de
emisiones y receptores sensibles sobre el dominio de la modelación. Para elaborar los escenarios a
modelar se requiere de datos de entrada mínimos los cuales fueron recopilados y procesados desde
estaciones de monitoreo e imágenes satelitales a través de una modelación de pronóstico mediante
WRF. El detalle de los datos recopilados para la confección de cada escenario se presenta a

continuación.

- Escenario de Emisiones y Receptores

 Ubicación y características de las fuentes emisoras, incluyendo la tasa de emisión
 Ubicación de los receptores sensibles en el área de influencia del Proyecto

- Escenario Meteorológico

 Información meteorológica del Modelo de Pronostico WRF:


Temperatura ambiente

 Velocidad del viento

 Dirección del viento

- Escenario Geofísico

 Topografía del área de modelación

A continuación se presentan los escenarios construidos para la modelación.

_**3.4.1**_ _**Escenario de Emisiones**_

Se ha considerado para la modelación de dispersión de contaminantes los escenarios de construcción y
operación del Proyecto. En cuyo caso se han considerado todas las emisiones descritas en el capítulo 2

de este informe.

La tasa de emisión y característica de cada una de las fuentes consideradas del Proyecto, se han
estimado a partir de los resultados del cálculo de emisiones indicado en la Tabla 1.

El detalle de los datos ingresados al modelo se encuentra en los archivos de entrada adjuntados como
respaldo digital al presente documento. A continuación en la Tabla 4 se resumen las tasas de emisión
asociados a la construcción de las obras las que consideran actividades como excavaciones,
compactación, transferencia de material, tránsito de vehículos por caminos pavimentados, combustión
generada por la operación de la maquinaria, combustión de la operación de vehículos y el uso de grupo
electrógeno y que corresponden a las actividades generadas en el año 1.

Por su parte durante la Fase de Operación del Proyecto se considera que la generación de emisiones
está dada por el tránsito de vehículos por caminos pavimentados, la combustión los motores de los
vehículos, el uso de grupos generadores y la operación de calderas.

Anexo 2-13- Modelación de emisiones atmosféricas 15

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

La Tabla 4 muestra las tasa de emisión de las fuentes consideradas en el escenario de Construcción,
mientras la Tabla 5 lo hace para las fuentes consideradas en el escenario de Operación.

**Tabla 4: Tasa de Emisión Consideradas - Fase de Construcción.**

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA| La Tabla 4 muestra las tasa de emisión de las fuentes consideradas en el escenario de Construcción, mientras la Tabla 5 lo hace para las fuentes consideradas en el escenario de Operación. -->

**Tabla 4: Tasa de Emisión Consideradas - Fase de Construcción.****

| Tipo de Fuente* | Descripción | Tasas de Emisión* | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Tipo de Fuente*** | **Descripción** | **PM10** | **PM2.5** | **NOX** | **CO** | **SO2** |
| **Línea Areal** | Camino Alto Hospicio | 5,09E-06 | 1,32E-06 | 4,59E-06 | 1,17E-06 | 1,79E-08 |
| **Línea Areal** | Camino Iquique | 2,50E-06 | 6,38E-07 | 1,62E-06 | 4,22E-07 | 6,43E-09 |
| **Areal** | Área de Proyecto | 5,10E-05 | 4,48E-05 | 4,56E-04 | 1,19E-04 | 0,00E+00 |
| **Puntual** | Generador de Construcción | 1,61E-01 | 1,61E-01 | 2,26E+00 | 4,87E-01 | 1,50E-01 |

<!-- Estadísticas: 5 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 5: Tasa de Emisión Consideradas - Fase de Operación.** |Tasas de Emisión*<br>Tipo de Fuente* Descripción<br>PM10 PM2.5 NOX CO SO2|Col2|Col3|Col4|Col5|Col6|Col7| |---|---|---|---|---|---|---| -->
<!-- FIN TABLA 4 -->


|Tipo de Fuente*|Descripción|Tasas de Emisión*|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Tipo de Fuente***|**Descripción**|**PM10**|**PM2.5**|**NOX**|**CO**|**SO2**|
|**Línea Areal**|Camino Alto Hospicio|5,09E-06|1,32E-06|4,59E-06|1,17E-06|1,79E-08|
|**Línea Areal**|Camino Iquique|2,50E-06|6,38E-07|1,62E-06|4,22E-07|6,43E-09|
|**Areal**|Área de Proyecto|5,10E-05|4,48E-05|4,56E-04|1,19E-04|0,00E+00|
|**Puntual**|Generador de Construcción|1,61E-01|1,61E-01|2,26E+00|4,87E-01|1,50E-01|

**Tabla 5: Tasa de Emisión Consideradas - Fase de Operación.**

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**Línea Areal**|Camino Alto Hospicio|5,09E-06|1,32E-06|4,59E-06|1,17E-06|1,79E-08| |**Línea Areal**|Camino Iquique|2,50E-06|6,38E-07|1,62E-06|4,22E-07|6,43E-09| |**Areal**|Área de Proyecto|5,10E-05|4,48E-05|4,56E-04|1,19E-04|0,00E+00| |**Puntual**|Generador de Construcción|1,61E-01|1,61E-01|2,26E+00|4,87E-01|1,50E-01| -->

**Tabla 5: Tasa de Emisión Consideradas - Fase de Operación.****

| Tasas de Emisión*<br>Tipo de Fuente* Descripción<br>PM10 PM2.5 NOX CO SO2 | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Tipo de Fuente***<br>**Descripción**<br>**Tasas de Emisión***<br>**PM10**<br>**PM2.5**<br>**NOX**<br>**CO**<br>**SO2** | **Tipo de Fuente***<br>**Descripción**<br>**Tasas de Emisión***<br>**PM10**<br>**PM2.5**<br>**NOX**<br>**CO**<br>**SO2** | **Tipo de Fuente***<br>**Descripción**<br>**Tasas de Emisión***<br>**PM10**<br>**PM2.5**<br>**NOX**<br>**CO**<br>**SO2** | **PM2.5** | **NOX** | **CO** | **SO2** |
| **Puntual** | Caldera 1 | 2,0643 | 1,5042 | 10,8174 | 0,9761 | 37,8289 |
| **Puntual** | Caldera 2 | 2,0644 | 1,5043 | 10,818 | 0,9762 | 37,8308 |
| **Puntual** | Caldera 3 | 2,065 | 1,5047 | 10,8216 | 0,9765 | 37,8434 |
| **Puntual** | Caldera 4 | 0,9021 | 0,6573 | 4,7268 | 0,4266 | 16,5299 |
| **Puntual** | Caldera 5 | 0,9034 | 0,6582 | 4,7336 | 0,4272 | 16,5535 |
| **Puntual** | Grupo Electrógeno 1 | 0,2083 | 0,2083 | 7,1376 | 1,6329 | 0,0121 |
| **Puntual** | Grupo Electrógeno 2 | 0,2545 | 0,2545 | 8,7238 | 1,9957 | 0,0147 |
| **Puntual** | Grupo Electrógeno 3 | 0,2083 | 0,2083 | 7,1376 | 1,6329 | 0,012 |
| **Puntual** | Grupo Electrógeno 4 | 0,2314 | 0,2314 | 7,9307 | 1,8143 | 0,0134 |
| **Puntual** | Grupo Electrógeno 5 | 0,2314 | 0,2314 | 7,9307 | 1,8143 | 0,0134 |
| **Puntual** | Grupo Electrógeno 6 | 0,2314 | 0,2314 | 7,9307 | 1,8143 | 0,0134 |
| **Areal** | Camino Pavimentado | 6,76E-06 | 1,73E-06 | 5,31E-06 | 1,33E-06 | 1,89E-08 |

<!-- Estadísticas: 13 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- (*) Las fuentes tipo puntual se ingresan al modelo con una tasa en unidad de (kg/h), mientras que las fuentes tipo Areales y Lineales-Areales se ingresan al modelo con una tasa en kg/(m2-h) distribuida en el área de la fuente considerada. Anexo 2-13- Modelación de emisiones atmosféricas 16 -->
<!-- FIN TABLA 5 -->


|Tasas de Emisión*<br>Tipo de Fuente* Descripción<br>PM10 PM2.5 NOX CO SO2|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Tipo de Fuente***<br>**Descripción**<br>**Tasas de Emisión***<br>**PM10**<br>**PM2.5**<br>**NOX**<br>**CO**<br>**SO2**|**Tipo de Fuente***<br>**Descripción**<br>**Tasas de Emisión***<br>**PM10**<br>**PM2.5**<br>**NOX**<br>**CO**<br>**SO2**|**Tipo de Fuente***<br>**Descripción**<br>**Tasas de Emisión***<br>**PM10**<br>**PM2.5**<br>**NOX**<br>**CO**<br>**SO2**|**PM2.5**|**NOX**|**CO**|**SO2**|
|**Puntual**|Caldera 1|2,0643|1,5042|10,8174|0,9761|37,8289|
|**Puntual**|Caldera 2|2,0644|1,5043|10,818|0,9762|37,8308|
|**Puntual**|Caldera 3|2,065|1,5047|10,8216|0,9765|37,8434|
|**Puntual**|Caldera 4|0,9021|0,6573|4,7268|0,4266|16,5299|
|**Puntual**|Caldera 5|0,9034|0,6582|4,7336|0,4272|16,5535|
|**Puntual**|Grupo Electrógeno 1|0,2083|0,2083|7,1376|1,6329|0,0121|
|**Puntual**|Grupo Electrógeno 2|0,2545|0,2545|8,7238|1,9957|0,0147|
|**Puntual**|Grupo Electrógeno 3|0,2083|0,2083|7,1376|1,6329|0,012|
|**Puntual**|Grupo Electrógeno 4|0,2314|0,2314|7,9307|1,8143|0,0134|
|**Puntual**|Grupo Electrógeno 5|0,2314|0,2314|7,9307|1,8143|0,0134|
|**Puntual**|Grupo Electrógeno 6|0,2314|0,2314|7,9307|1,8143|0,0134|
|**Areal**|Camino Pavimentado|6,76E-06|1,73E-06|5,31E-06|1,33E-06|1,89E-08|

(*) Las fuentes tipo puntual se ingresan al modelo con una tasa en unidad de (kg/h), mientras que las fuentes tipo Areales y Lineales-Areales se
ingresan al modelo con una tasa en kg/(m2-h) distribuida en el área de la fuente considerada.

Anexo 2-13- Modelación de emisiones atmosféricas 16

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

_**3.4.2**_ _**Escenario de Receptores**_

Se incluyen 5 receptores puntuales los que se encuentran entre 1500 y 3000 metros de la faena de
construcción y operación del Proyecto.

A continuación en la Tabla 6 se presenta con los puntos receptores considerados en la modelación.

**Tabla 6: Coordenadas de los receptores**

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Se incluyen 5 receptores puntuales los que se encuentran entre 1500 y 3000 metros de la faena de construcción y operación del Proyecto. A continuación en la Tabla 6 se presenta con los puntos receptores considerados en la modelación. -->

**Tabla 6: Coordenadas de los receptores****

| Nombre | Descripción | Coordenadas UTM (Huso 18. Datum WGS84) | Col4 |
| --- | --- | --- | --- |
| **Nombre** | **Descripción** | **Este (m)** | **Norte (m)** |
| **R1** | **Gobernación Marítima** | 379,515 | 7,764,708 |
| **R2** | **Intendencia Iquique** | 379,294 | 7,763,937 |
| **R3** | **Clínica Tarapacá** | 380,115 | 7,763,501 |
| **R4** | **Hospital Regional** | 381,090 | 7,764,366 |
| **R5** | **Mall Comercial Zofri** | 381,601 | 7,764,996 |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia_ Además, para generar los mapas de isoconcentraciones, se estableció una grilla de receptores que abarca un área de 17 x 25 km, equiespaciados cada 1 km. para el Escenario de Construcción y una grilla -->
<!-- FIN TABLA 6 -->


|Nombre|Descripción|Coordenadas UTM (Huso 18. Datum WGS84)|Col4|
|---|---|---|---|
|**Nombre**|**Descripción**|**Este (m)**|**Norte (m)**|
|**R1**|**Gobernación Marítima**|379,515|7,764,708|
|**R2**|**Intendencia Iquique**|379,294|7,763,937|
|**R3**|**Clínica Tarapacá**|380,115|7,763,501|
|**R4**|**Hospital Regional**|381,090|7,764,366|
|**R5**|**Mall Comercial Zofri**|381,601|7,764,996|

_Fuente: Elaboración propia_

Además, para generar los mapas de isoconcentraciones, se estableció una grilla de receptores que
abarca un área de 17 x 25 km, equiespaciados cada 1 km. para el Escenario de Construcción y una grilla
de 25 x 36 km para el Escenario de Operación, en donde se encuentra contenida el área del Proyecto, el
área de influencia directa del mismo y toda la información de interés. La Figura 10 presenta la
ubicación de los receptores mencionados.

Anexo 2-13- Modelación de emisiones atmosféricas 17

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 10 Ubicación de Receptores** .

**Proyecto**

_Fuente: Elaboración propia a partir de WRF-Calpuff y Google Earth._

Anexo 2-13- Memoria de Cálculo de Estimación de Emisiones Atmosféricas 18

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

_**3.4.3**_ _**Escenario Meteorológico**_

El escenario meteorológico se construyó a partir de la información meteorológica generada por el
modelo _WRF_, archivo proporcionado por el Titular. La Tabla 7 muestra la configuración utilizada por el
modelo meteorológico.

El dominio del área corresponde a una grilla de 62 x 62 km, teniendo origen en las coordenadas
presentadas en la siguiente Tabla 7 e ilustrada en la
Figura 11.

**Tabla 7 Detalle Archivo WRF**

|Proyección Cartográfica|Cónica conforme de Lambert (LCC)|
|---|---|
|**Período**|1 Enero al 31 de Diciembre 2014|
|**Origen**|Latitud: 20.186 ° ° S<br>Longitud: 70.137 ° W|
|**Datum**|NWS-83|
|**Grilla**|1 km|

**Figura 11. Dominio de Modelación.**

_Fuente: Elaboración propia a partir de WRF-Calpuff y Google Earth._

Anexo 2-13- Memoria de Cálculo de Estimación de Emisiones Atmosféricas

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

Las variables meteorológicas utilizadas en la modelación son aquellas generadas por _WR_ F y
corresponden a temperatura, velocidad y dirección de vientos, radiación, humedad entre otras.

_**3.4.4**_ _**Escenario Geofísico**_

La topografía de la zona se obtuvo de datos de elevación recopilados por satélite con una resolución de
tres arcos-segundo, lo que significa 1/1.200aba parte de un grado de latitud/longitud o bien 90 metros.
A continuación la Figura 12 presenta gráficamente la topografía del área.

**Figura 12 Topografías de la Zona.**

Anexo 2-13- Modelación de emisiones atmosféricas 20

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**3.5** **R** **ESULTADOS DE LA** **I** **MPLEMENTACIÓN DEL** **M** **ODELO**

A continuación se presentan los resultados de la implementación del modelo WRF-CALPUFF.

_**3.5.1**_ _**Implementación del Modelo de Dispersión CALPUFF**_

Utilizando CALPUFF, se modelaron las emisiones de MP10, MP2,5 y gases, sobre el dominio de
modelación establecido por la extensión en superficie del archivo WRF. La resolución con tamaño de
grilla de los receptores fue de 1000 x 1000 metros.

Para la aplicación de este modelo se consideró la meteorología WRF para el período entre el 1 de Enero
del 2014 al 31 de Diciembre de 2014. Luego, se obtuvieron las concentraciones de MP10, MP2,5 y gases
estimadas para cada una de las horas del periodo.

Finalmente se aplicó el módulo CALPOST para obtener los estadísticos establecidos en las normas de
calidad del aire presentadas en este documento. A continuación se presentan los resultados para la Fase
de Construcción y Operación del Proyecto en los receptores discretos evaluados.

Los resultados de la modelación para el escenario de Construcción se presentan en la Tabla 8 y Tabla 9,
mientras que los resultados para el escenario de Operación se presentan en la Tabla 10 y Tabla 11.

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**R2**|0,35|0,23%|0,10|0,19%|0,26|0,53%|0,07|0,36%| |**R3**|0,52|0,35%|0,13|0,27%|0,39|0,79%|0,10|0,50%| |**R4**|1,63|1,09%|0,33|0,67%|1,26|2,51%|0,25|1,25%| |**R5**|2,62|1,75%|0,54|1,08%|2,01|4,01%|0,41|2,03%| -->

**Tabla 11: Aportes de gases de la Fase de Operación del Proyecto (μg/Nm3)****

| Receptor | NO2 (μg/m3N) | Col3 | Col4 | Col5 | CO (μg/m3N) | Col7 | Col8 | Col9 | SO2 (μg/m3N) | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **P99 1 hora** | **% Norma** | **Anual** | **% Norma** | **P99 1 hora** | **% Norma** | **P99 8 horas** | **% Norma** | **P99 24**<br>**horas** | **% Norma** | **Anual** | **% Norma** |
| **R1** | 52,92 | 13,23% | 0,95 | 0,95% | 11,51 | 0,04% | 2,33 | 0,02% | 6,21 | 2,48% | 1,05 | 1,31% |
| **R2** | 32,82 | 8,20% | 0,78 | 0,78% | 6,45 | 0,02% | 1,43 | 0,01% | 5,30 | 2,12% | 0,90 | 1,12% |
| **R3** | 58,56 | 14,64% | 1,14 | 1,14% | 12,16 | 0,04% | 2,40 | 0,02% | 7,38 | 2,95% | 1,21 | 1,51% |
| **R4** | 175,75 | 43,94% | 3,05 | 3,05% | 31,14 | 0,10% | 7,30 | 0,07% | 26,25 | 10,50% | 3,24 | 4,04% |
| **R5** | 219,89 | 54,97% | 5,18 | 5,18% | 43,36 | 0,14% | 11,74 | 0,12% | 43,76 | 17,50% | 5,21 | 6,51% |

<!-- Estadísticas: 6 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Los mapas de isoconcentraciones asociados a cada uno de estos estadísticos se presentan en el APÉNDICE 1 de este documento [1.] 1 Los mapas de isoconcentraciones se elaboran en base a las concentraciones del estadístico representado en cada uno de los receptores que conforman la grilla los cuales se pueden registrar durante distintas horas del año. Por lo anterior, las figuras son una herramienta útil para la predicción de impactos pero no representan las concentraciones del -->
<!-- FIN TABLA 11 -->


Anexo 2-13- Modelación de emisiones atmosféricas 21

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Tabla 8: Aportes de Material Particulado de la Fase de Construcción del Proyecto (μg/Nm3)**

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3| |---|---|---| ||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA| -->

**Tabla 8: Aportes de Material Particulado de la Fase de Construcción del Proyecto (μg/Nm3)****

| Receptor | MP10 (μg/m3N) | Col3 | Col4 | Col5 | MP2.5 (μg/m3N) | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **P98 24 horas** | **% Norma** | **Anual** | **% Norma** | **P98 24 horas** | **% Norma** | **Anual** | **% Norma** |
| **R1** | 5,08E-02 | 0,03% | 1,42E-02 | 0,03% | 3,86E-02 | 0,08% | 8,95E-03 | 0,04% |
| **R2** | 4,05E-02 | 0,03% | 1,15E-02 | 0,02% | 2,72E-02 | 0,05% | 6,88E-03 | 0,03% |
| **R3** | 6,15E-02 | 0,04% | 1,74E-02 | 0,03% | 4,08E-02 | 0,08% | 1,02E-02 | 0,05% |
| **R4** | 4,00E-01 | 0,27% | 1,33E-01 | 0,27% | 1,69E-01 | 0,34% | 4,82E-02 | 0,24% |
| **R5** | 3,19E-01 | 0,21% | 8,88E-02 | 0,18% | 2,20E-01 | 0,44% | 4,81E-02 | 0,24% |

<!-- Estadísticas: 6 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 9: Aportes de Gases de la Fase de Construcción del Proyecto (μg/Nm3)** |Receptor|NO2 (μg/m3N)|Col3|Col4|Col5|CO (μg/m3N)|Col7|Col8|Col9|SO2 (μg/m3N)|Col11|Col12|Col13| |---|---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 8 -->


|Receptor|MP10 (μg/m3N)|Col3|Col4|Col5|MP2.5 (μg/m3N)|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Receptor**|**P98 24 horas**|**% Norma**|**Anual**|**% Norma**|**P98 24 horas**|**% Norma**|**Anual**|**% Norma**|
|**R1**|5,08E-02|0,03%|1,42E-02|0,03%|3,86E-02|0,08%|8,95E-03|0,04%|
|**R2**|4,05E-02|0,03%|1,15E-02|0,02%|2,72E-02|0,05%|6,88E-03|0,03%|
|**R3**|6,15E-02|0,04%|1,74E-02|0,03%|4,08E-02|0,08%|1,02E-02|0,05%|
|**R4**|4,00E-01|0,27%|1,33E-01|0,27%|1,69E-01|0,34%|4,82E-02|0,24%|
|**R5**|3,19E-01|0,21%|8,88E-02|0,18%|2,20E-01|0,44%|4,81E-02|0,24%|

**Tabla 9: Aportes de Gases de la Fase de Construcción del Proyecto (μg/Nm3)**

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**R2**|4,05E-02|0,03%|1,15E-02|0,02%|2,72E-02|0,05%|6,88E-03|0,03%| |**R3**|6,15E-02|0,04%|1,74E-02|0,03%|4,08E-02|0,08%|1,02E-02|0,05%| |**R4**|4,00E-01|0,27%|1,33E-01|0,27%|1,69E-01|0,34%|4,82E-02|0,24%| |**R5**|3,19E-01|0,21%|8,88E-02|0,18%|2,20E-01|0,44%|4,81E-02|0,24%| -->

**Tabla 9: Aportes de Gases de la Fase de Construcción del Proyecto (μg/Nm3)****

| Receptor | NO2 (μg/m3N) | Col3 | Col4 | Col5 | CO (μg/m3N) | Col7 | Col8 | Col9 | SO2 (μg/m3N) | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **P99 1 hora** | **% Norma** | **Anual** | **% Norma** | **P99 1 hora** | **% Norma** | **P99 8 horas** | **% Norma** | **P99 24 horas** | **% Norma** | **Anual** | **% Norma** |
| **R1** | 6,38E+00 | 1,59% | 7,88E-02 | 0,08% | 1,58E+00 | 0,01% | 2,81E-01 | 0,00% | 9,81E-03 | 0,00% | 1,83E-03 | 0,00% |
| **R2** | 3,26E+00 | 0,81% | 5,88E-02 | 0,06% | 8,73E-01 | 0,00% | 1,80E-01 | 0,00% | 7,57E-03 | 0,00% | 1,53E-03 | 0,00% |
| **R3** | 4,93E+00 | 1,23% | 8,68E-02 | 0,09% | 1,31E+00 | 0,00% | 3,17E-01 | 0,00% | 9,96E-03 | 0,00% | 2,05E-03 | 0,00% |
| **R4** | 1,66E+01 | 4,14% | 2,84E-01 | 0,28% | 4,19E+00 | 0,01% | 8,54E-01 | 0,01% | 3,56E-02 | 0,01% | 5,58E-03 | 0,01% |
| **R5** | 2,53E+01 | 6,33% | 4,20E-01 | 0,42% | 6,27E+00 | 0,02% | 1,31E+00 | 0,01% | 7,38E-02 | 0,03% | 1,12E-02 | 0,01% |

<!-- Estadísticas: 6 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Anexo 2-13- Modelación de emisiones atmosféricas 22 |Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3| |---|---|---| -->
<!-- FIN TABLA 9 -->


|Receptor|NO2 (μg/m3N)|Col3|Col4|Col5|CO (μg/m3N)|Col7|Col8|Col9|SO2 (μg/m3N)|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**P99 1 hora**|**% Norma**|**Anual**|**% Norma**|**P99 1 hora**|**% Norma**|**P99 8 horas**|**% Norma**|**P99 24 horas**|**% Norma**|**Anual**|**% Norma**|
|**R1**|6,38E+00|1,59%|7,88E-02|0,08%|1,58E+00|0,01%|2,81E-01|0,00%|9,81E-03|0,00%|1,83E-03|0,00%|
|**R2**|3,26E+00|0,81%|5,88E-02|0,06%|8,73E-01|0,00%|1,80E-01|0,00%|7,57E-03|0,00%|1,53E-03|0,00%|
|**R3**|4,93E+00|1,23%|8,68E-02|0,09%|1,31E+00|0,00%|3,17E-01|0,00%|9,96E-03|0,00%|2,05E-03|0,00%|
|**R4**|1,66E+01|4,14%|2,84E-01|0,28%|4,19E+00|0,01%|8,54E-01|0,01%|3,56E-02|0,01%|5,58E-03|0,01%|
|**R5**|2,53E+01|6,33%|4,20E-01|0,42%|6,27E+00|0,02%|1,31E+00|0,01%|7,38E-02|0,03%|1,12E-02|0,01%|

Anexo 2-13- Modelación de emisiones atmosféricas 22

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Tabla 10: Aportes de material particulado de la Fase de Operación del Proyecto (μg/Nm3)**

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3| |---|---|---| ||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA| -->

**Tabla 10: Aportes de material particulado de la Fase de Operación del Proyecto (μg/Nm3)****

| Receptor | MP10 (μg/m3N) | Col3 | Col4 | Col5 | MP2.5 (μg/m3N) | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **P98 24 horas** | **% Norma** | **Anual** | **% Norma** | **P98 24 horas** | **% Norma** | **Anual** | **% Norma** |
| **R1** | 0,41 | 0,27% | 0,11 | 0,23% | 0,32 | 0,63% | 0,08 | 0,42% |
| **R2** | 0,35 | 0,23% | 0,10 | 0,19% | 0,26 | 0,53% | 0,07 | 0,36% |
| **R3** | 0,52 | 0,35% | 0,13 | 0,27% | 0,39 | 0,79% | 0,10 | 0,50% |
| **R4** | 1,63 | 1,09% | 0,33 | 0,67% | 1,26 | 2,51% | 0,25 | 1,25% |
| **R5** | 2,62 | 1,75% | 0,54 | 1,08% | 2,01 | 4,01% | 0,41 | 2,03% |

<!-- Estadísticas: 6 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 11: Aportes de gases de la Fase de Operación del Proyecto (μg/Nm3)** |Receptor|NO2 (μg/m3N)|Col3|Col4|Col5|CO (μg/m3N)|Col7|Col8|Col9|SO2 (μg/m3N)|Col11|Col12|Col13| |---|---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 10 -->


|Receptor|MP10 (μg/m3N)|Col3|Col4|Col5|MP2.5 (μg/m3N)|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Receptor**|**P98 24 horas**|**% Norma**|**Anual**|**% Norma**|**P98 24 horas**|**% Norma**|**Anual**|**% Norma**|
|**R1**|0,41|0,27%|0,11|0,23%|0,32|0,63%|0,08|0,42%|
|**R2**|0,35|0,23%|0,10|0,19%|0,26|0,53%|0,07|0,36%|
|**R3**|0,52|0,35%|0,13|0,27%|0,39|0,79%|0,10|0,50%|
|**R4**|1,63|1,09%|0,33|0,67%|1,26|2,51%|0,25|1,25%|
|**R5**|2,62|1,75%|0,54|1,08%|2,01|4,01%|0,41|2,03%|

**Tabla 11: Aportes de gases de la Fase de Operación del Proyecto (μg/Nm3)**

|Receptor|NO2 (μg/m3N)|Col3|Col4|Col5|CO (μg/m3N)|Col7|Col8|Col9|SO2 (μg/m3N)|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**P99 1 hora**|**% Norma**|**Anual**|**% Norma**|**P99 1 hora**|**% Norma**|**P99 8 horas**|**% Norma**|**P99 24**<br>**horas**|**% Norma**|**Anual**|**% Norma**|
|**R1**|52,92|13,23%|0,95|0,95%|11,51|0,04%|2,33|0,02%|6,21|2,48%|1,05|1,31%|
|**R2**|32,82|8,20%|0,78|0,78%|6,45|0,02%|1,43|0,01%|5,30|2,12%|0,90|1,12%|
|**R3**|58,56|14,64%|1,14|1,14%|12,16|0,04%|2,40|0,02%|7,38|2,95%|1,21|1,51%|
|**R4**|175,75|43,94%|3,05|3,05%|31,14|0,10%|7,30|0,07%|26,25|10,50%|3,24|4,04%|
|**R5**|219,89|54,97%|5,18|5,18%|43,36|0,14%|11,74|0,12%|43,76|17,50%|5,21|6,51%|

Los mapas de isoconcentraciones asociados a cada uno de estos estadísticos se presentan en el APÉNDICE 1 de este documento [1.]

1 Los mapas de isoconcentraciones se elaboran en base a las concentraciones del estadístico representado en cada uno de los receptores que conforman la grilla los cuales se
pueden registrar durante distintas horas del año. Por lo anterior, las figuras son una herramienta útil para la predicción de impactos pero no representan las concentraciones del

sector en un determinado instante.

Anexo 2-13- Modelación de emisiones atmosféricas 23

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**3.6** **A** **NÁLISIS DE** **C** **UMPLIMIENTO** **N** **ORMATIVO VIGENTE DE** **C** **ALIDAD DEL** **A** **IRE**

Para verificar el cumplimiento de las normas de calidad del aire vigentes, se elaboró un análisis de los
efectos que genera el Proyecto sobre la calidad del aire de los sectores aledaños al Proyecto durante la
Fase de Construcción y Operación.

De acuerdo a esto, han sido incluidos 5 receptores puntuales en la modelación, los que corresponden a
edificios públicos y un centro comercial.

_**3.6.1**_ _**Material Particulado Respirable (MP10) y Fino (MP2,5) Escenario de Construcción**_

El análisis de cumplimiento de la normativa primaria de calidad del aire para MP10 para el escenario de
Construcción modelados no supera el 1% de la normativa para los criterios en 24 horas y anual.

A la vez en el caso del MP2,5 los valores modelados, tampoco superan el 1% de la normativa tanto para
el criterio en 24 horas y el anual.

El receptor con mayor aporte (menor al 1%) corresponde al Mall Zofri, receptor que cuenta con una
afluencia de población flotante no residencial.

Para ambas fracciones de material particulado se cumplen los criterios normativos alcanzando
porcentajes bajos respecto de la normativa.

_**3.6.2**_ _**Gases, Dióxido de Nitrógeno (NO2), Dióxido de Azufre (SO2) y Monóxido de Carbono (CO)**_

_**Escenario de Construcción**_

El análisis de cumplimiento de la normativa primaria de calidad del aire para NO2 para el escenario de
Construcción modelados alcanza valores menores al 7% de la normativa para los criterios en 1 hora y un

1% del criterio anual.

En el caso del SO2 los valores modelados no superan el 1% de la normativa en 24 horas y anual. De la
misma forma, para el caso del CO ambos criterios normativos tampoco superan el 1% en ambos criterios

normativos.

El receptor con los aportes indicados corresponde al Mall Zofri, receptor que cuenta con una afluencia
de población flotante no residencial.

Para todos los gases analizados se cumple los criterios normativos.

Anexo 2-13- Modelación de emisiones atmosféricas 24

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

_**3.6.3**_ _**Material Particulado Respirable (MP10) y Fino (MP2,5) Escenario de Operación**_

El análisis de cumplimiento de la normativa primaria de calidad del aire para MP10 para el escenario de
Operación modelados no supera el 2% de la normativa para los criterios en 24 horas y un 1,1% del

criterio anual.

En el caso del MP2,5 los valores modelados no superan el 4% de la normativa en 24 horas y el 2% en la

media anual.

El receptor indicado corresponde al Mall Zofri, receptor que cuenta con una afluencia de población

flotante no residencial.

Para ambas fracciones de material particulado se cumplen los criterios normativos alcanzando
porcentajes bajos respecto de la normativa.

_**3.6.4**_ _**Gases, Dióxido de Nitrógeno (NO2), Dióxido de Azufre (SO2) y Monóxido de Carbono (CO)**_

_**Escenario de Operación**_

El análisis de cumplimiento de la normativa primaria de calidad del aire para NO2 para el escenario de
Operación modelados alcanza valores cercanos al 55% de la normativa para los criterios en 1 hora y un

5% del criterio anual.

En el caso del SO2 los valores modelados no superan el 18% de la normativa en 24 horas y el 7% anual, y
para el caso del CO ambos criterios normativos no superan el 1%.

El receptor referido al análisis corresponde al Mall Zofri, receptor que cuenta con una afluencia de
población flotante no residencial.

Para todos los gases analizados se cumplen los criterios normativos.

Anexo 2-13- Modelación de emisiones atmosféricas 25

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

**3.7** **R** **ESUMEN DE** **R** **ESULTADOS Y** **C** **ONCLUSIONES**

Respecto a los resultados obtenidos de la modelación, estos permiten concluir, que el Proyecto no
provoca efectos adversos significativos sobre la salud de la población en su entorno, toda vez que:

 - Las emisiones del Proyecto se generan principalmente en un tiempo acotado para la Fase de

Construcción, y corresponden a obras menores respecto a movimiento de tierra. Las

mayores emisiones se generan por el tránsito de vehículos sobre caminos pavimentados.

 - Las emisiones en la Fase de Operación no son constantes ya que la operación de la planta no

considera duración de 24 horas diarias 7 días de la semana, las emisiones serán variables de

acuerdo al escenario productivo que está determinado por la disponibilidad y asignación de

cuotas del recurso pesquero.

 - Los resultados modelados para la Fase de Construcción, no generan aportes significativos en

sus criterios diarios y anuales según lo definido en la normativa vigente para MP10 en el D.S.

No 59/98, y MP2.5 en el D.S. No 12/11.

 - De la misma forma los aportes de gases del Proyecto en la Fase de Construcción no

sobrepasan las normativas vigentes correspondientes a NO2 (D.S. N° 114/2002), SO2 (D.S.

N° 113/2002) y CO (D.S. N° 115/2002).

 - Respecto a los resultados obtenidos de la modelación para el escenario de Operación se

puede concluir que no se generan aportes significativos en sus criterios diarios y anuales

según lo definido en la normativa vigente para MP10 en el D.S. No 59/98, y MP2.5 en el D.S.

No 12/11. Por otro lado, los resultados de la modelación son concordantes con la dirección

del viento predominante en el sector (SSO), por lo que las emisiones se dispersan en el

sentido contrario a la ubicación de los receptores de interés, no existiendo receptores

sensible en la dirección hacia donde se dirige la pluma de dispersión.

 - De la misma forma los aportes de gases del Proyecto en la Fase de Operación no sobrepasan

las normativas vigentes correspondientes a NO2 (D.S. N° 114/2002), SO2 (D.S. N° 113/2002)

y CO (D.S. N° 115/2002).

En el Apéndice A de este documento se presentan las curvas de isoconcentración asociadas a los
estadísticos estudiados para los contaminantes material particulado MP10, MP2.5 y gases.

Anexo 2-13- Modelación de emisiones atmosféricas 26

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO<br>CAMANCHACA|

## APÉNDICE A ISOCONCENTRACIONES DE CONTAMINANTES ATMOSFÉRICOS

Anexo 2-13 - Modelación de emisiones atmosféricas 27

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 13.Isoconcentraciones Promedio Anual MP10 (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 28

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 14.Isoconcentraciones Percentil 98 24 Horas MP10 (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 29

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 15.Isoconcentraciones Promedio Anual MP2,5 (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 30

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 16.Isoconcentraciones Percentil 98 24 Horas MP2,5 (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 31

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 17. Isoconcentraciones Percentil 99 1 Hora NO2 (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 32

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 18. Isoconcentraciones Anual NO2 (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 33

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 19. Isoconcentraciones Percentil 99 1 Hora CO (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 34

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 20. Isoconcentraciones Percentil 99 8 Horas CO (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 35

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 21. Isoconcentraciones Anual SO2 (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 36

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 22. Isoconcentraciones P99 24 horas SO2 (μg/m3N) Escenario de Construcción**

Anexo 2-13 - Modelación de emisiones atmosféricas 37

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 23.Isoconcentraciones Promedio Anual MP10 (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 38

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 24.Isoconcentraciones Percentil 98 24 Horas MP10 (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 39

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 25.Isoconcentraciones Promedio Anual MP2,5 (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 40

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 26.Isoconcentraciones Percentil 98 24 Horas MP2,5 (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 41

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 27. Isoconcentraciones Percentil 99 1 Hora NO2 (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 42

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 28. Isoconcentraciones Anual NO2 (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 43

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 29. Isoconcentraciones Percentil 99 1 Hora CO (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 44

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 30. Isoconcentraciones Percentil 99 8 Horas CO (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 45

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 31. Isoconcentraciones Anual SO2 (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 46

|Col1|DECLARACIÓN DE IMPACTO AMBIENTAL|Col3|
|---|---|---|
||PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|PROYECTO PLANTA DE HARINA Y ACEITE DE PESCADO CAMANCHACA|

**Figura 32. Isoconcentraciones P99 24 horas SO2 (μg/m3N) Escenario de Operación**

Anexo 2-13 - Modelación de emisiones atmosféricas 47

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Resumen Estimación de Emisiones, Etapa de Construcción y Operación****

| Fase del Proyecto | Parámetros | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Fase del Proyecto** | **MP10** | **MP2,5** | **NOx** | **CO** | **SO2** | **HC/COV** |
| Fase de Construcción Año 1 | 2,0893 | 1,1591 | 10,5595 | 2,6352 | 0,8817 | 0,1838 |
| Fase de Construcción Año 2 | 0,9656 | 0,3939 | 3,4218 | 0,7693 | 0,0440 | 0,1827 |
| Fase de Operación | 11,7448 | 8,3197 | 95,4463 | 15,2579 | 166,6972 | 0,268 |

**Tabla 2: Normas de Calidad del Aire Consideradas en el Estudio.****

| Parámetro | Tipo de<br>Norma | Indicador | Límite Máximo<br>Permitido (μg/m3N) | Referencia |
| --- | --- | --- | --- | --- |
| **MP10** | Primaria | Promedio Anual | 50 (μg/m3N) | Decreto Supremo N°<br>59/1998 del<br>MINSEGPRES |
| **MP10** | Primaria | Percentil 98 24 Horas | 150 (μg/m3N) | 150 (μg/m3N) |
| **MP2,5** | Primaria | Promedio Anual | 20 (μg/m3N) | Decreto Supremo N°<br>12/2011 del<br>MINSEGPRES |
| **MP2,5** | Primaria | Percentil 98 24 Horas | 50 (μg/m3N) | 50 (μg/m3N) |
| **NO2** | Primaria | Promedio Anual | 100 (μg/m3N) | Decreto Supremo N°<br>114/2002 del<br>MINSEGPRES |
| **NO2** | Primaria | Percentil 99 Máximos diarios concentración<br>de 1 Hora | 400 (μg/m3N) | 400 (μg/m3N) |
| **SO2** | Primaria | Promedio Anual | 80 (μg/m3N) | Decreto Supremo N°<br>113/2002 del<br>MINSEGPRES |
| **SO2** | Primaria | Percentil 99 24 Horas | 250 (μg/m3N) | 250 (μg/m3N) |
| **CO** | Primaria | Percentil 99 Máximos diarios concentración<br>de 1 Hora | 30000 (μg/m3N) | Decreto Supremo N°<br>115/2002 del<br>MINSEGPRES |
| **CO** | Primaria | Percentil 99 Máximos diarios concentración<br>de 8 Horas | 10000 (μg/m3N) | 10000 (μg/m3N) |

**Tabla 3: Valores de Temperatura WRF.****

| Mes | 2014 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Mes** | **T° Min** | **T° Max** | **T° Promedio** |
| Enero | 18,1 | 24,6 | 21,0 |
| Febrero | 17,3 | 22,8 | 19,9 |
| Marzo | 16,4 | 23,1 | 19,5 |
| Abril | 14,9 | 22,7 | 17,9 |
| Mayo | 14,7 | 24,7 | 16,9 |
| Junio | 13,1 | 20,5 | 15,5 |
| Julio | 11,8 | 22,1 | 14,4 |
| Agosto | 11,5 | 19,4 | 14,5 |
| Septiembre | 12,3 | 19,9 | 14,5 |
| Octubre | 12,9 | 20,8 | 15,7 |
| Noviembre | 14,3 | 20,1 | 16,6 |
| Diciembre | 15,2 | 20,7 | 17,3 |

**Tabla 7: Detalle Archivo WRF****

| Proyección Cartográfica | Cónica conforme de Lambert (LCC) |
| --- | --- |
| **Período** | 1 Enero al 31 de Diciembre 2014 |
| **Origen** | Latitud: 20.186 ° ° S<br>Longitud: 70.137 ° W |
| **Datum** | NWS-83 |
| **Grilla** | 1 km |
