---
title: Sin título
author: p_reszczynski@jaimeillanes.cl
date: D:20241023123958-03'00'
language: es
type: report
pages: 54
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO ADC-4.15
-->

# ANEXO ADC-4.15

## ACTUALIZACIÓN MODELACIÓN DE CALIDAD DEL AIRE

### _Cliente:_

**ÍNDICE**

1. MODELACIÓN DE CALIDAD DEL AIRE ...................................................................................................1

1.4.1. BASE TEÓRICA DEL MODELO UTILIZADO .......................................................................... 4

1.4.2. CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN ..................................................... 5

1.4.3. ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF ......................... 7

1.5.1. CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO ..................................................... 9

1.5.2. PARAMETRIZACIÓN DEL MODELO WRF/CALPUFF ........................................................... 9

1.5.3. CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO ................................................... 11

1.5.4. APORTES DE TERCEROS (LÍNEA DE BASE PROYECTADA) ............................................... 11

1.5.5. PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN ................. 13

1.5.6. ANALISIS DE INCERTIDUMBRE ........................................................................................... 30

1.6.1. PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC) ............................................................. 31

1.6.2. RESULTADOS DE LA MODELACIÓN .................................................................................. 34

1.7.1. ESTACIONES DE CALIDAD DEL AIRE ................................................................................. 40

1.7.2. RECEPTORES PRIMARIOS .................................................................................................... 45

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE

**APÉNDICES**

APÉNDICE 1: Archivos de Modelación

APÉNDICE 2: Isoconcentraciones y PMI Fase Construcción

APÉNDICE 3: Isoconcentraciones y PMI Fase Operación

APÉNDICE 4: Justificación Parametrización WRF

APÉNDICE 5: Cálculo Tasas de Emisión

**TABLAS**

TABLA-1: Norma Primaria de Calidad del Aire MP 10, MP 2,5, NO 2, SO 2 y CO ........................ 3
TABLA-2: Ubicación Receptores Primarios ....................................................................................... 5
TABLA-3: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF ........ 6

TABLA-4: Parametrización modelo WRF/CALPUFF ....................................................................... 9
TABLA-5: Línea de Base Proyectada (LBP) ...................................................................................... 12
TABLA-6: Emisiones del Escenario Construcción ......................................................................... 15

TABLA-7: Emisiones del Escenario Operación Actual................................................................. 19
TABLA-8: Emisiones del Escenario Operación Proyectada ....................................................... 24
TABLA-9: Estadígrafos de ajuste de la modelación meteorológica Estación Pudahuel 30
TABLA-10: Estadígrafos de ajuste de la modelación meteorológica Estación Cerro Navia

..................................................................................................................................................... 30

TABLA-11: Coordenadas y concentraciones de los PMC de cada parámetro modelado,
Fase Construcción ................................................................................................................ 31

TABLA-12: Coordenadas y concentraciones de los PMC de cada parámetro modelado,
Fase Operación Actual ....................................................................................................... 32
TABLA-13: Coordenadas y concentraciones de los PMC de cada parámetro modelado,
Fase Operación Proyectada .............................................................................................. 32
TABLA-14: Aportes Modelados a los Receptores, Fase de Construcción ............................. 35
TABLA-15: Aportes Modelados a los Receptores, Fase de Operación Actual ..................... 36
TABLA-16: Aportes Modelados a los Receptores, Fase de Operación Proyectada ........... 37
TABLA-17: Aportes Modelados a los Receptores, Fase de Operación Diferencia ............. 38
TABLA-18: Criterios de significancia de incremento en la calidad del aire de MP10 y
MP2,5 en Zonas Saturadas ............................................................................................... 39
TABLA-19: Criterios de Significancia de Aportes asociado a SIL (US/EPA) .......................... 40
TABLA-20: Análisis Normativo en Estaciones de Monitoreo, Fase de Construcción ........ 41
TABLA-21: Análisis Normativo en Estaciones de Monitoreo, Fase de Operación ............. 42
TABLA-22: Aportes Modelados en los Receptores comparado con los valores de
significancia de incremento en la calidad del aire, Fase de Construcción ..... 46
TABLA-23: Aportes Modelados en los Receptores comparado con los valores de
significancia de incremento en la calidad del aire, Fase de Operación ........... 47

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE

**FIGURAS**

FIGURA-1: Ubicación del Proyecto, Dominio de Modelación y Receptores .......................... 7
FIGURA-2: Ubicación Fuentes Emisoras y Receptores, Fase de Construcción .................... 18
FIGURA-3: Ubicación Fuentes Emisoras y Receptores, Fase de Operación Actual ............ 23
FIGURA-4: Ubicación Fuentes Emisoras y Receptores, Fase de Operación Proyectada .. 29
FIGURA-5: Área de Influencia Calidad del Aire del Proyecto .................................................... 49

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE

**1.** **MODELACIÓN DE CALIDAD DEL AIRE**

**INTRODUCCIÓN**

El presente informe da cuenta del análisis del transporte y dispersión de contaminantes
emitidos por las Fases de Construcción y Operación del proyecto “ **Nuevo Centro de**
**Distribución La Rambla”** (en adelante, el Proyecto), ubicado en la comuna de Renca, Región
Metropolitana.

La simulación de los aportes del Proyecto a las concentraciones ambientales se realiza
mediante la aplicación del sistema de modelación WRF/CALPUFF, sistema que considera la
utilización de la modelación meteorológica para el año 2021 (WRF) y un dominio de
modelación de CALPUFF de 53x53 [km] con una resolución de 1x1 [km], la cual incluye una
serie de receptores primaros, dentro de las cuales se encuentran las estaciones de calidad
del aire Cerro Navia y Pudahuel, presentes en el área determinada por el dominio de
modelación, donde se registraron valores basales de material particulado y gases.

A continuación, se presenta el análisis de la dispersión y transporte de las emisiones
correspondientes a las Fases de Construcción y Operación del Proyecto, que considera
principalmente las emisiones provenientes de fuentes fugitivas (movimientos de tierra),
fuentes móviles asociadas al transporte de estructuras, equipos, insumos y personas; y
fuentes puntuales como grupos electrógenos. Cabe señalar que para la Fase de Operación,
se consideran los escenarios de Operación Actual y Operación Proyectada, de manera de
cuantificar el aumento de los aportes del proyecto en dicha fase. De esta manera los
escenarios modelados corresponden a los siguientes:

 Escenario Construcción: Año con mayores emisiones (Año 1).

 Escenario Operación Actual: Funcionamiento actual del centro de distribución.

 Escenario Operación Proyectada: Funcionamiento total del centro de distribución

En concordancia a lo señalado en la Guía para el uso de modelos de calidad del aire en el
SEIA, los resultados de la modelación se entregan en tablas en función de los estadísticos
normados para cada contaminante.

Además, se comparan los resultados de la modelación respecto de la línea de base y, a su
vez, respecto de las normas primarias de calidad del aire nacionales (artículo 11 del D.S. N°
40/12 que aprueba el Reglamento del Sistema de Evaluación de Impacto Ambiental -RSEIA), de manera de evaluar el grado de cumplimiento normativo [1] .

Los parámetros que se analizan corresponden a MP 10 ; MP 2,5 ; NO 2 ; SO 2 y CO. Se indica que

1 No se evalúa la norma secundaria de calidad del aire, debido a que no existen puntos de interés secundarios en las cercanías
de las fuentes de emisión del Proyecto.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 1

los archivos digitales de la modelación con CALPUFF, incluyendo el modelo WRF utilizado,
se adjuntan sólo en formato digital debido a su tamaño, el cual no es soportado por la
plataforma digital del SEA (Apéndice 1). Por otro lado, las isocurvas de concentración, así
como los puntos de máxima concentración, son presentadas en los Apéndices 2 y 3,
diferenciadas por contaminante y escenario.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 2

**OBJETIVO**

Determinar el aporte incremental a las concentraciones ambientales de material particulado
y gases que generará el Proyecto en los receptores sensibles identificados y comparar dichos
aportes con respecto a la situación actual, línea base y las normas de calidad primaria
nacionales.

**MARCO LEGAL**

Para determinar la existencia de los efectos, características o circunstancias de los literales
a), b) y d) del art. 11 de la Ley 19.300 en el área de influencia del Proyecto en sus fases de
construcción y operación, se ha considerado la normativa ambiental primaria y de calidad
de aire vigente para MP 10, MP 2,5, NO 2, SO 2 y CO, presentadas en la Tabla 1:

TABLA-1: Norma Primaria de Calidad del Aire MP 10, MP 2,5, NO 2, SO 2 y CO

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**MP10 **|D.S. N°12/22 del<br>MMA|Promedio aritmético de tres años calendario<br>consecutivos|50 μg/m3|
|**MP10 **|D.S. N°12/22 del<br>MMA|Percentil 98 de las concentraciones de 24 horas<br>registradas durante un período anual|130 μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Promedio tri-anual de las concentraciones<br>anuales|20 μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Percentil 98 de los promedios diarios registrados<br>durante un año|50 μg/m3|
|**NO2 **|D.S. N° 40/2024 del<br>MMA|Promedio<br>aritmético<br>de<br>los<br>valores<br>de<br>concentración anual de tres años calendarios<br>sucesivos|40 μg/m3|
|**NO2 **|D.S. N° 40/2024 del<br>MMA|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario|200 μg/m3|
|**NO2 **|D.S. N° 40/2024 del<br>MMA|Promedio aritmético de tres años sucesivos de<br>los valores del percentil 99 de la concentración<br>de 24 horas registrados durante un año.|100 μg/m3|
|**SO2 **|D.S. N° 104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 99 de las<br>concentraciones de 24 horas registradas cada<br>año|150 μg/m3|
|**SO2 **|D.S. N° 104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores de concentración anual|60 μg/m3|
|**SO2 **|D.S. N° 104/2019 del<br>MINSEGPRES|Promedio aritmético de tres años calendario<br>sucesivos de los valores del percentil 98,5 de las<br>concentraciones de 1 hora registradas cada año|350 μg/m3|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 3

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**CO**|D.S. N° 115/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 1 hora registrados durante un<br>año calendario|30 mg/m3|
|**CO**|D.S. N° 115/2002 del<br>MINSEGPRES|Promedio aritmético de tres años sucesivos del<br>percentil 99 de los máximos diarios de<br>concentración de 8 horas (promedio móvil)<br>registrados durante un año calendario|10 mg/m3|

Fuente: Elaboración propia

**METODOLOGIA**

La modelación se realizó acorde con la metodología descrita en la Guía para el uso de
modelos de calidad del aire en el SEIA (2023), en adelante la “Guía de modelación”. Se utilizó
el modelo numérico Weather Research and Forecasting (WRF) en la generación de datos
meteorológicos para el año 2021, y el modelo CALPUFF para la modelación de la dispersión
y transporte de las emisiones, en los escenarios considerados.

**1.4.1.** **BASE TEÓRICA DEL MODELO UTILIZADO**

WRF es el modelo meteorológico recomendado en la Guía de modelación para la generación
de la grilla meteorológica, esto por sobre modelos que consideran estaciones de monitoreo
en la modelación. Este modelo genera una grilla tridimensional de viento y temperatura, a
través de dominios anidados con una resolución horizontal, recomendada para el dominio
de menor tamaño, de 1 kilómetro.

Por otro lado, CALPUFF es un modelo de dispersión, transporte y deposición de
contaminantes atmosféricos de tipo puff lagrangiano-gaussiano, no estacionario,
recomendado por la Guía de modelación y también por la Agencia de Protección Ambiental
de Estados Unidos (US EPA su sigla en inglés) [2], el cual es aplicable a terrenos complejos y a
múltiples tipos de fuentes emisoras (puntuales, areales y volumétricas). CALPUFF realiza sus
cálculos tomando los datos meteorológicos superficiales y de la capa superior atmosférica,
incluyendo la posibilidad de modelar la dispersión de contaminantes primarios y
secundarios, obteniendo resultados confiables para distancias de hasta 100 [km].

El sistema de modelación incluye tres componentes principales: Calmet, CALPUFF y
CALPOST, además de una serie de programas de pre-procesamiento diseñados para la
preparación de la información meteorológica y geofísica, En este caso, no fue necesario
utilizar los pre-procesadores ni el módulo CALMET, ya que se emplearon los resultados de

2 40 CFR Part 51, Revision to the Guideline on Air Quality Models: Adoption of a Preferred General Purpose (Flat
and Complex Terrain) Dispersion Model and Other Revisions; Final Rule.
http://www.epa.gov/ttn/scram/guidance/guide/appw_05.pdf

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 4

la modelación meteorológica realizada con WRF.

CALPOST es un programa post-procesador que permite compilar los resultados de CALPUFF
creando los archivos según los estadísticos establecidos en las normas de calidad del aire
para la evaluación de los resultados.

**1.4.2.** **CARACTERIZACIÓN DEL DOMINIO DE MODELACIÓN**

Para que los procesos meteorológicos de mesoescala sean representados de una forma
adecuada, tanto por el modelo meteorológico como por el modelo de dispersión, se generó
un dominio de modelación de WRF/CALPUFF de 53x53 [km], en donde se consideraron las
características topográficas de la zona, incluyendo los receptores primarios y las estaciones
de calidad del aire, donde se registraron valores basales de material particulado y gases
(TABLA-2).

TABLA-2: Ubicación Receptores Primarios

|ID|Nombre Receptor|Coordenadas UTM<br>WGS 84 Huso 19S|Col4|Coordenadas LCC<br>Datum NWS84|Col6|Elevación<br>[m]|
|---|---|---|---|---|---|---|
|**ID**|**Nombre Receptor**|**Este [m]**|**Norte [m]**|**X [m]**|**Y (m)**|**Y (m)**|
|R1|Vivienda La Rambla 1|336.731|6.303.619|230,79|-147,81|498,18|
|R2|Vivienda La Rambla 2|336.721|6.303.587|220,30|-179,64|498,25|
|R3|Vivienda La Rambla 3|336.702|6.303.531|200,45|-235,32|498,04|
|R4|Vivienda La Rambla 4|336.716|6.303.497|213,80|-269,55|498,7|
|R5|Vivienda La Rambla 5|336.702|6.303.460|199,25|-306,31|498,68|
|R6|Vivienda La Rambla 6|336.689|6.303.427|185,76|-339,09|498,61|
|R7|Vivienda La Rambla 7|336.685|6.303.380|180,98|-386,04|498,71|
|R8|Vivienda La Rambla 8|336.675|6.303.336|170,29|-429,87|498,53|
|R9|Vivienda La Rambla 9|336.663|6.303.297|157,69|-468,66|498,2|
|R10|Vivienda La Rambla 10|336.637|6.303.199|130,16|-566,23|497,03|
|R11|Vivienda La Rambla 11|336.623|6.303.158|115,53|-607,01|496,23|
|R12|Vivienda La Rambla 12|336.612|6.303.116|103,88|-648,81|495,37|
|R13|Vivienda La Hacienda|336.534|6.302.872|22,14|-891,50|490,47|
|R14|R04 (Ruido)|336.654|6.303.244|147,84|-521,51|497,82|
|R15|R05 (Ruido)|336.733|6.303.287|227,20|-479,85|499,4|
|R16|R06 (Ruido)|336.715|6.303.557|213,82|-209,54|498,43|
|R17|Estación Pudahuel|337.311|6.298.809|727,16|-4967,73|494,1|
|R18|Estación Cerro Navia|338.984|6.299.360|2.401,67|-4.445,01|500,81|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 5

Cabe señalar que la modelación meteorológica WRF fue realizada para el año 2021. Esta
determinación se efectuó en base al análisis de la línea de base de calidad del aire, en
comparación con la línea de base de meteorología de manera de seleccionar el año con las
condiciones meteorológicas más desfavorables como lo indica la Guía de Modelación. En el
análisis de los años 2020, 2021 y 2022, de las Estaciones Cerro Navia y Pudahuel, se observó
que los máximos de los estadísticos normados se presentan mayormente en el año 2021,
seguido por el año 2022. Por otra parte, al analizar las mediciones meteorológicas de las 2
estaciones, se obtienen que los años 2020 y 2021 son los que poseen peores condiciones
de ventilación, presentándose los mayores porcentajes de “calma” en la variable velocidad
del viento, lo que se traduce en una condición desfavorable para la dispersión de los
contaminantes . Finalmente, en base a el análisis de ambas líneas de base, se determinó que
el año de modelación meteorológica con las condiciones más conservadoras corresponde
al año 2021. De acuerdo con la configuración definida por el SEA en su guía de modelación,
la modelación cuenta con una resolución horizontal de 1 [km] y una resolución vertical de
10 niveles a 20, 40, 80, 160, 320, 640, 1.200, 2.000, 3.000 y 4.000 metros. En la Tabla a
continuación se señalan las coordenadas de los vértices del dominio de modelación

WRF/CALPUFF.

TABLA-3: Coordenadas de los vértices del sistema de modelación WRF/CALPUFF

|Vértices|Coordenadas UTM [m] Datum: WGS-84, Huso: 19S|Col3|
|---|---|---|
|**Vértices**|**Este**|**Norte**|
|**SW**|310.108|6.276.400|
|**NE**|362.688|6.330.688|
|**NW**|309.205|6.329.802|
|**SE**|363568|6.277.341|

Fuente: Elaboración propia

A continuación, se presenta gráficamente el dominio de modelación, los receptores
sensibles y la ubicación del proyecto:

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 6

FIGURA-1: Ubicación del Proyecto, Dominio de Modelación y Receptores

Fuente: Elaboración propia

**1.4.3.** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO METEOROLÓGICO WRF**

La modelación atmosférica está basada en uno de los modelos de pronóstico meteorológico
más avanzados y completos disponibles, el cual cuenta con un gran número de
parametrizaciones que permiten, si son adecuadamente seleccionadas e implementadas,
simular gran parte de los procesos meteorológicos de mesoescala, este modelo corresponde
como ya se ha mencionado al Weather Research and Forecasting (WRF).

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 7

Sin embargo, e independiente de las bondades del modelo utilizado, todo modelo
atmosférico requiere ser calibrado y validado para cada condición meteorológica y de
terreno. En este punto es donde se tienen las mayores dificultades, dado que la incorrecta
implementación de alguna parametrización puede llevar a errores significativos en la
estimación de los vientos en superficie y con esto de las trayectorias de los contaminantes.

La parametrización del modelo utilizado y su justificación se encuentra en el Apéndice 4, de
acuerdo con lo establecido por la Guía de Modelación.

Para realizar el análisis de incertidumbre se consideran las recomendaciones establecidas en

la Guía de modelación, donde se menciona que cualquier modelo representa una
aproximación a la realidad y sus resultados tienen incertidumbres asociadas, las cuales se
expresan a través de diferencias entre lo estimado y lo observado.

Cabe señalar que, a partir de la estación meteorológica más cercana se evaluaron los
estadígrafos meteorológicos recomendados por la guía, que corresponden al BIAS (sesgo),
MAE (error absoluto medio) y RMSE correspondiente a la raíz del error cuadrático medio,
además del coeficiente de correlación (r). Este análisis se realiza tanto para la velocidad [m/s],
como la temperatura [°C], entre los valores de la estación modelada a partir del modelo
meteorológico WRF utilizado y mediciones de estaciones meteorológicas disponibles para
el área a modelar. A continuación, se presentan las ecuaciones de estas métricas:

n

BIAS= [1]

n [∑(S] [i] [−O] [i] [)]

i=1

n

MAE= [1]

n [∑] [|] [S] [i] [−O] [i] [|]

i=1

n

RMSE= √ [1]

n

n [∑(S] [i] [−O] [i] [)] [2]

(Ec. 1)

(Ec. 2)

(Ec. 3)

i=1

Cabe señalar que, el error cuadrático medio mide la cantidad de error que hay entre dos
conjuntos de valores, es decir presenta la diferencia entre los valores pronosticados y
observados.

**PARÁMETROS DE ENTRADA DEL MODELO**

A continuación, se detallan los principales parámetros de entrada del modelo de calidad del
aire, los que corresponden a: características topográficas, uso del suelo, fuentes emisoras
externas (aportes de terceros) y escenario de modelación (emisiones asociadas a las
instalaciones donde se emplaza el Proyecto).

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 8

**1.5.1.** **CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO**

Las características topográficas y de uso de suelo, son parámetros asociados a la elevación
de terreno, los coeficientes de rugosidad, razón de bowen, entre otros, que son parte
integrante de los datos que incluye el archivo de modelación WRF, por lo cual no se requiere
su caracterización.

**1.5.2.** **PARAMETRIZACIÓN DEL MODELO WRF/CALPUFF**

Respecto de la parametrización de la modelación WRF/CALPUFF, se ha considerado como
referencia la “Guía de Modelación de Dispersión de Calidad del Aire de la Columbia Británica
de Canadá” (BC MoE, 2015) [3], cuyo detalle se subdivide en 4 categorías:

 Configuración estándar (si es modificada, incluir justificación);

 Recomendación de la guía;

 - Juicio experto;

 - No utilizar.

El detalle de la recomendación, así como la configuración utilizada en la presente evaluación,
se señalan a continuación, en la siguiente tabla. Las recomendaciones englobadas en
paréntesis no deben ser modificadas de acuerdo con lo señalado en la BC MoE.

TABLA-4: Parametrización modelo WRF/CALPUFF

|Parámetro|BC MoE<br>Recomendación|Valor utilizado en la<br>modelación|Comentario|
|---|---|---|---|
|MGAUSS|(1)|1|Modelo Gaussiano|
|MCTADJ|3|3|Ajuste partícula de la trayectoria de la<br>pluma|
|MCTSG|0|0|Parámetro por defecto|
|MSLUG|0|0|Parámetro por defecto|
|MTRANS|(1)|1|Parámetro por default|
|MTIP|1 o 2|1|Se considera debido a que existen fuentes<br>fijas en la modelación.|
|MRISE|1|1|Se considera “Briggs plume rise“<br>(elevación de la pluma)|
|MTIP_FL|-|0|Parámetro por defecto|
|MRISE_FL|-|2|Parámetro por defecto|
|MBDW|1 o 2|1|No aplica. No se considera “Building<br>Downwash”|
|MSHEAR|0|0|Parámetro por defecto|

3 British Columbia Air Quality Dispersion Modelling Guideline (Victoria, British Columbia, Canada):
[https://www2.gov.bc.ca/assets/gov/environment/air-land-water/air/reports-pub/bc-dispersion-modelling-guideline-2015.pdf](https://www2.gov.bc.ca/assets/gov/environment/air-land-water/air/reports-pub/bc-dispersion-modelling-guideline-2015.pdf)

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 9

|Parámetro|BC MoE<br>Recomendación|Valor utilizado en la<br>modelación|Comentario|
|---|---|---|---|
|MSPLIT|0|0|Parámetro por defecto|
|MCHEM|0 o 6|0|No se considera modelación de<br>transformación química|
|MAQCHEM|1|0|No se considera modelación de<br>transformación química, por lo que no<br>aplica considerar este punto.|
|MLWC|1|1|Se utiliza la data de grilla de agua de nube<br>de WRF|
|MWET|0 o 1|1|No aplica, debido a que no se modela<br>deposición.|
|MDRY|0 o 1|1|1|
|MTILT|0 o 1|0|Se modelan partículas pequeñas|
|MDISP|3|3|Parámetro por defecto|
|MTURBVW|3|3|3|
|MDISP2|3|3|3|
|MTAULY|0|0|Escala lagragiana de tiempo|
|MTAUADV|0|0|Opción “no turbulence advection”|
|MCTURB|1|1|Se consideran las subrutinas estándar de<br>CALPUFF|
|MROUGH|0|0|No se incluye ajuste por rugosidad de la<br>superficie|
|MPARTL|(1)|1|Se considera una parte de la pluma que<br>penetra la capa de mezcla debido a que<br>las fuentes puntuales fueron ingresadas<br>con temperatura.|
|MPARTLBA|1|0|No se considera penetración de la capa<br>de mezcla debido a que las fuentes<br>areales no presentan aumentos de niveles<br>de temperatura significantes.|
|MTINV|0|0|Calculo por default, no se incluyen perfiles<br>de temperatura.|
|MPDF|0 o 1|0|Se considera MDISP = 3|
|MSGTIBL|0 o 1|0|No se considera línea de costa en la<br>modelación|
|MBCON|0|0|No se consideran condiciones de borde|
|MFOG|0|0|No se considera FOG Model|
|MREG|0|0|Condiciones por defecto|
|SVMIN<br>SWMIN|σv = 0,2 para A, B,<br>C, D, E o F<br>σW = default|σv = 0,2 para A, B, C,<br>D, E o F<br>σW = default|Condiciones por defecto|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 10

Por otra parte, los contaminantes modelados corresponden a MP 10, MP 2,5, SO 2, NO x y CO,
cuyos parámetros de modelación corresponden a los entregados por defecto por CALPUFF.
Por otra parte, debido a que se modela NOx, en el postprocesador de los resultados de
CALPUFF (CALPOST) se considera que el NO 2 es un 10% del NOx, como se indica en el
capítulo 8.1.1. de la Guía de Modelación, de manera de poder comparar los aportes con la
normativa chilena. Cabe señalar que, el 7 de marzo del 2023 se publicó el D.S. N°5 que
“Establece Norma Primaria de Calidad del Aire para el Compuesto Orgánico Volátil
Benceno”, la cual corresponde a 3 μg /Nm [3] como promedio anual. Sin embargo, no se
considera la modelación de este contaminante, debido a que las fuentes de emisión emiten
bajas cantidades de COVS, del cual solo un 0,27% corresponde a benceno (según factores
del AP-42 de quema de petróleo Diésel), emitiéndose aproximadamente 0,001 t/año.

**1.5.3.** **CARACTERÍSTICAS TOPOGRÁFICAS Y USO DE SUELO**

Las características topográficas y de uso de suelo, son parámetros asociados a la elevación
de terreno, los coeficientes de rugosidad, razón de Bowen, entre otros, que son parte
integrante de los datos que incluye el archivo de modelación WRF, por lo cual no se requiere
su caracterización.

**1.5.4.** **APORTES DE TERCEROS (LÍNEA DE BASE PROYECTADA)**

Cabe señalar, que la línea base de calidad del aire monitoreada no considera los aportes de
proyectos aprobados que aún no se encuentran en Construcción u Operación al momento
de medir, por tanto, para considerar dichos aportes de terceros, se les suman estos a los
valores monitoreados obteniendo una línea base proyectada en el tiempo. Para ello, se
revisaron los proyectos de terceros que estuvieran al interior del área de influencia de calidad
del aire del presente Proyecto y que no estuvieran operando en un periodo de 5 años hacia
atrás.

Resultado de lo anterior se obtuvo la tabla con la línea base proyectada (LBP), con un
incremento en las concentraciones monitoreadas en la Línea de Base, ya que considera los
aportes de terceros más los valores monitoreados, la cual se presenta a continuación en la
siguiente Tabla.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 11

TABLA-5: Línea de Base Proyectada (LBP)

|Estación|Cont.|Estadístico|Unidad|Línea Base|Aporte de<br>Otros<br>Proyectos|Línea de<br>Base<br>Proyectada<br>(LBP)|
|---|---|---|---|---|---|---|
|**Pudahuel**|**MP10 **|**Percentil 98**<br>**Diario**|**μg/m3N**|176|1,01|177|
|**Pudahuel**|**MP10 **|**Promedio**<br>**Anual**|**μg/m3N**|64|0,10|64|
|**Pudahuel**|**MP2,5 **|**Percentil 98**<br>**Diario**|**μg/m3N**|103|0,10|103|
|**Pudahuel**|**MP2,5 **|**Promedio**<br>**Anual**|**μg/m3N**|27|0,00|27|
|**Pudahuel**|**NO2 **|**Percentil 99**<br>**Max 1 Hora**|**μg/m3N**|185|2,90|188|
|**Pudahuel**|**NO2 **|**Promedio**<br>**Anual**|**μg/m3N**|36|0,02|36|
|**Pudahuel**|**NO2 **|**Percentil 99**<br>**Diario**|**μg/m3N **|101|0,00|101|
|**Pudahuel**|**CO**|**Percentil 99**<br>**Max 1 Hora**|**mg/m3N**|11|0,00|11|
|**Pudahuel**|**CO**|**Percentil 99**<br>**Max 8 Hora**|**mg/m3N**|8|0,00|8|
|**Cerro Navia**|**MP10 **|**Percentil 98**<br>**Diario**|**μg/m3N**|187|2,20|189|
|**Cerro Navia**|**MP10 **|**Promedio**<br>**Anual**|**μg/m3N**|70|0,40|70|
|**Cerro Navia**|**MP2,5 **|**Percentil 98**<br>**Diario**|**μg/m3N**|107|0,30|107|
|**Cerro Navia**|**MP2,5 **|**Promedio**<br>**Anual**|**μg/m3N**|29|0,10|29|
|**Cerro Navia**|**NO2 **|**Percentil 99**<br>**Max 1 Hora**|**μg/m3N**|175|5,90|180|
|**Cerro Navia**|**NO2 **|**Promedio**<br>**Anual**|**μg/m3N**|38|0,10|38|
|**Cerro Navia**|**NO2 **|**Percentil 99**<br>**Diario**|**μg/m3N **|100|0,00|100|
|**Cerro Navia**|**CO**|**Percentil 99**<br>**Max 1 Hora**|**mg/m3N**|10|0,00|10|
|**Cerro Navia**|**CO**|**Percentil 99**<br>**Max 8 Hora**|**mg/m3N**|8|0,00|8|

 - Cabe señalar que los valores de línea de base han sido presentados sin decimales debido a las normas de

calidad de aire.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 12

**1.5.5.** **PARÁMETROS FÍSICOS E IDENTIFICACIÓN DE LAS FUENTES DE EMISIÓN**

En las siguientes secciones se presenta el resumen de las emisiones de cada una de las
fuentes emisoras ingresadas al modelo para los 3 escenarios modelados, correspondientes
a los siguientes:

 Fase Construcción: Se considera las emisiones del Año 1, correspondiente al
escenario más desfavorable de la Fase de Construcción.

 Fase de Operación Actual: Se consideran las emisiones actuales del centro de
distribución, sin la ejecución del proyecto.

 Fase de Operación Proyectada: Se consideran las emisiones del Año 3 en adelante,
correspondientes al escenario más desfavorable de la Fase de Operación.

Se destaca que las emisiones de los 3 escenarios fueron estimadas en el Anexo AD-23
“Actualización Emisiones Atmosféricas2 de la Adenda.

Cabe señalar que las tasas de emisión fueron temporalizadas al interior del sistema de
modelación WRF/CALPUFF, de acuerdo a lo señalado en la Descripción de Proyectos .

Adicionalmente a lo anterior, las tasas de emisión ingresadas al modelo fueron obtenidas a
través de las siguientes ecuaciones:

[g] t []]

T Point

~~[~~ [g] s [] =]

D

~~[~~ [días] año

[días] año ~~[]]~~ [ ∙H] ~~[[ ]~~ [h]

E ~~[~~ [t]

[t] ~~[[]~~ [g]

año ~~[]]~~ [ ∙10] [6] t

día [] ∙3600 [s] h

h ~~[]]~~

Ec. (4)

[g] t ~~[]]~~

T Road

~~[~~ s∙m [g] ~~[]]~~ [ =]

D[ [días] año

[h]

[días] año ~~[]]~~ [ ∙H[]

E ~~[~~ [t]

[t] ~~[[]~~ [g]

año ~~[]]~~ [ ∙10] [6] t

día ~~[]]~~ [ ∙3600 [s] h

h ~~[]]~~

t ~~[]]~~

g
T Area

[s∙m [2] ~~[]]~~ [ =]

g
T Line

~~[~~ s∙m [2] ~~[]]~~ [ =]

D[ [días] año

[h]

[días] año [] ∙H[] día

E [ [t]

[t] [[g]

año ~~[]]~~ [ ∙10] [6] t

día ~~[]]~~ [ ∙3600 [s] h

h ~~[]]~~

D[ [días] año

[días] año [] ∙H] ~~[[ ]~~ [h]

día ~~[]]~~ [ ∙3600 ] ~~[[]~~ h [s]

h [s] ~~[]]~~

E [ [t]

t ~~[]]~~

[t] [[g]

año ~~[]]~~ [ ∙10] [6] t

1
- Ec. (5)
L[m]

1
- Ec. (6)
A[m [2] ]

1
- Ec. (7)
A[m [2] ]

Donde,

T : Tasa de emisión ingresadas al modelo de los distintos tipos de fuentes
E : Emisión de cada fuente [t/año]
D : Días por año considerados [días/año]
H : Horas por día considerados [h/día]
L : Largo de la fuente [m]

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 13

A : Área de la fuente [m [2] ]

Cabe señalar que, para la presente modelaciones, se consideraron los siguientes ciclos
temporales para la generación de las tasas:

 Fase Construcción: Operación de 5 días a la semana (261 [días/año]) y 16 [h/día].

 Fase Operación [4] : Operación de 6 días a la semana (313 [días/año]) y 24 [h/día].

El detalle del cálculo de las tasas de emisión se entrega en el Apéndice 5.

El resumen de las emisiones de cada una de las fuentes emisoras ingresadas al modelo se
presentan en las tablas a continuación. Adicionalmente se presentan gráficamente las
fuentes y receptores del modelo:

4 Operación Actual y Proyectada.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 14

TABLA-6: Emisiones del Escenario Construcción

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|AREA_POLY|SRC_1|AREA_NORTE|1,3E-08|9,7E-07|3,1E-06|9,5E-07|4,5E-07|g/s-m2|
|AREA_POLY|SRC_2|AREA_SUR|1,3E-08|9,7E-07|3,1E-06|9,5E-07|4,5E-07|g/s-m2|
|AREA_POLY|SRC_3|DEM_TALLER|0,0E+00|0,0E+00|0,0E+00|2,6E-06|2,6E-07|g/s-m2|
|AREA|SRC_4|DEM_VARIAS_1|0,0E+00|0,0E+00|0,0E+00|1,4E-06|1,4E-07|g/s-m2|
|AREA_POLY|SRC_5|DEM_VARIAS_2|0,0E+00|0,0E+00|0,0E+00|1,4E-06|1,4E-07|g/s-m2|
|AREA_POLY|SRC_6|DEM_VARIOS_3|0,0E+00|0,0E+00|0,0E+00|1,4E-06|1,4E-07|g/s-m2|
|AREA_POLY|SRC_7|DEM_VARIOS_4|0,0E+00|0,0E+00|0,0E+00|1,4E-06|1,4E-07|g/s-m2|
|AREA_POLY|SRC_8|DEM_VARIOS_5|0,0E+00|0,0E+00|0,0E+00|1,4E-06|1,4E-07|g/s-m2|
|AREA_POLY|SRC_9|ACOPIO_M_1|0,0E+00|0,0E+00|0,0E+00|8,2E-09|1,3E-09|g/s-m2|
|AREA_POLY|SRC_10|ACOPIO_M_2|0,0E+00|0,0E+00|0,0E+00|3,5E-07|5,3E-08|g/s-m2|
|AREA_POLY|SRC_11|ACOPIO_EXC|0,0E+00|0,0E+00|0,0E+00|6,6E-06|1,0E-06|g/s-m2|
|AREA|SRC_12|ACOPIO_DEM|0,0E+00|0,0E+00|0,0E+00|5,0E-07|7,6E-08|g/s-m2|
|ROAD|SRC_13|ID01|9,5E-09|3,3E-06|1,6E-07|5,3E-06|1,3E-06|g/s-m|
|ROAD|SRC_14|ID02|6,9E-09|2,4E-06|1,1E-07|3,8E-06|9,5E-07|g/s-m|
|ROAD|SRC_15|ID03|6,8E-09|2,4E-06|1,1E-07|3,8E-06|9,4E-07|g/s-m|
|ROAD|SRC_16|ID04|2,7E-09|9,3E-07|5,1E-08|1,5E-06|3,7E-07|g/s-m|
|ROAD|SRC_17|ID05|2,0E-12|7,0E-10|3,2E-11|7,1E-12|7,1E-12|g/s-m|
|ROAD|SRC_18|ID06|2,3E-10|7,9E-08|3,7E-09|4,9E-08|1,3E-08|g/s-m|
|ROAD|SRC_19|ID07|1,8E-10|6,2E-08|2,9E-09|1,5E-07|3,6E-08|g/s-m|
|ROAD|SRC_20|ID08|1,4E-10|5,0E-08|2,3E-09|6,4E-09|1,9E-09|g/s-m|
|ROAD|SRC_21|ID09|3,6E-11|1,3E-08|5,8E-10|2,0E-08|5,0E-09|g/s-m|
|ROAD|SRC_22|ID10|3,6E-11|1,3E-08|5,8E-10|9,0E-09|2,3E-09|g/s-m|
|ROAD|SRC_23|ID11|6,8E-09|2,4E-06|1,1E-07|2,0E-06|5,1E-07|g/s-m|
|ROAD|SRC_24|ID12|1,2E-09|4,3E-07|2,0E-08|2,9E-08|1,0E-08|g/s-m|
|ROAD|SRC_25|ID13|4,8E-11|1,7E-08|7,8E-10|8,9E-07|2,2E-07|g/s-m|
|ROAD|SRC_26|ID14|4,8E-11|1,7E-08|7,7E-10|3,0E-08|7,3E-09|g/s-m|
|ROAD|SRC_27|ID15|5,1E-11|1,8E-08|8,2E-10|1,8E-07|4,4E-08|g/s-m|
|ROAD|SRC_28|ID16|4,8E-11|1,7E-08|7,7E-10|2,3E-09|6,9E-10|g/s-m|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 15

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_29|ID17|4,9E-09|1,7E-06|7,9E-08|1,7E-07|5,4E-08|g/s-m|
|ROAD|SRC_30|ID18|4,9E-09|1,7E-06|7,9E-08|6,1E-06|1,5E-06|g/s-m|
|ROAD|SRC_31|ID19|4,9E-09|1,7E-06|7,9E-08|1,8E-06|4,4E-07|g/s-m|
|ROAD|SRC_32|ID20|7,2E-09|2,5E-06|1,2E-07|3,8E-07|1,1E-07|g/s-m|
|ROAD|SRC_33|ID21|1,2E-09|4,3E-07|2,0E-08|6,9E-06|1,7E-06|g/s-m|
|ROAD|SRC_34|ID22|6,1E-09|2,1E-06|9,8E-08|8,3E-06|2,0E-06|g/s-m|
|ROAD|SRC_35|ID23|4,9E-09|1,7E-06|7,9E-08|2,8E-07|8,1E-08|g/s-m|
|ROAD|SRC_36|ID24|4,8E-09|1,7E-06|7,8E-08|4,5E-06|1,1E-06|g/s-m|
|ROAD|SRC_37|ID25|5,4E-09|1,9E-06|8,7E-08|1,5E-06|3,9E-07|g/s-m|
|ROAD|SRC_38|ID26|5,7E-09|2,0E-06|9,3E-08|4,8E-06|1,2E-06|g/s-m|
|ROAD|SRC_39|ID27|5,6E-09|1,9E-06|9,0E-08|1,7E-06|4,2E-07|g/s-m|
|ROAD|SRC_40|ID28|5,6E-09|2,0E-06|9,1E-08|1,0E-06|2,6E-07|g/s-m|
|ROAD|SRC_41|ID29|4,8E-09|1,7E-06|7,8E-08|2,0E-05|4,9E-06|g/s-m|
|ROAD|SRC_42|ID30|7,5E-10|2,6E-07|1,2E-08|2,3E-07|5,9E-08|g/s-m|
|ROAD|SRC_43|ID31|2,6E-09|9,2E-07|5,1E-08|2,3E-07|6,5E-08|g/s-m|
|ROAD|SRC_44|ID32|2,6E-09|9,2E-07|5,1E-08|8,1E-07|2,1E-07|g/s-m|
|ROAD|SRC_45|ID33|2,3E-09|7,8E-07|4,4E-08|8,6E-07|2,2E-07|g/s-m|
|ROAD|SRC_46|ID34|2,3E-09|7,9E-07|4,5E-08|8,3E-07|2,1E-07|g/s-m|
|ROAD|SRC_47|ID35|3,7E-10|1,3E-07|6,2E-09|4,4E-06|1,1E-06|g/s-m|
|ROAD|SRC_48|ID36|1,9E-09|6,6E-07|3,8E-08|2,8E-08|1,4E-08|g/s-m|
|ROAD|SRC_49|ID37|1,9E-09|6,6E-07|3,8E-08|2,9E-07|7,7E-08|g/s-m|
|ROAD|SRC_50|ID38|3,8E-10|1,3E-07|6,1E-09|6,5E-07|1,6E-07|g/s-m|
|ROAD|SRC_51|ID39|2,0E-12|7,0E-10|3,2E-11|6,9E-07|1,7E-07|g/s-m|
|ROAD|SRC_52|ID40|2,0E-12|7,0E-10|3,2E-11|7,6E-10|1,9E-10|g/s-m|
|ROAD|SRC_53|ID41|2,0E-12|7,0E-10|3,2E-11|1,6E-09|3,9E-10|g/s-m|
|ROAD|SRC_54|ID42|2,4E-09|8,5E-07|4,7E-08|1,5E-07|4,5E-08|g/s-m|
|ROAD|SRC_55|ID43|5,5E-10|1,9E-07|8,9E-09|1,2E-06|3,0E-07|g/s-m|
|ROAD|SRC_56|ID44|5,5E-10|1,9E-07|8,9E-09|1,0E-06|2,5E-07|g/s-m|
|ROAD|SRC_57|ID45|1,9E-09|6,6E-07|3,8E-08|1,2E-07|3,5E-08|g/s-m|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 16

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_58|ID46|2,4E-09|8,4E-07|4,7E-08|1,7E-06|4,3E-07|g/s-m|
|ROAD|SRC_59|ID47|2,5E-09|8,5E-07|5,0E-08|1,7E-06|4,1E-07|g/s-m|
|ROAD|SRC_60|ID49|6,7E-09|2,4E-06|1,1E-07|5,1E-06|1,2E-06|g/s-m|
|ROAD|SRC_61|ID50|2,0E-12|7,0E-10|3,2E-11|2,4E-07|2,4E-08|g/s-m|
|ROAD|SRC_62|ID51|3,8E-10|1,3E-07|6,1E-09|4,5E-05|4,5E-06|g/s-m|
|ROAD|SRC_63|ID52|9,7E-09|3,4E-06|1,7E-07|1,1E-04|1,1E-05|g/s-m|
|ROAD|SRC_64|ID53|2,4E-09|8,4E-07|4,7E-08|2,6E-05|2,6E-06|g/s-m|
|ROAD|SRC_65|ID54|7,2E-09|2,5E-06|1,2E-07|8,3E-05|8,3E-06|g/s-m|
|ROAD|SRC_66|ID55|1,6E-09|5,7E-07|2,6E-08|1,7E-05|1,8E-06|g/s-m|
|ROAD|SRC_67|ID56|6,2E-10|2,1E-07|1,0E-08|6,4E-06|6,4E-07|g/s-m|
|ROAD|SRC_68|ID57|3,8E-10|1,3E-07|6,4E-09|3,7E-06|3,7E-07|g/s-m|
|ROAD|SRC_69|ID58|2,4E-10|8,5E-08|3,9E-09|2,7E-06|2,7E-07|g/s-m|
|ROAD|SRC_70|ID59|7,9E-11|2,8E-08|1,3E-09|9,5E-07|9,5E-08|g/s-m|
|ROAD|SRC_71|ID60|1,4E-10|5,0E-08|2,3E-09|4,4E-08|4,8E-09|g/s-m|
|POINT|SRC_72|GE1|3,4E-03|5,2E-02|1,1E-02|3,6E-03|3,6E-03|g/s|
|POINT|SRC_73|GE2|2,1E-05|3,2E-04|7,0E-05|2,3E-05|2,3E-05|g/s|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 17

FIGURA-2: Ubicación Fuentes Emisoras y Receptores, Fase de Construcción

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 18

TABLA-7: Emisiones del Escenario Operación Actual

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_1|ID1|7,9E-09|2,5E-06|1,2E-07|1,0E-03|1,0E-04|g/s-m|
|ROAD|SRC_8|ID8|8,0E-09|2,6E-06|1,2E-07|8,1E-06|2,0E-06|g/s-m|
|ROAD|SRC_9|ID9|9,5E-09|3,0E-06|1,5E-07|9,4E-06|2,3E-06|g/s-m|
|ROAD|SRC_10|ID10|1,3E-09|4,2E-07|2,0E-08|4,7E-06|1,1E-06|g/s-m|
|ROAD|SRC_11|ID11|6,8E-09|2,2E-06|1,1E-07|7,1E-06|1,7E-06|g/s-m|
|ROAD|SRC_12|ID12|2,3E-09|7,4E-07|3,7E-08|1,2E-06|3,0E-07|g/s-m|
|ROAD|SRC_13|ID13|2,3E-09|7,1E-07|3,6E-08|1,2E-06|3,0E-07|g/s-m|
|ROAD|SRC_14|ID14|1,0E-10|3,4E-08|1,6E-09|3,6E-07|8,8E-08|g/s-m|
|ROAD|SRC_15|ID15|2,3E-09|7,1E-07|3,6E-08|1,2E-06|3,0E-07|g/s-m|
|ROAD|SRC_16|ID16|2,2E-09|6,8E-07|3,4E-08|1,2E-06|2,9E-07|g/s-m|
|ROAD|SRC_17|ID17|2,2E-09|6,8E-07|3,4E-08|1,2E-06|2,9E-07|g/s-m|
|ROAD|SRC_18|ID18|1,0E-09|3,2E-07|1,7E-08|6,5E-07|1,6E-07|g/s-m|
|ROAD|SRC_19|ID19|9,8E-10|3,0E-07|1,6E-08|6,3E-07|1,5E-07|g/s-m|
|ROAD|SRC_20|ID20|5,1E-10|1,6E-07|8,2E-09|3,3E-07|8,1E-08|g/s-m|
|ROAD|SRC_22|ID22|5,2E-11|1,6E-08|8,1E-10|3,2E-08|7,9E-09|g/s-m|
|ROAD|SRC_23|ID23|3,8E-12|1,2E-09|5,8E-11|3,4E-09|8,3E-10|g/s-m|
|ROAD|SRC_24|ID24|5,3E-11|1,9E-08|8,6E-10|9,0E-08|2,2E-08|g/s-m|
|ROAD|SRC_25|ID25|4,6E-10|1,4E-07|7,4E-09|3,0E-07|7,3E-08|g/s-m|
|ROAD|SRC_26|ID26|2,8E-10|8,7E-08|4,5E-09|1,8E-07|4,4E-08|g/s-m|
|ROAD|SRC_27|ID27|2,8E-10|8,6E-08|4,3E-09|3,8E-07|9,3E-08|g/s-m|
|ROAD|SRC_28|ID28|1,8E-11|5,8E-09|3,5E-10|1,5E-08|3,6E-09|g/s-m|
|ROAD|SRC_29|ID29|1,8E-10|5,5E-08|2,9E-09|2,5E-07|6,0E-08|g/s-m|
|ROAD|SRC_30|ID30|4,8E-11|1,5E-08|7,5E-10|6,6E-08|1,6E-08|g/s-m|
|ROAD|SRC_31|ID31|4,6E-10|1,4E-07|7,6E-09|3,0E-07|7,4E-08|g/s-m|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 19

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_32|ID32|4,4E-10|1,4E-07|6,9E-09|1,9E-06|4,5E-07|g/s-m|
|ROAD|SRC_33|ID33|2,0E-11|5,3E-09|6,4E-10|3,5E-08|8,5E-09|g/s-m|
|ROAD|SRC_34|ID34|1,4E-11|4,4E-09|2,1E-10|3,7E-08|9,0E-09|g/s-m|
|ROAD|SRC_35|ID35|6,6E-10|2,1E-07|1,1E-08|3,3E-07|8,1E-08|g/s-m|
|ROAD|SRC_36|ID36|6,6E-10|2,1E-07|1,1E-08|3,3E-07|8,1E-08|g/s-m|
|ROAD|SRC_37|ID37|6,6E-10|2,1E-07|1,1E-08|3,3E-07|8,1E-08|g/s-m|
|ROAD|SRC_38|ID38|6,6E-10|2,1E-07|1,1E-08|3,3E-07|8,1E-08|g/s-m|
|ROAD|SRC_39|ID39|4,3E-10|1,4E-07|6,5E-09|1,8E-07|4,4E-08|g/s-m|
|ROAD|SRC_41|ID41|2,3E-10|6,8E-08|4,1E-09|3,2E-07|7,9E-08|g/s-m|
|ROAD|SRC_42|ID42|3,0E-10|9,6E-08|4,8E-09|2,8E-07|6,8E-08|g/s-m|
|ROAD|SRC_44|ID44|2,1E-10|6,3E-08|3,5E-09|8,9E-07|2,2E-07|g/s-m|
|ROAD|SRC_46|ID46|4,3E-09|1,4E-06|6,8E-08|2,0E-06|4,9E-07|g/s-m|
|ROAD|SRC_47|ID47|4,3E-09|1,4E-06|6,7E-08|2,0E-06|4,9E-07|g/s-m|
|ROAD|SRC_48|ID48|4,3E-09|1,4E-06|6,7E-08|2,0E-06|4,9E-07|g/s-m|
|ROAD|SRC_49|ID49|3,8E-09|1,2E-06|5,9E-08|1,7E-06|4,3E-07|g/s-m|
|ROAD|SRC_50|ID50|3,7E-09|1,2E-06|5,8E-08|1,7E-06|4,2E-07|g/s-m|
|ROAD|SRC_51|ID51|3,3E-09|1,1E-06|5,1E-08|1,5E-06|3,8E-07|g/s-m|
|ROAD|SRC_52|ID52|1,8E-09|5,9E-07|2,9E-08|7,8E-07|1,9E-07|g/s-m|
|ROAD|SRC_53|ID53|1,7E-09|5,5E-07|2,6E-08|6,9E-07|1,7E-07|g/s-m|
|ROAD|SRC_54|ID54|4,7E-10|1,4E-07|7,6E-09|3,0E-07|7,4E-08|g/s-m|
|ROAD|SRC_55|ID55|4,5E-10|1,4E-07|7,0E-09|2,9E-07|7,0E-08|g/s-m|
|ROAD|SRC_56|ID56|4,5E-10|1,4E-07|7,0E-09|6,1E-07|1,5E-07|g/s-m|
|ROAD|SRC_58|ID58|4,4E-10|1,4E-07|6,6E-09|1,8E-07|4,4E-08|g/s-m|
|ROAD|SRC_60|ID62|1,0E-10|3,3E-08|1,5E-09|3,5E-07|8,6E-08|g/s-m|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 20

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_64|ID66|5,3E-12|1,7E-09|8,3E-11|7,3E-09|1,8E-09|g/s-m|
|ROAD|SRC_66|ID68|5,7E-10|1,8E-07|8,6E-09|2,6E-07|6,4E-08|g/s-m|
|ROAD|SRC_67|ID69|3,6E-09|1,1E-06|5,5E-08|1,7E-06|4,1E-07|g/s-m|
|ROAD|SRC_68|ID70|2,7E-11|9,3E-09|4,3E-10|1,5E-08|3,6E-09|g/s-m|
|ROAD|SRC_69|ID71|4,5E-10|1,4E-07|6,9E-09|4,0E-07|9,8E-08|g/s-m|
|ROAD|SRC_70|ID72|4,5E-10|1,4E-07|6,8E-09|1,2E-06|2,9E-07|g/s-m|
|ROAD|SRC_71|ID72|1,5E-09|4,6E-07|2,2E-08|1,6E-06|3,9E-07|g/s-m|
|ROAD|SRC_72|ID74|1,4E-09|4,5E-07|2,2E-08|1,6E-06|3,9E-07|g/s-m|
|ROAD|SRC_73|ID75|1,4E-09|4,5E-07|2,2E-08|7,4E-07|1,8E-07|g/s-m|
|ROAD|SRC_74|ID79|2,7E-11|9,3E-09|4,3E-10|4,5E-08|1,1E-08|g/s-m|
|ROAD|SRC_75|ID80|2,7E-11|9,3E-09|4,3E-10|4,5E-08|1,1E-08|g/s-m|
|ROAD|SRC_76|ID83|6,6E-12|2,3E-09|1,1E-10|3,7E-09|9,1E-10|g/s-m|
|ROAD|SRC_77|ID84|6,7E-12|2,3E-09|1,1E-10|3,7E-09|9,1E-10|g/s-m|
|ROAD|SRC_79|ID86|1,4E-10|4,5E-08|2,2E-09|2,0E-07|4,8E-08|g/s-m|
|ROAD|SRC_80|ID87|1,2E-09|4,0E-07|1,9E-08|3,9E-07|9,8E-08|g/s-m|
|ROAD|SRC_81|ID88|4,9E-10|1,6E-07|7,4E-09|2,1E-07|5,2E-08|g/s-m|
|ROAD|SRC_82|ID89|4,4E-10|1,4E-07|6,7E-09|3,9E-07|9,6E-08|g/s-m|
|ROAD|SRC_83|ID90|4,4E-11|1,4E-08|6,9E-10|6,0E-08|1,5E-08|g/s-m|
|ROAD|SRC_84|ID91|7,0E-10|2,4E-07|1,1E-08|3,9E-07|9,5E-08|g/s-m|
|ROAD|SRC_85|ID92|7,4E-10|2,6E-07|1,2E-08|4,6E-06|1,1E-06|g/s-m|
|ROAD|SRC_86|ID93|6,7E-12|2,3E-09|1,1E-10|3,7E-09|9,1E-10|g/s-m|
|ROAD|SRC_87|ID94|1,8E-11|4,6E-09|5,6E-10|9,9E-09|2,4E-09|g/s-m|
|ROAD|SRC_88|ID95|3,2E-10|1,0E-07|4,9E-09|8,8E-07|2,1E-07|g/s-m|
|ROAD|SRC_89|ID96|1,2E-10|4,0E-08|1,9E-09|4,8E-08|1,2E-08|g/s-m|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 21

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_91|ID99|4,3E-12|1,1E-09|1,3E-10|7,4E-09|1,8E-09|g/s-m|
|ROAD|SRC_96|ID101|5,5E-13|1,9E-10|8,9E-12|3,1E-10|7,6E-11|g/s-m|
|AREA_POLY|SRC_92|MAQ1|1,8E-08|2,6E-06|4,4E-07|2,0E-08|2,0E-08|g/s-m2|
|AREA_POLY|SRC_93|MAQ2|3,5E-08|5,0E-06|8,5E-07|4,0E-08|4,0E-08|g/s-m2|
|POINT|SRC_94|GE1|4,2E-04|6,5E-03|1,4E-03|4,5E-04|4,5E-04|g/s|
|POINT|SRC_95|GE2|4,2E-04|6,5E-03|1,4E-03|4,5E-04|4,5E-04|g/s|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 22

FIGURA-3: Ubicación Fuentes Emisoras y Receptores, Fase de Operación Actual

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 23

TABLA-8: Emisiones del Escenario Operación Proyectada

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_1|ID1|2,7E-09|8,3E-07|4,3E-08|7,2E-07|1,8E-07|g/s-m|
|ROAD|SRC_2|ID2|2,1E-08|7,3E-06|3,5E-07|8,9E-06|2,2E-06|g/s-m|
|ROAD|SRC_3|ID3|4,5E-08|1,5E-05|7,5E-07|3,0E-05|7,4E-06|g/s-m|
|ROAD|SRC_4|ID4|8,8E-09|3,0E-06|1,5E-07|5,8E-06|1,4E-06|g/s-m|
|ROAD|SRC_5|ID5|6,8E-10|2,4E-07|1,1E-08|3,9E-06|9,6E-07|g/s-m|
|ROAD|SRC_6|ID6|9,1E-09|3,1E-06|1,5E-07|6,0E-06|1,5E-06|g/s-m|
|ROAD|SRC_7|ID7|3,6E-08|1,2E-05|6,0E-07|2,4E-05|6,0E-06|g/s-m|
|ROAD|SRC_8|ID8|2,7E-09|8,4E-07|4,4E-08|3,7E-06|9,1E-07|g/s-m|
|ROAD|SRC_9|ID9|1,2E-08|3,9E-06|1,9E-07|9,6E-06|2,4E-06|g/s-m|
|ROAD|SRC_10|ID10|8,6E-09|3,0E-06|1,4E-07|5,0E-05|1,2E-05|g/s-m|
|ROAD|SRC_11|ID11|2,8E-09|8,8E-07|4,6E-08|3,8E-06|9,3E-07|g/s-m|
|ROAD|SRC_12|ID12|2,2E-08|7,4E-06|3,6E-07|7,2E-06|1,8E-06|g/s-m|
|ROAD|SRC_13|ID13|2,2E-08|7,6E-06|3,7E-07|7,4E-06|1,9E-06|g/s-m|
|ROAD|SRC_14|ID14|8,3E-10|2,8E-07|1,4E-08|4,5E-06|1,1E-06|g/s-m|
|ROAD|SRC_15|ID15|1,6E-08|5,5E-06|2,7E-07|5,5E-06|1,4E-06|g/s-m|
|ROAD|SRC_16|ID16|1,6E-08|5,5E-06|2,7E-07|5,4E-06|1,4E-06|g/s-m|
|ROAD|SRC_17|ID17|1,6E-08|5,3E-06|2,6E-07|5,3E-06|1,3E-06|g/s-m|
|ROAD|SRC_18|ID18|5,3E-09|1,8E-06|8,8E-08|2,0E-06|4,9E-07|g/s-m|
|ROAD|SRC_19|ID19|5,2E-09|1,8E-06|8,6E-08|1,9E-06|4,8E-07|g/s-m|
|ROAD|SRC_20|ID20|4,7E-09|1,6E-06|7,8E-08|1,6E-06|4,0E-07|g/s-m|
|ROAD|SRC_21|ID21|9,4E-09|3,3E-06|1,6E-07|6,2E-06|1,5E-06|g/s-m|
|ROAD|SRC_22|ID22|5,2E-11|1,6E-08|8,2E-10|3,2E-08|8,0E-09|g/s-m|
|ROAD|SRC_23|ID23|4,2E-12|1,3E-09|6,3E-11|3,7E-09|9,0E-10|g/s-m|
|ROAD|SRC_24|ID24|5,3E-11|1,9E-08|8,6E-10|9,0E-08|2,2E-08|g/s-m|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 24

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_25|ID25|4,7E-09|1,6E-06|7,8E-08|1,6E-06|4,0E-07|g/s-m|
|ROAD|SRC_26|ID26|2,8E-10|8,7E-08|4,5E-09|1,8E-07|4,4E-08|g/s-m|
|ROAD|SRC_27|ID27|2,8E-10|8,6E-08|4,3E-09|3,8E-07|9,3E-08|g/s-m|
|ROAD|SRC_28|ID28|1,8E-11|5,8E-09|3,5E-10|1,5E-08|3,6E-09|g/s-m|
|ROAD|SRC_29|ID29|4,4E-09|1,5E-06|7,3E-08|3,0E-06|7,4E-07|g/s-m|
|ROAD|SRC_30|ID30|4,8E-11|1,5E-08|7,5E-10|6,6E-08|1,6E-08|g/s-m|
|ROAD|SRC_31|ID31|4,6E-10|1,4E-07|7,6E-09|3,0E-07|7,4E-08|g/s-m|
|ROAD|SRC_32|ID32|4,4E-10|1,4E-07|6,9E-09|1,9E-06|4,5E-07|g/s-m|
|ROAD|SRC_33|ID33|2,0E-11|5,3E-09|6,4E-10|3,5E-08|8,5E-09|g/s-m|
|ROAD|SRC_34|ID34|1,4E-11|4,4E-09|2,1E-10|3,7E-08|9,0E-09|g/s-m|
|ROAD|SRC_35|ID35|8,0E-09|2,8E-06|1,3E-07|2,6E-06|6,5E-07|g/s-m|
|ROAD|SRC_36|ID36|6,6E-10|2,1E-07|1,1E-08|3,3E-07|8,1E-08|g/s-m|
|ROAD|SRC_37|ID37|2,1E-09|6,9E-07|3,6E-08|7,3E-07|1,8E-07|g/s-m|
|ROAD|SRC_38|ID38|1,5E-09|5,1E-07|2,5E-08|6,0E-07|1,5E-07|g/s-m|
|ROAD|SRC_39|ID39|1,3E-09|4,4E-07|2,1E-08|4,5E-07|1,1E-07|g/s-m|
|ROAD|SRC_40|ID40|1,9E-12|6,5E-10|3,1E-11|1,2E-09|3,0E-10|g/s-m|
|ROAD|SRC_41|ID41|2,3E-10|6,8E-08|4,1E-09|3,2E-07|7,9E-08|g/s-m|
|ROAD|SRC_42|ID42|1,7E-11|4,4E-09|5,3E-10|2,9E-08|7,1E-09|g/s-m|
|ROAD|SRC_43|ID43|1,3E-09|4,4E-07|2,1E-08|9,6E-07|2,4E-07|g/s-m|
|ROAD|SRC_44|ID44|2,1E-10|6,3E-08|3,5E-09|8,9E-07|2,2E-07|g/s-m|
|ROAD|SRC_45|ID45|5,1E-10|1,8E-07|1,0E-08|2,9E-07|7,2E-08|g/s-m|
|ROAD|SRC_46|ID46|2,2E-08|7,5E-06|3,6E-07|7,4E-06|1,8E-06|g/s-m|
|ROAD|SRC_47|ID47|2,0E-08|6,8E-06|3,3E-07|6,8E-06|1,7E-06|g/s-m|
|ROAD|SRC_48|ID48|2,0E-08|6,8E-06|3,3E-07|6,8E-06|1,7E-06|g/s-m|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 25

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_49|ID49|1,9E-08|6,7E-06|3,2E-07|6,6E-06|1,6E-06|g/s-m|
|ROAD|SRC_50|ID50|1,9E-08|6,6E-06|3,2E-07|6,5E-06|1,6E-06|g/s-m|
|ROAD|SRC_51|ID51|1,4E-08|4,7E-06|2,3E-07|4,7E-06|1,2E-06|g/s-m|
|ROAD|SRC_52|ID52|1,1E-08|3,9E-06|1,9E-07|3,7E-06|9,2E-07|g/s-m|
|ROAD|SRC_53|ID53|1,1E-08|3,8E-06|1,8E-07|3,6E-06|9,0E-07|g/s-m|
|ROAD|SRC_54|ID54|1,0E-08|3,4E-06|1,7E-07|3,2E-06|8,1E-07|g/s-m|
|ROAD|SRC_55|ID55|9,9E-09|3,4E-06|1,6E-07|3,2E-06|8,0E-07|g/s-m|
|ROAD|SRC_56|ID56|4,5E-10|1,4E-07|7,0E-09|6,1E-07|1,5E-07|g/s-m|
|ROAD|SRC_57|ID57|7,3E-09|2,5E-06|1,2E-07|1,5E-05|3,6E-06|g/s-m|
|ROAD|SRC_58|ID58|2,3E-09|7,9E-07|3,8E-08|7,6E-07|1,9E-07|g/s-m|
|ROAD|SRC_59|ID61|5,1E-10|1,8E-07|1,0E-08|8,8E-07|2,1E-07|g/s-m|
|ROAD|SRC_60|ID62|1,0E-10|3,3E-08|1,5E-09|5,6E-08|1,4E-08|g/s-m|
|ROAD|SRC_61|ID63|1,9E-09|6,6E-07|3,6E-08|5,4E-07|1,4E-07|g/s-m|
|ROAD|SRC_62|ID64|1,4E-09|4,8E-07|2,5E-08|4,0E-07|1,0E-07|g/s-m|
|ROAD|SRC_63|ID65|5,1E-10|1,8E-07|1,0E-08|1,3E-07|3,5E-08|g/s-m|
|ROAD|SRC_64|ID66|5,3E-12|1,7E-09|8,3E-11|7,3E-09|1,8E-09|g/s-m|
|ROAD|SRC_65|ID67|1,9E-12|6,4E-10|3,1E-11|1,2E-09|3,0E-10|g/s-m|
|ROAD|SRC_66|ID68|5,7E-10|1,8E-07|8,7E-09|2,6E-07|6,5E-08|g/s-m|
|ROAD|SRC_67|ID69|3,6E-09|1,1E-06|5,5E-08|1,7E-06|4,1E-07|g/s-m|
|ROAD|SRC_68|ID70|2,7E-11|9,3E-09|4,3E-10|1,5E-08|3,6E-09|g/s-m|
|ROAD|SRC_69|ID71|5,7E-09|2,0E-06|9,5E-08|3,9E-06|9,5E-07|g/s-m|
|ROAD|SRC_70|ID72|4,5E-10|1,4E-07|6,8E-09|1,2E-06|2,9E-07|g/s-m|
|ROAD|SRC_71|ID72|2,5E-09|8,1E-07|3,9E-08|2,3E-06|5,5E-07|g/s-m|
|ROAD|SRC_72|ID74|2,4E-09|8,0E-07|3,9E-08|2,2E-06|5,5E-07|g/s-m|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 26

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad|
|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_73|ID75|2,4E-09|8,0E-07|3,9E-08|1,0E-06|2,6E-07|g/s-m|
|ROAD|SRC_74|ID79|2,7E-11|9,3E-09|4,3E-10|4,5E-08|1,1E-08|g/s-m|
|ROAD|SRC_75|ID80|2,7E-11|9,3E-09|4,3E-10|4,5E-08|1,1E-08|g/s-m|
|ROAD|SRC_76|ID83|8,0E-12|2,8E-09|1,3E-10|4,6E-09|1,1E-09|g/s-m|
|ROAD|SRC_77|ID84|6,7E-12|2,3E-09|1,1E-10|3,7E-09|9,1E-10|g/s-m|
|ROAD|SRC_78|ID85|1,4E-12|4,8E-10|2,3E-11|2,8E-09|6,8E-10|g/s-m|
|ROAD|SRC_79|ID86|1,4E-10|4,5E-08|2,2E-09|2,0E-07|4,8E-08|g/s-m|
|ROAD|SRC_80|ID87|1,1E-09|3,8E-07|1,8E-08|3,8E-07|9,4E-08|g/s-m|
|ROAD|SRC_81|ID88|4,9E-10|1,6E-07|7,4E-09|2,1E-07|5,2E-08|g/s-m|
|ROAD|SRC_82|ID89|4,4E-10|1,4E-07|6,7E-09|3,9E-07|9,6E-08|g/s-m|
|ROAD|SRC_83|ID90|4,4E-11|1,4E-08|6,9E-10|6,0E-08|1,5E-08|g/s-m|
|ROAD|SRC_84|ID91|6,4E-10|2,3E-07|1,0E-08|3,6E-07|8,8E-08|g/s-m|
|ROAD|SRC_85|ID92|6,8E-10|2,4E-07|1,1E-08|4,2E-06|1,0E-06|g/s-m|
|ROAD|SRC_86|ID93|6,7E-12|2,3E-09|1,1E-10|3,7E-09|9,1E-10|g/s-m|
|ROAD|SRC_87|ID94|1,8E-11|4,6E-09|5,6E-10|9,9E-09|2,4E-09|g/s-m|
|ROAD|SRC_88|ID95|3,2E-10|1,0E-07|4,9E-09|8,8E-07|2,1E-07|g/s-m|
|ROAD|SRC_89|ID96|2,0E-09|6,9E-07|3,3E-08|6,2E-07|1,6E-07|g/s-m|
|ROAD|SRC_90|ID98|7,7E-09|2,7E-06|1,3E-07|4,5E-05|1,1E-05|g/s-m|
|ROAD|SRC_91|ID99|4,3E-12|1,1E-09|1,3E-10|7,4E-09|1,8E-09|g/s-m|
|ROAD|SRC_92|ID102|1,1E-09|3,4E-07|1,6E-08|3,9E-07|9,8E-08|g/s-m|
|ROAD|SRC_93|ID103|1,3E-09|4,6E-07|2,7E-08|1,6E-07|4,3E-08|g/s-m|
|AREA_POLY|SRC_94|MAQ1|1,1E-09|3,4E-07|1,6E-08|3,9E-07|9,8E-08|g/s-m2|
|AREA_POLY|SRC_95|MAQ2|1,3E-09|4,6E-07|2,7E-08|1,6E-07|4,3E-08|g/s-m2|
|POINT|SRC_96|GE1|1,8E-08|2,6E-06|4,4E-07|2,0E-08|2,0E-08|g/s|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 27

|Tipo de Fuente|ID|Descripción|SO<br>2|NO<br>X|CO|PM<br>10|PM<br>2.5|Unidad<br>g/s|
|---|---|---|---|---|---|---|---|---|
|POINT|SRC_97|GE2|3,5E-08|5,0E-06|8,5E-07|4,0E-08|4,0E-08|4,0E-08|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 28

FIGURA-4: Ubicación Fuentes Emisoras y Receptores, Fase de Operación Proyectada

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 29

**1.5.6.** **ANALISIS DE INCERTIDUMBRE**

A partir de los datos meteorológicos del año 2021 para las Estación Pudahuel y Cerro Navia,
se realizó un análisis de estadígrafos, obteniendo los resultados presentados en la tabla a
continuación. Estos resultados son comparados con los rangos de valores esperados
(bondad) para estos estadígrafos según la Guía para el Uso de Modelos de Calidad del Aire
en el SEIA:

TABLA-9: Estadígrafos de ajuste de la modelación meteorológica Estación Pudahuel

|Estadígrafos|Velocidad del Viento [m/s]|Col3|Temperatura [°C]|Col5|
|---|---|---|---|---|
|**Estadígrafos**|**Resultado**|**Bondad**|**Resultado**|**Bondad**|
|**BIAS**|0,74|[-2,5;2,5]|2,46|[-4;4]|
|**MAE**|0,91|≤3|2,94|≤4|
|**RMSE**|1,23|≤3|3,85|≤4,5|
|**Coef. Corr. (r)**|0,73|>0,6|0,90|>0,8|

Fuente: Elaboración propia

TABLA-10: Estadígrafos de ajuste de la modelación meteorológica Estación Cerro Navia

|Estadígrafos|Velocidad del Viento [m/s]|Col3|Temperatura [°C]|Col5|
|---|---|---|---|---|
|**Estadígrafos**|**Resultado**|**Bondad**|**Resultado**|**Bondad**|
|**BIAS**|0,63|[-2,5;2,5]|0,02|[-4;4]|
|**MAE**|0,84|≤3|2,43|≤4|
|**RMSE**|1,14|≤3|3,03|≤4,5|
|**Coef. Corr. (r)**|0,74|>0,6|0,91|>0,8|

Fuente: Elaboración propia

De la tabla anterior, se desprende que tanto los estadígrafos de la velocidad del viento, como
los de temperatura para ambas estaciones, se encuentran dentro de los rangos
recomendados por la Guía para el Uso de Modelos de Calidad del Aire en el SEIA, lo que
denota una incertidumbre aceptable por parte del modelo meteorológico utilizado,
concluyendo que el modelo describe correctamente la meteorología de la zona, validando
en base a esto su utilización como insumo para la modelación de calidad del aire.

**RESULTADOS**

A continuación, se presentan los aportes estimados de las Fase Construcción y Operación
cada uno de los parámetros modelados.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 30

**1.6.1.** **PUNTOS DE MÁXIMA CONCENTRACIÓN (PMC)**

En las tablas a continuación se presentan las coordenadas y aportes de los puntos de máxima
concentración modelada, para cada parámetro y estadístico de las Fases de Construcción,
Operación Actual y Proyectada.

TABLA-11: Coordenadas y concentraciones de los PMC de cada parámetro modelado, Fase

Construcción

|Norma|Parámetro|ID|Coordenadas UTM<br>[m]<br>WGS84 Huso 19S|Col5|Coordenadas<br>LCC [km] Datum<br>NWS-84|Col7|PMC|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|**Norte**|
|MP10|Promedio<br>del Periodo|PMC 1|336.536|6.303.358|0,032|-0,406|6,70|μg/m3N|
|MP10|Percentil 98<br>Diario|PMC 1|336.536|6.303.358|0,032|-0,406|18,72|μg/m3N|
|MP2,5|Promedio<br>del Periodo|PMC 2|336.505|6.303.387|0,002|-0,376|2,82|μg/m3N|
|MP2,5|Percentil 98<br>Diario|PMC 2|336.505|6.303.387|0,002|-0,376|7,46|μg/m3N|
|SO2|Promedio<br>del Periodo|PMC 2|336.505|6.303.387|0,002|-0,376|0,08|μg/m3N|
|SO2|Percentil 99<br>Diario|PMC 3|336.535|6.303.388|0,032|-0,376|0,25|μg/m3N|
|SO2|Percentil<br>98,5 Horario|PMC 2|336.505|6.303.387|0,002|-0,376|0,25|μg/m3N|
|NO2|Promedio<br>del Periodo|PMC 2|336.505|6.303.387|0,002|-0,376|0,60|μg/m3N|
|NO2|Percentil 99<br>Diario|PMC 2|336.505|6.303.387|0,002|-0,376|1,83|μg/m3N|
|NO2|Percentil 99<br>Horario|PMC 4|336.536|6.303.328|0,032|-0,436|8,84|μg/m3N|
|CO|Percentil 99<br>8 Horas|PMC 2|336.505|6.303.387|0,002|-0,376|0,08|mg/m3N|
|CO|Percentil 99<br>Horario|PMC 4|336.536|6.303.328|0,032|-0,436|0,29|mg/m3N|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 31

TABLA-12: Coordenadas y concentraciones de los PMC de cada parámetro modelado, Fase

Operación Actual

|Norma|Parámetro|ID|Coordenadas UTM<br>[m]<br>WGS84 Huso 19S|Col5|Coordenadas<br>LCC [km] Datum<br>NWS-84|Col7|PMC|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|**Norte**|
|MP10|Promedio<br>del Periodo|PMC 1|336.507|6.303.297|0,002|-0,466|64,22|μg/m3N|
|MP10|Percentil 98<br>Diario|PMC 1|336.507|6.303.297|0,002|-0,466|180,61|μg/m3N|
|MP2,5|Promedio<br>del Periodo|PMC 1|336.507|6.303.297|0,002|-0,466|6,54|μg/m3N|
|MP2,5|Percentil 98<br>Diario|PMC 1|336.507|6.303.297|0,002|-0,466|18,24|μg/m3N|
|SO2|Promedio<br>del Periodo|PMC 2|336.504|6.303.477|0,002|-0,286|0,34|μg/m3N|
|SO2|Percentil 99<br>Diario|PMC 2|336.504|6.303.477|0,002|-0,286|0,90|μg/m3N|
|SO2|Percentil<br>98,5 Horario|PMC 2|336.504|6.303.477|0,002|-0,286|1,90|μg/m3N|
|NO2|Promedio<br>del Periodo|PMC 3|336.476|6.303.327|-0,028|-0,436|1,71|μg/m3N|
|NO2|Percentil 99<br>Diario|PMC 4|336.416|6.303.296|-0,088|-0,466|4,33|μg/m3N|
|NO2|Percentil 99<br>Horario|PMC 3|336.476|6.303.327|-0,028|-0,436|1,71|μg/m3N|
|CO|Percentil 99<br>8 Horas|PMC 5|336.446|6.303.296|-0,058|-0,466|0,01|μg/m3N|
|CO|Percentil 99<br>Horario|PMC 5|336.446|6.303.296|-0,058|-0,466|0,03|μg/m3N|

Fuente: Elaboración propia

TABLA-13: Coordenadas y concentraciones de los PMC de cada parámetro modelado, Fase

Operación Proyectada

|Norma|Parámetro|ID|Coordenadas UTM<br>[m]<br>WGS84 Huso 19S|Col5|Coordenadas<br>LCC [km] Datum<br>NWS-84|Col7|PMC|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|**Norte**|
|MP10|Promedio<br>del Periodo|PMC 1|336.154|6.303.331|-0,348|-0,426|9,59|μg/m3N|
|MP10|Percentil 98<br>Diario|PMC 1|336.154|6.303.331|-0,348|-0,426|26,90|μg/m3N|
|MP2,5|Promedio<br>del Periodo|PMC 1|336.154|6.303.331|-0,348|-0,426|2,33|μg/m3N|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 32

|Norma|Parámetro|ID|Coordenadas UTM<br>[m]<br>WGS84 Huso 19S|Col5|Coordenadas<br>LCC [km] Datum<br>NWS-84|Col7|PMC|Unidad|
|---|---|---|---|---|---|---|---|---|
|**Norma**|**Parámetro**|**ID**|**Este**|**Norte**|**Este**|**Norte**|**Norte**|**Norte**|
|**Norma**|Percentil 98<br>Diario|PMC 1|336.154|6.303.331|-0,348|-0,426|6,54|μg/m3N|
|SO2|Promedio<br>del Periodo|PMC 2|336.506|6.303.357|0,002|-0,406|0,01|μg/m3N|
|SO2|Percentil 99<br>Diario|PMC 3|336.475|6.303.357|-0,028|-0,406|0,03|μg/m3N|
|SO2|Percentil<br>98,5 Horario|PMC 4|336.380|6.303.625|-0,118|-0,136|0,08|μg/m3N|
|NO2|Promedio<br>del Periodo|PMC 2|336.506|6.303.357|0,002|-0,406|0,35|μg/m3N|
|NO2|Percentil 99<br>Diario|PMC 3|336.475|6.303.357|-0,028|-0,406|9,63|μg/m3N|
|NO2|Percentil 99<br>Horario|PMC 5|336.566|6.303.328|0,062|-0,436|3,27|μg/m3N|
|CO|Percentil 99<br>8 Horas|PMC 4|336.380|6.303.625|-0,118|-0,136|0,00|μg/m3N|
|CO|Percentil 99<br>Horario|PMC 4|336.380|6.303.625|-0,118|-0,136|0,00|μg/m3N|

Fuente: Elaboración propia

En los Apéndices 2 y 3 se presentan gráficamente los puntos de máximo impacto para las
Fases de Construcción y Operación respectivamente. Cabe señalar que todos los puntos de
máxima concentración se encuentran sobre las obras del Proyecto para ambas fases
evaluadas.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 33

**1.6.2.** **RESULTADOS DE LA MODELACIÓN**

Los resultados de la modelación para cada uno de los parámetros modelados de acuerdo a
los estadísticos definidos en cada una de las normas primarias de calidad del aire evaluado,
para las Fases de Construcción y Operación (Actual y Proyectada) se presentan a
continuación, destacando que la Fase de Operación Proyecta incluye la operación completa
del centro . Cabe señalar que la totalidad de los receptores son de carácter primario, por lo
que no se evalúan las normas secundarias de calidad del aire.

Es importante mencionar que, para la Fase de Operación, la evaluación deberá recaer sobre
la modificación y no sobre el proyecto o actividad existente, sin perjuicio de que la
evaluación de impacto ambiental considerará la suma de los impactos provocados por la
modificación y el proyecto o actividad existente para todos los fines legales pertinentes. Es
por esto que la evaluación se realiza en base a la siguiente ecuación:

Ev. Normativa= Aporte Proyecto+ Situación Sin Proyecto+ Aportes Proyectos con RCA

Respecto al aporte del proyecto indicado en la ecuación, este corresponde a la diferencia
entre la operación proyectada y la operación actual. Por otra parte, la suma de la situación
actual y los aportes de proyectos con RCA aprobada, corresponden a la Línea de Base
Proyectada (LBP). De esta manera la ecuación pasa a ser la siguiente:

Ev. Normativa= Aporte Op. Proyectada−Aporte Op. Actual
⏟ [+ Línea de Base Proyectada] ⏟

Ev. Normativa= Diferencia Operación Proyectada y Actual+ Línea de Base Proyectada

Conforme a lo anterior, en los resultados se presenta adicionalmente una tabla con la
diferencia de los aportes proyectados y actuales de la fase de operación, nombrada como
“Fase de Operación Diferencia”, tomando como premisa que los aportes de la Operación
Actual ya se encuentran dentro de los niveles base de calidad del aire en los receptores
primarios dentro del área de influencia del proyecto y por ende están considerados en la
suma de impactos provocados por el proyecto.

Adicionalmente en los Apéndice 2 y 3 se encuentran los mapas de isoconcentraciones para
cada contaminante y estadístico de las Fases de Construcción y Operación respectivamente.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 34

**1.6.2.1.** **Resultados Fase de Construcción**

TABLA-14: Aportes Modelados a los Receptores, Fase de Construcción

|Receptor*|ID|MP<br>10<br>[μg /m3]|Col4|MP<br>2.5<br>[μg /m3]|Col6|SO<br>2<br>[μg /m3]|Col8|Col9|NO<br>2<br>[μg /m3]|Col11|Col12|CO<br>[mg /m3]|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor***|**ID**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor***|**ID**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|**P99 Diario**|**P98,5 Hr**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P99 Hr**|**P99**<br>**8 Hrs.**|**P99**<br>**Hr**|
|**Receptor***|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**40**|**100**|**200**|**10**|**30**|
|Vivienda La Rambla 1|R1|1,11|6,83|0,36|2,16|0,02|0,10|0,35|0,08|0,49|4,91|0,03|0,14|
|Vivienda La Rambla 2|R2|1,20|7,39|0,38|2,34|0,02|0,10|0,38|0,09|0,55|4,92|0,03|0,13|
|Vivienda La Rambla 3|R3|1,46|8,06|0,47|2,53|0,04|0,20|0,74|0,12|0,54|4,51|0,03|0,13|
|Vivienda La Rambla 4|R4|1,33|7,46|0,42|2,26|0,03|0,17|0,57|0,11|0,54|4,39|0,03|0,13|
|Vivienda La Rambla 5|R5|1,43|7,85|0,46|2,26|0,03|0,13|0,57|0,12|0,57|4,22|0,04|0,13|
|Vivienda La Rambla 6|R6|1,55|7,98|0,50|2,44|0,03|0,15|0,58|0,12|0,62|4,54|0,04|0,13|
|Vivienda La Rambla 7|R7|1,50|8,06|0,49|2,42|0,03|0,19|0,53|0,12|0,59|5,80|0,04|0,14|
|Vivienda La Rambla 8|R8|1,52|7,90|0,50|2,58|0,03|0,16|0,53|0,12|0,66|5,18|0,04|0,15|
|Vivienda La Rambla 9|R9|1,60|8,05|0,53|2,62|0,03|0,14|0,52|0,12|0,68|5,25|0,04|0,15|
|Vivienda La Rambla 10|R10|1,62|7,87|0,55|2,57|0,03|0,13|0,54|0,12|0,67|5,46|0,04|0,16|
|Vivienda La Rambla 11|R11|1,61|7,94|0,54|2,67|0,03|0,13|0,55|0,12|0,64|5,67|0,04|0,16|
|Vivienda La Rambla 12|R12|1,60|7,86|0,54|2,73|0,02|0,13|0,53|0,12|0,60|5,45|0,04|0,16|
|Vivienda La Hacienda|R13|0,91|4,85|0,31|1,57|0,02|0,09|0,33|0,07|0,34|4,00|0,03|0,11|
|R04 (Ruido)|R14|1,58|7,97|0,53|2,52|0,03|0,14|0,54|0,12|0,70|5,20|0,04|0,15|
|R05 (Ruido)|R15|1,11|6,41|0,37|2,10|0,02|0,10|0,42|0,09|0,52|4,81|0,03|0,13|
|R06 (Ruido)|R16|1,29|7,68|0,41|2,35|0,03|0,13|0,51|0,10|0,52|4,10|0,03|0,13|
|Estación Pudahuel|R17|0,01|0,06|0,00|0,02|0,00|0,00|0,01|0,00|0,01|0,06|0,00|0,00|
|Estación Cerro Navia|R18|0,01|0,04|0,00|0,01|0,00|0,00|0,00|0,00|0,01|0,05|0,00|0,00|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 35

**1.6.2.2.** **Resultados Fase de Operación**

TABLA-15: Aportes Modelados a los Receptores, Fase de Operación Actual

|Receptor*|ID|MP<br>10<br>[μg /m3]|Col4|MP<br>2.5<br>[μg /m3]|Col6|SO<br>2<br>[μg /m3]|Col8|Col9|NO<br>2<br>[μg /m3]|Col11|Col12|CO<br>[mg /m3]|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor***|**ID**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor***|**ID**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|**P99 Diario**|**P98,5 Hr**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P99 Hr**|**P99**<br>**8 Hrs.**|**P99**<br>**Hr**|
|**Receptor***|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**40**|**100**|**200**|**10**|**30**|
|Vivienda La Rambla 1|R1|1,96|7,89|0,22|0,91|0,01|0,05|0,18|0,15|0,78|4,51|0,00|0,01|
|Vivienda La Rambla 2|R2|2,17|8,47|0,25|0,98|0,01|0,06|0,19|0,16|0,83|4,56|0,00|0,01|
|Vivienda La Rambla 3|R3|2,65|9,74|0,30|1,12|0,01|0,06|0,20|0,18|0,88|4,52|0,00|0,01|
|Vivienda La Rambla 4|R4|2,88|10,84|0,32|1,22|0,01|0,06|0,20|0,18|0,87|4,46|0,00|0,01|
|Vivienda La Rambla 5|R5|3,38|12,28|0,37|1,36|0,02|0,06|0,21|0,19|0,90|4,57|0,00|0,01|
|Vivienda La Rambla 6|R6|3,97|14,10|0,43|1,50|0,02|0,07|0,21|0,21|0,93|4,67|0,00|0,01|
|Vivienda La Rambla 7|R7|4,79|15,70|0,52|1,71|0,02|0,07|0,22|0,21|0,99|4,60|0,00|0,01|
|Vivienda La Rambla 8|R8|5,88|17,67|0,63|1,95|0,02|0,08|0,23|0,23|1,14|5,79|0,00|0,01|
|Vivienda La Rambla 9|R9|7,21|22,83|0,77|2,36|0,02|0,09|0,26|0,25|1,22|8,05|0,00|0,01|
|Vivienda La Rambla 10|R10|13,68|52,56|1,45|5,41|0,02|0,09|0,30|0,31|1,30|9,22|0,00|0,02|
|Vivienda La Rambla 11|R11|16,99|70,76|1,81|7,30|0,02|0,10|0,31|0,33|1,41|7,90|0,00|0,01|
|Vivienda La Rambla 12|R12|19,02|62,62|2,15|6,87|0,03|0,10|0,32|0,36|1,45|8,03|0,00|0,01|
|Vivienda La Hacienda|R13|11,08|46,64|1,18|4,85|0,02|0,07|0,31|0,29|0,92|6,36|0,00|0,01|
|R04 (Ruido)|R14|9,56|37,07|1,02|3,86|0,02|0,09|0,28|0,28|1,30|8,14|0,00|0,01|
|R05 (Ruido)|R15|4,64|16,39|0,51|1,76|0,02|0,08|0,22|0,21|1,09|6,35|0,00|0,01|
|R06 (Ruido)|R16|2,39|9,03|0,27|1,05|0,01|0,06|0,19|0,17|0,86|4,45|0,00|0,01|
|Estación Pudahuel|R17|0,09|0,30|0,01|0,04|0,00|0,00|0,01|0,00|0,01|0,09|0,00|0,00|
|Estación Cerro Navia|R18|0,06|0,21|0,01|0,03|0,00|0,00|0,01|0,00|0,01|0,07|0,00|0,00|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 36

TABLA-16: Aportes Modelados a los Receptores, Fase de Operación Proyectada

|Receptor*|ID|MP<br>10<br>[μg /m3]|Col4|MP<br>2.5<br>[μg /m3]|Col6|SO<br>2<br>[μg /m3]|Col8|Col9|NO<br>2<br>[μg /m3]|Col11|Col12|CO<br>[mg /m3]|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor***|**ID**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor***|**ID**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|**P99 Diario**|**P98,5 Hr**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P99 Hr**|**P99**<br>**8 Hrs.**|**P99**<br>**Hr**|
|**Receptor***|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**40**|**100**|**200**|**10**|**30**|
|Vivienda La Rambla 1|R1|0,71|3,80|0,18|0,94|0,00|0,01|0,02|0,04|0,23|1,60|0,00|0,00|
|Vivienda La Rambla 2|R2|0,76|3,86|0,19|0,95|0,00|0,01|0,02|0,05|0,25|1,65|0,00|0,00|
|Vivienda La Rambla 3|R3|0,84|4,03|0,21|0,99|0,00|0,01|0,02|0,05|0,26|1,83|0,00|0,00|
|Vivienda La Rambla 4|R4|0,81|3,83|0,20|0,95|0,00|0,01|0,02|0,05|0,25|1,55|0,00|0,00|
|Vivienda La Rambla 5|R5|0,89|3,93|0,22|0,97|0,00|0,01|0,03|0,06|0,29|1,54|0,00|0,00|
|Vivienda La Rambla 6|R6|0,99|4,61|0,24|1,14|0,00|0,01|0,03|0,06|0,31|1,65|0,00|0,00|
|Vivienda La Rambla 7|R7|0,99|4,79|0,25|1,18|0,00|0,01|0,03|0,06|0,33|1,67|0,00|0,00|
|Vivienda La Rambla 8|R8|1,06|5,00|0,26|1,23|0,00|0,01|0,03|0,07|0,34|1,80|0,00|0,00|
|Vivienda La Rambla 9|R9|1,14|4,93|0,28|1,22|0,00|0,01|0,03|0,07|0,34|1,83|0,00|0,00|
|Vivienda La Rambla 10|R10|1,28|5,27|0,32|1,30|0,00|0,01|0,03|0,08|0,36|1,83|0,00|0,00|
|Vivienda La Rambla 11|R11|1,39|5,56|0,34|1,37|0,00|0,01|0,03|0,08|0,34|1,74|0,00|0,00|
|Vivienda La Rambla 12|R12|1,80|6,19|0,44|1,53|0,00|0,01|0,03|0,09|0,33|1,69|0,00|0,00|
|Vivienda La Hacienda|R13|1,09|3,59|0,27|0,88|0,00|0,01|0,02|0,07|0,24|1,22|0,00|0,00|
|R04 (Ruido)|R14|1,18|4,93|0,29|1,22|0,00|0,01|0,03|0,08|0,33|1,88|0,00|0,00|
|R05 (Ruido)|R15|0,86|4,00|0,21|0,99|0,00|0,01|0,03|0,05|0,28|1,66|0,00|0,00|
|R06 (Ruido)|R16|0,79|3,87|0,19|0,96|0,00|0,01|0,02|0,05|0,26|1,68|0,00|0,00|
|Estación Pudahuel|R17|0,08|0,20|0,02|0,05|0,00|0,00|0,00|0,01|0,02|0,07|0,00|0,00|
|Estación Cerro Navia|R18|0,05|0,14|0,01|0,03|0,00|0,00|0,00|0,00|0,01|0,04|0,00|0,00|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 37

TABLA-17: Aportes Modelados a los Receptores, Fase de Operación Diferencia [5]

|Receptor*|ID|MP<br>10<br>[μg /m3]|Col4|MP<br>2.5<br>[μg /m3]|Col6|SO<br>2<br>[μg /m3]|Col8|Col9|NO<br>2<br>[μg /m3]|Col11|Col12|CO<br>[mg /m3]|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor***|**ID**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor***|**ID**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|**P99 Diario**|**P98,5 Hr**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P99 Hr**|**P99**<br>**8 Hrs.**|**P99**<br>**Hr**|
|**Receptor***|**Norma**|**50**|**130**|**20**|**50**|**60**|**150**|**350**|**40**|**100**|**200**|**10**|**30**|
|Vivienda La Rambla 1|R1|0,00|0,00|0,00|0,02|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 2|R2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 3|R3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 4|R4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 5|R5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 6|R6|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 7|R7|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 8|R8|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 9|R9|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 10|R10|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 11|R11|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 12|R12|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Hacienda|R13|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|R04 (Ruido)|R14|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|R05 (Ruido)|R15|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|R06 (Ruido)|R16|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Estación Pudahuel|R17|0,00|0,00|0,01|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Estación Cerro Navia|R18|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

Fuente: Elaboración propia

5 Valores que en la resta de los aportes de Operación Actual y Proyectada resulten ser negativos, se presentan como cero (0,00), de manera de representar que no se
posee un incremento en los aportes de la operación del proyecto.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 38

**CUMPLIMIENTO DE NORMATIVA**

Antes de realizar el análisis normativo, es debido indicar que el Proyecto se encuentra dentro de
una zona declarada saturada en Material Particulado Respirable, Monóxido de Carbono (CO) y
Material Particulado Fino (MP 2,5 ); y latente en Dióxido de Nitrógeno (NO 2 ) en base los decretos
D.S. N°131/1996 y D.S. N°67/2014. Producto de esto se publicó el D.S. N°31/2016 que “Establece
Plan de Prevención y Descontaminación Atmosférica Para la Región Metropolitana de Santiago”.
Estas superaciones se pueden evidenciar en las líneas base de las estaciones de calidad del aire
consideradas en el presente estudio.

Lo anterior indica que en esta zona existe un riesgo preexistente de calidad del aire. Sin embargo,
la “Guía de Riesgo Para la Salud de Las Personas” del SEA indica lo siguiente:

“ _El hecho de que exista un área con riesgo preexistente de conformidad a los supuestos N°1 y N°2_
_descritos, no significa que se generen de forma automática los ECC del artículo 11, letra a), de la Ley_
_N°19.300 sino que, dicho escenario debe ser considerado por el titular y se debe realizar el análisis_
_de significancia para el contaminante respectivo. En esta línea, solo en el caso que se determine que_
_el aporte del proyecto generará un aumento o disminución significativo --según corresponda-- en_
_la concentración del contaminante en análisis, por sobre los valores establecidos en la norma de_
_calidad de que se trate, se estará en presencia del ECC del artículo 11, letra a), de la Ley N°19.300”_

De esta manera, el análisis normativo de los aportes del Proyecto, bajo un contexto de riesgo
preexistente, radicaría en el análisis de la significancia de dichos aportes. Referente a esto, el SEA
publicó el documento “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de emisiones en zonas
saturadas por material particulado respirable MP10 y material particulado fino respirable MP2,5”
con fecha septiembre de 2023. En este documento se presentan los umbrales de significancia de
los aportes de MP 2,5 y MP 10 para cada estadístico normado, los cuales dependen del periodo de
exposición a dicho aporte. En la siguiente tabla se presentan dichos valores acorde a las
temporalidades del proyecto, es decir 15 meses para la Fase de Construcción y más de 3 años para
la Fase de Operación:

TABLA-18: Criterios de significancia de incremento en la calidad del aire de MP10 y MP2,5 en

Zonas Saturadas

|Fase|Duración Impacto|MP (μg /m3)<br>10|Col4|MP (μg /m3)<br>2,5|Col6|
|---|---|---|---|---|---|
|**Fase**|**Duración Impacto**|**24 horas**|**Anual**|**24 horas**|**Anual**|
|Construcción|15 meses|10,00|2,40|4,10|0,79|
|Operación|>3 años|5,00|1,00|1,71|0,33|

Fuente: CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de emisiones en zonas saturadas por material particulado

respirable MP10 y material particulado fino respirable MP2,5, 2023.

Referente a los demás contaminantes (NO 2, CO y SO 2 ), el SEA en conjunto con el DICTUC,
publicaron el documento “Evaluación significancia del impacto de las emisiones de un Proyecto o
Actividad en Zonas Saturadas en el SEIA”, con fecha marzo del año 2022. En este documento se

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 39

presentan los niveles significativos de incremento de concentración ( _Significant Impact Level_ en
inglés _,_ SIL), diseñados en base a metodología US/EPA y que se construyen en base a porcentajes
de la norma, generando concentraciones umbrales de significancia, las cuales se presentan en la
siguiente tabla:

TABLA-19: Criterios de Significancia de Aportes asociado a SIL (US/EPA)

|Contaminante|Periodo|SIL porcentual<br>US. EPA|Incremento en<br>concentración<br>[μg/m3]|
|---|---|---|---|
|MP2,5|24 horas|3,4%|1,71|
|MP2,5|Anual|1,7%|0,33|
|MP10|24 horas|3,3%|5,00|
|MP10|Anual|2,0%|1,00|
|NO2|1 hora|4,0%|16,00|
|NO2|Anual|1,0%|1,00|
|CO|1 hora|5,0%|1.500,00|
|CO|8 horas|4,9%|488,89|
|SO2|1 hora|4,0%|14,00|
|SO2|24 horas|1,4%|2,04|
|SO2|Anual|2,0%|1,20|

Fuente: DICTUC, 2022.

En base a lo anterior, a continuación, se presentan las tablas de evaluación de cumplimiento
normativo para cada parámetro medido por las estaciones de monitoreo consideradas, en las
cuales se comparan los aportes del Proyecto respecto de la línea de base proyectada y la
significancia de este para material particulado y gases. Adicionalmente se realiza el análisis de
significancia para los receptores de carácter primario del presente estudio. Finalmente es
importante señalar, que la evaluación de la Fase de Operación se realiza en base al “Escenario Fase
Operación Diferencia” en base a lo planteado en el punto 1.6.2 del presente documento.

**1.7.1.** **ESTACIONES DE CALIDAD DEL AIRE**

A continuación, se presenta el análisis de cumplimiento normativo de las estaciones de calidad del
aire para cada fase:

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 40

TABLA-20: Análisis Normativo en Estaciones de Monitoreo, Fase de Construcción

|Estación|Cont.|Estadístico|Unidad|Aporte<br>(AP)|Línea de<br>base<br>Proyectada<br>(LBP)|Suma<br>AP + LBP|Norma|% AP<br>c/r<br>Norma|% Total<br>c/r<br>Norma|Umbral<br>Significancia|% AP c/r<br>SIL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cerro**<br>**Navia**|**MP10 **|**Percentil 98**<br>**Diario**|**μg/m3N **|0,04|189|189,04|130|0,03%|145%|10|0,40%|
|**Cerro**<br>**Navia**|**MP10 **|**Promedio**<br>**Anual**|**μg/m3N **|0,01|70|70,01|50|0,02%|140%|2,4|0,42%|
|**Cerro**<br>**Navia**|**MP2,5 **|**Percentil 98**<br>**Diario**|**μg/m3N **|0,01|107|107,01|50|0,02%|214%|4,1|0,24%|
|**Cerro**<br>**Navia**|**MP2,5 **|**Promedio**<br>**Anual**|**μg/m3N **|0,00|29|29,00|20|0,00%|145%|0,79|0,00%|
|**Cerro**<br>**Navia**|**NO2 **|**Percentil 99**<br>**Max 1 Hora**|**μg/m3N **|0,05|180|180,05|200|0,03%|90%|16|0,31%|
|**Cerro**<br>**Navia**|**NO2 **|**Promedio**<br>**Anual**|**μg/m3N **|0,00|38|38,00|40|0,00%|95%|1|0,00%|
|**Cerro**<br>**Navia**|**NO2 **|**Percentil 99**<br>**Diario**|**μg/m3N **|0,01|100|100,01|100|0,01%|100%|-|-|
|**Cerro**<br>**Navia**|**CO**|**Percentil 99**<br>**Max 1 Hora**|**mg/m3N **|0,00|10|10,00|30|0,00%|33%|1,5|0,00%|
|**Cerro**<br>**Navia**|**CO**|**Percentil 99**<br>**Max 8 Hora**|**mg/m3N **|0,05|8|8,05|10|0,50%|81%|0,48889|10,23%|
|**Pudahuel**|**MP10 **|**Percentil 98**<br>**Diario**|**μg/m3N **|0,06|177|177,06|130|0,05%|136%|4,29|1,40%|
|**Pudahuel**|**MP10 **|**Promedio**<br>**Anual**|**μg/m3N **|0,01|64|64,01|50|0,02%|128%|1|1,00%|
|**Pudahuel**|**MP2,5 **|**Percentil 98**<br>**Diario**|**μg/m3N **|0,02|103|103,02|50|0,04%|206%|1,71|1,17%|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 41

|Estación|Cont.|Estadístico|Unidad|Aporte<br>(AP)|Línea de<br>base<br>Proyectada<br>(LBP)|Suma<br>AP + LBP|Norma|% AP<br>c/r<br>Norma|% Total<br>c/r<br>Norma|Umbral<br>Significancia|% AP c/r<br>SIL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||**Promedio**<br>**Anual**|**μg/m3N **|0,00|27|27,00|20|0,00%|135%|0,33|0,00%|
||**NO2 **|**Percentil 99**<br>**Max 1 Hora**|**μg/m3N **|0,01|188|188,01|200|0,01%|94%|16|0,06%|
||**NO2 **|**Promedio**<br>**Anual**|**μg/m3N **|0,00|36|36,00|40|0,00%|90%|1|0,00%|
||**NO2 **|**Percentil 99**<br>**Diario**|**μg/m3N **|0,01|101|101,01|100|0,01%|101%|-|-|
||**CO**|**Percentil 99**<br>**Max 1 Hora**|**mg/m3N **|0,00|11|11,00|30|0,00%|37%|1,5|0,00%|
||**CO**|**Percentil 99**<br>**Max 8 Hora**|**mg/m3N **|0,00|8|8,00|10|0,00%|80%|0,48889|0,00%|

Fuente: Elaboración propia

TABLA-21: Análisis Normativo en Estaciones de Monitoreo, Fase de Operación

|Estación|Cont.|Estadístico|Unidad|Aporte<br>(AP)|Línea de<br>base<br>Proyectada<br>(LBP)|Suma<br>AP + LBP|Norma|% AP<br>c/r<br>Norma|% Total<br>c/r<br>Norma|Umbral<br>Significancia|% AP c/r<br>SIL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cerro**<br>**Navia**|**MP10 **|**Percentil 98**<br>**Diario**|**μg/m3N **|0,00|189|189,00|130|0,00%|145%|10|0,00%|
|**Cerro**<br>**Navia**|**MP10 **|**Promedio**<br>**Anual**|**μg/m3N **|0,00|70|70,00|50|0,00%|140%|2,4|0,00%|
|**Cerro**<br>**Navia**|**MP2,5 **|**Percentil 98**<br>**Diario**|**μg/m3N **|0,01|107|107,01|50|0,02%|214%|4,1|0,24%|
|**Cerro**<br>**Navia**|**MP2,5 **|**Promedio**<br>**Anual**|**μg/m3N **|0,00|29|29,00|20|0,00%|145%|0,79|0,00%|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 42

|Estación|Cont.|Estadístico|Unidad|Aporte<br>(AP)|Línea de<br>base<br>Proyectada<br>(LBP)|Suma<br>AP + LBP|Norma|% AP<br>c/r<br>Norma|% Total<br>c/r<br>Norma|Umbral<br>Significancia|% AP c/r<br>SIL|
|---|---|---|---|---|---|---|---|---|---|---|---|
||**NO2 **|**Percentil 99**<br>**Max 1 Hora**|**μg/m3N **|0,00|180|180,00|200|0,00%|90%|16|0,00%|
||**NO2 **|**Promedio**<br>**Anual**|**μg/m3N **|0,00|38|38,00|40|0,00%|95%|1|0,00%|
||**NO2 **|**Percentil 99**<br>**Diario**|**μg/m3N **|0,00|100|100,00|100|0,00%|100%|-|-|
||**CO**|**Percentil 99**<br>**Max 1 Hora**|**mg/m3N **|0,00|10|10,00|30|0,00%|33%|1,5|0,00%|
||**CO**|**Percentil 99**<br>**Max 8 Hora**|**mg/m3N **|0,00|8|8,00|10|0,00%|80%|0,48889|0,00%|
|**Pudahuel**|**MP10 **|**Percentil 98**<br>**Diario**|**μg/m3N **|0,00|177|177,00|130|0,00%|136%|4,29|0,00%|
|**Pudahuel**|**MP10 **|**Promedio**<br>**Anual**|**μg/m3N **|0,00|64|64,00|50|0,00%|128%|1|0,00%|
|**Pudahuel**|**MP2,5 **|**Percentil 98**<br>**Diario**|**μg/m3N **|0,01|103|103,01|50|0,02%|206%|1,71|0,58%|
|**Pudahuel**|**MP2,5 **|**Promedio**<br>**Anual**|**μg/m3N **|0,01|27|27,01|20|0,05%|135%|0,33|3,03%|
|**Pudahuel**|**NO2 **|**Percentil 99**<br>**Max 1 Hora**|**μg/m3N **|0,00|188|188,00|200|0,00%|94%|16|0,00%|
|**Pudahuel**|**NO2 **|**Promedio**<br>**Anual**|**μg/m3N **|0,00|36|36,00|40|0,00%|90%|1|0,00%|
|**Pudahuel**|**NO2 **|**Percentil 99**<br>**Diario**|**μg/m3N **|0,01|101|101,01|100|0,01%|101%|-|-|
|**Pudahuel**|**CO**|**Percentil 99**<br>**Max 1 Hora**|**mg/m3N **|0,00|11|11,00|30|0,00%|37%|1,5|0,00%|

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 43

|Estación|Cont.|Estadístico|Unidad|Aporte<br>(AP)|Línea de<br>base<br>Proyectada<br>(LBP)|Suma<br>AP + LBP|Norma|% AP<br>c/r<br>Norma|% Total<br>c/r<br>Norma|Umbral<br>Significancia|% AP c/r<br>SIL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||**Percentil 99**<br>**Max 8 Hora**|**mg/m3N **|0,00|8|8,00|10|0,00%|80%|0,48889|0,00%|

Fuente: Elaboración propia

.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 44

Cabe señalar, que ambas estaciones poseen superación de la norma para los estadísticos de
MP 10 y MP 2,5, sin embargo, como se explicó anteriormente, la zona posee un riesgo
preexistente, el cual se evidencia en las líneas base de dichos contaminantes, las cuales por
si solas ya están por sobre los límites normativos. En base a lo anterior, .es necesario evaluar
la significancia de los aportes, los cuales no superan para ningún contaminante los umbrales
de significancia presentados anteriormente, por ende, los aportes generados por las Fases
de Construcción y Operación en las Estaciones Pudahuel y Cerro Navia, no son significativos.

**1.7.2.** **RECEPTORES PRIMARIOS**

A continuación, se presenta el análisis de significancia de los aportes en los receptores
primarios. En las tablas siguientes, para cada Fase, se presentan los aportes, en comparación
con el umbral de significancia bajo el criterio de evaluación en el SEIA para MP 2,5 y MP 10 y
bajo la metodología SIL de la US/EPA para gases. Como se puede observar, ningún aporte
en los receptores supera estos umbrales, para ningún contaminante. Bajo este criterio, los
aportes del proyecto en sus Fases de Construcción y Operación no son de carácter
significativo.

.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 45

TABLA-22: Aportes Modelados en los Receptores comparado con los valores de significancia de incremento en la calidad del aire,

Fase de Construcción

|Receptor*|ID|MP<br>10<br>[μg /m3]|Col4|MP<br>2.5<br>[μg /m3]|Col6|SO<br>2<br>[μg /m3]|Col8|Col9|NO<br>2<br>[μg /m3]|Col11|CO<br>[mg /m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor***|**ID**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor***|**ID**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|**P99 Diario**|**P98,5 Hr**|**Media**<br>**Anual**|**P99 Hr**|**P99**<br>**8 Hrs.**|**P99**<br>**Hr**|
|**Receptor***|**Umbral**|**2,4**|**10**|**0,79**|**4,1**|**1,2**|**2,04**|**14**|**1 **|**16**|**0,489**|**1,5**|
|Vivienda La Rambla 1|R1|1,11|6,83|0,36|2,16|0,02|0,10|0,35|0,08|4,91|0,03|0,14|
|Vivienda La Rambla 2|R2|1,20|7,39|0,38|2,34|0,02|0,10|0,38|0,09|4,92|0,03|0,13|
|Vivienda La Rambla 3|R3|1,46|8,06|0,47|2,53|0,04|0,20|0,74|0,12|4,51|0,03|0,13|
|Vivienda La Rambla 4|R4|1,33|7,46|0,42|2,26|0,03|0,17|0,57|0,11|4,39|0,03|0,13|
|Vivienda La Rambla 5|R5|1,43|7,85|0,46|2,26|0,03|0,13|0,57|0,12|4,22|0,04|0,13|
|Vivienda La Rambla 6|R6|1,55|7,98|0,50|2,44|0,03|0,15|0,58|0,12|4,54|0,04|0,13|
|Vivienda La Rambla 7|R7|1,50|8,06|0,49|2,42|0,03|0,19|0,53|0,12|5,80|0,04|0,14|
|Vivienda La Rambla 8|R8|1,52|7,90|0,50|2,58|0,03|0,16|0,53|0,12|5,18|0,04|0,15|
|Vivienda La Rambla 9|R9|1,60|8,05|0,53|2,62|0,03|0,14|0,52|0,12|5,25|0,04|0,15|
|Vivienda La Rambla 10|R10|1,62|7,87|0,55|2,57|0,03|0,13|0,54|0,12|5,46|0,04|0,16|
|Vivienda La Rambla 11|R11|1,61|7,94|0,54|2,67|0,03|0,13|0,55|0,12|5,67|0,04|0,16|
|Vivienda La Rambla 12|R12|1,60|7,86|0,54|2,73|0,02|0,13|0,53|0,12|5,45|0,04|0,16|
|Vivienda La Hacienda|R13|0,91|4,85|0,31|1,57|0,02|0,09|0,33|0,07|4,00|0,03|0,11|
|R04 (Ruido)|R14|1,58|7,97|0,53|2,52|0,03|0,14|0,54|0,12|5,20|0,04|0,15|
|R05 (Ruido)|R15|1,11|6,41|0,37|2,10|0,02|0,10|0,42|0,09|4,81|0,03|0,13|
|R06 (Ruido)|R16|1,29|7,68|0,41|2,35|0,03|0,13|0,51|0,10|4,10|0,03|0,13|
|Estación Pudahuel|R17|0,01|0,06|0,00|0,02|0,00|0,00|0,01|0,00|0,06|0,00|0,00|
|Estación Cerro Navia|R18|0,01|0,04|0,00|0,01|0,00|0,00|0,00|0,00|0,05|0,00|0,00|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 46

TABLA-23: Aportes Modelados en los Receptores comparado con los valores de significancia de incremento en la calidad del aire,

Fase de Operación

|Receptor*|ID|MP<br>10<br>[μg /m3]|Col4|MP<br>2.5<br>[μg /m3]|Col6|SO<br>2<br>[μg /m3]|Col8|Col9|NO<br>2<br>[μg /m3]|Col11|CO<br>[mg /m3]|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor***|**ID**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor***|**ID**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|**P99 Diario**|**P98,5 Hr**|**Media Anual**|**P99 Hr**|**P99**<br>**8 Hrs.**|**P99**<br>**Hr**|
|**Receptor***|**Umbral**|**1 **|**5 **|**0,33**|**1,71**|**1,2**|**2,04**|**14**|**1 **|**16**|**0,489**|**1,5**|
|Vivienda La Rambla 1|R1|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 2|R2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 3|R3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 4|R4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 5|R5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 6|R6|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 7|R7|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 8|R8|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 9|R9|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 10|R10|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 11|R11|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Rambla 12|R12|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Vivienda La Hacienda|R13|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|R04 (Ruido)|R14|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|R05 (Ruido)|R15|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|R06 (Ruido)|R16|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Estación Pudahuel|R17|0,00|0,00|0,01|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|Estación Cerro Navia|R18|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

Fuente: Elaboración propia

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 47

**ÁREA DE INFLUENCIA CALIDAD DEL AIRE**

Se define el Área de influencia de Calidad del Aire como la superficie resultante de la
superposición de las isolíneas de concentración de todos los parámetros considerados en la
modelación CALPUFF, efectuada para el presente Proyecto, en sus Fases de Construcción y
Operación, con la finalidad de definir si se genera o presenta alguno de los efectos,
características o circunstancias del artículo 11 de la Ley, o para justificar la inexistencia de
dichos efectos, características o circunstancias.

Finalmente, el área de influencia ha sido elaborada considerando como metodología de
desarrollo lo señalado por el DICTUC en su informe denominado “Evaluación significancia
del impacto de las emisiones de un Proyecto o Actividad en Zonas Saturadas en el SEIA”,
publicada en marzo del año 2022, cuyos criterios han sido considerado como los
porcentajes de corte de las isocurvas de concentración para la elaboración del área de
influencia del Proyecto. En particular, estos criterios de corte consideran los valores, donde
se presentan los niveles significativos de incremento de concentración ( _Significant Impact_
_Level_ en inglés _,_ SIL), diseñados en base a metodología US. EPA. Dichos valores se encuentran
en la sección 1.7. Es importante destacar que dichos valores son iguales o menores a los
indicados en el documento documento “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de
emisiones en zonas saturadas por material particulado respirable MP10 y material
particulado fino respirable MP2,5”, manteniendo un carácter conservador.

A continuación, se presenta el Área de influencia de Calidad del Aire del Proyecto en base a
la metodología descrita anteriormente:

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 48

FIGURA-5: Área de Influencia Calidad del Aire del Proyecto

Fuente: Elaboración propia

Como se muestra, el área de influencia contiene principalmente las obras del proyecto,
caminos de acceso y sus alrededores. Si bien, esta engloba receptores primarios, en el punto
1.7 del presente informe se descarta que el proyecto genere aportes significativos en dicho

receptores.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 49

**CONCLUSIONES**

De los resultados obtenidos en la modelación atmosférica de emisiones, correspondientes
a las Fases de Construcción y Operación, se concluye que el Proyecto no generará un aporte
incremental significativo en las concentraciones ambientales de material particulado y gases
en los receptores considerados en el estudio con respecto a la Línea Base Proyectada, las
normas de calidad primaria nacionales vigentes y el análisis de significancia en base a los
criterios de evaluación en el SEIA y la metodología SIL de la EPA, para la evaluación en zonas
saturadas.

Respecto al área de influencia de calidad del aire, esta contiene principalmente las obras del
proyecto, caminos de acceso y sus alrededores. Si bien, esta engloba ciertos receptores
primarios, se descarta que el proyecto genere aportes significativos en dicho receptores.

Dado lo anterior, se concluye que el Proyecto en su escenario más desfavorable para las
Fases de Construcción y Operación, no produce impactos significativos sobre la salud de las
personas, dado que los aportes del Proyecto no modifican significativamente la condición
de calidad del aire de su entorno.

ANEXO ADC-4.15 ACTUALIZACIÓN MODELACIÓN CALIDAD DEL AIRE 50