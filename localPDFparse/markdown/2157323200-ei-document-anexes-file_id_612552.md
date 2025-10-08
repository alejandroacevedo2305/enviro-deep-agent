---
title: Sin título
author: Sebastián Carreño Gómez;Graciela Núñez
date: D:20221018125517-03'00'
language: es
type: manual
pages: 32
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. INTRODUCCIÓN
  - 2. OBJETIVOS
  - 3. ÁREA DE INFLUENCIA
  - 4. METODOLOGÍA
  - 5. RESULTADOS
  - 6. CONCLUSIONES
  - 7. REFERENCIAS BIBLIOGRÁFICAS
  - 8. PROFESIONALES
  - 9. APENDICES
-->



DECLARACIÓN DE IMPACTO AMBIENTAL

**PROYECTO SANTA GRACIELA SOLAR**

**ANEXO 2.4**

**CARACTERIZACIÓN DE INUNDACIÓN**

**OCTUBRE 2022**

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**ÍNDICE** **DE** **CONTENIDOS**

**1.** **CONTENIDO**

1. INTRODUCCIÓN ........................................................................................................................... 4

2. OBJETIVOS ................................................................................................................................... 5

3. ÁREA DE INFLUENCIA .................................................................................................................. 6

4. METODOLOGÍA ............................................................................................................................ 7

4.1 Método de Cálculo HEC-RAS ............................................................................................... 7

4.2 Caudales de Máxima Crecida .............................................................................................. 9

4.3 Topografía ......................................................................................................................... 10

4.4 Valor de Manning Según Método de Cowan .................................................................... 12

5. RESULTADOS ............................................................................................................................. 16

5.1 Estero Meco PC1 ............................................................................................................... 17

5.2 Estero Maule PC2 .............................................................................................................. 24

6. CONCLUSIONES ......................................................................................................................... 30

7. REFERENCIAS BIBLIOGRÁFICAS ................................................................................................. 32

8. PROFESIONALES ........................................................................................................................ 32

9. APENDICES ................................................................................................................................ 32

**ÍNDICE** **DE** **TABLAS**

Tabla 1 Caudales de Crecida en Puntos de Control Proyecto Santa Graciela Solar .......................... 10
Tabla 2 Condiciones de Borde en Esteros para HEC-RAS Proyecto Santa Graciela Solar ................. 10
Tabla 3 Coeficiente De Rugosidad Manning Según Cowan en Esteros Proyecto Santa Graciela Solar

........................................................................................................................................................... 15

Tabla 4 Resultados Parámetros Hidráulicos TR100 años Estero Meco Proyecto Santa Graciela Solar

........................................................................................................................................................... 18

Tabla 5 Resultados Parámetros Hidráulicos TR100 años Estero Maule Proyecto Santa Graciela Solar

........................................................................................................................................................... 25

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

2

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**ÍNDICE** **DE** **FIGURAS**

Figura 1.1 Ubicación Proyecto Santa Graciela Solar ........................................................................... 5
Figura 3.1 Área de Influencia de Inundación Proyecto Santa Graciela Solar ...................................... 6

............................................................................................................................................................. 6

Figura 4.1 Puntos de Control Proyecto Santa Graciela Solar .............................................................. 9
Tabla 2 Condiciones de Borde en Esteros para HEC-RAS Proyecto Santa Graciela Solar ................. 10
Figura 4.2 Topografía de los Esteros Proyecto Santa Graciela Solar ................................................ 11
Figura 4.3 Fotografía Detalle Estero Meco Proyecto Santa Graciela Solar ....................................... 12

........................................................................................................................................................... 12

Figura 4.4 Fotografía Aérea de Esteros Meco Parque Fotovoltaico Santa Graciela Solar ................ 13
Figura 4.5 Fotografía Aérea de Esteros Maule Parque Fotovoltaico Santa Graciela Solar ............... 13
Tabla 3 Coeficiente De Rugosidad Manning Según Cowan en Esteros Proyecto Santa Graciela Solar

........................................................................................................................................................... 15

Figura 5.1 Perfiles e Inundación TR100 HEC-RAS Quebrada PC1 Estero Meco Proyecto Santa Graciela

Solar ................................................................................................................................................... 17

Tabla 4 Resultados Parámetros Hidráulicos TR100 años Estero Meco Proyecto Santa Graciela Solar

........................................................................................................................................................... 18

Figura 5.2 Resultados de Profundidades TR100 HEC-RAS Quebrada PC1 Estero Meco Proyecto Santa

Graciela Solar .................................................................................................................................... 21

Figura 5.3 Resultados de Velocidades TR100 HEC-RAS Quebrada PC1 Estero Meco Proyecto Santa

Graciela Solar .................................................................................................................................... 22

Figura 5.4 Resultados de Elevación de Superficie de Inundación en TR100 HEC-RAS Quebrada PC1
Estero Meco Proyecto Santa Graciela Solar ...................................................................................... 23
Figura 5.5 Perfiles e Inundación TR100 HEC-RAS Quebrada PC2 Estero Maule Proyecto Santa Graciela

Solar ................................................................................................................................................... 24

Tabla 5 Resultados Parámetros Hidráulicos TR100 años Estero Maule Proyecto Santa Graciela Solar

........................................................................................................................................................... 25

Figura 5.6 Resultados de Profundidades TR100 HEC-RAS Quebrada PC2 Estero Maule Proyecto Santa

Graciela Solar .................................................................................................................................... 27

Figura 5.7 Resultados de Velocidades TR100 HEC-RAS Quebrada PC2 Estero Maule Proyecto Santa

Graciela Solar .................................................................................................................................... 28

Figura 5.8 Resultados de Elevación de Superficie de Inundación en TR100 HEC-RAS Quebrada PC2
Estero Maule Proyecto Santa Graciela Solar ..................................................................................... 29
Figura 6.1 Resultados de Modelo Hidráulico TR100 años y Emplazamiento DIA Santa Graciela Solar

........................................................................................................................................................... 31

........................................................................................................................................................... 31

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

3

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

# 1. INTRODUCCIÓN

El presente documento se enmarca en caracterizar la inundación de crecida centenaria de dos (2)
esteros en posible interacción con las partes y obras del proyecto de nombre Santa Graciela Solar
en adelante el Proyecto, a modo de caracterizar hidráulicamente estos cauces naturales para la
evaluación del Proyecto en el SEIA. Dicho Proyecto se emplaza en un entorno rural, específicamente
en la comuna de San Ignacio, Provincia de Diguillin, Región de Ñuble.

El Proyecto consiste en la construcción y posterior operación de un parque solar fotovoltaico
enmarcado dentro de las Energías Renovables No Convencionales (ERNC) destinado a la generación
de energía eléctrica, a partir de la tecnología solar fotovoltaica,, emplazado en una superficie de
aproximadamente de 109,17 hectáreas, con una Línea de Alta Tensión (LAT) de 2,99 km de longitud,
por lo que, en adelante el área de estudio comprenderá el área del Proyecto que contiene todas sus
partes y obras.

Conforme a lo dispuesto, se infiere que el emplazamiento de las partes y obras del Proyecto pueden
tener interacción con dos (2) cauces naturales identificadas en la cartografía 1:50.000 de nombre El
Carmen (F-109) del Instituto Geográfico Militar (IGM). Es por ello por lo que, en primer lugar, se
caracteriza la componente hidrológica en el Anexo 3.5 donde se estimaron caudales de crecidas en
los dos esteros identificados como Estero Meco y Estero Maule con puntos de control ubicados en
el sector más cercano al Proyecto, en segundo el presente documento comprende contener la
memoria de cálculo hidráulica de las áreas susceptible a inundación con caudales de TR100 años
mediante modelación computacional hidráulica en el software HEC-RAS.

En base a lo anterior y en específico, el presente estudio se basará en un levantamiento topográfico
de tipo LIDAR entregado por el titular del área de estudio con curvas de nivel cada 0,5 metros en el
área de estudio el cual se incluye dentro del Apéndice A del presente documento, conforme lo
establece la Dirección General de Aguas (DGA) en su Resolución N°135 del 30 de enero del año 2020,
guías de Permisos Ambientales Sectoriales Mixto 156 y 157, y su Guías Metodológicas para
Proyectos de Modificación de Cauces.

A continuación, se presenta una figura que demuestra la ubicación del Proyecto y los cauces a

estudiar.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

4

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 1.1 Ubicación Proyecto Santa Graciela Solar**

Fuente: Elaboración Propia, MODELING 2022.

# 2. OBJETIVOS

El principal objetivo es determinar las áreas de inundación dentro del área de influencia para un
caudal con periodo de retorno de 100 años estimados en los dos esteros en posible interacción con
el área del Proyecto, Estero Meco y Estero Maule.

Como objetivo secundario se determina realizar una modelación hidráulica mediante el software

HEC-RAS 5.0.7. en base a la estimación de caudales de crecida mostrada en el Anexo 3.5 de los

esteros, la topografía entregada por el titular, incluida en el Apéndice A, y la caracterización de
estratos y coberturas de los esteros realizada en terreno en la visita realizada el día 15 de enero del

año 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

5

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

# 3. ÁREA DE INFLUENCIA

El Proyecto se emplazará en la Región de Ñuble, en la Provincia de Diguillín, Comuna de San Ignacio,
a aproximadamente a 4,5 km al norte de la localidad de San Ignacio y 25 km al sur de la capital
regional de Chillán, su superficie comprenderá aproximadamente 109,17 ha, la zona de ingreso y
egreso al Proyecto es por medio de la Ruta N-605 y N-639.

A continuación, se demuestra el área de Proyecto junto al área de influencia de inundación en los
esteros en estudio, dicha área comprende 400 metros en el transversal de los cauces y desde 150
metros aguas arriba y aguas debajo del área del Proyecto.

**Figura 3.1 Área de Influencia de Inundación Proyecto Santa Graciela Solar**

Fuente: Elaboración Propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

6

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

# 4. METODOLOGÍA

A continuación, se representan la metodología de la presente memoria de cálculo, la cual se basa
en el uso del Software de Modelación Hidráulica HEC-RAS y los antecedentes necesarios para
efectuar dicho modelo computacional.

## 4.1 Método de Cálculo HEC-RAS

Este modelo, opera tanto con flujo supercrítico como subcrítico (mixto). El algoritmo numérico se
basa en la solución de la ecuación de energía y momento, en forma unidimensional; con pérdidas
de energía debidas a la fricción, calculadas mediante la ecuación de Manning, y singularidades
originadas por cambios de sección.

Los principios de cálculo utilizados por este programa son los siguientes:

 - Caudales de máximas crecidas

 - Geometría del cauce

 - Pendiente media

 - Secciones transversales

 - Coeficiente de rugosidad de Manning

Aplicando la Fórmula de Manning:

QQ= ~~[√]~~ [ii]

nn [∗Ω∗ RR]

22
33 **en** [m [3] /s]

Es decir,

QQ∗nn

~~√~~ ii

Ecuación de Balance de Energía

= Ω∗RR

22
33

El escurrimiento gradualmente variado se evalúa mediante la ecuación de balance de energía, es

decir:

B = B + P [[m] ]
11

Donde:

 - B1 = Nivel de energía en la sección aguas arriba

 - B2 = Nivel de energía en la sección aguas abajo

 - P = Pérdidas de carga friccionales y singulares por cambios de sección

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

7

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

Pérdidas Friccionales

Las pérdidas de carga friccionales corresponden a la siguiente relación:

Ω ff = JJ∗LL [m]

Donde:

 - L = Distancia entre las secciones 1 y 2

 - J = Pérdida de carga unitaria obtenida de la expresión de Manning

Pérdidas Singulares

Los cambios de sección generan pérdidas singulares que quedan determinadas por la siguiente

relación:

Ω ss = CC∗ ൬ VV 22e **e** 1 e **1** −VV,66 22s **s** s ൰ m

Donde:

 - Vent = Velocidad en la sección aguas arriba

 - Vsal = Velocidad en la sección aguas abajo.

 - C = Coeficiente. C es igual a 0,1 para contracción y 0,3 para expansión.

**e** **s**

**1**

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

**e** **s**

**1**

8

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

## 4.2 Caudales de Máxima Crecida

En primer lugar, es importante mencionar que el presente documento se encuentra basado en la
caracterización hidrológica mostrada en el Anexo 3.5, en la cual en primer lugar se identifican los
puntos de control respectivos en cada estero para estimar los caudales de crecida. Dichos puntos
de control fueron identificados como punto de control PC1 para Estero Meco y punto de control
PC2 como Estero Maule. A continuación, se incluye una figura que identifica los puntos de control
de los esteros, su red hidrográfica y sus cuencas aportantes.

**Figura 4.1 Puntos de Control Proyecto Santa Graciela Solar**

Fuente: Elaboración Propia, MODELING 2022.

De la caracterización hidrológica y estimación de caudales de crecida por cada punto de control se
desprenden los siguientes resultados los cuales se justifican del Anexo 3.5, dichos caudales fueron
estimados en periodos de retorno de 2, 5, 10, 20, 25, 50 y 100 años los cuales serán considerados
en las modelaciones hidráulicas computacionales para comprender de mejor manera el
comportamiento del flujo en una crecida de carácter centenaria, pero se mostraran los resultados
en el presente documento del resultado de la modelación para un periodo de retorno de 100 años.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

9

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Tabla 1 Caudales de Crecida en Puntos de Control Proyecto Santa Graciela Solar**

|PUNTO DE CONTROL|CAUDALES (T años) EN m3/s|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|PUNTO DE CONTROL<br>|~~2 ~~<br>|~~5 ~~<br>|~~10~~<br>|~~20~~<br>|~~25~~<br>|~~50~~<br>|~~100~~<br>|
|~~PC1 Estero Meco~~<br>|~~32.20~~<br>|~~49.69~~<br>|~~57.46~~<br>|~~70.78~~<br>|~~74.59~~<br>|~~86.06~~<br>|~~97.72~~<br>|
|~~PC2 Estero Maule~~<br>|~~5.20~~<br>|~~7.12~~<br>|~~8.50~~<br>|~~10.91~~<br>|~~11.43~~<br>|~~14.28~~<br>|~~16.89~~|

Fuente: Elaboración Propia en base a Anexo 3.5, MODELING 2022.

## 4.3 Topografía

En segundo lugar, la presente modelación computacional de carácter hidráulica HEC-RAS está
basada en una topografía de carácter LIDAR del área de influencia entregada por el titular, la cual
presenta curvas de nivel cada 0,5 metros y se adjunta en el Apéndice A. Dicha información
topográfica permitirá representar la geomorfología de terreno de los esteros en estudio y a su vez
identificar parámetros físicos necesarios para la modelación HEC-RAS como lo son las condiciones

de bordes.

Las condiciones de bordes a utilizar serán las de “Normal Depth” o más conocido como la pendiente
del fondo del cauce, esta fue estimadas mediante el software HEC-RAS y comprobadas en QGIS las
cuales se presentan en el siguiente cuadro.

**Tabla 2 Condiciones de Borde en Esteros para HEC-RAS Proyecto Santa Graciela Solar**

|QUEBRADA O CAUCE|PENDIENTE (M/M)|Col3|
|---|---|---|
|**QUEBRADA O CAUCE**<br>|~~**DOWNSTREAM**~~<br>|~~**UPSTREAM 1**~~<br>|
|~~PC1 Estero Meco ~~<br>|~~0.0075~~<br>|~~0.0075~~<br>|
|~~PC2 Estero Maule ~~<br>|~~0.0065~~<br>|~~0.0065~~<br>|

Fuente: Elaboración Propia en base a topografía y QGIS, MODELING 2022.

En general a nivel de pendientes los esteros demuestran bastante heterogeneidad en su trayectoria
por lo que fue considerada la misma pendiente aguas arriba tanto como aguas abajo a modo de
generar el peor escenario posible, a su vez se colige que los esteros presentan bajas pendientes
inferiores al 1% según lo calculado mediante SIG por lo que está dentro de los alcances del programa

HEC-RAS en una dimensión.

Es importante destacar que en la visita a terreno efectuada el día 15 de enero 2022 no se encontró
presencia de escurrimiento superficial contundente en los esteros y si se presenta alta vegetación
en el área de influencia, por lo que, no fue necesario un levantamiento topo batimétrico.

A continuación, se representa una figura que demuestra la información topográfica de los esteros,
de la cual dentro del software HEC-RAS se realizara el cálculo de perfiles transversales espaciados
cada 20 metros en cada estero los cuales representaran las secciones transversales a modelar. En el
capítulo resultados se entregarán los parámetros hidráulicos resultantes de la modelación por cada
perfil transversal entregado por el software con la identificación de cada uno de ellos con TR100.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

10

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 4.2 Topografía de los Esteros Proyecto Santa Graciela Solar**

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

11

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

## 4.4 Valor de Manning Según Método de Cowan

A modo de valorizar el coeficiente de Manning según Cowan se efectúa la visita a terreno el día 15
de enero 2022, en la cual se recorre el área de los esteros y se sobrevuela la misma área mediante
un Drone modelo DJI Phantom 4 v2, a continuación, se demuestra un registro de fotografías aéreas
de los esteros junto a una figura de detalle.

**Figura 4.3 Fotografía Detalle Estero Meco Proyecto Santa Graciela Solar**

Fuente: Elaboración propia en base a visita a terreno, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

12

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 4.4 Fotografía Aérea de Esteros Meco Parque Fotovoltaico Santa Graciela Solar**

Fuente: Elaboración propia en base a visita a terreno, MODELING 2022.

**Figura 4.5 Fotografía Aérea de Esteros Maule Parque Fotovoltaico Santa Graciela Solar**

Fuente: Elaboración propia en base a visita a terreno, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

13

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

Los valores de Manning representan la rugosidad de los cauces a modelar, para la correcta

modelación se determinan estos valores mediante el método de Cowan o multiparamétrico, que se

explica a continuación mediante la siguiente expresión la cual considera los factores según se

describan.

nn= (nn bb + nn 1 + nn 2 + nn 3 + nn 4 ) ∗mm

Donde:

 - nn bb = un valor de n en función del material de fondo.

 - nn 1 = factor de corrección para considerar el efecto de las irregularidades superficiales.

 - nn 2 = un valor que añade las variaciones de forma y tamaño de la sección del cauce.

 - nn 3 = un valor que considera el efecto de las obstrucciones, tales como troncos, tacos,
cantos rodados, escombros, pilotes y muelles, perturba el flujo y aumenta la rugosidad del

cauce.

 - nn 4 = un valor que incorpora el efecto de la presencia de vegetación y condiciones del
flujo. El efecto de la vegetación n4 depende de la profundidad del flujo y del perímetro
mojado cubierto por vegetación.

 - mm = un factor que implementa la sinuosidad del cauce. El grado de sinuosidad del
cauce será considerado sólo cuando el flujo es confinado al cauce.

Es importante destacar que para la estimación de los parámetros de Cowan de los cauces en estudio
se utilizó la guía “Guide for Selecting Manning's Roughness Coefficients for Natural Channels and
Flood Plains, United States Geological Survey Water-Supply Paper 2339, 1989”.

En vista y consideración que los cauces en estudio presentan diferencias entre sus secciones medias
y sus secciones de riberas en el contexto de estratos y vegetación, los valores de Manning serán
considerados de forma separada para cada uno de ellos, identificando estos en el cuadro a
continuación como IN para la sección media del cauce y OUT para las secciones de riberas del cauce.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

14

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Tabla 3 Coeficiente De Rugosidad Manning Según Cowan en Esteros Proyecto Santa**

**Graciela Solar**

|QUEBRADA|MÉTODO COWAN|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**QUEBRADA**<br>|~~**nb**~~<br>|~~**n1**~~<br>|~~**n2**~~<br>|~~**n3**~~<br>|~~**n4**~~<br>|~~**m **~~<br>|~~**MANNING (n)**~~<br>|
|~~IN PC1 Estero Meco ~~<br>|~~0.02 ~~<br>|~~0.015 ~~<br>|~~0.005 ~~<br>|~~0.01 ~~<br>|~~0.025 ~~<br>|~~1 ~~<br>|~~0.075~~<br>|
|~~OUT PC1 Estero Meco ~~<br>|~~0.02 ~~<br>|~~0.015 ~~<br>|~~0.005 ~~<br>|~~0.02 ~~<br>|~~0.1 ~~<br>|~~1 ~~<br>|~~0.16~~<br>|
|~~IN PC2 Estero Maule~~<br>|~~0.02 ~~<br>|~~0.015 ~~<br>|~~0.005 ~~<br>|~~0.01 ~~<br>|~~0.025 ~~<br>|~~1 ~~<br>|~~0.075~~<br>|
|~~OUT PC2 Estero Maule ~~<br>|~~0.02 ~~<br>|~~0.015 ~~<br>|~~0.005 ~~<br>|~~0.02 ~~<br>|~~0.1 ~~<br>|~~1 ~~<br>|~~0.16~~<br>|

Fuente: Elaboración propia en base a Guide for Selecting Manning's Roughness Coefficients for Natural
Channels and Flood Plains, United States Geological Survey Water-Supply Paper 2339, 1989.

Se logra identificar que en la zona de las riberas de los cauces se asume un valor de Manning
bastante conservador, esto debido a la gran cantidad de vegetación existente en la zona lo que
justifica el uso de ese valor elevado. En el caso del valor de Manning para las secciones medias de
los cauces se asume un valor que también es conservador, pero esto es debido a la alta existencia
de raíces y vegetación presente.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

15

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

# 5. RESULTADOS

Las modelaciones de las quebradas en estudio fueron ejecutadas basándose en los caudales
determinados en el Anexo 3.5 para periodos de retorno de 2, 5, 10, 20, 25, 50, 75 y 100 años en el
punto de control de los esteros, pero se demuestran solo los resultados del caudal con periodo de
retorno de 100 años por representar el peor escenario.

A modo de comprender las modelaciones, junto a los resultados se detalla la identificación de los
perfiles de la modelación en HEC-RAS para cada cauce, en cada uno de estos perfiles se demuestran
los parámetros hidráulicos entregados como resultados.

Para comprender los conceptos de los resultados entregados por la modelación en cada perfil, a
continuación, se demuestra un listado de los parámetros hidráulicos y su significancia, los cuales
serán mostrados en junto a las figuras de resultados de la modelación.

 - Q TOTAL : Caudal total modelado.

 - Perfil : Perfil en el cual se representan los resultados de parámetros hidráulicos.

 - TR : Tasa o periodo de retorno del caudal modelado.

 - MIN CH EL : Cota de elevación mínima del canal en el perfil modelado.

 - W.S. ELEV : Cota de elevación de la superficie del escurrimiento o pelo de agua.

 - E.G. ELEV : Cota de elevación de la energía también conocido como Bernulli.

 - E.G. SLOPE : Pendiente entre el perfil modelado y el perfil siguiente aguas abajo.

 - VEL CHNL : Velocidad del escurrimiento en el perfil modelado.

 - FLOW AREA : Área hidráulica o área en corte del escurrimiento

 - TOP WIDTH : Ancho del escurrimiento

 - FROUDE # Chl : Numero de froude

En las siguientes figuras cartográficas de resultados se demuestran los perfiles modelados en el
Programa HEC-RAS, junto a el área de inundación, profundidad del flujo, velocidad del flujo y
elevación de la superficie del flujo para un periodo de retorno de 100 años en cada estero por
separado. Los cuadros de resultados se incluyen junto a la figura de Perfiles y áreas de inundación
TR100 años para su mejor comprensión. En el Apéndice B se adjuntan los ejes hidráulicos de cada
perfil por cada estero en estudio.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

16

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

## 5.1 Estero Meco PC1

A continuación, se presentan las cartografías con los resultados de la modelación hidráulica HECRAS del Estero Meco (PC1), junto a la primera figura se encuentra el cuadro de resultados por perfil
a modo de comprender de mejor manera la ubicación de cada uno de los perfiles y los parámetros

hidráulicos en cada uno de ellos.

**Figura 5.1 Perfiles e Inundación TR100 HEC-RAS Quebrada PC1 Estero Meco Proyecto**

**Santa Graciela Solar**

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

17

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Tabla 4 Resultados Parámetros Hidráulicos TR100 años Estero Meco Proyecto Santa**

**Graciela Solar**

|RIVER<br>STA|PROFI<br>LE|Q<br>TOTAL|Col4|MIN<br>CH EL|W.S.<br>ELEV|E.G.<br>ELEV|E.G.<br>SLOPE|VEL<br>CHNL|FLOW<br>AREA|TOP<br>WIDTH|FROUDE #<br>CHL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||**(m3/s)**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|1754|TR100|97.72|196.81|196.81|198.8|198.86|0.007297|1.39|155.12|227.08|0.38|
|1740|TR100|97.72|196.5|196.5|198.69|198.76|0.006613|1.38|143.62|213.22|0.36|
|1717|TR100|97.72|196.5|196.5|198.58|198.6|0.006301|0.72|141.22|203.87|0.27|
|1700|TR100|97.72|196.5|196.5|198.46|198.49|0.006736|0.95|139.07|194.58|0.36|
|1680|TR100|97.72|196|196|198.3|198.36|0.00655|1.26|128.2|190.09|0.36|
|1660|TR100|97.72|196|196|198.2|198.26|0.004133|1.11|141.16|181.77|0.29|
|1639|TR100|97.72|196|196|198.12|198.15|0.005214|0.86|134.79|197.74|0.33|
|1617|TR100|97.72|196|196|198|198.05|0.004625|1.12|138.01|158.3|0.31|
|1600|TR100|97.72|196|196|197.93|197.98|0.004373|1.13|141.54|160.77|0.3|
|1580|TR100|97.72|195.95|195.95|197.81|197.87|0.005741|1.32|133.31|193.26|0.34|
|1558|TR100|97.72|195.5|195.5|197.6|197.7|0.010252|1.62|108.03|217.88|0.45|
|1540|TR100|97.72|195.5|195.5|197.38|197.51|0.01078|1.74|93.04|149|0.47|
|1521|TR100|97.72|195.5|195.5|197.16|197.29|0.012848|1.79|96.36|154.29|0.5|
|1500|TR100|97.72|195|195|196.98|197.08|0.007348|1.49|109.29|143.95|0.39|
|1481|TR100|97.72|195|195|196.82|196.91|0.0102|1.57|107.44|150.17|0.45|
|1462|TR100|97.72|194.5|194.5|196.68|196.75|0.006128|1.34|125.79|159.98|0.35|
|1440|TR100|97.72|194.5|194.5|196.54|196.62|0.006594|1.37|116.78|146.78|0.37|
|1421|TR100|97.72|194.5|194.5|196.38|196.47|0.009161|1.51|104.79|132.99|0.42|
|1401|TR100|97.72|194.22|194.22|196.2|196.29|0.009008|1.51|107.65|135.28|0.42|
|1381|TR100|97.72|193.78|193.78|196.03|196.11|0.008207|1.48|111.45|134.84|0.41|
|1361|TR100|97.72|193.51|193.51|195.88|195.96|0.007315|1.45|111.73|128.31|0.38|
|1340|TR100|97.72|193.5|193.5|195.69|195.79|0.008945|1.58|104.47|135.53|0.42|
|1320|TR100|97.72|193.5|193.5|195.55|195.62|0.007715|1.42|123.27|195.63|0.39|
|1300|TR100|97.72|193.5|193.5|195.4|195.46|0.008649|1.35|129.12|188.8|0.4|
|1280|TR100|97.72|193.5|193.5|195.24|195.3|0.007339|1.27|131.35|197.35|0.37|
|1261|TR100|97.72|193.5|193.5|195.1|195.16|0.007743|1.25|136.65|238.57|0.38|
|1240|TR100|97.72|193.5|193.5|194.9|194.97|0.010253|1.38|125.77|228.16|0.43|
|1220|TR100|97.72|193.5|193.5|194.72|194.77|0.010148|1.3|138.11|218.07|0.42|
|1200|TR100|97.72|193.5|193.5|194.46|194.52|0.014879|1.4|129.54|213.73|0.5|
|1180|TR100|97.72|193|193|194.25|194.29|0.008386|1.15|162.87|236.26|0.38|
|1160|TR100|97.72|193|193|194.08|194.12|0.008686|1.15|165.57|247.1|0.39|
|1141|TR100|97.72|192.5|192.5|193.9|193.95|0.009492|1.26|154.96|246.13|0.41|
|1121|TR100|97.72|192.5|192.5|193.71|193.75|0.009372|1.18|158.83|235.49|0.4|
|1099|TR100|97.72|192|192|193.51|193.55|0.008812|1.22|158.57|231.83|0.4|
|1079|TR100|97.72|192|192|193.36|193.39|0.007164|1.13|169.04|222.44|0.36|
|1060|TR100|97.72|192|192|193.21|193.24|0.008531|1.14|168.92|237.91|0.39|

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

18

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

|RIVER<br>STA|PROFI<br>LE|Q<br>TOTAL|Col4|MIN<br>CH EL|W.S.<br>ELEV|E.G.<br>ELEV|E.G.<br>SLOPE|VEL<br>CHNL|FLOW<br>AREA|TOP<br>WIDTH|FROUDE #<br>CHL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||**(m3/s)**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|1041|TR100|97.72|191.5|191.5|193.11|193.13|0.003683|0.88|215.65|239.46|0.26|
|1021|TR100|97.72|191.5|191.5|193.04|193.06|0.003245|0.86|213.24|236.02|0.25|
|1000|TR100|97.72|191.5|191.5|192.98|193|0.002512|0.8|232.45|236.64|0.22|
|980|TR100|97.72|191.5|191.5|192.93|192.95|0.002193|0.74|223.6|202.88|0.21|
|959|TR100|97.72|191.5|191.5|192.85|192.89|0.003892|1.01|159.89|170.46|0.28|
|941|TR100|97.72|191.5|191.5|192.77|192.8|0.005439|1.11|152.67|172.55|0.32|
|920|TR100|97.72|191|191|192.63|192.68|0.006877|1.26|152.46|192.27|0.36|
|900|TR100|97.72|191|191|192.48|192.53|0.007966|1.33|139.05|162.7|0.39|
|881|TR100|97.72|190.7|190.7|192.34|192.4|0.005847|1.26|141.96|168.6|0.34|
|860|TR100|97.72|190.5|190.5|192.18|192.24|0.009391|1.36|122.23|170.87|0.42|
|841|TR100|97.72|190.5|190.5|191.81|191.95|0.028601|1.88|83.46|165.66|0.69|
|820|TR100|97.72|190|190|191.64|191.71|0.005553|1.2|109.07|171.73|0.33|
|803|TR100|97.72|190|190|191.54|191.6|0.007276|1.21|120|163.24|0.37|
|781|TR100|97.72|190|190|191.34|191.41|0.009859|1.29|110.59|177.68|0.42|
|760|TR100|97.72|189.77|189.77|191.17|191.23|0.007377|1.13|121.1|166.09|0.36|
|740|TR100|97.72|189.5|189.5|190.99|191.06|0.009942|1.25|102.9|152.92|0.42|
|720|TR100|97.72|189.5|189.5|190.85|190.89|0.006177|1.04|130|156.89|0.33|
|700|TR100|97.72|189.15|189.15|190.73|190.77|0.006271|1.02|136.76|167.46|0.33|
|680|TR100|97.72|189.29|189.29|190.57|190.61|0.009336|1.12|128.93|186.95|0.4|
|660|TR100|97.72|189|189|190.42|190.46|0.006371|1.02|143|170.58|0.34|
|640|TR100|97.72|189|189|190.29|190.33|0.006749|1.06|135.34|163|0.35|
|621|TR100|97.72|189|189|190.12|190.17|0.010873|1.21|117.84|161.55|0.43|
|600|TR100|97.72|188.5|188.5|189.93|189.97|0.008081|1.13|127.2|160.44|0.38|
|580|TR100|97.72|188.5|188.5|189.78|189.83|0.006336|1.07|136.14|147.01|0.34|
|561|TR100|97.72|188|188|189.66|189.72|0.005205|1.13|122.81|124.79|0.32|
|540|TR100|97.72|187.5|187.5|189.58|189.63|0.003731|1.07|127.95|122.97|0.28|
|521|TR100|97.72|187.51|187.51|189.48|189.52|0.007211|1.19|124.84|112.79|0.37|
|500|TR100|97.72|187.85|187.85|189.32|189.35|0.009365|1.16|135.21|152.38|0.4|
|480|TR100|97.72|188|188|189.11|189.14|0.011942|1.2|136.38|155.26|0.44|
|459|TR100|97.72|187.01|187.01|188.87|188.91|0.010505|1.27|133.43|147.37|0.43|
|440|TR100|97.72|187|187|188.68|188.73|0.00826|1.31|134.75|158.76|0.39|
|421|TR100|97.72|187|187|188.49|188.55|0.011256|1.4|127.47|174.73|0.45|
|401|TR100|97.72|186.52|186.52|188.29|188.34|0.009325|1.28|140.12|210.4|0.41|
|380|TR100|97.72|186.5|186.5|188.08|188.14|0.01017|1.33|135.69|225.49|0.43|
|360|TR100|97.72|186.5|186.5|187.9|187.94|0.009425|1.19|147.86|225.89|0.4|
|341|TR100|97.72|186.18|186.18|187.75|187.79|0.006989|1.07|157.81|230.42|0.35|
|320|TR100|97.72|186|186|187.61|187.65|0.006739|1.05|158.53|233.47|0.35|
|300|TR100|97.72|186|186|187.46|187.5|0.008544|1.09|146.75|219.03|0.38|

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

19

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

|RIVER<br>STA|PROFI<br>LE|Q<br>TOTAL|Col4|MIN<br>CH EL|W.S.<br>ELEV|E.G.<br>ELEV|E.G.<br>SLOPE|VEL<br>CHNL|FLOW<br>AREA|TOP<br>WIDTH|FROUDE #<br>CHL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||**(m3/s)**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|280|TR100|97.72|185.5|185.5|187.25|187.32|0.010558|1.27|118.46|203.03|0.43|
|260|TR100|97.72|185.5|185.5|187.09|187.15|0.007251|1.19|116.58|174.38|0.37|
|243|TR100|97.72|185|185|186.99|187.04|0.004949|1.05|142.68|174.48|0.31|
|222|TR100|97.72|185.43|185.43|186.88|186.92|0.006753|1.11|142.38|168.51|0.35|
|200|TR100|97.72|185|185|186.74|186.78|0.007035|1.14|141.76|156.28|0.36|
|180|TR100|97.72|184.5|184.5|186.6|186.65|0.006017|1.19|141.61|155.96|0.34|
|160|TR100|97.72|184.5|184.5|186.47|186.51|0.006716|1.17|137.67|146.28|0.35|
|140|TR100|97.72|184.5|184.5|186.29|186.35|0.009539|1.33|116.21|158.74|0.42|
|120|TR100|97.72|184.05|184.05|186.06|186.13|0.01296|1.36|104.34|144.48|0.47|
|100|TR100|97.72|183.81|183.81|185.82|185.89|0.010332|1.37|108.04|140.79|0.43|
|80|TR100|97.72|183.5|183.5|185.65|185.73|0.00663|1.35|105.66|128.45|0.37|
|60|TR100|97.72|183.5|183.5|185.53|185.6|0.006237|1.25|113.25|125.39|0.35|
|40|TR100|97.72|183.5|183.5|185.34|185.43|0.010694|1.44|95.16|119.08|0.44|
|22|TR100|97.72|183.61<br>|183.61<br>|185.21<br>|185.27<br>|0.007506<br>|1.24<br>|114.41<br>|132.51|0.38|

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

20

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 5.2 Resultados de Profundidades TR100 HEC-RAS Quebrada PC1 Estero Meco**
**Proyecto Santa Graciela Solar**

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

21

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 5.3 Resultados de Velocidades TR100 HEC-RAS Quebrada PC1 Estero Meco**
**Proyecto Santa Graciela Solar**

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

22

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 5.4 Resultados de Elevación de Superficie de Inundación en TR100 HEC-RAS**
**Quebrada PC1 Estero Meco Proyecto Santa Graciela Solar**

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

23

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

## 5.2 Estero Maule PC2

A continuación, se presentan las cartografías con los resultados de la modelación hidráulica HECRAS del Estero Maule (PC2), junto a la primera figura se encuentra el cuadro de resultados por perfil
a modo de comprender de mejor manera la ubicación de cada uno de los perfiles y los parámetros

hidráulicos en cada uno de ellos.

**Figura 5.5 Perfiles e Inundación TR100 HEC-RAS Quebrada PC2 Estero Maule Proyecto**

**Santa Graciela Solar**

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

24

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Tabla 5 Resultados Parámetros Hidráulicos TR100 años Estero Maule Proyecto Santa**

**Graciela Solar**

|RIVER<br>STA|PROFI<br>LE|Q<br>TOTAL|Col4|MIN<br>CH EL|W.S.<br>ELEV|E.G.<br>ELEV|E.G.<br>SLOPE|VEL<br>CHNL|FLOW<br>AREA|TOP<br>WIDTH|FROUDE #<br>CHL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||**(m3/s)**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|1140|TR100|16.89|198.5|198.5|198.95|198.97|0.006528|0.6|35.07|87.91|0.3|
|1121|TR100|16.89|198.36|198.36|198.78|198.8|0.01222|0.7|32.05|96.22|0.39|
|1100|TR100|16.89|198.11|198.11|198.65|198.66|0.004156|0.48|48.44|107.19|0.24|
|1080|TR100|16.89|198|198|198.58|198.59|0.002601|0.4|58.51|116.68|0.19|
|1059|TR100|16.89|198|198|198.53|198.53|0.002654|0.4|61.4|136.25|0.19|
|1040|TR100|16.89|198|198|198.46|198.47|0.004257|0.49|50.63|137.76|0.24|
|1019|TR100|16.89|197.91|197.91|198.35|198.36|0.005755|0.54|44.44|130.19|0.28|
|1000|TR100|16.89|197.7|197.7|198.25|198.26|0.004484|0.53|43.76|125.83|0.25|
|980|TR100|16.89|197.5|197.5|198.15|198.16|0.005307|0.55|39.8|106.12|0.27|
|961|TR100|16.89|197.5|197.5|198.08|198.08|0.003026|0.44|51.58|116.07|0.21|
|942|TR100|16.89|197.5|197.5|198.02|198.03|0.002824|0.46|51|114.1|0.2|
|924|TR100|16.89|197.5|197.5|197.95|197.97|0.00466|0.54|43.63|116.7|0.25|
|901|TR100|16.89|197.27|197.27|197.84|197.85|0.005183|0.49|51.78|143.18|0.26|
|881|TR100|16.89|197|197|197.74|197.75|0.004649|0.5|49.98|136.96|0.25|
|859|TR100|16.89|197|197|197.64|197.65|0.003896|0.49|50.14|133.19|0.23|
|840|TR100|16.89|197|197|197.56|197.58|0.004695|0.55|44.52|120.76|0.26|
|819|TR100|16.89|197|197|197.39|197.42|0.012802|0.75|30.95|103.89|0.4|
|800|TR100|16.89|196.6|196.6|197.2|197.22|0.008168|0.68|30.98|108.25|0.33|
|780|TR100|16.89|196.5|196.5|197.01|197.04|0.010482|0.72|29.84|111.2|0.37|
|761|TR100|16.89|196.5|196.5|196.89|196.9|0.005223|0.52|48.42|134.95|0.26|
|740|TR100|16.89|196.14|196.14|196.81|196.82|0.002904|0.46|52.54|134.85|0.21|
|720|TR100|16.89|196|196|196.76|196.77|0.002158|0.43|53.73|132.42|0.18|
|699|TR100|16.89|196|196|196.69|196.71|0.004199|0.54|41.43|128.08|0.25|
|680|TR100|16.89|196|196|196.63|196.64|0.00317|0.5|45.21|136.82|0.22|
|660|TR100|16.89|196|196|196.54|196.56|0.005183|0.59|36.68|142.43|0.27|
|640|TR100|16.89|196|196|196.33|196.37|0.020608|0.9|20.99|76.08|0.51|
|619|TR100|16.89|195.5|195.5|196.16|196.17|0.005121|0.59|36.07|126.88|0.27|
|600|TR100|16.89|195.5|195.5|196.06|196.08|0.004807|0.55|39.93|135.87|0.26|
|580|TR100|16.89|195.5|195.5|195.92|195.94|0.009737|0.67|32.66|120.47|0.35|
|562|TR100|16.89|195|195|195.8|195.81|0.005459|0.59|36.49|108.76|0.28|
|541|TR100|16.89|195|195|195.69|195.71|0.004415|0.57|37.54|96.28|0.25|
|519|TR100|16.89|195|195|195.58|195.6|0.005651|0.61|30.97|79.97|0.28|
|500|TR100|16.89|194.91|194.91|195.45|195.47|0.007456|0.65|26.86|70.73|0.32|
|480|TR100|16.89|194.5|194.5|195.33|195.34|0.00564|0.57|30.13|75.91|0.28|
|460|TR100|16.89|194.5|194.5|195.19|195.21|0.008036|0.63|27.04|75.26|0.33|
|442|TR100|16.89|194.5|194.5|194.98|195.01|0.015763|0.79|21.32|65.48|0.44|

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

25

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

|RIVER<br>STA|PROFI<br>LE|Q<br>TOTAL|Col4|MIN<br>CH EL|W.S.<br>ELEV|E.G.<br>ELEV|E.G.<br>SLOPE|VEL<br>CHNL|FLOW<br>AREA|TOP<br>WIDTH|FROUDE #<br>CHL|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||**(m3/s)**|**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|418|TR100|16.89|194|194|194.69|194.72|0.00966|0.7|24.04|62.65|0.36|
|399|TR100|16.89|193.5|193.5|194.52|194.54|0.009156|0.7|24.4|79.04|0.35|
|379|TR100|16.89|193.5|193.5|194.4|194.42|0.004375|0.57|29.78|57.66|0.25|
|361|TR100|16.89|193.5|193.5|194.28|194.31|0.008652|0.69|24.59|64.17|0.34|
|340|TR100|16.89|193|193|193.99|194.05|0.018232|1.17|14.5|27.76|0.51|
|320|TR100|16.89|193|193|193.79|193.82|0.007673|0.76|22.23|42.42|0.33|
|298|TR100|16.89|193|193|193.66|193.68|0.004897|0.55|38.23|129.7|0.26|
|281|TR100|16.89|193|193|193.6|193.61|0.003089|0.48|42.51|129.32|0.21|
|260|TR100|16.89|193|193|193.52|193.53|0.004556|0.56|36.26|116.16|0.26|
|242|TR100|16.89|193|193|193.41|193.43|0.007154|0.62|37.43|126.89|0.31|
|220|TR100|16.89|192.54|192.54|193.3|193.31|0.004086|0.5|52.24|153.87|0.24|
|202|TR100|16.89|192.5|192.5|193.22|193.24|0.004663|0.53|51.38|185.89|0.25|
|182|TR100|16.89|192.5|192.5|193.12|193.13|0.00595|0.55|52.38|231.29|0.28|
|160|TR100|16.89|192.5|192.5|192.96|192.97|0.007897|0.58|46.01|167.86|0.32|
|140|TR100|16.89|192.37|192.37|192.79|192.8|0.009027|0.6|45.71|177.38|0.33|
|120|TR100|16.89|192.15|192.15|192.61|192.62|0.009102|0.56|45.21|177.31|0.33|
|100|TR100|16.89|192|192|192.52|192.53|0.002626|0.43|62.17|168.95|0.19|
|80|TR100|16.89|192|192|192.46|192.47|0.003098|0.43|60.83|151.25|0.21|
|60|TR100|16.89|191.69|191.69|192.38|192.39|0.00523|0.58|51.85|160.78|0.27|
|40|TR100|16.89|191.5|191.5|192.29|192.3|0.003862|0.55|51.84|167.89|0.24|
|20|TR100|16.89|191.5<br>|191.5<br>|192.18<br>|192.2<br>|0.006507<br>|0.63<br>|36.07<br>|131.12|0.3|

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

26

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 5.6 Resultados de Profundidades TR100 HEC-RAS Quebrada PC2 Estero Maule**
**Proyecto Santa Graciela Solar**

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

27

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 5.7 Resultados de Velocidades TR100 HEC-RAS Quebrada PC2 Estero Maule**
**Proyecto Santa Graciela Solar**

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

28

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 5.8 Resultados de Elevación de Superficie de Inundación en TR100 HEC-RAS**
**Quebrada PC2 Estero Maule Proyecto Santa Graciela Solar**

Fuente: Elaboración propia, MODELING 2022.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

29

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

# 6. CONCLUSIONES

Los cauces en el tramo modelado presentan bajas pendientes menores al 1% de lo cual se unifica
tanto aguas arriba como aguas abajo en su condición de borde asumiendo el peor escenario posible,
a su vez los cauces en conjunto demuestran una cobertura vegetal alta tanto en su sección de ribera,
abarcando un valor de Manning de 0,16, como en su sección media de cauce con valores de Manning
que se estimaron en 0,075 según Cowan.

Para el Estero Meco el caudal modelado máximos producto de una crecida con periodo de retorno
de 100 años fue de 97,72m [3] /s, demostrando como resultante en su modelo bajas profundidades en
gran parte de su trayectoria solo con zonas puntuales que asumen profundidades centrales del
cauce del orden de los 2,5 metros, a su vez presenta también bajas velocidades en su trayectoria
con valores que ascienden hasta los 2,25 m/s. Se demuestra un ancho máximo del flujo modelado
en 247 metros según el modelo HEC-RAS.

En el caso del Estero Maule el caudal modelado máximos producto de una crecida con periodo de
retorno de 100 años fue de 16,89m [3] /s, demostrando resultados en su modelo con bajas
profundidades en gran parte de su trayectoria solo con zonas puntuales que asumen profundidades
del orden de los 1,17 metros por irregularidades en su topografía, a su vez presenta también bajas
velocidades en su trayectoria con valores que ascienden hasta los 1,41 m/s según muestra el
modelo. Se demuestra un ancho máximo del flujo modelado en 231 metros según el modelo HEC
RAS.

En general se logra concluir que los cauces naturales de nombre Estero Meco (PC1) y Estero Maule
(PC2) en posible interacción con el Proyecto son capaces de contener la crecida de caudal de
carácter centenaria (TR100 años) dentro del área de influencia del presente estudio sin mostrar un
desborde de su cauce natural, junto a ello se demuestra su número de Froude en los esteros con un
régimen de escurrimiento subcrítico o lento lo que se logra comprender por la baja pendiente de
los esteros. Se demuestra un acho máximo del flujo en

Finalmente, junto a los argumentos mostrados en el estudio: características geomorfológicas de los
cauces, estimación de hidrología planteada y modelación hidráulica desarrollada en el presente
documento, el emplazamiento DIA del Proyecto Santa Graciela Solar se define a modo de evitar las
trazas de inundaciones resultantes de los caudales de crecida centenaria (TR100) en los esteros
estudiados para la disposición de su emplazamiento de partes y obras. En la figura a continuación
se visualiza el emplazamiento del Proyecto Santa Graciela Solar (DIA) junto a las trazas de inundación
resultantes del modelo hidráulico con caudales TR100 años justificado en el presente documento,
la cual justifica la inexistencia de afectación o intervención a la componente hidrológica dentro del
área de influencia del Proyecto Santa Graciela Solar.

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

30

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

**Figura 6.1 Resultados de Modelo Hidráulico TR100 años y Emplazamiento DIA Santa**

**Graciela Solar**

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

31

**ANEXO 2.4 • CARACTERIZACIÓN DE INUNDACIÓN**

DECLARACIÓN DE IMPACTO AMBIENTAL

PROYECTO SANTA GRACIELA SOLAR

# 7. REFERENCIAS BIBLIOGRÁFICAS

 - Manual de Carreteras V2 (2018), MOP Chile.

 - Manual de Carreteras V3 (2016), MOP Chile.

 - Hidráulica de Canales Abiertos (2004) Ven Te Chow

 - Guide for Selecting Manning's Roughness Coefficients for Natural Channels and Flood
Plains, United States Geological Survey Water-Supply Paper 2339, 1989

 - Manual Básico de HEC-RAS 3.1.3 y HEC-GeoRAS 3.1.1 (2007), Universidad de Granada

 - GUÍA PARA LA DESCRIPCIÓN DEL ÁREA DE INFLUENCIA (2017), SEA Chile.

 - Guía de Permisos Ambientales Sectoriales En El SEIA N°156 (2016), SEA-DGA Chile.

 - Guía de Permisos Ambientales Sectoriales En El SEIA N°157 (2016), SEA-DGA Chile.

 - Guías Metodológicas para Proyectos de Modificación de Cauces (2016), DGA-MOP Chile.

# 8. PROFESIONALES

 - Diego Campos Molina, Ingeniero Civil en Obras Civiles, Minor en Prevención de Riesgos y

Medio Ambiente.

# 9. APENDICES

 - APENDICE A - Topografía de Esteros Santa Graciela Solar

 APÉNDICE B - Ejes Hidráulico de Esteros Santa Graciela Solar

 - APÉNDICE C - Archivos HEC-RAS de modelo Esteros Santa Graciela Solar

www.energy-head.com
Príncipe de Gales 5921, of. 1806 - La Reina

32

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Caudales de Crecida en Puntos de Control Proyecto Santa Graciela Solar****

| PUNTO DE CONTROL | CAUDALES (T años) EN m3/s | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PUNTO DE CONTROL<br> | ~~2 ~~<br> | ~~5 ~~<br> | ~~10~~<br> | ~~20~~<br> | ~~25~~<br> | ~~50~~<br> | ~~100~~<br> |
| ~~PC1 Estero Meco~~<br> | ~~32.20~~<br> | ~~49.69~~<br> | ~~57.46~~<br> | ~~70.78~~<br> | ~~74.59~~<br> | ~~86.06~~<br> | ~~97.72~~<br> |
| ~~PC2 Estero Maule~~<br> | ~~5.20~~<br> | ~~7.12~~<br> | ~~8.50~~<br> | ~~10.91~~<br> | ~~11.43~~<br> | ~~14.28~~<br> | ~~16.89~~ |

**Tabla 2: Condiciones de Borde en Esteros para HEC-RAS Proyecto Santa Graciela Solar****

| QUEBRADA O CAUCE | PENDIENTE (M/M) | Col3 |
| --- | --- | --- |
| **QUEBRADA O CAUCE**<br> | ~~**DOWNSTREAM**~~<br> | ~~**UPSTREAM 1**~~<br> |
| ~~PC1 Estero Meco ~~<br> | ~~0.0075~~<br> | ~~0.0075~~<br> |
| ~~PC2 Estero Maule ~~<br> | ~~0.0065~~<br> | ~~0.0065~~<br> |

**Tabla 3: Coeficiente De Rugosidad Manning Según Cowan en Esteros Proyecto Santa****

| QUEBRADA | MÉTODO COWAN | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **QUEBRADA**<br> | ~~**nb**~~<br> | ~~**n1**~~<br> | ~~**n2**~~<br> | ~~**n3**~~<br> | ~~**n4**~~<br> | ~~**m **~~<br> | ~~**MANNING (n)**~~<br> |
| ~~IN PC1 Estero Meco ~~<br> | ~~0.02 ~~<br> | ~~0.015 ~~<br> | ~~0.005 ~~<br> | ~~0.01 ~~<br> | ~~0.025 ~~<br> | ~~1 ~~<br> | ~~0.075~~<br> |
| ~~OUT PC1 Estero Meco ~~<br> | ~~0.02 ~~<br> | ~~0.015 ~~<br> | ~~0.005 ~~<br> | ~~0.02 ~~<br> | ~~0.1 ~~<br> | ~~1 ~~<br> | ~~0.16~~<br> |
| ~~IN PC2 Estero Maule~~<br> | ~~0.02 ~~<br> | ~~0.015 ~~<br> | ~~0.005 ~~<br> | ~~0.01 ~~<br> | ~~0.025 ~~<br> | ~~1 ~~<br> | ~~0.075~~<br> |
| ~~OUT PC2 Estero Maule ~~<br> | ~~0.02 ~~<br> | ~~0.015 ~~<br> | ~~0.005 ~~<br> | ~~0.02 ~~<br> | ~~0.1 ~~<br> | ~~1 ~~<br> | ~~0.16~~<br> |

**Tabla 4: Resultados Parámetros Hidráulicos TR100 años Estero Meco Proyecto Santa****

| RIVER<br>STA | PROFI<br>LE | Q<br>TOTAL | Col4 | MIN<br>CH EL | W.S.<br>ELEV | E.G.<br>ELEV | E.G.<br>SLOPE | VEL<br>CHNL | FLOW<br>AREA | TOP<br>WIDTH | FROUDE #<br>CHL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | **(m3/s)** | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 1754 | TR100 | 97.72 | 196.81 | 196.81 | 198.8 | 198.86 | 0.007297 | 1.39 | 155.12 | 227.08 | 0.38 |
| 1740 | TR100 | 97.72 | 196.5 | 196.5 | 198.69 | 198.76 | 0.006613 | 1.38 | 143.62 | 213.22 | 0.36 |
| 1717 | TR100 | 97.72 | 196.5 | 196.5 | 198.58 | 198.6 | 0.006301 | 0.72 | 141.22 | 203.87 | 0.27 |
| 1700 | TR100 | 97.72 | 196.5 | 196.5 | 198.46 | 198.49 | 0.006736 | 0.95 | 139.07 | 194.58 | 0.36 |
| 1680 | TR100 | 97.72 | 196 | 196 | 198.3 | 198.36 | 0.00655 | 1.26 | 128.2 | 190.09 | 0.36 |
| 1660 | TR100 | 97.72 | 196 | 196 | 198.2 | 198.26 | 0.004133 | 1.11 | 141.16 | 181.77 | 0.29 |
| 1639 | TR100 | 97.72 | 196 | 196 | 198.12 | 198.15 | 0.005214 | 0.86 | 134.79 | 197.74 | 0.33 |
| 1617 | TR100 | 97.72 | 196 | 196 | 198 | 198.05 | 0.004625 | 1.12 | 138.01 | 158.3 | 0.31 |
| 1600 | TR100 | 97.72 | 196 | 196 | 197.93 | 197.98 | 0.004373 | 1.13 | 141.54 | 160.77 | 0.3 |
| 1580 | TR100 | 97.72 | 195.95 | 195.95 | 197.81 | 197.87 | 0.005741 | 1.32 | 133.31 | 193.26 | 0.34 |
| 1558 | TR100 | 97.72 | 195.5 | 195.5 | 197.6 | 197.7 | 0.010252 | 1.62 | 108.03 | 217.88 | 0.45 |
| 1540 | TR100 | 97.72 | 195.5 | 195.5 | 197.38 | 197.51 | 0.01078 | 1.74 | 93.04 | 149 | 0.47 |
| 1521 | TR100 | 97.72 | 195.5 | 195.5 | 197.16 | 197.29 | 0.012848 | 1.79 | 96.36 | 154.29 | 0.5 |
| 1500 | TR100 | 97.72 | 195 | 195 | 196.98 | 197.08 | 0.007348 | 1.49 | 109.29 | 143.95 | 0.39 |
| 1481 | TR100 | 97.72 | 195 | 195 | 196.82 | 196.91 | 0.0102 | 1.57 | 107.44 | 150.17 | 0.45 |
| 1462 | TR100 | 97.72 | 194.5 | 194.5 | 196.68 | 196.75 | 0.006128 | 1.34 | 125.79 | 159.98 | 0.35 |
| 1440 | TR100 | 97.72 | 194.5 | 194.5 | 196.54 | 196.62 | 0.006594 | 1.37 | 116.78 | 146.78 | 0.37 |
| 1421 | TR100 | 97.72 | 194.5 | 194.5 | 196.38 | 196.47 | 0.009161 | 1.51 | 104.79 | 132.99 | 0.42 |
| 1401 | TR100 | 97.72 | 194.22 | 194.22 | 196.2 | 196.29 | 0.009008 | 1.51 | 107.65 | 135.28 | 0.42 |
| 1381 | TR100 | 97.72 | 193.78 | 193.78 | 196.03 | 196.11 | 0.008207 | 1.48 | 111.45 | 134.84 | 0.41 |
| 1361 | TR100 | 97.72 | 193.51 | 193.51 | 195.88 | 195.96 | 0.007315 | 1.45 | 111.73 | 128.31 | 0.38 |
| 1340 | TR100 | 97.72 | 193.5 | 193.5 | 195.69 | 195.79 | 0.008945 | 1.58 | 104.47 | 135.53 | 0.42 |
| 1320 | TR100 | 97.72 | 193.5 | 193.5 | 195.55 | 195.62 | 0.007715 | 1.42 | 123.27 | 195.63 | 0.39 |
| 1300 | TR100 | 97.72 | 193.5 | 193.5 | 195.4 | 195.46 | 0.008649 | 1.35 | 129.12 | 188.8 | 0.4 |
| 1280 | TR100 | 97.72 | 193.5 | 193.5 | 195.24 | 195.3 | 0.007339 | 1.27 | 131.35 | 197.35 | 0.37 |
| 1261 | TR100 | 97.72 | 193.5 | 193.5 | 195.1 | 195.16 | 0.007743 | 1.25 | 136.65 | 238.57 | 0.38 |
| 1240 | TR100 | 97.72 | 193.5 | 193.5 | 194.9 | 194.97 | 0.010253 | 1.38 | 125.77 | 228.16 | 0.43 |
| 1220 | TR100 | 97.72 | 193.5 | 193.5 | 194.72 | 194.77 | 0.010148 | 1.3 | 138.11 | 218.07 | 0.42 |
| 1200 | TR100 | 97.72 | 193.5 | 193.5 | 194.46 | 194.52 | 0.014879 | 1.4 | 129.54 | 213.73 | 0.5 |
| 1180 | TR100 | 97.72 | 193 | 193 | 194.25 | 194.29 | 0.008386 | 1.15 | 162.87 | 236.26 | 0.38 |
| 1160 | TR100 | 97.72 | 193 | 193 | 194.08 | 194.12 | 0.008686 | 1.15 | 165.57 | 247.1 | 0.39 |
| 1141 | TR100 | 97.72 | 192.5 | 192.5 | 193.9 | 193.95 | 0.009492 | 1.26 | 154.96 | 246.13 | 0.41 |
| 1121 | TR100 | 97.72 | 192.5 | 192.5 | 193.71 | 193.75 | 0.009372 | 1.18 | 158.83 | 235.49 | 0.4 |
| 1099 | TR100 | 97.72 | 192 | 192 | 193.51 | 193.55 | 0.008812 | 1.22 | 158.57 | 231.83 | 0.4 |
| 1079 | TR100 | 97.72 | 192 | 192 | 193.36 | 193.39 | 0.007164 | 1.13 | 169.04 | 222.44 | 0.36 |
| 1060 | TR100 | 97.72 | 192 | 192 | 193.21 | 193.24 | 0.008531 | 1.14 | 168.92 | 237.91 | 0.39 |

**Tabla 5: Resultados Parámetros Hidráulicos TR100 años Estero Maule Proyecto Santa****

| RIVER<br>STA | PROFI<br>LE | Q<br>TOTAL | Col4 | MIN<br>CH EL | W.S.<br>ELEV | E.G.<br>ELEV | E.G.<br>SLOPE | VEL<br>CHNL | FLOW<br>AREA | TOP<br>WIDTH | FROUDE #<br>CHL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | **(m3/s)** | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 1140 | TR100 | 16.89 | 198.5 | 198.5 | 198.95 | 198.97 | 0.006528 | 0.6 | 35.07 | 87.91 | 0.3 |
| 1121 | TR100 | 16.89 | 198.36 | 198.36 | 198.78 | 198.8 | 0.01222 | 0.7 | 32.05 | 96.22 | 0.39 |
| 1100 | TR100 | 16.89 | 198.11 | 198.11 | 198.65 | 198.66 | 0.004156 | 0.48 | 48.44 | 107.19 | 0.24 |
| 1080 | TR100 | 16.89 | 198 | 198 | 198.58 | 198.59 | 0.002601 | 0.4 | 58.51 | 116.68 | 0.19 |
| 1059 | TR100 | 16.89 | 198 | 198 | 198.53 | 198.53 | 0.002654 | 0.4 | 61.4 | 136.25 | 0.19 |
| 1040 | TR100 | 16.89 | 198 | 198 | 198.46 | 198.47 | 0.004257 | 0.49 | 50.63 | 137.76 | 0.24 |
| 1019 | TR100 | 16.89 | 197.91 | 197.91 | 198.35 | 198.36 | 0.005755 | 0.54 | 44.44 | 130.19 | 0.28 |
| 1000 | TR100 | 16.89 | 197.7 | 197.7 | 198.25 | 198.26 | 0.004484 | 0.53 | 43.76 | 125.83 | 0.25 |
| 980 | TR100 | 16.89 | 197.5 | 197.5 | 198.15 | 198.16 | 0.005307 | 0.55 | 39.8 | 106.12 | 0.27 |
| 961 | TR100 | 16.89 | 197.5 | 197.5 | 198.08 | 198.08 | 0.003026 | 0.44 | 51.58 | 116.07 | 0.21 |
| 942 | TR100 | 16.89 | 197.5 | 197.5 | 198.02 | 198.03 | 0.002824 | 0.46 | 51 | 114.1 | 0.2 |
| 924 | TR100 | 16.89 | 197.5 | 197.5 | 197.95 | 197.97 | 0.00466 | 0.54 | 43.63 | 116.7 | 0.25 |
| 901 | TR100 | 16.89 | 197.27 | 197.27 | 197.84 | 197.85 | 0.005183 | 0.49 | 51.78 | 143.18 | 0.26 |
| 881 | TR100 | 16.89 | 197 | 197 | 197.74 | 197.75 | 0.004649 | 0.5 | 49.98 | 136.96 | 0.25 |
| 859 | TR100 | 16.89 | 197 | 197 | 197.64 | 197.65 | 0.003896 | 0.49 | 50.14 | 133.19 | 0.23 |
| 840 | TR100 | 16.89 | 197 | 197 | 197.56 | 197.58 | 0.004695 | 0.55 | 44.52 | 120.76 | 0.26 |
| 819 | TR100 | 16.89 | 197 | 197 | 197.39 | 197.42 | 0.012802 | 0.75 | 30.95 | 103.89 | 0.4 |
| 800 | TR100 | 16.89 | 196.6 | 196.6 | 197.2 | 197.22 | 0.008168 | 0.68 | 30.98 | 108.25 | 0.33 |
| 780 | TR100 | 16.89 | 196.5 | 196.5 | 197.01 | 197.04 | 0.010482 | 0.72 | 29.84 | 111.2 | 0.37 |
| 761 | TR100 | 16.89 | 196.5 | 196.5 | 196.89 | 196.9 | 0.005223 | 0.52 | 48.42 | 134.95 | 0.26 |
| 740 | TR100 | 16.89 | 196.14 | 196.14 | 196.81 | 196.82 | 0.002904 | 0.46 | 52.54 | 134.85 | 0.21 |
| 720 | TR100 | 16.89 | 196 | 196 | 196.76 | 196.77 | 0.002158 | 0.43 | 53.73 | 132.42 | 0.18 |
| 699 | TR100 | 16.89 | 196 | 196 | 196.69 | 196.71 | 0.004199 | 0.54 | 41.43 | 128.08 | 0.25 |
| 680 | TR100 | 16.89 | 196 | 196 | 196.63 | 196.64 | 0.00317 | 0.5 | 45.21 | 136.82 | 0.22 |
| 660 | TR100 | 16.89 | 196 | 196 | 196.54 | 196.56 | 0.005183 | 0.59 | 36.68 | 142.43 | 0.27 |
| 640 | TR100 | 16.89 | 196 | 196 | 196.33 | 196.37 | 0.020608 | 0.9 | 20.99 | 76.08 | 0.51 |
| 619 | TR100 | 16.89 | 195.5 | 195.5 | 196.16 | 196.17 | 0.005121 | 0.59 | 36.07 | 126.88 | 0.27 |
| 600 | TR100 | 16.89 | 195.5 | 195.5 | 196.06 | 196.08 | 0.004807 | 0.55 | 39.93 | 135.87 | 0.26 |
| 580 | TR100 | 16.89 | 195.5 | 195.5 | 195.92 | 195.94 | 0.009737 | 0.67 | 32.66 | 120.47 | 0.35 |
| 562 | TR100 | 16.89 | 195 | 195 | 195.8 | 195.81 | 0.005459 | 0.59 | 36.49 | 108.76 | 0.28 |
| 541 | TR100 | 16.89 | 195 | 195 | 195.69 | 195.71 | 0.004415 | 0.57 | 37.54 | 96.28 | 0.25 |
| 519 | TR100 | 16.89 | 195 | 195 | 195.58 | 195.6 | 0.005651 | 0.61 | 30.97 | 79.97 | 0.28 |
| 500 | TR100 | 16.89 | 194.91 | 194.91 | 195.45 | 195.47 | 0.007456 | 0.65 | 26.86 | 70.73 | 0.32 |
| 480 | TR100 | 16.89 | 194.5 | 194.5 | 195.33 | 195.34 | 0.00564 | 0.57 | 30.13 | 75.91 | 0.28 |
| 460 | TR100 | 16.89 | 194.5 | 194.5 | 195.19 | 195.21 | 0.008036 | 0.63 | 27.04 | 75.26 | 0.33 |
| 442 | TR100 | 16.89 | 194.5 | 194.5 | 194.98 | 195.01 | 0.015763 | 0.79 | 21.32 | 65.48 | 0.44 |
