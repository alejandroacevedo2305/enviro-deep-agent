---
title: Sin título
author: p_reszczynski@jaimeillanes.cl
date: D:20220211104427-03'00'
language: es
type: report
pages: 51
has_toc: True
has_tables: True
extraction_quality: high
---

**ANEXO ADC-4.1**
MODELACIÓN CALIDAD DEL AIRE

_Cliente:_

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

6.2.1. ESCENARIO CASO ACTUAL - RE N°237/2016 ........................................................... 12

6.2.2. ESCENARIO FASE DE OPERACIÓN - USO DE 100% BIOMASA........................... 14

7. EVALUACIÓN DE ESCENARIOS ......................................................................................................... 15

7.1. COMPARACIÓN CASO ACTUAL - ESCENARIO OPERACIÓN (100% USO DE

BIOMASA) ........................................................................................................................................ 15

7.1.1. MATERIAL PARTICULADO RESPIRABLE (MP 10 Y MP 2,5 ) .......................................... 15

7.1.2. GASES DIÓXIDO DE NITRÓGENO (NO 2 ) Y DIÓXIDO DE AZUFRE (SO 2 ) .......... 17

8. ANÁLISIS DE RESULTADOS Y CONCLUSIONES .......................................................................... 19

**APÉNDICES**

APÉNDICE ADC-4.1-1: Archivos de Modelación

APÉNDICE ADC-4.2-2: Isoconcentraciones

ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

**TABLAS**

TABLA ADC-4.1- 1: Norma Primaria de Calidad del Aire MP 10, MP 2,5, NO 2 y SO 2 ................... 2

TABLA ADC-4.1- 2: Norma Secundaria de Calidad del Aire............................................................. 3

TABLA ADC-4.1- 3: Ubicación Receptores primarios y secundarios ............................................. 4

TABLA ADC-4.1- 4: Coordenadas de los vértices del sistema de modelación WRF/Calpuff 4

TABLA ADC-4.1- 5: Línea de Base Proyectada (LBP) por Aporte de Proyectos con RCA que

aún no operan [μg/m [3] N] ......................................................................................... 7

TABLA ADC-4.1- 6: Emisiones del Escenario Caso Actual - RE N°237/2016 ............................. 8

TABLA ADC-4.1- 7: Emisiones del Escenario Operación - Uso de 100% Biomasa .................. 8

TABLA ADC-4.1- 8: Estadígrafos de ajuste de la modelación meteorológica ......................... 10

TABLA ADC-4.1- 9: Coordenadas y concentraciones de los PMC de cada parámetro

modelado - RE N°237/2016 ................................................................................. 11

TABLA ADC-4.1- 10: Coordenadas y concentraciones de los PMC de cada parámetro

modelado - Uso de 100% Biomasa ................................................................... 11

TABLA ADC-4.1- 11: Aportes modelados, Escenario Caso Actual, a los Receptores Primarios

y Secundarios Sin Factor de Corrección .......................................................... 12

TABLA ADC-4.1- 12: Aportes modelados, Escenario Caso Actual, a los Receptores Primarios

y Secundarios Con Factor de Corrección ........................................................ 13

TABLA ADC-4.1- 13: Aportes modelados, Escenario Fase de Operación (Uso de 100%

Biomasa), a los Receptores Primarios y Secundarios Sin Factor de
Corrección ................................................................................................................... 14

TABLA ADC-4.1- 14: Aportes modelados, Escenario Fase de Operación (Uso de 100%

Biomasa), a los Receptores Primarios y Secundarios Con Factor de
Corrección ................................................................................................................... 14

TABLA ADC-4.1- 15: Diferencia de MP 10 [μg/m [3] N] y MP 2,5 [μg/m [3] ] - Caso Actual vs Escenario

Operación (100% Uso de Biomasa) ................................................................... 16

TABLA ADC-4.1- 16: Concentraciones de NO 2 y SO 2 [μg/m [3] N] - Caso Actual vs Escenario

Operación (100% Uso de Biomasa) ................................................................... 18

**FIGURAS**

FIGURA ADC-4.1- 1: Dominio de Modelación (Computacional Grid), fuentes emisoras y

receptores. .................................................................................................................... 9

FIGURA ADC-4.1- 2: Frecuencia relativa de la dirección del viento observada y modelada

(WRF). Estación Ferrocarriles ................................................................................ 10

ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

**1.** **INTRODUCCIÓN**

En el marco de la presentación de la Declaración de Impacto Ambiental del Proyecto
“ **Operación Unidades CTA/CTH con 100% de Biomasa** ” (en adelante el Proyecto), el
presente informe da cuenta del análisis del transporte y dispersión de contaminantes
emitidos para los escenarios máximos evaluados autorizados para el caso actual y la
evaluación de la fase de operación del Proyecto, ubicado en el área industrial de la comuna
de Mejillones, provincia de Antofagasta, en la Región de Atacama.

La simulación de los aportes del Proyecto a las concentraciones ambientales se realiza
mediante la aplicación del sistema de modelación WRF/CALPUFF; sistema que considera la
utilización de la modelación meteorológica para el año 2019 (WRF) y un dominio de
modelación de Calpuff de 50x50 [km] con una resolución de 1x1 [km], la cual incluye como
receptores a las Estaciones Ferrocarriles y Compañía de Bomberos, las que se encuentran
presentes en el área determinada por el dominio de modelación, donde se registraron
valores basales de material particulado y gases.

A continuación, se presenta el análisis de la dispersión y transporte de las emisiones
correspondientes al escenario máximo informado para el caso actual y para la evaluación de
la fase de operación del Proyecto, que considera las emisiones en ton/día, llevadas a un
escenario operacional de 365 días (año completo de funcionamiento). El escenario caso
actual corresponde a los límites señalados en la Consulta de Pertinencia resuelta mediante
la RE N°237/2016; para el caso de la fase de operación, se consideran las máximas emisiones
obtenidas producto del uso de 100% Biomasa.

En concordancia a lo señalado en la Guía para el uso de modelos de calidad del aire en el
SEIA (emitida por el Servicio de Evaluación Ambiental el año 2012), los resultados de la
modelación se entregan en tablas a modo de comparar los aportes del Proyecto con y sin
factor de corrección.

Además, se comparan los resultados de la modelación respecto del caso actual y el escenario
de operación, y a su vez, respecto de las normas primarias y secundarias de calidad del aire
nacionales (artículo 11 del D.S. N° 40/12 MMA, que aprueba el Reglamento del Sistema de
Evaluación de Impacto Ambiental -RSEIA-), de manera de evaluar la reducción de emisiones
en términos de concentración.

Los parámetros que se analizan corresponden a MP 10 ; MP 2,5 ; NO 2 y SO 2 . Se indica que los
archivos digitales de la modelación con CALPUFF (salidas y entradas) son subidos al sistema
de manera digital en el Apéndice ADC-4.1-1.

1
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

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

TABLA ADC-4.1- 1: Norma Primaria de Calidad del Aire MP 10, MP 2,5, NO 2 y SO 2

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**MP10 **|D.S. N°59/98<br>MINSEGPRES,<br>modificada por<br>D.S.N°45/01|Promedio aritmético de tres años calendario<br>consecutivos|50 μg/m3N|
|**MP10 **|D.S. N°59/98<br>MINSEGPRES,<br>modificada por<br>D.S.N°45/01|Percentil 98 de las concentraciones de 24 horas<br>registradas durante un período anual|150 μg/m3N|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Promedio tri-anual de las concentraciones<br>anuales|20 μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Percentil 98 de los promedios diarios registrados<br>durante un año|50 μg/m3|
|**NO2 **|D.S. N° 114/2002 del<br>MINSEGPRES|Promedio<br>aritmético<br>de<br>los<br>valores<br>de<br>concentración anual de tres años calendarios<br>sucesivos|100 μg/m3N|
|**NO2 **|D.S. N° 114/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario|400 μg/m3N|
|**SO2 **|D.S. N° 104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 99 de las<br>concentraciones de 24 horas registradas cada<br>año|150 μg/m3N|
|**SO2 **|D.S. N° 104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores de concentración anual|60 μg/m3N|
|**SO2 **|D.S. N° 104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 98,5 de las<br>concentraciones de 1 hora registradas cada año|350 μg/m3N|

Fuente: Elaboración propia.

2
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

TABLA ADC-4.1- 2: Norma Secundaria de Calidad del Aire

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**SO2**|D.S. N°22/09 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos<br>del<br>Percentil<br>99,73<br>de<br>las<br>concentraciones de 1 hora registradas cada año|1.000<br>μg/m3N|
|**SO2**|D.S. N°22/09 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos<br>del<br>Percentil<br>99,7<br>de<br>las<br>concentraciones diarias|365 μg/m3N|
|**SO2**|D.S. N°22/09 del<br>MINSEGPRES|Promedio anual de 3 años sucesivos|80 μg/m3N|

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
resultados confiables para distancias de hasta 100 [km].

El sistema de modelación incluye tres componentes principales: Calmet, Calpuff y Calpost,
además de una serie de programas de pre-procesamiento diseñados para la preparación de
la información meteorológica y geofísica, En este caso, no fue necesario utilizar los preprocesadores ni el módulo Calmet, ya que se emplearon los resultados de la modelación
meteorológica realizada con WRF.

1 40 CFR Part 51, Revision to the Guideline on Air Quality Models: Adoption of a Preferred General Purpose (Flat
and Complex Terrain) Dispersion Model and Other Revisions; Final Rule.
http://www.epa.gov/ttn/scram/guidance/guide/appw_05.pdf

3
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

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

TABLA ADC-4.1- 3: Ubicación Receptores primarios y secundarios

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

TABLA ADC-4.1- 4: Coordenadas de los vértices del sistema de modelación WRF/Calpuff

|Vértices|Coordenadas UTM [m] Datum: WGS-84, Huso: 19S|Col3|
|---|---|---|
|**Vértices**|**Este**|**Norte**|
|**SW**|331.622|7.418.804|
|**NE**|381.226|7.469.080|
|**NW**|331.144|7.468.601|
|**SE**|381.705|7.419.286|

Fuente: Elaboración propia.

4
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

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

El modelo WRF analizado ha sido parametrizado de acuerdo con lo establecido por el SEA y
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
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

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
proyectos aprobados que aún no se encuentran en Construcción al momento de medir, por
tanto, para considerar dichos aportes de terceros se les suman a los valores monitoreados
obteniendo una línea base proyectada en el tiempo. Para ello, se revisaron los proyectos de
terceros que estuvieran al interior del área de influencia de calidad del aire del presente
Proyecto y que no estuvieran operando hasta septiembre de 2020.

Resultado de lo anterior se obtuvo la tabla con la línea base proyectada (LBP), con un
incremento en las concentraciones monitoreadas en la Línea de Base, ya que considera los
aportes de terceros más los valores monitoreados, la cual se presenta a continuación en la
siguiente Tabla. Para mayor detalle, revisar la “Línea de Base Calidad del Aire” de la presente

DIA.

6
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

TABLA ADC-4.1- 5: Línea de Base Proyectada (LBP) por Aporte de Proyectos con RCA que

aún no operan

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Línea de Base<br>Proyectada|Unidad|
|---|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|41|[μg/m3N]|
|MP10|Ferrocarriles|Primaria|Anual|16|16|
|MP10|Compañía<br>de<br>Bomberos|Compañía<br>de<br>Bomberos|24h P98|46|46|
|MP10|Compañía<br>de<br>Bomberos|Compañía<br>de<br>Bomberos|Anual|18|18|
|MP2,5|Ferrocarriles|Primaria|24h P98|17|[μg/m3]|
|MP2,5|Ferrocarriles|Primaria|Anual|7|7|
|SO2|Ferrocarriles|Primaria|24h P99|6|[μg/m3N]|
|SO2|Ferrocarriles|Primaria|1h P98,5|22|22|
|SO2|Ferrocarriles|Primaria|Anual|2|2|
|SO2|Ferrocarriles|Secundaria|24h P99,7|9|9|
|SO2|Ferrocarriles|Secundaria|1h P99,73|22|22|
|SO2|Ferrocarriles|Secundaria|Anual|2|2|
|NO2|Ferrocarriles|Primaria|1h P99|41|[μg/m3N]|
|NO2|Ferrocarriles|Primaria|Anual|3|3|
|NO2|Compañía<br>de<br>Bomberos|Compañía<br>de<br>Bomberos|1h P99|40|40|
|NO2|Compañía<br>de<br>Bomberos|Compañía<br>de<br>Bomberos|Anual|10|10|

Fuente: Anexo C2-2 de la presente DIA.

**5.3.** **PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN**

El resumen de las emisiones de cada una de las fuentes emisoras ingresadas al modelo para
cada escenario de modelación, en unidades de [g/s], se presentan en las Tablas a
continuación.

7
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

TABLA ADC-4.1- 6: Emisiones del Escenario Caso Actual - RE N°237/2016

|Tipo de Fuente|ID|Descripción|Elevación de<br>la Chimenea<br>[m]|Temperatura<br>de salida de<br>gases [K]|Diámetro de<br>la Chimenea<br>[m]|Velocidad<br>de salida<br>de gases<br>[m/s]|MP<br>10<br>[g/s]|MP<br>2,5<br>[g/s]|NO<br>2<br>[g/s]|SO<br>2<br>[g/s]|
|---|---|---|---|---|---|---|---|---|---|---|
|Point|SRC_1|CTA|85|407|3,60|31,80|9,30|9,30|78,10|74,10|
|Point|SRC_2|CTH|85|407|3,60|31,80|9,30|9,30|78,10|74,10|

Fuente: Elaboración propia.

TABLA ADC-4.1- 7: Emisiones del Escenario Operación - Uso de 100% Biomasa

|Tipo de Fuente|ID|Descripción|Elevación de<br>la Chimenea<br>[m]|Temperatura<br>de salida de<br>gases [K]|Diámetro de<br>la Chimenea<br>[m]|Velocidad<br>de salida<br>de gases<br>[m/s]|MP<br>10<br>[g/s]|MP<br>2,5<br>[g/s]|NO<br>2<br>[g/s]|SO<br>2<br>[g/s]|
|---|---|---|---|---|---|---|---|---|---|---|
|Point|SRC_1|CTA|85|407|3,60|39,75|6,10|6,10|65,30|4,30|
|Point|SRC_2|CTH|85|407|3,60|39,75|6,10|6,10|65,30|4,30|

Fuente: Elaboración propia.

8
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

A continuación, en la siguiente Figura se presenta la ubicación del dominio de modelación,
fuentes emisoras y receptores para cada escenario de evaluación. Dado que la ubicación de
los receptores y las fuentes de emisión es la misma, solo se presenta una figura para
referenciar la ubicación.

FIGURA ADC-4.1- 1: Dominio de Modelación (Computacional Grid), fuentes emisoras y

receptores.

Fuente: Elaboración propia.

**5.4.** **ANALISIS DE INCERTIDUMBRE Y DETERMINACIÓN DEL FACTOR DE**
**CORRECCIÓN**

A partir de los datos meteorológicos del año 2019 para la Estación Ferrocarriles, se realizó
un análisis de estadígrafo, obteniendo los resultados presentados en la tabla a continuación.

9
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

TABLA ADC-4.1- 8: Estadígrafos de ajuste de la modelación meteorológica

|Receptor|Variable|RMSE|BIAS|Bondad BIAS|IOA|Bondad IOA|
|---|---|---|---|---|---|---|
|Estación<br>Ferrocarriles|Dirección del<br>viento (°)|126,54|-13,06|<+-/10|0,45|--|
|Estación<br>Ferrocarriles|Velocidad del<br>viento (m/s)|1,89|-0,73|<+-/0,5|0,69|>0,60|

Fuente: Elaboración propia.

De la tabla anterior, se desprende que la velocidad del viento (m/s) en el estadístico BIAS e
IOA se encuentra por sobre el rango de bondad. Con respecto a la dirección del viento, el
estadístico BIAS se encuentra sobre los rangos de bondad.

De acuerdo a la metodología descrita en el numeral 4.3, se graficaron las frecuencias relativas
de las direcciones del viento que favorecen el transporte de los parámetros atmosféricos a
modelar, hacia el receptor Hospital, a modo de determinar los parámetros F WRF y F obs . El
gráfico de las frecuencias relativas señaladas se realizó tanto de los datos registrados en la
estación de monitoreo, como los datos modelados con WRF, lo cual se muestra a

continuación:

FIGURA ADC-4.1- 2: Frecuencia relativa de la dirección del viento observada y modelada

(WRF). Estación Ferrocarriles

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
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

**6.** **RESULTADOS**

A continuación, se presentan los aportes estimados de la Operación para cada uno de los
parámetros modelados.

**6.1.** **PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC)**

En las Tablas a continuación se presentan las coordenadas y aportes de los puntos de
máxima concentración modelada, para cada parámetro y estadístico para cada escenario de
modelación.

TABLA ADC-4.1- 9: Coordenadas y concentraciones de los PMC de cada parámetro

modelado - RE N°237/2016

|Norma|Parámetro|ID|Coordenadas UTM<br>[m]<br>WGS84 Huso 19S|Col5|Coordenadas<br>LCC [km]<br>Datum<br>NWS-84|Col7|PMC|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|**Norte**|
|MP10 <br>Primaria|Promedio Anual|PMC1|355.896|7.446.420|-0,50|2,50|3,90|[μg/m3N]|
|MP10 <br>Primaria|P98 diario|PMC1|355.896|7.446.420|-0,50|2,50|9,27|9,27|
|MP2,5 <br>Primaria|Promedio Anual|PMC1|355.896|7.446.420|-0,50|2,50|3,90|[μg/m3]|
|MP2,5 <br>Primaria|P98 diario|PMC1|355.896|7.446.420|-0,50|2,50|9,27|9,27|
|NO2 <br>Primario|Promedio Anual|PMC1|355.896|7.446.420|-0,50|2,50|32,73|[μg/m3N]|
|NO2 <br>Primario|P99 horario|PMC2|355.907|7.445.428|-0,50|1,50|641,33|641,33|
|SO2 <br>Primaria|Promedio Anual|PMC1|355.896|7.446.420|-0,50|2,50|30,86|[μg/m3N]|
|SO2 <br>Primaria|P99 diario|PMC1|355.896|7.446.420|-0,50|2,50|77,12|77,12|
|SO2 <br>Primaria|P98,5hr|PMC2|355.907|7.445.428|-0,50|1,50|604,19|604,19|
|SO2 <br>Secundaria|Promedio Anual|PMC1|355.896|7.446.420|-0,50|2,50|30,86|30,86|
|SO2 <br>Secundaria|P99,7 diario|PMC1|355.896|7.446.420|-0,50|2,50|79,69|79,69|
|SO2 <br>Secundaria|P99,73 hr|PMC2|355.907|7.445.428|-0,50|1,50|639,47|639,47|

Fuente: Elaboración propia.

TABLA ADC-4.1- 10: Coordenadas y concentraciones de los PMC de cada parámetro

modelado - Uso de 100% Biomasa

|Norma|Parámetro|ID|Coordenadas UTM<br>[m]<br>WGS84 Huso 19S|Col5|Coordenadas<br>LCC [km]<br>Datum<br>NWS-84|Col7|PMC|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|**Norte**|
|MP10 <br>Primaria|Promedio Anual|PMC2|355.907|7.445.428|-0,50|1,50|5,88|[μg/m3N]|
|MP10 <br>Primaria|P98 diario|PMC1|355.896|7.446.420|-0,50|2,50|2,22|2,22|
|MP2,5 <br>Primaria|Promedio Anual|PMC2|355.907|7.445.428|-0,50|1,50|5,88|[μg/m3]|
|MP2,5 <br>Primaria|P98 diario|PMC1|355.896|7.446.420|-0,50|2,50|2,22|2,22|
||Promedio Anual|PMC1|355.896|7.446.420|-0,50|2,50|23,75|[μg/m3N]|

11
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

|Norma<br>NO<br>2<br>Primario|Parámetro|ID|Coordenadas UTM<br>[m]<br>WGS84 Huso 19S|Col5|Coordenadas<br>LCC [km]<br>Datum<br>NWS-84|Col7|PMC|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Norma**<br>NO2 <br>Primario|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|**Norte**|
|**Norma**<br>NO2 <br>Primario|P99 horario|PMC2|355.907|7.445.428|-0,50|1,50|527,54|527,54|
|SO2 <br>Primaria|Promedio Anual|PMC1|355.896|7.446.420|-0,50|2,50|1,55|[μg/m3N]|
|SO2 <br>Primaria|P99 diario|PMC2|355.907|7.445.428|-0,50|1,50|4,45|4,45|
|SO2 <br>Primaria|P98,5hr|PMC2|355.907|7.445.428|-0,50|1,50|34,50|34,50|
|SO2 <br>Secundaria|Promedio Anual|PMC1|355.896|7.446.420|-0,50|2,50|1,55|1,55|
|SO2 <br>Secundaria|P99,7 diario|PMC2|355.907|7.445.428|-0,50|1,50|4,47|4,47|
|SO2 <br>Secundaria|P99,73 hr|PMC2|355.907|7.445.428|-0,50|1,50|34,56|34,56|

Fuente: Elaboración propia.

En el Apéndice ADC-4.1-2 se presenta la representación gráfica de cada uno de los puntos
de máxima concentración.

**6.2.** **RESULTADOS DE LA MODELACIÓN**

A continuación, se presentan los resultados de la modelación para cada uno de los
parámetros modelados de acuerdo con los estadísticos definidos en cada una de las normas
primarias y secundarias de calidad del aire evaluado, diferenciado por escenario de
modelación. Los resultados son presentados con y sin factor de corrección respectivamente
y de acuerdo con lo detallado en el numeral 4.3 (Análisis de incertidumbre) y lo solicitado
en la Guía de modelación.

**6.2.1.** **ESCENARIO CASO ACTUAL - RE N°237/2016**

En las siguientes tablas se presentan los aportes sin factor de corrección y con factor de
corrección para los receptores identificados.

TABLA ADC-4.1- 11: Aportes modelados, Escenario Caso Actual, a los Receptores

Primarios y Secundarios Sin Factor de Corrección

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte|Unidad|
|---|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,85|[μg/m3N]|
|MP10|Ferrocarriles|Primaria|Anual|0,15|0,15|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|24h P98|1,12|1,12|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|0,22|0,22|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,85|[μg/m3]|
|MP2,5|Ferrocarriles|Primaria|Anual|0,15<br>|0,15<br>|

12
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte|Unidad|
|---|---|---|---|---|---|
|NO2|Ferrocarriles|Primaria|1h P99|60,35|[μg/m3N]|
|NO2|Ferrocarriles|Primaria|Anual|1,26|1,26|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|1h P99|88,96|88,96|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|1,77|1,77|
|SO2|Ferrocarriles|Primaria|24h P99|7,14|[μg/m3N]|
|SO2|Ferrocarriles|Primaria|1h P98,5|57,03|57,03|
|SO2|Ferrocarriles|Primaria|Anual|1,10|1,10|
|SO2|Ferrocarriles|Secundaria|24h P99,7|7,08|7,08|
|SO2|Ferrocarriles|Secundaria|1h P99,73|57,95|57,95|
|SO2|Ferrocarriles|Secundaria|Anual|1,10|1,10|

Fuente: Elaboración propia.

TABLA ADC-4.1- 12: Aportes modelados, Escenario Caso Actual, a los Receptores

Primarios y Secundarios Con Factor de Corrección

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte<br>Rectificado*|Unidad|
|---|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,98|[μg/m3N]|
|MP10|Ferrocarriles|Primaria|Anual|0,18|0,18|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|24h P98|1,29|1,29|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|0,26|0,26|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,98|[μg/m3]|
|MP2,5|Ferrocarriles|Primaria|Anual|0,18|0,18|
|NO2|Ferrocarriles|Primaria|1h P99|69,41|[μg/m3N]|
|NO2|Ferrocarriles|Primaria|Anual|1,45|1,45|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|1h P99|102,31|102,31|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|2,04|2,04|
|SO2|Ferrocarriles|Primaria|24h P99|8,22|[μg/m3N]|
|SO2|Ferrocarriles|Primaria|1h P98,5|65,59|65,59|
|SO2|Ferrocarriles|Primaria|Anual|1,27|1,27|
|SO2|Ferrocarriles|Secundaria|24h P99,7|8,15|8,15|
|SO2|Ferrocarriles|Secundaria|1h P99,73|66,65|66,65|
|SO2|Ferrocarriles|Secundaria|Anual|1,27|1,27|

(*): Considera un factor de corrección de 1,15;

Fuente: Elaboración propia.

13
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

**6.2.2.** **ESCENARIO FASE DE OPERACIÓN - USO DE 100% BIOMASA**

En las siguientes tablas se presentan los aportes sin factor de corrección y con factor de
corrección para los receptores identificados.

TABLA ADC-4.1- 13: Aportes modelados, Escenario Fase de Operación (Uso de 100%

Biomasa), a los Receptores Primarios y Secundarios Sin Factor de Corrección

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte|Unidad|
|---|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,52|[μg/m3N]|
|MP10|Ferrocarriles|Primaria|Anual|0,10|0,10|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|24h P98|0,77|0,77|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|0,14|0,14|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,52|[μg/m3]|
|MP2,5|Ferrocarriles|Primaria|Anual|0,10|0,10|
|NO2|Ferrocarriles|Primaria|1h P99|51,15|[μg/m3N]|
|NO2|Ferrocarriles|Primaria|Anual|1,00|1,00|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|1h P99|83,75|83,75|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|1,47|1,47|
|SO2|Ferrocarriles|Primaria|24h P99|0,41|[μg/m3N]|
|SO2|Ferrocarriles|Primaria|1h P98,5|3,33|3,33|
|SO2|Ferrocarriles|Primaria|Anual|0,06|0,06|
|SO2|Ferrocarriles|Secundaria|24h P99,7|0,43|0,43|
|SO2|Ferrocarriles|Secundaria|1h P99,73|3,45|3,45|
|SO2|Ferrocarriles|Secundaria|Anual|0,06|0,06|

Fuente: Elaboración propia.

TABLA ADC-4.1- 14: Aportes modelados, Escenario Fase de Operación (Uso de 100%

Biomasa), a los Receptores Primarios y Secundarios Con Factor de Corrección

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte<br>Rectificado*|Unidad|
|---|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|0,60|[μg/m3N]|
|MP10|Ferrocarriles|Primaria|Anual|0,12|0,12|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|24h P98|0,89|0,89|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|0,17|0,17|
|MP2,5|Ferrocarriles|Primaria|24h P98|0,60|[μg/m3]|
|MP2,5|Ferrocarriles|Primaria|Anual|0,12|0,12|

14
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte<br>Rectificado*|Unidad|
|---|---|---|---|---|---|
|NO2|Ferrocarriles|Primaria|1h P99|58,83|[μg/m3N]<br>|
|NO2|Ferrocarriles|Primaria|Anual|1,15|1,15|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|1h P99|96,32|96,32|
|NO2|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|1,70|1,70|
|SO2|Ferrocarriles|Primaria|24h P99|0,48|<br> <br> <br>[μg/m3N]|
|SO2|Ferrocarriles|Primaria|1h P98,5|3,83|3,83|
|SO2|Ferrocarriles|Primaria|Anual|0,07|0,07|
|SO2|Ferrocarriles|Secundaria|24h P99,7|0,50|0,50|
|SO2|Ferrocarriles|Secundaria|1h P99,73|3,97|3,97|
|SO2|Ferrocarriles|Secundaria|Anual|0,07|0,07|

(*): Considera un factor de corrección de 1,15;

Fuente: Elaboración propia.

**7.** **EVALUACIÓN DE ESCENARIOS**

A continuación, en los siguientes puntos, se presentan las tablas de evaluación de los
escenarios para cada parámetro modelado, en las cuales se comparan los aportes del
Proyecto respecto del Caso Actual proyectado, en los receptores para material particulado
MP 10 y/o gases según corresponda.

Cabe señalar que los escenarios evaluados muestran, en términos de calidad, la diferencia
de los aportes en los receptores evaluados respecto de los niveles de emisión autorizados
vs los niveles de emisión que se encuentran en evaluación, considerando un funcionamiento
continuo de 365 días al año.

**7.1.** **COMPARACIÓN CASO ACTUAL - ESCENARIO OPERACIÓN (100% USO DE**

**BIOMASA)**

**7.1.1.** **MATERIAL PARTICULADO RESPIRABLE (MP** **10** **Y MP** **2,5** **)**

Respecto del Material Particulado Respirable MP 10 y MP 2,5, la diferencia entre las
concentraciones modeladas del Proyecto y el Caso Actual, en términos de calidad, en todos
sus estadísticos es negativo para los receptores evaluados, por lo que existe una reducción
para el escenario futuro (365 días de funcionamiento continuo). En la Tabla a continuación
se presentan los resultados analizados con respecto a cada normativa evaluada.

15
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

TABLA ADC-4.1- 15: Diferencia de MP 10 [μg/m [3] N] y MP 2,5 [μg/m [3] ] - Caso Actual vs Escenario Operación (100% Uso de Biomasa)

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Unidad|Aporte Caso<br>Actual (CA)|Aporte<br>Proyecto (P)|Diferencia<br>(P-CA)|% P-CA c/r<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Ferrocarriles|Primaria|24h P98|[μg/m3N]|0,98|0,60|-0,38|0%|
|MP10|Ferrocarriles|Primaria|Anual|Anual|0,18|0,12|-0,06|0%|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|24h P98|24h P98|1,29|0,89|-0,40|0%|
|MP10|Compañía de<br>Bomberos|Compañía de<br>Bomberos|Anual|Anual|0,26|0,17|-0,09|0%|
|MP2,5|Ferrocarriles|Primaria|24h P98|[μg/m3]|0,98|0,60|-0,38|-1%|
|MP2,5|Ferrocarriles|Primaria|Anual|Anual|0,18|0,12|-0,06|0%|

Fuente: Elaboración propia.

16
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

**7.1.2.** **GASES DIÓXIDO DE NITRÓGENO (NO** **2** **) Y DIÓXIDO DE AZUFRE (SO** **2** **)**

Respecto de gases, la diferencia entre las concentraciones modeladas del Proyecto y el Caso
Actual, en términos de calidad, en todos sus estadísticos es negativo para los receptores
evaluados, por lo que existe una reducción para el escenario futuro (365 días de
funcionamiento continuo). En la Tabla a continuación se presentan los resultados analizados
con respecto a cada normativa evaluada.

17
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

TABLA ADC-4.1- 16: Concentraciones de NO 2 y SO 2 [μg/m [3] N] - Caso Actual vs Escenario Operación (100% Uso de Biomasa)

|Parámetro|Estación|Tipo de<br>Norma|Estadístico|Aporte Caso<br>Actual (CA)<br>[μg/m3N]|Aporte<br>Proyecto (P)<br>[μg/m3N]|Diferencia (P-<br>CA) [μg/m3N]|% P-CA c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|NO2|Ferrocarriles|Primaria|1h P99|69,41|58,83|-10,58|-3%|
|NO2|Ferrocarriles|Primaria|Anual|1,45|1,15|-0,30|0%|
|NO2|Compañía de Bomberos|Compañía de Bomberos|1h P99|102,31|96,32|-5,99|-1%|
|NO2|Compañía de Bomberos|Compañía de Bomberos|Anual|2,04|1,70|-0,34|0%|
|SO2|Ferrocarriles|Primaria|24h P99|8,22|0,48|-7,74|-5%|
|SO2|Ferrocarriles|Primaria|1h P98,5|65,59|3,83|-61,76|-18%|
|SO2|Ferrocarriles|Primaria|Anual|1,27|0,07|-1,20|-2%|
|SO2|Ferrocarriles|Secundaria|24h P99,7|8,15|0,50|-7,65|-2%|
|SO2|Ferrocarriles|Secundaria|1h P99,73|66,65|3,97|-62,68|-6%|
|SO2|Ferrocarriles|Secundaria|Anual|1,27|0,07|-1,20|-2%|

Fuente: Elaboración propia.

18
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

**8.** **ANÁLISIS DE RESULTADOS Y CONCLUSIONES**

De los resultados obtenidos en la modelación atmosférica de emisiones, correspondientes
al Caso Actual y del escenario máximo para la Fase de Operación, se concluye que el
Proyecto “ **Operación Unidades CTA/CTH con 100% de Biomasa** ” no generará un
incremento en las concentraciones ambientales de material particulado y gases en las
estaciones con representatividad poblacional para material particulado y gases con respecto
a las normas de calidad primaria y secundaria nacionales vigentes.

Respecto de las características del Modelo, se consideró el sistema de modelación
WRF/Calpuff, con un dominio de modelación (computational grid) idéntico al dominio
meteorológico (WRF), correspondiente a 50x50 [km]. En este dominio, se identificaron dos
receptores sensibles, los que corresponden a las Estaciones Ferrocarriles y Compañía de
Bomberos.

Respecto de la línea de base proyectada, es posible señalar que los niveles de concentración
para los parámetros a modelar se encuentran bajo los límites dictados por las normas de
calidad primaria y secundaria nacionales vigentes.

Respecto de las fuentes de emisión, se consideraron dos fuentes de tipo puntual (point),
definidas como SRC_1 y SRC_2, cuya ubicación es la misma para los escenarios modelados,
pero que varía respecto de los niveles de emisión [g/s]. Los escenarios modelados
corresponden a los siguientes:

 - Escenario Caso Actual - RE N°237/2016;

 Escenario Operación - Uso de 100% Biomasa.

Respecto de la incertidumbre del modelo, es posible señalar que los estadísticos BIAS e IOA
se encuentran por sobre el rango de bondad de ajuste, tanto para velocidad, como dirección
del viento, por lo que se considera el uso de un factor de corrección, el que corresponde a
1,15.

Respecto de los puntos de máxima concentración, estos se encuentran todos ubicados
próximo al área del Proyecto, cuyos niveles de concentración se ven reducidos respecto de
la implementación del Proyecto (Caso Actual vs Operación) para todos los parámetros
modelados.

Respecto de los resultados de la implementación del modelo y la evaluación de los
escenarios, es posible señalar que, en términos de calidad, para el escenario Caso Actual vs
Operación (Uso de 100% Biomasa), en todos sus estadísticos, la diferencia de
concentraciones es negativa para los receptores evaluados, debido a que existe una
reducción de emisiones para el escenario futuro, considerando un funcionamiento de 365
días continuo.

19
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

Dado lo anterior, se concluye que el Proyecto en su etapa de Operación no produce
impactos significativos sobre la salud de las personas, ni recursos naturales, dado que los
aportes del Proyecto (diferencia entre Caso Actual y Escenario de Operación) reducen los
niveles de concentración para el peor escenario operacional (365 días de funcionamiento).
Por ende, no se produce alguno de los efectos, características o circunstancias de aquellos
señalados en el artículo 11 de la Ley N° 19.300.

20
ANEXO ADC-4.1 - MODELACIÓN CALIDAD DEL AIRE

**APÉNDICE ADC-4.1-1**

ARCHIVOS DE MODELACIÓN

_Cliente:_

De acuerdo a lo señalado en los artículos 31 y 32 (del Articulo Segundo) de la Ley N° 20.417
que “Crea el Ministerio, el Servicio de Evaluación Ambiental y la Superintendencia del Medio
Ambiente” emanada por el Ministerio Secretaria General de la Presidencia; se informa que
dada la naturaleza de los documentos los archivos Digitales de Modelación de Dispersión
Atmosférica CALPUFF, no es posible agregarlos directamente al expediente electrónico,
motivo por el cual dicha información se encuentra disponible para el público en general en
las oficinas del Servicio de Evaluación Ambiental (SEA) de la Región de Antofagasta.

Asimismo, y tal como es señalado en el Of. Ord. N°202099102718, se han actualizado las
directrices sobre la foliación y el registro de expedientes en el Sistema de Evaluación de
Impacto Ambiental (SEIA), sobre la “Solicitud de entrega de archivos de gran tamaño”, donde
se señala que “en caso de existir excepcionalmente documentos que durante el proceso de
evaluación de impacto ambiental se separen del expediente electrónico, en atención a su
tamaño en uso de memoria (bytes) o archivos de gran tamaño (mayor a 100MB), se deberá
emitir una resolución indicando tal situación, **incorporándola al expediente electrónico**
**en la fecha y hora en que se recibió, acompañado el comprobante de recepción emitido**
**por la oficina de partes** . Dicha información deberá incorporarse en el repositorio
[https://archivos.sea.gob.cl/, o el medio de respaldo que lo reemplace (...)”.](https://archivos.sea.gob.cl/)

Dicha información fue recibida por la oficina de partes con fecha 14/07/2021 a las 17:57
horas, cuyo comprobante de recepción emitido por la oficina de partes es acompañado en
el presente apéndice.

Los interesados en obtener dicha documentación deben comunicarse con Oficina de

Información y Atención Ciudadana del SEA Regional, ingresando su requerimiento a través
del siguiente formulario:

[http://www.portaltransparencia.cl/PortalPdT/web/guest](http://www.portaltransparencia.cl/PortalPdT/web/guest)

APÉNDICE ADC- 4. 1-1 - ARCHIVOS DE MODELACIÓN

1

**Anexo N** **[O ]** **5 - Acuse de recibo para entrega de archivos de gran tamaño**

Estimado Sr.

Mediante el presente acusamos recibo, en la fecha y hora de este correo, de los documentos que

se detallan a continuación, los cuales cumplen con las condiciones necesarias para la entrega de

documentos de gran tamaño al SEA:

Antecedentes del proyecto

I
Nombre del proyecto: OPERACIÓN UNIDADES CTA/CTH CON 100% DE BIOMASA

I
Modalidad de ingreso (EIA, DIA, Adenda): DIA

Antecedentes de los archivos de gran tamaño recibidos:

|Col1|Nombre y Extensión del Archivo|Tamaño del Archivo<br>(>100 Mb)|
|---|---|---|
|1|WRF.zip|4,17 GB|
|2|Escenario Caso Actual|584 MB|
|3|Escenario Fase de Operación|576 MB|
|4|||
|5|||
|6|||
|7|||

Saluda cordialmente

```
━━━━━━━━

```

**Cristian Paredes Loins**

Oficial de Partes
Dirección Regional de Antofagasta
(56-55) 2467100

**Servicio de Evaluación Ambiental**
**Gobierno de Chile**

**APÉNDICE ADC-4.1-2**

ISOCONCENTRACIONES

_Cliente:_

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
||||")<br>**Me**|")<br>!P<br>**jillones**|")<br>!P<br>**jillones**|**")**<br>#||||||||
|||||||||||||||
|||||||||||||||
||||**Comuna de**<br>**Mejillones**|||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||**Comuna de**<br>**Antofagasta**|**Comuna de**<br>**Antofagasta**|_F_|~~")~~<br>_errocarriles_<br>_Compañia de_<br>_Bomberos_|~~")~~<br>_errocarriles_<br>_Compañia de_<br>_Bomberos_||||**")**<br># PMC 2<br>SRC_2 (CTH)<br>SRC_1 (CTA)||
||||||||~~")~~<br>|~~")~~<br>||||||
|||||||||||||||
|||||||||||||||

**362500**

**369000**

**382000**

**356000**

**375500**

|30000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|Col9|382000|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**<br>|**Fuente de información**<br>|TITULAR<br><br><br>|TITULAR<br><br><br>|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>agen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|**Escala gráfica y nominal**<br><br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|**0**<br>**1**<br>**2**<br>**3**<br>**4**<br>**km.**<br>**1:200.000**|**0**<br>**1**<br>**2**<br>**3**<br>**4**<br>**km.**<br>**1:200.000**|**0**<br>**1**<br>**2**<br>**3**<br>**4**<br>**km.**<br>**1:200.000**|**0**<br>**1**<br>**2**<br>**3**<br>**4**<br>**km.**<br>**1:200.000**|**0**<br>**1**<br>**2**<br>**3**<br>**4**<br>**km.**<br>**1:200.000**|**0**<br>**1**<br>**2**<br>**3**<br>**4**<br>**km.**<br>**1:200.000**|**0**<br>**1**<br>**2**<br>**3**<br>**4**<br>**km.**<br>**1:200.000**|**0**<br>**1**<br>**2**<br>**3**<br>**4**<br>**km.**<br>**1:200.000**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br><br>|**LÁMINA**<br><br>|**LÁMINA**<br><br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>Im<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|30-10-2020|30-10-2020|01_de_12<br>T|01_de_12<br>T|01_de_12<br>T|abloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_MP10 P98 Diario_1 de 12_Lam.mxd

**330000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
||||**M**|")<br>")<br>!P<br>**")**#<br>**ejillones**||||||||
|||||||||||||
|||||||||||||
|||||||||||||
||||**Comuna de**<br>**Mejillones**|||||||||
||||**Comuna de**<br>**Mejillones**|||||||||
|||||||||||||
|||||**Comuna de**<br>**Antofagasta**|_Ferrocarriles_|_Compañia de_<br>_Bomberos_||SRC_1<br>SRC_2|**")**<br>#<br> (CTA)<br> (CTH)<br>PMC 1|||
||||||")<br>")<br><br>|")<br>")<br><br>||||||
|||||||||||||
|||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**349500**

**349500**

**362500**

**362500**

**369000**

**375500**

**382000**

**356000**

**356000**

**382000**

**369000**

**375500**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información<br>a Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br>Año de Consulta 2020|Col5|Col6|OPERACIÓN UNIDADES<br>CTA/CTH CON 100%<br>DE BIOMASA|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**|**FECHA**|**LÁMINA**<br>**F**|**LÁMINA**<br>**F**|**LÁMINA**<br>**F**|**ORMATO**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecció<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|02_de_12<br>Ta|02_de_12<br>Ta|02_de_12<br>Ta|bloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_MP10 Anual_2 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||")<br>")<br>!P<br>**Mejillones**|")<br>")<br>!P<br>**Mejillones**|**")**#|**")**#|||||||||
|||||||||||||||||
|||||||||||||||||
||||**Comuna de**<br>**Mejillones**|||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||PMC 1||
|||||**Comuna de**<br>**Antofagasta**|**Comuna de**<br>**Antofagasta**||")<br>_Ferrocar_|")<br>_riles_<br>_Compañia de_<br>_Bomberos_|")<br>_riles_<br>_Compañia de_<br>_Bomberos_||~~SR~~<br>SR|~~SR~~<br>SR|~~SR~~<br>SR|**")**<br>~~#~~<br>~~C_1 (CTA)~~<br>C_2 (CTH)||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||

**362500**

**369000**

**375500**

**382000**

**356000**

|30000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|Col9|382000|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**<br>|**Fuente de información**<br>|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|**Escala gráfica y nominal**<br><br><br><br><br>|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>**F**<br><br>|**LÁMINA**<br>**F**<br><br>|**LÁMINA**<br>**F**<br><br>|**ORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|03_de_12<br>Ta|03_de_12<br>Ta|03_de_12<br>Ta|bloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_MP2,5 P98 Diario_3 de 12_Lam.mxd

**330000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||**M**|")<br>")<br>!P<br>**")**#<br>**ejillones**|||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||||
||||||||||SRC_1 (CT<br>~~RC_2 (CT~~|**")**<br>#<br>A)<br>~~H)~~<br>PMC 1|**")**<br>#<br>A)<br>~~H)~~<br>PMC 1|||
||||||||||SRC_1 (CT<br>~~RC_2 (CT~~|**")**<br>#<br>A)<br>~~H)~~<br>PMC 1||||
||||||**Comun**<br>**Antofa**|")<br>")<br>_Ferrocarriles_<br>_Compañia de_<br>_Bomberos_<br>**a de**<br>**gasta**|")<br>")<br>_Ferrocarriles_<br>_Compañia de_<br>_Bomberos_<br>**a de**<br>**gasta**|||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**349500**

**349500**

**362500**

**362500**

**369000**

**375500**

**356000**

**356000**

**382000**

**382000**

**375500**

**369000**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información|Col5|Col6|OPERACIÓN UNIDADES<br>CTA/CTH CON 100%<br>DE BIOMASA<br>C|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>telital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>telital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>telital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>telital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>telital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>telital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>telital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>telital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|ONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|**Escala gráfica y nominal**|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>e Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>e Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>e Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>e Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**0**<br>Proyecció<br>Equidista<br>Sistema d<br>Cartografía<br>Fuente de<br>Imagen Sa<br>|n Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>e Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|04_de_12|04_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_MP2,5 Anual_4 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
|||||**M**|")<br>")<br>!P<br>**")**<br>#<br>**ejillones**||||||||
|||||||**S**|**S**||||||
||||||**Comuna de**<br>**MEJILLONE**|**Comuna de**<br>**MEJILLONE**|**Comuna de**<br>**MEJILLONE**|**Comuna de**<br>**MEJILLONE**|**Comuna de**<br>**MEJILLONE**|**Comuna de**<br>**MEJILLONE**|**Comuna de**<br>**MEJILLONE**|**Comuna de**<br>**MEJILLONE**|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||~~RC_1 (CTA)~~||
||||||||||||||
||||||||")<br>_Ferrocarriles_|")<br>_Compañia de_<br>_Bomberos_|||**")**<br># PMC 2<br><br>SRC_2 (CTH)||
||||||||||||||
||||||||||||||

**362500**

**369000**

**382000**

**356000**

**375500**

|30000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|382000|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**<br><br>|**Ubicación Nacional**|**Ubicación Local**|**Fuente de información**<br>|||**OPERACIÓN UNIDADE**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADE**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|CONSULTORA<br>**S**|CONSULTORA<br>**S**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**Escala gráfica y nominal**<br><br><br><br><br>|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|05_de_12|05_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_NO2 P99 horario_5 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||**M**|")<br>")<br>!P<br>**ejillones**|**")**#|**")**#|||||||
|||||||||||||||
|||||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
||||||**Comuna de**<br>**Antofagasta**|||_Compañia de_<br>~~_Bomberos_~~|_Compañia de_<br>~~_Bomberos_~~|SRC_1 (C<br>SRC_2 (C|SRC_1 (C<br>SRC_2 (C|**")**<br>#<br>TA)<br>TH)<br>PMC 1||
||||||||")<br>~~_Ferroc_~~|")<br>~~_rriles_~~<br>||||||
|||||||||||||||
|||||||||||||||

**362500**

**375500**

**382000**

**356000**

**369000**

|330000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|Col9|382000|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**<br>|**Fuente de información**<br><br><br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|I<br>|I<br>|I<br>|I<br>|I<br>|I<br>|I<br>|I<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|I<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|EMA<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|06_de_12|06_de_12|06_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_NO2 Anual_6 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||")<br>!P<br>**Mejillones**|")<br>**")**<br>#|||||||
|||||||||||||
|||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||**C**<br>**A**|**omuna de**<br>**ntofagasta**|||_Ferrocarriles_<br>_Compañia de_<br>_Bomberos_||**")**<br>#PMC 2<br>SRC_1 (CTA)<br>SRC_2 (CTH)||
|||||||||")<br>~~")~~||||
|||||||||||||
|||||||||||||

**362500**

**369000**

**382000**

**356000**

**375500**

|30000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación L|356000 362500 Fuente de información Local|369000|Col6|375500|Col8|382000|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación**|**Fuente de información**<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**ocal**<br>**1:200.000**<br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||||||||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||CONTENIDO<br>Isoconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||C2-2|30-10-2020|30-10-2020|07_de_12|07_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_SO2 P98,5 Horario_7 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|2|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
||||")<br><br>!P<br>**Mejillones**|")<br>**")**<br>#||||||
|||||||||||
||||**Comuna de**<br>**Mejillones**|||||||
|||||||||||
|||||||||||
|||||||||SRC_1 (CTA)||
||||**C**<br>**A**|**omuna de**<br>**ntofagasta**|")<br>")<br>_Ferrocarriles_<br>_Compañ_<br>_Bombe_|_ia de_<br>_ros_|_ia de_<br>_ros_|~~**")**~~<br>#PMC 2<br><br>~~SRC_2 (CTH)~~||
|||||||||||
|||||||||||
|||||||||||

**362500**

**369000**

**382000**

**356000**

**375500**

|0000 336500 Leyenda|343000 Ubicación Naciona|349500 Ubicación L al|356000 362500 Fuente de información Local|369000|Col6|375500|Col8|382000|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacion**|**Ubicación**<br>**l**|**Fuente de información**<br>CON<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>TEM<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**ocal**<br>**1:200.000**<br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020<br>**El**<br>**R**<br>**A**|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|CONSULTORA<br>|CONSULTORA<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|A<br>Calidad del Aire - Caso Actual|A<br>Calidad del Aire - Caso Actual|A<br>Calidad del Aire - Caso Actual|A<br>Calidad del Aire - Caso Actual|A<br>Calidad del Aire - Caso Actual|A<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|TENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|TENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|TENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|TENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|TENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|TENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**aborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**evisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**probado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|**ANEXO**|**FECHA**|**FECHA**|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>40 ug/m3<br>50 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerd**<br>** Limítro**<br>** Año 19**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|**o**<br>**fe**<br>**98**|**o**<br>**fe**<br>**98**|C2-2|30-10-2020|30-10-2020|08_de_12|08_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_SO2 P99,73 Horario_8 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
||||||")<br>")<br>!P<br>**Mejillones**|**")**#|**")**#|||||||
|||||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
||||||**Comuna de**<br>**Antofagasta**||")<br>_Ferrocarriles_|")<br>_Compañia d_<br>_Bomberos_|S<br>S<br>_e_|S<br>S<br>_e_|**")**<br>#<br>RC_1 (CTA)<br>RC_2 (CTH)<br>PMC 1|||
|||||||||||||||
|||||||||||||||

**362500**

**375500**

**382000**

**356000**

**369000**

|30000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|Col9|382000|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**<br>|**Fuente de información**<br>|TITULAR<br><br>ultores<br>ultores<br>RI|TITULAR<br><br>ultores<br>ultores<br>RI|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|artografía Elaborada: Jaime Illanes y Asociados Cons<br>uente de Información: Jaime Illanes y Asociados Cons<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ES<br> Año de Consulta 2020|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|**Escala gráfica y nominal**<br><br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br>**km.**<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br>**km.**<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br>**km.**<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br>**km.**<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br>**km.**<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br>**km.**<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br>TEMA<br>Calidad del Aire - Caso Actual<br>**km.**<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br><br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br><br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br><br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br><br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br><br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br><br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br><br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br><br>**1:200.000**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|30-10-2020|30-10-2020|09_de_12|09_de_12|09_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_SO2 P99 diario_9 de 12_Lam.mxd

**330000**

|2|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
||||")<br>")<br>!P<br>**")**#<br>**Mejillones**|||||
|||||||||
||||**Comuna de**<br>**Mejillones**|||||
|||||||||
|||||||||
|||||||#<br>~~SRC_1 (CTA)~~<br><br>PMC 1||
||||**Comuna de**<br>**Antofagasta**|")<br>")<br>_Ferrocarriles_<br>_Compañia de_<br>_Bomberos_||**")**<br><br>SRC_2 (CTH)||
|||||||||
|||||||||
|||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**349500**

**349500**

**362500**

**362500**

**369000**

**375500**

**382000**

**356000**

**356000**

**369000**

**375500**

**382000**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información<br>fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br>Año de Consulta 2020|OPE<br>CT<br>TITULAR|Col6|RACIÓN UNIDADES<br>A/CTH CON 100%<br>DE BIOMASA|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|CO<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>TE<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**<br>|MA<br>Calidad del Aire - Caso Actual|MA<br>Calidad del Aire - Caso Actual|MA<br>Calidad del Aire - Caso Actual|MA<br>Calidad del Aire - Caso Actual|MA<br>Calidad del Aire - Caso Actual|MA<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|CO<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>TE<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**<br>|NTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|NTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|NTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|NTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|NTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|NTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|ión Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br> de Referencia Geodésico Datum WGS84<br><br><br>|**laborado por:**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|ión Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br> de Referencia Geodésico Datum WGS84<br><br><br>|**Revisado por:**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|ión Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br> de Referencia Geodésico Datum WGS84<br><br><br>|**probado por:**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|ión Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br> de Referencia Geodésico Datum WGS84<br><br><br>|**ANEXO**|**FECHA**<br>|**LÁMINA**<br>**FOR**<br><br><br>|**LÁMINA**<br>**FOR**<br><br><br>|**LÁMINA**<br>**FOR**<br><br><br>|**MATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3<br>50 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecc<br>Equidist<br>Sistema<br>Cartogra<br>Fuente d<br>Imagen S<br>|ión Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br> de Referencia Geodésico Datum WGS84<br><br><br>|C2-2|30-10-202|10_de_12<br>Tabl<br>0|10_de_12<br>Tabl<br>0|10_de_12<br>Tabl<br>0|oide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_SO2 P99,7 diario_10 de 12_Lam.mxd

**330000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
|||||**M**|")<br>")<br>!P<br>**")**#<br>**ejillones**||||||||||
|||||**Comuna de**<br>**Mejillones**|||||||||||
|||||**Comuna de**<br>**Mejillones**|||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||**Comuna de**<br>**Antofagasta**||")<br>_Ferrocar_|")<br>_riles_<br>_Compañia de_<br>_Bomberos_||SRC_<br>SRC_|SRC_<br>SRC_|1 (CT<br>2 (CT|**")**<br>#<br>A)<br>H)<br>PMC 1||
||||||||||||||||
||||||||||||||||
||||||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**349500**

**349500**

**362500**

**362500**

**375500**

**382000**

**382000**

**356000**

**356000**

**369000**

**369000**

**375500**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información|TITULAR|Col6|OPERACIÓN UNIDADES<br>CTA/CTH CON 100%<br>DE BIOMASA<br>C|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|fía Elaborada: Jaime Illanes y Asociados Consultores<br>e Información: Jaime Illanes y Asociados Consultores<br>Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|ONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|**Escala gráfica y nominal**<br><br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br>TEMA<br>Calidad del Aire - Caso Actual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|ción Cartográfica UTM Huso 19 Sur<br>tancia Grilla UTM cada 6500 metros<br>a de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**PR**<br>|**PR**<br>|**Cargo**<br>|**:**<br><br>**Cartógrafo**<br>|**:**<br><br>**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|ción Cartográfica UTM Huso 19 Sur<br>tancia Grilla UTM cada 6500 metros<br>a de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**FO**<br>|**FO**<br>|**Cargo**<br>|**:**<br><br><br>**Ingeniero Civil Geografía**|**:**<br><br><br>**Ingeniero Civil Geografía**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|ción Cartográfica UTM Huso 19 Sur<br>tancia Grilla UTM cada 6500 metros<br>a de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**CP**|**CP**|**Cargo**|**:**<br>**Jefe de Proyecto**|**:**<br>**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|ción Cartográfica UTM Huso 19 Sur<br>tancia Grilla UTM cada 6500 metros<br>a de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|**FECHA**|**FECHA**|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>3 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyec<br>Equidis<br>Sistem<br>Cartogra<br>Fuente d<br>Imagen<br>|ción Cartográfica UTM Huso 19 Sur<br>tancia Grilla UTM cada 6500 metros<br>a de Referencia Geodésico Datum WGS84|**ANEXO**<br>C2-2<br>**Elaborado por:**<br>**Revisado por:**<br>**Aprobado por:**|30-10-2020|30-10-2020|11_de_12|11_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_SO2 Anual_11 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||**Me**|")<br>")<br>!P<br>**")**#<br>#<br>**jillones**|||||||||
|||||||||||||||
||||||**Comuna**<br>**MEJILLO**|**Comuna**<br>**MEJILLO**|**Comuna**<br>**MEJILLO**|**Comuna**<br>**MEJILLO**|**Comuna**<br>**MEJILLO**|**Comuna**<br>**MEJILLO**|**Comuna**<br>**MEJILLO**|**Comuna**<br>**MEJILLO**|**Comuna**<br>**MEJILLO**|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||_Ferrocarri_|_les_<br>_Compañia de_<br>_Bomberos_|SRC_1 (<br>SRC_2 (|**")**<br>#<br># PMC 2<br>PMC 1<br>CTA)<br>CTH)|||
|||||||||")|!P<br>")|||||
|||||||||||||||
|||||||||||||||

**362500**

**369000**

**375500**

**356000**

**382000**

|330000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|Col9|38200|
|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**|**Fuente de información**<br><br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||||||||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|TEMA<br>Calidad del Aire - Caso Actual|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|12_de_12|12_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Caso Base\CA_PMC y Dominio de Modelaciónl_12 de 12_Lam.mxd

**330000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
||||||**")**<br>#|**")**<br>#||||||
|||||")<br>")<br>!P<br><br><br>**Mejillones**|")<br>")<br>!P<br><br><br>**Mejillones**|")<br>")<br>!P<br><br><br>**Mejillones**|")<br>")<br>!P<br><br><br>**Mejillones**|")<br>")<br>!P<br><br><br>**Mejillones**|")<br>")<br>!P<br><br><br>**Mejillones**|")<br>")<br>!P<br><br><br>**Mejillones**|")<br>")<br>!P<br><br><br>**Mejillones**|
|||||||||||||
|||||||||||||
||||**Comuna de**<br>**Mejillones**|||||||||
|||||||||||||
|||||||||||||
|||||||||S<br>S|**")**<br>RC_1 (CTA)<br>RC_2 (CTH)|||
|||||**Comuna de**<br>**Antofagasta**||")<br>_Ferro_|")<br>_Compañia_<br>_de Bomberos_<br>_carriles_||#<br>PMC 2|||
|||||||||||||
|||||||||||||
|||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**356000**

**356000**

**362500**

**362500**

**369000**

**382000**

**382000**

**349500**

**349500**

**375500**

**375500**

**369000**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información<br>grafía Elaborada: Jaime Illanes y Asociados Consultores<br>e de Información: Jaime Illanes y Asociados Consultores<br>n Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br>Año de Consulta 2020|Col5|OPERACIÓN UNIDADES<br>CTA/CTH CON 100%<br>DE BIOMASA|Col7|Col8|
|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|TEMA<br>Calidad del Aire - Fase de Operación|TEMA<br>Calidad del Aire - Fase de Operación|TEMA<br>Calidad del Aire - Fase de Operación|TEMA<br>Calidad del Aire - Fase de Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP10 Percentil 98 Diario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**Cargo:**<br><br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**Cargo:**<br><br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**Cargo:**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>** Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|01_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_MP10 P98 Diario_1 de 12_Lam.mxd

**330000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||**M**|")<br>")<br>!P<br>**")**#<br>**ejillones**|||||||
||||||||||||
||||||||||||
||||**Comuna de**<br>**Mejillones**||||||||
||||||||||||
||||||||||||
||||||||||||
|||||**Comuna de**<br>**Antofagasta**|")<br>_Ferroca_|")<br>_rriles_<br>_Compañia de_<br>_Bomberos_|SRC<br>SRC|**")**<br>#<br>_1 (CTA)<br>_2 (CTH)<br>PMC 1|||
||||||||||||
||||||||||||
||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**349500**

**349500**

**362500**

**362500**

**369000**

**369000**

**375500**

**375500**

**356000**

**356000**

**382000**

**382000**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información<br>ía Elaborada: Jaime Illanes y Asociados Consultores<br>Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br>Año de Consulta 2020|Col5|Col6|OPERACIÓN UNIDADES<br>CTA/CTH CON 100%<br>DE BIOMASA|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de MP10 Anual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**ANEXO**<br>|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Área de Proyecto<br>Dominio Modelación<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP10 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidist<br>Sistema<br>Cartograf<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ancia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|02_de_12|02_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_MP10 Anual_2 de 12_Lam.mxd

**330000**

|2|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||
||||||||||||
||||||||||||
||||||||||||
||||")<br>")<br>!P<br><br><br>**Mejillones**|**")**<br>#|**")**<br>#||||||
||||||||||||
||||||||||||
|||**Comuna de**<br>**Mejillones**|||||||||
||||||||||||
||||||||||||
||||||||||||
||||**Comuna de**<br>**Antofagasta**||")<br>_Fer_|")<br>_rocarriles_<br>_Compañia de_<br>_Bomberos_|SRC_<br>SRC_|**")**<br>#<br>1 (CTA)<br>2 (CTH)<br>PMC 2|||
||||||||||||
||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**356000**

**356000**

**362500**

**362500**

**369000**

**382000**

**382000**

**349500**

**349500**

**369000**

**375500**

**375500**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información<br>ografía Elaborada: Jaime Illanes y Asociados Consultores<br>te de Información: Jaime Illanes y Asociados Consultores<br>en Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br>Año de Consulta 2020|Col5|OPERACIÓN UNI<br>CTA/CTH CON<br>DE BIOMAS|DADES<br>100%<br>A<br>CONSULTORA|Col8|
|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br><br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br><br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Percentil 98 Diario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|yección Cartográfica UTM Huso 19 Sur<br>idistancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br><br>**C**<br>|**argo:**<br><br>**Cartógrafo**<br>|**argo:**<br><br>**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|yección Cartográfica UTM Huso 19 Sur<br>idistancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br><br>**C**<br>|**argo:**<br><br>**Ingeniero Civil Geografia**<br>|**argo:**<br><br>**Ingeniero Civil Geografia**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|yección Cartográfica UTM Huso 19 Sur<br>idistancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**<br>**C**|**argo:**<br>**Jefe de Proyecto**|**argo:**<br>**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|yección Cartográfica UTM Huso 19 Sur<br>idistancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br><br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 P98 Diario**<br>1 ug/m3<br>2 ug/m3<br>5 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Pro<br>Equ<br>Sist<br>Cart<br>Fuen<br>Imag<br>|yección Cartográfica UTM Huso 19 Sur<br>idistancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|C2-2|0<br>30-10-2020|3_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_MP2,5 P98 Diario_3 de 12_Lam.mxd

**330000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
|||||**M**|")<br>")<br>!P<br>**")**#<br>**ejillones**|||||||
|||||||||||||
|||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||
|||||||||||||
|||||||||||||
|||||||||||||
||||||**Comuna de**<br>**Antofagasta**|_Ferroc_|_arriles_<br>_Compañia de_<br>_Bomberos_|SR<br>SRC|**")**<br>#<br>C_1 (CTA)<br>_2 (CTH)<br>PMC 1|||
|||||||")|~~")~~|||||
|||||||||||||
|||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**349500**

**349500**

**362500**

**362500**

**369000**

**375500**

**382000**

**356000**

**356000**

**375500**

**382000**

**369000**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información|Col5|Col6|OPERACIÓN UNIDADE<br>CTA/CTH CON 100%<br>DE BIOMASA|Col8|S<br>CONSULTORA|Col10|
|---|---|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|a Elaborada: Jaime Illanes y Asociados Consultores<br> Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|a Elaborada: Jaime Illanes y Asociados Consultores<br> Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|a Elaborada: Jaime Illanes y Asociados Consultores<br> Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|a Elaborada: Jaime Illanes y Asociados Consultores<br> Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|a Elaborada: Jaime Illanes y Asociados Consultores<br> Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|a Elaborada: Jaime Illanes y Asociados Consultores<br> Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|a Elaborada: Jaime Illanes y Asociados Consultores<br> Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|a Elaborada: Jaime Illanes y Asociados Consultores<br> Información: Jaime Illanes y Asociados Consultores<br>atelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|**Escala gráfica y nominal**<br><br><br><br><br>|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de MP2,5 Anual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|**Datos Cartográficos y Geodésicos**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografia**<br>|**Ingeniero Civil Geografia**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**MP2,5 Promedio Anual**<br>0,2 ug/m3<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proyecci<br>Equidista<br>Sistema<br>Cartografí<br>Fuente de<br>Imagen S<br>|ón Cartográfica UTM Huso 19 Sur<br>ncia Grilla UTM cada 6500 metros<br>de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|04_de_12|04_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_MP2,5 Anual_4 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||")<br>**Me**|")<br>!P<br>**")**<br>#<br>**jillones**|||||||||
|||||||||||||||
|||||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||||
|||||||||||||||
|||||||||||||||
||||||||||SRC_1<br>~~SRC_2~~|**")**<br>(CTA)<br>~~(CTH)~~||||
||||||**Comuna de**<br>**Antofagasta**||")<br>_Ferrocar_|")<br>_riles_<br>_Compañia de_<br>_Bomberos_||#<br><br>PMC 2||||
|||||||||||||||
|||||||||||||||
|||||||||||||||

**362500**

**369000**

**382000**

**356000**

**375500**

|330000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|Col9|38200|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**|**Fuente de información**<br><br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br><br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**1:200.000**<br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||||||||||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|CONTENIDO<br>Isoconcentraciones de NO2 Percentil 99 horario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 P99 horario**<br>40 ug/m3<br>60 ug/m3<br>100 ug/m3<br>200 ug/m3<br>500 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||C2-2|30-10-2020|30-10-2020|05_de_12|05_de_12|05_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_NO2 P99 horario_5 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||**M**|")<br>")<br>!P<br>**ejillones**|**")**#||||||||
|||||||||||||||
|||||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
||||||**Comuna d**<br>**Antofagas**|**e**<br>**ta**|**e**<br>**ta**|")<br>_Ferro_|")<br>_carriles_<br>_Compañia de_<br>_Bomberos_|SRC_<br>SRC_|**")**<br>#<br>1 (CTA)<br>2 (CTH)<br>PMC 1|**")**<br>#<br>1 (CTA)<br>2 (CTH)<br>PMC 1||
|||||||||||||||
|||||||||||||||
|||||||||||||||

**362500**

**369000**

**375500**

**382000**

**356000**

|330000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|Col9|382000|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**<br>|**Fuente de información**<br><br><br>artografía Elaborada: Jaime Illanes y Asociados Consultores<br>uente de Información: Jaime Illanes y Asociados Consultores<br>magen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|C<br>F<br>I<br>|C<br>F<br>I<br>|C<br>F<br>I<br>|C<br>F<br>I<br>|C<br>F<br>I<br>|C<br>F<br>I<br>|C<br>F<br>I<br>|C<br>F<br>I<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|C<br>F<br>I<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de NO2 Promedio Anual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Elaborado por**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br><br>|**LÁMINA**<br><br>|**LÁMINA**<br><br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**NO2 Promedio Anual**<br>2 ug/m3<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|C<br>F<br>I<br>|Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|06_de_12<br>|06_de_12<br>|06_de_12<br>|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_NO2 Anual_6 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
|||||**M**|")<br>")<br>!P<br>**")**<br>#<br>**ejillones**||||||||
||||||||||||||
||||||||||||||
|||||**Comuna de**<br>**Mejillones**|||||||||
||||||||||||||
||||||||||||||
|||||||||||~~SRC_1 (CT~~|~~A)~~||
||||||**Comuna de**<br>**Antofagasta**|||")<br>_Ferroc_|")<br>_arriles_<br>_Compañia_<br>_Bombero_|SRC_2 (CT<br>_de_<br>_s_|**")**<br>#<br><br>H)<br>PMC 2||
||||||||||||||
||||||||||||||

**362500**

**369000**

**375500**

**382000**

**356000**

|330000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000 375500|Col6|Col7|382000|Col9|
|---|---|---|---|---|---|---|---|---|
|**Leyenda**<br><br>|**Ubicación Nacional**|**Ubicación Local**|**Fuente de información**<br>T<br><br><br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|ITULAR<br>**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|ITULAR<br>**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|ITULAR<br>**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||||||||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||||||CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||CONTENI<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>I<br>TEMA<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**<br>|Calidad del Aire - Fase Operación|Calidad del Aire - Fase Operación|Calidad del Aire - Fase Operación|Calidad del Aire - Fase Operación|Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||CONTENI<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>I<br>TEMA<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**<br>|DO<br>soconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|DO<br>soconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|DO<br>soconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|DO<br>soconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|DO<br>soconcentraciones de SO2 Percentil 98,5 Horario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**ANE**<br><br>C2<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**Elabora**<br>**Revisad**<br>**Aproba**|**do por:**<br><br>**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**ANE**<br><br>C2<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**Elabora**<br>**Revisad**<br>**Aproba**|**o por:**<br><br>**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**ANE**<br><br>C2<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**Elabora**<br>**Revisad**<br>**Aproba**|**o por:**<br>**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**ANE**<br><br>C2<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**Elabora**<br>**Revisad**<br>**Aproba**|**XO**<br>**FECHA**<br><br>|**LÁMINA**<br>|**LÁMINA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P98,5 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**ANE**<br><br>C2<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**Elabora**<br>**Revisad**<br>**Aproba**|-2<br>30-10-2020|07_de_12|07_de_12|07_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_SO2 P98,5 Horario_7 de 12_Lam.mxd

**330000**

**336500**

**343000**

**356000**

**362500**

**369000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||
|||||||||||||
|||||||||||||
|||||||||||||
||||||")<br>")<br>!P<br>**")**<br>#<br>**Mejillones**|||||||
|||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||
|||||||||||||
|||||||||||||
||||||||||~~SRC_1 (CTA)~~|||
||||||**Comuna de**<br>**Antofagasta**|")<br>_Fer_|")<br>_rocarriles_<br>_Compañia de_<br>_Bomberos_||**")**<br>#<br><br>SRC_2 (CTH)<br>PMC 2|||
|||||||||||||
|||||||||||||
|||||||||||||

**382000**

**349500**

**375500**

|30000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|Col9|382000|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**|**Fuente de información**<br>C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84<br>**1:200.000**<br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||||||||||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||TITULAR|TITULAR|TITULAR|TITULAR|TITULAR|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99,73 Horario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br><br><br>|**LÁMINA**<br><br><br>|**LÁMINA**<br><br><br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,73 Horario**<br>5 ug/m3<br>10 ug/m3<br>20 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||C2-2|30-10-2020|30-10-2020|08_de_12<br>T|08_de_12<br>T|08_de_12<br>T|abloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_SO2 P99,73 Horario_8 de 12_Lam.mxd

**330000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||")<br><br>!P<br>**Mejillones**|")|**")**<br>#|**")**<br>#|||||||
|||||||||||||||
|||||||||||||||
|||||**Comuna de**<br>**Mejillones**||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
||||||**Comuna de**<br>**Antofagasta**||")<br>_Ferroc_|")<br>_arriles_<br>_Compañia de_<br>_Bomberos_|")<br>_arriles_<br>_Compañia de_<br>_Bomberos_||SRC_1<br>SRC_2|**")**<br>#<br>(CTA)<br>(CTH)<br>PMC 2||
|||||||||||||||
|||||||||||||||
|||||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**349500**

**349500**

**362500**

**362500**

**369000**

**382000**

**382000**

**356000**

**356000**

**369000**

**375500**

**375500**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información<br>grafía Elaborada: Jaime Illanes y Asociados Consultores<br>te de Información: Jaime Illanes y Asociados Consultores<br>en Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br>Año de Consulta 2020|OPE<br>CT<br>TITULAR|Col6|RACIÓN UNIDADES<br>A/CTH CON 100%<br>DE BIOMASA|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br>|**LÁMINA**<br>**FORMA**<br><br><br>|**LÁMINA**<br>**FORMA**<br><br><br>|**LÁMINA**<br>**FORMA**<br><br><br>|**TO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Sist<br>Carto<br>Fuen<br>Imag<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ema de Referencia Geodésico Datum WGS84|C2-2|30-10-202|09_de_12<br>Tablo<br>0|09_de_12<br>Tablo<br>0|09_de_12<br>Tablo<br>0|de|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_SO2 P99 diario_9 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
|||||")<br><br>**Mejillone**|")<br>!P<br>**s**|")<br>!P<br>**s**|**")**<br>#||||||||
||||||||||||||||
||||||||||||||||
|||||**Comuna de**<br>**Mejillones**|||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||**Comuna de**<br>**Antofagasta**|**Comuna de**<br>**Antofagasta**|")<br>_F_|")<br>_errocarriles_<br>_Compañia de_<br>_Bomberos_||~~SRC_1~~<br>SRC_2|**")**<br>#<br>~~ (CTA)~~<br> (CTH)<br>PMC 2||||
||||||||||||||||
||||||||||||||||

**362500**

**369000**

**382000**

**356000**

**375500**

|330000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|38200|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**<br>|**Fuente de información**<br><br><br>grafía Elaborada: Jaime Illanes y Asociados Consultores<br>e de Información: Jaime Illanes y Asociados Consultores<br>n Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|TITULAR<br><br>**OPER**<br>**CTA**<br>|TITULAR<br><br>**OPER**<br>**CTA**<br>|**ACIÓN UNIDADES**<br>**/CTH CON 100%**<br>**DE BIOMASA**|**ACIÓN UNIDADES**<br>**/CTH CON 100%**<br>**DE BIOMASA**|||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|CONSULTORA|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**<br>|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**<br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Percentil 99 Diario<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84<br><br><br>|**Elaborado por:**<br>|**PR**<br>|**Cargo:**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84<br><br><br>|**Revisado por:**<br>|**FO**<br>|**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84<br><br><br>|**Aprobado por:**|**CP**|**Cargo:**|**Jefe de Proyecto**|**Jefe de Proyecto**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84<br><br><br>|**ANEXO**|**FECHA**<br>|**LÁMINA**<br>**F**<br><br><br>|**LÁMINA**<br>**F**<br><br><br>|**LÁMINA**<br>**F**<br><br><br>|**RMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 P99,7 Diario**<br>0,5 ug/m3<br>1 ug/m3<br>2 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|Proy<br>Equi<br>Siste<br>Carto<br>Fuent<br>Image<br>|ección Cartográfica UTM Huso 19 Sur<br>distancia Grilla UTM cada 6500 metros<br>ma de Referencia Geodésico Datum WGS84<br><br><br>|C2-2|30-10-2020|10_de_12<br>Ta<br>|10_de_12<br>Ta<br>|10_de_12<br>Ta<br>|bloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_SO2 P99,7 diario_10 de 12_Lam.mxd

**330000**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
|||||")<br>**Me**|")<br>!P<br>**")**#<br>**jillones**|")<br>!P<br>**")**#<br>**jillones**|||||||
||||||||||||||
||||||||||||||
|||||**Comuna de**<br>**Mejillones**|||||||||
||||||||||||~~CTA)~~||
|||||||||||~~SRC_1~~|~~SRC_1~~|~~SRC_1~~|
|||||||||||SRC_2|(CTH)<br>~~PMC 1~~||
||||||**Comuna de**<br>**Antofagasta**|**Comuna de**<br>**Antofagasta**||")<br>_Ferrocarr_|")<br>_iles_<br>_Compañia de_<br>_Bomberos_|SRC_1 (CT<br>SRC_2 (CT|**")**<br>#<br>A)<br>H)<br>||
||||||||||||||
||||||||||||||
||||||||||||||

**330000**

**336500**

**336500**

**343000**

**343000**

**349500**

**349500**

**362500**

**362500**

**369000**

**375500**

**382000**

**382000**

**356000**

**356000**

**375500**

**369000**

|Leyenda|Ubicación Nacional|Ubicación Local|Fuente de información<br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br>Año de Consulta 2020|Col5|Col6|OPERACIÓN UNIDAD<br>CTA/CTH CON 100<br>DE BIOMASA|ES<br>%<br>CONSULTORA|
|---|---|---|---|---|---|---|---|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||||||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|EMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||C<br>**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>T<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|ONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br><br><br><br>|ONTENIDO<br>Isoconcentraciones de SO2 Promedio Anual<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br><br>**Cargo:**<br>|**PR**<br><br>**Cargo:**<br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br><br>**Cargo:**<br>|**FO**<br><br>**Cargo:**<br>|**Ingeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**<br>**Cargo:**|**CP**<br>**Cargo:**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**<br>|**FECHA**<br>**LÁM**<br><br>|**FECHA**<br>**LÁM**<br><br>|**INA**<br>**FORMATO**<br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal<br>**Isoconcentraciones**<br>**SO2 Promedio Anual**<br>0,3 ug/m3<br>0,5 ug/m3<br>1 ug/m3|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|C2-2|11_de<br>30-10-2020|11_de<br>30-10-2020|_12<br>Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_SO2 Anual_11 de 12_Lam.mxd

**330000**

**336500**

**343000**

**349500**

|Col1|2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||||
|||||**M**|")<br>")<br>!P<br>**")**#<br>#<br>**ejillones**||||||||
|||||**Comuna de**<br>**Mejillones**|||||||||
|||||**Comuna de**<br>**Mejillones**|||||||||
||||||||||||||
||||||||||||||
||||||||||||||
||||||||||||PMC 1||
||||||||||||||
||||||**Comuna de**<br>**Antofagasta**|||")<br>_Ferr_|!P<br>")<br>_ocarriles_<br>_Compañia de_<br>_Bomberos_|SRC_1<br>SRC_|**")**<br>~~#~~<br>#<br>PMC 2<br> (CTA)<br>2 (CTH)||
||||||||||||||
||||||||||||||
||||||||||||||

**362500**

**369000**

**375500**

**382000**

**356000**

|30000 336500 Leyenda|343000 Ubicación Nacional|349500 Ubicación Local|356000 362500 Fuente de información|369000|Col6|375500|Col8|382000|
|---|---|---|---|---|---|---|---|---|
|**Leyenda**|**Ubicación Nacional**|**Ubicación Local**<br>|**Fuente de información**<br><br>Cartografía Elaborada: Jaime Illanes y Asociados Consultores<br>Fuente de Información: Jaime Illanes y Asociados Consultores<br>Imagen Satelital; Imagen Geoeyes IKONOS 1 Para ESRI<br> Año de Consulta 2020|||**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**|**OPERACIÓN UNIDADES**<br>**CTA/CTH CON 100%**<br>**DE BIOMASA**||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||||||||
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**|||TITULAR<br>|TITULAR<br>|TITULAR<br>|TITULAR<br>|CONSULTORA|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|TEMA<br>Calidad del Aire - Fase Operación|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||**Datos Cartográficos y Geodésicos**<br>**Escala gráfica y nominal**<br>**0**<br>**2**<br>**4**<br>**6**<br>**8**<br>**km.**<br>**1:200.000**|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|CONTENIDO<br>Puntos de Máxima Concentración<br><br><br><br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Elaborado por:**<br>|**PR**<br>|**PR**<br>|**Cargo:**<br><br>|**Cartógrafo**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Revisado por:**<br>|**FO**<br>|**FO**<br>|**Cargo:**<br><br>|**ngeniero Civil Geografía**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**Aprobado por:**|**CP**|**CP**|**Cargo:**|**Jefe de Proyecto**|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|**ANEXO**|**FECHA**<br>|**FECHA**<br>|**LÁMINA**<br>|**FORMATO**<br>|
|#<br>Punto Máxima<br>Concentración<br>")<br>Fuente de Emisión<br>")<br>Receptores<br>Dominio Modelación<br>Área de Proyecto<br>**División Político**<br>**Administrativo**<br>Costa<br>Comunal|*** ; Acuerdo**<br>** Limítrofe**<br>** Año 1998**<br>k<br>**CHILE**<br>**Región**<br>**Antofagasta**<br>**Territorio**<br>**Antártico**<br>**Chileno**||Proyección Cartográfica UTM Huso 19 Sur<br>Equidistancia Grilla UTM cada 6500 metros<br>Sistema de Referencia Geodésico Datum WGS84|C2-2|30-10-2020|30-10-2020|12_de_12|Tabloide|

S:\3-ESTRUCTURA CARPETAS_GEODATABASE\100 - E - CL (Edelnor)\100-113 DIA Reemplazo carbon por uso de Pellet de Biomasa CTA y CTH\Resultados\mxd\LdB\CA\Isoconcentraciones\Fase Operación\CA_PMC y Dominio de Modelaciónl_12 de 12_Lam.mxd