---
title: Sin título
author: Pablo
date: D:20200318170641-03'00'
language: es
type: report
pages: 34
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. INTRODUCCIÓN
  - 1 Extraído de la DIA original “Modificación Planta de tratamiento de RILes”. Noviembre de 2019.
  - 2. MODELACIÓN DE VARIABLES METEOROLÓGICAS
  - 3. CÁLCULO DE INCERTIDUMBRE
  - 4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE
  - 5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS
  - 6. RESULTADOS DEL MODELO DE DISPERSIÓN Y ANÁLISIS DE IMPACTO POR
  - 7. CONCLUSIONES
-->

**Modelación de**

**Dispersión e Impacto**

**por Olores**

Viña Requingua

**Santiago - Chile**

**Marzo 2020**

**CONFIDENCIAL**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**CONTENIDO**

1. INTRODUCCIÓN ..................................................................................................................................................... 2

2. MODELACIÓN DE VARIABLES METEOROLÓGICAS ..................................................................................................... 3

3. CÁLCULO DE INCERTIDUMBRE .............................................................................................................................. 12

4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE ....................................................................... 18

5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS ............................................................................ 19

6. RESULTADOS DEL MODELO DE DISPERSIÓN Y ANÁLISIS DE IMPACTO POR OLORES .................................................. 26

8. CONCLUSIONES ................................................................................................................................................... 29

Página **1** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

# 1. INTRODUCCIÓN

El presente informe da cuenta de los resultados obtenidos de la modelación de dispersión de olores y los

impactos asociados al proyecto “Modificación Planta de Tratamiento de Riles”, presentado ante el SEA por

Agrícola Requingua Limitada, para su evaluación.

Las instalaciones del proyecto se ubican en el Fundo Requingua, Ruta K-156 S/N, Comuna de Sagrada

Familia, Provincia de Curicó, VII Región del Maule. El proyecto se ubica en una zona rural sin regulación del

Plan Regulador Comunal [1] .

**Tabla 1.** Coordenadas punto representativo del proyecto (Datum WGS 84).

|Coordenadas UTM del Proyecto.|Col2|
|---|---|
|Coordenada Este (m)|Coordenada Norte (m)|
|286244|6121209|

Las principales actividades llevadas a cabo en Viña Requingua son la producción y cosecha de uva para la

posterior elaboración de vino. Viña Requingua cuenta con distintos tipos de vino que son comercializados

a nivel nacional e internacional. Cuenta con una capacidad de guarda de 30 millones de litros de vino, en

cubas de diversos tamaños además de barricas de roble [ 2] .

____________________________________________________

# 1 Extraído de la DIA original “Modificación Planta de tratamiento de RILes”. Noviembre de 2019.

2 [http://www.requingua.com](http://www.requingua.c/)

Página **2** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

# 2. MODELACIÓN DE VARIABLES METEOROLÓGICAS

Para la generación de la base de datos de variables meteorológicas, se utilizó el modelo WRF versión 4.0.3.
Éste es un modelo meteorológico de alta resolución, desarrollado para la simulación de variables

meteorológicas, mediante la resolución de las ecuaciones físicas que describen los movimientos de la

atmósfera, utilizando aproximaciones basadas en métodos numéricos. Este modelo se encuentra en

constante desarrollo y mejora por medio de una asociación colaborativa, principalmente entre el National

Center for Atmospheric Research (NCAR, USA), National Oceanic and Atmospheric Administration (NCEP,

USA), Forecast Systems Laboratory (FSL, USA), Air Force Weather Agency (AFWA, USA), el Naval Research

Laboratory, University of Oklahoma, y la Federal Aviation Administration (FAA, USA). WRF es un Software

Libre y comunitario, por lo que su desarrollo y mejoramiento se realiza en distintos sitios alrededor del
mundo por voluntarios que deseen contribuir al proyecto [3] .

En el presente informe se utilizó la información meteorológica correspondiente al último año

meteorológico completo y validado a la fecha (2019). Esta información se obtuvo a partir del CISL Research

Data Archive (NCAR, USA), utilizándose el conjunto de datos de entrada ds083.2. NCAR (National Center

for Atmospherical Reseach) ofrece a los científicos de Estados Unidos y del mundo, una gran cantidad de

herramientas, desde modelos comunitarios hasta aviones de investigación, supercomputadores y

talleres. Los científicos internos de NCAR colaboran con sus colegas en el mundo académico, el gobierno y

el sector privado para construir, refinar y ampliar los recursos de la comunidad de NCAR para que sean lo
más relevantes y útiles posible. [4]

Para el área de influencia, la configuración del modelo WRF, comprendió la parametrización de variables

propias de los fenómenos de micro escala que inciden en la dispersión de los contaminantes, esto es:

parametrizaciones de microfísica de nubes, fenómenos radiativos, altura de la capa de mezcla y fenómenos

turbulentos causados por la orografía. En la Tabla 2 se detallan las configuraciones de importancia con las

cuales se ejecutó la modelación.

____________________________________________________

3 [The Weather Research & Forecasting Model, NCAR/UCAR, https://www.mmm.ucar.edu/weather-research-and-forecasting-](https://www.mmm.ucar.edu/weather-research-and-forecasting-model)

model

4 [National Center for Atmospheric Research, NCAR/UCAR, https://ncar.ucar.edu/what-we-offer](https://ncar.ucar.edu/what-we-offer)

Página **3** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

|Tabla 2. Configuración física del mode|elo WRF 4.0.3, dominio más pequeño.|
|---|---|
|Centro Latitud|-35.038538|
|Centro Longitud|-71.338829|
|Condiciones de entrada|FNL DS083.2 2019|
|Proyección cartográfica|Mercator|
|Puntos en X|15|
|Puntos en Y|15|
|Topografía|SRTM3 (Aproximadamente 100 metros)|
|Uso de suelo|USGS (Aproximadamente 1 Kilómetro)|
|Resolución horizontal (Km)|0,5|
|Resolución vertical (niveles)|27 niveles hasta 10 hPa <br>|
|Microfísica|~~“WRF Single-Moment 8-class scheme”.~~<br>Esquema microfísico de 8 clases, que<br>incorpora además de líquidos, hielo y nieve.<br>Parametrización ideal para simulaciones a<br>alta resolución. <br>|
|Radiación (Onda larga y Corta)|~~“RRTMG”. Esquema radiativo simple y~~<br>eficiente, capaz de simular los fenómenos<br>radiativos de onda larga a través del<br>solapamiento de capas nubosas. <br>|
|Modelo de suelo|~~“ETA Similarity”. Esquema fenómenos suelo-~~<br>atmósfera ampliamente utilizado por otros<br>modelos numéricos además de WRF, basado<br>en Monin-Obukhov (esquema requerido por<br>el modelo de dispersión) que incorpora la<br>longitud de rugosidad térmica Zilitinkevich y<br>funciones de similitud estándar desde tablas<br>predefinidas. <br>|
|Interacción suelo atmósfera|~~“Noah Land Surface Model”. Esquema~~<br>utilizado por NCEP/NCAR/AFWA que<br>incorpora temperatura y humedad del suelo<br>en cuatro capas. <br>|
|Capa planetaria|~~“Mellor-Yamada- Janjic”. Ampliamente~~<br>utilizado operacionalmente por otros<br>modelos además de WRF. Basado en un<br>régimen turbulento unidimensional de<br>energía cinética vertical local.|

Página **4** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

El dominio más pequeño definido, considera una zona de 15x15 kilómetros, con un dominio superior

de 75x75 kilómetros y otro principal de 375x375 kilómetros, los que se consideran lo suficientemente

amplios como para incorporar fenómenos de escala sinóptica, propios de la zona como los sistemas

frontales o la incursión de altas frías migratorias, configurado además a una alta resolución de 500

metros en su dominio más pequeño, con la capacidad de incorporar fenómenos de mesoescala como

oscilaciones en la capa altura de la mezcla por efecto radiativo o fenómenos de intercambio turbulento

causados por la orografía. En la Figura 1, Figura 2 y Figura 3, se presentan detalles del dominio

considerado en la modelación.

**Figura 1.** Emplazamiento geográfico del dominio considerado para la modelación de variables
meteorológicas y de dispersión.

Página **5** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 2.** Detalle del dominio considerado para la modelación de variables meteorológicas y de
dispersión, información topográfica utilizada por el modelo (SRTM3 a 90 metros de resolución).

Página **6** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 3.** Grilla de modelación de 60x60, a 500 metros de resolución espacial, definiendo un dominio de
30x30 kilómetros de extensión. Se observan, además, los distintos usos de suelo considerados.

De este modo, se logró tener una base de datos de variables meteorológicas para el área de interés, con

resolución horizontal de 500x500 metros, con una grilla de 60x60 para 27 niveles de altitud llegando al

tope de la atmósfera y resolución temporal de una hora para todo 2018, información requerida como base

por el modelo de dispersión.

A continuación, en la **Figura 4**, **Figura 5**, **Figura 6** y **Figura 7** se muestran los campos de vientos

característicos de la zona para las estaciones del año cálidas durante el período diurno y el período

nocturno, como también los campos de vientos característicos de la zona para las estaciones del año frías

durante el período diurno y nocturno.

Página **7** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 4.** Campos de vientos durante el período diurno en estaciones cálidas. Se observa el efecto brisa

valle-montaña, desde el noroeste.

Página **8** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 5.** Campos de vientos durante el período nocturno en estaciones cálidas. Se observa el sentido
contrario del régimen de vientos respecto al día (efecto brisa montaña-valle).

Página **9** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 6.** Campos de vientos durante el período diurno en estaciones frías. Se observa un decrecimiento
en la magnitud respecto al viento diurno durante el período cálido y una rotación desde el suroeste, ésta
es la situación predominante del viento.

Página **10** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 7.** Campos de vientos durante el período nocturno en estaciones frías. Se observa un ligero
incremento en la magnitud respecto al viento nocturno durante el período frío.

Página **11** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

# 3. CÁLCULO DE INCERTIDUMBRE

Para el cálculo de incertidumbre, la estación más cercana con información pública disponible corresponde a la

estación de monitoreo Sagrada Familia, propiedad de la Fundación para el Desarrollo Frutícola, y perteneciente a la

Red Agromet, cuyos datos públicos se encuentran en el Portal de Servicios Climáticos de dicha institución. En la

Tabla 3 se muestra la información de la estación y en la Figura 8, se presenta la ubicación de la estación dentro del

dominio de modelación.

**Tabla 3.** Información de la estación Sagrada Familia.

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Página **15** de **33** Modelación de Dispersión e Impacto por Olores Viña Requingua -->

**Tabla 3: y 4** . Valores de velocidad de viento promedio diario y mensual, observados y modelados.**

| MES | Col2 | OBSERVADO<br>(m/s) | MODELADO<br>(m/s) |
| --- | --- | --- | --- |
| ~~1 ~~<br> | ~~Ene~~<br> | ~~0,51182796~~<br> | ~~0,61205645~~<br> |
| ~~2 ~~<br> | ~~Feb~~<br> | ~~0,28184524~~<br> | ~~0,31577381~~<br> |
| ~~3 ~~<br> | ~~Mar~~<br> | ~~0,18588710~~<br> | ~~0,21376344~~<br> |
| ~~4 ~~<br> | ~~Abr~~<br> | ~~0,06152778~~<br> | ~~0,17433333~~<br> |
| ~~5 ~~<br> | ~~May~~<br> | ~~0,12096774~~<br> | ~~0,14588710~~<br> |
| ~~6 ~~<br> | ~~Jun~~<br> | ~~0,20611111~~<br> | ~~0,41577778~~<br> |
| ~~7 ~~<br> | ~~Jul~~<br> | ~~0,32500000~~<br> | ~~0,43071237~~<br> |
| ~~8 ~~<br> | ~~Ago~~<br> | ~~0,29502019~~<br> | ~~0,37813172~~<br> |
| ~~9 ~~<br> | ~~Sep~~<br> | ~~0,29750000~~<br> | ~~0,49565278~~<br> |
| ~~10~~<br> | ~~Oct~~<br> | ~~0,02150538~~<br> | ~~0,19047043~~<br> |
| ~~11~~<br> | ~~Nov~~<br> | ~~0,00944444~~<br> | ~~0,02743056~~<br> |
| ~~12~~<br> | ~~Dic~~<br> | ~~0,02046444~~<br> | ~~0,16644011~~<br> |

<!-- Estadísticas: 12 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- |HORA|OBSERVADO<br>(m/s)|MODELADO<br>(m/s)| |---|---|---| |~~0 ~~<br>|~~0,113535912~~<br>|~~0,227356164~~<br>| |~~1 ~~<br>|~~0,114325069~~<br>|~~0,22839726~~<br>| -->
<!-- FIN TABLA 3 -->


|Estación|UTM Este (m)|UTM Norte (m)|Altitud (m)|
|---|---|---|---|
|Sagrada Familia|283.317|6.124.717|164|

**Figura 8.** Ubicación de la estación de monitoreo utilizada para la evaluación del modelo meteorológico.

Página **12** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

La variable a analizar corresponde a la Magnitud y Dirección del viento, puesto que esta combinación de variables

crucial en el transporte y difusión de contaminantes. Se extrajo desde el dominio de modelación, el punto de grilla

correspondiente a la posición de la estación, de manera de calcular la incertidumbre de los datos modelados versus

los datos observados.

|Figura 9. Rosa de vientos observad Verano|da en la estación Sagrada Familia. Otoño|
|---|---|
|~~Verano~~<br>|~~Otoño~~<br>|
|~~Invierno~~<br> <br>|~~Primavera~~<br> <br>|

Página **13** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

|Col1|Verano|
|---|---|
||NORTH<br>8%<br>16%<br>24%<br>32%<br>40%|
|WEST|SOUTH<br>EAST|

|Col1|Otoño|
|---|---|
||NORTH<br>10%<br>20%<br>30%<br>40%<br>50%|
|WEST|SOUTH<br>EAST|

|Col1|Invierno|
|---|---|
||NORTH<br>10%<br>20%<br>30%<br>40%<br>50%|
|WEST|SOUTH<br>EAST|

|Col1|NORTH<br>50%<br>40%<br>30%<br>20%<br>10%|
|---|---|
|WEST|SOUTH<br>EAST|

|Figura 10. Rosa de vientos modelada para el punto Verano|Col2|Col3|o de grilla ubicado en la estación Sagrada Familia. Otoño|Col5|Col6|
|---|---|---|---|---|---|
|~~Verano~~<br> <br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>8%<br>16%<br>24%<br>32%<br>40%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 2,08%|~~Verano~~<br> <br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>8%<br>16%<br>24%<br>32%<br>40%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 2,08%|~~Verano~~<br> <br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>8%<br>16%<br>24%<br>32%<br>40%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 2,08%|~~Otoño~~<br> <br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,44%|~~Otoño~~<br> <br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,44%|~~Otoño~~<br> <br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,44%|
|~~Invierno~~<br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,80%|~~Invierno~~<br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,80%|~~Invierno~~<br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,80%|~~Primavera~~<br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 1,79%|~~Primavera~~<br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 1,79%|~~Primavera~~<br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 1,79%|
|~~Invierno~~<br><br>NORTH<br>SOUTH<br>WEST<br>EAST<br>10%<br>20%<br>30%<br>40%<br>50%<br>WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,80%|WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,80%|WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,80%|WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 3,80%|WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 1,79%|WIND SPEED<br>(m/s)<br> >= 11,1<br> 8,8 - 11,1<br> 5,7 - 8,8<br> 3,6 - 5,7<br> 2,1 - 3,6<br> 0,5 - 2,1<br>Calms: 1,79%|
|||||||

Página **14** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 11.** Ciclo diario de la magnitud del viento observada y modelada en la estación Sagrada Familia.

**Figura 12.** Ciclo anual de la magnitud del viento observada y modelada en la estación Sagrada Familia.

Página **15** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Tabla 3 y 4** . Valores de velocidad de viento promedio diario y mensual, observados y modelados.

|MES|Col2|OBSERVADO<br>(m/s)|MODELADO<br>(m/s)|
|---|---|---|---|
|~~1 ~~<br>|~~Ene~~<br>|~~0,51182796~~<br>|~~0,61205645~~<br>|
|~~2 ~~<br>|~~Feb~~<br>|~~0,28184524~~<br>|~~0,31577381~~<br>|
|~~3 ~~<br>|~~Mar~~<br>|~~0,18588710~~<br>|~~0,21376344~~<br>|
|~~4 ~~<br>|~~Abr~~<br>|~~0,06152778~~<br>|~~0,17433333~~<br>|
|~~5 ~~<br>|~~May~~<br>|~~0,12096774~~<br>|~~0,14588710~~<br>|
|~~6 ~~<br>|~~Jun~~<br>|~~0,20611111~~<br>|~~0,41577778~~<br>|
|~~7 ~~<br>|~~Jul~~<br>|~~0,32500000~~<br>|~~0,43071237~~<br>|
|~~8 ~~<br>|~~Ago~~<br>|~~0,29502019~~<br>|~~0,37813172~~<br>|
|~~9 ~~<br>|~~Sep~~<br>|~~0,29750000~~<br>|~~0,49565278~~<br>|
|~~10~~<br>|~~Oct~~<br>|~~0,02150538~~<br>|~~0,19047043~~<br>|
|~~11~~<br>|~~Nov~~<br>|~~0,00944444~~<br>|~~0,02743056~~<br>|
|~~12~~<br>|~~Dic~~<br>|~~0,02046444~~<br>|~~0,16644011~~<br>|

|HORA|OBSERVADO<br>(m/s)|MODELADO<br>(m/s)|
|---|---|---|
|~~0 ~~<br>|~~0,113535912~~<br>|~~0,227356164~~<br>|
|~~1 ~~<br>|~~0,114325069~~<br>|~~0,22839726~~<br>|
|~~2 ~~<br>|~~0,104958678~~<br>|~~0,237917808~~<br>|
|~~3 ~~<br>|~~0,125344353~~<br>|~~0,249383562~~<br>|
|~~4 ~~<br>|~~0,104155125~~<br>|~~0,234853425~~<br>|
|~~5 ~~<br>|~~0,108864266~~<br>|~~0,221856164~~<br>|
|~~6 ~~<br>|~~0,108033241~~<br>|~~0,224335616~~<br>|
|~~7 ~~<br>|~~0,116253444~~<br>|~~0,231653425~~<br>|
|~~8 ~~<br>|~~0,124517906~~<br>|~~0,246068493~~<br>|
|~~9 ~~<br>|~~0,152341598~~<br>|~~0,269465753~~<br>|
|~~10~~<br>|~~0,173002755~~<br>|~~0,339410959~~<br>|
|~~11~~<br>|~~0,236363636~~<br>|~~0,420561644~~<br>|
|~~12~~<br>|~~0,28953168~~<br>|~~0,563109589~~<br>|
|~~13~~<br>|~~0,362534435~~<br>|~~0,69530137~~<br>|
|~~14~~<br>|~~0,41707989~~<br>|~~0,772232877~~<br>|
|~~15~~<br>|~~0,410743802~~<br>|~~0,793246575~~<br>|
|~~16~~<br>|~~0,372928177~~<br>|~~0,785382484~~<br>|
|~~17~~<br>|~~0,302754821~~<br>|~~0,650506849~~<br>|
|~~18~~<br>|~~0,219283747~~<br>|~~0,476808219~~<br>|
|~~19~~<br>|~~0,174655647~~<br>|~~0,378150685~~<br>|
|~~20~~<br>|~~0,171349862~~<br>|~~0,298232877~~<br>|
|~~21~~<br>|~~0,158953168~~<br>|~~0,252123288~~<br>|
|~~22~~<br>|~~0,120936639~~|~~0,223873626~~|

Página **16** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

Según se observa en la Figura 9 y Figura 10, se puede ver una correcta representación de la dirección predominante

del viento, no ocurre lo mismo con la magnitud, donde se puede apreciar una constante sobreestimación de las

magnitudes del viento.

En la Figura 11 y Figura 12, se observa una constante sobreestimación de las magnitudes del viento de parte del

modelo, constante durante todo el día y constante durante todo el año, sobre todo durante los meses fríos.

Cabe destacar, que la información obtenida desde la estación de monitoreo, corresponden a datos operacionales,

sin validación, aun así, la disponibilidad fu de un 97% de datos.

De todas formas, para propósitos de determinar la incertidumbre del modelo, se toma de base la siguiente

información:

 - Magnitud del viento promedio observado: 0,195 m/s

 - Magnitud del viento promedio modelado: 0,385 m/s

De los datos anteriores se desprende que el error porcentual de la velocidad del viento está determinado por la

fórmula:

((0,385 - 0,195) * 100 / 0,195) = 97%

Dado que la magnitud del viento modelada sobreestima los valores observados, su efecto consiste en una

disminución de las unidades de olor, este efecto debe ser considerado en la corrección por incertidumbre.

Corregido = (1 + 0,97) * Modelado

Corregido = 1,97 * Modelado

De esta forma los resultados modelados deberían ser multiplicados por 1,97 de manera de corregir el sesgo del

modelo. Para propósitos de la presente evaluación, se aplicará esta corrección por exceso, de manera de considerar

un peor escenario.

Página **17** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

# 4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE

Para la presente modelación se han seguido los procedimientos establecidos por la “Guía metodológica de

uso de modelos de dispersión en el SEIA”, la cual recomienda el uso de CALPUFF como modelo de

dispersión de contaminantes. Para propósitos particulares de este estudio, se ha utilizado la versión 6.4.

CALPUFF es un modelo lagrangiano de dispersión de contaminantes basado en un sistema de “puffs”, los

cuales varían en su forma y posición en función del tiempo, del espacio, la estabilidad atmosférica y los

vientos, entre otros parámetros. Es un modelo que soporta múltiples tipos de fuentes con diferentes tipos

de tratamiento para cada una de ellas: Fuentes de área, fuentes de volumen, fuentes puntuales y fuentes

de línea [5] .

**Tabla 4.** Configuración del dominio del modelo CALPUFF.

|Ítem|Valor|
|---|---|
|Centro UTM E (m)|285792|
|Centro UTM N (m)|6121415|
|Resolución espacial (m)|500|
|Puntos en X|30|
|Puntos en Y|30|
|Topografía|SRTM3 (Aproximadamente 90 metros de resolución)|
|Uso de suelo|GLCC (USGS30 aproximadamente a 1 Kilómetro e resolución)|

__________________________________________________
5 A User’s Guide for the CALPUFF Dispersion Model (Version 5), Earth Tech Inc.

Página **18** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

# 5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS

Para la modelación se consideraron ocho fuentes o procesos de emisión de olor de los cuales solamente tres se

encuentran construidas y operativas, mientras que las restantes están en proceso de construcción.

**Tabla 5** . Fuentes de olor consideradas para la modelación.

|Fuente de<br>Olor|Unidades|Tipo Fuente|Principales factores operacionales que<br>influyen en la generación de emisión de olor|Horas de<br>Emisión<br>por<br>Jornada<br>Laboral|
|---|---|---|---|---|
|Laguna de<br>Aireación|2|Superficial<br>Activa|~~Laguna de aireación para la digestión de~~<br>materia orgánica. Se encuentran en proceso<br>de construcción dos piscinas de 10000 m3 de<br>capacidad, y una superficie de 3481 m2 cada<br>una.<br>|24 (marzo<br>a <br>diciembre)|
|Secado de<br>Lodos|2|Difusa Pasiva|~~El proceso de secado de lodos se llevará a~~<br>cabo en las mismas lagunas de aireación que<br>se encuentran en construcción. Las lagunas<br>serán vaciadas y el lodo sedimentado será<br>secado mediante volteo y exposición solar<br>para su posterior retiro y disposición.<br>|24 (enero,<br>cada dos<br>años)|
|Lecho de<br>Grava|1|Superficial<br>Pasiva|~~Segunda etapa de tratamiento para la~~<br>disminución de la carga orgánica, consiste en<br>una piscina de 1000 m3 y superficie de 1000<br>m2.<br>Esta<br>unidad<br>se<br>encuentra<br>en<br>construcción.|24 (marzo<br>a <br>diciembre)|
|Cámara 1|1|Superficial<br>Pasiva|Cámara de recolección de riles ubicada en el patio<br>de producción. Tiene una superficie de 5,5 m2. <br>Actualmente en operación. <br>|24 horas|
|Filtro<br>Parabólico|1|Superficial<br>Pasiva|~~Cuenta de un filtro parabólico para el filtrado~~<br>de residuos gruesos más un estanque de riles,<br>en total tiene 30 m2. Actualmente en<br>operación.<br>|24 horas|
|Laguna<br>Existente|1|Superficial<br>Activa|~~Laguna de tratamiento de riles, que dentro de~~<br>sus dimensiones considera una zona de<br>aireación, una zona anaeróbica y una zona de<br>decantación. Tiene una capacidad de 3224 m3 <br>y una superficie de 2940 m2.|24 horas|

Página **19** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 13** . Ubicación de las fuentes de emisión.

Las fuentes fueron seleccionadas mediante una visita a terreno por parte de panelistas expertos en

monitoreo de olores. Estas fuentes representan los principales puntos de emisión de olor dentro del

proceso de tratamiento de riles.

Página **20** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Tabla 6.** Dimensiones y ubicación de fuentes.

|Zona o<br>Proceso<br>Tratamiento<br>Primario|Fuente de<br>Olor|Dimensiones|Área<br>(m2)|Coordenadas UTM|Col6|Actividad<br>asociada a<br>emisión de<br>olor|
|---|---|---|---|---|---|---|
|**Zona o**<br>**Proceso **<br>**Tratamiento**<br>**Primario **|<br>**Fuente de**<br>**Olor**<br>|**Dimensiones**|**Área**<br>**(m2) **|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Tratamiento<br>Secundario|Cámara 1|2,5x2,2m|5,5|285982|6121266|~~Acumulación~~<br>de riles<br>|
|Tratamiento<br>Secundario|Filtro<br>Parabólico<br>|6x5m|30|285934|6121160|~~Filtrado de~~<br>sólidos en<br>riles<br>|
|Tratamiento<br>de Lodos|~~Laguna de~~<br>Aireación<br>|59x59 m|3481|285696|6121477|~~Tratamiento~~<br>de riles<br>|
|Tratamiento<br>de Lodos|~~Laguna~~<br>Existente<br>|50x20m|1000|285792|6121415|~~Tratamiento~~<br>de riles<br>|
|Tratamiento<br>de Lodos|~~Lecho de~~<br>Grava<br>|60x49m|2940|286117|6120851|~~Tratamiento~~<br>de riles<br>|
|Zona o<br>Proceso <br>|~~Secado de~~<br>Lodos|45x45m|2025|285696|6121477|~~Secado de~~<br>lodos|

Página **21** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

Para la presente modelación se utilizaron datos de tasas de emisión de referencia según lo recomendado
en el punto 3.1.1. de la “Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA”. En particular,
las tasas de emisión para este proyecto están basadas en el Estudio de Olor presentado en la Declaración
de Impacto Ambiental “Ampliación y Normalización de instalaciones Agroindustriales RR Wine”,
presentado ante el Servicio de Evaluación Ambiental en 2018 y aprobado en 2019. Las mediciones se
realizaron en conformidad a la normativa correspondiente:

- La toma de muestra se realizó en función de la Guía Metodológica 3386:2015 [6 ]

- El análisis de las muestras se realizó según NCh 3190:2010 [7]

- La campaña de medición fue llevada a cabo durante el mes de febrero de 2019.

Las normas mencionadas anteriormente dan cuenta de la metodología y procedimientos
adecuados para la toma de muestra y la determinación de su concentración.

Los valores de emisión utilizados se muestran en la Tabla 6.

**Tabla 7** . Tasas de emisión por unidad.

|Zona o<br>Proceso|Número de<br>Unidades|Fuente|Tasa de Emisión Total<br>por Unidad (Uo/s)|Concentración (Uo/m3)|
|---|---|---|---|---|
|Tratamiento<br>Primario<br>|1|Cámara 1|2,855|343|
|Tratamiento<br>Primario<br>|1|Filtro Parabólico|2,855|343|
|Tratamiento<br>Secundario<br>|1|Laguna Existente|5,783|646|
|Tratamiento<br>Secundario<br>|2|Laguna de Aireación|5,783|646|
|Tratamiento<br>Secundario<br>|1|Lecho de Grava|0,202|-|
|Tratamiento<br>de Lodos|2|Secado de Lodos|1,641|197|

__________________________________________________

6 Instituto Nacional de Normalización (2015). Norma Chilena 3386:2015 “Muestreo estático para olfatometría”. Chile.

7 Instituto Nacional de Normalización (2010). Norma Chilena 3190:2010 “Calidad del aire - Determinación de la concentración
de olor por olfatometría dinámica”. Chile.

Página **22** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

Para el lecho de grava, se realizó una estimación de la tasa de emisión en base a la reducción de DBO al

llegar a esta unidad, en comparación con la unidad anterior (laguna de aireación). Para ello, se consideró

el valor de DBO entrante a la laguna de aireación y el porcentaje de remoción de la misma. Se asoció este

valor al 100% de la tasa de emisión, y de este modo se obtuvo el valor para el lecho de grava.

**Tabla 8** . Descripción de las fuentes.

|Zona o<br>Proceso|Fuente de<br>Olor|Calidad|Tipo de<br>Olor|Tono<br>Hedónico|Intensidad|Concentración<br>(Uo/m3)*|
|---|---|---|---|---|---|---|
|Tratamiento<br>Primario|Cámara 1|Uva, Alcohol|Compuesto|~~-2~~<br>Ligeramente<br>Desagradable <br>|2|343|
|Tratamiento<br>Primario|Filtro<br>Parabólico|Uva, Alcohol,<br>descomposición <br>|Compuesto|~~- 2~~<br>Ligeramente<br>Desagradable|3|343|
|Tratamiento<br>Secundario<br>|Laguna<br>Existente<br>|~~Descomposición,~~<br>Humedad y<br>tierra, Séptico|Compuesto|-3<br>Desagradable|4|646|
|Tratamiento<br>Secundario<br>|~~Laguna de~~<br>Aireación<br>|-|-|-|-|646|
|Tratamiento<br>Secundario<br>|~~Lecho de~~<br>Grava<br>|-|-|-|-|-|
|~~Tratamiento~~<br>de Lodos|~~Secado de~~<br>Lodos|-|-|-|-|197|

Las unidades sin información aún no se encuentran en operación. *Las concentraciones fueron obtenidas

del estudio de olor mencionado anteriormente.

Página **23** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

Respecto a los receptores definidos, se consideraron 14 receptores discretos alrededor de las

instalaciones, tal como lo muestra la Figura 137.

**Figura 14** . Detalle de los receptores definidos dentro del dominio de modelación.

Página **24** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

La ubicación en detalles de los receptores definidos se presenta en la Tabla 9.

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Modelación de Dispersión e Impacto por Olores Viña Requingua La ubicación en detalles de los receptores definidos se presenta en la Tabla 9. -->

**Tabla 9: ** . Ubicación de los receptores discretos definidos dentro del dominio de modelación.**

| Receptor | UTM E (m) | UTM N (m) | Altitud<br>(m) | Altura<br>(m) |
| --- | --- | --- | --- | --- |
| 1 | 286387 | 6120888 | 185,15 | 2 |
| 2 | 286282 | 6121223 | 184,11 | 2 |
| 3 | 286184 | 6121356 | 182,96 | 2 |
| 4 | 286102 | 6121515 | 181,99 | 2 |
| 5 | 286026 | 6121672 | 181,14 | 2 |
| 6 | 285946 | 6121832 | 182,27 | 2 |
| 7 | 285871 | 6121986 | 183,24 | 2 |
| 8 | 285640 | 6122290 | 177,65 | 2 |
| 9 | 284569 | 6122730 | 171,88 | 2 |
| 10 | 284426 | 6122372 | 172,98 | 2 |
| 11 | 284394 | 6122117 | 173,45 | 2 |
| 12 | 284370 | 6121788 | 173,59 | 2 |
| 13 | 287030 | 6119453 | 206,02 | 2 |
| 14 | 287308 | 6119300 | 202,06 | 2 |

<!-- Estadísticas: 14 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Para la determinación de los receptores, se tomó en cuenta la presencia de casas y viviendas cercanas al proyecto, ya que principalmente en estas se concentra la población susceptible de ser afectada por -->
<!-- FIN TABLA 9 -->


**Tabla 9** . Ubicación de los receptores discretos definidos dentro del dominio de modelación.

|Receptor|UTM E (m)|UTM N (m)|Altitud<br>(m)|Altura<br>(m)|
|---|---|---|---|---|
|1|286387|6120888|185,15|2|
|2|286282|6121223|184,11|2|
|3|286184|6121356|182,96|2|
|4|286102|6121515|181,99|2|
|5|286026|6121672|181,14|2|
|6|285946|6121832|182,27|2|
|7|285871|6121986|183,24|2|
|8|285640|6122290|177,65|2|
|9|284569|6122730|171,88|2|
|10|284426|6122372|172,98|2|
|11|284394|6122117|173,45|2|
|12|284370|6121788|173,59|2|
|13|287030|6119453|206,02|2|
|14|287308|6119300|202,06|2|

Para la determinación de los receptores, se tomó en cuenta la presencia de casas y viviendas cercanas al

proyecto, ya que principalmente en estas se concentra la población susceptible de ser afectada por

potenciales emisiones de malos olores.

Página **25** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

# 6. RESULTADOS DEL MODELO DE DISPERSIÓN Y ANÁLISIS DE IMPACTO POR

OLORES

**Figura 15.** Unidades de olor, P98 Escenario 1.

Página **26** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Figura 16** . Área de Influencia por emisión de olores del proyecto [9] .

____________________________________________________

9 Guía para la predicción y evaluación de impactos por olor en el SEIA, Servicio de Evaluación Ambiental (SEA), 2017.

Página **27** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

En la figura anterior, que muestra el área de influencia por emisión de olores del proyecto, se puede

apreciar claramente que todos los receptores se encuentran dentro de la misma. Corresponde realizar el

análisis de la concentración de olor en cada uno de ellos para poder estimar el impacto asociado.

En la Tabla 10 se presenta un detalle de los valores horarios diarios (Percentil 98) calculados para cada

receptor discreto definido, junto a los valores calculados para el Punto de Máximo Impacto (PMI).

**Tabla 10** . Valores de concentración de olor calculados para cada uno de los receptores discretos

definidos.

|Receptor|P98 (Uo/m3)|
|---|---|
|1|95|
|2|79|
|3|69|
|4|65|
|5|81|
|6|89|
|7|12|
|8|50|
|9|11|
|10|15|
|11|18|
|12|10|
|13|2|
|14|2|
|PMI (285.543 E, 6.121.665 N)|156|

Como se mencionó anteriormente, todos los receptores se encuentran dentro del área de influencia, con diferencias
considerables entre los valoes mínimos y máximos de concentración de olor (2 y 95 Uo/m [3] respectivamente).

Página **28** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

# 7. CONCLUSIONES

Los resultados permiten cuantificar las molestias causadas por las emisiones de olores. La escala de
percepciones y concentración de olores generalmente aceptada a nivel internacional se resumen en la
siguente tabla:

**Tabla 11.** Concentración y percepción.

|Concentracion|Percepcion|
|---|---|
|1 Uo/m3|50% de la población puede comenzar a percibir un olor|
|3 Uo/m3|50% de la población puede reconocer o comenzar a reconocer un olor<br>|
|5 Uo/m3|~~El olor es calificable y puede comenzar a recibirse quejas (puede ser~~<br>identificado)|
|10 Uo/m3|Los olores son reconocibles y se pueden recibir reclamos|

Es importante matizar el limite que se debe alcanzar para que exista una queja, ya que estas dependen
tambien de la intensidad de los olores percibidos, de su agresividad, de su apreciación (positiva o negativa)
y de su frecuencia. En consecuencia, la sensibilidad individual hacia los olores tiene una influencia
importante en la presentacion de quejas. Varias jurisdicciones alrededor del mundo han implementado
con éxito programas de gestión de olores, que proponen criterios de percepción de olor que oscilan entre
1 y 10 Uo/m [3] .

Como referencia, se cita la Guía Técnica Preliminar “Horizontal Guidance for Odour Part 1 - Regulation and
Permitting” [10] de la Integrated Pollution Prevention and Control (IPPC), mecanismo regulatorio
medioambiental de la Unión Europea. En este documento se proponen los siguientes criterios de inmisión
según el tipo de actividad.

____________________________________________________

10 Horizontal Guidance for Odour Part 1 - Regulation and Permitting. Scotish Environment Prevention Agency/Environment and
[Heritage Service/UK Environmet Agency. 2002. https://olores.mma.gob.cl/wp-content/uploads/2019/03/Integrated-Pollution-](https://olores.mma.gob.cl/wp-content/uploads/2019/03/Integrated-Pollution-Prevention-and-Control-part1.pdf)

[Prevention-and-Control-part1.pdf](https://olores.mma.gob.cl/wp-content/uploads/2019/03/Integrated-Pollution-Prevention-and-Control-part1.pdf)

Página **29** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Tabla 12.** Valores de inmisión según actividad, IPPC.

|Ofensividad<br>Relativa del<br>Olor|Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales)|Tipo de Actividad Relacionada|
|---|---|---|
|ALTA|1,5 Uo/m3|Actividades que involucren basura putrescible<br>Procesos que involucren a restos de animales y pescados<br>Cementeras y cerámicas<br>Procesos lácteos<br>Procesamiento de grasas y aceites<br>Tratamiento de aguas residuales<br>Refino de petróleo<br>Producción de comida para animales|
|MEDIA|3 Uo/m3|Procesos de comida para engorde<br>Procesos de la remolacha<br>Ganadería intensiva|
|BAJA<br>|6 Uo/m3|Fabricación de chocolate/cacao.<br>Cervecerías.<br>Confiterías.<br>Producción de aromas y fragancias.<br>Tostado de café.<br>Panaderías|

En este caso, para la actividad evaluada, se puede considerar un máximo de emisión permitido de 1,5
Uo/m [3] (Criterio de inmisión para tratamiento de aguas residuales). Por otra parte, el documento
“Antecedentes para la regulación de olores en Chile” [11], propone los siguientes valores límites de inmisión

según el tipo de actividad. Estos valores se presentan en la Tabla 11.

____________________________________________________
11 ANTECEDENTES DE LA REGULACIÓN DE OLORES EN CHILE. Ecotec Ingeniería Ltda. 2013. Disponible para consulta en

 - https://olores.mma.gob.cl/wp content/uploads/2019/03/ECOTEC Ingenieria.pdf

Página **30** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**Tabla 13** . Valores de inmisión propuestos para Chile, ECOTEC.

|Ofensividad<br>Relativa del<br>Olor|Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales)|Tipo de Actividad Relacionada|
|---|---|---|
|ALTA|3 Uo/m3|Fabricación de celulosa<br>Pesqueras y procesamiento de productos del mar<br>Sitios de Disposición final de residuos<br>Plantas faenadoras de animales y mataderos<br>Fabricación de alimentos para animales<br>Refinerías de petróleo<br>Curtiembres<br>Plantas recuperadoras de molibdeno|
|MEDIA|5 Uo/m3|Planteles y estancias de crianza de animales<br>Plantas de tratamiento de aguas servidas<br>Industria siderúrgica<br>Fabricación de inulina|
|BAJA<br>|7 Uo/m3|Fabricación de queso|

Esta propuesta para la realidad nacional presenta un matiz, al calificar el tratamiento de aguas residuales
como actividad de ofensividad media. En este caso, el máximo de emisión permitido es de 5 Uo/m [3] .

Considerando los resultados obtenidos para el presente proyecto, sería aceptable una emisión que no
supere las 5 unidades de olor por metro cubico (5 Uo/m [3] ). Sin embargo, para los receptores propuestos,

este valor es superado por 12 de 14 receptores propuestos.

Página **31** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

 - Según los resultados de la modelación, el mayor impacto por olores provenientes del proyecto se
registra dentro de las dependencias del proyecto, con un valor de 156 Uo/m [3], considerando el

Percentil 98 de los valores promedios horarios diarios.

 - El área de influencia del proyecto tiene una dimensión de 103 km [2], con una distancia de impacto

máxima de 9,5 kilómetros aproximadamente, en línea recta desde el punto representativo del

proyecto hacia el Noroeste.

 - Según los resultados entregados en la Tabla 11, los valores de inmisión en los posibles receptores

están por sobre lo recomendado por la legislación internacional.

 - Considerando que las personas son susceptibles de ser afectadas por la emisión de malos olores,

es importante considerar que la zona de emplazamiento del proyecto presenta una baja densidad

poblacional, lo que ayuda a disminuir el número de individuos que pudiesen ser afectados en las

proximidades del proyecto. Sin embargo, debido al largo alcance observado en los resultados, el

proyecto podría afectar parte de la zona urbana correspondiente a la ciudad de Sagrada Familia.

En conclusión, los resultados permiten afirmar que el presente proyecto generaría impactos de

consideración para el medio ambiente y las personas cercanas al mismo. Se recomienda adoptar las

medidas necesarias en el Plan de Gestión de Olores, que permitan mantener alcanzar valores dentro de

los límites propuestos por la legislación existente, logrando un equilibrio entre la actividad productiva y su

entorno inmediato.

Página **32** de **33**

Modelación de Dispersión e Impacto por Olores Viña Requingua

**www.essconsultores.cl**

**La Capitanía 80, Oficina 108, Las Condes**
**Santiago, Chile**

**+562 23034022**

**+569 82234583**

Página **33** de **33**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Coordenadas punto representativo del proyecto (Datum WGS 84).**

| Coordenadas UTM del Proyecto. | Col2 |
| --- | --- |
| Coordenada Este (m) | Coordenada Norte (m) |
| 286244 | 6121209 |

**Tabla 4.: ** Configuración del dominio del modelo CALPUFF.**

| Ítem | Valor |
| --- | --- |
| Centro UTM E (m) | 285792 |
| Centro UTM N (m) | 6121415 |
| Resolución espacial (m) | 500 |
| Puntos en X | 30 |
| Puntos en Y | 30 |
| Topografía | SRTM3 (Aproximadamente 90 metros de resolución) |
| Uso de suelo | GLCC (USGS30 aproximadamente a 1 Kilómetro e resolución) |

**Tabla 5: ** . Fuentes de olor consideradas para la modelación.**

| Fuente de<br>Olor | Unidades | Tipo Fuente | Principales factores operacionales que<br>influyen en la generación de emisión de olor | Horas de<br>Emisión<br>por<br>Jornada<br>Laboral |
| --- | --- | --- | --- | --- |
| Laguna de<br>Aireación | 2 | Superficial<br>Activa | ~~Laguna de aireación para la digestión de~~<br>materia orgánica. Se encuentran en proceso<br>de construcción dos piscinas de 10000 m3 de<br>capacidad, y una superficie de 3481 m2 cada<br>una.<br> | 24 (marzo<br>a <br>diciembre) |
| Secado de<br>Lodos | 2 | Difusa Pasiva | ~~El proceso de secado de lodos se llevará a~~<br>cabo en las mismas lagunas de aireación que<br>se encuentran en construcción. Las lagunas<br>serán vaciadas y el lodo sedimentado será<br>secado mediante volteo y exposición solar<br>para su posterior retiro y disposición.<br> | 24 (enero,<br>cada dos<br>años) |
| Lecho de<br>Grava | 1 | Superficial<br>Pasiva | ~~Segunda etapa de tratamiento para la~~<br>disminución de la carga orgánica, consiste en<br>una piscina de 1000 m3 y superficie de 1000<br>m2.<br>Esta<br>unidad<br>se<br>encuentra<br>en<br>construcción. | 24 (marzo<br>a <br>diciembre) |
| Cámara 1 | 1 | Superficial<br>Pasiva | Cámara de recolección de riles ubicada en el patio<br>de producción. Tiene una superficie de 5,5 m2. <br>Actualmente en operación. <br> | 24 horas |
| Filtro<br>Parabólico | 1 | Superficial<br>Pasiva | ~~Cuenta de un filtro parabólico para el filtrado~~<br>de residuos gruesos más un estanque de riles,<br>en total tiene 30 m2. Actualmente en<br>operación.<br> | 24 horas |
| Laguna<br>Existente | 1 | Superficial<br>Activa | ~~Laguna de tratamiento de riles, que dentro de~~<br>sus dimensiones considera una zona de<br>aireación, una zona anaeróbica y una zona de<br>decantación. Tiene una capacidad de 3224 m3 <br>y una superficie de 2940 m2. | 24 horas |

**Tabla 6.: ** Dimensiones y ubicación de fuentes.**

| Zona o<br>Proceso<br>Tratamiento<br>Primario | Fuente de<br>Olor | Dimensiones | Área<br>(m2) | Coordenadas UTM | Col6 | Actividad<br>asociada a<br>emisión de<br>olor |
| --- | --- | --- | --- | --- | --- | --- |
| **Zona o**<br>**Proceso **<br>**Tratamiento**<br>**Primario ** | <br>**Fuente de**<br>**Olor**<br> | **Dimensiones** | **Área**<br>**(m2) ** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| Tratamiento<br>Secundario | Cámara 1 | 2,5x2,2m | 5,5 | 285982 | 6121266 | ~~Acumulación~~<br>de riles<br> |
| Tratamiento<br>Secundario | Filtro<br>Parabólico<br> | 6x5m | 30 | 285934 | 6121160 | ~~Filtrado de~~<br>sólidos en<br>riles<br> |
| Tratamiento<br>de Lodos | ~~Laguna de~~<br>Aireación<br> | 59x59 m | 3481 | 285696 | 6121477 | ~~Tratamiento~~<br>de riles<br> |
| Tratamiento<br>de Lodos | ~~Laguna~~<br>Existente<br> | 50x20m | 1000 | 285792 | 6121415 | ~~Tratamiento~~<br>de riles<br> |
| Tratamiento<br>de Lodos | ~~Lecho de~~<br>Grava<br> | 60x49m | 2940 | 286117 | 6120851 | ~~Tratamiento~~<br>de riles<br> |
| Zona o<br>Proceso <br> | ~~Secado de~~<br>Lodos | 45x45m | 2025 | 285696 | 6121477 | ~~Secado de~~<br>lodos |

**Tabla 7: ** . Tasas de emisión por unidad.**

| Zona o<br>Proceso | Número de<br>Unidades | Fuente | Tasa de Emisión Total<br>por Unidad (Uo/s) | Concentración (Uo/m3) |
| --- | --- | --- | --- | --- |
| Tratamiento<br>Primario<br> | 1 | Cámara 1 | 2,855 | 343 |
| Tratamiento<br>Primario<br> | 1 | Filtro Parabólico | 2,855 | 343 |
| Tratamiento<br>Secundario<br> | 1 | Laguna Existente | 5,783 | 646 |
| Tratamiento<br>Secundario<br> | 2 | Laguna de Aireación | 5,783 | 646 |
| Tratamiento<br>Secundario<br> | 1 | Lecho de Grava | 0,202 | - |
| Tratamiento<br>de Lodos | 2 | Secado de Lodos | 1,641 | 197 |

**Tabla 8: ** . Descripción de las fuentes.**

| Zona o<br>Proceso | Fuente de<br>Olor | Calidad | Tipo de<br>Olor | Tono<br>Hedónico | Intensidad | Concentración<br>(Uo/m3)* |
| --- | --- | --- | --- | --- | --- | --- |
| Tratamiento<br>Primario | Cámara 1 | Uva, Alcohol | Compuesto | ~~-2~~<br>Ligeramente<br>Desagradable <br> | 2 | 343 |
| Tratamiento<br>Primario | Filtro<br>Parabólico | Uva, Alcohol,<br>descomposición <br> | Compuesto | ~~- 2~~<br>Ligeramente<br>Desagradable | 3 | 343 |
| Tratamiento<br>Secundario<br> | Laguna<br>Existente<br> | ~~Descomposición,~~<br>Humedad y<br>tierra, Séptico | Compuesto | -3<br>Desagradable | 4 | 646 |
| Tratamiento<br>Secundario<br> | ~~Laguna de~~<br>Aireación<br> | - | - | - | - | 646 |
| Tratamiento<br>Secundario<br> | ~~Lecho de~~<br>Grava<br> | - | - | - | - | - |
| ~~Tratamiento~~<br>de Lodos | ~~Secado de~~<br>Lodos | - | - | - | - | 197 |

**Tabla 10: ** . Valores de concentración de olor calculados para cada uno de los receptores discretos**

| Receptor | P98 (Uo/m3) |
| --- | --- |
| 1 | 95 |
| 2 | 79 |
| 3 | 69 |
| 4 | 65 |
| 5 | 81 |
| 6 | 89 |
| 7 | 12 |
| 8 | 50 |
| 9 | 11 |
| 10 | 15 |
| 11 | 18 |
| 12 | 10 |
| 13 | 2 |
| 14 | 2 |
| PMI (285.543 E, 6.121.665 N) | 156 |

**Tabla 11.: ** Concentración y percepción.**

| Concentracion | Percepcion |
| --- | --- |
| 1 Uo/m3 | 50% de la población puede comenzar a percibir un olor |
| 3 Uo/m3 | 50% de la población puede reconocer o comenzar a reconocer un olor<br> |
| 5 Uo/m3 | ~~El olor es calificable y puede comenzar a recibirse quejas (puede ser~~<br>identificado) |
| 10 Uo/m3 | Los olores son reconocibles y se pueden recibir reclamos |

**Tabla 12.: ** Valores de inmisión según actividad, IPPC.**

| Ofensividad<br>Relativa del<br>Olor | Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales) | Tipo de Actividad Relacionada |
| --- | --- | --- |
| ALTA | 1,5 Uo/m3 | Actividades que involucren basura putrescible<br>Procesos que involucren a restos de animales y pescados<br>Cementeras y cerámicas<br>Procesos lácteos<br>Procesamiento de grasas y aceites<br>Tratamiento de aguas residuales<br>Refino de petróleo<br>Producción de comida para animales |
| MEDIA | 3 Uo/m3 | Procesos de comida para engorde<br>Procesos de la remolacha<br>Ganadería intensiva |
| BAJA<br> | 6 Uo/m3 | Fabricación de chocolate/cacao.<br>Cervecerías.<br>Confiterías.<br>Producción de aromas y fragancias.<br>Tostado de café.<br>Panaderías |

**Tabla 13: ** . Valores de inmisión propuestos para Chile, ECOTEC.**

| Ofensividad<br>Relativa del<br>Olor | Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales) | Tipo de Actividad Relacionada |
| --- | --- | --- |
| ALTA | 3 Uo/m3 | Fabricación de celulosa<br>Pesqueras y procesamiento de productos del mar<br>Sitios de Disposición final de residuos<br>Plantas faenadoras de animales y mataderos<br>Fabricación de alimentos para animales<br>Refinerías de petróleo<br>Curtiembres<br>Plantas recuperadoras de molibdeno |
| MEDIA | 5 Uo/m3 | Planteles y estancias de crianza de animales<br>Plantas de tratamiento de aguas servidas<br>Industria siderúrgica<br>Fabricación de inulina |
| BAJA<br> | 7 Uo/m3 | Fabricación de queso |
