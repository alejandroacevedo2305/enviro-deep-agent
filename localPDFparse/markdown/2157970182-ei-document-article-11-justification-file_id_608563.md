---
title: Microsoft Word - Anexo C2-1 Modelación Calidad del Aire.docx
author: Desconocido
date: D:20221230114026Z00'00'
language: es
type: report
pages: 58
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO C2-1
-->

# ANEXO C2-1

## MODELACIÓN DE CALIDAD DEL AIRE

### _Cliente:_

**ÍNDICE**

1. INTRODUCCIÓN ........................................................................................................................................ 1

2. OBJETIVO ..................................................................................................................................................... 2

3. MARCO LEGAL ........................................................................................................................................... 2

4. METODOLOGÍA ......................................................................................................................................... 4

4.1. BASE TEÓRICA DEL MODELO UTILIZADO ................................................................................ 4

4.2. CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN ....................................................... 5

4.3. ANÁLISIS METEOROLÓGICO Y DE INCERTIDUMBRE DEL MODELO

METEOROLÓGICO WRF .............................................................................................................. 11

4.3.1. ANÁLISIS MODELACIÓN METEOROLÓGICA ..................................................................... 11

4.3.2. EVALUACIÓN INCERTIDUMBRE DE LA MODELACIÓN METEOROLÓGICA ........... 21

5. PARÁMETROS DE ENTRADA DEL MODELO ................................................................................. 23

5.1. CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO ..................................................... 23

5.2. PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN .............. 23

5.2.1. ESCENARIO CONSTRUCCIÓN ................................................................................................. 24

5.2.2. ESCENARIO OPERACIÓN .......................................................................................................... 26

6. RESULTADOS ............................................................................................................................................ 31

6.1. PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC) ................................................................ 31

6.1.1. ESCENARIO CONSTRUCCIÓN ................................................................................................. 31

6.1.2. ESCENARIO OPERACIÓN .......................................................................................................... 32

6.2. RESULTADOS DE LA MODELACIÓN ......................................................................................... 34

6.2.1. ESCENARIO CONSTRUCCIÓN ................................................................................................. 35

6.2.1.1. RECEPTORES DE INTERÉS PRIMARIO ......................................................................... 35

6.2.1.2. RECEPTORES DE INTERÉS SECUNDARIO .................................................................. 36

6.2.2. ESCENARIO OPERACIÓN .......................................................................................................... 37

6.2.2.1. RECEPTORES DE INTERÉS PRIMARIO ......................................................................... 37

6.2.2.2. RECEPTORES DE INTERÉS SECUNDARIO .................................................................. 38

6.3. MAPAS DE ISOCONCENTRACIONES ........................................................................................ 40

7. CUMPLIMIENTO DE NORMATIVA .................................................................................................... 40

7.1. EVALUACIÓN APORTES EN RECEPTORES .............................................................................. 40

7.1.1. ESCENARIO CONSTRUCCIÓN ................................................................................................. 41

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

7.1.1.1. RECEPTORES DE INTERÉS PRIMARIO ......................................................................... 41

7.1.1.2. RECEPTORES DE INTERÉS SECUNDARIO .................................................................. 42

7.1.2. ESCENARIO OPERACIÓN .......................................................................................................... 43

7.1.2.1. RECEPTORES DE INTERÉS PRIMARIO ......................................................................... 43

7.1.2.2. RECEPTORES DE INTERÉS SECUNDARIO .................................................................. 44

7.2. EVALUACIÓN APORTES EN ESTACIONES DE MONITOREO ............................................ 46

7.3. ESCENARIO CONSTRUCCIÓN ..................................................................................................... 47

7.4. ESCENARIO OPERACIÓN .............................................................................................................. 49

8. CONCLUSIONES ...................................................................................................................................... 52

9. REFERENCIAS ............................................................................................................................................ 53

**APÉNDICES**

Apéndice 1: Archivos de Modelación

Apéndice 2: Isoconcentraciones de Escenario de Construcción, Operación Dominio
Costa y Operación Dominio Interior y Puntos de Máxima Concentración.

**TABLAS**

TABLA-1: Norma Primaria de Calidad del Aire .................................................................... 2

TABLA-2: Norma Secundaria de Calidad del Aire .............................................................. 3

TABLA-3: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF

............................................................................................................................................ 5

TABLA-4: Ubicación Receptores primarios y secundarios .............................................. 8

TABLA-5: Diferencia entre el promedio observado y modelado de la velocidad del
viento ............................................................................................................................. 21

TABLA-6: Estadísticos de correlación de velocidad del viento observada versus

modelada. .................................................................................................................... 23

TABLA-7: Tasas de emisión - Escenario Construcción (Dominio Costa) ................. 24

TABLA-8: Tasas de emisión - Escenario Operación (Dominio Costa) ...................... 27

TABLA-9: Tasas de emisión - Escenario Operación (Dominio Interior) ................... 28

TABLA-10: Puntos de máxima concentración y depositación (PMI) - Escenario
Construcción ............................................................................................................... 31

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA-11: Puntos de máxima concentración y depositación (PMI) - Escenario de
Operación (Dominio Costa) .................................................................................. 32

TABLA-12: Puntos de máxima concentración y depositación (PMI) - Escenario de
Operación (Dominio Interior) ............................................................................... 33

TABLA-13: Aportes del Proyecto Receptores Primarios - Escenario Construcción

.......................................................................................................................................... 35

TABLA-14: Aportes del Proyecto Receptores Secundarios - Escenario Construcción

.......................................................................................................................................... 36

TABLA-15: Aportes del Proyecto Receptores Primarios - Escenario Operación .... 37

TABLA-16: Aportes del Proyecto Receptores Secundarios - Escenario Operación

.......................................................................................................................................... 38

TABLA-17: Porcentaje Respecto a la Norma de Aportes del Proyecto en Receptores
Primarios - Escenario Construcción ................................................................... 41

TABLA-18: Porcentaje Respecto a la Norma de Aportes del Proyecto en Receptores
Secundarios - Escenario Construcción ............................................................. 42

TABLA-19: Porcentaje Respecto a la Norma de Aportes del Proyecto en Receptores
Primarios - Escenario Operación ........................................................................ 43

TABLA-20: Porcentaje Respecto a la Norma de Aportes del Proyecto en Receptores
Secundarios - Escenario Operación .................................................................. 45

TABLA-21: Calidad del aire futura para Estación Antofagasta - Escenario
Construcción ............................................................................................................... 47

TABLA-22: Calidad del aire futura para Estación La Negra - Escenario Construcción

.......................................................................................................................................... 48

TABLA-23: Calidad del aire futura para Estación Jardín Infantil Integra - Escenario
Construcción ............................................................................................................... 48

TABLA-24: Calidad del aire futura para Estación Juan José Latorre - Escenario
Construcción ............................................................................................................... 49

TABLA-25: Calidad del aire futura para Estación Antofagasta - Escenario Operación

.......................................................................................................................................... 49

TABLA-26: Calidad del aire futura para Estación La Negra - Escenario Operación

.......................................................................................................................................... 50

TABLA-27: Calidad del aire futura para Estación Jardín Infantil Integra - Escenario
Operación .................................................................................................................... 51

TABLA-28: Calidad del aire futura para Estación Juan José Latorre - Escenario
Construcción ............................................................................................................... 51

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**FIGURAS**

FIGURA-1: Ubicación Dominio de Modelación Sector Costa .......................................... 6

FIGURA-2: Ubicación Dominio de Modelación Sector Interior ....................................... 7

FIGURA-3: Ubicación de receptores discretos ..................................................................... 10

FIGURA-4: Serie de tiempo horaria velocidad del viento observada versus
modelada, Estación Mejillones ............................................................................ 12

FIGURA-5: Serie de tiempo horaria dirección del viento observada versus
modelada, Estación Mejillones ............................................................................ 13

FIGURA-6: Ciclos diarios velocidad del viento observada versus modelada, Estación
Mejillones ..................................................................................................................... 14

FIGURA-7: Ciclos diarios dirección del viento observada versus modelada, Estación
Mejillones ..................................................................................................................... 15

FIGURA-8: Ciclos estacionales de viento observado versus modelado, Estación
Mejillones ..................................................................................................................... 17

FIGURA-9: Rosas de viento observadas, Estación Mejillones ........................................ 19

FIGURA-10: Rosas de viento modeladas, Estación Mejillones ......................................... 20

FIGURA-11: Ubicación Fuentes de Emisión Escenario Construcción (Dominio Costa)

.......................................................................................................................................... 26

FIGURA-12: Ubicación Fuentes de Emisión Escenario Operación (Dominio Costa) 29

FIGURA-13: Ubicación Fuentes de Emisión Escenario Operación (Dominio Interior)

.......................................................................................................................................... 30

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**1.** **INTRODUCCIÓN**

El presente informe contiene la modelación y evaluación de la calidad del aire del proyecto
“ **Transporte Ferroviario en Región de Antofagasta** ” (en adelante, el “Proyecto”), el cual
consistirá en el desarrollo del servicio de transporte ferroviario, por vías existentes y
operativas, de ácido sulfúrico y cátodos de cobre existente actualmente entre la faena de
Minera Escondida Limitada (MEL) y los puertos de Mejillones y Antofagasta, ubicados en la
región de Antofagasta, del cual FERRONOR S.A. será el nuevo operador ferroviario.

El Proyecto contempla la construcción de dos nuevas instalaciones de apoyo a la operación
ferroviaria. La primera de ellas es el “Taller Mejillones”, el cual se ubicará en la ciudad de
Mejillones, y estará destinado a la mantención y maniobras de equipos ferroviarios. La
segunda instalación corresponde al “Patio Antofagasta”, el cual se emplazará en la ciudad
de Antofagasta, y estará destinado a realizar el transporte final de cátodos de cobre hacia el
Puerto de Antofagasta.

A partir de la descripción del Proyecto y la Estimación de Emisiones Atmosféricas detallada
en el Anexo C1-6 de la presente Declaración de Impacto Ambiental (DIA), se realiza la
Modelación de Calidad del Aire, obteniendo los efectos en la calidad del aire de las
emisiones generadas por el Proyecto en sus fases de Construcción y Operación. Cabe señalar
que debido a que el posicionamiento de las fuentes de emisión de la fase de Cierre es igual
al de la fase de Construcción y que las emisiones son considerablemente menores a las de
dicha fase, se homologa la modelación de la fase de Cierre, toda vez que la fase de
Construcción posea un escenario representativo más conservador.

La modelación de los aportes del Proyecto a las concentraciones ambientales se realiza
mediante la aplicación del sistema de modelación WRF/CALPUFF, el cual considera la
utilización de la modelación meteorológica para el año 2020 (WRF). Debido a la gran
extensión del Proyecto, se utilizan dos (2) dominios de modelación con una resolución de 1
x 1 [km]:

 - Dominio Costa: Posee un área de 50 x 119 [km], e incluye los puertos ubicados en
Mejillones y Antofagasta y la distribución de líneas ferroviarias entre éstos.

 - Dominio Interior: Posee un área de 116 x 62 [km] e incluye la línea ferroviaria hasta

MEL.

La modelación considera 36 receptores, que representan el área de estudio, dentro de los
cuales se incluyen las estaciones de calidad del aire consideradas, determinadas por el
dominio de modelación.

Por otra parte, y en concordancia a lo señalado en la “Guía para el Uso de Modelos de
Calidad del Aire en el SEIA” (Servicio de Evaluación Ambiental, 2012), los resultados de la
modelación se entregan en tablas, a modo de comparar los aportes del Proyecto con y sin
factor de corrección (obtenido en base al análisis de incertidumbre del modelo

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 1

meteorológico). Además, se comparan los resultados de la modelación respecto de la
condición de base y, a su vez, respecto de las normas primarias y secundarias de calidad del
aire nacionales y de referencia (artículo 11 del D.S. N° 40/12 que aprueba el Reglamento del
Sistema de Evaluación de Impacto Ambiental -RSEIA-), de manera de evaluar el grado de
cumplimiento normativo.

Los parámetros que se analizan corresponden a MPS, MP 10, MP 2,5, NO 2, SO 2 y CO,
presentándose para cada uno de ellos mapas con las isoconcentraciones y puntos de
máxima concentración en formato cartográfico. También, en el apéndice de este documento,
se incluyen los archivos digitales de la modelación, incluyendo los modelos WRF utilizados,
los cuales se adjuntan sólo en formato digital, debido a su tamaño, dado que no son
soportado por la plataforma digital del SEA.

Finalmente, es relevante indicar que los archivos digitales de la modelación con el modelo
CALPUFF (entradas y salidas) se presentan de manera digital en el Apéndice 1 de este
documento.

**2.** **OBJETIVO**

Determinar el aporte incremental a las concentraciones ambientales de material particulado
y gases que generará el Proyecto en los receptores sensibles identificados, y comparar
dichos aportes con respecto a las normas de calidad primaria y secundaria, considerando las
fases de construcción y operación.

**3.** **MARCO LEGAL**

Para determinar la existencia de los efectos, características o circunstancias de los literales
a), b) y d) del art. 11 de la Ley 19.300 en el área de influencia del Proyecto, debido a la
construcción y operación del Proyecto, se ha considerado la normativa ambiental primaria y
secundaria de calidad de aire vigente para el MPS, MP 10, MP 2,5, NO 2, SO 2 y CO, presentadas
en las Tablas 1 y 2 respectivamente.

TABLA-1: Norma Primaria de Calidad del Aire

|Parámetro|Cuerpo<br>Legal|Estadístico|Valor|
|---|---|---|---|
|MP10|D.S. N°12/22<br>del MMA|Promedio aritmético de tres años calendario<br>consecutivos|50 μg/m3N|
|MP10|D.S. N°12/22<br>del MMA|Percentil 98 de las concentraciones de 24 horas<br>registradas durante un período anual|130 μg/ m3N|
|MP2,5|D.S. N°12/11<br>del MMA|Promedio trianual de las concentraciones anuales|20 μg/m3|

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 2

|Parámetro|Cuerpo<br>Legal|Estadístico|Valor|
|---|---|---|---|
|||Percentil 98 de los promedios diarios registrados<br>durante un año|50 μg/m3|
|NO2|D.S. N°<br>114/2002 del<br>MINSEGPRES|Promedio<br>aritmético<br>de<br>los<br>valores<br>de<br>concentración anual de tres años calendarios<br>sucesivos|100 μg/m3N|
|NO2|D.S. N°<br>114/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario|400 μg/m3N|
|SO2|D.S.<br>N°<br>104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 99 de las<br>concentraciones de 24 horas registradas cada año|150 μg/m3N|
|SO2|D.S.<br>N°<br>104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores de concentración anual|60 μg/m3N|
|SO2|D.S.<br>N°<br>104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 98,5 de las<br>concentraciones de 1 hora registradas cada año|350 μg/m3N|
|CO|D.S. N°<br>115/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario|30.000 μg/m3N|
|CO|D.S. N°<br>115/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 8 horas (promedio móvil)<br>registrados durante un año calendario|10.000 μg/m3N|

Fuente: SINCA, 2022.

Para el caso de la normativa de calidad secundaria, se ha considerado la norma de Huasco
como referencia para el análisis de MPS.

TABLA-2: Norma Secundaria de Calidad del Aire

|Parámetro|Cuerpo<br>Legal|Estadístico|Valor|
|---|---|---|---|
|SO2|D.S. N°22/09<br>del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 99,73 de las<br>concentraciones de 1 hora registradas cada año|1.000 μg/m3N|
|SO2|D.S. N°22/09<br>del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 99,7 de las<br>concentraciones de 24 horas registradas cada año|365 μg/m3N|
|SO2|D.S. N°22/09<br>del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores de concentración anual|80 μg/m3N|
|MPS||Promedio anual (media aritmética).|150 mg/m2/día|

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 3

|Parámetro|Cuerpo<br>Legal|Estadístico|Valor|
|---|---|---|---|
||D.S.<br>N°4/1992 del<br>MINAGRI|Máximo Mensual (media aritmética)<br>|100 mg/m2/día|

Fuente: SINCA, 2022.

**4.** **METODOLOGÍA**

La modelación se realizó acorde con la metodología descrita en la Guía para el uso de
modelos de calidad del aire en el SEIA (2012), en adelante la “Guía de modelación”. Se utilizó
el modelo numérico Weather Research and Forecasting (WRF) en la generación de datos
meteorológicos para el año 2020, y el modelo CALPUFF para la modelación de la dispersión
y transporte de las emisiones, en los escenarios considerados.

**4.1.** **BASE TEÓRICA DEL MODELO UTILIZADO**

WRF es el modelo meteorológico recomendado en la Guía de modelación para la generación
de la grilla meteorológica. Este modelo genera una grilla tridimensional de campos de
viento, además de múltiples variables atmosféricas, a través de dominios anidados con una
resolución horizontal recomendada por la Guía de modelación para el dominio de menor
tamaño, de 1 kilómetro.

Por su parte, CALPUFF es un modelo de dispersión, transporte y deposición de
contaminantes atmosféricos de tipo puff lagrangiano-gaussiano, no estacionario,
recomendado por la Guía de modelación y también por la Agencia de Protección Ambiental
de Estados Unidos (US EPA en su sigla en inglés) [1], el cual es aplicable a terrenos complejos
y a múltiples tipos de fuentes emisoras (puntuales, areales y volumétricas). CALPUFF realiza
sus cálculos tomando los datos meteorológicos superficiales y de la capa superior
atmosférica, incluyendo la posibilidad de modelar la dispersión de contaminantes primarios
y secundarios, obteniendo resultados confiables para distancias de hasta 100 [km].

El sistema de modelación incluye tres componentes principales: CALMET, CALPUFF y
CALPOST, además de una serie de programas de preprocesamiento diseñados para la
preparación de la información meteorológica y geofísica. En este caso, no se utilizaron los
preprocesadores ni el módulo CALMET, ya que se emplearon directamente los resultados de
la modelación meteorológica realizada con WRF, en base a los lineamientos de la
mencionada Guía.

1 40 CFR Part 51, Revision to the Guideline on Air Quality Models: Adoption of a Preferred General Purpose (Flat
and Complex Terrain) Dispersion Model and Other Revisions; Final Rule.
http://www.epa.gov/ttn/scram/guidance/guide/appw_05.pdf

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 4

CALPOST es un programa postprocesador que permite compilar los resultados de CALPUFF,
creando los archivos según los estadísticos establecidos en las normas de calidad del aire
para la evaluación de los resultados.

**4.2.** **CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN**

Para que los procesos meteorológicos de mesoescala sean representados de una forma
adecuada, tanto por el modelo meteorológico como por el modelo de dispersión, se
generaron dos (2) dominios de modelación de WRF/CALPUFF, en donde se consideraron las
características topográficas de la zona.

Cabe señalar que las modelaciones meteorológicas WRF fueron realizada para el año 2020,
de acuerdo con la configuración definida por el SEA en su Guía de modelación: cuenta con
una resolución horizontal de 1 [km] y una resolución vertical de 10 niveles a 20, 40, 80, 160,
320, 640, 1.200, 2.000, 3.000 y 4.000 metros. En la tabla a continuación se señalan las
coordenadas de los vértices de los dominios de modelación WRF/CALPUFF.

TABLA-3: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF

|Dominio|Vértices|Coordenadas UTM [m] Datum: WGS-84, Huso: 19S|Col4|
|---|---|---|---|
|**Dominio**|**Vértices**|**Este**|**Norte**|
|**Costa**|**SW**|339.411|7.362.261|
|**Costa**|**NE**|388.399|7.481.239|
|**Costa**|**NW**|338.322|7.480.787|
|**Costa**|**SE**|389.489|7.362.733|
|**Interior**|**SW**|377.357|7.315.807|
|**Interior**|**NE**|493.253|7.378.083|
|**Interior**|**NW**|377.073|7.377.551|
|**Interior**|**SE**|493.533|7.316.349|

Fuente: JIA, 2022.

A continuación, se presentan gráficamente, ambos dominios:

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 5

FIGURA-1: Ubicación Dominio de Modelación Sector Costa

Fuente: JIA, 2022.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 6

FIGURA-2: Ubicación Dominio de Modelación Sector Interior

Fuente: JIA, 2022.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 7

Dentro del dominio, se han considerado los siguientes receptores, correspondientes a las
estaciones de monitoreo de calidad del aire operativas en las comunas de Antofagasta y
Mejillones. También se consideraron todos los receptores de interés de ruido, además de
sectores con posible riesgo de afectación a los recursos naturales, tales como nidos de
gaviotín y comunidades indígenas y agrícolas cercanas

TABLA-4: Ubicación Receptores primarios y secundarios

|ID|Nombre Receptor|Tipo de Receptor|Descripción|Coordenadas UTM<br>WGS84 Huso 19S [m]|Col6|
|---|---|---|---|---|---|
|**ID**|**Nombre Receptor**|**Tipo de Receptor**|**Descripción**|**Este**|**Norte**|
|R_1|Estación La Negra|Primario|Estación<br>Monitora|365.988|7.368.263|
|R_2|Estación monitora Antofagasta|Primario|Estación<br>Monitora|358.874|7.387.875|
|R_3|Estación monitora Juan José<br>Latorre|Primario|Estación<br>Monitora|352.346|7.444.100|
|R_4|Estación monitora Jardín Infantil<br>Integra|Primario|Estación<br>Monitora|352.064|7.444.407|
|R_5|R01|Primario|Ruido|355.188|7.444.680|
|R_6|R02|Primario|Ruido|355.647|7.444.804|
|R_7|R03|Primario|Ruido|356.248|7.444.390|
|R_8|R05|Primario|Ruido|354.528|7.445.124|
|R_9|R06|Primario|Ruido|357.148|7.398.933|
|R_10|R07|Primario|Ruido|357.055|7.398.870|
|R_11|R09|Primario|Ruido|357.679|7.398.684|
|R_12|R08|Primario|Ruido|357.461|7.397.976|
|R_13|RC1|Primario|Ruido|357.796|7.384.730|
|R_14|RC2|Primario|Ruido|358.766|7.392.127|
|R_15|RC3|Primario|Ruido|357.291|7.381.486|
|R_16|RC4|Primario|Ruido|371.654|7.389.726|
|R_17|RC5|Primario|Ruido|372.858|7.382.006|

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 8

|ID|Nombre Receptor|Tipo de Receptor|Descripción|Coordenadas UTM<br>WGS84 Huso 19S [m]|Col6|
|---|---|---|---|---|---|
|**ID**|**Nombre Receptor**|**Tipo de Receptor**|**Descripción**|**Este**|**Norte**|
|R_18|RC6|Primario|Ruido|358.429|7.386.993|
|R_19|G1|Secundario|Nido Gaviotín|356.480|7.399.280|
|R_20|G2|Secundario|Nido Gaviotín|355.820|7.399.546|
|R_21|G3|Secundario|Nido Gaviotín|354.700|7.402.572|
|R_22|G4|Secundario|Nido Gaviotín|353.236|7.402.746|
|R_23|G5|Secundario|Nido Gaviotín|351.555|7.406.113|
|R_24|G6|Secundario|Nido Gaviotín|351.973|7.442.615|
|R_25|G7|Secundario|Nido Gaviotín|357.424|7.446.515|
|R_26|G8|Secundario|Nido Gaviotín|358.042|7.445.613|
|R_27|G9|Secundario|Nido Gaviotín|358.835|7.447.451|
|R_28|G10|Secundario|Nido Gaviotín|360.618|7.449.815|
|R_29|G11|Secundario|Nido Gaviotín|363.803|7.455.423|
|R_30|G12|Secundario|Nido Gaviotín|366.343|7.461.606|
|R_31|G13|Secundario|Nido Gaviotín|368.698|7.465.827|
|R_32|AINA|Prim/Sec|Asociación<br>Indígena|357.195|7.400.048|
|R_33|Altos de la Portada|Prim/Sec|Asociación<br>Indígena|357.086|7.400.094|
|R_34|ASAIA|Prim/Sec|Asociación<br>Indígena|359.050|7.386.830|
|R_35|RX|Primario|Centro<br>poblado|357.225|7.399.081|
|R_36|Estación Monitora La Negra|Primario<br>|Estación<br>Monitora|365.786|7.367.902|

Fuente: JIA, 2022.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 9

Para una mejor comprensión, en la siguiente figura se presenta la ubicación geográfica de
los receptores discretos:

FIGURA-3: Ubicación de receptores discretos

Fuente: JIA, 2022.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 10

**4.3.** **ANÁLISIS METEOROLÓGICO Y DE INCERTIDUMBRE DEL MODELO**
**METEOROLÓGICO WRF**

La modelación atmosférica está basada en uno de los modelos de pronóstico meteorológico
más avanzados y completos disponibles [2], el cual cuenta con un gran número de
parametrizaciones que permiten, si son adecuadamente seleccionadas e implementadas,
simular gran parte de los procesos meteorológicos de mesoescala. Este modelo
corresponde, como ya se ha mencionado, al Weather Research and Forecasting (WRF). En el
caso del presente estudio, el modelo WRF utilizado ha sido parametrizado de acuerdo con
lo establecido por el SEA y corresponde al año 2020.

Sin embargo, e independiente de las bondades del sistema utilizado, todo modelo
atmosférico requiere ser validado para cada condición meteorológica y de terreno. En este
punto es donde se tienen las mayores dificultades, dado que la incorrecta implementación
de alguna parametrización puede llevar a errores significativos en la estimación de los
vientos en superficie y, consecuentemente, de las trayectorias de los contaminantes.

Por ello, para realizar el análisis de incertidumbre se han considerado las recomendaciones
establecidas en la Guía de modelación descritas en el acápite 7, donde menciona que
cualquier modelo representa una aproximación a la realidad y sus resultados tienen
incertidumbres asociadas, las cuales se expresan a través de diferencias entre lo estimado y
lo observado. A continuación, se realiza este análisis utilizando la Estación Meteorológica
Mejillones.

**4.3.1.** **Análisis Modelación Meteorológica**

En esta sección se presenta una comparación de series temporales, ciclos diarios, ciclos
estacionales y rosas de vientos entre los registros de la estación meteorológica Mejillones
en 2020 [3] (datos observados) con los valores de las variables meteorológicas pronosticados
por el modelo WRF (Weather Research and Forecasting) para la misma localización de la
estación mencionada (datos modelados) y durante el mismo periodo, con el fin de evaluar
la capacidad predictiva del modelo.

**Series de Tiempo**

En la presente sección se presentan las series de tiempo de velocidad y dirección del viento,
tanto observadas como modeladas:

2 Numeral 5.3.2 Fuentes de Datos Meteorológicas. Guía para el uso de modelos de calidad del aire. SEA 2012.

3 Información obtenida del Instituto de Investigaciones Agropecuarias (INIA), www.agrometeorología.cl

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 11

FIGURA-4: Serie de tiempo horaria velocidad del viento observada versus modelada,

Estación Mejillones

|OBSERVADO|Col2|
|---|---|
|**MODELADO**|<br>|

Fuente: Adaptación SGA.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 12

FIGURA-5: Serie de tiempo horaria dirección del viento observada versus modelada,

Estación Mejillones

|OBSERVADO|Col2|
|---|---|
|**MODELADO**|<br> <br>|

Fuente: Adaptación SGA.

En la figura de velocidad del viento, se puede apreciar la continuidad de registros para el
periodo de análisis, no observándose periodos extensos con falta de datos. Además, se
aprecia que tanto la velocidad del viento observada como modelada se mantienen la mayor
parte del año bajo los 5 [m/s]. No obstante, la velocidad del viento observada muestra mayor
cantidad de registros sobre este rango, por lo que se aprecia cierta subestimación de las
velocidades del viento modeladas. Además, se muestra una tendencia de las velocidades del

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 13

viento observadas a disminuir en el periodo abril-julio, lo cual no es claro en el caso de las
velocidades modeladas.

Con respecto a la dirección del viento, se muestra una similitud entre los registros
observados y modelados, con predominio en ambos de las direcciones con ángulos entre
180° y 240°, es decir, aquellos vientos de origen Suroeste. Además, en ambos casos se
observan componentes relevantes entre los 340° y 20°, es decir, vientos de origen Norte
durante todo el año.

**Ciclos Diarios**

En la presente sección se presentan los ciclos diarios de velocidad y dirección del viento,
tanto observados como modelados:

FIGURA-6: Ciclos diarios velocidad del viento observada versus modelada, Estación

Mejillones

|OBSERVADO|Col2|
|---|---|
|**MODELADO**|<br>|

Fuente: Adaptación SGA.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 14

FIGURA-7: Ciclos diarios dirección del viento observada versus modelada, Estación

Mejillones

|OBSERVADO|Col2|
|---|---|
|**MODELADO**|<br> <br> <br>|

Fuente: Adaptación SGA.

Para la velocidad del viento se presentan los ciclos diarios promedios junto con su
variabilidad en términos de los percentiles 5 y 95, correspondientes a la estación Mejillones,
tanto de la velocidad del viento observada como modelada. Estos gráficos muestran tanto
la variación típica de la velocidad del viento, como su variabilidad diaria. En esta figura se
puede apreciar que el ciclo de velocidad del viento observado en la estación Mejillones

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 15

presenta una velocidad promedio máxima a las 18:00 horas, la cual alcanza los 5,8 [m/s],
mientras que la máxima velocidad promedio del viento modelada se registra a las 16:00
horas, alcanzando los 4,02 [m/s]. Esto indica que el modelo sobreestima los valores de esta
variable. En ambos casos, la velocidad del viento desciende durante el ciclo nocturno,
alcanzando un mínimo promedio a las 09:00 horas para los datos observados y a las 03:00
horas en el caso modelado. En general, durante este periodo del ciclo diario, la velocidad
del viento observada es mayor que la observada, presentando ambas un rango de variación
bastante similar.

Respecto al ciclo diario de velocidad del viento se muestra, en términos porcentuales, la
frecuencia de las direcciones del viento durante el ciclo diario completo en la misma
estación, tanto observadas como modeladas con WRF 2020. En la figura se puede apreciar
que tanto los valores observados como modelados de esta variable presentan un
comportamiento similar, con un predominio durante el ciclo diurno (entre las 08:00 y 19:00
horas) de componentes Noroeste, es decir, en el rango entre 270°-360°, seguidos de
componentes de viento entre los 0° y 90°, es decir, Noreste. Durante el ciclo nocturno (20:00
horas a 07:00 horas), en tanto, la dirección del viento observada y modelada muestran un
mayor predominio de las componentes entre 90° y 180°, es decir, Sureste.

**Ciclos Estacionales**

En la presente sección se presentan los ciclos estacionales de viento, tanto observados como
modelados:

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 16

FIGURA-8: Ciclos estacionales de viento observado versus modelado, Estación Mejillones

|OBSERVADO|Col2|
|---|---|
|**MODELADO**|<br> <br>|

Fuente: Adaptación SGA.

En la figura se ilustra la variación estacional de los ciclos diarios anuales para la estación
Mejillones en el año 2020, de las velocidades y direcciones del viento, tanto observadas
como modeladas. Los colores representan las distintas intensidades de la velocidad del
viento durante el ciclo estacional, mientras que la dirección del viento está representada por
las flechas sobrepuestas que indican la componente predominante. En esta se puede

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 17

apreciar que los ciclos estacionales del viento observados y modelados muestran que los
vientos durante el periodo estival y durante el ciclo diurno son más intensos, generando
buenas condiciones de ventilación en el área de interés, lo que provocaría que los
contaminantes emitidos en la zona se dispersen de manera más rápida, específicamente
entre las 15:00 y 21:00 horas para el caso observado, y entre las 10:00 y 18:00 horas para el
caso modelado. Con respecto a la dirección del viento, las componentes predominantes
durante el ciclo diario y durante los distintos meses del año, están en concordancia con lo
indicado en el análisis de las series temporales y del ciclo diario, es decir, Noroeste-Noreste
en ciclo diurno y Sureste en ciclo nocturno.

**Rosas de Viento**

En la presente sección se presentan las rosas de viento, tanto observadas como modeladas,
en sus periodos diurno, nocturno y total:

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 18

FIGURA-9: Rosas de viento observadas, Estación Mejillones

|Ciclo Diurno|Ciclo Nocturno|
|---|---|
|||
|**Ciclo Diario Completo**|**Ciclo Diario Completo**|
|||

Fuente: Adaptación SGA.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 19

FIGURA-10: Rosas de viento modeladas, Estación Mejillones

|Ciclo Diurno|Ciclo Nocturno|
|---|---|
|||
|**Ciclo Diario Completo**|**Ciclo Diario Completo**|
|||

Fuente: Adaptación SGA.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 20

En las figuras de muestran las rosas de viento en la estación Mejillones en 2020, para el caso
observado y modelado, respectivamente. En cada una de estas figuras se representan tanto
la dirección del viento promedio anual (ciclo diario completo) así como también el promedio
del ciclo diurno (8:00 a 19:00 horas) y el ciclo nocturno (20:00 a 7:00 horas). De acuerdo con
estas rosas de vientos, se puede apreciar que, tanto en el caso de los registros observados
como los modelados, se presenta un comportamiento similar, con una componente
predominante durante el ciclo diario completo correspondiente a los vientos de origen
Suroeste, seguidos de los vientos Noroeste-Noreste. En el caso de las rosas del viento de los
datos observados y modelados, se observa que durante el ciclo nocturno se produce una
notable disminución en la predominancia de los vientos de origen Noroeste-Noreste,
mientras que aumentan y predominan los vientos de origen Suroeste. En tanto, durante el
ciclo diurno, se tiene un predominio más equitativo de las componentes de vientos de origen
Noroeste-Noreste y Suroeste.

**4.3.2.** **Evaluación Incertidumbre de la Modelación Meteorológica**

Para evaluar la incertidumbre de la modelación WRF-2020 se comparan las velocidades de
viento promedio modeladas con las velocidades registradas en la estación monitora
Mejillones, resumidas en la sección anterior. Esto con el objetivo de estimar un porcentaje
de error asociado a la modelación meteorológica que pueda ser extrapolado a las
concentraciones resultantes, de acuerdo con la modelación de la dispersión de
contaminantes.

La siguiente tabla presenta las diferencias entre la velocidad del viento promedio anual 2020,
de acuerdo con la modelación WRF con lo registrado en estación Mejillones

TABLA-5: Diferencia entre el promedio observado y modelado de la velocidad del viento

|Estación|Promedio Observado|Promedio Modelado|Diferencia Absoluta|
|---|---|---|---|
|Mejillones|3,81|2,72|28,6%|

Fuente: Adaptado SGA.

De la tabla anterior se puede deducir que el modelo, si bien replica aceptablemente las
condiciones meteorológicas de la zona, si posee una diferencia cuantitativa en comparación
con los datos observados. No obstante, también se puede apreciar que el modelo WRF
genera un escenario desfavorable respecto de las condiciones de ventilación en el área de
interés, debido a que subestima la magnitud de la velocidad del viento, lo que implica una
menor dispersión de contaminantes. Por lo tanto, considerando que la modelación WRF
establece las condiciones de dispersión en CALPUFF, la modelación de calidad del aire
estaría sobrestimando las concentraciones de contaminantes en el área de modelación, es
decir, los resultados representan una peor condición, por lo cual no se debe aplicar un factor
de corrección a las concentraciones modeladas.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 21

Adicionalmente a lo anterior, se han considerado las siguientes medidas de error estadístico
para el análisis de incertidumbre del modelo:

**Sesgo** : Representa la tendencia del modelo WRF a sobreestimar o subestimar las
condiciones reales. Si el valor es negativo, el modelo subestima el valor de las variables
modeladas y viceversa. La fórmula para el cálculo del sesgo es la siguiente:

"

S= [1]

N [%(M] [!] [ −O] [!] [)]

!#$

Donde:

S : Sesgo

N : Tamaño Muestra

M : Valor Modelado

O Valor Observado

**Error Cuadrático Medio** : Este valor entre la diferencia promedio entre los valores
promedios modelados y observados. La fórmula para el cálculo del error cuadrático medio
es la siguiente:

"

ECM=
%

!#$

~~-~~

"

(M ! −O ! ) [%]

N

!#$

Donde:

ECM : Error Cuadrático Medio

N : Tamaño Muestra

M : Valor Modelado

O Valor Observado

**Coeficiente de Correlación** : Mide la relación lineal entre la variable modelada y la variable
observada. El resultado de este coeficiente se encuentra en el intervalo [-1, 1]. El valor 1
representa una correlación positiva perfecta entre la variable modelada y observada,
mientras que el valor -1 muestra una correlación negativa perfecta. La fórmula para el cálculo
del error cuadrático medio es la siguiente:

"

r= [1]

N [%]

!#$

(M ! −M [/] )(O ! −O [0] )

σ & σ '

Donde:

r : Coeficiente de Correlación

N : Tamaño Muestra

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 22

M : Valor Modelado

O Valor Observado

σ Desviación Estándar

La siguiente tabla muestra los resultados del cálculo de estos estadísticos aplicados a la
velocidad del viento modelada y observada en la estación Mejillones en 2020. En ella se
puede ver que, según el sesgo, el modelo subestima la velocidad del viento, tal como se
mencionó anteriormente. Además, las velocidades observadas y modeladas tienen una
correlación positiva alta, mientras que el error medio entre ambas es de 2,281 [m/s].

TABLA-6: Estadísticos de correlación de velocidad del viento observada versus modelada.

|Estación|Sesgo|Coeficiente de<br>Correlación|Error Medio Cuadrático|
|---|---|---|---|
|Mejillones|-0,881<br>|0,308<br>|2,281|

Fuente: Adaptado SGA.

**5.** **PARÁMETROS DE ENTRADA DEL MODELO**

A continuación, se detallan los principales parámetros de entrada del modelo de calidad del
aire, los que corresponden a: características topográficas, uso del suelo, fuentes emisoras
externas (aportes de terceros) y escenario de modelación (emisiones asociadas a las
instalaciones donde se emplaza el Proyecto).

**5.1.** **CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO**

Las características topográficas y de uso de suelo, son parámetros asociados a la elevación
de terreno, los coeficientes de rugosidad, razón de bowen, entre otros, que son parte
integrante de los datos que incluye el archivo de modelación WRF, por lo cual no se requiere
su caracterización.

**5.2.** **PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN**

En los siguientes acápites se presentan las tasas de emisión ingresadas a la modelación de
calidad del aire. Como escenario de evaluación, se consideraron dos (2):

 - **Escenario Construcción** : Sus emisiones se presentan durante el primer año del
Proyecto.

 **Escenario Operación** : Para esta fase, las emisiones anuales son las mismas para cada
año de operación, por lo que se utilizan para la modelación estas emisiones anuales.

Las emisiones anuales asociadas a cada escenario se presentan con más detalle en el Anexo
C1-6 Estimación de Emisiones Atmosféricas.

ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE 23

**5.2.1.** **Escenario Construcción**

A continuación, se presentan las tasas de emisión por fuente. Cabe señalar que la totalidad de las fuentes se encuentran dentro del
Dominio Costa, por lo que solo se utiliza dicho dominio para la modelación:

TABLA-7: Tasas de emisión - Escenario Construcción (Dominio Costa)

|Tipo de<br>Fuente|ID|Fuente|Emisiones|Col5|Col6|Col7|Col8|Col9|Unidad|
|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Fuente**|**ID**|**Fuente**|**MPS**|**MP10 **|**MP2,5 **|**NOX **|**CO**|**SO2 **|**SO2 **|
|AREA_POLY|SRC_9|Patio Antofagasta|1,20E-05|3,84E-06|2,69E-06|3,15E-05|1,55E-05|9,61E-08|kg/h-m2|
|AREA_POLY|SRC_18|Taller Mejillones|5,78E-06|1,92E-06|1,37E-06|1,37E-05|6,72E-06|4,18E-08|kg/h-m2|
|POINT|SRC_34|Generador 50 kVA|5,90E-02|5,90E-02|5,90E-02|8,27E-01|1,79E-01|5,50E-02|kg/h|
|POINT|SRC_35|Generador 40 kVA|1,57E-02|1,57E-02|1,57E-02|2,21E-01|4,76E-02|1,47E-02|kg/h|
|ROAD|SRC_8|Camino acceso patio|8,90E-04|2,55E-04|2,59E-05|1,59E-05|5,60E-06|4,98E-08|kg/h-m|
|ROAD|SRC_10|Ruta Combustible Patio|1,95E-08|4,09E-09|1,32E-09|1,87E-08|4,67E-09|6,87E-11|kg/h-m|
|ROAD|SRC_11|Ruta Agua Potable Patio|3,91E-08|8,19E-09|2,63E-09|3,73E-08|9,34E-09|1,37E-10|kg/h-m|
|ROAD|SRC_12|Ruta Relleno Sanitario Patio|1,27E-07|2,66E-08|8,55E-09|1,21E-07|3,04E-08|4,47E-10|kg/h-m|
|ROAD|SRC_13|Ruta Hidronor - Patio|1,63E-09|3,41E-10|1,10E-10|1,56E-09|3,89E-10|5,72E-12|kg/h-m|
|ROAD|SRC_14|Ruta Personal Antofagasta- Patio|8,53E-07|1,74E-07|5,17E-08|4,72E-07|1,23E-07|1,85E-09|kg/h-m|
|ROAD|SRC_15|Ruta Personal Mejillones- Patio|6,38E-07|1,29E-07|3,69E-08|2,63E-07|6,99E-08|1,11E-09|kg/h-m|
|ROAD|SRC_16|Camino no pavimentado vertedero Mejillones|1,52E-05|4,36E-06|4,55E-07|6,38E-07|2,34E-07|2,03E-09|kg/h-m|
|ROAD|SRC_17|Camino Acceso Taller|4,39E-04|1,26E-04|1,31E-05|1,98E-05|6,32E-06|5,82E-08|kg/h-m|
|ROAD|SRC_19|Ruta Agua Potable Taller|1,56E-07|3,28E-08|1,05E-08|1,49E-07|3,74E-08|5,50E-10|kg/h-m|
|ROAD|SRC_20|Ruta Vertedero Mejillones|2,73E-07|5,73E-08|1,84E-08|2,61E-07|6,54E-08|9,62E-10|kg/h-m|
|ROAD|SRC_21|Ruta Personal Antofagasta- Taller|2,14E-06|4,39E-07|1,33E-07|1,36E-06|3,53E-07|5,17E-09|kg/h-m|
|ROAD|SRC_22|Ruta Personal Mejillones- Taller|2,14E-06|4,39E-07|1,33E-07|1,36E-06|3,53E-07|5,17E-09|kg/h-m|
|ROAD|SRC_23|Ruta Agua Industrial -Materiales Taller|3,76E-06|7,89E-07|2,53E-07|3,60E-06|9,00E-07|1,32E-08|kg/h-m|
|ROAD|SRC_24|Ruta Agua Industrial -Materiales Patio|5,53E-06|1,16E-06|3,72E-07|5,28E-06|1,32E-06|1,95E-08|kg/h-m|
|ROAD|SRC_25|Ruta Hidronor No Pavimentado|2,71E-07|7,78E-08|8,13E-09|1,14E-08|4,18E-09|3,63E-11|kg/h-m|
|ROAD|SRC_32|Ruta Hidronor Taller Mejillones- Parte 1|3,26E-09|6,82E-10|2,19E-10|3,11E-09|7,79E-10|1,14E-11|kg/h-m|
|ROAD|SRC_33|Ruta Hidronor Taller Mejillones- Parte 2|3,26E-09|6,82E-10|2,19E-10|3,11E-09|7,79E-10|1,14E-11|kg/h-m|

24
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|Tipo de<br>Fuente|ID|Fuente|Emisiones|Col5|Col6|Col7|Col8|Col9|Unidad|
|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Fuente**|**ID**|**Fuente**|**MPS**|**MP10 **|**MP2,5 **|**NOX **|**CO**|**SO2 **|**SO2 **|
|ROAD|SRC_36|Camino interior Patio|4,27E-04|1,22E-04|1,27E-05|1,59E-05|5,60E-06|4,98E-08|kg/h-m|
|ROAD|SRC_37|Camino interior Taller Mejillones 1|4,39E-04|1,26E-04|1,31E-05|1,98E-05|6,32E-06|5,82E-08|kg/h-m|
|ROAD|SRC_38|Camino interior Taller Mejillones 2|4,39E-04|1,26E-04|1,31E-05|1,98E-05|6,32E-06|5,82E-08|kg/h-m|

Fuente: JIA, 2022.

A continuación, se presentan gráficamente las fuentes utilizadas en el presente escenario:

25
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

FIGURA-11: Ubicación Fuentes de Emisión Escenario Construcción (Dominio Costa)

Fuente: JIA, 2022.
**5.2.2.** **Escenario Operación**

26
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

A continuación, se presentan las tasas de emisión por fuente. Cabe señalar que, para este escenario, las fuentes se encuentran dentro
de ambos Dominios, Costa e Interior, por lo que a continuación se diferencian las fuentes por dominio:

TABLA-8: Tasas de emisión - Escenario Operación (Dominio Costa)

|Tipo de<br>Fuente|ID|Fuente|Emisiones|Col5|Col6|Col7|Col8|Col9|Unidad|
|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Fuente**|**ID**|**Fuente**|**MPS**|**MP10 **|**MP2,5 **|**NOX **|**CO**|**SO2 **|**SO2 **|
|AREA_POLY|SRC_9|Patio Antofagasta|2,85E-06|2,85E-06|2,85E-06|1,35E-04|8,87E-05|5,63E-07|kg/h-m2|
|AREA_POLY|SRC_18|Taller Mejillones|1,24E-06|1,24E-06|1,24E-06|5,85E-05|3,85E-05|2,45E-07|kg/h-m2|
|LINE_AREA|SRC_1|Vía Férrea 3|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_2|Vía Férrea 4|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_3|Vía Férrea 5|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_4|Vía Férrea 6|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_5|Vía Férrea 7|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_6|Vía Férrea interior Patio|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_7|Vía Férrea Interior Taller|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_26|Vía Férrea 1 Dominio Costa|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_29|Vía Férrea 2 Parte 1|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_30|Vía Férrea 2 Parte 2|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_31|Vía Férrea 2 Parte 3|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|POINT|SRC_34|Generador 50 kVA|5,96E-04|5,96E-04|5,96E-04|8,36E-03|1,80E-03|5,56E-04|kg/h|
|POINT|SRC_35|Generador 500 kVA|5,96E-03|5,96E-03|5,96E-03|8,36E-02|1,80E-02|5,56E-03|kg/h|
|ROAD|SRC_8|Camino acceso patio|1,47E-04|4,21E-05|4,29E-06|3,20E-06|9,79E-07|9,86E-09|kg/h-m|
|ROAD|SRC_10|Ruta Combustible Patio|1,95E-08|4,09E-09|1,32E-09|1,87E-08|4,67E-09|6,87E-11|kg/h-m|
|ROAD|SRC_11|Ruta Agua Potable Patio|3,91E-08|8,19E-09|2,63E-09|3,73E-08|9,34E-09|1,37E-10|kg/h-m|
|ROAD|SRC_12|Ruta Relleno Sanitario Patio|2,54E-07|5,32E-08|1,71E-08|2,43E-07|6,07E-08|8,93E-10|kg/h-m|
|ROAD|SRC_13|Ruta Hidronor - Patio|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|kg/h-m|
|ROAD|SRC_14|Ruta Personal Antofagasta- Patio|1,16E-06|2,37E-07|7,05E-08|6,44E-07|1,68E-07|2,52E-09|kg/h-m|
|ROAD|SRC_15|Ruta Personal Mejillones- Patio|5,77E-07|1,13E-07|3,00E-08|7,26E-08|2,28E-08|5,14E-10|kg/h-m|
|ROAD|SRC_16|Camino no pavimentado vertedero Mejillones|1,52E-05|4,36E-06|4,55E-07|6,38E-07|2,34E-07|2,03E-09|kg/h-m|
|ROAD|SRC_17|Camino Acceso Taller|1,45E-04|4,17E-05|4,36E-06|8,44E-06|2,46E-06|2,36E-08|kg/h-m|

27
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|Tipo de<br>Fuente|ID|Fuente|Emisiones|Col5|Col6|Col7|Col8|Col9|Unidad|
|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Fuente**|**ID**|**Fuente**|**MPS**|**MP10 **|**MP2,5 **|**NOX **|**CO**|**SO2 **|**SO2 **|
|ROAD|SRC_19|Ruta Agua Potable Taller|7,81E-08|1,64E-08|5,26E-09|7,47E-08|1,87E-08|2,75E-10|kg/h-m|
|ROAD|SRC_20|Ruta Vertedero Mejillones|2,73E-07|5,73E-08|1,84E-08|2,61E-07|6,54E-08|9,62E-10|kg/h-m|
|ROAD|SRC_21|Ruta Personal Antofagasta- Taller|1,16E-06|2,37E-07|7,05E-08|6,44E-07|1,68E-07|2,52E-09|kg/h-m|
|ROAD|SRC_22|Ruta Personal Mejillones- Taller|1,82E-06|4,30E-07|1,33E-07|1,53E-06|3,92E-07|5,69E-09|kg/h-m|
|ROAD|SRC_23|Ruta Agua Industrial -Materiales Taller|6,84E-08|1,43E-08|4,60E-09|6,53E-08|1,64E-08|2,40E-10|kg/h-m|
|ROAD|SRC_24|Ruta Agua Industrial -Materiales Patio|3,42E-08|7,17E-09|2,30E-09|3,27E-08|8,18E-09|1,20E-10|kg/h-m|
|ROAD|SRC_25|Ruta Hidronor No Pavimentado|1,81E-07|5,19E-08|5,42E-09|7,59E-09|2,79E-09|2,42E-11|kg/h-m|
|ROAD|SRC_32|Ruta Hidronor Taller Mejillones- Parte 1|3,26E-09|6,82E-10|2,19E-10|3,11E-09|7,79E-10|1,14E-11|kg/h-m|
|ROAD|SRC_33|Ruta Hidronor Taller Mejillones- Parte 2|3,26E-09|6,82E-10|2,19E-10|3,11E-09|7,79E-10|1,14E-11|kg/h-m|
|ROAD|SRC_36|Camino interior Patio|7,05E-05|2,02E-05|2,10E-06|3,20E-06|9,79E-07|9,86E-09|kg/h-m|
|ROAD|SRC_37|Camino interior Taller Mejillones 1|1,45E-04|4,17E-05|4,36E-06|8,44E-06|2,46E-06|2,36E-08|kg/h-m|
|ROAD|SRC_38|Camino interior Taller Mejillones 2|1,45E-04|4,17E-05|4,36E-06|8,44E-06|2,46E-06|2,36E-08|kg/h-m|

Fuente: JIA, 2022.

TABLA-9: Tasas de emisión - Escenario Operación (Dominio Interior)

|Tipo de<br>Fuente|ID|Fuente|Emisiones|Col5|Col6|Col7|Col8|Col9|Unidad|
|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Fuente**|**ID**|**Fuente**|**MPS**|**MP10 **|**MP2,5 **|**NOX **|**CO**|**SO2 **|**SO2 **|
|LINE_AREA|SRC_1|Vía Férrea 1 Dominio Interior- Parte 1|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|
|LINE_AREA|SRC_2|Vía Férrea 1 Dominio Interior- Parte 2|2,45E-06|2,45E-06|2,45E-06|6,73E-05|1,74E-05|8,54E-08|kg/h-m|

Fuente: JIA, 2022.

A continuación, se presentan gráficamente las fuentes utilizadas en el presente escenario para cada dominio:

28
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

FIGURA-12: Ubicación Fuentes de Emisión Escenario Operación (Dominio Costa)

Fuente: JIA, 2022.

29
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

FIGURA-13: Ubicación Fuentes de Emisión Escenario Operación (Dominio Interior)

Fuente: JIA, 2022.

30
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**6.** **RESULTADOS**

A continuación, se presentan los valores de máxima concentración obtenidos mediante el
modelo, para cada contaminante y período analizado. Adicionalmente, se presentan los
aportes estimados de cada escenario considerado para cada parámetro de interés y
finalmente los mapas de isoconcentraciones.

**6.1.** **PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC)**

**6.1.1.** **Escenario Construcción**

En la siguiente tabla se presentan las coordenadas y aportes de los puntos de máxima
concentración modelada, para cada parámetro y estadístico del Escenario Construcción
(Dominio Costa)

TABLA-10: Puntos de máxima concentración y depositación (PMI) - Escenario

Construcción

|Puntos de Máximo Impacto (PMI) - Fase Construcción|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Parámetro**|**Tipo de norma**|**Coordenadas UTM**<br>**WGS84 Huso 19S**|**Coordenadas UTM**<br>**WGS84 Huso 19S**|**PMI**|**Unidad**|**ID**|
|**Parámetro**|**Tipo de norma**|**Este [m]**|**Norte [m]**|**Norte [m]**|**Norte [m]**|**Norte [m]**|
|MPS|Promedio anual|357.601|7.398.791|1,67|mg/m2-día|PMD 1|
|MPS|Promedio Mensual|357.601|7.398.791|3,29|mg/m2-día|PMD 1|
|MP10|Promedio anual|357.601|7.398.791|1,15|μg/m3|PMC 1|
|MP10|P98 diario|357.601|7.398.791|5,57|μg/m3|PMC 1|
|MP2,5|Promedio anual|357.601|7.398.791|0,46|μg/m3|PMC 1|
|MP2,5|P98 diario|357.601|7.398.791|2,21|μg/m3|PMC 1|
|SO2|Promedio anual|357.601|7.398.791|0,03|μg/m3|PMC 1|
|SO2|P99 diario|357.601|7.398.791|0,22|μg/m3|PMC 1|
|SO2|P98,5 horario|357.601|7.398.791|0,41|μg/m3|PMC 1|
|SO2|P99,7 diario|357.601|7.398.791|0,03|μg/m3|PMC 1|
|SO2|P99,73 horario|357.601|7.398.791|1,17|μg/m3|PMC 1|
|NO2|Promedio anual|357.601|7.398.791|0,25|μg/m3|PMC 1|
|NO2|P99 horario|357.601|7.398.791|0,45|μg/m3|PMC 1|
|CO|P99 horario|357.601|7.398.791|13,75|μg/m3|PMC 1|
|CO|P99 8 horas|357.601|7.398.791|27,04|μg/m3|PMC 1|

Fuente: JIA, 2022.

En el Apéndice 2 se presenta la representación gráfica de cada uno de los puntos de máxima
concentración.

31
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**6.1.2.** **Escenario Operación**

En la siguiente tabla se presentan las coordenadas y aportes de los puntos de máxima
concentración modelada, para cada parámetro y estadístico del Escenario Operación. Se
presenta una tabla para cada dominio.

TABLA-11: Puntos de máxima concentración y depositación (PMI) - Escenario de

Operación (Dominio Costa)

|Puntos de Máximo Impacto (PMI) - Fase Operación (Dominio Costa)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Parámetro**|**Tipo de norma**|**Coordenadas UTM**<br>**WGS84 Huso 19S**|**Coordenadas UTM**<br>**WGS84 Huso 19S**|**PMI**|**Unidad**|**ID**|
|**Parámetro**|**Tipo de norma**|**Este [m]**<br>|**Norte [m]**<br>|**Norte [m]**<br>|**Norte [m]**<br>|**Norte [m]**<br>|
|MPS|Promedio anual|358.704 <br>|7.387.845 <br>|0,85|mg/m2-día|PMD 1|
|MPS|Promedio Mensual|358.704 <br>|7.387.845 <br>|1,04|mg/m2-día|PMD 1|
|MP10|Promedio anual|371.716 <br>|7.388.962 <br>|1,29|μg/m3|PMC 1|
|MP10|P98 diario|357.601 <br>|7.398.791 <br>|4,51|μg/m3|PMC 2|
|MP2,5|Promedio anual|371.716 <br>|7.388.962 <br>|1,29|μg/m3|PMC 1|
|MP2,5|P98 diario|357.601 <br>|7.398.791 <br>|3,95|μg/m3|PMC 2|
|SO2|Promedio anual|357.601 <br>|7.398.791 <br>|0,09|μg/m3|PMC 2|
|SO2|P99 diario|357.601 <br>|7.398.791 <br>|0,44|μg/m3|PMC 2|
|SO2|P98,5 horario|357.601 <br>|7.398.791 <br>|1,93|μg/m3|PMC 2|
|SO2|P99,7 diario|357.601 <br>|7.398.791 <br>|0,09|μg/m3|PMC 2|
|SO2|P99,73 horario|357.601 <br>|7.398.791 <br>|0,53|μg/m3|PMC 2|
|NO2|Promedio anual|357.601 <br>|7.398.791 <br>|2,44|μg/m3|PMC 2|
|NO2|P99 horario|371.716 <br>|7.388.962 <br>|3,30|μg/m3|PMC 1|
|CO|P99 horario|353.237 <br>|7.437.597 <br>|85,88|μg/m3|PMC 3|
|CO|P99 8 horas|357.601|7.398.791|181,54|μg/m3|PMC 2|

Fuente: JIA, 2022.

32
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA-12: Puntos de máxima concentración y depositación (PMI) - Escenario de

Operación (Dominio Interior)

|Puntos de Máximo Impacto (PMI) - Fase Operación (Dominio Interior)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Parámetro**|**Tipo de norma**|**Coordenadas UTM**<br>**WGS84 Huso 19S**|**Coordenadas UTM**<br>**WGS84 Huso 19S**|**PMI**|**Unidad**|**ID**|
|**Parámetro**|**Tipo de norma**|**Este [m]**|**Norte [m]**|**Norte [m]**|**Norte [m]**|**Norte [m]**|
|MPS|Promedio anual|386.613|7.373.018|0,96|mg/m2-día|PMD 1|
|MPS|Promedio Mensual|386.613|7.373.018|1,12|mg/m2-día|PMD 1|
|MP10|Promedio anual|428.758|7.355.280|1,67|μg/m3|PMC 1|
|MP10|P98 diario|428.758|7.355.280|3,79|μg/m3|PMC 1|
|MP2,5|Promedio anual|428.758|7.355.280|1,68|μg/m3|PMC 1|
|MP2,5|P98 diario|428.758|7.355.280|3,80|μg/m3|PMC 1|
|SO2|Promedio anual|428.758|7.355.280|0,05|μg/m3|PMC 1|
|SO2|P99 diario|428.758|7.355.280|0,13|μg/m3|PMC 1|
|SO2|P98,5 horario|428.758|7.355.280|0,63|μg/m3|PMC 1|
|SO2|P99,7 diario|428.758|7.355.280|0,05|μg/m3|PMC 1|
|SO2|P99,73 horario|428.758|7.355.280|0,15|μg/m3|PMC 1|
|NO2|Promedio anual|428.758|7.355.280|0,97|μg/m3|PMC 1|
|NO2|P99 horario|428.758|7.355.280|4,24|μg/m3|PMC 1|
|CO|P99 horario|428.758|7.355.280|89,20|μg/m3|PMC 1|
|CO|P99 8 horas|428.758|7.355.280|68,75|μg/m3|PMC 1|

Fuente: JIA, 2022.

En el Apéndice 2 se presenta la representación gráfica de cada uno de los puntos de máxima
concentración.

33
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**6.2.** **RESULTADOS DE LA MODELACIÓN**

Los resultados de la modelación para cada uno de los parámetros modelados, de acuerdo
con los estadísticos definidos en las normas primarias y secundarias calidad del aire
evaluadas para cada escenario, se presentan a continuación. Cabe señalar que, en base a lo
recomendado en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, se realizó
un Análisis de Incertidumbre, el cual se encuentra en el numeral 4.3, sin embargo para el
presente modelo, no es necesario aplicar un factor de corrección, debido a que el modelo
meteorológico sobreestimaría las concentraciones modeladas, como se explica
detalladamente en dicho numeral, por lo que las concentraciones obtenidas en el modelo
corresponden a las evaluadas.

34
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**6.2.1.** **Escenario Construcción**

**6.2.1.1.** **Receptores de Interés Primario**

A continuación, se presentan los resultados modelados en los receptores de interés primario descritos anteriormente.

TABLA-13: Aportes del Proyecto Receptores Primarios - Escenario Construcción

|ID|Receptor|MP [μg/m3]<br>10|Col4|MP [μg/m3]<br>2,5|Col6|SO [μg/m3]<br>2|Col8|Col9|NO [μg/m3]<br>2|Col11|CO[μg/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|**Norma**|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_1 <br>|Estación La Negra<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_2 <br>|Estación monitora Antofagasta<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_3 <br>|Estación monitora Juan José Latorre<br>|0|0|0|0|0|0|0|0|0|0|1|
|R_4 <br>|Estación monitora Jardín Infantil Integra<br>|0|0|0|0|0|0|0|0|0|0|1|
|R_5 <br>|R01<br>|0|1|0|0|0|0|0|0|6|5|35|
|R_6 <br>|R02<br>|0|0|0|0|0|0|0|0|1|1|7|
|R_7 <br>|R03<br>|0|0|0|0|0|0|0|0|1|1|3|
|R_8 <br>|R05<br>|0|0|0|0|0|0|0|0|1|1|3|
|R_9|R06|4|13|1|3|0|1|5|1|30|28|88|
|R_10 <br>|R07<br>|1|2|0|1|0|1|3|0|17|8|41|
|R_11 <br>|R09<br>|1|4|0|2|0|0|0|0|11|23|60|
|R_12 <br>|R08<br>|0|0|0|0|0|0|0|0|3|3|12|
|R_13 <br>|RC1<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_14 <br>|RC2<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_15 <br>|RC3<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_16 <br>|RC4<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_17 <br>|RC5<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_18 <br>|RC6<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_32 <br>|AINA<br>|0|0|0|0|0|0|0|0|1|1|5|
|R_33|Altos de la Portada|0|0|0|0|0|0|0|0|1|1|4|

35
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|ID|Receptor|MP [μg/m3]<br>10|Col4|MP [μg/m3]<br>2,5|Col6|SO [μg/m3]<br>2|Col8|Col9|NO [μg/m3]<br>2|Col11|CO[μg/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|**Norma**<br>|**Norma**<br>|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_34 <br>|ASAIA<br>|0|0|0|0|0|0|0|0|0|0|0|
|R_35 <br>|RX<br>|2|5|0|1|0|0|1|0|13|15|63|
|R_36|Estación Monitora La Negra|0|0|0 <br>|0 <br>|0|0|0|0|0|0|0|

Fuente: JIA, 2022.

**6.2.1.2.** **Receptores de Interés Secundario**

A continuación, se presentan los resultados modelados en los receptores de interés secundario descritos anteriormente.

TABLA-14: Aportes del Proyecto Receptores Secundarios - Escenario Construcción

|ID|Receptor|MPS [mg/m2dia]|Col4|SO [μg/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|**Norma**|**Norma**|**100**|**150**|**80**|**365**|**1.000**|
|R_19|G1|0|0|0|0|1|
|R_20|G2|0|0|0|0|0|
|R_21|G3|0|0|0|0|0|
|R_22|G4|0|0|0|0|0|
|R_23|G5|0|0|0|0|0|
|R_24|G6|0|0|0|0|0|
|R_25|G7|0|0|0|0|0|
|R_26|G8|0|0|0|0|0|
|R_27|G9|0|0|0|0|0|
|R_28|G10|0|0|0|0|0|
|R_29|G11|0|0|0|0|0|
|R_30|G12|0|0|0|0|0|
|R_31|G13|0|0|0|0|0|
|R_32|AINA|0|0|0|0|0|

36
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|ID|Receptor|MPS [mg/m2dia]|Col4|SO [μg/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|**Norma**|**Norma**|**100**|**150**|**80**|**365**|**1.000**|
|R_33|Altos de la Portada|0|0|0|0|0|
|R_34|ASAIA|0|0 <br>|0 <br>|0|0|

Fuente: JIA, 2022.

**6.2.2.** **Escenario Operación**

**6.2.2.1.** **Receptores de Interés Primario**

A continuación, se presentan los resultados modelados en los receptores de interés primario descritos anteriormente.

TABLA-15: Aportes del Proyecto Receptores Primarios - Escenario Operación

|ID|Receptor|MP [μg/m3]<br>10|Col4|MP [μg/m3]<br>2,5|Col6|SO [μg/m3]<br>2|Col8|Col9|NO [μg/m3]<br>2|Col11|CO[μg/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|**Norma**|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_1|Estación La Negra|0|0|0|0|0|0|0|0|3|5|12|
|R_2|Estación monitora Antofagasta|0|1|0|1|0|0|0|1|8|8|35|
|R_3|Estación monitora Juan José Latorre|0|0|0|0|0|0|0|0|1|2|6|
|R_4|Estación monitora Jardín Infantil Integra|0|0|0|0|0|0|0|0|1|1|6|
|R_5|R01|0|1|0|1|0|0|0|1|51|73|410|
|R_6|R02|0|1|0|1|0|0|0|0|16|26|160|
|R_7|R03|0|0|0|0|0|0|0|0|6|14|50|
|R_8|R05|0|0|0|0|0|0|0|0|4|9|29|
|R_9|R06|2|5|1|4|0|0|2|4|87|216|547|
|R_10|R07|0|1|0|1|0|0|0|1|27|46|173|
|R_11|R09|1|3|1|3|0|0|2|2|69|219|438|
|R_12|R08|0|0|0|0|0|0|0|0|13|27|82|

37
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|ID|Receptor|MP [μg/m3]<br>10|Col4|MP [μg/m3]<br>2,5|Col6|SO [μg/m3]<br>2|Col8|Col9|NO [μg/m3]<br>2|Col11|CO[μg/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|**Norma**|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_13|RC1|0|0|0|0|0|0|0|0|2|2|7|
|R_14|RC2|1|2|1|2|0|0|0|3|68|58|198|
|R_15|RC3|0|0|0|0|0|0|0|0|11|6|43|
|R_16|RC4|0|1|0|1|0|0|0|1|13|13|47|
|R_17|RC5|0|1|0|1|0|0|0|1|11|16|43|
|R_18|RC6|0|1|0|1|0|0|0|1|16|14|79|
|R_32|AINA|0|1|0|1|0|0|0|0|11|23|56|
|R_33|Altos de la Portada|0|1|0|1|0|0|0|0|12|24|54|
|R_34|ASAIA|0|0|0|0|0|0|0|0|1|2|7|
|R_35|RX|1|3|1|3|0|0|1|3|74|128|447|
|R_36|Estación Monitora La Negra|0|0|0|0|0|0|0|0|3|4|9|

Fuente: JIA, 2022.

**6.2.2.2.** **Receptores de Interés Secundario**

A continuación, se presentan los resultados modelados en los receptores de interés secundario descritos anteriormente.

TABLA-16: Aportes del Proyecto Receptores Secundarios - Escenario Operación

|ID|Receptor|MPS [mg/m2dia]|Col4|SO [μg/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|**Norma**|**Norma**|**100**|**150**|**80**|**365**|**1.000**|
|R_19|G1|0|0|0|0|0|
|R_20|G2|0|0|0|0|0|
|R_21|G3|0|0|0|0|0|
|R_22|G4|0|0|0|0|0|
|R_23|G5|0|0|0|0|0|
|R_24|G6|0|0|0|0|0|

38
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|ID|Receptor|MPS [mg/m2dia]|Col4|SO [μg/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|**Norma**|**Norma**|**100**|**150**|**80**|**365**|**1.000**|
|R_25|G7|0|0|0|0|0|
|R_26|G8|0|0|0|0|0|
|R_27|G9|0|0|0|0|0|
|R_28|G10|0|0|0|0|0|
|R_29|G11|0|0|0|0|0|
|R_30|G12|0|0|0|0|0|
|R_31|G13|0|0|0|0|0|
|R_32|AINA|0|0|0|0|0|
|R_33|Altos de la Portada|0|0|0|0|0|
|R_34|ASAIA|0|0|0|0|0|

Fuente: JIA, 2022.

39
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**6.3.** **MAPAS DE ISOCONCENTRACIONES**

En el Apéndice 2 del presente documento se encuentran los mapas de isoconcentraciones
de todos los estadísticos normados para MPS, MP 10, MP 2,5, SO 2, NO 2 y CO de los escenarios
de Construcción y Operación. Para este último escenario, se presentan los mapas tanto para
los dominios interior y costa.

**7.** **CUMPLIMIENTO DE NORMATIVA**

**7.1.** **EVALUACIÓN APORTES EN RECEPTORES**

A continuación, se presentan las tablas de evaluación normativa para cada parámetro
modelado, en las cuales se comparan los aportes del Proyecto, considerando las fuentes y
las tasas de emisión detalladas en las secciones 5.2.1 y 5.2.2,en los receptores discretos
considerados con la normativa, presentando en estas el porcentaje respecto a la norma de
cada aporte.

40
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**7.1.1.** **Escenario Construcción**

**7.1.1.1.** **Receptores de Interés Primario**

En la siguiente tabla se presentan los porcentajes respecto a la norma de los aportes en los receptores de interés primario para el
Escenario de Construcción, donde se puede observar que el receptor con mayor aporte corresponde al R06, el cual para material
particulado alcanza el 10% de la norma Percentil 98 Diario de MP 10 y para gases el mayor aporte respecto a la norma corresponde a
7,5% de la norma Percentil 99 Horario de NO 2 .

TABLA-17: Porcentaje Respecto a la Norma de Aportes del Proyecto en Receptores Primarios - Escenario Construcción

|ID|Receptor|MP [μg/m3]<br>10|Col4|MP [μg/m3]<br>2,5|Col6|SO [μg/m3]<br>2|Col8|Col9|NO [μg/m3]<br>2|Col11|CO[μg/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|**Norma**|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_1 <br>|Estación La Negra<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_2 <br>|Estación monitora Antofagasta<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_3 <br>|Estación monitora Juan José Latorre<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_4 <br>|Estación monitora Jardín Infantil Integra<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_5 <br>|R01<br>|0,0%|0,8%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|1,5%|0,1%|0,1%|
|R_6 <br>|R02<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,3%|0,0%|0,0%|
|R_7 <br>|R03<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,3%|0,0%|0,0%|
|R_8 <br>|R05<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,3%|0,0%|0,0%|
|R_9|R06|8,0%|10,0%|5,0%|6,0%|0,0%|0,7%|1,4%|1,0%|7,5%|0,3%|0,3%|
|R_10 <br>|R07<br>|2,0%|1,5%|0,0%|2,0%|0,0%|0,7%|0,9%|0,0%|4,3%|0,1%|0,1%|
|R_11 <br>|R09<br>|2,0%|3,1%|0,0%|4,0%|0,0%|0,0%|0,0%|0,0%|2,8%|0,2%|0,2%|
|R_12 <br>|R08<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,8%|0,0%|0,0%|
|R_13 <br>|RC1<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_14 <br>|RC2<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_15 <br>|RC3<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_16 <br>|RC4<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_17|RC5|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|

41
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|ID|Receptor|MP [μg/m3]<br>10|Col4|MP [μg/m3]<br>2,5|Col6|SO [μg/m3]<br>2|Col8|Col9|NO [μg/m3]<br>2|Col11|CO[μg/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|**Norma**<br>|**Norma**<br>|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_18 <br>|RC6<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_32 <br>|AINA<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,3%|0,0%|0,0%|
|R_33 <br>|Altos de la Portada<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,3%|0,0%|0,0%|
|R_34 <br>|ASAIA<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_35 <br>|RX<br>|4,0%|3,8%|0,0%|2,0%|0,0%|0,0%|0,3%|0,0%|3,3%|0,2%|0,2%|
|R_36|Estación Monitora La Negra|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|

Fuente: JIA, 2022.

**7.1.1.2.** **Receptores de Interés Secundario**

En la siguiente tabla se presentan los porcentajes respecto a la norma de los aportes en los receptores de interés secundario para el
Escenario de Construcción, donde se puede observar que el receptor G1 es el único que posee un aporte correspondiente al 0,1% de
la normativa Percentil 99,73 Horario de SO 2 .

TABLA-18: Porcentaje Respecto a la Norma de Aportes del Proyecto en Receptores Secundarios - Escenario Construcción

|ID|Receptor|MPS [mg/m2dia]|Col4|SO [μg/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|**Norma**|**Norma**|**100**|**150**|**80**|**365**|**1.000**|
|R_19|G1|0,0%|0,0%|0,0%|0,0%|0,1%|
|R_20|G2|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_21|G3|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_22|G4|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_23|G5|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_24|G6|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_25|G7|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_26|G8|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_27|G9|0,0%|0,0%|0,0%|0,0%|0,0%|

42
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|ID|Receptor|MPS [mg/m2dia]|Col4|SO [μg/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|**Norma**|**Norma**|**100**|**150**|**80**|**365**|**1.000**|
|R_28|G10|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_29|G11|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_30|G12|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_31|G13|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_32|AINA|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_33|Altos de la Portada|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_34|ASAIA|0,0%|0,0%|0,0%|0,0%|0,0%|

Fuente: JIA, 2022.

**7.1.2.** **Escenario Operación**

**7.1.2.1.** **Receptores de Interés Primario**

En la siguiente tabla, se presentan los porcentajes respecto a la norma de los aportes en los receptores de interés primario para el
Escenario de Operación, donde se puede observar que el receptor con mayor aporte corresponde al R06, el cual para material
particulado alcanza el 8% de la norma Percentil 98 Diario de MP 10 y para gases el mayor aporte respecto a la norma corresponde a
21,8% de la norma Percentil 99 Horario de NO 2 .

TABLA-19: Porcentaje Respecto a la Norma de Aportes del Proyecto en Receptores Primarios - Escenario Operación

|ID|Receptor|MP [μg/m3]<br>10|Col4|MP [μg/m3]<br>2,5|Col6|SO [μg/m3]<br>2|Col8|Col9|NO [μg/m3]<br>2|Col11|CO[μg/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|**Norma**|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_1 <br>|Estación La Negra<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,8%|0,1%|0,0%|
|R_2 <br>|Estación monitora Antofagasta<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|1,0%|2,0%|0,1%|0,1%|
|R_3 <br>|Estación monitora Juan José Latorre<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,3%|0,0%|0,0%|
|R_4|Estación monitora Jardín Infantil Integra|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,3%|0,0%|0,0%|

43
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|ID|Receptor|MP [μg/m3]<br>10|Col4|MP [μg/m3]<br>2,5|Col6|SO [μg/m3]<br>2|Col8|Col9|NO [μg/m3]<br>2|Col11|CO[μg/m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99 8**<br>**hrs.**|**P99**<br>**Horario**|
|**Norma**<br>|**Norma**<br>|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**100**|**400**|**10.000**|**30.000**|
|R_5 <br>|R01<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|1,0%|12,8%|0,7%|1,4%|
|R_6 <br>|R02<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|0,0%|4,0%|0,3%|0,5%|
|R_7 <br>|R03<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|1,5%|0,1%|0,2%|
|R_8 <br>|R05<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|1,0%|0,1%|0,1%|
|R_9|R06|4,0%|3,8%|5,0%|8,0%|0,0%|0,0%|0,6%|4,0%|21,8%|2,2%|1,8%|
|R_10 <br>|R07<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|1,0%|6,8%|0,5%|0,6%|
|R_11 <br>|R09<br>|2,0%|2,3%|5,0%|6,0%|0,0%|0,0%|0,6%|2,0%|17,3%|2,2%|1,5%|
|R_12 <br>|R08<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|3,3%|0,3%|0,3%|
|R_13 <br>|RC1<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,5%|0,0%|0,0%|
|R_14 <br>|RC2<br>|2,0%|1,5%|5,0%|4,0%|0,0%|0,0%|0,0%|3,0%|17,0%|0,6%|0,7%|
|R_15 <br>|RC3<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|2,8%|0,1%|0,1%|
|R_16 <br>|RC4<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|1,0%|3,3%|0,1%|0,2%|
|R_17 <br>|RC5<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|1,0%|2,8%|0,2%|0,1%|
|R_18 <br>|RC6<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|1,0%|4,0%|0,1%|0,3%|
|R_32 <br>|AINA<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|0,0%|2,8%|0,2%|0,2%|
|R_33 <br>|Altos de la Portada<br>|0,0%|0,8%|0,0%|2,0%|0,0%|0,0%|0,0%|0,0%|3,0%|0,2%|0,2%|
|R_34 <br>|ASAIA<br>|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,3%|0,0%|0,0%|
|R_35 <br>|RX<br>|2,0%|2,3%|5,0%|6,0%|0,0%|0,0%|0,3%|3,0%|18,5%|1,3%|1,5%|
|R_36|Estación Monitora La Negra|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,8%|0,0%|0,0%|

Fuente: JIA, 2022.

**7.1.2.2.** **Receptores de Interés Secundario**

En la siguiente tabla se presentan los porcentajes respecto a la norma de los aportes en los receptores de interés secundario para el
Escenario de Operación, donde se puede observar que en ningún receptor de carácter secundario se presenta un aporte significativo.

44
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA-20: Porcentaje Respecto a la Norma de Aportes del Proyecto en Receptores Secundarios - Escenario Operación

|ID|Receptor|MPS [mg/m2dia]|Col4|SO [μg/m3]<br>2|Col6|Col7|
|---|---|---|---|---|---|---|
|**ID**|**Receptor**|**Media Anual**|**Media Mensual**|**Media Anual**|**P99.7 Diario**|**P99.73 Horario**|
|**Norma**|**Norma**|**100**|**150**|**80**|**365**|**1.000**|
|R_19|G1|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_20|G2|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_21|G3|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_22|G4|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_23|G5|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_24|G6|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_25|G7|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_26|G8|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_27|G9|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_28|G10|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_29|G11|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_30|G12|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_31|G13|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_32|AINA|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_33|Altos de la Portada|0,0%|0,0%|0,0%|0,0%|0,0%|
|R_34|ASAIA|0,0%|0,0%|0,0%|0,0%|0,0%|

Fuente: JIA, 2022.

45
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**7.2.** **EVALUACIÓN APORTES EN ESTACIONES DE MONITOREO**

Para la presente sección, se toman en cuenta las estaciones evaluadas en la línea base de
calidad del aire (Anexo C2-16). Particularmente, la evaluación normativa se realiza sumando
los Aportes del Proyecto en la estación de calidad del aire (AP) y la Línea Base (LB). En este
último aporte, se toman en cuenta las mediciones de la estación y el aporte de otros
proyectos aprobados cuyos aportes no se encuentran incluidos en las mediciones de la
estación (sinergia), como fue analizado en el numeral 1.6 del Anexo C2-16 “Caracterización
Ambiental Calidad del Aire”.

46
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**7.3.** **ESCENARIO CONSTRUCCIÓN**

En las tablas presentadas a continuación, se muestra la evaluación normativa en las estaciones de calidad del aire incluidas en el presente
estudio, para el Escenario Construcción, donde se evidencia que los aportes del Proyecto a las estaciones son nulos, por lo que no se
provoca un aumento en las estaciones que lleve a un estado de saturación o latencia de éstas. Respecto a Estación La Negra, los
estadísticos de MP 10 se encuentran sobre norma (saturados), sin embargo, esto se debe a que la situación base de la estación posee
esta condición, siendo los aportes del Proyecto a ésta nulos, como ya se mencionó anteriormente, no afectando la calidad del aire del
sector para este parámetro.

TABLA-21: Calidad del aire futura para Estación Antofagasta - Escenario Construcción

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|Antofagasta|MP10 <br>[μg/m3]|P98 Diario|0|60|60|130|46%|
|Antofagasta|MP10 <br>[μg/m3]|Promedio Anual|0|33|33|50|66%|
|Antofagasta|MP2,5 <br>[μg/m3]|P98 Diario|0|24|24|50|48%|
|Antofagasta|MP2,5 <br>[μg/m3]|Promedio Anual|0|11|11|20|55%|
|Antofagasta|SO2 <br>[μg/m3]|P98,5 Horario|0|3|3|350|1%|
|Antofagasta|SO2 <br>[μg/m3]|P99 Diario|0|3|3|150|2%|
|Antofagasta|SO2 <br>[μg/m3]|Promedio Anual|0|3|3|60|5%|
|Antofagasta|SO2 <br>[μg/m3]|P99,73 Horario|0|3|3|1.000|0%|
|Antofagasta|SO2 <br>[μg/m3]|P99,7 Diario|0|3|3|365|1%|
|Antofagasta|SO2 <br>[μg/m3]|Promedio Anual|0|3|3|80|4%|

Fuente: JIA, 2022.

47
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA-22: Calidad del aire futura para Estación La Negra - Escenario Construcción

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|La Negra|MP10 <br>[μg/m3]|P98 Diario|0|149|149|130|115%|
|La Negra|MP10 <br>[μg/m3]|Promedio Anual|0|64|64|50|128%|
|La Negra|MP2,5 <br>[μg/m3]|P98 Diario|0|26|26|50|52%|
|La Negra|MP2,5 <br>[μg/m3]|Promedio Anual|0|12|12|20|60%|
|La Negra|SO2 <br>[μg/m3]|P98,5 Horario|0|46|46|350|13%|
|La Negra|SO2 <br>[μg/m3]|P99 Diario|0|46|46|150|31%|
|La Negra|SO2 <br>[μg/m3]|Promedio Anual|0|8|8|60|13%|
|La Negra|SO2 <br>[μg/m3]|P99,73 Horario|0|93|93|1.000|9%|
|La Negra|SO2 <br>[μg/m3]|P99,7 Diario|0|43|43|365|12%|
|La Negra|SO2 <br>[μg/m3]|Promedio Anual|0|8|8|80|10%|
|La Negra|NO2 <br>[μg/m3]|P99 Horario|0|66|66|400|17%|
|La Negra|NO2 <br>[μg/m3]|Promedio Anual|0|11|11|100|11%|

Fuente: JIA, 2022.

TABLA-23: Calidad del aire futura para Estación Jardín Infantil Integra - Escenario Construcción

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|Jardín Infantil Integra|NO2 <br>[μg/m3]|P99 Horario|0|52|52|400|13%|
|Jardín Infantil Integra|NO2 <br>[μg/m3]|Promedio Anual<br>|0 <br>|6|6|100|6%|

Fuente: JIA, 2022.

48
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA-24: Calidad del aire futura para Estación Juan José Latorre - Escenario Construcción

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|Jardín Infantil Integra|NO2 <br>[μg/m3]|P99 Horario|0|46|46|400|12%|
|Jardín Infantil Integra|NO2 <br>[μg/m3]|Promedio Anual|0|6|6|100|6%|

Fuente: JIA, 2022.

**7.4.** **ESCENARIO OPERACIÓN**

A las tablas presentadas a continuación, se muestra la evaluación normativa en las estaciones de calidad del aire incluidas en el presente
estudio para el Escenario Operación, donde se evidencia que los aportes del Proyecto a las estaciones son nulos, a excepción de los
estadísticos diarios de material particulado para la Estación Antofagasta y el estadístico horario de NO 2 para las Estaciones La Negra,
Jardín Infantil Integral y Juna José Latorre, que poseen bajos aportes que no superan los 3 μg/m [3] . En base a lo mencionado, se evidencia
que no se provoca un aumento en las estaciones que lleve a un estado de saturación o latencia de las estaciones evaluadas. Respecto
a Estación La Negra, al igual que se mencionó para el Escenario de Construcción, los estadísticos de MP 10 se encuentran sobre norma
(saturados), sin embargo, esto se debe a que la situación base de la estación posee esta condición, siendo los aportes del Proyecto a
esta nulos, no afectando la calidad del aire del sector para este parámetro.

TABLA-25: Calidad del aire futura para Estación Antofagasta - Escenario Operación

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|Antofagasta|MP10 <br>[μg/m3]|P98 Diario|1|60|61|130|47%|
|Antofagasta|MP10 <br>[μg/m3]|Promedio Anual|0|33|33|50|66%|
|Antofagasta|MP2,5 <br>[μg/m3]|P98 Diario|1|24|25|50|50%|
|Antofagasta|MP2,5 <br>[μg/m3]|Promedio Anual|0|11|11|20|55%|
|Antofagasta|SO2 <br>[μg/m3]|P98,5 Horario|0|3|3|350|1%|
|Antofagasta|SO2 <br>[μg/m3]|P99 Diario|0|3|3|150|2%|
|Antofagasta|SO2 <br>[μg/m3]|Promedio Anual|0|3|3|60|5%|

49
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|||P99,73 Horario|0|3|3|1.000|0%|
|||P99,7 Diario|0|3|3|365|1%|
|||Promedio Anual|0|3|3|80|4%|

Fuente: JIA, 2022.

TABLA-26: Calidad del aire futura para Estación La Negra - Escenario Operación

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|La Negra|MP10 <br>[μg/m3]|P98 Diario|0|149|149|130|115%|
|La Negra|MP10 <br>[μg/m3]|Promedio Anual|0|64|64|50|128%|
|La Negra|MP2,5 <br>[μg/m3]|P98 Diario|0|26|26|50|52%|
|La Negra|MP2,5 <br>[μg/m3]|Promedio Anual|0|12|12|20|60%|
|La Negra|SO2 <br>[μg/m3]|P98,5 Horario|0|46|46|350|13%|
|La Negra|SO2 <br>[μg/m3]|P99 Diario|0|46|46|150|31%|
|La Negra|SO2 <br>[μg/m3]|Promedio Anual|0|8|8|60|13%|
|La Negra|SO2 <br>[μg/m3]|P99,73 Horario|0|93|93|1.000|9%|
|La Negra|SO2 <br>[μg/m3]|P99,7 Diario|0|43|43|365|12%|
|La Negra|SO2 <br>[μg/m3]|Promedio Anual|0|8|8|80|10%|
|La Negra|NO2 <br>[μg/m3]|P99 Horario|3|66|69|400|17%|
|La Negra|NO2 <br>[μg/m3]|Promedio Anual<br>|0 <br>|11|11|100|11%|

Fuente: JIA, 2022.

50
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

TABLA-27: Calidad del aire futura para Estación Jardín Infantil Integra - Escenario Operación

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|Jardín Infantil Integra|NO2 <br>[μg/m3]|P99 Horario|1|52|53|400|13%|
|Jardín Infantil Integra|NO2 <br>[μg/m3]|Promedio Anual|0|6|6|100|6%|

Fuente: JIA, 2022.

TABLA-28: Calidad del aire futura para Estación Juan José Latorre - Escenario Construcción

|Estación|Parámetro|Estadístico|Aportes del<br>Proyecto<br>(AP)|Línea de<br>Base (LB)|Total (AP+LB)|Norma|% AP+LB c/r<br>Norma|
|---|---|---|---|---|---|---|---|
|Juan José Latorre|NO2 <br>[μg/m3]|P99 Horario|1|46|47|400|12%|
|Juan José Latorre|NO2 <br>[μg/m3]|Promedio Anual|0|6|6|100|6%|

Fuente: JIA, 2022.

51
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**8.** **CONCLUSIONES**

De los resultados obtenidos en la modelación de dispersión de contaminantes,
correspondientes a los Escenarios de Construcción y Operación del Proyecto “ **Transporte**
**Ferroviario en Región de Antofagasta** ”, se obtiene lo siguiente:

 Para la modelación del Escenario Construcción, los aportes del Proyecto no superan
el 10% de la norma para MP 10 y MP 2,5 para todos sus estadísticos en puntos de interés
primarios, alcanzando este porcentaje en el receptor R06 para el Percentil 98 Diario
de MP 10 . Por otra parte, para el NO 2, CO y SO 2, los aportes en los receptores primarios
no superan el 7,5% de la norma, correspondiente al Percentil 99 Horario de NO 2 para
el receptor R06. Finalmente, para el MPS y SO 2 no se presentan aportes significativos
en los receptores secundarios, salvo en el receptor G1 para el estadístico Percentil
99,73 Horario, alcanzando el 0,1% de la norma.

 Para la modelación del Escenario Operación, los aportes del Proyecto no superan el
8% de la norma para MP 10 y MP 2,5 para todos sus estadísticos en puntos de interés
primarios, alcanzando este porcentaje en el receptor R06 para el Percentil 98 Diario
de MP 10 . Por otra parte, para el NO 2, CO y SO 2, los aportes en los receptores primarios
no superan el 21,8% de la norma, correspondiente al Percentil 99 Horario de NO 2
para el receptor R06. Finalmente, para el MPS y SO 2 no se presentan aportes
significativos en los receptores secundarios.

 - En base al análisis normativo de las estaciones de monitoreo de la suma de los

aportes con las líneas de base, considerando en esta última el aporte de otros
proyectos, se obtiene que, para la totalidad de estaciones de calidad del aire y puntos
de interés, no se superan las normas de calidad del aire primarias ni secundarias para
ninguna de las fases evaluadas del Proyecto.

Si bien la Estación La Negra exhibe porcentajes de superación de 115% y 128%
respecto de las normas diaria y anual de MP 10, respectivamente, esto se debe a que
su situación base ya posee esta condición, siendo los aportes de MP 10 del Proyecto
nulos a dicha estación, no afectando la calidad del aire del sector para este
parámetro.

En base a lo anteriormente señalado, se desprende que el Proyecto no generará un aporte
incremental significativo en las concentraciones ambientales de material particulado y/o
gases en los receptores y estaciones de calidad del aire evaluados con respecto a las normas
de calidad primaria y secundaria vigentes.

52
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE

**9.** **REFERENCIAS**

 Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (Servicio de Evaluación
Ambiental, 2012).

 Ley 19.300 del MINSEGPRES que Aprueba Ley Sobre Bases Generales Del Medio
Ambiente.

 D. S. N°40/2012 del MMA que Aprueba el Reglamento del Sistema de Evaluación de
Impacto Ambiental.

 D. S. N°12/2022 del MMA que Establece Norma Primaria De Calidad Ambiental Para
Material Particulado Respirable MP10.

 D.S. N°12/2011 del MMA que Establece Norma Primaria De Calidad Ambiental Para
Material Particulado Fino Respirable MP 2,5

 D.S. N°114/2002 del MINSEGPRES que Establece Norma Primaria De Calidad De Aire
Para Dióxido De Nitrógeno (NO2).

 D.S. N°104/2019 del MINSEGPRES que Establece Norma Primaria De Calidad De Aire
Para Dióxido De Azufre (SO2).

 D.S. N°115/2002 del MINSEGPRES que Establece Norma Primaria De Calidad De Aire
Para Monóxido De Carbono (CO).

 D.S. N°22/2009 del MINSEGPRES que Establece Norma De Calidad Secundaria De
Aire Para Anhídrido Sulfuroso (SO2).

 D.S. N°4/1992 del MINAGRI que Establece Norma de Calidad del Aire Para Material
Particulado Sedimentable en la Cuenca del Rio Huasco III Región,

 40 CFR Part 51, Revision to the Guideline on Air Quality Models: Adoption of a
Preferred General Purpose (Flat and Complex Terrain) Dispersion Model and Other
Revisions; Final Rule.

53
ANEXO C2-1 - MODELACIÓN CALIDAD DEL AIRE