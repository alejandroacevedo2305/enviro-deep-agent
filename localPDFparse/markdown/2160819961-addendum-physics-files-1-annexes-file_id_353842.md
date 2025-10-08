---
title: Sin título
author: Javi
date: D:20240301194318+01'00'
language: es
type: report
pages: 75
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE INUNDACIONES PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 13
-->

Informe Técnico

Marzo 2024

# ESTUDIO DE INUNDACIONES PROYECTO LÍNEA DE TRANSMISIÓN Y CENTRAL BESS HALCÓN 13

www.flujoing.cl /+562 29798241/ info@flujoing.cl

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

## CONTENIDO

1. INTRODUCCIÓN ............................................................................................................................... 6

2. OBJETIVOS.......................................................................................................................................... 7

3. ANALISIS HIDROLOGICO ............................................................................................................ 8

3.1. CUENCAS APORTANTES ............................................................................... 8

3.1.1. PARÁMETROS MORFOMÉTRICOS ............................................................ 10

3.1.2. TIEMPO DE CONCENTRACIÓN ........................................................... 13

3.2. ANALISIS DE PRECIPITACIONES .................................................................. 14

3.2.1. PRECIPITACIONES MÁXIMAS ............................................................... 15

3.2.2. GENERACIÓN CURVAS IDF ................................................................. 20

3.3. ANALISIS DE CAUDALES ............................................................................. 22

3.3.1. Analisis de frecuencia río Turbio ........................................................... 23

3.3.2. MÉTODO RACIONAL ........................................................................... 27

3.3.3. Caudales detriticos quebradas ............................................................. 30

4. ANALISIS HIDRAULICO .............................................................................................................. 31

4.1. Fundamentos de la modelación con Iber ...................................................... 33

4.2. DATOS Y CONDICIONES DEL MODELO Iber ............................................. 35

4.2.1. Geometría ............................................................................................ 35

4.2.2. Malla de cálculo ................................................................................... 36

4.2.3. Rugosidad............................................................................................. 38

4.2.4. Condiciones de contorno e internas ...................................................... 40

4.2.5. Condiciones iniciales............................................................................. 43

4.2.6. Singularidades ...................................................................................... 43

4.2.7. Simulación y postproceso ...................................................................... 44

4.3. Analisis de inundaciones río Turbio .............................................................. 45

4.4. Analisis de inundaciones Quebradas ........................................................... 47

www.flujoing.cl / info@flujoing.cl

1

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

4.4.1. Situación Sin Proyecto ........................................................................... 48

4.4.2. Situación con Proyecto .......................................................................... 50

5. MECÁNICA FLUVIAL ................................................................................................................... 53

5.1. Fundamentos de la modelación ................................................................... 53

5.2. Consideraciones Metodologicas .................................................................. 54

5.3. Resultados de mecanica fluvial ..................................................................... 57

6. DISEÑO Y ANÁLISIS DE OBRAS PROPUESTAS ............................................................ 62

6.1. Muros de Encauzamiento ............................................................................. 63

6.1.1. Localización en planta ............................................................................. 63

6.1.2. Sección transversal ............................................................................... 64

6.1.3. Coronamiento ....................................................................................... 64

6.1.4. Coraza de protección ........................................................................... 65

6.1.5. Analisis de socavación y fundaciones.................................................... 65

6.2. Entubamiento de las quebradas ................................................................... 66

6.2.1. Captaciones Entubamiento ................................................................... 67

6.2.2. Entubamiento ........................................................................................ 67

6.2.3. Entregas Entubamiento ......................................................................... 69

6.3. Obra de defensa postación ......................................................................... 70

7. CONCLUSIÓN .................................................................................................................................. 71

8. BIBLIOGRAFÍA ............................................................................................................................... 74

## ÍNDICE DE GRÁFICOS

Gráfico 1. Serie de datos de precipitaciones máximas en 24 hrs. ................................. 17

Gráfico 2. Curvas IDF duración mayor a 1 hora. .......................................................... 21

Gráfico 3. Curvas IDF duración menor a 1 hora. ......................................................... 22

Gráfico 4. Serie de caudales máximos anuales estación Río Turbio en Varillar. .......... 24

www.flujoing.cl / info@flujoing.cl

2

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

## ÍNDICE DE FIGURAS

Figura 1. Delimitación de cuencas hidrográfica río Turbio. ............................................. 9

Figura 2. Delimitación de cuencas hidrográficas quebradas de estudio. ...................... 10

Figura 3. Mapa de elevaciones área de estudio. ......................................................... 12

Figura 4. Mapa de pendientes (%) área de estudio. .................................................... 12

Figura 5. Ubicación estaciones meteorológicas. ........................................................... 16

Figura 6. Ajustes de distribuciones estadística PP máx 24 h. ......................................... 18

Figura 7. Valores estadísticos distribución seleccionada análisis PP máx 24h. .............. 19

Figura 8. Ubicación estación fluviométrica analizada. ................................................ 24

Figura 9. Ajustes de distribuciones estadística caudales máximos. ............................... 26

Figura 10. Valores estadísticos distribución seleccionada análisis QMI. ....................... 27

Figura 11. Área de modelación hidráulica río Turbio. ................................................... 32

Figura 12. Área de modelación hidráulica quebradas analizadas. ............................. 33

Figura 13. DEM utilizado para la geometría del modelo. ............................................ 36

Figura 14. Malla de cálculo de modelo. ...................................................................... 37

Figura 15. Distribución acumulada de tamaños de los elementos de la malla zona río

Turbio. ......................................................................................................................... 38

Figura 16. Distribución acumulada de tamaños de los elementos de la malla zona

quebradas. ................................................................................................................. 38

Figura 17. Registro de terreno río Turbio. ..................................................................... 40

Figura 18. Condiciones de contorno aplicadas al modelo río Turbio. .......................... 42

Figura 19. Condiciones de contorno aplicadas al modelo de la zona de Quebradas. 43

Figura 20. Registro de terreno puente sobre río Turbio. ............................................... 44

Figura 21. Dimensiones y características puente sobre río Turbio. ................................ 44

Figura 22. Profundidades de flujo inundación T-100 zona Río Turbio. .......................... 46

Figura 23. Velocidades de flujo inundación T-100 zona Río Turbio. ............................. 47

Figura 24. Profundidades de flujo inundación T-100 Quebradas situación SP. ............. 49

Figura 25. Velocidades de flujo inundación T-100 Quebradas situación SP. ................ 49

Figura 26. Obras de regularización y defensa proyectadas. ....................................... 50

Figura 27. Profundidades de flujo inundación T-100 Quebradas situación CP. ............ 52

Figura 28. Velocidades de flujo inundación T-100 Quebradas situación CP. ................ 52

www.flujoing.cl / info@flujoing.cl

3

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Figura 29. Registro de terreno Calicata N°5 Estudio de Suelos. .................................. 55

Figura 30. Erosión y depositación T-100 años quebradas situación SP. ....................... 58

Figura 31. Carga de sedimentos suspendidos T-100 años situación SP. ........................ 58

Figura 32. Erosión y depositación T-100 años quebradas situación CP. ....................... 59

Figura 33. Carga de sedimentos suspendidos T-100 años situación CP. ....................... 60

Figura 34. Socavación T-100 años quebradas situación SP. .......................................... 61

Figura 35. Socavación T-100 años quebradas situación CP. ......................................... 61

Figura 36. Planimetría obras de regularización y defensa........................................... 62

Figura 37. Diseño transversal defensa fluvial de muro de gaviones. ............................ 64

Figura 38. Socavación en la zona de obras del proyecto. .......................................... 66

Figura 39. Diseño obra de captación entubamientos. ................................................. 67

Figura 40. Condiciones de diseño Entubamiento N°1. ................................................. 68

Figura 41. Condiciones de diseño Entubamiento N°2. ................................................. 68

Figura 42. Diseño obra de entrega entubamientos. ..................................................... 70

Figura 43. Diseño obra de defensa postación. ............................................................. 71

## ÍNDICE DE TABLAS

Tabla 1. Parámetros Morfométricos. .............................................................................. 11

Tabla 2. Expresiones para determinar el Tiempo de Concentración. ............................ 13

Tabla 3. Tiempos de concentración estimados por cuenca. .......................................... 14

Tabla 4. Tiempos de concentración definidos por cuenca. ........................................... 14

Tabla 5. Datos estaciones meteorológicas cercanas. .................................................... 15

Tabla 6. Precipitaciones máximas diarias según distintas distribuciones. ...................... 18

Tabla 7. Precipitaciones máximas diarias definidas...................................................... 19

Tabla 8. Coeficientes de duración estación Rivadavia. ................................................ 20

Tabla 9. Curvas IDF duración mayor a 1 hora. ............................................................ 20

Tabla 10. Intensidad (mm/h) duración menor a 1 hora. ................................................ 21

Tabla 11. Datos estación fluviométrica analizada. ........................................................ 23

Tabla 12. Caudales máximos según distintas distribuciones. ........................................ 25

Tabla 13. Caudales máximos instantáneos Río Turbio (m [3] /s). ...................................... 27

www.flujoing.cl / info@flujoing.cl

4

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Tabla 14. Determinación coeficiente de escorrentía para método racional. ................. 29

Tabla 15. Coeficientes de escorrentía para método racional. ...................................... 29

Tabla 16. Intensidades en Tc para Método Racional. .................................................. 29

Tabla 17. Caudales determinados por Método Racional. ............................................ 30

Tabla 18. Caudales líquidos y detríticos quebradas analizadas T-100 años. ................. 31

Tabla 19. Rugosidad método de Cowan río Turbio. ..................................................... 39

Tabla 20. Rugosidad método de Cowan zona de quebradas. .................................... 40

Tabla 21. Caudales de condiciones de contorno de entrada. ....................................... 41

Tabla 22. Condiciones método de transporte en suspensión Iber. ............................... 56

Tabla 23. Condiciones método de transporte de fondo Iber. ...................................... 56

www.flujoing.cl / info@flujoing.cl

5

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

## 1. INTRODUCCIÓN

En el presente informe se detallan los análisis hidrológicos e hidráulicos realizados para

desarrollar un estudio de inundaciones en el marco del proyecto “Línea de Transmisión

y Central BESS Halcón 13” considerando sus respectivos aspectos metodológicos, análisis

de resultados y principales conclusiones.

El proyecto se encuentra emplazado en la comuna de Vicuña, provincia de Elqui, región

de Coquimbo y consiste en un proyecto de sistemas de almacenamiento de energía por

medio de contenedores de baterías de litio.

El área considerada para el este estudio, y en específico los cauces naturales analizados,

se determinaron a partir de la caracterización hidrológica del proyecto, donde se definió

su área de influencia y se identificó la presencia del río Turbio aproximadamente a 50

metros al sur del área de proyecto y tres quebradas naturales menores de características

efímeras cuyos trazados terminan en la Ruta D-369 al poniente del área de proyecto.

Tanto para el río Turbio como para las quebradas menores se consideró relevante

efectuar el análisis de inundaciones aquí desarrollado.

Se desarrolla en este informe un análisis hidrológico de crecidas, con el fin de obtener

los caudales máximos ordinarios y extraordinarios para los cauces identificados. Para el

caso del río Turbio se identificó la estación fluviométrica “Río Turbio en Varillar”, de

administración de la Dirección General de Aguas (DGA) en las cercanías del área del

proyecto. Dicha estación cuenta con un registro de 53 años, por lo tanto, los caudales

máximos de dicho cauce serán obtenidos mediante análisis de frecuencia sobre la serie

de datos. Por otro lado, para el caso de las quebradas naturales menores se utilizará el

método racional que relaciona la precipitación con la escorrentía para cuencas

pequeñas, para lo cual analizará de forma detallada las características y parámetros

representativos de las cuencas aportantes, las precipitaciones y curvas IDF características

de la zona de estudio y otros parámetros de interés para la obtención de caudales.

Posteriormente se realizan los análisis hidráulicos utilizando una metodología de

modelación numérica bidimensional mediante el software Iber, ampliamente utilizado

para la simulación de flujos en ríos y estuarios. En primer lugar, se desarrolla un modelo

www.flujoing.cl / info@flujoing.cl

6

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

para el río Turbio, considerando su cauce, sus singularidades y sus zonas aledañas

potencialmente inundables. Por otro lado, se realiza también un modelo para analizar

el comportamiento hidráulico de las quebradas cercanas al área de proyecto. Se

considera el análisis de influencia de estas condiciones hidráulicas sobre las obras del

proyecto.

Se desarrolla en este informe lo respectivo a la construcción del modelo y sus condiciones

de modelación, así como también el análisis de inundaciones para el escenario de

periodo de retorno de 100 años, considerando las principales variables hidráulicas

obtenidas y su posible influencia sobre las obras del proyecto. Se considera también el

diseño hidráulico de obras que sean requeridas para la protección de sus componentes,

así como los estudios complementarios para estas obras según la normativa ambiental

vigente.

## 2. OBJETIVOS

 Desarrollar los análisis hidrológicos que permitan obtener los caudales máximos

instantáneos de crecida para los cauces naturales identificados.

 Desarrollar los análisis mediante modelación hidráulica que permitan

caracterizar el comportamiento de los flujos de crecida de los cauces

identificados.

 Definir los límites y parámetros hidráulicos de inundación de los cauces

identificados y analizar su posible relación con las obras y componentes del

proyecto.

 Diseñar obras hidráulicas requeridas por el proyecto.

 Desarrollar estudios complementarios según normativa ambiental vigente.

www.flujoing.cl / info@flujoing.cl

7

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

## 3. ANALISIS HIDROLOGICO

En el presente capítulo se entregan los antecedentes del estudio hidrológico de crecidas

para las cuencas aportantes al área de estudio hidráulico del proyecto. Es importante

destacar que se analizaron todas las quebradas y cauces naturales que pueden

relacionarse con el proyecto y que serán evaluadas en este estudio de inundaciones.

Para la caracterización morfométrica de las cuencas naturales identificadas se utilizó el

levantamiento topográfico del área de estudio, los registros de terreno y los datos de

elevación del DEM Alos Palsar con una resolución de 12.5 metros (obtenido de la IDE).

Es importante mencionar que de acuerdo con el estudio de Peña-Vidal en la latitud del

proyecto (latitud 30o) la línea de nieves de está sobre los 2350 m.s.n.m. (Manual de

Cálculo de Crecidas y Caudales Mínimos en Cuencas sin Información Fluviométrica, DGA

1995). Lo anterior implica por una parte que la cuenca del río Turbio, cuyas alturas

oscilan entre 898 y 6181 m.s.n.m., posee un área de aporte nival por determinar, mientras

que, por otro lado, las microcuencas de las quebradas naturales identificadas solo

reciben aportes pluviales, ya que sus elevaciones oscilan entre 909 y 1550 m.s.n.m.

3.1. CUENCAS APORTANTES

Para determinar los cauces y sus respectivas cuencas aportantes al área de estudio, junto

con sus distintos parámetros morfométricos de interés, se utilizó información del modelo

de elevación digital de la zona (DEM) del satélite ALOS PALSAR, con una resolución del

píxel de 12.5x12.5 m, el cual fue descargado del portal Infraestructura de Datos

Geoespaciales de Chile (IDE Chile). Se utilizó también el levantamiento topográfico

realizado para el área de estudio, el cual cubrió una superficie aproximada de 71

hectáreas, otorgando un mayor nivel de detalle en la zona de interés.

Dicha información de elevación se procesó a través de una plataforma SIG, delimitando

el trazado de los cauces, sus cuencas aportantes y obteniendo los principales parámetros

morfométricos que las caracterizan y que son requeridos para los distintos métodos

hidrológicos aplicables para la obtención de los caudales de crecida.

www.flujoing.cl / info@flujoing.cl

8

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

En la _Figura 2_, se muestra la cuenca hidrográfica aportante al tramo de estudio que fue

determinada para el río Turbio, mientras que en la Figura 2 se ilustran las microcuencas

correspondientes a las quebradas en estudio del sector.

**Figura 1. Delimitación de cuencas hidrográfica río Turbio.**

**Fuente: Elaboración propia, plataforma SIG.**

www.flujoing.cl / info@flujoing.cl

9

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 2. Delimitación de cuencas hidrográficas quebradas de estudio.**

**Fuente: Elaboración propia, plataforma SIG.**

Como es posible observar, se delimitó para el río Turbio en el tramo de estudio una

cuenca aportante de 4111.81 km [2], mientras que para las quebradas analizadas se

delimitaron cuencas cuyas áreas oscilan entre 0.11 km [2] y 0.21 km [2], pudiendo considerarse

estas últimas cuencas de pequeña superficie o microcuencas.

Se destaca que, de acuerdo con lo evidenciado en terreno, las quebradas identificadas

corresponden a cauces de escurrimientos efímeros, características de zonas áridas, que

solo presentan flujos de corta duración en respuesta directa a eventos de precipitación.

3.1.1. PARÁMETROS MORFOMÉTRICOS

Para el análisis hidrológico de las cuencas delimitadas, en particular para la aplicación

de las distintas metodologías disponibles, es necesaria la definición y obtención de los

parámetros morfométricos de las cuencas. Los parámetros de interés corresponden al

Área (A), Longitud de la cuenca (L), Longitud al centro de gravedad (L g ), Pendiente

media del cauce principal (S), Pendiente media de la cuenca (S c ), Desnivel máximo de

la cuenca (H), Desnivel medio de la cuenca (H m ) y Latitud de la cuenca (Lat).

www.flujoing.cl / info@flujoing.cl

10

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Todos estos parámetros son determinados a partir de una herramienta SIG,

considerando las fuentes de datos de elevación ya mencionadas y la delimitación de

trazado de los cauces y sus áreas aportantes previamente definidas.

Los parámetros determinados se resumen a continuación en la Tabla 1.

|L Lg S S A H Hm Lat<br>Cuenca c<br>km km m/m m/m km2 m m °|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Cuenca<br>L<br>Lg<br>S<br>Sc <br>A <br>H <br>Hm<br>Lat<br>km<br>km<br>m/m<br>m/m<br>km2 <br>m <br>m <br>°|km|km|m/m|m/m|km2|m|m|°|
|Río Turbio|112|49|0.047|0.503|4111.81|5283|2638.2|29.95|
|SC-1|0.89|0.57|0.719|0.707|0.21|640|346.4|29.95|
|SC-2|0.92|0.58|0.696|0.712|0.11|640|391.7|29.95|
|SC-3|0.84|0.42|0.690|0.701|0.11|580|266.1|29.95|

**Tabla 1. Parámetros Morfométricos.**

**Fuente: Elaboración propia.**

Como se puede observar, se tiene para la cuenca del río Turbio una pendiente media

de 50%, consistente con sus características montañosas, mientras que para las

quebradas se tienen pendientes medias de las cuencas del orden de 70%, las cuales

fueron obtenidas a partir de la interpolación del mapa de pendientes de cada cuenca.

A continuación, la _Figura 3_ presenta un mapa de elevaciones del área de estudio,

mientras que la _Figura 4_ presenta un mapa de pendientes, caracterizando

adecuadamente la geomorfología del área.

www.flujoing.cl / info@flujoing.cl

11

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 3. Mapa de elevaciones área de estudio.**

**Fuente: Elaboración propia, plataforma SIG.**

**Figura 4. Mapa de pendientes (%) área de estudio.**

**Fuente: Elaboración propia, plataforma SIG.**

www.flujoing.cl / info@flujoing.cl

12

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

3.1.2. TIEMPO DE CONCENTRACIÓN

El tiempo de concentración corresponde a un concepto ampliamente utilizado en

hidrología para evaluar la respuesta hidrológica de una cuenca a un evento de

precipitación, y corresponde al tiempo característico en el cual la totalidad de una

cuenca contribuye al caudal en el punto de salida de esta. Su determinación es necesaria

para la utilización de metodologías hidrológicas para caudales de crecida, tales como

el método racional e hidrogramas unitarios.

Para estimar el tiempo de concentración de una cuenca (T c ) se emplearon las expresiones

que se presentan en la siguiente tabla, y que son recomendadas por el Manual de

Carreteras del Ministerio de Obras Públicas en su Tabla 3.702.501.A.

|Autor Expresión Observaciones|Col2|Col3|
|---|---|---|
|Normas Españolas|Tc= 18 ∗L0,76 S0,19<br>⁄<br>||
|California Culverts<br>Practice (1942)|Tc= 57 ∗(L3 H<br>⁄ )0,385|Cuencas de montaña|
|Giandotti|Tc= 60 ∗((4 ∗A0,5 + 1,5 ∗L)/(0,8 ∗Hm<br>0,5)|Cuencas pequeñas<br>con pendiente|
|SCS (1975)|Tc= 258,7 ∗L0,8 ∗((1000 CN<br>⁄<br>) −9)<br>0,7<br>1900 ∗S0,5<br>|Cuencas rurales|

**Tabla 2. Expresiones para determinar el Tiempo de Concentración.**

**Fuente: MC-V3.**

Donde:

 Tc: Tiempo de concentración (min).

 L: Longitud de cauce (km).

 S: Pendiente (m/m).

 A: Área de la cuenca (km).

 Hm: Diferencia de nivel entre la cota media de la cuenca y la salida (m).

 H: Diferencia de nivel total entre cotas extremas de la cuenca (m).

 CN: Curva Número (CN=85 de acuerdo con la Tabla 2-2a del artículo

“Hidrología Urbana para Cuencas Pequeñas” del Servicio de Conservación de

Recursos Naturales (USDA, 1986)).

www.flujoing.cl / info@flujoing.cl

13

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

En la tabla a continuación se presentan los tiempos de concentración calculados con las

cuatro metodologías indicadas para cada una de las cuencas en estudio, considerando

los parámetros morfométricos e hidrológicos definidos en los acápites anteriores.

|Tc (min)<br>Cuenca<br>Normas Españolas CCP (1942) Giandotti SCS (1975)|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Cuenca<br>Tc (min) <br>Normas Españolas<br>CCP (1942)<br>Giandotti<br>SCS (1975)|Normas Españolas|CCP (1942)|Giandotti|SCS (1975)|
|Río Turbio|1160.60|489.12|619.84|1398.75|
|SC-1|17.54|10.00|12.77|10.00|
|SC-2|18.10|10.00|10.26|10.00|
|SC-3|16.92|10.00|11.89|10.00|

**Tabla 3. Tiempos de concentración estimados por cuenca.**

**Fuente: Elaboración propia.**

Cabe destacar que de acuerdo con los criterios del Manual de Carreteras V3, el método

de Giandotti es solo aplicable cuando el área de la cuenca es menor a 200 ha. De igual

forma en el mismo documento se establece el criterio de adoptar 10 minutos como valor

mínimo para el tiempo de concentración, lo cual se establece como envolvente inferior

para el valor a determinar en cada método.

Por lo tanto, el tiempo de concentración adoptado para la cuenca del río Turbio

corresponde al promedio entre los métodos de Normas Españolas, CCP y SCS, mientras

que para las quebradas se utilizó el promedio de los cuatro métodos, ya que para todas

estas el método de Giandotti se determinó aplicable. Se destaca que con los distintos

métodos se determinaron tiempos de concentración similares.

Finalmente, los tiempos de concentración seleccionados se presentan en la siguiente

tabla.

|Cuenca Tc (min) Tc (h)|Col2|Col3|
|---|---|---|
|Río Turbio|1016.2|16.94|
|Quebrada Sin Nombre 1|12.6|0.21|
|Quebrada El Copado|12.1|0.20|
|Quebrada Sin Nombre 2|12.2|0.20|

**Tabla 4. Tiempos de concentración definidos por cuenca.**

**Fuente: Elaboración propia.**

3.2. ANALISIS DE PRECIPITACIONES

Dado que de los cauces analizados solo el río Turbio cuenta con estación fluviométrica,

para las quebradas en estudio es necesario estimar los caudales de crecidas a partir de

www.flujoing.cl / info@flujoing.cl

14

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

métodos que relacionan la precipitación con la escorrentía, siendo importante

determinar las precipitaciones máximas asociadas a los periodos de retorno de interés,

junto con las curvas de Intensidad-Duración-Frecuencia (IDF) características del área de

estudio.

3.2.1. PRECIPITACIONES MÁXIMAS

Para la determinación de las precipitaciones máximas, se utilizan los datos

pluviométricos obtenidos de las estaciones meteorológicas más cercanas a la zona de

estudio.

Se identificó una estación pluviométrica en las cercanías del proyecto, a una distancia

aproximada de 4.5 km, la cual cuenta con un registro pluviométrico amplio y continuo

desde 1954. Dicha estación se ubica en las coordenadas especificadas en la _Tabla 5_,

según también se ilustra en la _Figura 5_ .

|Distancia al<br>Estación Tipo Código BNA UTM E UTM N Cuenca<br>Proyecto|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Rivadavia|Pluviométrica|04308003-2|349.359|6.682.656|Río Elqui|4.5 Km al SO|

**Tabla 5. Datos estaciones meteorológicas cercanas.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

15

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 5. Ubicación estaciones meteorológicas.**

**Fuente: Elaboración propia.**

En el siguiente gráfico se muestra la serie de datos disponibles de precipitaciones

máximas en 24 horas por año, según el registro histórico de datos disponibles en dicha

estación entre los años 1954 y 2020.

www.flujoing.cl / info@flujoing.cl

16

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Gráfico 1. Serie de datos de precipitaciones máximas en 24 hrs.**

**Fuente: DGA.**

Sobre la serie de datos presentada se realizó un análisis de frecuencia utilizando el

software Easyfit 5.5. Se analizaron distintos ajustes de distribuciones estadísticas, y se

seleccionó la que presenta mejores indicadores, que en el caso de estudio corresponde

a la distribución Pearson 6 de 4 parámetros, para la cual se obtuvieron los mejores

valores de estadísticos de las pruebas Kolmogorov-Smirnov y Chi-cuadrado, sin presentar

rechazo estadístico ante ningún nivel de significancia de dichas pruebas, ni de la prueba

Anderson-Darling.

La siguiente tabla muestra los valores de precipitación máxima en 24 horas para distintos

periodos de retorno según las tres distribuciones que presentaron mejores ajustes

estadísticos. De igual forma, la Figura 6 ilustra la gráfica de función de densidad de

probabilidad para dichas distribuciones y sus distintos valores estadísticos y ranking de

ajuste.

www.flujoing.cl / info@flujoing.cl

17

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

|Período de Retorno|Precipitación máx. 24 h (mm)|Col3|Col4|
|---|---|---|---|
|Tr|Pearson 6 (4p)|Gen. Gamma (4p)|Lognormal (3p)|
|2|25.91|25.89|25.68|
|5|42.60|42.77|42.28|
|10|53.91|54.05|53.89|
|25|68.37|68.18|69.16|
|50|79.24|78.57|80.93|
|100|90.18|88.80|93.02|

**Tabla 6. Precipitaciones máximas diarias según distintas distribuciones.**

**Fuente: Elaboración propia.**

**Figura 6. Ajustes de distribuciones estadística PP máx 24 h.**

**Fuente: Elaboración propia, Easyfit.**

www.flujoing.cl / info@flujoing.cl

18

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

De igual forma, la Figura 7 detalla los valores estadísticos para la distribución

seleccionada, presentando además los valores críticos para los distintos niveles de

significancia.

**Figura 7. Valores estadísticos distribución seleccionada análisis PP máx 24h.**

**Fuente: Elaboración propia, Easyfit.**

Finalmente, la _Tabla 7_ resume los valores definidos, los cuales se consideran

estadísticamente más representativos y se utilizarán para este estudio.

|Período de Pearson 6<br>retorno (4P)|Col2|
|---|---|
|2|25.91|
|5|42.60|
|10|53.91|
|25|68.37|
|50|79.24|
|100|90.18|

**Tabla 7. Precipitaciones máximas diarias definidas.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

19

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

3.2.2. GENERACIÓN CURVAS IDF

Para la determinación de las intensidades de precipitación, asociadas a distintas

duraciones y frecuencias, se identificó que existe registro pluviográfico correspondiente

a la misma estación Rivadavia, para la cual el Manual de carreteras presenta curvas de

duración que pueden ser extrapoladas a distintos puntos de la región para la

determinación de las curvas IDF.

A partir de los coeficientes de duración que se presentan en la Tabla 3.702.403.A MC

V3) es posible construir las curvas IDF de duración entre 1 y 24 horas, para distintos

periodos de retorno, al conocer la precipitación máxima en 24 horas asociada a un

periodo de retorno en específico.

Se utilizaron entonces las precipitaciones máximas diarias determinadas en la Tabla 7,

los coeficientes de duración expuestos en la Tabla 8 y un coeficiente de corrección K=1.1

(que corrige los datos a las 24 horas más lluviosas de la tormenta).

|Duración (horas)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|Est. Pluv.|1|2|4|6|8|10|12|14|18|24|
|Rivadavia|0.12|0.21|0.35|0.48|0.59|0.68|0.75|0.78|0.87|1|

**Tabla 8. Coeficientes de duración estación Rivadavia.**

**Fuente: Manual de carreteras V-3.**

Se obtuvieron a partir de lo anterior las intensidades presentadas en la _Tabla 9_ y las

curvas IDF ilustradas en el _Gráfico 2_ .

|Duración<br>(min)|Intenisidad (mm/h) para distintos Tr|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Duración<br>(min)|2|5|10|25|50|100|
|60|3.42|5.62|7.12|9.02|10.46|11.90|
|120|2.99|4.92|6.23|7.90|9.15|10.42|
|240|2.49|4.10|5.19|6.58|7.63|8.68|
|360|2.28|3.75|4.74|6.02|6.97|7.94|
|480|2.10|3.46|4.37|5.55|6.43|7.32|
|600|1.94|3.19|4.03|5.11|5.93|6.75|
|720|1.78|2.93|3.71|4.70|5.45|6.20|
|840|1.59|2.61|3.30|4.19|4.86|5.53|
|1080|1.38|2.26|2.87|3.63|4.21|4.79|
|1440|1.19|1.95|2.47|3.13|3.63|4.13|

**Tabla 9. Curvas IDF duración mayor a 1 hora.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

20

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Gráfico 2. Curvas IDF duración mayor a 1 hora.**

**Fuente: Elaboración Propia.**

Por otro lado, es necesario determinar también las curvas IDF para duraciones menores

a 1 hora, para lo cual es posible utilizar la expresión de Bell.

En primer lugar, se tiene a partir de las curvas IDF anteriores la precipitación máxima

asociada a una duración de 1 hora para el periodo de retorno de 10 años es 7.12 mm.

A partir de este valor, se aplicó la expresión de Bell que se presenta a continuación:

T = (0,54 ∗t 0,25 ) ∗(0,21 ∗ln(T) + 0,52) ∗P 1

P t

10

Los resultados de la aplicación de la ecuación de Bell para la obtención de la intensidad

de precipitación se presentan en la _Tabla 10_, mientras que el _Gráfico 3_ muestra las curvas

IDF de duración menor a 1 hora obtenidas para la zona de estudio.

|Duración<br>(min)|Intensidad (mm/h) para distintos períodos de retorno|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Duración<br>(min)|2|5|10|25|50|100|
|5|17.47|22.53|26.35|31.40|35.22|39.04|
|10|13.08|16.86|19.72|23.50|26.36|29.22|
|15|10.66|13.74|16.07|19.15|21.49|23.82|
|20|9.12|11.76|13.75|16.39|18.38|20.38|
|25|8.04|10.37|12.12|14.45|16.21|17.97|
|30|7.23|9.33|10.91|13.00|14.58|16.16|
|35|6.60|8.51|9.96|11.87|13.31|14.76|
|40|6.10|7.86|9.19|10.95|12.29|13.62|
|45|5.67|7.31|8.56|10.20|11.44|12.68|
|50|5.32|6.86|8.02|9.56|10.72|11.88|
|55|5.01|6.46|7.56|9.01|10.11|11.20|
|60|4.75|6.12|7.16|8.53|9.57|10.61|

**Tabla 10. Intensidad (mm/h) duración menor a 1 hora.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

21

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Gráfico 3. Curvas IDF duración menor a 1 hora.**

**Fuente: Elaboración Propia.**

3.3. ANALISIS DE CAUDALES

En el presenta capitulo se detalla la obtención de caudales máximos instantáneos para

los cauces de interés. Según se indicó anteriormente, para el caso del río Turbio se

identificó la estación fluviométrica “Río Turbio en Varillar” en las cercanías del área del

proyecto, de administración de la DGA. Dicha estación cuenta con un amplio registro

histórico, por lo tanto, los caudales máximos de dicho cauce en el área de proyecto

serán obtenidos mediante análisis de frecuencia sobre la serie de datos, lo cual se

describe en el acápite 3.3.1.

Por otro lado, ninguna de las tres quebradas analizadas posee control fluviométrico, por

lo cual la estimación de caudales se realizará a partir de métodos que relacionan la

precipitación con la escorrentía, utilizando las caracterizaciones de las cuencas

aportantes y de las precipitaciones definidas en los capítulos anteriores.

Existen distintas metodologías para la obtención de caudales máximos en cuencas no

controladas, recomendadas tanto en las guías y manuales nacionales e internacionales,

siendo estas ampliamente utilizadas en hidrología. Los rangos de aplicabilidad de estos

métodos dependen de las características de las cuencas en cuestión, principalmente del

área de estas. Se diferencia entre cuencas con áreas mayores a 25 km [2] y cuencas

pequeñas menores a 25 km [2], definiendo este límite para la aplicación de distintos

métodos según lo establecido en el Manual de carreteras Volumen 3. Para este estudio,

www.flujoing.cl / info@flujoing.cl

22

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

dado que las quebradas analizadas corresponden a microcuencas que no superan los

0.21 km [2], se utilizará el método racional, según se describe en el acápite 3.3.2.

Finalmente, por las características de las quebradas analizadas, se determina que, si

bien los caudales de estos cauces son poco significativos, existe un potencial de aumento

volumétrico producto del arrastre y concentración de sedimentos (flujos detríticos) que

debe ser incorporado en el análisis, lo cual se detalla en el acápite 3.3.3.

3.3.1. ANALISIS DE FRECUENCIA RÍO TURBIO

Para la determinación de los caudales máximos instantáneos del río Turbio en el tramo

de estudio se utilizan los datos fluviométricos de la estación “Río Turbio en Varillar”,

ubicada a una distancia de 250 m aguas abajo del área de proyecto, pudiendo

considerarse que sus caudales son directamente representativos para el estudio sin

necesidad de análisis de transposición. Dicha estación cuenta con un registro

fluviométrico amplio y continuo desde 1969, y se ubica en las coordenadas especificadas

en la Tabla 11, según también se ilustra en la Figura 8.

|Distancia al<br>Estación Tipo Código BNA UTM E UTM N Cuenca<br>Proyecto|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Río Turbio<br>en Varillar|Fluviométrica|04308001-6|351.661|6.686.061|Río<br>Elqui|0.25 Km al SO|

**Tabla 11. Datos estación fluviométrica analizada.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

23

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 8. Ubicación estación fluviométrica analizada.**

**Fuente: Elaboración propia.**

En el siguiente gráfico se muestra la serie de máximos anuales elaborada a partir del

registro histórico de caudales instantáneos disponibles en dicha estación entre los años

1969 y 2021.

**Gráfico 4. Serie de caudales máximos anuales estación Río Turbio en Varillar.**

**Fuente: DGA.**

www.flujoing.cl / info@flujoing.cl

24

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Sobre la serie de datos presentada se realizó un análisis de frecuencia utilizando el

software Easyfit 5.5. Se analizaron distintos ajustes de distribuciones estadísticas, y se

seleccionó la que presenta mejores indicadores, que en el caso de estudio corresponde

a la distribución Lognormal de 3 parámetros, para la cual se obtuvieron los mejores

valores de estadísticos de las pruebas Kolmogorov-Smirnov y Anderson-Darling, sin

presentar rechazo estadístico ante ningún nivel de significancia de dichas pruebas, ni de

la prueba Chi-cuadrado.

Es importante destacar que dichos resultados son consistentes con lo indicado en el

“Manual de Crecidas para Cuencas Sin Información Fluviométrica” de la DGA, donde

se indica que se utilizó la distribución Lognormal para el ajuste de la curva de frecuencia

regional para las cuencas de Copiapó, Huasco y Elqui.

La siguiente tabla muestra los valores de caudales máximos para distintos periodos de

retorno según las tres distribuciones que presentaron mejores ajustes estadísticos. De

igual forma, la Figura 9 ilustra la gráfica de función de densidad de probabilidad para

dichas distribuciones y sus distintos valores estadísticos y ranking de ajuste.

|Período de Retorno|Caudal máximo instantáneo (m3/s)|Col3|Col4|
|---|---|---|---|
|Tr|Lognormal (3P)|Pearson 5|Gamma (3p)|
|2|10.51|10.41|11.23|
|5|25.99|24.53|26.63|
|10|43.29|42.22|39.09|
|25|75.70|82.27|56.07|
|50|109.17|133.71|69.16|
|100|152.09|215.37|82.39|

**Tabla 12. Caudales máximos según distintas distribuciones.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

25

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 9. Ajustes de distribuciones estadística caudales máximos.**

**Fuente: Elaboración propia, Easyfit.**

De igual forma, la Figura 10 detalla los valores estadísticos para la distribución

seleccionada, presentando además los valores críticos para los distintos niveles de

significancia.

www.flujoing.cl / info@flujoing.cl

26

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 10. Valores estadísticos distribución seleccionada análisis QMI.**

**Fuente: Elaboración propia, Easyfit.**

Finalmente, la Tabla 13 resume los valores definidos, los cuales se consideran

estadísticamente más representativos y se utilizarán para este estudio.

|Período de Log<br>retorno Normal|Col2|
|---|---|
|2|10.51|
|5|25.99|
|10|43.29|
|25|75.70|
|50|109.17|
|100|152.09|

**Tabla 13. Caudales máximos instantáneos Río Turbio (m** **[3]** **/s).**

**Fuente: Elaboración propia.**

3.3.2. MÉTODO RACIONAL

En el presente capítulo se describe la obtención de caudales para las tres quebradas

analizadas utilizando el Método Racional, recomendado por el Volumen 3 del Manual

de Carreteras. Este método es utilizable en cuencas pequeñas, menores que 25 km [2] .

Supone que el escurrimiento máximo proveniente de una tormenta es proporcional a la

www.flujoing.cl / info@flujoing.cl

27

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

lluvia caída, supuesto que se cumple en forma más rigurosa en cuencas mayoritariamente

impermeables o en la medida que la magnitud de la lluvia crece y el área aportante se

satura. El caudal máximo para un determinado periodo de retorno se calcula mediante

la siguiente expresión:

Q= [CxIxA]

3.6

En que:

 - Q: Caudal instantáneo máximo de período de retorno T, expresado en m [3] /s.

 C: Coeficiente de escorrentía asociado al período de retorno T.

 I: Intensidad media de lluvia asociada al período de retorno T y a una duración

igual al tiempo de concentración de la cuenca, expresada en mm/h.

 - A: Área aportante expresada en km [2] .

Considerando lo anterior, los valores de área para cada cuenca corresponden a los

definidos en la Tabla 1, mientras que los valores de intensidad asociados al tiempo de

concentración de cada cuenca se obtienen a partir de las curvas IDF determinadas en el

acápite 3.2.2.

Por otro lado, la determinación del coeficiente de escorrentía se describe a continuación.

3.3.2.1. Coeficiente de Escorrentía

El coeficiente de escorrentía depende de las características del terreno, uso y manejo del

suelo, condiciones de infiltración, entre otros aspectos. Para la selección del coeficiente

de escorrentía se aplicaron las recomendaciones de la sección 3.702.503 del Manual

de Carreteras, que propone una estimación en base a factores de relieve, infiltración,

cobertura vegetal y almacenamiento de agua en el suelo.

Para las tres quebradas analizadas se definieron como representativos los mismos

factores para la determinación del coeficiente de escorrentía. Los factores de infiltración,

cobertura vegetal y almacenamiento superficial se definieron en categorías de Normal,

Extremo y Extremo, respectivamente, considerando las características similares de las

cuencas. Por otro lado, considerando las pendientes medias de las cuencas, el factor de

relieve se ha definido en Extremo, al tener pendientes medias del orden del 70%.

www.flujoing.cl / info@flujoing.cl

28

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

A continuación, en la siguiente tabla, se presentan los parámetros adoptados para

determinar el coeficiente de escorrentía representativo.

|Factor Categoría Valor|Col2|Col3|
|---|---|---|
|Relieve|Extremo|0.32|
|Infiltración|Normal|0.07|
|Cobertura Vegetal|Extremo|0.14|
|Almacenamiento Superficial|Extremo|0.11|
|TOTAL|TOTAL|0.64|

**Tabla 14. Determinación coeficiente de escorrentía para método racional.**

**Fuente: Elaboración propia.**

Por otra parte, para los periodos de retorno mayores a 10 años, es necesario utilizar los

coeficientes de amplificación recomendados en la misma sección del manual,

correspondientes a 1.10, 1.20 y 1.25 para T-25, T-50 y T-100 años, respectivamente.

Considerando lo anterior, en la siguiente tabla se definen los coeficientes de escorrentía

asociados a los distintos periodos de retorno, aplicables a las tres cuencas analizadas.

|Coeficiente de Escorrentía T(2) T(5) T(10) T(25) T(50) T(100)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|C(T)|0.64|0.64|0.64|0.70|0.77|0.80|

**Tabla 15. Coeficientes de escorrentía para método racional.**

**Fuente: Elaboración propia.**

3.3.2.2. Obtención de caudales con Método Racional

A partir de lo anterior, para la aplicación del método racional se definen en primera

instancia en la _Tabla 16_, las áreas, tiempos de concentración, e intensidades asociadas

a cada tiempo de concentración y periodo de retorno para las cuencas en análisis.

|Área Tc Intensidad en Tc (mm/h)<br>Cuenca<br>(km2) (min) T(2) T(5) T(10) T(25) T(50) T(100)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|Cuenca<br>Área <br>(km2) <br>Tc <br>(min)<br>Intensidad en Tc (mm/h)<br>T(2)<br>T(5)<br>T(10)<br>T(25)<br>T(50)<br>T(100)|Cuenca<br>Área <br>(km2) <br>Tc <br>(min)<br>Intensidad en Tc (mm/h)<br>T(2)<br>T(5)<br>T(10)<br>T(25)<br>T(50)<br>T(100)|Cuenca<br>Área <br>(km2) <br>Tc <br>(min)<br>Intensidad en Tc (mm/h)<br>T(2)<br>T(5)<br>T(10)<br>T(25)<br>T(50)<br>T(100)|T(2)|T(5)|T(10)|T(25)|T(50)|T(100)|
|SC-1|0.21|12.6|11.8|15.3|17.8|21.3|23.8|26.4|
|SC-2|0.11|12.1|12.1|15.6|18.2|21.7|24.3|27.0|
|SC-3|0.11|12.2|12.0|15.5|18.1|21.6|24.2|26.8|

**Tabla 16. Intensidades en Tc para Método Racional.**

**Fuente: Elaboración propia.**

Con dichos valores de intensidades y áreas, en conjunto con los coeficientes de

escorrentía determinados en el acápite anterior, es posible obtener los caudales para

las distintas cuencas, según se presenta a continuación en la _Tabla 17_ .

www.flujoing.cl / info@flujoing.cl

29

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

|Caudales (m3/s)<br>Cuenca<br>T(2) T(5) T(10) T(25) T(50) T(100)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Cuenca<br>Caudales (m3/s)<br>T(2)<br>T(5)<br>T(10)<br>T(25)<br>T(50)<br>T(100)|T(2)|T(5)|T(10)|T(25)|T(50)|T(100)|
|SC-1|0.44|0.57|0.67|0.87|1.07|1.23|
|SC-2|0.24|0.30|0.36|0.47|0.57|0.66|
|SC-3|0.23|0.30|0.35|0.46|0.57|0.66|

**Tabla 17. Caudales determinados por Método Racional.**

**Fuente: Elaboración propia.**

Como es posible observar, se obtuvieron caudales de baja magnitud, que oscilan entre

los 0.66 y 1.23 m [3] /s, lo cual verifica que de dichas quebradas corresponden a

microcuencas de baja importancia hidrológica, que serán igualmente analizadas en el

estudio hidráulico asociados al proyecto para evaluar su relación con las componentes

del proyecto.

3.3.3. CAUDALES DETRITICOS QUEBRADAS

Por las características de las quebradas efímeras analizadas, las cuales poseen suelos

arenosos desnudos, sin presencia de vegetación y con elevadas pendientes medias y en

su tramo de estudio, se determina que existe un potencial de aumento volumétrico

producto del arrastre y concentración de sedimentos (flujos detríticos) que debe ser

incorporado en el análisis hidráulico.

De acuerdo con la Guía Metodológica para Presentación y Revisión Técnica de Proyectos

de Cauces Naturales y Artificiales (DGA, 2016) este caudal está definido mediante la

siguiente expresión:

Q detr = [Q] [lí][q]

1 −C

Donde:

 - Q detr : Caudal detrítico (sólido más líquido) (m [3] /s).

 - Q líq : Caudal líquido (m [3] /s).

 - C: Concentración volumen de sólidos.

El valor de C se consideró como una concentración de los sedimentos igual al 30%, valor

representativo y conservador.

En la _Tabla 18_ se presentan los caudales detríticos de las quebradas analizadas,

considerando las expresiones y valores definidos.

www.flujoing.cl / info@flujoing.cl

30

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

|T(100)<br>Cuenca<br>Qlíq (m3/s) Qdetr (m3/s)|Col2|Col3|
|---|---|---|
|Cuenca<br>T(100)<br>Qlíq (m3/s)<br>Qdetr (m3/s)|Qlíq (m3/s)|Qdetr (m3/s)|
|SC-1|1.23|1.76|
|SC-2|0.66|0.94|
|SC-3|0.66|0.94|

**Tabla 18. Caudales líquidos y detríticos quebradas analizadas T-100 años.**

**Fuente: Elaboración propia.**

## 4. ANALISIS HIDRAULICO

En este capítulo se detallan los aspectos relacionados al análisis de modelación

hidráulica realizado para el proyecto, definiendo en primer lugar lo respectivo a la

construcción del modelo y sus condiciones de modelación. Posteriormente se presentan

los resultados hidráulicos del modelo para el estudio de inundaciones sobre el escenario

con periodo de retorno T-100 años, tanto para el río Turbio como para las quebradas

menores, determinando las áreas de inundación, sus principales características

hidráulicas (profundidad y velocidad) y su influencia sobre la zona del proyecto y sus

obras.

Por otro lado, para el caso del análisis sobre las quebradas menores, se propone la

implementación de obras hidráulicas para la ejecución del proyecto, por lo tanto, se

realizará también el análisis hidráulico de la situación proyectada, verificando el

correcto comportamiento hidráulico de las obras, y sus efectos en el área de estudio ante

las mismas condiciones hidrológicas de modelación. Es importante destacar que el

detalle del diseño de obras propuestas y los estudios complementarios se desarrollan en

los capítulos posteriores.

La metodología aplicada para el análisis hidráulico corresponde a modelación numérica

bidimensional mediante el software Iber, ampliamente utilizado para la simulación de

flujos en ríos y estuarios. Dicho modelo es aplicable a condiciones donde las hipótesis

de distribución hidrostática de presiones y distribución uniforme de la velocidad en la

profundidad sean representativas de las condiciones dominantes, como es el caso de los

escurrimientos someros de los cauces de estudio.

www.flujoing.cl / info@flujoing.cl

31

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Por las características de los cauces en estudio, se desarrollaron dos modelos

independientes con el programa Iber. En primer lugar, se desarrolló un modelo para el

río Turbio, considerando su cauce, sus singularidades y sus zonas aledañas

potencialmente inundables, incluyendo el área donde se instalan las obras del proyecto.

La Figura 11 ilustra el tramo del río analizado, así como el área considerada para la

elaboración del modelo.

**Figura 11. Área de modelación hidráulica río Turbio.**

**Fuente: Elaboración propia.**

Por otro lado, se realizó también un modelo para analizar el comportamiento hidráulico

de las quebradas cercanas al área de proyecto, las cuales, si bien se determinó que

corresponden a microcuencas de baja importancia hidrológica, es necesario analizar su

relación con las componentes del proyecto. La Figura 12 ilustra los trazados de las

quebradas analizadas, así como el área de modelación considerada.

www.flujoing.cl / info@flujoing.cl

32

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 12. Área de modelación hidráulica quebradas analizadas.**

**Fuente: Elaboración propia.**

4.1. FUNDAMENTOS DE LA MODELACIÓN CON IBER

El modelo utilizado está basado en el software Iber, en su versión 3.3.1, el cual es un

modelo numérico de simulación de flujo turbulento en lámina libre en régimen no

permanente, y de procesos medioambientales en hidráulica fluvial. Dicho software

cuenta actualmente con una gran variedad de módulos para distintas aplicaciones,

pasando a ser un modelo que permite simular múltiples procesos ambientales de base

hidrodinámica. Se destaca en este caso la utilización del módulo hidrodinámico para

los análisis de inundación de interés.

El módulo de hidrodinámica de Iber permite predecir los valores que toman las variables

hidráulicas del flujo (profundidad, velocidad, caudal, etc.) resolviendo las ecuaciones

de Saint-Venant de forma bidimensional, es decir, se resuelven las ecuaciones en las dos

direcciones horizontales y promediadas en la profundidad, según se muestra en las

siguientes expresiones.

www.flujoing.cl / info@flujoing.cl

33

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

∂h

∂h∂t [+ ∂hU] ∂x [x]

[x]

∂x [+ ∂hU] [y]

= 0,
∂y

[∂]

∂y [(hU] [x] [U] [y] [) = −gh ∂Z] ∂x [b]

∂x [b] [+ τ] [s,x]

[s,x]

ρ [−τ] ρ [b,x]

2

[∂]

∂x [(hU] [x]

[2] [∂]

2 ~~[)]~~ [ +]

∂ [∂]
∂t [(hU] [x] [) +]

2 + g [h] [2]

[x]

∂x [x] ~~[)]~~ [ +] [∂]

∂y [∂] [(θ] [t] [h ∂U] ∂y [x]

[x]

∂y ~~[)]~~ [,]

[b,x] [∂]

ρ [+]

∂x [∂] [(θ] [t] [h ∂U] ∂x [x]

∂y [b] [+ τ] ρ [s,][y]

[s,][y]

ρ [−τ] [b,] ρ [y]

[2]

2 [) = −gh ∂Z] ∂y [b]

∂y [∂] [(θ] [t] [h ∂U] ∂y [y]

[y]

∂y ~~[)]~~ [,]

∂ [∂]
∂t [(hU] [y] [) +]

[∂] [∂]

∂x [(hU] [x] [U] [y] [) +]

2

[∂]

∂y [(hU] [y]

2 + g [h] [2]

∂x [y] [) +] [∂]

[b,][y] [∂]

ρ [+]

[∂]

∂x [(θ] [t] [h ∂U] ∂x [y]

en donde h es el calado o profundidad, Ux y Uy son las velocidades horizontales

promediadas en profundidad, g es la aceleración de gravedad, ρ es la densidad del

agua, Z b es la cota del fondo, τ s es la fricción en la superficie libre debido al rozamiento

producido por el viento, τ b es la fricción debido al rozamiento del fondo y θ t es la

viscosidad turbulenta (Bladé, 2012).

La fricción de fondo se evalúa mediante la fórmula de Manning como:

τ b,x = ρgh [n] [2] [U] h [4 3][x ] ⁄ [|U|] [2] ~~,~~

[|U|] [2]
τ b,y = ρgh [n] [2] [U] h [4 3][y] ⁄ ~~,~~

Dichas ecuaciones asumen una distribución de presión hidrostática y una distribución

relativamente uniforme de la velocidad en profundidad. La hipótesis de presión

hidrostática se cumple razonablemente en el flujo en ríos y aguas someras. Asimismo, la

hipótesis de distribución uniforme de velocidad en profundidad se cumple habitualmente

en aguas someras, aunque pueden existir zonas en las que dicha hipótesis no se cumpla

debido a flujos locales tridimensionales.

Dichas ecuaciones se resuelven mediante esquemas numéricos estables y robustos, sobre

un dominio espacial discretizado con volúmenes finitos en mallas no estructuradas,

formadas por elementos triangulares y cuadrangulares.

Según lo especificado por sus autores, algunas aplicaciones del modelo, particularmente

del módulo hidrodinámico, corresponden a:

 Simulación del flujo en lámina libre en cauces naturales.

 Evaluación de zonas inundables. Cálculo de las zonas de flujo preferente.

 - Cálculo hidráulico de encauzamientos.

www.flujoing.cl / info@flujoing.cl

34

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

 - Cálculo hidráulico de redes de canales en lámina libre.

 - Cálculo de corrientes de marea en estuarios.

4.2. DATOS Y CONDICIONES DEL MODELO IBER

Se detallan a continuación los aspectos relativos a la construcción del modelo

(geometría, malla de cálculo, rugosidad), las condiciones de modelación (condiciones

de contorno, condiciones internas, condiciones meteorológicas) y también aspectos de

la simulación y postproceso.

4.2.1. GEOMETRÍA

La construcción de la geometría del área de estudio es una de las etapas más

importantes del modelo, ya que permite caracterizar la morfología que determina el

movimiento del fluido. Para la elaboración de la geometría de las zonas de modelación

se utilizó el levantamiento topo batimétrico del área de estudio, de 71 hectáreas de

extensión, obtenido por medio de fotogrametría de precisión y levantamiento de puntos

topográficos y batimétricos con sistema GNSS, el cual fue procesado y transformado en

una superficie ráster de alta definición que puede ser incorporada al modelo mediante

distintas herramientas de la interfaz. La _Figura 13_ muestra el modelo de elevación digital

construido en base a este proceso.

www.flujoing.cl / info@flujoing.cl

35

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 13. DEM utilizado para la geometría del modelo.**

**Fuente: Elaboración propia, plataforma SIG.**

4.2.2. MALLA DE CÁLCULO

Para que el modelo pueda llevar a cabo la resolución de las ecuaciones gobernantes

por el método de volúmenes finitos, es necesario realizar previamente una discretización

espacial del dominio a estudiar. Para ello se divide el dominio de estudio en celdas o

elementos de tamaño relativamente pequeño, a la que se le denomina malla de cálculo.

La generación de la malla de cálculo es una de las etapas que requiere mayor tiempo y

esfuerzo a la hora de desarrollar un estudio de simulación numérica del flujo, ya que se

requiere determinar un tipo de malla que se adapte y represente adecuadamente la

geometría del problema y con una selección y distribución de tamaños adecuados para

lograr independizar de esta variable los resultados obtenidos, al mismo tiempo que

permitir eficiencia para la modelación.

El modelo Iber presenta distintas herramientas internas para la creación del mallado,

siendo indispensable hacer un análisis de sensibilidad para independizar los resultados

de esta variable. Para el caso de estudio se utilizó una malla irregular no estructurada

www.flujoing.cl / info@flujoing.cl

36

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

generada por medio de la herramienta Rfast, distribuida con distintos tamaños según las

características de la geometría y las zonas de mayor interés de análisis. Para la

modelación de la zona de río Turbio se definió como óptimo de trabajo una malla de

186.721 elementos, con tamaños entre 0.5 y 7.5 metros, caracterizando adecuadamente

las distintas zonas según sus niveles de detalles e importancia en el análisis. Para la zona

de las quebradas se definió una malla de 364.749 elementos, con tamaños variables

entre 0.25 y 5 m.

La _Figura 14_ ilustra un tramo de la malla utilizada, mientras que la _Figura 15 y Figura 16_

reflejan la distribución de tamaños de los elementos de la malla.

**Figura 14. Malla de cálculo de modelo.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

37

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 15. Distribución acumulada de tamaños de los elementos de la malla zona río Turbio.**

**Fuente: Elaboración propia, Iber.**

**Figura 16. Distribución acumulada de tamaños de los elementos de la malla zona quebradas.**

**Fuente: Elaboración propia, Iber.**

4.2.3. RUGOSIDAD

Para la aplicación de la rugosidad, el modelo permite asignar distintos valores conforme

a la identificación de usos de suelo. Se analiza para el caso de estudio la aplicación de

los distintos usos de suelo, según sus características como tipo de suelo, cobertura vegetal

y edificaciones del área de estudio.

Para el análisis de la zona del río Turbio se consideraron dos usos de suelo con

rugosidades diferentes, diferenciando entre el canal o sección normal de escurrimiento

www.flujoing.cl / info@flujoing.cl

38

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

del río y las planicies o zonas de inundación aledañas. Por otro lado, para el análisis

de la zona de las quebradas, se consideró la aplicación de un único uso de suelo, debido

a que no existen diferencias significativas en la cobertura ni características de este dentro

del esta área del estudio.

Se requirió entonces definir la rugosidad para estos usos de suelo en términos del

coeficiente de Manning (n). Para la sección normal de escurrimiento del río Turbio y para

la zona de las quebradas se utilizó el método de Cowan descrito en el MC V3, el que

se basa en la siguiente expresión:

n= m× (n 0 + n 1 + n 2 + n 3 + n 4 )

Donde:

n 0 = Rugosidad base.

n 1 = Rugosidad adicional por irregularidades perímetro mojado.

n 2 = Rugosidad adicional por variación de forma.

n 3 = Rugosidad adicional por obstrucciones.

n 4 = Rugosidad adicional por presencia de vegetación.

m= Factor de corrección por efecto sinuosidad.

Conforme a lo anterior y a las características de estos cauces, considerando el material

de lecho, las características geométricas obtenidas de la topografía y los registros de

terreno, se determinan un coeficiente de rugosidad de **n=0.038** para el río Turbio y

**n=0.035** para la zona de las quebradas, según lo expuesto en la Tabla 19 y Tabla 20.

|Condición Valor|Col2|Col3|Col4|
|---|---|---|---|
|Material del lecho|Grava Gruesa|n0|0.028|
|Grado de irregularidad P.M.|Leve|n1|0.005|
|Variaciones de secciones|Alternándose Ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Despreciable|n3|0.000|
|Densidad de vegetación|Baja|n4|0.000|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|n|n|n|0.038|

**Tabla 19. Rugosidad método de Cowan río Turbio.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

39

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

|Condición Valor|Col2|Col3|Col4|
|---|---|---|---|
|Material del lecho|Tierra (arena)|n0|0.020|
|Grado de irregularidad P.M.|Leve|n1|0.005|
|Variaciones de secciones|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Nula|n4|0.000|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|n|n|n|0.035|

**Tabla 20. Rugosidad método de Cowan zona de quebradas.**

**Fuente: Elaboración propia.**

Por otra parte, para las planicies de inundación aledañas al río Turbio, se recurre a la

Tabla 5-6 del texto “Hidráulica de Canales Abiertos, Ven Te Chow”, asociando un valor

de **n=0.050**, correspondiente a matorrales dispersos con mucha maleza (D-2 C1).

La Figura 17 ilustra un registro de terreno del río Turbio y zonas aledañas.

**Figura 17. Registro de terreno río Turbio.**

**Fuente: Elaboración propia.**

4.2.4. CONDICIONES DE CONTORNO E INTERNAS

Iber permite la asignación de condiciones de borde de entrada y salida, además de

condiciones internas como fuentes y sumideros. Para las condiciones de entrada es

posible asignar un caudal total, un caudal especifico o una cota de agua, junto con el

www.flujoing.cl / info@flujoing.cl

40

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

régimen y condiciones específicas en función de este. Para las condiciones de salida, es

necesario definir el régimen, donde en el caso de régimen supercrítico/critico no se

requieren mayores detalles de condiciones a diferencia del régimen subcrítico.

El tratamiento de estas condiciones debe ser cuidadosamente analizado, con el fin de

minimizar las influencias sobre los resultados del modelo, especialmente en las zonas de

interés, lo cual se realiza en este estudio por medio de un proceso de iteraciones y

extensión suficiente del área de estudio.

El modelo permite también la asignación de condiciones internas, como estructuras,

perdidas locales, fuentes y sumideros en cualquier parte del dominio de cálculo.

Para las condiciones de contorno de entrada se utilizaron escenarios estacionarios con

los caudales definidos en el capítulo 3.3 para el periodo de retorno de 100 años. En el

caso del análisis de las quebradas, por las condiciones antes descritas este caudal fue

mayorado considerando la estimación de caudales detríticos.

Se determinó que, de acuerdo con las características de los cauces y área de estudio, la

condición de entrada más apropiada es por medio de caudales totales en régimen

subcrítico, para lo cual se definieron los límites de entrada en función del trazado de los

cauces según la topografía e imágenes aéreas de alta definición. En la _Tabla 21_ se

detallan los caudales utilizados para cada condición de entrada, para los modelos de

cada zona definida _._

|Q total de entrada<br>Zona Entrada Cauce asociado<br>(m3/s)|Col2|Col3|Col4|
|---|---|---|---|
|Río Turbio|A-1|Río Turbio|152.09|
|Quebradas|B-1|SC-1|1.76|
|Quebradas|B-2|SC-2|0.94|
|Quebradas|B-3|SC-3|0.94|

**Tabla 21. Caudales de condiciones de contorno de entrada.**

**Fuente: Elaboración propia.**

Para las condiciones de contorno de salida se establecieron condiciones

supercríticas/criticas, y se definieron sus límites según la misma metodología indicada en

el párrafo anterior, e iterándolos para no generar condiciones poco realistas que no

permitan la salida de flujos del modelo.

www.flujoing.cl / info@flujoing.cl

41

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

La _Figura 18_ y _Figura 19_ ilustran las condiciones de contorno de entrada y salida

incorporadas al modelo de la zona del río Turbio y a la zona de las quebradas,

respectivamente, especificando la numeración de las distintas entradas. Se destaca que

de acuerdo con los requerimientos del estudio no fue necesaria la incorporación de

condiciones internas al modelo.

**Figura 18. Condiciones de contorno aplicadas al modelo río Turbio.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

42

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 19. Condiciones de contorno aplicadas al modelo de la zona de Quebradas.**

**Fuente: Elaboración propia.**

4.2.5. CONDICIONES INICIALES

Las condiciones iniciales del modelo, es decir los valores de partida de las variables de

cota o calado en las celdas del dominio, se asignaron como condición seca, aplicando

valores nulos de calado en todas las celdas; utilizando un calentamiento apropiado del

modelo en las respectivas simulaciones para permitir que los resultados se independicen

de esta condición inicial.

4.2.6. SINGULARIDADES

Para la modelación es necesario considerar también las singularidades existentes en los

tramos de cauce en estudio.

A partir del recorrido del terreno se identificó un puente sobre el río Turbio,

correspondiente a la Ruta 41, el cual fue caracterizado a detalle durante el levantamiento

topográfico, a partir de lo cual se incorporó al modelo utilizando las herramientas de

definición de estructuras que posee el módulo hidrodinámico de Iber.

La Figura 20 corresponde a un registro de terreno el puente identificado, así como la

Figura 21 esquematiza las dimensiones y características de la obra.

www.flujoing.cl / info@flujoing.cl

43

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 20. Registro de terreno puente sobre río Turbio.**

**Fuente: Elaboración propia.**

**Figura 21. Dimensiones y características puente sobre río Turbio.**

**Fuente: Elaboración propia.**

4.2.7. SIMULACIÓN Y POSTPROCESO

Para la aplicación del modelo se realizaron simulaciones de escenarios de caudales

estacionarios durante un tiempo suficiente para lograr un comportamiento estacionario

del flujo hidráulico.

Para las simulaciones se consideró un coeficiente de Courant-Friedrich-Levy (CFL) de

0.45, para condicionar la variación pasos de tiempo para la resolución de las

ecuaciones, buscando evitar inestabilidades en la solución.

www.flujoing.cl / info@flujoing.cl

44

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Se definió un límite seco-mojado para el dominio según las características y objetivos de

cada modelación, correspondiente a la profundidad bajo la cual se pierde relevancia

para los análisis en relación con la magnitud y características de los cauces y los

objetivos del estudio. Para el caso del análisis del río Turbio se definió un límite seco

mojado de 0.15 m, el cual corresponde a un umbral común utilizado para evaluar riesgos

de inundación de ríos, bajo el cual se consideran profundidades no significativas. Por

otro lado, para el caso del análisis de las quebradas, debido a la baja magnitud de los

caudales y altas pendientes, se estableció el límite seco-mojado de 0.01m, el cual

corresponde a la tolerancia mínima del modelo.

Para analizar el comportamiento hidráulico del área de estudio en los distintos

escenarios simulados, se estudiaron los resultados en la interfaz de postproceso de Iber

y exportándolos en formato ráster a una plataforma GIS, enfocándose en las principales

variables hidráulicas de interés.

4.3. ANALISIS DE INUNDACIONES RÍO TURBIO

A partir de los resultados del modelo, se analizó la inundación del escenario T-100 años

para el tramo de estudio del río Turbio. La _Figura 22_ y _Figura 23_ ilustran las condiciones

de profundidad y velocidad, respectivamente, de los flujos resultantes para dicho

escenario.

Como es posible observar, el flujo del río Turbio ante este escenario extraordinario

genera escurrimientos importantes, con profundidades que superan los 4 metros en

zonas de su flujo principal. Dicho escurrimiento genera inundación de zonas aledañas

que superan el metro de profundidad en ciertas áreas, lo cual se produce en la zona

superior y media del tramo de río analizado, ya que hacía aguas abajo se produce un

estrechamiento importante del flujo por las condiciones topográficas.

Es relevante destacar que respecto al puente de la Ruta 41 sobre el río Turbio, el cual se

emplaza en las cercanías del área de proyecto, se da cuenta de que las condiciones

utilizadas para este análisis son conservadoras, ya que dicha obra que por normativa

www.flujoing.cl / info@flujoing.cl

45

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

nacional debe encontrarse diseñada para periodos de retorno inclusive superiores, se

ve sobrepasada por profundidades de agua que superan los 50 cm.

Aun considerando lo anterior, y la cercanía del puente con el área de proyecto, se tiene

que el predio donde se emplaza el Proyecto se encuentra en general a una cota superior,

y solo zonas localizadas y de proporciones muy menores en su límite sur se verían

afectadas por el escenario analizado, con profundidades de entre 15 y 50 cm de agua.

Considerando esto, el proyecto a excluido cualquier tipo de obra o componente del

proyecto de los limites inundables determinados, siendo posible afirmar que este no se

verá en ningún caso afectado por la dinámica fluvial de inundaciones para el periodo

de retorno extraordinario de 100 años.

**Figura 22. Profundidades de flujo inundación T-100 zona Río Turbio.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

46

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 23. Velocidades de flujo inundación T-100 zona Río Turbio.**

**Fuente: Elaboración propia.**

Respecto a las velocidades de los flujos del río Turbio, observan valores en general

superiores a 1 m/s en las zonas principales de escurrimiento del río, que alcanzan valores

superiores a los 7 m/s, principalmente en la zona aguas abajo del tramo analizado,

donde se produce el estrechamiento topográfico del flujo según lo antes indicado.

En la zona media del tramo de estudio, las velocidades son menores, con valores en

general menores a 2 m/s en la zona principal del cauce, mientras que en las zonas de

inundación cercanas al área de proyecto las velocidades son menores a 1 m/s,

correspondiendo a flujos secundarios de inundación con bajo potencial de riesgo y

efectos erosivos.

4.4. ANALISIS DE INUNDACIONES QUEBRADAS

Según se indicó anteriormente, para el caso del estudio hidráulico sobre las quebradas

analizadas, los análisis hidráulicos se separan entre situación Sin Proyecto y Con

www.flujoing.cl / info@flujoing.cl

47

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Proyecto, ya que debido a los resultados del estudio de inundaciones proponen obras

hidráulicas de regularización y defensa sobre estos cauces.

4.4.1. SITUACIÓN SIN PROYECTO

Se analizó la inundación del escenario T-100 años para las quebradas menores

identificadas y su relación con las componentes del proyecto. La Figura 24 y Figura 25

ilustran las condiciones de profundidad y velocidad, respectivamente, de los flujos

resultantes para dicho escenario.

Como es posible observar, los flujos que se producen de las distintas quebradas

corresponden a escurrimientos menores, cuyas profundidades de escurrimiento en

general no superan los 25 centímetros, los cuales, de forma consistente con lo

identificado en terreno, terminan su escurrimiento definido en la Ruta D-369, al poniente

del área de proyecto.

Posteriormente estos flujos se dispersan, inundando el predio de emplazamiento con

escasas profundidades, en general menores a 5 cm, que alcanzan profundidades en un

rango de 5 a 25 cm en zonas principales del escurrimiento.

Respecto a las velocidades, se observan en el trazado de las quebradas altas

velocidades, en general superiores a los 2 m/s, con máximos sobre 5 m/s, representativos

de las condiciones supercríticas que se generan producto de las altas pendientes en esta

zona. Posteriormente, al llegar a la Ruta D-369 y dispersarse en el predio de

emplazamiento del proyecto, estos flujos disminuyen sus velocidades, con máximos en

un rango de 1 a 2 m/s.

De acuerdo con estos resultados, se determina que parte de las componentes del

proyecto se emplazarían dentro de los límites de inundación de estas quebradas para

la crecida con periodo de retorno T-100 años. El proyecto propondrá entonces obras de

regularización y defensa sobre estos cauces naturales para excluir la inundación de los

límites del proyecto, evitando que sus componentes se vean afectados por la crecida

centenaria.

www.flujoing.cl / info@flujoing.cl

48

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 24. Profundidades de flujo inundación T-100 Quebradas situación SP.**

**Fuente: Elaboración propia.**

**Figura 25. Velocidades de flujo inundación T-100 Quebradas situación SP.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

49

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

4.4.2. SITUACIÓN CON PROYECTO

Considerando los resultados del estudio de inundaciones de las quebradas analizadas,

se evaluó la implementación de obras de regularización y defensas fluviales para el

polígono de proyecto, buscando excluir la inundación de esta área, con el fin de evitar

que sus componentes se vean afectadas por la crecida centenaria.

La solución propuesta corresponde al encauzamiento de las 3 quebradas estudiadas por

medio de muros de gaviones, para posteriormente ser conducidas por medio de dos

entubamientos de HDPE de 800 mm, los cuales permitirán su paso por debajo del

polígono de proyecto, siendo luego devueltas por medio de una obra de entrega para

continuar con su escurrimiento natural. Se considera además una obra de defensa fluvial

para la postación proyectada que se encuentra fuera del polígono de proyecto. La

Figura 26 ilustra las obras propuestas, siendo importante considerar que sus detalles de

diseño serán presentados en capítulos posteriores.

**Figura 26. Obras de regularización y defensa proyectadas.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

50

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Para la determinación de las dimensiones requeridas para las obras y la evaluación de

su comportamiento hidráulico se utilizó la misma herramienta de modelación y

condiciones definidas previamente, incorporando la obras de muros de encauzamiento,

defensas, captaciones y entregas sobre la geometría del proyecto, así como los

entubamientos por medio de las herramientas disponibles en Iber. Se realizó un análisis

iterativo con el modelo para determinar las dimensiones de obra requeridas, cumpliendo

con las revanchas mínimas recomendadas en la normativa vigente.

La Figura 27 ilustra los resultados de profundidad para la situación proyectada. Como

es posible observar, las obras permiten excluir adecuadamente la inundación del área

de proyecto, cumpliendo con el objetivo de diseño planteado. La quebrada SC-1 se

encauza de forma efectiva con el muro de encauzamiento N°1, se conduce por el

entubamiento y devuelve al lado oriente del proyecto. Análogamente, las quebradas SC

2 y SC-3 son encauzadas por el muro de encauzamiento N°2, entubadas en conjunto y

entregadas también al lado oriente del proyecto. La Figura 28 ilustra también los

resultados de velocidad para este escenario.

Es importante destacar que, considerando estas variables, se determina que la influencia

hidráulica de las obras del proyecto termina aproximadamente 50 metros aguas abajo

de las obras proyectadas, donde tanto los límites de la inundación, sus profundidades y

velocidades, presentan nuevamente valores similares o sin alteraciones significativas

comparados con los de la situación sin proyecto. Esto permite verifica uno de las

objetivos de las obras propuestas, consistente en devolver los flujos a sus escurrimientos

naturales.

Por otro lado, se tiene que en el perímetro de los muros de encauzamiento las

profundidades de escurrimiento que enfrentan las obras están en un rango de 0.25 a

0.5 metros, con máximos locales en un rango de 0.5 a 1 metros. Lo anterior, considerando

que los muros se proyectan con una altura de 1.5 metros sobre el nivel de terreno natural,

verifica que se mantienen en todo momento revanchas mínimas de 50 cm, según se

verifica con mayor nivel de detalle en el capítulo de diseño de obras, al igual que las

verificaciones de diseño para el resto de las obras proyectadas.

www.flujoing.cl / info@flujoing.cl

51

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 27. Profundidades de flujo inundación T-100 Quebradas situación CP.**

**Fuente: Elaboración propia.**

**Figura 28. Velocidades de flujo inundación T-100 Quebradas situación CP.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

52

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

## 5. MECÁNICA FLUVIAL

Con relación a los estudios complementarios requeridos por la normativa ambiental

vigente para los proyectos que se someten a un Permiso Ambiental Sectorial 157, se

realiza en este capítulo un análisis de mecánica fluvial para los cauces que se someten

a la tramitación de este permiso, los cuales corresponden a las quebradas SC-1, SC-2 y

SC-3.

Los alcances de este análisis son evaluar el arrastre de sedimentos en estos cauces,

identificando y caracterizando los procesos de erosión y depositación, y las alteraciones

en estos procesos que se pueden producir producto de las obras asociadas a este

permiso.

Junto con lo anterior, se evalúa el efecto de socavación en los cauces, donde además

de analizar las posibles alteraciones inducidas por las obras, se busca definir

parámetros de diseño para las fundaciones de las obras proyectadas, garantizando su

estabilidad para el escenario de diseño.

La metodología para este estudio de mecánica fluvial corresponde a modelación de

lecho móvil utilizando el módulo de transporte de sedimentos del software Iber, donde

las condiciones de geometría, malla de cálculo, rugosidades, y en general las

condiciones de simulación hidráulica son análogas a las descritas en el capítulo 4.2. Se

detallan en este capítulo los fundamentos y aspectos metodológicos respectivos al

modelo de transporte de sedimentos del modelo, así como los resultados obtenidos.

5.1. FUNDAMENTOS DE LA MODELACIÓN

De acuerdo con lo indicado por los desarrolladores del modelo (E. Bladé et al, 2014),

en el módulo de transporte de sedimentos de Iber se resuelven las ecuaciones de

transporte por carga de fondo y por carga en suspensión. Teniendo en cuenta ambos

modos de transporte se calcula la evolución de la cota del fondo debido a procesos de

sedimentación y erosión mediante la ecuación de Exner. Se consideran granulometrías

uniformes, incluyendo en las actualizaciones más recientes la posibilidad de incorporar

granulometrías mixtas.

www.flujoing.cl / info@flujoing.cl

53

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

El caudal sólido de fondo se calcula mediante formulaciones empíricas en función de la

tensión de fondo. El módulo de transporte de sedimentos por carga de fondo incluye las

siguientes características:

 - Umbral de movimiento de Shields.

 Formulaciones para caudal sólido de fondo.

 Meyer Peter-Müller con corrección de Wong-Parker (D = 2-30 mm).

 Van Rijn (D = 0,2-2 mm).

 Corrección por pendiente de fondo en inicio del arrastre (tensión crítica en talud).

 Corrección por pendiente de fondo en transporte sólido (magnitud y dirección).

 Separación de tensiones de Einstein por formas de fondo y grano.

 Condiciones de contorno tipo sedimentograma (caudal sólido de fondo variable

en tiempo).

 Condición de cota de fondo no erosionable (puntos fijos).

El transporte en suspensión se calcula resolviendo la ecuación de convección-difusión

promediada en profundidad para la concentración de sedimento, incluyendo un término

de deposición/resuspensión que modela el intercambio de sedimento entre el lecho y la

carga en suspensión. Las principales características de este módulo son:

 Incorporación de transporte por difusión turbulenta.

 Término de deposición/resuspensión.

 Cálculo de la concentración de sedimento en suspensión según las formulaciones

de: Van Rijn, Smith McLean y Ariathurai.

 Cálculo de la velocidad de sedimentación de las partículas según Van Rijn.

 Condición de contorno de concentración de sedimento en suspensión variable en

tiempo

5.2. CONSIDERACIONES METODOLOGICAS

Dentro de las consideraciones metodológicas del modelo, se requiere en primer lugar

caracterizar los sedimentos representativos de los cauces. Para esto se considera

adecuado utilizar una condición de granulometría uniforme, para la cual es necesaria

incorporar el D50 representativo de los sedimentos del área de estudio.

www.flujoing.cl / info@flujoing.cl

54

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Para lo anterior, se analizó la caracterización edafológica de la DIA, donde en

particular se consideró la Calicata N°5, la cual fue caracterizada en los siguientes 3

horizontes:

 0 -35 cm Color 10YR 3/3 pardo oscuro en húmedo. La estructura del suelo es de

bloques subangulares medios y de grado moderado. La consistencia en seco es

ligeramente dura, friable en húmedo y no plástico y no adhesivo en mojado. La

textura es Franco arenosa, con densidad aparente de 1,3 g/cc y humedad

aprovechable de 6% HBSS. Con poros finos escasos. Límite lineal gradual.

Gravas y piedras semi angulosas de 3 a 30 cm que ocupan un 35% del horizonte.

 35-80 cm Color 10YR 5/2 pardo grisáceo en húmedo. Gravas y piedras semi

angulosas de 3 a 25 cm que ocupan un 50% del horizonte con matriz textura

Franca, con densidad aparente de 1,23 g/cc y humedad aprovechable de 6,8%

HBSS. Con horizonte compactado. Límite lineal gradual.

 80-150 cm y + Color 10YR 4/3 pardo grisáceo en húmedo. Capa de gravas y

piedras semi angulosas de 3 a 15 cm que ocupan un 60% del horizonte con matriz

textura franca, con densidad aparente de 1,25 g/cc y humedad aprovechable de

8,2% HBSS.

**Figura 29. Registro de terreno Calicata N°5 Estudio de Suelos.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

55

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Como es posible observar, se tienen en los primeros horizontes materiales granulares,

con dominancia de gravas y arenas y escasa presencia de materiales finos.

Considerando esto, se asume un diámetro representativo de D50=8mm, el cual se

considera conservador para el tipo de sedimentos observados.

En relación con los parámetros de modelación, para la estimación del transporte en

suspensión se utiliza el método de Van Rajn (Van Rajn, 1984), definiendo los

siguientes parámetros:

|Parámetro Valor|Col2|
|---|---|
|Diámetro Sed. Susp.(m)|0.001|
|Porosidad TS|0.4|
|Densidad Relativa TS|2.65|
|Coeficiente de difusión (m2/s)|0.001|
|Schmidt num|0.7|

**Tabla 22. Condiciones método de transporte en suspensión Iber.**

**Fuente: Elaboración propia.**

Por otro lado, en relación con el transporte de fondo, se utiliza el método de Meyer

Peter & Müller con corrección de Wong-Parker (M. Wong, G. Parker, 2006),

apropiado para los sedimentos granulares en estudio. Los parámetros

correspondientes al transporte de fondo se definen en la siguiente tabla.

|Parámetro Valor|Col2|
|---|---|
|D50 (m)|0.008|
|Porosidad TF|0.4|
|Densidad Relativa TF|2.65|
|Ángulo de fricción RF (rad)|0.55|

**Tabla 23. Condiciones método de transporte de fondo Iber.**

**Fuente: Elaboración propia.**

Adicionalmente, dado que no existen antecedentes para asumir condiciones de

entrada de sedimentos en suspensión ni por arrastre de fondo al modelo, se utiliza

por defecto una condición de agua clara, atendiendo a los objetivos del análisis que

es evaluar las tendencias del lecho dentro del área de estudio.

Se establece además la condición que todo el lecho de la geometría en estudio es

erosionable, con excepción de las obras proyectadas.

www.flujoing.cl / info@flujoing.cl

56

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Con respecto a las condiciones de hidrograma analizadas, se tiene en primer lugar

que, al tratarse de cauces efímeros que solo se activan en respuesta a eventos de

precipitación, no es posible hacer un análisis sobre caudales medios mensuales,

acotando el estudio al escenario de crecida de interés de T-100 años. Se asume un

calentamiento hidráulico del modelo, un hidrograma constante según lo definido el

capítulo de análisis hidráulico y un tiempo de modelación suficiente para que la

totalidad del aporte de las microcuencas en su tiempo de concentración pase por el

área de estudio.

5.3. RESULTADOS DE MECANICA FLUVIAL

En primer lugar, se presentan en la Figura 30 los resultados de los efectos de erosión

y depositación para la situación sin proyecto, mientras que en la Figura 31 se presenta

la carga de sedimentos en suspensión para el mismo escenario.

Como es posible observar, los cambios del lecho más relevantes ante el escenario

extraordinario T-100 años se concentran en las zonas superiores de las quebradas y

llegan hasta la zona donde se produce el cambio de pendiente al llegar a la Ruta

D-369. La tendencia es a erosionar las laderas de estas quebradas y depositar en la

zona central de sus trazados, generando un relleno natural de las misma, en

magnitudes mayores a los 50 cm. Lo anterior es consistente con las altas pendientes

presentes en esta zona, otorgándoles una alta dinámica morfológica ante eventos

de crecidas.

En la zona inferior de inundación, posterior a la dispersión del flujo de las

quebradas, los efectos erosivos y de depositación son más acotados producto de la

ralentización del flujo y las bajas profundidades, manteniéndose en general por

debajo de los 5 cm, con máximos locales en un rango de 10 a 25 cm.

En relación con la carga de sedimentos en suspensión, se tienen en general bajas

concentraciones, que superan los 0.10 g/l principalmente en las zonas superiores de

las quebradas. Estos resultados se pueden asociar a la baja magnitud de los

caudales presentes en los cauces analizados.

www.flujoing.cl / info@flujoing.cl

57

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 30. Erosión y depositación T-100 años quebradas situación SP.**

**Fuente: Elaboración propia.**

**Figura 31. Carga de sedimentos suspendidos T-100 años situación SP.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

58

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Por otro lado, la Figura 32 y la Figura 33 muestran los efectos de erosión y depositación,

así como la carga de sedimentos suspendidos, para la situación con proyecto.

Como es posible observar, los principales cambios inducidos por las obras del proyecto

son acotados a la zona donde se modifica el escurrimiento, y se determina que la

influencia de las obras del proyecto sobre la mecánica fluvial deja de ser significativa

aproximadamente 50 metros aguas abajo de las obras proyectadas, donde tanto los

patrones de erosión, depositación y transporte de sedimentos presentan nuevamente

extensiones similares y sin variaciones de magnitud técnicamente significativas para el

tipo de fenómenos analizados.

**Figura 32. Erosión y depositación T-100 años quebradas situación CP.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

59

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 33. Carga de sedimentos suspendidos T-100 años situación CP.**

**Fuente: Elaboración propia.**

Finalmente, considerando que el escenario modelado corresponde a la crecida

centenaria de diseño, se considera que el efecto de socavación a evaluar es equivalente

a la erosión estimada, por lo tanto, la Figura 34 y Figura 35 presentan los valores de

socavación de los cauces para la condición sin proyecto y con proyecto, respectivamente.

Como es posible observar, los efectos más significativos de socavación se presentan en

la zona superior de las quebradas, donde posteriormente en la zona del predio de

proyecto las socavaciones esperadas son inferiores a los 25 cm. Esta situación se

mantiene para la situación con proyecto, donde las principales alteraciones sobre este

proceso están acotadas a las zonas cercanas a las obras, producto de los cambios en

las lamina de inundación y sus variables hidráulicas, donde en general se reduce la

extensión del efecto de socavación. Hacia aguas abajo de la zona de proyecto, fuera

del rango de influencia hidráulica de este, no se presentan alteraciones significativas

sobre la extensión o magnitud de esta variable.

www.flujoing.cl / info@flujoing.cl

60

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 34. Socavación T-100 años quebradas situación SP.**

**Fuente: Elaboración propia.**

**Figura 35. Socavación T-100 años quebradas situación CP.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

61

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

## 6. DISEÑO Y ANÁLISIS DE OBRAS PROPUESTAS

En el presente capitulo se desarrolla lo respectivo al diseño y análisis de obras

hidráulicas propuestas sobre las quebradas naturales analizadas.

Con el fin de excluir la inundación del polígono de proyecto para el escenario T-100

años, se proyectaron obras de encauzamientos y entubamientos para las quebradas

analizadas, además de una obra de defensa para una postación proyectada,

emplazada fuera del polígono de proyecto. Según la normativa ambiental vigente, las

obras de encauzamiento y entubamiento de cauces naturales corresponden a obras de

regularización, las cuales, en conjunto con la obra de defensa fluvial para la postación,

se someten a la presentación de un Permiso Ambiental Sectorial 157.

El emplazamiento de las obras se detalla en los planos anexos del Permiso Ambiental

Sectorial (PAS) 157 y es ilustrado de forma referencial en la Figura 36.

**Figura 36. Planimetría obras de regularización y defensa.**

**Fuente: Elaboración propia.**

www.flujoing.cl / info@flujoing.cl

62

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Es importante destacar que, para todas las obras proyectadas se consideran los criterios

de diseño expuestos en el capítulo 3.700 de Diseño del Drenaje, Saneamiento, Mecánica

e Hidráulica fluvial del Manual de Carreteras Volumen N°3. De igual forma, se

consideraron los planos de obras tipo expuestos en el capítulo 4.100 de Drenaje y

Proyección de la Plataforma del Manual de Carreteras Volumen N°4.

6.1. MUROS DE ENCAUZAMIENTO

Para el encauzamiento de las quebradas se considera una solución de muros de

gaviones que permitirán evitar el ingreso de la lámina de inundación hacia el interior

del polígono de proyecto y redirigirla hacia la obra de captación del entubamiento.

Los gaviones corresponden a elementos con forma de paralelepípedo rectangular,

fabricados con malla hexagonal de alambre en acero galvanizado, revestidos con

materiales plásticos y que se rellenan con piedras, usualmente de origen fluvial. Estos

elementos se emplean para conformar estructuras, normalmente muros, que se utilizan

para la protección fluvial, y permiten construir obras de defensa flexibles, resistentes y

permeables. Los muros de gaviones corresponden a una solución ampliamente utilizada

para la protección de inundaciones.

Para el diseño de estas obras se siguen los criterios de diseños expuestos en el acápite

3.708 del MC V-3, en el cual se describen las principales consideraciones y criterios para

el dimensionamiento geométrico de muros de gaviones, los cuales se exponen a

continuación.

6.1.1. LOCALIZACIÓN EN PLANTA

La localización en planta de la obra dependerá principalmente del objetivo que esta

persiga. En el caso de estudio, se desea proteger de la inundación del escenario de

diseño una zona específica y encauzar las quebradas, por lo cual los muros se proyectan

en forma perimetral al proyecto, considerando alas en los extremos de los muros y en la

unión de estos para permitir el encauzamiento de los flujos y la separación del

escurrimiento de la quebrada SC-1 de las quebradas SC-2 y SC-3. El emplazamiento de

la obra se detalla en los planos anexos del PAS 157 y en la figura previamente

presentada.

www.flujoing.cl / info@flujoing.cl

63

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

6.1.2. SECCIÓN TRANSVERSAL

Respecto a la sección transversal del diseño, se tiene que, dependiendo de los elementos

de composición de la obra, es necesario definir condiciones tales como inclinación de

taludes, cortes, rellenos, entre otros.

En el caso de estudio la estructura propuesta corresponde a un muro de gaviones auto

soportado, que no se emplaza en un talud natural ni considera obra de pretil de

respaldo. El diseño contempla transversalmente dos elementos de gaviones de base (2

metros de ancho total) y un elemento superior, otorgando una altura de 1.5 metros sobre

el nivel de terreno. El diseño transversal de la obra se representa en la Figura 37.

**Figura 37. Diseño transversal defensa fluvial de muro de gaviones.**

**Fuente: Elaboración propia.**

6.1.3. CORONAMIENTO

Los principales parámetros que definen el coronamiento son su cota y su ancho. El

acápite 3.708.302(3) del M.C. V.3, indica que la cota de coronamiento dependerá de

la función y objetivo que cumpla la obra.

En el caso de la obra proyectada, la altura del coronamiento se diseña en función del

nivel de inundación. El nivel de inundación se define a partir de los antecedentes de la

modelación hidráulica en Situación Con Proyecto, detallada en el acápite respectivo,

donde en el tramo más desfavorable se alturas máximas en un rango de 0.5 a 1 metro

en los límites de los muros proyectados. Se considera una revancha de 50 cm sobre el

www.flujoing.cl / info@flujoing.cl

64

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

nivel máximo de aguas, según lo definido como revancha mínima en la lámina 4.501.001

del MC V-4.

Se define entonces una altura de coronamiento de 1.5 metros sobre el nivel de terreno

proyectado, especificando el coronamiento de la obra en los perfiles longitudinales de

diseño presentados en los planos anexos del Permiso Ambiental Sectorial (PAS) 157 de

esta presentación.

6.1.4. CORAZA DE PROTECCIÓN

Para el caso de estudio como ya se mencionó se proyectan defensas longitudinales

utilizando gaviones, correspondiendo este mismo elemento a la composición externa o

coraza de la obra.

La utilización de este tipo de elementos en el diseño de obras no requiere mayores

análisis de composición de los elementos, sin embargo, es necesario indicar que las

obras proyectadas deberán cumplir con las especificaciones técnicas definidas en el

capítulo 5.207.202 del MC V-5, con respecto a la malla de alambre utilizada, alambre

de aristas, amarre y para tirantes, así como se recubrimiento y ensayos de control de

calidad y certificación. Para el relleno de los gaviones se deberán utilizar piedras

naturales de canto rodado o canto vivo.

En los planos del proyecto se presentan las especificaciones técnicas de la construcción

del muro de gaviones, de forma consistente con lo especificado en el MC V-5.

6.1.5. ANALISIS DE SOCAVACIÓN Y FUNDACIONES.

La fundación de una obra de muro de gaviones queda definida por el nivel de la

socavación estimada para el lecho, para lo cual debe considerarse el valor más

desfavorable para el tramo de proyecto

Para la determinación de la profundidad de fundación se realiza un análisis de

socavación considerando los resultados del estudio de mecánica fluvial presentado

previamente.

A partir de dicho análisis fue posible determinar las profundidades de erosión o

socavación para el escenario de diseño T-100 años, en la zona de emplazamiento de

las obras. La Figura 38 ilustra estos resultados.

www.flujoing.cl / info@flujoing.cl

65

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 38. Socavación en la zona de obras del proyecto.**

**Fuente: Elaboración propia.**

Como es posible observar, en general la socavación en la zona del muro de

encauzamiento varía entre 0.05 a 0.25 m, con máximos locales en un rango de 0.25 a

0.5 m. Por lo tanto, se considera para el diseño una fundación de 0.5 metros, de acuerdo

con lo recomendado en el MC-V4.

6.2. ENTUBAMIENTO DE LAS QUEBRADAS

Para conducir el escurrimiento de las quebradas sin afectar las componentes del

proyecto se ha propuesto una solución de entubamiento por medio de tuberías de HDPE

estructuradas. Dichos entubamientos permitirán la conducción a flujo libre de los flujos

encauzados, por debajo del nivel de terreno, diseñándose para el escenario T-100 años.

Se proponen dos entubamientos con sus respectivas obras de captación y entrega. El

primero considera un caudal de diseño de 1.76 m [3] /s, correspondiente al caudal detrítico

de la quebrada SC-1. El segundo se diseña para un caudal de 1.88 m [3] /s, correspondiente

a la sumatoria de los caudales detríticos de las quebradas SC-2 y SC-3.

www.flujoing.cl / info@flujoing.cl

66

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

A continuación, se detallan las distintas componentes de estas obras.

6.2.1. CAPTACIONES ENTUBAMIENTO

Para captar los flujos encauzados se propone una obra de captación con caída,

revestida con mampostería en piedra, y un muro boca de hormigón en la entrada del

entubamiento.

Estas obras permitirán profundizar el flujo para llegar al nivel del entubamiento que

pasará por debajo del nivel de terreno.

Los detalles constructivos de estas obras se detallan en los planos anexos del PAS 157,

indicando que deben cumplir con las especificaciones técnicas de los respectivos

acápites del MC-V5.

Es importante destacar que el revestimiento en mampostería de piedra propuesto es

adecuado para las velocidades estimadas en el estudio hidráulico, al mismo tiempo que

consideran un sello de fundación de 0.6 metros, el cual es conservador de acuerdo con

los valores de socavación estimados previamente. De igual forma su efectividad para la

captación es verificada mediante la modelación hidráulica de la situación con proyecto.

**Figura 39. Diseño obra de captación entubamientos.**

**Fuente: Elaboración propia.**

6.2.2. ENTUBAMIENTO

Para el diseño de las tuberías se ha considerado una solución de HDPE estructurado

(corrugado), ampliamente utilizado para obras de drenaje. Para la determinación del

diámetro de diseño se consideran los caudales detríticos para el escenario T-100 años,

www.flujoing.cl / info@flujoing.cl

67

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

en conjunto con el diseño geométrico de la rasante del proyecto en concordancia al

levantamiento topográfico.

A partir de esto, se definieron para ambos entubamientos un diámetro de diseño de 800

milímetros, cuyas condiciones hidráulicas de diseño se obtienen utilizando el software

HCanales, que permite determinar las características hidráulicas y geométricas del

entubamiento basándose en la fórmula de Manning.

**Figura 40. Condiciones de diseño Entubamiento N°1.**

**Fuente: Elaboración propia, HCanales.**

**Figura 41. Condiciones de diseño Entubamiento N°2.**

**Fuente: Elaboración propia, HCanales.**

www.flujoing.cl / info@flujoing.cl

68

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

Como es posible observar en ambos casos se tiene una revancha superior al 50% del

diámetro de la tubería, muy superiores a las solicitadas en las recomendaciones de

diseño de las guías vigentes.

Por otro lado, el comportamiento adecuado de estos entubamientos fue verificado ante

condiciones no uniformes mediante la modelación hidráulica bidimensional de la

situación con proyecto, de acuerdo con lo presentado en el capítulo respectivo,

demostrando su efectividad para conducir los flujos de las quebradas hasta la obra de

entrega en el extremo oriente del perímetro del proyecto.

Finalmente, los detalles de instalación de los entubamientos se entregan en los planos

del proyecto, considerando cama de apoyo, un relleno estructurante y un recubrimiento

mínimo que permitirán proteger la obra adecuadamente de las actividades en la

superficie del terreno.

6.2.3. ENTREGAS ENTUBAMIENTO

De forma análoga a las obras de captación, se proponen obras de entrega revestidas

con mampostería en piedra, y un muro boca de hormigón en la salida del entubamiento.

Estas obras se extenderán con una pendiente mínima hasta intersecar con el nivel natural

del terreno, devolviendo de esta forma los escurrimientos encauzados a la superficie del

terreno para continuar con su flujo natural.

Los detalles constructivos de estas obras se detallan en los planos anexos del PAS 157,

indicando que deben cumplir con las especificaciones técnicas de los respectivos

acápites del MC-V5.

Es importante destacar que el revestimiento en mampostería de piedra propuesto es

adecuado para las velocidades estimadas en el estudio hidráulico, al mismo tiempo que

consideran un sello de fundación de 0.6 metros, el cual es conservador de acuerdo con

los valores de socavación estimados previamente. De igual forma la efectividad de la

obra de entrega fue verificada mediante la modelación hidráulica de la situación con

proyecto.

www.flujoing.cl / info@flujoing.cl

69

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 42. Diseño obra de entrega entubamientos.**

**Fuente: Elaboración propia.**

6.3. OBRA DE DEFENSA POSTACIÓN

Para la obra de postación emplazada fuera del polígono del proyecto se propone una

obra de defensa con mampostería de piedra que permitirá excluir la inundación,

dejando un polígono protegido para la instalación de la postación y sus obras.

Según los resultados de la modelación hidráulica para la situación con proyecto la

lámina de inundación en esta zona es mínima, inferior a los 10 cm. Se propone entonces

una altura de 0.5 m sobre el nivel de terreno, dejando una revancha de 40 cm para el

escenario de diseño T-100 años.

Por otro lado, de acuerdo con los resultados de socavación para el escenario de diseño,

se tienen en la zona de emplazamiento de la obra de defensa socavaciones que no

superan los 10 cm de profundidad, por lo tanto, de forma conservadora, se propone una

fundación de 50 cm.

Los detalles constructivos de estas obras se detallan en los planos anexos del PAS 157,

indicando que deben cumplir con las especificaciones técnicas de los respectivos

acápites del MC-V5.

www.flujoing.cl / info@flujoing.cl

70

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

**Figura 43. Diseño obra de defensa postación.**

**Fuente: Elaboración propia.**

## 7. CONCLUSIÓN

En el presente informe se describieron los antecedentes, metodologías y resultados del

estudio de inundaciones realizado para el proyecto Línea de Transmisión y Central BESS

Halcón 13, detallando los análisis hidrológicos e hidráulicos que se desarrollaron para

este estudio.

Conforme a lo establecido en la caracterización hidrológica del proyecto, se identificó

la presencia del río Turbio aproximadamente a 50 metros al sur del área de proyecto y

tres quebradas naturales menores de características efímeras cuyos trazados terminan

en la Ruta D-369 al poniente del área de proyecto.

Se determinaron las respectivas cuencas aportantes para estos cauces, delimitando para

el río Turbio un área aportante al tramo de estudio de 4111.81 km [2], mientras que para las

quebradas identificadas se obtuvieron áreas oscilan entre 0.11 km [2] y 0.21 km [2], pudiendo

considerárseles cuencas de pequeña superficie o microcuencas. Se determinaron para

www.flujoing.cl / info@flujoing.cl

71

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

cada cuenca sus parámetros morfométricos y se definieron sus tiempos de concentración

asociados. Se realizó también un análisis de precipitaciones, determinando las

precipitaciones máximas asociadas a los distintos periodos de retorno, junto con las

curvas de Intensidad-Duración-Frecuencia (IDF) características del área de estudio.

Para la determinación de los caudales máximos instantáneos del río Turbio en el tramo

de estudio se consideraron representativos los datos fluviométricos de la estación Río

Turbio en Varillar. Sobre dichos datos se realizó un análisis de frecuencia, obteniendo

un caudal máximo instantáneo de 152.09 m [3] /s para el periodo de retorno de 100 años.

Para las quebradas identificadas se utilizó el Método Racional, obteniendo caudales

máximos que oscilan entre los 0.66 y 1.23 m [3] /s para el periodo de retorno de 100 años.

Producto de sus características, para dichos cauces se estimó también el aumento

volumétrico producto del arrastre y concentración de sedimentos (flujos detríticos),

obteniendo caudales máximos entre 0.94 y 1.76 m [3] /s, los cuales fueron utilizados para

sus modelaciones hidráulicas.

Se desarrollaron modelaciones hidráulicas bidimensionales en el modelo Iber,

obteniendo las principales variables hidráulicas de interés para los flujos modelados,

correspondientes a las condiciones de profundidad y velocidad para el periodo de

retorno T-100 años.

Para el análisis del tramo del río Turbio se identificó que este escenario extraordinario

genera escurrimientos importantes, obteniendo con la metodología utilizada resultados

conservadores. El predio donde se emplaza el Proyecto se encuentra en general a una

cota superior, y solo zonas localizadas y de proporciones menores en su límite sur se

verían inundadas por el escenario analizado, con profundidades de entre 15 y 50 cm de

agua. El proyecto a excluido cualquier tipo de obra o componente del proyecto de los

limites inundables determinados, siendo posible afirmar que este no se verá en ningún

caso afectado por la dinámica fluvial de inundaciones para el periodo de retorno

extraordinario de 100 años.

Respecto al análisis hidráulico de las quebradas identificadas, los flujos que se producen

en las distintas quebradas corresponden a escurrimientos menores para el escenario

www.flujoing.cl / info@flujoing.cl

72

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

extraordinario T-100 años analizado, cuyas profundidades son en general menores a 25

cm, lo cual es consistente con sus bajos caudales. De forma consistente con lo

identificado en terreno, estas quebradas terminan su escurrimiento por sección definida

en la Ruta D-369, al poniente del área de proyecto. Posteriormente estos flujos se

dispersan, inundando el predio de emplazamiento con escasas profundidades, en

general menores a 5 cm, que alcanzan profundidades en un rango de 5 a 25 cm en

zonas principales del escurrimiento.

Con el fin de excluir la inundación del área de proyecto se evaluó la implementación de

obras de regularización y defensas fluviales para el polígono de proyecto, con el fin de

evitar que sus componentes se vean afectadas por la crecida centenaria. La solución

propuesta corresponde al encauzamiento de las 3 quebradas estudiadas por medio de

muros de gaviones, para posteriormente ser conducidas por medio de dos

entubamientos, permitiendo su paso por debajo del polígono de proyecto.

Se desarrolló el diseño y verificación hidráulica de la efectividad de estas obras, se

entregaron sus detalles y memorias de diseño, y se desarrollaron los estudios

complementarios para evaluar la influencia de las obras proyectadas sobre los cauces

en los cuales se emplazan, en concordancia a los contenidos técnicos solicitados en la

Guía Trámite PAS Artículo 157 Reglamento del SEIA.

Finalmente, se tiene que, con la implementación de las obras de regularización y

defensas fluviales proyectadas, las componentes del proyecto se emplazarán fuera de

las zonas inundables de las quebradas analizadas para el periodo de retorno de 100

años. No existen otras componentes del proyecto ni obras requeridas que intervengan

los cauces analizados, por lo tanto, corresponde únicamente la tramitación del Permiso

Ambiental Sectorial 157 respectivo a las obras sobre las quebradas SC-1, SC-2 y SC-3.

www.flujoing.cl / info@flujoing.cl

73

| ESTUDIO DE INUNDACIONES BESS HALCÓN 13

## 8. BIBLIOGRAFÍA

DGA-MOP. (2016). _Guías Metodológicas para Presentación y Revisión Técnica de_

_Proyectos de Modificación de Cauces Naturales y Artificiales._ Santiago, Chile:

Departamento de administración de recursos hídricos.

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

www.flujoing.cl / info@flujoing.cl

74

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 8.: Coeficientes de duración estación Rivadavia.****

| Duración<br>(min) | Intenisidad (mm/h) para distintos Tr | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Duración<br>(min) | 2 | 5 | 10 | 25 | 50 | 100 |
| 60 | 3.42 | 5.62 | 7.12 | 9.02 | 10.46 | 11.90 |
| 120 | 2.99 | 4.92 | 6.23 | 7.90 | 9.15 | 10.42 |
| 240 | 2.49 | 4.10 | 5.19 | 6.58 | 7.63 | 8.68 |
| 360 | 2.28 | 3.75 | 4.74 | 6.02 | 6.97 | 7.94 |
| 480 | 2.10 | 3.46 | 4.37 | 5.55 | 6.43 | 7.32 |
| 600 | 1.94 | 3.19 | 4.03 | 5.11 | 5.93 | 6.75 |
| 720 | 1.78 | 2.93 | 3.71 | 4.70 | 5.45 | 6.20 |
| 840 | 1.59 | 2.61 | 3.30 | 4.19 | 4.86 | 5.53 |
| 1080 | 1.38 | 2.26 | 2.87 | 3.63 | 4.21 | 4.79 |
| 1440 | 1.19 | 1.95 | 2.47 | 3.13 | 3.63 | 4.13 |
