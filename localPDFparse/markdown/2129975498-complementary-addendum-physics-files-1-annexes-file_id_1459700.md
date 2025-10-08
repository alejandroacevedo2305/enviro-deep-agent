---
title: Sin título
author: AZapata
date: D:20150515102922-03'00'
language: es
type: report
pages: 15
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO N° 12 ESTUDIO DE DISTRIBUCIÓN DE ESPECIES SINGULARES Y EN CATEGORÍA DE CONSERVACIÓN
-->

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

# ANEXO N° 12 ESTUDIO DE DISTRIBUCIÓN DE ESPECIES SINGULARES Y EN CATEGORÍA DE CONSERVACIÓN

**Rosario Norte 100 Piso 14, Las Condes, Santiago, Chile. Fono: 562-2580 6500;**

**e-mail: contacto@sgasa.cl;** **www.sgasa.cl**

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**INDICE**
1 INTRODUCCIÓN ................................................................................................................................ 1

2 METODOLOGÍA ................................................................................................................................. 1

2.1 Determinación de especies focales .......................................................................................... 1

2.2 Obtención de registros de presencia de las especies .............................................................. 1

2.3 Obtención de variables ambientales ........................................................................................ 2

2.4 Modelamiento de la distribución ............................................................................................. 2

2.5 Cálculo de áreas de distribución .............................................................................................. 2

3 RESULTADOS .................................................................................................................................... 2

4 CONCLUSIONES .............................................................................................................................. 12

5 BIBLIOGRAFÍA ................................................................................................................................. 13

**INDICE DE TABLAS**

Tabla 1. Especies en el área de influencia con problemas de conservación ............................................ 1
Tabla 2. Estimación de áreas de distribución de las especies en estudio ................................................ 3

**INDICE DE FIGURAS**

Figura 1. Resultados para _Galictis cuja_ (quique). ..................................................................................... 6
Figura 2. Resultados para _Lycalopex culpaeus_ (zorro culpeo). ................................................................ 7
Figura 3. Resultados para _Lycalopex griseus_ (zorro chilla). ...................................................................... 8
Figura 4. Resultados para _Octodon degus_ (degú). ................................................................................... 9
Figura 5. Resultados para _Pelurodema thaul_ (sapito de cuatro ojos). ................................................... 10

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación i

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**1** **INTRODUCCIÓN**

El presente informe da cuenta de los resultados de la caracterización de la distribución de especies de
Fauna Terrestre singulares y/o en categoría de conservación que fueron registradas en el área de
influencia del Proyecto "Parque Fotovoltaico Limache", durante los levantamientos de terreno de
línea base.

La metodología de estudio se basa en la utilización de registros de presencia de las especies, las
cuales permiten caracterizar su nicho ambiental, y el uso de capas de información ambiental (shapes
y rásters) que entregan el entorno ambiental. Cada ocurrencia de una especie se relaciona con un
pixél que contiene información ambiental, de esta forma, el programa de modelamiento (MaxEnt)
obtiene un consenso del rango de cada variable ambiental que la especie prefiere (maximizando la
entropía).

De esta forma, es posible identificar aquellos sectores donde las especies probablemente prefieran

establecerse.

**2** **METODOLOGÍA**

**2.1** **D** **ETERMINACIÓN DE ESPECIES FOCALES**

Para la inclusión de especies registradas durante los levantamientos de terreno del Proyecto dentro
de este estudio, se consideró la singularidad de éstas y sus categorías de conservación. A
continuación se detallan las especies singulares y aquellas listadas en alguna categoría de
conservación según la legislación vigente y que fueron detectadas en el área de influencia del

Proyecto.

**Tabla 1. Especies en el área de influencia con problemas de conservación**

|Nombre científico|Nombre común|Estado de conservación|Criterio|
|---|---|---|---|
|_Octodon degus_|degú|*|*|
|_Galictis cuja_|quique|VU|Ley de Caza|
|_Lycalopex griseus_|zorro chilla|LC|RCE|
|_Lycalopex culpaeus_|zorro rojo o culpeo|LC|RCE|
|_Liolaemus lemniscatus_|lagartija lemniscata|LC|RCE|
|_Pleurodema thaul_|sapito de cuatro ojos|NT|RCE|

_Fuente: Levantamiento de terreno._

_*: No listada, pero incluida en el listado por tratarse de una especie singular._

**2.2** **O** **BTENCIÓN DE REGISTROS DE PRESENCIA DE LAS ESPECIES**

Para la obtención de registros de presencia de cada especie se procedió a revisar el Global
Biodiversity Information Facility (GBIF, www.gbif.org) y el geoportal de datos de biodiversidad chileno

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 1

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

gestionado por la Pontificia Universidad Católica de Chile y Microsoft (LiveAndes,
www.liveandes.org), además de bases de datos internas del consultor.

**2.3** **O** **BTENCIÓN DE VARIABLES AMBIENTALES**

Para la obtención de variables ambientales se descargaron imágenes satelitales desde EarthExplorer,
plataforma administrada por el United States Geological Survey (USGS). Desde este buscador se
localizaron imágenes del satélite Landsat 8 que posee 30 metros de resolución por píxel. Mediante
esta imagen satelital se creó una imagen en color real y un Índice de Diferencia de Vegetación
Normalizada (NDVI), el cual permite evaluar en cada píxel el nivel de productividad vegetacional
existente. Estas variables ambientales fueron complementadas con información bioclimática (Hijmans
et al. 2005; www.worldclim.org) y geomorfológica, incluyendo promedio de precipitación anual,
promedio de temperatura anual, elevación y pendiente, entre otras variables.

**2.4** **M** **ODELAMIENTO DE LA DISTRIBUCIÓN**

Para el desarrollo del modelo de cada especie se obtuvo un set de datos consenso a partir de las
fuentes de información evaluadas. Este set de datos es cargado en el programa MaxEnt junto a las
variables a utilizar. El programa de modelamiento MaxEnt (Phillips et al. 2006) ha sido ampliamente
utilizado para la caracterización de la distribución de especies en el mundo, y su uso se recomienda ya
que para su implementación sólo requiere información sobre la presencia de las especies (Elith et al.
2006; Hijmans & Graham 2006). Este programa usa un algoritmo de máxima entropía para encontrar
la probabilidad de distribución más cercana a la uniformidad, en base a la caracterización que realiza
relacionando las ocurrencias de la especie sobre el espacio ambiental proporcionado (variables
ambientales utilizadas).

**2.5** **C** **ÁLCULO DE ÁREAS DE DISTRIBUCIÓN**

Para este procedimiento se descargó desde la web de la IUCN la información espacial de distribución
de cada una de las especies focales. Esta distribución fue trabajada en un programa de SIG (Quantum
GIS) para obtener la distribución en Chile, mediante la herramienta de intersección un shapefile de la
cobertura de Chile. Este procedimiento se repitió a nivel de región con el mismo propósito. A cada
área se le restó el área estimada de sitios antrópicos correspondiente a la localidad siguiendo la
metodología de Pliscoff et al. (2014). Finalmente, se calculó la representatividad de hábitat de cada
especie del Proyecto expresadas en porcentajes.

**2.6** **E** **VALUACIÓN DE RELACIÓN ENTRE COMPONENTE SUELOS Y FAUNA VERTEBRADA**

Una vez determinadas y cuantificadas las áreas de distribución de las especies de fauna vertebrada
terrestre existentes en el área de influencia del Proyecto, se realizó un análisis respecto a la clase de
suelo presentes, su relación con las especies y la representatividad de estas a nivel regional,
considerando la información generada en la línea de base de Suelo (Cap. XX del EIA).

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 2

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**3** **RESULTADOS**

**3.1** **M** **ODELAMIENTO DE DISTRIBUCIÓN DE ESPECIES**

La obtención de registros por especie reunió un total de 909 presencias, distribuidas de la siguiente
forma: 407 ocurrencias de _Galictis cuja_, 280 ocurrencias de _Pleurodema thaul_, 105 ocurrencias de
_Lycalopex culpaeus_, 69 de _Octodon degus_ y 48 de _Lycalopex griseus_ . La mayor representatividad en
número de ocurrencias de la especie _G. cuja_ se explica debido a la reciente publicación de un análisis
histórico de esta especie (Poo-Muñoz et al. 2014).

La estimación de áreas de distribución a partir de la IUCN por especie se resume en la siguiente tabla:

**Tabla 2. Estimación de áreas de distribución de las especies en estudio**

|Especie|Área (ha) en<br>Chile|Área (ha)<br>V Región|Área (ha) sin<br>sectores de<br>Influencia<br>antrópica|Representatividad a<br>nivel nacional|
|---|---|---|---|---|
|_Pleurodema thaul_|25.194.847|1.306.831|1.306.831|5.19%|
|_Octodon degus_|6.468.712|1.247.759|1.247.759|19.29%|
|_Lycalopex griseus_|34.257.410|961.491|961.491|2.81%|
|_Galictis cuja_|21.092.601|1.577.095|1.577.095|7.48%|
|_Lycalopex culpaeus_|51.210.484|890.171|890.171|1.74%|
|_Liolaemus_<br>_lemniscatus_|16.019.850|1.601.007|1.601.007|9.99%|

_Fuente: Elaboración propia._

Los resultados del modelamiento de distribución de cada especie permitieron identificar aquellas
áreas en que con mayor probabilidad se puede registrar la presencia de la especie o de condiciones
de hábitat que esta utilice. En cuanto a los mamíferos, la distribución conocida por la IUCN de _Galictis_
_cuja_ se superpone espacialmente con la distribución modelada, demostrando el poder predictivo de
éste. El análisis realizado de áreas de distribución permitió identificar que la especie posee un total de
20.831.637 hectáreas disponibles a nivel país, mientras que a nivel de la V región posee 1.316.131
hectáreas, correspondientes a un 6.2% de la distribución nacional. A nivel de Proyecto, el análisis de
modelamiento nos permitió identificar que la especie existe en el área de influencia con una
probabilidad promedio de 0.72, lo cual es un rango alto considerando que la probabilidad máxima
obtenida de presencia de la especie para toda el área de estudio (Sudamérica) fue de 0.89. Este
análisis permite identificar que el área de influencia del Proyecto representa en su totalidad hábitat
de la especie. Sin embargo, incluso aún cuando se consideró las áreas antrópicas en este análisis
como zona de exclusión del estudio, podemos observar que el área del Proyecto (30,81 ha)
representa sólo un 0.002% a nivel regional y 0.0001% a nivel nacional, del total del hábitat disponible
para la especie.

El zorro culpeo ( _Lycalopex culpaeus_ ) posee una distribución conocida por la IUCN que se superpone
espacialmente con la distribución modelada, demostrando el poder predictivo de este estudio.

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 3

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

Nuestro análisis de áreas de distribución permitió identificar que la especie posee un total de
51.210.484 hectáreas disponibles a nivel país, mientras que a nivel de la V región posee 890.171
hectáreas, correspondientes a un 1.2% de la distribución nacional. A nivel de Proyecto, el análisis de
modelamiento permitió identificar que la especie existe en el área de influencia con una probabilidad
promedio de 0.76, lo cual es un rango alto considerando que la probabilidad máxima obtenida de
presencia de la especia para toda el área de estudio (Sudamérica) fue de 0.92. Este análisis permite
identificar que el área de influencia del Proyecto representa en su totalidad hábitat de la especie. Sin
embargo, incluso aún cuando se consideró las áreas antrópicas en este análisis como zona de
exclusión del estudio, podemos observar que el área del Proyecto (30,81 ha) representa sólo un
0.003% a nivel regional y 0.00006% a nivel nacional del total de hábitat disponible para la especie.

El zorro chilla ( _Lycalopex griseus_ ) posee una distribución conocida por la IUCN que se superpone
espacialmente con la distribución modelada, demostrando el poder predictivo de este estudio.
Nuestro análisis de áreas de distribución permitió identificar que la especie posee un total de
34.257.410 hectáreas disponibles a nivel país, mientras que a nivel de la V región posee 961.491
hectáreas, correspondientes a un 2% de la distribución nacional. A nivel de Proyecto, el análisis de
modelamiento permitió identificar que la especie existe en el área de influencia con una probabilidad
promedio de 0.41, lo cual es un rango bajo de probabilidad considerando que la probabilidad máxima
obtenida de presencia de la especia para toda el área de estudio (Sudamérica) fue de 0.87. Este
análisis permitió identificar que el área de influencia del Proyecto representa más bien un hábitat
poco idóneo para la especie, y que su registro podría considerarse anecdótico. Sin embargo,
considerando la información de la distribución de la IUCN, el área del Proyecto está incluida dentro de
la distribución regional de la especie. Finalmente, cuando se consideró las áreas antrópicas en este
análisis como zona de exclusión del estudio, se obtuvo como resultado que el área del Proyecto
(30,81 ha) representa sólo un 0.003% a nivel regional y 0.00008% a nivel nacional, del total de hábitat
disponible para la especie.

El degú _(Octodon degus_ ) posee una distribución conocida por la IUCN que se superpone
espacialmente con la distribución modelada, demostrando el poder predictivo de este estudio.
Nuestro análisis de áreas de distribución permitió identificar que la especie posee un total de
6.468.712 hectáreas disponibles a nivel país, mientras que a nivel de la V región posee 1.247.759
hectáreas, correspondientes a un 15.3% de la distribución nacional. A nivel de Proyecto, nuestro
análisis de modelamiento nos permitió identificar que la especie existe en el área de influencia con
una probabilidad promedio de 0.71, lo cual es un rango alto considerando que la probabilidad
máxima obtenida de presencia de la especia para toda el área de estudio (Sudamérica) fue de 0.81.
Este análisis permite identificar que el área de influencia del Proyecto representa en su totalidad
hábitat de la especie. Sin embargo, incluso aún cuando se consideró las áreas antrópicas en este
análisis como zona de exclusión del estudio, se observa que el área del Proyecto (30,81 ha)
representa sólo un 0.002% a nivel regional y 0.0005% a nivel nacional, del total del hábitat disponible
para la especie.

El sapito de cuatro ojos ( _Pleurodema thaul_ ) posee una distribución conocida por la IUCN que se
superpone espacialmente con la distribución modelada, demostrando el poder predictivo de este
estudio. Nuestro análisis de áreas de distribución permitió identificar que la especie posee un total de
25.194.847 de hectáreas disponibles a nivel país, mientras que a nivel de la V región posee 1.306.831

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 4

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

hectáreas, correspondientes a un 10.1% de la distribución nacional. A nivel de Proyecto, el análisis de
modelamiento nos permitió identificar que la especie no existe habitualmente en el área de
influencia, sin embargo, tanto la IUCN como nuestra caracterización en terreno permitió definir que la
especie si existe en el área de influencia del Proyecto, al menos durante la época reproductiva, la cual
coincide con el periodo en que se realizo la visita a terreno.

Finalmente, respecto a la lagartija lemniscata ( _Liolaemus lemniscatus_ ) no fue posible obtener
modelos de distribución debido a la inexistencia de registros de presencias de la especie en ninguna
de las bases de datos consultados. Este corresponde a un resultado común con especies
cosmopolitas, con amplia distribución en el país, y una relativa alta frecuencia de avistamiento (Mella,
2005), disminuyendo de esta forma el interés por su investigación. Sin embargo, en la ficha de la
especie elaborada por el MMA se adjunta una figura correspondiente a un modelo de la distribución
que permite estimar que el área disponible para esta especie a nivel país corresponde a 16.019.850
hectáreas. Por otra parte, una simple extrapolación de este mapa permite identificar que la totalidad
de la región representa hábitat de la especie.

A continuación se adjuntan cartografías en que se grafican los resultados del estudio por especie:

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 5

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**Figura 1. Resultados para** _**Galictis cuja**_ **(quique).**

_Fuente: Elaboración propia a partir del estudio de distribución. Elaboración en Quantum GIS. A: Mapa de la distribución de la_

_especie de acuerdo a la IUCN. B: Resultado del modelamiento de la especie. C: Zoom de la distribución de la especie en la V_
_Región de acuerdo a la IUCN. D: Zoom de la distribución IUCN de la especie en el área de intervención del proyecto. E: Zoom_

_de la distribución modelada de la especie en el área de intervención del Proyecto._

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 6

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**Figura 2. Resultados para** _**Lycalopex culpaeus**_ **(zorro culpeo).**

_Fuente: Elaboración propia a partir del estudio de distribución. Elaboración en Quantum GIS. A: Mapa de la distribución de la_

_especie de acuerdo a la IUCN. B: Resultado del modelamiento de la especie. C: Zoom de la distribución de la especie en la V_
_Región de acuerdo a la IUCN. D: Zoom de la distribución IUCN de la especie en el área de intervención del proyecto. E: Zoom_

_de la distribución modelada de la especie en el área de intervención del Proyecto._

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 7

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**Figura 3. Resultados para** _**Lycalopex griseus**_ **(zorro chilla).**

_Fuente: Elaboración propia a partir del estudio de distribución. Elaboración en Quantum GIS. A: Mapa de la distribución de la_

_especie de acuerdo a la IUCN. B: Resultado del modelamiento de la especie. C: Zoom de la distribución de la especie en la V_
_Región de acuerdo a la IUCN. D: Zoom de la distribución IUCN de la especie en el área de intervención del proyecto. E: Zoom_

_de la distribución modelada de la especie en el área de intervención del Proyecto._

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 8

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**Figura 4. Resultados para** _**Octodon degus**_ **(degú).**

_Fuente: Elaboración propia a partir del estudio de distribución. Elaboración en Quantum GIS. A: Mapa de la distribución de la_

_especie de acuerdo a la IUCN. B: Resultado del modelamiento de la especie. C: Zoom de la distribución de la especie en la V_
_Región de acuerdo a la IUCN. D: Zoom de la distribución IUCN de la especie en el área de intervención del proyecto. E: Zoom_

_de la distribución modelada de la especie en el área de intervención del Proyecto._

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 9

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**Figura 5. Resultados para** _**Pelurodema thaul**_ **(sapito de cuatro ojos).**

_Fuente: Elaboración propia a partir del estudio de distribución. Elaboración en Quantum GIS. A: Mapa de la distribución de la_

_especie de acuerdo a la IUCN. B: Resultado del modelamiento de la especie. C: Zoom de la distribución de la especie en la V_
_Región de acuerdo a la IUCN. D: Zoom de la distribución IUCN de la especie en el área de intervención del proyecto. E: Zoom_

_de la distribución modelada de la especie en el área de intervención del Proyecto._

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 10

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**3.2** **A** **NÁLISIS DE RELACIÓN ENTRE COMPONENTES SUELO Y** **F** **AUNA** **T** **ERRESTRE**

Durante los levantamientos de terreno del componente suelo se observó las siguientes clases de
suelo en el área de influencia del Proyecto, cuya representatividad a nivel regional además se
describe en la siguiente tabla.

**Tabla 3. Estimación de áreas de distribución de las especies en estudio**

|Clase de Suelo|Superficie en el<br>Proyecto (ha)|Superficie en la Región<br>(ha)*|% Proyecto respecto a<br>la Región|
|---|---|---|---|
|III|0,086|157.630|0,00005|
|IV|0,636|64.583|0,00098|
|VII|0,705|373.120|0,00019|
|Miscelaneo Coluvial<br>(Clase VII)|0,505|15.405|0,00328|
|**TOTAL**|1,931|610.738|0,00032|

_Fuente: Elaboración propia._

La clase de suelo III está representada en el área de influencia del Proyecto por un sector con uso de
suelo actual de camino árboles introducidos laterales (calicata 4), praderas sin uso agrícola (calicata 8)
y sectores de uso agrícola (Calicatas 5 y 6). Esta clase de suelo sólo estuvo asociada a la presencia de
aves que hacen uso de estos sectores como percha (árboles de borde de camino) o sitios de
alimentación (pradera sin uso agrícola). Por otra parte, sectores de uso agrícola no representan
hábitat natural de especies de fauna vertebrada.

La clase de suelo IV está representada por sectores con uso de suelo caracterizado por la presencia de
praderas naturales en bosque de espino (calicatas 1, 2 y 8). Estos sectores presentaron una baja
presencia de especies de reptiles y micromamíferos.

La clase de suelo VII está representada por praderas naturales sin uso agrícola, y se encuentran
actualmente asociadas a bosque de espino. Estos sectores presentan las mismas características que la
clase de suelo IV a nivel de hábitats para la fauna.

El suelo de características misceláneo coluvial, está asociado al hábitat de bosque de quebradas, en
donde se presenta un hábitat de refugio y alimentación para especies de reptiles, micromamíferos y
aves observados en las campañas de terreno.

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 11

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**4** **CONCLUSIONES**

Durante los levantamientos de terreno realizados en el área de influencia del Proyecto se determinó
la existencia de 6 especies singulares y/o en categoría de conservación. Estas especies corresponden
a los mamíferos _Octodon degus_ (degu común), _Lycalopex griseus_ (zorro chilla), _L. culpaeus_ (zorro
culpeo), _Galictis cuja_ (quique), el reptil _Liolaemus lemniscatus_ (lagartija lemniscata) y el anfibio
_Pleurodema thaul_ (sapito de cuatro ojos), y se presentan en el hábitat asociado a bosque de
quebradas.

Con el objetivo de describir la relación del Proyecto con el hábitat disponible para cada una de las
especies, se realizaron modelaciones de distribución para cada una de las especies, utilizando
registros de ocurrencia e información ambiental obtenidos de diversas fuentes. Los resultados
indicaron que para la totalidad de las especies fue posible estimar el área de distribución nacional,
regional y a nivel de Proyecto.

A partir de los resultados presentados en el presente documento, se concluye que:

- La superficie de suelo que se verá afectada por la implementación del Proyecto corresponde
a un máximo del 0,003% del total del hábitat disponible para las especies focales del estudio a nivel
regional.

- Si bien se registró la presencia de especies singulares, en los hábitat de bosque de quebrada,
durante el levantamiento de información de línea base, al menos el zorro culpeo, el zorro chilla y el
quique serían especies de hábitos generalistas y de amplia movilidad, lo que les permitiría tener una
alta capacidad de resiliencia ante perturbaciones ambientales. En la zona existen hábitats similares y
disponibles, no afectando de manera significativa su ámbito de vida.

De acuerdo a los resultados presentados en el presente estudio, se estima que la ejecución del
Proyecto no afectará de forma significativa el suelo y su capacidad de sustento para la componente
fauna terrestre. Esto se justifica debido a la baja afectación directa del suelo por parte del Proyecto
(1,93 ha de pérdida de suelo), que la superficie del mismo intervendrá un área pequeña en relación
los hábitat de características similares que están disponibles a nivel regional, las especies poseen una
disponibilidad real de hábitat a utilizar en los alrededores del Proyecto, correspondientes a bosques
de quebrada.

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 12

|Col1|ADENDA N°1|Col3|
|---|---|---|
||PROYECTO PARQUE SOLAR LIMACHE|PROYECTO PARQUE SOLAR LIMACHE|

**5** **BIBLIOGRAFÍA**

 - Elith, J. et al., 2006. Novel methods improve prediction of species’ distributions from
occurrence data. Ecography, 29(2), pp.129-151. Available at:
http://doi.wiley.com/10.1111/j.2006.0906-7590.04596.x [Accessed July 11, 2014].

 - Hijmans, R.J. et al., 2005. Very high resolution interpolated climate surfaces for global land
areas. International Journal of Climatology, 25(15), pp.1965-1978. Available at:
http://doi.wiley.com/10.1002/joc.1276 [Accessed July 9, 2014].

 - Hijmans, R.J. & Graham, C.H., 2006. The ability of climate envelope models to predict the
effect of climate change on species distributions. Global Change Biology, 12(12), pp.22722281. Available at: http://doi.wiley.com/10.1111/j.1365-2486.2006.01256.x [Accessed July
10, 2014].

 - Phillips, S.J., Anderson, R.P. & Schapire, R.E., 2006. Maximum entropy modeling of species
geographic distributions. Ecological Modelling, 190(3-4), pp.231-259. Available at:
http://linkinghub.elsevier.com/retrieve/pii/S030438000500267X [Accessed July 9, 2014].

 - Pliscoff, P. et al., 2014. Effects of alternative sets of climatic predictors on species distribution
models and associated estimates of extinction risk: A test with plants in an arid environment.
Ecological Modelling, 288, pp.166-177. Available at:
http://dx.doi.org/10.1016/j.ecolmodel.2014.06.003.

 - Poo-Muñoz, D. a. et al., 2014. Galictis cuja (Mammalia): an update of current knowledge and
geographic distribution. Iheringia. Série Zoologia, 104(July 2013), pp.341-346. Available at:
http://www.scielo.br/scielo.php?script=sci_arttext&pid=S007347212014000300010&lng=en&nrm=iso&tlng=en.

Anexo 12 - Estudio de Distribución de Especies Singulares y en Categoría de Conservación 13

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Especies en el área de influencia con problemas de conservación****

| Nombre científico | Nombre común | Estado de conservación | Criterio |
| --- | --- | --- | --- |
| _Octodon degus_ | degú | * | * |
| _Galictis cuja_ | quique | VU | Ley de Caza |
| _Lycalopex griseus_ | zorro chilla | LC | RCE |
| _Lycalopex culpaeus_ | zorro rojo o culpeo | LC | RCE |
| _Liolaemus lemniscatus_ | lagartija lemniscata | LC | RCE |
| _Pleurodema thaul_ | sapito de cuatro ojos | NT | RCE |

**Tabla 2.: Estimación de áreas de distribución de las especies en estudio****

| Especie | Área (ha) en<br>Chile | Área (ha)<br>V Región | Área (ha) sin<br>sectores de<br>Influencia<br>antrópica | Representatividad a<br>nivel nacional |
| --- | --- | --- | --- | --- |
| _Pleurodema thaul_ | 25.194.847 | 1.306.831 | 1.306.831 | 5.19% |
| _Octodon degus_ | 6.468.712 | 1.247.759 | 1.247.759 | 19.29% |
| _Lycalopex griseus_ | 34.257.410 | 961.491 | 961.491 | 2.81% |
| _Galictis cuja_ | 21.092.601 | 1.577.095 | 1.577.095 | 7.48% |
| _Lycalopex culpaeus_ | 51.210.484 | 890.171 | 890.171 | 1.74% |
| _Liolaemus_<br>_lemniscatus_ | 16.019.850 | 1.601.007 | 1.601.007 | 9.99% |

**Tabla 3.: Estimación de áreas de distribución de las especies en estudio****

| Clase de Suelo | Superficie en el<br>Proyecto (ha) | Superficie en la Región<br>(ha)* | % Proyecto respecto a<br>la Región |
| --- | --- | --- | --- |
| III | 0,086 | 157.630 | 0,00005 |
| IV | 0,636 | 64.583 | 0,00098 |
| VII | 0,705 | 373.120 | 0,00019 |
| Miscelaneo Coluvial<br>(Clase VII) | 0,505 | 15.405 | 0,00328 |
| **TOTAL** | 1,931 | 610.738 | 0,00032 |
