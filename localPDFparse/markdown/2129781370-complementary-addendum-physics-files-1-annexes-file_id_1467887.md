---
title: Sin título
author: usuario
date: D:20160428180548-03'00'
language: es
type: report
pages: 69
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACION ATMOSFÉRICA. DECLARACIÓN DE IMPACTO AMBIENTAL “REGULARIZACIÓN Y CONTINUIDAD PLANTA DE ASFALTO E IMPLEMENTACIÓN DE EXTRACCIÓN Y PROCESAMIENTO DE ÁRIDOS”
-->

# MODELACION ATMOSFÉRICA. DECLARACIÓN DE IMPACTO AMBIENTAL “REGULARIZACIÓN Y CONTINUIDAD PLANTA DE ASFALTO E IMPLEMENTACIÓN DE EXTRACCIÓN Y PROCESAMIENTO DE ÁRIDOS”

**ABRIL DE 2016**

**ÍNDICE GENERAL**

**1.** **Introducción** ............................................................................................... 7

**2.** **Marco Legas Aplicable** ................................................................................ 9

**3.** **Antecedentes Calidad del Aire Temuco y Padre Las Casas** ...................... 10

**3.1** **Línea de Base** ................................................................................... 13

**4.** **Modelo Calpuff** ........................................................................................... 14

**5.** **Metodología** ............................................................................................... 15

**5.1** **Implementación del modelo meteorológico CALMET: Recopilación y**

**procesamiento de datos meteorológicos, topográficos y de uso de suelo**

**del área de estudio** ........................................................................................ 16

**5.1.1** **Dominio de Modelación de CALMET** ............................................. 16

**5.1.2** **Información meteorológica y geofísica** ....................................... 17

**5.1** . **3** **Procesamiento de datos en CALMET** ............................................ 18

**5.2** **Recopilación y procesamiento del escenario de emisión propuesto**

**para la modelación en CALPUFF** ................................................................... 19

**5.2.1.** **Dominio de la Modelación de CALPUFF** ........................................ 19

**5.2.2.** **Fuentes Modeladas** ....................................................................... 20

**5.3.** **Análisis de los resultados** .................................................................... 21

**6.** **Resultados.** ................................................................................................ 23

**6.1.** **Caracterización Geofísica** ....................................................................... 23

**6.1.1.** **Topografía** ........................................................................................... 23

**6.2.** **Caracterización Meteorológica** ............................................................... 24

**6.2.1.** **Viento** .................................................................................................. 24

**6.2.2.** **Temperatura y humedad relativa del aire** .......................................... 40

**6.3.** **Dispersión de Contaminantes Atmosféricos** .......................................... 43

**6.3.1.** **4.3.1. Material Paniculado Respirable, MP10** ..................................... 43

**6.3.2.** **4.3.2. Material Paniculado Fino Respirable, MP2,5** ............................ 46

Página **2** de **69**

**6.3.3.** **Óxidos de Nitrógeno, NOx** .................................................................. 49

**6.3.4.** **Dióxido de Azufre, SO2** ....................................................................... 51

**6.3.5.** **4.3.5. Monóxido de Carbono, CO** ........................................................ 54

**6.4.** **Evaluación discreta de las concentraciones de contaminantes** ............ 57

**6.4.1.** **Material Particulado: MP10 y MP2,5** .................................................. 57

**6.4.2.** **Gases: SO2, NOx y CO** ......................................................................... 60

**6.5.** **Aporte de las concentraciones generadas a la condición basal, año**

**2014** 63

**6.5.1.** **Material Paniculado Respirable, MP10** ............................................... 63

**6.5.2.** **4.5.2. Material Paniculado Fino Respirable, MP2,5** ............................ 65

**6.6.** **Área de Influencia del proyecto.** ............................................................ 66

**7.** **Conclusión** .................................................................................................. 68

Página **3** de **69**

**Índice de Tablas**

**Tabla 1. Normas de calidad aplicables al proyecto.** ........................................ 9

Tabla 2. Concentración promedio anual de MP10, comunas Temuco y Padre Las Casas

.......................................................................................................................... 11

Tabla 3. Concentración promedio anual de MP2,5, comunas Temuco y Padre Las Casas

.......................................................................................................................... 12

Tabla 4. Coordenadas de vértices del área de estudio. ............................................ 16

**Tabla 5. Datos meteorológicos y geofísicos considerados en la modelación.** 18

**Tabla 6.** Emisiones atmosféricas puntuales generadas en la producción de asfalto. ... 21

Tabla 7. Ubicación puntos receptores ..................................................................... 21

**Tabla 8. Dirección y velocidad de viento estacional, estación Museo**

**Ferroviario.** ....................................................................................................... 30

**Tabla 9. Dirección y velocidad de viento estacional, medidas en la estación**

**meteorológica Las Encinas.** .............................................................................. 32

Tabla 10. Concentración Modelada Diaria y Anual de MP10 y MP2,5 ......................... 59

Tabla 11. Concentración Modelada de NOx, SO 2 y CO ............................................. 62

Tabla 12. Aumento de la concentración basal de MP10 como concentración promedio

anual .................................................................................................................. 63

Tabla 13. Aumento de la concentración basal de MP10 como concentración promedio

diario .................................................................................................................. 64

Tabla 14. Aumento de la concentración basal de MP2,5 como concentración promedio

anual .................................................................................................................. 65

Tabla 15. Aumento de la concentración basal de MP2,5 como concentración promedio

diario .................................................................................................................. 65

Página **4** de **69**

Índice de Figuras

Figura 1. Emplazamiento del proyecto ..................................................................... 7

Figura 2. Concentración diaria de MP10, comunas Temuco y Padre Las Casas ........... 10

Figura 3. Concentración diaria de MP2,5, comunas Temuco y Padre Las Casas .......... 11

Figura 4. Concentración tri anual de MP10, comunas Temuco y Padre Las Casas ....... 12

Figura 5. Concentración tri anual de MP2,5, comunas Temuco y Padre Las Casas ...... 13

Figura 6. Dominio de Modelación de CALMET. ........................................................ 17

Figura 7. Esquema de procesamiento de datos para CALMET ................................... 19

Figura 8. Dominio de la Modelación de CALPUFF ..................................................... 20

Figura 9. Puntos Receptores .................................................................................. 22

**Figura 10. Elevación de terreno del área de estudio.** ...................................... 23

**Figura 11. Rosa de viento anual Estación Museo Ferroviario.** ........................ 25

**Figura 12. Viento anual en estación Museo Ferroviario.** ................................. 26

**Figura 13. Rosa de viento anual Estación Las Encinas.** .................................. 27

**Figura 14. Viento anual en estación Las Encinas.** ........................................... 28

**Figura 15. Rosas de viento según estación del año, Museo Ferroviario.** ....... 29

**Figura 16. Velocidad del viento estacional en estación Museo Ferroviario.** .. 30

**Figura 17. Rosas de viento según estación del año, Las Encinas.** .................. 31

**Figura 18. Velocidad de viento Estación Las Encinas.** ..................................... 32

**Figura 19. Rosas de viento según horas del día en verano, Museo Ferroviario.**

.......................................................................................................................... 33

**Figura 20. Rosas de viento según horas del día en otoño, Museo Ferroviario.**

.......................................................................................................................... 34

**Figura 21. Rosas de viento según horas del día en invierno, Museo**

**Ferroviario.** ....................................................................................................... 35

**Figura 22. Rosas de viento según horas del día en primavera, Museo**

**Ferroviario.** ....................................................................................................... 36

**Figura 23. Rosas de viento según horas del día en verano, Las Encinas.** ...... 37

**Figura 24. Rosas de viento según horas del día en otoño, Las Encinas.** ........ 38

**Figura 25. Rosas de viento según horas del día en invierno, Las Encinas.** .... 39

**Figura 26. Rosas de viento según horas del día en primavera, Las Encinas.** . 40

**Figura 27. Temperatura y humedad relativa según hora del día en estación**

**Museo Ferroviario - Temuco, año 2012.** .......................................................... 41

Página **5** de **69**

**Figura 28. Temperatura del aire según hora del día en estación Museo**

**Ferroviario - Temuco, año 2012.** ...................................................................... 42

Figura 29. Curvas de Iso-concentración anual (μg/m [3] ) de MP10 ............................... 43

Figura 30. Curvas de Iso-concentración diaria (μg/m [3] ) de MP10. .............................. 46

Figura 31. Curvas de Iso-concentración anual (μg/m [3] ) de MP2,5 .............................. 47

Figura 32. Curvas de Iso-concentración diaria (μg/m [3] ) de MP2,5 ............................. 49

Figura 33. Curvas de Iso-concentración anual (μg/m [3] ) de NO X ................................. 50

Figura 34. Curvas de Iso-concentración horaria (μg/m [3] ) de NO x ............................... 51

Figura 35. Curvas de Iso-concentración anual (μg/m [3] ) de SO 2 ................................. 52

Figura 36. Curvas de Iso-concentración diaria (μg/m [3] ) de SO 2 ................................. 54

Figura 37. Curvas de Iso-concentración promedio 8 horas (mg/m [3] ) de CO ................ 55

Figura 38. Curvas de Iso-concentración promedio 1 hora (mg/m [3] ) de CO.................. 56

Figura 39. Área de Influencia ................................................................................ 67

Página **6** de **69**

**1.** **Introducción**

La planta de asfalto se encuentra instalada de acuerdo a la Resolución de Calificación

Ambiental favorable RCA N°212 del 12 de Diciembre de 2007, con una vida útil de 5

años, la cual ha cumplido su período de operación, es por ello la necesidad de ampliar

su vida útil.

El predio donde se encuentra instalada la planta de asfalto se ubica en el Camino Viejo

a Cajón km 5 sector Feria Los Camiones, aproximadamente a 5 Km al Norte de la

ciudad de Temuco, entre las comunas de Temuco y Padre las Casas, novena región de

la Araucanía, ver Figura 1.

**Figura 1. Emplazamiento del proyecto**

Este informe presenta los resultados de la modelación de los contaminantes generados

en el proceso de asfalto, mediante el uso de un modelo de dispersión gaussiano

lagrangeano tipo puff, llamado CALPUFF, recomendado por el Ministerio de Medio

Ambiente en la Guía para el uso de modelos de calidad del aire en el SEIA, publicada el

año 2012.

Página **7** de **69**

Los análisis presentados en éste informa, se ajusta a la decisión del titular de no

continuar con la solicitud de extracción y procesamiento de áridos provenientes del río

Cautín, sólo en lo referente a dar continuidad operacional a la planta de asfalto que

cuenta con RCA Favorable N°212/2007, por lo tanto, los resultados y conclusiones que

derivan de este informe guardan relación a ello.

Página **8** de **69**

**2.** **Marco Legas Aplicable**

Actualmente en Chile, se encuentran regulados algunos de los contaminantes emitidos

a la atmósfera. Estas corresponden a normas de calidad primaria, donde el bien

jurídico protegido es la salud de las personas.

Entre los contaminantes normados se encuentran el MP10, MP2,5, SO 2, NO 2 y CO.

Cabe destacar, que a la fecha no existe una normativa aplicable a la concentración en

el aire de NOx, sin embargo, para efectos comparativos, se asumirá que todo el NOx

generado corresponde a NO 2 .

La siguiente tabla presenta los límites normativos de los contaminantes. Cabe destacar

que en dicha tabla se presentan aquellos que se aplican a las emisiones producidas

durante la operación del proyecto.

**Tabla 1. Normas de calidad aplicables al proyecto.**

|Normativa de calidad del aire primaria|Col2|Col3|Col4|
|---|---|---|---|
|**Contaminante**|**Límite Norma**|**Concentración**|**Decreto**|
|Material Particulado<br>(MP10)|150 μg/m~~3~~N|Máxima Diaria|N° 58/1998<br>MINSEGPRES|
|Material Particulado<br>(MP10)|50 μg/m3N <br>|Media anual|Media anual|
|Material Particulado<br>(MP2,5)|50 μg/m~~3~~N|Máxima Diaria|N° 12/2011<br>MMA|
|Material Particulado<br>(MP2,5)|20 μg/m3N <br>|Media anual|Media anual|
|Dióxido de azufre (SO2)|80 μg/m~~3~~N <br>|Media anual|N° 113/2002<br>MINSEGPRES|
|Dióxido de azufre (SO2)|250 μg/m~~3~~N|Máxima diaria|Máxima diaria|
|Dióxido de Nitrógeno<br>(NO2)|400 μg/m3N|1 hora|N° 114/2002<br>MNSEGPRES|
|Dióxido de Nitrógeno<br>(NO2)|100 μg/m3N|Media anual|Media anual|
|Monóxido de Carbono<br>(CO)|10 mg/m3N|8 horas|N° 115/2002<br>MINSEGPRES|

Página **9** de **69**

**3.** **Antecedentes Calidad del Aire Temuco y Padre Las Casas**

Las comunas de Temuco y Padre Las Casas fue declarada en 2005 zona saturada por

material particulado respirable MP10 como concentración de 24 horas por el

D.S. 35/2005 MINSEGEPRES, debido a las altas concentraciones de éste contaminante

registrados en la ciudad las que sobrepasaban ampliamente el límite establecido en el

D.S. 58/1998 MINSEGEPRES, correspondiente a la norma para calidad del aire primaria

de MP10.

En la Figura 2 se muestra la concentración promedio diaria, estimada como el percentil

98 de la concentración de MP10, de donde se puede ver que en las estaciones Las

Encinas, Museo Ferroviario y Padre las Casas II para todos los años con datos

disponibles la concentración observada supera ampliamente el límite de la norma. A

pesar de esto, se puede observar que durante los años 2014 y 2015 la concentración

promedio diaria de MP10 ha disminuido, sobre todo en el último año en las estaciones

Las Encinas y Museo Ferroviario.

**Figura 2. Concentración diaria de MP10, comunas Temuco y Padre Las Casas**

Nota: La poca disponibilidad de datos medidos imposibilita el análisis del cumplimiento

normativo en todas las estaciones.

A raíz de estado de la calidad del aire, fue decretado un Plan de Descontaminación

Atmosférica para las comunas de Temuco y Padre Las Casas, bajo el D.S. 78/2009

MINSEGEPRES, que estableció metas de reducción de concentración de MP10.

Página **10** de **69**

Finalmente, con la entrada en vigencia del D.S. 12/2011 MMA, Temuco y Padre Las

Casas fue declarado como Zona Saturada por Material Particulado Fino Respirable

MP2,5 como concentración diaria a las comunas bajo la figura legal de D.S. 2/2013

MMA.

De hecho, tal como se ve en la Figura 3 las concentraciones diarias, calculadas como el

percentil 98 de la concentración promedio 24 horas de MP2,5 supera ampliamente el

límite establecido en la norma de calidad del aire de material particulado fino

respirable.

**Figura 3. Concentración diaria de MP2,5, comunas Temuco y Padre Las Casas**

Nota: La poca disponibilidad de datos medidos imposibilita el análisis del cumplimiento

normativo en todas las estaciones.

Por otro lado, la concentración promedio anual de MP10 (ver Tabla 2) en las

estaciones de monitoreo también presentan altas concentraciones, de hecho, la

concentración tri-anual da paso a la superación de la norma, tal como se ven la Figura

4.

**Tabla 2. Concentración promedio anual de MP10, comunas Temuco y Padre**

**Las Casas**

|Año|Concentración Promedio Anual (μg/m3)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Año**|**Las Encinas**|**Museo Ferroviario**|**Padre las Casas II**|**Límite de la norma**|
|2009|64,87|53,91|-|50|
|2010|62,77|-|-|-|
|2011|65,24|74,18|-|-|

Página **11** de **69**

|Año|Concentración Promedio Anual (μg/m3)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Año**|**Las Encinas**|**Museo Ferroviario**|**Padre las Casas II**|**Límite de la norma**|
|2012|-|53,27|-||
|2013|60,42|63,65|72,46|72,46|
|2014|47,38|54,27|64,87|64,87|
|2015|48,66|47,39|62,25|62,25|

**Figura 4. Concentración tri anual de MP10, comunas Temuco y Padre Las**

**Casas**

Nota: La poca disponibilidad de datos medidos imposibilita el análisis del cumplimiento

normativo en todas las estaciones, sin embargo, la normativa deja establecido que
basta con una estación con valores de saturación para que la zona sea declarada como

tal.

Por otro lado, la concentración promedio anual de MP2,5 que se muestran en la Tabla

3, superan ampliamente el límite de la norma. De hecho, tal como se observa en la

Figura 5, las concentraciones calculadas como el promedio tri-anual de la

concentración promedio de MP2,5 dan cuenta de la superación de la norma, siendo

incluso el doble de la concentración establecida como límite.

**Tabla 3. Concentración promedio anual de MP2,5, comunas Temuco y Padre**

**Las Casas**

|Año|Concentración Promedio Anual (μg/m3)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Año**|**Las Encinas**|**Museo Ferroviario**|**Padre las Casas II**|**Límite de la norma**|
|2009|45,08|37,98|-|20|
|2011|48,68|41,48|-|-|
|2012|-|43,44|-|-|

Página **12** de **69**

|2013|40,65|37,55|46,28|Col5|
|---|---|---|---|---|
|2014|36,17|34,450|37,07|37,07|

**Figura 5. Concentración tri anual de MP2,5, comunas Temuco y Padre Las**

**Casas**

Nota: La poca disponibilidad de datos medidos imposibilita el análisis del cumplimiento

normativo en todas las estaciones, sin embargo, la normativa deja establecido que
basta con una estación con valores de saturación para que la zona sea declarada como

tal.

Debido al estado de la calidad del aire en las comunas de Temuco y Padre las Casas en

2015 entre en vigencia el D.S. 8/2015 MMA que Establece Plan de Descontaminación

Atmosférica por MP2,5, el que establece metas de reducción de la concentración de

este contaminante restringiendo emisiones en los distintos sectores que se desarrollan

en la ciudad. Este decreto deroga al anterior PDA, para entonces vigente en la zona,

por lo tanto, los análisis entorno a los requerimientos del cumplimiento normativo.

**3.1** **Línea de Base**

Se eligió el año 2014 como año de línea de base para efectos de evaluar el aporte a las

concentraciones de contaminantes.

El criterio en la elección del año base se basa en la disponibilidad de datos y en que es

un año relativamente reciente con el cual se puede tener una aproximación más

certera, sobre todo considerando que la concentración de material particulado MP10 y

MP2,5 han ido en descenso en los últimos años.

Página **13** de **69**

**4.** **Modelo Calpuff**

De acuerdo a la “Guía para el uso de modelos de calidad del aire en el SEIA” Los

modelos existentes se pueden clasificar en Gaussianos, Eulerianos, Lagrangeanos y

tipo “Puff”.

La modelación de la dispersión atmosférica de los contaminantes provenientes del

proyecto que se somete a evaluación ambiental, se realizó con un modelo tipo “Puff”,

específicamente el modelo CALPUFF.

Los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los

modelos Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de

contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo largo de

una trayectoria. Su aproximación matemática consiste en estimar la dispersión en

forma Gaussiana en cada punto de una trayectoria; es decir, los modelos tipo “puff”

sólo requieren una trayectoria por “puff”, lo que hace su cálculo mucho más rápido. En

el caso de emisiones continuas, se simulan las trayectorias y la dispersión Gaussiana

de muchos “puffs”.

Considerando las características del terreno, las distintas unidades geomorfológicas del

área de influencia del proyecto y el dominio de la modelación se consideró utilizar el

modelo CALPUFF para simular la dispersión de los contaminantes generados en por la

operación actual y futura del proyecto.

CALPUFF, es un modelo no estacionario desarrollado por “TRC Scientists”, ha sido

usado en una amplia variedad de estudios de modelación de calidad del aire,

incluyendo: deposición de contaminantes tóxicos, impactos de incendios forestales,

evaluaciones de visibilidad y un largo rango de estudios de transporte.

CALPUFF es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y pos procesamiento. Dicho modelo

es recomendado por la agencia de protección ambiental (EPA) para modelar transporte

a larga distancia de contaminantes.

CALPUFF se compone de tres módulos

Página **14** de **69**

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento
y temperatura en una grilla de tres dimensiones. También asocia campos en
dos dimensiones de altura y usos de suelo.

 CALPUFF: Es un modelo de transporte y dispersión emitido desde fuentes
modeladas, simulando procesos de dispersión y transformación. CALPUFF utiliza
los datos generados por CALMET. Los archivos de salida de CALPUFF contienen
las concentraciones horarias o deposición por hora de flujos evaluados en
receptores seleccionados.

 CALPOST: Es usado para procesar esos archivos generados por CALMET y
CALPUFF, produciendo tabulaciones que resumen los resultados de la
simulación, identificando por ejemplo, la concentración promedio de 24 horas
para cada receptor.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelaciones es la siguiente:

~~[~~

[] ] ~~[[]~~

[]]

]

⁄

∑

~~[~~

Dónde:

**C** : concentración a nivel del suelo (g/m [3] ),

**Q:** masa de contaminantes (g) en la nube.

**σ** **x** : desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la

dirección.

**σ** **y** **:** desviación estándar (m) de la distribución de Gauss en el viento de costado

**σ** **z** **:** desviación estándar (m) de la distribución de Gauss en la dirección vertical.

**d** **a** **:** distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

**d** **c** **:** distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

**5.** **Metodología**

Página **15** de **69**

La modelación de las dispersión de contaminantes atmosféricos se realizó de acuerdo a

la siguiente metodología.

**5.1 Implementación del modelo meteorológico CALMET: Recopilación y**

**procesamiento de datos meteorológicos, topográficos y de uso de suelo**
**del área de estudio**

**5.1.1 Dominio de Modelación de CALMET**

El dominio de la modelación de CALMET, consideró un área que abarca las estaciones

de monitoreo a partir de las cuales y en consideración con las características

topográficas de la zona, el modelo meteorológico CALMET simulará campos de vientos

en todo el dominio de la modelación.

De ésta forma se determinó un dominio de modelación CALMET que incluyó el área

circundante a la zona de emplazamiento del proyecto y parte de la ciudad de Temuco y

Padre Las Casas. Finalmente, el dominio de la modelación resultó ser 35 km x 35 km,

con resolución de 1 km, tal como se muestra en Figura 6 y cuyas coordenadas se

puede ver en Tabla 4.

**Tabla 4. Coordenadas de vértices del área de estudio.**

|Vértice|Proyección: UTM, Huso 18 Sur ; Datum: WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (km)**|**Norte (km)**|
|Suroeste|693,375|5.699,959|
|Sureste|728,375|5.699,959|
|Noroeste|728,375|5.724,959|
|Noreste|693,375|5.724,959|

Página **16** de **69**

**Figura 6. Dominio de Modelación de CALMET.**

**5.1.2 Información meteorológica y geofísica**

Se recopilaron de datos de las distintas fuentes de información, como por ejemplo,

estaciones meteorológicas de altura y de superficie de la comuna de Temuco,

provenientes de sondeos y modelos meteorológicos, además de la obtención de

modelos de elevación digital (DEM) con sus respectivos usos de suelo.

Para la recopilación de datos meteorológicos se consideró el 2012 como año base,

debido a que dicho año presenta una mayor disponibilidad de datos meteorológicos y

de calidad de aire.

En la Tabla 5, se presentan las categorías y el tipo de datos con las respectivas fuentes

de información.

Página **17** de **69**

**Tabla 5. Datos meteorológicos y geofísicos considerados en la modelación.**

|Categoría de datos|Parámetro|Fuente|
|---|---|---|
|Meteorología de altura|Temperatura|National<br>Oceanic<br>and<br>Atmospheric Administration<br>(NOAA)|
|Meteorología de altura|Presión|Presión|
|Meteorología de altura|Velocidad de viento|Velocidad de viento|
|Meteorología de altura|Dirección de viento|Dirección de viento|
|Meteorología de Superficie|Temperatura|Estación Museo Ferroviario<br>Estación Las Encinas|
|Meteorología de Superficie|Presión|Presión|
|Meteorología de Superficie|Velocidad de viento|Velocidad de viento|
|Meteorología de Superficie|Dirección de viento|Dirección de viento|
|Meteorología de Superficie|Humedad relativa|Humedad relativa|
|Geofísicos|Elevación de Terreno|United<br>Stated<br>Geological<br>Survey (USGS)|
|Geofísicos|Uso de Suelo|Uso de Suelo|

**5.1** . **3 Procesamiento de datos en CALMET**

El tercer paso, corresponde al procesamiento de los datos en el modelo meteorológico

CALMET. Como ya se mencionó CALMET integra datos, los cuales son ingresados en

tres pre-procesadores dentro del modelo meteorológico, estos son:

 Pre-procesador de datos de altura (READ62): se ingresan datos de

temperatura, presión, dirección del viento, velocidad de viento.

 - Pre-procesador de datos superficiales (SMERGE): se ingresan datos

superficiales como por ejemplo: humedad relativa, temperatura, presión

superficial, dirección del viento y velocidad de viento.

 Pre-procesador de datos Geofísicos (MAKEGEO): se ingresan datos de elevación

del terreno y de usos de suelo.

En la Figura 7 se observa un esquema con los datos ingresados a los pre-procesadores

y los archivos generados (.DAT) que procesa CALMET.

Página **18** de **69**

_**Datos**_

_**Geofísicos**_

_**Datos**_

_**Superficiales**_

_**Datos en**_

_**Altura**_

**Figura 7. Esquema de procesamiento de datos para CALMET**

**5.2 Recopilación y procesamiento del escenario de emisión propuesto para**

**la modelación en CALPUFF**

Para evaluar la dispersión de los contaminantes atmosféricos proveniente de la

operación de la planta, se utilizó la información presente en la Declaración de Impacto

Ambiental (DIA), específicamente las estimaciones de emisiones y Descripción de

proyecto. Para la modelación se consideró la emisión de contaminantes atmosféricos

proveniente de las principales actividades involucradas en el proceso de operación de

la planta. A continuación se presentan las emisiones de los procesos productivos en la

etapa de operación.

**5.2.1.** **Dominio de la Modelación de CALPUFF**

El dominio de la modelación de CALPUFF se extiende en un área 25 x 25 km, la cual

abarca zonas circundantes al área del proyecto. La extensión es menor al dominio de

CALMET, e incluye zonas con poca densidad habitacional, el dominio de la modelación

de CALPUFF se puede ver en la siguiente figura.

Página **19** de **69**

**Figura 8. Dominio de la Modelación de CALPUFF**

**5.2.2.** **Fuentes Modeladas**

Se modeló una fuente puntual correspondiente al calentador vertical y secador de

asfalto, el cual cuenta un filtro de mangas como sistema de abatimiento previo a salida

de gases y partículas.

La tasa de emisión de MP se obtuvo de la medición isocinética realizada a la fuente

emisora, cuyos resultados se presentan en Anexo 1. Con estos resultados se realizó el

ajuste por tamaño de partícula en conformidad a lo descrito en la Tabla 11.1-2 del

Capítulo 11 “Hot Mix Asphalt Plants” del AP-42, con el fin de estimar tasas de emisión

reales.

Respecto de los gases de combustión, se usaron los factores de emisión presentadas

en la Tabla 2 de la Guía Mitológica para la Estimación de Emisiones Atmosféricas de

Fuentes Fijas y Móviles en el Registro de Emisiones y Transferencia de Contaminantes.

Página **20** de **69**

En la Tabla 6 se presentan las emisiones puntuales que genera el proyecto sujeto a

evaluación ambiental, para ser consideradas en la modelación.

**Tabla 6.** Emisiones atmosféricas puntuales generadas en la producción de asfalto.

|Actividad|Emisiones Puntuales (ton/año)|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Actividad**|**MP10**|**MP2,5**|**CO**|**NOx**|**SO2 **|
|Calentador Vertical y secador de<br>Asfalto|0,72|0,22|8,57|2,57|0,18|

**5.3.** **Análisis de los resultados**

Para analizar los resultados de la modelación de dispersión de contaminantes

atmosféricos, se realizaron mapas de iso-concentración de las emisiones generadas por

el proyecto. Dichos mapas permitieron evaluar la dirección de la dispersión de los

contaminantes, además entrega información de la concentración promedio medida en

la primera capa vertical de la modelación, es decir, entre los 0 y 20 m.

Por otro lado, se evaluó la concentración de contaminante en puntos receptores

cercanos al proyecto ubicados en zonas pobladas, en las estaciones de monitoreo de

calidad del aire con el fin de evaluar el aporte a la concentración de contaminantes

respecto de la condición basal y en puntos pasivos ubicados en zonas no pobladas

alejadas del área de proyecto. Los puntos receptores elegidos son los que se presentan

en la siguiente tabla.

**Tabla 7. Ubicación puntos receptores**

|Puntos|Coordenadas UTM (km)|Col3|Distancia desde<br>la fuente<br>emisora (m)|
|---|---|---|---|
|**Puntos**|**X **|**Y **|**Y **|
|R1|5.714,313|714,958|421|
|R2|5.714,708|715,772|1.803|
|R3|5.713,818|714,309|50|
|R4|5.713,015|713,851|1.504|
|R5|5.715,867|717,056|2.800|
|R6|5.714,963|714,242|1.344|
|R7|5.712,401|716,087|1.816|
|R8|5.712,273|712,674|2.891|
|R9. Estación Ferroviaria|5.710,886|711,145|4.932|
|R10. Estación Las Encinas|5.708,391|706,773|9.906|
|R11. Estación Padre Las Casas II|5.708,391|708,623|9.754|
|R12. Estación Padre Las Casas|5.706,571|708,933|10.225|

Página **21** de **69**

|Puntos|Coordenadas UTM (km)|Col3|Distancia desde<br>la fuente<br>emisora (m)|
|---|---|---|---|
|**Puntos**|**X **|**Y **|**Y **|
|R13|5.705,694|706,117|9.068|
|R14|5.712,307|714,466|6.922|
|R15|5.702,189|706,458|14.487|
|R16|5.715,617|708,571|6.713|
|R17|5.713,304|701,871|13.288|

Nota: Receptores sombreados corresponden a estaciones de monitoreo de calidad del

aire.

La ubicación espacial de los puntos receptores se puede ver en la siguiente imagen.

**Figura 9. Puntos Receptores**

Nota: R 9, R 10, R 11 y R12 corresponden a las estaciones: Ferroviaria, Las Encinas,

Padre Las Casas II y Padre Las Casas, respectivamente.

Página **22** de **69**

**6.** **Resultados.**

A continuación se presentan los principales resultados de la modelación de emisiones

atmosféricas. Dichos resultados incluyen los datos generados por los procesadores

CALMET, CALPUFF Y CALPOST.

Se procesaron los datos geofísicos y meteorológicos (altura y superficie), los resultados

obtenidos con el procesador CALMET se presentan a continuación.

**6.1.** **Caracterización Geofísica**

**6.1.1.** **Topografía**

**Figura 10. Elevación de terreno del área de estudio.**

En la figura anterior se observa que Temuco está rodeado por 2 relieves montañosos

que se encuentran al norte y al sur de la ciudad, siendo el más prominente, el del

norte. Esta topografía influirá tanto en las velocidades de vientos como en la dirección,

así como en la dispersión de contaminantes.

Página **23** de **69**

**6.2.** **Caracterización Meteorológica**

**6.2.1.** **Viento**

A continuación, se presentan los resultados de las estaciones meteorológicas más

cercanas al proyecto, correspondiente a estación Meteorológica Museo Ferroviario y la

estación Las Encinas.

**Dirección y velocidad de vientos anuales**

A continuación se presentan las rosas de viento anual para las estaciones

meteorológicas, el cual es un método gráfico que consiste en representar

conjuntamente las distribuciones de frecuencias de la dirección y la velocidad del

viento. Las direcciones se agruparon en 16 clases representando la dirección desde

donde sopla el viento (N, NNE, NE, ENE, E, ESE, SE, SSE, S, SSO, SO, OSO, O, ONO,

NO, NNO), y las velocidades se discriminaron en intervalos. Se consideró como calma

(velocidad del viento muy baja o la) valores menores a 0,5 [m/s]. Las barras del

gráfico estas divididas en segmentos de diferentes tamaño y color. Cada segmento de

color representa un rango específico de velocidad del viento en unidades de [m/s]. El

tamaño o largo de cada segmento dentro de cada barra es proporcional a la

frecuencia de los vientos que soplan en ese rango. La frecuencia se representa

porcentualmente en los diferentes círculos concéntricos del gráfico.

Además, se presentan gráficos de barra para demostrar la dominancia de la velocidad

de los vientos.

Página **24** de **69**

a) Estación meteorológica Museo Ferroviario

**Figura 11. Rosa de viento anual Estación Museo Ferroviario.**

Página **25** de **69**

**Figura 12. Viento anual en estación Museo Ferroviario.**

De acuerdo a la dirección de vientos registrados el año 2012 en la estación Museo

Ferroviario, se puede apreciar que según el vector resultante, los vientos

predominantes provienen de la dirección sur (S) con un 45% de frecuencia.

Con respecto a las velocidades de viento, se puede apreciar que predominan las

velocidades entre 0,5-2,1 [m/s] con un 60% de frecuencia, luego siguen las

velocidades entre 2,1 - 3,6 [m/s] con 17,9% y las velocidades calmas (cercanas a 0

[m/s]) con un 16,8% de frecuencia. Se observa que los vientos son mayoritariamente

lentos y que existe un gran porcentaje de calmas, dificultando la dispersión de

contaminantes.

Página **26** de **69**

b) Estación Meteorológica Las Encinas

**Figura 13. Rosa de viento anual Estación Las Encinas.**

Página **27** de **69**

**Figura 14. Viento anual en estación Las Encinas.**

De acuerdo a la dirección de vientos registrados en el año 2012 en estación Las

Encinas, se puede apreciar que según el vector resultante, los vientos predominantes

provienen de la dirección oeste suroeste (OSO) con un 23% de frecuencia.

Con respecto a las velocidades de viento, se puede apreciar que predominan las

velocidades entre 0,5 - 2,1 [m/s] con un 60,8% de frecuencia y las velocidades entre

2,1-3,6 [m/s] con un 19,2% de frecuencia. Las calmas alcanzan un 12,1% de

frecuencia. En esta estación se puede observar que las velocidades aumentan

levemente, dado por la posición geográfica de la estación, sin embargo siguen siendo

velocidades bajas y un porcentaje considerable de calmas, por lo que se concluye que

no existen vientos favorables.

Página **28** de **69**

**Dirección y velocidad de viento estacional**

a) Estación meteorológica Museo Ferroviario:

**Figura 15. Rosas de viento según estación del año, Museo Ferroviario.**

En las rosas de vientos estacionales medidos en Museo Ferroviario se puede observar

que durante todo el año los vientos vienen principalmente del sur, existiendo una

variación de vientos predominantes que fluctúa entre direcciones oeste suroeste (OSO)

y sureste (SE), salvo en algunos meses de primavera donde existen vientos que soplan

desde el este (E) y este noreste (ENE).

En la Tabla 8, se observan las frecuencias según rango de velocidades.

Página **29** de **69**

**Tabla 8. Dirección y velocidad de viento estacional, estación Museo**

**Ferroviario.**

|Estaciones|Dirección de Vector<br>Resultante|Velocidades Predominantes<br>y Calmas (m/s)|Frecuencia<br>%|
|---|---|---|---|
|Verano|OSO (53%)|0,5-2,1|68,3|
|Verano|OSO (53%)|2,1-3,6|16,6|
|Verano|OSO (53%)|3,6-5,7|6,5|
|Verano|OSO (53%)|Calma|8,6|
|Otoño|S (54%)|0,5-2,1|60,9|
|Otoño|S (54%)|2,1-3,6|14,5|
|Otoño|S (54%)|3,6-5,7|3,6|
|Otoño|S (54%)|Calmas|20,3|
|Invierno|SSE (78 %)|0,5-2,1|58,1|
|Invierno|SSE (78 %)|2,1-3,6|15,7|
|Invierno|SSE (78 %)|3,6-5,7|3,2|
|Invierno|SSE (78 %)|Calmas|21,8|
|Primavera|SE (44 %)|0,5-2,1|55,7|
|Primavera|SE (44 %)|2,1-3,6|22,3|
|Primavera|SE (44 %)|3,6-5,7|5,1|
|Primavera|SE (44 %)|Calmas|16,9|

A continuación se presenta gráficamente la velocidad de los vientos en estación Museo

Ferroviario para cada estación del año.

**Figura 16. Velocidad del viento estacional en estación Museo Ferroviario.**

Página **30** de **69**

En la tabla y gráfico anterior se puede apreciar que los vientos no favorecen la

dispersión de contaminantes, debido a una considerable presencia de velocidades

calma (>16 %), salvo en los meses de verano donde las calmas disminuyen a 8,6%.

La estación de verano es la que presenta las condiciones más favorables para la

dispersión de los contaminantes, debido a que presenta la mayor frecuencia de rangos

de altas velocidades entre 3,6-5,7 [m/s] (6,5%) y la menor frecuencia de calmas

(8,6%). Por otro lado la estación más desfavorable es invierno, ya que posee la

frecuencia más baja de altas velocidades (3,2%) y la mayor frecuencia de calmas

(21,8%).

b) Estación meteorológica Las Encinas:

**Figura 17. Rosas de viento según estación del año, Las Encinas.**

Página **31** de **69**

Con respecto a Estación Las encinas se observa que durante todas las estaciones del

año los vientos vienen principalmente desde el oeste, existiendo una variación que

fluctúa entre oeste suroeste (OSO) y oeste noroeste (ONO). Sin embargo, existen

algunos episodios ocurridos durante otoño e invierno donde aparecen fuertes

componentes noreste (NE) que se asocian a frentes de mal tiempo.

**Tabla 9. Dirección y velocidad de viento estacional, medidas en la estación**

**meteorológica Las Encinas.**

|Estaciones|Dirección de Vector<br>Resultante|Col3|Velocidades Predominantes<br>y Calmas (m/s)|Col5|Frecuencia<br>%|
|---|---|---|---|---|---|
|Verano|Verano|OSO (50 %)|0,5-2,1|54,5|54,5|
|Verano|Verano|OSO (50 %)|2,1-3,6|23,1|23,1|
|Verano|Verano|OSO (50 %)|3,6-5,7|10,0|10,0|
|Verano|Verano|OSO (50 %)|Calma|12,1|12,1|
|Otoño|Otoño|O (12 %)|0,5-2,1|63,7|63,7|
|Otoño|Otoño|O (12 %)|2,1-3,6|16,2|16,2|
|Otoño|Otoño|O (12 %)|3,6-5,7|5,8|5,8|
|Otoño|Otoño|O (12 %)|Calmas|13,4|13,4|
|Invierno|Invierno|ONO (8 %)|0,5-2,1|62,5|62,5|
|Invierno|Invierno|ONO (8 %)|2,1-3,6|17,5|17,5|
|Invierno|Invierno|ONO (8 %)|3,6-5,7|6,1|6,1|
|Invierno|Invierno|ONO (8 %)|Calmas|12,6|12,6|
|Primavera|Primavera|OSO (39 %)|0,5-2,1|66,8|66,8|
|Primavera|Primavera|OSO (39 %)|2,1-3,6|22,4|22,4|
|Primavera|Primavera|OSO (39 %)|3,6-5,7|5,4|5,4|
|Primavera|Primavera|OSO (39 %)|Calmas|5,4|5,4|

**Figura 18. Velocidad de viento Estación Las Encinas.**

Página **32** de **69**

Con respecto a las velocidades, al igual que la estación Museo Ferroviario, los datos

registrados en la estación Las Encinas, permiten concluir que en al área de estudio no

se presentan una buena dispersión de contaminantes, debido a que existe un alto

porcentaje de calmas ( >12%) la mayor parte del año, a excepción de los meses de

primavera donde las calmas disminuyen a 5,4%, pero también existe una baja

frecuencia de velocidades altas (3,6 - 5,7 [m/s]) que apenas alcanza 5,4%.

La estación del año que presenta las mejores condiciones de dispersión es verano,

debido a que posee la mayor frecuencia de velocidades altas, mientras que la estación

de otoño es la que tiene menores condiciones de dispersión producto de su gran

cantidad de velocidades calmas y baja cantidad de altas velocidades.

**Dirección y velocidad de viento en ciclos diarios**

a) Estación meteorológica Museo Ferroviario:

**Figura 19. Rosas de viento según horas del día en verano, Museo Ferroviario.**

Página **33** de **69**

**Figura 20. Rosas de viento según horas del día en otoño, Museo Ferroviario.**

Página **34** de **69**

**Figura 21. Rosas de viento según horas del día en invierno, Museo**

**Ferroviario.**

Página **35** de **69**

**Figura 22. Rosas de viento según horas del día en primavera, Museo**

**Ferroviario.**

En los ciclos diarios de rosas de vientos para la estación Museo Ferroviario, se observa

que para todas las estaciones del año existe un componente oeste y sur oeste que se

acentúa llegada la tarde. Además se observa que las velocidades más altas se alcanzan

entre la tarde y noche, siendo más visible durante las estaciones de primavera y

verano. Por otro lado se observó que generalmente no existen cambios drásticos entre

distintas horas del día, salvo durante los meses de primavera que se observó una

inestabilidad notable entre la mañana y tarde, sin embargo esto no afecta de gran

manera al vector resultante. Algo similar se observó durante los meses de otoño, pero

en menor magnitud.

Página **36** de **69**

b) Estación meteorológica Las Encinas:

**Figura 23. Rosas de viento según horas del día en verano, Las Encinas.**

Página **37** de **69**

**Figura 24. Rosas de viento según horas del día en otoño, Las Encinas.**

Página **38** de **69**

**Figura 25. Rosas de viento según horas del día en invierno, Las Encinas.**

Página **39** de **69**

**Figura 26. Rosas de viento según horas del día en primavera, Las Encinas.**

En los ciclos diarios de rosas de vientos para la estación Las Encinas, se observa que

para todas las estaciones del año existe un aumento de las velocidades de durante las

tardes. También se observa un componente noreste que se hace notar en las

madrugadas y mañanas de Otoño-Invierno, sin embargo las velocidades que se

alcanzan son relativamente bajas (0,5 -2,1 m/s).

En general se observan componentes que varían de madrugada a noche entre

direcciones noroeste y suroeste.

**6.2.2.** **Temperatura y humedad relativa del aire**

En el gráfico que se presenta a continuación se muestran las temperaturas y

humedades relativas promedios como ciclo diario medidas en la estación museo

ferroviario de Temuco en el año base 2012.

Página **40** de **69**

**Figura 27. Temperatura y humedad relativa según hora del día en estación**

**Museo Ferroviario - Temuco, año 2012.**

En la figura anterior se observa la relación inversa entre temperatura del aire y

humedad relativa del aire, donde los niveles más altos de temperatura que se alcanzan

entre las 14 y 17 horas, coinciden con los niveles más bajos de humedad. Por otro lado

las temperaturas más bajas se alcanzan entre las 06 y 08 horas, coincidiendo con los

niveles más altos de humedad.

Para el caso de la temperatura, el máximo promedio alcanzado en la hora 16 fue de

17,47 °C, mientras que la temperatura promedio mínima se alcanzó a la hora 7 y fue

de 8,27°C.

Con respecto a la humedad relativa, el máximo promedio alcanzado en la hora 7 fue de

95,86%, mientras que el promedio mínimo se alcanzó a la hora 16 y fue de 78,1%.

También se presenta el siguiente gráfico de temperaturas indicando las máximas y

mínimas del año 2012.

Página **41** de **69**

**Figura 28. Temperatura del aire según hora del día en estación Museo**

**Ferroviario - Temuco, año 2012.**

En la figura precedente, se observa que existe una gran variabilidad de temperaturas a

lo largo del año y del día, esto es típico de ciudades ubicadas en la depresión

intermedia o valle longitudinal de Chile. Se observa la presencia de temperaturas

extremas, con mínimas bajo cero que llegan a los -2,7 °C y máximas que llegan a los

35,1 °C.

Es importante destacar que este tipo de comportamiento en las temperaturas da a

origen a eventos de inversión térmica que produce un aumento en la concentración

ambiental de contaminantes atmosféricos, esto se acentúa mucho más en las noches

frías de invierno, donde el aire superficial se enfría de gran manera, más rápido que el

aire superior, produciendo que los contaminantes no se escapen hacia zonas más altas.

Página **42** de **69**

**6.3.** **Dispersión de Contaminantes Atmosféricos**

A continuación se muestra la pluma de dispersión de MP10 en un área de 625 km [2] .

**6.3.1.** **4.3.1. Material Paniculado Respirable, MP10**

En la Figura 29 se puede apreciar que la pluma de dispersión de MP10 anual, donde se

observa que ésta se desplaza en dirección noreste a la planta acorde al régimen de

vientos presentes en la zona.

**Figura 29. Curvas de Iso-concentración anual (μg/m** **[3]** **) de MP10**

Nota: Circulo en blanco corresponde a la fuente emisora.

El análisis de la dispersión de MP10 en su concentración anual permite concluir lo

siguiente:

 Las concentraciones modeladas de MP10 promedio anual son de baja magnitud.

De hecho, las concentraciones obtenidas son mucho menores a 1 μg/m [3] N.

Página **43** de **69**

 El punto de máximo impacto se encuentra a unos 940 m (representada en Figura

30 con un círculo en blanco) hacia el noreste de la planta alcanzando una

concentración promedio [1] de 0,040 μg/m [3] N.

 Dentro del área de estudio se alcanzan concentraciones de 0 μg/m [3] N.

 Las concentraciones que fluctúan entre los 0,020 μg/m [3] N y el máximo modelado

abarcan un área de 17,8 km [2] . Esta zona es la que en la Figura 29 se muestra

desde las tonalidades rojas a verdes.

 La ciudad de Temuco y Padre las casas no se verá afectada por el aumento en la

concentración de MP10, pues la pluma de dispersión indica que las masas de aire

no transportarán MP10 a esa zona. En este sentido, las zonas más afectadas son

pequeños emplazamientos poblacionales cercanos a la planta BITUMIX CVV, la que

en el peor de los casos recibirá un aporte de su condición basal de 0,035 μg/m [3] N.

La concentración promedio diaria modelada de MP10, sugiere un comportamiento

ligeramente distinto en la dispersión de los contaminantes que la concentración

promedio anual. Si bien, sigue teniendo una importante componente norte y noreste,

existe desplazamiento de contaminantes en otros sentidos; esto se debe al

comportamiento de los vientos durante un día promedio.

De la dispersión del MP10 promedio diario, calculado como el percentil 98, visible

Figura 30 se puede concluir lo siguiente:

 La concentración promedio diaria de MP10 es de baja magnitud. En efecto, las

concentraciones modeladas para éste contaminantes son inferiores a

concentraciones de 1 μg/m [3] N.

 Dentro del área de estudio, la cual abarca la ciudad de Temuco, se alcanzan

concentraciones de 0 μg/m [3] N.

 En un área total de 17,8 km [2] las concentraciones van desde los 0,1 y 0,2

μg/m [3] N, esto representa tan sólo el 2,8% del área total de la zona en estudio.

Esto es lo que en Figura 30 se ve en colores verde a rojo.

1 Se refiere a la concentración promedio anual, como media aritmética entre los 0 y 20 m sobre
la elevación del nivel del suelo.

Página **44** de **69**

A partir de los 1,8 km a partir de la fuente emisora en dirección suroeste, la

concentración modelada de MP10 diario disminuye progresivamente desde los

0,08 μg/m [3] N. Esto significa que las zonas más densamente pobladas de las

comunas Temuco y Padre Las Casas no recibirán grandes aportes en la

concentración basal de la ciudad debido al funcionamiento de la planta.

La máxima concentración de MP10 horario se alcanza a los 940 m de la fuente

emisora (representada en Figura 30 con un círculo en blanco) hacia el noreste.

Respecto de su magnitud, la modelación sugiere que alcanzaría

concentraciones de 0,20 μg/m [3] N.

La dispersión del MP10 diario permite concluir que las zonas que reciben mayor

aporte son pequeños emplazamientos de poblaciones ubicados en dirección

noreste del proyecto, sin embargo, a pesar de que se desconoce la

concentración basal en esas zonas, es posible predecir que el aporte a la

concentración basal es bajo debido a que éstas alcanzan valores muy bajos.

Con lo anterior es posible afirmar la ejecución del proyecto no afectará la

calidad de vida de las personas que desarrollen sus actividades cerca de la

fuente emisora.

Página **45** de **69**

**Figura 30. Curvas de Iso-concentración diaria (μg/m** **[3]** **) de MP10.**

Nota: Circulo en blanco corresponde a la fuente emisora.

**6.3.2.** **4.3.2. Material Paniculado Fino Respirable, MP2,5**

A continuación, se muestra la pluma de dispersión de MP2,5 para el promedio anual y

diario de éste contaminante. Naturalmente, el comportamiento de la pluma de

dispersión del MP10 y las obtenidas para el MP2,5 son similares debido a que se trata

del mismo contaminante difiriendo sólo en el tamaño aerodinámico de la partícula.

En la Figura 31, se muestra la pluma de dispersión de MP2,5 anual, de donde se puede

concluir que el desplazamiento de la pluma tiene sentido norte y noreste

principalmente.

Página **46** de **69**

**Figura 31. Curvas de Iso-concentración anual (μg/m** **[3]** **) de MP2,5**

Nota: Circulo en blanco corresponde a la fuente emisora.

De la Figura anterior se puede concluir:

 Las concentraciones modeladas de MP2,5 producto de la emisión del

contaminante son de baja magnitud. Efectivamente, la concentración modelada

entre los 0 y 20 m desde el nivel del suelo, alcanza magnitudes muy inferiores a

1 μg/m [3] N.

 El punto de máximo impacto se ubica a unos 940 m hacia el noreste de la

fuente emisora (representada en Figura 30 con un círculo en blanco),

alcanzando una concentración modelada de 0,012 μg/m [3] N.

 Dentro del área de estudio, correspondiente a 625 km [2] se alcanzan

concentraciones modeladas del proyecto de 0 μg/m [3] N.

Página **47** de **69**

 Las concentraciones que fluctúan entre los 0,010 y 0,012 μg/m [3] N abarcan un

área de 1,61 km [2] representando el 0,3% del área total de estudio. Esta zona se

puede ver en colores naranja y rojo en la Figura 30.

Al avanzar 1,6 km hacia el suroeste de la fuente emisora las concentraciones

modeladas comienzan a ser inferiores a los 0,004 μg/m [3] N, valores tan bajos que no se

encuentran dentro del rango de la resolución de los equipos monitores de calidad del

aire. Con lo anterior, es posible predecir que el aporte a la concentración basal de las

comunas más afectadas por la contaminación por MP2,5, Temuco y Padre Las Casas,

no se ve afectada por el funcionamiento de BITUMIX CVV.

Po otro lado, la dispersión de la concentración diaria estimada como el percentil 98 de

la concentración promedio diaria de MP2,5, visible en la Figura 32, da cuenta de un

comportamiento de la dispersión predominantemente norte y noreste con una

componente más discreta en sentido suroeste.

De los resultados obtenidos se puede concluir lo siguiente:

 La magnitud de la concentración modelada como el promedio entre las

concentraciones entre los 0 y los 20 m sobre el nivel del suelo son de baja

magnitud, muy lejos de alcanzar concentraciones cercanas a 1 μg/m [3] N.

 El punto de máximo impacto se encuentra los 1.000 m al noreste de la fuente

emisora (en Figura 32 identificado como un circulo blanco) alcanzando una

magnitud de 0,062 μg/m [3] N.

 Las zonas de máximas concentraciones modeladas que van desde los 0,050 a

los 0,062 μg/m [3] N abarcan un área de 1,9 km [2] constituyendo tan solo el 0,3%

del área total de estudio.

 A partir de los 3,0 km hacia el suroeste de la fuente emisora las

concentraciones comienzan a ser inferiores a los 0,01 μg/m [3] N. Con lo anterior

es posible predecir que el aporte a la concentración basal de las comunas

Temuco y Padre Las Casas es muy baja y que por lo tanto, el proyecto no va en

desmedro de la calidad del aire de la zona.

Página **48** de **69**

**Figura 32. Curvas de Iso-concentración diaria (μg/m** **[3]** **) de MP2,5**

**6.3.3.** **Óxidos de Nitrógeno, NOx**

Debido al estado de la calidad del aire en la ciudad de Temuco y Padre Las Casas se

modeló la concentración de NO X en el aire, esto debido a que éste es considerado

como un propulsor de material particulado en el aire.

A continuación, se muestra la pluma de dispersión de NO X como concentración

promedio anual de donde se puede concluir que la pluma de dispersión se moverá en

sentido norte y noreste principalmente, tal como se muestra en la Figura 33.

De los resultados de la modelación de la concentración anual se puede concluir:

 La concentración promedio anual de NO x alcanza concentraciones en el aire de

baja magnitud. De hecho, la máxima concentración modelada como promedio

entre los 0 y 20 m respecto del nivel del suelo alcanza un máximo de 0,043

μg/m [3] N encontrado a 1 km de la fuente de emisión.

Página **49** de **69**

 Con lo anterior es posible predecir que la transformación de MP10 y MP2,5 en

el aire por efectos de las reacciones químicas en la atmosfera de los

propulsores es baja.

**Figura 33. Curvas de Iso-concentración anual (μg/m** **[3]** **) de NO** **X**

Nota: Circulo en blanco corresponde a la fuente emisora.

En Chile, existe una norma que para el NO 2 que regula la concentración horaria y

anual. Si bien, en éste informe los análisis son en torno a la concentración de NO X,

entendiendo que en él se agrupan varios compuestos químicos binarios gaseosos

formados por la combinación de oxígeno y nitrógeno [2] para efectos comparativos se

asimilará la totalidad del NO X al NO 2, a pesar de que este supuesto, sobre dimensiona

los valores de concentración de NO 2 .

2
Tales como N 2 O, NO, NO 2, N 2 O 4, NO 2 y N 2 O 5 .

Página **50** de **69**

En consecuencia con lo anterior y tal como se muestra en Figura 33 se prevé que el

aporte a la concentración de NO 2 basal en Temuco y Padre Las Casas será bajo, de

hecho, los mayores aportes se verán en la zona norte y noreste de la ciudad.

Por otro lado, tal como se ve en la Figura 34 la dispersión de NO X horario estimado

como la máxima concentración, sigue teniendo una componente norte y noreste

importante. La magnitud de la concentración generada por la actividad del proyecto es

baja y por lo tanto, se predice que el aporte a la concentración basal de NO 2 en

Temuco y Padre Las Casas será bajo; de hecho, la máxima concentración se alcanza a

1 km de la fuente emisora en dirección al noroeste alcanzando una magnitud de 2,04

μg/m [3] N.

**Figura 34. Curvas de Iso-concentración horaria (μg/m** **[3]** **) de NO** **x**

**6.3.4.** **Dióxido de Azufre, SO2**

Página **51** de **69**

El dióxido de azufre es un propulsor de material particulado en el aire, pues se oxida a

SO 4

-2, por tanto, la magnitud de la concentración obtenida en la modelación permitirá

predecir, si el aporte del material particulado secundario será de una magnitud tal que

al sumarse al MP10 y MP2,5 primario afecte la calidad de vida de las personas. Además

la concentración de SO 2 en el aire es normada por el D.S. 113/2022

En la Figura 35 se puede observar la pluma de dispersión de la concentración

promedio anual de SO 2 en el área de estudio.

**Figura 35. Curvas de Iso-concentración anual (μg/m** **[3]** **) de SO** **2**

De aquí se puede concluir que:

 La pluma de dispersión tiene una componente noreste predominante, por tanto,

la cuidad de Temuco y Padre Las Casas no recibirá aportes importantes a la

concentración basal de SO 2 registrada en la ciudad.

Página **52** de **69**

 Al avanzar hacia el suroeste de la fuente 1 km las concentraciones modeladas

promedio anual son interiores de 0,002 μg/m [3] N, concentración de magnitud no

predecible por la resolución de los equipos monitores.

 La magnitud de la concentración es baja, de hecho, la máxima concentración

modela fue de 0,005 μg/m [3] N a 2,1 km de la fuente emisora.

 Además las bajas concentraciones obtenidas, permiten predecir la

transformación química del SO 2 en el aire no generará una concentración de

material particulado secundario en el aire de magnitud tal que afecte

significativamente la calidad de vida de las personas.

En la Figura 36, se ve la pluma de dispersión de SO 2 como concentración promedio

diario, la cual se caracteriza ser más predominante en dirección norte y noreste de a

fuente emisora.

Página **53** de **69**

**Figura 36. Curvas de Iso-concentración diaria (μg/m** **[3]** **) de SO** **2**

De la figura precedente se concluye que:

 Las zonas que recibirán más aporte a la concentración basal son aquellas que

se encuentran hacia el noreste de la fuente emisora. Análogamente, Temuco y

Padre Las Casas no verá afectada considerablemente la condición basar del SO 2

como concentración promedio diaria.

 La máxima concentración se alcanza a los 1,8 km al noreste de la fuente

emisora y alcanza una concentración de 0,029 μg/m [3] N.

**6.3.5.** **4.3.5. Monóxido de Carbono, CO**

En ésta sección del informe se presenta la concentración promedio 8 horas y 1 hora

para CO, valores que son normados según el D.S. 115/2002 MINSEGEPRES válidos

Página **54** de **69**

para mediciones realizadas en EMRP [3] . Por ésta razón, a continuación exponen la pluma

de dispersión del CO como promedio de 8 horas y 1 horas como la concentración

máxima [4] .

De la figura que se ve a continuación se puede observar que el CO se dispersa hacia el

noreste de la planta uniformemente.

**Figura 37. Curvas de Iso-concentración promedio 8 horas (mg/m** **[3]** **) de CO**

Los resultados sugieren que:

 Dado que el desplazamiento de la masa de aire que contiene el CO es en

dirección noreste, las comunas de Temuco y Padre Las Casas no recibirán un

aporte sustancial respecto de su condición basal.

3 Estaciones de Monitoreo con Representatividad Poblacional.
4 El D.S. 115/2002 MINSEGEPRES norma como el percentil 99 de los máximos diarios.

Página **55** de **69**

 La magnitud de la concentración modelada de CO promedio de 8 horas es baja,

de hecho, la máxima concentración modelada se encuentra a 970 m de la

fuente y alcanza una magnitud de 0,006 mg/m [3] N.

Respecto el promedio horario de la concentración de CO, el cual es presentado en la

Figura 38, se observa que la pluma de dispersión no tiene forma definida, pero que se

desplaza principalmente hacia el noreste de la fuente de emisión. Este comportamiento

se debe al régimen de los vientos horario, esto fue presentado en las Figura 19, Figura

20, Figura 21, Figura 22, Figura 23, Figura 24, Figura 25 y Figura 26

**Figura 38. Curvas de Iso-concentración promedio 1 hora (mg/m** **[3]** **) de CO**

De los resultados de la concentración promedio horaria obtenidas, se puede concluir

que:

 Los principales aportes a la concentración basal de CO serán en la zona noreste

al proyecto, sin embargo debido a que la magnitud de la concentración es tan

Página **56** de **69**

baja, se puede predecir que no representarán un problema para la salud de las

personas y la calidad de vida.

 El punto de máximo impacto se encuentra a escasos 500 m de la fuente

emisora alcanzando una magnitud de 0,01 mg/m [3] N.

**6.4.** **Evaluación discreta de las concentraciones de contaminantes**

A continuación se presentan los resultados obtenidos de la evaluación discreta de la

concentración de los contaminantes estudiados. Los puntos fueron seleccionados

según los criterios explicados en metodología y la distribución espacial de los puntos

receptores mostrada en la Figura 9.

**6.4.1.** **Material Particulado: MP10 y MP2,5**

En la

Página **57** de **69**

Tabla 10, se presentan los resultados obtenidos de la modelación discreta de MP10 y

MP2,5 diario, calculado como el percentil 98 y el promedio anual.

De los resultados presentados anteriormente se puede concluir lo siguiente:

 Los resultados obtenidos son congruentes con los resultados presentados en las

Figura 29 y Figura 30. En efecto, a concentración más alta modelada en puntos

discretos corresponde a los puntos receptores 1 y el 2, ubicados a 421 m al

norte de la planta y a 1.083 m al noreste respectivamente.

 Los valores de la concentración promedio anual y diario de MP10 y MP2,5 en

los receptores más cercanos al área del proyecto: 3, 4, 5, 6 y 7 resultaron ser

de baja magnitud.

 Las comunas de Temuco y Padre Las Casas no reciben un aporte importante de

MP10 y MP2,5 en su concentración diaria y anual. De hecho las concentraciones

modeladas en los puntos receptores 8, 9, 10, 11, 12 y 13 son de baja

magnitud, incluso llegando a valores de 0 μg/m [3] N en los puntos 9, 10, 11 y 12

en la concentración promedio anual.

 Respecto a los puntos receptores pasivos correspondientes a los puntos

receptores 14, 15, 16 y 17 lejanos a la ciudad y al punto de emisión no reciben

concentración de material particulado MP10 y MP2,5.

Página **58** de **69**

**Tabla 10. Concentración Modelada Diaria y Anual de MP10 y MP2,5**

|Receptor|Distancia a la planta<br>(m)|Promedio Anual MP10<br>(μg/m3)|Concentración diaria<br>MP10 (μg/m3)|Promedio Anual<br>MP2,5 (μg/m3)|Concentración diaria<br>MP2,5 (μg/m3)|
|---|---|---|---|---|---|
|1|421|0,17|0,66|0,05|0,20|
|2|1.083|0,10|0,39|0,03|0,12|
|3|750|0,04|0,18|0,01|0,05|
|4|1.504|0,03|0,13|0,01|0,04|
|5|2.800|0,02|0,10|0,01|0,03|
|6|1.344|0,03|0,11|0,01|0,04|
|7|1.816|0,03|0,16|0,01|0,05|
|8|2.891|0,02|0,07|0,01|0,02|
|9. Estación Museo Ferroviario|4.932|0,01|0,04|0,00|0,01|
|10. Estación Las Encinas|9.907|0,00|0,02|0,00|0,01|
|11. Estación Padre Las Casas 2|9.754|0,00|0,02|0,00|0,00|
|12. Estación Padre Las Casas|10.225|0,00|0,01|0,00|0,00|
|13|9.068|0,00|0,02|0,00|0,01|
|14|6.921|0,00|0,02|0,00|0,01|
|15|14.487|0,00|0,01|0,00|0,00|
|16|6.713|0,00|0,02|0,00|0,00|
|17|13.288|0,00|0,01|0,00|0,00|

Nota: En sombreado celeste se presentan los puntos receptores correspondientes a estaciones de monitoreo y en morado los puntos receptores

pasivos.

Página **59** de **69**

Cabe destacar que la concentración obtenida en la modelación de dispersión de

contaminante es menor a la presentada en las tablas, debido a que estas últimas

corresponden a la concentración modelada a una altura de 2 m sobre el nivel del suelo

y las primeras a la concentración promedio entre los 0 y 20 m correspondientes a la

primera capa vertical de modelación.

**6.4.2.** **Gases: SO2, NOx y CO**

A continuación se presentan los resultados de la concentración modelada de NO X, SO 2

y CO.

**El análisis fue realizado según la normativa aplicable, por ejemplo, se medió**

**concentración de CO promedio horaria y de 8 horas calculada como el**

**los máximos diarios, según las disposiciones del D.S. 115/2002**

**concentración del SO** **2** **fue calculada en la concentración anual y el percentil**

**promedio de 24 horas, tal como lo especifica ele D.S.113/2002**

**concentración de NO** **X** **fue trabajada como la concentración anual y el**

**los máximos diarios. Los resultados obtenidos se presentan en la**

Página **60** de **69**

Tabla 11.

De los resultados obtenidos se puede concluir lo siguiente:

 - La concentración de NOx, SO 2 y CO no representan un aporte sustancial. De

hecho, muchas de las concentraciones modeladas resultaron ser de 0 μg/m [3] N.

 Debido a que la resolución de los equipos monitores es de 0,1 μg/m [3] N, es

decir, mucha de las concentraciones mostradas en la tabla precedente no

serían siguiera captadas por los equipos monitores.

 Los resultados obtenidos son mayores en aquellos puntos más cercanos a la

fuente y ubicados hacia el norte y noreste de la fuente emisora, tales como los

puntos receptores 1 y 2.

 A medida que se avanza hacia el suroeste de la fuente emisora las

concentraciones de gases disminuyen considerablemente. De hecho, las

concentraciones en los puntos receptores de las estaciones de monitoreo

correspondientes a los puntos 9, 10, 11 y 12 es despreciable.

Página **61** de **69**

**Tabla 11. Concentración Modelada de NOx, SO** **2** **y CO**

|Receptor|Concentración NOx (μg/m3N)|Col3|Concentración SO (μg/m3N)<br>2|Col5|Concentración CO (mg/m3N)|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**Promedio Anual**|**Horaria (P99**<br>**máximos horarios)**|**Promedio Anual**|**Diario**<br>**(P 99)**|**8 horas (P99**<br>**máximos diarios)**|**1 hora**<br>**(P99 máximos**<br>**diarios**|
|1|0,48|19,22|0,04|1,11|0,001|0,000|
|2|0,24|12,32|0,02|0,64|0,001|0,000|
|3|0,09|5,34|0,01|0,33|0,000|0,000|
|4|0,04|2,35|0,00|0,16|0,000|0,000|
|5|0,04|1,48|0,00|0,09|0,000|0,000|
|6|0,04|2,56|0,00|0,17|0,000|0,000|
|7|0,05|5,07|0,01|0,18|0,000|0,000|
|8|0,02|0,85|0,00|0,06|0,000|0,000|
|9. Estación Museo Ferroviario|0,01|0,35|0,00|0,03|0,000|0,000|
|10. Estación Las Encinas|0,00|0,06|0,00|0,01|0,000|0,000|
|11. Estación Padre Las Casas 2|0,00|0,11|0,00|0,01|0,000|0,000|
|12. Estación Padre Las Casas|0,00|0,18|0,00|0,01|0,000|0,000|
|13|0,00|0,10|0,00|0,01|0,000|0,000|
|14|0,00|0,25|0,00|0,02|0,000|0,000|
|15|0,00|0,02|0,00|0,00|0,000|0,000|
|16|0,00|0,15|0,00|0,01|0,000|0,000|
|17|0,00|0,02|0,00|0,00|0,000|0,000|

Nota: En sombreado celeste se presentan los puntos receptores correspondientes a estaciones de monitoreo y en morado los puntos receptores

pasivos.

Página **62** de **69**

**6.5.** **Aporte de las concentraciones generadas a la condición basal, año**

**2014**

A continuación, se presenta el aporte a las concentraciones generadas en la condición

basal.

Dentro de todos los contaminantes estudiados el SINCA [5] reporta datos horarios de

concentración mayor a 75% sólo para el MP10 y MP2,5, respecto a los gases: NO 2, SO 2

y CO, la cantidad de datos disponible es insuficiente. Por lo tanto en éste informe sólo

se presentará un análisis en torno a las concentraciones proyectadas anual y promedio

24 horas del MP10 y MP2,5.

**6.5.1.** **Material Paniculado Respirable, MP10**

En la Tabla 12 se muestra el aumento de la concentración promedio anual respecto del

año base. Según los datos obtenidos, la única estación en la que se prevé un aumento

en la concentración de MP10 promedio anual es en la Estación Museo Ferroviario, pues

es más cercana a la fuente emisora, sin embargo, dicho aumento sería de tan sólo

0,018%, llegando a una concentración de 54,28 μg/m [3] N.

**Tabla 12. Aumento de la concentración basal de MP10 como concentración**

**promedio anual**

|Estación|Distancia<br>a la<br>planta<br>(m)|Promedio<br>anual año<br>base<br>(μg/m3N)|Promedio<br>Anual MP10<br>(μg/m3N)|Aumento en la<br>concentración<br>(%)|Concentración<br>proyectada<br>(μg/m3N)|
|---|---|---|---|---|---|
|Museo<br>Ferroviario|4.932|54,27|0,01|0,018|54,28|
|Las Encinas|9.907|47,38|0,00|0,000|47,38|
|Padre Las Casas<br>II|9.754|64,87|0,00|0,000|64,87|
|Padre Las Casas|10.225|Sin datos|0,00|-|-|

En relación a la concentración promedio diaria de MP10, calculada como el percentil

98, los resultados de la concentración proyectada de MP10 se presentan en la

siguiente tabla.

5 Sistema de Información Nacional de Calidad del Aire

Página **63** de **69**

**Tabla 13. Aumento de la concentración basal de MP10 como concentración**

**promedio diario**

|Estación|Distancia<br>a la<br>planta<br>(m)|Promedio<br>anual año<br>base<br>(μg/m3N)|Promedio<br>Anual MP10<br>(μg/m3N)|Aumento en la<br>concentración<br>(%)|Concentració<br>n proyectada<br>(μg/m3N)|
|---|---|---|---|---|---|
|Museo<br>Ferroviario|4.932|203,0|0,04|0,019|203,04|
|Las Encinas|9.907|173,8|0,02|0,012|173,82|
|Padre Las<br>Casas II|9.754|228,7|0,02|0,008|228,73|
|Padre Las<br>Casas|10.225|Sin datos|0,01|-|-|

A diferencia de los resultados obtenidos para la concentración promedio anual de

MP10, la concentración promedio diaria alcanza valores en todas las estaciones del

estudio. Esto se debe a que la concentración promedio diaria, corresponde a la

concentración del octavo día del año en orden descendente de la magnitud de la

concentración, es decir, corresponde a la concentración de 1 día del año, en donde

probablemente las condiciones de dispersión de contaminantes fueron desfavorables

debido a periodos de vientos calmos, estabilidad atmosférica y/o inversión térmica.

En la estación Museo Ferroviario, se espera un aumento en la concentración basal del

0,019%, alcanzando una concentración de 203,04 μg/m [3] NLas estaciones Las Encinas y

Padre Las Casas II, experimentaran un aumento en la concentración basal de 0,02

μg/m [3] N, es decir, un 0,012 y 0,008% respectivamente.

Página **64** de **69**

de la planta lo esté en un 15,88%; análogamente, la estación Padre Las Casas II

supera en un 52,47% el límite normativo en la condición basal, con el funcionamiento

de la planta se dicha superación experimente un aumento de un 0,01%.

**6.5.2.** **4.5.2. Material Paniculado Fino Respirable, MP2,5**

En la Tabla 12 se presenta la condición basal de MP2,5 promedio anual en las

estaciones de monitoreo ubicadas en las comunas de Temuco y Padre las Casas.

**Tabla 14. Aumento de la concentración basal de MP2,5 como concentración**

**promedio anual**

|Estación|Distancia<br>a la<br>planta<br>(m)|Promedio<br>anual año<br>base<br>(μg/m3N)|Promedio<br>Anual MP10<br>(μg/m3N)|Aumento en la<br>concentración<br>(%)|Concentración<br>proyectada<br>(μg/m3N)|
|---|---|---|---|---|---|
|Museo<br>Ferroviario|4.932|37,55|0,00|0|37,56|
|Las Encinas|9.907|40,65|0,00|0|40,66|
|Padre Las Casas<br>II|9.754|46,28|0,00|0|46,28|
|Padre Las Casas|10.225|Sin datos|0,00|-|-|

Los resultados obtenidos, no representan un aumento en la concentración promedio

anual registradas en las estaciones bajo el escenario proyectado. Esto se debe

principalmente a que las emisiones de MP2,5 tan solo son 0,22 ton/año, lo que sumado

a la ubicación de planta BITUMIX CVV, a aproximadamente 5 km de la estación de

monitoreo más cercana, y los régimen de vientos de la ciudad.

En relación a la concentración de 24 horas de MP2,5, se prevé un aumento en la

concentración basal de 0,01 μg/m [3] N en las estaciones Museo Ferroviario y Las Encinas,

respeto a las otras estaciones, se espera que no exista aporte a la concentración basal

tal como se ve en la siguiente tabla.

**Tabla 15. Aumento de la concentración basal de MP2,5 como concentración**

**promedio diario**

|Estación|Distancia<br>a la<br>planta<br>(m)|Promedio<br>anual año<br>base<br>(μg/m3N)|Promedio<br>Anual MP10<br>(μg/m3N)|Aumento en la<br>concentración<br>(%)|Concentración<br>proyectada<br>(μg/m3N)|
|---|---|---|---|---|---|
|Museo<br>Ferroviario|4.932|171,0|0,01|0,027|171,01|

Página **65** de **69**

|Las Encinas|9.907|155,7|0,01|0,024|155,71|
|---|---|---|---|---|---|
|Padre Las Casas<br>II|9.754|160,7|0,00|0,000|160,0|
|Padre Las Casas|10.225|Sin datos|0,00|-|-|

A diferencia de los resultados obtenidos para la concentración promedio anual de

MP2,5, la concentración promedio diaria alcanza valores en todas las estaciones del

estudio. Esto se debe a que la concentración promedio diaria, corresponde a la

concentración del octavo día del año en orden descendente de la magnitud de la

concentración, es decir, corresponde a la concentración de 1 día del año, en donde

probablemente las condiciones de dispersión de contaminantes fueron desfavorables

debido a periodos de vientos calmos, estabilidad atmosférica y/o inversión térmica.

Los resultados obtenidos son de baja magnitud y no representan un cambio sustancial

respecto de la condición basal. De hecho, espera un aumento en la concentración

promedio 24 horas en las estaciones Museo Ferroviario y Las Encinas de 0,027 y

0,024% respectivamente.

Los resultados de las mediciones para la condición base de las concentraciones de 24

horas son el triple de la concentración establecida como límite, sin embargo el

funcionamiento de la planta BITUMIX CVV no aumenta el porcentaje de incumplimiento

respecto del límite normativo.

**6.6.** **Área de Influencia del proyecto.**

Con los resultados de obtenidos se estimaron área de influencia por contaminante

presentado en figura 39.

Cabe destacar que el área de influencia se estimó considerando las máximas

concentraciones modeladas, aun cuando el valor de la concentración sea de una

magnitud muy baja. Por ejemplo, las concentraciones de CO que son las que más área

ocupan, sin embargo las concentraciones máximas son del orden de 0,01 μg/m [3] N

como concentración máxima horaria; dicha concentración está muy lejos de afectar la

calidad de vida de las personas.

Tal como se puede ver en figura 39, el área de influencia se expande por 3,3 km [2] en

dirección al noreste de BITUMIX CVV. Ésta correspondería al área más impactada

producto de las emisiones generadas a la atmosferas durante el proceso llevado a cabo

en la planta, sin embargo, debido a la magnitud de éstas y la concentración generada

Página **66** de **69**

en el aire, no existiría en ningun caso un impacto negativo en la salud o calidad de vida

de las personas.

**Figura 39. Área de Influencia**

Página **67** de **69**

**7.** **Conclusión**

De acuerdo a los resultados obtenidos en la modelación se puede concluir que:

Debido a la predominancia de vientos Sur y Sur Oeste, los contaminantes se

dispersan hacia la zona noreste del área de estudio.

De acuerdo a los rangos de velocidad de viento, registrados en dos estaciones

meteorológicas, se puede inferir que en el área de estudio no existe una buena

dispersión de contaminantes, debido a un porcentaje considerable de velocidades

calmas (0 m/s) y vientos lentos.

Se evaluó mediante mapas de iso-concentración los aportes de contaminantes que

generará el futuro proyecto. En todos los caso se evidencio que las zonas más

afectadas son las que se encuentran hacia el norte y noreste de la fuente de

emisión, pero que dicha afectación no es sustancial, pues los resultados de la

modelación sugieren que se generará concentraciones bajas.

Para evaluar el efecto en los poblados cercanos a la planta, se realizó una

modelación en fuentes discretas. Para esto se definieron 17 receptores, seis de

estos correspondieron a puntos cercanos a la planta, cinco a receptores

emplazados dentro de las zonas más densamente pobladas y otros cinco lejanos

catalogados como puntos discretos. Los resultados de la modelación en los puntos

discretos, evidencian que los puntos con más altas concentraciones modeladas son

aquellos que se encuentran al norte y noreste del proyecto.

La evaluación de la concentración proyectada en las estaciones de monitoreo de la

ciudad, evidencian que el proyecto en ningún caso afectaría negativamente a la

calidad del aire, aportando concentraciones tales que representen un aumento

relevante en la concentración basal de los contaminantes estudiados, en especial,

aquellos críticos para la zona como MP10 y MP2,5.

Por lo tanto, considerando todo lo mencionado, se puede concluir que las futuras

emisiones atmosféricas de MP10, MP2,5, NO X, SO 2 y CO, no afectaran de manera

considerable la calidad del aire de la ciudad de Temuco y por tanto, no existirá

afectación a la salud y calidad de vida de las personas.

Página **68** de **69**

**Anexo 1. Resultados de la medición Isocinética**

En la siguiente tabla se muestra los resultados obtenidos en la medición isocinética

realizada a la fuente emisora.

|PARÁMETROS|C<br>1|C<br>2|C<br>prom|σ|
|---|---|---|---|---|
|Fecha|05/04/1<br>6|05/04/1<br>6|****|****|
|Hora|13:04|16:43|****|****|
|Hora|13:54|17:33|****|****|
|Conc. de Material Particulado,(mg/m3N) *) <br>|116,4|75,8|96,1|28,7|
|Conc. Corregida de Mat. Particulado, (mg/m~~3~~N) <br>*)|116,4|75,8|96,1|28,7|
|Emisión horaria, (kg/h)|1,648|0,949|1,298|0,5|
|Caudal de gases estandarizado, (m3N/h) *)|14.163|12.519|13.34<br>1|1.16<br>3|
|Exceso de aire, (%)|****|****|****|****|
|O2 (%)|14,0|13,8|13,9|0,1|
|CO2 (%)|3,8|3,8|3,8|0,0|
|CO (ppm)|725,0|800,0|762,5|53,0|
|Isocinetismo (%)|96,2|95,3|95,8|****|
|Humedad de los gases (%)|16,9|18,0|17,5|0,8|
|Velocidad de los gases (m/s)|14,75|13,33|14,04|1,01|
|Temperatura de los gases (°C)|127,1|130,3|128,7|2,2|
|Presión de trabajo (psi)|****|****|****|****|
|Consumo de combustible (kg/h)|****|****|****|****|
|Generación de Vapor (kg/h)**)|****|****|****|****|
|_*) Estandarización de resultados a: 298,15 K; 760 mm Hg y sin humedad._|_*) Estandarización de resultados a: 298,15 K; 760 mm Hg y sin humedad._|_*) Estandarización de resultados a: 298,15 K; 760 mm Hg y sin humedad._|_*) Estandarización de resultados a: 298,15 K; 760 mm Hg y sin humedad._|_*) Estandarización de resultados a: 298,15 K; 760 mm Hg y sin humedad._|

Página **69** de **69**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Normas de calidad aplicables al proyecto.****

| Normativa de calidad del aire primaria | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Contaminante** | **Límite Norma** | **Concentración** | **Decreto** |
| Material Particulado<br>(MP10) | 150 μg/m~~3~~N | Máxima Diaria | N° 58/1998<br>MINSEGPRES |
| Material Particulado<br>(MP10) | 50 μg/m3N <br> | Media anual | Media anual |
| Material Particulado<br>(MP2,5) | 50 μg/m~~3~~N | Máxima Diaria | N° 12/2011<br>MMA |
| Material Particulado<br>(MP2,5) | 20 μg/m3N <br> | Media anual | Media anual |
| Dióxido de azufre (SO2) | 80 μg/m~~3~~N <br> | Media anual | N° 113/2002<br>MINSEGPRES |
| Dióxido de azufre (SO2) | 250 μg/m~~3~~N | Máxima diaria | Máxima diaria |
| Dióxido de Nitrógeno<br>(NO2) | 400 μg/m3N | 1 hora | N° 114/2002<br>MNSEGPRES |
| Dióxido de Nitrógeno<br>(NO2) | 100 μg/m3N | Media anual | Media anual |
| Monóxido de Carbono<br>(CO) | 10 mg/m3N | 8 horas | N° 115/2002<br>MINSEGPRES |

**Tabla 2.: Concentración promedio anual de MP10, comunas Temuco y Padre****

| Año | Concentración Promedio Anual (μg/m3) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Año** | **Las Encinas** | **Museo Ferroviario** | **Padre las Casas II** | **Límite de la norma** |
| 2009 | 64,87 | 53,91 | - | 50 |
| 2010 | 62,77 | - | - | - |
| 2011 | 65,24 | 74,18 | - | - |

**Tabla 3.: Concentración promedio anual de MP2,5, comunas Temuco y Padre****

| Año | Concentración Promedio Anual (μg/m3) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Año** | **Las Encinas** | **Museo Ferroviario** | **Padre las Casas II** | **Límite de la norma** |
| 2009 | 45,08 | 37,98 | - | 20 |
| 2011 | 48,68 | 41,48 | - | - |
| 2012 | - | 43,44 | - | - |

**Tabla 4.: Coordenadas de vértices del área de estudio.****

| Vértice | Proyección: UTM, Huso 18 Sur ; Datum: WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (km)** | **Norte (km)** |
| Suroeste | 693,375 | 5.699,959 |
| Sureste | 728,375 | 5.699,959 |
| Noroeste | 728,375 | 5.724,959 |
| Noreste | 693,375 | 5.724,959 |

**Tabla 5.: Datos meteorológicos y geofísicos considerados en la modelación.****

| Categoría de datos | Parámetro | Fuente |
| --- | --- | --- |
| Meteorología de altura | Temperatura | National<br>Oceanic<br>and<br>Atmospheric Administration<br>(NOAA) |
| Meteorología de altura | Presión | Presión |
| Meteorología de altura | Velocidad de viento | Velocidad de viento |
| Meteorología de altura | Dirección de viento | Dirección de viento |
| Meteorología de Superficie | Temperatura | Estación Museo Ferroviario<br>Estación Las Encinas |
| Meteorología de Superficie | Presión | Presión |
| Meteorología de Superficie | Velocidad de viento | Velocidad de viento |
| Meteorología de Superficie | Dirección de viento | Dirección de viento |
| Meteorología de Superficie | Humedad relativa | Humedad relativa |
| Geofísicos | Elevación de Terreno | United<br>Stated<br>Geological<br>Survey (USGS) |
| Geofísicos | Uso de Suelo | Uso de Suelo |

**Tabla 6.: ** Emisiones atmosféricas puntuales generadas en la producción de asfalto.**

| Actividad | Emisiones Puntuales (ton/año) | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP10** | **MP2,5** | **CO** | **NOx** | **SO2 ** |
| Calentador Vertical y secador de<br>Asfalto | 0,72 | 0,22 | 8,57 | 2,57 | 0,18 |

**Tabla 7.: Ubicación puntos receptores****

| Puntos | Coordenadas UTM (km) | Col3 | Distancia desde<br>la fuente<br>emisora (m) |
| --- | --- | --- | --- |
| **Puntos** | **X ** | **Y ** | **Y ** |
| R1 | 5.714,313 | 714,958 | 421 |
| R2 | 5.714,708 | 715,772 | 1.803 |
| R3 | 5.713,818 | 714,309 | 50 |
| R4 | 5.713,015 | 713,851 | 1.504 |
| R5 | 5.715,867 | 717,056 | 2.800 |
| R6 | 5.714,963 | 714,242 | 1.344 |
| R7 | 5.712,401 | 716,087 | 1.816 |
| R8 | 5.712,273 | 712,674 | 2.891 |
| R9. Estación Ferroviaria | 5.710,886 | 711,145 | 4.932 |
| R10. Estación Las Encinas | 5.708,391 | 706,773 | 9.906 |
| R11. Estación Padre Las Casas II | 5.708,391 | 708,623 | 9.754 |
| R12. Estación Padre Las Casas | 5.706,571 | 708,933 | 10.225 |

**Tabla 8.: Dirección y velocidad de viento estacional, estación Museo****

| Estaciones | Dirección de Vector<br>Resultante | Velocidades Predominantes<br>y Calmas (m/s) | Frecuencia<br>% |
| --- | --- | --- | --- |
| Verano | OSO (53%) | 0,5-2,1 | 68,3 |
| Verano | OSO (53%) | 2,1-3,6 | 16,6 |
| Verano | OSO (53%) | 3,6-5,7 | 6,5 |
| Verano | OSO (53%) | Calma | 8,6 |
| Otoño | S (54%) | 0,5-2,1 | 60,9 |
| Otoño | S (54%) | 2,1-3,6 | 14,5 |
| Otoño | S (54%) | 3,6-5,7 | 3,6 |
| Otoño | S (54%) | Calmas | 20,3 |
| Invierno | SSE (78 %) | 0,5-2,1 | 58,1 |
| Invierno | SSE (78 %) | 2,1-3,6 | 15,7 |
| Invierno | SSE (78 %) | 3,6-5,7 | 3,2 |
| Invierno | SSE (78 %) | Calmas | 21,8 |
| Primavera | SE (44 %) | 0,5-2,1 | 55,7 |
| Primavera | SE (44 %) | 2,1-3,6 | 22,3 |
| Primavera | SE (44 %) | 3,6-5,7 | 5,1 |
| Primavera | SE (44 %) | Calmas | 16,9 |

**Tabla 9.: Dirección y velocidad de viento estacional, medidas en la estación****

| Estaciones | Dirección de Vector<br>Resultante | Col3 | Velocidades Predominantes<br>y Calmas (m/s) | Col5 | Frecuencia<br>% |
| --- | --- | --- | --- | --- | --- |
| Verano | Verano | OSO (50 %) | 0,5-2,1 | 54,5 | 54,5 |
| Verano | Verano | OSO (50 %) | 2,1-3,6 | 23,1 | 23,1 |
| Verano | Verano | OSO (50 %) | 3,6-5,7 | 10,0 | 10,0 |
| Verano | Verano | OSO (50 %) | Calma | 12,1 | 12,1 |
| Otoño | Otoño | O (12 %) | 0,5-2,1 | 63,7 | 63,7 |
| Otoño | Otoño | O (12 %) | 2,1-3,6 | 16,2 | 16,2 |
| Otoño | Otoño | O (12 %) | 3,6-5,7 | 5,8 | 5,8 |
| Otoño | Otoño | O (12 %) | Calmas | 13,4 | 13,4 |
| Invierno | Invierno | ONO (8 %) | 0,5-2,1 | 62,5 | 62,5 |
| Invierno | Invierno | ONO (8 %) | 2,1-3,6 | 17,5 | 17,5 |
| Invierno | Invierno | ONO (8 %) | 3,6-5,7 | 6,1 | 6,1 |
| Invierno | Invierno | ONO (8 %) | Calmas | 12,6 | 12,6 |
| Primavera | Primavera | OSO (39 %) | 0,5-2,1 | 66,8 | 66,8 |
| Primavera | Primavera | OSO (39 %) | 2,1-3,6 | 22,4 | 22,4 |
| Primavera | Primavera | OSO (39 %) | 3,6-5,7 | 5,4 | 5,4 |
| Primavera | Primavera | OSO (39 %) | Calmas | 5,4 | 5,4 |

**Tabla 10.: Concentración Modelada Diaria y Anual de MP10 y MP2,5****

| Receptor | Distancia a la planta<br>(m) | Promedio Anual MP10<br>(μg/m3) | Concentración diaria<br>MP10 (μg/m3) | Promedio Anual<br>MP2,5 (μg/m3) | Concentración diaria<br>MP2,5 (μg/m3) |
| --- | --- | --- | --- | --- | --- |
| 1 | 421 | 0,17 | 0,66 | 0,05 | 0,20 |
| 2 | 1.083 | 0,10 | 0,39 | 0,03 | 0,12 |
| 3 | 750 | 0,04 | 0,18 | 0,01 | 0,05 |
| 4 | 1.504 | 0,03 | 0,13 | 0,01 | 0,04 |
| 5 | 2.800 | 0,02 | 0,10 | 0,01 | 0,03 |
| 6 | 1.344 | 0,03 | 0,11 | 0,01 | 0,04 |
| 7 | 1.816 | 0,03 | 0,16 | 0,01 | 0,05 |
| 8 | 2.891 | 0,02 | 0,07 | 0,01 | 0,02 |
| 9. Estación Museo Ferroviario | 4.932 | 0,01 | 0,04 | 0,00 | 0,01 |
| 10. Estación Las Encinas | 9.907 | 0,00 | 0,02 | 0,00 | 0,01 |
| 11. Estación Padre Las Casas 2 | 9.754 | 0,00 | 0,02 | 0,00 | 0,00 |
| 12. Estación Padre Las Casas | 10.225 | 0,00 | 0,01 | 0,00 | 0,00 |
| 13 | 9.068 | 0,00 | 0,02 | 0,00 | 0,01 |
| 14 | 6.921 | 0,00 | 0,02 | 0,00 | 0,01 |
| 15 | 14.487 | 0,00 | 0,01 | 0,00 | 0,00 |
| 16 | 6.713 | 0,00 | 0,02 | 0,00 | 0,00 |
| 17 | 13.288 | 0,00 | 0,01 | 0,00 | 0,00 |

**Tabla 11.: Concentración Modelada de NOx, SO** **2** **y CO****

| Receptor | Concentración NOx (μg/m3N) | Col3 | Concentración SO (μg/m3N)<br>2 | Col5 | Concentración CO (mg/m3N) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Promedio Anual** | **Horaria (P99**<br>**máximos horarios)** | **Promedio Anual** | **Diario**<br>**(P 99)** | **8 horas (P99**<br>**máximos diarios)** | **1 hora**<br>**(P99 máximos**<br>**diarios** |
| 1 | 0,48 | 19,22 | 0,04 | 1,11 | 0,001 | 0,000 |
| 2 | 0,24 | 12,32 | 0,02 | 0,64 | 0,001 | 0,000 |
| 3 | 0,09 | 5,34 | 0,01 | 0,33 | 0,000 | 0,000 |
| 4 | 0,04 | 2,35 | 0,00 | 0,16 | 0,000 | 0,000 |
| 5 | 0,04 | 1,48 | 0,00 | 0,09 | 0,000 | 0,000 |
| 6 | 0,04 | 2,56 | 0,00 | 0,17 | 0,000 | 0,000 |
| 7 | 0,05 | 5,07 | 0,01 | 0,18 | 0,000 | 0,000 |
| 8 | 0,02 | 0,85 | 0,00 | 0,06 | 0,000 | 0,000 |
| 9. Estación Museo Ferroviario | 0,01 | 0,35 | 0,00 | 0,03 | 0,000 | 0,000 |
| 10. Estación Las Encinas | 0,00 | 0,06 | 0,00 | 0,01 | 0,000 | 0,000 |
| 11. Estación Padre Las Casas 2 | 0,00 | 0,11 | 0,00 | 0,01 | 0,000 | 0,000 |
| 12. Estación Padre Las Casas | 0,00 | 0,18 | 0,00 | 0,01 | 0,000 | 0,000 |
| 13 | 0,00 | 0,10 | 0,00 | 0,01 | 0,000 | 0,000 |
| 14 | 0,00 | 0,25 | 0,00 | 0,02 | 0,000 | 0,000 |
| 15 | 0,00 | 0,02 | 0,00 | 0,00 | 0,000 | 0,000 |
| 16 | 0,00 | 0,15 | 0,00 | 0,01 | 0,000 | 0,000 |
| 17 | 0,00 | 0,02 | 0,00 | 0,00 | 0,000 | 0,000 |

**Tabla 12.: Aumento de la concentración basal de MP10 como concentración****

| Estación | Distancia<br>a la<br>planta<br>(m) | Promedio<br>anual año<br>base<br>(μg/m3N) | Promedio<br>Anual MP10<br>(μg/m3N) | Aumento en la<br>concentración<br>(%) | Concentración<br>proyectada<br>(μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Museo<br>Ferroviario | 4.932 | 54,27 | 0,01 | 0,018 | 54,28 |
| Las Encinas | 9.907 | 47,38 | 0,00 | 0,000 | 47,38 |
| Padre Las Casas<br>II | 9.754 | 64,87 | 0,00 | 0,000 | 64,87 |
| Padre Las Casas | 10.225 | Sin datos | 0,00 | - | - |

**Tabla 13.: Aumento de la concentración basal de MP10 como concentración****

| Estación | Distancia<br>a la<br>planta<br>(m) | Promedio<br>anual año<br>base<br>(μg/m3N) | Promedio<br>Anual MP10<br>(μg/m3N) | Aumento en la<br>concentración<br>(%) | Concentració<br>n proyectada<br>(μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Museo<br>Ferroviario | 4.932 | 203,0 | 0,04 | 0,019 | 203,04 |
| Las Encinas | 9.907 | 173,8 | 0,02 | 0,012 | 173,82 |
| Padre Las<br>Casas II | 9.754 | 228,7 | 0,02 | 0,008 | 228,73 |
| Padre Las<br>Casas | 10.225 | Sin datos | 0,01 | - | - |

**Tabla 14.: Aumento de la concentración basal de MP2,5 como concentración****

| Estación | Distancia<br>a la<br>planta<br>(m) | Promedio<br>anual año<br>base<br>(μg/m3N) | Promedio<br>Anual MP10<br>(μg/m3N) | Aumento en la<br>concentración<br>(%) | Concentración<br>proyectada<br>(μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Museo<br>Ferroviario | 4.932 | 37,55 | 0,00 | 0 | 37,56 |
| Las Encinas | 9.907 | 40,65 | 0,00 | 0 | 40,66 |
| Padre Las Casas<br>II | 9.754 | 46,28 | 0,00 | 0 | 46,28 |
| Padre Las Casas | 10.225 | Sin datos | 0,00 | - | - |

**Tabla 15.: Aumento de la concentración basal de MP2,5 como concentración****

| Estación | Distancia<br>a la<br>planta<br>(m) | Promedio<br>anual año<br>base<br>(μg/m3N) | Promedio<br>Anual MP10<br>(μg/m3N) | Aumento en la<br>concentración<br>(%) | Concentración<br>proyectada<br>(μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Museo<br>Ferroviario | 4.932 | 171,0 | 0,01 | 0,027 | 171,01 |
