---
title: Sin título
author: usuario
date: D:20221205094544-03'00'
language: es
type: manual
pages: 30
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - DECLARACIÓN DE IMPACTO AMBIENTAL
-->

# DECLARACIÓN DE IMPACTO AMBIENTAL

## “PARQUE FOTOVOLTAICO HALCÓN PEREGRINO”

### ANEXO 2.7 ESTUDIO DE INUNDACIÓN

#### COMUNA DE MOLINA REGIÓN DEL MAULE

###### NOVIEMBRE - 2022

##### ESTUDIO DE INUNDACIÓN DEL RÍO LONTUÉ PFV HALCÓN PEREGRINO

Rev. 0

Elaborado por:

Estudio de Inundación Río Lontué
PFV Halcón Peregrino I

**ÍNDICE**

**1** **INTRODUCCIÓN ................................................................................................................ 1**

**2** **OBJETIVO .......................................................................................................................... 2**

2.1 REFERENCIAS .................................................................................................................... 2

**3** **INUNDACIONES HISTÓRICAS EN LA ZONA ....................................................................... 2**

**4** **ANTECEDENTES ................................................................................................................. 3**

4.1 Hidrología .......................................................................................................................... 3

4.2 Topografía ......................................................................................................................... 5

**5** **VISITA A TERRENO Y CARACTERIZACIÓN DE LA RUGOSIDAD ......................................... 6**

5.1 Visita a terreno .................................................................................................................. 6

5.2 Caracterización de la rugosidad del modelo hidráulico ............................................................ 9

**6** **CONSIDERACIONES GENERALES DE LA MODELACIÓN HIDRÁULICA ............................. 12**

6.1 Caudales y tiempo de modelación ....................................................................................... 12

6.2 Condición de borde ............................................................................................................ 12

6.3 Construcción del modelo geométrico en Iber ....................................................................... 12

**7** **RESULTADOS DE LA MODELACIÓN HIDRÁULICA ........................................................... 14**

7.1 Resultados de la modelación para T=100 años ..................................................................... 14

7.2 Mapas de peligrosidad de inundación .................................................................................. 18

**8** **CONCLUSIONES Y RECOMENDACIONES ......................................................................... 19**

ANEXO A: MAPAS DE RESULTADOS Y PELIGROSIDAD DE INUNDACIÓN

ANEXO B: DESCRIPCIÓN DEL MODELO NUMÉRICO BIDIMENSIONAL IBER

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 1

**1** **INTRODUCCIÓN**

La Empresa PFV Halcon Peregrino SpA, en el marco de búsqueda de nuevas oportunidades de negocio,
se encuentra en proceso de estudio para la materialización de un nuevo parque fotovoltaico, denominado
“Parque Fotovoltaico Halcón Peregrino”, ubicado en la Región del Maule, específicamente, en el sector
rural de Pichingal, comuna de Molina.

El área de estudio, el cual se presenta en la Figura 1, corresponde al “Fundo El Nogal” y colinda con la
ribera del río Lontué.

**Figura 1 - PFV Halcón Peregrino y Río Lontué**

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 2

**2** **OBJETIVO**

El objetivo del presente estudio es evaluar la inundabilidad del predio del Proyecto Fotovoltaico Halcón
Peregrino en un evento de crecidas del río Lontué.

Como parte del análisis se presenta un mapa de peligrosidad para las crecidas del Río Lontué en base a
criterios de profundidad y velocidad del flujo en los sectores donde se desborda el río. Las crecidas del Río
Lontué fueron estimadas en el Anexo 2.6 Estudio Hidrológico de Crecidas de la presente DIA, utilizando
para efectos de verificación la crecida con período de retorno de 100 años de acuerdo con las
recomendaciones de la DGA.

**2.1** **REFERENCIAS**

Para el desarrollo del presente estudio, se utilizaron las siguientes referencias:

Ref. 1 Anexo 2.6 Hidrología Estudio Hidrológico de Crecidas de la presente DIA
Ref. 2 Hidráulica de Canales Abiertos. Chow, V. T. (1994).
Ref. 3 Manual de Carreteras Volumen 3. Dirección de Vialidad MOP. 2020.
Ref. 4 Guidance for Flood Risk Analysis and Mapping, Flood Depth and Analysis Grid. Federal
Emergency Management Agency (FEMA), 2018.

**3** **INUNDACIONES HISTÓRICAS EN LA ZONA**

De manera histórica, el Río Lontué en su tramo del valle central ha tenido inundaciones que han provocado
perjuicios a la población. Entre los eventos más recientes se encuentra el Aluvión de Lontué de 1986, donde
lluvias continuas por más de 4 días desencadenaron una crecida que sobrepasó los límites del cauce
normal del río Lontué en el sector de Pichingal, provocando grandes daños. Más recientemente el año 2008
hubo desbordes del Río Lontué en varios puntos de la comuna de Molina.

**Figura 2 - Inundación de 1986 en sector de Pichingal, Río Lontué**

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 3

**Figura 3 - Inundación de 2008 en comuna de Molina, Río Lontué**

**4** **ANTECEDENTES**

**4.1** **Hidrología**

Para la elaboración del estudio de inundación se cuenta con un estudio hidrológico específico para el río
Lontué en la zona del Proyecto. En este estudio se identifica la cuenca aportante del río hasta el punto de
ubicación del Proyecto.

En la Figura 4 se presenta la cuenca del río Lontué asociada al PFV Halcón Peregrino y su red de drenaje,
la cual posee una superficie de aproximadamente 1.900 km [2], y donde se observa que la cuenca se
desarrolla en una proporción similar, tanto en el valle como el sector cordillerano, de lo cual se puede
concluir que el río Lontué en el sector de estudio posee un régimen de caudales pluvio-nival.

Cuenca Río

Lontué

PFV Halcón

Peregrino

**Figura 4 - Cuenca del Río Lontué en PFV Halcón Peregrino.**

**Fuente: Estudio Hidrológico del Proyecto.**

Del estudio se obtienen los siguientes caudales de crecidas para el Proyecto.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 4

**Tabla 1 - Caudal Máximo Instantáneo Adoptado para Río Lontué en PFV Halcón Peregrino.**

|Período de<br>Retorno<br>(años)|Caudal Máximo<br>Inst. (m3/s)|
|---|---|
|**5 **|1.240|
|**10**|1.648|
|**25**|2.162|
|**50**|2.534|
|**100**|2.892|
|**150**|3.095|

En el estudio hidrológico se identifican un hidrograma de crecida característico que permite modelar el
evento de inundación en el escenario de una crecida centenaria.

**Figura 5 - Hidrograma de Crecida Río Lontué en PFV Halcón Peregrino.**

Los valores del hidrograma de crecidas se presentan en la siguiente tabla.

**Tabla 2 - Hidrograma de Crecida Río Lontué en PFV Halcón Peregrino.**

|Tiempo (hr)|Caudal Hidrograma de Crecida Río Lontué en PFV Halcón Peregrino (m3/s)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Tiempo (hr)**|**T=5**|**T=10**|**T=25**|**T=50**|**T=100**|**T=150**|
|0,0|0|0|0|0|0|0|
|0,8|19|25|32|38|43|46|
|1,5|93|124|162|190|217|232|
|2,3|198|264|346|405|463|495|
|3,1|347|461|605|709|810|867|
|3,8|533|709|930|1090|1244|1331|
|4,6|744|989|1297|1520|1735|1857|
|6,1|1104|1467|1924|2255|2574|2755|
|7,6|1240|1648|2162|2534|2892|3095|
|9,2|1141|1516|1989|2331|2661|2848|
|10,7|930|1236|1621|1900|2169|2322|
|12,2|695|923|1211|1419|1620|1733|
|13,7|521|692|908|1064|1215|1300|

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 5

|Tiempo (hr)|Caudal Hidrograma de Crecida Río Lontué en PFV Halcón Peregrino (m3/s)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Tiempo (hr)**|**T=5**|**T=10**|**T=25**|**T=50**|**T=100**|**T=150**|
|15,3|397|527|692|811|925|991|
|16,8|298|396|519|608|694|743|
|18,3|223|297|389|456|521|557|
|19,8|161|214|281|329|376|402|
|21,4|122|162|212|248|283|303|
|22,9|93|124|162|190|217|232|
|26,7|45|59|78|91|104|111|
|30,5|22|30|39|46|52|56|
|34,3|11|15|19|23|26|28|
|38,1|5|7|9|10|12|12|

**4.2** **Topografía**

Para la elaboración del estudio se cuenta con información de topografía de fuentes satelitales de la Agencia
de Exploración Aeroespacial de Japón (Japan Aerospace Exploration Agency “JAXA”), ALOS Science
Project, Earth Observation Research Center (EORC). Este levantamiento tiene una resolución de 1
arcosegundo, aproximadamente 30 m.

**Figura 6 - Modelo de topografía para la modelación hidráulica**

Se usa una longitud de cauce suficiente para poder modelar un tramo de Río Lontué de al menos un
kilómetro hacia aguas arriba y hacia agua abajo desde los límites del parque.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 6

**5** **VISITA A TERRENO Y CARACTERIZACIÓN DE LA RUGOSIDAD**

**5.1** **Visita a terreno**

Para una mejor caracterización de la rugosidad del terreno y las condiciones que controlan el flujo se recurre
a una visita a terreno efectuada a la zona del proyecto el día 26 de septiembre de 2021. En esta visita se
visitó un tramo del río Lontué en la zona del Proyecto.

**Figura 7 - Vista aérea río Lontué en la zona del PFV**

En las imágenes aéreas se observa un río trenzado, indicador de un río con alta energía, una pendiente
media de 1% lo que supone un escurrimiento cercano a la crisis hidráulica, típico de ríos de la zona central
del país. El presenta un lecho de arena y gravas de tamaño mayor, con indicios de acorazamiento del lecho.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 7

**Figura 8 - Fotografía del río Lontué en ribera izquierda**

De manera longitudinal al parque se observa la presencia de una defensa fluvial, de tamaños de rocas
importante, mayores a los 300 kg de peso nominal. La defensa se aprecia en buen estado.

**Figura 9 - Vista aérea de la defensa fluvial lateral en la zona del PFV**

Hacia aguas arriba del Proyecto existe una defensa fluvial también en muy buenas condiciones, que
protege la ribera izquierda donde comienza el predio del Fundo. Hacia aguas arriba por la misma ribera
existe otra defensa fluvial, protegida por una línea de árboles que contribuyen a la protección de la ribera.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 8

**Figura 10 - Vista aérea de la defensa fluvial aguas arriba de la zona del PFV**

En distintos tramos del río se observan sectores dentro de la caja del río con distintos grados de
concentración de vegetación, con algunas zonas de bosque tupido que representa una mayor resistencia
al flujo, y otras zonas con vegetación intermedia dentro del cauce.

**Figura 11 - Vista aérea de la caja principal del Río Lontué en zona del PFV**

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 9

Fuera del cauce principal existen zonas como el predio del PFV donde se presentan cultivos con escasa
vegetación al momento de la visita, sin grandes obstrucciones al flujo. Estos son sectores planos, siendo
planicies de inundación naturales, y no constituyendo parte reciente del cauce activo del Río Lontué en la
zona del PFV.

**Figura 12 - Vista aérea del predio del PFV Halcón Peregrino**

La información obtenida mediante las imágenes de la visita a terreno se utiliza en el siguiente acápite para
la representación de la rugosidad en el modelo hidráulico bidimensional.

**5.2** **Caracterización de la rugosidad del modelo hidráulico**

Para la caracterización de la rugosidad del dominio de modelación se recurre a la información de la visita
a terreno e imágenes satelitales de Google Earth.

En la determinación del coeficiente de rugosidad se consideró, primeramente, lo propuesto por Cowan que
desarrolló un procedimiento para estimar el valor de _n_ de acuerdo con lo siguiente:

_n_  _(n_ _0_  _n_ _1_  _n_ _2_  _n_ _3_  _n_ _4_ _)_  _m_ _5_

Donde:

_n_ _0_ : Valor básico de n para un canal recto, uniforme y liso en materiales naturales.

_n_ _1_ : Valor agregado a n 0 para corregir el efecto de irregularidades de superficie.

_n_ _2_ : Valor para las variaciones en forma y tamaño de la sección transversal del cauce.

_n_ _3_ : Valor que toma en cuenta las obstrucciones.

_n_ _4_ : Valor que toma en cuenta la vegetación y las condiciones de flujo.

_m_ _5_ : Factor de corrección para los meandros.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 10

Los valores de los coeficientes se obtienen de la publicación Hidráulica de Canales Abiertos (Ven Te Chow)
y se corroboran con la publicación del UGCS “Guide for Selecting Manning's Roughness Coefficients for

Natural Channels and Flood Plains”.

**Tabla 3 - Método de Cowan para parámetros de rugosidad (Ven Te Chow)**

|Condiciones del Canal|Col2|Valores|Col4|
|---|---|---|---|
|Material involucrado|Tierra|n0|0,020|
|Material involucrado|Corte en roca|Corte en roca|0,025|
|Material involucrado|Grava fina|Grava fina|0,024|
|Material involucrado|Grava gruesa|Grava gruesa|0,028|
|Grado de irregularidad|Suave|n1|0,000|
|Grado de irregularidad|Menor|Menor|0,005|
|Grado de irregularidad|Moderado|Moderado|0,010|
|Grado de irregularidad|Severo|Severo|0,020|
|Variaciones de la sección transversal|Gradual|n2|0,000|
|Variaciones de la sección transversal|Ocasionalmente alterante|Ocasionalmente alterante|0,005|
|Variaciones de la sección transversal|Frecuentemente alterante|Frecuentemente alterante|0,010-0,015|
|Efecto relativo de las obstrucciones|Insignificante|n3|0,000|
|Efecto relativo de las obstrucciones|Menor|Menor|0,010-0,015|
|Efecto relativo de las obstrucciones|Apreciable|Apreciable|0,020-0,030|
|Efecto relativo de las obstrucciones|Severo|Severo|0,040-0,060|
|Vegetación|Baja|n4|0,005-0,010|
|Vegetación|Media|Media|0,010-0,025|
|Vegetación|Alta|Alta|0,025-0,050|
|Vegetación|Muy alta|Muy alta|0,050-0,100|
|Grado de los efectos por meandros|Menor|m5|1,000|
|Grado de los efectos por meandros|Apreciable|Apreciable|1,150|
|Grado de los efectos por meandros|Severo|Severo|1,300|

Para estimar el coeficiente “n 0 ” se utilizó lo observado en la visita a terreno. En base a los datos de

diámetros disponibles, se calcula la rugosidad base para la zona de cauce principal, cauce con vegetación,
bosque y planicie de inundación.

Al usar el método de Cowan no se consideran las variaciones de la sección transversal ya que forman parte
de las características del modelo hidráulico.

**Tabla 4 - Rugosidad de Manning del Cauce Principal**

|Parámetro|Col2|Cauce principal|Col4|
|---|---|---|---|
|**Parámetro**|**Parámetro**|**Grado**|**Valor**|
|n0|Rugosidad base||0,020|
|n1|Grado de irregularidad|Moderado|0,010|
|n2|Variaciones de la sección transversal|Ocasionalmente alternante|0,000|
|n3|Efecto de las obstrucciones|Insignificante|0,000|
|n4|Vegetación|Baja|0,005|
|m5|Meandros|Menor|1,000|
|**n **|**Coeficiente de rugosidad**||**0,035**|

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 11

**Tabla 5 - Rugosidad de Manning del Cauce con vegetación**

|Parámetro|Col2|Rugosidad de Ribera|Col4|
|---|---|---|---|
|**Parámetro**|**Parámetro**|**Grado**|**Valor**|
|n0|Valor básico de Manning||0,028|
|n1|Grado de irregularidad|Menor|0,005|
|n2|Variaciones de la sección transversal|No se Considera|0,000|
|n3|Efecto de las obstrucciones|Insignificante|0,000|
|n4|Vegetación|Media-Alta|0,025|
|m5|Meandros|Menor|1,000|
|**n **|**Coeficiente de rugosidad**||**0,058**|

**Tabla 6 - Rugosidad de Manning de zona de Bosque**

|Parámetro|Col2|Rugosidad con vegetación|Col4|
|---|---|---|---|
|**Parámetro**|**Parámetro**|**Grado**|**Valor**|
|n0|Valor básico de Manning||0,028|
|n1|Grado de irregularidad|Menor|0,005|
|n2|Variaciones de la sección transversal|No se Considera|0,000|
|n3|Efecto de las obstrucciones|Insignificante|0,000|
|n4|Vegetación|Muy alta|0,075|
|m5|Meandros|Menor|1,000|
|**n **|**Coeficiente de rugosidad**||**0,108**|

**Tabla 7 - Rugosidad de Manning de zonas de Planicie de Inundación**

|Parámetro|Col2|Rugosidad con vegetación|Col4|
|---|---|---|---|
|**Parámetro**|**Parámetro**|**Grado**|**Valor**|
|n0|Valor básico de Manning||0,028|
|n1|Grado de irregularidad|Menor|0,005|
|n2|Variaciones de la sección transversal|No se Considera|0,000|
|n3|Efecto de las obstrucciones|Menor|0,015|
|n4|Vegetación|Media|0,015|
|m5|Meandros|Menor|1,000|
|**n **|**Coeficiente de rugosidad**||**0,063**|

Con estos valores de rugosidad de las distintas zonas se construye la discretización de rugosidad en el
modelo hidráulico.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 12

**Figura 13 - Rugosidad del modelo hidráulico Iber por zonificación**

**6** **CONSIDERACIONES GENERALES DE LA MODELACIÓN HIDRÁULICA**

**6.1** **Caudales y tiempo de modelación**

Los caudales modelados corresponden al hidrograma de crecidas de período de retorno T=100 años que
se presenta en la Tabla 2. Para poder representar todo el paso del hidrograma se modela un total de 150

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 5 - Hidrograma de Crecida Río Lontué en PFV Halcón Peregrino.** Los valores del hidrograma de crecidas se presentan en la siguiente tabla. -->

**Tabla 2: - Hidrograma de Crecida Río Lontué en PFV Halcón Peregrino.****

| Tiempo (hr) | Caudal Hidrograma de Crecida Río Lontué en PFV Halcón Peregrino (m3/s) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Tiempo (hr)** | **T=5** | **T=10** | **T=25** | **T=50** | **T=100** | **T=150** |
| 0,0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0,8 | 19 | 25 | 32 | 38 | 43 | 46 |
| 1,5 | 93 | 124 | 162 | 190 | 217 | 232 |
| 2,3 | 198 | 264 | 346 | 405 | 463 | 495 |
| 3,1 | 347 | 461 | 605 | 709 | 810 | 867 |
| 3,8 | 533 | 709 | 930 | 1090 | 1244 | 1331 |
| 4,6 | 744 | 989 | 1297 | 1520 | 1735 | 1857 |
| 6,1 | 1104 | 1467 | 1924 | 2255 | 2574 | 2755 |
| 7,6 | 1240 | 1648 | 2162 | 2534 | 2892 | 3095 |
| 9,2 | 1141 | 1516 | 1989 | 2331 | 2661 | 2848 |
| 10,7 | 930 | 1236 | 1621 | 1900 | 2169 | 2322 |
| 12,2 | 695 | 923 | 1211 | 1419 | 1620 | 1733 |
| 13,7 | 521 | 692 | 908 | 1064 | 1215 | 1300 |

<!-- Estadísticas: 14 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros Estudio de Inundación Río Lontué PFV Halcón Peregrino 5 -->
<!-- FIN TABLA 2 -->

mil segundos, que representa un total de 41 horas de modelación.

**6.2** **Condición de borde**

En el modelo Iber la condición de borde ingresada en el extremo de aguas abajo es de crisis hidráulica para
la salida del modelo. Dada la pendiente del terreno en esta zona (≈1%) la condición se considera adecuada.
Por aguas arriba no se ingresa ninguna condición más que el hidrograma de ingreso de caudales, por lo
que las condiciones hidráulicas vienen determinadas por la geometría y rugosidad del terreno, sin forzar
condiciones que alteren el eje hidráulico del modelo.

**6.3** **Construcción del modelo geométrico en Iber**

A partir de la información batimétrica de la Figura 6 se construye en Iber un modelo de batimetría del río
Lontué. La representación del terreno se hace mediante elementos triangulares flexibles, de un tamaño de

lado de 10 m.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 13

**Figura 14 - Modelo de terreno en modelo Iber**

Una vez construido el modelo Iber, con las condiciones de ingreso de caudal y rugosidad se procede a la
modelación de los caudales de diseño (T=100 años). Los resultados de la modelación se incluyen en el
siguiente capítulo.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 14

**7** **RESULTADOS DE LA MODELACIÓN HIDRÁULICA**

**7.1** **Resultados de la modelación para T=100 años**

El primer momento que se identifica en la modelación durante el paso de la crecida es en t=5,8 horas,
donde se produce el ingreso de caudal hacia la zona del predio del proyecto PFV.

**Figura 15 - Campo de velocidades en PFV Halcón Peregrino en t=5,7 hrs**

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 15

**Figura 16 - Niveles de agua (m.s.n.m) en PFV Halcón Peregrino en t=5,7 hrs**

El nivel máximo de inundación se produce en el instante t=8,7 hrs, cuando la mancha de inundación alcanza
la mayor extensión. A partir de este instante la crecida entra en su fase de recesión y disminuyen los niveles
de inundación en el parque.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 16

**Figura 17 - Profundidad de flujo en PFV Halcón Peregrino en t=8,7 hrs en el punto de máxima**

**inundación en el predio**

De la figura anterior se observa que en promedio se tiene una profundidad menor o en torno a 50 cm en la
mayor parte del parque. Por otra parte, las velocidades en la parte inundada del parque están del orden de
0,5 m/s o menos, lo que no constituye velocidades capaces de generar daños en estructuras.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 17

**Figura 18 - Velocidad de flujo en PFV Halcón Peregrino en t=8,7 hrs en el punto de máxima**

**inundación en el predio**

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 18

**Figura 19 - Nivel de agua (m.s.n.m) en PFV Halcón Peregrino en t=8,7 hrs en el punto de máxima**

**inundación en el predio**

Con los resultados del modelo hidráulico en el punto de mayor inundación (t=8,7 hrs) se construyen mapas
de peligrosidad de inundación de acuerdo con recomendaciones internacionales.

**7.2** **Mapas de peligrosidad de inundación**

De acuerdo con las recomendaciones de la Agencia Federal para el Manejo de Emergencias (Federal
Emergency Management Agency, FEMA) de los Estados Unidos, existe una manera simplificada de
cuantificar el riesgo producto de inundaciones, y de presentar mapas de peligro por inundación o _flood_
_hazard_ (ver Ref. 4). Este consiste en multiplicar la profundidad de agua con las velocidades en cada punto
del modelo, obteniendo un producto que se puede asociar a un cierto riesgo. La clasificación propuesta por
FEMA es la siguiente:

**Tabla 8 - Clasificación FEMA del riesgo por inundación**

|Categoría de peligro de<br>la inundación|Rango Profundidad x<br>Velocidad<br>[m2/s]|
|---|---|
|Bajo|<0,2|
|Medio|0,2 - 0,5|
|Alto|0,5 - 1,5|
|Muy Alto|1,5 - 2,5|
|Extremo|> 2,5|

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino 19

En base a esta clasificación, se elaboran los mapas de riesgos correspondientes, para los valores máximos
de profundidad y velocidad en los escenarios de crecidas con período de retorno T=100 años. Los mapas
se elaboran con los valores obtenidos en cada celda en el instante de mayor inundación con t=8,7 hrs.

Los resultados de mapas de peligrosidad se incluyen en el ANEXO A.

**8** **CONCLUSIONES Y RECOMENDACIONES**

En el presente estudio se abordó el estudio de inundación del Parque Fotovoltaico Halcón Peregrino.

Los caudales de modelación se obtuvieron de un Estudio de Crecidas del Río Lontué que forma parte de
estos estudios. En el Estudio de Crecidas se estimó un caudal instantáneo máximo de 2.892 m [3] /s para un
período de retorno de 100 años.

Como parte del estudio se efectuó una visita a terreno donde se evaluó la zona del proyecto y el Río Lontué,
obteniendo los parámetros de rugosidad necesarios para la modelación. A partir de los datos de caudal,
rugosidad y del modelo de batimetría disponible para el estudio se procede a la modelación hidráulica del
Río Lontué mediante el software Iber, cuya descripción se incluye en el Anexo B.

Como resultado principal del estudio se obtuvieron los resultados hidráulicos en el río Lontué en la zona
del parque para un período de retorno de 100 años. A partir de los resultados de profundidad de flujo y
velocidad se obtiene un parámetro de peligrosidad de inundación en base a un criterio de la Agencia Federal
para el Manejo de Emergencias de Estados Unidos (FEMA). Este criterio define rangos de peligrosidad
desde bajo a extremo en base al producto de la velocidad y profundidad de flujo en las celdas del modelo.

En el caso del PFV Halcón Peregrino, los mapas de peligrosidad que se incluyen en el Anexo A muestran
que la mayor parte del parque presenta un peligro Bajo de riesgo por inundación, con solo algunos sectores
puntuales con un rango Medio. Las profundidades de escurrimiento en el parque para el instante de mayor
inundación (t=8,7 hrs) son del orden de 0,5 m o menores, con solo algunos sectores en el rango entre 0,5
y 1 m. Las velocidades en todo el parque son menores a 1 m/s, lo que asegura que en el caso de producirse
un evento de inundación la velocidad del flujo no generará problemas relevantes por socavación o erosión

del terreno.

Finalmente, se concluye a partir de los resultados del estudio de inundación del río Lontué que para una
crecida centenaria existen zonas del proyecto que se inundan de manera temporal, con profundidades y
velocidades que no representan condiciones hidráulicas críticas para la instalación de paneles solares, ni
representan un peligro para las personas. De todas formas, se recomienda que, en el caso de instalar
infraestructura en la zona de inundación identificada en el estudio, se realice una verificación estructural
con una profundidad de al menos 1 m por efecto de socavación general en las estructuras.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino A1

##### ANEXO A MAPAS DE RESULTADOS Y PELIGROSIDAD DE INUNDACIÓN T=100 AÑOS

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino A1

**Mapa de Peligro de Inundación para instante de mayor inundación t=8,7 hrs - T=100 años**

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino A2

**Mapa de Profundidad de Flujo para instante de mayor inundación t=8,7 hrs - T=100 años**

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino A3

**Mapa de Velocidad de Flujo para instante de mayor inundación t=8,7 hrs - T=100 años**

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino B1

##### ANEXO B DESCRIPCIÓN DEL MODELO NUMÉRICO BIDIMENSIONAL IBER (ARCHIVOS DIGITALES APÉNDICE 2.7.1)

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino B2

**B. DESCRIPCIÓN DEL MODELO NUMÉRICO BIDIMENSIONAL**

**a. Generalidades**

Iber es un modelo matemático bidimensional para la simulación de flujos en ríos y estuarios promovido por
el Centro de Estudios Hidrográficos del CEDEX (España) y desarrollado en colaboración con el Grupo de
Ingeniería del Agua y del Medio Ambiente, GEAMA (de la Universidad de La Coruña), el Grupo Flumen (de
la Universitat Politècnica de Catalunya UPC y de la Universitat de Barcelona UB) y el Centro Internacional
de Métodos Numéricos en Ingeniería, CIMNE (vinculado a la Universidad Politécnica de Cataluña UPC),
en el marco de un Convenio de Colaboración suscrito entre el CEDEX y la Dirección General del Agua de
España.

**b. Campos de aplicación**

Los campos de aplicación de la versión actual de _IBER_ son:

- Simulación del flujo en lámina libre en cauces naturales,

- Evaluación de zonas inundables. Cálculo de las zonas de flujo preferente,

- Cálculo hidráulico de encauzamientos,

- Cálculo hidráulico de redes de canales en lámina libre,

- Cálculo de corrientes de marea en estuarios,

- Estabilidad de los sedimentos del lecho,

- Procesos de erosión y sedimentación por transporte de material granular.

**c. Capacidades y características destacadas**

Las capacidades y características más destacadas del modelo Iber son las siguientes:

- Resolución integrada de las ecuaciones de Saint Venant 2D,

- Esquemas explícitos en volúmenes finitos con mallas no estructuradas,

- Capacidad de resolver flujo subcrítico y supercrítico, incluyendo resaltos hidráulicos móviles,

- Balance exacto de la ecuación de balance de masas,

- Modelización de la turbulencia mediante modelos de diferente complejidad,

- Cálculo de la infiltración,

- Tensión superficial por viento,

- Estructuras internas: puentes, compuertas y vertederos,

- Delimitación de la zona de flujo preferente según RDPH (vía de intenso desagüe y zonas de grave
riesgo para personas y bienes),

- Evolución del lecho debido a transporte de sedimentos por carga de fondo y en suspensión,

- Interfaz amigable de pre y post-proceso,

- Integración en SIG (Sistemas de Información Geográfica),

- Verificado y contrastado con soluciones analíticas, con otros modelos, con ensayos de laboratorio
y con medidas de campo.

**d. Módulo Hidrodinámico del modelo Iber**

El módulo hidrodinámico resuelve las ecuaciones de aguas poco profundas promediadas en la profundidad,
también conocidas como 2D Shallow Water Equations (2D-SWE) o ecuaciones de St. Venant
bidimensionales. Dichas ecuaciones asumen una distribución de presión hidrostática y una distribución
relativamente uniforme de la velocidad en profundidad. La hipótesis de presión hidrostática se cumple

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino B3

razonablemente en el flujo en ríos, así como en las corrientes generadas por la marea en estuarios.
Asimismo, la hipótesis de distribución uniforme de velocidad en profundidad se cumple habitualmente en
ríos y estuarios, aunque pueden existir zonas en las que dicha hipótesis no se cumpla debido a flujos locales
tridimensionales. En la actualidad, los modelos numéricos basados en las ecuaciones de aguas poco
profundas bidimensionales son los más utilizados en estudios de dinámica fluvial y litoral, evaluación de
zonas inundables, y cálculo de transporte de sedimentos y contaminantes.

**e. Ecuaciones hidrodinámicas**

En el módulo hidrodinámico se resuelven las ecuaciones de conservación de la masa y de momento en las
dos direcciones horizontales:

 _h_   _hU_ _x_  
 _t_  _x_

 _M_

_y_

_h_  _hU_



_t_  _x_

_hU_




_x_  _y_  _M_ _S_

_x_   _hU_ _x_ 2   _hU_ _x_ _U_ _y_   _gh_  _Z_ _s_   _s_, _x_   _b_, _x_  _gh_ 2   2  sin  _U_ _y_   _h_  _xxe_   _h_  _xye_

 _hU_ _x_   _hU_ _x_ 2  
 _t_  _x_

 _x_ _U_ _y_   _gh_  _Zx_ _s_   _s_, _x_   _b_, _x_  _g_ 2 _h_ 2  _x_  2  sin  _U_ _y_   _h_  _x_ _xxe_  

_y_ _x_ _U_ _y_   _gh_  _Zx_ _s_   _s_, _x_   _b_, _x_  _g_ 2 _h_   _x_  2  sin  _U_ _y_   _h_  _x_

 _M_

_y_

 _s_, _x_   _b_, _x_  _gh_   2  sin  _U_   _h_  _xx_  
  2   _x_ _y_  _x_  _y_

_hU_ _x_   _hU_

 _t_  _x_

_x_ 2  _hU_ _x_ _U_ _y_  _Z_ _s_  _s_, _x_  _b_, _x_ _gh_ 2

_hU_ _U_

_h_

 2  sin

2  _x_








_hU_ 

_y_ 

 _t_

_x_ _U_ _y_  

 _x_

_y_ _y_   _gh_  _Zy_ _s_   _s_, _y_   _b_, _y_  _g_ 2 _h_  2  _y_  2  sin  _U_ _x_   _h_



 _e_ 

_xy_ 

 _x_




 _M_

_y_

_hU_

_hU_ _U_

_hU_  _y_   _gh_  _Z_ _s_   _s_, _y_   _b_, _y_  _g_ 2 _h_ 2   2  sin  _U_ _x_  

_hU_

2  _Z_ _s_  _s_, _y_  _b_, _y_ _gh_ 2

_h_



_x_

_X_

_Y_

_t_

_y_   _hU_ _x_ _U_ _y_   _hU_ _y_   _gh_  _Z_ _s_   _s_, _y_   _b_, _y_  _gh_ 2   2  sin  _U_ _x_   _h_  _xye_   _h_  _yye_

_x_

 _b_, _y_  _g_ 2 _h_   _y_  2  sin  _U_ _x_   _x_ _xy_   _y_

 2  sin

2 

en donde _h_ es la profundidad, _U_ _x_, _U_ _y_ son las velocidades horizontales promediadas en profundidad, _g_ es la

aceleración de la gravedad, _Z_ _s_ es la cota de la superficie libre,  _s_ es la fricción en la superficie libre debida

al rozamiento producido por el viento,  b es la fricción debido al rozamiento del fondo, _ρ_ es la densidad del

agua, _Ω_ es la velocidad angular de rotación de la tierra, _λ_ es la latitud del punto considerado,  _[e]_ _xx_,  _[e]_ _xy_,  _[e]_ _yy_
son las tensiones tangenciales efectivas horizontales, y _Ms_, _Mx_, _My_ son respectivamente los términos
fuente/sumidero de masa y de momento, mediante los cuales se realiza la modelización de precipitación,
infiltración y sumideros.

Se incluyen los siguientes términos fuente en las ecuaciones hidrodinámicas:

 - Presión hidrostática,

 - Pendiente del fondo,

 - Tensiones tangenciales viscosas y turbulentas,

 - Rozamiento del fondo,

 - Rozamiento superficial por viento,

 - Precipitación,

 - Infiltración.

Se modelan asimismo los frentes seco-mojado, tanto estacionarios como no estacionarios, que puedan
aparecer en el dominio. Dichos frentes son fundamentales en la modelización de zonas inundables en ríos,
así como en estuarios. De esta forma se introduce la posibilidad de evaluar la extensión de zonas
inundables en ríos, así como el movimiento del frente de marea en estuarios y zonas costeras.

**f. Fricción de fondo**

El fondo ejerce una fuerza de rozamiento sobre el fluido que es equivalente al rozamiento con una pared,
con la particularidad de que, en general, en ingeniería hidráulica la rugosidad del fondo es elevada, como
ocurre en ríos y estuarios.

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

Estudio de Inundación Río Lontué
PFV Halcón Peregrino B4

La fricción del fondo tiene un doble efecto en las ecuaciones de flujo. Por un lado, produce una fuerza de
fricción que se opone a la velocidad media, y, por otro lado, produce turbulencia. Ambos efectos se pueden
caracterizar por la velocidad de fricción _u_ _f_, que no es más que una forma de expresar la tensión tangencial
de fondo con unidades de velocidad:

_u_ _f_   _b_

donde  _b_ es el módulo de la fuerza de fricción de fondo, y _ρ_ es la densidad del agua.

En los modelos promediados en profundidad no es posible calcular la velocidad de fricción por medio de
funciones de pared estándar, tal y como se hace en los contornos tipo pared, ya que las ecuaciones no se
resuelven en la dirección vertical. Por lo tanto, es necesario relacionar la velocidad de fricción _u_ _f_ con la
velocidad media promediada en profundidad mediante un coeficiente de fricción. La tensión de fondo se
puede expresar como:

2 2
 _b_  _u_ _f_    _C_ _f_ _U_

en donde _C_ _f_ es el coeficiente de fricción de fondo. Existen diferentes expresiones que permiten aproximar
el coeficiente de fricción _C_ _f_ . La mayor parte de ellas asumen flujo uniforme en canal con un perfil logarítmico
de velocidad en profundidad.

A diferencia de los modelos unidimensionales (1D), en los modelos bidimensionales (2D) el radio hidráulico
deja de definirse como cociente entre el área de la sección y el perímetro mojados de ésta, ya que en dos
dimensiones (2D) no tiene sentido el definir una sección transversal. Tomando una columna de fluido de
ancho _Δx_ y una profundidad _h_, el radio hidráulico se calcularía como:

_A_  _x_  _h_



_P_  _x_

_A_
_R_ 

 _h_

_x_

_A_  _x_ 

 

_h_   

_P_ _m_  _x_

Por lo tanto, en los modelos 2D es lo mismo hablar de radio hidráulico y de profundidad.

La fricción de fondo se evalúa mediante la fórmula de Manning, la cual utiliza el coeficiente de rugosidad
de Manning _n_ como parámetro. La fórmula relaciona el coeficiente de rugosidad con el coeficiente de
fricción como:

2

_n_
_C_ _f_  _g_

_h_

1 / 3

Anexo 2.7 Estudio de Inundación_Rev.0 **HidroPAS** Ingenieros

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: - Caudal Máximo Instantáneo Adoptado para Río Lontué en PFV Halcón Peregrino.****

| Período de<br>Retorno<br>(años) | Caudal Máximo<br>Inst. (m3/s) |
| --- | --- |
| **5 ** | 1.240 |
| **10** | 1.648 |
| **25** | 2.162 |
| **50** | 2.534 |
| **100** | 2.892 |
| **150** | 3.095 |

**Tabla 3: - Método de Cowan para parámetros de rugosidad (Ven Te Chow)****

| Condiciones del Canal | Col2 | Valores | Col4 |
| --- | --- | --- | --- |
| Material involucrado | Tierra | n0 | 0,020 |
| Material involucrado | Corte en roca | Corte en roca | 0,025 |
| Material involucrado | Grava fina | Grava fina | 0,024 |
| Material involucrado | Grava gruesa | Grava gruesa | 0,028 |
| Grado de irregularidad | Suave | n1 | 0,000 |
| Grado de irregularidad | Menor | Menor | 0,005 |
| Grado de irregularidad | Moderado | Moderado | 0,010 |
| Grado de irregularidad | Severo | Severo | 0,020 |
| Variaciones de la sección transversal | Gradual | n2 | 0,000 |
| Variaciones de la sección transversal | Ocasionalmente alterante | Ocasionalmente alterante | 0,005 |
| Variaciones de la sección transversal | Frecuentemente alterante | Frecuentemente alterante | 0,010-0,015 |
| Efecto relativo de las obstrucciones | Insignificante | n3 | 0,000 |
| Efecto relativo de las obstrucciones | Menor | Menor | 0,010-0,015 |
| Efecto relativo de las obstrucciones | Apreciable | Apreciable | 0,020-0,030 |
| Efecto relativo de las obstrucciones | Severo | Severo | 0,040-0,060 |
| Vegetación | Baja | n4 | 0,005-0,010 |
| Vegetación | Media | Media | 0,010-0,025 |
| Vegetación | Alta | Alta | 0,025-0,050 |
| Vegetación | Muy alta | Muy alta | 0,050-0,100 |
| Grado de los efectos por meandros | Menor | m5 | 1,000 |
| Grado de los efectos por meandros | Apreciable | Apreciable | 1,150 |
| Grado de los efectos por meandros | Severo | Severo | 1,300 |

**Tabla 4: - Rugosidad de Manning del Cauce Principal****

| Parámetro | Col2 | Cauce principal | Col4 |
| --- | --- | --- | --- |
| **Parámetro** | **Parámetro** | **Grado** | **Valor** |
| n0 | Rugosidad base |  | 0,020 |
| n1 | Grado de irregularidad | Moderado | 0,010 |
| n2 | Variaciones de la sección transversal | Ocasionalmente alternante | 0,000 |
| n3 | Efecto de las obstrucciones | Insignificante | 0,000 |
| n4 | Vegetación | Baja | 0,005 |
| m5 | Meandros | Menor | 1,000 |
| **n ** | **Coeficiente de rugosidad** |  | **0,035** |

**Tabla 5: - Rugosidad de Manning del Cauce con vegetación****

| Parámetro | Col2 | Rugosidad de Ribera | Col4 |
| --- | --- | --- | --- |
| **Parámetro** | **Parámetro** | **Grado** | **Valor** |
| n0 | Valor básico de Manning |  | 0,028 |
| n1 | Grado de irregularidad | Menor | 0,005 |
| n2 | Variaciones de la sección transversal | No se Considera | 0,000 |
| n3 | Efecto de las obstrucciones | Insignificante | 0,000 |
| n4 | Vegetación | Media-Alta | 0,025 |
| m5 | Meandros | Menor | 1,000 |
| **n ** | **Coeficiente de rugosidad** |  | **0,058** |

**Tabla 6: - Rugosidad de Manning de zona de Bosque****

| Parámetro | Col2 | Rugosidad con vegetación | Col4 |
| --- | --- | --- | --- |
| **Parámetro** | **Parámetro** | **Grado** | **Valor** |
| n0 | Valor básico de Manning |  | 0,028 |
| n1 | Grado de irregularidad | Menor | 0,005 |
| n2 | Variaciones de la sección transversal | No se Considera | 0,000 |
| n3 | Efecto de las obstrucciones | Insignificante | 0,000 |
| n4 | Vegetación | Muy alta | 0,075 |
| m5 | Meandros | Menor | 1,000 |
| **n ** | **Coeficiente de rugosidad** |  | **0,108** |

**Tabla 7: - Rugosidad de Manning de zonas de Planicie de Inundación****

| Parámetro | Col2 | Rugosidad con vegetación | Col4 |
| --- | --- | --- | --- |
| **Parámetro** | **Parámetro** | **Grado** | **Valor** |
| n0 | Valor básico de Manning |  | 0,028 |
| n1 | Grado de irregularidad | Menor | 0,005 |
| n2 | Variaciones de la sección transversal | No se Considera | 0,000 |
| n3 | Efecto de las obstrucciones | Menor | 0,015 |
| n4 | Vegetación | Media | 0,015 |
| m5 | Meandros | Menor | 1,000 |
| **n ** | **Coeficiente de rugosidad** |  | **0,063** |

**Tabla 8: - Clasificación FEMA del riesgo por inundación****

| Categoría de peligro de<br>la inundación | Rango Profundidad x<br>Velocidad<br>[m2/s] |
| --- | --- |
| Bajo | <0,2 |
| Medio | 0,2 - 0,5 |
| Alto | 0,5 - 1,5 |
| Muy Alto | 1,5 - 2,5 |
| Extremo | > 2,5 |
