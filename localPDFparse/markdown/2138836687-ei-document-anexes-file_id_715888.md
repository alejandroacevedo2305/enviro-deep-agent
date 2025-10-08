---
title: Sin título
author: Sony
date: D:20171229094519-03'00'
language: es
type: report
pages: 38
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME DE ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICA
  - ANEXO I MEMORIA DE CALCULO DE EMISIONES
  - ANEXO II MEMORIA MODELO SCREEN
-->

# INFORME DE ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICA

## PROYECTO AURORA

Diciembre, 2017

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**ÍNDICE**

1. INTRODUCCIÓN ........................................................................................................................ 3

2. FUENTES DE EMISIÓN EN LA FASE DE OPERACIÓN .......................................................... 4

3. METODOLOGÍA ......................................................................................................................... 6

4. ESTIMACIÓN DE EMISIONES ATMOSFÉRICAS FASE OPERACIÓN .................................... 6

4.1. Escarpe ............................................................................................................................... 7

4.2. Excavación ......................................................................................................................... 8

4.3. Transferencia de Material ................................................................................................ 9

4.4. Erosión de Material ......................................................................................................... 10

4.5. Erosión de Material por tránsito sin cubierta .............................................................. 11

4.6. Procesamiento de material ............................................................................................ 12

4.7. Circulación de camiones en caminos no pavimentados ............................................ 13

4.8. Emisiones generadas por tránsito de vehículos ......................................................... 14

4.9. Combustión interna de maquinaria fuera de ruta ...................................................... 16

4.10. Emisiones Grupos Electrógenos ................................................................................ 17

5. RESUMEN DE EMISIONES ..................................................................................................... 18

6. MODELACIÓN DE EMISIONES ATMOSFÉRICAS FASE OPERACIÓN ................................ 19

6.1. Descripción y Justificación del Modelo ......................................................................... 19

6.2. Fuentes de Emisión ......................................................................................................... 19

1.1. Área de Influencia ........................................................................................................... 20

1.2. Resultados de la Modelación ......................................................................................... 20

2. CONCLUSIONES ...................................................................................................................... 26

3. RECOMENDACIONES .............................................................................................................. 27

4. BIBLIOGRAFÍA ......................................................................................................................... 28

1

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**ÍNDICE DE TABLAS**

Tabla 1. Coordenadas del Proyecto ............................................................................................... 4
Tabla 2 Factor de emisión por Escarpe ......................................................................................... 7
Tabla 3 Emisión por Escarpe ........................................................................................................... 7
Tabla 4 Factor de emisión por Excavación .................................................................................... 8
Tabla 5 Emisión por Excavación ..................................................................................................... 8
Tabla 6 Factor de emisión por Transferencia de Material .......................................................... 9
Tabla 7 Emisión por Transferencia de Material ............................................................................ 9
Tabla 8 Factor de emisión por Erosión de Material ................................................................... 10
Tabla 9 Emisión por Erosión de Material ..................................................................................... 10
Tabla 10 Emisión por Erosión de Material por tránsito sin cubierta ........................................ 11
Tabla 11 Emisión por Erosión de Material por camión sin cubierta ........................................ 11
Tabla 12 Factores de Emisión para procesamiento de material .............................................. 12

Tabla 13 Emisiones del Procesamiento de material .................................................................. 12

Tabla 14 Emisión por tránsito en camino no pavimentado ...................................................... 13
Tabla 15 Peso promedio en vías no pavimentadas ................................................................... 14
Tabla 16 Nivel de Actividad y Emisiones por resuspensión en camino no pavimentado ..... 14
Tabla 17 Factor de emisión generados por la combustión vehicular ...................................... 15
Tabla 18 Nivel de actividad por camiones ................................................................................... 15
Tabla 19 Emisiones por combustión de camiones en Camino no pavimentado .................... 16
Tabla 20 Factor de Emisión por Maquinaria fuera de ruta ....................................................... 16
Tabla 21 Emisión por Maquinaria fuera de ruta ......................................................................... 16
Tabla 22 Factores de Emisión por Grupos Electrógenos ........................................................... 17
Tabla 23 Emisión por Grupos Electrógenos ................................................................................ 17
Tabla 24 Resumen de Emisiones por actividad .......................................................................... 18

Tabla 25 Tasa de emisiones aportada por el proyecto ............................................................. 20

Tabla 26. Datos de entrada del modelo ...................................................................................... 20

Tabla 27. Resultado del aporte de contaminantes entregadas por el modelo ...................... 21
Tabla 28. Máximas concentraciones horarias entregadas por el modelo ............................... 21
Tabla 29. Factor para obtener promedios máximos de concentración ................................... 21
Tabla 30. Análisis de Cumplimiento de la Norma de referencia de Calidad del Aire ............ 22

Tabla 31. Concentraciones por distancia de los contaminantes analizados........................... 23

**Índice de Figuras**

Figura 1 Ubicación del proyecto y caminos de acceso ................................................................ 5
Figura 2 Concentraciones de contaminantes asociados a las distancia desde la fuente ..... 25

2

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**1.** **INTRODUCCIÓN**

El siguiente informe contiene las Estimación y Modelación de Dispersión Atmosférica de
material particulado sedimentable (MPS), material particulado (MP 10 ), material particulado
fino respirable (MP 2,5 ) y gases (CO, HC, SO X y NO X ). El proyecto tiene por objeto disponer
de un sector para la extracción, procesamiento y abastecimiento de material integral para
obras de infraestructura vial, permitiendo así el desarrollo del contrato, “Mejoramiento
Ruta CH-257, Sector Onaissín-San Sebastián, Tramo Km. 135,7400 al Km. 180,90497;
Comuna de Porvenir, Provincia de Tierra del Fuego, Región de Magallanes y Antártica
Chilena” ejecutado por Mandato del Ministerio de Obras Públicas, que actualmente se
encuentran en ejecución.
Mediante la extracción mecanizada de aproximadamente 485.034,9 m [3] de material
integral, en un período de un año, para posteriormente considerar 2 años de recuperación,
con una superficie total de 12 Há, el proyecto contempla procesos de extracción y
selección, con la finalidad de obtener material integral destinado a la confección de
infraestructura vial, terraplenes, rellenos estructurales y otros.

La finalidad del presente informe, es estimar las emisiones atmosféricas producto del
desarrollo de estas actividades, para luego, modelar la dispersión del aporte de
contaminantes sobre algunos receptores de interés, para determinar los efectos en la
calidad del aire, utilizando un modelo básico del tipo gaussiano (SCREEN3), que nos
permitirá discriminar entre el utilizar otros modelos más complejos y sofisticados.

Las actividades propias del proyecto que generan emisiones atmosféricas corresponden a
las actividades extracción y tratamiento de material, por el tráfico interno de la maquinaria
que se encuentre operativa en la zona de extracción, operaciones de transferencia de
material, transito de camión sin cubierta, equipos electrógenos, entre otros.

Respecto a las concentraciones finales de contaminantes sobre eventuales receptores en
el área, se presentan los resultados de la modelación en conjunto con un análisis de
cumplimiento de las normas de referencia de calidad del aire aplicable, para los
contaminantes indicados en este documento.

Por último, se indicará recomendaciones con el fin de controlar las emisiones atmosféricas
por la actividad propia del proyecto. Cabe señalar, que se realizará humectación en las
vías internas y de acceso al proyecto, lo que será incluido en los cálculos de las emisiones
atmosféricas.

3

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**2.** **FUENTES DE EMISIÓN EN LA FASE DE OPERACIÓN**

En general, las principales emisiones a la atmósfera de material particulado MPS, MP 10 y
MP 2,5 provenientes de la modificación de la operación del proyecto, corresponden a 2
tipos:
a) Las emisiones relativas a la resuspensión del polvo natural producto de la extracción,

procesamiento y tráfico vehicular sobre caminos no pavimentados, del material a
trasladar.
b) Las emisiones que salen directamente desde el tubo de escape de los vehículos

pesados, que se deben al proceso de combustión interna, y procesamiento del
tratamiento de las arenas.

Durante la operación del proyecto se generará material particulado resuspendido, debido a
las actividades de: escarpe, extracción de áridos, transferencia de material, erosión de
pila, erosión por tránsito de camiones sin cubierta, resuspensión desde caminos por la
circulación de camiones y maquinarias, Chancador de áridos y Harnero.

En tanto que las emisiones de gases (CO, HC, SO X y NO X ), salen directamente desde el
tubo de escape debido al proceso de combustión interna de motores, se presentarán en la
operación de maquinarias, vehículos y equipos electrógenos, durante la extracción y
procesamiento de los áridos.

A continuación, se presentan unas figuras que permiten graficar la ubicación de las plantas
de tratamiento de las arenas extraídas y las rutas que tendrán que recorrer los camiones
hasta ellas.

En Figura 1, que se presenta a continuación, se muestra un plano a escala 1:6.000, de la
zona de extracción y la ubicación del camino de acceso al proyecto. Las coordenadas del
Proyecto se presentan en la siguiente Tabla.

Tabla 1. Coordenadas del Proyecto

|Punto|Y|X|Punto|Y|X|
|---|---|---|---|---|---|
|V-1|4.099.226,15|507.723,46|V-9|4.099.326,01|507.725,75|
|V-2|4.099.215,86|507.917,64|V-10|4.099.280,64|507.493,22|
|V-3|4.099.112,00|507.922,00|V-11|4.099.131,93|507.210,12|
|V-4|4.099.123,00|508.007,00|V-12|4.099.123,20|507.167,97|
|V-5|4.099.082,00|508.015,00|V-13|4.099.002,20|507.192,54|
|V-6|4.099.091,00|508.087,00|V-14|4.099.048,69|507.397,98|
|V-7|4.099.172,00|508.068,00|V-15|4.099.168,10|507.521,99|
|V-8|4.099.311,17|508.008,79|-|-|-|

Fuente: Elaboración Propia

4

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**3.** **METODOLOGÍA**

La metodología utilizada en la estimación de las emisiones atmosféricas corresponde a la
indicada principalmente por el documento “AP 42, Fifth Edition, Compilation of Air
Pollutant Emission Factors, Volume 1: Stationary Point and Area Sources, United States Environmental Protection Agency (US EPA)” y en el Informe Final, “Servicio de
Recopilación y Sistematización de Factores de Emisión al Aire para el Servicio de
Evaluación Ambiental”, de mayo 2015. También se consultó, como referencia, la “Guía
para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para la Región
Metropolitana”, Seremi del Medio Ambiente, 2012.

La estimación de las emisiones atmosféricas, para las distintas fases, se realizaron en
forma desagregadas, a través del cálculo individual de cada una de sus faenas o
actividades, obteniéndose de esta manera la sumatoria de los cálculos independientes de
las actividades de intervención directa e indirecta de la construcción y operación.

Estas emisiones fueron calculadas sobre una base anual y expresadas en función de un
año hipotético de comienzo del proyecto, considerando el mes 1 del año 1.

Los factores de emisión proporcionan un valor representativo de la cantidad de agentes
contaminantes que se emiten a la atmósfera en una actividad emisora. En muchos casos,
los factores de emisión representan la media de un conjunto de datos disponibles y por lo
general, se asume como representativo para períodos de largo plazo.

Los niveles de actividad considerados en los cálculos dependen exclusivamente del factor
de emisiones específico empleado para cada actividad, y la información que lo sustenta
está de acuerdo a las condiciones específicas de este proyecto.

**4.** **ESTIMACIÓN DE EMISIONES ATMOSFÉRICAS FASE OPERACIÓN**

A continuación se presentan la estimación de las emisiones de MPS, MP 10 y MP 2,5 por
resuspensión y MP 10, MP 2,5 y Gases por combustión que serán liberados a la atmósfera
producto de la operación del proyecto y que están asociadas, en primer lugar, a las
actividades de intervención directa en el sitio donde se realizarán las faenas de extracción
de áridos y en segundo lugar, las asociadas al transporte, disposición y transferencia del
material extraído, y la operaciones de la planta de chancado, equipos electrógenos, entre
otros.

6

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.1.Escarpe**

Considera la extracción de la capa vegetal del área intervenida del proyecto asociada a la
extracción del material. En la tabla siguiente, se presenta el Factor de Emisión utilizado en
el cálculo del material particulado resuspendido de esta actividad.

Tabla 2 Factor de emisión por Escarpe

|Factor de Emisión (kg/km)|Col2|Col3|
|---|---|---|
|MPS|MP10|MP2,5|
|8,906|5,7|1,140|

Fuente: Elaboración Propia

Para el MPS, el factor de emisión se obtuvo del documento Ap42, 4°Edition: Chapter 9,
Section 9,1 "Agricultural Tilling" calculado de la relación entre los factores de tamaño de
particulas en la preparación de terrenos para actividades agrícolas; para el MP2,5, el factor
de emisión se obtuvo en Factor de Chapter 2 Agricultural Tilling - “Fugitive Dust
Handbook” de la Asociación Western Regional Air (WRAP).

El Nivel de Actividad, se obtuvo considerando la distancia total recorrida por la maquinaria,
asociada a la superficie del terreno intervenida anualmente, durante la fase de operación
por el retiro de la capa vegetal del Proyecto. Para ello se consideró una pala de ancho 2,8
m, lo que dio como resultado un rendimiento de 3,57 km/ha.

El proyecto abarca una superficie total de 12 ha. En base a lo anterior, considerando un
área a intervenir de 12 ha anuales, se obtiene un nivel de actividad de 42,840 km.

En la tabla que se muestra a continuación se presentan los factores utilizados y los
resultados de las emisiones por escarpes durante la etapa de operación.

Tabla 3 Emisión por Escarpe

|Factor de Emisión (kg/km)|Col2|Col3|Nivel de Actividad<br>(km/año)|Emisión (ton/año)|Col6|Col7|
|---|---|---|---|---|---|---|
|MPS|MP10|MP2,5|42,840|MPS|MP10|MP2,5|
|8,906|5,7|1,140|1,140|0,382|0,244|0,049|

Fuente: Elaboración Propia

7

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.2.Excavación**

Considera la excavación en los frentes de extracción de áridos. En la tabla siguiente, se
presenta el Factor de Emisión utilizado en el cálculo del material particulado resuspendido
de esta actividad.

Tabla 4 Factor de emisión por Excavación

|Contaminante|Fórmula (kg/h)|Parámetro|Valor|
|---|---|---|---|
|MPS|<br>|K: factor de partícula|1|
|MPS|<br>|S: % de fino|3,9|
|MPS|<br>|M: Humedad del material (%)|6,5|
|MP10|<br>|K: factor de partícula|0,75|
|MP10|<br>|S: % de fino|3,9|
|MP10|<br>|M: Humedad del material (%)|6,5|
|MP2,5|<br>|K: factor de partícula|0,105|
|MP2,5|<br>|S: % de fino|3,9|
|MP2,5|<br>|M: Humedad del material (%)|6,5|

Fuente: Elaboración Propia

El porcentaje de finos (s) corresponde al valor obtenido de Compilado de Factores de
emisiones, SEA 2015 y el porcentaje de humedad del material (M), es el valor obtenido de
Guía para la estimación de emisiones para proyectos inmobiliarios.

El Nivel de Actividad se determinó a través del rendimiento de la maquinaria a utilizar. El
volumen considerado corresponde a la capacidad máxima de material que se puede
extraer al año, de 485.034,90 m [3] /año. El proyecto utilizará como máximo 3 excavadoras
con capacidad de 1,2 m [3] cada una.

Finalmente, el rendimiento de la maquinaria considerado es el valor por defecto
establecido en la guía de la SEREMI del Medio Ambiente de la RM 2012, de 30 m3/h para
una capacidad de palada de 1 m3. Como la capacidad de palada de 1,2 m [3] por
maquinaria, se obtiene un rendimiento de 36 m [3] /h y un nivel de actividad de 4.491
horas/año para cada una de las excavadoras.

En la tabla siguiente, se muestran los factores utilizados y los resultados de las emisiones
por la extracción del material, durante la etapa de operación.

Tabla 5 Emisión por Excavación

|Contaminante|FE (kg/h)|NA (h)|Emisión (ton/año)|
|---|---|---|---|
|MPS|0,556|13.473|15,737|
|MP10|0,075|0,075|2,548|
|MP2,5|0,058|0,058|1,652|

Fuente: Elaboración Propia

8

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.3.Transferencia de Material**

Considera la carga del material generados en el sitio del proyecto y su posterior descarga
en el lugar de destino final. En la tabla siguiente, se presenta el Factor de Emisión
utilizado en el cálculo del material particulado resuspendido de esta actividad.

Tabla 6 Factor de emisión por Transferencia de Material

|Contaminante|Fórmula (kg/ton)|Parámetros|Valor|
|---|---|---|---|
|MPS|<br>( <br> )<br> <br>( <br> ~~)~~<br>|K: factor de partícula|0,74|
|MPS|<br>( <br> )<br> <br>( <br> ~~)~~<br>|U: velocidad del viento (m/s)|4,7|
|MPS|<br>( <br> )<br> <br>( <br> ~~)~~<br>|M: Humedad del material (%)|6,5|
|MP10|<br>( <br> )<br> <br>( <br> ~~)~~<br>|K: factor de partícula|0,35|
|MP10|<br>( <br> )<br> <br>( <br> ~~)~~<br>|U: velocidad del viento (m/s)|4,7|
|MP10|<br>( <br> )<br> <br>( <br> ~~)~~<br>|M: Humedad del material (%)|6,5|
|MP2,5|<br>( <br> )<br> <br>( <br> ~~)~~<br>|K: factor de partícula|0,053|
|MP2,5|<br>( <br> )<br> <br>( <br> ~~)~~<br>|U: velocidad del viento (m/s)|4,7|
|MP2,5|<br>( <br> )<br> <br>( <br> ~~)~~<br>|M: Humedad del material (%)|6,5|

Fuente: Elaboración Propia

El valor de velocidad del viento (U), de 4,7 m/s, fue obtenido de la estación Tierra del
[Fuego, Primavera de www.agromet.inia.cl para el año 2016. El valor de la humedad del](http://www.agromet/)
material (M) es el valor por defecto de la Guía de la SEREMI del Medio Ambiente RM 2012.

El nivel de actividad se determinó a través del volumen de material que será movilizado
anualmente, de 485.035 m [3] /año. Las actividades consideradas, corresponden a la carga
de los camiones en el área de extracción, la descarga en el área de la planta y, finalmente,
la carga en la tolva de alimentación de la chancadora, mediante cargadores frontales. Es
en base a lo anterior, el volumen de extracción se multiplicó por 3, para considerar el
movimiento total del material, y una densidad estimada de 1,5 ton/m [3], obteniendo como
resultado un total de 2.182.657 ton/año que serán transferidas.

A continuación, se muestran los factores utilizados y los resultados de las emisiones por la
transferencia del material, durante la etapa de operación.

Tabla 7 Emisión por Transferencia de Material

|Contaminante|FE (kg/ton)|NA (ton/año)|Emisión (ton/año)|
|---|---|---|---|
|MPS|0,00060|2.182.657|1,319|
|MP10|0,00029|0,00029|0,624|
|MP2,5|0,00004|0,00004|0,095|

Fuente: Elaboración Propia

9

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.4.Erosión de Material**

Considera la erosión de pilas de material, por acción del viento, que serán acopiadas en el
sitio del proyecto, antes de ser trasladado hasta su sitio de disposición final. En la tabla
siguiente, se presenta el Factor de Emisión utilizado en el cálculo del material particulado
resuspendido de esta actividad.

Tabla 8 Factor de emisión por Erosión de Material

|Contaminante|Fórmula (kg/ha)|Parámetros|Valor|
|---|---|---|---|
|MPS|<br> <br>|K: factor de partícula|1|
|MPS|<br> <br>|S: % de fino|3,9|
|MPS|<br> <br>|f: tiempo que excede los 5,4 m/s (%)|37,8|
|MP10|<br> <br>|K: factor de partícula|0,5|
|MP10|<br> <br>|S: % de fino|3,9|
|MP10|<br> <br>|f: tiempo que excede los 5,4 m/s (%)|37,8|
|MP2,5|<br> <br>|K: factor de partícula|0,15|
|MP2,5|<br> <br>|S: % de fino|3,9|
|MP2,5|<br> <br>|f: tiempo que excede los 5,4 m/s (%)|37,8|

Fuente: Elaboración Propia

Considera un porcentaje de finos de un 3,9%, valor obtenido de Informe de compilado de
factores de emisiones, SEA 2015. Además, considera que un 37,8% del tiempo el viento
excede los 5,4 m/s, datos obtenidos de los registros la estación Tierra del Fuego,
[Primavera de www.agromet.inia.cl, para el año 2016.](http://www.agromet/)

El nivel de actividad (NA) se determinó a través del cálculo de la superficie expuesta al
viento de la pila del material excavado que se acumulará parcialmente, antes de ser
retirada diariamente hasta su sitio de disposición final. Para se consideró una altura de pila
de 4 m y un volumen diario de material expuesto de 1.701 m [3] /d (485.035 m [3] /285 día),
por el tiempo que tarde esta actividad (365 d/año de exposición al viento). Por lo anterior,
el área estimada de exposición será de 0,130 ha/día.

En la tabla que se muestra a continuación se presentan los factores utilizados y los
resultados de las emisiones por la erosión de pilas de material, durante la etapa de
operación.

Tabla 9 Emisión por Erosión de Material

|Contaminante|FE (kg/ha)|NA (ha/año)|Emisión (ton/año)|
|---|---|---|---|
|MPS|12,453|47,497|0,5915|
|MP10|6,227|6,227|0,2957|
|MP2,5|1,868|1,868|0,0887|

Fuente: Elaboración Propia

10

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.5.Erosión de Material por tránsito sin cubierta**

Considera el efecto de la erosión eólica que afectará los camiones sin su carga cubierta, se
utilizarán los factores de emisión presentados a continuación en la siguiente tabla.

Tabla 10 Emisión por Erosión de Material por tránsito sin cubierta

|Contaminante|Fórmula (lb/yd2/h)|Parámetros|Valor|
|---|---|---|---|
|MPS||K: factor de partícula|1|
|MPS||U: velocidad del vehículo (km/h)|40|
|MP10||K: factor de partícula|1|
|MP10||U: velocidad del vehículo (km/h)|40|
|MP2,5||K: factor de partícula|0,15|
|MP2,5||U: velocidad del vehículo (km/h)|40|

Fuente: Elaboración Propia

Se consideró como velocidad máxima de recorrido de los camiones que trasladarán el
material, una velocidad de 40 km/h.

El nivel de actividad se determinó a través del cálculo de la superficie expuesta al viento
de cada camión en el traslado del material extraído en el frente, hasta la planta para su
procesamiento. El proyecto considera un total de 15 camiones de 20 m [3], con una
superficie de tolva de 20 m [2], correspondiente a una superficie total expuesta es de 300
m [2] /h. La jornada laboral considerada para el funcionamiento de los camiones es de 8 hrs,
de las cuales la mitad del tiempo operan vacíos, por roles de 11x3 días, por lo que la
cantidad de días trabajados al mes es de aproximadamente 24 d/mes (aprox. 285 d/año).
Finalmente, el tiempo de exposición corresponde a 1.140 h/año.

En la siguiente tabla se presentan las emisiones por erosión por tránsito de camiones sin
cubierta.

Tabla 11 Emisión por Erosión de Material por camión sin cubierta

|Contaminante|FE (kg/m2/h)|NA (m2/año)|Emisión (ton/año)|
|---|---|---|---|
|MPS|0,0020|342.000|0,6868|
|MP10|0,0020|0,0020|0,6868|
|MP2,5|0,0003|0,0003|0,1030|

Fuente: Elaboración Propia

11

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.6.Procesamiento de material**

Considera la selección por harneo y el traslado por cintas transportadoras, del material
extraído durante su procesamiento. En la siguiente tabla se presentan los factores de
emisión para las actividades en la Planta de Procesamiento.

Tabla 12 Factores de Emisión para procesamiento de material

|Actividad|MPS|MP<br>10|MP<br>2,5|
|---|---|---|---|
|Harnero|0,00110|0,00037|0,00003|
|Cintas Transportadoras|0,0015|0,0006|0,0006|

Fuente: Compilado de factores de emisiones, SEA 2015.

El nivel de actividad para el harnero y cintas transportadoras se determinó a través del
volumen de material que será extraído anualmente el cual se estima un 30% del volumen
anual extraído 485.034,90 m [3] /año, es decir, 145.510 m [3] /año.

A continuación, se presentan los factores y emisiones por la actividad de procesamiento
del material extraído.

Tabla 13 Emisiones del Procesamiento de material

|Actividad|FE (kg/ton)|Col3|Col4|Volumen<br>(m3/año)|NA<br>(ton/año)|Emisión (ton/año)|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Actividad|MPS|MP10|MP2,5|MP2,5|MP2,5|MPS|MP10|MP2,5|
|Harnero|0,00110|0,00037|0,00003|145.510|218.266|0,2401|0,0808|0,0055|
|Cintas<br>Transportadoras|0,0015|0,0006|0,0006|0,0006|0,0006|0,3274|0,1200|0,1200|

Fuente: Elaboración propia

12

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.7.Circulación de camiones en caminos no pavimentados**

Considera la circulación de vehículos por caminos no pavimentados, asociadas al traslado
del material desde los frentes de extracción, hasta el harnero. En la siguiente tabla se
presentan los factores de emisión, para las vías internas del proyecto.

Tabla 14 Emisión por tránsito en camino no pavimentado

|Contaminante|Fórmula (g/km)|Parámetros|Valor|FE (g/km)|
|---|---|---|---|---|
|MPS|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|K: factor de partícula|49|1.260,0|
|MPS|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|S: % de fino|4,9|4,9|
|MPS|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|W: peso promedio (ton)|24,8|24,8|
|MP10|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|K: factor de partícula|1,5|322,5|
|MP10|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|S: % de fino|4,9|4,9|
|MP10|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|W: peso promedio (ton)|24,8|24,8|
|MP2,5|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|K: factor de partícula|0,15|32,2|
|MP2,5|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|S: % de fino|4,9|4,9|
|MP2,5|( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br>|W: peso promedio (ton)|24,8|24,8|

Fuente: Elaboración propia

Considera un porcentaje de finos de un 4,9%, valor obtenido de Informe de compilado de
factores de emisiones, SEA 2015.

El peso promedio de la flota que circulará por las vías no pavimentadas fue obtenido de
los pesos promedio de los vehículos del proyecto, requeridos para transportar el material
extraído. Estos camiones tendrán una capacidad de entre 12 a 20 m [3] (27 ton) y un peso
sin carga de 15 toneladas. Los resultados fueron obtenidos de la siguiente ecuación.

W total = (W vacío - W cargado )/2

Dónde:
W total : Peso promedio del total de la flota del proyecto (ton)
W vacío : Peso del camión sin carga (ton)
W cargado : Peso del camión a máxima capacidad (ton)

Dado que los camiones recorren la misma distancia, tanto cargados, como vacíos, el peso
W, se obtiene del promedio aritmético entre los pesos del camión cargado y sin carga.

La misma fórmula fue considerada, para el caso de la maquinaria. Donde el peso, para el
caso de los cargadores frontales con carga, se estimó en 23,2 ton. A continuación, se
presenta el peso promedio que recorren los vehículos por caminos no pavimentados.

13

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

Tabla 15 Peso promedio en vías no pavimentadas

|Materiales|Tipo de<br>vehículo|Capacidad<br>Vehículo<br>(ton)|Tara<br>(ton)|Peso Bruto<br>(ton)|Peso Wi<br>(ton)|Recorrido<br>(km/año)|Fracción W<br>(ton)|
|---|---|---|---|---|---|---|---|
|Zona de extracción a acopio|<br> C. Tolva|30,0|15,00|45,00|30,00|64.510|7,08|
|Transito Maquinaria|Maquinaria|3,9|21,25|25,15|23,20|208.938|17,73|
|Emisiones Totales|-|**-**|**-**|**-**|**-**|**273.448**|**24,8**|

Fuente: Elaboración propia

El nivel de actividad considera el recorrido total de los camiones en traslado del material
extraído. Por lo que se consideró el flujo total de camiones, obtenido la cantidad de
camiones necesarios para trasladar 485.035 m [3] /año de áridos, considerando una
capacidad de 20 m [3], el cual corresponde a 48.503 viajes ida y vuelta al año. Los que
deberán recorrer una distancia, por vías internas no pavimentadas, de 1,42 km, hasta la
ruta Y-891. Así, el recorrido total de los camiones será de 273.448 km/año.

La humectación de caminos internos se realizará 2 veces al día logrando que la humedad
de estos sea 2 veces mayor que la presente. Luego, según las estimaciones presentadas
en el AP-42, se considera que esta medida logrará mitigar en un 68,7%, debido a que
éstos serán humectados periódicamente.

A continuación, se presenta el nivel de actividad por el tránsito en caminos no
pavimentados según actividad.

Tabla 16 Nivel de Actividad y Emisiones por resuspensión en camino no pavimentado

|Materiales|Volumen<br>(m3)|No de<br>viajes<br>(ida y<br>vuelta)|Distancia<br>recorrida<br>(km)|NA<br>(km/año)|Ea (%)|Emisión (ton/año)|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Materiales|Volumen<br>(m3)|No de<br>viajes<br>(ida y<br>vuelta)|Distancia<br>recorrida <br>(km)|NA<br>(km/año)|Ea (%)|MP2,5|MP10|MPS|
|Zona de extracción a acopio|485.035|48.503|1,42|68.875|68,7|0,6926|6,9261|27,0640|
|Transito Cargador Frontal|485.035|373.104|0,71|264.904|68,7|2,6639|26,6390|104,0925|
|Emisión total|-|-|-|-|-|3,3565|33,5651|131,1565|

Fuente: Elaboración propia

**4.8.Emisiones generadas por tránsito de vehículos**

Los factores de emisión de MP y Gases producto de la combustión interna de los vehículos
del proyecto corresponden en su mayoría:

 Camiones Pesados Diesel Tipo 3, con peso bruto superior a 16 toneladas. Estos
camiones contarán con fecha de inscripción en el Registro Nacional de Vehículos
Motorizados posterior a septiembre de 2003, además cumplirán con los estándares de
emisión similar o superior a la norma EPA 98 o Euro III.

14

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

Tabla 17 Factor de emisión generados por la combustión vehicular

|Fuente de Emisión|Contaminante|FE (g/km )|
|---|---|---|
|Camiones pesados<br>diesel tipo III|CO|(1,24588358438859+(103,700537481749/(1+exp((((-1)*-<br>1,3906312471446)+(0,543451750078654*ln(V)))+(0,039006642599818<br>9*V)))))|
|Camiones pesados<br>diesel tipo III|HC|((0,135938586321894+(0,71588074810547*exp(((-<br>1)*0,0234666513590177)*V)))+(2,79878282504916*exp(((-<br>1)*0,123459782380517)*V)))|
|Camiones pesados<br>diesel tipo III|NOx|((5,58300975720938+(14,5724996214701*exp(((-<br>1)*0,0510403515051286)*V)))+(45,651882800859*exp(((-<br>1)*0,309240087785118)*V)))|
|Camiones pesados<br>diesel tipo III|MP|((0,100820480611018+(0,424449762706025*exp(((-<br>1)*0,0416436785215947)*V)))+(0,864328026775096*exp(((-<br>1)*0,159945936589218)*V)))|
|Camiones pesados<br>diesel tipo III|CC|((199,101296810716+(496,037924788222*exp(((-<br>1)*0,0466183266185801)*V)))+(3798,31076366067*exp(((-<br>1)*0,573715458508514)*V)))*2*0,0015<br>|

Fuente: Elaboración propia

Considerando la ausencia de factores de emisión de MP 2,5 tanto para vehículos como
grupos electrógenos que funcionan con combustible diesel, se ha considerado la relación
existente entre el MP 10 y MP 2,5 indicada en el documento “Actualización del inventario de
emisiones atmosféricas en las comunas de Temuco y Padre Las Casas” elaborado por
DICTUC en el año 2008, es decir: El MP 2,5 corresponde al 92% del MP 10 .

Respecto al factor de emisiones para el SO X se asume que todo el contenido de azufre (S)
en el combustible se transforma completamente en SO 2 . Considerando que el peso
atómico del azufre es el doble que el del oxígeno, la fórmula para su cálculo será la que se
presenta a continuación.
### fe SO 2 j  2  CC j, m  S comb, m

Dónde:

_fe_ _SO_ 2 _j_ [ = Factor de emisión del SO] [2] [ para un vehículo tipo j, (ton/año) ]

_CC_, _j_ = Consumo de combustible del vehículo tipo j que utiliza combustible m (g/Km) _m_

_S_ _comb_, _m_ [ = Contenido de azufre del combustible m (0,0015% en el diesel) ]

El factor de emisión se calculó utilizando una velocidad estimada promedio de 40 km/h,
para el tránsito de camiones del proyecto.

Los Niveles de Actividad generados por el funcionamiento de los motores de los camiones
que transportarán el material extraído, se obtuvieron de la misma manera que para la
actividad anterior, de circulación de camiones por vías pavimentadas (punto 4.8),
considerando distancia total anual recorrida, el cual se muestra a continuación.

Tabla 18 Nivel de actividad por camiones

|Vehículo|Velocidad (km/h)|NA (km/año)|
|---|---|---|
|Camión Tolva|40|68.875|

Fuente: Elaboración propia

15

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

En la tabla que se muestra a continuación, se presenta el resultado de las emisiones
atmosféricas por combustión interna, debido a la circulación de vehículos durante la etapa
de operación del Proyecto.

Tabla 19 Emisiones por combustión de camiones en Camino no pavimentado

|Fuente de Emisión|Contaminante|FE (g/km )|NA (km/año)|Emisión (ton/año)|
|---|---|---|---|---|
|Camiones pesados<br>diesel tipo III|CO|1,971|68.875|0,1358|
|Camiones pesados<br>diesel tipo III|HC|0,436|0,436|0,0300|
|Camiones pesados<br>diesel tipo III|SOX|0,193|0,193|0,0133|
|Camiones pesados<br>diesel tipo III|NOX|7,475|7,475|0,5148|
|Camiones pesados<br>diesel tipo III|MP10|0,168|0,168|0,0116|
|Camiones pesados<br>diesel tipo III|MP2,5|0,183|0,183|0,0126|

Fuente: Elaboración propia

**4.9.Combustión interna de maquinaria fuera de ruta**

Los factores de emisiones de material particulado de combustión y gases asociados a la
operación de la maquinaria durante la construcción del proyecto se encuentran en función
de la potencia y se resumen en la siguiente tabla.

Tabla 20 Factor de Emisión por Maquinaria fuera de ruta

|Maquinaria|Cantidad|Potencia<br>(kW)|Factores de Emisión (g/kW-h)|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Maquinaria|Cantidad|Potencia<br>(kW)|CO|HC|SO2<br>(*)|NOX|MP2,5|MP10|
|Cargador Frontal|2|98|3,76|1,72|0,88|14,36|1,11|1,23|
|Excavadora|3|120|3,76|1,72|1,08|14,36|1,11|1,23|

(*) El valor del factor de emisiones del SO X, se obtuvo de acuerdo a la formula presentada en el punto 4.8.

Fuente: Elaboración propia

Los Niveles de Actividad (NA) se encuentran asociados al tiempo de funcionamiento de la
maquinaria. Se estima que las horas de funcionamiento serán de 2.280 horas al año,
producto de una jornada laborales de 8 horas diarias por 285 días al año. El resultado de
las emisiones se presenta en la siguiente tabla.

Tabla 21 Emisión por Maquinaria fuera de ruta

|Maquinaria|Tiempo<br>Operación<br>(h/año)|NA<br>(kWh/año)|Emisión (ton/año)|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Maquinaria|Tiempo<br>Operación<br>(h/año)|NA<br>(kWh/año)|CO|HC|SO2|NOX|MP2,5|MP10|
|Retroexcavadora|2.280|446.880|1,680|0,769|0,394|6,417|0,495|0,550|
|Excavadora|2.280|820.800|3,086|1,412|0,886|11,787|0,909|1,010|
|Emisión total|-|- <br>|4,766<br>|2,180<br>|1,281|18,204|1,403|1,559|

Fuente: Elaboración propia

16

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.10.** **Emisiones Grupos Electrógenos**

Se contará con un grupo electrógeno de operación continua, de 75 kW de potencia el que
funcionará con combustible Diesel, para suministrar de energía eléctrica a las cintas
transportadora y harnero durante la etapa de operación. En la siguiente tabla se
presentan los factores de emisión.

Tabla 22 Factores de Emisión por Grupos Electrógenos

|Combustible|Unidad|CO|SOx|NOx|MP<br>2,5|MP<br>10|
|---|---|---|---|---|---|---|
|Diesel<br>(hasta 600 hp)|kg/kw-h|0,0041|0,0013|0,0188|0,0007|0,0013|
|Diesel<br>(más de 600 hp)|Diesel<br>(más de 600 hp)|0,0033|0,0000|0,0146|0,0007|0,0004|

Fuente: Guía de la SEREMI del Medio Ambiente Región Metropolitana, 2012.

Los Niveles de Actividad (NA) se encuentran asociados al tiempo de funcionamiento del
equipo. Se estima que las horas de funcionamiento serán de 8 horas diarias, por 285 días
al año, se ha estimado que operará un máximo de 2.280 horas/año. El resultado de las
emisiones se presenta en la siguiente tabla.

Tabla 23 Emisión por Grupos Electrógenos

|Equipos|Potencia<br>(kW)|Tiempo<br>Operación<br>(h/año)|NA<br>(kWh/año)|Emisión (ton/año)|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Equipos|Potencia<br>(kW)|Tiempo<br>Operación<br>(h/año)|NA<br>(kWh/año)|CO|SOx|NOx|MP2,5|MP10|
|Grupo<br>Electrógeno|75|2.280|171.000|0,6943|0,2138|3,2148|0,2108|0,2291|
|Emisión (ton/año)|Emisión (ton/año)|Emisión (ton/año)|Emisión (ton/año)|0,6943|0,2138|3,2148|0,2108|0,2291|

Fuente: Elaboración Propia

17

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**5.** **RESUMEN DE EMISIONES**

A continuación, se describen un resumen de las emisiones en la fase de operación del
proyecto para cada una de las actividades realizadas.

Tabla 24 Resumen de Emisiones por actividad

|Actividades|Emisiones Atmosféricas (ton/año)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Actividades|CO|HC|SOX|NOX|MP2,5<br>comb|MP10<br>comb|MP2,5<br>resus|MP10<br>resus|MPS <br>resus|MP2,5<br>total|MP10<br>total|MPS <br>total|
|Escarpe|-|-|-|-|-|-|0,05|0,24|0,38|0,05|0,24|0,38|
|Extracción|-|-|-|-|-|-|1,65|2,55|15,74|1,65|2,55|15,74|
|Transferencia de<br>material|-|-|-|-|-|-|0,09|0,62|1,32|0,09|0,62|1,32|
|Erosión de material en<br>acopio|-|-|-|-|-|-|0,09|0,30|0,59|0,09|0,30|0,59|
|Erosión por camión<br>sin cubierta|-|-|-|-|-|-|0,10|0,69|0,69|0,10|0,69|0,69|
|Harnero|-|-|-|-|-|-|0,01|0,08|0,24|0,01|0,08|0,24|
|Cintas<br>transportadoras|-|-|-|-|-|-|0,12|0,12|0,33|0,12|0,12|0,33|
|Circulación de<br>vehículos en caminos<br>no pavimentados|-|-|-|-|-|-|3,36|33,57|131,16|3,36|33,57|131,16|
|Combustión vehículos|0,14|0,03|0,01|0,51|0,01|0,01|-|-|-|0,01|0,01|-|
|Combustión<br>maquinaria fuera de<br>ruta|4,77|2,18|1,28|18,20|1,40|1,56|-|-|-|1,40|1,56|-|
|Grupo Electrógeno|0,69|-|0,21|3,21|0,21|0,23|-|-|-|0,21|0,23|-|
|**Emisiones Totales**<br>**(ton/año)**|**5,60**|**2,21**|**1,51**|**21,93**|**1,63**|**1,80**|**5,47**|**38,17**|**150,4**|**7,10**|**39,97**|**150,4**|

Fuente: Elaboración propia

18

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**6.** **MODELACIÓN DE EMISIONES ATMOSFÉRICAS FASE OPERACIÓN**

Para identificar los impactos significativos en los receptores cercanos a las zonas asociadas
al proyecto, se utilizó un modelo básico de dispersión de contaminantes, que nos
permitiera discriminar entre el utilizar otros modelos más complejos y sofisticados, para
determinar el aporte de emisiones a la atmósfera, que presentará el proyecto en su fase
de operación.

**6.1.Descripción y Justificación del Modelo**

El modelo utilizado para este análisis es el SCREEN 3 de la United States Environmental
Protection Agency (USEPA). Este modelo nos permite determinar el aporte de las
emisiones provenientes de fuentes emisoras, en localidades y sectores aledaños a las
instalaciones del Proyecto, permitiendo de este modo asignar las cuotas de
responsabilidad en los niveles de calidad del aire proyectados en su entorno.

El modelo SCREEN 3, se desarrolló como una herramienta para realizar estimaciones de
concentraciones de contaminantes, tomando como base el documento de procedimientos
de proyección de la USEPA, utilizando un modelo de dispersión Gaussiano que incorpora
factores relacionados a la fuente emisora y factores meteorológicos para estimar
concentraciones de contaminantes de fuentes continuas. Se asume que el contaminante
no sufre reacciones químicas y que la pluma no es afectada por procesos de remoción,
como deposición seca o húmeda, durante su transporte desde la fuente. Las variables de
entrada introducidas al modelo incluyen características de la fuente y la tasa de emisión
correspondiente a cada contaminante a evaluar.

Cabe destacar que el modelo SCREEN 3 siempre entrega como resultado concentraciones
ambientales sobreestimadas, debido a que genera internamente la condición
meteorológica más desfavorable, es decir, aquella con la que se obtiene la concentración
ambiental más alta, considerando además que el diseño del modelo ubica al receptor
recibiendo el viento directo de las fuentes y no considerando factores atenuadores como la
topografía. Por lo anterior, la estimación con SCREEN 3, establece un techo o valor
máximo, que en la práctica nunca ocurre, por lo que las concentraciones reales en un
punto determinado son siempre menores a las estimadas por este modelo.

**6.2.Fuentes de Emisión**

La modelación de las emisiones producto de la operación de la cantera, se realizó
considerando la dispersión del material particulado MPS, MP 10 y MP 2,5, presentes en las
emisiones por resuspensión y combustión, así como los Gases, NO X, SO X y CO, producto
de la combustión de fuentes estacionarias y móviles, asociadas a actividades de tránsito
por camino no pavimentado y funcionamiento de maquinarias y grupos electrógenos.

Además, se consideraron las emisiones anuales asociadas a todas las fuentes emisoras de
contaminantes del Proyecto (ver Tabla 23), las que se producirán en toda la superficie del

<!-- INICIO TABLA 23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los Niveles de Actividad (NA) se encuentran asociados al tiempo de funcionamiento del equipo. Se estima que las horas de funcionamiento serán de 8 horas diarias, por 285 días al año, se ha estimado que operará un máximo de 2.280 horas/año. El resultado de las emisiones se presenta en la siguiente tabla. -->

**Tabla 23: Emisión por Grupos Electrógenos**

| Equipos | Potencia<br>(kW) | Tiempo<br>Operación<br>(h/año) | NA<br>(kWh/año) | Emisión (ton/año) | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Equipos | Potencia<br>(kW) | Tiempo<br>Operación<br>(h/año) | NA<br>(kWh/año) | CO | SOx | NOx | MP2,5 | MP10 |
| Grupo<br>Electrógeno | 75 | 2.280 | 171.000 | 0,6943 | 0,2138 | 3,2148 | 0,2108 | 0,2291 |
| Emisión (ton/año) | Emisión (ton/año) | Emisión (ton/año) | Emisión (ton/año) | 0,6943 | 0,2138 | 3,2148 | 0,2108 | 0,2291 |

<!-- Estadísticas: 3 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia 17 -->
<!-- FIN TABLA 23 -->

sitio del proyecto (12 ha), en un lapso de un año. El resultado de las emisiones generadas
espacial y temporalmente, se presentan en la tabla siguiente.

19

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

Tabla 25 Tasa de emisiones aportada por el proyecto

|Emisiones|CO|SO<br>X|NO<br>X|MP<br>2,5 Total|MP<br>10 Total|MPS|
|---|---|---|---|---|---|---|
|ton/año|5,60|1,51|21,93|7,10|39,97|150,40|
|g/m2-s|0,00000296|0,00000080|0,00001159|0,00000375|0,00002112|0,00007949|

Fuente: Elaboración Propia.

Cabe destacar, que las tasas de emisión presentadas en la Tabla 25, corresponden al total
de las emisiones generadas por el proyecto, por lo que se está considerando que todas las
actividades se realizan al mismo tiempo, por lo tanto los valores entregados representan el
escenario de emisión más desfavorable para las fuentes descritas. Además de lo anterior,
en el presente informe no se han considerado medidas de mitigación en el cálculo de las
emisiones de algunas actividades (humectación del material).

**1.1.Área de Influencia**

A su vez, para efectos de la modelación, en el área más cercana al proyecto se
identificaron instalaciones a aproximadamente 16,3 km del sitio del proyecto,
correspondiente a la Tenencia San Sebastián, como la única área en la cual eventualmente
pueda suponerse la presencia de potenciales receptores en el sector. Por ello, el área de
influencia del proyecto se ubicó a 20 km a la redonda del sitio del proyecto, tal como se
grafica en la Figura N°2 que se muestra más adelante. Sin embargo, se considerará la
distancia del Punto de Máxima Concentración (PMC) proyectada desde la fuente de
emisión (100 m), para realizar el análisis de cumplimiento de las normas de referencia de
calidad del aire.

**1.2.Resultados de la Modelación**

La modelación de la dispersión de las emisiones de los distintos contaminantes, fue
considerada como fuentes de área, y se realizó estableciendo como datos de entrada las
siguientes opciones que permite el modelo.

Tabla 26. Datos de entrada del modelo

|Opciones de Entrada|Datos de entrada|Unidad|
|---|---|---|
|Tipo de Fuente|Área|-|
|Altura de Liberación|1,5|m|
|Longitud de Lado Largo|346,41|m|
|Longitud de Lado Corto|346,41|m|
|Altura de Receptor|2,0|m|
|Opción Urbana/Rural|Rural|-|
|Altura de Mezcla|30|m|
|Altura Anemométrica|10|m|
|Clase de Estabilidad|3|-|
|Velocidad Eólica|4,67|m/s|

Fuente: Elaboración Propia.

20

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

La tabla siguiente, muestra los resultados de la modelación, con el cual se obtuvo la
dispersión de las concentraciones de los distintos contaminantes, a distancias entre 100 y
20.000 m del proyecto, con lo que se determinó el aporte de contaminantes
(concentración) sobre los potenciales receptores de interés.

Tabla 27. Resultado del aporte de contaminantes entregadas por el modelo

|Distancia|Concentración horarias (μg/m3)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Distancia|CO|SOX|NOX|MP2,5 Total|MP10 Total|MPS|
|100|9,46|2,56|37,06|11,99|67,53|254,20|
|2.500|1,84|0,50|7,19|2,33|13,10|49,31|
|5.000|1,04|0,28|4,08|1,32|7,44|28,00|
|7.500|0,73|0,20|2,88|0,93|5,24|19,73|
|10.000|0,57|0,15|2,24|0,72|4,08|15,35|
|12.500|0,47|0,13|1,84|0,60|3,35|12,62|
|15.000|0,40|0,11|1,57|0,51|2,86|10,75|
|17.500|0,35|0,09|1,37|0,44|2,49|9,39|
|20.000|0,31|0,08|1,22|0,39|2,22|8,35|

Fuente: Elaboración Propia.

El resultado de las máximas concentraciones horarias (μg/m [3] ), arrojadas por el modelo, se
presentan en la Tabla 28, que se muestra a continuación.

Tabla 28. Máximas concentraciones horarias entregadas por el modelo

|Distancia|Concentración máxima de 1 hora (μg/m3)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Distancia|CO<br>(8 horas)|SOx<br>(Máx. 24<br>horas)|NOx<br>(Máx. 1 hora)|MP2,5<br>(Máx. 24<br>horas)|MP10<br>(Máx. 24<br>horas)|MPS<br>(Máx. 24<br>horas)|
|100|6,62|1,02|37,06|4,80|27,01|101,68|

Fuente: Elaboración Propia.

Es necesario destacar que el modelo entrega concentraciones a nivel horario, las que son
convertidas a concentraciones de 3 h, 8 h, 24 h o anuales, de acuerdo a los factores de
conversión establecidos por la EPA [a] y que se presentan en la siguiente tabla.

Tabla 29. Factor para obtener promedios máximos de concentración

|Tempo Promedio|Factor Multiplicador|
|---|---|
|3 horas|0,9 (±0,1)|
|8 horas|0,7 (±0,2)|
|24 horas|0,4 (±0,2)|
|Anual|0,08 (±0,02)|

Fuente: Screening Procedures for Estimating the Air Quality Impact of Stationary Sources (USEPA 1992).

a Screening Procedures for Estimating the Air Quality Impact of Stationary Sources. U.S. Environmental
Protection Agency (USEPA). Octubre de 1992. Pp 39.

21

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

Para evaluar el nivel de cumplimiento de la normativa ambiental con respecto al material
particulado, se ha considerado como referencia el D.S. N° 59/98, del Ministerio del
Ministerio Secretaría General de la Presidencia, que establece Norma de Calidad Primaria
Para Material Particulado Respirable MP 10, en Especial de los Valores que Definen
Situaciones de Emergencia y de sus modificaciones, la cual se comparó con la
concentración máxima aportada por el proyecto. En cambio para evaluar al material
particulado fino respirable, se ha considerado como referencia el D.S. N° 12/2010 del
Ministerio del Medio Ambiente, que establece la Norma de Calidad Primaria para Material
Particulado Fino Respirable MP 2,5 .

Para los gases NO X se ha considerado como referencia el D.S. N° 114 del Ministerio
Secretaría General de la Presidencia, que establece la Norma de Calidad Primaria de Aire
para Dióxido de Nitrógeno (NO 2 ). A su vez, para el contaminante SO X se ha considerado
como referencia el D.S. N°113 del Ministerio General de la Presidencia, que establece la
Norma de Calidad Primaria de Aire para Dióxido de Azufre (SO 2 ). Finalmente, para el
contaminante CO se ha considerado como referencia el D.S. N° 115 del Ministerio
Secretaría General de la Presidencia, que establece la Norma de Calidad Primaria de Aire
para Monóxido de Carbono (CO).

Por último, en Chile no existe una norma secundaria de calidad del aire para Material
Particulado Sedimentable (MPS) de carácter nacional o específico de la región, por lo
tanto, para evaluar los efectos de este tipo de emisiones se utilizó una norma de
referencia, tal como lo establece el Reglamento de Evaluación de Impacto Ambiental. La
norma de referencia utilizada corresponde a la Norma de Calidad del Aire Ambiente de la
Confederación Suiza que el Sistema de Evaluación de Impacto Ambiental ha validado para
su utilización.

A continuación, se presenta el análisis de cumplimiento de las normas de referencia de
calidad del aire, respecto de las concentraciones máximas para los contaminantes
indicados anteriormente, las cuales se presentaran a una distancia de 100 m de la fuente.

Tabla 30. Análisis de Cumplimiento de la Norma de referencia de Calidad del Aire

|Parámetro|Estadístico|Máxima del<br>Proyecto<br>(μg/m3N)|Límite según<br>Norma<br>(μg/m3N)|Porcentaje<br>respecto de la<br>Norma|Referencia|
|---|---|---|---|---|---|
|MP10|Concentración 24 horas|27,01|150|18,01%|D.S. N° 59 / 1998<br>MINSEGPRES|
|MP10|Concentración anual|5,40|50|10,80%|10,80%|
|MP2,5|Concentración 24 horas|4,80|50|9,59%|D.S. N° 12 / 2010<br>MMA|
|MP2,5|Concentración anual|0,96|20|4,80%|4,80%|
|NOx|Concentración 1 hora|37,06|400|9,27%|D.S. N° 114/ 2002<br>MINSEGPRES|
|SOx|Concentración 24 horas|1,02|250|0,41%|D.S. N° 113/ 2002<br>MINSEGPRES|
|CO|Concentración 1 hora|9,46|30.000|0,03%|D.S. N° 115/ 2002<br>MINSEGPRES|
|CO|Concentración 8 horas|6,62|10.000|0,07%|0,07%|
|MPS|Media aritmética anual|101,68|200|50,84%|Norma Suiza(*)|

(*) Norma Secundaria de Calidad del Aire del Ambiente de la Confederación Suiza.

Fuente: Elaboración Propia.

22

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

Al respecto, las concentraciones máximas, en todos los casos, se encontrarán muy por
debajo de los límites de concentración establecidos por sus correspondientes normas de
referencia, por lo que el aporte de emisiones a los potenciales receptores será igualmente
bajo, aun considerando el efecto sinérgico por la operación simultánea de todas las
actividades del proyecto.

En relación a los receptores potencialmente impactados por el aporte de emisiones del
proyecto, el más cercano se encuentra a una distancia de 16.300 metros de la fuente. En
la Tabla siguiente se presentan las concentraciones por distancia de los contaminantes
analizados en este documento.

Tabla 31. Concentraciones por distancia de los contaminantes analizados

|Distancia (m)|Concentración de Contaminantes (μg/m3)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Distancia (m)|CO<br>(8 horas)|SOX <br>(Máx. 24 horas)|NOX <br>(Máx. 1 horas)|MP2,5<br>(Máx. 24 horas)|MP10<br>(Máx. 24 horas)|MPS<br>(Máx. 24 horas)|
|**100***|6,62|1,02|37,06|4,80|27,01|101,68|
|2.500|1,29|0,20|7,19|0,93|5,24|19,72|
|5.000|0,73|0,11|4,08|0,53|2,98|11,20|
|7.500|0,51|0,08|2,88|0,37|2,10|7,89|
|10.000|0,40|0,06|2,24|0,29|1,63|6,14|
|12.500|0,33|0,05|1,84|0,24|1,34|5,05|
|**15.000***|0,28|0,04|1,57|0,20|1,14|4,30|
|17.500|0,24|0,04|1,37|0,18|1,00|3,75|
|20.000|0,22|0,03|1,22|0,16|0,89|3,34|

- Distancia en la que se presentará la concentración máxima de contaminantes
** Distancia en la que se encuentra el receptor potencialmente más afectado por las actividades del proyecto

De los resultados obtenidos de la modelación, considerando los puntos de Máximo
Impacto, así como el aporte de contaminantes a los correspondientes receptores, es
posible afirmar que las concentraciones de contaminantes en el aire, que se producen por
causa de las emisiones del proyecto durante la fase de operación futura, no son
significativas, por cuanto se encuentran muy por debajo del límite establecido por las
normativas de referencia.

En consecuencia, no se requeriría utilizar un modelo más complejo y los resultados son
concluyentes, por cuanto indican que las emisiones del Proyecto no producirán efectos
adversos significativos en la calidad del aire, aun considerando las peores condiciones de
emisión y meteorológicas.

Cabe destacar, que el modelo SCREEN 3, no entrega la opción de ingresar datos
meteorológicos que sean representativos de un sector específico. En lugar de eso, lo que
hace es examinar respecto de rangos de estabilidad y velocidades del viento, que si
pueden ser ingresados, para identificar el peor caso de condiciones meteorológicas, es
decir, la combinación de la velocidad del viento y estabilidad que resulta más
desfavorable.

23

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

No obstante, lo anterior, se consideraron los antecedentes estadísticas basadas en
observaciones medidas entre 01-01-2016 y el 31-12-2016, por la estación meteorológica
de Tierra del Fuego, Primavera [b], ubicada a unos 91 km en la comuna Tierra del Fuego,
provincia Porvenir, al noroeste del Proyecto, para comparar los datos ingresados al modelo
y así establecer si efectivamente estamos frente a la condición más desfavorable. Dicha
estación registró que la mayor parte del tiempo, el viento es de 4,67 m/s, lo que refleja
una intensidad moderada en la zona, y que la dirección más frecuente es hacia el sureste [c] .

Al respecto, los datos revisados de los registros de la estación meteorológica antes
señalada, nos indican que los vientos predominantes se dirigen hacia el sur-este, en
dirección hacia el receptor más cercano, pero por su lejanía al Proyecto, no se verá
afectado.

En el Anexo II, del presente informe se entregan los reportes de salida del modelo
utilizado, con los cuales es posible verificar los resultados presentados en la Tabla 26 y los
datos de entradas de la Tabla 25.

<!-- INICIO TABLA 25 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de Emisiones Atmosférica Proyecto Aurora -->

**Tabla 25: Tasa de emisiones aportada por el proyecto**

| Emisiones | CO | SO<br>X | NO<br>X | MP<br>2,5 Total | MP<br>10 Total | MPS |
| --- | --- | --- | --- | --- | --- | --- |
| ton/año | 5,60 | 1,51 | 21,93 | 7,10 | 39,97 | 150,40 |
| g/m2-s | 0,00000296 | 0,00000080 | 0,00001159 | 0,00000375 | 0,00002112 | 0,00007949 |

<!-- Estadísticas: 2 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. Cabe destacar, que las tasas de emisión presentadas en la Tabla 25, corresponden al total de las emisiones generadas por el proyecto, por lo que se está considerando que todas las -->
<!-- FIN TABLA 25 -->


En Figura 2, que se presenta a continuación, se muestra un mapa a escala 1:100.000, con
coordenadas (UTM SIRGA WGS 84 Huso 19S) y la ubicación de las isolíneas de
concentración de las emisiones atmosféricas analizadas en este informe (Tabla 24) y de

<!-- INICIO TABLA 24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.** **RESUMEN DE EMISIONES** A continuación, se describen un resumen de las emisiones en la fase de operación del proyecto para cada una de las actividades realizadas. -->

**Tabla 24: Resumen de Emisiones por actividad**

| Actividades | Emisiones Atmosféricas (ton/año) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Actividades | CO | HC | SOX | NOX | MP2,5<br>comb | MP10<br>comb | MP2,5<br>resus | MP10<br>resus | MPS <br>resus | MP2,5<br>total | MP10<br>total | MPS <br>total |
| Escarpe | - | - | - | - | - | - | 0,05 | 0,24 | 0,38 | 0,05 | 0,24 | 0,38 |
| Extracción | - | - | - | - | - | - | 1,65 | 2,55 | 15,74 | 1,65 | 2,55 | 15,74 |
| Transferencia de<br>material | - | - | - | - | - | - | 0,09 | 0,62 | 1,32 | 0,09 | 0,62 | 1,32 |
| Erosión de material en<br>acopio | - | - | - | - | - | - | 0,09 | 0,30 | 0,59 | 0,09 | 0,30 | 0,59 |
| Erosión por camión<br>sin cubierta | - | - | - | - | - | - | 0,10 | 0,69 | 0,69 | 0,10 | 0,69 | 0,69 |
| Harnero | - | - | - | - | - | - | 0,01 | 0,08 | 0,24 | 0,01 | 0,08 | 0,24 |
| Cintas<br>transportadoras | - | - | - | - | - | - | 0,12 | 0,12 | 0,33 | 0,12 | 0,12 | 0,33 |
| Circulación de<br>vehículos en caminos<br>no pavimentados | - | - | - | - | - | - | 3,36 | 33,57 | 131,16 | 3,36 | 33,57 | 131,16 |
| Combustión vehículos | 0,14 | 0,03 | 0,01 | 0,51 | 0,01 | 0,01 | - | - | - | 0,01 | 0,01 | - |
| Combustión<br>maquinaria fuera de<br>ruta | 4,77 | 2,18 | 1,28 | 18,20 | 1,40 | 1,56 | - | - | - | 1,40 | 1,56 | - |
| Grupo Electrógeno | 0,69 | - | 0,21 | 3,21 | 0,21 | 0,23 | - | - | - | 0,21 | 0,23 | - |
| **Emisiones Totales**<br>**(ton/año)** | **5,60** | **2,21** | **1,51** | **21,93** | **1,63** | **1,80** | **5,47** | **38,17** | **150,4** | **7,10** | **39,97** | **150,4** |

<!-- Estadísticas: 13 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia 18 -->
<!-- FIN TABLA 24 -->

sus potenciales receptores.

b [Red Agrometeorológica de INIA Agromet, http://agromet.inia.cl](http://agromet.inia.cl/)
c https://www.meteoblue.com/es/weather
maps/porvenir_chile_3875367?variable=wind_streamlines&level=surface&lines=none&mapcenter=-53.6251N70.4553&zoom=7

24

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**2.** **CONCLUSIONES**

En la Tabla 24, se observan los valores alcanzados por las emisiones anuales asociadas a
cada una de las fuente emisora de contaminantes, además de las emisiones totales,
considerando que todas las actividades operarán al mismo tiempo, extracción de áridos,
traslado y selección, para de esta forma obtener la situación más desfavorable asociada a
la operación del proyecto.

En cuanto a las emisiones de material particulado resuspendido (MPS, MP 10 y MP 2,5 ) la
mayor generación provienen de la circulación vehicular y extracción de material, que en
conjunto suman un total de 150,4 ton/año, 39,9 ton/año y 7,1 ton/año respectivamente. A
sí mismo, los gases producto de la combustión (SO X, CO y HC) de camiones, maquinarias
y grupos electrógenos, son emisiones relativamente bajas, con excepción de las emisiones
NO X, que alcanzan los 21,9 ton/año, generadas principalmente por la combustión de
maquinaria, que alcanzan casi el 83% de las emisiones. Lo anterior ya que funcionarán
simultáneamente 8 horas al día 285 días al año.

Por otra parte, en la Tabla 27, se pueden observar los valores de las concentraciones de
dispersión de los contaminantes, modelados mediante SCREEN 3, en el cual se consideró
la operación de todas las actividades a la vez, en una superficie de 12 ha, por un periodo
de tiempo de 1 año. Al respecto se aprecia que los puntos de máxima concentración
aportadas por el proyecto, se presentará a una distancia 100 m, alrededor de la fuente
emisora. En tanto, que en la Tabla 30, se estableció que ninguno de estos contaminantes
sobrepasará el umbral de sus correspondientes normas, por lo que su aporte de emisiones
a la atmósfera, no afectará de forma significativa a la calidad del aire del sector.

Sin embargo, de todos los contaminantes analizados, las concentraciones de MPS,
presenta el mayor porcentaje respecto de límite establecido por su norma de calidad,
alcanzando los 101,68 μg/m [3] N, como concentración máxima de 24 horas, correspondiente
al 50,84%, del valor límite de la norma (200 μg/m [3] N, según Norma Secundaria de Calidad
del Aire del Ambiente de la Confederación Suiza), la que se presentará a 100 m de la
fuente. Sin embargo, el receptor potencialmente más afectado, por ser el que se
encontrará más cercano al proyecto, se localizará a una distancia de 15.000 m de la
fuente, presentando una concentración aportante de 10,75 μg/m [3] N, equivalente a 5,37 %
de la Norma Secundaria de Calidad del Aire del Ambiente de la Confederación Suiza.

Finalmente y de acuerdo a los resultados aquí descritos, se puede concluir que las
emisiones asociadas al proyecto extracción de áridos “Aurora”, son bajas y en ningún caso
producirán efectos adversos significativos en la calidad del aire, que afecten a la salud de
las personas o la calidad de los recursos naturales del sector, aun considerando las peores
condiciones de emisión y meteorológicas. Así mismo, y por esta misma razón no se
requerirá en este análisis, la utilización de otro modelo más complejo.

26

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**3.** **RECOMENDACIONES**

Durante la operación del proyecto, se recomienda aplicar las siguientes medidas de
control, con el objetivo de reducir la emisión de polvos fugitivos generado por las
actividades del proyecto.

 Humectar los caminos internas y de acceso no pavimentadas, así como el material en
pilas, acopio, mediante riego periódico, siempre y cuando las condiciones climáticas
así lo ameriten (durante época estival regar con mayor frecuencia y en periodos de
lluvia no realizar humectación).

 Realizar mantenciones periódicas preventivas a maquinarias y equipos utilizados en el
recinto, para verificar su correcto funcionamiento y mantener su documentación al
día, en la instalación de faena, para una posterior fiscalización.

 - Evitar mantener vehículos y maquinarias, con sus motores encendidos
innecesariamente. Especialmente durante los momentos en los que no se realicen
faenas.

 Transportar en camiones con la tolva cubierta mediante lona hermética, impermeable
y sujeta a la carrocería, todo el material trasladado a través de la vía pública, y que
generen dispersión de contaminantes. Además, monitorear regularmente que todos
los vehículos utilizados en esta faena se encuentren con sus mantenciones y revisión
técnica al día.

 Limitar la velocidad de circulación de los vehículos a 30 km/h, en las vías internas no
pavimentadas del recinto y restringir la circulación de las maquinarias sólo a los
frentes de trabajo.

27

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

**4.** **BIBLIOGRAFÍA**

1) Compilation of Air Pollutant Emission Factors, AP 42. Actualizada por EPA en su sitio

Web en diciembre 2011.

2) Guía Metodológica Inventario de Emisiones Atmosféricas, M11 Metodología SINCA

2011 Ambiosis S.A., Octubre 2011.

3) Industria del Árido en Chile, Tomo I, Sistematización de Antecedentes Técnicos y

Ambientales, Corporación de Desarrollo Tecnológico, Comisión Nacional del Árido.
Santiago, Diciembre de 2001.

4) Informe Final, “Servicio de Recopilación y Sistematización de Factores de Emisión al

Aire para el Servicio de Evaluación Ambiental”, de mayo 2015.

5) Reconciling Urban Fugitive Dust Emissions Inventory and Ambient Source Contribution

Estimates: Summary of Current Knowledge and Needed Research, del Desert
Research Institute (2000), publicado por la Universidad University and Community
College System of Nevada.

28

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

# ANEXO I MEMORIA DE CALCULO DE EMISIONES

29

**Emisiones Atmosféricas Desagregadas**

**Aurora**

**Resuspensión de MP por Movimiento de Material**

|Escarpe|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|~~**FE**~~**MP2,5**~~** (kg/km)**~~|**1,140**||~~**FE**~~**MP10**~~** (kg/km)**~~|**5,7**||~~**FE**~~**MP30**~~** (kg/km)**~~|**8,906**|
|Superficie a recorrer (ha)|12,00|12,00|Superficie a recorrer (ha)|12,00|12,00|Superficie a recorrer (ha)|12,00|
|Recorrido de Maquinaria (km/ha)|3,57|3,57|Recorrido de Maquinaria (km/ha)<br>|3,57|3,57|Recorrido de Maquinaria (km/ha)|3,57|
|**Fa (km/año)**<br>|**42,840**|**42,840**|**Fa (km/año)**<br>|**42,840**|**42,840**|**Fa (km/año)**<br>|**42,840**|
|~~**Emisión MP**~~**2,5**~~** (ton/año)**~~|**0,049**|**0,049**|~~**Emisión MP**~~**10**~~** (ton/año)**~~|**0,244**|**0,244**|~~**Emisión MP**~~**30**~~** (ton/año)**~~|**0,382**|

|Extracción|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Contenido de fino s (%)|3,9||~~Fino del suelo s (%)~~<br>|3,9||~~Fino del suelo s (%)~~<br>|3,9|
|Humedad del suelo M (%)<br>|6,5|6,5|~~Humedad del suelo M (%)~~<br>|6,5|6,5|~~Humedad del suelo M (%)~~<br>|6,5|
|~~**FE**~~**MP2,5**~~** (kg/h)**~~|**0,123**|**0,123**|~~**FE**~~**MP10**~~** (kg/h)**~~|**0,189**|**0,189**|~~**FE**~~**MP30**~~** (kg/h)**~~|**1,168**|
|N° maquinarias|3|3|N° maquinarias<br>|3|3|N° maquinarias|3|
|Horas de funcionamiento (c/u)|4.491|4.491|Horas de funcionamiento (c/u)|4.491|4.491|Horas de funcionamiento (c/u)|4.491|
|**Fa (h/año)**<br>|**13.473**|**13.473**|**Fa (h/año)**<br>|**13.473**|**13.473**|**Fa (h/año)**<br>|**13.473**|
|~~**Emisión MP**~~**2,5**~~** (ton/año)**~~|**1,652**|**1,652**|~~**Emisión MP**~~**10**~~** (ton/año)**~~|**2,548**|**2,548**|~~**Emisión MP**~~**30**~~** (ton/año)**~~|**15,737**|

|Transferencia de material (carguío y volteo de camión)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Velocidad del viento U ( m/s)|4,7||Velocidad del viento U ( m/s)|4,7||Velocidad del viento U ( m/s)|4,7|
|Humedad del suelo M (%)<br>|6,5|6,5|Humedad del suelo M (%)<br>|6,5|6,5|Humedad del suelo M (%)<br>|6,5|
|~~**FE**~~**MP2,5**~~** (kg/ton)**~~<br>|**0,00004**|**0,00004**|~~**FE**~~**MP10**~~** (kg/ton)**~~|**0,00029**|**0,00029**|~~**FE**~~**MP30**~~** (kg/ton)**~~<br>|**0,00060**|
|~~Densidad de material (ton/m3)~~<br>|1,50|1,50|Densidad de material (ton/m~~3~~)<br><br>|1,50|1,50|Densidad de material (ton/m~~3~~)<br>|1,50|
|~~Cantidad de material (m3)~~|485.035|485.035|Cantidad de material (m~~3~~)|485.035|485.035|Cantidad de material (m~~3~~)|485.035|
|**Fa (ton/año)**<br>|**2.182.657**|**2.182.657**|**Fa (ton/año)**<br>|**2.182.657**|**2.182.657**|**Fa (ton/año)**<br>|**2.182.657**|
|~~**Emisión MP**~~**2,5**~~** (ton/año)**~~|**0,095**|**0,095**|~~**Emisión MP**~~**10**~~** (ton/año)**~~|**0,624**|**0,624**|~~**Emisión MP**~~**30**~~** (ton/año)**~~|**1,319**|

|Erosión de material en pila, acopios|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Tiempo que exede los 5,4 m/s f (%)|37,8||~~Tiempo que exede los 5,4 m/s f (%)~~|37,8||~~Tiempo que exede los 5,4 m/s f (%)~~<br>|37,8|
|Contenido de fino s (%)<br>|3,9<br>|3,9<br>|~~Contenido de fino s (%)~~|3,9|3,9|~~Contenido de fino s (%)~~<br>|3,9|
|~~**FE**~~**MP2,5**~~** (kg/ha)**~~|~~**1,868**~~|~~**1,868**~~|~~**FE**~~**MP10**~~** (kg/ha)**~~<br>|**6,227**|**6,227**|~~**FE**~~**MP30**~~** (kg/ha)**~~|**12,453**|
|Tiempo ocupación (día/año)|365|365|~~Tiempo ocupación (día/año)~~|365|365|~~Tiempo ocupación (día/año)~~<br><br>|365|
|Superficie expuesta (ha/día)|0,130|0,130|~~Superficie expuesta (ha/día)~~<br>|0,130|0,130|~~Superficie expuesta (ha/día)~~<br>|0,130|
|**Fa (ha/año)**<br>|**47,497**|**47,497**|~~**Fa (ha/año)**~~|**47,497**|**47,497**|~~**Fa (ha/año)**~~<br>|**47,497**|
|~~**Emisión MP**~~**2,5**~~** (ton/año)**~~|**0,0887**|**0,0887**|~~**Emisión MP**~~**10**~~** (ton/año)**~~|**0,2957**|**0,2957**|~~**Emisión MP**~~**30**~~** (ton/año)**~~|**0,5915**|

**Erosión por camión sin cubierta**

velocidad del camión (km/h) 40 velocidad del camión (km/h) 40 velocidad del camión (km/h) 40
**FE** **MP2,5** **(kg/m2/h)** **0,0003** **FE** **MP10** **(kg/m2/h)** **0,0020** **FE** **MP10** **(kg/m2/h)** **0,0020**
Tiempo exposición (h/año) 1.140 Tiempo exposición (h/año) 1.140 Tiempo exposición (h/año) 1.140
Superficie expuesta (m2/h) 300,0 Superficie expuesta (m2/h) 300,0 Superficie expuesta (m2/h) 300,0
**Fa (m2/año)** **342.000** **Fa (m2/año)** **342.000** **Fa (m2/año)** **342.000**
**Emisión MP** **2,5** **(ton/año)** **0,1030** **Emisión MP** **10** **(ton/año)** **0,6868** **Emisión MP** **10** **(ton/año)** **0,6868**

|velocidad del camión (km/h)|40|
|---|---|
|~~**FE**~~**MP2,5**~~** (kg/m2/h)**~~|**0,0003**|
|Tiempo exposición (h/año)|1.140|
|Superficie expuesta (m2/h)|300,0|
|**Fa (m2/año)**<br>|**342.000**|
|~~**Emisión MP**~~**2,5**~~** (ton/año)**~~|**0,1030**|

|velocidad del camión (km/h)|40|
|---|---|
|~~**FE**~~**MP10**~~** (kg/m2/h)**~~<br>|**0,0020**|
|~~Tiempo exposición (h/año)~~<br>|1.140|
|~~Superficie expuesta (m2/h)~~<br>|300,0|
|~~**Fa (m2/año)**~~<br>|**342.000**|
|~~**Emisión MP**~~**10**~~** (ton/año)**~~|**0,6868**|

|velocidad del camión (km/h)|40|
|---|---|
|~~**FE**~~**MP10**~~** (kg/m2/h)**~~<br>|**0,0020**|
|~~Tiempo exposición (h/año)~~<br>|1.140|
|~~Superficie expuesta (m2/h)~~<br>|300,0|
|~~**Fa (m2/año)**~~<br>|**342.000**|
|~~**Emisión MP**~~**10**~~** (ton/año)**~~|**0,6868**|

|Harnero|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|~~**FE**~~**MP2,5**~~** (kg/ton)**~~<br>|**0,00003**||~~**FE**~~**MP10**~~** (kg/ton)**~~<br>|**0,00037**||~~**FE**~~**MP30**~~** (kg/ton)**~~|**0,00110**|
|Cantidad de material (m~~3~~/año)<br>|145.510|145.510|Cantidad de material (m~~3~~/año)<br>|145.510|145.510|Cantidad de material (m~~3~~/año)<br><br>|145.510|
|Densidad del material (ton/m~~3~~)|1,5|1,5|Densidad del material (ton/m~~3~~)|1,5|1,5|Densidad del material (ton/m~~3~~)|1,5|
|**Fa (ton/año)**<br>|**218.266**|**218.266**|~~**Fa (ton/año)**~~<br><br>|**218.266**|**218.266**|~~**Fa (ton/año)**~~<br><br>|**218.266**|
|~~**Emisión MP**~~**2,5**~~** (ton/año)**~~|**0,0055**|**0,0055**|~~**Emisión MP**~~**10**~~** (ton/año)**~~|**0,0808**|**0,0808**|~~**Emisión MP**~~**30**~~** (ton/año)**~~|**0,2401**|

|Cintas transportadoras|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|~~**FE**~~**MP2,5**~~** (kg/ton)**~~<br>|**0,0006**||~~**FE**~~**MP10**~~** (kg/ton)**~~<br>|**0,0006**|
|Cantidad de material (m~~3~~/año)<br>|145.510|145.510|Cantidad de material (m~~3~~/año)|145.510|
|Densidad del material (ton/m~~3~~)|1,5|1,5|Densidad del material (ton/m~~3~~)<br><br>|1,5|
|**Fa (ton/año)**<br>|**218.266**|**218.266**|~~**Fa (ton/año)**~~|**218.266**|
|~~**Emisión MP**~~**2,5**~~** (ton/año)**~~|**0,1200**|**0,1200**|~~**Emisión MP**~~**10**~~** (ton/año)**~~|**0,1200**|

|Col1|Col2|
|---|---|
|~~**FE**~~**MP30**~~** (kg/ton)**~~<br>|**0,0015**|
|Cantidad de material (m~~3~~/año)|145.510|
|Densidad del material (ton/m~~3~~)<br><br>|1,5|
|~~**Fa (ton/año)**~~|**218.266**|
|~~**Emisión MP**~~**30**~~** (ton/año)**~~|**0,3274**|

|Resuspensión de MP por circulación de vehículos pesados en vías no pavimentadas|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Materiales|Porcentaje<br>Finos<br>s (%)|Peso<br>promedio W<br>(ton)|**FEMP2,5**<br>**(g/km)**|**FEMP10**<br>**(g/km)**|**FEMP30**<br>**(g/km)**|Volumen<br>(m3)|Densidad<br>(ton/m3)|Capacidad<br>del Vehiculo<br>(ton)|Tipo de<br>vehiculo|No de viajes<br>(ida y<br>vuelta)|Distancia<br>recorrida<br>(km)|**Fa**<br>**(km/año)**|**Ea (%)**|**E MP2,5**<br>**(ton/año)**|**E MP10**<br>**(ton/año)**|**E MP30**<br>**(ton/año)**|
|Zona de extracción y acopio|4,9|24,60|** 32,1**|** 321,3**|** 1.255,4**|485.035|1,5|30,0|C. Tolva|48.503|1,42|** 68.875**|** 68,7**|** 0,6926**|** 6,9261**|** 27,0640**|
|Tránsito Maquinaria|4,9|24,60|** 32,1**|** 321,3**|** 1.255,4**|485.035|1,5|3,9|Maquinaria|373.104|0,71|** 264.904**|** 68,7**|** 2,6639**|** 26,6390**|** 104,0925**|
|**Emisión (ton/año)**|** -**|** -**|** -**|** -**||** -**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** 3,3565**|** 33,5651**|** 131,1565**|

|Combustión vehículos|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Vehículo<br>|Velocidad<br>(km/h)|**Fa**<br>**(km/año)**|**FECO**<br>**(g/km)**|**FEHC**<br>**(g/km)**|**FESOX**<br>**(g/km)**|**FENOX**<br>**(g/km)**|**FEMP2,5**<br>**(g/km)**|**FEMP10**<br>**(g/km)**|**E CO**<br>**(ton/año)**|**E HC**<br>**(ton/año)**|**E SOX**<br>**(ton/año)**|**E NOX**<br>**(ton/año)**|**E MP2,5**<br>**(ton/año)**|**E MP10**<br>**(ton/año)**|
|~~Camión Tolva~~|40|** 68.875**|** 1,971**|** 0,436**|** 0,193**|** 7,475**|** 0,168**|** 0,183**|** 0,1358**|** 0,0300**|** 0,0133**|** 0,5148**|** 0,0116**|** 0,0126**|
|**Emisión (ton/año)**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** 0,1358**|** 0,0300**|** 0,0133**|** 0,5148**|** 0,0116**|** 0,0126**|

|Combustión maquinaria fuera de ruta|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Equipos|Cantidad|Potencia<br>(kW)|Tiempo<br>Operación<br>(h/año)|**FA**<br>**(kWh/año)**|**FECO**<br>**(g/kWh)**|**FEHC**<br>**(g/kWh)**|**FESOX**<br>**(g/kWh)**|**FENOX**<br>**(g/kWh)**|**FEMP2,5**<br>**(g/kWh)**|**FEMP10**<br>**(g/kWh)**|**E CO**<br>**(ton/año)**|**E HC**<br>**(ton/año)**|**E SOX**<br>**(ton/año)**|**E NOX**<br>**(ton/año)**|**E MP2,5**<br>**(ton/año)**|**E MP10**<br>**(ton/año)**|
|Cargador Frontal|2|98|2.280|** 446.880**|** 3,76**|** 1,72**|** 0,88**|** 14,36**|** 1,11**|** 1,23**|** 1,680**|** 0,769**|** 0,394**|** 6,417**|** 0,495**|** 0,550**|
|Excavadora|3|120|2.280|** 820.800**|** 3,76**|** 1,72**|** 1,08**|** 14,36**|** 1,11**|** 1,23**|** 3,086**|** 1,412**|** 0,886**|** 11,787**|** 0,909**|** 1,010**|
|**Emisión (ton/año)**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** 4,766**|** 2,180**|** 1,281**|** 18,204**|** 1,403**|** 1,559**|

|Combustión Grupos Electrógenos|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Equipos|Cantidad|Combustibl<br>e|Potencia<br>(kW)|Tiempo<br>Operación<br>(h/año)|**FA (kWh/año)**|**FECO**<br>**(kg/kWh)**|**FESOX**<br>**(kg/kWh)**|**FENOX**<br>**(kg/kWh)**|**FEMP2,5**<br>**(kg/kWh)**|**FEMP10**<br>**(kg/kWh)**|**E CO**<br>**(ton/año)**|**E SOX**<br>**(ton/año)**|**E NOX**<br>**(ton/año)**|**E MP2,5**<br>**(ton/año)**|**E MP10**<br>**(ton/año)**|
|Grupo Electrógeno|1|Diesel|75|2.280|** 171.000**|**0,0041**|**0,0013**|**0,0188**|**0,0012**|**0,0013**|** 0,6943**|** 0,2138**|** 3,2148**|** 0,2108**|** 0,2291**|
|**Emisión (ton/año)**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** -**|** 0,6943**|** 0,2138**|** 3,2148**|** 0,2108**|** 0,2291**|

|Total Emisiones Atmosféricas Operación del Proyecto|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**CO**<br>**(ton/año)**|**HC**<br>**(ton/año)**|**SOX**<br>**(ton/año)**|**NOX**<br>**(ton/año)**|**MP2,5 Comb**<br>**(ton/año)**|**MP10 Comb**<br>**(ton/año)**|**MP2,5 Resus**<br>**(ton/año)**|**MP10 Resus**<br>**(ton/año)**|**MP30 Resus**<br>**(ton/año)**|**MP2,5 Total**<br>**(ton/año)**|**MP10 Total**<br>**(ton/año)**|**MP30 Total**<br>**(ton/año)**|
|**5,597**|**2,210**|**1,508**|**21,934**|**1,626**|**1,801**|**5,470**|**38,165**|**150,441**|**7,095**|**39,966**|**150,441**|

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

# ANEXO II MEMORIA MODELO SCREEN

30

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

31

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

32

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

33

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

34

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

35

Informe Estimación y Modelación

de Emisiones Atmosférica

Proyecto Aurora

36

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Coordenadas del Proyecto**

| Punto | Y | X | Punto | Y | X |
| --- | --- | --- | --- | --- | --- |
| V-1 | 4.099.226,15 | 507.723,46 | V-9 | 4.099.326,01 | 507.725,75 |
| V-2 | 4.099.215,86 | 507.917,64 | V-10 | 4.099.280,64 | 507.493,22 |
| V-3 | 4.099.112,00 | 507.922,00 | V-11 | 4.099.131,93 | 507.210,12 |
| V-4 | 4.099.123,00 | 508.007,00 | V-12 | 4.099.123,20 | 507.167,97 |
| V-5 | 4.099.082,00 | 508.015,00 | V-13 | 4.099.002,20 | 507.192,54 |
| V-6 | 4.099.091,00 | 508.087,00 | V-14 | 4.099.048,69 | 507.397,98 |
| V-7 | 4.099.172,00 | 508.068,00 | V-15 | 4.099.168,10 | 507.521,99 |
| V-8 | 4.099.311,17 | 508.008,79 | - | - | - |

**Tabla 2: Factor de emisión por Escarpe**

| Factor de Emisión (kg/km) | Col2 | Col3 |
| --- | --- | --- |
| MPS | MP10 | MP2,5 |
| 8,906 | 5,7 | 1,140 |

**Tabla 3: Emisión por Escarpe**

| Factor de Emisión (kg/km) | Col2 | Col3 | Nivel de Actividad<br>(km/año) | Emisión (ton/año) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| MPS | MP10 | MP2,5 | 42,840 | MPS | MP10 | MP2,5 |
| 8,906 | 5,7 | 1,140 | 1,140 | 0,382 | 0,244 | 0,049 |

**Tabla 4: Factor de emisión por Excavación**

| Contaminante | Fórmula (kg/h) | Parámetro | Valor |
| --- | --- | --- | --- |
| MPS | <br> | K: factor de partícula | 1 |
| MPS | <br> | S: % de fino | 3,9 |
| MPS | <br> | M: Humedad del material (%) | 6,5 |
| MP10 | <br> | K: factor de partícula | 0,75 |
| MP10 | <br> | S: % de fino | 3,9 |
| MP10 | <br> | M: Humedad del material (%) | 6,5 |
| MP2,5 | <br> | K: factor de partícula | 0,105 |
| MP2,5 | <br> | S: % de fino | 3,9 |
| MP2,5 | <br> | M: Humedad del material (%) | 6,5 |

**Tabla 5: Emisión por Excavación**

| Contaminante | FE (kg/h) | NA (h) | Emisión (ton/año) |
| --- | --- | --- | --- |
| MPS | 0,556 | 13.473 | 15,737 |
| MP10 | 0,075 | 0,075 | 2,548 |
| MP2,5 | 0,058 | 0,058 | 1,652 |

**Tabla 6: Factor de emisión por Transferencia de Material**

| Contaminante | Fórmula (kg/ton) | Parámetros | Valor |
| --- | --- | --- | --- |
| MPS | <br>( <br> )<br> <br>( <br> ~~)~~<br> | K: factor de partícula | 0,74 |
| MPS | <br>( <br> )<br> <br>( <br> ~~)~~<br> | U: velocidad del viento (m/s) | 4,7 |
| MPS | <br>( <br> )<br> <br>( <br> ~~)~~<br> | M: Humedad del material (%) | 6,5 |
| MP10 | <br>( <br> )<br> <br>( <br> ~~)~~<br> | K: factor de partícula | 0,35 |
| MP10 | <br>( <br> )<br> <br>( <br> ~~)~~<br> | U: velocidad del viento (m/s) | 4,7 |
| MP10 | <br>( <br> )<br> <br>( <br> ~~)~~<br> | M: Humedad del material (%) | 6,5 |
| MP2,5 | <br>( <br> )<br> <br>( <br> ~~)~~<br> | K: factor de partícula | 0,053 |
| MP2,5 | <br>( <br> )<br> <br>( <br> ~~)~~<br> | U: velocidad del viento (m/s) | 4,7 |
| MP2,5 | <br>( <br> )<br> <br>( <br> ~~)~~<br> | M: Humedad del material (%) | 6,5 |

**Tabla 7: Emisión por Transferencia de Material**

| Contaminante | FE (kg/ton) | NA (ton/año) | Emisión (ton/año) |
| --- | --- | --- | --- |
| MPS | 0,00060 | 2.182.657 | 1,319 |
| MP10 | 0,00029 | 0,00029 | 0,624 |
| MP2,5 | 0,00004 | 0,00004 | 0,095 |

**Tabla 8: Factor de emisión por Erosión de Material**

| Contaminante | Fórmula (kg/ha) | Parámetros | Valor |
| --- | --- | --- | --- |
| MPS | <br> <br> | K: factor de partícula | 1 |
| MPS | <br> <br> | S: % de fino | 3,9 |
| MPS | <br> <br> | f: tiempo que excede los 5,4 m/s (%) | 37,8 |
| MP10 | <br> <br> | K: factor de partícula | 0,5 |
| MP10 | <br> <br> | S: % de fino | 3,9 |
| MP10 | <br> <br> | f: tiempo que excede los 5,4 m/s (%) | 37,8 |
| MP2,5 | <br> <br> | K: factor de partícula | 0,15 |
| MP2,5 | <br> <br> | S: % de fino | 3,9 |
| MP2,5 | <br> <br> | f: tiempo que excede los 5,4 m/s (%) | 37,8 |

**Tabla 9: Emisión por Erosión de Material**

| Contaminante | FE (kg/ha) | NA (ha/año) | Emisión (ton/año) |
| --- | --- | --- | --- |
| MPS | 12,453 | 47,497 | 0,5915 |
| MP10 | 6,227 | 6,227 | 0,2957 |
| MP2,5 | 1,868 | 1,868 | 0,0887 |

**Tabla 10: Emisión por Erosión de Material por tránsito sin cubierta**

| Contaminante | Fórmula (lb/yd2/h) | Parámetros | Valor |
| --- | --- | --- | --- |
| MPS |  | K: factor de partícula | 1 |
| MPS |  | U: velocidad del vehículo (km/h) | 40 |
| MP10 |  | K: factor de partícula | 1 |
| MP10 |  | U: velocidad del vehículo (km/h) | 40 |
| MP2,5 |  | K: factor de partícula | 0,15 |
| MP2,5 |  | U: velocidad del vehículo (km/h) | 40 |

**Tabla 11: Emisión por Erosión de Material por camión sin cubierta**

| Contaminante | FE (kg/m2/h) | NA (m2/año) | Emisión (ton/año) |
| --- | --- | --- | --- |
| MPS | 0,0020 | 342.000 | 0,6868 |
| MP10 | 0,0020 | 0,0020 | 0,6868 |
| MP2,5 | 0,0003 | 0,0003 | 0,1030 |

**Tabla 12: Factores de Emisión para procesamiento de material**

| Actividad | MPS | MP<br>10 | MP<br>2,5 |
| --- | --- | --- | --- |
| Harnero | 0,00110 | 0,00037 | 0,00003 |
| Cintas Transportadoras | 0,0015 | 0,0006 | 0,0006 |

**Tabla 13: Emisiones del Procesamiento de material**

| Actividad | FE (kg/ton) | Col3 | Col4 | Volumen<br>(m3/año) | NA<br>(ton/año) | Emisión (ton/año) | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Actividad | MPS | MP10 | MP2,5 | MP2,5 | MP2,5 | MPS | MP10 | MP2,5 |
| Harnero | 0,00110 | 0,00037 | 0,00003 | 145.510 | 218.266 | 0,2401 | 0,0808 | 0,0055 |
| Cintas<br>Transportadoras | 0,0015 | 0,0006 | 0,0006 | 0,0006 | 0,0006 | 0,3274 | 0,1200 | 0,1200 |

**Tabla 14: Emisión por tránsito en camino no pavimentado**

| Contaminante | Fórmula (g/km) | Parámetros | Valor | FE (g/km) |
| --- | --- | --- | --- | --- |
| MPS | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | K: factor de partícula | 49 | 1.260,0 |
| MPS | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | S: % de fino | 4,9 | 4,9 |
| MPS | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | W: peso promedio (ton) | 24,8 | 24,8 |
| MP10 | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | K: factor de partícula | 1,5 | 322,5 |
| MP10 | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | S: % de fino | 4,9 | 4,9 |
| MP10 | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | W: peso promedio (ton) | 24,8 | 24,8 |
| MP2,5 | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | K: factor de partícula | 0,15 | 32,2 |
| MP2,5 | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | S: % de fino | 4,9 | 4,9 |
| MP2,5 | ( <br> )<br> <br> ~~(~~ <br> ~~)~~<br> <br> | W: peso promedio (ton) | 24,8 | 24,8 |

**Tabla 15: Peso promedio en vías no pavimentadas**

| Materiales | Tipo de<br>vehículo | Capacidad<br>Vehículo<br>(ton) | Tara<br>(ton) | Peso Bruto<br>(ton) | Peso Wi<br>(ton) | Recorrido<br>(km/año) | Fracción W<br>(ton) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Zona de extracción a acopio | <br> C. Tolva | 30,0 | 15,00 | 45,00 | 30,00 | 64.510 | 7,08 |
| Transito Maquinaria | Maquinaria | 3,9 | 21,25 | 25,15 | 23,20 | 208.938 | 17,73 |
| Emisiones Totales | - | **-** | **-** | **-** | **-** | **273.448** | **24,8** |

**Tabla 16: Nivel de Actividad y Emisiones por resuspensión en camino no pavimentado**

| Materiales | Volumen<br>(m3) | No de<br>viajes<br>(ida y<br>vuelta) | Distancia<br>recorrida<br>(km) | NA<br>(km/año) | Ea (%) | Emisión (ton/año) | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Materiales | Volumen<br>(m3) | No de<br>viajes<br>(ida y<br>vuelta) | Distancia<br>recorrida <br>(km) | NA<br>(km/año) | Ea (%) | MP2,5 | MP10 | MPS |
| Zona de extracción a acopio | 485.035 | 48.503 | 1,42 | 68.875 | 68,7 | 0,6926 | 6,9261 | 27,0640 |
| Transito Cargador Frontal | 485.035 | 373.104 | 0,71 | 264.904 | 68,7 | 2,6639 | 26,6390 | 104,0925 |
| Emisión total | - | - | - | - | - | 3,3565 | 33,5651 | 131,1565 |

**Tabla 17: Factor de emisión generados por la combustión vehicular**

| Fuente de Emisión | Contaminante | FE (g/km ) |
| --- | --- | --- |
| Camiones pesados<br>diesel tipo III | CO | (1,24588358438859+(103,700537481749/(1+exp((((-1)*-<br>1,3906312471446)+(0,543451750078654*ln(V)))+(0,039006642599818<br>9*V))))) |
| Camiones pesados<br>diesel tipo III | HC | ((0,135938586321894+(0,71588074810547*exp(((-<br>1)*0,0234666513590177)*V)))+(2,79878282504916*exp(((-<br>1)*0,123459782380517)*V))) |
| Camiones pesados<br>diesel tipo III | NOx | ((5,58300975720938+(14,5724996214701*exp(((-<br>1)*0,0510403515051286)*V)))+(45,651882800859*exp(((-<br>1)*0,309240087785118)*V))) |
| Camiones pesados<br>diesel tipo III | MP | ((0,100820480611018+(0,424449762706025*exp(((-<br>1)*0,0416436785215947)*V)))+(0,864328026775096*exp(((-<br>1)*0,159945936589218)*V))) |
| Camiones pesados<br>diesel tipo III | CC | ((199,101296810716+(496,037924788222*exp(((-<br>1)*0,0466183266185801)*V)))+(3798,31076366067*exp(((-<br>1)*0,573715458508514)*V)))*2*0,0015<br> |

**Tabla 18: Nivel de actividad por camiones**

| Vehículo | Velocidad (km/h) | NA (km/año) |
| --- | --- | --- |
| Camión Tolva | 40 | 68.875 |

**Tabla 19: Emisiones por combustión de camiones en Camino no pavimentado**

| Fuente de Emisión | Contaminante | FE (g/km ) | NA (km/año) | Emisión (ton/año) |
| --- | --- | --- | --- | --- |
| Camiones pesados<br>diesel tipo III | CO | 1,971 | 68.875 | 0,1358 |
| Camiones pesados<br>diesel tipo III | HC | 0,436 | 0,436 | 0,0300 |
| Camiones pesados<br>diesel tipo III | SOX | 0,193 | 0,193 | 0,0133 |
| Camiones pesados<br>diesel tipo III | NOX | 7,475 | 7,475 | 0,5148 |
| Camiones pesados<br>diesel tipo III | MP10 | 0,168 | 0,168 | 0,0116 |
| Camiones pesados<br>diesel tipo III | MP2,5 | 0,183 | 0,183 | 0,0126 |

**Tabla 20: Factor de Emisión por Maquinaria fuera de ruta**

| Maquinaria | Cantidad | Potencia<br>(kW) | Factores de Emisión (g/kW-h) | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Maquinaria | Cantidad | Potencia<br>(kW) | CO | HC | SO2<br>(*) | NOX | MP2,5 | MP10 |
| Cargador Frontal | 2 | 98 | 3,76 | 1,72 | 0,88 | 14,36 | 1,11 | 1,23 |
| Excavadora | 3 | 120 | 3,76 | 1,72 | 1,08 | 14,36 | 1,11 | 1,23 |

**Tabla 21: Emisión por Maquinaria fuera de ruta**

| Maquinaria | Tiempo<br>Operación<br>(h/año) | NA<br>(kWh/año) | Emisión (ton/año) | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Maquinaria | Tiempo<br>Operación<br>(h/año) | NA<br>(kWh/año) | CO | HC | SO2 | NOX | MP2,5 | MP10 |
| Retroexcavadora | 2.280 | 446.880 | 1,680 | 0,769 | 0,394 | 6,417 | 0,495 | 0,550 |
| Excavadora | 2.280 | 820.800 | 3,086 | 1,412 | 0,886 | 11,787 | 0,909 | 1,010 |
| Emisión total | - | - <br> | 4,766<br> | 2,180<br> | 1,281 | 18,204 | 1,403 | 1,559 |

**Tabla 22: Factores de Emisión por Grupos Electrógenos**

| Combustible | Unidad | CO | SOx | NOx | MP<br>2,5 | MP<br>10 |
| --- | --- | --- | --- | --- | --- | --- |
| Diesel<br>(hasta 600 hp) | kg/kw-h | 0,0041 | 0,0013 | 0,0188 | 0,0007 | 0,0013 |
| Diesel<br>(más de 600 hp) | Diesel<br>(más de 600 hp) | 0,0033 | 0,0000 | 0,0146 | 0,0007 | 0,0004 |

**Tabla 26.: Datos de entrada del modelo**

| Opciones de Entrada | Datos de entrada | Unidad |
| --- | --- | --- |
| Tipo de Fuente | Área | - |
| Altura de Liberación | 1,5 | m |
| Longitud de Lado Largo | 346,41 | m |
| Longitud de Lado Corto | 346,41 | m |
| Altura de Receptor | 2,0 | m |
| Opción Urbana/Rural | Rural | - |
| Altura de Mezcla | 30 | m |
| Altura Anemométrica | 10 | m |
| Clase de Estabilidad | 3 | - |
| Velocidad Eólica | 4,67 | m/s |

**Tabla 27.: Resultado del aporte de contaminantes entregadas por el modelo**

| Distancia | Concentración horarias (μg/m3) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Distancia | CO | SOX | NOX | MP2,5 Total | MP10 Total | MPS |
| 100 | 9,46 | 2,56 | 37,06 | 11,99 | 67,53 | 254,20 |
| 2.500 | 1,84 | 0,50 | 7,19 | 2,33 | 13,10 | 49,31 |
| 5.000 | 1,04 | 0,28 | 4,08 | 1,32 | 7,44 | 28,00 |
| 7.500 | 0,73 | 0,20 | 2,88 | 0,93 | 5,24 | 19,73 |
| 10.000 | 0,57 | 0,15 | 2,24 | 0,72 | 4,08 | 15,35 |
| 12.500 | 0,47 | 0,13 | 1,84 | 0,60 | 3,35 | 12,62 |
| 15.000 | 0,40 | 0,11 | 1,57 | 0,51 | 2,86 | 10,75 |
| 17.500 | 0,35 | 0,09 | 1,37 | 0,44 | 2,49 | 9,39 |
| 20.000 | 0,31 | 0,08 | 1,22 | 0,39 | 2,22 | 8,35 |

**Tabla 28.: Máximas concentraciones horarias entregadas por el modelo**

| Distancia | Concentración máxima de 1 hora (μg/m3) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Distancia | CO<br>(8 horas) | SOx<br>(Máx. 24<br>horas) | NOx<br>(Máx. 1 hora) | MP2,5<br>(Máx. 24<br>horas) | MP10<br>(Máx. 24<br>horas) | MPS<br>(Máx. 24<br>horas) |
| 100 | 6,62 | 1,02 | 37,06 | 4,80 | 27,01 | 101,68 |

**Tabla 29.: Factor para obtener promedios máximos de concentración**

| Tempo Promedio | Factor Multiplicador |
| --- | --- |
| 3 horas | 0,9 (±0,1) |
| 8 horas | 0,7 (±0,2) |
| 24 horas | 0,4 (±0,2) |
| Anual | 0,08 (±0,02) |

**Tabla 30.: Análisis de Cumplimiento de la Norma de referencia de Calidad del Aire**

| Parámetro | Estadístico | Máxima del<br>Proyecto<br>(μg/m3N) | Límite según<br>Norma<br>(μg/m3N) | Porcentaje<br>respecto de la<br>Norma | Referencia |
| --- | --- | --- | --- | --- | --- |
| MP10 | Concentración 24 horas | 27,01 | 150 | 18,01% | D.S. N° 59 / 1998<br>MINSEGPRES |
| MP10 | Concentración anual | 5,40 | 50 | 10,80% | 10,80% |
| MP2,5 | Concentración 24 horas | 4,80 | 50 | 9,59% | D.S. N° 12 / 2010<br>MMA |
| MP2,5 | Concentración anual | 0,96 | 20 | 4,80% | 4,80% |
| NOx | Concentración 1 hora | 37,06 | 400 | 9,27% | D.S. N° 114/ 2002<br>MINSEGPRES |
| SOx | Concentración 24 horas | 1,02 | 250 | 0,41% | D.S. N° 113/ 2002<br>MINSEGPRES |
| CO | Concentración 1 hora | 9,46 | 30.000 | 0,03% | D.S. N° 115/ 2002<br>MINSEGPRES |
| CO | Concentración 8 horas | 6,62 | 10.000 | 0,07% | 0,07% |
| MPS | Media aritmética anual | 101,68 | 200 | 50,84% | Norma Suiza(*) |

**Tabla 31.: Concentraciones por distancia de los contaminantes analizados**

| Distancia (m) | Concentración de Contaminantes (μg/m3) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Distancia (m) | CO<br>(8 horas) | SOX <br>(Máx. 24 horas) | NOX <br>(Máx. 1 horas) | MP2,5<br>(Máx. 24 horas) | MP10<br>(Máx. 24 horas) | MPS<br>(Máx. 24 horas) |
| **100*** | 6,62 | 1,02 | 37,06 | 4,80 | 27,01 | 101,68 |
| 2.500 | 1,29 | 0,20 | 7,19 | 0,93 | 5,24 | 19,72 |
| 5.000 | 0,73 | 0,11 | 4,08 | 0,53 | 2,98 | 11,20 |
| 7.500 | 0,51 | 0,08 | 2,88 | 0,37 | 2,10 | 7,89 |
| 10.000 | 0,40 | 0,06 | 2,24 | 0,29 | 1,63 | 6,14 |
| 12.500 | 0,33 | 0,05 | 1,84 | 0,24 | 1,34 | 5,05 |
| **15.000*** | 0,28 | 0,04 | 1,57 | 0,20 | 1,14 | 4,30 |
| 17.500 | 0,24 | 0,04 | 1,37 | 0,18 | 1,00 | 3,75 |
| 20.000 | 0,22 | 0,03 | 1,22 | 0,16 | 0,89 | 3,34 |
