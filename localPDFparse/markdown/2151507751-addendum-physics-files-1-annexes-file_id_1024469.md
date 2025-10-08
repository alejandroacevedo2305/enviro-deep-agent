---
title: Sin título
author: Usuario
date: D:20210722101354-04'00'
language: es
type: report
pages: 17
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - RESUMEN
  - 1 INTRODUCCIÓN
  - 2 TOPOGRAFÍA
  - 3 ZONA DE ESTUDIO Y RED HÍDRICA
  - 4 ANÁLISIS HIDROLÓGICO
  - 5 CONCLUSIONES
  - 6 REFERENCIAS
-->

|PROYECTO|PFV NUESTRA SEÑORA DE LOS ÁNGELES|
|---|---|
|**MATERIA**|**CARACTERIZACIÓN HIDROLÓGICA**|
|**CLIENTE**|**3MW**|
|**CODIGO**|**033-2106.084**|

|Rev.|Fecha|Realizado|Revisado|Aprobado|Descripción|
|---|---|---|---|---|---|
|A|21-07-21|RCA|AGL|AGL|Para revisión interna|
|||||||
|||||||

|Rev.|Fecha|Revisión/aprobación cliente|Descripción|
|---|---|---|---|
|||||
|||||

Página ii

# RESUMEN

El objetivo del presente informe es definir las características hidrológicas y áreas de
inundación de la red hídrica asociada al proyecto “Planta Fotovoltaica Nuestra Señora de Los
Ángeles”, que se materializará en la comuna de Curicó, Región del Maule.

Para esto, se realizó un levantamiento topográfico y batimétrico con GPS geodésico, se hizo
un análisis hidrológico para los dos cauces identificados y se desarrolló un modelo
bidimensional para caracterizar las propiedades hidráulicas de los flujos.

En la zona de estudio se identificaron dos cauces naturales, correspondientes al río Lontué
por el sur poniente y el estero Guaiquillo por el nororiente. Los caudales máximos
instantáneos para un período de retorno de 100 años corresponden a 1994.44 m [3] /s para el río
Lontué y a 578.32 m [3] /s para el estero Guaiquillo.

Los resultados indican que las futuras obras del parque interactúan con la planicie de
inundación calculada, donde el área en común es de aproximadamente 6.4 ha, y se localiza
en el sector norponiente del área del proyecto. En general las profundidades calculadas son
menores a 30 centímetros; sin embargo, el sector más alejado hacia el poniente presenta
profundidades de entre 1.5 y 2.0m.

Página iii

**ÍNDICE**

RESUMEN .......................................................................................................................................... ii

1 INTRODUCCIÓN ...................................................................................................................... 4

2 TOPOGRAFÍA ........................................................................................................................... 5

3 ZONA DE ESTUDIO Y RED HÍDRICA ................................................................................... 6

4 ANÁLISIS HIDROLÓGICO ...................................................................................................... 8

4.1 Análisis de transposición de cuencas .................................................................................. 8

4.1.1 Análisis estadístico de datos disponibles ..................................................................... 8

4.1.2 Análisis de cuencas ..................................................................................................... 9

4.2 Modelación Hidráulica ...................................................................................................... 10

4.2.1 Caudales .................................................................................................................... 10

4.2.2 Modelo Digital de Terreno ........................................................................................ 11

4.2.3 Rugosidad del Lecho ................................................................................................. 11

4.2.4 Condición de Borde ................................................................................................... 13

4.3 Resultados y Área de Crecida o Inundación ..................................................................... 14

5 CONCLUSIONES .................................................................................................................... 16

6 REFERENCIAS ........................................................................................................................ 17



# 1 INTRODUCCIÓN

El presente informe se desarrolla en el contexto de la evaluación ambiental asociado al
proyecto “Parque Fotovoltaico Nuestra Señora de los Ángeles”. El proyecto se materializará
en la comuna de Curicó, provincia de Curicó, región del Maule.

El proyecto consiste en la construcción y operación de una planta de generación de
electricidad a partir de la energía solar, su ubicación se muestra en la Figura 1-1.

Figura 1-1. Ubicación del Proyecto.

El objetivo del presente informe consiste en determinar las principales características
hidrológicas y definir las áreas de inundación de la red hídrica del área donde se emplazará
el parque fotovoltaico proyectado.

Para lo anterior, se realizó un levantamiento de información en terreno, se hizo una revisión

de antecedentes, se realizaron labores de topografía y se definieron las principales
características hidrológicas del área. Con ello, para los cauces naturales se generó un modelo
hidráulico para definir el área de inundación que circula por el área del proyecto, para un
periodo de retorno de 100 años.



# 2 TOPOGRAFÍA

La campaña de levantamiento topográfico del área de interés fue realizada el día 13 de julio
de 2021 mediante GPS geodésico en modo RTK, utilizando un GPS fijo en tierra, y otro en
estado móvil para la captura de los datos de terreno en los cauces de interés (Figura 2 1).

Figura 2-1. Levantamiento Topográfico mediante GPS RTK.

Con el fin de complementar la información de terreno obtenida del levantamiento topográfico
con GPS geodésico, se realizó un levantamiento aerofotogramétrico con dron DJI Phantom
4 RTK. Este dron cuenta con una cámara fotográfica de 20 MP y un estabilizador Gimbal
con rango de vibración angular de + 0.02°. El levantamiento abarca toda el área de estudio,
y es ligado con algunos puntos de control en tierra, los que son identificados, individualizados
y georreferenciados durante el levantamiento topográfico mediante GPS. Con ello se generó,
a través de un proceso fotogramétrico, un ortomosaico georreferenciado, mediante el

software Pix4D.



# 3 ZONA DE ESTUDIO Y RED HÍDRICA

La zona de estudio se ubica referencialmente en las coordenadas UTM (m) N: 6.124.481 y

E: 292.419, datum WGS84, Huso 19, al occidente de la comuna de Curicó.

En particular, el proyecto se encuentra aguas arriba de la confluencia entre el río Lontué y el
estero Guaiquillo, que son afluentes del río Mataquito (Figura 3-1).

Figura 3-1. Área de estudio del proyecto y red hídrica.

La Dirección General de Aguas a través de la Resolución DGA N°135/20 y el Memo DGA
N°118/20, ha definido qué obras serán sometidas a permisos de modificación de cauce en
virtud de los artículos 41 y 171 del Código de Aguas, y, por lo tanto, sometidos al permiso
ambiental sectorial 156 o 157 de competencia de dicho servicio. De los citados documentos
se desprende que los cauces naturales que deberán someterse al permiso de modificación de
cauce deberán identificarse según la base de datos oficiales asociada a la cartografía IGM,
documentación técnica generada por la DGA, los planes maestros de aguas lluvias y los
demás antecedentes oficiales de gestión territorial, evaluados para un periodo de retorno de
100 años; mientras que los cauces artificiales que requerirán la respectiva autorización de
modificación de cauce y los PAS 156 y 157 serán todos aquellos que porteen un caudal
superior a 500 litros por segundo (0.5 m [3] /s) y que se encuentren emplazados en áreas rurales.



Adicionalmente, la red hídrica IGM muestra canales o cauces incipientes que cruzan la zona
del parque (Figura 3-1), pero en terreno no existe evidencia de ellos. En efecto, por el extremo
de aguas arriba del predio de parque, paralelo al camino, existe un pretil de aproximadamente
2m de altura (Figura 4-1), sin obras de drenaje, que impide cualquier tipo de flujo desde el
predio colindante hacia el predio del PFV.

Figura 3-2. Camino (en rojo) y pretil (en amarillo) por aguas arriba del predio del PFV.



# 4 ANÁLISIS HIDROLÓGICO

## 4.1 Análisis de transposición de cuencas

A continuación, se describe el desarrollo de la correspondiente caracterización y análisis
hidrológico de los cauces oficiales del IGM, con el fin de describir sus principales
características y los alcances de una crecida para un periodo de retorno de 100 años.

Figura 4-1. Red Hidrométrica sector de estudio.

### 4.1.1 Análisis estadístico de datos disponibles

Los caudales obtenidos a partir del registro diario de la estación DGA rio Mataquito en
Licantén se clasifican y filtran para extraer el caudal máximo anual registrado por la estación,
a estos caudales máximos anuales se les ajustan diferentes distribuciones de probabilidad de
tal manera de estimar cual predice mejor el comportamiento hidrológico del rio.

Tabla 4-1. Caudales máximos anuales estación DGA Rio Mataquito en Licantén (Ministerio
de Obras Públicas, 2020).

|Año|Caudal m3/s|Año|Caudal m3/s|Año|Caudal m3/s|
|---|---|---|---|---|---|
|~~1987~~<br>|~~4638.32~~<br>|~~1999~~<br>|~~1200.64~~<br>|~~2011~~<br>|~~417.76~~<br>|
|~~1988~~<br>|~~663.20~~<br>|~~2000~~<br>|~~4195.49~~<br>|~~2012~~<br>|~~1292.67~~<br>|
|~~1989~~<br>|~~1360.66~~<br>|~~2001~~<br>|~~3343.54~~<br>|~~2013~~<br>|~~647.79~~<br>|
|~~1990~~<br>|~~333.96~~<br>|~~2002~~<br>|~~3206.78~~<br>|~~2014~~<br>|~~1000.68~~<br>|
|~~1991~~<br>|~~1797.20~~<br>|~~2003~~<br>|~~1177.60~~<br>|~~2015~~<br>|~~1666.35~~<br>|
|~~1992~~<br>|~~1666.68~~<br>|~~2004~~<br>|~~1482.85~~<br>|~~2016~~<br>|~~1359.51~~<br>|
|~~1993~~<br>|~~1241.16~~<br>|~~2005~~<br>|~~2394.86~~<br>|~~2017~~<br>|~~1183.62~~<br>|
|~~1994~~<br>|~~1502.54~~<br>|~~2006~~<br>|~~3603.74~~<br>|~~2018~~<br>|~~1117.83~~<br>|
|~~1995~~<br>|~~1116.35~~<br>|~~2007~~<br>|~~387.96~~<br>|~~2019~~<br>|~~93.97~~<br>|
|~~1996~~<br>|~~788.47~~<br>|~~2008~~<br>|~~2193.68~~<br>|~~2020~~|~~1041.66~~|
|~~1997~~<br>|~~2526.17~~<br>|~~2009~~<br>|~~1623.73~~<br>|||
|~~1998~~|~~235.99~~|~~2010~~|~~438.48~~|~~438.48~~|~~438.48~~|



A los datos de la Tabla 4-1 se les ajustaron distintas distribuciones de probabilidad para
encontrar la que mejor describiera su comportamiento. En particular el ajuste estadístico se
muestra en la Tabla 4-2. Se considera la distribución Pearson 5 (3P) como la más adecuada

para realizar el análisis estadístico a los datos, con la que se genera una caudal de diseño,
para T=100 años, de 5929.1 m [3] /s.

Tabla 4-2. Caudales calculados y bondad de ajuste por distribución analizada.

|T(años)|P(x)|Q (m3/s)|
|---|---|---|
|~~2 ~~<br>|~~0.5~~<br>|~~1283~~<br>|
|~~5 ~~<br>|~~0.8~~<br>|~~2263.2~~<br>|
|~~10~~<br>|~~0.9~~<br>|~~3007.6~~<br>|
|~~25~~<br>|~~0.96~~<br>|~~4068.7~~<br>|
|~~50~~<br>|~~0.98~~<br>|~~4954.6~~<br>|
|~~100~~|~~0.99~~<br>|~~5929.1~~|

|Distribucion|Kolmogorov-Smirnov|Col3|
|---|---|---|
|Distribucion<br>|~~Estadistica~~<br>|~~Rango~~<br>|
|~~Pearson 5 (3P)~~<br>|~~0.10248~~<br>|~~1 ~~<br>|
|~~Pearson 6 (4P)~~<br>|~~0.10248~~<br>|~~2 ~~<br>|
|~~Lognormal (3P)~~<br>|~~0.1074~~<br>|~~3 ~~<br>|
|~~Gamma~~<br>|~~0.11022~~<br>|~~4 ~~<br>|
|~~Pearson 6~~<br>|~~0.11072~~<br>|~~5 ~~<br>|
|~~Gamma (3P)~~<br>|~~0.11572~~<br>|~~6 ~~<br>|
|~~Log-Pearson 3~~<br>|~~0.11783~~<br>|~~7 ~~<br>|
|~~Gumbel Max~~<br>|~~0.12608~~<br>|~~8 ~~<br>|
|~~Lognormal~~<br>|~~0.16113~~<br>|~~9 ~~<br>|
|~~Log-Gamma~~|~~0.17746~~|~~10~~|

### 4.1.2 Análisis de cuencas

Las áreas de las distintas cuencas analizadas se muestran en la Figura 4-2, en particular se
utiliza el método de transposición de cuencas para estimar el caudal del río Lontué y el Estero
Guaiquillo, que se pueden observar en la Tabla 4-3.

Figura 4-2. Áreas de las cuencas analizadas



Tabla 4-3. Caudales para el estero Guaiquillo y río Lontué en el sector de estudio.

|Periodo de retorno|Río Lontue (m3/s)|Estero Guaiquillo (m3/s)|
|---|---|---|
|~~2 ~~<br>|~~431.58~~<br>|~~125.14~~<br>|
|~~5 ~~<br>|~~761.30~~<br>|~~220.75~~<br>|
|~~10~~<br>|~~1011.70~~<br>|~~293.36~~<br>|
|~~25~~<br>|~~1368.63~~<br>|~~396.86~~<br>|
|~~50~~<br>|~~1666.63~~<br>|~~483.27~~<br>|
|~~100~~|~~1994.44~~|~~578.32~~|

## 4.2 Modelación Hidráulica

A partir de los caudales calculados en el Análisis Hidrológico, se efectúa un Análisis
Hidráulico 2d (Figura 4-3), a fin de conocer las cotas de crecida asociadas al periodo de

retorno de 100 años. El análisis consiste en la construcción de un modelo hidráulico mediante

el software HEC-RAS (Hydrologic Engineering Center - River Analysis System). Como
datos de entrada, el modelo HEC-RAS requiere de los siguientes antecedentes:

 - Caudales

 - Modelo Digital de Terreno

 - Coeficientes de rugosidad

 - Condiciones de borde

Figura 4-3. Modelo Hidráulico 2d.

### 4.2.1 Caudales

Para la verificación de la zona de inundación se utiliza el caudal obtenido por el método de
transposición de cuencas, que corresponde a 1994.44 m [3] /s para el río Lontué y 578.32 m [3] /s
para el estero Guaiquillo.



### 4.2.2 Modelo Digital de Terreno

Para la caracterización geométrica de las quebradas se generó un modelo digital de terreno a
partir de los datos extraídos del vuelo dron y puntos tomados con GPS geodésico (Figura
4-4).

Figura 4-4. Modelo Digital de Terreno

### 4.2.3 Rugosidad del Lecho

Para determinar el valor del coeficiente de rugosidad de Manning en el cauce se utiliza la
formulación de Cowan (ecuación 4-1) en conjunto con la Tabla 4-4.

### nn= mm∗(nn 0 + nn 1 + nn 2 + nn 3 + nn 4 ) 4-1

Donde

nn: Rugosidad del lecho
nn 0 : Rugosidad por material del lecho
nn 1 : Grado de irregularidad de perímetro de mojado
nn 2 : Variaciones de las secciones
nn 3 : Efecto relativo de las obstrucciones
### nn 4 : Densidad de la vegetación

mm: Sinuosidad y frecuencia de meandros



Tabla 4-4, Factores de rugosidad para distintos tipos de cauce (MC, Vol 3, 2020).

Durante la visita a terreno (Figura 4-5) se identificaron al menos 3 unidades características
que describen rugosidades en el lecho, estas quedan indicadas en la Tabla 4-5, Así su
distribución espacial sobre el dominio de modelación queda descrita en la Figura 4-6.

Figura 4-5. Fotografías del Cauce en el sector de estudio.



Tabla 4-5. Rugosidades de los distintos sectores identificados.

|Variable|Sin vegetación|Vegetación media|Vegetación alta|Comentario|
|---|---|---|---|---|
|Variable<br>|~~S1~~<br>|~~S2~~<br>|~~S3~~<br>|<br>|
|~~n0~~<br>|~~0.028~~<br>|~~0.028~~<br>|~~0.028~~<br>|<br>|
|~~n1~~<br>|~~0 ~~<br>|~~0 ~~<br>|~~0 ~~<br>|~~No aplica a modelo 2d~~<br>|
|~~n2~~<br>|~~0 ~~<br>|~~0 ~~<br>|~~0 ~~<br>|~~No aplica a modelo 2d~~<br>|
|~~n3~~<br>|~~0.01~~<br>|~~0.01~~<br>|~~0.01~~<br>|<br>|
|~~n4~~<br>|~~0.005~~<br>|~~0.015~~<br>|~~0.04~~<br>|<br>|
|~~m ~~<br>|~~1 ~~<br>|~~1 ~~<br>|~~1 ~~<br>|<br>|
|~~**n **~~|~~**0.043**~~|~~**0.053**~~|~~**0.078**~~|~~**Rugosidad a aplicar**~~|

El valor base (S1) se aplica sobre todo el dominio de modelación y se generan polígonos o
sectores donde aumenta la rugosidad (a S2 o S3), según se presenta en la Figura 4-6.

Figura 4-6. Distribución de rugosidad en el área de modelación.

### 4.2.4 Condición de Borde

En el modelo hidráulico del estero se ha definido por una condición de borde aguas abajo de
altura normal, asociada a la pendiente del cauce con un valor de 0.0044 m/m.



## 4.3 Resultados y Área de Crecida o Inundación

En la Figura 4-7 y Figura 4-8 se observa el cauce modelado y su planicie de inundación para
un TR de 100 años. La planicie calculada presenta una intromisión en el área definida para
la instalación de los Paneles fotovoltaicos, que se estimó en 6.4 ha (intersección entre planicie
de inundación y área PFV).

Figura 4-7. Área de Inundación TR 100 años.

En un análisis más detallado del área de inundación se puede apreciar que la profundidad es
mayoritariamente menor a 30 centímetros y solo el sector norponiente muestra inundaciones
mayores a esa profundidad (Figura 4-8). En particular, estas zonas más profundas
corresponden depresiones del terreno asociadas a paleo cauces del río Lontué,



Figura 4-8. Detalle área de inundación en polígono de proyecto.



# 5 CONCLUSIONES

En el área de estudio se identifican 2 cauces naturales principales, de norte a sur serian el
estero Guaiquillo y el río Lontué.

Del análisis hidráulico del cauce se desprende que el área en la que se proyectan las obras
tiene interacción con la planicie de inundación calculada para un periodo de retorno de 100

años.

Considerando lo anterior, la Dirección General de Aguas a través de la Resolución DGA
N°135/20 y el Memo DGA N°118/20, ha definido que los cauces naturales que deberán
someterse al permiso de modificación de cauce deberán identificarse según la base de datos
oficiales asociada a la cartografía IGM, documentación técnica generada por la DGA, los
planes maestros de aguas lluvias y los demás antecedentes oficiales de gestión territorial,
evaluados para un periodo de retorno de 100 años, por lo que, dado que las obras del proyecto

se encuentran en el área de inundación de uno de los cauces oficiales identificado se estima

generar los permisos sectoriales correspondientes.

Alex García L.

Ingeniero Civil, M.Sc.
Dr. en Ciencias Ambientales



# 6 REFERENCIAS

Ministerio de Obras Públicas. (1995). _Manual de calculo de crecidas y caudales minimos_
_en cuencas sin información fluviométrica._ Santiago, Chile.

Ministerio de Obras Públicas. (2020). _Manual de Carreteras_ (Vol. III). Santiago.

Ministerio de Obras Públicas. (2020). _Dirección General de Aguas_ . Recuperado el 2020, de
https://dga.mop.gob.cl/Paginas/hidrolineasatel.aspx

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1.: Caudales máximos anuales estación DGA Rio Mataquito en Licantén (Ministerio**

| Año | Caudal m3/s | Año | Caudal m3/s | Año | Caudal m3/s |
| --- | --- | --- | --- | --- | --- |
| ~~1987~~<br> | ~~4638.32~~<br> | ~~1999~~<br> | ~~1200.64~~<br> | ~~2011~~<br> | ~~417.76~~<br> |
| ~~1988~~<br> | ~~663.20~~<br> | ~~2000~~<br> | ~~4195.49~~<br> | ~~2012~~<br> | ~~1292.67~~<br> |
| ~~1989~~<br> | ~~1360.66~~<br> | ~~2001~~<br> | ~~3343.54~~<br> | ~~2013~~<br> | ~~647.79~~<br> |
| ~~1990~~<br> | ~~333.96~~<br> | ~~2002~~<br> | ~~3206.78~~<br> | ~~2014~~<br> | ~~1000.68~~<br> |
| ~~1991~~<br> | ~~1797.20~~<br> | ~~2003~~<br> | ~~1177.60~~<br> | ~~2015~~<br> | ~~1666.35~~<br> |
| ~~1992~~<br> | ~~1666.68~~<br> | ~~2004~~<br> | ~~1482.85~~<br> | ~~2016~~<br> | ~~1359.51~~<br> |
| ~~1993~~<br> | ~~1241.16~~<br> | ~~2005~~<br> | ~~2394.86~~<br> | ~~2017~~<br> | ~~1183.62~~<br> |
| ~~1994~~<br> | ~~1502.54~~<br> | ~~2006~~<br> | ~~3603.74~~<br> | ~~2018~~<br> | ~~1117.83~~<br> |
| ~~1995~~<br> | ~~1116.35~~<br> | ~~2007~~<br> | ~~387.96~~<br> | ~~2019~~<br> | ~~93.97~~<br> |
| ~~1996~~<br> | ~~788.47~~<br> | ~~2008~~<br> | ~~2193.68~~<br> | ~~2020~~ | ~~1041.66~~ |
| ~~1997~~<br> | ~~2526.17~~<br> | ~~2009~~<br> | ~~1623.73~~<br> |  |  |
| ~~1998~~ | ~~235.99~~ | ~~2010~~ | ~~438.48~~ | ~~438.48~~ | ~~438.48~~ |

**Tabla 4-2.: Caudales calculados y bondad de ajuste por distribución analizada.**

| T(años) | P(x) | Q (m3/s) |
| --- | --- | --- |
| ~~2 ~~<br> | ~~0.5~~<br> | ~~1283~~<br> |
| ~~5 ~~<br> | ~~0.8~~<br> | ~~2263.2~~<br> |
| ~~10~~<br> | ~~0.9~~<br> | ~~3007.6~~<br> |
| ~~25~~<br> | ~~0.96~~<br> | ~~4068.7~~<br> |
| ~~50~~<br> | ~~0.98~~<br> | ~~4954.6~~<br> |
| ~~100~~ | ~~0.99~~<br> | ~~5929.1~~ |

**Tabla 4-3.: Caudales para el estero Guaiquillo y río Lontué en el sector de estudio.**

| Periodo de retorno | Río Lontue (m3/s) | Estero Guaiquillo (m3/s) |
| --- | --- | --- |
| ~~2 ~~<br> | ~~431.58~~<br> | ~~125.14~~<br> |
| ~~5 ~~<br> | ~~761.30~~<br> | ~~220.75~~<br> |
| ~~10~~<br> | ~~1011.70~~<br> | ~~293.36~~<br> |
| ~~25~~<br> | ~~1368.63~~<br> | ~~396.86~~<br> |
| ~~50~~<br> | ~~1666.63~~<br> | ~~483.27~~<br> |
| ~~100~~ | ~~1994.44~~ | ~~578.32~~ |

**Tabla 4-5.: Rugosidades de los distintos sectores identificados.**

| Variable | Sin vegetación | Vegetación media | Vegetación alta | Comentario |
| --- | --- | --- | --- | --- |
| Variable<br> | ~~S1~~<br> | ~~S2~~<br> | ~~S3~~<br> | <br> |
| ~~n0~~<br> | ~~0.028~~<br> | ~~0.028~~<br> | ~~0.028~~<br> | <br> |
| ~~n1~~<br> | ~~0 ~~<br> | ~~0 ~~<br> | ~~0 ~~<br> | ~~No aplica a modelo 2d~~<br> |
| ~~n2~~<br> | ~~0 ~~<br> | ~~0 ~~<br> | ~~0 ~~<br> | ~~No aplica a modelo 2d~~<br> |
| ~~n3~~<br> | ~~0.01~~<br> | ~~0.01~~<br> | ~~0.01~~<br> | <br> |
| ~~n4~~<br> | ~~0.005~~<br> | ~~0.015~~<br> | ~~0.04~~<br> | <br> |
| ~~m ~~<br> | ~~1 ~~<br> | ~~1 ~~<br> | ~~1 ~~<br> | <br> |
| ~~**n **~~ | ~~**0.043**~~ | ~~**0.053**~~ | ~~**0.078**~~ | ~~**Rugosidad a aplicar**~~ |
