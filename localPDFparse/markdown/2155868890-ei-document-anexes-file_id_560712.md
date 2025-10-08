---
title: Sin título
author: Sergio Gonzalez
date: D:20220516125007-04'00'
language: es
type: report
pages: 40
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO CENTRAL SOLAR FOTOVOLTAICA EL SAUCE Anexo 04 B: Estudio Hidráulico
-->

# DECLARACIÓN DE IMPACTO AMBIENTAL PROYECTO CENTRAL SOLAR FOTOVOLTAICA EL SAUCE Anexo 04 B: Estudio Hidráulico

**PREPARADO PARA**

**MAYO 2022**

Dirección: Presidente Batlle y Ordóñez 3784, Ñuñoa, Santiago de Chile
Fono: (56-2) 2223 2346 - 2785 7975 E-mail: kas@kas.cl / Web: www.kas.cl

**Índice de Contenidos**

**1.** **INTRODUCCIÓN .................................................................................................................................. 3**

1.1. O BJETIVO ............................................................................................................................................ 3

1.2. A LCANCE ............................................................................................................................................ 3

1.3. R EFERENCIAS B IBLIOGRÁFICAS ................................................................................................................ 3

**2.** **UBICACIÓN DEL PROYECTO ................................................................................................................. 4**

**3.** **MODELACIÓN HIDRÁULICA ................................................................................................................. 6**

3.1. I MPLEMENTACIÓN DE LOS MODELOS HIDRÁULICOS ...................................................................................... 6

_3.1.1 Caudales de simulación .................................................................................................................... 6_

_3.1.2 Geometría de modelación ................................................................................................................ 6_

_3.1.3 Cálculo de coeficiente de Manning .................................................................................................. 8_

_3.1.4 Condiciones de Borde ..................................................................................................................... 12_

**4.** **RESULTADOS DEL ESTUDIO HIDRÁULICO .......................................................................................... 13**

**5.** **RESULTADOS SUPERPUESTOS CON OBRAS DEL PROYECTO ............................................................... 29**

**6.** **CONCLUSIÓN .................................................................................................................................... 39**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
2

**1.** **INTRODUCCIÓN**

El proyecto parque fotovoltaico “El Sauce”, en adelante el Proyecto, se ubica en la comuna de Freirina,
región de Atacama, Chile. Este proyecto contempla la construcción e instalación de paneles solares y
una línea de alta tensión, con el fin de ampliar la matriz energética del país en energías renovables
y disminuir la dependencia de los combustibles fósiles, principales causantes del cambio climático.

**1.1.** **OBJETIVO**

El objetivo del presente estudio es construir modelos hidráulicos en cada curso de agua en la zona
de influencia del proyecto y simular el escurrimiento de los caudales con periodo de retorno de 100
años.

**1.2.** **ALCANCE**

Este informe contempla los siguientes alcances:

 Implementar los modelos hidráulicos para simular el escurrimiento de los caudales
máximos de crecida en los cauces naturales que cruzan y/o colindan con el proyecto.

 Determinar en base a los resultados de modelación, la aplicabilidad de algún PAS 156 o
PAS 157.

**1.3.** **REFERENCIAS BIBLIOGRÁFICAS**

Para la elaboración del presente documento se utilizaron las referencias que se indican a
continuación:

**REF1** : Chow, V., Maidment, D. y Mays, L. (1994). Hidrología Aplicada. Santafé de Bogotá, Colombia:
McGRAW-HILL, Inc.

**REF2** : Dirección General de Aguas. (2009). Mapa Vectorial de la Red Hidrográfica de Chile.

**REF3** : Ministerio de Obras Públicas. (2020). Manual de Carreteras Volumen N°3 “Instrucciones y
Criterios de Diseño”.

**REF4** : Mega Hidro (2022). M19-20-HID-INF-001- Informe hidrológico en PFV El Sauce.

**REF5** : Genermin. (2021). Levantamiento Aerofotogramétrico en PFV El Sauce.

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
3

**2.** **UBICACIÓN DEL PROYECTO**

El Proyecto se ubica en la región de Atacama, a 29 km aproximadamente al Noreste de la ciudad de
Huasco, en el cual la zona de paneles solares y la respectiva línea de transmisión se encuentran en
el área de influencia de 12 cauces naturales, entre ellos el río Huasco. Las áreas de cuenca asociadas
a estos cursos de agua se muestran en la siguiente Figura.

**Figura 1: Cuencas aportantes en el proyecto.**

Fuente: Elaboración propia.

Los parámetros geomorfológicos de las cuencas asociadas a cada uno de los cursos de agua que
involucran al proyecto se muestran en la siguiente Tabla.

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
4

**Tabla 1: Parámetros geomorfológicos de las cuencas involucradas.**

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto Central Solar Fotovoltaica El Sauce Anexo Hidrología KAS Servicios S.A. 4 -->

**Tabla 1: Parámetros geomorfológicos de las cuencas involucradas.****

| Cuenca | Nombre | Área [km2] | Cota máxima<br>[m s.n.m.] | Cota media [m<br>s.n.m.] | Cota mínima<br>[m s.n.m.] | Desnivel<br>[m] | Longitud del<br>cauce<br>principal [m] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Sin Nombre | 19,42 | 1.226 | 670 | 416 | 810 | 6.691 |
| 2 | Sin Nombre | 11,60 | 1.226 | 602 | 431 | 795 | 5.911 |
| 3 | Sin Nombre | 2,55 | 768 | 505 | 434 | 334 | 3.968 |
| 4 | Sin Nombre | 8,61 | 952 | 731 | 558 | 394 | 3.978 |
| 5 | Sin Nombre | 1,35 | 942 | 758 | 607 | 335 | 1.766 |
| 6 | Sin Nombre | 1,64 | 889 | 534 | 347 | 542 | 1.375 |
| 7 | Sin Nombre | 2,07 | 1.090 | 769 | 460 | 630 | 2.557 |
| 8 | Sin Nombre | 2,39 | 889 | 534 | 347 | 542 | 2.338 |
| 9 | Sin Nombre | 1,18 | 714 | 477 | 331 | 383 | 1.528 |
| 10 | Quebrada Alday | 89,1 | 1.161 | 560 | 247 | 914 | 15.000 |
| 11 | Río Huasco | 8490,46 | 5.998 | 2.907 | 257 | 5,741 | 168.147 |
| 12 | Quebrada Agua<br>Verde | 585,44 | 1.675 | 815 | 231 | 1.444 | 37.530 |

<!-- Estadísticas: 12 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Proyecto Central Solar Fotovoltaica El Sauce Anexo Hidrología KAS Servicios S.A. 5 -->
<!-- FIN TABLA 1 -->


|Cuenca|Nombre|Área [km2]|Cota máxima<br>[m s.n.m.]|Cota media [m<br>s.n.m.]|Cota mínima<br>[m s.n.m.]|Desnivel<br>[m]|Longitud del<br>cauce<br>principal [m]|
|---|---|---|---|---|---|---|---|
|1|Sin Nombre|19,42|1.226|670|416|810|6.691|
|2|Sin Nombre|11,60|1.226|602|431|795|5.911|
|3|Sin Nombre|2,55|768|505|434|334|3.968|
|4|Sin Nombre|8,61|952|731|558|394|3.978|
|5|Sin Nombre|1,35|942|758|607|335|1.766|
|6|Sin Nombre|1,64|889|534|347|542|1.375|
|7|Sin Nombre|2,07|1.090|769|460|630|2.557|
|8|Sin Nombre|2,39|889|534|347|542|2.338|
|9|Sin Nombre|1,18|714|477|331|383|1.528|
|10|Quebrada Alday|89,1|1.161|560|247|914|15.000|
|11|Río Huasco|8490,46|5.998|2.907|257|5,741|168.147|
|12|Quebrada Agua<br>Verde|585,44|1.675|815|231|1.444|37.530|

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
5

**3.** **MODELACIÓN HIDRÁULICA**

La elaboración de los modelos hidráulicos se realizó mediante la aplicación del software HECRAS
6.0.1, el cual resuelve el cálculo del eje hidráulico suponiendo un flujo permanente gradualmente
variado. Para este proyecto se ha utilizado el módulo bidimensional, el cual permite obtener con
precisión las formas de manchas de agua en cauces meandrosos o zonas planas.

**3.1.** **IMPLEMENTACIÓN DE LOS MODELOS HIDRÁULICOS**

**3.1.1 Caudales de simulación**

La simulación del escurrimiento se realiza considerando los caudales máximos de crecidas, asociados
a un período de retorno de 100 años, los cuales son 12 cauces naturales relacionados con el proyecto
acorde a la REF5, los cuales se presentan en la siguiente Tabla.

**Tabla 2: Caudales de crecida para T=100 años en los cauces naturales de la zona de**

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La simulación del escurrimiento se realiza considerando los caudales máximos de crecidas, asociados a un período de retorno de 100 años, los cuales son 12 cauces naturales relacionados con el proyecto acorde a la REF5, los cuales se presentan en la siguiente Tabla. -->

**Tabla 2: Caudales de crecida para T=100 años en los cauces naturales de la zona de****

| Cuenca | Nombre | Caudal máximo instantáneo<br>[m3/s] |
| --- | --- | --- |
| **1 ** | Quebrada Sin Nombre | 66,46 |
| **2 ** | Quebrada Sin Nombre | 42,53 |
| **3 ** | Quebrada Sin Nombre | 10,99 |
| **4 ** | Quebrada Sin Nombre | 36,16 |
| **5 ** | Quebrada Sin Nombre | 8,64 |
| **6 ** | Quebrada Sin Nombre | 10,84 |
| **7 ** | Quebrada Sin Nombre | 11,82 |
| **8 ** | Quebrada Sin Nombre | 13,21 |
| **9 ** | Quebrada Sin Nombre | 7,67 |
| **10** | Quebrada Alday | 11,84 |
| **11** | Río Huasco | 442,84 |
| **12** | Quebrada Agua Verde | 77,93 |

<!-- Estadísticas: 12 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **3.1.2 Geometría de modelación** La geometría del terreno sobre la cual se emplazan los cauces modelados se obtiene a partir de un levantamiento topográfico efectuado por Genermin (REF5) mediante un Vehículo Aéreo No Tripulado -->
<!-- FIN TABLA 2 -->

**influencia del proyecto.**

|Cuenca|Nombre|Caudal máximo instantáneo<br>[m3/s]|
|---|---|---|
|**1 **|Quebrada Sin Nombre|66,46|
|**2 **|Quebrada Sin Nombre|42,53|
|**3 **|Quebrada Sin Nombre|10,99|
|**4 **|Quebrada Sin Nombre|36,16|
|**5 **|Quebrada Sin Nombre|8,64|
|**6 **|Quebrada Sin Nombre|10,84|
|**7 **|Quebrada Sin Nombre|11,82|
|**8 **|Quebrada Sin Nombre|13,21|
|**9 **|Quebrada Sin Nombre|7,67|
|**10**|Quebrada Alday|11,84|
|**11**|Río Huasco|442,84|
|**12**|Quebrada Agua Verde|77,93|

**3.1.2 Geometría de modelación**

La geometría del terreno sobre la cual se emplazan los cauces modelados se obtiene a partir de un
levantamiento topográfico efectuado por Genermin (REF5) mediante un Vehículo Aéreo No Tripulado
(UAV, por sus siglas en inglés), que permitieron obtener un DTM con resolución de 0,42 cm x 0,42

cm.

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
6

La superficie total levantada comprende un área aproximada de 1310 ha, a partir de la cual se
construyeron mallas de modelación, junto con sus respectivas condiciones de borde, como se ilustra
en la siguiente Figura.

**Figura 2: Ejemplo de construcción de modelo en quebrada 4.**

Debido a que no todos los cuerpos de agua tienen el mismo tamaño, se realizó una discretización
espacial y temporal personalizada en cada cauce, de tal forma de obtener números de courant iguales
o menor a la unidad, lo que implica estabilidad numérica y resultados representativos. Estos
parámetros de modelación se muestran en la siguiente Tabla.

**Tabla 3: Definición de parámetros espaciales y temporales por cada cuenca.**

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Debido a que no todos los cuerpos de agua tienen el mismo tamaño, se realizó una discretización espacial y temporal personalizada en cada cauce, de tal forma de obtener números de courant iguales o menor a la unidad, lo que implica estabilidad numérica y resultados representativos. Estos parámetros de modelación se muestran en la siguiente Tabla. -->

**Tabla 3: Definición de parámetros espaciales y temporales por cada cuenca.****

| Cuenca | Δx (m) | Δy (m) | Δt (s) | Tiempo de simulación<br>(min) |
| --- | --- | --- | --- | --- |
| 1 | 5,0 | 0,0 | 0,5 | 45,0 |
| 2 | 5,0 | 0,0 | 0,5 | 45,0 |
| 3 | 5,0 | 0,0 | 0,5 | 45,0 |
| 4 | 2,0 | 2,0 | 1,0 | 30,0 |
| 5 | 3,5 | 3,5 | 0,5 | 15,0 |
| 6 | 3,5 | 3,5 | 0,5 | 15,0 |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Proyecto Central Solar Fotovoltaica El Sauce Anexo Hidrología KAS Servicios S.A. 7 -->
<!-- FIN TABLA 3 -->


|Cuenca|Δx (m)|Δy (m)|Δt (s)|Tiempo de simulación<br>(min)|
|---|---|---|---|---|
|1|5,0|0,0|0,5|45,0|
|2|5,0|0,0|0,5|45,0|
|3|5,0|0,0|0,5|45,0|
|4|2,0|2,0|1,0|30,0|
|5|3,5|3,5|0,5|15,0|
|6|3,5|3,5|0,5|15,0|

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
7

|7|1,5|1,5|0,5|20,0|
|---|---|---|---|---|
|8|1,5|1,5|1,0|30,0|
|9|1,2|1,2|1,0|30,0|
|10|3,0|3,0|1,0|30,0|
|11|5,0|5,0|0,5|45,0|
|12|5,0|5,0|0,5|45,0|

**3.1.3 Cálculo de coeficiente de Manning**

La rugosidad del lecho se cuantifica en términos del coeficiente de Manning, el cual se determina en
base a lo observado durante la visita a terreno y la fotografía levantada por el dron. Los valores se
ajustaron considerando tramos homogéneos tanto de la caja principal del cauce respectivo como de
las planicies de inundación. Para ello se consideraron los parámetros asociados al material del lecho,
la irregularidad del cauce, el efecto de obstrucciones, la mayor o menor presencia de vegetación, la
variación de la sección transversal a lo largo del cauce y las curvaturas en planta de este, los cuales
son definidos en la fórmula de Cowan.

n= (n 0 + n 1 + n 2 + n 3 + n 4 ) ∙m

Donde

n 0 : Valor del coeficiente de Manning base para un canal recto, uniforme, prismático y con perímetro
de rugosidad homogénea.
n 1 : Corrección por irregularidades superficiales del perímetro mojado.
n 2 : Corrección por variación de forma y dimensiones de las secciones.
n 3 : Corrección por obstrucciones.
n 4 : Corrección por presencia de vegetación
m : Factor de meandros del canal

En la siguiente Tabla se reporta el rango conceptual de los parámetros de la fórmula de Cowan, a
partir del cual se determinan los coeficientes de Manning para cada cauce interceptado y/o colindante
con el trazado del proyecto.

**Tabla 4: Rango conceptual de los parámetros definidos en la fórmula de Cowan.**

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la siguiente Tabla se reporta el rango conceptual de los parámetros de la fórmula de Cowan, a partir del cual se determinan los coeficientes de Manning para cada cauce interceptado y/o colindante con el trazado del proyecto. -->

**Tabla 4: Rango conceptual de los parámetros definidos en la fórmula de Cowan.****

| Parámetro | Característica | Valor medio |
| --- | --- | --- |
| **n0 ** | Tierra | 0,020 |
| **n0 ** | Roca | 0,025 |
| **n0 ** | Grava Fina | 0,024 |
| **n0 ** | Grava Gruesa | 0,028 |
| **n1 ** | Ligero | 0,000 |
| **n1 ** | Menor | 0,005 |
| **n1 ** | Moderado | 0,010 |
| **n1 ** | Severo | 0,020 |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Proyecto Central Solar Fotovoltaica El Sauce Anexo Hidrología KAS Servicios S.A. 8 -->
<!-- FIN TABLA 4 -->


|Parámetro|Característica|Valor medio|
|---|---|---|
|**n0 **|Tierra|0,020|
|**n0 **|Roca|0,025|
|**n0 **|Grava Fina|0,024|
|**n0 **|Grava Gruesa|0,028|
|**n1 **|Ligero|0,000|
|**n1 **|Menor|0,005|
|**n1 **|Moderado|0,010|
|**n1 **|Severo|0,020|

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
8

|n<br>2|Gradual|0,000|
|---|---|---|
|**n2 **|Ocasional|0,005|
|**n2 **|Frecuente|0,010 - 0,015|
|**n3 **|Despreciable|0,000|
|**n3 **|Menor|0,010 - 0,015|
|**n3 **|Apreciable|0,020 - 0,030|
|**n3 **|Severo|0,040 - 0,060|
|**n4 **|Baja|0,005 - 0,010|
|**n4 **|Media|0,010 - 0,025|
|**n4 **|Alta|0,025 - 0,050|
|**n4 **|Muy Alta|0,050 - 0,100|
|**m **|Menor|1,00|
|**m **|Apreciable|1,05|
|**m **|Severo|1,10|

En base a la visita a terreno realizada, se muestran distintas fotografías de la zona de estudio.

**Figura 3: Fotografía de la zona en quebrada 1, 2 y 3.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
9

**Figura 4: Fotografía de quebrada 4.**

**Figura 5: Fotografía representativa de quebradas 5, 6 y 7.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
10

**Figura 6: Fotografía representativa de quebradas 8 y 9.**

**Figura 7: Fotografía representativa de quebrada 10, río Huasco y quebrada 12.**

A través de las fotografías presentadas y la experiencia del consultor, se muestran los cálculos de los
coeficientes de Manning para cada una de las cuencas en la siguiente Tabla.

**Tabla 5: Cálculo de coeficientes de Manning con método de Cowan para los distintos**

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 7: Fotografía representativa de quebrada 10, río Huasco y quebrada 12.** A través de las fotografías presentadas y la experiencia del consultor, se muestran los cálculos de los coeficientes de Manning para cada una de las cuencas en la siguiente Tabla. -->

**Tabla 5: Cálculo de coeficientes de Manning con método de Cowan para los distintos****

| Col1 | Parámetros | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Cuenca** | **n0 ** | **n1 ** | **n2 ** | **n3 ** | **n4 ** | **n ** |
| **1 ** | 0,020 | 0,005 | 0,005 | 0,000 | 0,005 | 0,035 |
| **2 ** | 0,020 | 0,005 | 0,005 | 0,000 | 0,005 | 0,035 |
| **3 ** | 0,020 | 0,005 | 0,005 | 0,000 | 0,005 | 0,035 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Proyecto Central Solar Fotovoltaica El Sauce Anexo Hidrología KAS Servicios S.A. 11 -->
<!-- FIN TABLA 5 -->

**lechos.**

|Col1|Parámetros|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Cuenca**|**n0 **|**n1 **|**n2 **|**n3 **|**n4 **|**n **|
|**1 **|0,020|0,005|0,005|0,000|0,005|0,035|
|**2 **|0,020|0,005|0,005|0,000|0,005|0,035|
|**3 **|0,020|0,005|0,005|0,000|0,005|0,035|

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
11

|4|0,024|0,005|0,005|0,000|0,005|0,039|
|---|---|---|---|---|---|---|
|**5 **|0,028|0,005|0,005|0,000|0,005|0,043|
|**6 **|0,028|0,005|0,005|0,000|0,005|0,043|
|**7 **|0,028|0,005|0,005|0,000|0,005|0,043|
|**8 **|0,028|0,005|0,005|0,000|0,005|0,043|
|**9 **|0,028|0,005|0,005|0,000|0,005|0,043|
|**10**|0,028|0,005|0,005|0,012|0,025|0,075|
|**11**|0,028|0,005|0,005|0,012|0,025|0,075|
|**12**|0,028|0,005|0,005|0,012|0,025|0,075|

Se destaca que no hay diferencias significativas de cobertura de suelo entre las riberas de inundación
y el cajón principal, por ende, los coeficientes de Manning ingresados al modelo no variarán en el
dominio de modelación.

**3.1.4 Condiciones de Borde**

Debido a que se desconoce, a priori, el régimen de flujo de los distintos cauces en el área de estudio,
se supone un régimen mixto, determinando así las condiciones que restringen el comportamiento
hidráulico de los cauces durante el proceso de modelación. Para ello, es necesario incorporar
condiciones de borde tanto aguas arriba como aguas abajo de los cauces modelados, las cuales se
suponen representadas por una altura normal, que depende de la pendiente de fondo de los cauces,
la geometría del terreno y el número de Manning del dominio de modelación. En virtud de lo anterior,
las condiciones de borde para los cauces naturales relacionados con el Proyecto.

**Tabla 6: Condiciones de borde para la modelación hidráulica de los cauces naturales en**

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- condiciones de borde tanto aguas arriba como aguas abajo de los cauces modelados, las cuales se suponen representadas por una altura normal, que depende de la pendiente de fondo de los cauces, la geometría del terreno y el número de Manning del dominio de modelación. En virtud de lo anterior, las condiciones de borde para los cauces naturales relacionados con el Proyecto. -->

**Tabla 6: Condiciones de borde para la modelación hidráulica de los cauces naturales en****

| Cuenca | Nombre | Condición de borde aguas arriba | Condición de borde aguas abajo |
| --- | --- | --- | --- |
| **1 ** | Sin Nombre | i = 0,020 | i = 0,010 |
| **2 ** | Sin Nombre | i = 0,013 | i = 0,010 |
| **3 ** | Sin Nombre | i = 0,018 | i = 0,010 |
| **4 ** | Sin Nombre | i = 0,030 | i = 0,030 |
| **5 ** | Sin Nombre | i = 0,070 | i = 0,070 |
| **6 ** | Sin Nombre | i = 0,080 | i = 0,080 |
| **7 ** | Sin Nombre | i = 0,100 | i = 0,100 |
| **8 ** | Sin Nombre | i = 0,030 | i = 0,030 |
| **9 ** | Sin Nombre | i = 0,030 | i = 0,030 |
| **10** | Sin Nombre | i = 0,020 | i = 0,020 |
| **11** | Río Huasco | i = 0,001 | i = 0,001 |

<!-- Estadísticas: 11 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Proyecto Central Solar Fotovoltaica El Sauce Anexo Hidrología KAS Servicios S.A. 12 -->
<!-- FIN TABLA 6 -->

**la zona de influencia del proyecto.**

|Cuenca|Nombre|Condición de borde aguas arriba|Condición de borde aguas abajo|
|---|---|---|---|
|**1 **|Sin Nombre|i = 0,020|i = 0,010|
|**2 **|Sin Nombre|i = 0,013|i = 0,010|
|**3 **|Sin Nombre|i = 0,018|i = 0,010|
|**4 **|Sin Nombre|i = 0,030|i = 0,030|
|**5 **|Sin Nombre|i = 0,070|i = 0,070|
|**6 **|Sin Nombre|i = 0,080|i = 0,080|
|**7 **|Sin Nombre|i = 0,100|i = 0,100|
|**8 **|Sin Nombre|i = 0,030|i = 0,030|
|**9 **|Sin Nombre|i = 0,030|i = 0,030|
|**10**|Sin Nombre|i = 0,020|i = 0,020|
|**11**|Río Huasco|i = 0,001|i = 0,001|

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
12

**4.** **RESULTADOS DEL ESTUDIO HIDRÁULICO**

Los resultados de alturas y velocidades de los 11 cursos de agua se muestran en las siguientes
Figuras, las alturas se expresan en [m] y las velocidades en [m/s].

**Figura 8: Mapa de alturas en quebrada 1, 2 y 3 para T=100 años.**

**Figura 9: Mapa de velocidades en quebrada 1, 2 y 3 para T=100 años.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
13

**Figura 10: Mapa de alturas en quebrada 4 Sin Nombre para T=100 años en cruce con**

**línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
14

**Figura 11: Mapa de velocidades en quebrada 4 Sin Nombre para T=100 años en cruce**

**con línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
15

**Figura 12: Mapa de alturas en quebrada 5 Sin Nombre para T=100 años en cruce con**

**línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
16

**Figura 13: Mapa de velocidades en quebrada 5 Sin Nombre para T=100 años en cruce**

**con línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
17

**Figura 14: Mapa de alturas en quebrada 6 Sin Nombre para T=100 años en cruce con**

**línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
18

**Figura 15: Mapa de velocidades en quebrada 6 Sin Nombre para T=100 años en cruce**

**con línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
19

**Figura 16: Mapa de alturas en quebrada 7 Sin Nombre para T=100 años en cruce con**

**línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
20

**Figura 17: Mapa de velocidades en quebrada 7 Sin Nombre para T=100 años en cruce**

**con línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
21

**Figura 18: Mapa de alturas en quebrada 8 Sin Nombre para T=100 años en cruce con**

**línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
22

**Figura 19: Mapa de velocidades en quebrada 8 Sin Nombre para T=100 años en cruce**

**con línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
23

**Figura 20: Mapa de alturas en quebrada 9 Sin Nombre para T=100 años en cruce con**

**línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
24

**Figura 21: Mapa de velocidades en quebrada 9 Sin Nombre para T=100 años en cruce**

**con línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
25

**Figura 22: Mapa de alturas en quebrada 10 Alday para T=100 años en cruce con línea**

**de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
26

**Figura 23: Mapa de velocidades en quebrada 10 Alday para T=100 años en cruce con**

**línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
27

**Figura 24: Mapa de alturas en río Huasco y quebrada 12 Agua Verde para T=100 años**

**en cruce con línea de transmisión.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
28

**Figura 25: Mapa de velocidades en río Huasco y quebrada 12 Agua Verde para T=100**

**años en cruce con línea de transmisión.**

**5.** **RESULTADOS SUPERPUESTOS CON OBRAS DEL PROYECTO**

A partir de los resultados anteriores, es posible superponer las manchas de agua y las obras del
Proyecto.

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
29

**Figura 26: Superposición de obras y manchas de agua en quebradas 1, 2 y 3.**

Para el caso particular de la figura anterior, se aclara que la mancha intermedia de agua no es interceptada por las obras del proyecto, dado que los
atraviesos que se muestran son aéreos, y las obras que tocan tierra están con un buffer mínimo de 5 m con respecto a las manchas de agua.

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
30

**Figura 27: Superposición de obras y mancha de agua 4.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
31

**Figura 28: Superposición de obras y mancha de agua 5.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
32

**Figura 29: Superposición de obras y mancha de agua 6.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
33

**Figura 30: Superposición de obras y mancha de agua 7.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
34

**Figura 31: Superposición de obras y mancha de agua 8.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
35

**Figura 32: Superposición de obras y mancha de agua 9.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
36

**Figura 33: Superposición de obras y mancha de agua 10.**

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
37

**Figura 34: Superposición de obras y manchas de agua de río Huasco y quebrada Agua Verde.**

Se aprecia que las manchas de agua no interceptan ninguna obra del proyecto, por lo que no se cambian los ejes hidráulicos ni los patrones de

drenaje de estos cursos de agua.

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
38

**6.** **CONCLUSIÓN**

A partir de los resultados obtenidos, se concluye lo siguiente:

Ninguna parte del proyecto está afecto a un riesgo hidráulico, por lo que no es necesario modificar

cauces y/o construir defensas fluviales para mantener la integridad del Proyecto, ya que los

resultados de línea base serán los mismos que la situación proyectada para las crecidas

centenarias.

Finalmente, este proyecto no contempla realizar modificaciones de cauce, como desvíos o

perfilamientos, ni tampoco contempla realizar obras dentro del cauce y, por consiguiente,

tampoco se contempla realizar obras de defensa fluvial, es posible concluir que en el presente

Proyecto no aplica realizar estudios específicos para los artículos 155, 156 y 157 de los Permisos

Ambientales Sectoriales.

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
39

Proyecto Central Solar Fotovoltaica El Sauce
Anexo Hidrología KAS Servicios S.A.
40