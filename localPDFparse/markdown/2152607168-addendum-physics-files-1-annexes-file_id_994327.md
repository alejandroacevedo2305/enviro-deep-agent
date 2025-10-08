---
title: Sin título
author: p_reszczynski@jaimeillanes.cl
date: D:20211130164353-03'00'
language: es
type: report
pages: 30
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO AD-I.7
-->

# ANEXO AD-I.7

## ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

### _Cliente:_

**ÍNDICE**

1. INTRODUCCIÓN ....................................................................................................................................... 1

2. OBJETIVO .................................................................................................................................................... 2

3. MARCO LEGAL .......................................................................................................................................... 2

4. METODOLOGIA ........................................................................................................................................ 3

4.1. BASE TEÓRICA DEL MODELO UTILIZADO ............................................................................. 3

4.2. CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN .................................................... 4

4.3. ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF Y FACTOR
DE CORRECIÓN................................................................................................................................ 5

5. PARÁMETROS DE ENTRADA DEL MODELO ................................................................................... 6

5.1. CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO ..................................................... 6

5.2. APORTES DE TERCEROS (LÍNEA DE BASE PROYECTADA) ............................................... 6

5.3. PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN ............. 7

5.4. ANALISIS DE INCERTIDUMBRE Y DETERMINACIÓN DEL FACTOR DE CORRECCIÓN

............................................................................................................................................................... 9

6. RESULTADOS ........................................................................................................................................... 11

6.1. PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC) .............................................................. 11

6.2. RESULTADOS DE LA MODELACIÓN....................................................................................... 12

6.2.1. ESCENARIO CASO ACTUAL - RCA N°50/2015 (USO DE CARBÓN) ................... 13

6.2.2. ESCENARIO FASE DE OPERACIÓN - USO DE GAS NATURAL ............................. 14

6.2.3. ESCENARIO FASE DE OPERACIÓN - USO DE PETRÓLEO DIÉSEL ...................... 15

7. EVALUACIÓN DE ESCENARIOS ......................................................................................................... 17

7.1. CASO ACTUAL - ESCENARIO OPERACIÓN (USO GAS NATURAL) ............................. 17

7.1.1. MATERIAL PARTICULADO RESPIRABLE (MP 10 Y MP 2,5 ) .......................................... 17

7.1.2. GASES DIÓXIDO DE NITRÓGENO (NO 2 ) Y DIÓXIDO DE AZUFRE (SO 2 ) .......... 19

7.2. CASO ACTUAL - ESCENARIO OPERACIÓN (USO DE PETRÓLEO DIÉSEL) ................ 21

7.2.1. MATERIAL PARTICULADO RESPIRABLE (MP 10 Y MP 2,5 ) .......................................... 21

7.2.2. GASES DIÓXIDO DE NITRÓGENO (NO 2 ) Y DIÓXIDO DE AZUFRE (SO 2 ) .......... 23

8. ANÁLISIS DE RESULTADOS Y CONCLUSIONES .......................................................................... 25

ANEXO AD-I.7 - ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE

**TABLAS**

TABLA-1: Norma Primaria de Calidad del Aire MP 10, MP 2,5, NO 2 y SO 2 ..................... 2

TABLA-2: Norma Secundaria de Calidad del Aire .............................................................. 3

TABLA-3: Ubicación Receptores primarios y secundarios .............................................. 4

TABLA-4: Coordenadas de los vértices del sistema de modelación WRF/Calpuff 4

TABLA-5: Línea de Base Proyectada (LBP) por Aporte de Proyectos con RCA que
aún no operan [μg/m [3] ] ............................................................................................ 7

TABLA-6: Emisiones del Escenario Caso Actual - RCA N°50/2015 (Uso de Carbón)

........................................................................................................................................... 8

TABLA-7: Emisiones del Escenario Operación - Uso de Gas Natural ......................... 8

TABLA-8: Emisiones del Escenario Operación - Uso de Petróleo Diésel .................. 8

TABLA-9: Estadígrafos de ajuste de la modelación meteorológica .......................... 10

TABLA-10: Coordenadas y concentraciones de los PMC de cada parámetro
modelado - RCA N°50/2015 (Uso de Carbón) .............................................. 11

TABLA-11: Coordenadas y concentraciones de los PMC de cada parámetro
modelado - Uso Gas Natural ............................................................................... 11

TABLA-12: Coordenadas y concentraciones de los PMC de cada parámetro
modelado - Uso de Petróleo Diésel .................................................................. 12

TABLA-13: Aportes modelados, Escenario Caso Actual (Uso de Carbón), a los
Receptores Primarios y Secundarios Sin Factor de Corrección [μg/m [3] ]

......................................................................................................................................... 13

TABLA-14: Aportes modelados, Escenario Caso Actual (Uso de Carbón), a los
Receptores Primarios y Secundarios Con Factor de Corrección [μg/m [3] ]

......................................................................................................................................... 13

TABLA-15: Aportes modelados, Escenario Fase de Operación (Uso de Gas Natural),
a los Receptores Primarios y Secundarios Sin Factor de Corrección

[μg/m [3] ] ......................................................................................................................... 14

TABLA-16: Aportes modelados, Escenario Fase de Operación (Uso de Gas Natural),
a los Receptores Primarios y Secundarios Con Factor de Corrección

[μg/m [3] ] ......................................................................................................................... 15

TABLA-17: Aportes modelados, Escenario Fase de Operación (Uso de Petróleo
Diésel), a los Receptores Primarios y Secundarios Sin Factor de
Corrección [μg/m [3] ] .................................................................................................. 15

ANEXO AD-I.7 - ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE

TABLA-18: Aportes modelados, Escenario Fase de Operación (Uso de Petróleo
Diésel), a los Receptores Primarios y Secundarios Con Factor de
Corrección [μg/m [3] ] .................................................................................................. 16

TABLA-19: Diferencia de MP 10 y MP 2,5 [μg/m [3] ] - Caso Actual (Uso de Carbón) vs
Escenario Operación (Uso Gas Natural) ........................................................... 18

TABLA-20: Concentraciones de NO 2 y SO 2 [μg/m [3] ] - Caso Actual (Uso de Carbón)
vs Escenario Operación (Uso Gas Natural) ..................................................... 20

TABLA-21: Diferencia de MP 10 y MP 2,5 [μg/m [3] ] - Caso Actual (Uso de Carbón) vs
Escenario Operación (Uso de Petróleo Diésel) .............................................. 22

TABLA-22: Concentraciones de NO 2 y SO 2 [μg/m [3] ] - Caso Actual (Uso de Carbón)
vs Escenario Operación (Uso de Petróleo Diésel) ........................................ 24

**FIGURAS**

FIGURA-1: Dominio de Modelación (Computacional Grid), fuentes emisoras y
receptores. .................................................................................................................... 9

FIGURA-2: Frecuencia relativa de la dirección del viento observada y modelada
(WRF). Estación Ferrocarriles ................................................................................ 10

ANEXO AD-I.7 - ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE

**1.** **INTRODUCCIÓN**

El presente informe da cuenta del análisis del transporte y dispersión de contaminantes
emitidos para los escenarios máximos evaluados autorizados para el caso actual y la
evaluación de la fase de operación del Proyecto en evaluación, ubicado en el área industrial
de la comuna de Mejillones, provincia de Antofagasta, en la Región de Antofagasta.

En este contexto, de acuerdo con las consultas realizadas por la autoridad, enmarcado en
las respuestas de la Adenda N°1 del Proyecto, se actualiza el Anexo C2-3 de la DIA,
incorporando principalmente dentro del escenario de evaluación el uso de 100% Petróleo
Diésel, como evaluación de calidad del aire. Respecto a lo anterior, dado que la modelación
realizada no sufrió modificaciones en su configuración, no se considera actualizar las curvas
de isoconcentraciones entregadas en la presentación original, así como tampoco los
archivos digitales de modelación, debido a que corresponden a los mismos.

La simulación de los aportes del Proyecto a las concentraciones ambientales se realiza
mediante la aplicación del sistema de modelación WRF/CALPUFF; sistema que considera la
utilización de la modelación meteorológica para el año 2019 (WRF) y un dominio de
modelación de Calpuff de 50x50 [km] con una resolución de 1x1 [km], la cual incluye como
receptores a las Estaciones Ferrocarriles y Compañía de Bomberos, las que se encuentran
presentes en el área determinada por el dominio de modelación, donde se registraron
valores basales de material particulado y gases.

A continuación, se presenta el análisis de la dispersión y transporte de las emisiones
correspondientes al escenario máximo autorizado para el caso actual y para la evaluación
de la fase de operación del Proyecto, que considera las emisiones en ton/día, llevadas a un
escenario operacional de 365 días (año completo de funcionamiento). El escenario caso
actual corresponde a los límites señalados en la RCA N°50/2015; para el caso de la fase de
operación, se consideran los siguientes escenarios de evaluación:

 - Uso Gas Natural;

 - Uso Petróleo Diésel.

En concordancia a lo señalado en la Guía para el uso de modelos de calidad del aire en el
SEIA (emitida por el Servicio de Evaluación Ambiental el año 2012), los resultados de la
modelación se entregan en tablas a modo de comparar los aportes del Proyecto con y sin
factor de corrección.

Además, se comparan los resultados de la modelación respecto del caso actual y los
escenarios de operación, y a su vez, respecto de las normas primarias y secundarias de
calidad del aire nacionales (artículo 11 del D.S. N° 40/12 que aprueba el Reglamento del
Sistema de Evaluación de Impacto Ambiental -RSEIA-), de manera de evaluar la reducción
de emisiones en términos de concentración.

1
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

Los parámetros que se analizan corresponden a MP 10 ; MP 2,5 ; NO 2 y SO 2 . Se indica que los
archivos digitales de la modelación con CALPUFF (salidas y entradas) fueron entregados en
el marco de la presentación original y que no sufren modificaciones en la presente entrega,
dado que solamente se replantean los resultados evaluados originalmente.

**2.** **OBJETIVO**

Determinar la reducción de las concentraciones ambientales de material particulado y gases
que generará el Proyecto en los receptores sensibles identificados y comparar dicha
reducción con respecto a las normas de calidad primaria y secundaria nacionales.

**3.** **MARCO LEGAL**

Para determinar la existencia de los efectos, características o circunstancias de los literales
a), b) y d) del art. 11 de la Ley 19.300 en el área de influencia del Proyecto en su fase de
operación considerando el “peor escenario”, se ha considerado la normativa ambiental
primaria y secundaria de calidad de aire vigente para MP 10, MP 2,5, NO 2 y SO 2, presentadas en
las Tablas 1 y 2.

TABLA-1: Norma Primaria de Calidad del Aire MP 10, MP 2,5, NO 2 y SO 2

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**MP10 **|D.S. N°59/98<br>MINSEGPRES,<br>modificada por D.S.<br>N°45/01|Promedio aritmético de tres años calendario<br>consecutivos|50 μg/m3|
|**MP10 **|D.S. N°59/98<br>MINSEGPRES,<br>modificada por D.S.<br>N°45/01|Percentil 98 de las concentraciones de 24<br>horas registradas durante un período anual|150 μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Promedio tri-anual de las concentraciones<br>anuales|20 μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Percentil<br>98<br>de<br>los<br>promedios<br>diarios<br>registrados durante un año|50 μg/m3|
|**NO2 **|D.S. N° 114/2002 del<br>MINSEGPRES|Promedio aritmético de los valores de<br>concentración anual de tres años calendarios<br>sucesivos|100 μg/m3|
|**NO2 **|D.S. N° 114/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante<br>un año calendario|400 μg/m3|
|**SO2 **|D.S. N° 104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 99 de las<br>concentraciones de 24 horas registradas cada<br>año|150 μg/m3|
|**SO2 **|D.S. N° 104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores de concentración<br>anual|60 μg/m3|

2
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|||Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 98,5 de<br>las concentraciones de 1 hora registradas cada<br>año|350 μg/m3|

Fuente: Elaboración propia.

TABLA-2: Norma Secundaria de Calidad del Aire

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**SO2**|D.S. N°22/09 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos<br>del<br>Percentil<br>99,73<br>de<br>las<br>concentraciones de 1 hora registradas cada año|1.000 μg/m3|
|**SO2**|D.S. N°22/09 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos<br>del<br>Percentil<br>99,7<br>de<br>las<br>concentraciones diarias|365 μg/m3|
|**SO2**|D.S. N°22/09 del<br>MINSEGPRES|Promedio anual de 3 años sucesivos|80 μg/m3|

Fuente: Elaboración propia.

**4.** **METODOLOGIA**

La modelación se realizó acorde con la metodología descrita en la Guía para el uso de
modelos de calidad del aire en el SEIA (2012), en adelante la “Guía de modelación”. Se utilizó
el modelo numérico Weather Research and Forecasting (WRF) en la generación de datos
meteorológicos para el año 2019, y el modelo Calpuff para la modelación de la dispersión y
transporte de las emisiones, en el escenario considerado.

**4.1.** **BASE TEÓRICA DEL MODELO UTILIZADO**

WRF es el modelo meteorológico recomendado en la Guía de modelación para la generación
de la grilla meteorológica, esto por sobre modelos que consideran estaciones de monitoreo
en la modelación. Este modelo genera una grilla tridimensional de viento y temperatura, a
través de dominios anidados con una resolución horizontal, recomendada para el dominio
de menor tamaño, de 1 kilómetro.

Por otro lado, Calpuff es un modelo de dispersión, transporte y deposición de contaminantes
atmosféricos de tipo puff lagrangiano-gaussiano, no estacionario, recomendado por la Guía
de modelación y también por la Agencia de Protección Ambiental de Estados Unidos (US
EPA su sigla en inglés) [1], el cual es aplicable a terrenos complejos y a múltiples tipos de
fuentes emisoras (puntuales, areales y volumétricas). Calpuff realiza sus cálculos tomando
los datos meteorológicos superficiales y de la capa superior atmosférica, incluyendo la
posibilidad de modelar la dispersión de contaminantes primarios y secundarios, obteniendo

1 40 CFR Part 51, Revision to the Guideline on Air Quality Models: Adoption of a Preferred General Purpose (Flat
and Complex Terrain) Dispersion Model and Other Revisions; Final Rule.
http://www.epa.gov/ttn/scram/guidance/guide/appw_05.pdf

3
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

resultados confiables para distancias de hasta 100 [km].

El sistema de modelación incluye tres componentes principales: Calmet, Calpuff y Calpost,
además de una serie de programas de pre-procesamiento diseñados para la preparación de
la información meteorológica y geofísica, En este caso, no fue necesario utilizar los preprocesadores ni el módulo Calmet, ya que se emplearon los resultados de la modelación
meteorológica realizada con WRF.

Calpost es un programa post-procesador que permite compilar los resultados de Calpuff
creando los archivos según los estadísticos establecidos en las normas de calidad del aire
para la evaluación de los resultados.

**4.2.** **CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN**

Para que los procesos meteorológicos de mesoescala sean representados de una forma
adecuada, tanto por el modelo meteorológico como por el modelo de dispersión, se generó
un dominio de modelación de WRF/Calpuff de 50x50 [km], en donde se consideraron las
características topográficas de la zona, incluyendo como receptores a las Estaciones
Ferrocarriles y Compañía de Bomberos, donde se registraron valores basales de material
particulado y gases (Tabla 3).

TABLA-3: Ubicación Receptores primarios y secundarios

|ID|Nombre<br>Receptor|Coordenadas UTM [m]<br>WGS 84 Huso 19S|Col4|Altura de Elevación<br>Modelo WRF<br>[m]|Coordenadas Datum LCC<br>[m] NWS84|Col7|
|---|---|---|---|---|---|---|
|**ID**|**Nombre**<br>**Receptor**|**Este**|**Norte**|**Norte**|**Este**|**Norte**|
|**R_1**|**Ferrocarriles**|350.017|7.444.552|13,65|-6.392,78|673,85|
|**R_2**|**Compañía de**<br>**Bomberos**|351.468|7.444.654|13,83|-4.940,34|758,98|

Fuente: Elaboración propia.

Cabe señalar que la modelación meteorológica WRF fue realizada para el año 2019, de
acuerdo con la configuración definida por el SEA en su Guía de modelación, cuenta con una
resolución horizontal de 1 [km] y una resolución vertical de 10 niveles a 20, 40, 80, 160, 320,
640, 1.200, 2.000, 3.000 y 4.000 metros. En la Tabla a continuación se señalan las coordenadas
de los vértices del dominio de modelación WRF/Calpuff.

TABLA-4: Coordenadas de los vértices del sistema de modelación WRF/Calpuff

|Vértices|Coordenadas UTM [m] Datum: WGS-84, Huso: 19S|Col3|
|---|---|---|
|**Vértices**|**Este**|**Norte**|
|**SW**|331.622|7.418.804|
|**NE**|381.226|7.469.080|
|**NW**|331.144|7.468.601|
|**SE**|381.705|7.419.286|

Fuente: Elaboración propia.

4
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

**4.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF Y**
**FACTOR DE CORRECIÓN**

La modelación atmosférica está basada en uno de los modelos de pronóstico meteorológico
más avanzados y completos disponibles [2], el cual cuenta con un gran número de
parametrizaciones que permiten, si son adecuadamente seleccionadas e implementadas,
simular gran parte de los procesos meteorológicos de mesoescala, este modelo corresponde
como ya se ha mencionado al Weather Research and Forecasting (WRF).

Sin embargo, e independiente de las bondades del modelo utilizado, todo modelo
atmosférico requiere ser calibrado y validado para cada condición meteorológica y de
terreno. En este punto es donde se tienen las mayores dificultades, dado que la incorrecta
implementación de alguna parametrización puede llevar a errores significativos en la
estimación de los vientos en superficie y con esto de las trayectorias de los contaminantes.

El modelo WRF analizado ha sido parametrizado de acuerdo con lo establecido por él SEA y
corresponde al año 2019.

Para realizar el análisis de incertidumbre se consideran las recomendaciones establecidas en

la Guía de modelación, donde en su acápite 7 menciona que cualquier modelo representa
una aproximación a la realidad y sus resultados tienen incertidumbres asociadas, las cuales
se expresan a través de diferencias entre lo estimado y lo observado.

Cabe señalar que, a partir de la estación meteorológica más cercana se evaluaron los
estadígrafos meteorológicos recomendados por la US.EPA, que corresponden al BIAS
(sesgo) y al IOA (índice de ajustes), además de error cuadrático medio (RMSE) para la
velocidad [m/s] y la dirección del viento [°] entre los valores de la estación modelada a partir
del modelo meteorológico WRF utilizado y las observaciones de terreno disponibles para el
área a modelar, los resultados se presentan en la Tabla 9.

Cabe señalar que, el error cuadrático medio mide la cantidad de error que hay entre dos
conjuntos de valores, es decir presenta la diferencia entre los valores pronosticados y
observados.

Luego del ajuste en las direcciones de viento, se calcula la frecuencia relativa del viento para
cada una de las direcciones seleccionadas respecto de la frecuencia total de las estas, tanto
para los datos observados como para los datos modelados. Por lo tanto, si denominamos _Xi_
a las frecuencias observadas de cada una de las direcciones de viento (i) y _Wi_ a las frecuencias
modeladas, entonces matemáticamente las frecuencias relativas observadas ( F obs )
corresponderán a las calculadas de acuerdo a la ecuación 1:

2 Numeral 5.3.2 Fuentes de Datos Meteorológicas. Guía para el uso de modelos de calidad del aire. SEA 2012.

5
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

F obs =

∑ 3i=1 X i X i Ecuación 1

Y las frecuencias relativas modeladas ( F WRF ), corresponderán a las calculadas de acuerdo a
la ecuación 2:

F WRF =

∑ 3i=1 W i W i Ecuación 2

De esta manera, al restar ambas frecuencias relativas obtenemos información respecto al
grado de subestimación o sobrestimación de las direcciones de viento que pueden favorecer
el transporte de los parámetros atmosféricos a modelar. En el caso de que la diferencia entre
lo observado y lo modelado sea mayor que cero, significaría que el modelo subestimó la
dirección que favorece el transporte de contaminantes, y por lo tanto se aplicará un factor
de corrección dado por la ecuación 3 a continuación:

FC= 1 + [F obs −F WRF ] Ecuación 3

**5.** **PARÁMETROS DE ENTRADA DEL MODELO**

A continuación, se detallan los principales parámetros de entrada del modelo de calidad del
aire, los que corresponden a: características topográficas, uso del suelo, fuentes emisoras
externas (aportes de terceros) y los escenarios de modelación (emisiones asociadas a las
instalaciones donde se emplaza el Proyecto).

**5.1.** **CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO**

Las características topográficas y de uso de suelo, son parámetros asociados a la elevación
de terreno, los coeficientes de rugosidad, razón de bowen, entre otros, que son parte
integrante de los datos que incluye el archivo de modelación WRF, por lo cual no se requiere
su caracterización.

**5.2.** **APORTES DE TERCEROS (LÍNEA DE BASE PROYECTADA)**

Cabe señalar, que la línea base de calidad del aire monitoreada no considera los aportes de
proyectos aprobados que aún no se encuentran en construcción al momento de medir, por
tanto, para considerar dichos aportes de terceros se les suman a los valores monitoreados
obteniendo una línea base proyectada en el tiempo. Para ello, se revisaron los proyectos de
terceros que estuvieran al interior del área de influencia de calidad del aire del presente
Proyecto y que no estuvieran operando hasta septiembre de 2020.

Resultado de lo anterior se obtuvo la tabla con la línea base proyectada (LBP), con un
incremento en las concentraciones monitoreadas en la Línea de Base, ya que considera los
aportes de terceros más los valores monitoreados, la cual se presenta a continuación en la
siguiente Tabla. Para mayor detalle, revisar la “Línea de Base Calidad del Aire” de la presente
DIA (Anexo C2-2).

6
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

TABLA-5: Línea de Base Proyectada (LBP) por Aporte de Proyectos con RCA que aún no

operan [μg/m [3] ]

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Línea de Base Proyectada<br>[μg/m3]|
|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|41|
|MP10|Ferrocarriles|Primaria|Anual|16|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|24h P98|46|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|18|
|MP2,5|Ferrocarriles|Primaria|24h P98|17|
|MP2,5|Ferrocarriles|Primaria|Anual|7|
|SO2|Ferrocarriles|Primaria|24h P99|6|
|SO2|Ferrocarriles|Primaria|1h P98,5|22|
|SO2|Ferrocarriles|Primaria|Anual|2|
|SO2|Ferrocarriles|Secundaria|24h P99,7|9|
|SO2|Ferrocarriles|Secundaria|1h P99,73|22|
|SO2|Ferrocarriles|Secundaria|Anual|2|
|NO2|Ferrocarriles|Primaria|1h P99|41|
|NO2|Ferrocarriles|Primaria|Anual|3|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|1h P99|40|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|10|

Fuente: Anexo C2-2 de la DIA.

**5.3.** **PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN**

El resumen de las emisiones de cada una de las fuentes emisoras ingresadas al modelo para
cada escenario de modelación, en unidades de [g/s], se presentan en las Tablas a
continuación.

7
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

TABLA-6: Emisiones del Escenario Caso Actual - RCA N°50/2015 (Uso de Carbón)

|Tipo de Fuente|ID|Descripción|Elevación de<br>la Chimenea<br>[m]|Temperatura<br>de salida de<br>gases [K]|Diámetro de<br>la Chimenea<br>[m]|Velocidad<br>de salida<br>de gases<br>[m/s]|MP<br>10<br>[g/s]|MP<br>2,5<br>[g/s]|NO<br>2<br>[g/s]|SO<br>2<br>[g/s]|
|---|---|---|---|---|---|---|---|---|---|---|
|Point|SRC_1|Chimenea U7|100|323|5,11|17,32|10,42|10,42|70,60|70,60|

Nota: Tasas de emisión corresponden al uso de Carbón como combustible;

Fuente: Elaboración propia.

TABLA-7: Emisiones del Escenario Operación - Uso de Gas Natural

|Tipo de Fuente|ID|Descripción|Elevación de<br>la Chimenea<br>[m]|Temperatura<br>de salida de<br>gases [K]|Diámetro de<br>la Chimenea<br>[m]|Velocidad<br>de salida<br>de gases<br>[m/s]|MP<br>10<br>[g/s]|MP<br>2,5<br>[g/s]|NO<br>2<br>[g/s]|SO<br>2<br>[g/s]|
|---|---|---|---|---|---|---|---|---|---|---|
|Point|SRC_1|Chimenea U7|100|378,35|5,11|16,47|3,38|3,38|16,89|3,38|

Fuente: Elaboración propia.

TABLA-8: Emisiones del Escenario Operación - Uso de Petróleo Diésel

|Tipo de Fuente|ID|Descripción|Elevación de<br>la Chimenea<br>[m]|Temperatura<br>de salida de<br>gases [K]|Diámetro de<br>la Chimenea<br>[m]|Velocidad<br>de salida<br>de gases<br>[m/s]|MP<br>10<br>[g/s]|MP<br>2,5<br>[g/s]|NO<br>2<br>[g/s]|SO<br>2<br>[g/s]|
|---|---|---|---|---|---|---|---|---|---|---|
|Point|SRC_1|Chimenea U7|100|379,33|5,11|15,48|1,80|1,80|19,05|1,59|

Fuente: Elaboración propia.

8
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

A continuación, en la siguiente Figura se presenta la ubicación del dominio de modelación,
fuentes emisoras y receptores para cada escenario de evaluación. Dado que la ubicación de
los receptores y las fuentes de emisión es la misma, solo se presenta una figura para
referenciar la ubicación.

FIGURA-1: Dominio de Modelación (Computacional Grid), fuentes emisoras y receptores.

Fuente: Elaboración propia.

**5.4.** **ANALISIS DE INCERTIDUMBRE Y DETERMINACIÓN DEL FACTOR DE**
**CORRECCIÓN**

A partir de los datos meteorológicos del año 2019 para la Estación Ferrocarriles, se realizó
un análisis de estadígrafo, obteniendo los resultados presentados en la tabla a continuación.

9
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

TABLA-9: Estadígrafos de ajuste de la modelación meteorológica

|Receptor|Variable|RMSE|BIAS|Bondad BIAS|IOA|Bondad IOA|
|---|---|---|---|---|---|---|
|Estación<br>Ferrocarriles|Dirección del<br>viento (°)|126,54|-13,06|<+-/10|0,45|--|
|Estación<br>Ferrocarriles|Velocidad del<br>viento (m/s)|1,89|-0,73|<+-/0,5|0,69|>0,60|

Fuente: Elaboración propia.

De la tabla anterior, se desprende que la velocidad del viento (m/s) en el estadístico BIAS e
IOA se encuentra por sobre el rango de bondad. Con respecto a la dirección del viento, el
estadístico BIAS se encuentra sobre los rangos de bondad.

De acuerdo con la metodología descrita en el numeral 4.3, se graficaron las frecuencias
relativas de las direcciones del viento que favorecen el transporte de los parámetros
atmosféricos a modelar, hacia el receptor Hospital, a modo de determinar los parámetros
F WRF y F obs . El gráfico de las frecuencias relativas señaladas se realizó tanto de los datos
registrados en la estación de monitoreo, como los datos modelados con WRF, lo cual se
muestra a continuación:

FIGURA-2: Frecuencia relativa de la dirección del viento observada y modelada (WRF).

Estación Ferrocarriles

|Col1|N|NNE|NE|ENE|E|ESE|SE|SSE|S|SSW|SW|WSW|W|WNW|NW|NNW|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|OBS|8%|5%|4%|2%|1%|1%|2%|8%|28%|18%|3%|1%|1%|1%|4%|14%|
|WRF|9%|6%|4%|2%|1%|0%|1%|4%|13%|32%|22%|2%|0%|0%|1%|4%|

Fuente: Elaboración propia.

Como se puede observar en la Figura anterior, el modelo WRF subestima las direcciones S,
NNW, SSE, NW, WNW, SE y ESE, en un 15%, 10%, 5%, 4%, 1%, 1% y 1% respectivamente, por
lo tanto, en la corrección considerará la peor situación, que significa corregir las
concentraciones por 1,15, de acuerdo con la fórmula señalada en el acápite anterior.

10
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

**6.** **RESULTADOS**

A continuación, se presentan los aportes estimados de la operación del Proyecto para cada
uno de los parámetros modelados.

**6.1.** **PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC)**

En las Tablas a continuación se presentan las coordenadas y aportes de los puntos de
máxima concentración modelada, para cada parámetro y estadístico para cada escenario de
modelación. Se presenta la actualización respecto de las normativas aplicables para el
escenario 100% uso de petróleo diésel.

TABLA-10: Coordenadas y concentraciones de los PMC de cada parámetro modeladoRCA N°50/2015 (Uso de Carbón)

|Norma|Parámetro|ID|Coordenadas UTM [m]<br>WGS84 Huso 19S|Col5|Coordenadas LCC [m]<br>Datum NWS-84|Col7|PMC<br>[μg/m3]|
|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|
|MP10 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|1,83|
|MP10 <br>Primaria|P98 diario|PMC1|355.908|7.445.432|-0,50|1,50|6,42|
|MP2,5 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|1,83|
|MP2,5 <br>Primaria|P98 diario|PMC1|355.908|7.445.432|-0,50|1,50|6,42|
|NO2 <br>Primario|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|12,34|
|NO2 <br>Primario|P99 horario|PMC1|355.908|7.445.432|-0,50|1,50|428,08|
|SO2 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|12,23|
|SO2 <br>Primaria|P99 diario|PMC1|355.908|7.445.432|-0,50|1,50|51,27|
|SO2 <br>Primaria|P98,5hr|PMC1|355.908|7.445.432|-0,50|1,50|423,47|
|SO2 <br>Secundaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|12,23|
|SO2 <br>Secundaria|P99,7 diario|PMC1|355.908|7.445.432|-0,50|1,50|55,02|
|SO2 <br>Secundaria|P99,73 hr|PMC1|355.908|7.445.432|-0,50|1,50|426,34|

Fuente: Elaboración propia.

TABLA-11: Coordenadas y concentraciones de los PMC de cada parámetro modeladoUso Gas Natural

|Norma|Parámetro|ID|Coordenadas UTM [m]<br>WGS84 Huso 19S|Col5|Coordenadas LCC [m]<br>Datum NWS-84|Col7|PMC<br>[μg/m3]|
|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|
|MP10 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|0,50|
|MP10 <br>Primaria|P98 diario|PMC1|355.908|7.445.432|-0,50|1,50|1,91|
|MP2,5 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|0,50|
|MP2,5 <br>Primaria|P98 diario|PMC1|355.908|7.445.432|-0,50|1,50|1,91|
|NO2 <br>Primario|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|2,51|
|NO2 <br>Primario|P99 horario|PMC1|355.908|7.445.432|-0,50|1,50|78,63|
|SO2 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|0,50|
|SO2 <br>Primaria|P99 diario|PMC1|355.908|7.445.432|-0,50|1,50|2,08|

11
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

|Norma|Parámetro|ID|Coordenadas UTM [m]<br>WGS84 Huso 19S|Col5|Coordenadas LCC [m]<br>Datum NWS-84|Col7|PMC<br>[μg/m3]|
|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|
|**Norma**|P98,5hr|PMC1|355.908|7.445.432|-0,50|1,50|15,71|
|SO2 <br>Secundaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|0,50|
|SO2 <br>Secundaria|P99,7 diario|PMC1|355.908|7.445.432|-0,50|1,50|2,09|
|SO2 <br>Secundaria|P99,73 hr|PMC1|355.908|7.445.432|-0,50|1,50|16,66|

Fuente: Elaboración propia.

TABLA-12: Coordenadas y concentraciones de los PMC de cada parámetro modeladoUso de Petróleo Diésel

|Norma|Parámetro|ID|Coordenadas UTM [m]<br>WGS84 Huso 19S|Col5|Coordenadas LCC [m]<br>Datum NWS-84|Col7|PMC<br>[μg/m3]|
|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|
|MP10 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|0,27|
|MP10 <br>Primaria|P98 diario|PMC1|355.908|7.445.432|-0,50|1,50|1,03|
|MP2,5 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|0,27|
|MP2,5 <br>Primaria|P98 diario|PMC1|355.908|7.445.432|-0,50|1,50|1,03|
|NO2 <br>Primario|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|2,85|
|NO2 <br>Primario|P99 horario|PMC1|355.908|7.445.432|-0,50|1,50|91,40|
|SO2 <br>Primaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|0,24|
|SO2 <br>Primaria|P99 diario|PMC1|355.908|7.445.432|-0,50|1,50|0,97|
|SO2 <br>Primaria|P98,5hr|PMC1|355.908|7.445.432|-0,50|1,50|7,62|
|SO2 <br>Secundaria|Promedio Anual|PMC1|355.908|7.445.432|-0,50|1,50|0,24|
|SO2 <br>Secundaria|P99,7 diario|PMC1|355.908|7.445.432|-0,50|1,50|0,99|
|SO2 <br>Secundaria|P99,73 hr|PMC1|355.908|7.445.432|-0,50|1,50|7,66|

Fuente: Elaboración propia.

En el Apéndice C2-3-2, entregado en el marco de la DIA, fueron presentados los puntos de
máxima concentración.

**6.2.** **RESULTADOS DE LA MODELACIÓN**

A continuación, se presentan los resultados de la modelación para cada uno de los
parámetros modelados de acuerdo con los estadísticos definidos en cada una de las normas
primarias y secundarias de calidad del aire evaluado, diferenciado por escenario de
modelación. Los resultados son presentados con y sin factor de corrección respectivamente
y de acuerdo con lo detallado en el numeral 4.3 (Análisis de incertidumbre) y lo solicitado
en la Guía de modelación.

12
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

**6.2.1.** **ESCENARIO CASO ACTUAL - RCA N°50/2015 (USO DE CARBÓN)**

En las siguientes tablas se presentan los aportes sin factor de corrección y con factor de
corrección para los receptores identificados.

TABLA-13: Aportes modelados, Escenario Caso Actual (Uso de Carbón), a los Receptores

Primarios y Secundarios Sin Factor de Corrección [μg/m [3] ]

|Parámetro|Estación|Tipo de Norma|Estadístico|Aporte<br>[μg/m3]|
|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,49|
|MP10|Ferrocarriles|Primaria|Anual|0,09|
|MP10|Compañía de Bomberos|Compañía de Bomberos|24h P98|0,60|
|MP10|Compañía de Bomberos|Compañía de Bomberos|Anual|0,12|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,49|
|MP2,5|Ferrocarriles|Primaria|Anual|0,09|
|NO2|Ferrocarriles|Primaria|1h P99|30,22|
|NO2|Ferrocarriles|Primaria|Anual|0,57|
|NO2|Compañía de Bomberos|Compañía de Bomberos|1h P99|43,49|
|NO2|Compañía de Bomberos|Compañía de Bomberos|Anual|0,81|
|SO2|Ferrocarriles|Primaria|24h P99|3,29|
|SO2|Ferrocarriles|Primaria|1h P98,5|29,95|
|SO2|Ferrocarriles|Primaria|Anual|0,52|
|SO2|Ferrocarriles|Secundaria|24h P99,7|3,39|
|SO2|Ferrocarriles|Secundaria|1h P99,73|30,04|
|SO2|Ferrocarriles|Secundaria|Anual|0,52|

Fuente: Elaboración propia.

TABLA-14: Aportes modelados, Escenario Caso Actual (Uso de Carbón), a los Receptores

Primarios y Secundarios Con Factor de Corrección [μg/m [3] ]

|Parámetro|Estación|Tipo de Norma|Estadístico|Aporte<br>Rectificado<br>[μg/m3]*|
|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,57|
|MP10|Ferrocarriles|Primaria|Anual|0,11|
|MP10|Compañía de Bomberos|Compañía de Bomberos|24h P98|0,69|
|MP10|Compañía de Bomberos|Compañía de Bomberos|Anual|0,15|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,57|
|MP2,5|Ferrocarriles|Primaria|Anual|0,11|
|NO2|Ferrocarriles|Primaria|1h P99|34,76|
|NO2|Ferrocarriles|Primaria|Anual|0,66|
|NO2|Compañía de Bomberos|Compañía de Bomberos|1h P99|50,02|
|NO2|Compañía de Bomberos|Compañía de Bomberos|Anual|0,94|
|SO2|Ferrocarriles|Primaria|24h P99|3,79|
|SO2|Ferrocarriles|Primaria|1h P98,5|34,45|

13
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Estación|Tipo de Norma|Estadístico|Aporte<br>Rectificado<br>[μg/m3]*|
|---|---|---|---|---|
||||Anual|0,61|
|||Secundaria|24h P99,7|3,90|
|||Secundaria|1h P99,73|34,55|
|||Secundaria|Anual|0,61|

(*): Considera un factor de corrección de 1,15;

Fuente: Elaboración propia.

**6.2.2.** **ESCENARIO FASE DE OPERACIÓN - USO DE GAS NATURAL**

En las siguientes tablas se presentan los aportes sin factor de corrección y con factor de
corrección para los receptores identificados.

TABLA-15: Aportes modelados, Escenario Fase de Operación (Uso de Gas Natural), a los

Receptores Primarios y Secundarios Sin Factor de Corrección [μg/m [3] ]

|Parámetro|Estación|Tipo de Norma|Estadístico|Aporte<br>[μg/m3]|
|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,14|
|MP10|Ferrocarriles|Primaria|Anual|0,03|
|MP10|Compañía de Bomberos|Compañía de Bomberos|24h P98|0,03|
|MP10|Compañía de Bomberos|Compañía de Bomberos|Anual|0,04|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,14|
|MP2,5|Ferrocarriles|Primaria|Anual|0,03|
|NO2|Ferrocarriles|Primaria|1h P99|5,37|
|NO2|Ferrocarriles|Primaria|Anual|0,13|
|NO2|Compañía de Bomberos|Compañía de Bomberos|1h P99|9,45|
|NO2|Compañía de Bomberos|Compañía de Bomberos|Anual|0,18|
|SO2|Ferrocarriles|Primaria|24h P99|0,14|
|SO2|Ferrocarriles|Primaria|1h P98,5|1,07|
|SO2|Ferrocarriles|Primaria|Anual|0,02|
|SO2|Ferrocarriles|Secundaria|24h P99,7|0,14|
|SO2|Ferrocarriles|Secundaria|1h P99,73|1,21|
|SO2|Ferrocarriles|Secundaria|Anual|0,02|

Fuente: Elaboración propia.

14
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

TABLA-16: Aportes modelados, Escenario Fase de Operación (Uso de Gas Natural), a los

Receptores Primarios y Secundarios Con Factor de Corrección [μg/m [3] ]

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte<br>Rectificado<br>[μg/m3]*|
|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,17|
|MP10|Ferrocarriles|Primaria|Anual|0,04|
|MP10|Compañía de Bomberos|Compañía de Bomberos|24h P98|0,04|
|MP10|Compañía de Bomberos|Compañía de Bomberos|Anual|0,05|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,17|
|MP2,5|Ferrocarriles|Primaria|Anual|0,04|
|NO2|Ferrocarriles|Primaria|1h P99|6,18|
|NO2|Ferrocarriles|Primaria|Anual|0,15|
|NO2|Compañía de Bomberos|Compañía de Bomberos|1h P99|10,87|
|NO2|Compañía de Bomberos|Compañía de Bomberos|Anual|0,21|
|SO2|Ferrocarriles|Primaria|24h P99|0,17|
|SO2|Ferrocarriles|Primaria|1h P98,5|1,24|
|SO2|Ferrocarriles|Primaria|Anual|0,03|
|SO2|Ferrocarriles|Secundaria|24h P99,7|0,17|
|SO2|Ferrocarriles|Secundaria|1h P99,73|1,40|
|SO2|Ferrocarriles|Secundaria|Anual|0,03|

(*): Considera un factor de corrección de 1,15;

Fuente: Elaboración propia.

**6.2.3.** **ESCENARIO FASE DE OPERACIÓN - USO DE PETRÓLEO DIÉSEL**

Cabe señalar que en la presentación original se consideró realizar una ponderación de las
concentraciones modeladas para gas natural y petróleo diésel, a modo de evaluar un
escenario combinado durante el año. Para esta presentación, se considera el funcionamiento
100% de petróleo diésel durante todo el año.

En las siguientes tablas se presentan los aportes sin factor de corrección y con factor de
corrección para los receptores identificados.

TABLA-17: Aportes modelados, Escenario Fase de Operación (Uso de Petróleo Diésel), a

los Receptores Primarios y Secundarios Sin Factor de Corrección [μg/m [3] ]

|Parámetro|Estación|Tipo de Norma|Estadístico|Aporte<br>[μg/m3]|
|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,07|
|MP10|Ferrocarriles|Primaria|Anual|0,01|
|MP10|Compañía de Bomberos|Compañía de Bomberos|24h P98|0,11|
|MP10|Compañía de Bomberos|Compañía de Bomberos|Anual|0,02|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,07|

15
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Estación|Tipo de Norma|Estadístico|Aporte<br>[μg/m3]|
|---|---|---|---|---|
||||Anual|0,01|
|NO2|Ferrocarriles|Primaria|1h P99|6,57|
|NO2|Ferrocarriles|Primaria|Anual|0,15|
|NO2|Compañía de Bomberos|Compañía de Bomberos|1h P99|11,08|
|NO2|Compañía de Bomberos|Compañía de Bomberos|Anual|0,20|
|SO2|Ferrocarriles|Primaria|24h P99|0,07|
|SO2|Ferrocarriles|Primaria|1h P98,5|0,54|
|SO2|Ferrocarriles|Primaria|Anual|0,01|
|SO2|Ferrocarriles|Secundaria|24h P99,7|0,07|
|SO2|Ferrocarriles|Secundaria|1h P99,73|0,56|
|SO2|Ferrocarriles|Secundaria|Anual|0,01|

Fuente: Elaboración propia.

TABLA-18: Aportes modelados, Escenario Fase de Operación (Uso de Petróleo Diésel), a

los Receptores Primarios y Secundarios Con Factor de Corrección [μg/m [3] ]

|Parámetro|Estación|Tipo de Norma|Estadístico|Aporte<br>Rectificado<br>[μg/m3]*|
|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,09|
|MP10|Ferrocarriles|Primaria|Anual|0,02|
|MP10|Compañía de Bomberos|Compañía de Bomberos|24h P98|0,12|
|MP10|Compañía de Bomberos|Compañía de Bomberos|Anual|0,02|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,09|
|MP2,5|Ferrocarriles|Primaria|Anual|0,02|
|NO2|Ferrocarriles|Primaria|1h P99|7,55|
|NO2|Ferrocarriles|Primaria|Anual|0,17|
|NO2|Compañía de Bomberos|Compañía de Bomberos|1h P99|12,74|
|NO2|Compañía de Bomberos|Compañía de Bomberos|Anual|0,24|
|SO2|Ferrocarriles|Primaria|24h P99|0,08|
|SO2|Ferrocarriles|Primaria|1h P98,5|0,63|
|SO2|Ferrocarriles|Primaria|Anual|0,01|
|SO2|Ferrocarriles|Secundaria|24h P99,7|0,08|
|SO2|Ferrocarriles|Secundaria|1h P99,73|0,65|
|SO2|Ferrocarriles|Secundaria|Anual|0,01|

(*): Considera un factor de corrección de 1,15;

Fuente: Elaboración propia.

16
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

**7.** **EVALUACIÓN DE ESCENARIOS**

A continuación, en los siguientes puntos, se presentan las tablas de evaluación de los
escenarios para cada parámetro modelado, en las cuales se comparan los aportes del
Proyecto respecto del Caso Actual proyectado, en los receptores para material particulado
MP 10 y/o gases según corresponda.

Cabe señalar que los escenarios evaluados muestran, en términos de calidad, la diferencia
de los aportes en los receptores evaluados respecto de los niveles de emisión autorizados
vs los niveles de emisión que se encuentran en evaluación, considerando un funcionamiento
continuo de 365 días al año.

**7.1.** **CASO ACTUAL - ESCENARIO OPERACIÓN (USO GAS NATURAL)**

**7.1.1.** **MATERIAL PARTICULADO RESPIRABLE (MP** **10** **Y MP** **2,5** **)**

Respecto del Material Particulado Respirable MP 10 y MP 2,5, la diferencia entre las
concentraciones modeladas del Proyecto y el Caso Actual, en términos de calidad, en todos
sus estadísticos es negativo para los receptores evaluados, por lo que existe una reducción
para el escenario futuro (365 días de funcionamiento continuo). En la Tabla a continuación
se presentan los resultados analizados con respecto a cada normativa evaluada.

17
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

TABLA-19: Diferencia de MP 10 y MP 2,5 [μg/m [3] ] - Caso Actual (Uso de Carbón) vs Escenario Operación (Uso Gas Natural)

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte Caso<br>Actual (CA)<br>[μg/m3]|Aporte<br>Proyecto<br>(P) [μg/m3]|Diferencia<br>(P-CA)<br>[μg/m3]|Norma<br>[μg/m3]|% P-CA c/r<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,57|0,17|-0,40|150|0%|
|MP10|Ferrocarriles|Primaria|Anual|0,11|0,04|-0,07|50|0%|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|24h P98|0,69|0,04|-0,65|150|0%|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|0,15|0,05|-0,10|50|0%|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,57|0,17|-0,40|50|-1%|
|MP2,5|Ferrocarriles|Primaria|Anual|0,11|0,04|-0,07|20|0%|

Fuente: Elaboración propia.

18
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

**7.1.2.** **GASES DIÓXIDO DE NITRÓGENO (NO** **2** **) Y DIÓXIDO DE AZUFRE (SO** **2** **)**

Respecto de gases, la diferencia entre las concentraciones modeladas del Proyecto y el Caso
Actual, en términos de calidad, en todos sus estadísticos es negativo para los receptores
evaluados, por lo que existe una reducción para el escenario futuro (365 días de
funcionamiento continuo). En la Tabla a continuación se presentan los resultados analizados
con respecto a cada normativa evaluada.

19
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

TABLA-20: Concentraciones de NO 2 y SO 2 [μg/m [3] ] - Caso Actual (Uso de Carbón) vs Escenario Operación (Uso Gas Natural)

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte Caso<br>Actual (CA)<br>[μg/m3]|Aporte<br>Proyecto<br>(P) [μg/m3]|Diferencia<br>(P-CA)<br>[μg/m3]|Norma<br>[μg/m3]|% P-CA c/r<br>Norma|
|---|---|---|---|---|---|---|---|---|
|NO2|Ferrocarriles|Primaria|1h P99|34,76|6,18|-28,58|400|-7%|
|NO2|Ferrocarriles|Primaria|Anual|0,66|0,15|-0,51|100|-1%|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|1h P99|50,02|10,87|-39,15|400|-10%|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|0,94|0,21|-0,73|100|-1%|
|SO2|Ferrocarriles|Primaria|24h P99|3,79|0,17|-3,62|150|-2%|
|SO2|Ferrocarriles|Primaria|1h P98,5|34,45|1,24|-33,21|350|-9%|
|SO2|Ferrocarriles|Primaria|Anual|0,61|0,03|-0,58|60|-1%|
|SO2|Ferrocarriles|Secundaria|24h P99,7|3,90|0,17|-3,73|400|-1%|
|SO2|Ferrocarriles|Secundaria|P99 1h|34,55|1,40|-33,15|1.000|-3%|
|SO2|Ferrocarriles|Secundaria|Anual|0,61|0,03|-0,58|80|-1%|

Fuente: Elaboración propia.

20
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

**7.2.** **CASO ACTUAL - ESCENARIO OPERACIÓN (USO DE PETRÓLEO DIÉSEL)**

**7.2.1.** **MATERIAL PARTICULADO RESPIRABLE (MP** **10** **Y MP** **2,5** **)**

Respecto del Material Particulado Respirable MP 10 y MP 2,5, la diferencia entre las
concentraciones modeladas del Proyecto (escenario con uso de petróleo diésel) y el Caso
Actual, en términos de calidad, en todos sus estadísticos es negativo para los receptores
evaluados, por lo que existe una reducción para el escenario futuro (365 días de
funcionamiento continuo). Cabe señalar que para los aportes del Proyecto (escenario uso de
petróleo diésel), fueron considerados, como peor escenario, a un funcionamiento durante el
100% del año.

En la Tabla a continuación se presentan los resultados analizados con respecto a cada
normativa evaluada.

21
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

TABLA-21: Diferencia de MP 10 y MP 2,5 [μg/m [3] ] - Caso Actual (Uso de Carbón) vs Escenario Operación (Uso de Petróleo Diésel)

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte Caso<br>Actual (CA)<br>[μg/m3]|Aporte<br>Proyecto<br>(P) [μg/m3]|Diferencia<br>(P-CA)<br>[μg/m3]|Norma<br>[μg/m3]|% P-CA c/r<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,57|0,09|-0,48|150|0%|
|MP10|Ferrocarriles|Primaria|Anual|0,11|0,02|-0,09|50|0%|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|24h P98|0,69|0,13|-0,56|150|0%|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|0,15|0,03|-0,12|50|0%|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,57|0,09|-0,48|50|-1%|
|MP2,5|Ferrocarriles|Primaria|Anual|0,11|0,02|-0,09|20|0%|

Fuente: Elaboración propia.

22
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

**7.2.2.** **GASES DIÓXIDO DE NITRÓGENO (NO** **2** **) Y DIÓXIDO DE AZUFRE (SO** **2** **)**

Respecto de gases, la diferencia entre las concentraciones modeladas del Proyecto
(escenario con uso de petróleo diésel) y el Caso Actual, en términos de calidad, en todos sus
estadísticos es negativo para los receptores evaluados, por lo que existe una reducción para
el escenario futuro (365 días de funcionamiento continuo). Cabe señalar que para los aportes
del Proyecto (escenario uso de petróleo diésel), fueron considerados, como peor escenario,
a un funcionamiento durante el 100% del año.

En la Tabla a continuación se presentan los resultados analizados con respecto a cada
normativa evaluada.

23
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

TABLA-22: Concentraciones de NO 2 y SO 2 [μg/m [3] ] - Caso Actual (Uso de Carbón) vs Escenario Operación (Uso de Petróleo Diésel)

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte<br>Caso<br>Actual<br>(CA)<br>[μg/m3]|Aporte<br>Proyecto<br>(P) [μg/m3]|Diferencia<br>(P-CA)<br>[μg/m3]|Norma<br>[μg/m3]|% P-CA c/r<br>Norma|
|---|---|---|---|---|---|---|---|---|
|NO2|Ferrocarriles|Primaria|1h P99|34,76|7,56|-27,20|400|-7%|
|NO2|Ferrocarriles|Primaria|Anual|0,66|0,17|-0,49|100|0%|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|1h P99|50,02|12,74|-37,28|400|-9%|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|0,94|0,24|-0,70|100|-1%|
|SO2|Ferrocarriles|Primaria|24h P99|3,79|0,08|-3,71|150|-2%|
|SO2|Ferrocarriles|Primaria|1h P98,5|34,45|0,63|-33,82|350|-10%|
|SO2|Ferrocarriles|Primaria|Anual|0,61|0,02|-0,59|60|-1%|
|SO2|Ferrocarriles|Secundaria|24h P99,7|3,90|0,09|-3,81|400|-1%|
|SO2|Ferrocarriles|Secundaria|P99 1h|34,55|0,65|-33,90|1.000|-3%|
|SO2|Ferrocarriles|Secundaria|Anual|0,61|0,02|-0,59|80|-1%|

Fuente: Elaboración propia.

24
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

**8.** **ANÁLISIS DE RESULTADOS Y CONCLUSIONES**

De los resultados obtenidos en la modelación atmosférica de emisiones, correspondientes
al Caso Actual y los dos escenarios de la Fase de Operación, se concluye que el Proyecto no
generará un incremento en las concentraciones ambientales de material particulado y gases
en las estaciones con representatividad poblacional para material particulado y gases con
respecto a las normas de calidad primaria y secundaria nacionales vigentes.

Respecto de las características del Modelo, se consideró el sistema de modelación
WRF/Calpuff, con un dominio de modelación (computational grid) idéntico al dominio
meteorológico (WRF), correspondiente a 50x50 [km]. En este dominio, se identificaron dos
receptores sensibles, los que corresponden a las Estaciones Ferrocarriles y Compañía de
Bomberos.

Respecto de la línea de base proyectada, es posible señalar que los niveles de concentración
para los parámetros a modelar se encuentran bajo los límites dictados por las normas de
calidad primaria y secundaria nacionales vigentes.

Respecto de las fuentes de emisión, se consideró una fuente de tipo puntual (point), definida
como SRC_1, cuya ubicación es la misma para los escenarios modelados, pero que varía
respecto de la temperatura y velocidad de salida de los gases, así como los niveles de
emisión [g/s]. Los escenarios modelados corresponden a los siguientes:

 - Escenario Caso Actual - RCA N°50/2015;

 Escenario Operación - Uso de Gas Natural;

 Escenario Operación - Uso de Petróleo Diésel.

Respecto de la incertidumbre del modelo, es posible señalar que los estadísticos BIAS e IOA
se encuentran por sobre el rango de bondad de ajuste, tanto para velocidad, como dirección
del viento, por lo que se considera el uso de un factor de corrección, el que corresponde a
1,15.

Respecto de los puntos de máxima concentración, estos se encuentran todos ubicados
próximo al área del Proyecto (único punto), cuyos niveles de concentración se ven reducidos
respecto de la implementación del Proyecto (Caso Actual vs Operación) para todos los
parámetros modelados.

Respecto de los resultados de la implementación del modelo y la evaluación de los
escenarios, es posible señalar que, en términos de calidad, tanto para el escenario Caso
Actual vs Operación Uso Gas Natural, como Caso Actual vs Operación Uso de Petróleo
Diésel, en todos sus estadísticos, la diferencia de concentraciones es negativa para los
receptores evaluados, debido a que existe una reducción de emisiones para el escenario
futuro, considerando un funcionamiento de 365 días continuo.

25
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE

Dado lo anterior, se concluye que el Proyecto en su fase de operación no produce impactos
significativos sobre la salud de las personas, ni recursos naturales, dado que los aportes del
Proyecto (diferencia entre Caso Actual y Escenarios de Operación) reducen los niveles de
concentración para el peor escenario operacional (365 días de funcionamiento). Por ende,
no se produce alguno de los efectos, características o circunstancias de aquellos señalados
en el artículo 11 de la Ley N° 19.300.

26
ANEXO AD-I.7 - ACTUALIZACIÓN INFORME MODELACIÓN CALIDAD DEL AIRE