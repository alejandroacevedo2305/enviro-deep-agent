---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 45
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE CRECIDAS PROYECTO PLANTA FOTOVOLTAICA CORNIGLIA
-->

## ADENDA EN RESPUESTA AL INFORME CONSOLIDADO DE SOLICITUD DE ACLARACIONES, RECTIFICACIONES Y/O AMPLIACIONES A LA DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO PLANTA FOTOVOLTAICA CORNIGLIA ANEXO AC-5.10 ESTUDIO DE CRECIDAS

#### Noviembre 2024

Informe Técnico

2024

Revisión 2

# ESTUDIO DE CRECIDAS PROYECTO PLANTA FOTOVOLTAICA CORNIGLIA

info@flujoing.cl / www.flujoing.cl /+562 29798241

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

### CONTENIDO

1. GENERALIDADES ............................................................................................................................4

2. OBJETIVOS.......................................................................................................................................... 5

3. ANALISIS HIDROLOGICO ............................................................................................................ 5

3.1. CUENCAS APORTANTES ............................................................................... 5

3.1.1. PARÁMETROS MORFOMÉTRICOS ........................................................... 7

3.1.2. TIEMPO DE CONCENTRACIÓN .............................................................. 7

3.2. ANALISIS DE PRECIPITACIONES ................................................................... 8

3.2.1. PRECIPITACIONES MÁXIMAS .................................................................. 8

3.2.2. GENERACIÓN CURVAS IDF ................................................................... 12

3.3. ANALISIS DE CAUDALES .............................................................................. 15

4. ANÁLISIS HIDRÁULICO .............................................................................................................. 18

4.1. METODOLOGÍA DE LA MODELACIÓN ....................................................... 19

4.2. FUNDAMENTOS DE LA MODELACIÓN CON HEC-RAS 2D ......................... 19

4.3. GEOMETRÍA ................................................................................................. 21

4.4. MALLA DE CÁLCULO ................................................................................... 22

4.5. RUGOSIDAD ................................................................................................ 23

4.6. CONDICIONES DE CONTORNO ............................................................... 26

4.1. CONDICIONES INICIALES Y SINGULARIDADES ........................................ 28

4.2. SIMULACIÓN Y POSTPROCESO ................................................................. 28

4.3. RESULTADOS Y ANALISIS DE INUNDACIONES ......................................... 29

5. OBRAS PROPUESTAS ................................................................................................................ 37

5.1. BADÉN ......................................................................................................... 37

5.2. ATRAVIESO ALCANTARILLA BAJO CAMINO DE ACCESO .......................... 39

6. APLICABILIDAD PAS 156 ........................................................................................................... 41

7. CONCLUSIÓN .................................................................................................................................. 41

8. BIBLIOGRAFÍA ............................................................................................................................... 43

info@flujoing.cl / www.flujoing.cl

1

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

### Índice de Gráficos

Gráfico 1. Curvas IDF duración mayor a 1 hora. ........................................................... 14

Gráfico 2. Curvas IDF duración menor a 1 hora. .......................................................... 15

### Índice de Tablas

Tabla 1. Parámetros Morfométricos. .............................................................................. 7

Tabla 2. Tiempos de concentración en minutos estimados por cuenca. ......................... 8

Tabla 3. Datos estación meteorológica utilizada. .......................................................... 9

Tabla 4. Serie de datos de precipitaciones máximas en 24 h adoptados. .................... 10

Tabla 5. Precipitación máxima diaria considerando distintas funciones de probabilidad.

..................................................................................................................................... 11

Tabla 6. Precipitaciones máximas diarias AF. ................................................................ 11

Tabla 7. Precipitaciones máximas en 24 horas con corrección. .................................... 12

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 11 | ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA -->

**Tabla 7: que serán utilizados para las estimaciones hidrológicas que se analicen según**

| Período de retorno PP máximas 24 horas<br>(años) (mm) | Col2 |
| --- | --- |
| 2 | 62.5 |
| 5 | 90.5 |
| 10 | 109.1 |
| 25 | 132.5 |
| 50 | 149.9 |
| 100 | 167.1 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 7. Precipitaciones máximas en 24 horas con corrección.** **Fuente: Elaboración propia.** -->
<!-- FIN TABLA 7 -->


Tabla 8. Precipitaciones máximas Plan Maestro de Aguas Lluvias de Concón. ............. 12

Tabla 9. Coeficientes de duración estación Quillota. ................................................... 13

Tabla 10. Curvas IDF duración mayor a 1 hora. ............................................................ 13

Tabla 11. Intensidad (mm/h) duración menor a 1 hora. ................................................. 14

Tabla 12. Determinación coeficiente de escorrentía cuencas. ........................................ 17

Tabla 13. Coeficientes de escorrentía para método racional. ....................................... 17

Tabla 14. Intensidades según Tc para Método Racional. .............................................. 17

Tabla 15. Caudales determinados por Método Racional. ............................................. 18

Tabla 16. Coeficiente de rugosidad Cowan Quebradas Tipo A. .................................. 25

Tabla 17. Coeficiente de rugosidad Cowan Quebradas Tipo B. .................................. 25

Tabla 18. Coeficiente de rugosidad Cowan Quebradas Tipo C. .................................. 25

Tabla 19. Coeficiente de rugosidad determinado para las distintas quebradas. .......... 26

Tabla 20. Hidrograma de caudales máximos instantáneos para T-100 años. .............. 28

info@flujoing.cl / www.flujoing.cl

2

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

### Índice de Figuras

Figura 1. Delimitación de cuencas hidrográficas. ........................................................... 6

Figura 2. Ubicación estación meteorológica utilizada. .................................................. 9

Figura 3. Área de modelación hidráulica PFV Corniglia. .............................................. 19

Figura 4. Geometría del modelo. ................................................................................ 22

Figura 5. Mallas de cálculo sector Parque (izquierda) y camino acceso (derecha). .... 23

Figura 6. Imágenes de quebradas analizadas para determinación de rugosidad. ..... 24

Figura 7. Condiciones de contorno aplicadas al modelo sector Parque. ..................... 27

Figura 8. Condiciones de contorno aplicadas al modelo sector Camino de Acceso. ... 27

Figura 9. Perfil longitudinal hidráulico SC1, sector Parque. .......................................... 30

Figura 10. Perfil longitudinal hidráulico SC2, sector Parque. ........................................ 30

Figura 11. Perfil longitudinal hidráulico SC3, sector Parque. .......................................... 31

Figura 12. Perfil longitudinal hidráulico SC4, sector Parque. ......................................... 31

Figura 13. Perfil longitudinal hidráulico SC5, sector Camino de Acceso. ...................... 32

Figura 14. Perfil longitudinal hidráulico SC6, sector Camino de Acceso. ...................... 32

Figura 15. Profundidades de flujo inundación T-100, sector Parque. ............................. 34

Figura 16. Profundidades de flujo inundación T-100, sector Camino de Acceso. ........... 34

Figura 17. Velocidades de flujo inundación T-100, sector Parque. ................................ 35

Figura 18. Velocidades de flujo inundación T-100, sector Camino de Acceso. .............. 36

Figura 19. Ubicación futura del badén proyectado en la Quebrada SC6. ................... 37

Figura 20. Planta Badén sin escurrimiento permanente. .............................................. 38

Figura 21. Corte A-A Baden sin escurrimiento permanente. .......................................... 38

Figura 22. Corte B-B Baden sin escurrimiento permanente. ......................................... 39

Figura 23. Cajón doble de hormigón armado. ............................................................ 39

Figura 24. Capacidad de la obra a instalar. .............................................................. 40

Figura 25. Disposición de cajón doble de hormigón armado sobre el canal. ............... 41

info@flujoing.cl / www.flujoing.cl

3

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

##### 1. GENERALIDADES

En el presente informe se detallan los análisis hidrológicos e hidráulicos realizados para

desarrollar un estudio de crecidas sobre los cauces naturales que forman parte del Área

de Influencia (AI) determinada para el componente hídrico del proyecto “Planta

Fotovoltaica Corniglia”. Se consideran los aspectos metodológicos, análisis de

resultados y principales conclusiones.

El proyecto se encuentra emplazado en la comuna de Quinteros, región de Valparaíso

y consiste en la construcción y operación de un proyecto de parque fotovoltaico

destinado a la generación y almacenamiento energético.

El área considerada para el este estudio, y en específico los cauces naturales analizados,

se determinaron a partir de la caracterización hidrológica del proyecto, donde se definió

su área de influencia y se identificaron seis cauces naturales que se ubican en las

cercanías del proyecto y camino de acceso para los cuales se consideró relevante

efectuar un análisis de inundaciones.

Se desarrolla en este informe un análisis hidrológico de crecidas, con el fin de obtener

los caudales máximos ordinarios y extraordinarios para los cauces identificados. Para

esto, debido a que estos cauces no poseen control fluviométrico, se utilizará el método

racional según las indicaciones del Manual de Carreteras para las cuencas pequeñas,

mientras que, para las cuencas de mayor tamaño, de existir, se utilizarán los métodos

recomendados en el Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas

Sin Información Fluviométrica (DGA, 1995).

Posteriormente se realizan los análisis hidráulicos utilizando una metodología de

modelación numérica bidimensional mediante el software HEC-RAS, ampliamente

utilizado para la simulación de flujos en ríos y estuarios. Se desarrolla un modelo para

los tramos de interés de los cauces en estudio, considerando sus secciones normales de

escurrimiento, sus singularidades y sus zonas aledañas potencialmente inundables. Se

desarrolla en este informe lo respectivo a la construcción del modelo y sus condiciones

de modelación, así como también el análisis de inundaciones para el escenario de

periodo de retorno de 100 años, considerando las principales variables hidráulicas

obtenidas y su posible influencia sobre las obras del proyecto.

info@flujoing.cl / www.flujoing.cl

4

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

##### 2. OBJETIVOS

 Desarrollar los análisis hidrológicos que permitan obtener los caudales máximos

instantáneos de crecida para los cauces naturales identificados.

 Desarrollar los análisis mediante modelación hidráulica que permitan

caracterizar el comportamiento de los flujos de crecida de los cauces

identificados.

 Definir los límites y parámetros hidráulicos de inundación de los cauces

identificados y analizar su posible relación con las obras y componentes del

proyecto.

 Definir la aplicabilidad de permisos ambientales sectoriales de modificación de

cauces (PAS 156) y/o regularización o defensas fluviales (PAS 157).

##### 3. ANALISIS HIDROLOGICO

En este capítulo se entregan los antecedentes del estudio hidrológico de crecidas para

las cuencas aportantes al área de estudio hidráulico del proyecto. Según se detallará,

los cauces naturales analizados corresponden a 6 quebradas sin nombre.

Es importante mencionar que los análisis hidrológicos realizados son exclusivamente

sobre aportes pluviales, ya que la línea de nieves en la latitud del proyecto (Latitud

32.8°) está sobre los 1940 m.s.n.m. (Manual de Cálculo de Crecidas y Caudales Mínimos

en Cuencas sin Información Fluviométrica, DGA 1995), considerándose despreciable el

aporte nival para las elevaciones del área de estudio.

3.1. CUENCAS APORTANTES

Para determinar los cauces y sus respectivas cuencas aportantes al área de estudio, junto

con sus distintos parámetros morfométricos de interés, se utilizó información del modelo

de elevación digital de la zona (DEM) del satélite Alos Palsar, con una resolución del

píxel de 12.5x12.5 m, el cual fue descargado del portal Infraestructura de Datos

Geoespaciales de Chile (IDE Chile). Se utilizó también el levantamiento topográfico

info@flujoing.cl / www.flujoing.cl

5

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

realizado para el área de estudio, el cual cubrió una superficie aproximada de 80

hectáreas, otorgando un mayor nivel de detalle en la zona de interés.

Dicha información de elevación se procesó a través de una plataforma SIG, delimitando

el trazado de los cauces y sus cuencas aportantes, obteniendo también los principales

parámetros morfométricos que las caracterizan y que son requeridos para los distintos

métodos hidrológicos aplicables para la obtención de los caudales de crecida.

En la _Figura 1_, se muestran las cuencas hidrográficas para los cauces naturales en estudio

del sector.

**Figura 1. Delimitación de cuencas hidrográficas.**

**Fuente: Elaboración propia, plataforma SIG.**

Como es posible observar, las cuencas determinadas tienen superficies que varían entre

los 0.11 km [2] a 0.72 km [2] . Se destaca que, las quebradas identificadas corresponden a

cauces de escurrimientos intermitentes, que solo presentan flujos de corta duración en

respuesta directa a eventos de precipitación.

info@flujoing.cl / www.flujoing.cl

6

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

3.1.1. PARÁMETROS MORFOMÉTRICOS

Para el análisis hidrológico de las cuencas delimitadas, en particular para la aplicación

de las distintas metodologías disponibles, es necesaria la definición y obtención de los

parámetros morfométricos de las cuencas. Los parámetros de interés corresponden al

Área (A), Longitud de la cuenca (L), Longitud al centro de gravedad (Lg), Pendiente

media del cauce principal (S), Pendiente media de la cuenca (), Desnivel máximo de la

cuenca (H), Desnivel medio de la cuenca (Hm) y Latitud de la cuenca (Lat).

Todos estos parámetros son determinados a partir de una herramienta SIG,

considerando las fuentes de datos de elevación ya mencionadas y la delimitación de

trazado de los cauces y áreas aportantes previamente definidas.

Los parámetros determinados se resumen a continuación en la Tabla 1.

|L L S S A H H Lat<br>Cuenca g c m<br>km km m/m m/m km2 m m °|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Cuenca<br>L <br>Lg <br>S <br>Sc <br>A <br>H <br>Hm <br>Lat<br>km<br>km<br>m/m<br>m/m<br>km2 <br>m <br>m <br>°|km|km|m/m|m/m|km2|m|m|°|
|SC1|0.67|0.48|0.050|0.107|0.22|33.8|24|32.8|
|SC2|0.70|0.42|0.072|0.173|0.11|50.6|28|32.8|
|SC3|0.89|0.58|0.068|0.151|0.15|60.1|27.3|32.8|
|SC4|0.48|0.39|0.083|0.135|0.13|39.4|23.6|32.8|
|SC5|1.38|0.69|0.046|0.156|0.72|63|20|32.8|
|SC6|0.88|0.58|0.102|0.134|0.23|89.9|56.7|32.8|

**Tabla 1. Parámetros Morfométricos.**

**Fuente: Elaboración propia.**

3.1.2. TIEMPO DE CONCENTRACIÓN

El tiempo de concentración corresponde a un concepto ampliamente utilizado en

hidrología para evaluar la respuesta hidrológica de una cuenca a un evento de

precipitación, y corresponde al tiempo característico en el cual la totalidad de una

cuenca contribuye al caudal en el punto de salida de esta. Su determinación es necesaria

para la utilización de metodologías hidrológicas para caudales de crecida, tales como

el método racional e hidrogramas unitarios.

Para estimar el tiempo de concentración de una cuenca (T c ) se empleó la expresión que

se recomienda en el Manual de Carreteras del Ministerio de Obras Públicas en su Tabla

3.702.501.A. para cuencas montañosas del autor California Culvert Practice (1942)

info@flujoing.cl / www.flujoing.cl

7

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

ampliamente utilizada a nivel nacional al ser adecuada desde el punto de vista de la

seguridad.

T c = 57 ∗(L [3] ⁄ )H [0,385]

Donde:

 Tc: Tiempo de concentración (min).

 L: Longitud de cauce (km).

 H: Diferencia de nivel total entre cotas extremas de la cuenca (m).

Cabe destacar que de acuerdo con el Manual de Carreteras V3, este tipo de expresiones

son producto de resultados empíricos, obtenidos bajo ciertas condiciones particulares,

por lo tanto, como norma general, el tiempo de concentración no debe ser inferior a 10

minutos.

En la tabla a continuación se presentan los tiempos de concentración calculados con

esta metodología para cada una de las cuencas en estudio, considerando los

parámetros morfométricos e hidrológicos definidos en el acápite anterior.

|Cuenca T (CCP 1942) T adoptado<br>C C|Col2|Col3|
|---|---|---|
|SC1|9.26|10.00|
|SC2|8.36|10.00|
|SC3|10.25|10.25|
|SC4|5.89|10.00|
|SC5|16.74|16.74|
|SC6|8.71|10.00|

**Tabla 2. Tiempos de concentración en minutos estimados por cuenca.**

**Fuente: Elaboración propia.**

3.2. ANALISIS DE PRECIPITACIONES

Dado que no existen estaciones fluviométricas para los cauces en estudio, es necesario

estimar los caudales de crecidas a partir de métodos que relacionan la precipitación con

la escorrentía, siendo importante determinar las precipitaciones máximas asociadas a

los periodos de retorno de interés, junto con las curvas de Intensidad-Duración

Frecuencia (IDF) características del área de estudio.

3.2.1. PRECIPITACIONES MÁXIMAS

El cálculo de las precipitaciones máximas se realizó verificando las estaciones cercanas

al lugar de estudio y que contara con ciertas características, estas son: que cuenten con

info@flujoing.cl / www.flujoing.cl

8

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

un registro pluviométrico mayor a 20 años, que se localicen en las proximidades del

proyecto, que se encuentren en estado vigente y en el registro de estaciones de DGA, y

que posean una altitud similar a la zona de estudio.

Existen dos estaciones meteorológicas en las cercanías del proyecto que se detallan sus

parámetros a continuación:

|Estación|Los Aromos|
|---|---|
|Tipo|Meteorológica|
|Código BNA|05427007-0|
|WGS 84 H19S Este|280.800|
|WGS 84 H19S Norte|6.350.896|
|Registro de datos|1983 al 2021|
|Distancia al proyecto|21.3 km al SE|
|Altitud|100 msnm|
|Cuenca|Río Aconcagua|
|Subcuenca|Rio Aconcagua Bajo (Entre<br>despues E Seco y Desemb)|

**Tabla 3. Datos estación meteorológica utilizada.**

**Fuente: Elaboración propia.**

**Figura 2. Ubicación estación meteorológica utilizada.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

9

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

En la siguiente tabla se muestra la serie de datos disponibles de precipitaciones máximas

en 24 horas por año, según el registro histórico de datos disponibles en dicha estación

entre los años 1983 y 2021.

Año Pp (mm) Año Pp (mm) Año Pp (mm)

1983 54.5 1996 57 2009 62

1984 77.3 1997 96 2010 39

1985 44.5 1998 13 2011 28.5

1986 73.5 1999 39 2012 68

1987 126.1 2000 101 2013 49.5

1988 40 2001 122 2014 66

1989 50 2002 120.5 2015 55

1990 41 2003 72.5 2016 43

1991 79.5 2004 57.5 2017 67

1992 101 2005 42 2018 67

1993 54 2006 84 2019 28

1994 71 2007 22 2020 38

1995 50 2008 95 2021 6.5

|Año Pp (mm)|Col2|
|---|---|
|1983|54.5|
|1984|77.3|
|1985|44.5|
|1986|73.5|
|1987|126.1|
|1988|40|
|1989|50|
|1990|41|
|1991|79.5|
|1992|101|
|1993|54|
|1994|71|
|1995|50|

|Año Pp (mm)|Col2|
|---|---|
|1996|57|
|1997|96|
|1998|13|
|1999|39|
|2000|101|
|2001|122|
|2002|120.5|
|2003|72.5|
|2004|57.5|
|2005|42|
|2006|84|
|2007|22|
|2008|95|

|Año Pp (mm)|Col2|
|---|---|
|2009|62|
|2010|39|
|2011|28.5|
|2012|68|
|2013|49.5|
|2014|66|
|2015|55|
|2016|43|
|2017|67|
|2018|67|
|2019|28|
|2020|38|
|2021|6.5|

**Tabla 4. Serie de datos de precipitaciones máximas en 24 h adoptados.**

**Fuente: DGA.**

De acuerdo con los antecedentes presentados anteriormente, se justifica la utilización de

los datos obtenidos a partir de la estación meteorológica Los Aromos, al ser datos

medidos en terreno durante los últimos 39 años y los más recientes.

Una vez definidos los datos de precipitaciones se realizó un análisis de frecuencia de los

datos, ajustando distintas distribuciones de probabilidad, para poder estimar las

precipitaciones para los diferentes períodos de retorno.

Para este Proyecto se analizan las series de distribución de frecuencia según los métodos

Normal, Log-Normal, Gumbel, Gamma, Pearson III y Log Pearson III. La serie de datos

fue analizada en el Subanexo No1 “Análisis de Frecuencia” del presente informe, en el

cual se obtuvieron las curvas de ajuste probabilístico, y a su vez se realizó el test de

bondad de ajuste Kolmogorov-Smirnov, obteniéndose los valores de precipitación

máxima diaria para las distintas funciones de probabilidad estudiadas.

info@flujoing.cl / www.flujoing.cl

10

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

|Período de retorno|Precipitación (mm)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|T|Normal|Log Normal|Gamma|Pearson III|LogPearson III|Gumbel|
|2|61.6|55.8|57.2|59.2|46.8|56.8|
|5|85.8|81.1|83.6|84.9|81.1|82.3|
|10|98.5|98.6|100.1|99.7|118.2|99.2|
|25|112.0|121.5|119.9|116.5|190.1|120.5|
|50|120.7|139.0|134.0|128.0|269.3|136.3|
|100|128.6|157.0|147.4|138.7|379.0|151.9|

**Tabla 5. Precipitación máxima diaria considerando distintas funciones de probabilidad.**

**Fuente: Elaboración propia.**

Del Subanexo No1 se destaca que la función de probabilidad que poseen mayor ajuste

a los valores extremos está dada por Gumbel, siendo la más apropiada para modelar

las precipitaciones (99.91% de ajuste), y a la vez, alcanza el mejor ajuste a los datos de

precipitación.

A partir de este análisis la precipitación máxima en 24 horas y período de retorno de 10

años es de P 2410 = 99.2 mm.

De acuerdo con los antecedentes presentados anteriormente, se justifica la utilización de

los datos obtenidos a partir de la estación Los Aromos, al ser datos medidos en terreno

durante 39 años y ser los datos más recientes, así como también se define utilizar la

distribución Gumbel para determinar la precipitación máxima diaria para los distintos

períodos de retorno. La Tabla 6 resume los valores definidos a partir del análisis de

frecuencia.

|Período de retorno Gumbel<br>(años) (mm)|Col2|
|---|---|
|2|56.8|
|5|82.3|
|10|99.2|
|25|120.5|
|50|136.3|
|100|151.9|

**Tabla 6. Precipitaciones máximas diarias AF.**

**Fuente: Elaboración propia.**

Finalmente, según las recomendaciones del Manual de Carreteras se utiliza el factor

k=1.1 para corregir los datos de precipitaciones máximas medidas entre 8 am y 8 am

respecto de las 24 horas más lluviosas de la tormenta, obteniendo los resultados de la

info@flujoing.cl / www.flujoing.cl

11

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

Tabla 7 que serán utilizados para las estimaciones hidrológicas que se analicen según

el Manual de Carreteras.

|Período de retorno PP máximas 24 horas<br>(años) (mm)|Col2|
|---|---|
|2|62.5|
|5|90.5|
|10|109.1|
|25|132.5|
|50|149.9|
|100|167.1|

**Tabla 7. Precipitaciones máximas en 24 horas con corrección.**

**Fuente: Elaboración propia.**

Independientemente de lo anterior, a solicitud de la autoridad y de forma conservadora,

para la determinación de las curvas IDF y cálculo de caudales que se presentan más

adelante en el presente informe, se utilizarán los valores de precipitaciones máximas

diarias de los distintos periodos de retorno que se determinaron en el PM-43 “Plan

Maestro de Evacuación y Drenaje de Aguas Lluvias de Concón” (Dirección de Obras

Hidráulicas, 2020), específicamente en el Volumen 1 Capítulo 3 “Estudios Básicos” (Ver

Subanexo 8), en el cual, para la estación Los Aromos, se calcularon los valores que se

presentan a continuación:

|Período de retorno PP máximas<br>(años) (mm)|Col2|
|---|---|
|2|66.7|
|5|99.8|
|10|123.3|
|25|146.9|
|50|178.7|
|100|203.7|

**Tabla 8. Precipitaciones máximas Plan Maestro de Aguas Lluvias de Concón.**

**Fuente: (Dirección de Obras Hidráulicas, 2020).**

3.2.2. GENERACIÓN CURVAS IDF

Para la determinación de las intensidades de precipitación, asociadas a distintas

duraciones y frecuencias, se identificó la existencia de una estación pluviográfica

cercana, correspondiente a la estación Quillota, para la cual el Manual de Carreteras

presenta curvas de duración que pueden ser extrapoladas a distintos puntos de la región

para la determinación de las curvas IDF.

info@flujoing.cl / www.flujoing.cl

12

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

A partir de los coeficientes de duración que se presentan en la Tabla 3.702.403.A

(Manual de Carreteras V3) es posible construir las curvas IDF de duración entre 1 y 24

horas, para distintos periodos de retorno, al conocer la precipitación máxima en 24

horas asociada a cada periodo de retorno en específico (Se utilizaron los valores de

precipitaciones máximas que se muestran en Tabla 8 del presente informe).

Se utilizaron entonces las precipitaciones máximas diarias determinadas y los

coeficientes de duración expuestos en la Tabla 9.

|Duración (horas)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Est. Pluv.**|1|2|4|6|8|10|12|14|18|24|
|**Quillota**|0.13|0.23|0.38|0.5|0.58|0.67|0.75|0.8|0.88|1|

**Tabla 9. Coeficientes de duración estación Quillota.**

**Fuente: Manual de carreteras V-3.**

Se obtuvieron a partir de lo anterior las intensidades presentadas en la Tabla 10 y las

curvas IDF ilustradas en el Gráfico 1.

|Duración<br>(min)|Intensidad (mm/h) para distintos T|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Duración<br>(min)|2|5|10|25|50|100|
|60|8.67|12.97|16.03|19.10|23.23|26.48|
|120|7.67|11.48|14.18|16.89|20.55|23.43|
|240|6.34|9.48|11.71|13.96|16.98|19.35|
|360|5.56|8.32|10.28|12.24|14.89|16.98|
|480|4.84|7.24|8.94|10.65|12.96|14.77|
|600|4.47|6.69|8.26|9.84|11.97|13.65|
|720|4.17|6.24|7.71|9.18|11.17|12.73|
|840|3.81|5.70|7.05|8.39|10.21|11.64|
|1080|3.26|4.88|6.03|7.18|8.74|9.96|
|1440|2.78|4.16|5.14|6.12|7.45|8.49|

**Tabla 10. Curvas IDF duración mayor a 1 hora.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

13

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Gráfico 1. Curvas IDF duración mayor a 1 hora.**

**Fuente: Elaboración Propia.**

Por otro lado, es necesario determinar también las curvas IDF para duraciones menores

a 1 hora, para lo cual es posible utilizar la expresión de Bell.

En primer lugar, se tiene a partir de las curvas IDF anteriores la precipitación máxima

asociada a una duración de 1 hora para los distintos periodos de retorno (según los

valores de precipitaciones máximas que se muestran en Tabla 7 del presente informe). A

partir de este valor, se aplicó la expresión de Bell que se presenta a continuación, sin su

componente de frecuencia, en consistencia con el análisis de frecuencia desarrollado:

T = (0,54 ∗t 0,25 −0.5) ∗P 1T

P t

T

Los resultados de la aplicación de la ecuación de Bell para la obtención de la intensidad

de precipitación se presentan en la Tabla 11, mientras que el Gráfico 2 muestra las curvas

IDF de duración menor a 1 hora obtenidas para la zona de estudio.

|Duración<br>(min)|Intensidad (mm/h) para distintos períodos de retorno|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Duración<br>(min)|2|5|10|25|50|100|
|5|31.99|47.87|59.14|70.47|85.72|97.71|
|10|23.95|35.83|44.27|52.74|64.16|73.13|
|15|19.52|29.20|36.08|42.98|52.29|59.60|
|20|16.70|24.99|30.87|36.78|44.74|51.00|
|25|14.72|22.03|27.22|32.43|39.44|44.96|
|30|13.25|19.82|24.49|29.17|35.49|40.45|
|35|12.09|18.09|22.35|26.63|32.39|36.93|
|40|11.16|16.70|20.63|24.58|29.90|34.08|
|45|10.39|15.54|19.21|22.88|27.83|31.73|
|50|9.74|14.57|18.00|21.45|26.09|29.74|
|55|9.18|13.74|16.97|20.22|24.60|28.04|
|60|8.67|12.97|16.03|19.10|23.23|26.48|

**Tabla 11. Intensidad (mm/h) duración menor a 1 hora.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

14

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Gráfico 2. Curvas IDF duración menor a 1 hora.**

**Fuente: Elaboración Propia.**

3.3. ANALISIS DE CAUDALES

En este capítulo se detalla la obtención de caudales máximos instantáneos para los

cauces de interés. Ninguno de los cauces analizados posee control fluviométrico, por lo

tanto, la estimación de caudales se realiza a partir de métodos que relacionan la

precipitación con la escorrentía, utilizando las caracterizaciones de las cuencas

aportantes y de las precipitaciones definidas en los capítulos anteriores.

Existen distintas metodologías ampliamente utilizadas en la hidrología nacional para la

obtención de caudales máximos en cuencas no controladas. Los rangos de aplicabilidad

de estos métodos dependen de las características de las cuencas en cuestión,

principalmente del área de estas. Se diferencia entre cuencas con áreas mayores a 25

km [2] y cuencas pequeñas menores a 25 km [2], según el límite establecido para la aplicación

de distintos métodos según el Manual de carreteras Volumen 3. Para las cuencas en

estudio, que poseen un área menor a 25 km [2], se utilizará el Método Racional según lo

descrito en el acápite de Curvas IDF.

Por lo tanto, en el presente capítulo se describe la obtención de caudales para las

cuencas utilizando el Método Racional. Este método supone que el escurrimiento máximo

proveniente de una tormenta es proporcional a la lluvia caída, supuesto que se cumple

info@flujoing.cl / www.flujoing.cl

15

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

en forma más rigurosa en cuencas mayoritariamente impermeables o en la medida que

la magnitud de la lluvia crece y el área aportante se satura.

El caudal máximo para un determinado periodo de retorno se calcula mediante la

siguiente expresión:

Q= [CxIxA]

3.6

En que:

 - Q: Caudal instantáneo máximo de período de retorno T, expresado en m [3] /s.

 C: Coeficiente de escorrentía asociado al período de retorno T.

 I: Intensidad media de lluvia asociada al período de retorno T y a una duración

igual al tiempo de concentración de la cuenca, expresada en mm/h.

 - A: Área aportante expresada en km [2] .

Considerando lo anterior, los valores de área para las cuencas analizadas corresponden

a lo definido en el Acápite 3.1.1, mientras que los valores de intensidad asociados al

tiempo de concentración se obtienen a partir de las curvas IDF determinadas en el

Acápite 3.2.2.

Por otro lado, la determinación del coeficiente de escorrentía se describe a continuación.

###### 3.3.1.1. Coeficiente de Escorrentía

El coeficiente de escorrentía depende de las características del terreno, uso y manejo del

suelo, condiciones de infiltración, entre otros aspectos. Para la selección del coeficiente

de escorrentía se aplicaron las recomendaciones de la sección 3.702.503 del Manual

de Carreteras, que propone una estimación en base a factores de relieve, infiltración,

cobertura vegetal y almacenamiento de agua en el suelo.

A continuación, en la Tabla 12, se presentan los parámetros adoptados para determinar

el coeficiente de escorrentía para las distintas cuencas para T=10 años.

info@flujoing.cl / www.flujoing.cl

16

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

|Factor Descripción Categoría Valor|Col2|Col3|Col4|
|---|---|---|---|
|Relieve|Suelos y pendientes entre 5% y 10%|Alto|0.20|
|Infiltración|Suelos profundos de arena u otros suelos bien drenados|Normal|0.06|
|Cobertura<br>Vegetal|90% del área con praderas, bosques o cobertura equivalente|Normal|0.06|
|Almacenamiento<br>Superficial|Capacidad alta, sistema hidrográfico poco definido|Normal|0.06|
|TOTAL|TOTAL|TOTAL|0.38|

**Tabla 12. Determinación coeficiente de escorrentía cuencas.**

**Fuente: Elaboración propia.**

Por otra parte, para los periodos de retorno mayores a 10 años, es necesario utilizar los

coeficientes de amplificación recomendados en la misma sección del manual,

correspondientes a 1.10, 1.20 y 1.25 para T-25, T-50 y T-100 años, respectivamente.

Considerando lo anterior, en la siguiente tabla se definen los coeficientes de escorrentía

asociados a los distintos periodos de retorno, correspondientes a la cuenca analizada.

|Período de retorno T(2) T(5) T(10) T(25) T(50) T(100)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Coeficientes de escorrentía|0.38|0.38|0.38|0.42|0.46|0.48|

**Tabla 13. Coeficientes de escorrentía para método racional.**

**Fuente: Elaboración propia.**

###### 3.3.1.2. Obtención de caudales con Método Racional

A partir de lo anterior, para la aplicación del método racional, se definen en primera

instancia en la _Tabla 14_, los valores de área, tiempo de concentración, e intensidades

asociadas a cada tiempo de concentración y período de retorno para las cuencas en

análisis.

|Área Tc Intensidad en Tc (mm/h)<br>Cuenca<br>(km2) (min) T(2) T(5) T(10) T(25) T(50) T(100)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Cuenca<br>Área <br>(km2) <br>Tc <br>(min)<br>Intensidad en Tc (mm/h)<br>T(2)<br>T(5)<br>T(10)<br>T(25)<br>T(50)<br>T(100)|Cuenca<br>Área <br>(km2) <br>Tc <br>(min)<br>Intensidad en Tc (mm/h)<br>T(2)<br>T(5)<br>T(10)<br>T(25)<br>T(50)<br>T(100)|Cuenca<br>Área <br>(km2) <br>Tc <br>(min)<br>Intensidad en Tc (mm/h)<br>T(2)<br>T(5)<br>T(10)<br>T(25)<br>T(50)<br>T(100)|T(2)|T(5)|T(10)|T(25)|T(50)|T(100)|
|SC 1|0.22|10.0|23.95|35.83|44.27|52.74|64.16|73.13|
|SC 2|0.11|10.0|23.95|35.83|44.27|52.74|64.16|73.13|
|SC 3|0.15|10.3|23.72|35.50|43.85|52.25|63.56|72.45|
|SC 4|0.13|10.0|23.95|35.83|44.27|52.74|64.16|73.13|
|SC 5|0.72|16.7|18.54|27.74|34.27|40.83|49.67|56.61|
|SC 6|0.23|10.0|23.95|35.83|44.27|52.74|64.16|73.13|

**Tabla 14. Intensidades según Tc para Método Racional.**

**Fuente: Elaboración propia.**

Con dichos valores de intensidades y áreas en conjunto con los coeficientes de

escorrentía determinados en el acápite anterior, es posible obtener los caudales para

las diferentes cuencas, según se presenta a continuación en la _Tabla 15_ .

info@flujoing.cl / www.flujoing.cl

17

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

|Caudales (m3/s)<br>Cuenca<br>T(2) T(5) T(10) T(25) T(50) T(100)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|SC 1|0.55|0.82|1.01|1.32|1.76|2.08|
|SC 2|0.29|0.43|0.53|0.69|0.92|1.09|
|SC 3|0.37|0.56|0.69|0.90|1.20|1.42|
|SC 4|0.33|0.50|0.61|0.80|1.06|1.26|
|SC 5|1.41|2.11|2.60|3.41|4.52|5.37|
|SC 6|0.57|0.85|1.06|1.38|1.84|2.18|

**Tabla 15. Caudales determinados por Método Racional.**

**Fuente: Elaboración propia.**

Como es posible observar, los caudales obtenidos para el sector del parque (SC 1 a SC

4) van desde los 1.09 m [3] /s hasta los 2.08 m [3] /s para los periodos de retorno de 100 años.

Y las cuencas en el sector del camino de acceso al Proyecto tiene caudales de 5.37 m [3] /s

(SC 5) y 2.18 m [3] /s (SC 6). Dichos valores de caudales máximos instantáneos para T-100

serán utilizados para los estudios hidráulicos asociados al Proyecto.

##### 4. ANÁLISIS HIDRÁULICO

En este capítulo se detallan los aspectos relacionados al análisis de modelación

hidráulica realizado para el Proyecto, definiendo en primer lugar lo respectivo a la

construcción del modelo y sus condiciones de modelación. Posteriormente se presentan

los resultados hidráulicos del modelo para el estudio de inundaciones sobre el escenario

con periodo de retorno T-100 años, determinando las áreas de inundación, sus

principales características hidráulicas (profundidad y velocidad) y su influencia sobre la

zona del proyecto y sus obras.

La metodología aplicada para el análisis hidráulico corresponde a modelación numérica

bidimensional mediante el software HEC-RAS, en su versión 6.5, ampliamente utilizado

para la simulación de flujos en ríos y estuarios. Dicho modelo es aplicable a condiciones

donde las hipótesis de distribución hidrostática de presiones y distribución uniforme de

la velocidad en la profundidad sean representativas de las condiciones dominantes,

como es el caso de los escurrimientos someros de los cauces de estudio.

Se desarrolló un modelo considerando los 6 cauces de interés, considerando las

secciones normales de estos cauces, sus singularidades y sus zonas aledañas

potencialmente inundables, incluyendo el área donde se instalan las obras del Proyecto.

info@flujoing.cl / www.flujoing.cl

18

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

La Figura 3 ilustra los tramos de los cauces analizados, así como el área considerada

para la elaboración del modelo.

**Figura 3. Área de modelación hidráulica PFV Corniglia.**

**Fuente: Elaboración propia.**

4.1. METODOLOGÍA DE LA MODELACIÓN

En este capítulo se detallan los aspectos metodológicos relacionados al estudio de

modelación hidráulica realizado, definiendo los fundamentos y limitaciones del modelo,

lo relativo a la construcción del modelo (geometría, malla de cálculo, rugosidad), las

condiciones de modelación (condiciones de contorno, condiciones internas, condiciones

meteorológicas) y también aspectos de la simulación y postproceso.

4.2. FUNDAMENTOS DE LA MODELACIÓN CON HEC-RAS 2D

El modelo utilizado está basado en el software HEC-RAS, en su versión 6.5, el cual es un

modelo numérico de simulación de flujos de agua en dos dimensiones (longitudinal y

info@flujoing.cl / www.flujoing.cl

19

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

transversal) en quebradas, ríos, y otros cuerpos de agua. Dicho software cuenta

actualmente con una gran variedad de módulos para distintas aplicaciones, pasando a

ser un modelo que permite simular múltiples procesos ambientales de base

hidrodinámica.

Utilizando las ecuaciones fundamentales de conservación de la masa y la cantidad de

movimiento, el software calcula el flujo del agua a través del dominio en función de las

condiciones bases definidas. HEC-RAS 2D utiliza un enfoque de elementos finitos para

resolver estas ecuaciones y simular el comportamiento del flujo en dos dimensiones.

Las principales ecuaciones que se resuelven son:

**a)** **Ecuación de continuidad o ecuación de conservación de la masa:**

Esta ecuación establece que la cantidad total de agua en un sistema cerrado no cambia

con el tiempo. En términos matemáticos, la ecuación de continuidad para flujo

incompresible se puede expresar como:

∂h∂t [+ ∂(hu)] ∂x

= 0
∂y

∂h

+ [∂(hv)]
∂x

Donde:

 - _h_ : altura del agua en un punto dado.

 - _t_ : tiempo.

 - _u_ y _v_ : componentes de la velocidad en las direcciones _x_ e _y_ respectivamente.

**b)** **Ecuación de cantidad de movimiento o Ecuación de Navier-Stokes:**

Esta ecuación describe la relación entre la aceleración del fluido y las fuerzas que actúan

sobre él. En su forma simplificada para flujo de aguas poco profundas, la ecuación de

cantidad de movimiento se expresa como:

∂u

∂u

∂t [+ u∂u] ∂x

∂x [+ v∂u]

∂y [= −g∂z] ∂x

[1]
∂x [−f] [c] [u|u| +]

ρ

∂
∂x [(τ] [bx] [−1] 2 [ρgz] [2] [) + S] [u]

∂v

∂v

∂t [+ u∂v] ∂x

∂x [+ v∂v]

∂y [= −g∂z] ∂y

[1]
∂y [−f] [c] [v|v| +] ρ

ρ

∂
∂y [(τ] [by] [−1] 2 [ρgz] [2] [) + S] [v]

info@flujoing.cl / www.flujoing.cl

20

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

Donde:

 - _g_ : aceleración de gravedad.

 - _z_ : elevación del lecho del río o quebrada.

 - _f_ _c_ : coeficiente de resistencia al flujo.

 - τ bx y τ by : componentes de la tensión de corte en las direcciones _x_ e _y_

respectivamente.

 - _S_ _u_ y _S_ _v_ : representan las fuerzas externas que actúan en las direcciones _x_ e _y_

respectivamente.

HEC-RAS 2D resuelve estas ecuaciones utilizando métodos numéricos como el método

de los elementos finitos para simular el comportamiento del flujo de agua en dos

dimensiones en un dominio específico.

Según lo especificado por sus autores, algunas aplicaciones del modelo, particularmente

del módulo hidrodinámico, corresponden a:

 Simulación del flujo en lámina libre en cauces naturales.

 Evaluación de zonas inundables. Cálculo de las zonas de flujo preferente.

 - Cálculo hidráulico de encauzamientos.

 - Cálculo hidráulico de redes de canales en lámina libre.

4.3. GEOMETRÍA

La construcción de la geometría del área de estudio es una de las etapas más

importantes del modelo, ya que permite caracterizar la morfología que determina el

movimiento del fluido. Para la elaboración de la geometría se utilizó la topografía del

área de estudio, de 80 hectáreas de extensión, obtenida por medio de fotogrametría de

precisión, la cual fue procesada y transformada en una superficie ráster que puede ser

incorporada al modelo mediante distintas herramientas de la interfaz. La _Figura 4_

muestra el modelo de elevación digital construido en base a este proceso.

Es importante destacar que al área de estudio se le ha realizado un filtrado de la

cubierta vegetal de relevancia, por lo tanto, el levantamiento topográfico por

fotogrametría refleja apropiadamente las condiciones morfológicas del terreno.

info@flujoing.cl / www.flujoing.cl

21

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 4. Geometría del modelo.**

**Fuente: Elaboración propia, plataforma SIG.**

4.4. MALLA DE CÁLCULO

Para que el modelo pueda llevar a cabo la resolución de las ecuaciones gobernantes

por el método de volúmenes finitos, es necesario realizar previamente una discretización

espacial del dominio a estudiar. Para ello se divide el dominio de estudio en celdas o

elementos de tamaño relativamente pequeño, a la que se le denomina malla de cálculo.

La generación de la malla de cálculo es una de las etapas que requiere mayor tiempo y

esfuerzo a la hora de desarrollar un estudio de simulación numérica del flujo, ya que se

requiere determinar un tipo de malla que se adapte y represente adecuadamente la

geometría del problema y con una selección y distribución de tamaños adecuados para

lograr independizar de esta variable los resultados obtenidos, al mismo tiempo que

permitir eficiencia para la modelación. Esta se hace con la herramienta interna del

software llamada RAS-Mapper que proporciona funcionalidades para la visualización,

análisis y manipulación de las condiciones iniciales previos a la simulación.

info@flujoing.cl / www.flujoing.cl

22

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

Se ha definido como óptimo de trabajo una malla de 58.341 elementos para el sector

de camino de acceso, y de 358.218 elementos para el sector del parque fotovoltaico,

con lados de 0.5 metros en las zonas que requieren mayor nivel de detalle. Aquello fue

definido consecuentemente a través de distintas iteraciones, concluyendo la necesidad

de utilizar una malla densa por las características ya indicadas de la zona de estudio.

**Figura 5. Mallas de cálculo sector Parque (izquierda) y camino acceso (derecha).**

**Fuente: Elaboración propia, HEC-RAS.**

4.5. RUGOSIDAD

Para la aplicación de la rugosidad, el modelo permite asignar distintos valores conforme

a la identificación de usos de suelo. En el caso de estudio se considera la aplicación de

distintos usos de suelo según las características de los cauces identificados y sus planicies

de inundación. Para esto, se han considerado las fotografías en terreno y áreas de alta

definición provistas por el cliente, el levantamiento topográfico y los registros de terreno

presentados previamente en este proceso de evaluación ambiental (para mayor detalle

ver Subanexo No6 “Determinación de Rugosidades”).

info@flujoing.cl / www.flujoing.cl

23

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 6. Imágenes de quebradas analizadas para determinación de rugosidad.**

**Fuente: Elaboración propia.**

Se requirió entonces definir la rugosidad para dicho uso de suelo, en términos del

coeficiente de Manning (n), para lo cual se utilizó el método de Cowan descrito en el

MC V3, el que se basa en la siguiente expresión:

n= m× (n 0 + n 1 + n 2 + n 3 + n 4 )

Donde:

 - n 0 = Rugosidad base.

 - n 1 = Rugosidad adicional por irregularidades perímetro mojado.

 - n 2 = Rugosidad adicional por variación de forma.

 - n 3 = Rugosidad adicional por obstrucciones.

 - n 4 = Rugosidad adicional por presencia de vegetación.

 m= Factor de corrección por efecto sinuosidad.

Conforme a lo anterior y a las características de los cauces del área de estudio,

considerando el material de lecho, las características geométricas obtenidas de la

topografía y los registros de terreno se agruparon y determinaron las rugosidades para

los siguientes grupos de cauces:

 Quebradas Tipo A: agrupa las quebradas y esteros con baja vegetación,

determinando un valor de rugosidad de n=0.038.

info@flujoing.cl / www.flujoing.cl

24

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

 Quebradas Tipo B: agrupa las quebradas con vegetación moderada,

determinando un valor de rugosidad de n=0.048.

 Quebradas Tipo C: agrupa las quebradas con vegetación alta, determinando un

valor de rugosidad de n=0.055.

La determinación de estos valores mediante el método de Cowan se detalla en las

siguientes tablas.

|Condición del Cauce Valor|Col2|Col3|Col4|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad P.M.|Despreciable|n1|0.000|
|Variaciones de secciones|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.008|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|n|n|n|0.038|

**Tabla 16. Coeficiente de rugosidad Cowan Quebradas Tipo A.**

**Fuente: Elaboración propia.**

|Condición del Cauce Valor|Col2|Col3|Col4|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad P.M.|Despreciable|n1|0.000|
|Variaciones de secciones|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.018|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|n|n|n|0.048|

**Tabla 17. Coeficiente de rugosidad Cowan Quebradas Tipo B.**

**Fuente: Elaboración propia.**

|Condición del Cauce Valor|Col2|Col3|Col4|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad P.M.|Despreciable|n1|0.000|
|Variaciones de secciones|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Alta|n4|0.025|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|n|n|n|0.055|

**Tabla 18. Coeficiente de rugosidad Cowan Quebradas Tipo C.**

**Fuente: Elaboración propia.**

Así, la clasificación de cada quebrada y de las confluencias entre ellas queda

determinada de la siguiente forma:

info@flujoing.cl / www.flujoing.cl

25

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

|Coeficiente de<br>Quebrada Tipo Vegetación<br>rugosidad|Col2|Col3|Col4|
|---|---|---|---|
|SC1|B|Media|0.048|
|SC2|B|Media|0.048|
|SC3|A|Baja|0.038|
|SC4|B|Media|0.048|
|Confluencia SC1-SC2|B|Media|0.048|
|Confluencia SC1-SC3|B|Media|0.048|
|Confluencia SC1-SC4|A|Baja|0.038|
|SC5|C|Alta|0.055|
|SC6|A|Baja|0.038|

**Tabla 19. Coeficiente de rugosidad determinado para las distintas quebradas.**

**Fuente: Elaboración propia.**

Por otro lado, para las planicies de inundación se definieron también distintos usos de

suelo, para lo cual se recurrió a la Tabla 5-6 del texto “Hidráulica de Canales Abiertos,

Ven Te Chow”, definiendo los siguientes valores de Manning según la cobertura del

suelo:

 Zonas Pastizales: se considera un valor de rugosidad de n=0.03, considerando

el valor recomendado para Pastizales, sin matorrales y pasto corto (D-2 a.1)

 Zonas Matorrales: se considera un valor de rugosidad de n=0.05, considerando

el valor recomendado para Matorrales dispersos con mucha maleza (D-2 c.1)

 Zonas Árboles: se considera un valor de rugosidad de n=0.06, considerando el

valor recomendado para Árboles con retoños (D-2 d.3)

4.6. CONDICIONES DE CONTORNO

La función de Condiciones de Contorno en RAS Mapper, dentro del software HEC-RAS,

permite definir y ajustar las condiciones de frontera para una simulación hidráulica. Estas

condiciones de frontera son esenciales para establecer cómo se comportará el flujo de

agua en los límites del dominio modelado. Se pueden especificar las condiciones de

flujo en los puntos donde el agua entra y sale del dominio modelado.

info@flujoing.cl / www.flujoing.cl

26

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 7. Condiciones de contorno aplicadas al modelo sector Parque.**

**Fuente: Elaboración propia.**

**Figura 8. Condiciones de contorno aplicadas al modelo sector Camino de Acceso.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

27

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

En este caso de estudio se incluyen los caudales prescritos obtenidos en el Capítulo 3.3

del presente informe para un periodo de retorno T=100 años implementados como

hidrogramas de caudal variable considerando un inicio con suelo seco, que se resumen

a continuación:

|Cuenca SC 1 SC 2 SC 3 SC 4 SC 5 SC 6<br>Intervalo Q (m3/s) Q (m3/s) Q (m3/s) Q (m3/s) Q (m3/s) Q (m3/s)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Intervalo|Intervalo|Intervalo|Intervalo|Intervalo|Intervalo|Intervalo|
|0:00:00|0.00|0.00|0.00|0.00|0.00|0.00|
|0:10:00|0.69|0.36|0.47|0.42|1.79|0.73|
|0:20:00|1.39|0.73|0.95|0.84|3.58|1.45|
|0:30:00|2.08|1.09|1.42|1.26|5.37|2.18|
|0:40:00|2.08|1.09|1.42|1.26|5.37|2.18|
|0:50:00|1.39|0.73|0.95|0.84|3.58|1.45|
|1:00:00|0.69|0.36|0.47|0.42|1.79|0.73|

**Tabla 20. Hidrograma de caudales máximos instantáneos para T-100 años.**

**Fuente: Elaboración propia.**

4.1. CONDICIONES INICIALES Y SINGULARIDADES

Las condiciones iniciales del modelo, es decir los valores de partida de las variables de

cota o calado en las celdas del dominio, se asignaron como condición seca, aplicando

valores nulos de calado en todas las celdas; siendo relevante utilizar un calentamiento

apropiado del modelo en las respectivas simulaciones para permitir que los resultados

se independicen de esta condición inicial.

Para la modelación es necesario considerar también las singularidades existentes en los

tramos de cauce en estudio. A partir del recorrido del terreno se identificó un atravieso

bajo el camino de acceso sobre la Quebrada SC5, el cual fue caracterizado a detalle,

a partir de lo cual se incorporó al modelo utilizando las herramientas de definición de

estructuras que posee el módulo hidrodinámico de HEC-RAS.

4.2. SIMULACIÓN Y POSTPROCESO

Para la aplicación del modelo se realizaron simulaciones de escenarios de caudales

estacionarios de 1 hora de duración, considerando un periodo de calentamiento del

modelo de 10 minutos ante las mismas condiciones.

info@flujoing.cl / www.flujoing.cl

28

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

Para las simulaciones se consideró un coeficiente de Courant máximo de 1.0, y mínimo

de 0.45, para condicionar la variación pasos de tiempo para la resolución de las

ecuaciones, buscando evitar inestabilidades en la solución del modelo y obtener

precisión de los resultados. Se definió un límite seco-mojado de 1 centímetros para el

dominio, que por las características del área de estudio corresponde a una profundidad

bajo la cual se pierde relevancia para los análisis.

Para analizar el comportamiento hidráulico del área de estudio en los distintos

escenarios simulados, se estudiaron los resultados en la interfaz de post-proceso de HEC

RAS 2D y exportándolos en formato ráster a una plataforma GIS, enfocándose en las

principales variables hidráulicas de interés.

4.3. RESULTADOS Y ANALISIS DE INUNDACIONES

A partir de los resultados del modelo, se presentan en el Subanexo 4 “Secciones

transversales resultados hidráulicos” se presentan las secciones elaboradas con el

software HEC-RAS para representar los niveles de inundación obtenidos para el

escenario T-100 años modelado.

Las siguientes figuras ilustran los perfiles hidráulicos para los distintos cauces y tramos

analizados, considerando el periodo de retorno T-100 años modelado, donde el eje X

del gráfico representa la distancia en metros y el eje Y la cota de elevación también en

metros.

info@flujoing.cl / www.flujoing.cl

29

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 9. Perfil longitudinal hidráulico SC1, sector Parque.**

**Fuente: Elaboración propia.**

**Figura 10. Perfil longitudinal hidráulico SC2, sector Parque.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

30

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 11. Perfil longitudinal hidráulico SC3, sector Parque.**

**Fuente: Elaboración propia.**

**Figura 12. Perfil longitudinal hidráulico SC4, sector Parque.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

31

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 13. Perfil longitudinal hidráulico SC5, sector Camino de Acceso.**

**Fuente: Elaboración propia.**

**Figura 14. Perfil longitudinal hidráulico SC6, sector Camino de Acceso.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

32

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

Se analizó la inundación del escenario T-100 años para los cauces naturales de estudio

y su posible relación con las componentes del proyecto.

Las próximas figuras ilustran las condiciones de profundidad y velocidad,

respectivamente, de los flujos resultantes para dicho escenario.

En primer lugar, como es posible observar, en los límites del área de proyecto las

distintas quebradas presentan un flujo acotado a sus secciones geométricas, sin producir

inundación de riberas o zonas aledañas que afecte las componentes del proyecto.

El quebrada SC1 no presenta desbordes dentro de todo el tramo modelado, verificando

que es capaz de portear de forma efectiva los caudales a los asociados al periodo de

retorno T-100 años sin producir inundación de los predios aledaños incluso al recibir el

caudal aportante de las otras quebradas secundarias.

Las mayores profundidades se observan en las zonas de flujo principal de la quebrada

SC1, en su tramo final desde las confluencias con las otras quebradas, a más de 100

metros del proyecto, donde se alcanzan valores superiores a los 4.6 metros. En la

Quebrada SC5 se tienen profundidades en un rango de 1 a 1.2 metros, cerca de la

confluencia con la Quebrada SC6, y profundidades de escurrimientos máximas aguas

abajo del atravieso de 1.6 metros.

info@flujoing.cl / www.flujoing.cl

33

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 15. Profundidades de flujo inundación T-100, sector Parque.**

**Fuente: Elaboración propia.**

**Figura 16. Profundidades de flujo inundación T-100, sector Camino de Acceso.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

34

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

Respecto a las velocidades de los cauces en el sector del Parque se observan valores

que en general oscilan en un rango de 2 m/s en las zonas principales de los

escurrimientos, con máximos localizados que superan los 4.4 m/s en los estrechamientos

producidos en la zona del tramo final de la Quebrada SC1.

**Figura 17. Velocidades de flujo inundación T-100, sector Parque.**

**Fuente: Elaboración propia.**

Del mismo modo, se puede observar que las velocidades de los cauces en el sector del

Camino de Acceso oscilan en un rango de 1.2 a 1.8 m/s en las zonas principales de los

escurrimientos, con máximos localizados que superan los 2.5 m/s aguas arriba del

atravieso.

info@flujoing.cl / www.flujoing.cl

35

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 18. Velocidades de flujo inundación T-100, sector Camino de Acceso.**

**Fuente: Elaboración propia.**

A partir de lo anterior, es posible definir que los cauces identificados en el sector del

Parque no revisten un riesgo para el Proyecto para el escenario extraordinario T-100 años

analizado, ya que las obras y componentes proyectadas se encuentran fuera de los

límites de inundación de la crecida centenaria.

De igual forma, se determina que las obras y componentes del Proyecto se emplazan

fuera de los límites de estos cauces naturales, y que no se requieren ni proyectan obras

que los intervengan, desafectando entonces la aplicabilidad de permisos ambientales

sectoriales respectivos a estos cauces naturales en el sector del Parque Fotovoltaico.

Por otra parte, para el sector Camino de Acceso será necesario de acuerdo con los

resultados obtenidos la realización de obras lineales de modificación de cauces tanto

para la quebrada SC5 como para la SC6.

info@flujoing.cl / www.flujoing.cl

36

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

##### 5. OBRAS PROPUESTAS

En el presente capitulo se desarrolla lo respectivo al diseño y análisis de obras

hidráulicas propuestas sobre los cauces analizados.

Con el fin de minimizar el alteramiento de los régimenes de escurrimiento de las aguas,

se proyectaron obras de modificación de cauces en el sector de Camino de Acceso del

Proyecto, correspondientes a una obra tipo badén y otro atravieso tipo alcantarilla bajo

el camino de acceso en los límites de inundación de las quebradas SC5 y SC6.

5.1. BADÉN

Para el correcto funcionar del camino de acceso, se contempla la protección del lecho

de la quebrada SC6 en la superficie del terreno para no interferir en el libre

escurrimiento de las aguas. Por lo tanto, se proyecta un atravieso de camino proyectado

sobre la quebrada natural intermitente SC6, la cual fue ubicada e identificada

previamente en el presente documento.

Se asegurará que se tenga una protección superficial del suelo donde se funda el badén.

La función de esta obra es evitar erosiones en el suelo de fundación del badén mientras

que permita el libre escurrimiento del agua.

**Figura 19. Ubicación futura del badén proyectado en la Quebrada SC6.**

**Fuente: Elaboración propia.**

info@flujoing.cl / www.flujoing.cl

37

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

Para este atravieso se proyecta un badén simple para escurrimientos no permanentes,

según lo especificado en el Manual de Carreteras Volumen 4, específicamente en la

lámina 4.704.101 que detalla el diseño de badenes sin escurrimiento permanente.

Este badén está compuesto en la zona de calzada de una losa de hormigón armado H

30 con acero estructural A63-42H. Esta se emplaza sobre un emplantillado de hormigón

H-5 y un relleno estructural. Se contemplan capas de rocas de protección a nivel de

terreno, aguas arriba y aguas abajo de la calzada. Se consideran juntas de dilatación

cada 20 metros si la longitud lo requiere y no se consideran rejas de protección debido

a las características de los cauces.

Esta obra seguirá las especificaciones técnicas propuestas en el Manual de Carreteras

Volumen 5 para cada una de sus componentes, según establece la lámina de diseño

tipo. La Figura 20, Figura 21 y Figura 22 ilustran la obra propuesta, según la lámina de

diseño tipo del Subanexo No5 “Planos Tipo Cajón de Hormigón doble y Badén MC V4”.

**Figura 20. Planta Badén sin escurrimiento permanente.**

**Fuente: Lámina 4.704.101 MC-V4.**

**Figura 21. Corte A-A Baden sin escurrimiento permanente.**

**Fuente: Lámina 4.704.101 MC-V4.**

info@flujoing.cl / www.flujoing.cl

38

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 22. Corte B-B Baden sin escurrimiento permanente.**

**Fuente: Lámina 4.704.101 MC-V4.**

El ancho de calzada del camino será de 5 metros, en relación con lo definido

anteriormente, y la longitud del badén se obtiene en función de la lámina de inundación

para el período de retorno T=100 años del cauce, fijándose en el sector del atravieso en

25,1 metros.

5.2. ATRAVIESO ALCANTARILLA BAJO CAMINO DE ACCESO

Esta obra corresponde a la construcción de un atravieso para el acceso a la planta solar

sobre la quebrada SC5, con el fin de permitir el correcto ingreso de maquinaria y

vehículos a la zona del proyecto.

**Figura 23. Cajón doble de hormigón armado.**

**Fuente: Manual de Carreteras, Volumen 4.**

info@flujoing.cl / www.flujoing.cl

39

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

La obra se materializará mediante la instalación de un cajón doble de hormigón armado

de 1,0 x 1,0 según Manual de Carreteras V4 Plano de Obras Tipo 4.103.801 (ver

Subanexo No5), el cual da cumplimiento a la capacidad requerida para el caudal

aportante de ambas quebradas, considerando la pendiente de terreno en el sector y un

coeficiente de rugosidad característico para el hormigón, como se muestra en la

siguiente figura:

**Figura 24. Capacidad de la obra a instalar.**

**Fuente: Elaboración propia, HCanales.**

Se ha utilizado el software HCanales que permite determinar las características

hidráulicas y geométricas del atravieso basado en la fórmula de Manning, para

determinar la capacidad de porteo de la solución propuesta. Como se puede apreciar

en la Figura 24 anterior, la capacidad de porteo de la obra es mayor que la capacidad

aportante de ambas quebradas para un período de retorno T=100 años, contemplando

una capacidad de porteo de 12,55 m [3] /s vs los 7,55 m [3] /s de ambas quebradas.

El ancho del atravieso corresponde a 5,0 m, correspondiente al ancho del atravieso vial

proyectado más un metro a cada lado de este con el fin de dar estabilidad al relleno,

en el sentido del escurrimiento del cauce. La siguiente figura muestra el perfil de

instalación de la obra sobre el la quebrada SC-5.

info@flujoing.cl / www.flujoing.cl

40

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

**Figura 25. Disposición de cajón doble de hormigón armado sobre el canal.**

**Fuente: Elaboración propia.**

##### 6. APLICABILIDAD PAS 156

El Proyecto PFV Corniglia contempla dos obras a las que les aplica Permiso Ambiental

Sectorial 156:

 - Badén

 Atravieso tipo Alcantarilla bajo camino de acceso

Ya que dichas obras proyectadas alterarán el régimen de escurrimiento de las aguas

cuando ocurra un evento de crecidas extraordinario para un período de retorno T-100

años.

##### 7. CONCLUSIÓN

En el presente informe se describieron los antecedentes, metodologías y resultados del

estudio de crecidas realizado para el Proyecto PFV Corniglia, detallando los análisis

hidrológicos e hidráulicos que se desarrollaron para los seis cauces naturales que se

ubican en las cercanías del proyecto.

Se determinaron las cuencas aportantes de estos esteros, donde se destaca la cuenca

de mayor tamaño correspondiente a la Quebrada SC5, para la cual se delimitó un área

info@flujoing.cl / www.flujoing.cl

41

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

aportante de 0.72 km [2] . Las demás cuencas comprenden superficies del orden de 0.11 a

0.23 km [2] . Para cada cuenca sus parámetros morfométricos y se definieron sus tiempos

de concentración asociados.

A modo conservador, se utilizan las precipitaciones máximas diarias para los distintos

períodos de retorno determinadas en el el PM-43 “Plan Maestro de Evacuación y Drenaje

de Aguas Lluvias de Concón” (Dirección de Obras Hidráulicas, 2020) para la estación

Los Aromos, documentación técnica oficial aprobada por la autoridad competente, en

la cual la precipitación máxima diaria para un T=100 años es de 203.70 mm.

Para la determinación de caudales se utilizaron los métodos aplicables para cuencas sin

control fluviométrico. Específicamente al ser todas las cuencas de un área menor a 25

km [2], se utilizó el método racional (Manual de Carreteras, V3). Los caudales obtenidos

para el sector del Parque (SC1 a SC4) van desde los 1.09 m [3] /s hasta los 2.08 m [3] /s para

los periodos de retorno de 100 años. Y las cuencas en el sector del camino de acceso al

Proyecto tiene caudales de 5.37 m [3] /s (SC5) y 2.18 m [3] /s (SC6).

Se desarrollaron modelaciones hidráulicas bidimensionales en el modelo HEC-RAS,

obteniendo las principales variables hidráulicas de interés para los flujos modelados,

correspondientes a las condiciones de lámina de inundación, profundidad y velocidad

para el periodo de retorno T-100 años.

Luego se analizó la inundación del escenario T-100 años para las quebradas estudiadas

y su posible relación con las componentes del Proyecto, determinado que en los límites

del área de Proyecto las distintas quebradas presentan un flujo acotado a sus secciones

geométricas, sin producir inundación de riberas o zonas aledañas que afecte las

componentes del proyecto, con excepción del atravieso bajo el camino existente.

Con el fin de minimizar el alteramiento de los régimenes de escurrimiento de las aguas,

se proyectaron obras de modificación de cauces en el sector de Camino de Acceso del

Proyecto, correspondientes a una obra tipo badén y otro atravieso tipo alcantarilla bajo

el camino de acceso en los límites de inundación de las quebradas SC5 y SC6, obras a

las cuales corresponde aplicar el Permiso Ambiental Sectorial 156.

info@flujoing.cl / www.flujoing.cl

42

| ESTUDIO DE CRECIDAS PROYECTO PFV CORNIGLIA

##### 8. BIBLIOGRAFÍA

DGA-MOP. (2016). _Guías Metodológicas para Presentación y Revisión Técnica de_

_Proyectos de Modificación de Cauces Naturales y Artificiales._ Santiago, Chile:

Departamento de administración de recursos hídricos.

Dirección de Obras Hidráulicas. (2020). _PM-43 "Plan Maestro de Evacuación y Drenaje_

_de Aguas Lluvias de Concón, Región de Valparaiso"._ Santiago: Arrau Ingeniería.

Dirección de Vialidad - MOP. (2021). _Manual de Carreteras._ Chile: MOP-DGOP.

Dirección General de Aguas. (1991). _Precipitaciones máximas en 1, 2 y 3 días._ Chile:

CIRH-DGA.

Dirección General de Aguas. (1995). _Manual de cálculo de crecidas y caudales mínimos_

_en cuencas sin información fluviométrica._ Chile: CIRH-DGA.

Instituto Geográfico Militar. (1922). _Instituto Geográfico Militar de Chile_ . Obtenido de

https://www.igm.cl/

Ministerio de Bienes Nacionales. (2023). _IDE Chile_ . Obtenido de Infraestructura de

Datos Geoespaciales: https://www.ide.cl/

MOP. (1981). _Código de Aguas - DFL No1.122._ Santiago, Chile.

SEA. (2017). _Guía para la descripción del área de influencia._

SEA. (2021). _Criterio de evaluación en la SEIA: Contenidos técnicos para la evaluación_

_ambiental del Recurso Hídrico._

SERNAGEOMIN. (2003). _Mapa Geológico de Chile._

Te Chow, V., R. Maidment, D., & W. Mays, L. (1994). _Hidrología Aplicada._ Illinois:

McGraw-Hill.

United States Department of Agriculture. (1986). _Urban Hydrology for Small Watersheds_

_TR-55._ Washington DC: Conservation Engineering Division.

info@flujoing.cl / www.flujoing.cl

43

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 9.: Coeficientes de duración estación Quillota.****

| Duración<br>(min) | Intensidad (mm/h) para distintos T | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Duración<br>(min) | 2 | 5 | 10 | 25 | 50 | 100 |
| 60 | 8.67 | 12.97 | 16.03 | 19.10 | 23.23 | 26.48 |
| 120 | 7.67 | 11.48 | 14.18 | 16.89 | 20.55 | 23.43 |
| 240 | 6.34 | 9.48 | 11.71 | 13.96 | 16.98 | 19.35 |
| 360 | 5.56 | 8.32 | 10.28 | 12.24 | 14.89 | 16.98 |
| 480 | 4.84 | 7.24 | 8.94 | 10.65 | 12.96 | 14.77 |
| 600 | 4.47 | 6.69 | 8.26 | 9.84 | 11.97 | 13.65 |
| 720 | 4.17 | 6.24 | 7.71 | 9.18 | 11.17 | 12.73 |
| 840 | 3.81 | 5.70 | 7.05 | 8.39 | 10.21 | 11.64 |
| 1080 | 3.26 | 4.88 | 6.03 | 7.18 | 8.74 | 9.96 |
| 1440 | 2.78 | 4.16 | 5.14 | 6.12 | 7.45 | 8.49 |

**Tabla 16.: Coeficiente de rugosidad Cowan Quebradas Tipo A.****

| Condición del Cauce Valor | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad P.M. | Despreciable | n1 | 0.000 |
| Variaciones de secciones | Graduales | n2 | 0.000 |
| Efecto relativo de las obstrucciones | Leve | n3 | 0.010 |
| Densidad de vegetación | Media | n4 | 0.018 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |
| n | n | n | 0.048 |

**Tabla 17.: Coeficiente de rugosidad Cowan Quebradas Tipo B.****

| Condición del Cauce Valor | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad P.M. | Despreciable | n1 | 0.000 |
| Variaciones de secciones | Graduales | n2 | 0.000 |
| Efecto relativo de las obstrucciones | Leve | n3 | 0.010 |
| Densidad de vegetación | Alta | n4 | 0.025 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |
| n | n | n | 0.055 |
