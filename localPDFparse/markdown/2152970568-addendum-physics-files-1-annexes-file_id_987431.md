---
title: Sin título
author: p_reszczynski@jaimeillanes.cl
date: D:20211126003039-03'00'
language: es
type: report
pages: 21
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO AD-5.2-2
-->

# ANEXO AD-5.2-2

## MODELACIÓN CALIDAD DEL AIRE

### _Cliente:_

**ÍNDICE**

1. INTRODUCCIÓN ....................................................................................................................................... 1

2. OBJETIVO .................................................................................................................................................... 2

3. MARCO LEGAL .......................................................................................................................................... 2

4. METODOLOGIA ........................................................................................................................................ 3

4.1. BASE TEÓRICA DEL MODELO UTILIZADO ................................................................................ 3

4.2. CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN ....................................................... 3

4.3. ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF Y FACTOR

DE CORRECIÓN ................................................................................................................................ 5

5. PARÁMETROS DE ENTRADA DEL MODELO ................................................................................... 7

5.1. CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO ....................................................... 7

5.2. PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN ................ 7

5.3. ANALISIS DE INCERTIDUMBRE Y DETERMINACIÓN DEL FACTOR DE CORRECCIÓN

............................................................................................................................................................... 9

6. RESULTADOS ........................................................................................................................................... 10

6.1.1. LÍNEA DE BASE ............................................................................................................................. 10

6.1.2. PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC) ........................................................... 12

6.2. RESULTADOS DE LA MODELACIÓN ......................................................................................... 13

6.2.1. FASE DE OPERACIÓN ................................................................................................................ 13

6.2.2. ANÁLISIS DE SINERGIA CON PROYECTO COLINDANTE .............................................. 14

7. CUMPLIMIENTO DE NORMATIVA ................................................................................................... 15

8. CONCLUSIONES ..................................................................................................................................... 18

**APÉNDICES**

Apéndice AD-5.2-1: Archivos de Modelación

Apéndice AD-5.2-2 Isoconcentraciones Fase de Operación

ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

**TABLAS**

TABLA-1: Norma Primaria de Calidad del Aire MP 10 y MP 2,5, ........................................ 2

TABLA-2: Ubicación Receptores primarios y secundarios .............................................. 4

TABLA-3: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF

........................................................................................................................................... 4

TABLA-4: Tasas de Emisión del Escenario Fase de Operación [g/s-m [2] ] .................... 7

TABLA-5: Estadígrafos de ajuste de la modelación meteorológica ............................ 9

TABLA-6: Línea de Base de Calidad del Aire. ..................................................................... 10

TABLA-7: Punto de máxima concentración- Fase de Operación ............................... 12

TABLA-8: Aportes modelados en Receptores Primarios, Escenario de Fase de
Operación .................................................................................................................... 13

TABLA-9: Aportes modelados en Receptores Primarios, Proyecto “HyEx - Síntesis
de Amoniaco Verde”, Escenario de Fase de Construcción ....................... 14

TABLA-10: Aportes modelados en Receptores Primarios, Escenario de Sinergia .. 15

TABLA-11: Concentración total MP 10 [μg/m [3] N] y MP 2,5 [μg/m [3] ] y comparación con
normativa .................................................................................................................... 17

**FIGURAS**

FIGURA-1: Dominio de Modelación (Computacional Grid), fuentes emisoras y
receptores discretos. Fase de Operación. ......................................................... 8

FIGURA-2: Frecuencia relativa de la dirección del viento observada y modelada
(WRF). Estación Tres Marías.................................................................................... 9

ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

**1.** **INTRODUCCIÓN**

En el marco de la Adenda del Proyecto “’ **HyEx** - **Producción de Hidrógeno Verde** ” (en
adelante el Proyecto), el presente informe da cuenta del análisis del transporte y dispersión
de contaminantes particulados emitidos por la fase de operación de éste, señalados en el
Anexo C1-3 de la DIA del Proyecto, ubicado aproximadamente a 15 kilómetros en línea recta
de la ciudad de Tocopilla. Cabe señalar que solo se consideró la modelación de los
contaminantes MP 10 y MP 2,5, dado que el Proyecto se encuentra ubicado en una zona
cercana a la ciudad de Tocopilla, zona declarada como saturada por MP 10 en su norma anual
(D.S. No50/2007 de MINSEGPRES).

La simulación de los aportes del Proyecto a las concentraciones ambientales se realiza
mediante la aplicación del sistema de modelación WRF/CALPUFF; sistema que considera la
utilización de la modelación meteorológica para el año 2020 (WRF), un dominio
computacional de modelación de CALPUFF de 50x31 [km] con una resolución de 1x1 [km],
la cual incluye como receptores las estaciones Tres Marías, Super Site, Gobernación y
Bomberos, todos receptores ubicados a aproximadamente 15 [km] al oeste del Proyecto.
Respecto de lo anterior, y de acuerdo con lo presentado en el Anexo C2-5 de la DIA, es
posible señalar que, al interior del Área de Influencia definida y sus proximidades, no se
identifican Áreas Protegidas bajo ninguna de las 11 categorías listadas.

En concordancia a lo señalado en la Guía para el uso de modelos de calidad del aire en el
SEIA, emitida por el Servicio de Evaluación Ambiental el año 2012, los resultados de la
modelación se entregan en tablas adecuadas, a modo de comparar los aportes del Proyecto
con y sin factor de corrección. Además, se comparan los resultados de la modelación
respecto de la línea de base y, a su vez, respecto de las normas de calidad del aire nacionales
(artículo 11 del D.S. N° 40/12 que aprueba el Reglamento del Sistema de Evaluación de
Impacto Ambiental -RSEIA-), de manera de evaluar el grado de cumplimiento normativo.

Finalmente, es relevante indicar que los archivos digitales de la modelación con el modelo
CALPUFF (entradas y salidas) fueron presentadas de manera digital acorde a lo indicado en
el Apéndice AD-5.2-2.

1
ANEXO AD-5.2-2 - MODELACIÓN CALIDAD DEL AIRE

**2.** **OBJETIVO**

Determinar el aporte incremental a las concentraciones ambientales de material particulado
que generará el Proyecto en su fase de operación en los receptores sensibles identificados,
y comparar dichos aportes con respecto a la línea base y las normas de calidad primaria.

**3.** **MARCO LEGAL**

Para determinar la existencia de los efectos, características o circunstancias de los literales
a), b) y d) del art. 11 de la Ley 19.300 en el área de influencia del Proyecto en su fase de
operación en el “peor escenario”, se ha considerado la normativa ambiental primaria y
secundaria de calidad de aire vigente para MP 10 y MP 2,5, presentadas en la tabla a
continuación:

TABLA-1: Norma Primaria de Calidad del Aire MP 10 y MP 2,5,

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**MP10 **|D.S. N°59/98<br>MINSEGPRES,<br>modificada por D.S.<br>N°45/01|Promedio aritmético de tres años calendario<br>consecutivos|50 μg/m3N|
|**MP10 **|D.S. N°59/98<br>MINSEGPRES,<br>modificada por D.S.<br>N°45/01|Percentil 98 de las concentraciones de 24 horas<br>registradas durante un período anual|150 μg/m3N|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Promedio tri-anual de las concentraciones<br>anuales|20 μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Percentil 98 de los promedios diarios registrados<br>durante un año|50 μg/m3|

2
ANEXO AD-5.2-2 - MODELACIÓN CALIDAD DEL AIRE

**4.** **METODOLOGIA**

La modelación se realizó acorde con la metodología descrita en la Guía para el uso de
modelos de calidad del aire en el SEIA (2012), en adelante la “Guía de modelación”. Se utilizó
el modelo numérico Weather Research and Forecasting (WRF) en la generación de datos
meteorológicos para el año 2020, y el modelo CALPUFF para la modelación de la dispersión
y transporte de las emisiones, en el escenario considerado.

**4.1.** **BASE TEÓRICA DEL MODELO UTILIZADO**

WRF es el modelo meteorológico recomendado en la Guía de modelación para la generación
de la grilla meteorológica. Este modelo genera una grilla tridimensional de campos de
viento, además de múltiples variables atmosféricas, a través de dominios anidados con una
resolución horizontal recomendada para el dominio de menor tamaño, de 1 kilómetro.

Por su parte, CALPUFF es un modelo de dispersión, transporte y deposición de
contaminantes atmosféricos de tipo puff lagrangiano-gaussiano, no estacionario,
recomendado por la Guía de modelación y también por la Agencia de Protección Ambiental
de Estados Unidos (US EPA su sigla en inglés) [1], el cual es aplicable a terrenos complejos y a
múltiples tipos de fuentes emisoras (puntuales, areales y volumétricas). CALPUFF realiza sus
cálculos tomando los datos meteorológicos superficiales y de la capa superior atmosférica,
incluyendo la posibilidad de modelar la dispersión de contaminantes primarios y
secundarios, obteniendo resultados confiables para distancias de hasta 100 [km].

El sistema de modelación incluye tres componentes principales: CALMET, CALPUFF y
CALPOST, además de una serie de programas de pre-procesamiento diseñados para la
preparación de la información meteorológica y geofísica, En este caso, no fue necesario
utilizar los pre-procesadores ni el módulo CALMET, ya que se emplearon los resultados de
la modelación meteorológica realizada con WRF.

CALPOST es un programa post-procesador que permite compilar los resultados de CALPUFF
creando los archivos según los estadísticos establecidos en las normas de calidad del aire
para la evaluación de los resultados.

**4.2.** **CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN**

Para que los procesos meteorológicos de mesoescala sean representados de una forma
adecuada, tanto por el modelo meteorológico como por el modelo de dispersión, se generó
un dominio de modelación de WRF/CALPUFF de 50x31 [km], en donde se consideraron las
características topográficas de la zona, las estaciones Tres Marías, Super Site, Gobernación y

1 40 CFR Part 51, Revision to the Guideline on Air Quality Models: Adoption of a Preferred General Purpose (Flat
and Complex Terrain) Dispersion Model and Other Revisions; Final Rule.
[http://www.epa.gov/ttn/scram/guidance/guide/appw_05.pdf](http://www.epa.gov/ttn/scram/guidance/guide/appw_05.pdf)

3
ANEXO AD-5.2-2 - MODELACIÓN CALIDAD DEL AIRE

Bomberos, todos receptores ubicados a aproximadamente 15 [km] al oeste del Proyecto, en
línea recta. Respecto de lo anterior y, como se detalla en los siguientes capítulos del presente
documento, es posible señalar que al interior del Área de Influencia definida y sus
proximidades, no se logran identificar Áreas Protegidas bajo ninguna de las 11 categorías
listadas.

TABLA-2: Ubicación Receptores primarios y secundarios

|ID|Nombre<br>Receptor|Tipo de<br>Receptor|Coordenadas UTM [m]<br>WGS 84 Huso 19S|Col5|Altura de<br>Elevación<br>Modelo<br>WRF<br>[m]|Coordenadas Datum<br>LCC [m] NWS84|Col8|
|---|---|---|---|---|---|---|---|
|**ID**|**Nombre**<br>**Receptor**|**Tipo de**<br>**Receptor**|**Este**|**Norte**|**Norte**|**Este**|**Norte**|
|**R_1**|**Bomberos**|Primario|375.319|7.554.741|110,38|-20163,43|7341,87|
|**R_2**|**Tres Marías**|Primario|377.485|7.560.029|99,61|-17965,78|12637,67|
|**R_3**|**Super Site**|Primario|377.404|7.557.193|126,79|-18065,44|9790,26|
|**R_4**|**Gobernación**|Primario|376.284|7.556.725|39,52|-19186,79|9327,77|

Fuente: Elaboración propia.

La ubicación de estos receptores se presenta en la figura 1.

Cabe señalar que la modelación meteorológica WRF fue realizada para el año 2020, de
acuerdo con la configuración definida por el SEA en su Guía de modelación: cuenta con una
resolución horizontal de 1 [km] y una resolución vertical de 10 niveles a 20, 40, 80, 160, 320,
640, 1.200, 2.000, 3.000 y 4.000 metros. En la tabla a continuación se señalan las coordenadas
de los vértices del dominio de modelación WRF/CALPUFF.

TABLA-3: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF

|Vértices|Coordenadas UTM [m] Datum: WGS-84, Huso: 19S|Col3|
|---|---|---|
|**Vértices**|**Este**|**Norte**|
|**SW**|370.512|7.522.533|
|**NE**|420.512|7.572.533|
|**NW**|370.512|7.572.533|
|**SE**|420.512|7.522.533|

Fuente: Elaboración propia.

4
ANEXO AD-5.2-2 - MODELACIÓN CALIDAD DEL AIRE

**4.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF Y**
**FACTOR DE CORRECIÓN**

La modelación atmosférica está basada en uno de los modelos de pronóstico meteorológico
más avanzados y completos disponibles [2], el cual cuenta con un gran número de
parametrizaciones que permiten, si son adecuadamente seleccionadas e implementadas,
simular gran parte de los procesos meteorológicos de mesoescala. Este modelo
corresponde, como ya se ha mencionado, al Weather Research and Forecasting (WRF). En el
caso del presente estudio, el modelo WRF utilizado ha sido parametrizado de acuerdo con
lo establecido por el SEA y corresponde al año 2020.

Sin embargo, e independiente de las bondades del modelo utilizado, todo modelo
atmosférico requiere ser calibrado y validado para cada condición meteorológica y de
terreno. En este punto es donde se tienen las mayores dificultades, dado que la incorrecta
implementación de alguna parametrización puede llevar a errores significativos en la
estimación de los vientos en superficie y con esto de las trayectorias de los contaminantes.

Para realizar el análisis de incertidumbre se han considerado las recomendaciones

establecidas en la Guía de modelación descritas en el acápite 7, donde menciona que
cualquier modelo representa una aproximación a la realidad y sus resultados tienen
incertidumbres asociadas, las cuales se expresan a través de diferencias entre lo estimado y
lo observado.

Cabe señalar que, a partir de la estación meteorológica más cercana se evaluaron los
estadígrafos meteorológicos recomendados por la US.EPA, que corresponden al BIAS
(sesgo) y al IOA (índice de ajustes), además de error cuadrático medio (RMSE) para la
velocidad [m/s] y la dirección del viento [°] entre los valores de la estación modelada a partir
del modelo meteorológico WRF utilizado y las observaciones de terreno disponibles para el
área a modelar, y sus resultados se presentan en la Tabla 9.

Luego del ajuste en las direcciones de viento, se calcula la frecuencia relativa del viento para
cada una de las direcciones seleccionadas respecto de la frecuencia total de las estas, tanto
para los datos observados como para los datos modelados. Por lo tanto, si se denomina _Xi_
a las frecuencias observadas de cada una de las direcciones de viento (i) y _Wi_ a las frecuencias
modeladas, entonces las frecuencias relativas observadas ( F obs ) corresponderán a las
calculadas de acuerdo con la ecuación 1:

F obs =

∑ 3i=1 X i X i Ecuación 1

Asimismo, las frecuencias relativas modeladas ( F WRF ), corresponderán a las calculadas de
acuerdo con la ecuación 2:

2 Numeral 5.3.2 Fuentes de Datos Meteorológicas. Guía para el uso de modelos de calidad del aire. SEA 2012.

5
ANEXO AD-5.2-2 - MODELACIÓN CALIDAD DEL AIRE

F WRF =

∑ 3i=1 W i W i Ecuación 2

De esta manera, al restar ambas frecuencias relativas obtenemos información respecto al
grado de subestimación o sobrestimación de las direcciones de viento que pueden favorecer
el transporte de los parámetros atmosféricos a modelar. En el caso de que la diferencia entre
lo observado y lo modelado sea mayor que cero, significaría que el modelo subestimó la
dirección que favorece el transporte de contaminantes. En dicho caso, se aplicó un factor de
corrección dado por la ecuación 3:

FC= 1 + [F obs −F WRF ] Ecuación 3

6
ANEXO AD-5.2-2 - MODELACIÓN CALIDAD DEL AIRE

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

En los siguientes acápites se presentan las tasas de emisión ingresadas al modelo del
escenario establecido, a saber, la fase de operación del Proyecto. El resumen de las emisiones
de cada una de las fuentes emisoras ingresadas al modelo, en unidades de [g/s-m [2] ], se
presentan en la Tabla a continuación.

TABLA-4: Tasas de Emisión del Escenario Fase de Operación [g/s-m [2] ]

|Tipo de Fuente|ID|Descripción|Emisiones [g/m2-s]|Col5|Área [m2]|Tiempo [s]|
|---|---|---|---|---|---|---|
|**Tipo de Fuente**|**ID**|**Descripción**|**MP10 **|**MP2,5 **|**MP2,5 **|**MP2,5 **|
|LINE_AREA|SRC_1|Ruta 1|3,75E-07|7,20E-08|169796|15768000|
|LINE_AREA|SRC_2|Ruta 2|3,55E-10|6,82E-11|365060|15768000|
|LINE_AREA|SRC_3|Ruta 3|3,56E-05|1,02E-05|44762|15768000|
|LINE_AREA|SRC_4|Ruta 4|3,55E-05|1,01E-05|24857|15768000|
|LINE_AREA|SRC_5|Ruta 5|2,91E-06|5,59E-07|1535|15768000|
|LINE_AREA|SRC_6|Ruta 6|2,24E-06|4,30E-07|2771|15768000|

Fuente: Elaboración propia.

A continuación, en la siguiente Figura se presenta la ubicación del dominio de modelación,
fuentes emisoras y receptores para la fase de operación:

7
ANEXO AD-5.2-2 - MODELACIÓN CALIDAD DEL AIRE

FIGURA-1: Dominio de Modelación (Computacional Grid), fuentes emisoras y receptores discretos.

Fase de Operación.

Fuente: Elaboración propia.

8
ANEXO AD-5.2-2 - MODELACIÓN CALIDAD DEL AIRE

**5.3.** **ANALISIS DE INCERTIDUMBRE Y DETERMINACIÓN DEL FACTOR DE**
**CORRECCIÓN**

En el Anexo C2-1 Caracterización Ambiental presentado en la DIA del Proyecto se analizaron
los datos disponibles para las estaciones Super Site y Tres Marías, siendo esta última la que
tiene una serie más completa para el año 2020, y que coincide con el año de valores
modelados. Por lo anterior, a partir de los datos meteorológicos disponibles de dicha
estación, se realizó un breve análisis estadístico, obteniendo los resultados presentados en
la tabla a continuación:

TABLA-5: Estadígrafos de ajuste de la modelación meteorológica

|Receptor|Variable|RMSE|BIAS|Bondad<br>BIAS|IOA|Bondad<br>IOA|
|---|---|---|---|---|---|---|
|Estación<br>Tres Marías|Dirección del<br>viento (°)|131,94|-0,46|<+-/10|0,37|--|
|Estación<br>Tres Marías|Velocidad del<br>viento (m/s)|1,60|0,98|<+-/0,5|0,56|>0,60|

Fuente: Elaboración propia.

De la tabla anterior, se desprende que la velocidad del viento, en el estadístico IOA, se
encuentra por sobre el rango de bondad.

De acuerdo a la metodología descrita en el numeral 4.3, se graficaron las frecuencias relativas
de las direcciones del viento que favorecen el transporte de los parámetros atmosféricos a
modelar, a modo de determinar los parámetros F WRF y F obs . El gráfico de las frecuencias
relativas señaladas se realizó tanto de los datos registrados en la estación de monitoreo,
como los datos modelados con WRF, lo cual se muestra a continuación:

FIGURA-2: Frecuencia relativa de la dirección del viento observada y modelada (WRF).

Estación Tres Marías

Fuente: Elaboración propia.

9
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

Como se puede observar en la Figura anterior, el modelo WRF subestima las direcciones con
componente sur y especialmente vientos desde el tercer cuadrante (SSW, SW y WSW). Dada
la posición del proyecto respecto de la estación considerada para el cálculo de análisis de
incertidumbre, hacia el suroeste desde dicha posición, se espera que la sobreestimación de
vientos desde el cuadrante mencionado por parte del modelo implique una sobreestimación
de las concentraciones calculadas en el sector de Tocopilla. Sin perjuicio de lo anterior, y
considerando la condición más desfavorable de cálculo, se ha la corrección la utilización de
un factor de corrección, con lo que se considerará la peor situación, que significa corregir
las concentraciones por 1,20, de acuerdo con la fórmula señalada en el acápite anterior.

**6.** **RESULTADOS**

A continuación, se presentan los aportes estimados de la Fase de Operación, para cada uno
de los parámetros modelados.

**6.1.1.** **LÍNEA DE BASE**

En la tabla siguiente se presenta un resumen de los registros basales de calidad del aire, los
cuales han sido obtenidos desde los documentos “Informe de Monitoreo de Calidad del
Aire, junio 2021” [ 3] para las estaciones “Bomberos”, “Tres Marías” y “Gobernación”, mientras
que en el caso de la estación “Super Site” los valores fueron obtenidos del documento
“Campaña de Monitoreo de Calidad del Aire y Meteorología, Estación Super Site, Localidad
Tocopilla, enero 2021” [ 4] :

TABLA-6: Línea de Base de Calidad del Aire.

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Línea de<br>Base (LB)|Límite<br>normado|Porcentaje<br>respecto<br>del límite|
|---|---|---|---|---|---|---|
|MP10|Bomberos|Primaria|24h P98|-|150|-|
|MP10|Bomberos|Primaria|Anual|-|50|-|
|MP10|Tres Marías|Tres Marías|24h P98|110|150|73%|
|MP10|Tres Marías|Tres Marías|Anual|45|50|90%|
|MP10|Super Site|Super Site|24h P98|61|150|41%|
|MP10|Super Site|Super Site|Anual|36|50|72%|
|MP10|Gobernación|Gobernación|24h P98|72|150|48%|
|MP10|Gobernación|Gobernación|Anual|38|50|76%|
|MP2,5|Bomberos|Primaria|24h P98|35|50|70%|
|MP2,5|Bomberos|Primaria|Anual|16|20|80%|

3
Disponible en WWW: [https://snifa.sma.gob.cl/General/DescargarInformeSeguimiento/290964. Último acceso: 5 de noviembre](https://snifa.sma.gob.cl/General/DescargarInformeSeguimiento/290964)
de 2021.

4
Disponible en WWW: [https://snifa.sma.gob.cl/General/DescargarInformeSeguimiento/274678. Último acceso: 5 de noviembre](https://snifa.sma.gob.cl/General/DescargarInformeSeguimiento/274678)
de 2021.

10
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Línea de<br>Base (LB)|Límite<br>normado|Porcentaje<br>respecto<br>del límite|
|---|---|---|---|---|---|---|
||Tres Marías||24h P98|25|50|49%|
||Tres Marías||Anual|16|20|80%|
||Super Site|Super Site|24h P98|18|50|36%|
||Super Site|Super Site|Anual|11|20|55%|
||Gobernación|Gobernación|24h P98|-|50|-|
||Gobernación|Gobernación|Anual|-|20|-|

Fuente: Elaboración propia.

Respecto de los registros basales anteriormente presentados, y considerando que en la zona
de emplazamiento del proyecto existen otros proyectos sometidos a evaluación por parte
del SEIA, se realizó una revisión de los proyectos aprobados en los últimos 5 años para
verificar si alguno de ellos presentó aportes en la zona de Tocopilla, lo cual se presenta en
la Tabla a continuación:

TABLA-7: Proyectos cercanos aprobados recientemente

|ID|Nombre|RCA|Estado|Presenta aportes en<br>Tocopilla|
|---|---|---|---|---|
|1|Planta Desaladora Tocopilla|0164/2016|Aprobado|No|
|2|Adecuación Planta Desaladora RT Sulfuros|0045/2018|Aprobado|No|
|3|Tamaya Solar|0065/2019|Aprobado|Si|
|4|Distrito Norte|0006/2021|Aprobado|Si|

Fuente: Elaboración propia.

De la tabla anterior se observa que existen dos proyectos aprobados en los últimos 5 años
que no ha presentado aportes sobre la zona de Tocopilla:

 “Planta Desaladora Tocopilla” se encuentra en fase de operación según la
información disponible en el Sistema Nacional de Información de Fiscalización
Ambiental y, por tanto, es parte de la Línea de Base medida;

 “Adecuación Planta Desaladora RT Sulfuros” no presentó modelación en el área de
Tocopilla argumentando que las emisiones en el área son despreciables [5] ;

Por su parte, hay dos proyectos que declaran aportes sobre el sector de Tocopilla, pero que,
al mismo tiempo, pueden ser considerados como nulos en dicho sector:

5 Anexo 2.1: Cálculo de emisiones y Modelación de dispersión Adecuación Planta Desaladora RT Sulfuros.
Disponible en WWW:
https://seia.sea.gob.cl/archivos/2017/08/17/Anexo_2.1_Calculo_de_emisiones_y_Modelacion_de_dispersion.pdf.
Último acceso el 18 de noviembre de 2021.

11
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

 “Tamaya Solar” se encuentra actualmente en fase de construcción [6], la cual según su
evaluación ambiental es la de mayor emisión [7], y estará en fase de operación para
cuando el presente proceso de evaluación haya finalizado. Declara aporte igual a
cero sobre el área de Tocopilla.

 “Distrito Norte”, este se encuentra ubicado a 20 kilómetros hacia el sur de la ciudad
de Tocopilla. Declara aporte igual a cero sobre el área de Tocopilla [8] .

Por todo lo anteriormente presentado, es posible establecer que la Línea de Base medida
no se verá modificada de manera significativa por efectos sinérgicos de otros proyectos
aprobados, pero no ejecutados.

**6.1.2.** **PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC)**

En la Tabla a continuación se presentan las coordenadas y aportes de los puntos de máxima
concentración modelada, para cada parámetro y estadístico de la Fase de Operación.

TABLA-8: Punto de máxima concentración- Fase de Operación

|Norma|Parámetro|ID|Coordenadas UTM [m]<br>WGS84 Huso 19S|Col5|Coordenadas LCC [km]<br>Datum NWS-84|Col7|PMC|
|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|
|MP10 <br>[μg/m3N]*|Promedio<br>Anual|PMC1|390.036|7.550.017|-5,50|2,50|10,31|
|MP10 <br>[μg/m3N]*|P98 diario|PMC1|390.036|7.550.017|-5,50|2,50|33,85|
|MP2,5 <br>[μg/m3]*|Promedio<br>Anual|PMC1|390.036|7.550.017|-5,50|2,50|2,95|
|MP2,5 <br>[μg/m3]*|P98 diario|PMC1|390.036|7.550.017|-5,50|2,50|9,68|

Fuente: Elaboración propia.

En el Apéndice AD-5.2-2 se presenta la representación gráfica de cada uno de los puntos de
máxima concentración.

6 Avanzan nuestras iniciativas renovables: Planta Solar Tamaya inicia pruebas de energización. Disponible en
WWW: [https://engie-energia.cl/avanzan-nuestras-iniciativas-renovables-planta-solar-tamaya-inicia-pruebas-](https://engie-energia.cl/avanzan-nuestras-iniciativas-renovables-planta-solar-tamaya-inicia-pruebas-de-energizacion/)
[de-energizacion/. Último acceso el 18 de noviembre de 2021.](https://engie-energia.cl/avanzan-nuestras-iniciativas-renovables-planta-solar-tamaya-inicia-pruebas-de-energizacion/)
7 Anexo 7 Estimación y Modelación de Emisiones Atmosféricas Tamaya Solar. Disponible en WWW:
[https://seia.sea.gob.cl/archivos/2018/09/12/Anexo_7_-_Emisiones_Atmosfericas.pdf. Último acceso el 18 de](https://seia.sea.gob.cl/archivos/2018/09/12/Anexo_7_-_Emisiones_Atmosfericas.pdf)
noviembre de 2021.
8 Informe de Resultados Modelación de la Dispersión de Emisiones Atmosféricas. Disponible en WWW:
[https://seia.sea.gob.cl/archivos/2020/07/08/Anexo_G_Emisiones.rar. Último acceso el 18 de noviembre de 2021.](https://seia.sea.gob.cl/archivos/2020/07/08/Anexo_G_Emisiones.rar)

12
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

**6.2.** **RESULTADOS DE LA MODELACIÓN**

**6.2.1.** **FASE DE OPERACIÓN**

Los resultados de la modelación para cada uno de los parámetros modelados de acuerdo
con los estadísticos definidos en las normas primarias calidad del aire evaluadas para la Fase
de Operación se presentan a continuación. Los resultados son presentados con y sin factor
de corrección (FC en las tablas siguientes), de acuerdo con lo detallado en el numeral 4.3
(Análisis de incertidumbre) y lo recomendado en la Guía de modelación.

TABLA-9: Aportes modelados en Receptores Primarios, Escenario de Fase de Operación

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Unidad|Aporte<br>Proyecto|Aporte<br>Proyecto<br>(con FC)|
|---|---|---|---|---|---|---|
|MP10|Bomberos|Primaria|24h P98|μg/m3N|0,06|0,07|
|MP10|Bomberos|Primaria|Anual|μg/m3N|0,01|0,01|
|MP10|Tres Marías|Tres Marías|24h P98|μg/m3N|0,06|0,07|
|MP10|Tres Marías|Tres Marías|Anual|μg/m3N|0,01|0,02|
|MP10|Super Site|Super Site|24h P98|μg/m3N|0,09|0,11|
|MP10|Super Site|Super Site|Anual|μg/m3N|0,03|0,03|
|MP10|Gobernación|Gobernación|24h P98|μg/m3N|0,06|0,07|
|MP10|Gobernación|Gobernación|Anual|μg/m3N|0,01|0,02|
|MP2,5|Bomberos|Primaria|24h P98|μg/m3|0,02|0,02|
|MP2,5|Bomberos|Primaria|Anual|μg/m3|0,00|0,00|
|MP2,5|Tres Marías|Tres Marías|24h P98|μg/m3|0,02|0,02|
|MP2,5|Tres Marías|Tres Marías|Anual|μg/m3|0,00|0,00|
|MP2,5|Super Site|Super Site|24h P98|μg/m3|0,02|0,03|
|MP2,5|Super Site|Super Site|Anual|μg/m3|0,01|0,01|
|MP2,5|Gobernación|Gobernación|24h P98|μg/m3|0,02|0,02|
|MP2,5|Gobernación|Gobernación|Anual|μg/m3|0,00|0,00|

Fuente: Elaboración propia.

13
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

**6.2.2.** **ANÁLISIS DE SINERGIA CON PROYECTO COLINDANTE**

Como se indicó en el Capítulo 1 de la DIA en evaluación, el Proyecto corresponde a una
planta de producción de Hidrógeno Verde, el cual alimentará con dicho producto a la planta
de producción de Amoníaco Verde, de propiedad de ENAEX, la que se ubicará en un terreno
adyacente.

Dicho lo anterior, y considerando que la condición más desfavorable en términos de calidad
del aire correspondería al hecho de que la fase de construcción del proyecto vecino coincida
en el tiempo con la fase de operación del proyecto en evaluación, se ha realizado un análisis
de sinergia de éstos, sumando ambos aportes de manera simultánea. Es necesario indicar
que dicho análisis corresponde a un caso hipotético, toda vez que los proyectos han sido
tramitados de forma paralela, y tienen la misma fecha estimada de inicio de labores de sus
fases de construcción.

También resulta relevante indicar que para los aportes calculados se ha considerado el
mismo factor de corrección mencionado anteriormente, toda vez que el archivo de datos
meteorológicos generado como entrada para el modelo de dispersión de contaminantes
utilizados para la evaluación de ambos Proyectos es el mismo.

En la tabla a continuación se presentan los resultados de aporte a la calidad del aire
calculados para el proyecto “HyEx - Síntesis de Amoniaco Verde”:

TABLA-10: Aportes modelados en Receptores Primarios, Proyecto “HyEx - Síntesis de

Amoniaco Verde”, Escenario de Fase de Construcción

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Unidad|Aporte<br>Proyecto<br>Colindante|Aporte<br>Proyecto<br>Colindante<br>(con FC)|
|---|---|---|---|---|---|---|
|MP10|Bomberos|Primaria|24h P98|μg/m3N|0,05|0,06|
|MP10|Bomberos|Primaria|Anual|μg/m3N|0,01|0,01|
|MP10|Tres Marías|Tres Marías|24h P98|μg/m3N|0,05|0,06|
|MP10|Tres Marías|Tres Marías|Anual|μg/m3N|0,01|0,01|
|MP10|Super Site|Super Site|24h P98|μg/m3N|0,08|0,09|
|MP10|Super Site|Super Site|Anual|μg/m3N|0,02|0,03|
|MP10|Gobernación|Gobernación|24h P98|μg/m3N|0,05|0,06|
|MP10|Gobernación|Gobernación|Anual|μg/m3N|0,01|0,01|
|MP2,5|Bomberos|Primaria|24h P98|μg/m3|0,01|0,02|
|MP2,5|Bomberos|Primaria|Anual|μg/m3|0,00|0,00|
|MP2,5|Tres Marías|Tres Marías|24h P98|μg/m3|0,01|0,02|
|MP2,5|Tres Marías|Tres Marías|Anual|μg/m3|0,00|0,00|
|MP2,5|Super Site|Super Site|24h P98|μg/m3|0,02|0,02|
|MP2,5|Super Site|Super Site|Anual|μg/m3|0,01|0,01|

14
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

|Col1|Gobernación|Col3|24h P98|μg/m3|0,02|0,02|
|---|---|---|---|---|---|---|
||Gobernación||Anual|μg/m3|0,00|0,00|

Fuente: Elaboración propia, en base a información disponible en Anexo C2-2 Modelación Calidad del Aire,

Adenda al Proyecto “HyEx - Síntesis de Amoniaco Verde “, en calificación (Res. Adm. 0317/2021).

Finalmente, en base a los resultados de la modelación de ambos proyectos, se presenta en

la tabla a continuación el análisis de sinergia establecido:

TABLA-11: Aportes modelados en Receptores Primarios, Escenario de Sinergia

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Línea<br>de<br>Base<br>(LB)|Aporte<br>Proyecto<br>(con FC)|Aporte<br>Proyecto<br>colindante<br>(con FC)|Concentración<br>total|
|---|---|---|---|---|---|---|---|
|MP10|Bomberos|Primaria|24h P98|-|0,07|0,06|0,13|
|MP10|Bomberos|Primaria|Anual|-|0,01|0,01|0,03|
|MP10|Tres Marías|Tres Marías|24h P98|110|0,07|0,06|110,13|
|MP10|Tres Marías|Tres Marías|Anual|45|0,02|0,01|45,03|
|MP10|Super Site|Super Site|24h P98|61|0,11|0,09|61,20|
|MP10|Super Site|Super Site|Anual|36|0,03|0,03|35,72|
|MP10|Gobernación|Gobernación|24h P98|72|0,07|0,06|71,63|
|MP10|Gobernación|Gobernación|Anual|38|0,02|0,01|37,60|
|MP2,5|Bomberos|Primaria|24h P98|35|0,02|0,02|35,04|
|MP2,5|Bomberos|Primaria|Anual|14|0,00|0,00|14,01|
|MP2,5|Tres Marías|Tres Marías|24h P98|32|0,02|0,02|31,57|
|MP2,5|Tres Marías|Tres Marías|Anual|13|0,00|0,00|13,01|
|MP2,5|Super Site|Super Site|24h P98|18|0,03|0,02|18,05|
|MP2,5|Super Site|Super Site|Anual|11|0,01|0,01|11,01|
|MP2,5|Gobernación|Gobernación|24h P98|-|0,02|0,02|0,04|
|MP2,5|Gobernación|Gobernación|Anual|-|0,00|0,00|0,01|

Fuente: Elaboración propia.

De la tabla anterior, se observa que los aportes de ambos proyectos no sobrepasan los 0,5
μg/m3 y, por tanto, es posible establecer que sus aportes son nulos a todo efecto, incluso
en el escenario de modelación más desfavorable, como se ha descrito anteriormente.

**7.** **CUMPLIMIENTO DE NORMATIVA**

A continuación, se presentan las tablas de evaluación de cumplimiento normativo para cada
parámetro modelado, en las cuales se comparan los aportes del Proyecto, así como la
sinergia con el proyecto colindante, respecto de la línea de base, en los receptores discretos
considerados para material particulado (MP 10 y MP 2,5 ).

15
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

Respecto de los resultados obtenidos, se estima que los aportes en material particulado a
los receptores correspondientes a las estaciones de calidad del aire en la ciudad de Tocopilla
no modificarán la condición basal de calidad del aire, toda vez que los aportes estimados,
incluyendo el factor de corrección por incertidumbre, corresponden a valores que pueden
considerarse como nulos.

Respecto lo anterior, a continuación, se presentan la tabla con el análisis normativo.

16
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

TABLA-12: Concentración total MP 10 [μg/m [3] N] y MP 2,5 [μg/m [3] ] y comparación con normativa

|Parámetro|Receptor|Tipo de<br>Norma|Estadístico|Aporte<br>ambos<br>proyectos<br>(AP)|Línea de<br>Base<br>(LB)|SUMA<br>(AP+LB)|Norma|% AP c/r<br>Norma|% Total<br>Norma|
|---|---|---|---|---|---|---|---|---|---|
|MP10<br>[μg/m3N]|Bomberos|Primaria|24h P98|0|-|-|150|0%|-|
|MP10<br>[μg/m3N]|Bomberos|Primaria|Anual|0|-|-|50|0%|-|
|MP10<br>[μg/m3N]|Tres Marías|Tres Marías|24h P98|0|110|110|150|0%|73%|
|MP10<br>[μg/m3N]|Tres Marías|Tres Marías|Anual|0|45|45|50|0%|90%|
|MP10<br>[μg/m3N]|Super Site|Super Site|24h P98|0|61|61|150|0%|41%|
|MP10<br>[μg/m3N]|Super Site|Super Site|Anual|0|36|36|50|0%|71%|
|MP10<br>[μg/m3N]|Gobernación|Gobernación|24h P98|0|72|72|150|0%|48%|
|MP10<br>[μg/m3N]|Gobernación|Gobernación|Anual|0|38|38|50|0%|75%|
|MP2,5<br>[μg/m3]|Bomberos|Primaria|24h P98|0|35|35|50|0%|70%|
|MP2,5<br>[μg/m3]|Bomberos|Primaria|Anual|0|14|14|20|0%|70%|
|MP2,5<br>[μg/m3]|Tres Marías|Tres Marías|24h P98|0|32|32|50|0%|63%|
|MP2,5<br>[μg/m3]|Tres Marías|Tres Marías|Anual|0|13|13|20|0%|65%|
|MP2,5<br>[μg/m3]|Super Site|Super Site|24h P98|0|18|18|50|0%|36%|
|MP2,5<br>[μg/m3]|Super Site|Super Site|Anual|0|11|11|20|0%|55%|
|MP2,5<br>[μg/m3]|Gobernación|Gobernación|24h P98|0|-|-|50|0%|-|
|MP2,5<br>[μg/m3]|Gobernación|Gobernación|Anual|0|-|-|20|0%|-|

Nota: (*) Los aportes informados como 0 μg/m [3], corresponden a valores menores a 0,5 μg/m [3] . Esto, porque la normativa de calidad del aire señala que se

deben aproximar al entero más cercano;

Fuente: Elaboración propia.

17
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE

**8.** **CONCLUSIONES**

De los resultados obtenidos en la modelación atmosférica de emisiones, correspondientes
a la Fase de Operación, se concluye que el Proyecto “ **HyEx** - **Producción de Hidrógeno**
**Verde** ” no generará un aporte incremental significativo en las concentraciones ambientales
de material particulado en los receptores evaluados con respecto a la Línea Base y las normas
de calidad primaria vigentes.

Respecto a la ubicación de los puntos de máxima concentración de la grilla de receptores,
se observa que se localizan en sectores aledaños al camino de acceso a la Planta, donde no
existen receptores discretos de interés, razón por la cual han sido considerados dentro del
análisis normativo.

Dado lo anterior, se concluye que el Proyecto no produce impactos significativos sobre la
calidad del aire, dado que los aportes del Proyecto no modifican significativamente la
condición de calidad del aire de su entorno. Por ende, no se produce alguno de los efectos,
características o circunstancias de aquellos señalados en el artículo 11 de la Ley N° 19.300.

18
ANEXO AD-5.2-2- MODELACIÓN CALIDAD DEL AIRE